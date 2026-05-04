#!/usr/bin/env python3
"""Find raw files in 01_Raw/ that don't yet have a corresponding summary in 02_Wiki/Summaries/.

Run at session start (CLAUDE.md hooks this) so the LLM sees:
    📋 待 ingest: N 个文件
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "01_Raw"
SUMMARIES = ROOT / "02_Wiki" / "Summaries"


def list_raw_files() -> list[Path]:
    """List every .md file under 01_Raw/, following symlinks (defensive)."""
    files: list[Path] = []
    for p in RAW.rglob("*.md"):
        # skip _meta and hidden
        rel = p.relative_to(RAW)
        if any(part.startswith("_") or part.startswith(".") for part in rel.parts):
            continue
        files.append(p)
    return files


def list_summaries() -> set[str]:
    """A summary should encode the original raw path. We'll match by stem for now."""
    if not SUMMARIES.exists():
        return set()
    return {p.stem for p in SUMMARIES.rglob("*.md") if not p.name.startswith("_")}


def main() -> int:
    raw_files = list_raw_files()
    summary_stems = list_summaries()
    pending = [p for p in raw_files if p.stem not in summary_stems]

    if not pending:
        print(f"✓ No pending raw files. ({len(raw_files)} raw, {len(summary_stems)} summaries)")
        return 0

    print(f"📋 待 ingest: {len(pending)} 个文件 (共 {len(raw_files)} raw)")
    print()
    # Group by top-level source
    by_source: dict[str, list[Path]] = {}
    for p in pending:
        rel = p.relative_to(RAW)
        source = rel.parts[0] if rel.parts else "(root)"
        by_source.setdefault(source, []).append(p)
    for source, files in sorted(by_source.items()):
        print(f"  {source}: {len(files)} files")
        for p in files[:5]:
            print(f"    - {p.relative_to(RAW)}")
        if len(files) > 5:
            print(f"    ... ({len(files) - 5} more)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
