---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=zh-CN
fetched_at: 2026-06-01T19:47:37.288483+00:00
title: "\u5728 Google AI Studio \u4e2d\u6784\u5efa\u5e94\u7528 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 在 Google AI Studio 中构建应用

本页介绍了如何使用 Google AI Studio 快速构建（或“氛围编程”）和部署应用，以测试 Gemini 的最新功能，例如 [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn) 和 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn)。Google AI Studio 支持使用全栈运行时构建 **Web 应用**，以及使用 Kotlin 和 Jetpack Compose 构建**原生 Android 应用**，所有这些都可以通过自然语言提示完成。

## 开始使用

在 Google AI Studio 的[构建模式](https://aistudio.google.com/apps?hl=zh-cn)中开始氛围编程。您可以通过以下几种方式开始构建：

- **从提示开始**：在“构建”模式下，使用输入框输入您要构建的内容的说明。选择 AI 芯片，以便在提示中添加图片生成或 Google 地图数据等特定功能。您甚至可以使用语音转文字按钮说出您想要的内容。
- **“手气不错”按钮**：如果您需要创意灵感，请使用“手气不错”按钮，Gemini 会生成包含项目想法的提示，帮助您开始创作。
- **混搭库中的项目**：打开[应用库](https://aistudio.google.com/apps?source=showcase&hl=zh-cn)中的项目，然后选择**复制应用**。

运行提示后，您会看到必要的代码和文件已生成，右侧会实时显示应用的预览效果。

## 创建了什么？

运行提示后，AI Studio 会创建一个完整的应用。您可以使用平台选择器选择构建 **Web 应用**还是**原生 Android 应用**。

对于**Web 应用**（默认），AI Studio 会创建一个包含以下内容的全栈环境：

- **客户端**：Web 前端（默认使用 React）。
- **服务器端**：一种 Node.js 运行时，可实现安全的 API 调用、数据库连接和 npm 软件包使用。

对于 **Android 应用**，AI Studio 会生成一个 Kotlin 和 Jetpack Compose 项目，您可以在基于浏览器的模拟器中预览该项目，将其安装在实体设备上，并将其发布到 Play 商店以进行测试。[详细了解如何构建 Android 应用](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=zh-cn)。

您可以在右侧的预览窗格中选择**代码**标签页，查看生成的代码。**反重力代理**可智能管理堆栈中的多个文件，确保更改得到正确传播。

### Antigravity Agent

**Antigravity Agent** 是 [Google Antigravity](https://antigravity.google?hl=zh-cn) 中的主要 AI 功能，现在，智能体框架的核心组件正在为 Google AI Studio 中的“构建”模式体验提供支持。它不仅能生成简单的代码，还能维护整个项目的上下文、管理多个文件，并理解复杂的指令，从而构建强大的全栈应用。

主要功能包括：

- **上下文感知**：保持之前提示和文件状态的上下文。
- **多文件管理**：处理多个文件之间的依赖关系。
- **经过验证的执行**：验证代码更新，以减少幻觉。

## 全栈功能

Google AI Studio 可充分发挥现代 Web 生态系统的强大功能，让您不仅可以构建客户端原型。

- **服务器端运行时和 npm**：使用丰富的 npm 软件包库。代理会根据应用的需求自动识别并安装软件包（例如，用于数据可视化的特定库或 API 客户端）。您也可以根据需要请求特定软件包。
- **密文管理**：在**设置**菜单中安全地存储 API 密钥和密文。这些密钥可在服务器端代码中访问，因此不会在客户端泄露。
- **多人模式**：直接在 AI Studio 中构建实时协作体验。服务器端运行时管理用户一起互动所需的状态和连接。
- **Firebase Firestore 和 Authentication**：自动预配和设置 Firebase，包括 Firestore 数据库（持久性数据存储）和 Firebase Authentication（登录流程，特别是“使用 Google 账号登录”）。该代理会处理整个设置过程，甚至会在您的应用中为这些服务编写代码。
- **Google Workspace 集成**：将您的应用连接到 Gmail、Google 表格、Google 文档、Google 云端硬盘、Google 日历等 Google Workspace API。AI Studio 会自动处理所有 OAuth 配置。

[详细了解如何开发全栈应用](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=zh-cn)

### Android 应用

您还可以使用 Kotlin 和 Jetpack Compose 构建原生 Android 应用。
在基于浏览器的 Android 模拟器中预览应用，使用浏览器中的 ADB 将应用安装到实体设备上，然后发布到 Play 商店以进行内部测试。

[详细了解如何构建 Android 应用](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=zh-cn)

## 继续构建

Google AI Studio 为您的应用生成初始代码后，您可以继续对其进行优化：

### 在 Google AI Studio 中构建

- **与 Gemini 迭代**：在**构建模式**下使用聊天面板，问问 Gemini 进行修改、添加新功能或更改样式。
- **直接修改代码**：在预览面板中打开**“代码”标签页**，进行实时修改。

### 在外部开发

对于更高级的工作流，您可以导出代码并在自己偏好的环境中工作：

- **下载并进行本地开发**：将生成的代码导出为 **ZIP 文件**，然后将其导入到代码编辑器中。
- **推送到 GitHub**：通过将代码推送到 **GitHub 代码库**，将代码与现有的开发和部署流程集成。

## 主要特性

Google AI Studio 包含多项功能，可让构建过程直观且可视化：

- **创建和迭代全栈应用**：只需提供提示即可创建全栈应用，并通过聊天或**注释模式**进行迭代。在注释模式下，您可以突出显示应用界面的任何部分，并描述您想要的更改。
- **分享和部署应用**：您可以与他人分享自己的作品，以便协作或展示您的作品。共享时，API 调用会计入您的使用量限额。如果您使用付费模型，可能需要支付费用。然后，当应用准备就绪后，将其部署到 Cloud Run。
- **应用程序库**：应用程序库提供了一个项目创意可视化库。您可以浏览 Gemini 的各种功能，立即预览应用，并对其进行混搭，打造出属于自己的应用。

## 部署或归档应用

应用准备就绪后，您可以按以下方式部署应用：

- **Cloud Run**：将应用部署为可扩缩的服务。
  [Google Cloud Run](https://cloud.google.com/run?hl=zh-cn) 的价格可能取决于用量。如需详细了解部署，请参阅[从 Google AI Studio 进行部署](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=zh-cn)。
- **GitHub**：将项目导出到 GitHub 代码库。

## 限制

本部分列出了 Google AI Studio 中构建模式的当前限制。

### API 密钥管理

当您创建使用 Gemini API 的新应用时，AI Studio 会自动将您的 Gemini API 密钥配置为应用服务器端环境中的密钥。您可以在 **Secrets** 面板中查看和管理此密钥。

- **自动设置**：系统会自动为您设置 `GEMINI_API_KEY`，无需手动配置即可开始构建。
- **仅限服务器端**：API 密钥会注入到服务器端运行时，绝不会包含在客户端代码中。
- **现有应用**：对于在 2026 年 5 月 14 日之前构建的应用，当您下次修改应用的 Gemini 功能时，该代理会自动将您的 Gemini API 集成升级为推荐的服务器端方法。

### 在 Google AI Studio 之外进行部署

- **Cloud Run**：当您从 AI Studio 部署到 Cloud Run 时，您的 API 密钥会安全地包含在服务器端环境中。部署的应用将使用您的 API 密钥来处理所有用户的 Gemini API 调用。
- **ZIP 下载**：如果您将应用下载为 ZIP 文件以在其他位置运行，则需要在托管环境中设置 `GEMINI_API_KEY` 环境变量。由于您应用的 Gemini API 调用是从服务器端代码发出的，因此密钥不会向最终用户公开。

### 分享应用时出错

如果您分享了应用，而最终用户在使用分享的网址时遇到 **403 访问受限**错误，则可能是由于以下原因之一：

- **浏览器扩展程序**：Privacy Badger 等隐私保护扩展程序可能会屏蔽该应用。请停用该扩展程序，以免出现此错误。
- **构建问题**：当前代码可能存在问题。提示代理“修复当前代码的所有 build 问题”，然后重新分享网址。

## 常见问题解答

### 什么是“在 AI Studio 中构建”？

AI Studio Build 平台旨在帮助您使用 Gemini 将简单的提示转化为可用于生产用途的 AI 赋能型应用。通过提示描述您想要构建的内容，Gemini 就会为您生成应用。您还可以浏览我们的库，了解 Gemini API 的用途，并重新合成应用以打造自己的应用。

### Build 如何处理我的 Gemini API 密钥？

当您创建使用 Gemini API 的应用时，AI Studio 会自动将您的 Gemini API 密钥设置为服务器端密钥。您应用的 Gemini API 调用是通过使用此密钥的服务器端代码进行的，因此该密钥永远不会在浏览器中公开。您可以在“设置”中的 **Secrets** 面板中查看 API 密钥。

### 分享应用时，我的 API 密钥是否会泄露？

不会。您的 API 密钥会作为服务器端密钥存储，绝不会包含在客户端代码中。分享应用后，其他用户可以使用该应用，但无法看到您的 API 密钥。

与他人分享应用时，API 调用次数会计入您的使用限额。
如果您使用付费模型，可能需要支付费用。在设置过程中以及在您分享应用之前，AI Studio 会提前告知您应用是否可能会产生费用。

### 哪些人可以查看我的应用？

默认情况下，您的应用处于非公开状态。您可以与其他用户分享应用，以便他们使用该应用。与您共享应用的用户可以查看该应用的代码，并出于自己的目的派生该应用。如果您以修改权限分享应用，其他用户就可以修改应用的代码。

### 我可以在 AI Studio 之外运行应用吗？

可以。您可以从 AI Studio 将应用部署到 [Cloud Run](https://cloud.google.com/run?hl=zh-cn)，这会为您的应用提供一个公共网址，并在服务器端环境中安全地配置您的 API 密钥。您还可以将应用下载为 ZIP 文件并托管在其他位置，但需要在托管环境中设置 `GEMINI_API_KEY` 环境变量。由于 Gemini API 调用是从服务器端代码发出的，因此您的密钥始终安全无虞。

如需详细了解部署选项，请参阅[从 Google AI Studio 进行部署](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=zh-cn)。

### 我能否使用自己的工具在本地开发应用，然后在此处分享？

此功能尚未推出。我们很高兴未来能支持更多应用使用情形。如果您有任何具体想法，请考虑向我们提供反馈。

### 如何将数据库或其他存储空间与我的应用搭配使用？

AI Studio 应用是在 Cloud Run 容器中运行的标准应用。您可以使用可通过网络连接的任何存储解决方案，前提是防火墙不会阻止从动态 IP 范围进行访问。

我们正在努力在未来添加对存储空间的直接支持，届时您将可以直接在 AI Studio 中配置存储空间。

### 如何访问麦克风、摄像头和其他 Navigator API？

为确保观看者了解应用对其摄像头或其他设备的使用情况，我们要求应用在访问这些 [Navigator API](https://developer.mozilla.org/en-US/docs/Web/API/Navigator) 之前，必须先获得观看者的额外确认。
应用创建者可以将这些权限请求添加到应用的 `metadata.json` 文件中。例如：

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

`requestFramePermissions` 支持的值是标准[受政策控制的功能](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md)的子集。

### 如何将 GitHub 与我的应用搭配使用？

借助 AI Studio 的 GitHub 集成，您可以为自己的工作创建代码库并提交最新更改。我们目前不支持拉取远程更改。

### 我可以向其他用户授予应用的修改权限吗？

目前尚不支持此功能，但很快就会推出。

### 为什么我的应用因违反政策而被标记？

我们有系统会自动审核应用，以确保其符合我们的政策。如果我们发现某个应用违反了我们的政策，我们会将其从 AI Studio 中移除。违规行为包括但不限于以下情况：

- 包含恶意软件、钓鱼式攻击或冒充行为的应用
- 展示或分发违反“儿童性虐待影像”政策的内容的应用
- 应用展示或分发违反骚扰政策的内容
- 应用展示或分发违反“仇恨言论”政策的内容
- 展示或分发违反人口贩卖政策的内容的应用
- 展示或散布违反露骨色情内容政策的内容的应用
- 展示或分发违反暴力和血腥内容政策的内容的应用
- 显示或分发违反“有害或危险内容”政策的内容的应用

如果您的应用被标记为违反政策，但您认为我们的认定有误，可以提交申诉。屡次违反我们的政策可能会导致您无法再使用 AI Studio。

### 作为应用开发者，我有哪些责任？

请注意，作为应用的所有者，您有责任确保应用的行为符合相关规定，并负责应用处理的所有数据。其中包括：

- **法律合规性和第三方权利**：确保您的应用符合所有适用的法律法规，并且不侵犯他人的权利，包括知识产权和隐私权。
- **内容监控**：您的应用使用的其他服务可能需要遵守其他条款。例如，[Google Cloud 服务条款](https://cloud.google.com/terms?hl=zh-cn)（适用于 Firestore）要求托管第三方内容的客户发布政策，以定义禁止的内容（例如非法内容），并监控是否存在此类非法内容。
- **安全实现**：实现必要的安全措施和内容审核工具，以防止您的应用被滥用。

请注意服务条款中的[使用限制](https://ai.google.dev/gemini-api/terms?hl=zh-cn#use-restrictions)。

### 哪些条款适用于 AI Studio 中的应用程序库？

除非另有说明，否则使用 AI Studio 应用程序库中精选的应用时须遵守[《Gemini API 附加服务条款》](https://ai.google.dev/gemini-api/terms?hl=zh-cn)。

## 后续步骤

- [开发全栈应用](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=zh-cn)（网页）
- [构建 Android 应用](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=zh-cn)
- 请参阅[应用库](https://aistudio.google.com/apps?source=showcase&hl=zh-cn)中的示例。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-19。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-19。"],[],[]]
