---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=zh-CN
fetched_at: 2026-11-02T07:19:10.704032+00:00
title: "Gemini 4 Argon \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini 4 Argon

Gemini 4 Argon (`gemini-4-argon`) 是我们的旗舰推理模型，专为复杂的软件工程、深度数学和科学问题解决、自主多步智能体以及长达 100 万 token 的长解码而打造。

[在 Google AI Studio 中试用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)

## 文档

如需全面了解功能、API 变更和迁移指南，请访问[最新模型](https://ai.google.dev/gemini-api/docs/latest-model?hl=zh-cn)页面。

## gemini-4-argon

| 属性 | 说明 |
| --- | --- |
| id\_card模型代码 | `gemini-4-argon` |
| save支持的数据类型 | **输入源**  文本、图片、视频、音频和 PDF  **输出**  文本 |
| token\_autoToken 限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn) | **上下文窗口（统一的输入和输出 token 限制）**  1,048,576  **全速输出**  65,536（默认同步）/最多 1,048,576（使用[长解码](https://ai.google.dev/gemini-api/docs/long-decode?hl=zh-cn)） |
| handyman功能 | **[智能体视频理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn#agentic-video-understanding)**  支持（默认为 `static`）  **[音频生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)**  不受支持  **[缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)**  支持（仅限隐式）  注意：不支持显式缓存。  **[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)**  支持  **[计算机使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)**  支持  **[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)**  支持  **[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)**  支持  **[Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn)**  支持  **[图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)**  不受支持  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn)**  不受支持  **[利用 Google 搜索建立回答依据](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)**  支持  **[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)**  支持  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)**  支持（低、中、高）  **[网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)**  支持 |
| speed使用选项 | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)**  支持  **[Flex 推理](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn)**  支持  **[优先级推断](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-cn)**  支持 |
| 123 个版本 | 如需了解详情，请参阅[模型版本模式](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#model-versions)。  - 稳定：`gemini-4-argon` |
| calendar\_month最后更新时间 | 2026 年 10 月 |
| id\_card模型卡片 | [模型卡片](https://deepmind.google/models/model-cards/gemini-4-argon/?hl=zh-cn) |
| paid价格 | [价格](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn#gemini-4-argon) |

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-30。"],[],[]]
