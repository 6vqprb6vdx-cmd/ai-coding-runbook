---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/maps-grounding?hl=zh-TW
fetched_at: 2026-10-19T05:38:37.608309+00:00
title: "\u5229\u7528 Google \u5730\u5716\u5efa\u7acb\u57fa\u6e96 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-tw)

提供意見

# 利用 Google 地圖建立基準

「利用 Google 地圖建立基準」功能可將 Gemini 的生成功能，與 Google 地圖豐富、真實且最新的資料連結。開發人員可以利用這項功能，輕鬆將位置感知功能整合到應用程式中。如果使用者查詢的內容與 Maps 資料相關，Gemini 模型會利用 Google 地圖，提供與使用者指定位置或大概區域相關、符合事實且最新的答案。

- **準確且考量位置的回覆：**運用 Google 地圖廣泛且最新的資料，處理特定地理位置的查詢。
- **強化個人化功能：**根據使用者提供的所在位置，量身打造推薦內容和資訊。

## 開始使用

本範例說明如何將 Grounding with Google Maps 整合至應用程式，根據使用者查詢提供準確的回覆，並加入位置資訊。提示會要求提供當地建議，並可選用使用者位置資訊，讓 Gemini 模型使用 Google 地圖資料。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## 「利用 Google 地圖建立基準」的運作方式

利用 Google 地圖建立基準，將 Gemini API 與 Google 地理生態系統整合，並使用 Maps API 做為基準來源。當使用者的查詢包含地理位置背景資訊時，Gemini 模型可以叫用「利用 Google 地圖建立基準」工具。模型接著就能根據與所提供位置相關的 Google 地圖資料，生成回覆。

整個程序通常涵蓋下列工作：

1. **使用者查詢：**使用者向應用程式提交查詢，可能包含地理位置背景資訊 (例如「附近的咖啡店」、「舊金山的博物館」)。
2. **叫用工具：**Gemini 模型辨識出地理意圖，叫用「利用 Google 地圖建立基準」工具。這項工具可選擇提供使用者的 `latitude` 和 `longitude`。這項工具是文字搜尋工具，運作方式與在 Google 地圖上搜尋類似，也就是說，本地查詢 (「附近」) 會使用座標，而特定或非本地查詢則不太可能受到明確位置的影響。
3. **資料擷取：**「利用 Google 地圖建立基準」服務會查詢 Google 地圖，取得相關資訊 (例如地點、評論、相片、地址、營業時間)。
4. **建立基準生成：**系統會使用檢索到的 Maps 資料，提供 Gemini 模型回覆，確保事實準確性和關聯性。
5. **回覆：**模型會傳回文字回覆，其中包含 Google 地圖來源的引用內容。

## 使用 Google 地圖建立基準的原因和時機

如果應用程式需要準確、最新且特定地點的資訊，就非常適合使用「利用 Google 地圖建立基準」功能。這項功能會根據 Google 地圖全球超過 2.5 億個地點的龐大資料庫，提供相關且個人化的內容，提升使用者體驗。

如果應用程式需要執行下列操作，請使用「利用 Google 地圖建立基準」功能：

- 完整且如實回答特定地區的問題。
- 打造對話式行程規劃工具和當地導覽。
- 根據位置和使用者偏好 (例如餐廳或商店)，推薦搜尋點。
- 為社群、零售或餐飲外送服務打造位置感知體驗。

如果用途需要考量距離和最新事實資料，例如尋找「附近最棒的咖啡店」或規劃路線，利用 Google 地圖建立基準就是絕佳選擇。

## API 方法和參數

透過 Gemini API，您可以使用 [`generateContent`](https://ai.google.dev/api/generate-content?hl=zh-tw) 方法，將 Google 地圖做為工具建立基準。如要啟用及設定利用 Google 地圖建立基準，請在要求的 `tools` 參數中加入 [`googleMaps`](https://ai.google.dev/api/caching?hl=zh-tw#GoogleMaps) 物件。

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

此外，這項工具支援以 `toolConfig` 形式傳遞情境位置。

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### 瞭解基準回覆

如果回覆成功以 Google 地圖資料建立基準，回覆會包含 [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=zh-tw#GroundingMetadata) 欄位。這類結構化資料對於驗證聲明、在應用程式中建立豐富的引用體驗，以及符合服務使用規定至關重要。

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ]
      }
    }
  ]
}
```

Gemini API 會傳回下列資訊：
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=zh-tw#GroundingMetadata)：

- `groundingChunks`：包含 `maps` 來源 (`uri`、`placeId` 和 `title`) 的物件陣列。
- `groundingSupports`：區塊陣列，用於將模型回覆文字連結至 `groundingChunks` 中的來源。每個區塊都會將文字範圍 (由 `startIndex` 和 `endIndex` 定義) 連結至一或多個 `groundingChunkIndices`。這是建立內嵌引用的關鍵。

如需顯示如何以文字呈現文內引用的程式碼片段，請參閱「以 Google 搜尋強化事實基礎」文件中的[範例](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw#attributing_sources_with_inline_citations)。

## 用途

「利用 Google 地圖建立基準」功能支援多種位置感知用途。以下範例說明如何透過不同的提示詞和參數，利用 Google 地圖建立基準。Google 地圖基準結果中的資訊可能與實際情況不同。

### 處理地點相關問題

詢問特定地點的詳細問題，根據 Google 使用者評論和其他地圖資料取得解答。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### 提供適地性個人化服務

根據使用者的偏好和特定地理區域，取得專屬建議。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### 協助規劃行程

生成多日計畫，提供路線和各個地點的資訊，非常適合旅遊應用程式。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

## 服務使用規定

本節說明使用「利用 Google 地圖建立基準」服務時須遵守的規定。

### 告知使用者 Google 地圖來源的使用方式

每筆 Google 地圖基準結果都會提供 `groundingChunks` 中的來源，佐證各項回覆。系統也會傳回下列中繼資料：

- 來源 URI
- title
- ID

呈現利用 Google 地圖建立基準的結果時，您必須指定相關聯的 Google 地圖來源，並告知使用者下列事項：

- Google 地圖來源必須緊接在來源支援的生成內容之後。這類生成內容也稱為 Google 地圖基準結果。
- Google 地圖來源必須在一次使用者互動中可供查看。

### 顯示 Google 地圖來源和 Google 地圖連結

針對 `groundingChunks` 和 `grounding_chunks.maps.placeAnswerSources.reviewSnippets` 中的每個來源，都必須按照下列規定產生連結預覽畫面：

- 請按照 Google 地圖文字[出處指南](#maps-attribution-guidelines)，將每個來源歸功於 Google 地圖。
- 顯示回覆中提供的來源標題。
- 使用回覆中的 `uri` 或 `googleMapsUri` 連結至來源。

這些圖片顯示來源和 Google 地圖連結的最低顯示要求。

![提示和回覆，並顯示來源](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=zh-tw)

您可以收合來源檢視畫面。

![提示詞與回覆和來源 (收合)](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=zh-tw)

選用：加入其他內容 (例如：) 來強化連結預覽畫面：

- Google 地圖文字出處標示前方會插入 [Google 地圖網站小圖示](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=zh-tw)。
- 來源網址 (`og:image`) 的相片。

如要進一步瞭解部分 Google 地圖資料供應商及其授權條款，請參閱「[Google 地圖和 Google 地球法律聲明](https://www.google.com/help/legalnotices_maps/?hl=zh-tw)」。

### Google 地圖文字出處資訊規範

在文字中將來源歸給 Google 地圖時，請遵循下列規範：

- 請勿以任何方式修改「Google 地圖」文字：
  - 請勿變更 Google 地圖的大小寫。
  - 請勿將 Google 地圖分成多行。
  - 請勿將 Google 地圖本地化為其他語言。
  - 使用 HTML 屬性 translate="no"，防止瀏覽器翻譯 Google 地圖。
- 請按照下表說明設定 Google 地圖文字樣式：

| 屬性 | 樣式 |
| --- | --- |
| `Font family` | Roboto。載入字型為選用步驟。 |
| `Fallback font family` | 產品中已使用的任何 Sans Serif 內文字型，或「Sans-Serif」以叫用預設系統字型 |
| `Font style` | 一般 |
| `Font weight` | 400 |
| `Font color` | 白色、黑色 (#1F1F1F) 或灰色 (#5E5E5E)。與背景保持無障礙對比度 (4.5:1)。 |
| `Font size` | - 字型大小下限：12sp - 字型大小上限：16sp - 如要瞭解 sp，請參閱 [Material Design 網站](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc)上的字型大小單位。 |
| `Spacing` | 一般 |

#### CSS 範例

下列 CSS 會在白色或淺色背景上，以適當的字體排版樣式和顏色顯示 Google 地圖。

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### 地點 ID 和評論 ID

Google 地圖資料包括地點 ID 和評論 ID。您可以快取、儲存及匯出下列回應資料：

- `placeId`
- `reviewId`

《利用 Google 地圖建立基準條款》中的快取限制不適用。

### 禁止的活動和地域

利用 Google 地圖建立基準時，某些內容和活動會受到額外限制，以維護安全可靠的平台。除了《[條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw#grounding-with-google-maps)》中的使用限制外，您也同意不從事下列行為：

- 您不會將「利用 Google 地圖建立基準」功能用於高風險活動，包括緊急應變服務。
- 您不得在禁止地區發行或行銷提供「利用 Google 地圖建立基準」功能的應用程式。詳情請參閱「[Google Maps Platform 禁止地區](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=zh-tw)」一文。「禁止地域」清單可能會不時更新。

## 最佳做法

- **提供使用者位置資訊：**如要取得最相關的個人化回覆，請在知道使用者位置資訊時，務必在 `googleMapsGrounding` 設定中加入 `user_location` (經緯度)。
- **告知使用者：**明確告知使用者，系統會使用 Google 地圖資料回答查詢，尤其是在啟用工具時。
- **監控延遲時間：**如果是對話式應用程式，請確保基準回覆的 P95 延遲時間維持在可接受的門檻內，以維持流暢的使用者體驗。
- **在不需要時關閉：**預設會關閉利用 Google 地圖建立基準的功能。只有在查詢有明確的地理位置脈絡時，才啟用這項功能 (`"tools": [{"googleMaps": {}}]`)，以提升效能並節省費用。

## 限制

- **適用地區：**利用 Google 地圖建立基準的功能已在全球推出
- **支援的機型：**請參閱「[支援的機型](#supported-models)」一節。
- **多模態輸入/輸出：**目前「利用 Google 地圖建立基準」功能不支援文字以外的多模態輸入或輸出內容。
- **預設狀態：**「利用 Google 地圖建立基準」工具預設為關閉。您必須在 API 要求中明確啟用這項功能。

## 定價和頻率限制

利用 Google 地圖建立基準的定價因模型世代而異：

- **Gemini 3 和更新的模型：**模型決定執行的每項搜尋查詢都會計入專案費用，所有 Gemini 3 和更新的模型每月共用 5,000 次免費要求，之後**每 1,000 次搜尋查詢收費$14 美元**。單一搜尋提示 (您對模型發出的 API 要求) 可能會導致模型執行多項搜尋查詢，以找出必要資訊。這些查詢都會計為工具的付費使用次數。
- **Gemini 2.5 和舊版模型：**系統會根據搜尋提示向專案收費 (每 1,000 個基礎提示 $25 美元)。只有在提示成功傳回至少一個 Google 地圖錨定結果時，才會針對要求收費，無論模型在內部執行多少個別搜尋查詢來取得該結果，皆是如此。

「利用 Google 地圖建立基準」的配額通常與基礎 Gemini 模型的頻率限制一致。如需詳細的定價資訊，請參閱 [Gemini API 定價頁面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)。

## 支援的模型

下列機型支援「利用 Google 地圖建立基準」：

| 模型 | 利用 Google 地圖建立基準 |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=zh-tw) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=zh-tw) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-tw) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Pro 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 3 Flash 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-tw) | ✔️ |

## 支援的工具組合

您可以將「利用 Google 地圖建立基準」與其他內建工具搭配使用，例如[以 Google 搜尋強化事實基礎](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw) (Gemini 3.5 Flash-Lite 和後續模型支援)，以支援更複雜的用途。Gemini 3 模型也支援將這些內建工具與自訂工具 (函式呼叫) 結合。詳情請參閱「[工具組合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-tw)」頁面。

## 後續步驟

- 請參閱 [Gemini API 教戰手冊中的「以 Google 搜尋強化事實基礎」一節](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=zh-tw)。
- 瞭解其他[可用工具](https://ai.google.dev/gemini-api/docs/tools?hl=zh-tw)。
- 如要進一步瞭解負責任的 AI 最佳做法和 Gemini API 的安全篩選器，請參閱[安全設定指南](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-15 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-15 (世界標準時間)。"],[],[]]
