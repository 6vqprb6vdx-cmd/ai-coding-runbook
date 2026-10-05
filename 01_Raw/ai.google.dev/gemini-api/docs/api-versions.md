---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=zh-TW
fetched_at: 2026-10-05T06:37:08.771937+00:00
title: "API \u7248\u672c\u8aaa\u660e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [API 參考資料](https://ai.google.dev/api?hl=zh-tw)

提供意見

# API 版本說明

本文將概略說明 Gemini API 的 `v1` 和 `v1beta` 版本之間的差異。

- **v1**：API 穩定版。穩定版中的功能在主要版本生命週期內完全受支援。如有任何重大變更，系統會建立新的 API 主要版本，並在一段合理時間後淘汰現有版本。API 可能會導入非破壞性變更，但不會變更主要版本。**Interactions API** 和核心功能已在 `v1` 正式推出。
- **v1beta**：這個版本包含正在積極開發的早期功能和功能。`v1beta` 中的功能可能會根據意見回饋進行調整，但您可以在這些功能升級為穩定版之前搶先試用。

## 支援的功能和特色

下表詳細列出 `v1` (正式版) 和 `v1beta` (Beta 版) 的功能適用情形。核心 API 功能和工具適用於 Interactions API 和 `generateContent`，除非另有規定：

| 功能 | v1 | v1beta |
| --- | --- | --- |
| **核心 API 功能** |  |  |
| [Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=zh-tw) |  |  |
| [函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw) |  |  |
| [結構化輸出內容](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw) |  |  |
| [思考 / 推論](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw) |  |  |
| [系統指令](https://ai.google.dev/gemini-api/docs/system-instructions?hl=zh-tw) |  |  |
| [音訊輸出 (語音設定)](https://ai.google.dev/gemini-api/docs/audio?hl=zh-tw) |  |  |
| [服務層級 (優先 / 彈性)](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-tw) |  |  |
| **工具** |  |  |
| [程式碼執行工具](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw) |  |  |
| [Google 搜尋基礎](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw) |  |  |
| [Google 地圖基礎](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw) |  |  |
| [網址背景資訊工具](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw) |  |  |
| [檔案搜尋工具](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw) |  |  |
| [電腦使用工具](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw) |  |  |
| [MCP 伺服器工具](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw#mcp) |  |  |
| **Realtime API** |  |  |
| [Live API (WebSockets)](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-tw) |  |  |
| [Live Music API](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=zh-tw) |  |  |
| [臨時權杖 (Live API)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=zh-tw) |  |  |
| **平台 API** |  |  |
| [Models API](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw) |  |  |
| [檔案服務路徑](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw) |  |  |
| [File Search Stores Route](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw) |  |  |
| [Agents API](https://ai.google.dev/gemini-api/docs/agents?hl=zh-tw) |  |  |
| [Webhooks API](https://ai.google.dev/gemini-api/docs/webhooks?hl=zh-tw) |  |  |
| [脈絡快取功能](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw) |  |  |

- - 支援

## 在 SDK 中設定 API 版本

Gemini API SDK 預設為 `v1beta`，但您可以明確指定版本，方法是設定 API 版本，如下列程式碼範例所示：

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client = Client.builder()
    .httpOptions(HttpOptions.builder().apiVersion("v1").build())
    .build();

CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.6-flash"))
    .input(InteractionsInput.of("Explain how AI works"))
    .build();
var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        HTTPOptions: genai.HTTPOptions{
            APIVersion: "v1",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.6-flash"),
            Input: interactions.NewInteractionsInput("Explain how AI works"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works",
  }'
```

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-24 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-24 (世界標準時間)。"],[],[]]
