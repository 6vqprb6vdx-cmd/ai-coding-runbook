---
source_url: https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=zh-TW
fetched_at: 2026-05-11T12:38:52.007946+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 結合內建工具和函式呼叫

Gemini 允許在單一互動中組合[內建工具](https://ai.google.dev/gemini-api/docs/tools?hl=zh-tw) (例如 `google_search`) 和[函式呼叫](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-tw) (也稱為*自訂工具*)，方法是保留並公開工具呼叫的脈絡記錄。內建和自訂工具組合可支援複雜的代理功能工作流程，例如模型可先根據即時網路資料建立基準，再呼叫特定商業邏輯。

以下範例會透過 `google_search` 和自訂函式 `getWeather`，啟用內建和自訂工具組合：

### Python

```
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3-flash-preview",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## 運作方式

Gemini 3 模型使用*工具脈絡循環*，可啟用內建和自訂工具組合。工具脈絡循環可保留及公開內建工具的脈絡，並在同一互動中與自訂工具共用。

### 啟用工具組合

- 加入 [`function_declarations`](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-tw#function-declarations)，以及要使用的內建工具，即可觸發組合行為。

### API 傳回步驟

在互動回應中，API 會針對內建工具呼叫和函式 (自訂工具) 呼叫，分別傳回步驟：

- **內建工具步驟**：API 會自動管理這些步驟，並在各個回合中保留脈絡。
- **函式呼叫步驟**：API 會傳回自訂函式的 `function_call` 步驟。執行函式並傳回結果。

### 傳回步驟中的重要欄位

傳回步驟中的特定欄位對於維護工具環境和啟用工具組合至關重要：

- **`id`**：在 `function_call` 和 `function_response` 步驟中找到。可將呼叫對應至回應的專屬 ID。
- **`signature`**：位於 `thought` 步驟，以及 Gemini 3 以上模型的所有工具呼叫 (例如 `function_call`) 和結果 (例如 `function_response`) 步驟。這個加密內容可讓**工具內容在互動之間流通**。

**管理這些欄位：**

- **有狀態模式 (建議使用)**：使用 `previous_interaction_id` 時，伺服器會自動處理 `id` 和 `signature` 欄位。
- **無狀態模式**：手動管理對話記錄時，請務必在後續要求中將 `id` 和 `signature` 欄位傳回模型，以驗證真實性並保留背景資訊。如果您將完整的回應物件傳回記錄，官方 SDK 會自動處理這項作業。

### 工具專屬資料

部分內建工具會傳回使用者可見的資料引數，這些引數專屬於工具類型。

| 工具 | 使用者可見的工具呼叫引數 (如有) | 使用者可見的工具回應 (如有) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` 要瀏覽的網址 | `status`：瀏覽狀態 `retrieved_url`：瀏覽的網址 |
| **file\_search** | 無 | 無 |

## 權杖和價格

請注意，要求中內建工具呼叫的部分會計入 `prompt_token_count`。由於這些中間工具步驟現在會顯示並傳回給您，因此屬於對話記錄的一部分。這只適用於*要求*，不適用於*回應*。

Google 搜尋工具不在此限。Google 搜尋已在查詢層級套用自己的定價模式，因此不會重複收取權杖費用 (請參閱「[定價](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)」頁面)。

詳情請參閱「[符記](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=zh-tw)」頁面。

## 限制

- 啟用工具環境循環時，預設為 `validated` 模式 (不支援 `auto` 模式)。
- `google_search` 等內建工具會根據位置和目前時間資訊運作，因此如果 `system_instruction` 或 `function_declaration.description` 的位置和時間資訊有衝突，工具組合功能可能無法正常運作。

## 支援的工具

標準工具環境流通適用於伺服器端 (內建) 工具。程式碼執行也是伺服器端工具，但有自己的內建解決方案，可進行脈絡循環。電腦使用和函式呼叫是用戶端工具，也內建解決方案，可循環使用內容。

| 工具 | 執行端 | 支援情境循環 |
| --- | --- | --- |
| [Google 搜尋](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=zh-tw) | 伺服器端 | 有權限 |
| [Google 地圖](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=zh-tw) | 伺服器端 | 有權限 |
| [網址環境](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=zh-tw) | 伺服器端 | 有權限 |
| [檔案搜尋](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=zh-tw) | 伺服器端 | 有權限 |
| [程式碼執行](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=zh-tw) | 伺服器端 | 支援 (內建，使用 `code_execution` 和 `code_execution_result` 步驟) |
| [電腦使用](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=zh-tw) | 用戶端 | 支援 (內建，使用 `function_call` 和 `function_response` 步驟) |
| [自訂函式](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-tw) | 用戶端 | 支援 (內建，使用 `function_call` 和 `function_response` 步驟) |

## 後續步驟

- 進一步瞭解 Gemini API 中的[函式呼叫](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-tw)。
- 探索支援的工具：
  - [Google 搜尋](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=zh-tw)
  - [Google 地圖](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=zh-tw)
  - [網址環境](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=zh-tw)
  - [檔案搜尋](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=zh-tw)

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-09 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-09 (世界標準時間)。"],[],[]]
