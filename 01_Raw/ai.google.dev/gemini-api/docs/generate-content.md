---
source_url: https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-TW
fetched_at: 2026-10-12T06:58:30.114518+00:00
title: "Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-tw)

# Gemini API

Gemini API 是從提示到製作的最快途徑，可使用 Gemini、Veo、Nano Banana 等模型。您可將這些生成模型整合至應用程式，生成文字和圖片、分析多模態輸入內容，以及建構對話式代理程式。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.8-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3.8-flash", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

[開始建構](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)

---

## 認識各種機型

[查看全部](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw)

[auto\_awesome
Gemini 3.1 Pro
新推出

這是 Google 最聰明的模型，也是全球最出色的多模態理解模型，一切都建立在最先進的推論技術基礎。](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-tw)
[spark
Gemini 3.6 Flash
新模型

這是 Google 最新的模型，兼具速度與智慧，可在代理功能和多模態工作提供強大效能。](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-tw)
[graphic\_eq
Gemini 3.8 Flash TTS
新推出

工作室等級的文字轉語音模型，可提供富有表現力的演繹、自訂語音設計和語音複製功能。](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=zh-tw)
[spark
Gemini 3.5 Flash-Lite
新

這個模型專為低延遲高處理量的子代理工作設計，適合處理大量工作，且具備成本效益。](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-tw)
[spark
Gemini 3.1 Flash-Lite

這款模型具備 Gemini 3 系列的效能和品質，適合處理大量資料，且成本效益高。](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-tw)
[spark
Gemini 3 Flash

效能可與大型模型匹敵，但成本遠低於大型模型。](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-tw)
[🍌
Nano Banana

最先進的圖像生成和編輯模型。](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)
[video\_library
Veo 3.1

Google 最先進的影片生成模型，支援原生音訊。](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw)
[spark
Gemini Robotics

這款視覺語言模型 (VLM) 可將 Gemini 的代理功能帶入機器人領域，並在實體世界中進行進階推理。](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-tw)

## 探索各種功能

[imagesmode

原生圖像生成 (Nano Banana)

使用 Gemini 2.5 Flash Image 原生生成及編輯高度相關的圖片。](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)
[article

長脈絡

將數百萬個權杖輸入 Gemini 模型，從非結構化圖片、影片和文件中取得理解。](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-tw)
[code

結構化輸出內容

限制 Gemini 只能以 JSON 格式回覆，這種結構化資料格式適合自動處理。](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw)
[functions

呼叫函式

將 Gemini 連結至外部 API 和工具，建構代理工作流程。](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)
[videocam

使用 Veo 3.1 生成影片

使用最先進的模型，根據文字或圖像提示詞製作高品質影片內容。](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw)
[android\_recorder

使用 Live API 的語音代理

使用 Live API 建構即時語音應用程式和代理。](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-tw)
[build

工具

透過 Google 搜尋、網址背景資訊、Google 地圖、程式碼執行和電腦使用等內建工具，讓 Gemini 連結到世界。](https://ai.google.dev/gemini-api/docs/tools?hl=zh-tw)
[stacks

文件解讀

處理最多 1000 頁的 PDF 檔案，並充分理解多模態內容或其他文字型檔案。](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-tw)
[cognition\_2

思考中

瞭解思考能力如何提升複雜工作和代理程式的推論能力。](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)

[Google AI Studio

測試提示、管理 API 金鑰、監控用量及建構原型。](https://aistudio.google.com?hl=zh-tw)
[group

開發人員社群

向其他開發人員和 Google 工程師提問及尋求解決方案。](https://discuss.ai.google.dev/c/gemini-api/4?hl=zh-tw)
[menu\_book

API 參考資料

如要進一步瞭解 Gemini API，請參閱官方參考文件。](https://ai.google.dev/api?hl=zh-tw)
[sensors

狀態

查看 Gemini API、Google AI Studio 和模型服務的狀態。](https://aistudio.google.com/status?hl=zh-tw)

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-09 (世界標準時間)。

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-09 (世界標準時間)。"],[],[]]
