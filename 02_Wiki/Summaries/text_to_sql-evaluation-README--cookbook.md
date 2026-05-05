---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/capabilities/text_to_sql/evaluation/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/capabilities/text_to_sql/evaluation/README.md
title: "Claude Cookbooks — text_to_sql/evaluation README (Promptfoo)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Promptfoo-driven evaluation setup for the Text-to-SQL cookbook.

**Notes.** Full eval suite may require higher-than-normal rate limits — consider a subset. Not every test passes out of the box; the suite is intentionally moderately challenging.

**Prerequisites.** Node.js + npm. Use `npx`. `promptfooconfig.yaml` is pre-initialized.

**Run.** `export ANTHROPIC_API_KEY=...`, `cd ./evaluation`, then `npx promptfoo@latest eval -c promptfooconfig.yaml --output ../data/results.csv`. View results via `npx promptfoo@latest view`.

**How it works.** `promptfooconfig.yaml` defines:

- **Prompts** — imported from `prompts.py`, designed to test various aspects of LM performance.
- **Providers** — selects which Claude model(s) to use.
- **Tests** — input/expected-output pairs; Promptfoo offers built-in test types or you can define your own.
- **Output** — format and location of results.

**Python binary.** Promptfoo runs `python` in the shell. Set `PROMPTFOO_PYTHON` to override (path or executable name in PATH).
