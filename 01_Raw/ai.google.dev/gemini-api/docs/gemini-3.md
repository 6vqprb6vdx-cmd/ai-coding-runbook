---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=ja
fetched_at: 2026-06-29T05:30:17.565497+00:00
title: "Gemini 3 \u30c7\u30d9\u30ed\u30c3\u30d1\u30fc \u30ac\u30a4\u30c9 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)

フィードバックを送信

# Gemini 3 デベロッパー ガイド

Gemini 3 は、最先端の推論を基盤として構築された、Google 史上最もインテリジェントなモデル ファミリーです。エージェント ワークフロー、自律型コーディング、複雑なマルチモーダル タスクをマスターして、あらゆるアイデアを実現できるように設計されています。
このガイドでは、Gemini 3 モデル ファミリーの主な機能と、その機能を最大限に活用する方法について説明します。

Gemini 3 アプリの[コレクション](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=ja)で、モデルが高度な推論、自律型コーディング、複雑な
マルチモーダル タスクをどのように処理するかを
ご確認ください。

数行のコードで始めましょう。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Gemini 3 シリーズの紹介

Gemini 3.1 Pro は、幅広い世界知識とモダリティ間の高度な推論を必要とする複雑なタスクに最適です。

Gemini 3 Flash は、Google の最新の 3 シリーズ モデルで、Pro レベルのインテリジェンスを Flash の速度と料金で実現します。

Nano Banana Pro（Gemini 3 Pro Image とも呼ばれます）は、Google の最高品質の画像生成モデルです。Nano Banana 2（Gemini 3.1 Flash Image とも呼ばれます）は、大量の画像を低価格で効率的に生成できる同等のモデルです。

Gemini 3.1 Flash-Lite は、費用対効果の高いモデルと大量のタスク向けに構築されたワークホース モデルです。

現在、すべての Gemini 3 モデルはプレビュー版です。

| モデル ID | コンテキスト ウィンドウ（入力 / 出力） | ナレッジ カットオフ | 料金（入力 / 出力）\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 100 万 / 64,000 | 2025 年 1 月 | $0.25（テキスト、画像、動画）、$0.50（音声） / $1.50 |
| **gemini-3.1-flash-image-preview** | 128,000 / 32,000 | 2025 年 1 月 | $0.25（テキスト入力） / $0.067（画像出力）\*\* |
| **gemini-3.1-pro-preview** | 100 万 / 64,000 | 2025 年 1 月 | $2 / $12（<200,000 トークン）  $4 / $18（>200,000 トークン） |
| **gemini-3-flash-preview** | 100 万 / 64,000 | 2025 年 1 月 | $0.50 / $3 |
| **gemini-3-pro-image-preview** | 65,000 / 32,000 | 2025 年 1 月 | $2（テキスト入力） / $0.134（画像出力）\*\* |

\* 料金は、特に記載のない限り、100 万トークンあたりです。 *\*\* 画像の料金は解像度によって異なります。詳細については、[料金ページ](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)をご覧ください。*

上限、料金、その他の詳細については、
[モデルのページ](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja)をご覧ください。

## Gemini 3 の API の新機能

Gemini 3 では、デベロッパーがレイテンシ、費用、マルチモーダルの忠実度をより細かく制御できるように設計された新しいパラメータが導入されています。

### 思考レベル

Gemini 3 シリーズのモデルは、デフォルトで動的思考を使用してプロンプトを推論します。`thinking_level` パラメータを使用すると、レスポンスを生成する前のモデルの内部推論プロセスの**最大** 深度を制御できます。Gemini 3 では、これらのレベルは厳密なトークン保証ではなく、思考の相対的な許容範囲として扱われます。

`thinking_level` が指定されていない場合、Gemini 3 はデフォルトで `high` になります。複雑な推論が必要ない場合に、より高速で低レイテンシのレスポンスを得るには、モデルの思考レベルを `low` に制約します。

| 思考レベル | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | 説明 |
| --- | --- | --- | --- | --- |
| **`minimal`** | サポート対象外 | サポート対象（デフォルト） | サポート対象 | ほとんどのクエリで「思考なし」の設定と一致します。複雑なコーディング タスクの場合、モデルは非常に最小限の思考を行うことがあります。チャットや高スループット アプリケーションのレイテンシを最小限に抑えます。なお、`minimal` は思考がオフであることを保証するものではありません。 |
| **`low`** | サポート対象 | サポート対象 | サポート対象 | レイテンシと費用を最小限に抑えます。簡単な指示の実行、チャット、高スループット アプリケーションに最適です。 |
| **`medium`** | サポート対象 | サポート対象 | サポート対象 | ほとんどのタスクでバランスの取れた思考。 |
| **`high`** | サポート対象（デフォルト、動的） | サポート対象（動的） | サポート対象（デフォルト、動的） | 推論の深さを最大化します。最初の（思考以外の）出力トークンに到達するまでに時間がかかることがありますが、出力はより慎重に推論されます。 |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### 温度

すべての Gemini 3 モデルで、温度パラメータをデフォルト値の `1.0` に維持することを強くおすすめします。

以前のモデルでは、多くの場合、Temperature をチューニングして創造性と決定論を制御することでメリットが得られました。しかし、Gemini 3 の推論機能はデフォルト設定用に最適化されています。温度を変更する（1.0 未満に設定する）と、特に複雑な数学的タスクや推論タスクで、ループやパフォーマンスの低下などの予期しない動作が発生する可能性があります。

### 思考シグネチャ

Gemini 3 モデルは、思考シグネチャを使用して、API 呼び出し間で推論コンテキストを維持します。これらのシグネチャは、モデルの内部的な思考プロセスを暗号化したものです。

- **ステートフル モード（推奨）**: ステートフル モード（`previous_interaction_id` を指定）で Interactions API を使用する場合、サーバーは会話履歴と思考シグネチャを自動的に管理します。
- **ステートレス モード**: 会話履歴を手動で管理する場合は、信頼性を検証するために、後続のリクエストにシグネチャ付きの思考ブロックを含める必要があります。

詳細については、[思考シグネチャ](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)のページをご覧ください。

### ツールを使用した構造化出力

Gemini 3 モデルでは、[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)を、組み込みツール（
[Google 検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)、[URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)、[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)、[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)など）と組み合わせることができます。

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### 画像生成

Gemini 3.1 Flash Image と Gemini 3 Pro Image を使用すると、テキスト プロンプトから画像を生成して編集できます。推論を使用してプロンプトを「思考」し、天気予報や株価チャートなどのリアルタイム データを取得してから、[Google 検索](https://ai.google.dev/gemini-api/docs/google-search?hl=ja) グラウンディングを使用して高忠実度の画像を生成できます。

**新機能と改善された機能:**

- **4K とテキスト レンダリング:** 最大 2K と 4K の解像度で、鮮明で読みやすいテキストと図を生成します。
- **グラウンディングされた生成:** `google_search` ツールを使用して事実を確認し、実際の情報に基づいて画像生成を行います。Gemini 3.1 Flash Image で Google 画像検索によるグラウンディングを利用できます。
- **話して編集:** 変更をリクエストするだけで、マルチターン画像編集が可能です（例: 「背景を夕焼けにする」）。このワークフローでは、**思考シグネチャ** を使用してターン間で視覚的なコンテキストを保持します。

アスペクト比、編集ワークフロー、構成
オプションの詳細については、[画像生成ガイド](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)をご覧ください。

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**レスポンスの例**

![東京の天気](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=ja)

### 画像を使用したコード実行

Gemini 3 Flash は、ビジョンを静的な一瞥ではなく、アクティブな調査として扱うことができます。推論と[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)を組み合わせることで、モデルは計画を立て、Python コードを記述して
実行し、画像をステップごとに拡大、切り抜き、注釈付け、その他の操作を行い、回答を視覚的にグラウンディングします。

**使用例:**

- **ズームと検査:** モデルは、詳細が小さすぎる場合（遠くのゲージやシリアル番号の読み取りなど）を暗黙的に検出し、コードを記述して切り抜き、高解像度で領域を再確認します。
- **視覚的な数学とプロット:** モデルは、コードを使用して複数ステップの計算を実行できます（領収書の明細の合計、抽出したデータからの Matplotlib グラフの生成など）。
- **画像の注釈:** モデルは、矢印、境界ボックス、その他の注釈を画像に直接描画して、「このアイテムはどこに配置すればよいですか？」などの空間に関する質問に回答できます。

視覚的な思考を有効にするには、[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)をツールとして構成します。必要に応じて、モデルはコードを使用して画像を自動的に操作します。

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

画像を使用したコード実行の詳細については、[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja#images)をご覧ください。

### マルチモーダル関数レスポンス

[マルチモーダル関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#multimodal)
を使用すると、
マルチモーダル オブジェクトを含む関数レスポンスを取得できるため、
モデルの関数呼び出し機能をより有効に活用できます。標準の関数呼び出しでは、テキストベースの関数レスポンスのみがサポートされます。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### 組み込みツールと関数呼び出しを組み合わせる

[Gemini 3 では、組み込みツール（Google 検索、URL
コンテキストなど）とカスタム[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)ツールを同じ API 呼び出しで使用できるため、
より複雑なワークフローが可能になります。](https://ai.google.dev/gemini-api/docs/tools?hl=ja)

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

## Gemini 2.5 からの移行

Gemini 3 は、Google 史上最も高性能なモデル ファミリーであり、Gemini 2.5 から段階的に改善されています。移行する際は、次の点に注意してください。

- **思考:** 以前に複雑なプロンプト エンジニアリング（
  思考の連鎖など）を使用して Gemini 2.5 に推論を強制していた場合は、Gemini 3 と
  `thinking_level: "high"` および簡略化されたプロンプトを試してください。
- **Temperature 設定:** 既存のコードで Temperature が明示的に設定されている場合（特に決定的出力が低い値に設定されている場合）、このパラメータを削除して Gemini 3 のデフォルトの 1.0 を使用することをおすすめします。これにより、複雑なタスクで発生する可能性のあるループの問題やパフォーマンスの低下を回避できます。
- **PDF とドキュメントの理解:** 高密度ドキュメントの解析で特定の動作に依存していた場合は、新しい `media_resolution_high` 設定をテストして、精度が維持されることを確認してください。
- **トークンの使用量:** Gemini 3 のデフォルトに移行すると、PDF のトークン使用量が**増加** する可能性がありますが、動画のトークン使用量は**減少** する可能性があります。デフォルトの解像度が高くなったことでリクエストがコンテキスト ウィンドウを超えるようになった場合は、メディアの解像度を明示的に下げることをおすすめします。
- **画像セグメンテーション:** 画像セグメンテーション機能（オブジェクトのピクセルレベルのマスクを返す）は、Gemini 3 Pro または Gemini 3 Flash では対象外です。組み込みの画像セグメンテーションを必要とする
  ワークロードでは、思考を無効にした Gemini 2.5 Flash または [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ja) を引き続き
  使用することをおすすめします。
- **コンピュータの使用:** Gemini 3 Pro と Gemini 3 Flash は[コンピュータ
  の使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)をサポートしています。2.5 シリーズとは異なり、コンピュータの使用ツールにアクセスするために別のモデルを使用する必要はありません。
- **ツールのサポート**: [組み込みツールと関数呼び出しの組み合わせ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)が、Gemini 3 モデルでサポートされるようになりました。Gemini 3
  モデルで Google [マップ
  のグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)もサポートされるようになりました。

## OpenAI の互換性

[OpenAI 互換性レイヤ](https://ai.google.dev/gemini-api/docs/openai?hl=ja)を使用している場合、
標準パラメータ（OpenAI の `reasoning_effort`）は
Gemini（`thinking_level`）の同等のパラメータに自動的にマッピングされます。

## プロンプトのベスト プラクティス

Gemini 3 は推論モデルであるため、プロンプトの作成方法が変わります。

- **正確な指示:** 入力プロンプトは簡潔にしてください。Gemini 3 は、明確で直接的な指示に最適に応答します。古いモデルで使用されている冗長または複雑すぎるプロンプト エンジニアリング手法では、過剰な分析になる可能性があります。
- **出力の冗長性:** デフォルトでは、Gemini 3 は冗長性が低く、直接的で効率的な回答を好みます。ユースケースで会話調のペルソナが必要な場合は、プロンプトでモデルを明示的に誘導する必要があります（例: 「親しみやすく、おしゃべりなアシスタントとして説明してください」）。
- **コンテキスト管理:** 大規模なデータセット（書籍全体、
  コードベース、長い動画など）を扱う場合は、データ コンテキストの後に、プロンプトの末尾に具体的な指示や質問を記述します。質問を「上記の情報を基に...」などのフレーズで始めることで、モデルの推論を提供されたデータに固定します。

プロンプト設計戦略の詳細については、[プロンプト エンジニアリング ガイド](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ja)をご覧ください。

## よくある質問

1. **Gemini 3 のナレッジ カットオフはいつですか？**Gemini 3 モデルのナレッジ カットオフは 2025 年 1 月です。最新の情報については、
   [検索グラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja) ツールを使用してください。
2. **コンテキスト ウィンドウの上限はどのくらいですか？**Gemini 3 モデルは、100 万トークンの入力コンテキスト ウィンドウと最大 64,000 トークンの出力をサポートしています。
3. **Gemini 3 の無料枠はありますか？**Gemini 3 Flash `gemini-3-flash-preview` には、Gemini API の無料枠があります。Google AI Studio で Gemini 3.1 Pro と 3 Flash を無料で試すことができますが、Gemini API の `gemini-3.1-pro-preview` には無料枠はありません。
4. **古い `thinking_budget` コードは引き続き機能しますか？**はい。下位互換性のために `thinking_budget` は引き続きサポートされていますが、より予測可能なパフォーマンスを得るために `thinking_level` に移行することをおすすめします。同じリクエストで両方を使用しないでください。
5. **Gemini 3 は Batch API をサポートしていますか？**はい。Gemini 3 は
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)をサポートしています。
6. **コンテキスト キャッシュ保存はサポートされていますか？**はい。[コンテキスト キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)は Gemini 3 でサポートされています。
7. **Gemini 3 でサポートされているツールはどれですか？**Gemini 3 は、
   [Google 検索](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)、
   [Google マップによるグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)、
   [ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)、
   [コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)、および
   [URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)をサポートしています。また、独自のカスタムツールや組み込みツールとの[組み合わせ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)で、標準の[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)もサポートしています。
8. **`gemini-3.1-pro-preview-customtools` とは何ですか？**
   `gemini-3.1-pro-preview` を使用しているときに、モデルがカスタムツールを無視して
   bash コマンドを優先する場合は、代わりに `gemini-3.1-pro-preview-customtools` モデルを試してください。
   詳細については、[こちら][customtools-model]をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-22 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-22 UTC。"],[],[]]
