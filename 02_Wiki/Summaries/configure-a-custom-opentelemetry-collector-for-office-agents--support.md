---
type: summary
source: 01_Raw/support.claude.com/en/articles/14447276-configure-a-custom-opentelemetry-collector-for-office-agents.md
source_url: https://support.claude.com/en/articles/14447276-configure-a-custom-opentelemetry-collector-for-office-agents
title: "Configure a Custom Opentelemetry Collector for Office Agents"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Enterprise-gateway]
concepts_referenced: []
---

You can route full audit telemetry from Office agents to your own OpenTelemetry (OTEL) collector. This gives your organization complete control over retention, encryption, and integration with your SIEM or observability platform.

This guide covers how to enable a custom collector, what data you'll receive, and the full span schema reference.

Custom OTEL collectors are available to Claude Enterprise organizations and to direct-provider deployments (Amazon Bedrock, Google Vertex AI, or a gateway).

When you configure a custom collector, Office agents send trace data covering every user turn. Each turn produces a tree of spans capturing the prompt, model calls, tool executions, file uploads, and context compaction events.

Covers: What you'll receive; Enable a custom collector; Claude Enterprise (OAuth) organizations; Direct provider deployments (Amazon Bedrock, Google Vertex AI, gateway); Deployment modes; Surface and vendor labels; Span reference; Resource attributes.
