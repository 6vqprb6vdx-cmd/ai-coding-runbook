---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/managed_agents/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/README.md
title: "Claude Cookbooks — managed_agents/ tutorial README"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Session-API, Memory-store, Vault, Skill, MCP-server, Environment-API]
concepts_referenced: []
---

Tutorials for Claude Managed Agents — Anthropic's hosted runtime for stateful, tool-using agents. You define an agent and a sandboxed environment once, then run them in sessions that persist files, tool state, and conversation across turns.

**Applied cookbooks:**

- `data_analyst_agent.ipynb` — analyst that turns a CSV into a narrative HTML report using pandas and plotly. Configures environment + agent, mounts a dataset, streams the run, retrieves generated artifacts.
- `slack_data_bot.ipynb` — wraps that analyst as a Slack bot. Mention with a CSV → report in-thread; replies continue the same session.
- `sre_incident_responder.ipynb` — Managed Agents on the on-call path: pager alert starts a session, agent investigates and opens a PR, pauses for human approval before merging. Wires the alert webhook, attaches a Skill and custom tools, reviews the run in the Console.

**Guided tutorials** (no strict order, but `CMA_iterate_fix_failing_tests.ipynb` is a good entry point — introduces every API shape the others build on):

| Notebook | Teaches |
|----------|---------|
| `CMA_iterate_fix_failing_tests.ipynb` | Do → observe → fix loop on a failing test suite. Entry-point: agent / environment / session, file mounts, streaming event loop. |
| `CMA_orchestrate_issue_to_pr.ipynb` | Issue → fix → PR → CI → review → merge through a mock `gh` CLI. Multi-turn steering, mid-chain recovery from CI failure and review comment. Sidebar: swap file mount for `github_repository` resource. |
| `CMA_explore_unfamiliar_codebase.ipynb` | Grounding in unfamiliar code with a planted stale-doc trap. Sidebar: `sessions.resources.add` on a running session. |
| `CMA_gate_human_in_the_loop.ipynb` | HITL expense approval via custom-tool `decide()` / `escalate()`. Custom-tool round-trip pattern, `requires_action` idle bounce, parallel-tool-call dedupe. |
| `CMA_prompt_versioning_and_rollback.ipynb` | Server-side prompt versioning: create v1, evaluate, ship v2, detect regression, roll back by pinning sessions to v1. Covers `agents.update`, version pinning on `sessions.create`. |
| `CMA_operate_in_production.ipynb` | Production setup: MCP toolsets, vaults for per-end-user credentials, the `session.status_idled` webhook for HITL without long-lived connections, resource-lifecycle CRUD verbs. |
| `CMA_remember_user_preferences.ipynb` | Memory stores: shopping agent learns a customer's preferences in one session and recalls them in the next. `memory_stores.create`, per-attachment `instructions`, inspecting/seeding memories from your own application, combining a per-customer read-write store with a brand-wide read-only store. |

The streaming event loop is walked through line by line in the iterate notebook and then factored into `utilities.stream_until_end_turn` for reuse. The gate notebook keeps the loop inline because custom-tool agents need to handle `requires_action` idle bounces in addition to `end_turn`.

**Getting started.** Set `ANTHROPIC_API_KEY`, open `data_analyst_agent.ipynb`, run top to bottom. Some notebooks need `GITHUB_TOKEN` (fine-grained PAT with public-repo read). Fixture data lives in `example_data/` (see `example_data/OVERVIEW.md`).
