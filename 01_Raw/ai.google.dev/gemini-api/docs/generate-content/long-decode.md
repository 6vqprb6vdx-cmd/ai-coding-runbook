---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=ko
fetched_at: 2026-10-19T05:41:18.149522+00:00
title: "\uae34 \ub514\ucf54\ub529 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon을 지금 이용 가능합니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs/generate-content?hl=ko)

의견 보내기

# 긴 디코딩

긴 디코딩을 사용하면 Gemini 4 Argon이 심층 추론 작업에 대해 단일 요청 출력 한도를 초과하여 통합된 100만 토큰 컨텍스트 윈도우 (입력, 사고, 출력 전반에 공유되는 1,048,576개 토큰)까지 생성할 수 있습니다.

모델 ID만 변경해서는 긴 디코딩을 사용 설정할 수 없습니다. 추가 설정이 없으면 스트리밍 호출의 경우 64,000개 토큰, 비스트리밍 호출의 경우 32,000개 토큰에서 출력이 중지됩니다. 긴 디코딩을 사용 설정하는 가장 빠른 방법은 Google 생성형 AI SDK를 업그레이드하고 `max_output_tokens`을 65,536보다 큰 값으로 설정하는 것입니다. 이 가이드에서는 긴 디코딩의 작동 방식, 사용 시기, `generateContent`로 사용 설정하는 방법을 설명합니다.

## 디코딩이 작동하는 시간

단일 스트리밍 또는 SDK 요청은 최대 64,000개의 토큰을 생성하고 비스트리밍 REST 요청은 최대 32,000개의 토큰을 생성합니다. 대답에 더 많은 토큰이 필요한 경우 모델은 이전 홉이 중지된 위치에서 각각 계속되는 여러 요청-응답 홉에 걸쳐 대답을 생성합니다.

- **통합 입력 및 출력 토큰 한도:** 입력, 사고, 함수 호출, 최종 대답이 하나의 100만 토큰 창을 공유합니다. 출력은 최대 1,048,576개에서 입력 토큰 수를 뺀 만큼 사용할 수 있습니다.
- **홉당 한도:** 한 홉에서 최대 65,536개의 출력 토큰이 반환됩니다. 비스트리밍 REST 요청은 최대 32,768개를 반환합니다.
- **연속 신호:** 모델이 한도에 도달했지만 토큰이 남아 있는 경우 대답은 `finish_reason: CONTINUATION` 및 `continuation_token`로 끝납니다.
- **다음 홉:** 클라이언트가 토큰과 함께 동일한 요청을 다시 전송합니다. 모델이 중지된 지점부터 계속됩니다.
- **모든 홉의 총계:** `max_output_tokens`는 모든 홉의 총 사고 및 출력 토큰을 함께 설정합니다.
- **중지 신호:** 모델이 `max_output_tokens`를 모두 사용하면 대답이 `finish_reason: MAX_TOKENS`로 끝납니다.

어려운 문제의 경우 홉이 내부 사고에 모든 토큰을 사용하고 `continuation_token`와 함께 빈 텍스트를 반환할 수 있습니다. 이는 정상적인 현상이며 최종 답변은 이후 홉에서 제공됩니다.

## 기본 출력 한도

긴 디코딩이 없으면 단일 요청이 요청당 한도에서 중지됩니다.

- **Google 생성형 AI SDK (`generate_content`)를 통한 스트리밍 요청 및 비스트리밍 요청:** 기본값은 64,000개의 출력 토큰입니다.
- **직접 비스트리밍 REST 호출 (`generateContent`):** 기본값은 출력 토큰 32,000개입니다. `continuation_token` 없이 스트리밍되지 않는 REST 호출에서 `max_output_tokens`을 32,768보다 크게 설정하면 `400` 오류가 반환됩니다.

| 모델을 호출하는 방법 | 긴 디코딩이 없는 출력 한도 | 시작 시 긴 디코딩 | 필요한 조치 |
| --- | --- | --- | --- |
| Google 생성형 AI SDK, 최신 버전 | 64K | 예, SDK가 계속 진행합니다. | `max_output_tokens`을 설정합니다. |
| Google GenAI SDK, 이전 버전, 비스트리밍 | 64K | 아니요 | SDK를 업그레이드합니다. |
| REST `streamGenerateContent` | 64K | 예, 자체 루프 사용 | 루프를 작성합니다. [옵션 2](#option-2-loop)를 참고하세요. |
| REST `generateContent` | 32,000 | 예, 자체 루프 사용 | 루프를 작성합니다. [옵션 2](#option-2-loop)를 참고하세요. |

## 긴 디코딩을 사용해야 하는 경우

대부분의 요청은 단일 요청 한도 (스트리밍 및 SDK 호출의 경우 64,000개 토큰, 비스트리밍 REST 호출의 경우 32,000개 토큰) 내에서 완료됩니다. 대답에 단일 요청에서 허용하는 것보다 더 많은 결합된 사고 및 출력 토큰이 필요한 경우 긴 디코딩을 사용하세요. `max_output_tokens`을 높이면 표준 답변이 길어지는 대신 모델이 어려운 문제를 추론할 수 있는 한도가 높아집니다.

| 워크로드 | 긴 디코딩을 사용하시겠습니까? | 이유 |
| --- | --- | --- |
| 어려운 수학, 과학, 연구, 정형 증명 | 예 | 모델은 64,000개 이상의 토큰을 사용하여 추론을 탐색하고 확인할 수 있습니다. |
| 가장 어려운 코딩 및 에이전트형 작업 | 예 | 일부 작업에서는 한 번의 대답에 64,000개가 넘는 토큰의 사고와 코드가 필요합니다. 대부분의 코딩 및 에이전트형 작업은 64,000개 미만으로 완료됩니다. |
| 출력 한도에서 중지되는 평가 하네스 | 예 | 긴 디코딩은 모델이 사고에 전체 64K 또는 32K 요청을 사용할 때 답변이 잘리는 것을 방지합니다. |
| 채팅, Q&A, 요약, 분류, 추출 | 아니요 | 이러한 작업은 32,000개 미만의 토큰으로 완료됩니다. |
| '700,000단어 분량의 책을 작성해 줘'와 같이 고정된 길이를 요청하는 경우 | 아니요 | 모델이 길이 타겟을 따르지 않습니다. |
| 짧은 차례로 도구를 여러 번 호출하는 에이전트 | 아니요 | 각 차례는 짧습니다. 각 차례의 대규모 출력은 통합된 100만 개의 입력 및 출력 창을 빠르게 채웁니다. |
| 입력 한도 100만 개에 근접한 프롬프트 | 아니요 | 출력은 입력에서 1M을 뺀 값만 사용할 수 있습니다. |
| 지연 시간에 민감한 요청 | 아니요 | 긴 디코딩은 몇 분 동안 실행될 수 있습니다. |

`max_output_tokens`를 높게 설정하면 모델이 어려운 문제에 대해 더 오래 생각할 수 있지만, 모델은 여전히 얼마나 작성할지 결정합니다. 모델이 사용하는 추론 노력의 양을 제어하려면 [`thinking_level`](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ko)를 설정합니다.

## 긴 디코딩 사용 설정

Google GenAI SDK (옵션 1, 대부분의 앱에 권장)를 사용하여 긴 디코딩을 자동으로 실행하거나 자체 연속 루프를 작성할 수 있습니다 (옵션 2). 두 옵션 모두 100만 개의 토큰 컨텍스트 윈도우를 지원합니다.

|  | 옵션 1: Google GenAI SDK (권장) | 옵션 2: 자체 스트리밍 루프 | 옵션 2: 자체 비스트리밍 루프 |
| --- | --- | --- | --- |
| **각 홉을 시작하는 주체** | SDK `max_output_tokens`를 설정했습니다. | 각 체크포인트 또는 스트림이 삭제된 후의 코드 | 32, 000토큰마다 코드 |
| **요청당 토큰 수** | 홉당 64,000개 | 스트림당 64,000개, 32,000개 후 5,000개 토큰마다 체크포인트 | 요청당 32,000개 |
| **요청당 시간 제한** | 20분 | 20분 | 20분 |
| **스토리지** | 서버 스토리지가 없음 | 서버 스토리지가 없음 | 서버 스토리지가 없음 |
| **권장** | 대부분의 애플리케이션 | 스트리밍하는 REST 호출자 및 커스텀 하네스 | 간단한 평가 도구 |

암호화된 `continuation_token`는 요청 간에 모델의 상태를 전달하므로 서버에 아무것도 저장되지 않습니다.

### 옵션 1: Google 생성형 AI SDK 사용 (권장)

최신 Google 생성형 AI SDK에서는 스트리밍 및 비스트리밍 호출 모두에 `automatic_continuation`가 기본적으로 사용 설정되므로 설정할 필요가 없습니다. 요청별 한도를 초과하여 `max_output_tokens`를 설정하면 SDK가 자동으로 연속 홉을 실행하고 하나의 결합된 응답을 반환합니다.

1. SDK를 업그레이드합니다.

   ### Python

   ```
   pip install -U "google-genai>=2.30.1"
   ```

   ### JavaScript

   ```
   npm install "@google/genai@>=2.29.1"
   ```
2. `max_output_tokens`을 65,536보다 크게 설정합니다.

   ### Python

   ```
   from google import genai
   from google.genai import types

   client = genai.Client()  # Reads GEMINI_API_KEY

   response = client.models.generate_content(
       model="gemini-4-argon",
       contents="Write a complete, rigorous proof of the prime number theorem.",
       config=types.GenerateContentConfig(
           max_output_tokens=262_144,  # Total thinking and output for all hops
           thinking_config=types.ThinkingConfig(thinking_level="high"),
           automatic_continuation=True,  # Default. Shown for clarity.
       ),
   )

   print(response.text)
   print("Finish reason:", response.candidates[0].finish_reason)
   print("Prompt size:", response.usage_metadata.initial_prompt_token_count)
   print("Billed tokens:", response.usage_metadata.total_token_count)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI, ThinkingLevel } from "@google/genai";

   const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY

   const response = await ai.models.generateContent({
     model: "gemini-4-argon",
     contents: "Write a complete, rigorous proof of the prime number theorem.",
     config: {
       maxOutputTokens: 262144, // Total thinking and output for all hops
       thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
       automaticContinuation: true, // Default. Shown for clarity.
     },
   });

   console.log(response.text);
   console.log("Finish reason:", response.candidates?.[0]?.finishReason);
   console.log("Prompt size:", response.usageMetadata?.initialPromptTokenCount);
   console.log("Billed tokens:", response.usageMetadata?.totalTokenCount);
   ```

다음 내용을 기억하세요.

- **스트리밍:** `generate_content_stream` (Python) 및 `generateContentStream` (JavaScript)도 계속됩니다. 체크포인트 이후에 스트림이 중단되면 SDK는 해당 체크포인트부터 다시 시작합니다.
- **제한 시간:** 제한 시간과 재시도는 전체 실행이 아닌 각 홉에 적용됩니다.
- **수동 제어:** 직접 루프를 실행하려면 `automatic_continuation=False` (Python) 또는 `automaticContinuation: false` (JavaScript)를 설정합니다. 그런 다음 옵션 2를 따릅니다.
- **사용량:** 사용량 필드에는 모든 홉의 합계가 표시됩니다. 프롬프트 크기를 가져오려면 `initial_prompt_token_count`를 읽어보세요. [토큰 집계](#count-tokens)를 참조하세요.

### 옵션 2: 자체 루프 작성

REST를 직접 호출하거나, 최신 SDK가 없는 언어를 사용하거나, 완전한 제어가 필요한 경우 자체 루프를 작성합니다. [Python](https://github.com/googleapis/python-genai/blob/v2.30.1/google/genai/models.py#L6111) 및 [JavaScript/TypeScript](https://github.com/googleapis/js-genai/blob/v2.29.1/src/models.ts#L88)의 Google GenAI SDK 구현을 참고할 수도 있습니다.

다음과 같은 규칙을 따르세요.

1. **모든 홉에서 동일한 요청을 보냅니다.** 원본 `contents`, `system_instruction`, `tools`, `generation_config`을 보냅니다. `max_output_tokens`을 동일하게 유지합니다.
2. **`contents`에 부분 출력을 추가하지 마세요.** `continuation_token`는 사고를 포함한 모델의 상태를 전달합니다.
3. **최신 토큰만 전송합니다.** 각 토큰에는 이전의 모든 진행 상황이 포함됩니다.
4. **`finish_reason`이 `CONTINUATION`인 동안 계속합니다.** 다른 종료 이유로 중지합니다.
5. **마지막 홉 이후에 부분을 조인합니다.** 모든 홉의 파트를 대화 기록을 위한 하나의 모델 턴으로 결합합니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()  # Reads GEMINI_API_KEY
PROMPT = "Write a complete, rigorous proof of the prime number theorem."
parts = []
token = None

while True:
    response = client.models.generate_content(
        model="gemini-4-argon",
        contents=PROMPT,  # The original contents on every request
        config=types.GenerateContentConfig(
            max_output_tokens=262_144,  # The same total on every request
            thinking_config=types.ThinkingConfig(thinking_level="high"),
            automatic_continuation=False,  # You run the loop
            continuation_token=token,
        ),
    )
    candidate = response.candidates[0]
    if candidate.content and candidate.content.parts:
        parts.extend(candidate.content.parts)
    token = candidate.continuation_token
    if candidate.finish_reason != types.FinishReason.CONTINUATION or not token:
        break

print("".join(p.text for p in parts if p.text and not p.thought))
print("Finish reason:", candidate.finish_reason)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY
const PROMPT = "Write a complete, rigorous proof of the prime number theorem.";
const parts = [];
let token = undefined;
let candidate = undefined;

while (true) {
  const response = await ai.models.generateContent({
    model: "gemini-4-argon",
    contents: PROMPT, // The original contents on every request
    config: {
      maxOutputTokens: 262144, // The same total on every request
      thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
      automaticContinuation: false, // You run the loop
      continuationToken: token,
    },
  });
  candidate = response.candidates?.[0];
  if (candidate?.content?.parts) {
    parts.push(...candidate.content.parts);
  }
  token = candidate?.continuationToken;
  if (candidate?.finishReason !== "CONTINUATION" || !token) {
    break;
  }
}

console.log(parts.filter((p) => p.text && !p.thought).map((p) => p.text).join(""));
console.log("Finish reason:", candidate?.finishReason);
```

### REST

```
# Hop 1: send the request with max_output_tokens.
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
    "generationConfig": {
      "maxOutputTokens": 262144,
      "thinkingConfig": {"thinkingLevel": "high"}
    }
  }'

# Hop 2: if finishReason is CONTINUATION, send the same request plus the token.
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
    "generationConfig": {
      "maxOutputTokens": 262144,
      "thinkingConfig": {"thinkingLevel": "high"}
    },
    "continuationToken": "TOKEN_FROM_HOP_1"
  }'
```

사고에만 소요된 홉은 `finishReason: "CONTINUATION"`가 있는 빈 `text`를 반환합니다. 이를 정상적인 진행 상황으로 간주하고 다음 홉을 요청합니다.

```
{
  "candidates": [{
    "content": {"role": "model", "parts": [{"text": ""}]},
    "finishReason": "CONTINUATION",
    "continuationToken": "CiQ4ZmQ3..."
  }],
  "usageMetadata": {
    "promptTokenCount": 142,
    "candidatesTokenCount": 0,
    "thoughtsTokenCount": 32768,
    "totalTokenCount": 32910
  }
}
```

**스트리밍 루프**에는 규칙이 하나 더 필요합니다. 처음 32,768개의 토큰이 지나면 스트림은 5,000개의 토큰마다 체크포인트 토큰을 전송합니다. 새 청크를 대기중 목록에 보관합니다. 청크에 `continuation_token`가 있으면 대기 중인 청크를 커밋된 출력으로 이동하고 토큰을 저장합니다. 스트림이 끊어지면 대기 중인 청크를 삭제하고 마지막 토큰부터 다시 시작합니다. 첫 번째 체크포인트 전에 스트림이 끊어지면 원래 요청을 다시 전송합니다.

## `max_output_tokens` 설정

`max_output_tokens`는 모든 홉에서 사고 및 출력의 결합된 한도를 설정합니다. 이 값을 낮춘다고 해서 모델이 더 간결하게 생각하는 것은 아니며, 대신 대답이 더 빨리 잘립니다.

| 워크로드 | 권장 기간: `max_output_tokens` |
| --- | --- |
| 한도가 32K 미만인 기존 앱 | 32,768로 올립니다. |
| 긴 코딩 및 에이전트형 작업 | 65,536부터 시작합니다. |
| 어려운 수학, 과학, 연구, 증명 | 262,144부터 1,048,576에서 입력 토큰을 뺀 값까지의 값을 테스트합니다. |

토큰을 더 적게 사용하려면 `thinking_level`를 낮춥니다. 가장 어려운 추론 작업에는 `high`를 사용하세요. 대부분의 코딩 및 에이전트 작업에는 `medium` (기본값)를 사용하세요. 복잡성이 낮은 작업에는 `low`를 사용합니다.

## 장기 실행 요청 처리

Gemini 4 Argon은 어려운 문제에 대해 Gemini 3.x 모델보다 더 오래 생각하므로, 긴 요청이 조기에 연결 해제되지 않도록 클라이언트 제한 시간을 늘려야 합니다.

- **비스트리밍 호출:** 서버가 10분 후에 연결을 닫습니다.
- **스트리밍 호출:** 서버가 20분 후에 스트림을 닫습니다.
- **클라이언트 제한 시간:** HTTP 읽기 제한 시간을 20분으로 설정합니다. 3분 또는 5분 제한 시간으로 인해 요청이 일찍 중지됩니다.

Python에서 클라이언트의 제한 시간을 밀리초 단위로 설정합니다.

```
client = genai.Client(http_options=types.HttpOptions(timeout=1_200_000))  # 20 minutes
```

클라이언트가 폴링하는 작업의 경우 Interactions API는 서버에서 긴 디코딩을 실행합니다. [백그라운드 실행](https://ai.google.dev/gemini-api/docs/background-execution?hl=ko)을 참고하세요.

## 모델이 모든 출력 토큰을 사용할 때 재개

응답이 `MAX_TOKENS`로 끝나도 `continuation_token`는 계속 포함됩니다. 다음 두 가지 중에서 선택할 수 있습니다.

- **계속:** 토큰과 더 높은 `max_output_tokens`를 사용하여 동일한 요청을 보냅니다. 값은 지금까지 사용된 토큰보다 커야 합니다. 그렇지 않으면 API에서 400 오류를 반환합니다.
- **다시 시작:** 더 높은 `max_output_tokens`와 토큰 없이 원래 요청을 전송합니다. 두 실행 모두에 대해 비용을 지불합니다.

## 토큰 집계

자동 연속을 사용하면 `usage_metadata`에서 모든 홉의 합계를 보고합니다. SDK는 모든 개수 필드(`prompt_token_count`, `cached_content_token_count`, `candidates_token_count`, `thoughts_token_count`, `total_token_count`)를 합산합니다.

`prompt_token_count`는 모든 홉의 입력 토큰을 합산합니다. 각 홉은 프롬프트와 지금까지 생성된 모든 항목을 입력으로 모델에 다시 전송하므로 이후의 모든 홉에서 동일한 토큰이 다시 계산됩니다. 예를 들어 Google GenAI SDK를 사용하면 200,000개의 사고 및 출력 토큰을 생성하는 1,000개의 토큰 프롬프트는 4번의 홉을 거칩니다.

| Hop | 모델에 전송된 입력 | 입력 토큰 |
| --- | --- | --- |
| 1 | 프롬프트 | 1,000 |
| 2 | 프롬프트 + 홉 1 | 66,536 |
| 3 | 프롬프트 + 1, 2단계 | 132,072 |
| 4 | 프롬프트 + 홉 1~3 | 197,608 |
| **합계** |  | **397,216** |

`prompt_token_count`는 약 397,000개의 토큰을 보고하고(암시적 캐싱에 의해 반복된 홉 입력이 자동으로 95% 할인됨), `total_token_count`는 약 597,000개의 토큰을 보고합니다. 실제 컨텍스트 크기는 약 201,000개의 토큰(1,000개의 토큰 프롬프트와 200,000개의 사고 및 출력 토큰)에 불과합니다. 스트리밍되지 않는 REST 루프는 32K 홉을 사용하므로 동일한 출력에 7홉이 필요하며 695,128개의 입력 토큰을 보고합니다.

| 모델을 호출하는 방법 | `usage_metadata`에 표시되는 정보 | 비용 | 프롬프트 크기 |
| --- | --- | --- | --- |
| Google GenAI SDK, 자동 연속 (기본값) | 모든 홉의 합계 | 사용 필드를 있는 그대로 읽습니다. | `usage_metadata.initial_prompt_token_count` (Python) 또는 `usageMetadata.initialPromptTokenCount` (JavaScript)을 읽습니다. |
| `automatic_continuation=False`가 포함된 SDK 또는 REST | 응답당 홉 1개 | 홉 전체에 각 필드를 추가합니다. | 첫 번째 홉에서 `prompt_token_count`을 읽습니다. |

`prompt_token_count` 및 `total_token_count`는 컨텍스트의 크기가 아니라 모든 홉의 합계입니다. 대화 기록을 요약하거나 자르는 시점 (컨텍스트 압축)을 결정하거나 컨텍스트 한도를 적용하는 데 사용하지 마세요. 컨텍스트 크기를 추정하려면 표의 프롬프트 크기를 `candidates_token_count` 및 `thoughts_token_count`에 추가합니다.

긴 디코딩을 실행하기 전에 에이전트 프레임워크, 평가 도구 또는 프록시를 업데이트합니다.

- **에이전트 및 평가 도구:** 코드에서 컨텍스트를 압축하거나 토큰 한도에서 실행을 중지하는 경우 합산된 `prompt_token_count` 대신 `initial_prompt_token_count` (또는 REST의 첫 번째 홉의 `prompt_token_count`)를 사용합니다. 한 번에 완료되는 응답은 두 필드에 동일한 값을 보고하므로 짧은 테스트에서는 문제가 표시되지 않습니다.
- **REST를 호출하는 프록시 및 게이트웨이:** 각 REST 응답은 자체 홉만 보고합니다. 홉 간의 각 필드를 추가하여 비용을 계산하고 첫 번째 홉의 `promptTokenCount`를 프롬프트 크기로 유지합니다. 그렇지 않으면 사용자가 동일한 요청에 대해 SDK 사용자와 다른 숫자를 보게 됩니다.
- **로그 및 직렬화된 응답:** SDK는 클라이언트에서 `initial_prompt_token_count`를 계산합니다. REST 응답이나 SDK의 JSON 출력(예: `model_dump()`)에 없습니다. 나중에 필요하면 별도의 값으로 저장하세요.

자체 루프에서 스트리밍하는 경우 `usage_metadata`는 각 스트림 내에서 누적됩니다. 각 스트림의 마지막 값만 유지한 다음 홉 전체의 값을 더합니다.

## 청구 이해

생각만 포함된 홉을 포함하여 모든 홉의 모든 토큰에 대해 요금을 지불합니다.

- **캐시 할인:** 암시적 캐싱은 각 홉에서 반복되는 입력에 대해 95%의 할인을 제공합니다. 캐시된 입력 비용은 신규 할인 기간 동안 토큰 100만 개당 $2.00가 아닌 $0.10입니다.
- **캐시 만료:** 캐시는 사용하지 않고 15~20분이 지나면 만료됩니다. 홉 사이에 긴 일시중지가 있으면 전체 입력 속도가 다시 청구됩니다.
- **비스트리밍 홉 실패:** 대답이 완료된 경우에만 비용을 지불합니다. 실패하거나 중단된 요청에는 비용이 청구되지 않습니다.
- **삭제된 스트림:** 32,000개 토큰 전에 삭제된 스트림의 비용은 $0입니다. 그런 다음 마지막 체크포인트 토큰까지 지불합니다. 이 토큰부터 재개할 수 있기 때문입니다.

## 문제 해결

| 증상 | 원인 및 해결 방법 |
| --- | --- |
| `CONTINUATION`를 사용하면 출력이 64,000 또는 32,000에서 중지됨 | 모델에 토큰이 남아 있지만 요청이 계속되지 않았습니다. SDK를 업그레이드하거나 루프를 추가합니다. |
| `MAX_TOKENS`을 사용하면 출력이 64,000 또는 32,000에서 중지됨 | `max_output_tokens`가 설정되지 않았거나 너무 낮습니다. 65,536보다 큰 값으로 설정합니다. |
| `MAX_TOKENS`이(가) 있는 빈 텍스트 | 모델이 사고에 모든 토큰을 사용했습니다. `max_output_tokens`을 올리거나 `thinking_level`을 내립니다. |
| 400: '연속 토큰이 이미 출력 토큰을 사용했습니다…' | `max_output_tokens`이 지금까지 사용된 토큰보다 높지 않습니다. 우선순위(Raise)를 살펴보겠습니다. |
| `thinking_level: "minimal"` 또는 `thinking_level`가 있는 `thinking_budget`의 오류 | Gemini 4 Argon은 `minimal`을 지원하지 않습니다. `low`, `medium`, `high`을 사용합니다. `thinking_level` 또는 `thinking_budget`를 설정합니다(둘 다 아님). |
| `thinking_budget`, `temperature`, `top_p` 또는 `top_k`에 대한 경고 | Gemini 4 Argon은 이러한 필드를 무시하거나 매핑합니다. `thinking_level`를 사용하고 샘플링 파라미터를 삭제합니다. |
| 3분 또는 5분 후 요청 종료 | 클라이언트 제한 시간이 너무 짧습니다. 20분으로 설정해 줘. |
| 컨텍스트 압축이 너무 일찍 시작됨 | 하네스는 합산된 입력을 읽습니다. 대신 `initial_prompt_token_count`을(를) 읽어보세요. |

## 제한사항

- **OpenAI 호환성 엔드포인트:** 긴 디코드는 사용할 수 없습니다. 요청당 한도에서 출력이 중지됩니다.
- **이전 SDK:** 참고의 최소 버전보다 낮은 버전은 자동으로 계속되지 않습니다.
- **길이:** 모델이 토큰 길이 또는 단어 수 목표를 따르지 않습니다.

## 체크리스트

- Google GenAI SDK를 최소 버전으로 업그레이드합니다.
- `max_output_tokens`을 65,536보다 크게 설정합니다.
- `thinking_budget`가 아닌 `thinking_level` (`low`, `medium` 또는 `high`)를 사용합니다.
- HTTP 읽기 제한 시간을 20분으로 설정합니다.
- 컨텍스트 크기 및 압축에 `initial_prompt_token_count`를 사용합니다.
- 대규모 평가 전에 프롬프트 하나를 테스트로 실행합니다.

## 다음 단계

- [Gemini 4 Argon의 새로운 기능](https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=ko)
- [사고](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ko)
- [토큰 수 계산](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-10-13(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-10-13(UTC)"],[],[]]
