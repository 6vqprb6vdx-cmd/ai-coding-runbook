---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-CN
fetched_at: 2026-10-19T05:33:52.165166+00:00
title: "Interactions API\uff1a\u91cd\u5927\u66f4\u6539\u8fc1\u79fb\u6307\u5357\uff082026 \u5e74 5 \u6708\uff09 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Interactions API：重大更改迁移指南（2026 年 5 月）

`v1beta` Interactions API 引入了破坏性更改，这些更改会重构 API 形状，以支持飞行中转向和异步工具调用等未来功能。本页介绍了哪些内容发生了变化，并提供了更改前后的代码示例，以帮助您进行迁移。更改分为两类：

1. [**steps 架构**](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn#steps-schema)：
   新的 `steps` 数组取代了 `outputs` 数组，提供了每个交互轮次的结构化
   时间线。
2. [**输出格式配置**](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn#output-format-config)：
   新的多态 `response_format` 整合了所有输出格式控制项
   并移除了 `response_mime_type`。

请按照
[如何迁移到新架构](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn#how-to-migrate)
中的步骤更新集成。

## 核心更改：`outputs` 变为 `steps`

新架构将 `outputs` 数组替换为 `steps` 数组。

- **旧版**：响应返回一个扁平的 `outputs` 数组，其中仅包含模型生成的内容。
- **新架构**：响应返回一个 `steps` 数组，其中包含带有类型鉴别器的结构化步骤。

`POST /interactions` 仅返回输出步骤。`GET /interactions/{id}`
返回完整的步骤时间线，包括初始 `user_input` 步骤。

### 基本输入/输出（一元）

#### 之前（旧版）

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.8-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a joke."
  }'
```

```
// Response
{
  "id": "int_123",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "Why did the chicken cross the road?"
    }
  ]
}
```

#### 之后（新架构）

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.8-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Tell me a joke.'
});

// Response access (Recommended sugar)
console.log(interaction.output_text);
```

[sdk-convenience]: /gemini-api/docs/interactions-overview#sdk-sugar

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a joke."
  }'
```

```
// POST Response
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}

// GET /v1beta/interactions/int_123 (returns full timeline including input)
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "content": [
        { "type": "text", "text": "Tell me a joke." }
      ]
    },
    {
      "type": "model_output",
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

### 函数调用

请求结构保持不变，但响应会将扁平的 `outputs` 内容替换为结构化步骤。

#### 之前（旧版）

### Python

```
# Accessing function call in legacy schema
for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Calling {output.name} with {output.arguments}")
```

### JavaScript

```
// Accessing function call in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Calling ${output.name} with ${JSON.stringify(output.arguments)}`);
    }
}
```

### REST

```
// Response
{
  "id": "int_001",
  "role": "model",
  "status": "requires_action",
  "outputs": [
    {
      "type": "thought",
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

#### 之后（新架构）

### Python

```
# Accessing function call in new steps schema
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Calling {step.name} with {step.arguments}")
```

### JavaScript

```
// Accessing function call in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Calling ${step.name} with ${JSON.stringify(step.arguments)}`);
    }
}
```

### REST

```
// POST Response
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "thought",
      "summary": [{
        "type": "text",
        "text": "I need to check the weather in Boston..."
      }],
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

### 服务器端工具

服务器端工具（例如 Google 搜索或代码执行）现在会在 `steps` 数组中生成特定步骤类型。虽然旧版架构将这些操作作为 `outputs` 数组中的特定内容类型返回，但新架构会将它们移到 `steps` 数组中。以下示例使用 Google 搜索。

#### 之前（旧版）

### Python

```
# Accessing search results in legacy schema
for output in interaction.outputs:
    if output.type == "google_search_call":
        print(f"Searched for: {output.arguments.queries}")
    elif output.type == "google_search_result":
        print(f"Found results: {output.result.rendered_content}")
```

### JavaScript

```
// Accessing search results in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'google_search_call') {
        console.log(`Searched for: ${output.arguments.queries}`);
    } else if (output.type === 'google_search_result') {
        console.log(`Found results: ${output.result.renderedContent}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// Response
{
  "id": "int_456",
  "outputs": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] }
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "rendered_content": "<div>...</div>",
        "url": "https://www.nfl.com/super-bowl"
      }
    },
    {
      "type": "text",
      "text": "The Kansas City Chiefs won the last Super Bowl.",
      "annotations": [
        {
          "start_index": 4,
          "end_index": 22,
          "source": "https://www.nfl.com/super-bowl"
        }
      ]
    }
  ],
  "status": "completed"
}
```

#### 之后（新架构）

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result[0].search_suggestions}")
```

### JavaScript

```
// Accessing search results in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'google_search_call') {
        console.log(`Searched for: ${step.arguments.queries}`);
    } else if (step.type === 'google_search_result') {
        console.log(`Found results: ${step.result[0].search_suggestions}`);
    }
}
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// POST Response
{
  "id": "int_456",
  "steps": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] },
      "signature": "abc123..."
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "search_suggestions": "<div>...</div>"
      },
      "signature": "abc123..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The Kansas City Chiefs won the last Super Bowl.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.nfl.com/super-bowl",
              "title": "NFL.com",
              "start_index": 4,
              "end_index": 22
            }
          ]
        }
      ]
    }
  ],
  "status": "completed"
}
```

### 流式

流式公开了新的事件类型：

#### 新事件类型

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### 已废弃的事件类型

以下旧版事件类型已替换为上面列出的新事件：

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → 替换为 `interaction.in_progress`、`interaction.requires_action` 等。

**流式函数调用**：当您将流式与函数调用搭配使用时，
`step.start` 事件会传递函数名称，而 `step.delta` 事件
会以部分 JSON 字符串的形式流式传输实参（使用 `arguments_delta`）。您
必须累积这些增量才能获得完整的实参。这与一元调用不同，在一元调用中，您会一次性收到完整的函数调用对象。

#### 示例

##### 之前（旧版）

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain quantum entanglement in simple terms.",
    stream=True,
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
```

### JavaScript

```
// Legacy streaming used content.delta
const stream = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Explain quantum entanglement in simple terms.',
    stream: true,
});

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text') {
            process.stdout.write(chunk.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain quantum entanglement in simple terms.",
    "stream": true
  }'
```

```
// Response (SSE Lines)
// event: interaction.start
// data: {"id": "int_123", "status": "in_progress"}
//
// event: content.start
// data: {"index": 0, "type": "text"}
//
// event: content.delta
// data: {"delta": {"type": "text", "text": "Quantum entanglement is..."}}
//
// event: content.stop
// data: {"index": 0}
//
// event: interaction.complete
// data: {"id": "int_123", "status": "done", "usage": {"total_tokens": 42}}
```

##### 之后（新架构）

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a story.",
    stream=True,
):
    if event.event_type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Tell me a story.',
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.delta') {  // CHANGED: step.delta instead of content.delta
        if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
 # Opt-in needed before May 26th
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "Accept: text/event-stream" \
   -H "Api-Revision: 2026-05-20" \
   -d '{
     "model": "gemini-3.8-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.8-flash"}, "event_type": "interaction.created"}
 //
 // event: interaction.in_progress
 // data: {"interaction_id": "int_xyz", "event_type": "interaction.in_progress"}
 //
 // event: step.start
 // data: {"index": 0, "step": {"type": "thought", "signature": "abc123..."}, "event_type": "step.start"}
 //
 // event: step.stop
 // data: {"index": 0, "event_type": "step.stop"}
 //
 // event: step.start
 // data: {"index": 1, "step": {"content": [{"text": "Once upon", "type": "text"}], "type": "model_output"}, "event_type": "step.start"}
 //
 // event: step.delta
 // data: {"index": 1, "delta": {"text": " a time...", "type": "text"}, "event_type": "step.delta"}
 //
 // event: step.stop
 // data: {"type": "step.stop", "index": 1, "status": "done"}
 //
 // event: interaction.completed
 // data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}} // NEW: Dedicated completion event
```

### 无状态对话记录

如果您在客户端手动管理对话记录（无状态用例），则必须更新串联先前轮次的方式。

- **旧版**：开发者通常会从响应中收集 `outputs` 数组，并在下一轮次中将其发送回 `input` 字段。
- **新架构**：您现在应从响应中收集 `steps` 数组，并将其传递到下一个请求的 `input` 字段中，将新的用户轮次附加为 `user_input` 步骤。

## 输出格式配置：`response_format` 更改

更新后的 API 将所有输出格式控制项整合到一个统一的多态 `response_format` 字段中。这会将输出配置集中在顶层，并使 `generation_config` 专注于模型行为（例如温度、top\_p 和思考）。

### 主要变化

- **API 移除 `response_mime_type`。**您现在可以在 `response_format` 中为每个格式条目指定 MIME 类型。
- **`response_format` 现在是一个多态对象（或数组）。**每个条目都有一个 `type` 鉴别器（`text`、`audio`、`image`）和特定于类型的字段。如需请求多种输出模态，请传递格式条目数组。
- **`image_config` 从 `generation_config` 移至 `response_format`。**
  您现在可以在 `response_format` 条目中指定图片输出设置，例如 `aspect_ratio` 和 `image_size`
  ，并使用 `"type": "image"`。

### 结构化输出 (JSON)

新架构移除了 `response_mime_type` 字段。请改为在
对象中使用`response_format`
`"type": "text"`指定 MIME 类型和 JSON 架构。

#### 之前（旧版）

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Summarize this article.",
    response_mime_type="application/json",
    response_format={
        "type": "object",
        "properties": {
            "summary": {"type": "string"}
        }
    },
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Summarize this article.',
    response_mime_type: 'application/json',
    response_format: {
        type: 'object',
        properties: {
            summary: { type: 'string' }
        }
    },
});

console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Summarize this article.",
    "response_mime_type": "application/json",
    "response_format": {
      "type": "object",
      "properties": {
        "summary": { "type": "string" }
      }
    }
  }'
```

#### 之后（新架构）

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Summarize this article.",
    # response_mime_type is removed — specify mime_type inside response_format
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string"}
            }
        }
    },
)

# Print response
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Summarize this article.',
    // response_mime_type is removed — specify mime_type inside response_format
    response_format: {
        type: 'text',
        mime_type: 'application/json',
        schema: {
            type: 'object',
            properties: {
                summary: { type: 'string' }
            }
        }
    },
});

// Print response
console.log(interaction.output_text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Summarize this article.",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "summary": { "type": "string" }
        }
      }
    }
  }'
```

### 图片配置

新架构从 `generation_config` 中移除了 `image_config`。您现在可以在 `response_format` 条目中使用 `"type": "image"` 指定
图片输出设置。

#### 之前（旧版）

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Generate an image of a sunset over the ocean.",
    generation_config={
        "image_config": {
            "aspect_ratio": "1:1",
            "image_size": "1K"
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Generate an image of a sunset over the ocean.',
    generation_config: {
        image_config: {
            aspect_ratio: '1:1',
            image_size: '1K'
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### 之后（新架构）

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Generate an image of a sunset over the ocean.",
    # image_config is removed from generation_config — use response_format
    response_format={
        "type": "image",
        "mime_type": "image/jpeg",
        "aspect_ratio": "1:1",
        "image_size": "1K"
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Generate an image of a sunset over the ocean.',
    // image_config is removed from generation_config — use response_format
    response_format: {
        type: 'image',
        mime_type: 'image/jpeg',
        aspect_ratio: '1:1',
        image_size: '1K'
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

### 音频配置

新架构将 `response_modalities: ["audio"]` 替换为 `response_format` 条目 `"type": "audio"`。

#### 之前（旧版）

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    response_modalities: ['audio'],
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_modalities": ["audio"],
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

#### 之后（新架构）

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    # response_modalities is removed — use response_format
    response_format={
        "type": "audio"
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    // response_modalities is removed — use response_format
    response_format: {
        type: 'audio'
    },
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

如需请求多种输出模态（例如同时请求文本和音频），请将格式条目数组传递给 `response_format`，而不是传递单个对象。

## 如何迁移到新架构

### SDK 用户

请升级到最新 SDK 版本（Python ≥2.0.0、JavaScript ≥2.0.0）。SDK 会自动让您选择启用新架构，除了更新读取响应的方式（请参阅上面的示例）之外，无需更改任何代码。请注意，这些 SDK 版本仅支持新架构。旧版 SDK（Python 1.x.x、JavaScript 1.x.x）将继续正常运行，直到旧版架构于 **2026 年 6 月 8 日** 移除。

### REST API 用户

请将 `Api-Revision: 2026-05-20` 标头添加到您的请求中，以便立即选择启用新架构。在 **5 月 26 日** 之后，新架构将成为所有
请求的默认架构。您可以使用 `Api-Revision: 2026-05-07`
暂时选择停用，直到 **6 月 8 日**，届时 API 将永久移除旧版架构。

### 时间轴

| 日期 | 阶段 | SDK 用户 | REST API 用户 |
| --- | --- | --- | --- |
| **5 月 7 日** | 选择启用 | 新 SDK 版本可用（Python ≥2.0.0、JS ≥2.0.0）。升级即可自动获取新架构。 | 添加 `Api-Revision: 2026-05-20` 标头以选择启用。默认值仍为旧版。 |
| **5 月 26 日** | 默认翻转 | 如果已升级，则无需执行任何操作。旧版 SDK（Python 1.x.x、JS 1.x.x）仍可正常运行，但会返回旧版响应。 | 新架构现在是默认架构。发送 `Api-Revision: 2026-05-07` 标头以选择停用。 |
| **6 月 8 日** | 落日余晖 | Python 1.x.x 和 JS 1.x.x SDK 版本在调用 Interactions API 时将会失效。 | 为 Interactions API 移除了旧版架构。`Api-Revision` 标头被忽略。 |

## 迁移核对清单

### steps 架构 (`steps`)

- 更新代码，以便从 `steps` 数组而不是 `outputs` 中读取响应内容。
  [请参阅示例](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn#basic-unary)。
- 验证您的代码是否同时处理 `user_input` 和 `model_output` 步骤类型。
  [请参阅示例](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn#basic-unary)。
- （函数调用）更新代码，以便在 `steps` 数组中查找 `function_call` 步骤。
  [请参阅示例](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn#function-calling)。
- （服务器端工具）更新代码以处理特定于工具的步骤（例如 `google_search_call`、`google_search_result`）。
  [请参阅示例](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn#server-side-tools)。
- （无状态记录）更新记录管理，以便在下一个请求的 `input` 字段中传递 `steps` 数组。
  [请参阅详情](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn#stateless-history)。
- （仅限流式）更新客户端以监听新的 SSE 事件类型（`interaction.created`、`step.delta` 等）。
  [请参阅示例](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn#streaming)。

### 输出格式配置 (`response_format`)

- 将 `response_mime_type` 替换为 `response_format` 中的 `mime_type` 字段。
  [请参阅示例](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn#structured-output)。
- 将现有的 `response_format` JSON 架构封装在 `{"type": "text", "schema": ...}` 对象中。
  [请参阅示例](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn#structured-output)。
- （图片生成）将 `image_config` 从 `generation_config` 移至 `response_format` 中的 `{"type": "image", ...}` 条目。
  [请参阅示例](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn#image-config)。
- （语音生成）将 `response_modalities=["audio"]` 替换为 `response_format` 中的 `{"type": "audio"}` 条目。
  [请参阅示例](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-cn#audio-config)。
- （多模态）在请求多种输出模态时，将 `response_format` 从单个对象转换为数组。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-15。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-15。"],[],[]]
