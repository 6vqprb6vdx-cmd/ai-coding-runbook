---
type: summary
source: 01_Raw/support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide.md
source_url: https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide
title: "Claude Enterprise Analytics API Reference Guide"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

The Claude Enterprise Analytics API gives your organization programmatic access to engagement data for Claude and Claude Code usage within your Enterprise organization. Whether you're building internal dashboards for user activity or tracking adoption of projects, this API provides the aggregated metrics you need.

All data is aggregated per organization, per day. Each endpoint returns a snapshot for a single date that you specify. Data for day (N-1) is run at 10:00:00 UTC time on day N, and is available for querying three days after aggregation, to ensure accuracy of data.

Covers: Overview; Data aggregation; Enabling access; Base URL; Authentication; Pagination; Error responses; Rate limiting.
