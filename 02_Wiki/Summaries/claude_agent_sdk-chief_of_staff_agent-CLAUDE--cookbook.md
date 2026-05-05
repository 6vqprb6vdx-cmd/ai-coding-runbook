---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/claude_agent_sdk/chief_of_staff_agent/CLAUDE.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/chief_of_staff_agent/CLAUDE.md
title: "Claude Cookbooks — chief_of_staff_agent CLAUDE.md (fixture data)"
summarized_at: 2026-05-05
entities_referenced: [Memory, Subagent]
concepts_referenced: []
---

Per-project CLAUDE.md used as the persistent context file for the Chief of Staff demo agent in the Claude Agent SDK tutorial series. It is a fictional company snapshot the agent reads as background knowledge.

**Company.** TechStart Inc — Series A B2B SaaS for AI-powered developer tools, founded 2022, HQ San Francisco. Closed $10M in January 2024.

**Financials.** $500K monthly burn, 20-month runway (until September 2025), $2.4M ARR (15% MoM growth), $10M cash, $48K revenue/employee.

**Team (50 headcount).** Engineering 25 (12 backend / 8 frontend / 5 DevOps-SRE), Sales & Marketing 12, Product 5, Operations 5, Executive 3.

**Key metrics.** 120 enterprise customers, NPS 72, 2.5% monthly churn, $15K CAC, $85K LTV, 10-month CAC payback.

**Q2 2024 priorities.** Hire 10 engineers, launch AI code-review feature by end of Q2, expand into European market, begin Series B conversations targeting $30M.

**Compensation benchmarks.** Senior Engineer $180–220K + 0.1–0.3% equity; Junior $100–130K + 0.05–0.1%; EM $200–250K + 0.3–0.5%; VP Eng $250–300K + 0.5–1%.

**Board.** CEO Sarah Chen (Founder), Mark Williams (Sequoia), Jennifer Park (a16z), Independent Michael Torres (former CTO of GitHub).

**Competitive landscape.** Main competitors: DevTools AI, CodeAssist Pro, SmartDev Inc. Differentiation: superior AI accuracy, 10× faster processing. $5B market growing 25% annually.

**Recent decisions.** Approved hiring 3 senior backend engineers (March 2024), launched freemium tier (February), opened European entity (January), closed Series A (January).

**Upcoming decisions.** Whether to acquire SmartDev Inc ($8M asking), Q3 hiring plan (engineering vs sales focus), office expansion vs remote-first, stock option refresh for early employees.

**Risk factors.** High AWS dependency (70% of COGS), key engineer retention (3 critical members), Big Tech competition, economic-downturn impact on enterprise sales.

**Available scripts.** `scripts/simple_calculation.py <total_runway> <monthly_burn>` — quick financial-metrics calculator. Returns JSON with monthly_burn, runway_months, total_runway_dollars, quarterly_burn, burn_rate_daily.

The closing line reminds the agent it has access to financial data in `financial_data/` and can delegate to subagents (financial-analyst, recruiter). Functionally this CLAUDE.md doubles as both demo data and the system context loaded at every Chief of Staff session start.
