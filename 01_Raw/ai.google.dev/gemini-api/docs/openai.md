---
source_url: https://ai.google.dev/gemini-api/docs/openai?hl=zh-CN
fetched_at: 2026-08-17T02:22:57.001523+00:00
title: "OpenAI \u517c\u5bb9\u6027 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# OpenAI 兼容性

您可以使用 OpenAI 库（Python 和 TypeScript /
JavaScript）以及 REST API 来访问 Gemini 模型，只需更新三行代码
并使用您的 [Gemini API 密钥](https://aistudio.google.com/apikey?hl=zh-cn)即可。如果您尚未使用 OpenAI 库，我们建议您直接调用
[Gemini API](https://ai.google.dev/gemini-api/docs/get-started?hl=zh-cn)。

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

有何变化？只有三行！

- **`api_key="GEMINI_API_KEY"`**：将“`GEMINI_API_KEY`”替换为您的实际 Gemini
  API 密钥，您可以在[Google AI Studio](https://aistudio.google.com?hl=zh-cn)中获取该密钥。
- **`base_url="https://generativelanguage.googleapis.com/v1beta/openai/"`:** 这会告知 OpenAI 库将请求发送到 Gemini API 端点，而不是默认网址。
- **`model="gemini-3.5-flash"`**：选择兼容的 Gemini 模型

## 思考

Gemini 模型经过专门训练，能够思考复杂问题，从而大幅提升推理能力。Gemini API 附带 [思考
参数](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)，可用于精细
控制模型的思考量。

不同的 Gemini 模型具有不同的推理配置，您可以按如下方式查看它们与 OpenAI 推理工作的对应关系：

| `reasoning_effort` (OpenAI) | `thinking_level` (Gemini 3.1 Pro) | `thinking_level` (Gemini 3.1 Flash-Lite) | `thinking_level` (Gemini 3 Flash) | `thinking_budget` (Gemini 2.5) |
| --- | --- | --- | --- | --- |
| `minimal` | `low` | `minimal` | `minimal` | `1,024` |
| `low` | `low` | `low` | `low` | `1,024` |
| `medium` | `medium` | `medium` | `medium` | `8,192` |
| `high` | `high` | `high` | `high` | `24,576` |

如果未指定 `reasoning_effort`，Gemini 会使用模型的
默认 [级别](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn#levels) 或 [预算](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn#set-budget)。

如果您想停用思考功能，可以为
2.5 模型将 `reasoning_effort` 设置为 `"none"`。对于 Gemini 2.5 Pro 或 3 模型，无法关闭推理功能。

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

Gemini 思考模型还会生成[思考摘要](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn#summaries)。
您可以使用 [`extra_body`](#extra-body) 字段在请求中添加 Gemini 字段
在您的请求中。

请注意，`reasoning_effort` 和 `thinking_level`/`thinking_budget` 的功能重叠，因此不能同时使用。

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

Gemini 3 支持在聊天补全 API 中使用 OpenAI 兼容的思考签名。您可以在[思考签名](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=zh-cn#openai)页面上找到完整示例。

## 流式

Gemini API 支持[流式回答](https://ai.google.dev/gemini-api/docs/text-generation?lang=python&hl=zh-cn#generate-a-text-stream)。

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

## 函数调用

函数调用功能可让您更轻松地从
生成式模型获取结构化数据输出，并且在 Gemini API 中[受支持](https://ai.google.dev/gemini-api/docs/function-calling/tutorial?hl=zh-cn)。

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

## 图片理解

Gemini 模型是原生多模态模型，在
[许多常见的视觉任务中](https://ai.google.dev/gemini-api/docs/vision?hl=zh-cn)可提供出色的性能。

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

## 生成图片

使用 `gemini-2.5-flash-image` 或 `gemini-3-pro-image-preview` 生成图片。支持的参数包括 `prompt`、`model`、`n`、`size` 和 `response_format`。兼容性层会默默忽略此处或 [`extra_body`](#extra-body) 部分中未列出的任何其他参数。

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

## 生成视频

通过与 Sora 兼容的 `/v1/videos` 端点，使用 `veo-3.1-generate-preview` 生成视频。支持的顶级参数包括 `prompt` 和 `model`。必须使用 `extra_body` 传递其他参数，例如 `duration_seconds`、`image` 和 `aspect_ratio`。如需查看所有可用参数，请参阅 [`extra_body`](#extra-body) section
。

视频生成是一项长时间运行的操作，会返回一个操作 ID，您可以轮询该 ID 以检查操作是否完成。

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

### 检查视频状态

视频生成是异步的。使用 `GET /v1/videos/{id}` 轮询状态，并在完成后检索最终视频网址：

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

## 音频理解

分析音频输入：

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

## 结构化输出

Gemini 模型可以输出采用您定义的任何 [结构的 JSON 对象](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)。

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

## Embeddings

文本嵌入用于衡量文本字符串的相关性，可以使用
[Gemini API](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-cn)生成。您可以将 `gemini-embedding-2-preview` 用于多模态嵌入，或将 `gemini-embedding-001` 用于仅限文本的嵌入。

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

## Batch API

您可以使用 OpenAI 库创建 [批处理作业](https://ai.google.dev/gemini-api/docs/batch-mode?hl=zh-cn)、提交作业并检查
作业状态。

您需要准备采用 OpenAI 输入格式的 JSONL 文件。例如：

```
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.5-flash", "messages": [{"role": "user", "content": "Tell me a one-sentence joke."}]}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gemini-3.5-flash", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}
```

Batch 的 OpenAI 兼容性支持创建批处理、监控作业状态和查看批处理结果。

目前不支持上传和下载的兼容性。相反，以下示例使用 `genai` 客户端上传和下载
[文件](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn)，这与使用 Gemini [Batch API](https://ai.google.dev/gemini-api/docs/batch-mode?hl=zh-cn#input-file) 时相同。

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

OpenAI SDK 还支持[使用 Batch API 生成嵌入](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn#batch-embeddings)。为此，请将 `create` 方法的 `endpoint` 字段替换为嵌入端点，并将 JSONL 文件中的 `url` 和 `model` 键替换为：

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

如需查看完整示例，请参阅 OpenAI 兼容性实用手册的[批量嵌入生成](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb)
部分。

## Flex 和 Priority 推理

Gemini API 在名称和逻辑上与 OpenAI 的 `service_tier` 参数匹配，对 Flex 和 Priority 推理层强制执行限制并妥善引导流量。

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

如果未明确分配，`service_tier` 默认设置为 `standard`，相当于 OpenAI 的 `default`。
如需详细了解推理层，请参阅[优化](https://ai.google.dev/gemini-api/docs/optimization?hl=zh-cn)文档。

## 使用 `extra_body` 启用 Gemini 功能

Gemini 支持多项 OpenAI 模型中没有的功能，但可以使用 `extra_body` 字段启用这些功能。

| 参数 | 类型 | 端点 | 说明 |
| --- | --- | --- | --- |
| **`cached_content`** | 文字 | 聊天 | 对应于 Gemini 的通用内容缓存。 |
| **`thinking_config`** | 对象 | 聊天 | 对应于 Gemini 的 ThinkingConfig。 |
| **`aspect_ratio`** | 文字 | Google 图片 | 输出宽高比（例如 `"16:9"`、`"1:1"`、`"9:16"`）。 |
| **`generation_config`** | 对象 | Google 图片 | Gemini 生成配置对象（例如 `{"responseModalities": ["IMAGE"], "candidateCount": 2}`）。 |
| **`safety_settings`** | 列表 | Google 图片 | 自定义安全阈值过滤条件（例如 `[{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"}]`）。 |
| **`tools`** | 列表 | Google 图片 | 启用 Grounding（例如 `[{"google_search": {}}]`）。仅适用于 `gemini-3-pro-image-preview`。 |
| **`aspect_ratio`** | 文字 | 视频 | 输出视频的尺寸（横向为 `16:9`，纵向为 `9:16`）。如果未指定，则从 `size` 映射。 |
| **`resolution`** | 文字 | 视频 | 输出分辨率（`720p`、`1080p`、`4K`）。注意：`1080p` 和 `4K` 会触发升采样器流水线。 |
| **`duration_seconds`** | 整数 | 视频 | 生成时长（值：`4`、`6`、`8`）。使用 `reference_images`、插值或扩展程序时，必须为 `8`。 |
| **`frame_rate`** | 文字 | 视频 | 视频输出的帧速率（例如 `"24"`）。 |
| **`input_reference`** | 文字 | 视频 | 用于生成视频的参考输入。 |
| **`extend_video_id`** | 文字 | 视频 | 要延长的现有视频的 ID。 |
| **`negative_prompt`** | 文字 | 视频 | 要排除的项（例如 `"shaky camera"`）。 |
| **`seed`** | 整数 | 视频 | 用于确定性生成的整数。 |
| **`style`** | 文字 | 视频 | 视觉样式（默认 `cinematic`，针对社交媒体优化的 `creative`）。 |
| **`person_generation`** | 文字 | 视频 | 控制人物的生成（`allow_adult`、`allow_all`、`dont_allow`）。 |
| **`reference_images`** | 列表 | 视频 | 最多 3 张图片，用于样式/人物参考（base64 素材资源）。 |
| **`image`** | 文字 | 视频 | 经过 base64 编码的初始输入图片，用于调节视频生成。 |
| **`last_frame`** | 对象 | 视频 | 用于插值的最终图片（需要将 `image` 作为第一帧）。 |

### 使用 `extra_body` 的示例

以下示例展示了如何使用 `extra_body` 设置 `cached_content`：

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

## 列出模型

获取可用 Gemini 模型的列表：

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

## 检索模型

检索 Gemini 模型：

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

## 当前限制

在扩展功能支持的同时，对 OpenAI 库的支持仍处于 Beta 版阶段。

如果您对支持的参数、即将推出的功能有疑问，或者在开始使用 Gemini 时遇到
任何问题，请加入我们的 [开发者论坛](https://discuss.ai.google.dev/c/gemini-api/4?hl=zh-cn)。

## 后续步骤

尝试我们的 [OpenAI 兼容性 Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb?hl=zh-cn)，了解更多详细
示例。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-22。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-22。"],[],[]]
