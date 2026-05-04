#!/usr/bin/env python3
"""
Refresh 01_Raw/ from all sources defined in scripts/sources.yaml.

Usage:
    python3 scripts/refresh_raw.py                # refresh everything
    python3 scripts/refresh_raw.py --only docs    # only docs_sites
    python3 scripts/refresh_raw.py --only github  # only github_repos
    python3 scripts/refresh_raw.py --only blog    # only rss_or_index
    python3 scripts/refresh_raw.py --dry-run      # list what would be fetched

Exit codes:
    0 = success (may include skipped sources)
    1 = at least one source completely failed (sitemap fetch error, repo clone error, etc.)
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, urljoin
from xml.etree import ElementTree as ET

import requests
import yaml
from bs4 import BeautifulSoup
from markdownify import markdownify

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "01_Raw"
META = RAW / "_meta"
SOURCES_FILE = ROOT / "scripts" / "sources.yaml"

# Use a browser UA. Anthropic doc CDN (Cloudflare) returns empty body to plain bot UAs.
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)
HEADERS = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8"}
HTTP_TIMEOUT = 30
SLEEP_BETWEEN_REQUESTS = 0.4  # be nice


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def load_sources() -> dict:
    with open(SOURCES_FILE) as f:
        return yaml.safe_load(f)


def url_to_path(url: str, target_dir: str) -> Path:
    """Map a URL to a relative file path under 01_Raw/<target_dir>/.
    Strips host + leading slash, drops query string, ensures .md suffix."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    # docs.claude.com URLs like /en/docs/claude-code/overview → en/docs/claude-code/overview.md
    if not path.endswith(".md"):
        # Treat trailing slash or no extension as a page
        if path.endswith("/") or "." not in path.rsplit("/", 1)[-1]:
            path = path.rstrip("/") + ".md"
    return RAW / target_dir / path


def fetch_url(url: str) -> requests.Response | None:
    try:
        r = requests.get(url, headers=HEADERS, timeout=HTTP_TIMEOUT, allow_redirects=True)
    except requests.RequestException as e:
        log(f"  ✗ {url} → {e}")
        return None
    if r.status_code != 200:
        log(f"  ✗ {url} → HTTP {r.status_code}")
        return None
    return r


def html_to_markdown(html: str, source_url: str) -> str:
    """Extract main content from HTML and convert to markdown.
    Strips nav/footer/sidebar via common selectors before conversion."""
    soup = BeautifulSoup(html, "html.parser")
    # Remove nav, footer, header, scripts, styles
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()
    # Try common main-content containers
    main = (
        soup.select_one("main")
        or soup.select_one("article")
        or soup.select_one("[role=main]")
        or soup.select_one(".content, .docs-content, #content, #main-content")
        or soup.body
    )
    if main is None:
        return ""
    md = markdownify(str(main), heading_style="ATX", bullets="-")
    # Collapse repeated blank lines
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    header = f"---\nsource_url: {source_url}\nfetched_at: {datetime.now(timezone.utc).isoformat()}\n"
    if title:
        header += f"title: {json.dumps(title)}\n"
    header += "---\n\n"
    return header + md + "\n"


def fetch_doc_page(url: str) -> str | None:
    """Try Mintlify-style .md endpoint first, then fall back to HTML extraction."""
    # Strategy 1: try url + .md (Mintlify convention)
    md_url = url.rstrip("/") + ".md"
    r = fetch_url(md_url)
    if r is not None and r.headers.get("content-type", "").startswith(("text/markdown", "text/plain")):
        body = r.text
        header = (
            f"---\nsource_url: {url}\n"
            f"fetched_at: {datetime.now(timezone.utc).isoformat()}\n"
            f"fetch_method: mintlify_md\n---\n\n"
        )
        return header + body + ("\n" if not body.endswith("\n") else "")
    # Strategy 2: fetch HTML and extract
    r = fetch_url(url)
    if r is None:
        return None
    return html_to_markdown(r.text, url)


def write_if_changed(path: Path, content: str) -> bool:
    """Write file only if content differs. Returns True if written."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        old = path.read_text(encoding="utf-8")
        # Compare ignoring the fetched_at line so timestamp churn doesn't generate noise
        old_norm = re.sub(r"^fetched_at:.*$", "", old, count=1, flags=re.MULTILINE)
        new_norm = re.sub(r"^fetched_at:.*$", "", content, count=1, flags=re.MULTILINE)
        if old_norm == new_norm:
            return False
    path.write_text(content, encoding="utf-8")
    return True


def crawl_docs_site(site: dict, dry_run: bool) -> tuple[int, int, int]:
    """Crawl one docs_site. Returns (fetched, written, errors)."""
    name = site["name"]
    sitemap_url = site["sitemap"]
    target_dir = site["target_dir"]
    prefixes = site.get("include_prefixes", [])

    log(f"docs_site: {name} — fetching sitemap {sitemap_url}")
    r = fetch_url(sitemap_url)
    if r is None:
        log(f"  ✗ sitemap fetch failed; skipping {name}")
        return 0, 0, 1

    try:
        # Strip XML namespace for simpler XPath
        xml_str = re.sub(r'xmlns="[^"]+"', "", r.text, count=1)
        root = ET.fromstring(xml_str)
    except ET.ParseError as e:
        log(f"  ✗ sitemap parse failed: {e}")
        return 0, 0, 1

    urls: list[str] = []
    # Sitemap may be a sitemapindex (nested) or urlset
    for loc in root.iter("loc"):
        u = (loc.text or "").strip()
        if not u:
            continue
        # If it's a sub-sitemap, recurse one level
        if u.endswith(".xml"):
            sub = fetch_url(u)
            if sub is None:
                continue
            try:
                sub_xml = re.sub(r'xmlns="[^"]+"', "", sub.text, count=1)
                sub_root = ET.fromstring(sub_xml)
                for sub_loc in sub_root.iter("loc"):
                    sub_u = (sub_loc.text or "").strip()
                    if sub_u:
                        urls.append(sub_u)
            except ET.ParseError:
                continue
        else:
            urls.append(u)

    # Filter by prefix
    if prefixes:
        urls = [u for u in urls if any(urlparse(u).path.startswith(p) for p in prefixes)]

    log(f"  → {len(urls)} URLs match prefixes")
    if dry_run:
        for u in urls[:10]:
            print(f"    {u}")
        if len(urls) > 10:
            print(f"    ... ({len(urls) - 10} more)")
        return len(urls), 0, 0

    fetched, written, errors = 0, 0, 0
    for i, url in enumerate(urls, 1):
        if i % 25 == 0:
            log(f"  progress: {i}/{len(urls)}")
        content = fetch_doc_page(url)
        time.sleep(SLEEP_BETWEEN_REQUESTS)
        if content is None:
            errors += 1
            continue
        fetched += 1
        path = url_to_path(url, target_dir)
        if write_if_changed(path, content):
            written += 1

    log(f"  ✓ {name}: {fetched} fetched, {written} written/changed, {errors} errors")
    return fetched, written, errors


def crawl_blog_index(site: dict, dry_run: bool) -> tuple[int, int, int]:
    """Crawl an index page and extract post URLs matching pattern."""
    name = site["name"]
    index_url = site["index_url"]
    target_dir = site["target_dir"]
    pattern = re.compile(site["post_url_pattern"])

    log(f"index: {name} — {index_url}")
    r = fetch_url(index_url)
    if r is None:
        log(f"  ✗ index fetch failed; skipping {name}")
        return 0, 0, 1

    soup = BeautifulSoup(r.text, "html.parser")
    candidates: set[str] = set()
    for a in soup.find_all("a", href=True):
        href = urljoin(index_url, a["href"])
        if pattern.match(href):
            candidates.add(href)

    urls = sorted(candidates)
    log(f"  → {len(urls)} post URLs match pattern")
    if dry_run:
        for u in urls[:10]:
            print(f"    {u}")
        if len(urls) > 10:
            print(f"    ... ({len(urls) - 10} more)")
        return len(urls), 0, 0

    fetched, written, errors = 0, 0, 0
    for i, url in enumerate(urls, 1):
        if i % 25 == 0:
            log(f"  progress: {i}/{len(urls)}")
        rr = fetch_url(url)
        time.sleep(SLEEP_BETWEEN_REQUESTS)
        if rr is None:
            errors += 1
            continue
        content = html_to_markdown(rr.text, url)
        fetched += 1
        path = url_to_path(url, target_dir)
        if write_if_changed(path, content):
            written += 1

    log(f"  ✓ {name}: {fetched} fetched, {written} written/changed, {errors} errors")
    return fetched, written, errors


def sync_github_repo(spec: dict, dry_run: bool) -> tuple[int, int, int]:
    """git clone --depth 1 if missing, else git pull. Returns (fetched=1, written=0_or_1, errors).

    A 404 on the repo URL counts as 'skipped' (returned errors=0) so that one renamed/deleted
    repo doesn't fail the whole workflow. Real errors (network / git internal) still count."""
    owner = spec["owner"]
    repo = spec["repo"]
    target = RAW / "github" / owner / repo
    url = f"https://github.com/{owner}/{repo}.git"
    web_url = f"https://github.com/{owner}/{repo}"

    if dry_run:
        log(f"github: {owner}/{repo} → would clone/pull at {target.relative_to(ROOT)}")
        return 1, 0, 0

    if not target.exists():
        # Probe with HEAD before clone — git auth prompt is the slowest failure mode.
        try:
            probe = requests.head(web_url, headers={"User-Agent": UA}, timeout=10, allow_redirects=False)
            if probe.status_code == 404:
                log(f"github: ⚠ {owner}/{repo} returns 404 (renamed or removed) — skipping")
                return 0, 0, 0
            # 301/302 = renamed; warn but still attempt (clone will follow)
            if probe.status_code in (301, 302):
                new_loc = probe.headers.get("location", "(unknown)")
                log(f"github: ⚠ {owner}/{repo} redirects to {new_loc} — update sources.yaml")
        except requests.RequestException as e:
            log(f"github: probe failed for {owner}/{repo}: {e} (continuing to clone)")

        log(f"github: cloning {owner}/{repo} (shallow)")
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", url, str(target)],
                check=True, capture_output=True, text=True,
                env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},  # never prompt for auth
            )
            return 1, 1, 0
        except subprocess.CalledProcessError as e:
            log(f"  ✗ clone failed: {e.stderr.strip()}")
            return 0, 0, 1
    else:
        # pull (shallow clones can pull, with --depth=1 to keep shallow)
        try:
            before = subprocess.run(
                ["git", "-C", str(target), "rev-parse", "HEAD"],
                check=True, capture_output=True, text=True,
            ).stdout.strip()
            subprocess.run(
                ["git", "-C", str(target), "fetch", "--depth", "1", "origin"],
                check=True, capture_output=True, text=True,
            )
            subprocess.run(
                ["git", "-C", str(target), "reset", "--hard", "origin/HEAD"],
                check=True, capture_output=True, text=True,
            )
            after = subprocess.run(
                ["git", "-C", str(target), "rev-parse", "HEAD"],
                check=True, capture_output=True, text=True,
            ).stdout.strip()
            changed = (before != after)
            if changed:
                log(f"github: {owner}/{repo} updated {before[:7]} → {after[:7]}")
            return 1, (1 if changed else 0), 0
        except subprocess.CalledProcessError as e:
            log(f"  ✗ pull failed for {owner}/{repo}: {e.stderr.strip()}")
            return 0, 0, 1


def write_meta(stats: dict) -> None:
    META.mkdir(parents=True, exist_ok=True)
    meta_file = META / "last_crawl.json"
    payload = {
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "stats": stats,
    }
    meta_file.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=["docs", "github", "blog"], help="Restrict to one source kind")
    ap.add_argument("--dry-run", action="store_true", help="Show what would be fetched, don't write")
    args = ap.parse_args()

    sources = load_sources()
    stats = {"docs_sites": [], "rss_or_index": [], "github_repos": []}
    total_errors = 0

    if args.only in (None, "docs"):
        for site in sources.get("docs_sites", []):
            f, w, e = crawl_docs_site(site, args.dry_run)
            stats["docs_sites"].append({"name": site["name"], "fetched": f, "written": w, "errors": e})
            total_errors += e

    if args.only in (None, "blog"):
        for site in sources.get("rss_or_index", []):
            f, w, e = crawl_blog_index(site, args.dry_run)
            stats["rss_or_index"].append({"name": site["name"], "fetched": f, "written": w, "errors": e})
            total_errors += e

    if args.only in (None, "github"):
        for spec in sources.get("github_repos", []):
            f, w, e = sync_github_repo(spec, args.dry_run)
            stats["github_repos"].append(
                {"repo": f"{spec['owner']}/{spec['repo']}", "fetched": f, "written": w, "errors": e}
            )
            total_errors += e

    if not args.dry_run:
        write_meta(stats)

    log(f"DONE. Errors: {total_errors}")
    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
