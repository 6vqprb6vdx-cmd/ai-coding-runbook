---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko
fetched_at: 2026-08-31T06:38:34.952322+00:00
title: "\uae30\ubcf8 \uc81c\uacf5 \ub3c4\uad6c\uc640 \ud568\uc218 \ud638\ucd9c \uacb0\ud569 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 기본 제공 도구와 함수 호출 결합

Gemini는 도구 호출의 컨텍스트 기록을 보존하고 노출하여 단일 상호작용에서 [기본 제공 도구](https://ai.google.dev/gemini-api/docs/tools?hl=ko)(예: `google_search`)과 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)(*커스텀 도구*라고도 함)을 결합할 수 있습니다. 기본 제공 도구와 커스텀 도구 조합을 사용하면 복잡한 에이전트 워크플로가 가능합니다. 예를 들어 모델은 특정 비즈니스 로직을 호출하기 전에 실시간 웹 데이터를 기반으로 자체적으로 접지할 수 있습니다.

`google_search` 및 커스텀 함수 `getWeather`를 사용하여 기본 제공 도구와 커스텀 도구 조합을 사용 설정하는 예는 다음과 같습니다.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.6-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## 작동 방식

Gemini 3 모델은 *도구 컨텍스트 순환* 을 사용하여 기본 제공 도구와 커스텀 도구 조합을 사용 설정합니다. 도구 컨텍스트 순환을 사용하면 기본 제공 도구의 컨텍스트를 보존하고 노출하여 동일한 상호작용에서 커스텀 도구와 공유할 수 있습니다.

### 도구 조합 사용 설정

- 조합 동작을 트리거하려면 사용하려는 기본 제공 도구와 함께 [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko#function-declarations)를 포함합니다.

### API 반환 단계

상호작용 응답에서 API는 기본 제공 도구 호출과 함수 (커스텀 도구) 호출에 대해 별도의 단계를 반환합니다.

- **기본 제공 도구 단계**: API는 이러한 단계를 자동으로 관리하여
  턴 간에 컨텍스트를 보존합니다.
- **함수 호출 단계**: API는 커스텀 함수에 대해 `function_call` 단계를 반환합니다. 함수를 실행하고 결과를 다시 제공합니다.

### 반환된 단계의 중요 필드

반환된 단계의 특정 필드는 도구 컨텍스트를 유지하고 도구 조합을 사용 설정하는 데 중요합니다.

- **`id`**: `function_call` 및 `function_response` 단계에서 찾을 수 있습니다. 호출을 응답에 매핑하는 고유 식별자입니다.
- **`signature`**: Gemini 3+ 모델의 모든 도구 호출 (예: `function_call`) 및 결과 (예: `function_response`) 단계뿐만 아니라 `thought` 단계에서도 찾을 수 있습니다. 이 암호화된 컨텍스트를 사용하면 상호작용 전반에서 **도구 컨텍스트 순환** 이 가능합니다.

**이러한 필드 관리:**

- **스테이트풀 모드 (권장)**: `previous_interaction_id`를 사용하면 서버에서 `id` 및 `signature` 필드를 모두 자동으로 처리합니다.
- **스테이트리스 모드**: 대화 기록을 수동으로 관리할 때는 진위성을 검증하고 컨텍스트를 유지하기 위해 후속 요청에서 `id` 및 `signature` 필드를 모두 모델에 다시 전달해야 합니다. 전체 응답 객체를 기록에 다시 전달하면 공식 SDK에서 이 작업을 자동으로 처리합니다.

### 도구별 데이터

일부 기본 제공 도구는 도구 유형과 관련된 사용자에게 표시되는 데이터 인수를 반환합니다.

| 도구 | 사용자에게 표시되는 도구 호출 인수 (있는 경우) | 사용자에게 표시되는 도구 응답 (있는 경우) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` 탐색할 URL | `status`: 탐색 상태 `retrieved_url`: 탐색된 URL |
| **file\_search** | 없음 | 없음 |

## 토큰 및 가격 책정

요청의 기본 제공 도구 호출 부분은 `prompt_token_count`에 포함됩니다. 이제 이러한 중간 도구 단계를 볼 수 있고 사용자에게 반환되므로 대화 기록의 일부입니다. 이는 *응답*이 아닌
*요청*에만 해당합니다.

Google 검색 도구는 이 규칙에서 제외됩니다. Google 검색은 이미
쿼리 수준에서 자체 가격 책정 모델을 적용하므로 토큰이
이중 청구되지 않습니다 ([가격 책정](https://ai.google.dev/gemini-api/docs/pricing?hl=ko) 페이지 참고).

자세한 내용은 [토큰](https://ai.google.dev/gemini-api/docs/tokens?hl=ko) 페이지를 참고하세요.

## 제한사항

- 도구 컨텍스트 순환이 사용 설정된 경우 `validated` 모드가 기본값입니다 (`auto` 모드는 지원되지 않음).
- `google_search`와 같은 기본 제공 도구는 위치 및 현재 시간 정보를 사용하므로 `system_instruction` 또는 `function_declaration.description`에 위치 및 시간 정보가 충돌하는 경우 도구 조합 기능이 제대로 작동하지 않을 수 있습니다.

## 지원되는 도구

표준 도구 컨텍스트 순환은 서버 측 (기본 제공) 도구에 적용됩니다.
코드 실행도 서버 측 도구이지만 컨텍스트 순환을 위한 자체 기본 제공 솔루션이 있습니다. 컴퓨터 사용 및 함수 호출은 클라이언트 측 도구이며 컨텍스트 순환을 위한 기본 제공 솔루션도 있습니다.

| 도구 | 실행 측 | 컨텍스트 순환 지원 |
| --- | --- | --- |
| [Google 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko) | 서버 측 | 지원됨 |
| [Google 지도](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko) | 서버 측 | 지원됨 |
| [URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko) | 서버 측 | 지원됨 |
| [파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko) | 서버 측 | 지원됨 |
| [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko) | 서버 측 | 지원됨 (기본 제공, `code_execution` 및 `code_execution_result` 단계 사용) |
| [컴퓨터 사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko) | 클라이언트 측 | 지원됨 (기본 제공, `function_call` 및 `function_response` 단계 사용) |
| [커스텀 함수](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko) | 클라이언트 측 | 지원됨 (기본 제공, `function_call` 및 `function_response` 단계 사용) |

## 다음 단계

- Gemini API의 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)에 대해 자세히 알아보세요.
- 지원되는 도구를 살펴보세요.
  - [Google 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)
  - [Google 지도](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko)
  - [URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko)
  - [파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-30(UTC)"],[],[]]
