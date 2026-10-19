---
source_url: https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ja
fetched_at: 2026-10-19T05:30:22.579068+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini Robotics ER

Gemini Robotics ER（embodied reasoning）モデルは、ロボットが現実世界を認識して操作できるようにする視覚言語モデル（VLM）です。視覚データを解釈し、空間的および時間的な推論を行い、マルチステップのタスクを計画し、ロボットとツールをオーケストレートします。

## モデル

Gemini Robotics ER 2 モデルは、Gemini Robotics の最新モデルです。これは、ロボットが環境を正確に理解できるようにする、更新された推論モデルです。ロボットの自律的なオーケストレーション（VLA の使用など）、進捗状況の把握や成功の検出を含むロボット動画の理解、計測器の読み取り、ポインティング、空間推論など、身体化された推論機能に特化しています。

Gemini Robotics ER 2 モデルには、次の 2 つのモデル エンドポイントが導入されています。

- **`gemini-robotics-er-2-preview`**: 標準の ER 2 モデル。Gemini 3.5 Flash をベースに、空間推論、動画の瞬間検出、動画の進行状況の分類、マルチロボット オーケストレーション、マルチステップ ツール使用が改善されています。
- **`gemini-robotics-er-2-streaming-preview`**: [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ja) を使用したリアルタイム ストリーミング用に最適化されています。このモデルは、連続した音声入力と動画入力を処理する低レイテンシのロボット エージェントに使用します。

Gemini Robotics ER 1.6 は [2026 年 8 月 31 日に非推奨になりました](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja#robotics-models)。Gemini Robotics ER 1.6 をまだ使用している場合は、API 呼び出しで `model="gemini-robotics-er-1.6-preview"` を `model="gemini-robotics-er-2-preview"` または `model="gemini-robotics-er-2-streaming-preview"` に置き換えて、Gemini Robotics ER 2 にアップグレードします。

[Google AI Studio で Gemini Robotics ER 2 を試す](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=ja)

## ロボット工学の機能

Gemini Robotics ER は、さまざまな身体化された推論機能をサポートしています。機能を選択して詳細を確認します。

| 能力 | 説明 | ガイド |
| --- | --- | --- |
| 空間推論 | オブジェクトをポイントし、動画内で追跡し、境界ボックスで検出し、軌跡を計画します。 | [空間推論](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=ja) |
| エージェントのビジョン | コード実行を使用して、画像操作ツールを活用して他の機能を強化します。 | [エージェントのビジョン](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=ja) |
| タスク オーケストレーション | 空間推論とカスタム ロボット API を組み合わせて、長期的なタスクを完了します。 | [タスク オーケストレーション](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ja) |
| ストリーミング（Gemini Robotics ER 2 ストリーミング エンドポイントのみ） | 低レイテンシの関数呼び出しによるリアルタイム ロボット エージェントの双方向ストリーミング。 | [ロボット工学向けのストリーミング](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ja) |
| 動画の進行状況（Gemini Robotics ER 2 のみ） | 継続的な動画フィードからの瞬間検出と進行状況の分類。 | [動画に関する理解を深める](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ja) |

## 始める前に

Gemini Robotics ER モデルは、**Gemini Developer API** を通じて利用できます。まず、[Google AI Studio](https://aistudio.google.com/apikey?hl=ja) または [Google Cloud コンソール](https://ai.google.dev/gemini-api/docs/api-key?hl=ja#cloud-console)で [Gemini API キー](https://ai.google.dev/gemini-api/docs/api-key?hl=ja)を作成し、[環境を設定](https://ai.google.dev/gemini-api/docs/api-key?hl=ja#setup-environment)します。

キーの種類、セキュリティ、Python、JavaScript などの言語でキーを構成する方法の詳細については、[Gemini API キーを使用する](https://ai.google.dev/gemini-api/docs/api-key?hl=ja)をご覧ください。

## スタートガイド

次の例では、画像内のオブジェクトを検出し、正規化された 2D 座標とラベルを返します。この出力は、ロボット アクションを生成するために、ロボット API または VLA モデルに直接渡すことができます。

### Python

```
from google import genai

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

image_response = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": PROMPT}
    ],
    generation_config={"thinking_level": "high"},
)

print(image_response.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const PROMPT = `
  Point to no more than 10 items in the image. The label returned
  should be an identifying name for the object detected.
  The answer should follow the json format: [{"point": <point>,
  "label": <label1>}, ...]. The points are in [y, x] format
  normalized to 0-1000.
`;
const client = new GoogleGenAI();

const uploadedFile = await client.files.upload({ file: "my-image.png" });

const imageResponse = await client.interactions.create({
  model: "gemini-robotics-er-2-preview",
  input: [
    {
      type: "image",
      uri: uploadedFile.uri,
      mime_type: uploadedFile.mimeType,
    },
    { type: "text", text: PROMPT },
  ],
  generation_config: { thinking_level: "high" },
});

console.log(imageResponse.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.List;

Client client = new Client();

String prompt =
    "Point to no more than 10 items in the image. The label returned "
        + "should be an identifying name for the object detected. "
        + "The answer should follow the json format: [{\"point\": <point>, "
        + "\"label\": <label1>}, ...]. The points are in [y, x] format "
        + "normalized to 0-1000.";

File uploadedFile =
    client.files.upload(
        new java.io.File("my-image.png"),
        UploadFileConfig.builder().mimeType("image/png").build());

Content imageContent =
    ImageContent.builder()
        .uri(uploadedFile.uri().orElse(""))
        .mimeType(ImageContentMimeType.of(uploadedFile.mimeType().orElse("image/png")))
        .build();
Content textContent = TextContent.builder().text(prompt).build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-robotics-er-2-preview"))
        .input(InteractionsInput.ofContent(List.of(imageContent, textContent)))
        .generationConfig(
            GenerationConfig.builder().thinkingLevel(ThinkingLevel.HIGH).build())
        .build();

Interaction imageResponse =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(imageResponse.outputText().orElse(""));
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

    prompt := `Point to no more than 10 items in the image. The label returned
should be an identifying name for the object detected.
The answer should follow the json format: [{"point": <point>,
"label": <label1>}, ...]. The points are in [y, x] format
normalized to 0-1000.`

    uploadedFile, err := client.Files.UploadFromPath(ctx, "my-image.png", &genai.UploadFileConfig{
        MIMEType: "image/png",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-robotics-er-2-preview"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    URI:      genai.Ptr(uploadedFile.URI),
                    MimeType: genai.Ptr(interactions.ImageMimeTypeImagePng),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelHigh.ToPointer(),
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
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-robotics-er-2-preview",
    "input": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "image/png",
            "data": "'"${IMAGE_BASE64}"'"
          }
        },
        {
          "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
        }
      ]
    },
    "generation_config": {
      "thinking_config": {
        "thinking_level": "high"
      }
    }
  }'
```

出力は、オブジェクトを含む JSON 配列になります。各オブジェクトには、`point`（正規化された `[y, x]` 座標）と、オブジェクトを識別する `label` が含まれます。

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

次の画像は、これらのポイントの表示例です。

![画像内のオブジェクトのポイントを表示する例](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=ja)

## 仕組み

Gemini Robotics ER は、自然言語プロンプトで画像、動画、音声の入力を受け取ります。オブジェクトを識別し、シーンのコンテキストと空間関係について推論し、座標や境界ボックスなどの構造化された出力を返します。

Gemini Robotics ER はエージェント機能も備えています。複雑なタスクをサブタスクに分割し、ロボット関数を呼び出すか、生成されたコードを実行してサブタスクを実行します。たとえば、「りんごをボウルに入れる」というタスクは、りんごを見つける、りんごを掴む、りんごを置くという一連のステップになります。

Gemini がツール呼び出しを実行する方法の詳細については、[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=ja#how-it-works)をご覧ください。

## 安全性

Gemini Robotics ER は安全性を考慮して構築されていますが、ロボットの周囲の安全な環境を維持するのはお客様の責任です。生成 AI モデルは間違えることがあり、物理的なロボットは損傷を引き起こす可能性があります。詳しくは、[Gemini Robotics の安全性に関するページ](https://deepmind.google/models/gemini-robotics/safety?hl=ja)をご覧ください。

## ベスト プラクティス

1. 平易で自然な言葉を使用します。ロボットに実行させたいことを、人に説明するのと同じように記述します。用語が機能しない場合は、一般的な同義語を試してください。
2. 視覚的な入力を最適化します。画像を送信する前に、小さくて不鮮明なオブジェクトを切り抜くか、拡大します。照明や色のコントラストが低いと、検出に影響することがあります。
3. 複雑なタスクをステップに分割します。各ステップを個別のプロンプトとして送信して、モデルの焦点を絞り、精度を高めます。
4. 高精度のタスクでは、複数回クエリを実行して結果を平均します。このコンセンサス アプローチにより、空間出力の分散が減少します。

## 制限事項

Gemini Robotics ER を使用して開発する場合は、次の制限事項を考慮してください。

- **API キーの制限:** Gemini API は、制限のない API キーからのリクエストを受け付けず、`403 Forbidden` エラーを返します。[AI Studio](https://aistudio.google.com/api-keys?hl=ja) で制限を追加して、API キーを保護します。詳細については、[制限のない API キーを保護する](https://ai.google.dev/gemini-api/docs/api-key?hl=ja#secure-unrestricted-keys)をご覧ください。
- **レイテンシとパフォーマンス:** 複雑なクエリ、高解像度の入力、高度な思考レベルは、処理時間の増加につながる可能性があります。思考レベルでは、レイテンシとパフォーマンスのバランスが取れた中を使用します。
- **ハルシネーション:** すべての大規模言語モデルと同様に、Gemini Robotics ER モデルも、特に曖昧なプロンプトや分布外の入力に対して、ハルシネーションを起こしたり、不正確な情報を提供したりすることがあります。
- **プロンプトの品質に依存:** 出力の品質は、入力プロンプトの明確さに依存します。具体的で構造化されたプロンプトを使用します。
- **コンピューティング費用:** モデルを実行すると、特に動画入力や高い `thinking_budget` を使用すると、コンピューティング リソースが消費され、費用が発生します。詳細については、[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)のページをご覧ください。
- **入力タイプ:** 各モードの制限事項について詳しくは、以下のトピックをご覧ください。
  - [画像入力](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ja#technical-details-image)
  - [動画入力](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja#supported-formats)
  - [音声入力](https://ai.google.dev/gemini-api/docs/audio?hl=ja#supported-formats)

## プライバシーに関するお知らせ

お客様は、このドキュメントで言及されているモデル（以下「ロボット モデル」）が、お客様の指示に従ってハードウェアを操作し、移動するために動画データと音声データを活用することを理解し、これに同意するものとします。そのため、音声、画像、肖像データなどの個人を特定できる人物のデータ（「個人データ」）がロボット モデルによって収集されるように、ロボット モデルを操作することがあります。個人データを収集する方法でロボット モデルを運用することを選択した場合、Gemini API の追加利用規約（[https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=ja)）に記載されているとおり、Google に個人データが提供され、使用される可能性があることを十分に通知し、同意を得るまで、ロボット モデルの周囲のエリアで個人を特定できる人物がロボット モデルとやり取りしたり、ロボット モデルの周囲のエリアに立ち入ったりすることを許可しないことに同意するものとします（「Google によるデータの使用方法」というセクションに記載されているとおり）。お客様は、かかる通知が本規約に定める個人データの収集と使用を許可することを保証し、顔のぼかしなどの技術を使用したり、識別可能な人物が含まれないエリアでロボット モデルを運用したりするなど、商業上合理的な努力をもって、個人データの収集と配布を可能な限り最小限に抑えます。

## 料金

料金と利用可能なリージョンの詳細については、[料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)ページをご覧ください。

## モデル エンドポイント

### Gemini Robotics ER 2 プレビュー版

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | `gemini-robotics-er-2-preview` |
| save でサポートされているデータ型 | **入力**  テキスト、画像、動画、音声  **出力**  テキスト |
| token\_autoトークンの上限[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ja) | **入力トークンの上限**  131,072  **出力トークンの上限**  65,536 |
| handyman機能 | **[音声生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja)**  サポート対象外  **[キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)**  サポート対象  **[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)**  サポート対象  **[パソコンの使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)**  サポート対象  **[ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)**  サポート対象  **[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)**  サポート対象  **[Google マップによるグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)**  サポート対象  **[画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)**  サポート対象外  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ja)**  サポート対象外  **[検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)**  サポート対象  **[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)**  サポート対象  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)**  サポート対象  **[URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)**  サポート対象 |
| speed使用オプション | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)**  サポート対象  **[Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja)**  サポート対象外  **[優先度推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)**  サポート対象外 |
| 123 バージョン | 詳しくは、[モデル バージョンのパターン](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#model-versions)をご覧ください。  - プレビュー: `gemini-robotics-er-2-preview` |
| calendar\_month最新の更新 | 2026 年 7 月 |
| id\_cardモデルカード | [モデルカード](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=ja) |

### Gemini Robotics ER 2 ストリーミング プレビュー

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | `gemini-robotics-er-2-streaming-preview` |
| save でサポートされているデータ型 | **入力**  テキスト、画像、動画、音声  **出力**  テキスト |
| token\_autoトークンの上限[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ja) | **入力トークンの上限**  131,072  **出力トークンの上限**  65,536 |
| handyman機能 | **[音声生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja)**  サポート対象外  **[キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)**  サポート対象外  **[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)**  サポート対象外  **[パソコンの使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)**  サポート対象外  **[ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)**  サポート対象外  **[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)**  サポート対象  **[Google マップによるグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)**  サポート対象外  **[画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)**  サポート対象外  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ja)**  サポート対象  **[検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)**  サポート対象  **[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)**  サポート対象外  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)**  サポート対象  **[URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)**  サポート対象外 |
| speed使用オプション | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)**  サポート対象外  **[Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja)**  サポート対象外  **[優先度推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)**  サポート対象外 |
| 123 バージョン | 詳しくは、[モデル バージョンのパターン](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#model-versions)をご覧ください。  - プレビュー: `gemini-robotics-er-2-streaming-preview` |
| calendar\_month最新の更新 | 2026 年 7 月 |
| id\_cardモデルカード | [モデルカード](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=ja) |

### Gemini Robotics ER 1.6 プレビュー版

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | `gemini-robotics-er-1.6-preview` |
| save でサポートされているデータ型 | **入力**  テキスト、画像、動画、音声  **出力**  テキスト |
| token\_autoトークンの上限[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ja) | **入力トークンの上限**  131,072  **出力トークンの上限**  65,536 |
| handyman機能 | **[音声生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja)**  サポート対象外  **[キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)**  サポート対象  **[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)**  サポート対象  **[パソコンの使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)**  サポート対象  **[ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)**  サポート対象  **[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)**  サポート対象  **[Google マップによるグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)**  サポート対象  **[画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)**  サポート対象外  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ja)**  サポート対象外  **[検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)**  サポート対象  **[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)**  サポート対象  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)**  サポート対象  **[URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)**  サポート対象 |
| speed使用オプション | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)**  サポート対象  **[Flex 推論](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja)**  サポート対象外  **[優先度推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)**  サポート対象外 |
| 123 バージョン | 詳しくは、[モデル バージョンのパターン](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#model-versions)をご覧ください。  - プレビュー: `gemini-robotics-er-1.6-preview` |
| calendar\_month最新の更新 | 2025 年 12 月 |
| cognition\_2ナレッジ カットオフ | 2025 年 1 月 |

## 次のステップ

- [空間推論](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=ja) - ポインティング、トラッキング、境界ボックス、軌跡。
- [エージェント機能](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=ja) - コード実行、計測器の読み取り、画像アノテーション。
- [タスク オーケストレーション](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ja) - カスタム ロボット API を使用した長期的なタスク。
- [ストリーミングを使用したロボット工学](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ja) - リアルタイムの双方向ストリーミング（Gemini Robotics ER 2 のみ）。
- [動画の理解](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ja) - 瞬間検出と進捗状況の分類（Gemini Robotics ER 2 のみ）。
- [Gemini Robotics の安全性](https://deepmind.google/models/gemini-robotics/safety?hl=ja) - モデル ファミリーの背後にある安全性に関する研究。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-06 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-06 UTC。"],[],[]]
