---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=zh-TW
fetched_at: 2026-06-08T15:00:05.762139+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-tw)
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
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

如要瞭解詳情，請試用[搜尋工具筆記本](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=zh-tw)。

## 如何運用 Google 搜尋強化事實基礎

啟用 `google_search` 工具後，模型會自動處理搜尋、處理及引用資訊的整個工作流程。

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=zh-tw)

1. **使用者提示：**應用程式會將使用者的提示傳送至 Gemini API，並啟用 `google_search` 工具。
2. **提示分析：**模型會分析提示，判斷 Google 搜尋是否能提升回覆品質。
3. **Google 搜尋：**模型會視需要自動生成一或多個搜尋查詢並執行。
4. **處理搜尋結果：**模型會處理搜尋結果、整合資訊並擬定回覆。
5. **根據搜尋結果生成的回覆：**API 會根據搜尋結果，傳回最終的易讀回覆。這項回覆包含模型生成的文字答案和 `groundingMetadata`，以及搜尋查詢、網頁結果和引文。

## 瞭解基礎回應

如果回應成功完成基礎化，回應會包含 `groundingMetadata` 欄位。這項結構化資料對於驗證聲明，以及在應用程式中建構豐富的引用體驗至關重要。

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

Gemini API 會透過 `groundingMetadata` 傳回下列資訊：

- `webSearchQueries`：使用的搜尋查詢陣列。這有助於偵錯及瞭解模型的推理過程。
- `searchEntryPoint`：包含算繪必要搜尋建議的 HTML 和 CSS。如需完整的使用規定，請參閱《[服務條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw#grounding-with-google-search)》。
- `groundingChunks`：包含網頁來源 (`uri` 和 `title`) 的物件陣列。
- `groundingSupports`：要將模型回應 `text` 連結至 `groundingChunks` 中來源的區塊陣列。每個區塊都會將文字 `segment` (由 `startIndex` 和 `endIndex` 定義) 連結至一或多個 `groundingChunkIndices`。這是建立內文引用內容的關鍵。

您也可以搭配[網址內容工具](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)使用以 Google 搜尋強化事實基礎，同時參考公開網路資料和您提供的特定網址。

## 使用內嵌引文註明出處

這項 API 會傳回結構化引文資料，讓您完全掌控在使用者介面中顯示來源的方式。您可以使用 `groundingSupports` 和 `groundingChunks` 欄位，將模型陳述直接連結至來源。以下是處理中繼資料的常見模式，可建立內嵌可點選引文的回覆。

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

新回覆會內嵌引用內容，如下所示：

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
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
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Flash Image 預先發布版 | ✔️ |
| Gemini 3.1 Pro 預先發布版 | ✔️ |
| Gemini 3 Pro Image 預先發布版 | ✔️ |
| Gemini 3 Flash 預先發布版 | ✔️ |
| Gemini 3.1 Flash-Lite 預先發布版 | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## 支援的工具組合

您可以將「以 Google 搜尋強化事實基礎」與[程式碼執行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)和 [URL 內容](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)等其他工具搭配使用，處理更複雜的用途。

Gemini 3 模型支援結合內建工具 (例如使用 Google 搜尋建立基準) 和自訂工具 (函式呼叫)。詳情請參閱「[工具組合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-tw)」頁面。

## 後續步驟

- 請參閱 [Gemini API 教戰手冊中的「以 Google 搜尋強化事實基礎」一節](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=zh-tw)。
- 瞭解其他可用工具，例如[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)。
- 瞭解如何使用[網址內容工具](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)，透過特定網址擴增提示。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-19 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-19 (世界標準時間)。"],[],[]]
