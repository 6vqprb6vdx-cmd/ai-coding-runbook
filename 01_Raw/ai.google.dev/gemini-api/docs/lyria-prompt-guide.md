---
source_url: https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=zh-CN
fetched_at: 2026-09-28T06:23:57.600837+00:00
title: "Lyria \u63d0\u793a\u6307\u5357 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Lyria 提示指南

Gemini API 提供了两种使用 Lyria 生成音乐的方式：

- **Lyria 3.5 和 Lyria 3 Clip**：非流式生成，可生成 30 秒的片段或包含歌词和人声的完整歌曲。请参阅[使用 Lyria 3.5 生成音乐](https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-cn)。
- **Lyria RealTime**：通过 WebSocket 进行实时交互式音乐流式传输和实时控制。请参阅[使用 Lyria RealTime 实时生成音乐](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=zh-cn)。

这两个模型都能响应描述性文本提示、音乐术语和结构指令。本指南介绍了如何为批量生成和实时引导撰写有效的提示。

## 提示基础知识

您的提示可以是简短的短语：

```
A folk song about cute cats avoiding puddles, female vocals, acoustic guitar, sound of rain
```

或者，结构化的详细说明：

```
A 1980s-style synth-pop track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. The song should have a retro-futuristic feel with modern production polish. Upbeat tempo around 120 BPM, clear verse-chorus structure, and a memorable instrumental hook. The lyrics describe getting ready for a party.
```

无论是简短的提示还是详细的提示，都能产生出色的结果。使用以下策略引导模型生成您想要的精确声音。

## 流派和风格

在提示中先指定主要音乐类型。您可以组合多种流派，打造独特的混合流派：

- 金属乐和嘻哈音乐的融合
- 死亡金属与歌剧唱腔的结合
- 包含暗黑电子无人机元素的古典室内乐
- 将现代电子舞曲 (EDM) 与欧陆流行音乐相融合

您还可以指定音乐时代或地区变体：

- 20 世纪 90 年代初的 boom-bap 嘻哈音乐
- 20 世纪 60 年代法国耶耶流行乐
- 20 世纪 80 年代的后朋克和新浪潮
- 2000 年代主流 R&B
- 柏林极简高科技舞曲或湾区 hyphy

### 流派关键字

在 Lyria 3.5 和 Lyria RealTime 的提示中使用以下公认的音乐流派术语：

- **电子音乐和舞曲**：`Acid House, Breakbeat, Chillout, Chiptune, Deep House, Drum & Bass, Dubstep, EDM, Electro Swing, Glitch Hop, Hyperpop, Minimal Techno, Moombahton, Psytrance, Synthpop, Techno, Trance, Trip Hop, Vaporwave`
- **嘻哈音乐和 R&B**：`808 Hip Hop, Boom-Bap, Contemporary R&B, G-funk, Grime, Lo-Fi Hip Hop, Neo-Soul, New Jack Swing, Trap Beat`
- **摇滚和另类**：`Alternative Country, Blues Rock, Classic Rock, Funk Metal, Garage Rock, Indie Folk, Indie Pop, Post-Punk, 60s Psychedelic Rock, Shoegaze, Surf Rock`
- **爵士、灵魂和放克音乐**：`Acid Jazz, Afrobeat, Bossa Nova, Disco Funk, Funk, Jazz Fusion, Latin Jazz`
- **民谣与传统音乐**：`Bengal Baul, Bhangra, Bluegrass, Celtic Folk, Cumbia, Indian Classical, Irish Folk, Merengue, Polka, Reggae, Reggaeton, Renaissance Music, Salsa`
- **古典和原声**：`Baroque, Orchestral Score, Piano Ballad`

## 乐器和纹理

Lyria 会自动为所请求的音乐类型选择合适的乐器。如果您需要特定乐器或不寻常的组合，请明确声明：

```
A dance track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. A saxophone solo enters during the bridge.
```

描述乐器的声音和互动方式，以营造氛围和质感：

- 失真的 303 低音线穿透清脆紧凑的踩镲
- 温暖的模拟合成器柔音在干燥、亲切的原声吉他下方逐渐增强
- 由多层模糊吉他打造的音墙，搭配遥远而充满混响的人声

### 插桩关键字

- **键盘和合成器**：`Buchla Synths, Clavichord, Dirty Synths, Harpsichord, Mellotron, Moog Oscillations, Ragtime Piano, Rhodes Piano, Smooth Pianos, Spacey Synths, Synth Pads`
- **贝斯和鼓**：`303 Acid Bass, 808 Hip Hop Beat, Boomy Bass, Conga Drums, Drumline, Funk Drums, Precision Bass, Tabla, TR-909 Drum Machine`
- **吉他和琴弦**：`Banjo, Balalaika, Bouzouki, Cello, Charango, Dulcimer, Fiddle, Flamenco Guitar, Guitar, Harp, Koto, Lyre, Mandolin, Pipa, Shamisen, Shredding Guitar, Sitar, Slide Guitar, Viola Ensemble, Warm Acoustic Guitar`
- **管乐和铜管乐**：`Alto Saxophone, Bagpipes, Bass Clarinet, Didgeridoo, Harmonica, Ocarina, Trumpet, Tuba, Woodwinds`
- **打击乐**：`Bongos, Djembe, Glockenspiel, Hang Drum, Kalimba, Maracas, Marimba, Mbira, Steel Drum, Vibraphone`

## 歌曲结构和时间安排

对于 Lyria 3.5，请使用标记或箭头定义歌曲进度：

- `[Intro] -> [Verse 1] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Bridge] -> [Outro]`
- 以舒缓的钢琴前奏开场，逐渐过渡到充满活力的主歌，暂停片刻，然后爆发到合唱部分。

您可以指导能量动态和转变：

- 通过副歌前的部分营造紧张感，然后在爆发性的副歌之前突然静音
- 歌曲中逐渐增强的渐强，每个乐段增加一种乐器
- 桥段后突然停止，然后是无伴奏合唱

您还可以提示特定时间标记：

- 在 12 秒时达到高潮
- 人声样本每 4 小节重复一次
- 合唱部分从第 22 秒开始

## 歌词和人声

Lyria 3.5 默认生成带有歌词的人声轨道。您可以提供自己的歌词，也可以让模型生成歌词，还可以请求提供伴奏曲目。

### 使用您自己的歌词

在 `Lyrics:` 标题下方的提示中直接添加歌词。为每个部分添加标记，以指导语音播报：

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

使用圆括号表示和声、回声或即兴演唱，例如 `(moving on)`。

### 指导生成的歌词

让 Lyria 3.5 撰写歌词时，请提供叙事、情感或关键短语的大纲：

```
The lyrics describe driving down the Pacific Coast Highway at sunset. The mood is nostalgic and reflective. Include an uplifting, anthemic chorus about second chances and starting over.
```

对于电子音乐和舞曲，请要求提供简短的重复人声钩子：

```
An upbeat dance-pop track with a repetitive, high-energy vocal hook: "Feel the rhythm all night long."
```

### 人声演绎和歌手个人资料

指定性别、音域和音色，以便实现精准的朗读效果：

- **女高音**：音色清澈透亮，演唱灵活而高亢。明亮音调，可营造出空灵、气声质感。
- **女低音**：低音浑厚、温暖、沙哑。烟嗓，胸腔共鸣，深情而富有磁性。
- **男高音**：明亮、穿透力强、充满活力。音色年轻，高音穿透力强，可穿透密集混音。
- **男中音**：深沉、丝滑的胸腔共鸣，温暖、舒缓、低吟浅唱。
- **风化摇滚**：沙哑、粗犷的音色，让人想起 20 世纪 90 年代的另类摇滚。原始的情感强度，高音略显紧张。

### 非歌词人声效果

您还可以提示生成对话、人声切片和采样效果：

- 在节拍开始之前，老式电台广播的声音介绍了这首歌
- 在音乐高潮前，人声低语，随后是动感十足的合成器
- 切分、变调的人声采样循环播放，作为乐器节奏元素

## 音乐参数

使用标准音乐属性优化提示：

- **速度 (BPM)**：直接设置速度（例如 `120 BPM`、`slow tempo around 72 BPM`、`fast 160 BPM`）。
- **调和音阶**：指定根音和调性（例如 `in G major`、`in D minor`、`in C pentatonic`）。
- **曲调和氛围**：使用描述情感的形容词：
  `Ambient, Bright, Chill, Dark, Dreamy, Emotional, Ethereal, Euphoric, Funky, Groovy, Melancholic, Nostalgic, Ominous, Psychedelic, Relaxed, Soulful, Triumphant, Upbeat, Whimsical`

## 为 Lyria RealTime 提供提示

Lyria RealTime 使用**加权提示**，而不是单个整体提示字符串。这样一来，您就可以动态融合多种音乐风格，并通过 WebSocket 连接持续引导音乐。

### 加权提示结构

每个加权提示都包含一段描述性文字短语和一个浮点权重：

```
prompts = [
    types.WeightedPrompt(text="minimal techno", weight=1.0),
    types.WeightedPrompt(text="deep sub bass", weight=0.6),
    types.WeightedPrompt(text="shimmering hi-hats", weight=0.4),
]
```

### 实时转向策略

- **混合流派**：通过分配均衡的权重来混合不同的风格：
  - `ambient synth pads (weight: 0.8)` + `lo-fi hip-hop drums (weight: 0.6)`
  - `flamenco guitar (weight: 0.7)` + `deep house groove (weight: 0.5)`
- **动态过渡**：为了让音乐平稳过渡，请随时间调整提示权重：
  1. 以 `chill jazz piano (weight: 1.0)` 开头的链。
  2. 逐步添加 `electronic breakbeat (weight: 0.3)`。
  3. 将 `electronic breakbeat` 提高到 `0.8`，同时将 `chill jazz piano` 降低到 `0.3`。
- **分层元素**：将乐器标记和情绪标记分开，以便单独调整它们：
  - 提示 1：`bossa nova guitar (weight: 0.9)`
  - 提示 2：`warm acoustic bass (weight: 0.7)`
  - 提示 3：`subtle vinyl crackle (weight: 0.3)`

## 示例提示

### Lyria 3.5 示例

- **Lo-Fi Study Beat**：
  `none
  A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes piano chords, a relaxed boom-bap drum groove at 82 BPM, and a warm upright bassline. Instrumental only.`
- **流行国歌**：
  `none
  An upbeat, feel-good indie-pop song in G major at 122 BPM. Bright acoustic guitar strumming, driving kick drum, handclaps, and warm female vocal harmonies. The lyrics describe an unforgettable summer road trip with friends.`
- **Cinematic Cyberpunk**：
  `none
  Dark, cinematic cyberpunk synthwave at 110 BPM in D minor. Heavy distorted bass, ominous arpeggiated analog synthesizers, distant metallic percussion, and an ethereal female vocalise swelling during the climax.`

### Lyria RealTime 指向性设置

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

## 后续步骤

- [使用 Lyria 3.5 生成音乐](https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-cn)：使用 Interactions API 生成完整歌曲和 30 秒的片段。
- [使用 Lyria RealTime 实时音乐创作](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=zh-cn)：通过 WebSocket 构建实时交互式音乐串流应用。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-18。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-18。"],[],[]]
