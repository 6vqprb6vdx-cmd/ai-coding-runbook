---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/managed_agents/example_data/orchestrate/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/example_data/orchestrate/README.md
title: "Claude Cookbooks — managed_agents/example_data/orchestrate README"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent]
concepts_referenced: []
---

Self-contained mock of a maintainer workflow used by `CMA_orchestrate_issue_to_pr.py`. The cookbook zips this directory and hands it to the agent so the entire issue → PR → merge flow runs without touching real GitHub.

**Contents.**

- `gh-mock` — bash script faking the relevant `gh` subcommands. State persists in `.gh-state/`.
- `issue_42.json` — Unicode bug report (`Café Culture` → `caf-culture`). Vague enough that the agent has to read code.
- `src/url_utils.py` + `src/blog.py` + `tests/test_urls.py` — buggy `slugify()` and the failing tests that catch it.

**Recovery points.** Two are deliberately planted: an incomplete first fix fails CI with a pytest traceback, and the mock reviewer-bot blocks the merge if `slugify()` is missing a docstring. A healthy run ends with `.gh-state/pr_101.json` showing `state: merged`, `ci/test: pass`, and an `APPROVED` review.
