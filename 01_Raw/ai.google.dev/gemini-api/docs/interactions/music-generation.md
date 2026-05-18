---
source_url: https://ai.google.dev/gemini-api/docs/interactions/music-generation?hl=ja
fetched_at: 2026-05-18T13:01:13.268342+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Lyria 3 で音楽を生成する

Lyria 3 は、Gemini API を介して利用できる Google の音楽生成モデル ファミリーです。Lyria 3 を使用すると、テキスト プロンプトや画像から、高音質の 44.1 kHz ステレオ音声を生成できます。これらのモデルは、ボーカル、タイミング付きの歌詞、完全な楽器編成など、構造的な一貫性を提供します。

Lyria 3 ファミリーには次の 2 つのモデルがあります。

| モデル | モデル ID | 最適な用途 | 所要時間 | 出力 |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | 短いクリップ、ループ、プレビュー | 30 秒 | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | A メロ、サビ、ブリッジを含むフルレングスの曲 | 数分（プロンプトで制御可能） | MP3 |

どちらのモデルも新しい [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ja) を使用して利用でき、
マルチモーダル入力（テキストと画像）をサポートし、**44.1 kHz
の高忠実度ステレオ** 音声を生成します。

## 音楽クリップを生成する

Lyria 3 Clip モデルは常に **30 秒** のクリップを生成します。クリップを生成するには、テキスト プロンプトを指定して `interactions.create` メソッドを呼び出します。レスポンスには常に、生成された歌詞と曲の構成が `steps` スキーマの音声とともに含まれます。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                print(f"Generated audio with mime_type: {content_block.mime_type}")
                with open("music.mp3", "wb") as f:
                    f.write(base64.b64decode(content_block.data))
            elif content_block.type == "text":
                print(f"Lyrics: {content_block.text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                console.log(`Generated audio with mime_type: ${contentBlock.mime_type}`);
                fs.writeFileSync('music.mp3', Buffer.from(contentBlock.data, 'base64'));
            } else if (contentBlock.type === 'text') {
                console.log(`Lyrics: ${contentBlock.text}`);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "Api-Revision: 2026-05-20" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

## フルレングスの曲を生成する

`lyria-3-pro-preview` モデルを使用して、数分間のフルレングスの曲を生成します。Pro モデルは音楽の構成を理解し、明確な A メロ、サビ、ブリッジを含む楽曲を作成できます。[プロンプトで期間を指定する（例: 「2 分間の曲を作成する」）か、
タイムスタンプ](#timing)を使用して構成を定義することで、期間に影響を与えることができます。

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "Api-Revision: 2026-05-20" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## 出力形式を選択する

デフォルトでは、Lyria 3 モデルは **MP3** 形式で音声を生成します。Lyria 3 Pro では、`response_format` を設定して **WAV** 形式で出力をリクエストすることもできます。

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## レスポンスをパースする

Lyria 3 からのレスポンスには、`steps` スキーマ内に複数のコンテンツ ブロックが含まれています。
インタラクションは一連のステップを返します。`model_output` ステップには生成されたコンテンツが含まれます。
テキスト コンテンツ ブロックには、生成された歌詞または曲の構成の JSON 説明が含まれます。
`audio` タイプのコンテンツ ブロックには、Base64 エンコードされた音声データが含まれます。

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

## 画像から音楽を生成する

Lyria 3 はマルチモーダル入力をサポートしています。`input` リストにテキスト プロンプトとともに最大 **10 個の画像** を指定すると、モデルはビジュアル コンテンツにインスパイアされた音楽を作成します。

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3-pro-preview",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### JavaScript

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3-pro-preview",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## カスタムの歌詞を指定する

独自の歌詞を作成して、プロンプトに含めることができます。`[Verse]`、`[Chorus]`、`[Bridge]` などのセクション タグを使用して、モデルが曲の構成を理解できるようにします。

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## タイミングと構成を制御する

タイムスタンプを使用して、曲の特定の瞬間に何が起こるかを正確に指定できます。これは、楽器の開始タイミング、歌詞の配信タイミング、曲の進行方法を制御するのに役立ちます。

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## インストゥルメンタル トラックを生成する

バックグラウンド ミュージック、ゲーム サウンドトラックなど、ボーカルが不要なユースケースでは、インストゥルメンタルのみのトラックを生成するようにモデルにプロンプトを表示できます。

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## さまざまな言語で音楽を生成する

Lyria 3 は、プロンプトの言語で歌詞を生成します。フランス語の歌詞を含む曲を生成するには、プロンプトをフランス語で記述します。モデルは、言語に合わせてボーカル スタイルと発音を調整します。

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## モデルのインテリジェンス

Lyria 3 は、プロンプトに基づいてモデルが音楽の構成（イントロ、A メロ、サビ、ブリッジなど）を推論するプロンプト プロセスを分析します。
これは音声が生成される前に行われ、構造的な一貫性と音楽性を確保します。

## プロンプト ガイド

プロンプトが具体的であるほど、より良い結果が得られます。生成をガイドするために含めることができる要素は次のとおりです。

- **ジャンル**: ジャンルまたはジャンルのブレンドを指定します（例: 「ローファイ ヒップホップ」、
  「ジャズ フュージョン」、「映画音楽のようなオーケストラ」）。
- **楽器**: 具体的な楽器の名前を指定します（例: 「フェンダー ローズ ピアノ」、
  「スライド ギター」、「TR-808 ドラムマシン」）。
- **BPM**: テンポを設定します（例: 「120 BPM」、「70 BPM 前後の遅いテンポ」）。
- **キー/スケール**: 音楽キーを指定します（例: 「ト長調」、「ニ短調」）。
- **ムードと雰囲気**: 説明的な形容詞を使用します（例: 「ノスタルジック」、
  「アグレッシブ」、「エーテル」、「夢のような」）。
- **構成**: `[Verse]`、`[Chorus]`、`[Bridge]`、`[Intro]`、
  `[Outro]`などのタグまたはタイムスタンプを使用して、曲の進行を制御します。
- **期間**: Clip モデルは常に 30 秒のクリップを生成します。Pro モデルの場合は、プロンプトで目的の長さを指定する（例: 「2 分間の曲を作成する」）か、タイムスタンプを使用して期間を制御します。

### プロンプトの例

効果的なプロンプトの例を次に示します。

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## ベスト プラクティス

- **最初に Clip で反復処理を行います。**より高速な `lyria-3-clip-preview` モデルを使用してプロンプトを試してから、`lyria-3-pro-preview` でフルレングスの生成を行います。
- **具体的に記述しましょう。**曖昧なプロンプトでは、一般的な結果しか得られません。最適な出力が得られるように、楽器、BPM、キー、ムード、構成を指定してください。
- **言語を一致させます。**歌詞に使用する言語でプロンプトを作成します。
- **セクション タグを使用します。**`[Verse]`、`[Chorus]`、`[Bridge]` タグを使用すると、モデルが従うべき明確な構造が提供されます。
- **歌詞と指示を分離します。**カスタムの歌詞を指定する場合は、音楽の方向に関する指示と明確に区別してください。

## 制限事項

- **安全性**: すべてのプロンプトは安全フィルタによってチェックされます。フィルタをトリガーするプロンプトはブロックされます。これには、特定のアーティストの音声や著作権で保護された歌詞の生成をリクエストするプロンプトが含まれます。
- **透かし**: 生成されたすべての音声には、識別用の
  [SynthID オーディオ ウォーターマーク](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=ja)が含まれています。この透かしは人間の耳には聞こえず、リスニング体験に影響しません。
- **複数ターンの編集**: 音楽生成は単一ターンのプロセスです。
  現在のバージョンの Lyria 3 では、複数のプロンプトを使用して生成されたクリップを反復的に編集または改良することはできません。
- **長さ**: Clip モデルは常に 30 秒のクリップを生成します。Pro モデルは数分間の曲を生成します。正確な期間はプロンプトで制御できます。
- **決定論**: 同じプロンプトでも、呼び出しごとに結果が異なる場合があります。

## 次のステップ

- Lyria 3 モデルの[料金](https://ai.google.dev/gemini-api/docs/interactions/pricing?hl=ja)を確認する。
- [リアルタイムのストリーミング音楽生成](https://ai.google.dev/gemini-api/docs/interactions/realtime-music-generation?hl=ja)
  を Lyria RealTime で試す。
- TTS モデルで複数の話者による会話を生成する
  。
- [[画像や動画を生成する方法を確認する。](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=ja)](https://ai.google.dev/gemini-api/docs/interactions/video?hl=ja)
- Gemini が音声ファイルを[理解する](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=ja)方法を確認する。
- [Live API を使用して Gemini とリアルタイムで会話する。](https://ai.google.dev/gemini-api/docs/interactions/live?hl=ja)

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-05-11 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-05-11 UTC。"],[],[]]
