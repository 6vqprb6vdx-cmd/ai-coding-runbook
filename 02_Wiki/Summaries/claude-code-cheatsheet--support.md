---
type: summary
source: 01_Raw/support.claude.com/en/articles/14553413-claude-code-cheatsheet.md
source_url: https://support.claude.com/en/articles/14553413-claude-code-cheatsheet
title: "Claude Code Cheatsheet"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Subagent, Hooks, Slash-command]
concepts_referenced: []
---

This page collects the vocabulary, commands, and keyboard shortcuts that are worth committing to muscle memory. Keep it open in a browser tab (or printed beside your keyboard) during your first few weeks with Claude Code. Most of the friction new users hit comes from not knowing a command already exists for what they are trying to do, so a quick scan here before reaching for a workaround usually pays off. | Term | Definition | | --- | --- | | Session | One run of `claude` in a directory, from launch to exit. Each session has its own conversation history, while project memory (`CLAUDE.md`) persists across sessions. | | Context window | The total amount of text — your prompts, Claude's replies, and any files it has read — that the model can hold in mind at once. When it fills up, older content is compacted or dropped. It is managed with `/clear` and `/compact`. | | Token | The unit models use to measure text (roughly ¾ of a word). Usage limits and API billing are counted in tokens. You will mostly encounter this via `/cost` or the context indicator. | | CLAUDE.md | A markdown file (project root, home directory, or subfolder) that Claude reads automatically at the start of every session. It holds your project's conventions, commands, and constraints so you do not have to repeat them.
