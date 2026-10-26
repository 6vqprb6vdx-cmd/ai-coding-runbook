---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=ko
fetched_at: 2026-10-26T05:56:53.629167+00:00
title: "Gemini Live API\ub97c \uc0ac\uc6a9\ud55c \uc2e4\uc2dc\uac04 \uc2a4\ud06c\ub9bd\ud2b8 \uc791\uc131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon을 지금 이용 가능합니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini Live API를 사용한 실시간 스크립트 작성

Gemini Live API는 [`gemini-3.5-transcribe-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=ko) 모델을 사용하여 지연 시간이 짧은 실시간 음성 텍스트 변환을 지원합니다. WebSocket을 통해 Live API에 연결하거나 Google 생성형 AI SDK를 사용하면 연속 오디오 입력을 스트리밍하고 음성이 발생할 때 증분 실시간 텍스트 스크립트를 수신할 수 있습니다.

[Google AI Studio에서 실시간 스크립트 사용해 보기mic](https://aistudio.google.com/live?model=gemini-3.5-transcribe-live&hl=ko)
[Colab 쿡북 열기code](https://github.com/google-gemini/cookbook)
[코딩 에이전트 기술 사용하기terminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ko#gemini-live-api-dev)

Gemini Live API를 활용하여 [Agora](https://docs.agora.io/en/ai/models/asr/gemini), [Fishjam](https://docs.fishjam.io/tutorials/gemini-live-integration), [LiveKit](https://docs.livekit.io/agents/models/stt/gemini/), [Pipecat](https://docs.pipecat.ai/api-reference/server/services/stt/google), [Vercel](https://vercel.com/docs/ai-gateway/modalities/speech-to-text), [Vision Agents](https://visionagents.ai/integrations/stt/gemini)와 같은 개발자 플랫폼을 통해 개발자는 고성능 음성 기반 인터페이스를 쉽게 빌드하고 배포할 수 있습니다. 이러한 플랫폼은 복잡한 실시간 미디어 스트리밍 인프라를 백그라운드에서 관리하므로 개발자는 사용자 환경을 만드는 데만 집중할 수 있습니다.

## 실시간 상담사와 실시간 스크립트 비교

둘 다 Live API 양방향 스트리밍 연결을 사용하지만, 실시간 텍스트 변환은 대화형 에이전트가 아닌 전용의 지연 시간이 짧은 음성 인식 파이프라인으로 작동합니다.

| 기능 | 실제 상담사 | 실시간 스크립트 |
| --- | --- | --- |
| **기본 역할** | 듣고, 추론하고, 대답하는 대화형 어시스턴트 | 수신 오디오를 스크립트로 변환하는 실시간 음성 텍스트 변환 파이프라인 |
| **응답 모달리티** | 음성 오디오 및 텍스트 (`response_modalities=["AUDIO"]`) | 스트리밍 텍스트 스크립트 (`response_modalities=["TEXT"]`개) |
| **상호작용 스타일** | 일시중지 감지 및 인터럽트가 있는 턴 기반 대화 | 화자가 말할 때 연속 스트림 처리 |
| **지원되는 기능** | 함수 호출, Google 검색, 시스템 안내 | 음성 바이어싱 (`custom_vocabulary`), 언어 감지, 수동 및 하이브리드 VAD, 스마트 텍스트 변환 |
| **입력 스트림** | 멀티모달: 오디오, 동영상, 이미지, 텍스트 | 오디오 입력 (원시 16비트 PCM) |

## 시작하기

다음 예에서는 `gemini-3.5-transcribe-live`로 양방향 스트리밍 세션을 열고 실시간 스크립트를 수신하는 방법을 보여줍니다.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.5-transcribe-live"

config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],  # Automatic language detection
    ),
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session established with Live Transcription")

        # Receive transcription events
        async for response in session.receive():
            server_content = response.server_content
            if server_content and server_content.input_transcription:
                print("Transcript:", server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### 자바스크립트

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-transcribe-live';

const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [], // Automatic language detection
  },
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.log('Connected to Live Transcription'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Transcript:', content.inputTranscription.text);
        }
      },
      onerror: (e) => console.error('Error:', e.message),
      onclose: (e) => console.log('Connection closed:', e.reason),
    },
  });
}

main();
```

### WebSocket

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-transcribe-live";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['TEXT'],
      },
      inputAudioTranscription: {
        languageCodes: []
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.inputTranscription) {
    console.log('Transcript:', content.inputTranscription.text);
  }
};
```

## 임시 및 최종 스크립트

오디오가 Live API로 스트리밍되면 서버는 `server_content` 내에서 두 개의 보완적인 스크립트 필드를 내보냅니다.

- **`interim_input_transcription`**: 화자가 활발하게 말하는 동안 업데이트되는 지연 시간이 짧은 추측성 부분 가설입니다. 이러한 부분 업데이트는 지연이 최소화되어 빠르게 발생합니다. `interim_input_transcription`를 사용하여 반응형 라이브 UI 자막을 렌더링하거나 자막을 미리 봅니다.
- **`input_transcription`**: 화자가 일시중지되거나, 턴이 완료되거나, 음성이 완료될 때 내보내지는 최종 스크립트입니다. 이 텍스트는 내보내진 후 해당 음성 세그먼트에 대한 모델의 공신력 있는 스크립트를 나타냅니다. 스마트 스크립트 모드에서는 정리되고 형식이 지정된 대답이 포함됩니다.

다음 예에서는 스트리밍 임시 부분 데이터를 표시하고 최종 스크립트를 커밋하는 방법을 보여줍니다.

### Python

```
async def receive_transcripts(session):
    async for response in session.receive():
        server_content = response.server_content
        if not server_content:
            continue

        # Real-time interim hypothesis (updates dynamically as user speaks)
        if server_content.interim_input_transcription:
            interim_text = server_content.interim_input_transcription.text
            print(f"\r[Interim] {interim_text}", end="", flush=True)

        # Finalized transcript (emitted on speech completion)
        if server_content.input_transcription:
            final_text = server_content.input_transcription.text
            print(f"\n[Final] {final_text}")
```

### 자바스크립트

```
onmessage: (message) => {
  const content = message.serverContent;
  if (!content) return;

  if (content.interimInputTranscription) {
    // Update live subtitle preview on screen
    renderInterimPreview(content.interimInputTranscription.text);
  }

  if (content.inputTranscription) {
    // Append final committed transcript to chat history
    commitFinalTranscript(content.inputTranscription.text);
  }
};
```

### WebSocket

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.interimInputTranscription) {
    console.log('[Interim]:', content.interimInputTranscription.text);
  }
  if (content?.inputTranscription) {
    console.log('[Final]:', content.inputTranscription.text);
  }
};
```

## 오디오 전송

활성 연결을 통해 오디오 청크를 원시 16비트 PCM 오디오로 스트리밍합니다.

- **오디오 형식:** 16kHz의 원시 16비트 PCM (모노, little-endian)
- **청크 크기:** 100ms (1,024~2,048프레임) 청크로 오디오를 전송합니다.
- **MIME 유형:** `audio/pcm;rate=16000` (또는 일치하는 샘플링 속도)

### Python

```
# Stream a raw PCM audio chunk
await session.send_realtime_input(
    audio=types.Blob(
        data=audio_chunk_bytes,
        mime_type="audio/pcm;rate=16000"
    )
)

# Signal the end of the audio stream when finished
await session.send_realtime_input(audio_stream_end=True)
```

### 자바스크립트

```
// Send base64-encoded PCM audio chunk
session.sendRealtimeInput({
  audio: {
    data: audioChunkBase64,
    mimeType: 'audio/pcm;rate=16000'
  }
});

// Signal stream end
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSocket

```
// Send base64-encoded PCM audio chunk
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: {
      data: audioChunkBase64,
      mimeType: 'audio/pcm;rate=16000'
    }
  }
}));

// Signal stream end
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

## 스크립트 작성 기능

### 언어 자동 감지

기본적으로 `language_codes`를 생략하거나 `language_codes=[]`를 설정하면 자동 언어 식별이 사용 설정됩니다. 이 모델은 다국어 대화와 코드 전환을 비롯한 발화 전반에서 음성 언어를 동적으로 감지합니다.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
    ),
)
```

### 자바스크립트

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
  },
};
```

### WebSocket

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### 특정 언어 힌트

특정 언어에 대한 인식 편향을 위해 명시적인 BCP-47 언어 코드 (예: 스페인어의 경우 `["es-ES"]`, 프랑스어의 경우 `["fr-FR"]`)를 제공합니다 ([지원되는 언어](#supported-languages) 참고).

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    ),
)
```

### 자바스크립트

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: ['es-ES'],
  },
};
```

### WebSocket

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: ['es-ES'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### 맞춤 어휘 바이어스

`custom_vocabulary`에 최대 1,000개의 구, 고유명사, 브랜드 이름 또는 기술 용어 목록을 제공하여 음성 인식이 특정 용어를 인식하도록 편향시킵니다 (일반적으로 최대 100개의 용어로 최상의 결과를 얻을 수 있음).

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
        custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
    ),
)
```

### 자바스크립트

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
    customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
  },
};
```

### WebSocket

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
      customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### 스마트 스크립트

`input_audio_transcription`에서 `mode` 매개변수를 사용하여 스크립트 출력 형식을 구성합니다.

- **`VERBATIM` (기본값)**: 말한 모든 내용을 그대로 텍스트로 변환하여 원시 필러 단어 ('음', '어', 'like'), 반복, 잘못된 시작을 보존합니다.
- **`SMART` (스마트 텍스트 변환)**: 가독성을 위해 스크립트를 정리하고 구조화합니다.

  - **유창성 저해 요소 삭제**: 필러 단어, 더듬기, 잘못된 시작을 삭제합니다.
  - **인라인 자체 수정**: 음성 수정을 자연스럽게 해결합니다.
  - **구조화된 서식**: 목록, 글머리 기호, 숫자, 날짜, 단락 나누기를 자동으로 서식 지정합니다.
  - **문법 및 대소문자**: 자연스러운 대문자 및 구두점 수정이 적용됩니다.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        mode="SMART",
    ),
)
```

### 자바스크립트

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    mode: 'SMART',
  },
};
```

### WebSocket

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      mode: 'SMART',
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

## 음성 활동 감지 (VAD) 전략

### 자동 VAD (기본값)

기본적으로 서버 측 자동 음성 활동 감지는 화자가 말하기를 시작하고 중지하는 시점을 감지합니다.

### 하이브리드 VAD

[하이브리드 VAD](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ko#hybrid-vad)는 지연 시간 없는 턴 종료를 위해 서버 측 자동 음성 시작 감지와 클라이언트 측 음성 종료 감지를 결합합니다.

1. **서버 측 자동 VAD는 계속 사용 설정**되어 접두사 오디오 패딩으로 음성 시작을 정확하게 감지하여 앞 단어 잘림을 방지합니다.
2. **클라이언트 측 VAD가 무음을 감지함**: 로컬 기기 내 VAD가 화자가 말을 멈춘 것을 감지하면 클라이언트가 즉시 `audio_stream_end` 신호를 보냅니다.
3. **빠른 최종화**: 서버는 `audio_stream_end`를 즉각적인 턴 최종화 프롬프트로 취급하여 기본 서버 측 무음 대기 시간을 우회하고 지연 시간이 최소화된 최종 스크립트를 반환합니다.
4. **대체**: 클라이언트 VAD가 트리거되지 않으면 서버 측 VAD가 자동 대체로 작동합니다.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Stream audio chunks...
    await session.send_realtime_input(
        audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000")
    )

    # When client-side VAD detects end of speech, send audio_stream_end:
    await session.send_realtime_input(audio_stream_end=True)
```

### 자바스크립트

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {},
};

// Stream audio...
session.sendRealtimeInput({
  audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
});

// When client VAD detects end of speech, send audioStreamEnd:
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSocket

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
  }
}));

// When client VAD detects end of speech, send audioStreamEnd:
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

### 수동 VAD (푸시-투-토크)

무전기 인터페이스나 푸시 투 토크 버튼의 경우 자동 VAD를 완전히 사용 중지하고 `activity_start` 및 `activity_end`를 사용하여 턴 경계를 명시적으로 제어합니다.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    realtime_input_config=types.RealtimeInputConfig(
        automatic_activity_detection=types.AutomaticActivityDetection(
            disabled=True
        )
    ),
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Button pressed: signal speech start
    await session.send_realtime_input(activity_start=types.ActivityStart())

    # Stream audio chunks...
    await session.send_realtime_input(audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000"))

    # Button released: signal speech end
    await session.send_realtime_input(activity_end=types.ActivityEnd())
```

### 자바스크립트

```
const config = {
  responseModalities: [Modality.TEXT],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    },
  },
  inputAudioTranscription: {},
};

// Signal speech start
session.sendRealtimeInput({ activityStart: {} });

// Stream audio...

// Signal speech end
session.sendRealtimeInput({ activityEnd: {} });
```

### WebSocket

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    realtimeInputConfig: {
      automaticActivityDetection: {
        disabled: true,
      },
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Button pressed: signal speech start
websocket.send(JSON.stringify({
  realtimeInput: {
    activityStart: {},
  },
}));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' },
  },
}));

// Button released: signal speech end
websocket.send(JSON.stringify({
  realtimeInput: {
    activityEnd: {},
  },
}));
```

## 클라이언트 애플리케이션의 임시 토큰

클라이언트-서버 애플리케이션 (예: 마이크에서 직접 스트리밍하는 모바일 또는 웹 앱)의 경우 [일시적인 토큰](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=ko)을 사용하여 클라이언트 코드에서 API 키가 노출되지 않도록 합니다.

클라이언트 연결을 시작하기 전에 서버에서 제한된 임시 토큰을 만듭니다.

### Python

```
import datetime
from google import genai

client = genai.Client()
expire_time = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=30)

token = client.auth_tokens.create(
    config={
        "uses": 1,
        "expire_time": expire_time,
        "live_connect_constraints": {
            "model": "gemini-3.5-transcribe-live",
            "config": {
                "response_modalities": ["TEXT"],
                "input_audio_transcription": {
                    "language_codes": [],
                },
            },
        },
    }
)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
  config: {
    uses: 1,
    expireTime: expireTime,
    liveConnectConstraints: {
      model: 'gemini-3.5-transcribe-live',
      config: {
        responseModalities: ['TEXT'],
        inputAudioTranscription: {
          languageCodes: [],
        },
      },
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.5-transcribe-live",
      "config": {
        "responseModalities": ["TEXT"],
        "inputAudioTranscription": {
          "languageCodes": []
        }
      }
    }
  }'
```

## 지원 언어

Gemini 3.5 실시간 스크립트에서는 다음 언어와 BCP-47 언어 코드가 지원됩니다.

| 언어 | BCP-47 코드 | 언어 | BCP-47 코드 |
| --- | --- | --- | --- |
| 아프리칸스어 | `af-ZA` | 일본어 | `ja-JP` |
| 암하라어 | `am-ET` | 자바어 | `jv-ID` |
| 아랍어(이집트) | `ar-EG` | Kabuverdianu | `kea-CV` |
| 아르메니아어 | `hy-AM` | 칸나다어 | `kn-IN` |
| 아삼어 | `as-IN` | 카자흐어 | `kk-KZ` |
| 아제르바이잔어 | `az-AZ` | 한국어 | `ko-KR` |
| 벨라루스어 | `be-BY` | 키르기스어 | `ky-KG` |
| 벵골어(방글라데시) | `bn-BD` | 라트비아어 | `lv-LV` |
| 벵골어(인도) | `bn-IN` | 링갈라어 | `ln-CD` |
| 보스니아어 | `bs-BA` | 리투아니아어 | `lt-LT` |
| 불가리아어 | `bg-BG` | 마케도니아어 | `mk-MK` |
| 불가리아어 (아로마어) | `rup-BG` | 말레이어 | `ms-MY` |
| 버마어 | `my-MM` | 말라얄람어 | `ml-IN` |
| 광둥어 (번체) | `yue-Hant-HK` | 몰타어 | `mt-MT` |
| 카탈로니아어 | `ca-ES` | 중국어 (간체) | `cmn-Hans-CN` |
| 세부아노어 | `ceb` | 마라타어 | `mr-IN` |
| 표준 크메르어 | `km-KH` | 몽골어 | `mn-MN` |
| 크로아티아어 | `hr-HR` | 네팔어 | `ne-NP` |
| 체코어 | `cs-CZ` | 노르웨이어 | `nb-NO` |
| 덴마크어 | `da-DK` | 오리야어 | `or-IN` |
| 네덜란드어 | `nl-NL` | 폴란드어 | `pl-PL` |
| 영어(영국) | `en-GB` | 포르투갈어(브라질) | `pt-BR` |
| 영어(인도) | `en-IN` | 포르투갈어(포르투갈) | `pt-PT` |
| 영어(미국) | `en-US` | 펀자브어 | `pa-IN` |
| 에스토니아어 | `et-EE` | 펀자브어 (구르무키 문자) | `pa-Guru-IN` |
| 페르시아어 | `fa-IR` | 루마니아어 | `ro-RO` |
| 필리핀어 | `fil-PH` | 러시아어 | `ru-RU` |
| 핀란드어 | `fi-FI` | 세르비아어 | `sr-RS` |
| 프랑스어 | `fr-FR` | 신디어 (아랍 문자) | `sd-Arab-IN` |
| 갈리시아어 | `gl-ES` | 슬로바키아어 | `sk-SK` |
| 조지아어 | `ka-GE` | 슬로베니아어 | `sl-SI` |
| 독일어 | `de-DE` | 스페인어(라틴 아메리카) | `es-419` |
| 그리스어 | `el-GR` | 스페인어(미국) | `es-US` |
| 구자라트어 | `gu-IN` | 스와힐리어(케냐) | `sw-KE` |
| 하우사어 | `ha-NG` | 스웨덴어 | `sv-SE` |
| 히브리어 | `he-IL` | 타지크어 | `tg-TJ` |
| 힌디어 | `hi-IN` | 텔루구어 | `te-IN` |
| 헝가리어 | `hu-HU` | 태국어 | `th-TH` |
| 아이슬란드어 | `is-IS` | 튀르키예어 | `tr-TR` |
| 인도 영어 | `en-IN` | 우크라이나어 | `uk-UA` |
| 인도네시아어 | `id-ID` | 우즈베크어 | `uz-UZ` |
| 이탈리아어 | `it-IT` | 베트남어 | `vi-VN` |

## 파라미터 참조

`input_audio_transcription` 및 `realtime_input_config`의 필드를 사용하여 실시간 스크립트를 구성합니다.

| 매개변수 | 유형 | 설명 |
| --- | --- | --- |
| `language_codes` | 문자열 배열 | BCP-47 언어 코드 (예: `["en-US"]`)입니다. 생략되거나 비어 있는 경우 (`[]`) 모델이 언어를 자동으로 감지하고 다국어 음성을 처리합니다. |
| `custom_vocabulary` | 문자열 배열 | 음성 인식을 편향시킬 수 있는 최대 1,000개의 맞춤 용어, 약어, 브랜드 이름 또는 고유명사 |
| `mode` | 문자열 | 스크립트 작성 모드: `"VERBATIM"` (기본값) 또는 `"SMART"` (스마트 스크립트 작성) `"SMART"`로 설정하면 모델이 추임새를 삭제하고, 목록을 형식화하며, 유창하지 않은 부분을 수정합니다. |
| `automatic_activity_detection.disabled` | 불리언 | 자동 음성 활동 감지를 사용 중지하고 `activityStart` 및 `activityEnd` 신호를 수동으로 전송하려면 `true`로 설정합니다. |

### 서버 응답 필드

| 필드 | 설명 |
| --- | --- |
| `server_content.interim_input_transcription` | 사용자가 적극적으로 말하는 동안 지속적으로 방출되는 지연 시간이 짧은 임시 부분 전사 가설입니다. |
| `server_content.input_transcription` | 음성 턴이 완료되면 내보내지는 최종적이고 공신력 있는 입력 스크립트입니다. |

## 제한사항

- **세션 시간:** 실시간 텍스트 변환 세션은 최대 10분 동안 연속 스트리밍을 지원합니다.
- **화자 분할:** 라이브 스트리밍 세션에서는 화자 분할이 지원되지 않습니다. 화자 분리의 경우 비스트리밍 [오디오 스크립트 작성](https://ai.google.dev/gemini-api/docs/transcribe?hl=ko#speaker-diarization) 엔드포인트를 사용합니다.
- **단어 수준 타임스탬프:** 단어 수준 타임스탬프는 Live API를 통해 지원되지 않습니다. Live API는 발화 수준 타임스탬프 (`interim_input_transcription` 및 `input_transcription`)를 내보냅니다.
- **맞춤 어휘:** `custom_vocabulary`에 최대 1,000개의 단어를 제공할 수 있지만 일반적으로 최대 100개의 단어로 최상의 결과를 얻을 수 있습니다.
- **모드 호환성:** 스마트 스크립트 (`"mode": "SMART"`)는 필러 단어를 삭제하고 의도 인식 텍스트의 형식을 지정하지만 단어 주석과 결합할 수는 없습니다.

## 다음 단계

- 스트리밍되지 않는 오디오 파일의 경우 [Gemini 스크립트 작성 문서](https://ai.google.dev/gemini-api/docs/transcribe?hl=ko)를 참고하세요.
- 대화형 음성 에이전트를 위한 [Live API 개요](https://ai.google.dev/gemini-api/docs/live-api?hl=ko)를 읽어보세요.
- 실시간 음성 통역에 관한 [실시간 번역 가이드](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=ko)를 참고하세요.
- Live API 스트리밍 가격은 [가격 책정 페이지](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#gemini-3.5-transcribe-live)를 참고하세요.
- [Live API 기능 가이드](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ko)를 살펴보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-10(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-10(UTC)"],[],[]]
