---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/skills/custom_skills/analyzing-financial-statements/SKILL.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/skills/custom_skills/analyzing-financial-statements/SKILL.md
title: "Claude Cookbooks — analyzing-financial-statements custom SKILL"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Custom skill from the Claude Cookbooks `skills/custom_skills/` directory.

**Frontmatter.** `name: analyzing-financial-statements`, `description: This skill calculates key financial ratios and metrics from financial statement data for investment analysis`.

**Capabilities.** Calculate and interpret a comprehensive ratio set:

- **Profitability Ratios** — ROE, ROA, Gross Margin, Operating Margin, Net Margin
- **Liquidity Ratios** — Current Ratio, Quick Ratio, Cash Ratio
- **Leverage Ratios** — Debt-to-Equity, Interest Coverage, Debt Service Coverage
- **Efficiency Ratios** — Asset Turnover, Inventory Turnover, Receivables Turnover
- **Valuation Ratios** — P/E, P/B, P/S, EV/EBITDA, PEG
- **Per-Share Metrics** — EPS, Book Value per Share, Dividend per Share

**How to use.** Provide financial statement data (income statement, balance sheet, cash flow); specify which ratios to calculate or use "all"; the skill calculates them and provides industry-standard interpretation.

**Input format.** CSV with line items, JSON with structured financial statements, plain text description of key figures, or Excel files.

**Output format.** Calculated ratios with values, industry benchmark comparisons (when available), trend analysis (if multiple periods), interpretation and insights, Excel report with formatted results.

**Example usage.** "Calculate key financial ratios for this company based on the attached financial statements"; "What's the P/E ratio if the stock price is $50 and annual earnings are $2.50 per share?"; "Analyze the liquidity position using the balance sheet data."

**Scripts.** `calculate_ratios.py` (main calculation engine), `interpret_ratios.py` (interpretation and benchmarking).

**Best practices.** Validate data completeness; handle missing values appropriately (industry averages or exclude); consider industry context when interpreting; include period comparisons for trend analysis; flag unusual or concerning ratios.

**Limitations.** Requires accurate financial data; industry benchmarks are general guidelines; some ratios don't apply to all industries; historical data doesn't guarantee future performance.
