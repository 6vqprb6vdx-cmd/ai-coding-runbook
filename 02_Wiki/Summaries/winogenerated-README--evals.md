---
type: summary
source: 01_Raw/github/anthropics/evals/winogenerated/README.md
source_url: https://github.com/anthropics/evals/blob/main/winogenerated/README.md
title: "Anthropic Evals — winogenerated README"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Generated Winogender dataset, as discussed in the paper section "Evaluation Gender Bias with Human-AI Dataset Creation".

**`generated_winogender_data.jsonl`.** Provides 10 Winogender-format sentences for each occupation. Per-entry keys: `index`, `occupation`, `other_person`, `sentence_with_blank` (the sentence the model fills in), three `pronoun_options` in a list, and the `BLS_original_occupation` and `BLS_percent_women_2019` for reference. Total: 299 professions and 2,990 sentences.

**`bls_occupations.jsonl`.** Lists the model-modified occupational titles (`occupation`) with corresponding original Bureau of Labor Statistics titles (`BLS_original_occupation`), the 2019 percent-women per occupation (`BLS_percent_women_2019`), and the model-generated `other_person` for each.

The dataset is the larger, model-generated counterpart to the original Winogender Dataset (Rudinger et al. 2018) for evaluating gender bias in coreference resolution.
