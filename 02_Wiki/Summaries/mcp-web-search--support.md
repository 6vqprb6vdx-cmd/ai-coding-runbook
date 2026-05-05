---
type: summary
source: 01_Raw/support.claude.com/en/articles/14503775-mcp-web-search.md
source_url: https://support.claude.com/en/articles/14503775-mcp-web-search
title: "MCP Web Search"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

The Web Search connector gives Claude the ability to search the public internet for real-time information, including verifying facts, pulling recent news, and researching topics outside its training data.

For questions about web search in commercial Claude, see Enabling and using web search.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2256120763/7652c6c669446113eae75f3c5977/9c74d57e-aaa2-4f1c-bfe4-2b9b87fd41ab?expires=1777916700&amp;signature=0b4e69fd93b4d17d3e47f9571176470edf94ca8b972c81d4b3ff8f165274e339&amp;req=diIiEMh8nYZZWvMW1HO4zQvFI7VajML%2FM%2Fw5SJgC29GngH7WJ0rJnKVfV9Ak%0AWq4Lqjm7l3Rpf1zd1ZU%3D%0A)

In commercial Claude, web search is a built-in capability. In Claude for Government, native web search is disabled. The Web Search MCP connector replaces it, providing the same capability with additional transparency and control appropriate for a FedRAMP environment.

Important: The Web Search connector runs inside Claude for Government's FedRAMP High boundary, but it calls the Brave Search API, which is outside that boundary. When you approve a search, the query string — and only the query string — is transmitted to Brave. No conversation history, user identity, organization identity, or attached files are sent.

Covers: How Web Search differs for Claude for Government; Approve each search before it runs; Set up the Web Search connector; Owners and Primary Owners; For individual users; Example use cases; Frequently asked questions; Does any of my conversation data get sent to Brave?.
