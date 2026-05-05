---
type: summary
source: 01_Raw/support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry.md
source_url: https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry
title: "Monitor Claude Cowork Activity with Opentelemetry"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

This article explains how to use OpenTelemetry (OTel) to monitor Claude Cowork activity across your organization. With OTel, your security and operations teams can stream Cowork events into the observability tools you already use to track usage, investigate incidents, and analyze performance.

OpenTelemetry monitoring for Claude Cowork is available on Team and Enterprise plans. It requires Claude Desktop version 1.1.4173 or later.

When you connect Claude Cowork to an OpenTelemetry collector, Cowork streams events covering:

A shared `prompt.id` attribute links every event triggered by a single user prompt, so you can reconstruct everything Claude did in response to one input.

Covers: What you can monitor; When to use OpenTelemetry; Compatible destinations; Set up OpenTelemetry monitoring; Security and privacy considerations; Joining OpenTelemetry data with the Compliance API.
