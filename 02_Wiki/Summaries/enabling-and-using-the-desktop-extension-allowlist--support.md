---
type: summary
source: 01_Raw/support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist.md
source_url: https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist
title: "Enabling and Using the Desktop Extension Allowlist"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

The desktop extension allowlist is available for Owners and Primary Owners of Team and Enterprise plans.

This article introduces a desktop extension allowlist that Team and Enterprise plan Owners can use to manage their organization’s access to extensions.

Important: If you’ve previously configured Enterprise policy controls at the user-machine level, these will override the in-app allowlist. Ensure both `isDesktopExtensionDirectoryEnabled` and `isDesktopExtensionEnabled` are not set to "false" so the allowlist can populate the available registry. Refer to our desktop enterprise configuration documentation for more information.

The desktop extension allowlist is disabled by default, so an organization Owner will need to switch it on manually. Note that users will be able to access all desktop extensions in the registry until you enable the allowlist. To prevent this, ensure you activate the allowlist to block all desktop extensions by default, then add only the extensions your team needs access to.

Covers: How to enable the allowlist; What happens after enabling the allowlist?; Managing allowed extensions; Uploading custom extensions; Updating custom extensions.
