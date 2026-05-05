---
type: summary
source: 01_Raw/support.claude.com/en/articles/14680741-install-and-configure-claude-cowork-with-third-party-platforms.md
source_url: https://support.claude.com/en/articles/14680741-install-and-configure-claude-cowork-with-third-party-platforms
title: "Install and Configure Claude Cowork with Third Party Platforms"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Enterprise-gateway]
concepts_referenced: []
---

This guide walks IT admins through deploying Claude Cowork on Amazon Bedrock, Google Cloud Vertex AI, Azure AI Foundry, or an LLM gateway. It covers download, MDM configuration for macOS and Windows, provider-specific setup, and the full MDM key reference.

If you're evaluating whether this deployment is right for your organization, start with Claude Cowork with third-party platforms.

Download Claude Desktop for your platform from the download page. The same binary ships for standard Claude Cowork and third-party deployments—the MDM configuration profile determines which mode the app runs in.

Open the downloaded Claude Desktop app (you do not need to log in). Navigate to the Menu Bar, and select Help → Troubleshooting → Enable Developer mode. With Developer mode enabled, go Developer → Configure third-party inference. This activates a setup UI to configure the required fields. You can find more information about each field here: Configuration reference.

Covers: Before you begin; Download the installer; macOS; Windows; Configure third-party inference via the Setup UI; Apply the MDM configuration; VDI deployments; Set up plugins.
