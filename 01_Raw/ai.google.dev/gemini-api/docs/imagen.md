---
source_url: https://ai.google.dev/gemini-api/docs/imagen?hl=zh-CN
fetched_at: 2026-10-26T05:39:15.137492+00:00
title: "\u4f7f\u7528 Imagen \u751f\u6210\u56fe\u7247 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)

发送反馈

# 使用 Imagen 生成图片

Imagen 是 Google 的旧版图片生成模型。现已关闭，不再在 Gemini API 中提供。

## 迁移到 Nano Banana

改用 Nano Banana 生成图片：

- **模型名称**：请使用 `gemini-2.5-flash-image`（或 Nano Banana 2 模型，例如 `gemini-3.1-flash-image`），而不是 Imagen 模型名称。
- **方法**：使用 `client.models.generate_content` 而不是 `client.models.generate_images`。
- **响应处理**：Nano Banana 会返回包含图片数据的内容部分，而不是特定的图片响应对象。

如需了解详情和示例，请参阅[图片生成指南](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-18。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-18。"],[],[]]
