---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=ko
fetched_at: 2026-06-29T05:37:33.376252+00:00
title: "Lyria 3\ub85c \uc74c\uc545 \uc0dd\uc131\ud558\uae30 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Lyria 3로 음악 생성하기

Lyria 3는 Gemini API를 통해 사용할 수 있는 Google의 음악 생성 모델 계열입니다. Lyria 3를 사용하면 텍스트 프롬프트 또는 이미지에서 고품질의 44.1kHz 스테레오 오디오를 생성할 수 있습니다. 이러한 모델은 보컬, 시간 지정 가사, 전체 악기 편곡을 비롯한 구조적 일관성을 제공합니다.

Lyria 3 계열에는 두 가지 모델이 포함됩니다.

| 모델 | 모델 ID | 권장 용도 | 기간 | 출력 |
| --- | --- | --- | --- | --- |
| **Lyria 3 클립** | `lyria-3-clip-preview` | 짧은 클립, 루프, 미리보기 | 30초 | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | 절, 코러스, 브리지가 포함된 전체 길이 노래 | 몇 분 (프롬프트를 사용하여 제어 가능) | MP3 |

두 모델 모두 새로운
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)를 사용하여 멀티모달
입력 (텍스트 및 이미지)을 지원하고 **44.1kHz 고음질 스테레오**
오디오를 생성할 수 있습니다.

## 뮤직 클립 생성

Lyria 3 클립 모델은 항상 **30초** 클립을 생성합니다. 클립을 생성하려면 텍스트 프롬프트로 `interactions.create` 메서드를 호출합니다. 응답에는 항상 `steps` 스키마의 오디오와 함께 생성된 가사와 노래 구조가 포함됩니다.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
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

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

`interaction.output_audio` 속성을 사용하여 생성된 음악 데이터를 검색할 수 있습니다. 이 속성은 마지막으로 생성된 오디오 블록을 반환합니다. `interaction.output_text` 속성을 사용하여 노래의 가사와 구조를 검색할 수도 있습니다. 편의 속성에 관한 자세한 내용은
[상호작용 개요](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko#convenience-properties)를 참고하세요.

## 전체 길이 노래 생성

`lyria-3-pro-preview` 모델을 사용하여 몇 분 동안 지속되는 전체 길이 노래를 생성합니다. Pro 모델은 음악 구조를 이해하고 고유한 절, 코러스, 브리지가 포함된 작곡을 만들 수 있습니다. [프롬프트에서 기간을 지정하거나 (예: "2분짜리 노래 만들기") 타임스탬프를 사용하여 구조를 정의하여 기간에 영향을 줄 수 있습니다.](#timing)

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
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## 출력 형식 선택

기본적으로 Lyria 3 모델은 **MP3** 형식으로 오디오를 생성합니다. Lyria 3 Pro의 경우 `response_format`을 설정하여 **WAV** 형식으로 출력을 요청할 수도 있습니다.

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
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## 응답 파싱

Lyria 3의 응답에는 `steps` 스키마 내에 여러 콘텐츠 블록이 포함되어 있습니다.
상호작용은 단계 시퀀스를 반환하며, `model_output` 단계에는 생성된 콘텐츠가 포함됩니다.
텍스트 콘텐츠 블록에는 생성된 가사 또는 노래 구조의 JSON 설명이 포함됩니다.
`audio` 유형의 콘텐츠 블록에는 base64로 인코딩된 오디오 데이터가 포함됩니다.

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### 인터리브 가사 및 음악

Lyria 3의 출력은 생성된 가사 (텍스트)와 노래 자체 (오디오)를 위한 별도의 단계와 블록을 포함하는 복잡한 출력이므로 편의 속성은 빠르고 권장되는 바로가기를 제공합니다.

하지만 서버에서 반환된 단계의 원시 타임라인을 프로그래매틱 방식으로 완전히 제어하려면 (예: 개별 콘텐츠 블록이 수신될 때 로깅) 대신 `steps`를 수동으로 반복할 수 있습니다.

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

## 이미지에서 음악 생성

Lyria 3는 멀티모달 입력을 지원합니다. `input` 목록에서 텍스트 프롬프트와 함께 최대 **10개의 이미지** 를 제공할 수 있으며 모델은 시각적 콘텐츠에서 영감을 받은 음악을 작곡합니다.

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
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## 맞춤 가사 제공

자체 가사를 작성하여 프롬프트에 포함할 수 있습니다. `[Verse]`, `[Chorus]`, `[Bridge]`와 같은 섹션 태그를 사용하여 모델이 노래 구조를 이해하도록 돕습니다.

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
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## 타이밍 및 구조 제어

타임스탬프를 사용하여 노래의 특정 순간에 발생하는 상황을 정확하게 지정할 수 있습니다. 이는 악기가 들어오는 시점, 가사가 전달되는 시점, 노래가 진행되는 방식을 제어하는 데 유용합니다.

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
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## 악기 트랙 생성

배경 음악, 게임 사운드트랙 또는 보컬이 필요하지 않은 모든 사용 사례의 경우 모델에 악기 전용 트랙을 생성하도록 프롬프트를 표시할 수 있습니다.

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
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## 다양한 언어로 음악 생성

Lyria 3는 프롬프트의 언어로 가사를 생성합니다. 프랑스어 가사가 포함된 노래를 생성하려면 프롬프트를 프랑스어로 작성하세요. 모델은 언어에 맞게 보컬 스타일과 발음을 조정합니다.

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
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## 모델 인텔리전스

Lyria 3는 모델이 프롬프트에 따라 음악 구조 (인트로, 절, 코러스, 브리지 등)를 추론하는 프롬프트 프로세스를 분석합니다.
이는 오디오가 생성되기 전에 발생하며 구조적 일관성과 음악성을 보장합니다.

## 프롬프트 작성 가이드

프롬프트가 구체적일수록 결과가 더 좋습니다. 생성을 안내하기 위해 포함할 수 있는 내용은 다음과 같습니다.

- **장르**: 장르 또는 장르 조합을 지정합니다 (예: "로파이 힙합",
  "재즈 퓨전", "시네마틱 오케스트라").
- **악기**: 특정 악기 이름을 지정합니다 (예: "펜더 로즈 피아노",
  "슬라이드 기타", "TR-808 드럼 머신").
- **BPM**: 템포를 설정합니다 (예: "120BPM", "약 70BPM의 느린 템포").
- **키/스케일**: 음악 키를 지정합니다 (예: 'G장조', 'D단조').
- **분위기** : 설명하는 형용사를 사용합니다 (예: '향수',
  '공격적', '몽환적', '꿈결 같은').
- **구조**: `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]`,
  `[Outro]`와 같은 태그 또는 타임스탬프를 사용하여 노래의 진행을 제어합니다.
- **기간**: 클립 모델은 항상 30초 클립을 생성합니다. Pro 모델의 경우 프롬프트에서 원하는 길이를 지정하거나 (예: '2분짜리 노래 만들기') 타임스탬프를 사용하여 기간을 제어합니다.

### 프롬프트 예시

다음은 효과적인 프롬프트의 몇 가지 예입니다.

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## 권장사항

- **먼저 클립으로 반복합니다.** 더 빠른 `lyria-3-clip-preview` 모델을 사용하여 `lyria-3-pro-preview`로 전체 길이 생성을 커밋하기 전에 프롬프트를 실험합니다.
- **자세히 설명합니다.** 모호한 프롬프트는 일반적인 결과를 생성합니다. 최상의 출력을 위해 악기, BPM, 키, 분위기, 구조를 언급합니다.
- **언어를 일치시킵니다.** 가사를 원하는 언어로 프롬프트를 표시합니다.
- **섹션 태그를 사용합니다.** `[Verse]`, `[Chorus]`, `[Bridge]` 태그는 모델에 따라야 할 명확한 구조를 제공합니다.
- **안내에서 가사를 분리합니다.** 맞춤 가사를 제공할 때는 음악 방향 안내와 명확하게 구분합니다.

## 제한사항

- **안전**: 모든 프롬프트는 안전 필터로 확인됩니다. 필터를 트리거하는 프롬프트는 차단됩니다. 여기에는 특정 아티스트 음성 또는 저작권이 있는 가사 생성을 요청하는 프롬프트가 포함됩니다.
- **워터마킹**: 생성된 모든 오디오에는 식별을 위한
  [SynthID 오디오 워터마크](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=ko)가 포함됩니다. 이 워터마크는 사람의 귀에 들리지 않으며 청취 경험에 영향을 미치지 않습니다.
- **멀티턴 편집**: 음악 생성은 단일 턴 프로세스입니다.
  여러 프롬프트를 통해 생성된 클립을 반복적으로 수정하거나 다듬는 것은 현재 버전의 Lyria 3에서 지원되지 않습니다.
- **길이**: 클립 모델은 항상 30초 클립을 생성합니다. Pro 모델은 몇 분 동안 지속되는 노래를 생성합니다. 정확한 기간은 프롬프트를 통해 영향을 받을 수 있습니다.
- **결정론**: 동일한 프롬프트라도 호출 간에 결과가 다를 수 있습니다.

## 다음 단계

- Lyria 3 모델의 [가격 책정](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)을 확인합니다.
- Lyria RealTime으로 [실시간 스트리밍 음악 생성](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ko)
  을 시도합니다.
- [TTS 모델](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko)로 여러 화자가 포함된 대화를 생성합니다.
- [이미지](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko) 또는 [동영상](https://ai.google.dev/gemini-api/docs/video?hl=ko)을 생성하는 방법을 알아봅니다.
- Gemini가 오디오 파일을 [이해하는 방법](https://ai.google.dev/gemini-api/docs/audio?hl=ko)을 알아봅니다.
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ko)를 사용하여 Gemini와 실시간으로 대화합니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-22(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-22(UTC)"],[],[]]
