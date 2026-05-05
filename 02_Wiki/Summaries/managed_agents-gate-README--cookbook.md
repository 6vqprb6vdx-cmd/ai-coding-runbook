---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/managed_agents/example_data/gate/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/example_data/gate/README.md
title: "Claude Cookbooks — managed_agents/example_data/gate README"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent]
concepts_referenced: []
---

Fixture data for `CMA_gate_human_in_the_loop.py` — the human-in-the-loop expense-approver tutorial.

Contains a `policy.yaml` and twelve receipts in `inbox/receipts.jsonl`. The agent classifies each receipt against the policy using two custom tools: `decide()` for clear approves and rejects, `escalate()` for anything ambiguous.

**Receipt design.** The twelve receipts are constructed to hit every branch of the policy: a handful that should auto-approve cleanly, one with no receipt image where the policy demands one, a couple in the manager-approval band, two over the threshold, one travel charge that always escalates regardless of amount, and one with a deliberately ambiguous category. A healthy run produces a mix of `approve`, `reject`, and `escalated` decisions — never all of one lane.
