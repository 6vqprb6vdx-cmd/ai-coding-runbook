---
type: summary
source: 01_Raw/support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions.md
source_url: https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions
title: "Enforce Network Level Access Control with Tenant Restrictions"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Tenant Restrictions are available for members of Enterprise plans and Console organizations.

Tenant Restrictions enable IT administrators on Enterprise plans to enforce network-level access control for Claude. This feature ensures that users on corporate networks can only access approved organizational accounts, preventing unauthorized use of personal accounts.

When enabled, your network proxy injects an HTTP header into requests to Claude. Anthropic validates this header and blocks access from any organization not in the allowed list.

``` anthropic-allowed-org-ids: <org-uuid-1>,<org-uuid-2>,... ```

``` anthropic-allowed-org-ids: 550e8400-e29b-41d4-a716-446655440000,6ba7b810- 9dad-11d1-80b4-00c04fd430c8 ```

Members of Console organizations can find this in Settings > Organization.

Covers: How it works; Header format; Configuration steps; 1. Find your organization UUID; 2. Configure your network proxy; 3. Test your configuration; Error response; Supported proxy platforms.
