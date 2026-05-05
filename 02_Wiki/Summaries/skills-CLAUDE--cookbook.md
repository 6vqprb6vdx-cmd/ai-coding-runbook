---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/skills/CLAUDE.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/skills/CLAUDE.md
title: "Claude Cookbooks — skills/CLAUDE.md (Claude Code project guide)"
summarized_at: 2026-05-05
entities_referenced: [Skill, Files-API, Code-execution-tool, Anthropic-SDK-Python]
concepts_referenced: []
---

Claude Code project guide for the Skills cookbook subdirectory. Three progressive Jupyter notebooks demonstrating Claude's Skills feature for document generation (Excel, PowerPoint, PDF).

**Quick start.** `python -m venv venv` and activate. `pip install -r requirements.txt` (must use local whl for Skills support). `cp .env.example .env` and add API key. `jupyter notebook` (or VSCode with Jupyter extension; ensure venv kernel is selected).

**Testing & verification.** `python -c "import anthropic; print(f'SDK Version: {anthropic.__version__}')"`. Check `outputs/` for generated files.

**Architecture.** Directory structure: `notebooks/` (3 progressive Jupyter notebooks), `sample_data/`, `custom_skills/`, `outputs/`, `file_utils.py` (Files API helper functions), `docs/`.

**Key technical details.**

- **Beta API.** All Skills functionality uses `client.beta.*`. Required beta headers: `code-execution-2025-08-25`, `files-api-2025-04-14`, `skills-2025-10-02`. Use `client.beta.messages.create()` with `container` parameter. The code-execution tool (`code_execution_20250825`) is REQUIRED. Use pre-built Agent skills via `skill_id` or upload your own via the Skills API.
- **Files API.** Skills generate files and return `file_id` attributes. Use `client.beta.files.download()` to download, `client.beta.files.retrieve_metadata()` for metadata. Helper functions in `file_utils.py` handle extraction and download.
- **Built-in skills.** `xlsx`, `pptx`, `pdf`, `docx`.

**Development gotchas (numbered list of subtle pitfalls):**

1. **SDK version.** Need anthropic SDK 0.71.0+. Restart Jupyter kernel after upgrading.
2. **Beta namespace required.** Use `client.beta.messages.create()` and `client.beta.files.*` — non-beta versions fail.
3. **Beta headers placement.** Setting Skills beta in `default_headers` requires `code_execution` on ALL requests. Use the per-request `betas=[...]` parameter instead.
4. **File ID extraction.** Response structure differs from standard Messages — file IDs are nested at `bash_code_execution_tool_result.content.content[0].file_id`. Use `file_utils.extract_file_ids()`.
5. **Files API response objects.** Use `.read()` for binary content (not `.content`) and `.size_bytes` for size (not `.size`). Metadata fields: id, filename, size_bytes, mime_type, created_at, type, downloadable.
6. **Jupyter kernel.** Always pick the venv kernel.
7. **Module reload.** Restart kernel or `importlib.reload(file_utils)` to pick up changes.
8. **Document generation times.** Excel ~2 minutes, PowerPoint ~1–2 minutes, PDF ~1–2 minutes. Document this expectation in markdown above generation cells so users don't think the cell is frozen.

**Common tasks.** Adding a new notebook section (follow Notebook 1 structure, include setup with imports/beta headers, show API call/response handling/file download, error handling, update `docs/skills_cookbook_plan.md`). Creating sample data (CSV for tabular, JSON for structured, <100KB). Testing file download (run cell, check `file_id`, use `download_all_files()`, verify in `outputs/`, open in native app).

**Project-specific notes.** Focus domain: finance & analytics. Audience: intermediate developers and business analysts. Notebook 1 complete; 2 and 3 WIP.

**Required env vars.** `ANTHROPIC_API_KEY`. Optional `ANTHROPIC_BASE_URL` for proxies.
