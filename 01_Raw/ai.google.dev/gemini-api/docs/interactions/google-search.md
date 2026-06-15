---
source_url: https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=zh-TW
fetched_at: 2026-06-15T06:24:50.715949+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 以 Google 搜尋建立基準

如果啟用「以 Google 搜尋強化事實基礎」功能，Gemini 模型就能連結至即時網路內容，並支援所有可用語言。Gemini 就能提供更準確的答案，並引用知識截點以外的可驗證來源。

基礎化可協助您建構的應用程式：

- **提高事實準確度：**根據真實資訊生成回覆，減少模型幻覺。
- **取得即時資訊：**回答近期事件和主題相關問題。
- **提供引文：**顯示模型聲明的來源，贏得使用者信任。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## 如何運用 Google 搜尋強化事實基礎

啟用 `google_search` 工具後，模型會自動處理搜尋、處理及引用資訊的整個工作流程。

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=zh-tw)

1. **使用者提示：**應用程式會將使用者的提示傳送至 Gemini API，並啟用 `google_search` 工具。
2. **提示分析：**模型會分析提示，判斷 Google 搜尋是否能提升回覆品質。
3. **Google 搜尋：**模型會視需要自動生成一或多個搜尋查詢並執行。
4. **處理搜尋結果：**模型會處理搜尋結果、整合資訊並擬定回覆。
5. **根據搜尋結果生成的回覆：**API 會根據搜尋結果，傳回最終的易讀回覆。這項回覆包含模型提供的文字答案，以及內含引文的 `annotations`，還有 `google_search_call` 和 `google_search_result` 步驟，其中包含搜尋查詢和搜尋建議。

## 瞭解基礎回應

如果模型成功根據資訊來源生成回應，文字輸出內容會直接在文字內容區塊中加入 `annotations`。這些註解會提供引文資訊，將回覆內容的各個部分連結至來源。

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

回應中的主要欄位：

- `google_search_call`：包含模型執行的搜尋`queries`。
- `google_search_result`：包含 `search_suggestions`，這是用於在 UI 中顯示搜尋建議的 HTML 片段。完整使用規定詳見《[服務條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw#grounding-with-google-search)》。
- `text`，並附上 `annotations`：模型合成的答案，內含引文。每個 `url_citation` 註解都會將文字區段 (由 `start_index` 和 `end_index` 定義) 連結至來源網址。這是建構內文引文的關鍵。

您也可以搭配[網址內容工具](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=zh-tw)使用以 Google 搜尋強化事實基礎，以公開網路資料和您提供的特定網址做為回覆的基準。

## 使用內嵌引文註明出處

API 會在文字內容區塊中傳回內嵌`url_citation`註解，讓您完全掌控在使用者介面中顯示來源的方式。每則註解都會包含 `start_index` 和 `end_index`，指出註解引用的文字部分。以下說明如何擷取及顯示這些資料。

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

輸出內容會顯示文字和引文：

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## 定價

在 Gemini 3 中使用「以 Google 搜尋強化事實基礎」功能時，系統會針對模型執行的每項搜尋查詢向專案收費。如果模型決定執行多個搜尋查詢來回答單一提示 (例如在同一個 API 呼叫中搜尋 `"UEFA Euro 2024 winner"` 和 `"Spain vs England Euro 2024 final
score"`)，則該要求會計為兩次工具使用次數。為計費起見，計算不重複查詢時，我們會忽略空白的網路搜尋查詢。這項計費模式僅適用於 Gemini 3 模型；如果您使用 Gemini 2.5 或更舊的模型進行搜尋基礎作業，系統會依提示向專案收費。

如需詳細的定價資訊，請參閱 [Gemini API 定價頁面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)。

## 支援的模型

如要瞭解完整功能，請前往[模型總覽](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw)頁面。

| 型號 | 以 Google 搜尋建立基準 |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash Image 預先發布版 | ✔️ |
| Gemini 3.1 Pro 預先發布版 | ✔️ |
| Gemini 3 Pro Image 預先發布版 | ✔️ |
| Gemini 3 Flash 預先發布版 | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## 支援的工具組合

您可以搭配使用「以 Google 搜尋強化事實基礎」功能與其他工具，例如[程式碼執行](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=zh-tw)和[網址內容](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=zh-tw)，以支援更複雜的用途。

Gemini 3 模型支援結合內建工具 (例如使用 Google 搜尋建立基準) 和自訂工具 (函式呼叫)。詳情請參閱「[工具組合](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=zh-tw)」頁面。

## 後續步驟

- 瞭解其他可用工具，例如[函式呼叫](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-tw)。
- 瞭解如何使用[網址內容工具](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=zh-tw)，在提示中加入特定網址。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-28 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-28 (世界標準時間)。"],[],[]]
