---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-TW
fetched_at: 2026-07-27T04:49:00.084268+00:00
title: "Antigravity \u4ee3\u7406\u7a0b\u5f0f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Antigravity 代理程式

Antigravity 代理是 Gemini API 中的一般用途受管理代理。只要呼叫單一 API，您就能在 Google 代管的專屬安全 Linux 沙箱中，取得可進行推理、執行程式碼、管理檔案及瀏覽網頁的代理程式。

這項工具採用 Gemini 3.6 Flash 技術，並使用與 Antigravity IDE 相同的架構。您可以使用 `agent_config` 設定基礎 Gemini 模型。可透過 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 和 [Google AI Studio](https://aistudio.google.com?hl=zh-tw) 使用。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## 功能

每次呼叫都會佈建 Linux 沙箱，並啟動工具使用迴圈。代理會規劃、行動、觀察結果，並重複執行這些步驟，直到完成工作為止。

- **執行程式碼：**執行 Bash、Python 和 Node.js 指令。安裝套件、執行測試、建構應用程式。
- **檔案管理：**讀取、寫入、編輯、搜尋及列出沙箱中的檔案。檔案會保留在所有互動中。
- **網路存取權：**Google 搜尋和網址擷取功能，可取得資料。
- **內容壓縮：**自動壓縮內容 (約 135, 000 個權杖時觸發)，支援長時間的多輪對話，不會遺失內容或達到權杖上限。

如要瞭解如何使用多輪對話和串流功能，請參閱[快速入門導覽課程](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=zh-tw)。

## 支援的工具

根據預設，代理程式可以存取 `code_execution`、`google_search` 和 `url_context`。指定 `environment` 參數時，系統會自動啟用檔案系統工具。您也可以定義**自訂函式**，將代理程式連結至自己的 API 和工具。只有在自訂或限制預設集，或是新增自訂函式時，才需要指定 `tools` 參數。

| 工具 | 輸入值 | 說明 |
| --- | --- | --- |
| 程式碼執行 | `code_execution` | 執行殼層指令 (bash、Python、Node)，並擷取 stdout/stderr。 |
| Google 搜尋 | `google_search` | 搜尋公開網路。 |
| 網址背景資訊 | `url_context` | 擷取及閱讀網頁。 |
| 檔案系統 | *(透過 `environment` 啟用)* | 在沙箱中讀取、寫入、編輯、搜尋及列出檔案。沒有獨立的工具類型，只要設定 `environment`，就會自動啟用。 |
| 自訂函式 | `function` | 定義代理可要求執行的自訂函式。請參閱[函式呼叫](#function-calling)。 |
| 遠端 MCP 伺服器 | `mcp_server` | 將外部 Model Context Protocol (MCP) 伺服器註冊為工具。請參閱「[MCP 伺服器](#mcp-servers)」。 |

如要限制代理程式只能使用特定工具，請只傳遞您需要的工具：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## 多模態輸入

Antigravity 代理程式支援多模態輸入，目前僅支援 `text` 和 `image` 輸入內容。圖片必須以內嵌的 Base64 編碼字串 (`data`) 提供。

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### REST

```
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## 函式呼叫

您可以定義代理可叫用的自訂工具，透過函式呼叫將 Antigravity 代理程式連結至外部 API 和資料庫。如要瞭解一般概念，請參閱「[使用 Gemini API 進行函式呼叫](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-tw)」。

以下範例說明 2 輪互動。代理程式會先要求自訂 `get_weather` 函式呼叫，用戶端執行該呼叫後，會在第二輪傳回結果。

### Python

```
from google import genai

client = genai.Client()

# 1. Define the custom function
get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and country, e.g. San Francisco, USA",
            }
        },
        "required": ["location"],
    },
}

# 2. Call the agent with the custom tool (Turn 1)
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[
        {"type": "code_execution"},  # Enable default code execution
        get_weather_tool,            # Add custom function
    ],
)

# Check if the agent requested a function call
if interaction.status == "requires_action":
    # Find function calls that do not have a matching function result.
    # Filesystem tools (like write_file) are also represented as function calls
    # but are executed automatically by the environment.
    executed_calls = {step.call_id for step in interaction.steps if step.type == "function_result"}
    pending_calls = [step for step in interaction.steps if step.type == "function_call" and step.id not in executed_calls]

    if pending_calls:
        fc_step = pending_calls[0]
        print(f"Function to call: {fc_step.name} (ID: {fc_step.id})")
        print(f"Arguments: {fc_step.arguments}")

        # 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        function_result = {
            "temperature": 23,
            "unit": "celsius"
        }

        final_interaction = client.interactions.create(
            agent="antigravity-preview-05-2026",
            previous_interaction_id=interaction.id,  # Reference the interaction ID
            environment=interaction.environment_id,
            input=[
                {
                    "type": "function_result",
                    "name": fc_step.name,
                    "call_id": fc_step.id,
                    "result": function_result,
                }
            ],
        )

        print(final_interaction.output_text)
        # Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    else:
        print("No pending function calls.")
else:
    print(f"Interaction completed with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// 1. Define the custom function
const get_weather_tool = {
  type: "function",
  name: "get_weather",
  description: "Gets the current weather for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city and country, e.g. San Francisco, USA",
      },
    },
    required: ["location"],
  },
};

// 2. Call the agent with the custom tool (Turn 1)
const interaction = await client.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "What is the weather in Tokyo?",
  environment: "remote",
  tools: [
    { type: "code_execution" },
    get_weather_tool,
  ],
}, { timeout: 300000 });

if (interaction.status === "requires_action") {
  // Find function calls that do not have a matching function result.
  // Filesystem tools (like write_file) are also represented as function calls
  // but are executed automatically by the environment.
  const executedCalls = new Set(
    interaction.steps
      .filter(s => s.type === "function_result")
      .map(s => s.call_id)
  );
  const pendingCalls = interaction.steps.filter(
    s => s.type === "function_call" && !executedCalls.has(s.id)
  );

  if (pendingCalls.length > 0) {
    const fcStep = pendingCalls[0];
    console.log(`Function to call: ${fcStep.name} (ID: ${fcStep.id})`);

    // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
    const functionResult = {
      temperature: 23,
      unit: "celsius"
    };

    const finalInteraction = await client.interactions.create({
      agent: "antigravity-preview-05-2026",
      previous_interaction_id: interaction.id, // Reference the interaction ID
      environment: interaction.environment_id,
      input: [
        {
          type: "function_result",
          name: fcStep.name,
          call_id: fcStep.id,
          result: functionResult,
        }
      ],
    }, { timeout: 300000 });

    console.log(finalInteraction.output_text);
  } else {
    console.log("No pending function calls.");
  }
} else {
  console.log(`Interaction completed with status: ${interaction.status}`);
}
```

### REST

```
# 1. Turn 1: Request function call
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [
          {"type": "code_execution"},
          {
              "type": "function",
              "name": "get_weather",
              "description": "Gets the current weather for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string"}
                  },
                  "required": ["location"]
              }
          }
      ]
  }')

# Extract interaction ID, environment ID, and call ID (requires jq)
INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')
ENVIRONMENT_ID=$(echo $RESPONSE | jq -r '.environment_id')
CALL_ID=$(echo $RESPONSE | jq -r '.steps[] | select(.type=="function_call") | .id')

# 2. Turn 2: Send function result back using variables
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"input\": [
          {
              \"type\": \"function_result\",
              \"name\": \"get_weather\",
              \"call_id\": \"$CALL_ID\",
              \"result\": {
                  \"temperature\": 23,
                  \"unit\": \"celsius\"
              }
          }
      ]
  }"
```

## MCP 伺服器

註冊遠端 Model Context Protocol (MCP) 伺服器，即可將 Antigravity 代理程式連線至外部工具。代理程式支援透過可串流的 HTTP 連至遠端 MCP 伺服器。

註冊 MCP 伺服器時，您必須在 `tools` 陣列中指定下列欄位：

| 欄位 | 類型 | 必要 | 說明 |
| --- | --- | --- | --- |
| `type` | 字串 | 是 | 必須為 `"mcp_server"`。 |
| `name` | 字串 | 是 | 伺服器的專屬 ID。必須是嚴格的小寫英數字元 (與 `^[a-z0-9_-]+$` 相符)。 |
| `url` | 字串 | 是 | 遠端 MCP 伺服器的端點網址。 |
| `headers` | 物件 | 否 | 隨要求傳送的自訂標頭 (例如驗證)。 |
| `allowed_tools` | 陣列 | 否 | 允許執行的工具名稱清單。如果省略，系統會允許所有工具。 |

### Python

```
from google import genai

client = genai.Client()

# Register a remote HTTP MCP server
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "weather", # Must be lowercase
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "What is the weather in Tokyo?",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "weather", // Must be lowercase
        url: "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [{
          "type": "mcp_server",
          "name": "weather",
          "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
      }]
  }'
```

## 多種模型供您選擇

對於 `antigravity-preview-05-2026`，預設模型為 **Gemini 3.6 Flash** (`gemini-3.6-flash`)。如果省略 `agent_config`，代理程式預設為 `gemini-3.6-flash`。

你可以使用 `agent_config` 設定基礎 Gemini 模型，以最佳化速度、成本或推論能力。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Summarize the key differences between functional and object-oriented programming.",
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.5-flash-lite",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Summarize the key differences between functional and object-oriented programming.",
    environment: "remote",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.5-flash-lite",
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Summarize the key differences between functional and object-oriented programming.",
      "environment": "remote",
      "agent_config": {
          "type": "antigravity",
          "model": "gemini-3.5-flash-lite"
      }
  }'
```

`agent_config.model` 支援的值如下：

| 模型 | `agent_config.model` 中的值 | 說明 |
| --- | --- | --- |
| **Gemini 3.6 Flash** (預設) | `gemini-3.6-flash` | 預設的平衡模型，適用於推論、程式設計和工具使用。 |
| **Gemini 3.5 Flash** | `gemini-3.5-flash` | 適用於一般代理工作流程的上一代 Flash 模型。 |
| **Gemini 3.5 Flash-Lite** | `gemini-3.5-flash-lite` | 輕量型模型，專為低延遲和成本敏感型工作最佳化。 |

使用 `agents.create` 建立受管理代理程式時，請傳遞 `base_agent` 和 `agent_config`，以相同方式設定模型。請注意，使用 `agents.create` 建立的代管代理程式，無法在互動時覆寫模型。模型會鎖定為建立代理程式時設定的模型。這可確保工具呼叫行為可預測、偵錯一致，並遵守安全邊界。

## 自訂代理程式

您可以自訂 Antigravity 代理程式的指令、工具和環境，藉此擴充其功能。代理程式支援檔案系統原生自訂方法：您可以將 `AGENTS.md` 等檔案掛接至沙箱中的 `.agents/skills/`，做為指令和技能，也可以在互動時內嵌傳遞設定。您可以內嵌疊代設定，然後在準備就緒時將其儲存為受管理代理程式。

如要進一步瞭解如何建構自訂代理程式，請參閱「[建構 Managed Agents](https://ai.google.dev/gemini-api/docs/custom-agents?hl=zh-tw)」。

## 背景執行

如果代理的工作涉及多步驟推論、執行程式碼或檔案作業，可能需要幾分鐘才能完成。使用 `background=True` 以非同步方式執行互動。API 會立即傳回互動 ID，您可輪詢該 ID，直到狀態為 `completed` 或 `failed` 為止。

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the interaction in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run a complex analysis on the repository.",
    environment="remote",
    background=True,
)

print(f"Interaction started in background: {interaction.id}")

# 2. Poll for completion
while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run a complex analysis on the repository.",
    environment: "remote",
    background: true,
});

console.log(`Interaction started in background: ${interaction.id}`);

let result = interaction;
while (result.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    result = await client.interactions.get(interaction.id);
}

if (result.status === "completed") {
    console.log(result.output_text);
} else {
    console.log(`Finished with status: ${result.status}`);
}
```

### REST

```
# 1. Start the interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Run a complex analysis on the repository.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll for results (repeat until status is "completed")
curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

背景執行功能需要 `store=True` (預設值)。如要在背景執行期間即時更新進度，請參閱「[串流背景互動](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=zh-tw#streaming-background)」。

您可以使用 `cancel` 方法取消正在執行的背景互動。

### Python

```
client.interactions.cancel(id="INTERACTION_ID")
```

### JavaScript

```
await client.interactions.cancel("INTERACTION_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID:cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

**多輪對話與背景執行**

如果背景互動涉及有狀態的工具 (例如在沙箱中執行程式碼)，請使用完成互動中的 `environment_id`，在相同環境中繼續作業。這樣一來，代理程式就能從上次停止的地方繼續作業，所有檔案和狀態都會保持不變。

### Python

```
import time
from google import genai

client = genai.Client()

# First turn: run a task in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Clone https://github.com/google/generative-ai-python and run its tests.",
    environment="remote",
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Second turn: continue in the same environment
followup = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Fix any failing tests and re-run them.",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    background=True,
)

while followup.status == "in_progress":
    time.sleep(5)
    followup = client.interactions.get(id=followup.id)

print(followup.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First turn: run a task in the background
let interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Clone https://github.com/google/generative-ai-python and run its tests.",
    environment: "remote",
    background: true,
});

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

// Second turn: continue in the same environment
let followup = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Fix any failing tests and re-run them.",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    background: true,
});

while (followup.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    followup = await client.interactions.get(followup.id);
}

console.log(followup.output_text);
```

### REST

```
# 1. Start first interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Clone https://github.com/google/generative-ai-python and run its tests.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll until completed (repeat until status is "completed")
RESULT=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY")

ENVIRONMENT_ID=$(echo $RESULT | jq -r '.environment_id')

# 3. Continue in the same environment
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"input\": \"Fix any failing tests and re-run them.\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"background\": true
  }"
```

## 環境

每次呼叫都會建立或重複使用 Linux 沙箱。`environment` 參數有三種形式：

| 表單 | 說明 |
| --- | --- |
| `"remote"` | 使用預設設定佈建新的沙箱。 |
| `"env_abc123"` | 透過 ID 重複使用現有環境，保留所有檔案和狀態。 |
| `{...}` | 完整`EnvironmentConfig`，可自訂來源和網路規則。 |

如要進一步瞭解來源 (Git、GCS、內嵌)、網路、生命週期和資源限制，請參閱「[環境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw)」。

## 觸發條件

您可以透過觸發條件，排定代理程式的執行時間 (使用 cron 排程)。觸發條件會將代理程式、環境、提示和排程繫結至持續性資源，並在沒有人為介入的情況下觸發。每次執行作業都會重複使用相同的環境，因此在一次執行作業中建立的檔案會保留下來，並在下次執行作業時顯示。

### 建立觸發條件

指定 Cron 排程、時區和互動設定，即可建立觸發條件。觸發程序會以 `active` 狀態啟動，並在下一個相符的 cron 時間觸發。儲存傳回的 `id`，以便在後續呼叫中管理觸發條件。

### Python

```
from google import genai

client = genai.Client()

trigger = client.triggers.create(
    schedule="0 9 * * *",
    time_zone="America/Argentina/Buenos_Aires",
    display_name="issue-solver",
    interaction={
        "agent": "antigravity-preview-05-2026",
        "input": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        "environment": {
            "type": "remote",
            "network": {
                "allowlist": [
                    {
                        "domain": "api.github.com",
                        "transform": {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                        },
                    },
                    {"domain": "github.com"},
                ]
            },
        },
    },
)

print(f"Trigger created: {trigger.id}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const trigger = await client.triggers.create({
    schedule: "0 9 * * *",
    time_zone: "America/Argentina/Buenos_Aires",
    display_name: "issue-solver",
    interaction: {
        agent: "antigravity-preview-05-2026",
        input: [{
            type: "text",
            text: "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        }],
        environment: {
            type: "remote",
            network: {
                allowlist: [
                    {
                        domain: "api.github.com",
                        transform: {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                        },
                    },
                    { domain: "github.com" },
                ],
            },
        },
    },
});

console.log(`Trigger created: ${trigger.id}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "schedule": "0 9 * * *",
      "time_zone": "America/Argentina/Buenos_Aires",
      "display_name": "issue-solver",
      "interaction": {
          "agent": "antigravity-preview-05-2026",
          "input": [{"type": "text", "text": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled accepted, skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."}],
          "environment": {
              "type": "remote",
              "network": {
                  "allowlist": [
                      {
                          "domain": "api.github.com",
                          "transform": {
                              "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                          }
                      },
                      {"domain": "github.com"}
                  ]
              }
          }
      }
  }'
```

`CreateTrigger` 要求接受下列欄位：

| 欄位 | 類型 | 必要 | 說明 |
| --- | --- | --- | --- |
| `schedule` | 字串 | 是 | Cron 運算式 (例如每小時的 `0 * * * *`，或工作日早上的 `0 9 * * 1-5`)。 |
| `time_zone` | 字串 | 是 | IANA 時區 (例如 `UTC`、`America/Argentina/Buenos_Aires`)。 |
| `display_name` | 字串 | 否 | 使用者可解讀的觸發條件名稱。 |
| `max_consecutive_failures` | 整數 | 否 | 觸發程序自動暫停前的失敗次數上限。預設值為 5。 |
| `execution_timeout_seconds` | 整數 | 否 | 每次執行的逾時時間 (以秒為單位)。預設值為 600。 |
| `interaction` | 物件 | 是 | `CreateInteractionRequest` 定義代理程式、輸入內容、工具和環境。 |

回應會包括下列重要欄位：

| 欄位 | 類型 | 說明 |
| --- | --- | --- |
| `id` | 字串 | 觸發條件的專屬 ID。在所有後續作業中，請使用這個值。 |
| `status` | 字串 | 目前狀態：`active`、`paused` 或 `disabled`。 |
| `next_run_time` | 字串 | 下次排定執行的 ISO 8601 時間戳記。 |
| `consecutive_failure_count` | 整數 | 自上次成功執行以來，連續失敗的次數。 |

### 列出觸發條件

擷取與專案相關聯的所有觸發條件。

### Python

```
triggers = client.triggers.list()
for trigger in triggers.triggers:
    print(f"{trigger.id}: {trigger.display_name} ({trigger.status})")
```

### JavaScript

```
const triggers = await client.triggers.list();
for (const trigger of triggers.triggers) {
    console.log(`${trigger.id}: ${trigger.display_name} (${trigger.status})`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### 取得觸發條件

擷取單一觸發條件的完整設定和目前狀態。

### Python

```
trigger = client.triggers.get(id="TRIGGER_ID")
print(f"Schedule: {trigger.schedule}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
const trigger = await client.triggers.get("TRIGGER_ID");
console.log(`Schedule: ${trigger.schedule}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### 暫停及繼續

您可以暫停觸發條件來停止排定的執行作業，並恢復觸發條件來重新啟用排程。暫停不會影響手動執行。

### Python

```
# Pause
client.triggers.update(id="TRIGGER_ID", status="paused")

# Resume
client.triggers.update(id="TRIGGER_ID", status="active")
```

### JavaScript

```
// Pause
await client.triggers.update("TRIGGER_ID", { status: "paused" });

// Resume
await client.triggers.update("TRIGGER_ID", { status: "active" });
```

### REST

```
# Pause
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "paused"}'

# Resume
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "active"}'
```

### 刪除觸發條件

永久移除觸發條件。系統不會刪除過去的執行記錄。

### Python

```
client.triggers.delete(id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.delete("TRIGGER_ID");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### 立即執行觸發條件

不必等待下一個排定時間，即可視需要觸發觸發條件。即使觸發條件已暫停，這項功能仍可運作。

### Python

```
client.triggers.run(trigger_id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.run("TRIGGER_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### 列出執行作業

查看觸發條件的執行記錄。每次執行作業都會包含 `status`、時間戳記、可用於擷取完整互動輸出內容的 `interaction_id`，以及確認所有執行作業共用相同沙箱的 `environment_id`。

### Python

```
executions = client.triggers.list_executions(trigger_id="TRIGGER_ID")
for ex in executions.trigger_executions:
    print(f"{ex.id}: {ex.status} ({ex.start_time} - {ex.end_time})")

# Fetch the full interaction for an execution
interaction = client.interactions.get(id=ex.interaction_id)
print(interaction.output_text)
```

### JavaScript

```
const executions = await client.triggers.listExecutions("TRIGGER_ID");
for (const ex of executions.trigger_executions) {
    console.log(`${ex.id}: ${ex.status} (${ex.start_time} - ${ex.end_time})`);
}

// Fetch the full interaction for an execution
const interaction = await client.interactions.get(ex.interaction_id);
console.log(interaction.output_text);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## 適用情形與定價

您可以在 Google AI Studio 中，透過 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 預先發布版使用 Antigravity 代理程式，也可以在免費和付費方案專案中，透過 Gemini API 使用。

價格採用[即付即用模式](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#pricing-for-agents)，依據基礎 Gemini 模型權杖和代理使用的工具計算。標準聊天要求只會產生單一輸出內容，但 Antigravity 互動不同，這是一種代理工作流程。單一要求會觸發自主迴圈，進行推論、執行工具、執行程式碼和管理檔案。免費方案專案包含免費的速率限制和用量配額。

Antigravity 互動會執行多輪自主迴圈，並消耗大量權杖。在要求中設定[預算控制項](#budget-controls)，限制權杖用量。您也可以透過 [SSE 串流](https://ai.google.dev/gemini-api/docs/streaming?hl=zh-tw)即時監控進度，或取消執行中的要求。

### 預算控制

除了[模型選取](#model-selection)之外，請在 `agent_config` 內設定 `max_total_tokens` (使用 `"type": "antigravity"`)，限制互動可消耗的詞元總數 (輸入 + 輸出 + 思考)。快取權杖不會計入這項限制。當代理程式達到限制時，互動會停止並傳回 `status: "incomplete"`。這項限制是盡量達成，實際用量可能會略高於限制，視代理程式在步驟之間檢查預算的時間而定。

在 `agent_config` 中，於 `agent` 和 `input` 旁設定互動要求的預算。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    },
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": "/workspace/data.csv",
                "content": "id,name,value\n1,alpha,100\n2,beta,200\n",
            }
        ],
    }
)
print(f"Status: {interaction.status}")  # "incomplete" if budget was hit
print(f"Tokens used: {interaction.usage.total_tokens}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    },
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: "/workspace/data.csv",
                content: "id,name,value\n1,alpha,100\n2,beta,200\n",
            },
        ],
    },
});
console.log(`Status: ${interaction.status}`);
console.log(`Tokens used: ${interaction.usage.total_tokens}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    },
    "environment": {
      "type": "remote",
      "sources": [
        {
          "type": "inline",
          "target": "/workspace/data.csv",
          "content": "id,name,value\n1,alpha,100\n2,beta,200\n"
        }
      ]
    }
  }'
```

#### 繼續未完成的互動

互動傳回 `status: "incomplete"` 時，代理的工作和脈絡會保留。傳送參照原始互動 `id` 和 `environment_id` 的新互動，即可從中斷處繼續。新互動會取得自己的 `max_total_tokens` 預算。

### Python

```
# Continue from where the agent stopped
continuation = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="continue",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    }
)
print(f"Status: {continuation.status}")
```

### JavaScript

```
const continuation = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "continue",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    }
});
console.log(`Status: ${continuation.status}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "continue",
    "previous_interaction_id": "INTERACTION_ID",
    "environment": "ENVIRONMENT_ID",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    }
  }'
```

### 預估費用

費用會因工作複雜度而異。代理會自主判斷需要多少工具呼叫、程式碼執行和檔案作業。以下預估值是以跑步為依據。

| 工作類別 | 輸入內容詞元 | 輸出內容詞元 | 一般費用 |
| --- | --- | --- | --- |
| **研究與資訊整合** | 10 萬至 50 萬 | 1 萬至 4 萬 | $0.30 美元至 $1.00 美元 |
| **生成文件和內容** | 10 萬至 50 萬 | 15,000 至 50,000 | $0.30 美元至 $1.30 美元 |
| **流程和系統設計** | 10 萬至 40 萬 | 1 萬至 3 萬 | $0.25 美元至 $0.80 美元 |
| **資料處理與分析** | 30 萬至 300 萬 | 3 萬至 15 萬 | $0.70 美元至 $3.25 美元 |

通常會快取 50% 至 70% 的輸入權杖。如果代理工作流程複雜，且需要多次呼叫工具，單次互動可能會累積 300 萬到 500 萬個權杖，費用最高可達$5 美元。

在預先發布期間，**環境運算** (CPU、記憶體、沙箱執行) **不會產生費用**。

## 限制

- **預覽版狀態：**Antigravity 代理程式和 Interactions API。功能和結構定義可能會有所異動。
- **不支援的生成設定：**系統不支援下列參數，並會傳回 400 錯誤：`temperature`、`top_p`、`top_k`、`stop_sequences`、`max_output_tokens`。
- **結構化輸出內容：**Antigravity 代理程式不支援結構化輸出內容。
- **不支援的工具：**目前不支援 `file_search`、`computer_use` 和 `google_maps`。
- **遠端 MCP 限制：**不支援伺服器傳送事件 (SSE) 傳輸 (請使用可串流的 HTTP)。此外，伺服器 `name` 必須嚴格使用小寫英數字元 (使用大寫字母會觸發一般 `400 Bad Request` 錯誤)。
- **檔案系統工具：**目前沒有檔案系統工具。這是「`environment`」的一部分。
- **商店規定：**使用 `background=True` 執行代理程式時，必須提供 `store=True`。
- **僅支援有狀態的函式呼叫：**函式呼叫僅支援有狀態模式。您必須使用 `previous_interaction_id` 繼續對話，系統不支援手動重建記錄 (無狀態模式)。
- **不支援多模態類型。**目前不支援音訊、影片和文件輸入。只能使用文字和圖片。

## 後續步驟

- [快速入門導覽課程](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=zh-tw)：多輪對話和串流。
- [建構自訂代理](https://ai.google.dev/gemini-api/docs/custom-agents?hl=zh-tw)：自訂指令、技能和儲存代理。
- [環境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw)：沙箱設定、來源、網路。
- [Deep Research 代理](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw)：執行長期研究工作。
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw)：基礎 API。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-21 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-21 (世界標準時間)。"],[],[]]
