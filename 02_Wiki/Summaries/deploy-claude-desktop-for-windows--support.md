---
type: summary
source: 01_Raw/support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows.md
source_url: https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows
title: "Deploy Claude Desktop for Windows"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Administrators on Team or Enterprise plans can deploy Claude Desktop automatically across their organization to manage installations and updates centrally. We offer MSIX packages for Windows deployments via Microsoft Intune, SCCM, Group Policy, or PowerShell, enabling secure, scalable distribution.

Claude Desktop for Windows requires the Virtual Machine Platform to use Cowork. You can automate installation of this feature via most endpoint management solutions, but you may also run the following command to install it manually:

``` Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -All -NoRestart ```

``` ```powershell Add-AppxPackage -Path "Claude.msix" ``` ``` For more details, see Microsoft's Add-AppxPackage documentation.

Covers: Installation requirements; Cowork requirements; Download; Installation commands; Install for single user; Install for all users (provisions machine-wide); Deploy via MDM; Configuration.
