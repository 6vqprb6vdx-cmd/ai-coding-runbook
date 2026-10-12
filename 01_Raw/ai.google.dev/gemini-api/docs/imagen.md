---
source_url: https://ai.google.dev/gemini-api/docs/imagen?hl=zh-TW
fetched_at: 2026-10-12T07:01:27.614206+00:00
title: "\u4f7f\u7528 Imagen \u751f\u6210\u5716\u7247 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)

提供意見

# 使用 Imagen 生成圖片

Imagen 是 Google 的舊版圖像生成模型。這項服務現已關閉，且不再支援 Gemini API。

## 遷移至 Nano Banana

改用 Nano Banana 生成圖像：

- **模型名稱**：使用 `gemini-2.5-flash-image` (或 Nano Banana 2 模型，例如 `gemini-3.1-flash-image`) 取代 Imagen 模型名稱。
- **方法**：請使用 `client.models.generate_content`，不要使用 `client.models.generate_images`。
- **回應處理**：Nano Banana 會傳回含有圖片資料的內容部分，而非特定圖片回應物件。

詳情和範例請參閱[圖片生成指南](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-18 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-18 (世界標準時間)。"],[],[]]
