---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=ja
fetched_at: 2026-10-05T06:34:03.472078+00:00
title: "Gemini for Research \u3067\u767a\u898b\u3092\u52a0\u901f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)

# Gemini for Research で発見を加速

[Gemini API キーを取得する](https://aistudio.google.com/apikey?hl=ja)

Gemini モデルは、さまざまな分野の基礎研究を進めるために使用できます。Gemini を調査に活用する方法は次のとおりです。

- **モデルの出力を分析して制御する**: さらに分析するために、`CitationMetadata` などのツールを使用して、モデルによって生成されたレスポンス候補を調べることができます。`responseSchema`、`topP`、`topK` など、モデルの生成と出力のオプションを構成することもできます。[詳細](https://ai.google.dev/api/generate-content?hl=ja)
- **マルチモーダル入力**: Gemini は画像、音声、動画を処理できるため、さまざまなエキサイティングな研究の方向性を実現できます。[詳細](https://ai.google.dev/gemini-api/docs/vision?hl=ja)
- **長いコンテキスト機能**: Gemini 3.0 Flash と Pro には、100 万トークンのコンテキスト ウィンドウが搭載されています。[詳細](https://ai.google.dev/gemini-api/docs/long-context?hl=ja)
- **Grow with Google**: API と Google AI Studio を通じて Gemini モデルにすばやくアクセスし、本番環境のユースケースに活用できます。Google Cloud ベースのプラットフォームをお探しの場合は、Gemini Enterprise Agent Platform で追加のサポート インフラストラクチャを利用できます。

学術研究を支援し、最先端の研究を推進するため、Google は [Gemini アカデミック プログラム](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=ja#gemini-academic-program)を通じて、科学者や学術研究者に Gemini API クレジットを提供しています。

## Gemini を使ってみる

Gemini API と Google AI Studio を使用すると、Google の最新モデルの利用を開始し、アイデアをスケーラブルなアプリケーションに変えることができます。

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;

Client client = new Client();
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("How large is the universe?"))
    .build();
var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("How large is the universe?"),
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## 注目の学術関係者

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=ja)

「私たちの研究では、Gemini を視覚言語モデル（VLM）として、堅牢性と安全性の観点からさまざまな環境におけるエージェントの動作を調査しています。これまでのところ、VLM エージェントがコンピュータ タスクを実行する際のポップアップ ウィンドウなどの妨害に対する Gemini の堅牢性を評価し、Gemini を活用してソーシャル インタラクション、時間的イベント、動画入力に基づくリスク要因を分析してきました。」

[Diyi Yang のウェブサイト](https://cs.stanford.edu/~diyiy/)

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=ja)

「Gemini Pro と Flash は、長いコンテキスト ウィンドウを備えており、オープン ボキャブラリー モバイル マニピュレーション プロジェクトである OK-Robot で活用されています。Gemini を使用すると、ロボットの「メモリ」（この場合は、ロボットが長期間の動作中に取得した過去の観測データ）に対して、複雑な自然言語クエリとコマンドを実行できます。Mahi Shafiullah と私は、Gemini を使用して、ロボットが現実世界で実行できるコードにタスクを分解しています。」

[Lerrel Pinto のウェブサイト](https://www.lerrelpinto.com/)

## Gemini アカデミック プログラム

[対象国](https://ai.google.dev/gemini-api/docs/available-regions?hl=ja)の認定学術研究者（教員、職員、博士課程の学生など）は、研究プロジェクトで Gemini API クレジットとレート上限の引き上げを受けることができます。このサポートにより、科学実験のスループットが向上し、研究が進歩します。

特に、次のセクションの研究分野に関心がありますが、さまざまな科学分野からの応募を歓迎します。

- **評価とベンチマーク**: 事実性、安全性、指示の遵守、推論、計画などの分野で強力なパフォーマンス シグナルを提供できる、コミュニティで承認された評価方法。
- **人類に利益をもたらす科学的発見の加速**: 希少疾患や顧みられない病気、実験生物学、材料科学、持続可能性などの分野を含む、学際的な科学研究における AI の潜在的な応用。
- **エンボディメントとインタラクション**: 大規模言語モデルを活用して、エンボディド AI、アンビエント インタラクション、ロボティクス、ヒューマン コンピュータ インタラクションの分野における新しいインタラクションを調査します。
- **新機能**: 推論と計画を強化するために必要な新しいエージェント機能を検討し、推論中に機能を拡張する方法（Gemini Flash の活用など）を検討します。
- **マルチモーダルなインタラクションと理解**: さまざまなタスクにわたる分析、推論、計画のためのマルチモーダル基盤モデルのギャップと機会を特定します。

対象: 有効な教育機関または学術研究機関に所属する個人（教員、研究者など）のみが申請できます。API へのアクセス権とクレジットは、Google の裁量で付与および削除されます。お申し込みは毎月審査されます。

### Gemini API を使用して調査を開始する

[今すぐ申し込む](https://forms.gle/HMviQstU8PxC5iCt5)

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-24 UTC。

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-24 UTC。"],[],[]]
