---
type: summary
source: 01_Raw/github/anthropics/evals/README.md
source_url: https://github.com/anthropics/evals/blob/main/README.md
title: "Anthropic Evals — root README"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Model-Written Evaluation Datasets repo. Includes datasets written by language models, used in the Anthropic paper "Discovering Language Model Behaviors with Model-Written Evaluations".

**Intended audience.** Researchers interested in the quality and properties of model-generated data, and practitioners who want to evaluate other models for the behaviors examined (model persona, sycophancy, advanced AI risks, gender bias). Designed for dialogue agents (finetuned to respond to user utterances or pretrained models prompted as dialogue agents); adaptable to other model classes.

**Dataset collections:**

1. **`persona/`** — datasets testing models for various aspects of behavior related to stated political and religious views, personality, moral beliefs, and desire to pursue potentially dangerous goals (e.g., self-preservation or power-seeking).
2. **`sycophancy/`** — datasets testing whether models repeat back a user's view to philosophy, NLP research, and political questions.
3. **`advanced-ai-risk/`** — datasets testing behaviors related to catastrophic risks from advanced AI systems. Generated few-shot. Also includes human-written datasets collected by Surge AI for reference and comparison.
4. **`winogender/`** (directory shipped as `winogenerated/`) — larger, model-generated version of the Winogender Dataset (Rudinger et al. 2018). Includes the model-generated occupation titles plus occupation gender statistics from the Bureau of Labor Statistics.

**Disclaimer.** Some data contains content with social biases and stereotypes; may also contain other harmful or offensive content. Views expressed in the data don't reflect Anthropic or its employees' views.

**Contact.** Questions to `ethan at anthropic dot com`.

**Citation.** Provides BibTeX for `@misc{perez2022discovering, …}` (arXiv 2212.09251). Long author list reflecting the joint Anthropic team.
