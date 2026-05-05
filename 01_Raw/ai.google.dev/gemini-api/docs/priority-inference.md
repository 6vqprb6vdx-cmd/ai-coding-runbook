---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja
fetched_at: 2026-05-05T13:12:05.882537+00:00
title: "\u512a\u5148\u5ea6\u63a8\u8ad6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 優先度推論

Gemini Priority API は、低レイテンシと最高の信頼性を必要とするビジネス クリティカルなワークロード向けに設計されたプレミアム推論ティアです。優先度ティアのトラフィックは、標準 API と Flex ティアのトラフィックよりも優先されます。

優先度推論は、GenerateContent API と Interactions API のエンドポイントで、[Tier 2 と Tier 3](https://ai.google.dev/gemini-api/docs/billing?hl=ja#about-billing) のユーザーが利用できます。

## 優先度の使用方法

優先度階層を使用するには、リクエスト本文の `service_tier` フィールドを `priority` に設定します。フィールドが省略されている場合、デフォルトの階層は標準です。

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3-flash-preview",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
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
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## 優先度推論の仕組み

優先度推論では、リクエストを高クリティカルなコンピューティング キューにルーティングし、ユーザー向けアプリケーションに予測可能で高速なパフォーマンスを提供します。主なメカニズムは、動的上限を超えるトラフィックに対して、サーバーサイドで標準処理にグレースフルにダウングレードすることです。これにより、リクエストが失敗するのではなく、アプリケーションの安定性が確保されます。

| 機能 | 優先度 | 標準 | Flex | バッチ |
| --- | --- | --- | --- | --- |
| **料金** | Standard の 75 ～ 100% 増 | 通常料金 | 50% 割引 | 50% 割引 |
| **レイテンシ** | 秒 | 数秒～数分 | 分（1 ～ 15 分の目標） | 最大 24 時間 |
| **信頼性** | 高（抜け毛なし） | 高 / 中～高 | ベスト エフォート（破棄可能） | 高（スループットの場合） |
| **インターフェース** | 同期 | 同期 | 同期 | 非同期 |

### 主なメリット

- **低レイテンシ**: インタラクティブなユーザー向け AI ツールで、応答時間が 1 秒になるように設計されています。
- **高い信頼性**: トラフィックは最も高い重要度で処理され、厳密にシェーディングされません。
- **グレースフル デグラデーション**: 動的上限を超えるトラフィックの急増は、失敗するのではなく、処理のために自動的に Standard 階層にダウングレードされ、サービス停止を防ぎます。
- **摩擦が少ない**: 標準階層と Flex 階層と同じ同期 `generateContent` メソッドを使用します。

### ユースケース

優先処理は、パフォーマンスと信頼性が最も重要なビジネス クリティカルなワークフローに最適です。

- **インタラクティブ AI アプリケーション**: ユーザーがプレミアム料金を支払い、迅速で一貫性のある応答を期待するカスタマー サービス chatbot と copilot。
- **リアルタイムの意思決定エンジン**: ライブチケットのトリアージや不正行為の検出など、信頼性が高く、レイテンシの低い結果を必要とするシステム。
- **プレミアム カスタマー機能**: 有料ユーザーに対してより高いサービスレベル目標（SLO）を保証する必要があるデベロッパー。

### レート上限

優先度の高い消費は、[インタラクティブ トラフィックの全体的なレート上限](https://aistudio.google.com/rate-limit?hl=ja)に対してカウントされますが、独自のレート上限が適用されます。優先度推論のデフォルトのレート上限は、**モデル / 階層の標準レート上限の 0.3 倍**です。

### グレースフル ダウングレード ロジック

輻輳により優先度の上限を超えた場合、オーバーフロー リクエストは 503 エラーまたは 429 エラーで失敗するのではなく、**自動的に正常に** Standard 処理にダウングレードされます。ダウングレードされたリクエストは、優先度の高いプレミアム料金ではなく、標準料金で課金されます。

### お客様の責任

- **レスポンスのモニタリング**: デベロッパーは、API レスポンスの `x-gemini-service-tier` ヘッダーをモニタリングして、リクエストが `standard` に頻繁にダウングレードされているかどうかを検出する必要があります。
- **再試行**: クライアントは、`DEADLINE_EXCEEDED` などの標準エラーに対して再試行ロジック/指数バックオフを実装する必要があります。

## 料金

優先度推論の料金は、[標準 API](https://ai.google.dev/gemini-api/docs/pricing?hl=ja) の 75 ～ 100% 増しで、トークン単位で課金されます。

## サポートされているモデル

次のモデルは優先度付き推論をサポートしています。

| モデル | 優先度の推論 |
| --- | --- |
| [Gemini 3.1 Flash-Lite プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ja) | ✔️ |
| [Gemini 3.1 Pro プレビュー版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja) | ✔️ |
| [Gemini 3 Flash プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ja) | ✔️ |
| [Gemini 3 Pro Image プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=ja) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ja) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ja) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=ja) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ja) | ✔️ |

## 次のステップ

Gemini のその他の[推論と最適化](https://ai.google.dev/gemini-api/docs/optimization?hl=ja)のオプションについては、以下をご覧ください。

- [Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja)により、費用を 50% 削減。
- 24 時間以内の非同期処理用の [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)。
- 入力トークン費用を削減するための[コンテキスト キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-04-29 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-04-29 UTC。"],[],[]]
