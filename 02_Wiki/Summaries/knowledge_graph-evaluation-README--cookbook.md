---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/capabilities/knowledge_graph/evaluation/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/capabilities/knowledge_graph/evaluation/README.md
title: "Claude Cookbooks — knowledge_graph/evaluation README"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Evaluation script that scores entity and relation extraction against the hand-labeled gold set in `../data/sample_triples.json`.

**Running.** From repo root: `uv sync --all-extras`, copy `.env.example` to `.env` and add `ANTHROPIC_API_KEY`. Then `uv run python capabilities/knowledge_graph/evaluation/eval_extraction.py`.

**Metrics.**

- **Entity P/R/F1** — an extracted entity counts as a true positive if its canonicalized name matches a gold entity in the same document. Canonicalization lowercases and maps known surface-form variants ("National Aeronautics and Space Administration" → "nasa") via `data/alias_map.json`.
- **Relation P/R/F1** — a relation counts as a true positive if both canonicalized endpoints match a gold (source, target) pair. **Predicate wording is ignored**: "commanded" and "was commander of" both count, but so would a semantically wrong predicate like "destroyed" between the same two entities. This makes reported relation recall an upper bound — measures whether the extractor found the right *connections*, not whether it labeled them correctly. For stricter scoring, add a predicate-similarity check (e.g. a Claude judge call per candidate pair).

**Expected baseline** (with `claude-haiku-4-5` and the guide's extraction prompt; ranges are indicative, vary run-to-run due to model non-determinism):

| Metric | P | R | F1 |
|---|---|---|---|
| Entities | 0.80–0.90 | 0.70–0.85 | 0.75–0.85 |
| Relations | 0.70–0.85 | 0.55–0.70 | 0.60–0.75 |

Recall on relations is the hard number — the extractor tends conservative (fewer high-confidence edges). Tuning the extraction prompt for higher recall (e.g. "extract every stated relationship, even minor ones") trades precision for recall.
