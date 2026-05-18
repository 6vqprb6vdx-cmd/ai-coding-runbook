---
source_url: https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=ja
fetched_at: 2026-05-18T13:08:30.912687+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini API のクイックスタート

[このクイックスタートでは、ライブラリをインストールし、Interactions API を使用して最初の Gemini API リクエストを行う方法について説明します。](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)

## 始める前に

Gemini API を使用するには、リクエストの認証、セキュリティ制限の適用、アカウントの使用状況の追跡を行うための API キーが必要です。

AI Studio で無料で作成して、使用を開始します。

[Gemini API キーを作成する](https://aistudio.google.com/app/apikey?hl=ja)

## Google GenAI SDK をインストールする

### Python

[Python 3.9+](https://www.python.org/downloads/) 以降を使用して、次の
[pip コマンド](https://packaging.python.org/en/latest/tutorials/installing-packages/)で
[`google-genai` パッケージ](https://pypi.org/project/google-genai/)をインストールします。

```
pip install -q -U google-genai
```

### JavaScript

[Node.js v18+](https://nodejs.org/en/download/package-manager) 以降を使用して、次の [npm コマンド](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)で [TypeScript と JavaScript 用の Google Gen AI SDK](https://www.npmjs.com/package/@google/genai) をインストールします。

```
npm install @google/genai
```

## 最初のリクエストを送信する

を使用して Gemini API にリクエストを送信する方法は 2 つあります。

- ***（推奨）*** [Interactions API](https://ai.google.dev/api/interactions-api?hl=ja) は、型付き実行ステップによるマルチステップ ツール使用、オーケストレーション、複雑な推論フローをネイティブにサポートする新しいプリミティブです。今後、コア メインライン ファミリー以外の新しいモデル、新しいエージェント機能とツールは、Interactions API でのみリリースされます。
- [`generateContent`](https://ai.google.dev/api/generate-content?hl=ja#method:-models.generatecontent) を使用すると、モデルからシンプルなステートレス レスポンスを生成できます。Interactions API を使用することをおすすめしますが、`generateContent` は完全にサポートされています。

この例では、Interactions API を使用して、Gemini 3 Flash モデルを使用して Gemini API にリクエストを送信します。

API キーを[環境変数 `GEMINI_API_KEY`として](https://ai.google.dev/gemini-api/docs/interactions/api-key?hl=ja#set-api-env-var)設定すると、
Gemini API ライブラリを[使用するときにクライアントによって](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)自動的に取得されます。
[それ以外の場合は、クライアントを初期化するときに API キーを引数として渡す必要があります。](https://ai.google.dev/gemini-api/docs/interactions/api-key?hl=ja#provide-api-key-explicitly)

Gemini API ドキュメントのすべてのコードサンプルでは、環境変数 `GEMINI_API_KEY` が設定されていることを前提としています。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview", 
    input="Explain how AI works in a few words"
)

# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

// The client gets the API key from the environment variable `GEMINI_API_KEY`.
const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain how AI works in a few words",
  });

  const modelStep = interaction.steps.find(s => s.type === 'model_output');
  if (modelStep) {
    for (const contentBlock of modelStep.content) {
      if (contentBlock.type === 'text') console.log(contentBlock.text);
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain how AI works in a few words"
  }'
```

### ステートレス モード

デフォルトでは、`previous_interaction_id` を使用すると、Interactions API は会話の状態をサーバー側で管理します。会話履歴をクライアント側で自分で管理する場合は、`store=false` を設定し、後続のリクエストの `input` フィールドに累積されたステップを渡すことで、ステートレス モードを選択できます。

詳細と完全なマルチターン ステートレスの例については、[テキスト生成ガイド](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ja#stateless-conversations)をご覧ください。

## 次のステップ

最初の API リクエストを行ったので、Gemini の動作を示す次のガイドをご覧ください。

- [テキスト生成](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ja)
- [画像生成](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=ja)
- [画像理解](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=ja)
- [思考モード](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=ja)
- [関数呼び出し](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ja)
- [長いコンテキスト](https://ai.google.dev/gemini-api/docs/long-context?hl=ja)
- [エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja)

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-05-12 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-05-12 UTC。"],[],[]]
