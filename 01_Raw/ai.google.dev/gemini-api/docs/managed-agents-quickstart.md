---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=zh-TW
fetched_at: 2026-07-20T04:45:21.675798+00:00
title: "\u4ee3\u7ba1\u4ee3\u7406\u7a0b\u5f0f\u5feb\u901f\u5165\u9580\u5c0e\u89bd\u8ab2\u7a0b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 代管代理程式快速入門導覽課程

本指南將逐步說明如何使用 [Antigravity 代理](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=zh-tw)，在 Gemini API 上建立及使用 Managed Agents。您將進行第一次代理程式呼叫、繼續多輪對話、串流回應、從沙箱下載檔案，以及使用 Antigravity 管理型代理程式。

## 執行首次代理互動

只要呼叫一次 [Interactions API](https://ai.google.dev/gemini-api/docs?hl=zh-tw)，即可佈建 Linux 沙箱、執行代理程式迴圈，並傳回結果。您將定義三項參數：

- 以 `"antigravity-preview-05-2026",` 形式傳遞 `agent`，這是預先定義的通用型受管理代理程式目前版本。
- 定義 `environment="remote"`，以佈建全新的沙箱環境。
- 建立輸入內容，定義代理程式要執行的動作。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

回應會傳回 `Interaction` 物件。儲存 `interaction.id` 和 `interaction.environment_id`，即可在同一個沙箱中繼續對話。使用 `interaction.output_text` 存取代理的最終回覆。`interaction.steps` 列出代理執行的每個步驟 (推論、工具呼叫、程式碼執行作業)。

## 繼續對話 (多輪)

這項 API 會追蹤兩個獨立的狀態維度：

- **對話脈絡：**對話記錄、推論追蹤、工具使用情形、使用 `previous_interaction_id`。
- [**環境狀態：**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw)檔案、已安裝的套件和沙箱狀態，使用 `environment`。

在各自的位置傳遞這兩項內容，即可繼續：

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

第 1 回合 (`fibonacci.txt`) 的檔案會保留到第 2 回合。專員也會保留對話脈絡。

您可以獨立混搭下列項目：

- **清除對話，保留檔案：**省略 `previous_interaction_id`，只使用 `environment` 傳遞環境 ID，在同一個工作區中展開新的對話。
- **保留對話，建立新工作區：**傳遞 `previous_interaction_id`，為新的沙箱設定 `environment="remote"`。

### 自動壓縮脈絡

在長時間的多輪對話中，推論步驟、工具呼叫和大型檔案內容的原始記錄可能會快速增長，並消耗大量脈絡空間。為避免發生權杖限制錯誤，並維持代理程式的專注度 (防止「脈絡腐化」)，Managed Agents API 會在權杖數量達到約 135,000 個時，執行原生脈絡壓縮步驟。這個步驟會自動執行。

## 逐句顯示回覆

如果是長時間執行的工作，您可以串流回應，即時查看代理程式的工作情形：

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

串流會傳回步驟差異的可疊代項目，包括遞增文字、推論詞元和工具呼叫更新。如要進一步瞭解如何串流回應，請參閱[串流指南](https://ai.google.dev/gemini-api/docs/streaming?hl=zh-tw)。

## 從環境下載檔案

代理程式在沙箱中建立檔案時。使用 Files API 透過直接 HTTP 要求下載 (目前沒有 SDK 方法)：

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

tar -xf snapshot.tar -C extracted_snapshot
```

## 儲存代管代理程式

在先前的步驟中，我們使用了預設的 Antigravity 代理程式，並內嵌自訂。完成設定 (指令、技能和環境) 的疊代後，您可以將設定儲存為受管理代理程式。這樣一來，您就能透過 ID 叫用該函式，不必重複設定。

儲存代理程式時，您會定義 `base_environment` (來自來源或分叉現有環境)。每次新互動時，代理程式都會使用這個環境。

**從來源：**內嵌定義來源，或從 GitHub 或 Cloud Storage 等其他來源定義。

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## 叫用代管代理程式

儲存受管理代理程式後，您就可以透過 ID 叫用該代理程式。每次叫用都會分叉基本環境，因此每次執行都會從乾淨的狀態開始：

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## 後續步驟

- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-tw)：功能、支援的工具、多模態輸入、價格和限制。
- [建構受管理代理](https://ai.google.dev/gemini-api/docs/custom-agents?hl=zh-tw)：使用您自己的指令、技能和資料擴充 Antigravity。
- [環境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw)：來源、網路、生命週期、資源限制。
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw)：模型和代理程式的基礎 API。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-22 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-22 (世界標準時間)。"],[],[]]
