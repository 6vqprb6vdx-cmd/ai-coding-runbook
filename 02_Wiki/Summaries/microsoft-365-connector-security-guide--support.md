---
type: summary
source: 01_Raw/support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide.md
source_url: https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide
title: "Microsoft 365 Connector Security Guide"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

The Microsoft 365 connector is available on all Claude plans: Free, Pro, Max, Team, and Enterprise.

The Microsoft 365 Connector is an Anthropic-hosted integration that enables Claude to securely access Microsoft 365 services (Outlook, SharePoint, OneDrive, Teams) through user-delegated permissions. Anthropic has completed Microsoft's publisher verification process, associating our verified Microsoft Partner Network account with this application to confirm our organizational identity.

The connector operates as a secure proxy, and your Microsoft 365 documents, emails, and files remain in your tenant. The connector only retrieves data on-demand during active queries and doesn’t cache file content. Credentials are encrypted and managed by Anthropic's backend infrastructure. The MCP server itself doesn’t store or manage these credentials. Microsoft's Azure SDK handles the On-Behalf-Of token exchange and caching on a per-user basis for accessing the Graph API.

Covers: What it is; Access restriction; Access can be fully restricted; Security architecture summary; Authentication flow; Data flow; Multi-tenant isolation; Available capabilities.
