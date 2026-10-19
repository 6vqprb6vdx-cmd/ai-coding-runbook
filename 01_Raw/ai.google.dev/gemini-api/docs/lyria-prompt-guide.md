---
source_url: https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=ja
fetched_at: 2026-10-19T05:43:57.702624+00:00
title: "Lyria \u30d7\u30ed\u30f3\u30d7\u30c8 \u30ac\u30a4\u30c9 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Lyria プロンプト ガイド

Gemini API には、Lyria で音楽を生成する 2 つの方法があります。

- **Lyria 3.5 と Lyria 3 Clip**: 30 秒のクリップまたは歌詞とボーカルを含むフルレングスの楽曲をストリーミングなしで生成します。[Lyria 3.5 で音楽を生成する](https://ai.google.dev/gemini-api/docs/music-generation?hl=ja)をご覧ください。
- **Lyria RealTime**: WebSocket 経由のリアルタイムのインタラクティブな音楽ストリーミングとライブ ステアリング。[Lyria RealTime によるリアルタイムの音楽生成](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ja)をご覧ください。

どちらのモデルも、説明的なテキスト プロンプト、音楽用語、構造的な指示に応答します。このガイドでは、バッチ生成とリアルタイム ステアリングの両方で効果的なプロンプトを作成する方法について説明します。

## プロンプトの基本

プロンプトは短いフレーズにすることができます。

```
A folk song about cute cats avoiding puddles, female vocals, acoustic guitar, sound of rain
```

または、構造化された詳細な説明:

```
A 1980s-style synth-pop track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. The song should have a retro-futuristic feel with modern production polish. Upbeat tempo around 120 BPM, clear verse-chorus structure, and a memorable instrumental hook. The lyrics describe getting ready for a party.
```

短いプロンプトと詳細なプロンプトのどちらでも、優れた結果が得られます。次の戦略を使用して、モデルを目的のサウンドに導きます。

## ジャンルとスタイル

プロンプトの先頭にメインのジャンルを入力します。ジャンルを組み合わせて、独自のハイブリッドを作成できます。

- メタルとヒップホップの融合
- デス メタルとオペラ調のボーカルを組み合わせた音楽
- クラシックな室内楽にダークなエレクトロニック ドローン要素を加えた音楽
- モダンなエレクトロニック ダンス ミュージック（EDM）とユーロポップをミックス

音楽の時代や地域バリエーションを指定することもできます。

- 1990 年代初頭のブームバップ ヒップホップ
- 1960 年代のフランスのイエイエ ポップ
- 1980 年代のポストパンクとニューウェーブ
- 2000 年代のメインストリーム R&B
- ベルリンのミニマル テクノか、ベイエリアのハイフィー

### ジャンルのキーワード

Lyria 3.5 と Lyria RealTime のプロンプトでは、次のジャンル用語を使用できます。

- **エレクトロニック＆ダンス**: `Acid House, Breakbeat, Chillout, Chiptune, Deep House, Drum & Bass, Dubstep, EDM, Electro Swing, Glitch Hop, Hyperpop, Minimal Techno, Moombahton, Psytrance, Synthpop, Techno, Trance, Trip Hop, Vaporwave`
- **ヒップホップ、R&B**: `808 Hip Hop, Boom-Bap, Contemporary R&B, G-funk, Grime, Lo-Fi Hip Hop, Neo-Soul, New Jack Swing, Trap Beat`
- **ロックとオルタナティブ**: `Alternative Country, Blues Rock, Classic Rock, Funk Metal, Garage Rock, Indie Folk, Indie Pop, Post-Punk, 60s Psychedelic Rock, Shoegaze, Surf Rock`
- **ジャズ、ソウル、ファンク**: `Acid Jazz, Afrobeat, Bossa Nova, Disco Funk, Funk, Jazz Fusion, Latin Jazz`
- **フォーク＆トラディショナル**: `Bengal Baul, Bhangra, Bluegrass, Celtic Folk, Cumbia, Indian Classical, Irish Folk, Merengue, Polka, Reggae, Reggaeton, Renaissance Music, Salsa`
- **クラシック & アコースティック**: `Baroque, Orchestral Score, Piano Ballad`

## 楽器とテクスチャー

Lyria は、リクエストされたジャンルに適切な楽器を自動的に選択します。特定の楽器や珍しい組み合わせが必要な場合は、明示的に宣言します。

```
A dance track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. A saxophone solo enters during the bridge.
```

楽器の音と相互作用を説明して、ムードとテクスチャを設定します。

- 歪んだ 303 ベースラインが、歯切れのよいタイトなハイハットを切り裂く
- 暖かく親しみのあるアコースティック ギターの下で、アナログ シンセパッドが盛り上がっていく
- 複数のファズギターのレイヤーで構築された音の壁と、遠くでリバーブが効いたボーカル

### インストゥルメント キーワード

- **キーボードとシンセサイザー**: `Buchla Synths, Clavichord, Dirty Synths, Harpsichord, Mellotron, Moog Oscillations, Ragtime Piano, Rhodes Piano, Smooth Pianos, Spacey Synths, Synth Pads`
- **Bass & Drums**: `303 Acid Bass, 808 Hip Hop Beat, Boomy Bass, Conga Drums, Drumline, Funk Drums, Precision Bass, Tabla, TR-909 Drum Machine`
- **ギターと弦**: `Banjo, Balalaika, Bouzouki, Cello, Charango, Dulcimer, Fiddle, Flamenco Guitar, Guitar, Harp, Koto, Lyre, Mandolin, Pipa, Shamisen, Shredding Guitar, Sitar, Slide Guitar, Viola Ensemble, Warm Acoustic Guitar`
- **Wind & Brass**: `Alto Saxophone, Bagpipes, Bass Clarinet, Didgeridoo, Harmonica, Ocarina, Trumpet, Tuba, Woodwinds`
- **パーカッション**: `Bongos, Djembe, Glockenspiel, Hang Drum, Kalimba, Maracas, Marimba, Mbira, Steel Drum, Vibraphone`

## 曲の構成とタイミング

Lyria 3.5 では、タグまたは矢印を使用して曲の進行を定義します。

- `[Intro] -> [Verse 1] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Bridge] -> [Outro]`
- 静かなピアノのイントロから始まり、エネルギッシュなバースへと展開し、一瞬の静寂を挟んで、サビへと爆発的に盛り上がります。

エネルギーのダイナミクスと移行を指示できます。

- プリコーラスで緊張感を高め、コーラスの直前に静寂に落とす
- 曲全体を通して徐々にクレッシェンドし、セクションごとに楽器を追加する
- ブリッジの後の突然の停止、アカペラのコーラス

特定のタイミング マーカーを求めることもできます。

- 12 秒でビートがドロップするようビルドする
- 歌声のサンプルが 4 小節ごとに繰り返される
- 22 秒でサビが始まる

## 歌詞とボーカル

Lyria 3.5 は、デフォルトで歌詞付きのボーカル トラックを生成します。独自の歌詞を指定したり、モデルに歌詞の生成を依頼したり、インストゥルメンタル トラックをリクエストしたりできます。

### 独自の歌詞を使用する

`Lyrics:` ヘッダーの下のプロンプトに歌詞を直接含めます。各セクションにタグを付けて、音声の配信をガイドします。

```
Lyrics:

[Intro]
Ooooh, yeah

[Verse 1]
Early morning rain on the window pane
City lights wash away the pain
Walking down this empty street again

[Chorus]
We keep moving on (moving on)
Until the morning light
Everything will be alright
```

バッキング ボーカル、エコー、アドリブには、`(moving on)` のようにかっこを使用します。

### 生成された歌詞の指示

Lyria 3.5 に歌詞の作成を依頼する場合は、物語、感情、キーフレーズの概要を説明します。

```
The lyrics describe driving down the Pacific Coast Highway at sunset. The mood is nostalgic and reflective. Include an uplifting, anthemic chorus about second chances and starting over.
```

エレクトロニックやダンスのジャンルでは、短いボーカル フックの繰り返しをリクエストします。

```
An upbeat dance-pop track with a repetitive, high-energy vocal hook: "Feel the rhythm all night long."
```

### ボーカルの配信と歌手のプロフィール

正確な配信のために、性別、音域、音色を指定します。

- **女性ソプラノ**: 澄んだクリスタルのような音色で、軽快で伸びのある歌声。軽やかで息遣いのあるテクスチャを表現できる明るいトーン。
- **女性アルト**: 豊かで温かみのあるハスキーな低音域。スモーキーな音色と、ソウルフルで響きのあるチェスト ボイス。
- **男性テノール**: 明るく、鋭く、エネルギッシュ。若々しい音色と、密度の高いミックスを突き抜ける高いベルティング パワー。
- **男性バリトン**: 深く、ベルベットのように滑らかな胸声で、温かく、心地よく、クルーニングのような歌い方。
- **Weathered Rocker**: 1990 年代のオルタナティブ ロックを彷彿とさせる、かすれたざらざらした音色。感情の強さがむき出しで、高音は張り詰めている。

### 歌詞のないボーカル エフェクト

会話、ボーカル チョップ、サンプリング効果を求めることもできます。

- ビンテージ ラジオ放送の音声が曲を紹介してからビートが始まる
- ドロップの直前にささやくような音声が流れ、続いてエネルギッシュなシンセサイザーの音が流れます
- 楽器のリズム要素としてループする、チョップされピッチシフトされたボーカル サンプル

## 音楽パラメータ

標準の音楽プロパティを使用してプロンプトを調整します。

- **テンポ（BPM）**: テンポを直接設定します（`120 BPM`、`slow tempo around 72 BPM`、`fast 160 BPM` など）。
- **キーとスケール**: ルートキーと調性（`in G major`、`in D minor`、`in C pentatonic` など）を指定します。
- **ムードと雰囲気**: 説明的な感情を表す形容詞を使用します。
  `Ambient, Bright, Chill, Dark, Dreamy, Emotional, Ethereal, Euphoric, Funky, Groovy, Melancholic, Nostalgic, Ominous, Psychedelic, Relaxed, Soulful, Triumphant, Upbeat, Whimsical`

## Lyria RealTime のプロンプト

Lyria RealTime は、単一のモノリシックなプロンプト文字列ではなく、**重み付けされたプロンプト**を使用します。これにより、複数の音楽的影響を動的にブレンドし、WebSocket 接続を介して音楽を継続的に操作できます。

### 重み付けされたプロンプト構造

重み付けされた各プロンプトは、説明的なテキスト フレーズと浮動小数点数の重みで構成されます。

```
prompts = [
    types.WeightedPrompt(text="minimal techno", weight=1.0),
    types.WeightedPrompt(text="deep sub bass", weight=0.6),
    types.WeightedPrompt(text="shimmering hi-hats", weight=0.4),
]
```

### リアルタイムのステアリング戦略

- **ジャンルのブレンド**: バランスの取れた重みを割り当てることで、異なるスタイルをブレンドします。
  - `ambient synth pads (weight: 0.8)` + `lo-fi hip-hop drums (weight: 0.6)`
  - `flamenco guitar (weight: 0.7)` + `deep house groove (weight: 0.5)`
- **動的なトランジション**: 音楽をスムーズにトランジションするには、プロンプトの重みを時間とともに調整します。
  1. `chill jazz piano (weight: 1.0)` で始まるチェーン。
  2. `electronic breakbeat (weight: 0.3)` を徐々に追加します。
  3. `electronic breakbeat` を `0.8` に増やし、`chill jazz piano` を `0.3` に減らします。
- **要素のレイヤリング**: 楽器タグとムードタグを別々に保持して、個別に調整できるようにします。
  - プロンプト 1: `bossa nova guitar (weight: 0.9)`
  - プロンプト 2: `warm acoustic bass (weight: 0.7)`
  - プロンプト 3: `subtle vinyl crackle (weight: 0.3)`

## プロンプトの例

### Lyria 3.5 の例

- **Lo-Fi Study Beat**:
  `none
  A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes piano chords, a relaxed boom-bap drum groove at 82 BPM, and a warm upright bassline. Instrumental only.`
- **ポップ アンセム**:
  `none
  An upbeat, feel-good indie-pop song in G major at 122 BPM. Bright acoustic guitar strumming, driving kick drum, handclaps, and warm female vocal harmonies. The lyrics describe an unforgettable summer road trip with friends.`
- **シネマティック サイバーパンク**:
  `none
  Dark, cinematic cyberpunk synthwave at 110 BPM in D minor. Heavy distorted bass, ominous arpeggiated analog synthesizers, distant metallic percussion, and an ethereal female vocalise swelling during the climax.`

### Lyria RealTime ステアリング セット

```
# Initial high-energy groove
await session.set_weighted_prompts(
    prompts=[
        types.WeightedPrompt(text="techno groove", weight=1.0),
        types.WeightedPrompt(text="acid 303 bass", weight=0.8),
    ]
)

# Transition to a melodic breakdown
await session.set_weighted_prompts(
    prompts=[
        types.WeightedPrompt(text="ambient synth pads", weight=1.0),
        types.WeightedPrompt(text="subtle reverberant piano", weight=0.7),
        types.WeightedPrompt(text="techno groove", weight=0.2),
    ]
)
```

## 次のステップ

- [Lyria 3.5 で音楽を生成する](https://ai.google.dev/gemini-api/docs/music-generation?hl=ja): Interactions API を使用して、フルソングと 30 秒のクリップを生成します。
- [Lyria RealTime によるリアルタイムの音楽生成](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ja): WebSocket 経由でリアルタイムのインタラクティブな音楽ストリーミング アプリケーションを構築します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-18 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-18 UTC。"],[],[]]
