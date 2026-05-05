---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/skills/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/skills/README.md
title: "Claude Cookbooks — skills/ README"
summarized_at: 2026-05-05
entities_referenced: [Skill, Skill-API, Files-API, Code-execution-tool]
concepts_referenced: []
---

Comprehensive guide to using Claude's Skills feature for document generation, data analysis, and business automation. Demonstrates Claude's built-in skills for Excel, PowerPoint, and PDF, and how to build custom skills.

**What are Skills.** Organized packages of instructions, executable code, and resources that give Claude specialized capabilities for specific tasks. Loaded dynamically. Use cases: professional documents (Excel, PowerPoint, PDF, Word), complex data analysis and visualization, company-specific workflows and branding, business-process automation.

**Cookbook structure (3 notebooks):**

- **Notebook 1 — Introduction to Skills.** Skills architecture, beta headers, first Excel spreadsheet, PowerPoint, PDF.
- **Notebook 2 — Financial Applications.** Financial dashboards with charts and pivot tables, portfolio analysis and investment reporting, cross-format workflows (CSV → Excel → PowerPoint → PDF), token optimization.
- **Notebook 3 — Custom Skills Development.** Financial ratio calculator, company brand guidelines skill, financial modeling suite, best practices and security.

**Quick start.** Python 3.8+, Claude API key, Jupyter. Clone the repo, `cd claude-cookbooks/skills`, create venv, `pip install -r requirements.txt`, copy `.env.example` to `.env`, `jupyter notebook`, open Notebook 1.

**Sample data** in `sample_data/`: `financial_statements.csv`, `portfolio_holdings.json`, `budget_template.csv`, `quarterly_metrics.json`.

**API configuration.** Skills require beta headers: `code-execution-2025-08-25`, `files-api-2025-04-14`, `skills-2025-10-02`. Notebooks set them via `default_headers={"anthropic-beta": "..."}`.

**Working with generated files.** Skills create files during code execution, response includes `file_id` for each, use the Files API to download, then save locally. Example flow: `client.messages.create(... container={"skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]}, tools=[{"type": "code_execution_20250825", ...}], ...)` → extract `file_id` from tool result blocks → `client.beta.files.download(file_id=file_id)` → write `.read()` output to disk. Files API methods include `.download()`, `.retrieve_metadata()` (use `size_bytes`), `.list()`, `.delete()`. Files are temporarily stored on Anthropic servers and overwritten by default on rerun.

**Built-in skills.** `xlsx` (Excel), `pptx` (PowerPoint), `pdf` (PDF), `docx` (Word).

**Custom skill structure.** `my_skill/SKILL.md` (required), optional `scripts/` (Python/JS code), optional `resources/` (templates, data).

**Common use cases.** Financial reporting (quarterly reports, budget variance, dashboards), data analysis (Excel analytics, pivot tables, statistical visualization), document automation (branded presentations, multi-source report compilation, cross-format conversion).

**Performance tips.** Progressive disclosure (skills load in stages to minimize tokens), batch operations in a single conversation, skill composition for complex workflows, container ID reuse for cached loaded skills.

**Troubleshooting.** Missing API key (set `.env`), missing beta header (ensure correct headers in notebooks), token limit exceeded (chunk operations, leverage progressive disclosure).

References Anthropic's "Equipping agents for the real world with Skills" engineering blog post and the "Claude Creates Files" announcement showing the same Skills powering documents in Claude.ai and the desktop app.
