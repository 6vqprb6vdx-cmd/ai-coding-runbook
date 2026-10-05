---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ja
fetched_at: 2026-10-05T06:31:45.683306+00:00
title: "Gemini \u306e\u601d\u8003 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash が利用可能になりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ja)。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs/generate-content?hl=ja)

フィードバックを送信

# Gemini の思考

[Gemini 3 および 2.5 シリーズのモデル](https://ai.google.dev/gemini-api/docs/models?hl=ja)は、推論と多段階計画の能力を大幅に向上させる内部の「思考プロセス」を使用します。これにより、コーディング、高度な数学、データ分析などの複雑なタスクに非常に効果的です。

このガイドでは、Gemini API を使用して Gemini の思考機能を操作する方法について説明します。

## 思考を伴うコンテンツの生成

思考モデルでリクエストを開始する手順は、他のコンテンツ生成リクエストと同様です。主な違いは、次の[テキスト生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja#text-input)の例に示すように、`model` フィールドで[思考サポート付きモデル](#supported-models)のいずれかを指定することです。

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
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

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.8-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## 思考の要約

思考の要約は、モデルの生の思考を要約したもので、モデルの内部推論プロセスに関する分析情報を提供します。思考レベルと予算は、モデルの生の思考に適用され、思考の要約には適用されません。

リクエスト構成で `includeThoughts` を `true` に設定すると、思考の要約を有効にできます。概要にアクセスするには、`response` パラメータの `parts` を反復処理し、`thought` ブール値を確認します。

次の例は、ストリーミングなしで思考の要約を有効にして取得する方法を示しています。これにより、レスポンスとともに単一の最終的な思考の要約が返されます。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.8-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

ストリーミングによる思考を使用して、生成中にローリング増分要約を返す例を次に示します。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.8-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.8-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
  }
}

await main();
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

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.8-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## 思考の制御

Gemini モデルはデフォルトで動的思考を行い、ユーザーのリクエストの複雑さに基づいて推論の労力を自動的に調整します。ただし、特定のレイテンシの制約がある場合や、モデルが通常よりも深い推論を行う必要がある場合は、必要に応じてパラメータを使用して思考動作を制御できます。

### 思考レベル（Gemini 3）

Gemini 3 以降のモデルにおすすめの `thinkingLevel` パラメータを使用すると、推論の動作を制御できます。

次の表に、各モデルタイプの `thinkingLevel` 設定の詳細を示します。

| 思考レベル | Gemini 3.8 & 3.7 Flash | Gemini 3.6 & 3.5 Flash | Gemini 3.1 Pro | Gemini 3.5 & 3.1 Flash-Lite | Gemini 3.1 Flash-Lite Image | Gemini 3 Flash | Gemini Robotics ER 2 | 説明 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | サポート対象外（エラー） | サポート対象 | サポート対象外 | Supported（デフォルト） | Supported（デフォルト） | サポート対象 | サポート対象 | ほとんどのクエリで「思考なし」の設定と一致します。なお、`minimal` を設定しても思考がオフになるわけではありません。複雑なタスクでは、モデルが最小限の推論を行うことがあります。 |
| **`low`** | サポート対象 | サポート対象 | サポート対象 | サポート対象 | サポート対象外 | サポート対象 | サポート対象 | レイテンシと費用を最小限に抑えます。 |
| **`medium`** | Supported（デフォルト） | Supported（デフォルト） | サポート対象 | サポート対象 | サポート対象外 | サポート対象 | サポート対象 | ほとんどのタスクでバランスの取れた思考。 |
| **`high`** | サポート対象（動的） | サポート対象（動的） | サポート対象（デフォルト、動的） | サポート対象（動的） | サポート対象（動的） | サポート対象（デフォルト、動的） | サポート対象（デフォルト、動的） | 推論の深さを最大化します。最初の（思考以外の）出力トークンに到達するまでに時間がかかることがありますが、出力はより慎重に推論されます。 |

次の例は、思考レベルを設定する方法を示しています。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Gemini 3.1 Pro では思考を無効にできません。Gemini 3 Flash と Flash-Lite も、思考の完全なオフをサポートしていません。思考レベルを指定しない場合、Gemini は Gemini 3 モデルのデフォルトの思考レベル（Gemini 3.1 Pro の場合は `"high"`、Gemini 3.5 Flash の場合は `"medium"` など）を使用します。

Gemini 2.5 シリーズ モデルは `thinkingLevel` をサポートしていません。代わりに `thinkingBudget` を使用してください。

### トークンの上限と `max_output_tokens`

[`max_output_tokens`](https://ai.google.dev/api/generate-content?hl=ja#v1beta.GenerationConfig) 生成パラメータは、レスポンスが生成できるトークンの最大数（思考トークンを含む）を設定します。

このパラメータを設定すると、モデルが思考予算（`thinking_level`）を割り当てる方法を変更することなく、インフラストラクチャによって強制されるハードカットオフとして機能します。

推論中にモデルがこの上限に達すると、`finish_reason: MAX_TOKENS` で生成を停止し、切り捨てられた出力または空の出力を返します（生成された思考トークンは引き続き課金されます）。レスポンスを切り捨てずに費用やレイテンシを削減するには、小さい `max_output_tokens` を設定するのではなく、`thinking_level`（`low` または `medium`）を小さくします。

### 思考予算

Gemini 2.5 シリーズで導入された `thinkingBudget` パラメータは、推論に使用する思考トークンの特定の数に関するガイダンスをモデルに提供します。

以下に、各モデルタイプの `thinkingBudget` 構成の詳細を示します。思考を無効にするには、`thinkingBudget` を 0 に設定します。`thinkingBudget` を -1 に設定すると、**動的思考**が有効になります。つまり、モデルはリクエストの複雑さに基づいて予算を調整します。

| モデル | デフォルト設定 （思考予算が設定されていない） | 範囲 | 思考を無効にする | 動的思考をオンにする |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | 動的な思考 | `128` から `32768` | N/A: 思考を無効にできない | `thinkingBudget = -1`（デフォルト） |
| **2.5 Flash** | 動的な思考 | `0` から `24576` | `thinkingBudget = 0` | `thinkingBudget = -1`（デフォルト） |
| **2.5 Flash プレビュー** | 動的な思考 | `0` から `24576` | `thinkingBudget = 0` | `thinkingBudget = -1`（デフォルト） |
| **2.5 Flash-Lite** | モデルは思考しない | `512` から `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite プレビュー** | モデルは思考しない | `512` から `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 プレビュー版** | 動的な思考 | `0` から `24576` | `thinkingBudget = 0` | `thinkingBudget = -1`（デフォルト） |
| **2.5 Flash Live ネイティブ音声プレビュー（2025 年 9 月）** | 動的な思考 | `0` から `24576` | `thinkingBudget = 0` | `thinkingBudget = -1`（デフォルト） |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

プロンプトによっては、モデルがトークン予算を超過または不足する可能性があります。

## 思考シグネチャ

Gemini API はステートレスであるため、モデルはすべての API リクエストを個別に処理し、マルチターンのやり取りで以前のターンの思考コンテキストにアクセスできません。

マルチターンのインタラクションで思考コンテキストを維持できるようにするために、Gemini は思考シグネチャを返します。これは、モデルの内部思考プロセスを暗号化したものです。

- **Gemini 2.5 モデル**は、思考が有効になっていて、リクエストに[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#thinking)（具体的には[関数宣言](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#step-2)）が含まれている場合に、思考シグネチャを返します。
- **Gemini 3 モデル**は、すべてのタイプの[パーツ](https://ai.google.dev/api/caching?hl=ja#Part)の思考シグネチャを返すことがあります。すべてのシグネチャをそのまま返すことをおすすめしますが、関数呼び出しシグネチャでは*必須*です。詳しくは、[思考シグネチャ](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ja)のページをご覧ください。

関数呼び出しで考慮すべきその他の使用上の制限は次のとおりです。

- シグネチャは、レスポンスの他の部分（関数呼び出しやテキストなど）からモデルによって返されます。[すべての部分を含むレスポンス全体を返す](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#step-4)
  後続のターンで、すべての部分を含むレスポンス全体をモデルに返します。
- シグネチャを含むパートを連結しないでください。
- シグネチャ付きのパートとシグネチャなしのパートを結合しないでください。

## 料金

思考がオンになっている場合、レスポンスの料金は出力トークンと思考トークンの合計になります。生成された思考トークンの合計数は、`thoughtsTokenCount` フィールドから取得できます。

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

思考モデルは、最終的なレスポンスの品質を高めるために完全な思考を生成し、思考プロセスに関する分析情報を提供するために[要約](#summaries)を出力します。そのため、API から出力されるのは要約のみですが、料金はモデルが要約を作成するために生成する必要があるすべての思考トークンに基づいて計算されます。

トークンの詳細については、[トークン数のカウント](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)のガイドをご覧ください。

## ベスト プラクティス

このセクションでは、思考モデルを効率的に使用するためのガイダンスを紹介します。これまでと同様に、[プロンプトのガイダンスとベスト プラクティス](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ja)に沿って操作することで、最良の結果を得ることができます。

### デバッグとステアリング

- **推論を確認する**: 思考モデルから期待どおりの回答が得られない場合は、Gemini の思考の要約を慎重に分析すると役立ちます。タスクをどのように分解して結論に達したかを確認し、その情報を使用して正しい結果が得られるように修正できます。
- **推論でガイダンスを提供する**: 特に長い出力を希望する場合は、プロンプトでガイダンスを指定して、モデルが使用する[思考の量](#set-budget)を制限することをおすすめします。これにより、レスポンス用にトークン出力をより多く予約できます。

### タスクの複雑さ

- **簡単なタスク（思考をオフにできる）:** 事実の取得や分類など、複雑な推論を必要としない簡単なリクエストの場合、思考は必要ありません。次のようなアプリケーションがあります。
  - 「DeepMind はどこで設立されましたか？」
  - 「このメールは会議の依頼ですか、それとも単に情報を提供しているだけですか？」
- **中程度のタスク（デフォルト/ある程度の思考が必要）:** 多くの一般的なリクエストは、段階的な処理やより深い理解によってメリットが得られます。Gemini は、次のようなタスクに思考機能を柔軟に使用できます。
  - 光合成と成長を例える。
  - 電気自動車とハイブリッド車を比較対照します。
- **難しいタスク（思考能力を最大限に活用）:** 複雑な数学の問題やコーディング タスクなど、非常に複雑な課題には、思考予算を高く設定することをおすすめします。このようなタスクでは、モデルが推論と計画の機能を最大限に活用する必要があります。多くの場合、回答を提供する前に多くの内部ステップが必要になります。次のようなアプリケーションがあります。
  - AIME 2025 の問題 1 を解きます。17b が 97b の約数となるすべての整数基数 b > 9 の合計を求めます。
  - ユーザー認証を含む、リアルタイムの株式市場データを可視化するウェブ アプリケーションの Python コードを記述します。できるだけ効率的にします。

## サポートされているモデル、ツール、機能

思考機能は、3 シリーズと 2.5 シリーズのすべてのモデルでサポートされています。すべてのモデル機能については、[モデルの概要](https://ai.google.dev/gemini-api/docs/models?hl=ja)ページをご覧ください。

思考モデルは、Gemini のすべてのツールと機能で動作します。これにより、モデルは外部システムとやり取りしたり、コードを実行したり、リアルタイム情報にアクセスしたりして、その結果を推論と最終的な回答に組み込むことができます。

[思考クックブック][Colab] で、思考モデルでツールを使用する例を試すことができます。

## 次のステップ

- 思考の範囲については、[OpenAI 互換性](https://ai.google.dev/gemini-api/docs/openai?hl=ja#thinking)ガイドをご覧ください。

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-25 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-25 UTC。"],[],[]]
