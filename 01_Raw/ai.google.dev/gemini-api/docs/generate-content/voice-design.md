---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=ko
fetched_at: 2026-09-28T06:08:04.719366+00:00
title: "\uc74c\uc131 \ub514\uc790\uc778 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs/generate-content?hl=ko)

의견 보내기

# 음성 디자인

음성 디자인을 사용하면 Gemini API 음성 엔드포인트(`POST /v1beta/voices`)를 사용하여 자연어 설명에서 완전히 새로운 영구적인 음성 페르소나를 만들 수 있습니다. 사전 빌드된 음성이나 참조 오디오 녹음에 국한되지 않고 캐릭터의 나이, 음색, 억양, 기본 전달을 설명하여 프로젝트에 저장된 재사용 가능한 `voice_...` ID를 받을 수 있습니다.

맞춤 음성을 설계하고, 오디션을 진행하고, 반복하는 가장 빠른 방법은 [Google AI Studio](https://aistudio.google.com/generate-speech?hl=ko)의 대화형 **음성 디자인** 스튜디오를 사용하는 것입니다. 텍스트 프롬프트에서 맞춤 페르소나를 생성하고, 샘플 스크립트로 테스트하고, 결과 `voice_...` ID를 애플리케이션 코드에 직접 복사할 수 있습니다.

[Google AI Studio에서 사용해 보기](https://aistudio.google.com/generate-speech?hl=ko)

[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ko)(`gemini-3.8-flash-tts`)와 [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ko)(`gemini-3.8-flash-lite-tts`) 모두 음성 디자인을 지원합니다.

## 설계된 음성 만들기

Google GenAI SDK (`google-genai` 2.25.0 이상 / `@google/genai` 2.24.0 이상) 또는 REST API를 사용하여 텍스트 설명에서 맞춤 음성을 만듭니다. `"prompted"` 음성의 경우 `voices.create` (`CreateVoice`)와 `voices.get` (`GetVoice`) 모두 출력 전용 `sample_audio` 필드 (`mime_type: "audio/wav"`, base64로 인코딩된 `data`)를 반환하므로 생성된 음성을 즉시 오디션할 수 있습니다.

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### 자바스크립트

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## 음성 설계 작동 방식

1. **프롬프트된 음성 만들기:** `type="prompted"` 및 `store=True`로 `voices.create` (`POST /v1beta/voices`)를 호출합니다.
2. **지속적인 `voice_id` 및 `sample_audio` 미리보기 수신:** API는 음성 ID를 생성하고, 이를 프로젝트에 저장하고, 생성된 음성 미리보기 오디오가 포함된 `sample_audio` (`mime_type: "audio/wav"`, base64로 인코딩된 `data`)와 함께 영구 ID(예: `voice_abc123...`)를 반환합니다.
3. **음성 합성:** `generateContent`을 호출할 때 `speechConfig.voiceConfig.voice`에서 `voice_id`를 전달합니다.

## 설계된 음성으로 음성 합성

`generateContent` 호출 시 반환된 `id` (`voice_...`)를 `voiceConfig.voice`에 전달합니다.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "speech_metadata": {"style": "reflective and awe-inspired"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": created_voice.id}
        },
    },
)

audio_bytes = response.candidates[0].content.parts[0].inline_data.data
with open("designed_voice.wav", "wb") as f:
    f.write(audio_bytes)
```

### 자바스크립트

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash-tts",
  contents: [{
    role: "user",
    parts: [{
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      speechMetadata: { style: "reflective and awe-inspired" },
    }],
  }],
  config: {
    responseModalities: ["AUDIO"],
    speechConfig: {
      voiceConfig: { voice: createdVoice.id },
    },
  },
});

const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
if (data) {
  fs.writeFileSync("designed_voice.wav", Buffer.from(data, "base64"));
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [{
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "speech_metadata": {
          "style": "reflective and awe-inspired"
        }
      }]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "voice": "voice_YOUR_DESIGNED_VOICE_ID"
        }
      }
    }
  }'
```

## 음성 관리

Voices API를 사용하여 언제든지 저장된 음성을 나열, 필터링, 검사, 삭제할 수 있습니다 (모든 필터 매개변수는 [확장된 음성 라이브러리 및 필터링](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=ko#voice-library) 참고).

- **저장소 한도 및 TTL:** 상태 저장 음성 (`store=True`, 프롬프트된 음성 및 복제된 음성 간에 공유됨)에는 **프로젝트당 200개의 음성** 한도와 **1년의 TTL** (수명)이 있습니다.
- **`sample_audio` 가용성:** `voices.create()` (`CreateVoice`) 및 `voices.get()` (`GetVoice`)은 `"prompted"` 음성의 `sample_audio` (`mime_type:
  "audio/wav"`, base64로 인코딩된 `data`)을 채웁니다. 등록정보를 가볍게 유지하기 위해 `voices.list()` (`ListVoices`)는 `sample_audio`를 생략합니다(`"replicated"` 및 `"prebuilt"` 음성의 경우 `sample_audio`가 설정되지 않음).

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## 음성 설계 프롬프트 작성 권장사항

- **`style`이 아닌 Voice 디자인에 영구적인 보컬 특성 넣기:** `voices.create`에서 음성을 만들 때 나이, 성별, 음색, 보컬 질감, 지역 사투리 등 불변의 특성을 정의합니다.
- **상황에 맞는 감정을 위해 `speech_metadata.style` 예약:** 맞춤 음성을 만든 후에는 짧은 `style` 프롬프트 (예: `"whispered urgently"` 또는 `"cheerful and energetic"`)를 사용하여 화자의 핵심 정체성을 변경하지 않고 턴별 연기를 유도합니다.
- **구체적이고 간결하게 작성:** 명확한 1~2문장 설명 (예: *'30대 초반의 활기차고 또렷한 스포츠 아나운서, 중서부 사투리 약간 사용'*)은 모순되거나 지나치게 긴 단락보다 더 깔끔하고 일관성 있는 결과를 생성합니다.

## 다음 단계

- [음성 복제](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=ko)에서 기존 화자의 음성을 복제하는 방법을 알아보세요.
- [텍스트 음성 변환 가이드](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=ko)에서 턴 수준 스타일 지정, 인라인 태그, 다중 화자 대화를 살펴보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-24(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-24(UTC)"],[],[]]
