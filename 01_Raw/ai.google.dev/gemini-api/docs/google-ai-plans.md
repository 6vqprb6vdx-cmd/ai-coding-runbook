---
source_url: https://ai.google.dev/gemini-api/docs/google-ai-plans?hl=zh-TW
fetched_at: 2026-11-02T07:13:04.177069+00:00
title: "Google AI \u65b9\u6848 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Google AI 方案

在 AI Studio 使用 Google AI 訂閱方案。

相較於免費方案，Google AI Pro 和 Ultra 訂閱方案提供更廣泛的模型存取權，並提高 AI Studio 的原型設計和開發頻率限制。

如要註冊 Google AI 方案，可以直接在 Google AI Studio 升級，只要點選左側導覽選單中的「Upgrade」(升級) 按鈕即可。或者，你也可以前往 [Google AI 方案頁面](https://one.google.com/about/google-ai-plans/?hl=zh-tw)訂閱。

## 總覽

開發人員訂閱 Google AI Pro 和 Ultra 後，即可在 Google AI Studio Playground 使用付費模型和更高的頻率限制，並在[建構模式](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=zh-tw)中使用程式開發輔助等功能，進行直覺式程式開發。訂閱者在 [Playground](https://aistudio.google.com/prompts/new_chat?hl=zh-tw) 和 [Build](https://aistudio.google.com/apps?hl=zh-tw) 介面中，可享高於免費方案的每日基本配額。每日上限是透過重設來強制執行，而非滾動時間範圍，確保您在轉換至 Cloud Billing 的正式環境規模開發作業前，能享有流暢的開發體驗。

| 方案 | AI Studio 用量 | 模型存取權和福利 |
| --- | --- | --- |
| **免費** | 配額較低 | 基本用量和存取權，可選擇升級以享有更多功能。 |
| **AI Pro** | 提高配額 | 使用 [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=zh-tw)、Gemini Pro、Nano Banana 和 Lyria 等進階模型。 |
| **AI Ultra** | 配額最高 | 享有原型設計、開發和 [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=zh-tw) 等先進前沿模型的最高用量。 |

## Gemini API 用量

AI Studio 的每日基準訂閱配額用盡後，您可以使用已啟用 Cloud Billing 的 Gemini API 金鑰，直接按 Gemini API 的要求次數付費，繼續執行工作流程。您可以在 [AI Studio 資訊主頁](https://aistudio.google.com/projects?hl=zh-tw)查看專案和 API 金鑰的 Gemini API 用量。

訂閱者只要啟用 Google Cloud Platform (GCP) 專案和 Cloud Billing，即可每月獲得 [Google Developer Program](https://developers.google.com/program?hl=zh-tw) 提供的 Cloud 抵免額，用於 Gemini API 等 Cloud 服務。預付和後付的使用與計費方式維持不變。如果是預付帳單使用者，AI Studio 的付費餘額必須大於 $0 美元，才能啟用促銷抵免額。系統會優先套用符合資格的 Google Cloud 抵免額 (如有)。[瞭解詳情](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw#billing-plans)。

Google AI 訂閱方案整合服務可降低進階實驗和開發的門檻。不過，如要大規模部署正式版，建議使用 Google Cloud 雲端專案、[Google Cloud 入門級](https://cloud.google.com/blog/topics/developers-practitioners/the-starter-tier-for-google-ai-studio-explained?hl=zh-tw) 和 Gemini API 金鑰。

## 限制和相容性

- **僅限 AI Studio UI：**Google AI 方案的開發人員福利，僅適用於 Google AI Studio 網頁介面。直接使用 Gemini API (例如使用 API 金鑰或外部應用程式) 則會另外計費及管理。不過，您可以在其他 Google 產品中使用訂閱方案 (請參閱 [Google AI 方案](https://one.google.com/about/google-ai-plans/?hl=zh-tw))。
- **與 API 計費方式不同：**AI Studio 的 Google AI 方案與 [Gemini API 用量級別](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw)分開，後者涵蓋開發和正式環境 API 用量。
- **Google One 點數：** [Google One AI 點數](https://support.google.com/googleone/answer/16287445?hl=zh-tw)是獨立的點數系統，不適用於 AI Studio，也不會與 Google Cloud 抵免額重疊。
- **Gemini 4 Argon 存取權：**免費方案不提供 [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=zh-tw)。
- **代理存取權：**Google AI 方案不包含 AI Studio 代理 (Deep Research 和 Antigravity 預先發布版) 的存取權，須使用[付費 API 金鑰](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw#setup-billing)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-16 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-16 (世界標準時間)。"],[],[]]
