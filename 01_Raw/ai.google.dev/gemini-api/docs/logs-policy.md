---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=zh-TW
fetched_at: 2026-11-02T07:20:42.266309+00:00
title: "\u8cc7\u6599\u8a18\u9304\u548c\u5206\u4eab \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 資料記錄和分享

本頁面概述 [Gemini API 記錄](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-tw)的儲存和管理方式。這類記錄是開發人員擁有的 API 資料，來自已啟用計費功能的專案中支援的 Gemini API 呼叫。記錄會涵蓋從使用者要求到模型回覆的整個過程。這些記錄是您的 Google Cloud 雲端專案的私人記錄，與僅用於[濫用行為監控](https://ai.google.dev/gemini-api/docs/usage-policies?hl=zh-tw)的記錄分開。

## 可分享的資料

根據預設，系統會記錄 Interactions API 呼叫，以及 2026 年 10 月 26 日當天或之後建立的專案中的 Generate Content API 呼叫。專案擁有者隨時可以前往 AI Studio 的「Logs and Datasets」(記錄和資料集) 頁面，開啟或關閉記錄功能。記錄僅供您個人使用，您可以選擇將記錄分享給 Google 做為意見回饋，協助我們持續改良模型。

啟用記錄功能後，您可以選擇提供下列資料，協助我們改良產品及訓練模型，打造出能持續為各領域開發人員和用途提供價值的 AI 系統：

- **資料集：**使用 Google AI Studio 的「記錄和資料集」介面，從支援的 Gemini API 呼叫中選擇感興趣的記錄 (要求、回覆、中繼資料等)；透過加入資料集提供，並可在建立資料集時選擇不採用。
- **意見回饋：**查看記錄時，您可以提供意見回饋，包括按讚和倒讚評分，以及任何書面評論。

與 Google 共用資料集時，該資料集中的記錄 (包括要求和回覆) 會依據「[免付費服務](https://ai.google.dev/gemini-api/terms?hl=zh-tw#data-use-unpaid)」[條款](https://developers.google.com/terms?hl=zh-tw)處理，也就是說，資料集可能會用於開發及改良 Google 產品、服務和機器學習技術，包括改良及訓練模型。**請勿提供個人、敏感或機密資訊。**

## 我們如何使用您的資料

記錄預設最多保留 55 天。超過這個期限後，系統會自動將記錄標示為待刪除。您可以在 AI Studio 中更新專案的儲存空間保留期限，讓系統在 7、14、28 或 55 天後自動將記錄標示為刪除。

您可以建立[資料集](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-tw)，在設定的保留期限過後，繼續保留感興趣的記錄，用於下游用途，並視需要協助改善模型。儲存在資料集中的記錄檔沒有設定保留期限。

根據預設，只有啟用計費功能的專案才能使用記錄功能，因此根據我們的資料使用[條款](https://developers.google.com/terms?hl=zh-tw)，記錄中的提示和回覆不會用於產品改善或開發。

如果您選擇與 Google 共用記錄資料集，這些資料集將做為實際示範資料，協助我們進一步瞭解 AI 系統和應用程式使用的網域和情境多樣性。這類資料可能用於提升模型品質，以及訓練和評估日後的模型與服務。我們會依據[無償服務](https://ai.google.dev/gemini-api/terms?hl=zh-tw#data-use-unpaid)的資料使用條款處理這類資料。

因此，人工審查員可能會查看、標註及處理您分享的 API 輸入和輸出內容。在將資料用於改善模型之前，Google 會採取適當措施來保護使用者隱私。包括在審查員查看或加註前，將這類資料與 Google 帳戶、API 金鑰和 Cloud 專案解除連結。

## 資料權限

選擇加入提供 API 資料，即表示您確認已取得必要權限，允許 Google 按照本文件所述處理及使用資料。**請勿提供含有透過付費服務取得的敏感、機密或專屬資訊的記錄**。您根據《API 條款》中「[提交內容](https://developers.google.com/terms?hl=zh-tw#b_submission_of_content)」一節授予 Google 的授權，在適用法律要求我們使用的範圍內，也適用於您提交至「服務」的任何內容 (例如提示，包括相關系統指令、快取內容，以及圖片、影片或文件等檔案) 和任何生成的內容。

## 資料共用和意見回饋

您可以選擇加入分享資料做為範例，協助我們推動 AI 研究、Gemini API 和 Google AI Studio 的發展，讓我們能持續改進模型，因應各種情境，並建構 AI 系統，持續為各領域和用途的開發人員提供價值。

### Gemini API 貢獻者層級

開發人員加入 Gemini 貢獻者計畫後，可享特定模型的 Token 折扣，但須授權 Google 使用這些模型的資料，提供、改良及開發 Google 產品、服務和機器學習技術。

開發人員使用特定模型時，可享高達 50% 的詞元費用折扣，並享有與[標準 API](https://ai.google.dev/gemini-api/docs/optimization?hl=zh-tw) 相同的即時效能。支援的模型如下：

| 模型 | 貢獻者級別 |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#gemini-4-argon) | ✔️ |
| [Gemini 3.1 Pro 預先發布版](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#gemini-3.1-pro-preview) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#gemini-3.8-flash) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#gemini-3.5-flash-lite) | ✔️ |

**資料使用方式：**

- 為專案啟用貢獻者級別後，專案中參與模型使用的資料，將依據「[免付費服務](https://ai.google.dev/gemini-api/terms?hl=zh-tw#unpaid-services)」條款使用。您的資料會用於改善 Google 產品和機器學習技術，因此請勿提交機密或個人資訊。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-26 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-26 (世界標準時間)。"],[],[]]
