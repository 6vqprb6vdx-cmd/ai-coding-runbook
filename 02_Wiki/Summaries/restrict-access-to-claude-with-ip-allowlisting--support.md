---
type: summary
source: 01_Raw/support.claude.com/en/articles/13200993-restrict-access-to-claude-with-ip-allowlisting.md
source_url: https://support.claude.com/en/articles/13200993-restrict-access-to-claude-with-ip-allowlisting
title: "Restrict Access to Claude with IP Allowlisting"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

IP allowlisting is available for Enterprise plans only.

IP allowlisting enables Enterprise plan administrators to control which IP addresses can access Claude through their organization. This feature ensures that requests can only be made from approved network locations, providing an additional layer of security.

When enabled, we validate the source IP address of every authenticated request against your organization's configured allowlist. Requests from IP addresses not added to the allowlist will be blocked.

IP allowlisting supports CIDR ranges. For example: `10.0.0.0/8, 2001:db8::/32`.

If your Enterprise organization is interested in enabling an IP allowlist, please compile a list of all necessary CIDR ranges for your organization, including office locations, VPN exit points, and any other approved access points. Omitting required CIDR ranges could result in users getting locked out of Claude. Then, reach out to your Anthropic Contact or our Sales team to share your list of CIDR ranges. They can add these to your account’s allowlist to enable the feature.

Covers: How to configure IP allowlisting.
