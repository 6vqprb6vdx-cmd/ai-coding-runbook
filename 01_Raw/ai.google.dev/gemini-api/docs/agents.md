---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=zh-TW
fetched_at: 2026-06-08T14:59:59.216364+00:00
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

Gemini API 的代管代理程式提供可設定的代理程式架構。只要呼叫單一 API，即可佈建 Linux 沙箱，讓代理自主推論、執行程式碼、管理檔案及瀏覽網頁。

[rocket\_launch

快速入門導覽課程

進行第一次代理呼叫、串流回應，以及建構自訂代理。](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=zh-tw)
[smart\_toy

Antigravity 代理程式

預設代理程式的功能、工具、多模態輸入和定價。](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-tw)
[experiment

AI Studio 中的代理

視覺化測試區，可設計代理程式原型，完全不必編寫程式碼。](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=zh-tw)

## 可用的受管理代理程式

- **[Antigravity 代理](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-tw)**：一般用途
  受管理代理，採用 Gemini 3.5 Flash 技術。在 Google 代管的安全 Linux 沙箱中執行程式碼、管理檔案及搜尋網路。您可以加入自己的指令、技能和資料來擴充功能，[建構自訂代理程式](https://ai.google.dev/gemini-api/docs/custom-agents?hl=zh-tw)。
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw)**：自主研究代理，可規劃、執行及整合多步驟研究工作，適用於市場分析、盡職調查和文獻回顧等用途。

## 安全性與最佳做法

每個代理程式都會在沙箱環境中執行，並在 OS 層級隔離。根據預設，沙箱的傳出網路存取權不受限制。您可以使用許可清單限制或停用網路存取權。

### 網路存取

根據預設，環境具有不受限制的輸出網路存取權。使用`network`許可清單將輸出流量限制在特定網域或萬用字元模式。如需設定詳情，請參閱「[網路允許清單](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=zh-tw#network_allow_list)」(AI Studio) 或「[網路規則](https://ai.google.dev/gemini-api/docs/custom-agents?hl=zh-tw#with_network_rules)」(API)。

### 外部工具和 API

您可以連結外部工具和 API，擴充代理程式功能。請只使用信任來源的工具，並將權限範圍設為最低必要權限。憑證可透過輸出 Proxy 標頭轉換安全地注入，且絕不會在沙箱中公開。代理程式可以使用有權存取的任何憑證，因此請只提供您願意授予完整範圍的憑證。

- 使用最低權限的服務帳戶或 API 金鑰。
- 建議使用短期有效權杖，而非長期有效金鑰。
- 請只提供您願意授予完整範圍的憑證。
- 定期輪替憑證。

如要進一步瞭解如何設定標頭轉換，請參閱「[憑證](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw#credentials)」。

### 專人監督

部署前請務必驗證輸出內容 (生成的程式碼、資料轉換、設定變更)，尤其是會修改資料或與外部系統互動的工作。

## 定價

受管理代理程式採用[即付即用模式](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#pricing-for-agents)，費用取決於 Gemini 模型權杖和工具用量。單一互動可能會觸發多個推理迴圈，通常會耗用 10 萬到 300 萬個權杖。預先發布版**不會收取**環境運算費用。查看各項工作的[預估費用](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-tw#availability-and-pricing)。

## 限制

| 限制 | 說明 |
| --- | --- |
| **環境生命週期** | 環境閒置 7 天後就會永久刪除。 |
| **VM 關機** | VM 閒置一段時間後會關機，以節省資源。下一個要求會還原狀態 (冷啟動)。 |
| **預先安裝的軟體** | 以 Ubuntu 為基礎的環境，搭載 Python 3.12 和 Node.js 22。如要進一步瞭解環境的基礎映像檔，請參閱「[預先安裝的軟體](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw#pre-installed-software)」。 |
| **最多代理程式** | 最多可有 1,000 個受管理代理程式。 |

## 代理架構

您也可以使用下列架構和 SDK，透過 Gemini 建構代理程式：

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=zh-tw)：使用圖表結構建構具狀態的複雜應用程式流程和多代理系統。
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=zh-tw)：將 Gemini 代理程式連結至私人資料，以利 RAG 增強型工作流程。
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=zh-tw)：自動調度管理角色扮演的自主式 AI 代理，進行協作。
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=zh-tw)：在 JavaScript/TypeScript 中建構 AI 輔助的使用者介面和代理程式。
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/)：開放原始碼框架，用於建構及自動調度可互通的 AI 代理。
- [**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=zh-tw)：使用與 Google Antigravity 相同的工具、代理程式迴圈和環境管理功能，以 Python 建構自主式 AI 代理程式。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-20 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-20 (世界標準時間)。"],[],[]]
