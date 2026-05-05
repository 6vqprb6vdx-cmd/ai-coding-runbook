---
type: summary
source: 01_Raw/support.claude.com/en/articles/14680753-extend-claude-cowork-with-third-party-platforms.md
source_url: https://support.claude.com/en/articles/14680753-extend-claude-cowork-with-third-party-platforms
title: "Extend Claude Cowork with Third Party Platforms"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Subagent, Plugin, Enterprise-gateway]
concepts_referenced: []
---

When Claude Cowork is deployed on Amazon Bedrock, Google Cloud Vertex AI, Azure AI Foundry, or an LLM gateway, MCP connectors, plugins, and skills work differently than they do on Claude Enterprise. Everything is controlled via MDM and local filesystem mounts, with a local setup interface and configuration pushed via MDM.

This article covers admin controls (allowlisting, distribution, policies) and the end-user experience (what's available, what isn't).

MCP (Model Context Protocol) lets Claude connect to tools and data sources beyond what's built into Claude Desktop. Both local MCP servers running on the user's machine and remote MCP servers accessed over HTTP or SSE are supported.

Covers: MCP connectors; Admin-managed remote MCP servers; User-added local MCP servers; Disabling built-in tools; Plugins; Plugin mount location; Plugin directory structure; Desktop extensions.
