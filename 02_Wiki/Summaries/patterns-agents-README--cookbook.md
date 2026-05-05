---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/patterns/agents/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/patterns/agents/README.md
title: "Claude Cookbooks — patterns/agents/ README (Building Effective Agents)"
summarized_at: 2026-05-05
entities_referenced: [Subagent]
concepts_referenced: [Agentic-loop, Agent-team]
---

Reference implementation for "Building Effective Agents" by Erik Schluntz and Barry Zhang on Anthropic's research blog.

The directory contains minimal example implementations of common agent workflows discussed in the blog post:

**Basic Building Blocks.**

- Prompt Chaining
- Routing
- Multi-LLM Parallelization

**Advanced Workflows.**

- Orchestrator-Subagents
- Evaluator-Optimizer

**Notebooks** (in this directory):

- `basic_workflows.ipynb` — covers the basic building blocks above.
- `evaluator_optimizer.ipynb` — evaluator-optimizer workflow.
- `orchestrator_workers.ipynb` — orchestrator-workers workflow.

The notebooks are direct, runnable companions to the blog post — each shows the canonical pattern in a few cells with explanations. They are intentionally minimal so the structural shape of each pattern is visible without framework overhead.
