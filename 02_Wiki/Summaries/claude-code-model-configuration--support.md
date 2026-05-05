---
type: summary
source: 01_Raw/support.claude.com/en/articles/11940350-claude-code-model-configuration.md
source_url: https://support.claude.com/en/articles/11940350-claude-code-model-configuration
title: "Claude Code Model Configuration"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

This guide shows you three ways to change which Claude model you're using with Claude Code: the quick `/model` command for instant changes, the `--model` flag for one-time session changes, and environment variables to set your preferred model as the permanent default.

The simplest way to change models is to use the /model command directly within Claude Code. This works immediately without restarting your terminal.

Note: You can check your current model anytime by running `/status` in Claude Code.

Use the `--model` flag when starting Claude Code.

Step 1) Check your shell type by running: `echo $SHELL`

Covers: Easiest method: Use /model command; Supported models; Change model for current session only; Change default model for all future sessions; For ZSH users (macOS); For BASH users (Linux).
