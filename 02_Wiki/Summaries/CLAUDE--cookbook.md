---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/CLAUDE.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/CLAUDE.md
title: "Claude Cookbooks — root CLAUDE.md (Claude Code project guide)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command]
concepts_referenced: []
---

Repository-level Claude Code project guide for `claude-cookbooks`.

**Quick start.** `uv sync --all-extras`, `uv run pre-commit install`, copy `.env.example` to `.env` with the API key.

**Development commands.** `make format`, `make lint`, `make check` (format-check + lint), `make fix` (auto-fix + format), `make test` (pytest). Or directly via `uv run ruff format .` / `uv run ruff check .` / `uv run ruff check --fix .` / `uv run pre-commit run --all-files`.

**Code style.** 100-char line length, double quotes, ruff formatter. Notebooks have relaxed rules (E402 mid-file imports, F811 redefinitions, N803/N806 variable naming).

**Git workflow.** Branch `<username>/<feature-description>`. Conventional commit format.

**Key rules:**

1. **API keys.** Never commit `.env`. Use `dotenv.load_dotenv()` then `os.environ` / `os.getenv()`.
2. **Dependencies.** Use `uv add <package>` or `uv add --dev <package>`. Never edit `pyproject.toml` directly.
3. **Models.** Use current Claude models. Sonnet `claude-sonnet-4-6`, Haiku `claude-haiku-4-5`, Opus `claude-opus-4-6`. Never use dated model IDs like `claude-sonnet-4-6-20250514` — always the non-dated alias. **Bedrock model IDs use a different format**: e.g., `anthropic.claude-opus-4-6-v1`, `anthropic.claude-sonnet-4-5-20250929-v1:0`, `anthropic.claude-haiku-4-5-20251001-v1:0`. Prepend `global.` for global endpoints (recommended). Note: Bedrock models before Opus 4.6 require dated IDs in their Bedrock model ID.
4. **Notebooks.** Keep outputs (intentional for demonstration). One concept per notebook. Test top-to-bottom.
5. **Quality checks.** Run `make check` before committing. Pre-commit hooks validate formatting and notebook structure.

**Slash commands** (Claude Code + CI): `/notebook-review`, `/model-check`, `/link-review`.

**Project structure.** `capabilities/` (RAG, classification, etc.), `skills/`, `tool_use/`, `multimodal/`, `misc/` (batch, caching, utilities), `third_party/` (Pinecone, Voyage, Wikipedia), `extended_thinking/`, `scripts/` (validation), `.claude/` (Claude Code commands and skills).

**Adding a new cookbook.** Create notebook in the appropriate directory; add entry to `registry.yaml` with title/description/path/authors/categories; add author info to `authors.yaml` if new; run quality checks; submit PR.
