---
type: summary
source: 01_Raw/support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government.md
source_url: https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government
title: "Set Up SCIM in Claude for Government"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

System for Cross-domain Identity Management (SCIM) lets your identity provider automatically manage user accounts in Claude for Government. With SCIM, your IdP controls who has access, what role they hold, and what seat tier they're assigned—without manual intervention in the Claude admin console.

For SCIM setup on Claude Enterprise, see Set up JIT or SCIM provisioning.

Claude for Government uses a first-party SCIM implementation hosted within the FedRAMP-authorized environment. The commercial Claude Enterprise plan uses a different SCIM backend.

| Feature | Claude for Government | Claude Enterprise | | --- | --- | --- | | SCIM endpoint | claude.fedstart.com/v1/scim/v2 | Configured via claude.ai | | SCIM implementation | Anthropic first-party (FedRAMP-authorized) | Third-party integration | | API key management | Self-service via identity settings page | Self-service via admin settings | | Parent Organization Support | Yes — for multi-org identity management | Not applicable |

Covers: How SCIM differs for Claude for Government; Prerequisites; How provisioning works with and without SCIM; Step 1: Generate a SCIM API key; Step 2: Configure SCIM in your Identity Provider; Step 3: Verify sync status; Step 4: Map groups to roles and seat tiers; Parent organizations (multi-org setups).
