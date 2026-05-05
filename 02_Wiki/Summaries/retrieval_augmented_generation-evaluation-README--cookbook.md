---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/capabilities/retrieval_augmented_generation/evaluation/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/capabilities/retrieval_augmented_generation/evaluation/README.md
title: "Claude Cookbooks — RAG/evaluation README (Promptfoo)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Promptfoo-driven evaluation setup for the RAG cookbook. Splits evaluation logic between `promptfooconfig_retrieval.yaml` (for the retrieval system in isolation) and `promptfooconfig_end_to_end.yaml` (for full end-to-end performance).

**Prerequisites.** Node.js + npm. Use `npx`. The `promptfooconfig.yaml` files are pre-initialized.

**Retrieval evaluations.** Prompts pass through `{{query}}` to each retrieval provider (no LLM prompt needed). Providers are custom — each retrieval method from `guide.ipynb` is wired as a custom Promptfoo provider. Tests use the same data as the guide, split into `end_to_end_dataset.csv` and `retrieval_dataset.csv` with an `__expected` column for automatic per-row assertions. Logic in `eval_retrieval.py`.

**End-to-end evaluations.** Three prompts (one per method used in the guide), imported from a `prompts.py`-style module that returns the prompt instead of calling the API. Promptfoo handles API orchestration. The `VectorDB` class is reused from the guide via `vectordb.py`. Providers can be swapped to test multiple Claude models. Tests use the same datasets with `__expected` columns. Logic in `eval_end_to_end.py`. Output paths are configurable; results can also be viewed via Promptfoo's web UI.

**Run.** `cd ./evaluation`, set `ANTHROPIC_API_KEY` and `VOYAGE_API_KEY`, then either:

- End-to-end: `npx promptfoo@latest eval -c promptfooconfig_end_to_end.yaml --output ../data/end_to_end_results.json`
- Retrieval only: `npx promptfoo@latest eval -c promptfooconfig_retrieval.yaml --output ../data/retrieval_results.json`

Run `npx promptfoo@latest view` to open the UI viewer.
