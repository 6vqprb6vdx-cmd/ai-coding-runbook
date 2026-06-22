---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-CN
fetched_at: 2026-06-22T06:30:17.525617+00:00
title: "\u4f7f\u7528 Gemini MCP \u548c\u6280\u80fd\u8bbe\u7f6e\u7f16\u7801\u52a9\u7406 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 Gemini MCP 和技能设置编码助理

AI 编码助理功能强大，但也有局限性 - 训练数据在特定日期截止，无法获取新的 API 功能和更改。如果无法访问 Gemini 专用文档，代理可能会建议通用模式，而不是优化方法。

为了让您的编码助理能够及时了解不断发展的 Gemini API 及其推荐用法，我们建议您设置 **Gemini 文档 MCP** 并通过 **Gemini API 技能**增强您的环境。虽然这些工具可以单独使用，但它们旨在协同工作，以提供全面的覆盖范围。

## 连接 Gemini 文档 MCP

Gemini 在 `https://gemini-api-docs-mcp.dev` 上托管了一个公共 Model Context Protocol (MCP) 服务器。将编码代理连接到此服务器可确保所有查询都能访问最新的 API、代码更新和最佳配置示例。

在代理的终端或项目根目录中运行以下命令，以安装服务器：

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

此服务器添加了一个 `search_documentation` 函数，您的代理可以使用该函数从官方 Gemini 文档文件中检索实时 API 定义和集成模式。

## 添加 API 开发技能

技能可直接在助理的上下文中提供**内置规则和最佳实践**（例如强制执行正确的 SDK 和当前模型版本）。该技能可与 Gemini Docs MCP 服务搭配使用：如果您同时安装了这两者，该技能会使用 MCP 服务来获取文档；但即使没有安装 MCP，它也会从 `ai.google.dev` 中提取 `llms.txt` 作为后备方案。

如需安装这些技能，您可以使用以下任一受支持的工具。下面提供了每个技能模块的安装说明：

- **[skills.sh](https://skills.sh)**：推荐。用于实现可移植的代理行为的开放标准。
- **[Context7](https://context7.com)**：支持已在使用 Context7 生态系统的用户。

### gemini-api-dev

用于开发通用 Gemini 应用的基础技能。此技能提供以下方面的文档和最佳实践：

- 将提示路由到当前模型（例如 Gemini 3.1 Pro/Flash），并避免使用已弃用的模型
- 多模态提示、函数调用、结构化输出和常见集成模式

#### 使用 skills.sh 进行安装

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### 通过 Context7 安装

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

技能：使用 Gemini Live API 构建实时对话式 AI 应用。此技能提供以下方面的文档和最佳实践：

- 用于低延迟流式传输的 WebSocket 连接
- 流式音频、视频和文本
- 语音活动检测和抢占支持

#### 使用 skills.sh 进行安装

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### 通过 Context7 安装

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

使用 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-cn) 构建应用的技能。Interactions API 是一个用于与 Gemini 模型和代理互动的统一接口，专为代理应用而设计。此技能涵盖以下内容：

- 文本生成、多轮对话和流式传输
- 函数调用、结构化输出和图片生成
- 后台执行和深度研究智能体
- 服务器端对话状态管理
- Python 和 TypeScript SDK 模式

#### 使用 skills.sh 进行安装

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### 通过 Context7 安装

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## 验证安装

安装完成后，请确认您的编码助理可以连接到 Gemini Docs MCP 服务器并使用您安装的技能。

### 1. 验证代理行为

最可靠的验证方式是向您的代理提出有关 Gemini API 的技术问题。

**提示**：“如何使用 Gemini API 进行上下文缓存？”

成功设置后，系统将：

- **提供准确的代码**：引用最新端点中的特定 Gemini 方法，例如 `cacheContent` 或 `cachedContents.create`。
- **使用 MCP 工具**：表明已连接到 **Gemini Docs MCP 服务器**或正在使用 `search_documentation` 工具来提取数据。
- **调用已加载的技能**：显示“正在使用技能：gemini-api-dev”（如果依赖于辅助封装容器）。

### 2. 验证清单和工具

如果代理给出的回答是常规回答或泛泛而谈，请使用适用于您环境的特定 Discovery 或 Status 命令来验证 Docs MCP 或技能是否已加载到内存中。

| 环境 | MCP 验证 | 技能验证 |
| --- | --- | --- |
| **Claude Code** | 在终端中输入 `/mcp`，以查看活跃服务器和 `search_documentation` 工具。 | 在终端中输入 `/skills`，列出所有有效清单。 |
| **Cursor** | 依次前往**设置 > 功能 > MCP**。确保服务器处于“已连接”状态。 | 依次打开**“设置”>“规则”**。验证该技能是否显示在“代理决定”下。 |
| **Antigravity** | 在**自定义 > 连接** 边栏中查看 MCP 状态。 | 输入 `/skills list` 或查看**自定义 > 规则**边栏。 |
| **Gemini CLI** | 运行 `gemini mcp list` 或使用 `/mcp list`。 | 运行 `gemini skills list` 或在对话期间使用 `/skills` 斜杠命令。 |
| **Copilot** | 输入 `@gemini /mcp` 可列出有效的数据连接器。 | 输入 `@gemini /skills`（或 `/skills`）可查看有效扩展程序。 |

## 问题排查

如果您的代理仅提供一般信息或无法识别 Gemini 特有的方法，请检查以下内容：

### 代理未发现技能

大多数代理仅在启动时对技能进行索引。

**修复**：完全重启 IDE（Cursor/VS Code），或退出并重新打开基于终端的代理（Claude Code）。

### 全球冲突与局部冲突

如果您使用 `--global` 标志进行安装，则代理可能会忽略该标志，而采用项目专用规则。

**修复**：尝试直接将技能安装到项目根目录中，而不使用全局标志：

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## 资源

- [GitHub 上的 Gemini API 技能](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-cn)
- [快速入门](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-cn)
- [库](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn)

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-19。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-19。"],[],[]]
