---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/CONTRIBUTING.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/CONTRIBUTING.md
title: "Claude Cookbooks — CONTRIBUTING"
summarized_at: 2026-05-05
entities_referenced: [Slash-command]
concepts_referenced: []
---

Contributor guide for the `claude-cookbooks` repo.

**Setup.** Python 3.11+, `uv` package manager (recommended). Steps: install `uv`, clone the repo, `uv sync --all-extras` (or `pip install -e ".[dev]"`), `uv run pre-commit install`, `cp .env.example .env` and add the API key.

**Quality stack.** `nbconvert` for notebook execution, `ruff` for lint/format with native Jupyter support, plus a Claude AI Review step. Notebook outputs are intentionally kept in the repo because they demonstrate expected results to readers.

**Slash commands (work in Claude Code locally and in GitHub Actions CI).** `/link-review` validates links, `/model-check` verifies Claude model usage is current, `/notebook-review` does a comprehensive notebook quality check. The same definitions live under `.claude/commands/` for both local and CI use.

**Before committing.** Run `uv run ruff check skills/ --fix`, `uv run ruff format skills/`, then `uv run python scripts/validate_notebooks.py`. Optionally test execution with `uv run jupyter nbconvert --to notebook --execute skills/.../guide.ipynb ...`. Pre-commit hooks auto-format with ruff and validate notebook structure.

**Notebook best practices.** Always read API keys via `os.environ.get("ANTHROPIC_API_KEY")`. Use current Claude models — model aliases preferred for maintainability; latest Haiku is `claude-haiku-4-5`; Claude validates model usage in PR reviews. Keep notebooks focused (one concept), with explanations and expected outputs as markdown cells. Test top-to-bottom, use minimal tokens, include error handling.

**Git workflow.** Branch naming `<your-name>/<feature-description>`. Conventional commits (`feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ci`). Atomic commits, one logical change each. Push with `-u` and create PR via `gh pr create` or web UI.

**PR guidelines.** Conventional commit title. Body includes what/why/how-to-test/related-issue. One feature/fix per PR. Respond to feedback promptly.

**Testing.** Local: `uv run python scripts/validate_notebooks.py` and `uv run pre-commit run --all-files`. CI auto-runs notebook structure validation, ruff lint, link checks, Claude model-usage review; for maintainers, full notebook execution. External contributors get limited API testing to conserve resources.

**Security.** Never commit API keys/secrets. Use environment variables. Report security issues to security@anthropic.com.

**License.** Contributions are MIT-licensed.
