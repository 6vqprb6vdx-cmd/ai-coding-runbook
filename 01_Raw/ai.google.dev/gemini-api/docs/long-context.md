---
source_url: https://ai.google.dev/gemini-api/docs/long-context?hl=zh-CN
fetched_at: 2026-05-25T12:55:20.253078+00:00
title: "\u957f\u4e0a\u4e0b\u6587 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 长上下文

许多 Gemini 模型都配备了 100 万个或更多 token 的大型上下文窗口。过去，大语言模型 (LLM) 受到一次可传递给模型的文本（或 token）数量的极大限制。Gemini 的长上下文窗口发掘了许多新的应用场景和开发者模式。

您已用于[文本生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn)或[多模态输入](https://ai.google.dev/gemini-api/docs/vision?hl=zh-cn)等场景的代码可以直接用于长上下文，无需进行任何更改。

本文档简要介绍了如何使用上下文窗口包含 100 万个及更多 token 的模型。本页面简要介绍了上下文窗口，并探讨了开发者应如何考虑长上下文、长上下文的各种实际应用场景，以及优化长上下文使用的方法。

如需了解特定模型的上下文窗口大小，请参阅[模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)页面。

## 什么是上下文窗口？

使用 Gemini 模型的基本方法是将信息（上下文）传递给模型，模型随后会生成回答。上下文窗口可以比作短期记忆。人们的短期记忆可以存储有限的信息量，生成模型也是如此。

您可以参阅我们的[生成模型指南](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-cn#under-the-hood)，详细了解模型在后台的工作原理。

## 开始使用长上下文

早期的生成模型一次只能处理 8,000 个词元。较新的模型进一步提高了此数字，可接受 32,000 个甚至 128,000 个词元。Gemini 是第一个能够接受 100 万个 token 的模型。

在实际中，100 万个词元相当于：

- 50,000 行代码（标准为每行 80 个字符）
- 您在过去 5 年内发送的所有短信
- 8 部平均长度的英语小说
- 200 多个平均时长播客剧集的转写内容

许多其他模型中常见的上下文窗口较为有限，因此通常需要采用一些策略，例如随意舍弃旧消息、总结内容、将 RAG 与向量数据库搭配使用，或过滤提示以节省 token。

虽然这些技巧在特定场景中仍然很有价值，但 Gemini 庞大的上下文窗口支持更直接的方法：预先提供所有相关信息。由于 Gemini 模型是使用强大的上下文功能专门构建的，因此它们具有强大的上下文学习能力。例如，仅使用上下文中的教学材料（一本 500 页的参考语法书、一本字典和约 400 个平行句子），Gemini [学会了](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)将英语翻译成卡拉芒语（一种使用者不到 200 人的巴布亚语言），翻译质量与使用相同材料的人类学习者相当。这说明了 Gemini 的长上下文所带来的范式转变，通过强大的上下文学习能力开辟了新的可能性。

## 长上下文应用场景

虽然大多数生成模型的标准应用场景仍然是文本输入，但 Gemini 模型系列可实现多模态应用场景的新模式。这些模型可采用原生方式理解文本、视频、音频和图片。它们附带[可接受多模态文件类型的 Gemini API](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=zh-cn)，以方便使用。

### 长文本

事实证明，文本是支撑 LLM 大部分发展势头的智能层。如前所述，LLM 的很多实际限制是因为没有足够大的上下文窗口来执行某些任务。这导致了检索增强生成 (RAG) 和其他技术的快速采用，这些技术可为模型动态提供相关的上下文信息。现在，随着上下文窗口越来越大，出现了一些新技术可用于发掘新的应用场景。

基于文本的长上下文的一些新兴和标准应用场景包括：

- 总结大型文本语料库
  - 之前使用较小上下文模型的总结方法需要使用滑动窗口或其他技术，以便在新词元传递给模型时保留之前部分的状态
- 问答
  - 过去在上下文数量有限且模型的真实召回率较低的情况下，只有使用 RAG 才能实现这一目的
- 智能体工作流
  - 文本是智能体如何保存已完成的操作和需要执行的操作的状态的基础；如果没有关于实际世界和智能体目标的足够信息，会限制智能体的可靠性

[多样本上下文学习](https://arxiv.org/pdf/2404.11018)是长上下文模型发掘的最独特功能之一。研究表明，采用常见的“单样本”或“多样本”示例模式，在其中向模型提供一个或几个任务示例，然后扩展到多达数百个、数千个甚至数十万个示例，这可能形成全新的模型功能。事实证明，这种多样本方法的性能与针对特定任务进行了微调的模型类似。对于 Gemini 模型的性能尚不足以满足生产发布的应用场景，您可以尝试多样本方法。正如您稍后将在长上下文优化部分中所了解的那样，上下文缓存使这种高输入词元工作负载类型在经济上更加可行，在某些场景中甚至可降低延迟。

### 长视频

无法访问媒体本身长期以来一直限制着视频内容的实用性。浏览内容并非易事，转写通常无法捕获视频的细微差别，而且大多数工具无法同时处理图片、文本和音频。在 Gemini 中，长上下文文本功能可转换为以持续的性能推理和回答有关多模态输入的问题的能力。

视频长上下文的一些新兴和标准应用场景包括：

- 视频问答
- 视频内存，如 [Google 的 Project Astra](https://deepmind.google/technologies/gemini/project-astra/?hl=zh-cn) 所示
- 视频字幕
- 视频推荐系统，通过新的多模态理解来丰富现有元数据
- 视频自定义，可查看数据以及关联视频元数据的语料库，然后移除与观看者无关的视频部分
- 视频内容审核
- 实时视频处理

处理视频时，重要的是考虑如何[将视频处理为词元](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn#media-token)，这会影响结算和用量限额。如需详细了解如何使用视频文件进行提示，请参阅[提示指南](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=zh-cn#prompting-with-videos)。

### 长音频

Gemini 模型是首批能够理解音频的原生多模态大语言模型。传统上，典型的开发者工作流涉及将多个特定于领域的模型（例如语音转文字模型和文本到文本模型）串联起来，以便处理音频。这会导致执行多次往返请求所需的延迟时间增加并且性能下降，这通常归因于多模型设置的分离架构。

音频上下文的一些新兴和标准应用场景包括：

- 实时转写和翻译
- 播客/视频问答
- 会议转写和总结
- 语音助理

如需详细了解如何使用音频文件进行提示，请参阅[提示指南](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=zh-cn#prompting-with-videos)。

## 长上下文优化

使用长上下文和 Gemini 模型时，主要优化方法是使用[上下文缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)。除了以前无法在单个请求中处理大量词元之外，另一个主要限制是费用。如果您有一个“与数据聊天”应用，用户在其中上传了 10 个 PDF 文件、一个视频和一些工作文档，那么过去您必须使用更复杂的检索增强生成 (RAG) 工具/框架来处理这些请求，并为移入上下文窗口的词元支付大量费用。现在，您可以缓存用户上传的文件，并按小时为存储这些文件付费。例如，使用 Gemini Flash 时，每个请求的输入 / 输出费用比标准输入 / 输出费用低约 4 倍，因此如果用户与其数据进行足够多的聊天，便可为作为开发者的您节省大量费用。

## 长上下文限制

在本指南的各个部分中，我们讨论了 Gemini 模型如何在各种“大海捞针”检索评估中实现高性能。这些测试考虑了最基本的设置，您在其中只需寻找一根“针”。如果您要寻找多根“针”或特定信息，模型执行的准确率会有所不同。性能可能会因上下文而变化很大。考虑这一点很重要，因为在检索到正确信息与费用之间存在固有的权衡。您在单个查询中可获得大约 99% 的准确率，但每次发送该查询时，您都必须支付输入词元费用。因此，要检索 100 条信息，如果您需要 99% 的性能，则可能需要发送 100 个请求。这是一个很好的示例，上下文缓存在其中可显著降低与使用 Gemini 模型关联的费用，同时保持高性能。

## 常见问题解答

### 在上下文窗口中，将查询放在哪个位置效果最好？

在大多数情况下，尤其是当总上下文较长时，如果您将查询 / 问题放在提示的末尾（在所有其他上下文之后），模型的效果会更好。

### 向查询中添加更多令牌后，模型性能会下降吗？

一般来说，如果您不需要将令牌传递给模型，最好避免传递令牌。不过，如果您有一大块包含某些信息的 token，并且想就这些信息提问，模型能够非常准确地提取这些信息（在许多情况下，准确率高达 99%）。

### 如何通过长上下文查询降低费用？

如果您有一组类似的 token / 上下文想要多次重复使用，[上下文缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)有助于减少与询问该信息相关联的费用。

### 上下文长度是否会影响模型延迟时间？

无论请求大小如何，任何给定请求都存在一定的固定延迟时间，但一般来说，较长的查询会产生更高的延迟时间（从发出请求到获得第一个令牌的时间）。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-04-29。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-04-29。"],[],[]]
