---
type: summary
source: 01_Raw/support.claude.com/en/articles/14729294-open-claude-desktop-with-a-link.md
source_url: https://support.claude.com/en/articles/14729294-open-claude-desktop-with-a-link
title: "Open Claude Desktop with a Link"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Claude for macOS and Windows respond to the `claude://` URL scheme, much like a browser responds to the `https://` scheme. You can use these links from a website, a script, or another app to open Claude Desktop and jump straight to a chat, a Cowork session, or a Code session.

This article lists the link formats Claude Desktop supports and the parameters each one accepts.

When your operating system opens a `claude://` URL, it hands the URL to Claude. If the app isn't running, both macOS and Windows will launch it first. Claude then reads the path and query parameters and navigates to the right place inside the app.

Covers: How deep links work; Start a new chat; Open an existing chat or project; Start a Claude Code session; Start a Claude Cowork session; Test a deep link; On macOS; On Windows.
