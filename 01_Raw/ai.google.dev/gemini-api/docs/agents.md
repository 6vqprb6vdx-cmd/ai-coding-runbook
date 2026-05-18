---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=zh-TW
fetched_at: 2026-05-18T13:09:24.970861+00:00
title: "\u4ee3\u7406\u7a0b\u5f0f\u7e3d\u89bd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 代理程式總覽

代理是運用 Gemini 模型、一組工具和推論能力的系統，可執行複雜的多步驟工作，並達成特定目標。與單一模型呼叫不同，代理可以規劃及執行一系列動作、與外部系統互動，並彙整資訊來滿足使用者的要求。

透過 Gemini API，您可以運用下列功能建構強大的代理程式：

- **[Gemini 模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw)：**核心智慧，提供推理和語言理解能力。
- **[工具](https://ai.google.dev/gemini-api/docs/tools?hl=zh-tw)：**可將模型連結至真實世界資訊和動作的功能。這些工具可以是內建工具 (例如 Google 搜尋、地圖、程式碼執行)，也可以是自訂工具。
- **[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)：**定義及連結自訂工具和 API 與 Gemini 模型的機制。
- **[思考型](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)：**可強化模型推論能力，並規劃複雜工作。
- **[長脈絡](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-tw)：**讓代理程式在長時間的互動中，持續記住狀態和資訊。

## 可用的代理程式

- **[深入研究代理](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw)：**自主代理，可規劃、執行及整合多步驟研究工作，適用於市場分析、盡職調查和文獻回顧等用途。

## 建構代理

代理會使用模型和工具完成多步驟工作。Gemini 提供推論能力 (「大腦」) 和必要工具 (「雙手」)，但您通常需要自動化調度管理框架來管理代理程式的個人化記憶、規劃迴圈，以及執行複雜的工具鍊結。

如要盡量提升多步驟工作流程的可靠性，請編寫指令，明確控管模型的推論和規劃方式。雖然 Gemini 的一般推論能力很強大，但複雜的代理程式需要提示，強制執行特定行為，例如在遇到問題時堅持不懈、評估風險，以及主動規劃。

如需設計這些提示的策略，請參閱[代理程式工作流程](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-tw#agentic-workflows)。以下是[系統指令](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-tw#agentic-si-template)範例，可將多個代理程式基準的效能提升約 5%。

## 代理架構

Gemini 整合了領先業界的開放原始碼代理框架，例如：

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=zh-tw)：使用圖表結構建構有狀態的複雜應用程式流程和多代理系統。
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=zh-tw)：將 Gemini 代理程式連結至私人資料，以利 RAG 增強型工作流程。
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=zh-tw)：自動調度管理角色扮演的自主式 AI 代理，進行協作。
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=zh-tw)：在 JavaScript/TypeScript 中建構 AI 輔助的使用者介面和代理程式。
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/)：開放原始碼框架，用於建構及自動調度可互通的 AI 代理。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-04-29 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-04-29 (世界標準時間)。"],[],[]]
