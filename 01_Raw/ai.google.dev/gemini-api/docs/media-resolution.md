---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=ja
fetched_at: 2026-10-19T05:42:52.821741+00:00
title: "\u30e1\u30c7\u30a3\u30a2\u306e\u89e3\u50cf\u5ea6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# メディアの解像度

`media_resolution` パラメータは、メディア入力に割り当てられる**トークンの最大数**を決定することで、Gemini API が画像、動画、音声、PDF ドキュメントなどのメディア入力を処理する方法を制御します。これにより、回答の品質とレイテンシ、費用を調整できます。ビジュアル入力とドキュメント入力では、解像度の設定に基づいてトークンの割り当てがスケーリングされますが、音声入力は、すべての解像度レベルで 1 秒あたり固定レートでトークン化されます。さまざまな設定、デフォルト値、トークンとの対応については、[トークン数](#token-counts)セクションをご覧ください。

リクエスト内の個々のメディア オブジェクト（コンテンツ アイテム）に対してメディア解像度を構成できます（Gemini 4 モデルと Gemini 3 モデル）。

## コンテンツ アイテムごとのメディア解像度（Gemini 4 モデルと Gemini 3 モデル）

Gemini 4 モデルと Gemini 3 モデルでは、リクエスト内の個々のメディア オブジェクトにメディア解像度を設定できるため、トークンの使用量を細かく最適化できます。1 つのリクエストで複数の解像度レベルを混在させることができます。たとえば、複雑な図には高解像度を使用し、シンプルなコンテキスト画像には低解像度を使用します。

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Describe the details in this high-resolution image.").build();
Content imageContent =
    ImageContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/image/scones.jpg")
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
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

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/image.jpg", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe the details in this high-resolution image.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:        genai.Ptr(uploadedFile.URI),
                    MimeType:   interactions.ImageContentMimeType(uploadedFile.MIMEType).ToPointer(),
                    Resolution: interactions.MediaResolutionHigh.ToPointer(),
                }),
            }),
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
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## 使用可能な解像度の値

Gemini API では、メディアの解像度について次のレベルが定義されています。

- `unspecified`: デフォルト設定。このレベルのトークン数は、Gemini 4/3 と以前の Gemini モデルで大きく異なります。
- `low`: トークン数が減り、処理が高速化され、コストが削減されますが、詳細が少なくなります。
- `medium`: 詳細、費用、レイテンシのバランスが取れています。
- `high`: トークン数が多いほど、モデルが処理する詳細情報が増えますが、レイテンシと費用が増加します。
- `ultra_high`（コンテンツ アイテムごと）: トークン数が最も多く、[パソコンの使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)などの特定のユースケースで必要です。

`high` は、ほとんどのユースケースで最適なパフォーマンスを提供します。

これらの各レベルで生成されるトークンの正確な数は、**メディアタイプ**（画像、動画、音声、PDF）と**モデル バージョン**の両方によって異なります。

## トークン数

次の表は、モデル ファミリーごとの各 `media_resolution` 値とメディアタイプのおおよそのトークン数をまとめたものです。

**Gemini 4 モデルと Gemini 3 モデル**

| MediaResolution | 画像 | 動画 | 音声 | PDF |
| --- | --- | --- | --- | --- |
| `unspecified`（デフォルト） | 1120 | 70 | 25（1 秒あたり） | 560 |
| `low` | 280 | 70 | 25（1 秒あたり） | 280 + ネイティブ テキスト |
| `medium` | 560 | 70 | 25（1 秒あたり） | 560 + ネイティブ テキスト |
| `high` | 1120 | 280 | 25（1 秒あたり） | 1120 + ネイティブ テキスト |
| `ultra_high` | 2240 | なし | 該当なし | なし |

## 適切な解像度の選択

- **デフォルト（`unspecified`）:** デフォルトから始めます。最も一般的なユースケースで品質、レイテンシ、費用のバランスが取れるように調整されています。
- **`low`:** 費用とレイテンシが最も重要で、詳細な情報がそれほど重要でないシナリオで使用します。
- **`medium` / `high`:** メディア内の複雑な詳細を理解する必要があるタスクでは、解像度を上げます。これは、複雑な視覚分析、グラフの読み取り、密度の高いドキュメントの理解に必要になることがよくあります。
- **`ultra_high`** - コンテンツ アイテムごとの設定でのみ使用できます。コンピュータの使用など、特定のユースケースや、テストで `high` よりも明確な向上が示されている場合に推奨されます。
- **コンテンツ アイテムごとの制御（Gemini 4 と Gemini 3）:** トークンの使用量を最適化します。たとえば、複数の画像を含むプロンプトでは、複雑な図には `high` を使用し、よりシンプルなコンテキスト画像には `low` または `medium` を使用します。

**おすすめの設定**

以下に、サポートされているメディアタイプごとに推奨されるメディア解像度の設定を示します。

| メディアタイプ | 推奨される設定 | 最大トークン数 | 使用ガイダンス |
| --- | --- | --- | --- |
| **画像** | `high` | 1120 | 品質を最大限に高めるため、ほとんどの画像分析タスクに推奨されます。 |
| **PDF** | `medium` | 560 | ドキュメントの理解に最適です。通常、品質は `medium` で飽和します。`high` に増やしても、標準ドキュメントの OCR 結果が改善されることはほとんどありません。 |
| **動画**（一般） | `low`（または `medium`） | 70（フレームあたり） | **注:** 動画の場合、コンテキストの使用を最適化するために、`low` と `medium` の設定は同じ（70 トークン）として扱われます。これは、ほとんどのアクション認識と説明のタスクで十分です。 |
| **動画**（テキストが多い） | `high` | 280（フレームあたり） | ユースケースに、動画フレーム内の高密度テキスト（OCR）や細部の読み取りが含まれる場合にのみ必要です。 |
| **音声** | `unspecified`（デフォルト） | 25（1 秒あたり） | 音声は、サポートされているすべての解像度設定（`unspecified`、`low`、`medium`、`high`）で、1 秒あたり 25 トークンの固定レートでトークン化されます。 |

さまざまな解像度設定がアプリケーションに与える影響を常にテストして評価し、品質、レイテンシ、費用の間で最適なトレードオフを見つけてください。

## 動画処理モードとの関係

`media_resolution` と処理パラメータは、動画入力のさまざまな側面を制御します。

- `media_resolution` は、各フレームの**解像度**（フレームあたりのトークン数）を制御します。
- `processing` / `media_processing` は、**動画のどのコンテンツ**がコンテキストに読み込まれるかを制御します。

同じ動画入力に両方を設定できます。たとえば、メディア解像度の低いエージェント処理を使用して、長い動画の合計トークン使用量を最小限に抑えることができます。

動画処理モードの詳細については、[エージェントによる動画理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja#agentic-video-understanding)のガイドをご覧ください。

## バージョンの互換性の概要

- 個々のコンテンツ アイテムに `resolution` を設定することは、**Gemini 4 モデルと Gemini 3 モデルでサポートされています**。

## 次のステップ

- Gemini API のマルチモーダル機能の詳細については、[画像の理解](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ja)、[動画の理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja)、[音声の理解](https://ai.google.dev/gemini-api/docs/audio?hl=ja)、[ドキュメントの理解](https://ai.google.dev/gemini-api/docs/document-processing?hl=ja)のガイドをご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-13 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-13 UTC。"],[],[]]
