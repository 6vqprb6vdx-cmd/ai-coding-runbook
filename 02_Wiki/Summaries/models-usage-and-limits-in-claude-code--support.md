---
type: summary
source: 01_Raw/support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code.md
source_url: https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code
title: "Models Usage and Limits in Claude Code"
summarized_at: 2026-05-05
entities_referenced: [Enterprise-gateway]
concepts_referenced: []
---

This guide explains which model you are using, how usage is metered, and how to keep long sessions within their context and usage limits.

How you signed in determines how usage is metered. Everything else about Claude Code behaves the same way regardless.

| You signed in with… | You get | What "running out" looks like | | --- | --- | --- | | Claude Enterprise seat (via `/login`) | A pool of usage included in your organization's plan, reset on a rolling window. | A "limit reached, resets at *time*" message. | | API key (Console, Bedrock, Vertex, or Microsoft Foundry) | Pay-as-you-go, billed per token to that cloud or Console account. | No hard stop; the account is charged for what it uses. |

Covers: How usage is metered; Choosing a model; What actually consumes tokens; Managing the context window; Five habits that stretch your usage furthest; 1. Clear between tasks; 2. Match the model to the job; 3. Point at files instead of pasting them.
