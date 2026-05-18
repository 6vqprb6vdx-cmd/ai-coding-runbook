---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=ja
fetched_at: 2026-05-18T13:02:33.723224+00:00
title: "Interactions API: \u7834\u58ca\u7684\u5909\u66f4\u306e\u79fb\u884c\u30ac\u30a4\u30c9\uff082026 \u5e74 5 \u6708\uff09 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Interactions API: 破壊的変更の移行ガイド（2026 年 5 月）

`v1beta` Interactions API には、API の形状を再構築して、飛行中のステアリングや非同期ツール呼び出しなどの今後の機能をサポートするための破壊的変更が導入されています。このページでは、変更点について説明し、移行に役立つように変更前後のコード例を示します。変更には次の 2 つのカテゴリがあります。

1. [**ステップ スキーマ**](#steps-schema): 新しい `steps` 配列が `outputs` 配列に代わり、各インタラクション ターンの構造化されたタイムラインを提供します。
2. [**出力形式の構成**](#output-format-config): 新しいポリモーフィック `response_format` により、すべての出力形式の制御が統合され、`response_mime_type` が削除されます。

[新しいスキーマに移行する方法](#how-to-migrate)の手順に沿って、統合を更新します。

## コアの変更: `outputs` から `steps`

新しいスキーマでは、`outputs` 配列が `steps` 配列に置き換えられます。

- **以前**: レスポンスは、モデルの生成コンテンツのみを含むフラットな `outputs` 配列を返していました。
- **新しいスキーマ**: レスポンスは、型判別子を含む構造化されたステップを含む `steps` 配列を返します。

`POST /interactions` は出力ステップのみを返します。`GET /interactions/{id}` は、最初の `user_input` ステップを含む完全なステップ タイムラインを返します。

### 基本的な入出力（単項）

#### 以前（従来版）

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3-flash-preview", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
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
    "model": "gemini-3-flash-preview",
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

#### 変更後（新しいスキーマ）

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3-flash-preview", input="Tell me a joke."
)

# Response access
print(interaction.steps[-1].content[0].text)  # CHANGED: steps instead of outputs
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
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

### 関数呼び出し

リクエストの構造は変更されませんが、レスポンスではフラットな `outputs` コンテンツが構造化されたステップに置き換えられます。

#### 以前（従来版）

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
        console.log(`Calling {output.name} with {JSON.stringify(output.arguments)}`);
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

#### 変更後（新しいスキーマ）

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
        console.log(`Calling {step.name} with {JSON.stringify(step.arguments)}`);
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

### サーバーサイド ツール

サーバーサイド ツール（Google 検索やコード実行など）は、`steps` 配列で特定のステップタイプを生成するようになりました。以前のスキーマでは、これらのオペレーションは `outputs` 配列内の特定のコンテンツ タイプとして返されていましたが、新しいスキーマでは `steps` 配列に移動されています。次の例では、Google 検索を使用します。

#### 以前（従来版）

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
        console.log(`Searched for: {output.arguments.queries}`);
    } else if (output.type === 'google_search_result') {
        console.log(`Found results: {output.result.renderedContent}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
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

#### 変更後（新しいスキーマ）

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result.search_suggestions}")
```

### JavaScript

```
// Accessing search results in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'google_search_call') {
        console.log(`Searched for: {step.arguments.queries}`);
    } else if (step.type === 'google_search_result') {
        console.log(`Found results: {step.result.searchSuggestions}`);
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
    "model": "gemini-3-flash-preview",
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

### ストリーミング

ストリーミングでは、新しいイベントタイプが公開されます。

#### 新しいイベントタイプ

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### 非推奨のイベントタイプ

次の以前のイベントタイプは、上記の新しいイベントに置き換えられます。

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → `interaction.in_progress`、`interaction.requires_action` などに置き換えられました。

**ストリーミング関数呼び出し**: 関数呼び出しでストリーミングを使用する場合、`step.start` イベントは関数名を配信し、`step.delta` イベントは引数を部分的な JSON 文字列としてストリーミングします（`arguments_delta` を使用）。これらのデルタを累積して、完全な引数を取得する必要があります。これは、完全な関数呼び出しオブジェクトを一度に受け取る単項呼び出しとは異なります。

#### 例

##### 変更前（従来版）

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3-flash-preview",
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
    model: 'gemini-3-flash-preview',
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
    "model": "gemini-3-flash-preview",
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

##### 変更後（新しいスキーマ）

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me a story.",
    stream=True,
):
    if event.type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a story.',
    stream: true,
});

for await (const event of stream) {
    if (event.type === 'step.delta') {  // CHANGED: step.delta instead of content.delta
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
     "model": "gemini-3-flash-preview",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3-flash-preview"}, "event_type": "interaction.created"}
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

### ステートレスの会話履歴

クライアント側で会話履歴を手動で管理している場合（ステートレスのユースケース）、以前のターンを連結する方法を更新する必要があります。

- **以前の動作**: デベロッパーは、レスポンスから `outputs` 配列を収集し、次のターンで `input` フィールドで返送していました。
- **新しいスキーマ**: レスポンスから `steps` 配列を収集し、次のリクエストの `input` フィールドに渡して、新しいユーザー ターンを `user_input` ステップとして追加する必要があります。

## 出力形式の構成: `response_format` の変更

更新された API では、すべての出力形式制御が統合されたポリモーフィック `response_format` フィールドに統合されています。これにより、出力構成が最上位レベルで一元化され、`generation_config` はモデルの動作（Temperature、Top-P、思考モードなど）に集中できます。

### 主な変更点

- **API は `response_mime_type` を削除します。**`response_format` 内の形式エントリごとに MIME タイプを指定するようになりました。
- **`response_format` はポリモーフィック オブジェクト（または配列）になりました。**各エントリには、`type` 判別子（`text`、`audio`、`image`）と型固有のフィールドがあります。複数の出力モードをリクエストするには、形式エントリの配列を渡します。
- **`image_config` が `generation_config` から `response_format` に移動します。**`aspect_ratio` や `image_size` などの画像出力設定は、`"type": "image"` を含む `response_format` エントリで指定するようになりました。

### 構造化出力（JSON）

新しいスキーマでは `response_mime_type` フィールドが削除されています。代わりに、`"type": "text"` を使用して `response_format` オブジェクト内に MIME タイプと JSON スキーマを指定します。

#### 以前（従来版）

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
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
    model: 'gemini-3-flash-preview',
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
    "model": "gemini-3-flash-preview",
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

#### 変更後（新しいスキーマ）

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
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

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
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

console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
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

### イメージの構成

新しいスキーマでは、`generation_config` から `image_config` が削除されています。`"type": "image"` を使用して `response_format` エントリで画像出力設定を指定するようになりました。

#### 以前（従来版）

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
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
    model: 'gemini-3-flash-preview',
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
    "model": "gemini-3-flash-preview",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### 変更後（新しいスキーマ）

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
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
    model: 'gemini-3-flash-preview',
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
    "model": "gemini-3-flash-preview",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

複数の出力モダリティ（テキストと音声など）を同時にリクエストするには、単一のオブジェクトではなく、形式エントリの配列を `response_format` に渡します。

## 新しいスキーマに移行する方法

### SDK ユーザー

最新の SDK バージョン（Python ≥2.0.0、JavaScript ≥2.0.0）にアップグレードします。SDK は新しいスキーマを自動的に有効にします。レスポンスの読み取り方法を更新する以外にコードを変更する必要はありません（上記の例を参照）。これらの SDK バージョンでは、新しいスキーマのみがサポートされます。古い SDK バージョン（Python 1.x.x、JavaScript 1.x.x）は、2026 年 6 月 8 日にレガシー スキーマが削除されるまで引き続き動作します。

### REST API ユーザー

リクエストに `Api-Revision: 2026-05-20` ヘッダーを追加して、新しいスキーマを今すぐ有効にしてください。**5 月 26 日**以降、新しいスキーマがすべてのリクエストのデフォルトになります。**6 月 8 日**までは `Api-Revision: 2026-05-07` で一時的にオプトアウトできます。この日以降は、API によって以前のスキーマが完全に削除されます。

### タイムライン

| 日付 | フェーズ | SDK ユーザー | REST API ユーザー |
| --- | --- | --- | --- |
| **5 月 7 日** | オプトイン | 新しい SDK バージョンが利用可能（Python ≥2.0.0、JS ≥2.0.0）。アップグレードすると、新しいスキーマが自動的に取得されます。 | `Api-Revision: 2026-05-20` ヘッダーを追加してオプトインします。デフォルトはレガシーのままです。 |
| **5 月 26 日** | デフォルトの反転 | すでにアップグレード済みの場合は、対応は不要です。古い SDK（Python 1.x.x、JS 1.x.x）は引き続き機能しますが、以前のレスポンスを返します。 | 新しいスキーマがデフォルトになりました。オプトアウトするには、`Api-Revision: 2026-05-07` ヘッダーを送信します。 |
| **6 月 8 日** | 夕暮れ | Python 1.x.x と JS 1.x.x の SDK バージョンでは、Interactions API 呼び出しが失敗します。 | Interactions API の従来のスキーマが削除されました。`Api-Revision` ヘッダーは無視されます。 |

## 移行チェックリスト

### 歩数スキーマ（`steps`）

- `outputs` ではなく `steps` 配列からレスポンス コンテンツを読み取るようにコードを更新します。[例を見る](#basic-unary)。
- コードで `user_input` と `model_output` の両方のステップタイプが処理されることを確認します。[例を見る](#basic-unary)。
- （関数呼び出し）`steps` 配列で `function_call` ステップを見つけるようにコードを更新します。[例を見る](#function-calling)。
- （サーバーサイド ツール）ツール固有の手順（`google_search_call`、`google_search_result` など）を処理するようにコードを更新します。[例をご覧ください](#server-side-tools)。
- （ステートレス履歴）履歴管理を更新して、次のリクエストの `input` フィールドに `steps` 配列を渡します。[詳細](#stateless-history)
- （ストリーミングのみ）新しい SSE イベントタイプ（`interaction.created`、`step.delta` など）をリッスンするようにクライアントを更新します。[例を見る](#streaming)。

### 出力形式の構成（`response_format`）

- `response_mime_type` を `response_format` 内の `mime_type` フィールドに置き換えます。[例を見る](#structured-output)。
- 既存の `response_format` JSON スキーマを `{"type": "text", "schema": ...}` オブジェクトでラップします。[例を見る](#structured-output)。
- （画像生成）`image_config` を `generation_config` から `response_format` の `{"type": "image", ...}` エントリに移動します。[例を見る](#image-config)。
- （マルチモーダル）複数の出力モードをリクエストするときに、`response_format` を単一のオブジェクトから配列に変換します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-05-12 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-05-12 UTC。"],[],[]]
