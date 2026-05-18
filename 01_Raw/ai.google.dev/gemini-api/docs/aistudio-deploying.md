---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=zh-CN
fetched_at: 2026-05-18T12:58:51.515643+00:00
title: "\u4ece Google AI Studio \u90e8\u7f72 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 从 Google AI Studio 部署

借助 Google AI Studio，您可以直接从构建模式部署全栈应用。这样，您就可以快速从原型过渡到可扩缩的托管生产环境。

## 部署方案

如需从 AI Studio 构建模式部署应用，具体要求取决于您使用的层级：

- [**Google Cloud Starter 层级**](https://docs.cloud.google.com/docs/starter-tier?hl=zh-cn): 您无需设置 Google Cloud 云项目或结算账号，即可发布最多 2 个全栈应用。
- **标准部署**：需要将 Google Cloud 项目与您的
  AI Studio 账号相关联，并对该项目启用结算功能。

## 关于 Starter 层级

借助 Google Cloud Starter 层级，您可以直接从 Google AI Studio 将应用部署到 Google Cloud，而无需设置完整的 Google Cloud 环境或结算账号，从而简化了部署流程。

每次 Google AI Studio 部署都会在 Cloud Run 中创建一个相应的服务。对于在 Google AI Studio 中使用 Starter 层级部署的服务，存在以下限制：

- 您最多可以部署两个服务。
- 您的服务部署在
  [单个 Cloud Run 区域中](https://docs.cloud.google.com/run/docs/locations?hl=zh-cn)。

## Starter 层级部署步骤

在构建模式下设计应用后，使用 Starter 层级进行部署：

1. 点击右上角的**发布** 按钮。
2. 点击**开始使用** 。
3. 点击**发布应用** 。

部署完成后，AI Studio 会提供一个 Cloud Run 网址，您可以通过该网址访问您的正式版应用。

## 标准部署

随着应用的发展，您可能需要 Starter 层级之外的功能，例如更高的配额、更多的计算资源，或 Starter 层级中没有的其他 Google Cloud 产品。如需解锁这些功能，您可以将全托管式 Starter 层级项目转换为标准 Google Cloud 云项目。

这样，您就可以无缝扩缩，而不会丢失进度。[[请按照以下步骤创建 Cloud Billing 账号，正式接受标准 Google Cloud 服务条款，并升级到标准 Google Cloud 项目。](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=zh-cn#create-new-billing-account)](https://docs.cloud.google.com/docs/starter-tier?hl=zh-cn#upgradee)如需了解详情，请参阅
[付费账号的设置](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=zh-cn#paid-setup)。

如需详细了解结算层级，请参阅[结算](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn)。

## 删除应用

如果您不再需要某个应用，可以在 Google AI Studio 中按照以下说明将其删除：

1. 在 Google AI Studio 中，前往您的
   [应用页面](https://aistudio.google.com/app/apps?hl=zh-cn)。
2. 在左侧菜单中，选择**应用** 。
3. 将指针悬停在要删除的应用上。
4. 点击该行右侧的垃圾桶图标，即可删除该应用。

## 后续步骤

- 详细了解
  [Google Cloud Starter 层级](https://docs.cloud.google.com/docs/starter-tier?hl=zh-cn)。
- 了解 Gemini API 中的[结算](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-16。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-16。"],[],[]]
