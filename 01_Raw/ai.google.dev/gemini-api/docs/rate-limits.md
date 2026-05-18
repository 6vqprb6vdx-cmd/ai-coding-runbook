---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-TW
fetched_at: 2026-05-18T13:10:37.350725+00:00
title: "\u983b\u7387\u9650\u5236 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 頻率限制

頻率限制會控管您在特定時間範圍內可向 Gemini API 發出的要求數量。這些限制有助於維持公平使用原則、防範濫用行為，以及確保所有使用者都能享有良好的系統效能。

[在 AI Studio 中查看有效費率限制](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=zh-tw)

## 速率限制的運作方式

頻率限制通常會從三個面向進行測量：

- 每分鐘要求數 (**RPM**)
- 每分鐘權杖數 (輸入) (**TPM**)
- 每日要求數 (**RPD**)

系統會根據各項限制評估您的用量，如果超出任何限制，就會觸發速率限制錯誤。舉例來說，如果 RPM 上限為 20，即使您未超過 TPM 或其他限制，在一分鐘內提出 21 個要求仍會導致錯誤。

頻率限制適用於專案，而非 API 金鑰。每日要求數 (**RPD**)：配額會在太平洋時間午夜重設。

限制會因使用的模型而異，部分限制僅適用於特定模型。舉例來說，每分鐘圖像數 (IPM) 只會針對可生成圖像的模型 (Nano Banana) 計算，但概念上與 TPM 相似。其他模型可能設有每日權杖數上限 (TPD)。

實驗和預覽模型的頻率限制較嚴格。

## 用量層級

頻率限制與專案的使用層級相關。隨著 API 用量和支出增加，系統會自動將您升級至較高的級別，並提高費率限制。

第 2 級和第 3 級的資格條件，是根據連結至專案的帳單帳戶，在 Google Cloud 服務 (包括但不限於 Gemini API) 的累計總支出而定。

| 用量層級 | 資格賽 | [帳單層級上限](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw#tier-spend-caps) |
| --- | --- | --- |
| **免費** | [有效專案](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw#google-cloud-projects)或免費試用方案 | 不適用 |
| **第 1 級** | [設定並連結有效的帳單帳戶](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw#setup-billing) | $250 美元 |
| **第 2 級** | 支付 $100 美元 + 首次付款成功後 3 天 | $2,000 美元 |
| **第 3 級** | 支付 $1,000 美元 + 首次付款成功後 30 天 | $20,000 美元 - $100,000 美元以上 |

一般而言，只要符合上述資格條件，升級要求通常就會獲得核准。但少數情況下，我們可能會根據審查過程中發現的其他因素，拒絕升級要求。

這項系統有助於維護所有使用者的 Gemini API 平台安全和完整性。

## Gemini API 頻率限制

速率限制取決於多種因素 (例如使用層級)，您可以在 Google AI Studio 中查看。隨著層級和帳戶狀態改變，費率限制會自動更新。

[在 AI Studio 中查看有效費率限制](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=zh-tw)

我們無法保證一定會達到指定的速率限制，實際容量可能有所不同。

## 優先順序推斷頻率限制

[優先順序](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-tw)用量有自己的速率限制，但用量會計入整體互動式流量速率限制。**預設速率限制：每個模型和層級的[標準速率限制](https://aistudio.google.com/rate-limit?hl=zh-tw)的 0.3 倍**

## 批次 API 頻率限制

[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw) 要求有自己的速率限制，與非批次 API 呼叫不同。

- **並行批次要求：**100 個
- **輸入檔案大小上限：**2 GB
- **檔案儲存空間上限：**20 GB
- **每個模型排入佇列的詞元數：**「批次排入佇列的詞元數」資料表會列出特定模型所有有效批次工作可排入佇列的詞元數上限。

### 級別 1

| 型號 | 批次加入佇列的權杖 |
| --- | --- |
| 文字輸出模型 | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3 Pro 預先發布版 | 5,000,000 |
| Gemini 3.1 Flash-Lite | 10,000,000 |
| Gemini 3.1 Flash-Lite 預先發布版 | 10,000,000 |
| Gemini 3 Flash 預先發布版 | 3,000,000 |
| Gemini 2.5 Pro | 5,000,000 |
| Gemini 2.5 Pro TTS | 25,000 |
| Gemini 2.5 Flash | 3,000,000 |
| Gemini 2.5 Flash 預先發布版 | 3,000,000 |
| Gemini 2.5 Flash Image 預先發布版 | 3,000,000 |
| Gemini 2.5 Flash TTS | 100,000 |
| Gemini 2.5 Flash-Lite | 10,000,000 |
| Gemini 2.5 Flash-Lite 預先發布版 | 10,000,000 |
| Gemini 2.0 Flash | 10,000,000 |
| Gemini 2.0 Flash Image | 3,000,000 |
| Gemini 2.0 Flash-Lite | 10,000,000 |
| 多模態生成模型 | | | | |
| Gemini 3.1 Flash Image 預先發布版 🍌 | 1,000,000 |
| Gemini 3 Pro Image 預先發布版 🍌 | 2,000,000 |
| 嵌入模型 | | | | |
| Gemini Embedding | 500,000 |

### 級別 2

| 型號 | 批次加入佇列的權杖 |
| --- | --- |
| 文字輸出模型 | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3 Pro 預先發布版 | 500,000,000 |
| Gemini 3.1 Flash-Lite | 500,000,000 |
| Gemini 3.1 Flash-Lite 預先發布版 | 500,000,000 |
| Gemini 3.1 Flash 預先發布版 | 400,000,000 |
| Gemini 2.5 Pro | 500,000,000 |
| Gemini 2.5 Pro TTS | 100,000 |
| Gemini 2.5 Flash | 400,000,000 |
| Gemini 2.5 Flash 預先發布版 | 400,000,000 |
| Gemini 2.5 Flash Image 預先發布版 | 400,000,000 |
| Gemini 2.5 Flash TTS | 100,000 |
| Gemini 2.5 Flash-Lite | 500,000,000 |
| Gemini 2.5 Flash-Lite 預先發布版 | 500,000,000 |
| Gemini 2.0 Flash | 1,000,000,000 |
| Gemini 2.0 Flash Image | 400,000,000 |
| Gemini 2.0 Flash-Lite | 1,000,000,000 |
| 多模態生成模型 | | | | |
| Gemini 3.1 Flash Image 預先發布版 🍌 | 250,000,000 |
| Gemini 3 Pro Image 預先發布版 🍌 | 270,000,000 |
| 嵌入模型 | | | | |
| Gemini Embedding | 5,000,000 |

### 階層 3

| 型號 | 批次加入佇列的權杖 |
| --- | --- |
| 文字輸出模型 | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3 Pro 預先發布版 | 1,000,000,000 |
| Gemini 3.1 Flash-Lite | 1,000,000,000 |
| Gemini 3.1 Flash-Lite 預先發布版 | 1,000,000,000 |
| Gemini 3.1 Flash 預先發布版 | 1,000,000,000 |
| Gemini 2.5 Pro | 1,000,000,000 |
| Gemini 2.5 Pro TTS | 1,000,000 |
| Gemini 2.5 Flash | 1,000,000,000 |
| Gemini 2.5 Flash 預先發布版 | 1,000,000,000 |
| Gemini 2.5 Flash Image 預先發布版 | 1,000,000,000 |
| Gemini 2.5 Flash TTS | 4,000,000 |
| Gemini 2.5 Flash-Lite | 1,000,000,000 |
| Gemini 2.5 Flash-Lite 預先發布版 | 1,000,000,000 |
| Gemini 2.0 Flash | 5,000,000,000 |
| Gemini 2.0 Flash Image | 1,000,000,000 |
| Gemini 2.0 Flash-Lite | 5,000,000,000 |
| 多模態生成模型 | | | | |
| Gemini 3.1 Flash Image 預先發布版 🍌 | 750,000,000 |
| Gemini 3 Pro Image 預先發布版 🍌 | 1,000,000,000 |
| 嵌入模型 | | | | |
| Gemini Embedding | 10,000,000 |

## 如何升級至下一個級別

如要從免費方案轉換為付費方案，請先[在 AI Studio 中設定帳單資訊](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw)。

專案符合[指定條件](#usage-tiers)後，系統就會自動升級至下一個層級。從免費方案升級至第 1 級方案通常會立即生效，後續升級作業則會在 10 分鐘內生效。前往 AI Studio 的「Projects」頁面，即可查看層級。

## 要求提高頻率限制

每個模型變體都有相關聯的速率限制 (每分鐘要求數，RPM)。
如要進一步瞭解這些速率限制，請參閱「[AI Studio 速率限制](https://aistudio.google.com/rate-limit?hl=zh-tw)」頁面。

[申請提高付費層級的速率限制](https://forms.gle/ETzX94k8jf7iSotH9)

我們無法保證會提高速率限制，但會盡力審查您的要求。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-07 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-07 (世界標準時間)。"],[],[]]
