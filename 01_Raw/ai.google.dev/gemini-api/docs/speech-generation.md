---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko
fetched_at: 2026-08-24T02:30:24.440440+00:00
title: "\ud14d\uc2a4\ud2b8 \uc74c\uc131 \ubcc0\ud658 \uc0dd\uc131 (TTS) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 텍스트 음성 변환 생성 (TTS)

Gemini API는 Gemini 텍스트 음성 변환 (TTS) 생성 기능을 사용하여 텍스트 입력을 단일 화자 또는 다중 화자 오디오로 변환할 수 있습니다.
텍스트 음성 변환 (TTS) 생성은 *[제어 가능](#controllable)*합니다. 즉, 자연어를 사용하여 상호작용을 구성하고 오디오의 *스타일*, *억양*, *속도*, *어조*를 안내할 수 있습니다.

TTS 기능은 대화형, 구조화되지 않은 오디오, 멀티모달 입력 및 출력을 위해 설계된 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ko)를 통해 제공되는 음성 생성과 다릅니다. Live API는 동적 대화 컨텍스트에 탁월하지만 Gemini API를 통한 TTS는 스타일과 사운드를 세부적으로 제어하여 정확한 텍스트 암송이 필요한 시나리오(예: 팟캐스트 또는 오디오북 생성)에 맞게 조정됩니다.

이 가이드에서는 텍스트에서 단일 화자 및 다중 화자 오디오를 생성하는 방법을 보여줍니다.

## 시작하기 전에

[지원되는 모델](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko#supported-models) 섹션에 나열된 대로 Gemini 텍스트 음성 변환 (TTS) 기능이 있는 Gemini 2.5 모델 변형을 사용해야 합니다. 최적의 결과를 얻으려면 특정 사용 사례에 가장 적합한 모델을 고려하세요.

빌드를 시작하기 전에 [AI Studio에서 Gemini TTS 모델을 테스트](https://aistudio.google.com/generate-speech?hl=ko)하는 것이 유용할 수 있습니다.

## 단일 화자 TTS

텍스트를 단일 화자 오디오로 변환하려면 응답 모달리티를 'audio'로 설정하고 음성 이름이 포함된 `speech_config` 객체를 전달합니다.
사전 빌드된 [출력 음성](#voices)에서 음성 이름을 선택해야 합니다.

이 예시에서는 모델의 출력 오디오를 웨이브 파일에 저장합니다.

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: "Say cheerfully: Have a wonderful day!",
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' }
         ]
      },
    });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
       "type": "audio"
     },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

마지막으로 생성된 오디오 블록을 반환하는 `interaction.output_audio` 속성을 사용하여 생성된 오디오 데이터를 검색할 수 있습니다. 편의 속성에 관한 자세한 내용은 [상호작용 개요](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko#convenience-properties)를 참고하세요.

## 다중 화자 TTS

멀티 스피커 오디오의 경우 각 스피커 (최대 2개)가 `speaker_voice_config`로 구성된 `multi_speaker_voice_config` 객체가 필요합니다.
[프롬프트](#controllable)에 사용된 것과 동일한 이름으로 각 `speaker`를 정의해야 합니다.

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

 interaction = client.interactions.create(
     model="gemini-3.1-flash-tts-preview",
     input=prompt,
     response_format={"type": "audio"},
     generation_config={
         "speech_config": [
             {"speaker": "Joe", "voice": "Kore"},
             {"speaker": "Jane", "voice": "Puck"}
         ]
     }
 )

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: prompt,
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { speaker: 'Joe', voice: 'Kore' },
            { speaker: 'Jane', voice: 'Puck' }
         ]
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "gemini-3.1-flash-tts-preview",
  "input": "TTS the following conversation between Joe and Jane: Joe: Hows it going today Jane? Jane: Not too bad, how about you?",
  "response_format": {
       "type": "audio"
     },
  "generation_config": {
    "speech_config": [
      { "speaker": "Joe", "voice": "Kore" },
      { "speaker": "Jane", "voice": "Puck" }
    ]
  }
}'
```

## 프롬프트로 음성 스타일 제어하기

단일 화자 및 다중 화자 TTS 모두에 자연어 프롬프트를 사용하여 스타일, 어조, 억양, 속도를 제어할 수 있습니다.
예를 들어 단일 화자 프롬프트에서는 다음과 같이 말할 수 있습니다.

```
Say in an spooky whisper:
"By the pricking of my thumbs...
Something wicked this way comes"
```

여러 화자가 있는 프롬프트에서는 각 화자의 이름과 해당 스크립트를 모델에 제공합니다. 각 스피커에 대해 개별적으로 안내를 제공할 수도 있습니다.

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... what's on the agenda today?
Speaker2: You're never going to guess!
```

전달하고 싶은 스타일이나 감정에 해당하는 [음성 옵션](#voices)을 사용하여 더욱 강조해 보세요. 예를 들어 이전 프롬프트에서 *엔셀라두스*의 숨소리는 '피곤함'과 '지루함'을 강조할 수 있고, *퍽*의 경쾌한 어조는 '신남'과 '행복함'을 보완할 수 있습니다.

## 오디오로 변환할 프롬프트 생성

TTS 모델은 오디오만 출력하지만 [다른 모델](https://ai.google.dev/gemini-api/docs/models?hl=ko)을 사용하여 먼저 스크립트를 생성한 다음 해당 스크립트를 TTS 모델에 전달하여 소리 내어 읽을 수 있습니다.

### Python

```
from google import genai

client = genai.Client()

transcript_interaction = client.interactions.create(
   model="gemini-3.6-flash",
   input="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam."""
)
transcript = transcript_interaction.output_text

tts_interaction = client.interactions.create(
   model="gemini-3.1-flash-tts-preview",
   input=transcript,
   response_format={"type": "audio"},
   generation_config={
      "speech_config": [
         {"speaker": "Dr. Anya", "voice": "Kore"},
         {"speaker": "Liam", "voice": "Puck"}
      ]
   }
)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {

const transcriptInteraction = await client.interactions.create({
   model: "gemini-3.6-flash",
   input: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const ttsInteraction = await client.interactions.create({
   model: "gemini-3.1-flash-tts-preview",
   input: transcriptInteraction.output_text,
   response_format: { type: 'audio' },
   generation_config: {
      speech_config: [
         { speaker: "Dr. Anya", voice: "Kore" },
         { speaker: "Liam", voice: "Puck" }
      ]
   }
  });
}

await main();
```

## 음성 생성 스트리밍

`stream: true`를 설정하면 모델에서 생성된 오디오를 생성되는 대로 스트리밍할 수 있습니다.

### Python

```
from google import genai
import base64

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "audio":
            audio_data = base64.b64decode(event.delta.data)
            # Process the audio chunk (e.g. play it or write to a file)
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const stream = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: "Say cheerfully: Have a wonderful day!",
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' }
         ]
      },
      stream: true
   });

   for await (const event of stream) {
      if (event.event_type === 'step.delta') {
         if (event.delta.type === 'audio') {
            const audioBuffer = Buffer.from(event.delta.data, 'base64');
            // Process the audio buffer
         }
      }
   }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions"       -H "x-goog-api-key: $GEMINI_API_KEY"       -H "Content-Type: application/json"       -H "Api-Revision: 2026-05-20"       --no-buffer       -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    },
    "stream": true
  }'
```

## 음성 옵션

TTS 모델은 `voice_name` 필드에서 다음 30가지 음성 옵션을 지원합니다.

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** - *경쾌함* | **Charon** - *유용한 정보를 제공함* |
| **Kore** - *Firm* | **Fenrir** - *Excitable* | **Leda** - *Youthful* |
| **Orus** -- *Firm* | **Aoede** - *Breezy* | **Callirrhoe** - *느긋함* |
| **Autonoe** -- *밝음* | **엔셀라두스** -- *숨소리* | **Iapetus** - *Clear* |
| **Umbriel** - *느긋함* | **Algieba** -- *Smooth* | **Despina** - *Smooth* |
| **Erinome** - *맑음* | **Algenib** - *자갈* | **Rasalgethi** - *유용한 정보를 전달함* |
| **Laomedeia** - *경쾌함* | **Achernar** - *Soft* | **Alnilam** - *Firm* |
| **Schedar** -- *Even* | **Gacrux** - *성인용* | **Pulcherrima** -- *앞으로* |
| **Achird** - *친근함* | **Zubenelgenubi** - *캐주얼* | **Vindemiatrix** - *온화함* |
| **Sadachbia** - *활기참* | **Sadaltager** -- *지식이 풍부함* | **Sulafat** - *따뜻함* |

[AI Studio](https://aistudio.google.com/generate-speech?hl=ko)에서 모든 음성 옵션을 들을 수 있습니다.

## 지원 언어

TTS 모델은 입력 언어를 자동으로 감지합니다. 지원되는 언어는 다음과 같습니다.

| 언어 | BCP-47 코드 | 언어 | BCP-47 코드 |
| --- | --- | --- | --- |
| 아랍어 | ar | 필리핀어 | fil |
| 벵골어 | bn | 핀란드어 | fi |
| 네덜란드어 | nl | 갈리시아어 | gl |
| 영어 | en | 조지아어 | ka |
| 프랑스어 | fr | 그리스어 | el |
| 독일어 | de | 구자라트어 | gu |
| 힌디어 | hi | 아이티 크리올어 | ht |
| 인도네시아어 | id | 히브리어 | he |
| 이탈리아어 | it | 헝가리어 | hu |
| 일본어 | ja | 아이슬란드어 | is |
| 한국어 | ko | 자바어 | jv |
| 마라타어 | mr | 칸나다어 | kn |
| 폴란드어 | pl | 콘칸어 | kok |
| 포르투갈어 | pt | 라오어 | lo |
| 루마니아어 | ro | 라틴 | la |
| 러시아어 | ru | 라트비아어 | lv |
| 스페인어 | es | 리투아니아어 | lt |
| 타밀어 | ta | 룩셈부르크어 | lb |
| 텔루구어 | te | 마케도니아어 | mk |
| 태국어 | th | 마이틸리어 | mai |
| 튀르키예어 | tr | 말라가시어 | mg |
| 우크라이나어 | uk | 말레이어 | ms |
| 베트남어 | vi | 말라얄람어 | ml |
| 아프리칸스어 | af | 몽골어 | mn |
| 알바니아어 | sq | 네팔어 | ne |
| 암하라어 | am | 노르웨이어(보크말) | nb |
| 아르메니아어 | hy | 노르웨이어(뉘노르스크) | nn |
| 아제르바이잔어 | az | 오리야어 | 또는 |
| 바스크어 | eu | 파슈토어 | ps |
| 벨라루스어 | be | 페르시아어 | fa |
| 불가리아어 | bg | 펀자브어 | pa |
| 버마어 | my | 세르비아어 | sr |
| 카탈로니아어 | ca | 신드어 | sd |
| 세부아노어 | ceb | 싱할라어 | si |
| 중국어, 북경어 | cmn | 슬로바키아어 | sk |
| 크로아티아어 | 시간 | 슬로베니아어 | sl |
| 체코어 | cs | 스와힐리어 | sw |
| 덴마크어 | da | 스웨덴어 | sv |
| 에스토니아어 | et | 우르두어 | ur |

## 지원되는 모델

| 모델 | 단일 화자 | 다중 화자 |
| --- | --- | --- |
| [Gemini 3.1 Flash TTS 프리뷰](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=ko) | ✔️ | ✔️ |
| [Gemini 2.5 Flash 프리뷰 TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=ko) | ✔️ | ✔️ |
| [Gemini 2.5 Pro 프리뷰 TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=ko) | ✔️ | ✔️ |

## 프롬프트 가이드

**Gemini 네이티브 오디오 생성 TTS (텍스트 음성 변환)** 모델은 ***무엇을 말해야 하는지뿐만 아니라 어떻게 말해야 하는지도 아는*** 대규모 언어 모델을 사용하여 기존 TTS 모델과 차별화됩니다.

고급 프롬프트는 모델이 따라야 하는 시스템 요청 사항이라고 생각하면 됩니다. 모델에 더 많은 컨텍스트를 제공하고 성능을 제어하는 방법입니다.

이 기능을 사용하려면 사용자가 가상 음성 연기자가 연기할 장면을 설정하는 감독이라고 생각하면 됩니다. 프롬프트를 작성하려면 캐릭터의 핵심 정체성과 원형을 정의하는 **오디오 프로필**, 물리적 환경과 감정적 '분위기'를 설정하는 **장면 설명**, 스타일, 억양, 속도 제어에 관한 더 정확한 연기 지침을 제공하는 **감독의 메모**를 고려하는 것이 좋습니다.

정확한 지역 억양, 구체적인 준언어적 특징 (예: 숨소리), 속도와 같은 미묘한 지침을 제공하면 사용자는 모델의 맥락 인식 기능을 활용하여 매우 역동적이고 자연스러우며 표현력이 풍부한 오디오 성능을 생성할 수 있습니다. 최적의 성능을 위해 **스크립트**와 연출 프롬프트가 일치하여 *'누가 말하는지'*가 *'무엇을 말하는지'* 및 *'어떻게 말하는지'*와 일치하는 것이 좋습니다.

이 가이드의 목적은 Gemini TTS 오디오 생성을 사용하여 오디오 환경을 개발할 때 기본적인 방향을 제시하고 아이디어를 제공하는 것입니다. 여러분이 만들 멋진 결과물을 기대하겠습니다.

### 오디오 태그

태그는 `[whispers]` 또는 `[laughs]`과 같은 인라인 수정자로, 게재를 세부적으로 제어할 수 있습니다. 이러한 스타일을 사용하여 스크립트의 한 줄 또는 섹션의 어조, 속도, 감정적 분위기를 변경할 수 있습니다. `[cough]`, `[sighs]`, `[gasp]`와 같은 감탄사 및 기타 비언어적 소리를 공연에 추가하는 데 사용할 수도 있습니다.

작동하는 태그와 작동하지 않는 태그의 전체 목록은 없으므로 다양한 감정과 표현을 실험하여 출력이 어떻게 달라지는지 확인하는 것이 좋습니다.

스크립트가 영어로 되어 있지 않은 경우 최상의 결과를 얻으려면 영어 오디오 태그를 사용하는 것이 좋습니다.

**오디오 태그에 창의성 발휘하기**

오디오 태그로 얻을 수 있는 변동성을 보여주기 위해 각각 동일한 내용을 말하지만 사용된 태그에 따라 전달이 달라지는 일련의 예가 있습니다.

줄 시작 부분에 태그를 추가하여 화자가 신나거나, 지루하거나, 망설이는 것처럼 들리게 하여 전달의 강조를 변경할 수 있습니다.

- `[excitedly]` 안녕하세요. 저는 새로운 텍스트 음성 변환 모델로, 다양한 방식으로 말할 수 있습니다. 무엇을 도와드릴까요?
- `[bored]` 안녕하세요. 저는 새로운 텍스트 음성 변환 모델입니다.
- `[reluctantly]` 안녕하세요. 저는 새로운 텍스트 음성 변환 모델입니다.

태그를 사용하여 전달 속도를 변경하거나 속도와 강조를 결합할 수도 있습니다.

- `[very fast]` 안녕하세요. 저는 새로운 텍스트 음성 변환 모델입니다.
- `[very slow]` 안녕하세요. 저는 새로운 텍스트 음성 변환 모델입니다.
- `[sarcastically, one painfully slow word at a time]` 안녕하세요. 저는 새로운 텍스트 음성 변환 모델입니다.

특정 섹션을 정확하게 제어할 수도 있으므로 한 부분은 속삭이고 다른 부분은 소리칠 수 있습니다.

- `[whispers]` 안녕하세요. 저는 새로운 텍스트 음성 변환 모델인 `[shouting]`입니다. 다양한 방식으로 말할 수 있습니다. `[whispers]` 무엇을 도와드릴까요?

원하는 창의적인 아이디어를 실험해 볼 수도 있습니다.

- `[like a cartoon dog]` 안녕하세요. 저는 새로운 텍스트 음성 변환 모델입니다.
- `[like dracula]` 안녕하세요. 저는 새로운 텍스트 음성 변환 모델입니다.

흔히 사용되는 태그는 다음과 같습니다.

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

태그를 사용하면 스크립트의 전송을 빠르게 제어할 수 있습니다. 더욱 세밀하게 제어하려면 컨텍스트 프롬프트와 결합하여 공연의 전반적인 분위기와 느낌을 설정할 수 있습니다.

### 프롬프트 구조

강력한 프롬프트에는 훌륭한 성능을 만들기 위해 함께 작동하는 다음 요소가 포함되어야 합니다.

- **오디오 프로필** - 음성의 페르소나를 설정하여 캐릭터 정체성, 원형, 연령, 배경 등의 기타 특징을 정의합니다.
- **장면** - 무대를 설정합니다. 물리적 환경과 '분위기'를 모두 설명합니다.
- **감독의 메모** - 가상 인재가 참고해야 하는 중요한 지침을 분류할 수 있는 성능 가이드입니다. 예로는 스타일, 호흡, 페이싱, 조음, 강세가 있습니다.
- **샘플 컨텍스트** - 모델에 컨텍스트 기반 시작점을 제공하므로 가상 배우자가 설정한 장면으로 자연스럽게 들어갑니다.
- **스크립트** - 모델이 말할 텍스트입니다. 최상의 성능을 위해 스크립트 주제와 글쓰기 스타일이 제공하는 방향과 관련이 있어야 합니다.
- **오디오 태그** - 텍스트의 해당 부분이 전달되는 방식을 변경하기 위해 스크립트에 넣을 수 있는 수정자입니다(예: `[whispers]` 또는 `[shouting]`).

전체 프롬프트 예시:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions - no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
Yes, massive vibes in the studio! You are locked in and it is absolutely
popping off in London right now. If you're stuck on the tube, or just sat
there pretending to work... stop it. Seriously, I see you. Turn this up!
We've got the project roadmap landing in three, two... let's go!
```

### 자세한 프롬프트 작성 전략

프롬프트의 각 요소를 다음과 같이 분류합니다.

#### 오디오 프로필

캐릭터의 페르소나를 간략하게 설명해 줘.

- **이름.** 캐릭터에 이름을 지정하면 모델과 긴밀한 연기를 함께 연결하는 데 도움이 됩니다. 장면과 맥락을 설정할 때 이름으로 캐릭터를 언급하세요.
- **역할** 장면에 등장하는 캐릭터의 핵심 정체성과 원형입니다. 예를 들어 라디오 DJ, 팟캐스터, 뉴스 리포터 등이 있습니다.

예:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### 장면

톤과 분위기를 설정하는 위치, 분위기, 환경 세부정보 등 장면의 컨텍스트를 설정합니다. 캐릭터 주변에서 어떤 일이 일어나고 있으며 그 일이 캐릭터에게 어떤 영향을 미치는지 설명해 줘. 장면은 전체 상호작용의 환경 컨텍스트를 제공하고 연기 성능을 미묘하고 유기적인 방식으로 안내합니다.

예:

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### 디렉터 메모

이 중요한 섹션에는 구체적인 성능 안내가 포함되어 있습니다. 다른 요소는 모두 건너뛸 수 있지만 이 요소를 포함하는 것이 좋습니다.

성능에 중요한 것만 정의하고 과도하게 지정하지 않도록 주의하세요. 엄격한 규칙이 너무 많으면 모델의 창의성이 제한되고 성능이 저하될 수 있습니다. 역할과 장면 설명의 균형을 특정 연기 규칙과 맞추세요.

가장 일반적인 방향은 **스타일, 페이싱, 악센트**이지만 모델은 이에 국한되지 않으며 이러한 방향이 필요하지도 않습니다. 실적에 중요한 추가 세부정보를 포함하는 맞춤 안내를 자유롭게 포함하고 필요한 만큼 자세히 설명하세요.

예를 들면 다음과 같습니다.

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**스타일:**

생성된 음성의 어조와 스타일을 설정합니다. 공연을 안내하기 위해 신나는, 활기찬, 편안한, 지루한 등의 표현을 포함하세요. 자세히 설명하고 필요한 만큼 세부정보를 제공하세요. *'전염성 있는 열정. 청취자가 대규모의 흥미로운 커뮤니티 이벤트에 참여하고 있다는 느낌을 받아야 합니다.'*라는 표현이 *'활기차고 열정적'*이라는 표현보다 더 적합합니다.

'보컬 스마일'과 같이 성우 업계에서 인기 있는 용어를 사용해 볼 수도 있습니다. 원하는 만큼 스타일 특성을 레이어링할 수 있습니다.

예:

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

더 깊은 내용

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

복잡

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**억양:**

선택한 악센트를 설명합니다. 구체적일수록 더 나은 결과를 얻을 수 있습니다. 예를 들어 '*영국 크로이던에서 들리는 영국 영어 억양*'을 '*영국 억양*' 대신 사용합니다.

예:

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a from Brixton, London
...
```

**예산 소진 속도:**

전반적인 페이싱과 작품 전체의 페이스 변화

예:

단순

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

더 깊이 있는 정보

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

복잡

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

**사용해 보기**

[TTS 앱](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=ko)에서 직접 이러한 예시를 사용해 보고 Gemini가 감독의 역할을 맡도록 해 보세요. 다음 팁을 참고하여 멋진 보컬 퍼포먼스를 만들어 보세요.

- 전체 프롬프트가 일관성을 유지해야 합니다. 스크립트와 연출은 훌륭한 공연을 만드는 데 함께 작용합니다.
- 모든 것을 설명할 필요는 없습니다. 모델이 부족한 부분을 채울 수 있도록 공간을 두면 자연스러움을 유지하는 데 도움이 됩니다. (재능 있는 배우처럼)
- 막히는 부분이 있다면 Gemini의 도움을 받아 스크립트나 공연을 만들어 보세요.

## 제한사항

- TTS 모델은 텍스트 입력만 수신하고 오디오 출력을 생성할 수 있습니다.
- TTS 세션의 [컨텍스트 윈도우](https://ai.google.dev/gemini-api/docs/long-context?hl=ko) 한도는 32,000개의 토큰입니다.
- 언어 지원은 [언어](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko#languages) 섹션을 참고하세요.
- TTS는 `gemini-3.1-flash-tts-preview`를 사용하는 경우를 제외하고 스트리밍을 지원하지 않습니다.

음성 생성을 위해 Gemini 3.1 Flash TTS 프리뷰 모델을 사용할 때는 다음 제약 조건이 적용됩니다.

- **프롬프트 안내와 음성 불일치:** 모델의 출력이 선택한 화자와 항상 엄격하게 일치하지 않아 오디오가 예상과 다르게 들릴 수 있습니다. 톤이 일치하지 않는 경우 (예: 깊은 남성 목소리가 어린 소녀처럼 말하려고 하는 경우)를 방지하려면 프롬프트의 톤과 컨텍스트가 선택한 화자의 프로필과 자연스럽게 일치해야 합니다.
- **긴 출력의 품질:** 몇 분보다 긴 생성된 출력의 경우 음성 품질과 일관성이 떨어질 수 있습니다. 스크립트를 더 작은 청크로 분할하는 것이 좋습니다.
- **가끔 텍스트 토큰 반환:** 모델이 오디오 토큰 대신 텍스트 토큰을 반환하여 서버에서 `500` 오류와 함께 요청이 실패하는 경우가 있습니다. 이 오류는 매우 적은 비율의 요청에서 무작위로 발생하므로 애플리케이션에서 자동 재시도 로직을 구현하여 이를 처리해야 합니다.
- **프롬프트 분류기 거짓 거부:** 모호한 프롬프트는 음성 합성 분류기를 트리거하지 못하여 요청이 거부(`PROHIBITED_CONTENT`)되거나 모델이 스타일 지침과 감독의 메모를 소리 내어 읽게 될 수 있습니다. 모델에 음성을 합성하도록 지시하는 명확한 서문을 추가하고 실제 음성 스크립트가 시작되는 위치를 명시적으로 라벨링하여 프롬프트를 검증합니다.

## 다음 단계

- Gemini의 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ko)는 다른 모달리티와 인터리브할 수 있는 대화형 오디오 생성 옵션을 제공합니다.
- 오디오 *입력* 작업에 관한 내용은 [오디오 이해](https://ai.google.dev/gemini-api/docs/audio?hl=ko) 가이드를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-30(UTC)"],[],[]]
