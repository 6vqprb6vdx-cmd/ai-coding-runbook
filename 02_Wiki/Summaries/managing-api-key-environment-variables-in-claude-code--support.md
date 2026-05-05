---
type: summary
source: 01_Raw/support.claude.com/en/articles/12304248-managing-api-key-environment-variables-in-claude-code.md
source_url: https://support.claude.com/en/articles/12304248-managing-api-key-environment-variables-in-claude-code
title: "Managing API Key Environment Variables in Claude Code"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

When using Claude Code, it's important to understand how authentication methods are prioritized to avoid unexpected API charges and ensure you're using your intended account.

To use Claude Code with your Claude subscription: Keep the ANTHROPIC_API_KEY environment variable unset.

Claude Code will notify you when there's a conflict between your authenticated subscription and an environment variable API key:

To verify if an API key is set as an environment variable, run /status in Claude Code. This will show you which authentication method is currently active.

To check your environment variable directly, run one of these commands in a terminal (outside of Claude Code):

Covers: Understanding authentication priority in Claude Code; How authentication works; Best practices; Authentication conflict warnings; Checking your current configuration; Setting an API key temporarily; Setting an API key environment variable permanently; Removing an API key environment variable.
