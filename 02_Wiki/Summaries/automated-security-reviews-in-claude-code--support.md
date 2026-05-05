---
type: summary
source: 01_Raw/support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code.md
source_url: https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code
title: "Automated Security Reviews in Claude Code"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, CI-integration]
concepts_referenced: []
---

Claude Code now includes automated security review features to help you identify and fix vulnerabilities in your code. This guide explains how to use the /security-review command and GitHub Actions to improve your code security.

Note: While automated security reviews help identify many common vulnerabilities, they should complement, not replace, your existing security practices and manual code reviews.

Automated security reviews in Claude Code help developers catch vulnerabilities before they reach production. These features check for common security issues including SQL injection risks, cross-site scripting (XSS) vulnerabilities, authentication flaws, insecure data handling, and dependency vulnerabilities.

Covers: Overview; Availability; Using the /security-review command; Running a Security Review; Implementing Fixes; Customizing the Command; Setting up GitHub Actions for automated PR reviews; Installation.
