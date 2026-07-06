---
source_url: https://ai.google.dev/gemini-api/docs/openai?hl=ja
fetched_at: 2026-07-06T05:14:43.625069+00:00
title: "OpenAI \u306e\u4e92\u63db\u6027 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# OpenAI の互換性

Gemini モデルには、OpenAI ライブラリ（Python と TypeScript / JavaScript）と REST API を使用してアクセスできます。これには、3 行のコードを更新し、[Gemini API キー](https://aistudio.google.com/apikey?hl=ja)を使用します。OpenAI ライブラリを使用していない場合は、[Gemini API を直接](https://ai.google.dev/gemini-api/docs/get-started?hl=ja)呼び出すことをおすすめします。

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: [
        {   role: "system",
            content: "You are a helpful assistant." 
        },
        {
            role: "user",
            content: "Explain to me how AI works",
        },
    ],
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.5-flash",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

変更点3 行だけです。

- **`api_key="GEMINI_API_KEY"`**: 「`GEMINI_API_KEY`」を実際の Gemini API キーに置き換えます。このキーは [Google AI Studio](https://aistudio.google.com?hl=ja) で取得できます。
- **`base_url="https://generativelanguage.googleapis.com/v1beta/openai/"`:** OpenAI ライブラリに、デフォルトの URL ではなく Gemini API エンドポイントにリクエストを送信するように指示します。
- **`model="gemini-3.5-flash"`**: 互換性のある Gemini モデルを選択する

## 思考モード

Gemini モデルは、複雑な問題を思考するようトレーニングされているため、推論が大幅に改善されています。Gemini API には、モデルの思考量をきめ細かく制御できる[思考パラメータ](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)が用意されています。

Gemini モデルごとに推論構成が異なります。OpenAI の推論の取り組みとのマッピングは次のとおりです。

| `reasoning_effort`（OpenAI） | `thinking_level`（Gemini 3.1 Pro） | `thinking_level`（Gemini 3.1 Flash-Lite） | `thinking_level`（Gemini 3 Flash） | `thinking_budget`（Gemini 2.5） |
| --- | --- | --- | --- | --- |
| `minimal` | `low` | `minimal` | `minimal` | `1,024` |
| `low` | `low` | `low` | `low` | `1,024` |
| `medium` | `medium` | `medium` | `medium` | `8,192` |
| `high` | `high` | `high` | `high` | `24,576` |

`reasoning_effort` が指定されていない場合、Gemini はモデルのデフォルトの[レベル](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#levels)または[予算](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#set-budget)を使用します。

思考を無効にする場合は、2.5 モデルの `reasoning_effort` を `"none"` に設定します。Gemini 2.5 Pro モデルまたは Gemini 3 モデルでは推論を無効にできません。

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    reasoning_effort="low",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    reasoning_effort: "low",
    messages: [
        {   role: "system",
            content: "You are a helpful assistant." 
        },
        {
            role: "user",
            content: "Explain to me how AI works",
        },
    ],
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.5-flash",
    "reasoning_effort": "low",
    "messages": [
      {
        "role": "user",
        "content": "Explain to me how AI works"
      }
    ]
  }'
```

Gemini の思考モデルは、[思考の要約](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#summaries)も生成します。[`extra_body`](#extra-body) フィールドを使用して、リクエストに Gemini フィールドを含めることができます。

`reasoning_effort` と `thinking_level`/`thinking_budget` は機能が重複しているため、同時に使用することはできません。

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": "Explain to me how AI works"}],
    extra_body={
      'extra_body': {
        "google": {
          "thinking_config": {
            "thinking_level": "low",
            "include_thoughts": True
          }
        }
      }
    }
)

print(response.choices[0].message)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

const response = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: [{role: "user", content: "Explain to me how AI works",}],
    extra_body: {
      "google": {
        "thinking_config": {
          "thinking_level": "low",
          "include_thoughts": true
        }
      }
    }
});

console.log(response.choices[0].message);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.5-flash",
        "messages": [{"role": "user", "content": "Explain to me how AI works"}],
        "extra_body": {
          "google": {
            "thinking_config": {
              "thinking_level": "low",
              "include_thoughts": true
            }
          }
        }
      }'
```

Gemini 3 は、チャット補完 API の思考シグネチャの OpenAI 互換性をサポートしています。完全な例は、[思考シグネチャ](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ja#openai)のページで確認できます。

## ストリーミング

Gemini API は[ストリーミング レスポンス](https://ai.google.dev/gemini-api/docs/text-generation?lang=python&hl=ja#generate-a-text-stream)をサポートしています。

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
  model="gemini-3.5-flash",
  messages=[
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {   "role": "user",
        "content": "Hello!"
    }
  ],
  stream=True
)

for chunk in response:
    print(chunk.choices[0].delta)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: [
      {
          "role": "system",
          "content": "You are a helpful assistant."
      },
      {
          "role": "user",
          "content": "Hello!"
      }
    ],
    stream: true,
  });

  for await (const chunk of completion) {
    console.log(chunk.choices[0].delta.content);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.5-flash",
      "messages": [
          {"role": "user", "content": "Explain to me how AI works"}
      ],
      "stream": true
    }'
```

## 関数呼び出し

関数呼び出しを使用すると、生成モデルから構造化データ出力を簡単に取得できます。これは [Gemini API でサポート](https://ai.google.dev/gemini-api/docs/function-calling/tutorial?hl=ja)されています。

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

tools = [
  {
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get the weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. Chicago, IL",
          },
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
      },
    }
  }
]

messages = [{"role": "user", "content": "What's the weather like in Chicago today?"}]
response = client.chat.completions.create(
  model="gemini-3.5-flash",
  messages=messages,
  tools=tools,
  tool_choice="auto"
)

print(response)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const messages = [{"role": "user", "content": "What's the weather like in Chicago today?"}];
  const tools = [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "Get the weather in a given location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. Chicago, IL",
              },
              "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
          },
        }
      }
  ];

  const response = await openai.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: messages,
    tools: tools,
    tool_choice: "auto",
  });

  console.log(response);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.5-flash",
  "messages": [
    {
      "role": "user",
      "content": "What'\''s the weather like in Chicago today?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. Chicago, IL"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location"]
        }
      }
    }
  ],
  "tool_choice": "auto"
}'
```

## 画像理解

Gemini モデルはネイティブ マルチモーダルであり、[多くの一般的なビジョンタスク](https://ai.google.dev/gemini-api/docs/vision?hl=ja)でクラス最高のパフォーマンスを実現します。

### Python

```
import base64
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Getting the base64 string
base64_image = encode_image("Path/to/agi/image.jpeg")

response = client.chat.completions.create(
  model="gemini-3.5-flash",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url":  f"data:image/jpeg;base64,{base64_image}"
          },
        },
      ],
    }
  ],
)

print(response.choices[0])
```

### JavaScript

```
import OpenAI from "openai";
import fs from 'fs/promises';

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function encodeImage(imagePath) {
  try {
    const imageBuffer = await fs.readFile(imagePath);
    return imageBuffer.toString('base64');
  } catch (error) {
    console.error("Error encoding image:", error);
    return null;
  }
}

async function main() {
  const imagePath = "Path/to/agi/image.jpeg";
  const base64Image = await encodeImage(imagePath);

  const messages = [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url": `data:image/jpeg;base64,${base64Image}`
          },
        },
      ],
    }
  ];

  try {
    const response = await openai.chat.completions.create({
      model: "gemini-3.5-flash",
      messages: messages,
    });

    console.log(response.choices[0]);
  } catch (error) {
    console.error("Error calling Gemini API:", error);
  }
}

main();
```

### REST

```
bash -c '
  base64_image=$(base64 -i "Path/to/agi/image.jpeg");
  curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer GEMINI_API_KEY" \
    -d "{
      \"model\": \"gemini-3.5-flash\",
      \"messages\": [
        {
          \"role\": \"user\",
          \"content\": [
            { \"type\": \"text\", \"text\": \"What is in this image?\" },
            {
              \"type\": \"image_url\",
              \"image_url\": { \"url\": \"data:image/jpeg;base64,${base64_image}\" }
            }
          ]
        }
      ]
    }"
'
```

## 画像を生成

`gemini-2.5-flash-image` または `gemini-3-pro-image-preview` を使用して画像を生成します。サポートされているパラメータには、`prompt`、`model`、`n`、`size`、`response_format` があります。ここに記載されていないパラメータ、または [`extra_body`](#extra-body) セクションに記載されていないパラメータは、互換性レイヤによって通知なく無視されます。

### Python

```
import base64
from openai import OpenAI
from PIL import Image
from io import BytesIO

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.images.generate(
    model="gemini-2.5-flash-image",
    prompt="a portrait of a sheepadoodle wearing a cape",
    response_format='b64_json',
    n=1,
)

for image_data in response.data:
  image = Image.open(BytesIO(base64.b64decode(image_data.b64_json)))
  image.show()
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const image = await openai.images.generate(
    {
      model: "gemini-2.5-flash-image",
      prompt: "a portrait of a sheepadoodle wearing a cape",
      response_format: "b64_json",
      n: 1,
    }
  );

  console.log(image.data);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/images/generations" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer GEMINI_API_KEY" \
  -d '{
        "model": "gemini-2.5-flash-image",
        "prompt": "a portrait of a sheepadoodle wearing a cape",
        "response_format": "b64_json",
        "n": 1,
      }'
```

## 動画を生成

Sora 互換の `/v1/videos` エンドポイントを介して `veo-3.1-generate-preview` を使用して動画を生成します。サポートされている最上位パラメータは `prompt` と `model` です。`duration_seconds`、`image`、`aspect_ratio` などの追加パラメータは、`extra_body` とともに渡す必要があります。使用可能なすべてのパラメータについては、[`extra_body`](#extra-body) セクションをご覧ください。

動画生成は、完了のためにポーリングできるオペレーション ID を返す長時間実行オペレーションです。

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Returns a Long Running Operation (status: processing)
response = client.videos.create(
    model="veo-3.1-generate-preview",
    prompt="A cinematic drone shot of a waterfall",
)

print(f"Operation ID: {response.id}")
print(f"Status: {response.status}")
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
    // Returns a Long Running Operation (status: processing)
    const response = await openai.videos.create({
        model: "veo-3.1-generate-preview",
        prompt: "A cinematic drone shot of a waterfall",
    });

    console.log(`Operation ID: ${response.id}`);
    console.log(`Status: ${response.status}`);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/videos" \
  -H "Authorization: Bearer $GEMINI_API_KEY" \
  -F "model=veo-3.1-generate-preview" \
  -F "prompt=A cinematic drone shot of a waterfall"
```

### 動画のステータスを確認する

動画の生成は非同期です。`GET /v1/videos/{id}` を使用してステータスをポーリングし、完了時に最終的な動画 URL を取得します。

### Python

```
import time
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Poll until video is ready
video_id = response.id  # From the create call
while True:
    video = client.videos.retrieve(video_id)
    if video.status == "completed":
        print(f"Video URL: {video.url}")
        break
    elif video.status == "failed":
        print(f"Generation failed: {video.error}")
        break
    print(f"Status: {video.status}. Waiting...")
    time.sleep(10)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
    // Poll until video is ready
    const videoId = response.id;  // From the create call
    while (true) {
        const video = await openai.videos.retrieve(videoId);
        if (video.status === "completed") {
            console.log(`Video URL: ${video.url}`);
            break;
        } else if (video.status === "failed") {
            console.log(`Generation failed: ${video.error}`);
            break;
        }
        console.log(`Status: ${video.status}. Waiting...`);
        await new Promise(resolve => setTimeout(resolve, 10000));
    }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/videos/VIDEO_ID" \
  -H "Authorization: Bearer $GEMINI_API_KEY"
```

## 音声の理解

以下のように音声入力を分析します。

### Python

```
import base64
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

with open("/path/to/your/audio/file.wav", "rb") as audio_file:
  base64_audio = base64.b64encode(audio_file.read()).decode('utf-8')

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Transcribe this audio",
        },
        {
              "type": "input_audio",
              "input_audio": {
                "data": base64_audio,
                "format": "wav"
          }
        }
      ],
    }
  ],
)

print(response.choices[0].message.content)
```

### JavaScript

```
import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

const audioFile = fs.readFileSync("/path/to/your/audio/file.wav");
const base64Audio = Buffer.from(audioFile).toString("base64");

async function main() {
  const response = await client.chat.completions.create({
    model: "gemini-3.5-flash",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Transcribe this audio",
          },
          {
            type: "input_audio",
            input_audio: {
              data: base64Audio,
              format: "wav",
            },
          },
        ],
      },
    ],
  });

  console.log(response.choices[0].message.content);
}

main();
```

### REST

```
bash -c '
  base64_audio=$(base64 -i "/path/to/your/audio/file.wav");
  curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer GEMINI_API_KEY" \
    -d "{
      \"model\": \"gemini-3.5-flash\",
      \"messages\": [
        {
          \"role\": \"user\",
          \"content\": [
            { \"type\": \"text\", \"text\": \"Transcribe this audio file.\" },
            {
              \"type\": \"input_audio\",
              \"input_audio\": {
                \"data\": \"${base64_audio}\",
                \"format\": \"wav\"
              }
            }
          ]
        }
      ]
    }"
'
```

## 構造化出力

Gemini モデルは、[定義した構造](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)で JSON オブジェクトを出力できます。

### Python

```
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

completion = client.beta.chat.completions.parse(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "John and Susan are going to an AI conference on Friday."},
    ],
    response_format=CalendarEvent,
)

print(completion.choices[0].message.parsed)
```

### JavaScript

```
import OpenAI from "openai";
import { zodResponseFormat } from "openai/helpers/zod";
import { z } from "zod";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai"
});

const CalendarEvent = z.object({
  name: z.string(),
  date: z.string(),
  participants: z.array(z.string()),
});

const completion = await openai.chat.completions.parse({
  model: "gemini-3.5-flash",
  messages: [
    { role: "system", content: "Extract the event information." },
    { role: "user", content: "John and Susan are going to an AI conference on Friday" },
  ],
  response_format: zodResponseFormat(CalendarEvent, "event"),
});

const event = completion.choices[0].message.parsed;
console.log(event);
```

## エンベディング

テキスト エンベディングは、テキスト文字列の関連性を測定し、[Gemini API](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja) を使用して生成できます。マルチモーダル エンベディングには `gemini-embedding-2-preview` を使用し、テキストのみのエンベディングには `gemini-embedding-001` を使用できます。

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.embeddings.create(
    input="Your text string goes here",
    model="gemini-embedding-2-preview"
)

print(response.data[0].embedding)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: "GEMINI_API_KEY",
    baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/"
});

async function main() {
  const embedding = await openai.embeddings.create({
    model: "gemini-embedding-2-preview",
    input: "Your text string goes here",
  });

  console.log(embedding);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/openai/embeddings" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer GEMINI_API_KEY" \
-d '{
    "input": "Your text string goes here",
    "model": "gemini-embedding-2-preview"
  }'
```

## バッチ API

OpenAI ライブラリを使用して、[バッチジョブ](https://ai.google.dev/gemini-api/docs/batch-mode?hl=ja)を作成して送信し、ステータスを確認できます。

OpenAI 入力形式で JSONL ファイルを準備する必要があります。次に例を示します。

```
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.5-flash", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.5-flash", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}
```

Batch の OpenAI 互換性では、バッチの作成、ジョブ ステータスのモニタリング、バッチ結果の表示がサポートされています。

アップロードとダウンロードは現在対象外です。代わりに、次の例では、Gemini [Batch API](https://ai.google.dev/gemini-api/docs/batch-mode?hl=ja#input-file) を使用する場合と同じように、`genai` クライアントを使用して[ファイル](https://ai.google.dev/gemini-api/docs/files?hl=ja)をアップロードおよびダウンロードします。

### Python

```
from openai import OpenAI

# Regular genai client for uploads & downloads
from google import genai
client = genai.Client()

openai_client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Upload the JSONL file in OpenAI input format, using regular genai SDK
uploaded_file = client.files.upload(
    file='my-batch-requests.jsonl',
    config=types.UploadFileConfig(display_name='my-batch-requests', mime_type='jsonl')
)

# Create batch
batch = openai_client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h"
)

# Wait for batch to finish (up to 24h)
while True:
    batch = client.batches.retrieve(batch.id)
    if batch.status in ('completed', 'failed', 'cancelled', 'expired'):
        break
    print(f"Batch not finished. Current state: {batch.status}. Waiting 30 seconds...")
    time.sleep(30)
print(f"Batch finished: {batch}")

# Download results in OpenAI output format, using regular genai SDK
file_content = genai_client.files.download(file=batch.output_file_id).decode('utf-8')

# See batch_output JSONL in OpenAI output format
for line in file_content.splitlines():
    print(line)
```

OpenAI SDK は、[Batch API を使用したエンベディングの生成](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja#batch-embeddings)もサポートしています。これを行うには、`create` メソッドの `endpoint` フィールドをエンベディング エンドポイントに置き換え、JSONL ファイルの `url` キーと `model` キーも置き換えます。

```
# JSONL file using embeddings model and endpoint
# {"custom_id": "request-1", "method": "POST", "url": "/v1/embeddings", "body": {"model": "ggemini-embedding-001", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
# {"custom_id": "request-2", "method": "POST", "url": "/v1/embeddings", "body": {"model": "gemini-embedding-001", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}

# ...

# Create batch step with embeddings endpoint
batch = openai_client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/embeddings",
    completion_window="24h"
)
```

完全な例については、OpenAI 互換性クックブックの[バッチ エンベディング生成](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb)セクションをご覧ください。

## Flex と Priority の推論

Gemini API は、名前とロジックで OpenAI の `service_tier` パラメータと一致し、Flex と Priority の両方の推論階層で制限を適用し、トラフィックを適切に転送します。

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

completion = client.chat.completions.create(
  model="gemini-3.5-flash",
  messages=[
    {"role": "user", "content": "Write a short poem about clouds."}
  ],
  service_tier="priority" # Or service_tier="flex"
)

print(completion)
```

明示的に割り当てられていない場合、`service_tier` はデフォルトで `standard` に設定されます。これは OpenAI の `default` と同等です。推論階層の詳細については、[最適化](https://ai.google.dev/gemini-api/docs/optimization?hl=ja)のドキュメントをご覧ください。

## `extra_body` で Gemini の機能を有効にする

Gemini でサポートされている機能のうち、OpenAI モデルでは利用できないものがいくつかありますが、`extra_body` フィールドを使用して有効にできます。

| パラメータ | タイプ | エンドポイント | 説明 |
| --- | --- | --- | --- |
| **`cached_content`** | テキスト | チャット | Gemini の一般的なコンテンツ キャッシュに対応します。 |
| **`thinking_config`** | オブジェクト | チャット | Gemini の ThinkingConfig に対応します。 |
| **`aspect_ratio`** | テキスト | 画像 | 出力アスペクト比（`"16:9"`、`"1:1"`、`"9:16"` など）。 |
| **`generation_config`** | オブジェクト | 画像 | Gemini 生成構成オブジェクト（`{"responseModalities": ["IMAGE"], "candidateCount": 2}` など）。 |
| **`safety_settings`** | リスト | 画像 | カスタムの安全しきい値フィルタ（例: `[{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"}]`）。 |
| **`tools`** | リスト | 画像 | グラウンディング（`[{"google_search": {}}]` など）を有効にします。`gemini-3-pro-image-preview` のみ。 |
| **`aspect_ratio`** | テキスト | 動画 | 出力動画のサイズ（横向きの場合は `16:9`、縦向きの場合は `9:16`）。指定しない場合、`size` からマップします。 |
| **`resolution`** | テキスト | 動画 | 出力解像度（`720p`、`1080p`、`4K`）。注: `1080p` と `4K` はアップサンプラー パイプラインをトリガーします。 |
| **`duration_seconds`** | 整数 | 動画 | 生成の長さ（値: `4`、`6`、`8`）。`reference_images`、補間、拡張機能を使用する場合は `8` にする必要があります。 |
| **`frame_rate`** | テキスト | 動画 | 動画出力のフレームレート（`"24"` など）。 |
| **`input_reference`** | テキスト | 動画 | 動画生成のリファレンス入力。 |
| **`extend_video_id`** | テキスト | 動画 | 延長する既存の動画の ID。 |
| **`negative_prompt`** | テキスト | 動画 | 除外するアイテム（例: `"shaky camera"`）。 |
| **`seed`** | 整数 | 動画 | 決定論的生成の整数。 |
| **`style`** | テキスト | 動画 | ビジュアル スタイル（`cinematic` はデフォルト、`creative` はソーシャル メディア向けに最適化）。 |
| **`person_generation`** | テキスト | 動画 | 人物の生成を制御します（`allow_adult`、`allow_all`、`dont_allow`）。 |
| **`reference_images`** | リスト | 動画 | スタイル/キャラクターの参照用画像（base64 アセット）を最大 3 枚。 |
| **`image`** | テキスト | 動画 | 動画生成の条件付けに使用する、Base64 でエンコードされた初期入力画像。 |
| **`last_frame`** | オブジェクト | 動画 | 補間の最終画像（最初のフレームとして `image` が必要）。 |

### `extra_body` の使用例

`extra_body` を使用して `cached_content` を設定する例を次に示します。

### Python

```
from openai import OpenAI

client = OpenAI(
    api_key=MY_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

stream = client.chat.completions.create(
    model="gemini-3.5-flash",
    n=1,
    messages=[
        {
            "role": "user",
            "content": "Summarize the video"
        }
    ],
    stream=True,
    stream_options={'include_usage': True},
    extra_body={
        'extra_body':
        {
            'google': {
              'cached_content': "cachedContents/0000aaaa1111bbbb2222cccc3333dddd4444eeee"
          }
        }
    }
)

for chunk in stream:
    print(chunk)
    print(chunk.usage.to_dict())
```

## モデルの一覧表示

使用可能な Gemini モデルのリストを取得します。

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

models = client.models.list()
for model in models:
  print(model.id)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const list = await openai.models.list();

  for await (const model of list) {
    console.log(model);
  }
}
main();
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/openai/models \
-H "Authorization: Bearer GEMINI_API_KEY"
```

## モデルを取得する

Gemini モデルを取得します。

### Python

```
from openai import OpenAI

client = OpenAI(
  api_key="GEMINI_API_KEY",
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = client.models.retrieve("gemini-3.5-flash")
print(model.id)
```

### JavaScript

```
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "GEMINI_API_KEY",
  baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/",
});

async function main() {
  const model = await openai.models.retrieve("gemini-3.5-flash");
  console.log(model.id);
}

main();
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/openai/models/gemini-3.5-flash \
-H "Authorization: Bearer GEMINI_API_KEY"
```

## 現在の制限事項

機能サポートの拡大に伴い、OpenAI ライブラリのサポートは引き続きベータ版となります。

サポートされているパラメータ、今後の機能についてご不明な点がある場合や、Gemini の使用を開始する際に問題が発生した場合は、[デベロッパー フォーラム](https://discuss.ai.google.dev/c/gemini-api/4?hl=ja)にご参加ください。

## 次のステップ

[OpenAI 互換性 Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb?hl=ja) を試して、より詳細な例を確認してください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-22 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-22 UTC。"],[],[]]
