---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=zh-TW
fetched_at: 2026-08-31T06:43:18.941001+00:00
title: "\u5408\u4f5c\u5925\u4f34\u548c\u7a0b\u5f0f\u5eab\u6574\u5408 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 合作夥伴和程式庫整合

本指南將說明如何運用 Gemini API 建構程式庫、平台和閘道的架構策略。內容詳細說明使用官方 GenAI SDK、Direct API (REST/gRPC) 和 OpenAI 相容層之間的技術取捨。

如果您要為其他開發人員建構工具 (例如開放原始碼架構、企業閘道或 SaaS 聚合器)，並需要針對依附元件衛生、套件大小或功能同位進行最佳化，請參閱本指南。

## 什麼是合作夥伴整合？

合作夥伴是指在 Gemini API 和使用者開發人員之間建立整合的任何人。我們將合作夥伴分為四種原型。找出最符合您需求的選項，有助於選擇正確的整合路徑。

#### 生態系統架構

- **適用對象：**開放原始碼架構 (例如 LangChain、LlamaIndex、Spring AI) 或語言專屬用戶端的維護人員。
- **目標：**廣泛相容性。您希望程式庫能在使用者選擇的任何環境中運作，且不會強制發生衝突。

#### 執行階段和邊緣平台

- **適用對象：**SaaS 平台、AI 閘道或雲端基礎架構供應商 (例如 Vercel、Cloudflare、Zapier)，這些平台/供應商會在受限環境中執行程式碼。
- **您的目標：**成效。您需要低延遲、最小的套件大小，以及快速的冷啟動。

#### 集結網站

- **適用對象：**平台、Proxy 或內部「模型花園」，可將多個不同 LLM 供應商 (例如 OpenAI、Anthropic、Google) 的存取權，統一整合至單一介面。
- **目標：**可攜性和一致性。

#### 企業閘道

- **適用對象：**大型企業的內部平台工程團隊，為數百名內部開發人員建構「黃金途徑」。
- **目標：**標準化、管理及統一驗證。

## 功能比較概要

**全球最佳做法：**無論選擇哪種路徑，所有合作夥伴都必須傳送 [`x-goog-api-client`
標頭](#client-id)。

| 如果您是... | 建議路徑 | 主要優點 | 主要缺點 | 最佳做法 |
| --- | --- | --- | --- | --- |
| **企業閘道、生態系統架構** | **[Google GenAI SDK](#genai-sdk)** | **Gemini Enterprise Agent Platform 的同等功能和速度。**內建類型、驗證和複雜功能 (例如檔案上傳) 的處理機制。順暢遷移至 Google Cloud。 | **依附元件權重。**遞移依附元件可能很複雜，且不在您的控管範圍內。僅限支援的語言 (Python/Node/Go/Java)。 | **鎖定版本。**在內部基礎映像檔中釘選 SDK 版本，確保各團隊的穩定性。 |
| **生態系統架構、邊緣平台和匯總工具** | **[直接 API](#rest)**  *(REST / gRPC)* | **零依附元件。**您可以控管 HTTP 用戶端和確切的套件大小。具備所有 API 和模型功能的完整存取權。 | **開發人員負擔高。**JSON 結構可能深層巢狀化，需要嚴格的手動驗證和型別檢查。 | **使用 OpenAPI 規格。**使用官方規格自動產生型別，不必手動撰寫。 |
| **使用 OpenAI SDK 的匯總工具，僅需以文字為基礎的工作流程**  *(針對舊版可攜性進行最佳化)* | **[OpenAI 相容性](#openai)** | **即時可攜性。**重複使用現有的 OpenAI 相容程式碼或程式庫。 | **功能上限。**你可能無法使用特定機型專屬功能 (原生影片、快取)。 | **遷移計畫**。您可以使用這項功能快速驗證，但建議升級至 Direct API，以使用完整的 API 功能。 |

## 整合 Google GenAI SDK

就架構而言，實作 [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-tw) 通常是最簡單的方法，因為支援的語言程式碼行數最少。

對內部平台團隊而言，主要交付項目通常是「黃金路徑」，可讓產品工程師快速採取行動，同時遵守安全政策。

**福利：**

- **Gemini Enterprise Agent Platform 遷移作業的統一介面：**內部開發人員通常會使用 API 金鑰 (Gemini API) 製作原型，並部署至 Gemini Enterprise Agent Platform (IAM)，確保符合生產環境的規範。SDK 會將這些驗證差異抽象化。同樣地，您也可以實作一個程式碼路徑，支援兩組使用者。
- **用戶端輔助程式：**SDK 包含慣用公用程式，可減少複雜工作的樣板。
  - *示例：*直接在提示中支援 `PIL` 圖片物件、自動呼叫函式，以及全面類型。
- **搶先使用新功能：**透過 SDK，您可以在新 API 功能推出時立即使用。
- **更完善的程式碼生成支援：**安裝本機 SDK 後，型別定義和文件字串會公開給程式碼助理 (例如 Cursor、Copilot)。與產生原始 REST 要求相比，這個脈絡可提高程式碼生成準確度。

**取捨：**

- **依附元件權重和複雜度：**SDK 有自己的依附元件，可能會增加套裝組合大小，並造成供應鏈風險。
- **版本管理：**新的 API 功能通常會固定在最低 SDK 版本。您可能需要向使用者推送更新，才能存取新功能或模型，有時這可能需要變更影響使用者的轉換依附元件。
- **通訊協定限制：**SDK 僅支援主要 API 的 HTTPS 和 Live API 的 WebSocket (WSS)。高階 SDK 用戶端不支援 gRPC。
- **語言支援：**SDK 支援*目前*的語言版本。如需支援產品停產 (EOL) 版本 (例如 Python 3.9)，您必須維護分支版本。

**最佳做法：**

- **鎖定版本：**在內部基礎映像檔中固定 SDK 版本，確保各團隊的穩定性。

## 直接整合 API

如果您要將程式庫發布給數千名開發人員、在受限環境中執行，或是建構需要 Gemini 最新功能的匯總工具，可能需要使用 REST 或 gRPC 直接整合 API。

**福利：**

- **完整功能存取權：**與 OpenAI 相容層不同，直接使用 API 可啟用 Gemini 專屬功能，例如上傳至 File API、建立內容快取，以及使用雙向 Live API。
- **依附元件最少：**在依附元件因大小或稽核成本而敏感的環境中。直接透過 `fetch` 等標準程式庫使用 API，或透過 `httpx` 等包裝函式使用 API，可確保程式庫保持輕巧。
- **不限語言：**這是唯一適用於 SDK 未涵蓋語言的路徑，例如 Rust、PHP 和 Ruby，因為沒有語言限制。
- **效能：**Direct API 的初始化負擔為零，可將無伺服器函式中的冷啟動情形降至最低。

**取捨：**

- **手動實作 Gemini Enterprise Agent Platform：**與 SDK 不同，直接使用 API 不會自動處理 AI Studio (API 金鑰) 和 Gemini Enterprise Agent Platform (IAM) 之間的驗證差異。如要同時支援這兩個環境，請分別導入驗證處理常式。
- **沒有原生型別或輔助程式：**除非自行實作，否則您不會取得要求物件的程式碼完成或編譯時間檢查。沒有用戶端「輔助程式」(例如函式到結構定義的轉換器)，因此您必須手動編寫這個邏輯。

**最佳做法**

我們提供機器可讀取的規格，您可以用來為程式庫產生型別定義，不必手動編寫。在建構程序中下載規格、產生型別，然後運送已編譯的程式碼。

- **端點：** `https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## 整合 OpenAI SDK

如果您是平台，且優先採用統一結構定義 (OpenAI Chat Completions) 而非模型專屬功能，這是最快路線。

**福利：**

- **低摩擦：**您通常可以透過變更 `baseURL` 和 `apiKey` 來新增 Gemini 支援。這是整合「自備金鑰」實作項目的快速方法，無須編寫新程式碼，即可新增 Gemini 支援。
- **限制：**如果您只能使用 OpenAI SDK，且不需要 File API 等進階 Gemini 功能，或手動新增對以 Google 搜尋強化事實基礎等工具的支援，建議採用這個路徑。

**取捨：**

- **功能限制：**相容性層會限制核心 Gemini 功能。各平台提供的伺服器端工具不同，可能需要手動處理，才能搭配 Gemini API 工具使用。
- **翻譯負擔：**由於 OpenAI 架構與 Gemini 架構並非 1:1 對應，因此依賴相容性層會產生一些複雜性，需要額外的實作工作才能解決，例如將使用者「搜尋」工具對應至正確的平台工具。如果需要大量特殊情況處理，為每個平台使用專屬 SDK 或 API 可能更有價值。

**最佳做法**

盡可能直接整合 Gemini API。不過，為了達到最大相容性，建議使用可辨識不同供應商的程式庫，並為您處理工具和訊息對應。

## 所有合作夥伴適用的最佳做法：識別用戶端

以平台或程式庫身分呼叫 Gemini API 時，您必須使用 `x-goog-api-client` 標頭識別用戶端。

這樣一來，Google 就能找出特定流量區隔，如果您的程式庫產生特定錯誤模式，我們就能與您聯絡，協助您進行偵錯。

使用 `company-product/version` 格式 (例如 `acme-framework/1.2.0`)。

### 導入範例

### GenAI SDK

提供 API 用戶端後，SDK 會自動將自訂標頭附加至內部標頭。

```
from google import genai

client = genai.Client(
    api_key="...",
    http_options={
        "headers": {
            "x-goog-api-client": "acme-framework/1.2.0",
        }
    }
)
```

### Direct API (REST)

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H 'x-goog-api-client: acme-framework/1.2.0' \
    -d '{...}'
```

### OpenAI SDK

```
from openai import OpenAI

client = OpenAI(
    api_key="...",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    default_headers={
        "x-goog-api-client": "acme-framework-oai/1.2.0",
    }
)
```

## 後續步驟

- 請參閱[程式庫總覽](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-tw)，瞭解 GenAI SDK
- 瀏覽 [API 參考資料](https://ai.google.dev/api?hl=zh-tw)
- 閱讀 [OpenAI 相容性指南](https://ai.google.dev/gemini-api/docs/openai?hl=zh-tw)

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-22 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-22 (世界標準時間)。"],[],[]]
