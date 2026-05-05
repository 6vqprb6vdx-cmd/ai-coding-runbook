---
type: summary
source: 01_Raw/support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations.md
source_url: https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations
title: "How SCIM Sync Works for Enterprise Organizations"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

SCIM provisioning keeps your Enterprise organization's membership and groups in sync with your identity provider. This article covers what gets synced, how syncs are triggered, and what to watch for when resyncing.

Available on the Enterprise plan. For setup instructions, see Set up JIT or SCIM provisioning.

When you connect your identity provider (IdP) to your Enterprise organization through the WorkOS integration, two things sync from your IdP:

Group membership in your organization determines which capabilities members with custom roles can access, along with group spend limits.

Your Enterprise organization receives changes from your IdP automatically whenever your IdP pushes member or group updates (adds, removes, or edits) to WorkOS.

Covers: What gets synced; Automatic syncing; Manual syncing; Actions that trigger a manual sync; How to manually trigger a sync; Member sync vs. group sync; How long manual syncs take; Verifying your sync status.
