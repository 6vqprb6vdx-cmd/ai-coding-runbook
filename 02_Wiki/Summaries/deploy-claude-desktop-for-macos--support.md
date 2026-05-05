---
type: summary
source: 01_Raw/support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos.md
source_url: https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos
title: "Deploy Claude Desktop for Macos"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Administrators on Team or Enterprise plans can deploy Claude Desktop automatically to manage installations and updates centrally. Claude Desktop installs to `/Applications` and updates automatically when new versions are released, unless disabled via enterprise policies.

Cowork will be installed automatically when you download and install Claude Desktop for macOS.

Universal (x64 or arm64) Claude PKG

The Universal build is compatible with both Intel and Apple Silicon machines and supports all Mac hardware.

Upload the PKG to your MDM solution (Jamf, Kandji, Microsoft Intune) and deploy to target machines.

To configure Claude Desktop settings such as auto-updates, extensions, and MCP servers, see the Enterprise Configuration article.

Covers: Available installation formats; Cowork requirements; Download; Deploy via MDM; Configuration; Troubleshooting; Users cannot update Claude Desktop.
