---
type: summary
source: 01_Raw/support.claude.com/en/articles/14680729-use-claude-cowork-with-third-party-platforms.md
source_url: https://support.claude.com/en/articles/14680729-use-claude-cowork-with-third-party-platforms
title: "Use Claude Cowork with Third Party Platforms"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Computer-use, Enterprise-gateway]
concepts_referenced: []
---

If your organization uses Amazon Bedrock, Google Cloud Vertex AI, Azure AI Foundry, or an LLM gateway to access Claude, you can deploy Claude Cowork to run on the same infrastructure. Prompts and completions route through your inference provider, so Anthropic never sees them, while users get the same Cowork experience: delegate long-running tasks to Claude, work with local files, and use MCP connectors. Your IT team configures the deployment via MDM.

This deployment supports both Claude Cowork (the long-running task experience) and Claude Code Desktop (CCD), an agentic coding interface for developers who prefer a graphical environment over a terminal. For more on CCD, see Use Claude Code Desktop.

Covers: Who this is for; Supported inference providers; Architecture and data flow; Data residency; How it compares to Claude Enterprise; Virtual Desktop Infrastructure (VDI) support; Pricing; Frequently asked questions.
