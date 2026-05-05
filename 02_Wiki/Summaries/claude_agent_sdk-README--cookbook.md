---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/claude_agent_sdk/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/README.md
title: "Claude Cookbooks — claude_agent_sdk/ tutorial series README"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, MCP-server, Hooks, Subagent, Memory, Slash-command, Output-style]
concepts_referenced: [Agentic-loop, Agent-team]
---

A tutorial series on building powerful general-purpose agents with the Claude Agent SDK. Progresses from simple research agents to multi-agent orchestration with external system integration.

**Setup.** Install `uv`, Node, and the Claude Code CLI (`npm install -g @anthropic-ai/claude-code`). Clone the cookbook, `cd` into `claude_agent_sdk/`, run `uv sync`. Register the venv as a Jupyter kernel: `uv run python -m ipykernel install --user --name="cc-sdk-tutorial" --display-name "Python (cc-sdk-tutorial)"`. Get an API key at platform.claude.ai. For Notebook 02 also need a fine-grained GitHub PAT and Docker running.

**What you'll learn.** Core SDK fundamentals (`query()`, `ClaudeSDKClient`, `ClaudeAgentOptions`); tool patterns from basic WebSearch to complex MCP integration; multi-agent orchestration via specialized subagents; enterprise features via hooks (compliance / audit trails); external system integration via MCP. Tutorial assumes some familiarity with Claude Code.

**Notebook structure:**

- **Notebook 00 — One-Liner Research Agent.** Simple research agent built in a few lines. Introduces `query()` + async iteration, the WebSearch tool, multimodal Read tool, conversation context management with `ClaudeSDKClient`, system-prompt specialization.
- **Notebook 01 — Chief of Staff Agent.** Comprehensive AI Chief of Staff for a startup CEO. Persistent CLAUDE.md memory, output styles for different audiences, plan mode, custom slash commands, hooks for compliance/audit, subagent orchestration, Bash tool for Python script execution.
- **Notebook 02 — Observability Agent.** External integration via MCP. Git MCP Server (13+ tools), GitHub MCP Server (100+ tools), real-time CI/CD pipeline analysis, intelligent incident response, automated production workflow.
- **Notebook 03 — Site Reliability Agent.** Read-write remediation. Custom MCP tool server (12+ tools for metrics/infra/diagnostics/docs via JSON-RPC subprocess), Prometheus PromQL queries, edits config files / restarts Docker services / verifies fixes, PreToolUse safety hooks (e.g., pool size range checks), end-to-end incident lifecycle, optional PagerDuty / Confluence integration via conditional MCP registration.

**Standalone agents.** Each notebook ships with its own agent module: `research_agent/`, `chief_of_staff_agent/`, `observability_agent/`, `site_reliability_agent/`. To import outside notebooks, run from `claude_agent_sdk/` directly or `uv pip install -e .`.

**Background.** Frames the Claude Agent SDK's evolution: Claude Code's breakthrough was that Claude is exceptionally good at agentic work — task decomposition, intelligent tool choice, long-running context, error recovery, knowing when to ask vs. proceed. The SDK exposes that minimal harness for any domain, and this series shows how to leverage it beyond coding (research / data analysis / workflow automation / monitoring / content generation).
