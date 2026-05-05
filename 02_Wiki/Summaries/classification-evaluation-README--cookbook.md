---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/capabilities/classification/evaluation/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/capabilities/classification/evaluation/README.md
title: "Claude Cookbooks — classification/evaluation README (Promptfoo)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Promptfoo-driven evaluation setup for the classification cookbook.

**Prerequisites.** Node.js + npm. Use `npx` (no `npx promptfoo@latest init` needed — `promptfooconfig.yaml` already initialized).

**Configuration sections in `promptfooconfig.yaml`:**

- **Prompts.** Three prompts loaded from `prompts.py`. Functions are identical to the ones in `guide.ipynb` except they return the prompt instead of calling the Claude API; Promptfoo handles the API orchestration and result storage. Python format allows reuse of the `VectorDB` class needed for RAG (in `vectordb.py`).
- **Providers.** `guide.ipynb` used Haiku at temperature 0.0; the eval uses Promptfoo to sweep an array of temperatures to find the optimum.
- **Tests.** Same data as `guide.ipynb` (`dataset.csv`). Per-row test conditions live in CSV; cross-test conditions live in `promptfooconfig.yaml`.
- **Transform.** `defaultTest` defines a Python transform that extracts the specific output to be tested from the LLM response.
- **Output.** Promptfoo supports many output formats; the file path is configured here. Web UI also available.

**Run.** `cd ./evaluation`, `export ANTHROPIC_API_KEY=...`, `export VOYAGE_API_KEY=...`, then `npx promptfoo@latest eval`. Default concurrency is 4; override with `-j 25`. Results print per row when complete; analyze in `guide.ipynb`.
