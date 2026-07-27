---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=ja
fetched_at: 2026-07-27T04:43:24.348515+00:00
title: "API \u30d0\u30fc\u30b8\u30e7\u30f3\u306e\u8aac\u660e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [API リファレンス](https://ai.google.dev/api?hl=ja)

フィードバックを送信

# API バージョンの説明

このドキュメントでは、Gemini API の `v1`
と `v1beta` バージョンの違いの概要について説明します。

- **v1**: API の安定版。安定版の機能は、メジャー バージョンのライフサイクル全体にわたって完全にサポートされます。互換性を破る変更がある場合は、API の次のメジャー バージョンが作成され、既存のバージョンは妥当な期間が経過した後に非推奨になります。
  互換性を破らない変更は、メジャー バージョンを変更せずに API に導入できます。2026 年 6 月の時点で、**Interactions API** は一般提供されており、`v1` でサポートされています。
- **v1beta**: このバージョンには、現在
  開発中の初期の機能が含まれています。`v1beta` の機能は、フィードバックに基づいて改良されるため変更される可能性がありますが、安定版に昇格する前に新機能を試すことができます。

| 機能 | v1 | v1beta |
| --- | --- | --- |
| Interactions API |  |  |
| コンテンツの生成 - テキストのみの入力 |  |  |
| コンテンツの生成 - テキストと画像の入力 |  |  |
| コンテンツの生成 - テキスト出力 |  |  |
| コンテンツの生成 - マルチターンの会話（チャット） |  |  |
| コンテンツの生成 - 関数呼び出し |  |  |
| コンテンツの生成 - ストリーミング |  |  |
| コンテンツの埋め込み - テキストのみの入力 |  |  |
| 回答を生成する |  |  |
| セマンティック リトリーバー |  |  |

- - サポート対象
- - サポート対象外

## SDK で API バージョンを構成する

Gemini API SDK のデフォルトは `v1beta` ですが、次のコードサンプルに示すように API バージョンを設定して、バージョンを明示的に指定できます。

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.5-flash',
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
    model: "gemini-3.5-flash",
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
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works"
  }'
```

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-22 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-22 UTC。"],[],[]]
