---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=ja
fetched_at: 2026-08-17T02:30:35.569433+00:00
title: "API \u30d0\u30fc\u30b8\u30e7\u30f3\u306e\u8aac\u660e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [API リファレンス](https://ai.google.dev/api?hl=ja)

フィードバックを送信

# API バージョンの説明

このドキュメントでは、Gemini API の `v1`
と `v1beta` バージョンの違いの概要について説明します。

- **v1**: API の安定版。安定版の機能は、メジャー バージョンのライフサイクル全体にわたって完全にサポートされます。互換性を破る変更がある場合は、API の新しいメジャー バージョンが作成され、既存のバージョンは妥当な期間が経過した後に非推奨になります。
  互換性を破らない変更は、メジャー バージョンを変更せずに API に導入できます。**Interactions API** とそのコア機能は、`v1` で一般提供されています。
- **v1beta**: このバージョンには、
  積極的に開発されている初期の機能が含まれています。`v1beta` の機能は、フィードバックに基づいて改良されるため変更される可能性がありますが、安定版に昇格する前に新機能を試すことができます。

## 機能と機能のサポート

次の表に、`v1`（GA）
と `v1beta`（ベータ版）で利用できる機能の詳細を示します。特に指定がない限り、コア API の機能とツールは Interactions API と `generateContent` の両方に適用されます。

| 機能 | v1 | v1beta |
| --- | --- | --- |
| **コア API の機能** |  |  |
| [Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=ja) |  |  |
| [関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja) |  |  |
| [構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja) |  |  |
| [思考 / 推論](https://ai.google.dev/gemini-api/docs/thinking?hl=ja) |  |  |
| [システム指示](https://ai.google.dev/gemini-api/docs/system-instructions?hl=ja) |  |  |
| [音声出力（音声構成）](https://ai.google.dev/gemini-api/docs/audio?hl=ja) |  |  |
| [サービス階層（優先度 / フレックス）](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja) |  |  |
| **ツール** |  |  |
| [コード実行ツール](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja) |  |  |
| [Google 検索グラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja) |  |  |
| [Google マップのグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja) |  |  |
| [URL コンテキスト ツール](https://ai.google.dev/gemini-api/docs/url-context?hl=ja) |  |  |
| [ファイル検索ツール](https://ai.google.dev/gemini-api/docs/file-search?hl=ja) |  |  |
| [コンピュータ使用ツール](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja) |  |  |
| [MCP サーバーツール](https://ai.google.dev/gemini-api/docs/eap/remote_mcp?hl=ja) |  |  |
| **リアルタイム API** |  |  |
| [Live API（WebSocket）](https://ai.google.dev/gemini-api/docs/live-api?hl=ja) |  |  |
| [Live Music API](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ja) |  |  |
| [エフェメラル トークン（Live API）](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=ja) |  |  |
| **プラットフォーム API** |  |  |
| [Models API](https://ai.google.dev/gemini-api/docs/models?hl=ja) |  |  |
| [Files Service Route](https://ai.google.dev/gemini-api/docs/files?hl=ja) |  |  |
| [File Search Stores Route](https://ai.google.dev/gemini-api/docs/file-search?hl=ja) |  |  |
| [Agents API](https://ai.google.dev/gemini-api/docs/agents?hl=ja) |  |  |
| [Webhooks API](https://ai.google.dev/gemini-api/docs/webhooks?hl=ja) |  |  |
| [コンテキスト キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja) |  |  |

- - サポート対象

## SDK で API バージョンを構成する

Gemini API SDK のデフォルトは `v1beta` ですが、次のコードサンプルに示すように API バージョンを設定することで、バージョンを明示的に指定できます。

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.6-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
  }'
```

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-28 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-28 UTC。"],[],[]]
