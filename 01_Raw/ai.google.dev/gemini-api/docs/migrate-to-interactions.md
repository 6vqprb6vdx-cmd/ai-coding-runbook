---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=zh-CN
fetched_at: 2026-10-05T06:36:50.736747+00:00
title: "\u8fc1\u79fb\u5230 Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 迁移到 Interactions API

本指南可帮助您从 `generateContent` API 迁移到 Interactions API。

Interactions API 是使用 Gemini 模型和智能体进行构建的最简单、最出色的方式。虽然 `generateContent` 仍完全受支持，但我们建议所有新开发项目都使用 Interactions API。

### 为什么迁移？

Interactions API 是使用 Gemini 模型和智能体进行构建的最简单、最出色的方式：

- **服务器端历史记录管理**：通过 `previous_interaction_id` 简化多轮对话流程。服务器默认启用状态 (`store=true`)，但您可以通过设置 `store=false` 选择无状态行为。
- **可观测的执行步骤**：类型化步骤可轻松调试复杂流程，并为中间事件（例如想法或搜索 widget）呈现界面。
- **工具使用和智能体工作流**：通过类型化的执行步骤，原生支持多步骤工具使用、编排和复杂的推理流程。
- **长时间运行的任务和后台任务**：支持使用 `background=true` 将耗时的操作（例如 Deep Think 和 Deep Research）分流到后台进程。

## 基本输入/输出

本部分展示了如何迁移简单的文本生成请求。

### 之前 (`generateContent`)

`generateContent` API 是无状态的，可直接返回响应。响应结构将输出封装在 `candidates` 列表中，每个都包含一个 `content`，其中包含要解析的 `parts` 列表。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite", contents="Tell me a joke."
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-2.5-flash-lite",
  contents: "Tell me a joke.",
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

GenerateContentResponse response =
    client.models.generateContent("gemini-2.5-flash-lite", "Tell me a joke.", null);
System.out.println(response.text());
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

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-2.5-flash-lite",
        genai.Text("Tell me a joke."),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Tell me a joke."
        }]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Why did the chicken cross the road? To get to the other side!"
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 4,
    "candidatesTokenCount": 12,
    "totalTokenCount": 16
  }
}
```

Interactions API 会返回具有 `steps` 时间轴的已存储互动资源。虽然您可以手动检查 `steps` 数组来查找中间事件，但 Google GenAI SDK 会在返回的 `Interaction` 对象上直接提供便捷的属性来访问最终输出。

最常用的便捷属性是 **`.output_text`**（字符串），它会自动提取并联接模型回答末尾的连续 `TextContent` 代码块。虽然这对于简单回答来说非常有效，但它不包括被非文本内容（例如想法、图片、音频或工具调用）分隔的早期文本块。对于复杂或交错的多模态回答，您必须手动迭代 `steps`。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash", input="Tell me a joke."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Tell me a joke.'
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me a joke."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Tell me a joke."),
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
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a joke."
}'

# Response
{
  "id": "int_123",
  "status": "completed",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Tell me a joke."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

## 多轮对话

默认情况下，Interactions API 会存储互动，从而实现多轮对话的服务器端状态管理。

### 之前 (`generateContent`)

在 `generateContent` 中，您必须使用 `contents` 数组或客户端聊天辅助程序手动管理对话历史记录。

### Python

**使用聊天帮助程序（推荐）**

```
from google import genai

client = genai.Client()

chat = client.chats.create(model="gemini-2.5-flash-lite")
response1 = chat.send_message("Hi, my name is Phil.")
print(response1.text)

response2 = chat.send_message("What is my name?")
print(response2.text)
```

**手动管理历史记录**

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[
        types.Content(
            role="user", parts=[types.Part.from_text(text="Hi, my name is Phil.")]
        ),
        types.Content(
            role="model",
            parts=[types.Part.from_text(text="Hi Phil, how can I help you?")],
        ),
        types.Content(
            role="user", parts=[types.Part.from_text(text="What is my name?")]
        ),
    ],
)
print(response.text)
```

### JavaScript

**使用聊天帮助程序（推荐）**

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const chat = client.chats.create({ model: 'gemini-2.5-flash-lite' });
let response = await chat.sendMessage({ message: 'Hi, my name is Phil.' });
console.log(response.text);

response = await chat.sendMessage({ message: 'What is my name?' });
console.log(response.text);
```

**手动管理历史记录**

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: [
        { role: 'user', parts: [{ text: 'Hi, my name is Phil.' }] },
        { role: 'model', parts: [{ text: 'Hi Phil, how can I help you?' }] },
        { role: 'user', parts: [{ text: 'What is my name?' }] }
    ]
});
console.log(response.text);
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import java.util.Arrays;

Client client = new Client();

// Using the chat helper (recommended)
Chat chat = client.chats.create("gemini-2.5-flash-lite");
GenerateContentResponse response1 = chat.sendMessage("Hi, my name is Phil.");
System.out.println(response1.text());

GenerateContentResponse response2 = chat.sendMessage("What is my name?");
System.out.println(response2.text());

// Manually managing history
GenerateContentResponse manualResponse =
    client.models.generateContent(
        "gemini-2.5-flash-lite",
        Arrays.asList(
            Content.builder()
                .role("user")
                .parts(Arrays.asList(Part.fromText("Hi, my name is Phil.")))
                .build(),
            Content.builder()
                .role("model")
                .parts(Arrays.asList(Part.fromText("Hi Phil, how can I help you?")))
                .build(),
            Content.builder()
                .role("user")
                .parts(Arrays.asList(Part.fromText("What is my name?")))
                .build()),
        null);
System.out.println(manualResponse.text());
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

    // Using the chat helper (recommended)
    chat, err := client.Chats.Create(ctx, "gemini-2.5-flash-lite", nil, nil)
    if err != nil {
        log.Fatal(err)
    }
    response1, err := chat.SendMessage(ctx, genai.Part{Text: "Hi, my name is Phil."})
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response1.Text())

    response2, err := chat.SendMessage(ctx, genai.Part{Text: "What is my name?"})
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response2.Text())

    // Manually managing history
    history := []*genai.Content{
        genai.NewContentFromText("Hi, my name is Phil.", genai.RoleUser),
        genai.NewContentFromText("Hi Phil, how can I help you?", genai.RoleModel),
        genai.NewContentFromText("What is my name?", genai.RoleUser),
    }
    manualResponse, err := client.Models.GenerateContent(ctx, "gemini-2.5-flash-lite", history, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(manualResponse.Text())
}
```

### REST

```
# Request (the second turn requires sending the entire history)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [
        {"role": "user", "parts": [{"text": "Hi, my name is Phil."}]},
        {"role": "model", "parts": [{"text": "Hi Phil, how can I help you?"}]},
        {"role": "user", "parts": [{"text": "What is my name?"}]}
    ]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Your name is Phil."
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ]
}
```

### 之后（Interactions API）

Interactions API 在服务器上管理状态。您可以通过引用 `previous_interaction_id` 继续对话。

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.8-flash", input="Hi, my name is Phil."
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    previous_interaction_id=interaction1.id,
    input="What is my name?",
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Hi, my name is Phil.'
});
console.log("Response 1:", interaction.output_text);

interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    previous_interaction_id: interaction.id,
    input: 'What is my name?'
});
console.log("Response 2:", interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction req1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Hi, my name is Phil."))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(req1)).interaction().get();
System.out.println("Response 1: " + interaction1.outputText().orElse(""));

CreateModelInteraction req2 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .previousInteractionId(interaction1.id().orElse(""))
        .input(InteractionsInput.of("What is my name?"))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(req2)).interaction().get();
System.out.println("Response 2: " + interaction2.outputText().orElse(""));
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Hi, my name is Phil."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res1.Interaction.OutputText != nil {
        fmt.Println("Response 1:", *res1.Interaction.OutputText)
    }

    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            PreviousInteractionID: res1.Interaction.ID,
            Input:                 interactions.NewInteractionsInput("What is my name?"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res2.Interaction.OutputText != nil {
        fmt.Println("Response 2:", *res2.Interaction.OutputText)
    }
}
```

### REST

```
# First Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Hi, my name is Phil."
}'

# Second Request (using ID from first response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "previous_interaction_id": "int_123",
    "input": "What is my name?"
}'

# Response to Second Request
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Hi, my name is Phil." }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [{ "type": "text", "text": "Hello Phil! How can I help you today?" }]
    },
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "What is my name?" }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [{ "type": "text", "text": "Your name is Phil." }]
    }
  ]
}
```

## 多模态输入

这两个 API 都支持多模态输入（文本、图片、视频等）。

### 之前 (`generateContent`)

在 `generateContent` 中，您可以在 `contents` 数组中传递 `parts` 的列表。响应会在第一个候选对象的 `parts` 中返回输出。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open("sample.jpg", "rb") as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
        "Describe this image.",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const imageBytes = fs.readFileSync('sample.jpg').toString('base64');

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: [
        {
            inlineData: {
                data: imageBytes,
                mimeType: 'image/jpeg',
            },
        },
        'Describe this image.',
    ],
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("sample.jpg"));

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-2.5-flash-lite",
        Content.fromParts(
            Part.fromBytes(imageBytes, "image/jpeg"), Part.fromText("Describe this image.")),
        null);
System.out.println(response.text());
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    imageBytes, err := os.ReadFile("sample.jpg")
    if err != nil {
        log.Fatal(err)
    }

    contents := []*genai.Content{
        genai.NewContentFromParts([]*genai.Part{
            genai.NewPartFromBytes(imageBytes, "image/jpeg"),
            genai.NewPartFromText("Describe this image."),
        }, genai.RoleUser),
    }

    response, err := client.Models.GenerateContent(ctx, "gemini-2.5-flash-lite", contents, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [
            {
                "inlineData": {
                    "mimeType": "image/jpeg",
                    "data": "..."
                }
            },
            {
                "text": "Describe this image."
            }
        ]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "This is a picture of a beautiful sunset."
          }
        ],
        "role": "model"
      }
    }
  ]
}
```

### 之后（Interactions API）

在 Interactions API 中，您需要将数组传递给 `input` 字段。您可以在时间轴中找到 `model_output` 步骤，以检索输出内容。

### Python

```
import base64
from google import genai

client = genai.Client()

with open("sample.jpg", "rb") as f:
    image_bytes = f.read()
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
        {"type": "text", "text": "Describe this image."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const imageBytes = fs.readFileSync('sample.jpg').toString('base64');

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: [
        {
            type: 'image',
            mime_type: 'image/jpeg',
            data: imageBytes
        },
        {
            type: 'text',
            text: 'Describe this image.'
        }
    ]
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("sample.jpg"));
String base64ImageData = Base64.getEncoder().encodeToString(imageBytes);

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    ImageContent.builder()
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .data(base64ImageData)
                        .build(),
                    TextContent.builder().text("Describe this image.").build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    imageBytes, err := os.ReadFile("sample.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64ImageData := base64.StdEncoding.EncodeToString(imageBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    MimeType: interactions.ImageContentMimeType("image/jpeg").ToPointer(),
                    Data:     genai.Ptr(base64ImageData),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe this image.",
                }),
            }),
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
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": [
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": "..."
        },
        {
            "type": "text",
            "text": "Describe this image."
        }
    ]
}'

# Response
{
  "id": "int_multimodal",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        {
          "type": "image",
          "mime_type": "image/jpeg",
          "data": "..."
        },
        {
          "type": "text",
          "text": "Describe this image."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "This is a picture of a beautiful sunset over the mountains."
        }
      ]
    }
  ]
}
```

## 结构化输出

如需让模型返回符合特定架构的 JSON，请配置回答格式。

### 之前 (`generateContent`)

在 `generateContent` 中，您可以使用嵌套在 `config`（或 `generationConfig`）对象内的 `response_mime_type` 和 `response_schema` 字段来配置输出格式。

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel

client = genai.Client()

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Give me a recipe for chocolate chip cookies.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Recipe,
    ),
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: 'Give me a recipe for chocolate chip cookies.',
    config: {
        responseMimeType: 'application/json',
        responseSchema: {
            type: Type.OBJECT,
            properties: {
                recipe_name: { type: Type.STRING },
                ingredients: {
                    type: Type.ARRAY,
                    items: { type: Type.STRING },
                },
            },
            required: ['recipe_name', 'ingredients'],
        },
    },
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Schema;
import com.google.genai.types.Type;
import java.util.Arrays;
import java.util.Map;

Client client = new Client();

Schema recipeSchema =
    Schema.builder()
        .type(Type.Known.OBJECT)
        .properties(
            Map.of(
                "recipe_name", Schema.builder().type(Type.Known.STRING).build(),
                "ingredients",
                    Schema.builder()
                        .type(Type.Known.ARRAY)
                        .items(Schema.builder().type(Type.Known.STRING).build())
                        .build()))
        .required(Arrays.asList("recipe_name", "ingredients"))
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-2.5-flash-lite",
        "Give me a recipe for chocolate chip cookies.",
        GenerateContentConfig.builder()
            .responseMimeType("application/json")
            .responseSchema(recipeSchema)
            .build());
System.out.println(response.text());
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

    recipeSchema := &genai.Schema{
        Type: genai.TypeObject,
        Properties: map[string]*genai.Schema{
            "recipe_name": {Type: genai.TypeString},
            "ingredients": {
                Type:  genai.TypeArray,
                Items: &genai.Schema{Type: genai.TypeString},
            },
        },
        Required: []string{"recipe_name", "ingredients"},
    }

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-2.5-flash-lite",
        genai.Text("Give me a recipe for chocolate chip cookies."),
        &genai.GenerateContentConfig{
            ResponseMIMEType: "application/json",
            ResponseSchema:   recipeSchema,
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Give me a recipe for chocolate chip cookies."
        }]
    }],
    "generationConfig": {
        "responseMimeType": "application/json",
        "responseSchema": {
            "type": "OBJECT",
            "properties": {
                "recipe_name": { "type": "STRING" },
                "ingredients": {
                    "type": "ARRAY",
                    "items": { "type": "STRING" }
                }
            },
            "required": ["recipe_name", "ingredients"]
        }
    }
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"
          }
        ],
        "role": "model"
      }
    }
  ]
}
```

### 之后（Interactions API）

在 Interactions API 中，输出格式控制移至顶级 `response_format` 数组。

### Python

```
from google import genai
from pydantic import BaseModel

client = genai.Client()

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Give me a recipe for chocolate chip cookies.",
    response_format=[
        {
            "type": "text",
            "mime_type": "application/json",
            "schema": Recipe.model_json_schema(),
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Give me a recipe for chocolate chip cookies.',
    response_format: [
        {
            type: 'text',
            mime_type: 'application/json',
            schema: {
                type: 'object',
                properties: {
                    recipe_name: { type: 'string' },
                    ingredients: {
                        type: 'array',
                        items: { type: 'string' }
                    }
                },
                required: ['recipe_name', 'ingredients']
            }
        }
    ]
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();
properties.put("recipe_name", Map.of("type", "string"));
properties.put("ingredients", Map.of("type", "array", "items", Map.of("type", "string")));

Map<String, Object> schema = new HashMap<>();
schema.put("type", "object");
schema.put("properties", properties);
schema.put("required", Arrays.asList("recipe_name", "ingredients"));

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Give me a recipe for chocolate chip cookies."))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                Arrays.asList(
                    ResponseFormat.of(
                        TextResponseFormat.builder()
                            .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                            .schema(schema)
                            .build()))))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    schema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "recipe_name": map[string]any{"type": "string"},
            "ingredients": map[string]any{
                "type":  "array",
                "items": map[string]any{"type": "string"},
            },
        },
        "required": []string{"recipe_name", "ingredients"},
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Give me a recipe for chocolate chip cookies."),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.TextResponseFormat{
                    MimeType: interactions.TextResponseFormatMimeType("application/json").ToPointer(),
                    Schema:   schema,
                }),
            )),
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
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Give me a recipe for chocolate chip cookies.",
    "response_format": [
        {
            "type": "text",
            "mime_type": "application/json",
            "schema": {
                "type": "OBJECT",
                "properties": {
                    "recipe_name": { "type": "STRING" },
                    "ingredients": {
                        "type": "ARRAY",
                        "items": { "type": "STRING" }
                    }
                },
                "required": ["recipe_name", "ingredients"]
            }
        }
    ]
}'

# Response
{
  "id": "int_structured",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Give me a recipe for chocolate chip cookies." }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"
        }
      ]
    }
  ]
}
```

## 多模态生成

当生成文本以外的模态内容（例如图片或音频）时，主要区别在于回答如何构建生成的媒体。

### 之前 (`generateContent`)

在 `generateContent` 中，响应直接在候选对象的 `parts` 中返回生成的媒体，通常以 `inlineData` 中的 base64 数据形式返回。

```
# Response structure concept
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Here is your generated image:"
          },
          {
            "inlineData": {
              "mimeType": "image/jpeg",
              "data": "...base64..."
            }
          }
        ]
      }
    }
  ]
}
```

### 之后（Interactions API）

在 Interactions API 中，生成的媒体会显示为时间轴中 `model_output` 步骤的 `content` 数组中的不同项，从而保持互动的按时间顺序排列的流程。

```
# Response structure concept
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Here is your generated image:"
        },
        {
          "type": "image",
          "mime_type": "image/jpeg",
          "data": "...base64..." // Or a reference URL in future
        }
      ]
    }
  ]
}
```

这样可确保响应解析与输入和文本输出的处理方式保持一致，即所有内容都是时间轴中的一个步骤。

## 服务器端工具

Gemini 支持内置的服务器端工具，例如 Google 搜索接地。主要区别在于响应如何表示工具执行。

### 之前 (`generateContent`)

在 `generateContent` 中，服务器端工具在很大程度上是不透明的。您启用该工具，并获得包含单独 `groundingMetadata` 对象的最终回答。至关重要的是，引用不是内嵌的；`groundingSupports` 使用字符索引将文本段映射回 `groundingChunks` 中的网页来源。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Who won Euro 2024?",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}]
    ),
)

metadata = response.candidates[0].grounding_metadata
if metadata.search_entry_point:
    print(f"Search Entry Point: {metadata.search_entry_point.rendered_content}")

for support in metadata.grounding_supports:
    print(f"Citation: {support.segment.text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: 'Who won Euro 2024?',
    config: {
        tools: [{ google_search: {} }]
    }
});

const metadata = response.candidates[0].groundingMetadata;
if (metadata.searchEntryPoint) {
    console.log(`Search Entry Point: ${metadata.searchEntryPoint.renderedContent}`);
}
for (const support of metadata.groundingSupports) {
    console.log(`Citation: ${support.segment.text}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Candidate;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.GoogleSearch;
import com.google.genai.types.GroundingMetadata;
import com.google.genai.types.GroundingSupport;
import com.google.genai.types.Tool;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Optional;

Client client = new Client();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-2.5-flash-lite",
        "Who won Euro 2024?",
        GenerateContentConfig.builder()
            .tools(
                Arrays.asList(
                    Tool.builder().googleSearch(GoogleSearch.builder().build()).build()))
            .build());

List<Candidate> candidates = response.candidates().orElse(Collections.emptyList());
if (!candidates.isEmpty() && candidates.get(0).groundingMetadata().isPresent()) {
  GroundingMetadata metadata = candidates.get(0).groundingMetadata().get();
  if (metadata.searchEntryPoint().isPresent()) {
    System.out.println(
        "Search Entry Point: " + metadata.searchEntryPoint().get().renderedContent().orElse(""));
  }
  for (GroundingSupport support : metadata.groundingSupports().orElse(Collections.emptyList())) {
    Optional<String> segmentText = support.segment().flatMap(s -> s.text());
    segmentText.ifPresent(text -> System.out.println("Citation: " + text));
  }
}
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

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-2.5-flash-lite",
        genai.Text("Who won Euro 2024?"),
        &genai.GenerateContentConfig{
            Tools: []*genai.Tool{
                {GoogleSearch: &genai.GoogleSearch{}},
            },
        },
    )
    if err != nil {
        log.Fatal(err)
    }

    if len(response.Candidates) > 0 && response.Candidates[0].GroundingMetadata != nil {
        metadata := response.Candidates[0].GroundingMetadata
        if metadata.SearchEntryPoint != nil {
            fmt.Println("Search Entry Point:", metadata.SearchEntryPoint.RenderedContent)
        }
        for _, support := range metadata.GroundingSupports {
            if support.Segment != nil {
                fmt.Println("Citation:", support.Segment.Text)
            }
        }
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Who won Euro 2024?"
        }]
    }],
    "tools": [{
        "googleSearchRetrieval": {}
    }]
}'

# Response
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

### 之后（Interactions API）

在 Interactions API 中，服务器端工具可提供完全的时间轴透明度。该 API 会将调用和结果记录为不同的执行 `steps`（`google_search_call` 和 `google_search_result`），从而准确显示模型检索到的数据。

此外，该 API 还会**内嵌**返回引用。`model_output` 步骤中的文本项包含自己的 `annotations` 数组，可直接链接到来源，而不是从单独的元数据对象映射索引。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Who won Euro 2024?",
    tools=[{"type": "google_search"}],
)

for step in interaction.steps:
    if step.type == "google_search_result":
        print(f"Search Suggestions: {step.result[0].search_suggestions}")
    elif step.type == "model_output":
        print(f"Answer: {step.content[0].text}")
        if step.content[0].annotations:
            for anno in step.content[0].annotations:
                print(f"Citation: {anno.title} ({anno.uri})")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Who won Euro 2024?',
    tools: [{ type: 'google_search' }]
});

for (const step of interaction.steps) {
    if (step.type === 'google_search_result') {
        console.log(`Search Suggestions: ${step.result[0].search_suggestions}`);
    } else if (step.type === 'model_output') {
        console.log(`Answer: ${step.content[0].text}`);
        if (step.content[0].annotations) {
            for (const anno of step.content[0].annotations) {
                console.log(`Citation: ${anno.title} (${anno.uri})`);
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.GoogleSearchResult;
import com.google.genai.gaos.models.interactions.GoogleSearchResultStep;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.URLCitation;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won Euro 2024?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof GoogleSearchResultStep) {
    GoogleSearchResultStep searchStep = (GoogleSearchResultStep) step;
    for (GoogleSearchResult res : searchStep.result().orElse(Collections.emptyList())) {
      System.out.println("Search Suggestions: " + res.searchSuggestions().orElse(""));
    }
  } else if (step instanceof ModelOutputStep) {
    ModelOutputStep modelOutput = (ModelOutputStep) step;
    for (Content contentBlock : modelOutput.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent) {
        TextContent textContent = (TextContent) contentBlock;
        System.out.println("Answer: " + textContent.text().orElse(""));
        for (Annotation anno : textContent.annotations().orElse(Collections.emptyList())) {
          if (anno instanceof URLCitation) {
            URLCitation cit = (URLCitation) anno;
            System.out.println(
                "Citation: " + cit.title().orElse("") + " (" + cit.url().orElse("") + ")");
          }
        }
      }
    }
  }
}
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Who won Euro 2024?"),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if searchStep := step.GoogleSearchResultStep; searchStep != nil {
            for _, r := range searchStep.Result {
                if r.SearchSuggestions != nil {
                    fmt.Println("Search Suggestions:", *r.SearchSuggestions)
                }
            }
        } else if modelOutput := step.ModelOutputStep; modelOutput != nil {
            for _, contentBlock := range modelOutput.Content {
                if textContent := contentBlock.TextContent; textContent != nil {
                    fmt.Println("Answer:", textContent.Text)
                    for _, anno := range textContent.Annotations {
                        if cit := anno.URLCitation; cit != nil {
                            fmt.Printf("Citation: %s (%s)\n", cit.GetTitle(), cit.GetURL())
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "Who won Euro 2024?",
    "tools": [{"type": "google_search"}]
}'

# Response (showing grounding)
{
  "id": "int_grounded",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Who won Euro 2024?" }]
    },
    {
      "type": "google_search_call",
      "status": "done",
      "content": [{ "type": "text", "text": "UEFA Euro 2024 winner" }]
    },
    {
      "type": "google_search_result",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024..."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1.",
          "annotations": [
            {
              "start_index": 0,
              "end_index": 42,
              "uri": "https://vertexaisearch...",
              "title": "aljazeera.com"
            }
          ]
        }
      ]
    }
  ]
}
```

## 函数调用

函数调用和结果的结构也已更改，以适应步骤架构。

### 之前 (`generateContent`)

在 `generateContent` 中，响应会返回候选对象中的函数调用。\* {Python}

```
```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="What's the weather in Boston?",
    config=types.GenerateContentConfig(tools=[weather_tool]),
)

function_call = response.candidates[0].content.parts[0].function_call
print(f"Requested tool: {function_call.name}")

result = "52°F and rain"

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="What's the weather in Boston?")
            ],
        ),
        response.candidates[0].content,
        types.Content(
            role="user",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"result": result},
                )
            ],
        ),
    ],
    config=types.GenerateContentConfig(tools=[weather_tool]),
)
print(response.text)
```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: "What's the weather in Boston?",
    config: { tools: [weatherTool] }
});

const functionCall = response.candidates[0].content.parts[0].functionCall;
console.log(`Requested tool: ${functionCall.name}`);

const result = "52°F and rain";

response = await client.models.generateContent({
    model: 'gemini-2.5-flash-lite',
    contents: [
        { role: 'user', parts: [{ text: "What's the weather in Boston?" }] },
        response.candidates[0].content,
        {
            role: 'user',
            parts: [{
                functionResponse: {
                    name: functionCall.name,
                    response: { result: result }
                }
            }]
        }
    ],
    config: { tools: [weatherTool] }
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.FunctionCall;
import com.google.genai.types.FunctionDeclaration;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import com.google.genai.types.Schema;
import com.google.genai.types.Tool;
import com.google.genai.types.Type;
import java.util.Arrays;
import java.util.Map;

Client client = new Client();

FunctionDeclaration weatherFunc =
    FunctionDeclaration.builder()
        .name("get_weather")
        .description("Gets weather")
        .parameters(
            Schema.builder()
                .type(Type.Known.OBJECT)
                .properties(Map.of("location", Schema.builder().type(Type.Known.STRING).build()))
                .build())
        .build();

Tool weatherTool = Tool.builder().functionDeclarations(Arrays.asList(weatherFunc)).build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-2.5-flash-lite",
        "What's the weather in Boston?",
        GenerateContentConfig.builder().tools(Arrays.asList(weatherTool)).build());

FunctionCall functionCall = response.functionCalls().get(0);
System.out.println("Requested tool: " + functionCall.name().orElse(""));

String result = "52°F and rain";

GenerateContentResponse finalResponse =
    client.models.generateContent(
        "gemini-2.5-flash-lite",
        Arrays.asList(
            Content.builder()
                .role("user")
                .parts(Arrays.asList(Part.fromText("What's the weather in Boston?")))
                .build(),
            response.candidates().get().get(0).content().get(),
            Content.builder()
                .role("user")
                .parts(
                    Arrays.asList(
                        Part.fromFunctionResponse(
                            functionCall.name().orElse(""), Map.of("result", result))))
                .build()),
        GenerateContentConfig.builder().tools(Arrays.asList(weatherTool)).build());
System.out.println(finalResponse.text());
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

    weatherTool := &genai.Tool{
        FunctionDeclarations: []*genai.FunctionDeclaration{
            {
                Name:        "get_weather",
                Description: "Gets weather",
                Parameters: &genai.Schema{
                    Type: genai.TypeObject,
                    Properties: map[string]*genai.Schema{
                        "location": {Type: genai.TypeString},
                    },
                },
            },
        },
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{weatherTool},
    }

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-2.5-flash-lite",
        genai.Text("What's the weather in Boston?"),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }

    calls := response.FunctionCalls()
    if len(calls) > 0 {
        functionCall := calls[0]
        fmt.Println("Requested tool:", functionCall.Name)

        result := "52°F and rain"
        history := []*genai.Content{
            genai.NewContentFromText("What's the weather in Boston?", genai.RoleUser),
            response.Candidates[0].Content,
            genai.NewContentFromParts([]*genai.Part{
                genai.NewPartFromFunctionResponse(functionCall.Name, map[string]any{"result": result}),
            }, genai.RoleUser),
        }

        finalResponse, err := client.Models.GenerateContent(ctx, "gemini-2.5-flash-lite", history, config)
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(finalResponse.Text())
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "What is the weather like in Boston, MA?"
        }]
    }],
    "tools": [{
        "functionDeclarations": [{
            "name": "get_weather",
            "description": "Get the current weather",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "location": {"type": "STRING"}
                },
                "required": ["location"]
            }
        }]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "functionCall": {
              "name": "get_weather",
              "args": { "location": "Boston, MA" }
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ]
}
```

### 之后（Interactions API）

工具调用和结果现在是时间轴中的不同步骤。

### Python

```
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets weather",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string"}
        },
    },
}

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's the weather in Boston?",
    tools=[weather_tool],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Executing {step.name} for {step.arguments}")

        result = "52°F and rain"

        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            previous_interaction_id=interaction.id,
            input=[
                {
                    "type": "function_result",
                    "call_id": step.id,
                    "name": step.name,
                    "result": [{"type": "text", "text": result}],
                }
            ],
        )
        print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: "function",
    name: "get_weather",
    description: "Get weather for a location",
    parameters: {
        type: "object",
        properties: {
            location: { type: "string" }
        },
        required: ["location"]
    }
};

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: "What's the weather in Boston?",
    tools: [weatherTool]
});

for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Executing ${step.name} for ${JSON.stringify(step.arguments)}`);

        const result = "52°F and rain";

        const nextInteraction = await client.interactions.create({
            model: 'gemini-3.8-flash',
            previous_interaction_id: interaction.id,
            input: [
                {
                    type: 'function_result',
                    call_id: step.id,
                    name: step.name,
                    result: [{ type: 'text', text: result }]
                }
            ]
        });

        console.log(nextInteraction.output_text);
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();
properties.put("location", Map.of("type", "string"));

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("location"));

Function weatherTool =
    Function.builder()
        .name("get_weather")
        .description("Gets weather")
        .parameters(parameters)
        .build();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What's the weather in Boston?"))
        .tools(Arrays.asList(weatherTool))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof FunctionCallStep) {
    FunctionCallStep fcStep = (FunctionCallStep) step;
    System.out.println(
        "Executing "
            + fcStep.name().orElse("")
            + " for "
            + fcStep.arguments().orElse(Collections.emptyMap()));

    String result = "52°F and rain";

    FunctionResultStep funcResult =
        FunctionResultStep.builder()
            .callId(fcStep.id().orElse(""))
            .name(fcStep.name().orElse(""))
            .result(
                FunctionResultStepResultUnion.of(
                    Arrays.asList(TextContent.builder().text(result).build())))
            .build();

    CreateModelInteraction nextRequest =
        CreateModelInteraction.builder()
            .model(Model.of("gemini-3.8-flash"))
            .previousInteractionId(interaction.id().orElse(""))
            .input(InteractionsInput.ofStep(Arrays.asList(funcResult)))
            .build();

    Interaction nextInteraction =
        client.interactions.create(CreateInteractionRequestBody.of(nextRequest)).interaction().get();
    System.out.println(nextInteraction.outputText().orElse(""));
  }
}
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    weatherTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_weather"),
        Description: genai.Ptr("Gets weather"),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "location": map[string]any{"type": "string"},
            },
            "required": []string{"location"},
        },
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("What's the weather in Boston?"),
            Tools: []interactions.Tool{weatherTool},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if fcStep := step.FunctionCallStep; fcStep != nil {
            fmt.Printf("Executing %s for %v\n", fcStep.Name, fcStep.Arguments)

            result := "52°F and rain"
            funcResult := interactions.NewStep(interactions.FunctionResultStep{
                CallID: fcStep.ID,
                Name:   genai.Ptr(fcStep.Name),
                Result: interactions.NewFunctionResultStepResultUnion([]interactions.FunctionResultSubcontent{
                    interactions.NewFunctionResultSubcontent(interactions.TextContent{Text: result}),
                }),
            })

            nextRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model:                 interactions.Model("gemini-3.8-flash"),
                    PreviousInteractionID: res.Interaction.ID,
                    Input:                 interactions.NewInteractionsInput([]interactions.Step{funcResult}),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            if nextRes.Interaction.OutputText != nil {
                fmt.Println(*nextRes.Interaction.OutputText)
            }
        }
    }
}
```

### REST

```
# Initial Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "What's the weather in Boston?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Get weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": { "type": "string" }
            },
            "required": ["location"]
        }
    }]
}'

# Response (requires action)
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        { "type": "text", "text": "What's the weather in Boston?" }
      ]
    },
    {
      "type": "function_call",
      "status": "waiting",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}

# Submit Tool Result Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "previous_interaction_id": "int_001",
    "input": {
        "type": "function_result",
        "call_id": "fc_1",
        "name": "get_weather",
        "result": [
            { "type": "text", "text": "52°F with rain" }
        ]
    }
}'

# Final Response
{
  "id": "int_002",
  "status": "completed",
  "steps": [
    {
      "type": "function_result",
      "call_id": "fc_1",
      "name": "get_weather",
      "result": [
        { "type": "text", "text": "52°F with rain" }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        { "type": "text", "text": "It's 52°F with rain in Boston." }
      ]
    }
  ]
}
```

## 流式

流式传输的一个主要区别在于，Interactions API 使用的端点与 `generateContent` API 相同，但前者在请求正文中包含 `"stream": true`，而后者需要调用专用端点 (`:streamGenerateContent`)。

此外，流式事件现在使用专用类型来监控互动生命周期，并沿时间轴跟踪执行步骤。

### 之前 (`generateContentStream`)

借助 `generateContent`，您可以接收响应块的流。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content_stream(
    model="gemini-2.5-flash-lite", contents="Tell me a story"
)
for chunk in response:
    print(chunk.text, end="")
```

### JavaScript

```
const responseStream = await client.models.generateContentStream({
    model: 'gemini-2.5-flash-lite',
    contents: 'Tell me a story',
});
for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

try (ResponseStream<GenerateContentResponse> responseStream =
    client.models.generateContentStream("gemini-2.5-flash-lite", "Tell me a story", null)) {
  for (GenerateContentResponse chunk : responseStream) {
    System.out.print(chunk.text());
  }
}
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

    for chunk, err := range client.Models.GenerateContentStream(
        ctx,
        "gemini-2.5-flash-lite",
        genai.Text("Tell me a story"),
        nil,
    ) {
        if err != nil {
            log.Fatal(err)
        }
        fmt.Print(chunk.Text())
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:streamGenerateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Tell me a story"
        }]
    }]
}'

# Response stream
event: content.start
data: {"event_type": "content.start", "index": 0, "content": {"type": "thought"}}
event: content.delta
data: {"event_type": "content.delta", "index": 0, "delta": {"type": "thought_summary", "text": "User wants an explanation."}}
event: content.stop
data: {"event_type": "content.stop", "index": 0}
event: content.start
data: {"event_type": "content.start", "index": 1, "content": {"type": "text"}}
event: content.delta
data: {"event_type": "content.delta", "index": 1, "delta": {"type": "text", "text": "Hello"}}
event: content.stop
data: {"event_type": "content.stop", "index": 1}
```

### 之后（Interactions API）

在 Interactions API 中，流式传输使用服务器发送的事件 (SSE) 和专门的增量类型来表示执行步骤。

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a story",
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta" and event.delta:
        if getattr(event.delta, "type", None) == "text" and getattr(event.delta, "text", None):
            print(event.delta.text, end="", flush=True)
    elif event.event_type == "interaction.completed":
        print(f"\n\n--- Stream Finished ---")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Tell me a story',
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.delta' && event.delta) {
        if (event.delta.type === 'text' && event.delta.text) {
            process.stdout.write(event.delta.text);
        }
    } else if (event.event_type === 'interaction.completed') {
        console.log('\n\n--- Stream Finished ---');
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionCompletedEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me a story"))
        .stream(true)
        .build();

try (EventStream<InteractionSSEStreamEvent> stream =
    client.interactions.create(CreateInteractionRequestBody.of(request)).events()) {
  for (InteractionSSEStreamEvent streamEvent : stream) {
    if (streamEvent.data().isPresent()) {
      InteractionSSEEvent event = streamEvent.data().get();
      if (event instanceof StepDelta) {
        StepDelta stepDelta = (StepDelta) event;
        if (stepDelta.delta().isPresent() && stepDelta.delta().get() instanceof TextDelta) {
          TextDelta textDelta = (TextDelta) stepDelta.delta().get();
          System.out.print(textDelta.text().orElse(""));
        }
      } else if (event instanceof InteractionCompletedEvent) {
        System.out.println("\n\n--- Stream Finished ---");
      }
    }
  }
}
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:  interactions.Model("gemini-3.8-flash"),
            Input:  interactions.NewInteractionsInput("Tell me a story"),
            Stream: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        } else if event.GetDataInteractionCompleted() != nil {
            fmt.Println("\n\n--- Stream Finished ---")
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

# SSE 流输出示例
**event: interaction.created
data: {"type": "interaction.created", "interaction": {"id": "int\_xyz", "status": "created"}}
event: interaction.in\_progress
data: {"type": "interaction.in\_progress", "interaction": {"id": "int\_xyz", "status": "in\_progress"}}
event: step.start
data: {"type": "step.start", "index": 0, "step": {"type": "thought"}}
event: step.delta
data: {"type": "step.delta", "index": 0, "delta": {"type": "thought", "text": "User wants an explanation."}}
event: step.stop
data: {"type": "step.stop", "index": 0, "status": "done"}
event: step.start
data: {"type": "step.start", "index": 1, "step": {"type": "model\_output"}}
event: step.delta
data: {"type": "step.delta", "index": 1, "delta": {"type": "text", "text": "Hello"}}
event: step.stop
data: {"type": "step.stop", "index": 1, "status": "done"}
event: interaction.completed
data: {"type": "interaction.completed", "interaction": {"id": "int\_xyz", "status": "completed", "usage": {"prompt\_tokens": 10, "completion\_tokens": 5, "total\_tokens": 15}}}**
```

### 流式工具和函数调用

信息流中工具的行为方式已从 `generateContent` 发生显著变化，可提供更精细的控制和可见性。

#### 之前 (`generateContent`)

使用 `generateContent` 时，流式函数调用会以单个块的形式完整到达。您无法实时看到正在生成的实参，因此处理程序只是检查是否存在完整的 `functionCall` 对象。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

stream = client.models.generate_content_stream(
    model="gemini-2.5-flash-lite",
    contents="What's the weather in Boston?",
    config=types.GenerateContentConfig(tools=[weather_tool]),
)

for chunk in stream:
    # Function calls arrived complete — no partial arguments
    if chunk.candidates[0].content.parts[0].function_call:
        fc = chunk.candidates[0].content.parts[0].function_call
        print(f"Call: {fc.name}({fc.args})")
    elif chunk.text:
        print(chunk.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.models.generateContentStream({
    model: 'gemini-2.5-flash-lite',
    contents: "What's the weather in Boston?",
    config: { tools: [weatherTool] }
});

for await (const chunk of stream) {
    const part = chunk.candidates[0].content.parts[0];
    if (part.functionCall) {
        console.log(`Call: ${part.functionCall.name}(${JSON.stringify(part.functionCall.args)})`);
    } else if (part.text) {
        process.stdout.write(part.text);
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.FunctionCall;
import com.google.genai.types.FunctionDeclaration;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Schema;
import com.google.genai.types.Tool;
import com.google.genai.types.Type;
import java.util.Arrays;
import java.util.Map;

Client client = new Client();

FunctionDeclaration weatherFunc =
    FunctionDeclaration.builder()
        .name("get_weather")
        .description("Gets weather")
        .parameters(
            Schema.builder()
                .type(Type.Known.OBJECT)
                .properties(Map.of("location", Schema.builder().type(Type.Known.STRING).build()))
                .build())
        .build();

Tool weatherTool = Tool.builder().functionDeclarations(Arrays.asList(weatherFunc)).build();

try (ResponseStream<GenerateContentResponse> stream =
    client.models.generateContentStream(
        "gemini-2.5-flash-lite",
        "What's the weather in Boston?",
        GenerateContentConfig.builder().tools(Arrays.asList(weatherTool)).build())) {
  for (GenerateContentResponse chunk : stream) {
    if (chunk.functionCalls() != null && !chunk.functionCalls().isEmpty()) {
      FunctionCall fc = chunk.functionCalls().get(0);
      System.out.println("Call: " + fc.name().orElse("") + "(" + fc.args().orElse(Map.of()) + ")");
    } else if (chunk.text() != null) {
      System.out.print(chunk.text());
    }
  }
}
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

    weatherTool := &genai.Tool{
        FunctionDeclarations: []*genai.FunctionDeclaration{
            {
                Name:        "get_weather",
                Description: "Gets weather",
                Parameters: &genai.Schema{
                    Type: genai.TypeObject,
                    Properties: map[string]*genai.Schema{
                        "location": {Type: genai.TypeString},
                    },
                },
            },
        },
    }

    for chunk, err := range client.Models.GenerateContentStream(
        ctx,
        "gemini-2.5-flash-lite",
        genai.Text("What's the weather in Boston?"),
        &genai.GenerateContentConfig{
            Tools: []*genai.Tool{weatherTool},
        },
    ) {
        if err != nil {
            log.Fatal(err)
        }
        if calls := chunk.FunctionCalls(); len(calls) > 0 {
            fc := calls[0]
            fmt.Printf("Call: %s(%v)\n", fc.Name, fc.Args)
        } else if text := chunk.Text(); text != "" {
            fmt.Print(text)
        }
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:streamGenerateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{"parts": [{"text": "What is the weather in Boston?"}]}],
    "tools": [{"functionDeclarations": [{"name": "get_weather", "parameters": {"type": "OBJECT", "properties": {"location": {"type": "STRING"}}}}]}]
}'

# Response stream — function call arrives complete in one chunk
{"candidates": [{"content": {"parts": [{"functionCall": {"name": "get_weather", "args": {"location": "Boston, MA"}}}]}}]}
```

#### 之后（Interactions API）

Interactions API 会以字符为单位将函数调用实参作为 `arguments` 事件进行流式传输。整个工具生命周期（思考、调用、结果和输出）以一系列不同的步骤呈现。

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's the weather in Boston?",
    tools=[get_weather_tool],
    stream=True,
)

for event in stream:
    if event.event_type == "step.start" and event.step:
        if getattr(event.step, "type", None) == "function_call":
            print(f"Calling: {event.step.name}")
    elif event.event_type == "step.delta" and event.delta:
        if getattr(event.delta, "type", None) == "arguments":
            print(f"  args: {event.delta.partial_arguments}")
        elif getattr(event.delta, "type", None) == "text" and getattr(event.delta, "text", None):
            print(event.delta.text, end="")
    elif event.event_type == "interaction.completed":
        print("\n--- Done ---")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: "What's the weather in Boston?",
    tools: [getWeatherTool],
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.start' && event.step) {
        if (event.step.type === 'function_call') {
            console.log(`Calling: ${event.step.name}`);
        }
    } else if (event.event_type === 'step.delta' && event.delta) {
        if (event.delta.type === 'arguments' && event.delta.partial_arguments) {
            console.log(`  args: ${event.delta.partial_arguments}`);
        } else if (event.delta.type === 'text' && event.delta.text) {
            process.stdout.write(event.delta.text);
        }
    } else if (event.event_type === 'interaction.completed') {
        console.log('\n--- Done ---');
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ArgumentsDelta;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.InteractionCompletedEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.StepDeltaData;
import com.google.genai.gaos.models.interactions.StepStart;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.utils.EventStream;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();
properties.put("location", Map.of("type", "string"));

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("location"));

Function getWeatherTool =
    Function.builder()
        .name("get_weather")
        .description("Gets weather")
        .parameters(parameters)
        .build();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What's the weather in Boston?"))
        .tools(Arrays.asList(getWeatherTool))
        .stream(true)
        .build();

try (EventStream<InteractionSSEStreamEvent> stream =
    client.interactions.create(CreateInteractionRequestBody.of(request)).events()) {
  for (InteractionSSEStreamEvent streamEvent : stream) {
    if (streamEvent.data().isPresent()) {
      InteractionSSEEvent event = streamEvent.data().get();
      if (event instanceof StepStart) {
        StepStart stepStart = (StepStart) event;
        if (stepStart.step().isPresent() && stepStart.step().get() instanceof FunctionCallStep) {
          FunctionCallStep fcStep = (FunctionCallStep) stepStart.step().get();
          System.out.println("Calling: " + fcStep.name().orElse(""));
        }
      } else if (event instanceof StepDelta) {
        StepDelta stepDelta = (StepDelta) event;
        if (stepDelta.delta().isPresent()) {
          StepDeltaData delta = stepDelta.delta().get();
          if (delta instanceof ArgumentsDelta) {
            System.out.println("  args: " + ((ArgumentsDelta) delta).arguments().orElse(""));
          } else if (delta instanceof TextDelta) {
            System.out.print(((TextDelta) delta).text().orElse(""));
          }
        }
      } else if (event instanceof InteractionCompletedEvent) {
        System.out.println("\n--- Done ---");
      }
    }
  }
}
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    getWeatherTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_weather"),
        Description: genai.Ptr("Gets weather"),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "location": map[string]any{"type": "string"},
            },
            "required": []string{"location"},
        },
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:  interactions.Model("gemini-3.8-flash"),
            Input:  interactions.NewInteractionsInput("What's the weather in Boston?"),
            Tools:  []interactions.Tool{getWeatherTool},
            Stream: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepStart := event.GetDataStepStart(); stepStart != nil {
            if fcStep := stepStart.GetStepFunctionCall(); fcStep != nil {
                fmt.Println("Calling:", fcStep.Name)
            }
        } else if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if argsDelta := stepDelta.GetDeltaArgumentsDelta(); argsDelta != nil {
                fmt.Println("  args:", argsDelta.GetArguments())
            } else if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        } else if event.GetDataInteractionCompleted() != nil {
            fmt.Println("\n--- Done ---")
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.8-flash",
    "input": "What is the weather in Boston?",
    "tools": [{"type": "function", "name": "get_weather", "parameters": {"type": "object", "properties": {"location": {"type": "string"}}}}],
    "stream": true
}'

# Response stream
// Interaction created
event: interaction.created
data: {"type": "interaction.created", "interaction": {"id": "int_xyz", "status": "created"}}

event: interaction.in_progress
data: {"type": "interaction.in_progress", "interaction": {"id": "int_xyz", "status": "in_progress"}}

// ── Step 0: Thought ──────────────────────────────────
event: step.start
data: {"type": "step.start", "index": 0, "step": {"type": "thought"}}

event: step.delta
data: {"type": "step.delta", "index": 0, "delta": {"type": "thought", "text": "The user wants weather data for Boston. I'll call the get_weather tool."}}

event: step.stop
data: {"type": "step.stop", "index": 0, "status": "done"}

// ── Step 1: Function Call (arguments streamed) ───────
event: step.start
data: {"type": "step.start", "index": 1, "step": {"type": "function_call", "id": "fc_1", "name": "get_weather"}}

event: step.delta
data: {"type": "step.delta", "index": 1, "delta": {"type": "arguments", "partial_arguments": "{\"location\": \"Boston, MA\"}"}}

event: step.stop
data: {"type": "step.stop", "index": 1, "status": "waiting"}

// The interaction pauses — the model needs the tool result before continuing.
event: interaction.requires_action
data: {"type": "interaction.requires_action", "interaction": {"id": "int_xyz", "status": "requires_action"}}

// ── (Client submits the tool result) ──────────────────
// The client calls interactions.create with the function_result as input
// and the previous interaction's ID, then resumes consuming the stream.

event: interaction.in_progress
data: {"type": "interaction.in_progress", "interaction": {"id": "int_xyz", "status": "in_progress"}}

// ── Step 2: Function Result (echoed back, no deltas) ─
event: step.start
data: {"type": "step.start", "index": 2, "step": {"type": "function_result", "call_id": "fc_1", "name": "get_weather", "result": [{"type": "text", "text": "52°F, rain"}]}}

event: step.stop
data: {"type": "step.stop", "index": 2, "status": "done"}

// ── Step 3: Thought ──────────────────────────────────
event: step.start
data: {"type": "step.start", "index": 3, "step": {"type": "thought"}}

event: step.delta
data: {"type": "step.delta", "index": 3, "delta": {"type": "thought", "text": "Got weather data. Composing the final response."}}

event: step.stop
data: {"type": "step.stop", "index": 3, "status": "done"}

// ── Step 4: Model Output (text streamed) ─────────────
event: step.start
data: {"type": "step.start", "index": 4, "step": {"type": "model_output"}}

event: step.delta
data: {"type": "step.delta", "index": 4, "delta": {"type": "text", "text": "It's currently 52°F and rainy in Boston."}}

event: step.stop
data: {"type": "step.stop", "index": 4, "status": "done"}

// ── Interaction complete ─────────────────────────────
event: interaction.completed
data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 256, "completion_tokens": 128, "total_tokens": 384}}}
```

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-24。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-24。"],[],[]]
