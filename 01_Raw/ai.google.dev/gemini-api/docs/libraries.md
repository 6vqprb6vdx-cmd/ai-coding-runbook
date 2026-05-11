---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=zh-CN
fetched_at: 2026-05-11T12:35:54.322484+00:00
title: "Gemini API \u5e93 \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini API 库

使用 Gemini API 进行构建时，我们建议使用 **Google GenAI SDK** 。
这些是我们为最常用的语言开发和维护的官方可用于生产用途库。它们处于[正式版](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn#new-libraries)状态，并用于我们的所有官方
文档和示例。

如果您是 Gemini API 的新手，请按照我们的 [快速入门指南](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-cn) 开始使用。

## 语言支持和安装

Google GenAI SDK 支持 Python、JavaScript/TypeScript、Go 和 Java 语言。您可以使用软件包管理器安装每种语言的库，也可以访问其 GitHub 代码库以进行进一步互动：

### Python

- 库： [`google-genai`](https://pypi.org/project/google-genai)
- GitHub 代码库：[googleapis/python-genai](https://github.com/googleapis/python-genai)
- 安装：`pip install google-genai`

### JavaScript

- 库： [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- GitHub 代码库：[googleapis/js-genai](https://github.com/googleapis/js-genai)
- 安装：`npm install @google/genai`

### Go

- 库： [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- GitHub 代码库：[googleapis/go-genai](https://github.com/googleapis/go-genai)
- 安装：`go get google.golang.org/genai`

### Java

- 库：`google-genai`
- GitHub 代码库：[googleapis/java-genai](https://github.com/googleapis/java-genai)
- 安装：如果您使用的是 Maven，请将以下代码添加到您的依赖项中：

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

- 库：`Google.GenAI`
- GitHub 代码库：[googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- 安装：`dotnet add package Google.GenAI`

## 正式版

截至 2025 年 5 月，Google GenAI SDK 已在所有受支持的平台上达到正式版 (GA) 状态，是访问 Gemini API 的推荐库。
它们稳定可靠，完全支持在生产环境中使用，并且会积极维护。
它们提供对最新功能的访问权限，并提供与 Gemini 配合使用的最佳性能。

如果您使用的是我们的旧版库，我们强烈建议您进行迁移，以便能够访问最新功能并获得与 Gemini 配合使用的最佳性能。如需了解详情，请参阅[旧版库](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn#previous-sdks)部分。

## 旧版库和迁移

如果您使用的是我们的旧版库，我们建议您
[迁移到新库](https://ai.google.dev/gemini-api/docs/migrate?hl=zh-cn)。

旧版库无法访问最新功能（例如
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn) 和 [Veo](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn)），并且已于
2025 年 11 月 30 日废弃。

每个旧版库的支持状态各不相同，详见下表：

| 语言 | 旧版库 | 支持状态 | 推荐的库 |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | 不会积极维护 | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | 不会积极维护 | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | 不会积极维护 | `google.golang.org/genai` |
| **Dart 和 Flutter** | `google_generative_ai` | 不会积极维护 | 使用 [Genkit Dart](https://genkit.dev/docs/dart/get-started/) 或 [Firebase AI Logic](https://pub.dev/packages/firebase_ai) |
| **Swift** | `generative-ai-swift` | 不会积极维护 | 使用 [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=zh-cn) |
| **Android** | `generative-ai-android` | 不会积极维护 | 使用 [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=zh-cn) |

**Java 开发者注意** ：Gemini API 没有 Google 提供的旧版 Java SDK，因此无需从之前的 Google 库进行迁移。您可以直接从[语言支持和安装](#install)部分开始使用新库。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-04-29。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-04-29。"],[],[]]
