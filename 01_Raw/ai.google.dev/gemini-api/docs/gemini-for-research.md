---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=ja
fetched_at: 2026-07-06T05:21:21.851185+00:00
title: "Gemini for Research \u3067\u767a\u898b\u3092\u52a0\u901f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)

# Gemini for Research で発見を加速

[Gemini API キーを取得する](https://aistudio.google.com/apikey?hl=ja)

Gemini モデルは、さまざまな分野の基礎研究を進めるために使用できます。
Gemini を研究に活用する方法は次のとおりです。

- **モデルの出力を分析して制御する**: さらに分析するために、
  モデルによって生成されたレスポンス候補を
  `CitationMetadata`使用して調べることができます。また、`responseSchema`、`topP`、`topK` など、モデルの生成と出力のオプションを構成することもできます。[詳細](https://ai.google.dev/api/generate-content?hl=ja)
- **マルチモーダル入力**: Gemini は画像、音声、動画を処理できるため、さまざまな研究の方向性を探ることができます。[詳細](https://ai.google.dev/gemini-api/docs/vision?hl=ja)
- **長いコンテキスト機能**: Gemini 3.0 Flash と Pro には、100 万トークンの
  コンテキスト ウィンドウが搭載されています。[詳細](https://ai.google.dev/gemini-api/docs/long-context?hl=ja)
- **Grow with Google**: API と Google AI
  Studio を使用して、本番環境のユースケース向けに Gemini モデルにすばやくアクセスできます。Google Cloud ベースのプラットフォームをお探しの場合は、Gemini Enterprise Agent Platform で追加のサポート インフラストラクチャを利用できます。

学術研究をサポートし、最先端の研究を推進するため、Google は
Gemini Academic Programを通じて、科学者や学術研究者に Gemini API クレジットへの
[アクセスを提供しています。](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=ja#gemini-academic-program)

## Gemini を使ってみる

Gemini API と Google AI Studio を使用すると、Google の最新モデルを使い始め、アイデアをスケーラブルなアプリケーションに変えることができます。

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## 注目の学術研究者

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=ja)

「私たちの研究では、Gemini をビジュアル言語モデル（VLM）として調査し、堅牢性と安全性の観点から、さまざまな環境におけるエージェントの動作を調査しています。これまでのところ、VLM エージェントがコンピュータ タスクを実行する際にポップアップ ウィンドウなどの妨害に対する Gemini の堅牢性を評価し、Gemini を活用してソーシャル インタラクション、時間的イベント、動画入力に基づくリスク要因を分析しています。」

[Diyi Yang のウェブサイト](https://cs.stanford.edu/~diyiy/)

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=ja)

「Gemini Pro と Flash は、長いコンテキスト ウィンドウを備えているため、オープンボキャブラリー モバイル操作プロジェクトである OK-Robot で役立っています。Gemini を使用すると、ロボットの「メモリ」（この場合は、ロボットが長期間の操作で取得した過去の観測）に対して、複雑な自然言語クエリとコマンドを実行できます。Mahi Shafiullah と私も Gemini を使用して、タスクをロボットが現実世界で実行できるコードに分解しています。」

[Lerrel Pinto のウェブサイト](https://www.lerrelpinto.com/)

## Gemini Academic Program

[対象国の資格のある学術研究者（教員、職員、博士課程の学生など）は、研究プロジェクトで Gemini API
クレジットと上限の引き上げを申請できます。](https://ai.google.dev/gemini-api/docs/available-regions?hl=ja)このサポートにより、科学実験のスループットが向上し、研究が進みます。

特に、次のセクションの研究分野に関心がありますが、さまざまな科学分野からの応募を歓迎します。

- **評価とベンチマーク**: 事実性、安全性、
  指示の遵守、推論、プランニングなどの分野で強力なパフォーマンス シグナルを提供できる、
  コミュニティで承認された評価方法。
- **科学的発見を加速して人類に貢献する**: 希少疾患や顧みられない病気、実験生物学、材料科学、持続可能性など、学際的な科学研究における AI の潜在的な応用。
- **具現化とインタラクション**: 大規模言語モデルを活用して、具現化された AI、アンビエント インタラクション、ロボット工学、人間とコンピュータのインタラクションの分野で新しいインタラクションを調査する。
- **創発的な機能**: 推論とプランニングを強化するために必要な新しいエージェント機能を調査し、推論中に機能を拡張する方法（Gemini Flash の活用など）。
- **マルチモーダルなインタラクションと理解**: 分析、推論、
  さまざまなタスクでプランニングを行うためのマルチモーダル基盤モデルのギャップと
  機会を特定する。

対象者: 有効な学術機関または学術研究機関に所属する個人（教員、研究者、または同等の者）のみが申請できます。API アクセスとクレジットは、Google の裁量で付与および削除されます。お申し込みは毎月審査されます。

### Gemini API を使用して研究を開始する

[今すぐ申し込む](https://forms.gle/HMviQstU8PxC5iCt5)

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-01 UTC。

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-01 UTC。"],[],[]]
