---
source_url: https://ai.google.dev/gemini-api/docs/long-decode?hl=ko
fetched_at: 2026-11-02T07:02:37.247946+00:00
title: "\uae34 \ub514\ucf54\ub529 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon을 지금 이용 가능합니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 긴 디코딩

긴 디코드를 사용하면 Gemini 4 Argon이 통합된 100만 토큰 컨텍스트 창 (입력, 사고,출력 전반에서 공유되는 1,048, 576개 토큰)까지 심층 추론 작업을 위해 64, 000개 이상의 토큰을 생성할 수 있습니다. Interactions API에서 백그라운드 실행으로 긴 디코드를 사용 설정하면 서버에서 각 64, 000개 홉을 자동으로 생성하고 단일 상호작용으로 결합합니다.

## 긴 디코드 작동 방식

단일 모델 호출은 최대 64,000개 토큰을 생성합니다. 응답에 64,000개 이상의 토큰이 필요한 경우 서버는 이전 홉이 중지된 지점에서 계속되는 64,000개 홉으로 생성합니다. 각 홉은 동일한 상호작용 ID 아래의 `interaction.steps`에 `model_output` 단계를 추가하므로 이러한 단계를 조인하여 전체 응답을 읽습니다.

1. `background: true` 및 65,536보다 큰 `max_output_tokens`(최대 100만)로 상호작용을 만듭니다.
2. 서버는 최대 64, 000개 토큰의 첫 번째 홉을 생성합니다.
3. 서버는 마지막 홉이 중지된 지점에서 다음 홉을 시작하고 모델이 완료되거나 모든 `max_output_tokens`를 사용할 때까지 반복합니다.
4. 상호작용을 폴링하거나 스트리밍하여 결과를 가져옵니다.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Write a complete, rigorous proof of the prime number theorem.",
    background=True,
    generation_config={
        "max_output_tokens": 262144,
        "thinking_level": "high",
    },
)

while interaction.status in ("in_progress", "queued"):
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Each hop adds a model_output step, so join the text of all of them.
text = "".join(
    content.text
    for step in interaction.steps
    if step.type == "model_output"
    for content in step.content
    if content.type == "text"
)
print(text)
print("Status:", interaction.status)
print("Usage:", interaction.usage)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Write a complete, rigorous proof of the prime number theorem.",
  background: true,
  generation_config: {
    max_output_tokens: 262144,
    thinking_level: "high",
  },
});

while (interaction.status === "in_progress" || interaction.status === "queued") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await client.interactions.get(interaction.id);
}

// Each hop adds a model_output step, so join the text of all of them.
const text = interaction.steps
  .filter((step) => step.type === "model_output")
  .flatMap((step) => step.content ?? [])
  .filter((content) => content.type === "text")
  .map((content) => content.text)
  .join("");
console.log(text);
console.log("Status:", interaction.status);
console.log("Usage:", interaction.usage);
```

### REST

```
# 1. Create the background interaction. It returns an ID right away.
ID=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a complete, rigorous proof of the prime number theorem.",
    "background": true,
    "generation_config": {"max_output_tokens": 262144, "thinking_level": "high"}
  }' | jq -r '.id')

# 2. Poll until the status is no longer in_progress or queued.
#    The REST response has no output_text field, so join the text of every model_output step.
while true; do
  RESP=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
  STATUS=$(echo "$RESP" | jq -r '.status')
  if [[ "$STATUS" != "in_progress" && "$STATUS" != "queued" ]]; then
    echo "$RESP" | jq -r '[.steps[]? | select(.type == "model_output") | .content[]? | select(.type == "text") | .text] | join("")'
    echo "$RESP" | jq '{status, usage}'
    break
  fi
  sleep 5
done
```

## 출력 한도

스트리밍 및 비스트리밍 상호작용은 기본적으로 64,000개 출력 토큰 한도로 설정되므로 최대 64,000개 토큰의 응답에는 코드 변경이 필요하지 않습니다. 64, 000개 이상의 토큰을 생성하려면 백그라운드 실행을 사용 설정하고 `max_output_tokens`를 늘립니다.

| 상호작용을 만드는 방법 | 출력 한도 |
| --- | --- |
| `background: false` (스트리밍 또는 비스트리밍) | 65,536개 토큰. 65,536보다 큰 값은 400 오류를 반환합니다. 긴 디코드가 곧 제공될 예정입니다. |
| `background: true`, `max_output_tokens`가 설정되지 않음 | 65,536개 토큰 |
| `background: true`, `max_output_tokens`가 65,536보다 큼 | 입력을 뺀 최대 1,048,576개의 `max_output_tokens` |

## 긴 디코드를 사용하는 경우

대부분의 요청은 64,000개 토큰 내에서 완료됩니다. 하나의 응답에 그보다 더 많은 사고와 출력이 필요한 경우에만 긴 디코드를 사용하세요.

| 워크로드 | 긴 디코드를 사용하시겠어요? | 이유 |
| --- | --- | --- |
| 어려운 수학, 과학, 연구, 공식 증명 | 예 | 모델은 추론을 탐색하고 확인하는 데 64,000개 이상의 토큰을 사용할 수 있습니다. |
| 가장 어려운 코딩 및 에이전트 작업 | 예 | 일부 작업에는 하나의 응답에 64,000개 이상의 사고 및 코드가 필요합니다. 대부분의 코딩 및 에이전트 작업은 64,000개 미만으로 완료됩니다. |
| 출력 한도에서 중지되는 평가 도구 | 예 | 긴 디코드는 모델이 사고에 전체 64,000개 응답을 사용하는 경우 잘린 답변을 방지합니다. |
| 채팅, Q&A, 요약, 분류, 추출 | 아니요 | 이러한 작업은 32,000개 토큰 미만으로 완료됩니다. |
| '70만 단어 책 쓰기'와 같은 고정 길이 요청 | 아니요 | 모델은 길이 타겟을 따르지 않습니다. |
| 짧은 턴으로 도구를 여러 번 호출하는 에이전트 | 아니요 | 각 턴은 짧습니다. 각 턴의 큰 출력은 공유 컨텍스트 창을 빠르게 채웁니다. |
| 입력 한도에 가까운 프롬프트 | 아니요 | 출력은 입력을 뺀 1,048,576개 토큰만 사용할 수 있습니다. |
| 지연 시간에 민감한 요청 | 아니요 | 긴 디코드는 몇 분 동안 실행될 수 있습니다. |

높은 `max_output_tokens`를 설정하면 모델이 어려운 문제에 대해 더 오래 생각할 수 있지만 모델은 여전히 작성할 양을 결정합니다. 모델이 사용하는 추론 노력을 제어하려면 [`thinking_level`](https://ai.google.dev/gemini-api/docs/thinking?hl=ko)을 설정하세요.

## 긴 디코드 실행 방법 선택

백그라운드 실행은 Interactions API에서 긴 디코드를 실행하는 가장 쉬운 방법입니다. 코드에서 각 홉을 시작하는 클라이언트 측 연속은 GenerateContent API에서 사용할 수 있습니다. 자체 복원력을 관리하는 고급 옵션으로 Interactions API에 곧 출시될 예정입니다.

|  | 백그라운드 실행 (Interactions API) | 클라이언트 측 연속 (GenerateContent API) |
| --- | --- | --- |
| **각 홉을 시작하는 사용자** | Google 서버 | Google 생성형 AI SDK 또는 자체 코드 |
| **요청당 토큰 수** | 하나의 상호작용에서 `max_output_tokens` | 스트림당 64,000개, 비스트리밍 요청당 32,000개 |
| **실행 시간** | 최대 24시간 | 20분 |
| **스토리지** | `store: true` 필요 | 서버에 저장된 항목이 없습니다. |
| **권장** | 긴 디코드를 실행하는 가장 쉬운 방법 | 재시도를 세밀하게 제어하여 자체 백오프, 오류 처리, 복원력을 빌드할 수 있습니다. |

클라이언트 측 연속을 사용하려면 [GenerateContent API를 사용한 긴 디코드](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=ko)를 참고하세요.

## 긴 디코드 스트리밍

출력 및 사고 요약을 도착하는 대로 스트리밍하려면 `stream: true` 및 `thinking_summaries: "auto"`를 추가하세요. 긴 스트림은 삭제될 수 있으므로 클라이언트가 다시 연결해야 합니다. [백그라운드 실행 가이드](https://ai.google.dev/gemini-api/docs/background-execution?hl=ko)의 다시 연결 패턴을 따르세요. 긴 디코드는 다음 규칙을 추가합니다.

- **상호작용 ID 저장:** `interaction.created` 이벤트에서 읽습니다.
- **모든 `event_id` 저장:** `event_id`는 텍스트 델타뿐만 아니라 `interaction.status_update` 이벤트에서도 도착할 수 있습니다.
- **`last_event_id`로 다시 연결:** `interactions.get` 및 마지막 `event_id`로 `stream: true`을 호출합니다. 스트림은 해당 이벤트 후에 계속됩니다.
- **끝까지 읽기:** 다시 연결한 후 상태를 확인하기 전에 스트림을 끝까지 읽습니다. 서버는 상호작용이 완료된 후에도 누락된 이벤트를 재생합니다.
- **긴 제한 시간 설정:** 스트림당 HTTP 읽기 제한 시간을 15~20분으로 설정합니다.
- **5,000개 토큰 청크로 출력 예상:** 처음 64,000개 토큰 (약 처음 10분) 후 스트림은 약 5,000개 토큰의 청크로 출력을 전송합니다. 청크 간의 일시중지는 정상입니다. 상호작용이 중지되지 않으므로 연결을 열어 두세요.

## 백그라운드 상태

백그라운드 상호작용은 최대 24시간 동안 실행될 수 있습니다. 상태가 더 이상 `in_progress` 또는 `queued`가 아니면 이 표를 사용하여 최종 상태를 처리합니다.

| 상태 | 의미 | 필요한 조치 |
| --- | --- | --- |
| `completed` | 모델이 완료되었습니다. | `steps`에서 `model_output` 단계를 조인하고 `usage`를 읽습니다. 대화를 계속하려면 이 상호작용의 `id`를 `previous_interaction_id`로 전달합니다. |
| `requires_action` | 모델이 도구 호출을 요청했습니다. | 도구를 실행합니다. 그런 다음 이 상호작용의 `id`로 결과를 전송합니다. |
| `incomplete` | 모델이 모든 `max_output_tokens`를 사용했습니다. 모델이 여전히 사고 중인 경우 텍스트가 비어 있을 수 있습니다. | 더 높은 `max_output_tokens`로 요청을 다시 전송합니다. |
| `failed` | 서버가 완료할 수 없거나 상호작용이 24시간 넘게 실행되었습니다. | 요청을 다시 시도하세요. 다시 실패하면 상호작용 `id`를 지원팀과 공유하세요. |
| `cancelled` | 상호작용을 취소했습니다. | `usage`를 읽어 청구된 토큰을 확인합니다. |

실행 중인 상호작용을 중지하려면 Python에서 `client.interactions.cancel(id=interaction.id)`, JavaScript에서 `client.interactions.cancel(interaction.id)`, REST에서 `POST /v1beta/interactions/{id}/cancel`을 호출합니다.

## `max_output_tokens` 설정

`max_output_tokens`는 상호작용 전반에서 사고 및 출력의 결합된 한도를 설정합니다. 이를 낮춘다고 해서 모델이 더 간결하게 사고하는 것은 아니며 대신 응답이 더 빨리 잘립니다.

| 워크로드 | 권장 `max_output_tokens` |
| --- | --- |
| 한도가 32,000 미만인 기존 앱 | 32,768로 늘립니다. 백그라운드 실행은 필요하지 않습니다. |
| 긴 코딩 및 에이전트 작업 | 65,536 (기본값)부터 시작합니다. 백그라운드 실행은 필요하지 않습니다. |
| 복잡한 추론, 어려운 수학, 과학, 증명 | `background: true`를 설정하고 262,144부터 시작하여 입력 토큰을 뺀 최대 1,048,576까지 설정합니다. |

토큰을 더 적게 사용하려면 `thinking_level`을 낮추세요. 가장 어려운 추론 작업에는 `high`를 사용하세요. 대부분의 코딩 및 에이전트 작업에는 `medium` (기본값)을 사용하세요.

## 토큰 집계

`interaction.usage`는 모든 홉의 합계를 보고합니다. `total_input_tokens`, `total_cached_tokens`, `total_output_tokens`, `total_thought_tokens`, `total_tokens` 필드를 읽습니다.

`total_input_tokens`는 모든 홉의 입력 토큰을 합산합니다. 각 홉은 프롬프트와 지금까지 생성된 모든 항목을 입력으로 모델에 다시 전송하므로 동일한 토큰이 이후의 모든 홉에서 다시 집계됩니다. 예를 들어 200,000개 토큰의 사고 및 출력을 생성하는 1,000개 토큰 프롬프트는 4개의 홉을 사용합니다.

| 홉 | 모델에 전송된 입력 | 입력 토큰 |
| --- | --- | --- |
| 1 | 프롬프트 | 1,000 |
| 2 | 프롬프트 + 홉 1 | 66,536 |
| 3 | 프롬프트 + 홉 1 및 2 | 132,072 |
| 4 | 프롬프트 + 홉 1~3 | 197,608 |
| **합계** |  | **397,216** |

`total_input_tokens`는 실제 컨텍스트 크기가 1,000개 토큰 프롬프트와 200,000개 토큰의 사고 및 출력인 약 201,000개 토큰에 불과하지만 약 397,000개 토큰 (반복되는 홉 입력은 암시적 캐싱으로 95% 자동 할인)을 보고합니다.

스트림 중에 `step.stop` 및 `interaction.status_update` 이벤트 모두 `usage` (상호작용의 누적)를 포함합니다. 이를 함께 추가하는 대신 최신 `usage` 값을 읽으세요.

## 청구 이해

사고만 포함된 홉을 포함하여 모든 홉의 모든 토큰에 대해 비용을 지불합니다.

- **캐시 할인:** 암시적 캐싱은 각 홉에서 반복되는 입력을 95% 할인합니다. 캐시된 입력 비용은 프로모션 기간 동안 200만 토큰당 2달러가 아닌 100만 토큰당 0.10달러입니다.
- **취소되고 실패한 상호작용:** 상호작용이 종료되기 전에 완료된 모든 작업에 대해 비용을 지불합니다.

## 문제 해결

| 증상 | 원인 및 해결 방법 |
| --- | --- |
| 출력이 64,000에서 중지됨 | `background`가 `false`이거나 `max_output_tokens`가 설정되지 않았습니다. `background: true` 및 `max_output_tokens`를 65,536보다 크게 설정합니다. |
| 400: 'max\_output\_tokens가 65536보다 큰 값은 아직 background=false에서 지원되지 않습니다.' | 백그라운드 실행이 없는 긴 디코드는 아직 사용할 수 없습니다. `background: true`를 설정합니다. |
| 400: '백그라운드 상호작용에는 store=true가 필요합니다.' | 백그라운드 실행에는 `store: true`가 필요합니다. |
| 텍스트가 비어 있는 상태 `incomplete` | 모델이 사고에 모든 토큰을 사용했습니다. `max_output_tokens`를 늘리거나 `thinking_level`을 낮춥니다. |
| 컨텍스트 압축이 너무 일찍 시작됨 | 에이전트 프레임워크 또는 평가 도구가 `total_input_tokens`를 읽습니다. [토큰 집계](#count-tokens)를 참고하세요. |

## 제한사항

- **백그라운드 실행이 없는 긴 디코드 없음:** `background: false`가 있는 상호작용은 65,536개 토큰에서 중지됩니다. 곧 지원될 예정입니다.
- **길이 타겟 없음:** 모델은 토큰 길이 또는 단어 수 타겟을 따르지 않습니다.

## 다음 단계

- [Gemini 4 Argon의 새로운 기능](https://ai.google.dev/gemini-api/docs/latest-model?hl=ko)
- [백그라운드 실행](https://ai.google.dev/gemini-api/docs/background-execution?hl=ko)
- [사고](https://ai.google.dev/gemini-api/docs/thinking?hl=ko)
- [GenerateContent API를 사용한 긴 디코드](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-10-13(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-10-13(UTC)"],[],[]]
