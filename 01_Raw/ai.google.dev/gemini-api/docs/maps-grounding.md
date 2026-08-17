---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-TW
fetched_at: 2026-08-17T02:23:12.405385+00:00
title: "\u5229\u7528 Google \u5730\u5716\u5efa\u7acb\u57fa\u6e96 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 利用 Google 地圖建立基準

利用 Google 地圖建立基準，讓 Gemini 的生成式功能連結至 Google 地圖豐富、真實且最新的資料。開發人員可以輕鬆將位置辨識功能整合至自家應用程式。如果使用者查詢的內容與地圖資料相關，Gemini 模型會利用 Google 地圖提供準確且最新的答案，並與使用者指定的確切位置或大概區域相關。

- **準確的地理位置感知回覆：**針對特定地理位置的查詢，運用 Google 地圖的豐富最新資料。
- **強化個人化功能：**根據使用者提供的地點，量身打造推薦內容和資訊。

## 開始使用

本範例說明如何將 Grounding with Google Maps 整合至應用程式，根據使用者查詢提供準確的回覆，並瞭解相關位置資訊。提示會要求提供當地建議，並可選擇提供使用者位置資訊，讓 Gemini 模型使用 Google 地圖資料。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## 如何利用 Google 地圖建立基準

利用 Google 地圖建立基準時，系統會使用 Maps API 做為基準來源，將 Gemini API 與 Google 地理位置生態系統整合。如果使用者查詢包含地理位置資訊，Gemini 模型可以呼叫「以 Google 地圖建立基準」工具。模型接著會根據與所提供位置相關的 Google 地圖資料，生成回覆。

整個程序通常涵蓋下列工作：

1. **使用者查詢：**使用者向應用程式提交查詢，可能包含地理位置背景資訊 (例如「我附近的咖啡店」、「舊金山的博物館」)。
2. **工具呼叫：**Gemini 模型會辨識地理意圖，並呼叫「利用 Google 地圖建立基準」工具。這項工具可選擇性提供使用者的 `latitude` 和 `longitude`。這項工具是文字搜尋工具，運作方式與在 Google 地圖上搜尋類似，也就是說，系統會使用座標來處理本地查詢 (「我附近」)，而特定或非本地查詢則不太會受到明確位置的影響。
3. **資料擷取：**「利用 Google 地圖建立基準」服務會查詢 Google 地圖，找出相關資訊 (例如地點、評論、相片、地址、營業時間)。
4. **以擷取資料為基準生成內容：**系統會使用擷取的 Google 地圖資料，做為 Gemini 模型回覆的依據，確保內容符合事實且具關聯性。
5. **回覆和註解：**模型會傳回文字回覆，並附上連結至 Google 地圖來源的內嵌註解，方便開發人員顯示引用內容。

## 使用 Google 地圖建立基準的原因與時機

如果應用程式需要準確、最新且特定地點的資訊，就非常適合使用「利用 Google 地圖建立基準」功能。這項功能會根據 Google 地圖全球超過 2.5 億個地點的龐大資料庫，提供相關且個人化的內容，提升使用者體驗。

如果應用程式需要執行下列操作，請使用「利用 Google 地圖建立基準」功能：

- 完整且如實回答特定地區的問題。
- 建構對話式旅遊行程規劃工具和當地導覽。
- 根據位置和使用者偏好 (例如餐廳或商店) 推薦興趣點。
- 為社交、零售或外送服務打造位置感知體驗。

在需要鄰近地區和當前事實資料的應用情境中，以 Google 地圖為基礎的搜尋功能表現出色，例如尋找「我附近最好的咖啡店」或取得路線。

## 用途

利用 Google 地圖建立基準支援各種需要位置資訊的用途。

### 處理地點相關問題

詳細詢問特定地點的問題，根據 Google 使用者評論和其他地圖資料取得解答。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### 提供以位置為依據的個人化服務

根據使用者的偏好和特定地理區域提供建議。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### 協助規劃行程

生成多日行程，提供各個地點的路線和資訊，非常適合用於旅遊應用程式。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## 服務使用規定

本節說明 Grounding with Google Maps 的服務使用規定。

### 告知使用者 Google 地圖來源的使用情形

對於每項 Google 地圖 Grounded 結果，您都會在 `model_output` 步驟的內容區塊中收到來源註解，這些註解支援每項回覆。系統會傳回下列中繼資料：

- 來源網址
- 名稱

呈現利用 Google 地圖建立基準的結果時，您必須指定相關聯的 Google 地圖來源，並告知使用者下列事項：

- Google 地圖來源必須緊接在來源支援的生成內容後方。這類生成內容也稱為「Google 地圖基礎結果」。
- Google 地圖來源必須在一次使用者互動中顯示。

### 顯示 Google 地圖來源和連結

系統必須按照下列規定，為每個來源註解產生連結預覽畫面：

- 請按照 Google 地圖文字[出處標示指南](#maps-attribution-guidelines)，將每個來源歸功於 Google 地圖。
- 顯示回覆中提供的來源名稱。
- 使用註解中的 `url` 連結至來源。

### Google 地圖文字出處註明規範

在文字中將來源歸給 Google 地圖時，請遵循下列規範：

- 請勿以任何方式修改「Google 地圖」文字：
  - 請勿變更 Google 地圖的英文大小寫。
  - 請勿將 Google 地圖換行。
  - 請勿將 Google 地圖本地化為其他語言。
  - 使用 HTML 屬性 translate="no"，禁止瀏覽器翻譯 Google 地圖。

如要進一步瞭解部分 Google 地圖資料供應商及其授權條款，請參閱 [Google 地圖和 Google 地球法律聲明](https://www.google.com/help/legalnotices_maps/?hl=zh-tw)。

## 最佳做法

- **提供使用者位置資訊：**如要提供最相關的個人化回覆，請在使用者位置資訊已知的情況下，一律在 `google_maps` 工具設定中加入 `latitude` 和 `longitude`。
- **告知使用者：**清楚告知使用者系統會使用 Google 地圖資料回答查詢，尤其是在啟用這項工具時。
- **在不需要時關閉：**根據預設，系統會關閉利用 Google 地圖建立基準的功能。只有在查詢有明確的地理位置脈絡時，才啟用這項功能 (`"tools": [{"type": "google_maps"}]`)，以提升效能並節省費用。

## 限制

- 利用 Google 地圖建立基準功能目前僅支援英文提示和回覆。
- 這項工具可能僅適用於部分地區。
- 結果可能因定位精確度和可用的 Google 地圖資料而異。
- **地理範圍：**利用 Google 地圖建立基準的服務已在全球推出。
- **預設狀態：**「利用 Google 地圖建立基準」工具預設為關閉。
  您必須在 API 要求中明確啟用這項功能。

## 定價與頻率限制

利用 Google 地圖建立基準的定價會因模型世代而異：

- **Gemini 3 模型：**如果模型決定執行**搜尋查詢**，專案就會產生費用。單一**搜尋提示** (您對模型發出的 API 要求) 可能會導致模型執行多項搜尋查詢，以找出必要資訊。每項查詢都會計為工具的計費使用量。
- **Gemini 2.5 和舊版模型：**系統會根據**搜尋提示**向專案收費。
  只有在提示成功傳回至少一個 Google 地圖基礎結果時，才會針對要求收費，無論模型在內部執行多少次個別搜尋查詢來取得該結果。

如需詳細定價資訊，請參閱 [Gemini API 定價頁面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)。

## 支援的模型

下列模型支援「利用 Google 地圖建立基準」：

| 模型 | 利用 Google 地圖建立基準 |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-tw) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Pro 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 3 Flash 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-tw) | ✔️ |

## 支援的工具組合

Gemini 3 模型支援結合內建工具 (例如「以 Google 地圖強化事實基礎」) 和自訂工具 (函式呼叫)。詳情請參閱「[工具組合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-tw)」頁面。

## 後續步驟

- 瞭解其他[可用工具](https://ai.google.dev/gemini-api/docs/tools?hl=zh-tw)。
- 如要進一步瞭解負責任的 AI 技術最佳做法和 Gemini API 的安全篩選器，請參閱[安全設定指南](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-30 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-30 (世界標準時間)。"],[],[]]
