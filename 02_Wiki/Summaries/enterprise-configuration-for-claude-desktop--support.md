---
type: summary
source: 01_Raw/support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop.md
source_url: https://support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop
title: "Enterprise Configuration for Claude Desktop"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Administrators on Team or Enterprise plans can control Claude Desktop through system policies.

Note: Enterprise policy controls at the user-machine level will override the in-app allowlist. If you want to use the allowlist, ensure `isDesktopExtensionEnabled` and `isDesktopExtensionDirectoryEnabled` are not set to "false" so the allowlist can populate the available registry.

Deploy configuration settings through your MDM solution using configuration profiles. Claude Desktop reads preferences from the domain `com.anthropic.claudefordesktop`. Use your MDM tool (Jamf Pro, Kandji, Microsoft Intune) to deploy configuration profiles to target machines or user groups. Configuration profiles allow you to manage Claude Desktop settings centrally without user intervention.

Covers: macOS enterprise configuration; Windows enterprise configuration; Enterprise policy options.
