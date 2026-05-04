---
source_url: https://support.claude.com/en/articles/13163631-configuring-session-security-settings
fetched_at: 2026-05-04T16:55:33.802957+00:00
fetch_method: mintlify_md
---

This feature is available to Admins and Owners of Enterprise plans and Console Admins.

Session duration controls allow Enterprise and Console Admins to set a maximum session length for all users in their organization. When enabled, users will need to sign in again after the specified period, even if they've been actively using Claude. This helps protect your organization by limiting how long a compromised session could remain valid.

## Enabling session length settings

### For Enterprise Admins

1. Log in to your Enterprise organization as an Admin or above.

2. Navigate to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.

3. Locate the **Session security** section.

4. Click “Enable” next to **Shortened session length**, then select a duration from the dropdown: 7 days, 14 days, or 28 days.

5. Confirm your selection by clicking “Enable.”

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469436/1725e63ea1a2615948faecf4ec73/9bd276a1-7329-414d-87a1-d04dac93fff7?expires=1777915800&amp;signature=da73449d3229cbea21538d91f313b8ae496626fcfbd324a29cefb824d49a1252&amp;req=dSgvHs14lIVcX%2FMW1HO4zQNx5OUuQl9Yg%2F6XaftFnjzKGvBRYrE%2BsqoZbe1v%0ASHm95zPvxLSbCNMxU9M%3D%0A)

### For Console Admins

1. Log in to your Console account as an Admin.

2. Navigate to **[Settings > Organization and access](http://platform.claude.com/settings/organization)**.

3. Locate the **Session security** section.

4. Click “Enable” next to **Shortened session length**, then select a duration from the dropdown: 1 day, 3 days, or 7 days.

5. Confirm your selection by clicking “Enable.”

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469435/7a766bbe02e61c7d8f05deb5b8f0/b0bda400-47c6-43dd-9907-131ebe180b36?expires=1777915800&amp;signature=e3b88b9b2dfe51b9d9122083424a5f7d98a3005f8de00d4260ba6f6a0fd2e379&amp;req=dSgvHs14lIVcXPMW1HO4zWzx174%2FJnopXZ5D7eVpMtdPie%2By36vaWLULojK8%0As2XFeCZwCo1LyGk8uhI%3D%0A)

### What happens after enabling shortened session length?

- Existing sessions older than the selected duration will expire immediately.

- Other active sessions will expire no later than the selected duration.

- Users whose sessions expire will be directed to sign in again.

## Updating session duration

You can change the session duration at any time by selecting a new value from the dropdown. If you select a shorter duration:

- Sessions older than the new duration will expire immediately.

- Sessions scheduled to expire beyond the new duration will have their expiration shortened accordingly.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469437/46ac5bc55484ca01556d87a5ade7/b01a7651-ad65-4b32-93ff-16dbc9ca97c0?expires=1777915800&amp;signature=c97d2d00135f963b697ed065b978751bed26319d44d51cdf700e8e81b990d85f&amp;req=dSgvHs14lIVcXvMW1HO4zZ7mVc%2BS5jyrA00cbyPOLDXt1zlaHxSwD0gKnAt4%0AzIipbjTsJYfpk6h%2Fq2E%3D%0A)

## Disabling session length settings

To disable session duration, select "Disable" next to **Shortened session length**. Existing active sessions will continue to expire at their scheduled time. New sessions will return to default behavior, where sessions remain active as long as the user stays active.

## Users in multiple organizations

If a user belongs to multiple organizations with different session duration settings, the shortest duration will be applied. For example, if a user is a member of Organization A (7-day limit) and Organization B (28-day limit), their sessions will expire after seven days. This is because a single session is used across all their organizations, so the most restrictive setting takes precedence.
