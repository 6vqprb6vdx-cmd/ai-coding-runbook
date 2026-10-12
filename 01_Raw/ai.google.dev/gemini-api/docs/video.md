---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=zh-TW
fetched_at: 2026-10-12T07:13:31.772209+00:00
title: "Gemini API \u5f71\u7247\u751f\u6210\u529f\u80fd \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Gemini API 影片生成功能

Gemini API 提供兩種影片生成模型：[Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=zh-tw) 和 [Veo](https://ai.google.dev/gemini-api/docs/veo?hl=zh-tw)。兩者適用於不同的工作流程。

將 Gemini Omni Flash 設為影片生成的預設模型。這項模型可提供優異的影片連貫性、多輸入推論 (同時支援文字、圖片、音訊和影片輸入)、角色一致性、事實準確度，以及多輪對話式編輯 (例如更換元素或變更視角)。使用 Veo 3.1 處理特定功能，例如場景擴充、最後一格控制，或整合舊版管道。

## Gemini Omni Flash

Gemini Omni Flash 是快速的多模態模型，可生成影片及透過對話編輯影片。這項 API 擅長快速將文字提示和圖片轉換為短片，並可讓您使用 Interactions API，在多個回合中修正結果。

[開始使用 Gemini Omni Flash →](https://ai.google.dev/gemini-api/docs/omni?hl=zh-tw)

## Veo 3.1

Veo 3.1 是一種模型，可生成含有原生音訊的影片。透過 `generateContent` API，這項功能支援影片擴充、特定影格生成，以及以圖片為基礎的導向等功能。

[開始使用 Veo 3.1 →](https://ai.google.dev/gemini-api/docs/veo?hl=zh-tw)

## 影片解讀

如要擷取及分析現有影片內容，而非生成新影片，請參閱[影片理解指南](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-30 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-30 (世界標準時間)。"],[],[]]
