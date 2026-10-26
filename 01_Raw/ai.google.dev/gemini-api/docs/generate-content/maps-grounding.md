---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/maps-grounding?hl=zh-CN
fetched_at: 2026-10-26T05:49:59.906690+00:00
title: "\u4f9d\u6258 Google \u5730\u56fe\u8fdb\u884c\u63a5\u5730 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-cn)

发送反馈

# 依托 Google 地图进行接地

Grounding with Google Maps 可将 Gemini 的生成能力与 Google 地图丰富、真实且最新的数据联系起来。借助此功能，开发者可以轻松将位置感知功能融入到自己的应用中。当用户查询的上下文与 Google 地图数据相关时，Gemini 模型会利用 Google 地图提供与用户指定位置或大致区域相关的真实且最新的回答。

- **准确、位置感知的回答**： 利用 Google 地图广泛且最新的数据来处理特定地理位置的查询。
- **增强的个性化体验**： 根据用户提供的位置定制推荐内容和信息。

## 开始使用

此示例演示了如何将 Grounding with Google Maps 集成到您的应用中，以便为用户查询提供准确、位置感知的回答。提示要求提供本地推荐，并提供可选的用户位置，以便 Gemini 模型使用 Google 地图数据。

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

## Grounding with Google Maps 的工作原理

“依托 Google 地图进行接地”功能使用 Google 地图 API 作为接地来源，将 Gemini API 与 Google 地理生态系统集成在一起。当用户的查询包含地理位置上下文时，Gemini 模型可以调用“依托 Google 地图进行接地”工具。然后，模型可以根据与所提供位置相关的 Google 地图数据生成回答。

该过程通常涉及以下步骤：

1. **用户查询**： 用户向您的应用提交查询，其中可能包含地理位置上下文（例如“我附近的咖啡店”“旧金山的博物馆”）。
2. **工具调用**： Gemini 模型识别出地理位置意图，并调用“Grounding with Google Maps”工具。您可以选择性地为该工具提供用户的 `latitude` 和 `longitude`。该工具是一种文本搜索工具，其行为与在 Google 地图上搜索类似，即本地查询（“我附近”）将使用坐标，而特定或非本地查询不太可能受到明确位置的影响。
3. **数据检索**： Grounding with Google Maps 服务会查询 Google 地图以获取相关信息（例如地点、评价、照片、地址、营业时间）。
4. **接地生成**： 检索到的 Google 地图数据用于为 Gemini 模型的回答提供信息，确保事实准确性和相关性。
5. **回答**： 模型会返回文本回答，其中包含对 Google 地图来源的引用。

## 使用 Grounding with Google Maps 的原因和时机

Grounding with Google Maps 功能非常适合需要准确、最新且特定于位置的信息的应用。它通过提供相关且个性化的内容来提升用户体验，这些内容由 Google 地图在全球范围内超过 2.5 亿个地点的庞大数据库提供支持。

当您的应用需要执行以下操作时，应使用 Grounding with Google Maps 功能：

- 针对特定地理位置的问题提供完整且准确的回答。
- 构建对话式行程规划师和本地向导。
- 根据位置和用户偏好（例如餐馆或商店）推荐兴趣点。
- 为社交、零售或外卖服务打造位置感知体验。

在需要考虑邻近度和最新真实数据的使用场景中，“依托 Google 地图进行接地”功能表现出色，例如查找“我附近最好的咖啡店”或获取路线。

## API 方法和参数

Grounding with Google Maps 通过 Gemini API 作为工具在 [`generateContent`](https://ai.google.dev/api/generate-content?hl=zh-cn) 方法中公开。您可以通过在请求的 `tools` 参数中添加 [`googleMaps`](https://ai.google.dev/api/caching?hl=zh-cn#GoogleMaps) 对象来启用和配置 Grounding with Google Maps。

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

此外，该工具还支持将上下文位置作为 `toolConfig` 传递。

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

### 了解接地回答

当回答成功依托 Google 地图数据进行接地时，回答
中会包含 [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=zh-cn#GroundingMetadata) 字段。
此结构化数据对于验证声明、在应用中打造丰富的引用体验以及满足服务使用要求至关重要。

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

Gemini API 会随
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=zh-cn#GroundingMetadata)返回以下信息：

- `groundingChunks`：包含 `maps` 来源（`uri`、`placeId` 和 `title`）的对象数组。
- `groundingSupports`：用于将模型回答文本连接到 `groundingChunks` 中的来源的块数组。每个块将文本范围（由 `startIndex` 和 `endIndex` 定义）链接到一个或多个 `groundingChunkIndices`。这是构建内嵌引用的关键。

如需查看演示如何在文本中呈现内嵌引用的代码段，请参阅[“依托 Google 搜索进行接地”文档中的
示例](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn#attributing_sources_with_inline_citations)
。

## 使用场景

Grounding with Google Maps 支持各种位置感知应用场景。以下示例演示了不同的提示和参数如何利用 Grounding with Google Maps 功能。Google 地图接地结果中的信息可能与实际情况有所不同。

### 处理特定地点的问题

提出有关特定地点的详细问题，以获取基于 Google 用户评价和其他 Google 地图数据的回答。

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

### 提供基于位置的个性化体验

获取根据用户偏好和特定地理区域量身定制的推荐。

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

### 协助规划行程

生成包含路线和各种地点信息的行程计划，非常适合旅行应用。

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

## 服务使用要求

本部分介绍了“依托 Google 地图进行接地”功能的服务使用要求。

### 告知用户 Google 地图来源的使用情况

对于每个 Google 地图接地结果，您都会收到 `groundingChunks` 中支持相应回答的来源。系统还会返回以下元数据：

- 源 URI
- 标题
- ID

呈现“Grounding with Google Maps”功能的结果时，您必须指定关联的 Google 地图来源，并告知用户以下信息：

- Google 地图来源必须紧跟在来源支持的生成内容之后。此类生成的内容也称为 Google 地图接地结果。
- Google 地图来源必须在一次用户互动中可见。

### 使用 Google 地图链接显示 Google 地图来源

对于 `groundingChunks` 和 `grounding_chunks.maps.placeAnswerSources.reviewSnippets` 中的每个来源，必须按照以下要求生成链接预览：

- 请按照 Google 地图文字
  [提供方指南](#maps-attribution-guidelines)，将每项来源归属至 Google 地图。
- 显示回答中提供的来源标题。
- 使用回答中的 `uri` 或 `googleMapsUri` 链接到来源。

这些图片展示了显示来源和 Google 地图链接的最低要求。

![显示来源的回答提示](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=zh-cn)

您可以收起“来源”视图。

![已折叠包含回答和来源的提示](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=zh-cn)

可选：使用其他内容（例如以下内容）增强链接预览：

- 在 [Google 地图网站图标](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=zh-cn)
  之前插入 Google 地图文字提供方。
- 来自来源网址 (`og:image`) 的照片。

如需详细了解我们的部分 Google 地图数据提供商及其
许可条款，请参阅
[Google 地图和 Google 地球法律声明](https://www.google.com/help/legalnotices_maps/?hl=zh-cn)。

### Google 地图文字提供方指南

在文本中将来源归属至 Google 地图时，请遵循以下指南：

- 请勿以任何方式修改 Google 地图文字：
  - 请勿更改 Google 地图的大小写。
  - 请勿将 Google 地图换行到多行。
  - 请勿将 Google 地图本地化为其他语言。
  - 使用 HTML 属性 translate="no" 防止浏览器翻译 Google 地图。
- 按照下表中的说明设置 Google 地图文字的样式：

| 属性 | 样式 |
| --- | --- |
| `Font family` | Roboto。您可以选择性地加载字体。 |
| `Fallback font family` | 产品中已使用的任何无衬线正文字体，或“Sans-Serif”以调用默认系统字体 |
| `Font style` | 正常 |
| `Font weight` | 400 |
| `Font color` | 白色、黑色 (#1F1F1F) 或灰色 (#5E5E5E)。保持与背景的可访问对比度 (4.5:1)。 |
| `Font size` | - 字体大小下限：12sp - 字体大小上限：16sp - 如需了解 sp，请参阅 [Material Design 网站](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc)上的字体大小单位。 |
| `Spacing` | 正常 |

#### 示例 CSS

以下 CSS 代码段会在白色或浅色背景上呈现具有适当排版样式和颜色的 Google 地图。

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

### 地点 ID 和评价 ID

Google 地图数据包括地点 ID 和评价 ID。您可能会缓存、存储和导出以下回答数据：

- `placeId`
- `reviewId`

Grounding with Google Maps 条款中针对缓存的限制不适用。

### 禁止的活动和地区

Grounding with Google Maps 对某些内容和活动有额外的限制，以维护安全可靠的平台。除了条款中的使用
限制之外：

- 您不得将“依托 Google 地图进行接地”功能用于高风险活动，包括应急响应服务。
- 您不得在禁止地区分发或营销提供“依托 Google 地图进行接地”功能的应用。如需了解详情，请参阅
  [Google Maps Platform 禁止地区](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=zh-cn)。
  禁止地区列表可能会不时更新。

## 最佳做法

- **提供用户位置**： 为了获得最相关且个性化的回答，请务必在知道用户位置的情况下，在 `googleMapsGrounding` 配置中添加 `user_location`（纬度和经度）。
- **告知最终用户**： 明确告知最终用户，系统正在使用 Google 地图数据来回答他们的查询，尤其是在启用该工具时。
- **监控延迟时间**： 对于对话式应用，请确保接地回答的 P95 延迟时间保持在可接受的阈值范围内，以维持流畅的用户体验。
- **在不需要时关闭**： Grounding with Google Maps 默认处于关闭状态。只有当查询具有
  明确的地理位置上下文时，才启用该功能 (`"tools": [{"googleMaps": {}}]`)，以优化性能和费用。

## 限制

- **地理范围**： Grounding with Google Maps 在全球范围内可用
- **模型支持**： 请参阅[支持的模型](#supported-models)部分。
- **多模态输入/输出**： Grounding with Google Maps 目前不支持文本以外的多模态输入或输出。
- **默认状态**： “依托 Google 地图进行接地”工具默认处于关闭状态。
  您必须在 API 请求中明确启用该工具。

## 价格和速率限制

Grounding with Google Maps 的价格因模型代系而异：

- **Gemini 3 及更新的模型**： 您的项目将按模型决定执行的每个搜索查询收费，所有 Gemini 3 及更新的模型每月共享 5,000 个免费请求，超出后按**每 1,000 次搜索查询 14 美元** 收费。单个搜索提示（您向模型发出的 API 请求）可能会导致模型执行多个搜索查询来查找必要的信息。每个查询都算作该工具的可计费使用。
- **Gemini 2.5 及更旧的模型**： 您的项目将按搜索提示收费（每 1,000 条接地提示 25 美元）。只有当提示成功返回至少一个 Google 地图接地结果时，系统才会针对请求收费，无论模型在内部执行了多少个单独的搜索查询来获取该结果。

Grounding with Google Maps 的配额通常与底层 Gemini 模型的速率限制一致。如需了解详细的价格信息，请参阅 [Gemini API
价格页面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)。

## 支持的模型

以下模型支持 Grounding with Google Maps：

| 模型 | Grounding with Google Maps |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=zh-cn) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=zh-cn) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-cn) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3 Flash 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-cn) | ✔️ |

## 支持的工具组合

您可以将 Grounding with Google Maps 功能与其他内置工具（例如
[“依托 Google 搜索进行接地”功能](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)，
Gemini 3.5 Flash-Lite 及更新的模型支持此功能）搭配使用，以支持更复杂的使用场景。Gemini 3 模型还支持将这些内置工具与自定义工具（函数调用）相结合。如需了解详情，请参阅
[工具组合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)页面。

## 后续步骤

- 试试 [Gemini API 实战宝典
  中的“依托 Google 搜索进行接地”功能](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=zh-cn)。
- 了解其他[可用工具](https://ai.google.dev/gemini-api/docs/tools?hl=zh-cn)。
- 如需详细了解 Responsible AI 最佳实践和 Gemini API 的安全性
  过滤机制，请参阅[安全设置指南](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-15。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-15。"],[],[]]
