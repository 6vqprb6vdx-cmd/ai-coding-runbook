---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=zh-TW
fetched_at: 2026-07-06T05:13:51.792453+00:00
title: "\u8108\u7d61\u5feb\u53d6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 脈絡快取

在典型的 AI 工作流程中，您可能會重複將相同的輸入權杖傳遞至模型。Gemini API 提供隱含快取功能，可提升效能並節省費用。

## 隱含快取

所有 Gemini 2.5 以上版本模型都會預設啟用隱式快取功能。如果要求命中快取，系統會自動將節省的費用退還給您。這項功能會自動啟用，您無需採取任何行動。下表列出各模型進行內容快取時的最低輸入權杖數：

| 模型 | 詞元數量下限 |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Gemini 3.1 Pro 預先發布版 | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

如要提高隱含快取命中的機率，請採取下列行動：

- 請嘗試在提示開頭放入大型和常見內容
- 嘗試在短時間內傳送具有類似前置字串的要求

您可以在回應物件的 `usage_metadata` (Python) 或 `usageMetadata` (JavaScript) 欄位中，查看快取命中次數。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-22 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-22 (世界標準時間)。"],[],[]]
