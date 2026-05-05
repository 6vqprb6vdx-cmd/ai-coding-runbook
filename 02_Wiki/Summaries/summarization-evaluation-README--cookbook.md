---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/capabilities/summarization/evaluation/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/capabilities/summarization/evaluation/README.md
title: "Claude Cookbooks — summarization/evaluation README (Promptfoo)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Promptfoo-driven evaluation setup for the summarization cookbook.

**Notes.** Running the full eval suite may require higher than normal rate limits — consider running a subset. Not every test passes out of the box; the suite is intentionally moderately challenging.

**Prerequisites.** Node.js + npm. Use `npx`. `promptfooconfig.yaml` is pre-initialized. Additional Python deps: `pip install nltk rouge-score` (needed by custom evals).

**Run.** `export ANTHROPIC_API_KEY=...`, `cd ./evaluation`, then `npx promptfoo@latest eval -c promptfooconfig.yaml --output ../data/results.csv`. View results with `npx promptfoo@latest view`.

**How it works.** `promptfooconfig.yaml` defines:

- **Prompts** — imported from `prompts.py`, designed to test various aspects of model performance.
- **Providers** — multiple Claude versions and parameter combos (e.g., temperature settings) for cross-model testing.
- **Tests** — defined in this file or imported from `tests.yaml`. Each test specifies inputs and expected outputs. Three custom evaluators plus one built-in (`contains`):
  - `bleu_eval.py` — BLEU score (machine vs. reference text similarity).
  - `rouge_eval.py` — ROUGE score (summary quality vs. reference summaries).
  - `llm_eval.py` — custom Claude-judge evaluators for coherence, relevance, factual accuracy.
- **Output** — format and location of results; Promptfoo supports many formats.

**Python binary.** Promptfoo runs `python` in the shell. If you see `python: command not found`, set `PROMPTFOO_PYTHON` to a path (e.g., `/path/to/python3.11`) or executable name (`python3.11`).
