---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=zh-CN
fetched_at: 2026-10-05T06:33:13.571572+00:00
title: "\u4ece Google AI Studio \u90e8\u7f72 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 从 Google AI Studio 部署

借助 Google AI Studio，您可以直接从“构建”模式部署全栈应用。这提供了一条从原型设计到可扩缩的受管理生产环境的快速路径。

## 部署方案

如需从 AI Studio 构建模式部署应用，具体要求取决于您使用的层级：

- [**Google Cloud 新手体验层级**](https://docs.cloud.google.com/docs/starter-tier?hl=zh-cn)：符合条件的账号无需设置 Google Cloud 云项目或结算账号，即可发布最多 2 个全栈应用。
- **标准部署**：需要一个与 AI Studio 账号相关联的 Google Cloud 项目，并且该项目已启用结算功能。

## 新手体验层级简介

Google Cloud 新手体验层级为符合条件的账号提供了一条简化的途径，让其能够直接从 Google AI Studio 将应用部署到 Google Cloud。您无需设置完整的 Google Cloud 环境或结算账号。

每次 Google AI Studio 部署都会在 Cloud Run 中创建相应的服务。对于在 Google AI Studio 中以 Starter 级部署的服务，存在以下限制：

- 您最多可以部署两项服务。
- 您的服务部署在[单个 Cloud Run 区域](https://docs.cloud.google.com/run/docs/locations?hl=zh-cn)中。

### 新手体验层级资格条件

并非所有账号都符合使用 Google Cloud 新手体验层级的条件。如果您的账号符合以下任何条件，则可能不符合条件：

- 您登录的是 Google Workspace 账号（包括付费或免费的 Google Workspace、Google Workspace 教育版或 Google 公益支持 订阅）。
- 您拥有有效的付费 Google Cloud 结算账号或曾经拥有付费 Google Cloud 结算账号。
- 根据您账号的活动情况，我们目前没有足够的证据来授予您 Starter 级访问权限。

Google AI Studio 支持团队无法覆盖入门级资格要求。如果您的账号不符合条件，请附加结算账号并使用[标准部署](#standard-deployment)来发布应用。

## 使用新手体验层级进行部署

在 Build 模式下设计应用后，使用新手体验层级部署应用：

1. 点击右上角的**发布**按钮。
2. 点击**开始使用**。
3. 点击**发布应用**。

部署完成后，AI Studio 会提供一个 Cloud Run 网址，您可以通过该网址访问已上线的应用。

## AI Studio 的自定义网址

从 Google AI Studio 发布应用时，您可以设置 `ai.studio` 下的自定义子网域（例如 `https://your-app-name.ai.studio`），以便用户轻松记住。

Google AI Studio 要求子网域在所有项目中是全局唯一的，并按先到先得的原则进行分配。如果其他项目已使用某个名称，AI Studio 会提示您选择其他名称。如果您取消发布或删除应用，其自定义网址将被释放，并可供其他用户声明。

### 设置自定义网址

如需为应用设置或更新自定义网址，请执行以下操作：

1. 在 **Build** 模式下，在 Google AI Studio 中打开您的应用。
2. 点击右上角的**发布**。
3. 在部署配置中，在**自定义网址**字段中输入首选子域名，或接受建议的网址。
4. 点击**发布应用**。

如需将现有自定义网址转移到其他应用，您必须先取消发布或删除分配了该自定义网址的应用，然后使用所选子网域发布新应用。

### 举报商标或版权问题

自定义子网域必须遵守 [Google 服务条款](https://policies.google.com/terms?hl=zh-cn)。如果您发现某个自定义网址侵犯了商标或未经许可使用了受版权保护的名称，可以使用 [Google 法律问题排查工具](https://support.google.com/legal/troubleshooter/1114905?hl=zh-cn)进行举报。

## 标准部署

随着应用的发展，您可能需要新手体验层级以外的功能，例如更高的配额、更多的计算资源，或者新手体验层级中未提供的其他 Google Cloud 产品。如需解锁这些功能，您可以将完全受管的新手体验层级项目转换为标准 Google Cloud 项目。

这样可确保您能够顺畅地扩展规模，而不会丢失进度。按照步骤[创建 Cloud Billing 账号](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=zh-cn#create-new-billing-account)，正式接受标准 Google Cloud 服务条款，并[升级为标准 Google Cloud 项目](https://docs.cloud.google.com/docs/starter-tier?hl=zh-cn#upgradee)。
如需了解详情，请参阅[付费账号的设置](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=zh-cn#paid-setup)。

如需详细了解结算层级，请参阅[结算](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn)。

## 删除您的申请

如果您不再需要自己的应用，可以按照以下说明在 Google AI Studio 中将其删除：

1. 在 Google AI Studio 中，前往[应用页面](https://aistudio.google.com/app/apps?hl=zh-cn)。
2. 在左侧菜单中，选择**应用**。
3. 将鼠标指针悬停在要删除的应用上。
4. 点击相应行右侧的回收站图标即可删除该应用。

## 后续步骤

- 详细了解 [Google Cloud 新手体验层级](https://docs.cloud.google.com/docs/starter-tier?hl=zh-cn)。
- 阅读有关 Gemini API 中[结算](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn)的内容。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-28。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-28。"],[],[]]
