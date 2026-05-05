---
type: summary
source: 01_Raw/support.claude.com/en/articles/14552646-troubleshoot-claude-code-installation-and-authentication.md
source_url: https://support.claude.com/en/articles/14552646-troubleshoot-claude-code-installation-and-authentication
title: "Troubleshoot Claude Code Installation and Authentication"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

These ten issues account for the large majority of installation and authentication support tickets related to Claude Code. Each entry includes the most reliable fix.

The installer added `claude` to your PATH, but your current shell has not picked it up yet. Open a new terminal, or run `source ~/.zshrc` (or `~/.bashrc`). On Windows, close and reopen PowerShell.

This usually means the install was run with `sudo`, or your global npm directory is root-owned. Do not use sudo. Instead, use the native installer (`curl -fsSL <https://claude.ai/install.sh> | bash`), or fix npm's prefix with `npm config set prefix ~/.npm-global` and add that `bin` directory to your PATH.

Covers: 1. **claude: command not found** right after installing.; 2. npm install fails with `EACCES` / permission denied.; 3. "Node version not supported" or silent crash on launch.; 4. WSL: **claude** runs the Windows Node instead of Linux Node.; 5. Installer hangs or fails behind a corporate network.; 6. **SELF_SIGNED_CERT_IN_CHAIN** or other TLS errors.; 7. **/login** opens a browser but the terminal never finishes ("Waiting for authentication…").; 8. "Not authenticated" even though you set `ANTHROPIC_API_KEY`..
