---
source_url: https://ai.google.dev/gemini-api/docs/safety-settings?hl=ja
fetched_at: 2026-10-19T05:41:14.516741+00:00
title: "\u5b89\u5168\u6027\u8a2d\u5b9a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 安全性設定

Gemini API には、プロトタイピングの段階で調整できる安全性の設定が用意されています。これにより、アプリケーションに対してより厳しいまたは緩い安全性の構成が必要かどうかを判断できます。これらの設定は、フィルタ
カテゴリ全体で調整して、特定の種類のコンテンツを制限または許可できます。

このガイドでは、インタラクションで安全性の設定を行う方法、コンテンツがブロックされた場合の動作、使用できるカテゴリとしきい値について説明します。

## 安全性の設定を行う

インタラクションを作成するときに、`safety_settings` のリストを渡します。各設定では、有害カテゴリ（`type`）としきい値（`threshold`）がペアになっています。

次の例では、ヘイトスピーチ（`hate_speech`）カテゴリを `block_low_and_above` に設定しています。これにより、ヘイトスピーチである確率が低い以上のコンテンツはすべてブロックされます。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Some potentially unsafe prompt.",
    safety_settings=[
        {
            "type": "hate_speech",
            "threshold": "block_low_and_above",
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Some potentially unsafe prompt.",
    safety_settings: [
      {
        type: "hate_speech",
        threshold: "block_low_and_above",
      },
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.HarmCategory;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.SafetySetting;
import com.google.genai.gaos.models.interactions.Threshold;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

SafetySetting hateSpeechSafety =
    SafetySetting.builder()
        .type(HarmCategory.HATE_SPEECH)
        .threshold(Threshold.BLOCK_LOW_AND_ABOVE)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Some potentially unsafe prompt."))
        .safetySettings(List.of(hateSpeechSafety))
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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Some potentially unsafe prompt."),
            SafetySettings: []interactions.SafetySetting{
                {
                    Type:      interactions.HarmCategoryHateSpeech,
                    Threshold: interactions.ThresholdBlockLowAndAbove,
                },
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Some potentially unsafe prompt.",
    "safety_settings": [
      {"type": "hate_speech", "threshold": "block_low_and_above"}
    ]
  }'
```

カテゴリごとに 1 つの設定を含めることができます。設定しないカテゴリでは、デフォルトのしきい値が使用されます。Gemini 2.5 以降のモデルでは、デフォルトのしきい値は**オフ** です。

## コンテンツがブロックされた場合

安全フィルタによって入力またはモデルのレスポンスがブロックされると、インタラクションは HTTP `400` エラーで失敗します。ブロックされたコンテンツは返されません。

エラー `code` は、リクエストがブロックされた理由を示します。

- `safety`: 入力またはレスポンスが安全フィルタによってブロックされました。
- `jailbreak`、`prohibited_content`、`blocklist`: 入力がその理由でブロックされました。エラー `message` は `Input blocked:` で始まります。

次に例を示します。

```
{
  "error": {
    "code": "safety",
    "message": "Request blocked due to safety violations (harmful content). Please modify your input and retry."
  }
}
```

バックグラウンド インタラクション（`background=true`）の場合、インタラクションの `status` は
`failed` に設定され、同じ `code` と `message` が `errors` リストに表示されます。
ストリーミングの場合、エラーは `error` イベントとして到着します。

## 安全フィルタ

Gemini API の調整可能な安全フィルタは、次のカテゴリを対象としています。

| カテゴリ | 値（API） | 説明 |
| --- | --- | --- |
| ハラスメント | `harassment` | 虐待的、脅迫的、またはいじめ、苦しめ、嘲笑を目的としたコンテンツ。 |
| ヘイトスピーチ | `hate_speech` | 特定の属性に基づいて、個人またはグループに対する暴力や憎悪を助長するコンテンツ。 |
| 露骨な性表現 | `sexually_explicit` | 露骨な性表現を含むコンテンツ。 |
| 危険 | `dangerous_content` | 危険な行為を助長、促進、可能にするコンテンツ。 |
| ジェイルブレイク | `jailbreak` | 安全フィルタを回避するように設計されたプロンプト。 |

これらのフィルタを使用して、ユースケースに適切なコンテンツとなるように調整できます。たとえば、ゲームの会話を作成する場合、ゲームの性質上、 「危険」として評価されたコンテンツをより多く許容することを問題ないとみなす場合があります。

Gemini API には、調整可能な安全フィルタに加えて、児童を危険にさらすようなコンテンツなど、重大な有害性に対する保護機能が組み込まれています。
このような種類の有害性は常にブロックされ、調整することはできません。

## ブロックしきい値

モデルには固有の安全性があるため、追加のフィルタはデフォルトで**オフ** になっています。
デフォルトのモデルの動作はほとんどのユースケースに対応しているため、アプリケーションで常に必要な場合にのみ、これらの設定を調整してください。

次の表に、カテゴリごとに設定できるしきい値を示します。たとえば、**ヘイトスピーチ** を**少量をブロック** （`block_only_high`）に設定すると、ヘイトスピーチである確率が高いコンテンツはブロックされ、確率が低いコンテンツは許可されます。

| しきい値（Google AI Studio） | しきい値（API） | 説明 |
| --- | --- | --- |
| オフ | `off` | 安全フィルタをオフにする |
| 少量をブロック | `block_only_high` | 安全でないコンテンツである確率が高い場合にブロックする |
| 一部をブロック | `block_medium_and_above` | 安全でないコンテンツである確率が中程度または高い場合にブロックする |
| ほとんどをブロック | `block_low_and_above` | 安全でないコンテンツである確率が低い、中程度、高い場合にブロックする |

### 確率と重大度

Gemini API は、コンテンツが安全でない確率を、高い、中程度、低い、無視できるのいずれかに評価します。有害性の重大度ではなく、その確率に基づいてコンテンツをブロックします。有害性が深刻であっても、安全でない確率が低いコンテンツもあります。たとえば、次の文を比較します。

1. ロボットが私をパンチした。
2. ロボットが私を切り付けた。

最初の文は安全でない確率が高い可能性がありますが、2 番目の文はより深刻であると考えるかもしれません。エンドユーザーへの危害を最小限に抑えながら、ユースケースをサポートするブロックレベルを見つけるために、慎重にテストしてください。

## Google AI Studio で安全性の設定を調整する

[**実行設定**] パネルの [**詳細設定**] で [**安全性の設定**] をクリックして、[**実行の安全性の設定**] モーダルを開きます。モーダルでは、スライダーを使用して、安全カテゴリごとにコンテンツ フィルタリング レベルを調整できます。

![](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_ui.png?hl=ja)

リクエストを送信すると（たとえば、モデルに質問するなど）、リクエストの
コンテンツがブロックされた場合、
warning [**\*\*コンテンツがブロックされました\*\***] メッセージが表示されます。詳細を確認するには、[**コンテンツがブロックされました**] テキストにポインタを合わせると、カテゴリと有害性の分類の確率が表示されます。

## 次のステップ

- 完全な API について詳しくは、[Interactions API リファレンス](https://ai.google.dev/api/interactions-api?hl=ja)
  をご覧ください。
- LLM を使用して開発する際の安全性
  の考慮事項の概要については、[安全に関するガイダンス](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ja)をご覧ください。
- 確率と重大度の評価について詳しくは、[Jigsaw
  チーム](https://developers.perspectiveapi.com/s/about-the-api-score)をご覧ください。
- [Perspective
  API](https://medium.com/jigsaw/reducing-toxicity-in-large-language-models-with-perspective-api-c31c39b7a4d7) などの安全ソリューションに貢献するプロダクトについて詳しくは、こちらをご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-15 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-15 UTC。"],[],[]]
