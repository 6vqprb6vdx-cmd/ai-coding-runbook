---
type: summary
source: 01_Raw/support.claude.com/en/articles/14503613-sso-login.md
source_url: https://support.claude.com/en/articles/14503613-sso-login
title: "SSO Login"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Claude for Government requires Single Sign-on (SSO) for user authentication. Unlike the commercial Claude Enterprise plan, email based (magic link) login is only available to the Primary Owner during account setup. All other users must authenticate through your organization's identity provider (IdP).

Once SSO is configured, the Primary Owner can disable magic link login entirely so that all authentication flows through your IdP.

For SSO setup on Claude Enterprise, see Set up single sign-on (SSO).

| Feature | Claude for Government | Claude Enterprise | | --- | --- | --- | | Email (magic link) login | Primary Owner only, during initial setup | Available to all users | | SSO Requirement | Required for all non-Primary Owner users | Optional |

Covers: How SSO differs for Claude for Government; Steps for setting up SSO; Prerequisites; Step 1: Sign in as Primary Owner; Step 2: Verify your domain; Step 3: Configure your Identity Provider; Step 4: Configure Anthropic with your IdP details; Step 5: Test and finalize.
