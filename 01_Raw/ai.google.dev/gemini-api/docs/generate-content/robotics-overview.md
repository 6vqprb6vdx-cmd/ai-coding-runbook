---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-overview?hl=ja
fetched_at: 2026-09-14T05:45:14.899440+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash が利用可能になりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ja)。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs/generate-content?hl=ja)

フィードバックを送信

# Gemini Robotics ER

Gemini Robotics ER（embodied reasoning）モデルは、ロボットが現実世界を認識して操作できるようにする視覚言語モデル（VLM）です。視覚データを解釈し、空間的および時間的推論を実行し、マルチステップ タスクを計画し、ロボットとツールをオーケストレートします。

## モデル

Gemini Robotics ER 2 モデルは、Gemini Robotics の最新モデルです。これは、ロボットが環境を正確に理解できるようにする、更新された推論モデルです。ロボットの自律的なオーケストレーション（VLA の使用など）、進捗状況の把握や成功検出を含むロボット動画の理解、計測器の読み取り、ポインティング、空間推論など、身体化された推論機能に特化しています。

Gemini Robotics ER 2 モデルには、次の 2 つのモデル エンドポイントが導入されています。

- **`gemini-robotics-er-2-preview`**: 標準の ER 2 モデル。Gemini 3.5 Flash をベースに、空間推論、動画の瞬間検出、動画の進行状況の分類、マルチロボット オーケストレーション、マルチステップ ツール使用が改善されています。
- **`gemini-robotics-er-2-streaming-preview`**: [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ja) を介したリアルタイム ストリーミング用に最適化されています。このモデルは、継続的な音声入力と動画入力を処理する低レイテンシのロボット エージェントに使用します。

Gemini Robotics ER 1.6 を使用している場合は、API 呼び出しで `model="gemini-robotics-er-1.6-preview"` を `model="gemini-robotics-er-2-preview"` または `model="gemini-robotics-er-2-streaming-preview"` に置き換えて、Gemini Robotics ER 2 にアップグレードします。Gemini Robotics ER 1.6 モデルは、[8 月末](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja#robotics-models)にシャットダウンされます。

[Google AI Studio で Gemini Robotics ER 2 を試す](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=ja)

## ロボット工学の機能

Gemini Robotics ER は、さまざまな身体化された推論機能をサポートしています。機能を選択して詳細を確認します。

| 能力 | 説明 | ガイド |
| --- | --- | --- |
| 空間推論 | オブジェクトをポイントし、動画内で追跡し、境界ボックスで検出し、軌跡を計画します。 | [空間推論](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=ja) |
| エージェントのビジョン | コード実行を使用して、画像操作ツールを活用して他の機能を強化します。 | [エージェントのビジョン](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=ja) |
| タスク オーケストレーション | 空間推論とカスタム ロボット API を組み合わせて、長期的なタスクを完了します。 | [タスク オーケストレーション](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=ja) |
| ストリーミング（Gemini Robotics ER 2 ストリーミング エンドポイントのみ） | 低レイテンシの関数呼び出しによるリアルタイム ロボット エージェントの双方向ストリーミング。 | [ロボット工学向けのストリーミング](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ja) |
| 動画の進行状況（Gemini Robotics ER 2 のみ） | 連続動画フィードからの瞬間検出と進行状況の分類。 | [動画に関する理解を深める](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=ja) |

## スタートガイド

次の例では、画像内のオブジェクトを検出し、正規化された 2D 座標とラベルを返します。この出力をロボット工学 API または VLA モデルに直接渡して、ロボット アクションを生成できます。

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_uri(
            file_uri=uploaded_file.uri,
            mime_type=uploaded_file.mime_type
        ),
        PROMPT
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    ),
)

print(response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
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
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

出力は、オブジェクトを含む JSON 配列になります。各オブジェクトには、オブジェクトを識別する `point`（正規化された `[y, x]` 座標）と `label` が含まれます。

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

次の図は、これらのポイントを表示する方法の例です。

![画像内のオブジェクトのポイントを表示する例](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=ja)

## 仕組み

Gemini Robotics ER は、自然言語プロンプトで画像、動画、音声の入力を受け取ります。オブジェクトを識別し、シーンのコンテキストと空間関係を推論して、座標や境界ボックスなどの構造化された出力を返します。

Gemini Robotics ER はエージェント機能も備えています。複雑なタスクをサブタスクに分割し、ロボット関数を呼び出すか、生成されたコードを実行してサブタスクを実行します。たとえば、「りんごをボウルに入れて」という指示は、見つける、つかむ、置くという一連のステップになります。

Gemini がツール呼び出しを実行する方法の詳細については、[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=ja#how-it-works)をご覧ください。

## 安全性

Gemini Robotics ER は安全性を考慮して構築されていますが、ロボットの周囲の安全な環境を維持するのはお客様の責任です。生成 AI モデルは間違えることがあり、物理的なロボットは損傷を引き起こす可能性があります。詳しくは、[Google DeepMind のロボット工学の安全性に関するページ](https://deepmind.google/models/gemini-robotics/safety?hl=ja)をご覧ください。

## ベスト プラクティス

1. 平易で自然な言葉を使用します。ロボットに何をしてほしいかを、人に説明するのと同じように記述します。用語が機能しない場合は、一般的な同義語を試してください。
2. 視覚的な入力を最適化します。画像を送信する前に、小さくて不鮮明な対象物を切り抜くか、拡大します。照明や色のコントラストが低いと、検出に影響する可能性があります。
3. 複雑なタスクをステップに分割します。各ステップを個別のプロンプトとして送信して、モデルの焦点を絞り、精度を高めます。
4. 高精度のタスクでは、複数回クエリを実行して結果を平均します。このコンセンサス アプローチにより、空間出力の分散が減少します。

## 制限事項

Gemini Robotics ER を使用して開発する場合は、次の制限事項を考慮してください。

- **API キーの制限:** Gemini API は、制限のない API キーからのリクエストを受け付けず、`403 Forbidden` エラーを返します。[AI Studio](https://aistudio.google.com/api-keys?hl=ja) で制限を追加して、API キーを保護します。詳細については、[制限のない API キーを保護する](https://ai.google.dev/gemini-api/docs/api-key?hl=ja#secure-unrestricted-keys)をご覧ください。
- **レイテンシとパフォーマンス:** 複雑なクエリ、高解像度の入力、高度な思考レベルは、処理時間の増加につながる可能性があります。思考レベルには、レイテンシとパフォーマンスのバランスが取れた中を使用します。
- **ハルシネーション:** すべての大規模言語モデルと同様に、Gemini Robotics ER モデルも、特に曖昧なプロンプトや分布外の入力に対して、ハルシネーションを起こしたり、誤った情報を提供したりすることがあります。
- **プロンプトの品質に依存:** 出力の品質は、入力プロンプトの明瞭さに依存します。具体的で構造化されたプロンプトを使用します。
- **コンピューティング費用:** モデルを実行すると、特に動画入力や高い `thinking_budget` を使用すると、コンピューティング リソースが消費され、費用が発生します。詳細については、[思考](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ja)のページをご覧ください。
- **入力タイプ:** 各モードの制限事項について詳しくは、以下のトピックをご覧ください。
  - [画像入力](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=ja#technical-details-image)
  - [ビデオ入力](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ja#supported-formats)
  - [音声入力](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=ja#supported-formats)

## プライバシーに関するお知らせ

お客様は、このドキュメントで言及されているモデル（以下「ロボティクス モデル」）が、お客様の指示に従ってハードウェアを操作し、移動させるために動画データと音声データを活用することを理解し、これに同意するものとします。そのため、音声、画像、肖像データなどの個人を特定できる人物のデータ（「個人データ」）がロボット モデルによって収集されるように、ロボット モデルを操作することがあります。個人データを収集する形でロボット モデルを運用することを選択した場合、Gemini API の追加利用規約（[https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=ja)）に記載されているとおり、Google に個人データが提供され、Google がそれを使用する可能性があることを、識別可能な人物に十分に通知し、その人物が同意するまで、その人物がロボット モデルとやり取りしたり、ロボット モデルの周囲に立ち入ったりすることを許可しないことに同意するものとします。これには、「Google によるデータの使用方法」というセクションに記載されている内容も含まれます。お客様は、かかる通知が本規約に記載されているとおりの個人データの収集と使用を許可することを保証し、顔のぼかしなどの技術を使用したり、識別可能な人物が含まれないエリアでロボティクス モデルを運用したりするなど、商業上合理的な努力をもって、個人データの収集と配布を可能な限り最小限に抑えます。

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
| calendar\_month最終更新日 | 2026 年 7 月 |
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
| calendar\_month最終更新日 | 2026 年 7 月 |
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
| calendar\_month最終更新日 | 2025 年 12 月 |
| cognition\_2ナレッジ カットオフ | 2025 年 1 月 |

## 次のステップ

- [空間推論](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=ja) - ポインティング、トラッキング、境界ボックス、軌跡。
- [エージェント機能](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=ja) - コード実行、計測器の読み取り、画像アノテーション。
- [タスク オーケストレーション](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=ja) - カスタム ロボット API を使用した長期的なタスク。
- [ストリーミングを使用したロボティクス](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ja) - リアルタイム双方向ストリーミング（Gemini Robotics ER 2 のみ）。
- [動画の理解](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=ja) - 瞬間検出と進捗状況の分類（Gemini Robotics ER 2 のみ）。
- [Google DeepMind のロボット工学の安全性](https://deepmind.google/models/gemini-robotics/safety?hl=ja) - モデル ファミリーの背後にある安全性研究。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-08 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-08 UTC。"],[],[]]
