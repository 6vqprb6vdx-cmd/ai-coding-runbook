---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja
fetched_at: 2026-11-02T07:29:53.019899+00:00
title: "\u7d44\u307f\u8fbc\u307f\u30c4\u30fc\u30eb\u3068\u95a2\u6570\u547c\u3073\u51fa\u3057\u3092\u7d44\u307f\u5408\u308f\u305b\u308b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 組み込みツールと関数呼び出しを組み合わせる

Gemini では、ツールの呼び出しのコンテキスト履歴を保持して公開することで、[組み込みツール](https://ai.google.dev/gemini-api/docs/tools?hl=ja)（`google_search`など）と[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)（*カスタムツール*とも呼ばれます）を 1 つのインタラクションで組み合わせることができます。組み込みツールとカスタムツールの組み合わせにより、複雑な Agentic Workflows が可能になります。たとえば、モデルは特定のビジネス ロジックを呼び出す前に、リアルタイムのウェブデータに基づいて判断できます。

組み込みツールとカスタムツールの組み合わせを有効にする例を次に示します。`google_search` とカスタム関数 `getWeather` を使用します。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

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

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");

Function customFunc =
    Function.builder()
        .name("get_user_location")
        .description("Retrieves user current location.")
        .parameters(parameters)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the weather like where I am right now?"))
        .tools(Arrays.asList(customFunc, new GoogleSearch()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

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

    customFunc := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_user_location"),
        Description: genai.Ptr("Retrieves user current location."),
        Parameters: map[string]any{
            "type": "object",
        },
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("What is the weather like where I am right now?"),
            Tools: []interactions.Tool{
                customFunc,
                interactions.NewTool(interactions.GoogleSearch{}),
            },
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
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.8-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## 仕組み

Gemini 3 モデルは、ツール コンテキストの循環 を使用して、組み込みツールとカスタムツールの組み合わせを可能にします。ツール
コンテキストの循環により、組み込みツールのコンテキストを保持して公開し、同じインタラクション内のカスタムツールと共有できます。

### ツールの組み合わせを有効にする

- 組み合わせ動作をトリガーするには、使用する組み込みツールとともに [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#function-declarations) を含めます。

### API がステップを返す

インタラクション レスポンスでは、API は組み込みツールの呼び出しと関数（カスタムツール）の呼び出しに対して個別のステップを返します。

- **組み込みツールのステップ**: API がこれらを自動的に管理し、
  ターン間でコンテキストを保持します。
- **関数呼び出しのステップ**: API は、カスタム関数に対して `function_call` ステップを返します。関数を実行して、結果を返します。

### 返されたステップの重要なフィールド

返されたステップの特定のフィールドは、ツールのコンテキストを維持し、ツールの組み合わせを有効にするために重要です。

- **`id`**: `function_call` ステップと `function_response` ステップにあります。呼び出しをレスポンスにマッピングする固有識別子。
- **`signature`**: `thought` ステップと、Gemini 3 以降のモデルのすべてのツール呼び出し（`function_call` など）と結果（`function_response` など）のステップにあります。この暗号化されたコンテキストにより、インタラクション間で**ツール コンテキストの循環** が可能になります。

**これらのフィールドの管理:**

- **ステートフル モード（推奨）**: `previous_interaction_id` を使用すると、サーバーは `id` フィールドと `signature` フィールドの両方を自動的に処理します。
- **ステートレス モード**: 会話履歴を手動で管理する場合は、信頼性を検証してコンテキストを維持するために、後続のリクエストで `id` フィールドと `signature` フィールドの両方をモデルに渡す必要があります。完全なレスポンス オブジェクトを履歴に渡すと、公式 SDK がこれを自動的に処理します。

### ツール固有のデータ

一部の組み込みツールは、ツールタイプに固有のユーザーに表示されるデータ引数を返します。

| ツール | ユーザーに表示されるツール呼び出し引数（存在する場合） | ユーザーに表示されるツール レスポンス（存在する場合） |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` ブラウジングする URL | `status`: ブラウジング ステータス `retrieved_url`: ブラウジングした URL |
| **file\_search** | なし | なし |

## トークンと料金

リクエストの組み込みツールの呼び出し部分は `prompt_token_count` にカウントされます。これらのツールの中間ステップが表示され、返されるようになったため、会話履歴の一部となります。**これは
リクエスト*の場合のみで、レスポンス*の場合は該当しません。

Google 検索ツールはこのルールの例外です。Google 検索では、クエリレベルですでに独自の料金モデルが適用されているため、トークンが二重に課金されることはありません（[料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)ページをご覧ください）。

詳細については、[トークン](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)ページをご覧ください。

## 制限事項

- ツール コンテキストの循環が有効になっている場合は、デフォルトで `validated` モードになります（`auto` モードはサポートされていません）。
- `google_search` などの組み込みツールは、現在地と現在時刻の情報に依存しています。そのため、`system_instruction` または `function_declaration.description` に競合する現在地と時刻の情報が含まれている場合、ツールの組み合わせ機能が正常に動作しない可能性があります。

## サポートされているツール

標準のツール コンテキストの循環は、サーバーサイド（組み込み）ツールに適用されます。
コード実行もサーバーサイド ツールですが、コンテキストの循環には独自の組み込みソリューションがあります。コンピュータの使用と関数呼び出しはクライアントサイド ツールであり、コンテキストの循環にも組み込みソリューションがあります。

| ツール | 実行側 | コンテキストの循環のサポート |
| --- | --- | --- |
| [Google 検索](https://ai.google.dev/gemini-api/docs/google-search?hl=ja) | サーバーサイド | サポート対象 |
| [Google マップ](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja) | サーバーサイド | サポート対象 |
| [URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja) | サーバーサイド | サポート対象 |
| [ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja) | サーバーサイド | サポート対象 |
| [コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja) | サーバーサイド | サポート対象（組み込み、`code_execution` ステップと `code_execution_result` ステップを使用） |
| [コンピュータ使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja) | クライアントサイド | サポート対象（組み込み、`function_call` ステップと `function_response` ステップを使用） |
| [カスタム関数](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja) | クライアントサイド | サポート対象（組み込み、`function_call` ステップと `function_response` ステップを使用） |

## 次のステップ

- Gemini API の [関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja) の詳細を確認する。
- サポートされているツールを確認する。
  - [Google 検索](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)
  - [Google マップ](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)
  - [URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)
  - [ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-13 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-13 UTC。"],[],[]]
