---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/skills/custom_skills/creating-financial-models/SKILL.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/skills/custom_skills/creating-financial-models/SKILL.md
title: "Claude Cookbooks — creating-financial-models custom SKILL"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Custom skill providing an advanced financial-modeling suite for investment analysis, valuation, and risk assessment using industry-standard methodologies.

**Frontmatter.** `name: creating-financial-models`, `description: This skill provides an advanced financial modeling suite with DCF analysis, sensitivity testing, Monte Carlo simulations, and scenario planning for investment decisions`.

**Core capabilities.**

1. **Discounted Cash Flow (DCF) Analysis.** Build complete DCF models with multiple growth scenarios; terminal values via perpetuity growth and exit-multiple methods; weighted average cost of capital (WACC); enterprise and equity valuations.
2. **Sensitivity Analysis.** Test key-assumption impact on valuation; data tables for multiple variables; tornado charts for sensitivity ranking; identify critical value drivers.
3. **Monte Carlo Simulation.** Run thousands of scenarios with probability distributions; model uncertainty in inputs; generate confidence intervals for valuations; calculate probability of achieving targets.
4. **Scenario Planning.** Build best/base/worst case scenarios; model different economic environments; test strategic alternatives; compare outcome probabilities.

**Input requirements.**

- **DCF.** Historical financial statements (3–5 years); revenue growth assumptions; operating margin projections; capital expenditure forecasts; working capital requirements; terminal growth rate or exit multiple; discount rate components (risk-free rate, beta, market premium).
- **Sensitivity.** Base-case model; variable ranges to test; key metrics to track.
- **Monte Carlo.** Probability distributions for uncertain variables; correlation assumptions; iteration count (typically 1,000–10,000).
- **Scenario planning.** Scenario definitions and assumptions; probability weights; KPIs to track.

The file continues with output formats (Excel models with formulas, sensitivity tables, charts), example invocations, scripts, best practices, and limitations — all in service of demonstrating a more sophisticated finance-domain custom skill in **Notebook 3: Custom Skills Development** of the Skills cookbook.
