---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/README.md
title: "Claude Cookbooks — root README"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-Python, Vision, PDF-support, Subagent]
concepts_referenced: [Tool-use, Prompt-caching]
---

The Claude Cookbooks is a collection of code and guides designed to help developers build with Claude, offering copy-able snippets that integrate easily into other projects. Examples are primarily Python but the concepts adapt to any language with HTTP/SDK support. Newcomers are pointed at the Claude API Fundamentals course for a foundation.

**Table of recipes:**

- **Capabilities** — Classification, Retrieval Augmented Generation, Summarization (each in its own subdirectory under `capabilities/`).
- **Tool Use and Integration** — generic `tool_use/` directory plus specific notebooks: customer service agent, calculator integration, SQL queries.
- **Third-party integrations for RAG** — Vector databases (Pinecone), Wikipedia, web pages, plus VoyageAI for embeddings.
- **Multimodal** — Vision with Claude (`multimodal/` directory): getting started with images, best practices, interpreting charts/graphs/PowerPoints, extracting content from forms. Also: generating images via Stable Diffusion.
- **Advanced techniques** — sub-agents (using Haiku as a sub-agent in combination with Opus), uploading PDFs, automated evaluations, JSON mode, content moderation filter, prompt caching.

**Prerequisites.** A Claude API key. Free signup at anthropic.com.

**Additional resources.** Anthropic developer documentation, Anthropic support docs, Anthropic Discord, plus Anthropic on AWS and broader AWS Samples.

The README also lays out the contribution path: review existing issues/PRs, open ideas on the issues page. The actual contributor mechanics (env setup, lint, notebook validation) live in `CONTRIBUTING.md`.
