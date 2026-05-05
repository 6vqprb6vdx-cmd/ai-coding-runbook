---
type: summary
source: 01_Raw/support.claude.com/en/articles/8243635-our-approach-to-rate-limits-for-the-claude-api.md
source_url: https://support.claude.com/en/articles/8243635-our-approach-to-rate-limits-for-the-claude-api
title: "Our Approach to Rate Limits for the Claude API"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Your rate limit depends on your usage tier, and is currently measured in three key metrics:

If you exceed any of these rate limits, you will get a 429 error describing which rate limit was exceeded, along with a `retry-after` header indicating how long to wait.

Rate limits are set at the organization level and are defined by usage tiers. Each tier has different spend and rate limits, with automatic tier advancement based on usage thresholds up to Tier 4.

You can view your organization's current tier and limits in the Claude Console.
