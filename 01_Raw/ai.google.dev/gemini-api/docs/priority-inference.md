---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja
fetched_at: 2026-09-28T06:18:29.691465+00:00
title: "\u512a\u5148\u5ea6\u63a8\u8ad6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 優先度推論

説明: Interactions API の優先度推論階層を使用してレイテンシを最適化する方法について説明します

Gemini Priority API は、低レイテンシと最高の信頼性を必要とするビジネス クリティカルなワークロード向けに設計されたプレミアム推論ティアです。優先度階層のトラフィックは、標準 API と Flex 階層のトラフィックよりも優先されます。

優先度推論は、Interactions API エンドポイント全体で利用できます。

## 優先度の使用方法

優先度階層を使用するには、リクエストの `service_tier` フィールドを `priority` に設定します。フィールドが省略されている場合、デフォルトの階層は標準です。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Triage this critical customer support ticket immediately.",
    service_tier='priority'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
    const interaction = await ai.interactions.create({
        model: "gemini-3.8-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Perform a priority inference task."))
        .serviceTier(ServiceTier.PRIORITY)
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("Perform a priority inference task."),
            ServiceTier: interactions.ServiceTierPriority.ToPointer(),
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## 優先度推論の仕組み

優先度推論では、リクエストが重要度の高いコンピューティング キューに転送され、ユーザー向けアプリケーションに予測可能で高速なパフォーマンスが提供されます。主なメカニズムは、動的上限を超えるトラフィックに対して、サーバーサイドで標準処理にグレースフルにダウングレードすることです。これにより、リクエストが失敗するのではなく、アプリケーションの安定性が確保されます。

| 機能 | 優先度 | 標準 | Flex | バッチ |
| --- | --- | --- | --- | --- |
| **料金** | Standard の 75 ～ 100% 増 | 通常料金 | 50% 割引 | 50% 割引 |
| **レイテンシ** | 秒 | 数秒～数分 | 分（1 ～ 15 分の目標） | 最大 24 時間 |
| **信頼性** | 高（非脱落性） | 高 / 中高 | ベスト エフォート（Sheddable） | 高（スループットの場合） |
| **インターフェース** | 同期 | 同期 | 同期 | 非同期 |

### 主なメリット

- **低レイテンシ**: ユーザー向けのインタラクティブな AI ツールで、応答時間が 1 秒になるように設計されています。
- **高い信頼性**: トラフィックは最も高い重要度で処理され、厳密に非シェディングです。
- **グレースフル デグラデーション**: 動的上限を超えるトラフィックの急増は、失敗するのではなく、処理のために自動的に Standard 階層にダウングレードされ、サービス停止を防ぎます。
- **低摩擦**: 標準階層と Flex 階層と同じ同期 `create` メソッドを使用します。

### ユースケース

優先処理は、パフォーマンスと信頼性が最優先されるビジネス クリティカルなワークフローに最適です。

- **インタラクティブ AI アプリケーション**: ユーザーがプレミアム料金を支払い、迅速で一貫性のある応答を期待するカスタマー サービス chatbot と copilot。
- **リアルタイムの意思決定エンジン**: ライブ チケットのトリアージや不正行為の検出など、信頼性が高く、レイテンシの低い結果を必要とするシステム。
- **プレミアム カスタマー機能**: 有料ユーザーに対してより高いサービスレベル目標（SLO）を保証する必要があるデベロッパー。

### レート上限

優先度の消費は、[インタラクティブ トラフィックの全体的なレート制限](https://aistudio.google.com/rate-limit?hl=ja)に対してカウントされますが、独自のレート制限が適用されます。優先度推論のデフォルトのレート上限は、**モデル / ティアの標準レート上限の 0.3 倍**です。

### グレースフル ダウングレード ロジック

輻輳により優先度の上限を超えた場合、オーバーフロー リクエストは 503 エラーまたは 429 エラーで失敗するのではなく、**自動的にかつ安全に** Standard 処理にダウングレードされます。ダウングレードされたリクエストは、優先度プレミアム料金ではなく、標準料金で課金されます。

### お客様の責任

- **レスポンスのモニタリング**: デベロッパーは、API レスポンスの `x-gemini-service-tier` ヘッダーをモニタリングして、リクエストが `standard` に頻繁にダウングレードされているかどうかを検出する必要があります。
- **再試行**: クライアントは、`DEADLINE_EXCEEDED` などの標準エラーに対して再試行ロジック/指数バックオフを実装する必要があります。

## 料金

優先推論の料金は、[標準 API](https://ai.google.dev/gemini-api/docs/pricing?hl=ja) の 75 ～ 100% 増しで、トークンごとに課金されます。

## サポートされているモデル

次のモデルは優先度推論をサポートしています。

| モデル | 優先度推論 |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=ja) | ✔️ |
| [Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=ja) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ja) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ja) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ja) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ja) | ✔️ |
| [Gemini 3.1 Pro プレビュー版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja) | ✔️ |
| [Gemini 3 Flash プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ja) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ja) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ja) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ja) | ✔️ |

## 次のステップ

- 費用削減のための[フレキシブル推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja)。
- [トークン](https://ai.google.dev/gemini-api/docs/tokens?hl=ja): トークンについて理解します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-24 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-24 UTC。"],[],[]]
