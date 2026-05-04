# Canonical Names — Entity Registry + 错别字勘误表

> **enrich / 写 summary 前必读** —— 这是 vault 的单一事实源。
> Raw 文档里同一概念可能有多个写法，vault 内统一用 canonical 名，aliases 在每个 entity 的 frontmatter。
>
> 新发现 raw 里有不一致写法 → 在这里登记 → entity frontmatter `aliases:` 加上变体 → 再 enrich。

---

## 命名约定

- 多词 entity 用 `Hyphen-Joined` (`MCP-server`, `Slash-command`, `Agent-SDK`, `Status-line`)
- entity frontmatter `aliases:` 列所有变体（含 raw 中的错别字 / 单复数 / 连字符差异 / 大小写差异）
- summary frontmatter `entities_referenced:` / `concepts_referenced:` 字段**必须用 canonical 名**
- 不确定时 `ls 02_Wiki/Entities/ 02_Wiki/Concepts/` 先看真实存在的文件

---

## P1 Entity Registry（25 entities + 4 concepts）

### Entities (`02_Wiki/Entities/`)

**核心 features**

| Canonical | Raw 中常见变体 |
|---|---|
| Hooks | hook / hook system / session hooks |
| Skill | skills / Anthropic Skill / agent skill |
| Plugin | Claude Code plugin / claude-plugin |
| Subagent | sub-agent / sub agent / subagents / Sub-agent |
| Slash-command | slash command / slash-command / /command |
| MCP-server | MCP / Model Context Protocol server / MCP 服务器 |
| Output-style | output style / output styles |
| Status-line | statusline / status line |
| Memory | memory system / Claude Code memory |
| Checkpointing | checkpoint / file checkpoints |
| Settings | settings.json / user settings / project settings |
| Plugin-marketplace | plugin marketplace / marketplace |

**执行模式 / config**

| Canonical | 变体 |
|---|---|
| Permission-mode | permission mode / permission modes |
| Sandboxing | sandbox / Claude Code sandbox |
| Auto-mode | auto mode / auto-mode-config |
| Fast-mode | fast mode |
| Headless-mode | headless / headless mode / non-interactive |
| Computer-use | computer use / computer-use tool |
| Routine | routines / scheduled routine（云端 cron） |
| Scheduled-task | scheduled task / scheduled tasks（桌面端定时） |

**集成 / 接口**

| Canonical | 包含 |
|---|---|
| Agent-SDK | claude-agent-sdk / agent-sdk / Claude Agent SDK |
| IDE-integration | VS Code / JetBrains / Chrome 扩展 |
| Native-interface | CLI / Desktop / Web / Slack |
| CI-integration | GitHub Actions / GitLab CI/CD |
| Enterprise-gateway | Amazon Bedrock / Google Vertex AI / Microsoft Foundry / LLM Gateway |

### Concepts (`02_Wiki/Concepts/`)

| Canonical | 变体 |
|---|---|
| Agentic-loop | agent loop / agentic loop / tool use loop |
| Context-window | context window / 上下文窗口 |
| Channel | channels / Claude Code channels |
| Agent-team | agent teams / subagent team |

---

## 跨产品概念（不属于 Claude Code，但 raw 里频繁出现）

| Canonical | 变体 / 备注 |
|---|---|
| Tool-use | Function calling（其他 vendor 术语，Anthropic docs 偶尔混用） |
| Extended-thinking | extended-thinking / thinking mode / interleaved thinking（thinking mode 偶指别的） |
| Prompt-caching | prompt cache / cache control / cached prompts |

> 这些将来 P2/P3 enrich Anthropic API docs 时建对应 entity；P1 阶段如 summary 提到，写到 `entities_referenced` 但**不要** create stub。

---

## Model 名字

| Canonical | model ID |
|---|---|
| Opus 4.7 | claude-opus-4-7 |
| Sonnet 4.6 | claude-sonnet-4-6 |
| Haiku 4.5 | claude-haiku-4-5-20251001 |
| Opus 4.6 | claude-opus-4-6（Fast mode 用此 model） |

---

## 维护规则

1. 发现新变体 → 加到对应 canonical 行的"变体"列
2. 发现完全新概念 → 在合适 section 加新行
3. 不确定哪个是 canonical → 先问用户
4. **不要**因为 raw 里某个写法出现得多就改 canonical —— canonical 是设计选择，跟出现频次无关
