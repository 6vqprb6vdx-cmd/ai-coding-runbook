---
type: summary
source: 01_Raw/support.claude.com/en/articles/14554922-claude-code-user-faq.md
source_url: https://support.claude.com/en/articles/14554922-claude-code-user-faq
title: "Claude Code User FAQ"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Subagent, Hooks, Slash-command, Settings, IDE-integration]
concepts_referenced: []
---

Short answers to the questions that come up most at office hours, with a link to go deeper. Organized by where you are in your first few weeks. Five sections follow the arc of a developer’s first weeks: getting started, day-to-day use, leveling up, common gotchas, privacy, and trust. Skim the section that matches where you are, or search for a specific question. | Question | Answer | | --- | --- | | 1.1 How do I install it? | macOS/Linux: `curl -fsSL <https://claude.ai/install.sh> | bash` <br>​Windows PowerShell: `irm <https://claude.ai/install.ps1> | iex` <br>​Homebrew: `brew install --cask claude-code` <br>​WinGet: `winget install Anthropic.ClaudeCode` <br>Then run `claude` from any repo.<br> <br>Reference: Quickstart | | 1.2 Installed, but “claude: command not found” | The native installer puts the binary at `~/.local/bin/claude` (Windows: `%USERPROFILE%\.local\bin`). Add that directory to your PATH, e.g. `export PATH="$PATH:$HOME/.local/bin"` in `~/.zshrc` or `~/.bashrc`, then restart your terminal.<br> <br>Reference: Troubleshooting: PATH | | 1.3 Login opens a browser on the wrong machine / I’m on SSH | Press `c` at the login prompt to copy the auth URL. Open it in a local browser, then paste the code back into the terminal.<br> <br>Reference: Troubleshooting: auth | | 1.4 Auth errors right after login, but I have access | 400 “organization disabled”: a stray `ANTHROPIC_API_KEY` env var is overriding your login. Unset it, remove from your shell profile, restart. Run `/status` to confirm which auth is active.
