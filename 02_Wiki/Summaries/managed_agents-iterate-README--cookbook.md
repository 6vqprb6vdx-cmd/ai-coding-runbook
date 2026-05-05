---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/managed_agents/example_data/iterate/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/example_data/iterate/README.md
title: "Claude Cookbooks — managed_agents/example_data/iterate README"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent]
concepts_referenced: []
---

Fixture data for `CMA_iterate_fix_failing_tests.py` — the do → observe → fix loop tutorial.

Contains `calc.py` with three planted bugs and `test_calc.py` with three assertions that catch them.

**Trap.** The interesting bug is `test_mean`: `mean()` calls `add` and `divide` internally, so it goes green on its own once the other two are fixed. An agent that edits `mean()` directly is over-fixing — the planted trap teaches the agent to read failures carefully and only patch the actual root cause.
