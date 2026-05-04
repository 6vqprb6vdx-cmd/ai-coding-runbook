# Canonical Names — 错别字 / 多名同实勘误表

> **enrich 前必读** —— 这是 vault 的单一事实源。raw 文档里同一概念可能有多个写法，vault 内统一用 canonical 名，aliases 写在每个 entity 的 frontmatter。
>
> 新发现 raw 里有不一致写法 → 先在这里登记 → 在对应 entity 的 frontmatter `aliases:` 加上变体 → 再 enrich。

---

## 命名约定

- Vault 内文件名 / wikilink / entity name 字段 → 用 canonical 名
- entity frontmatter `aliases:` 字段列出所有变体（含错别字、单复数、连字符差异、大小写差异）

---

## Anthropic 同概念多写法

| Canonical（vault 用） | 变体（raw 出现） | 备注 |
|---|---|---|
| Subagent | Sub-agent / sub-agent / Sub agent / subagents | Anthropic 文档里至少 3 种写法 |
| Slash command | slash-command / Slash Command / SlashCommand | |
| Tool use | Function calling | function calling 是其他 vendor 的术语，Anthropic 自己的 docs 偶尔混用 |
| MCP server | MCP / Model Context Protocol server | MCP = Model Context Protocol，server 是其中一种 role |
| Skill | skills / Anthropic Skill | 注意 vs 单数复数 |
| Hook | hooks / Hook system | |
| Plugin | Claude Code plugin / claude-plugin | |
| Extended thinking | extended-thinking / thinking mode / interleaved thinking | 注意 thinking mode 有时指别的 |
| Prompt caching | prompt cache / cache control / cached prompts | |
| Computer use | computer-use / Computer-use tool | |
| Agent SDK | claude-agent-sdk / agent-sdk | |
| Claude Code SDK | claude-code-sdk | |

---

## 历史错别字 / 实例修正

（暂无——等 ingest 后逐步发现登记）

---

## Model 名字

| Canonical | 变体 / model ID |
|---|---|
| Opus 4.7 | claude-opus-4-7 / claude-opus-4.7 |
| Sonnet 4.6 | claude-sonnet-4-6 |
| Haiku 4.5 | claude-haiku-4-5 / claude-haiku-4-5-20251001 |
| Opus 4 | claude-opus-4-20250514 |
| Sonnet 3.7 | claude-3-7-sonnet-20250219 |

---

## 维护规则

1. 发现新变体 → 加到对应 canonical 行的"变体"列
2. 发现完全新概念 → 在合适的 section 加新行
3. 不确定哪个是 canonical → 先问用户
4. **不要**因为 raw 里某个写法出现得多就改 canonical —— canonical 是设计选择，跟出现频次无关
