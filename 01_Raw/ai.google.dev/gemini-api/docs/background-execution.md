---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=ja
fetched_at: 2026-08-10T03:26:13.087227+00:00
title: "\u30d0\u30c3\u30af\u30b0\u30e9\u30a6\u30f3\u30c9\u5b9f\u884c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# バックグラウンド実行

詳細な調査、複雑な推論、多段階のエージェント実行などの長時間実行タスクの場合、接続タイムアウトにより標準の HTTP リクエスト（通常は 60 秒後に終了）が中断されることがあります。[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) は、これらのタスクを非同期で実行するための**バックグラウンド実行**を提供します。

サーバーでタスクが完了するまでインタラクションを実行するには、インタラクションの作成時に `"background": true` を設定します。API はすぐにインタラクション ID を返します。クライアント アプリケーションはこの ID を使用して、ステータスのポーリング、進行状況のストリーミング、切断されたストリームへの再接続を行うことができます。

バックグラウンド実行は、標準の Gemini モデル（`gemini-3.6-flash` や `gemini-3.1-pro-preview` など）と Managed Agents（`antigravity-preview-05-2026` など）でサポートされています。

## バックグラウンド インタラクションを作成する

バックグラウンド インタラクションを開始するには、リソースの作成時に `background` パラメータを `true` に設定します。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a guide on space exploration.",
    background=True,
)
print(f"Created background interaction ID: {interaction.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Write a guide on space exploration.",
    background: true,
});
console.log(`Created background interaction ID: ${interaction.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Write a guide on space exploration.",
    "background": true
  }'
```

## バックグラウンド実行の仕組み

バックグラウンド操作を作成すると、タスクはサーバー上で非同期的に実行されます。インタラクションは、さまざまな実行状態に移行します。

- `in_progress`: サーバーがインタラクション（コードの実行や調査など）をアクティブに実行しています。
- `requires_action`: やり取りが一時停止し、クライアントの入力（ツールの実行の確認や質問への回答など）を待機しています。
- `completed`: インタラクションが正常に完了し、出力が利用可能です。
- `failed`: 実行中にエラーが発生しました（ツールの障害やレート制限など）。
- `cancelled`: クライアント リクエストにより実行が停止しました。

### ユースケース

バックグラウンド実行は、次の目的で使用します。

- **エージェントの実行:** コード実行、ウェブ ブラウジング、サブエージェントのオーケストレーション（`antigravity-preview-05-2026` など）を必要とするタスク。
- **Deep Research:** `deep-research-preview-04-2026` または `deep-research-max-preview-04-2026` を使用して実行され、数分かかります。
- **長い推論:** モデルの思考ステップが標準の HTTP 接続制限を超えるタスク。

## 結果を取得する

**ポーリング**または**ストリーミング**を使用して、バックグラウンドでのインタラクションの結果を取得します。

### ポーリング パターン（ブロックなし）

ポーリングでは、非ブロッキング GET リクエストを使用してインタラクションのステータスを定期的に確認し、完了状態に達するまで続けます。

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.get(id="YOUR_INTERACTION_ID")

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.get("YOUR_INTERACTION_ID");

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

if (interaction.status === "completed") {
    console.log(interaction.output_text);
} else {
    console.log(`Finished with status: ${interaction.status}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### ストリーミング パターン

ネットワークの中断によりストリームが切断された場合、最後に受信したイベントからストリーミングを再開できます。各デルタのペイロードには一意の `event_id` が含まれています。この ID を `last_event_id` として渡すと、そのイベントからストリームが再開されます。

### Python

```
import time
from google import genai

client = genai.Client()
interaction_id = "YOUR_INTERACTION_ID"

def stream_with_reconnect(interaction_id: str):
    last_event_id = None
    while True:
        try:
            # Retrieve the stream. If resuming, pass last_event_id
            stream = client.interactions.get(
                id=interaction_id,
                stream=True,
                last_event_id=last_event_id
            )

            for event in stream:
                # Log event updates and capture event_id if present
                if event.event_id:
                    last_event_id = event.event_id

                if event.event_type == "step.delta" and event.delta.type == "text":
                    print(event.delta.text, end="", flush=True)

                if event.event_type == "interaction.completed":
                    return

        except Exception as e:
            print(f"\n[Connection lost: {e}. Reconnecting in 3s...]")
            time.sleep(3)

stream_with_reconnect(interaction_id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const interactionId = "YOUR_INTERACTION_ID";

async function streamWithReconnect(id) {
    let lastEventId = undefined;
    while (true) {
        try {
            // Retrieve the stream. If resuming, pass last_event_id in options
            const stream = await client.interactions.get(id, {
                stream: true,
                last_event_id: lastEventId
            });

            for await (const event of stream) {
                // Capture event_id if present
                const idVal = event.event_id || event.id;
                if (idVal) {
                    lastEventId = idVal;
                }

                if (event.event_type === "step.delta" && event.delta?.type === "text") {
                    process.stdout.write(event.delta.text);
                }

                if (event.event_type === "interaction.completed") {
                    return;
                }
            }
        } catch (error) {
            console.log(`\n[Connection lost: ${error.message}. Reconnecting in 3s...]`);
            await new Promise(resolve => setTimeout(resolve, 3000));
        }
    }
}

await streamWithReconnect(interactionId);
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## マルチターンの会話

後続のインタラクションは、次の制約に従って `previous_interaction_id` を使用してバックグラウンド会話にチェーンできます。

1. **アクティブな実行がブロックされる:** `in_progress` ステータスのインタラクションに後続のインタラクションをチェーンすると、`400 Bad Request` エラーが返されます。インタラクションが `completed` 状態になるまで待ってから、次のインタラクションを開始します。
2. **マネージド エージェントの環境パラメータ:** マネージド エージェント（`antigravity-preview-05-2026` など）のインタラクションをチェーンする場合、リクエストには `previous_interaction_id` と `environment` の両方を含める必要があります。

次の例は、インタラクションをチェーンする方法を示しています。

### Python

```
import time
from google import genai

client = genai.Client()
agent_model = "antigravity-preview-05-2026"

# First interaction: Provision sandbox environment and execute first instruction
interaction1 = client.interactions.create(
    model=agent_model,
    input="Create a folder named project/ and write hello.py inside.",
    environment="remote",
    background=True
)

# Wait for completion
while True:
    check = client.interactions.get(id=interaction1.id)
    if check.status != "in_progress":
        break
    time.sleep(2)

# Second interaction: Chain using previous_interaction_id and environment
interaction2 = client.interactions.create(
    model=agent_model,
    input="List all files in the project/ directory.",
    previous_interaction_id=interaction1.id,
    environment="remote",
    background=True
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const agentModel = "antigravity-preview-05-2026";

// First interaction: Provision sandbox environment and execute first instruction
const interaction1 = await client.interactions.create({
    model: agentModel,
    input: "Create a folder named project/ and write hello.py inside.",
    environment: "remote",
    background: true
});

// Wait for completion
while (true) {
    const check = await client.interactions.get(interaction1.id);
    if (check.status !== "in_progress") {
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// Second interaction: Chain using previous_interaction_id and environment
const interaction2 = await client.interactions.create({
    model: agentModel,
    input: "List all files in the project/ directory.",
    previous_interaction_id: interaction1.id,
    environment: "remote",
    background: true
});
```

### REST

```
# Chain second interaction (Make sure FIRST_INTERACTION_ID has status 'completed')
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "antigravity-preview-05-2026",
    "input": "List all files in the project/ directory.",
    "previous_interaction_id": "FIRST_INTERACTION_ID",
    "environment": "remote",
    "background": true
  }'
```

## キャンセルと削除

実行中の実行を制御し、キャンセル リクエストと削除リクエストを使用してストレージを管理します。

- **キャンセル（`POST /interactions/{id}/cancel`）:** 実行中のタスクを停止します。ステータスが `cancelled` に移行します。サーバーでのクリーンアップ アクションにより、GET リクエストでのステータスの更新がわずかに遅れることがあります。
- **削除（`DELETE /interactions/{id}`）:** サーバーからインタラクション レコードを削除します。以降の GET リクエストは `404 Not Found` エラーを返します。

### Python

```
from google import genai

client = genai.Client()

# Cancel a running interaction
client.interactions.cancel(id="YOUR_INTERACTION_ID")

# Delete the interaction record entirely
client.interactions.delete(id="YOUR_INTERACTION_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Cancel a running interaction
await client.interactions.cancel("YOUR_INTERACTION_ID");

// Delete the interaction record entirely
await client.interactions.delete("YOUR_INTERACTION_ID");
```

### REST

```
# Cancel the interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID/cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"

# Delete the interaction
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## 次のステップ

- セッションと状態の管理については、[Interactions API の概要](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja)をご覧ください。
- リアルタイム イベントの更新について詳しくは、[ストリーミングのインタラクション](https://ai.google.dev/gemini-api/docs/streaming?hl=ja) ガイドをご覧ください。
- [マネージド エージェントのクイックスタート](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ja)を参照して、ステートフル マルチターン エージェントを構築します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-30 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-30 UTC。"],[],[]]
