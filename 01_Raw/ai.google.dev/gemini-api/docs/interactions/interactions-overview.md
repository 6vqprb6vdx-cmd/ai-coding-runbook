---
source_url: https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=zh-TW
fetched_at: 2026-06-15T06:19:08.482765+00:00
title: "\u4e92\u52d5 API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 互動 API

**Interactions API** 是使用 Gemini 建構應用程式時，我們建議採用的新標準。這項 API 專為代理工作流程、伺服器端狀態管理，以及複雜的多模態多輪對話而設計。原始的 [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=zh-tw) API 仍完全支援。

## 為什麼要使用 Interactions API？

- **伺服器端記錄管理**：透過 `previous_interaction_id` 簡化多輪對話流程。伺服器預設會啟用狀態 (`store=true`)，但您可以設定 `store=false`，選擇無狀態行為。
- **可觀察的執行步驟**：輸入步驟可輕鬆偵錯複雜流程，並為中繼事件 (例如想法或搜尋小工具) 算繪 UI。
- **專為代理工作流程打造**：透過型別執行步驟，原生支援多步驟工具使用、自動調度管理和複雜的推論流程。
- **長期執行的工作和背景工作**：支援使用 `background=true` 將耗時的作業轉移至背景程序。這項功能支援模型 (例如「Deep Think」) 和代理程式 (例如「Deep Research」)。
- **使用新模型和功能**：未來，除了核心主線系列之外，新的模型以及新的代理能力和工具，都只會在 Interactions API 上推出。

**如果您要啟動新專案、建構代理程式應用程式，或需要伺服器端對話管理功能，請**使用 Interactions API**。如果您有符合需求的現有整合項目，或需要 Interactions API [尚未提供的功能](#limitations) (例如 Batch API 或明確快取)，請使用 [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=zh-tw)**。

## 開始使用

- **設定程式設計代理**：連線至 **Gemini 文件 MCP** 並安裝 `gemini-interactions-api` 技能，讓助理直接存取最新的開發人員文件和最佳做法。[設定程式設計代理 →](https://ai.google.dev/gemini-api/docs/coding-agents?hl=zh-tw)
- **從 `generateContent` 遷移**：如果您已整合，請按照[遷移指南](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=zh-tw)的說明，改用 Interactions API。
- **試用快速入門導覽課程**：透過[互動式 API 快速入門導覽課程](https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=zh-tw)，開始使用最簡單的運作範例。

### 功能指南

請參閱這些指南，瞭解 Interactions API 的具體功能。您可以在這些頁面使用切換按鈕，在 generateContent 和 Interactions API 之間切換：

- [生成文字](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=zh-tw)
- [圖像生成](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=zh-tw)
- [圖像解讀](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=zh-tw)
- [音訊理解](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=zh-tw)
- [影片理解](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=zh-tw)
- [文件處理](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=zh-tw)
- [函式呼叫](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-tw)
- [結構化輸出內容](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=zh-tw)
- [Deep Research 代理](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=zh-tw)
- [Flex 推論](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=zh-tw)
- [優先推論](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=zh-tw)
- [串流](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=zh-tw)

## Interactions API 的運作方式

Interactions API 的核心資源是 [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=zh-tw#Resource:Interaction)。`Interaction` 代表對話或工作中的完整回合，可做為工作階段記錄，內含互動的完整記錄，以 **執行步驟**的時間順序排列。這些步驟包括模型想法、伺服器端或用戶端工具呼叫和結果 (例如 `function_call` 和 `function_result`)，以及最終的 `model_output`。儲存的資源 (透過 `interactions.get` 擷取) 也包含 `user_input` 步驟，可提供完整脈絡，但 `interactions.create` 回應只會傳回模型產生的步驟。

呼叫 [`interactions.create`](https://ai.google.dev/api/interactions-api?hl=zh-tw#CreateInteraction) 時，您會建立新的 `Interaction` 資源。

### 使用 SDK 便利屬性存取輸出內容

雖然 Interactions API 會傳回執行步驟的結構化時間軸 (例如想法、搜尋查詢和函式呼叫)，但您不需要手動遍歷這些步驟，即可取得最終模型回應。

Google GenAI SDK 會在傳回的 `Interaction` 物件上直接提供便利屬性，方便您存取不同模態的輸出內容：

| SDK 便利屬性 | 傳回類型 | 說明 |
| --- | --- | --- |
| **`interaction.output_text`** | 字串 | 傳回模型回覆中的最後一個文字區塊。如果回覆內容分散在多個連續的 `TextContent` 區塊中，系統會自動合併這些區塊。不包括以非文字內容 (例如想法、圖片、音訊或工具呼叫) 分隔的先前文字區塊。如為複雜或交錯的多模態回覆，您必須手動疊代 `steps`。 |
| **`interaction.output_image`** | ImageContent 或 `None` | 傳回模型在目前要求中生成的最後一個圖片區塊。 |
| **`interaction.output_audio`** | AudioContent 或 `None` | 傳回模型在目前要求中生成的最後一個音訊區塊。 |

如要進行進階用途 (例如算繪中間思考程序、檢查逐步工具呼叫或偵錯)，您仍可手動檢查及遍歷原始 `interaction.steps` 時間軸。

### 伺服器端狀態管理

您可以在後續呼叫中使用 `previous_interaction_id` 參數，藉此使用已完成互動的 `id` 繼續對話。伺服器會使用這組 ID 擷取對話記錄，因此您不必重新傳送完整的對話記錄。

`previous_interaction_id` 參數只會使用 `previous_interaction_id` 保留對話記錄 (輸入和輸出內容)。其他參數為**互動範圍**，且僅適用於目前產生的特定互動：

- `tools`
- `system_instruction`
- `generation_config` (包括 `thinking_level`、`temperature` 等)

也就是說，如要套用這些參數，您必須在每次新互動中重新指定。這項伺服器端狀態管理功能為選用功能，您也可以在無狀態模式下運作，方法是在每個要求中傳送完整的對話記錄。

### 背景執行

如要長時間執行工作，可以在要求中設定 `background=true`，在背景執行互動。這項功能支援以下兩種情況：

- **模型**：適用於處理時間較長的工作，例如使用[思考](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=zh-tw)功能的工作。
- **代理**：長時間執行的代理工作流程 (例如[Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=zh-tw)) 必須使用代理。

在背景執行時：

- 您必須設定 `store=true` (預設值)，因為系統需要儲存互動資源，方便您日後擷取。
- 對 `interactions.create` 的初始呼叫會立即傳回狀態為 `in_progress` 的結果。
- 您可以透過互動 ID 呼叫 `interactions.get`，擷取互動狀態和結果，也可以設定[網頁掛鉤](https://ai.google.dev/gemini-api/docs/interactions/webhooks?hl=zh-tw)，在互動完成時接收通知。
- 您也可以[串流](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=zh-tw#streaming-background)互動內容，接收進度更新。

### 資料儲存與保留

根據預設，API 會儲存所有 Interaction 物件 (`store=true`)，以簡化伺服器端狀態管理功能 (使用 `previous_interaction_id`)、背景執行作業 (使用 `background=true`) 和觀測能力用途的使用。

- **付費層級**：系統會保留互動記錄 **55 天**。
- **免費方案**：系統會保留互動記錄 **1 天**。

如果不希望系統執行上述作業，可以在要求中`store=false`。這項控制項與狀態管理功能無關，您可以選擇不儲存任何互動。不過請注意，`store=false` 與 `background=true` 不相容，且會禁止在後續回合使用 `previous_interaction_id`。

您隨時可以使用 [API 參考資料](https://ai.google.dev/api/interactions-api?hl=zh-tw)中的刪除方法，刪除儲存的互動記錄。只有在知道互動 ID 的情況下，才能刪除互動記錄。

超過保留期限後，系統會自動刪除資料。

系統會根據[條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw)處理 Interaction 物件。

## 最佳做法

- **快取命中率**：使用 `previous_interaction_id` 繼續對話時，系統可以更輕鬆地運用對話記錄的隱含快取，進而提升效能並降低費用。
- **混合互動**：您可以在對話中彈性混合搭配使用 Agent 和模型互動。舉例來說，您可以先使用 Deep Research 代理等專用代理收集初始資料，然後使用標準 Gemini 模型執行後續工作，例如摘要或重新格式化，並使用 `previous_interaction_id` 連結這些步驟。

## 支援的模型和代理程式

| 模型名稱 | 類型 | 模型 ID |
| --- | --- | --- |
| Gemini 3.5 Flash | 模型 | `gemini-3.5-flash` |
| Gemini 3.1 Flash-Lite | 模型 | `gemini-3.1-flash-lite` |
| Gemini 3.1 Pro 預先發布版 | 模型 | `gemini-3.1-pro-preview` |
| Gemini 3 Flash 預先發布版 | 模型 | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | 模型 | `gemini-2.5-pro` |
| Gemini 2.5 Flash | 模型 | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | 模型 | `gemini-2.5-flash-lite` |
| Lyria 3 剪輯片段預覽 | 模型 | `lyria-3-clip-preview` |
| Lyria 3 Pro 預先發布版 | 模型 | `lyria-3-pro-preview` |
| Deep Research 預先發布版 | 代理 | `deep-research-pro-preview-12-2025` |
| Deep Research 預先發布版 | 代理 | `deep-research-preview-04-2026` |
| Deep Research 預先發布版 | 代理 | `deep-research-max-preview-04-2026` |

## SDK

您可以使用最新版的 Google GenAI SDK，存取 Interactions API。

- 在 Python 中，這是 `1.55.0` 版本之後的 `google-genai` 套件。
- 在 JavaScript 中，這是 `1.33.0` 版本以上的 `@google/genai` 套件。

如要進一步瞭解如何安裝 SDK，請參閱「[程式庫](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-tw)」頁面。

## 限制

- **Beta 版狀態**：Interactions API 目前為 Beta 版/預覽版。功能和結構定義可能會變更。
- **遠端 MCP**：Gemini 3 不支援遠端 MCP，但這項功能即將推出。

[`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=zh-tw) API 支援下列功能，但 Interactions API **尚未提供**這些功能：

- **[影片中繼資料](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=zh-tw)**：`video_metadata` 欄位，用於設定剪輯間隔和自訂影格速率，以利瞭解影片內容。
- **[批次 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw)**
- **[自動函式呼叫 (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=zh-tw#automatic_function_calling_python_only)**
- **[明確快取](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=zh-tw)**：請注意，伺服器端隱含快取可透過 `previous_interaction_id` 在 Interactions API 中使用。

## 破壞性變更

目前 Interactions API 處於早期 Beta 版階段。我們會根據實際使用情況和開發人員意見回饋，積極開發及改良 API 功能、資源結構定義和 SDK 介面。因此**可能會發生重大變更**。

現有的破壞性變更：

- **步驟結構定義**：新的步驟陣列會取代輸出陣列，提供每個互動回合的結構化時間軸。

如要瞭解最近的重大變更，以及如何遷移，請參閱「[重大變更遷移指南 (2026 年 5 月)](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-tw)」。

其他可能的更新包括輸入和輸出內容的結構定義、SDK 方法簽章和物件結構，以及特定功能行為的變更。

對於實際工作負載，您應繼續使用標準 [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=zh-tw) API。這仍是穩定部署作業的建議做法，我們也會持續積極開發及維護。

## 意見回饋

您的意見回饋對 Interactions API 的開發至關重要。歡迎前往 [Google AI 開發人員社群論壇](https://discuss.ai.google.dev/c/gemini-api/4?hl=zh-tw)分享想法、回報錯誤或要求功能。

## 後續步驟

- 請試用 [Interactions API 快速入門筆記本](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=zh-tw)。
- 瞭解如何使用[串流互動](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=zh-tw)即時處理回覆。
- 進一步瞭解 [Gemini Deep Research 代理程式](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-08 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-08 (世界標準時間)。"],[],[]]
