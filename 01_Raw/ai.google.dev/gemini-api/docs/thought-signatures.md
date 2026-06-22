---
source_url: https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ko
fetched_at: 2026-06-22T06:27:18.886808+00:00
title: "\uc0dd\uac01 \uc11c\uba85 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 생각 서명

생각 서명은 모델의 내부 사고 과정을 암호화한 표현으로, 다단계 상호작용 전반에서 추론 컨텍스트를 유지하는 데 사용됩니다.
사고 모델 (예: Gemini 3 및 2.5 시리즈)을 사용하는 경우 API는 응답의 [콘텐츠 파트](https://ai.google.dev/api/caching?hl=ko#Part) (예: `text` 또는 `functionCall` 파트) 내에 `thoughtSignature` 필드를 반환할 수 있습니다.

일반적으로 모델 응답에서 생각 서명을 수신하면 다음 턴에서 대화 기록을 보낼 때 수신한 그대로 다시 전달해야 합니다.
**Gemini 3 모델을 사용하는 경우 함수 호출 중에 생각 서명을 다시 전달해야 합니다. 그렇지 않으면 유효성 검사 오류가 발생합니다** (4xx 상태 코드).
여기에는 Gemini 3 Flash에 `minimal`
[사고 수준](https://ai.google.dev/gemini-api/docs/thinking?hl=ko#thinking-levels) 설정을 사용하는 경우도 포함됩니다.

## 작동 방식

아래 그래픽은 Gemini API의 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)과 관련된 '턴'과 '단계'의 의미를 시각화합니다. '턴'은 사용자와 모델 간의 대화에서 완전한 하나의 교환입니다. '단계'는 모델이 실행하는 더 세부적인 작업 또는 작업으로, 턴을 완료하기 위한 더 큰 프로세스의 일부인 경우가 많습니다.

![함수 호출 턴 및 단계 다이어그램](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=ko)

*이 문서에서는 Gemini 3 모델의 함수 호출 처리에 중점을 둡니다. 2.5와의 차이점은 [모델 동작](#model-behavior) 섹션을 참고하세요.*

Gemini 3는 함수 호출이 포함된 모든 모델 응답 (API의 응답)에 대해 생각 서명을 반환합니다. 생각 서명은 다음 경우에 표시됩니다.

- [병렬 함수](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko#parallel_function_calling) 호출이 있는 경우 모델 응답에서 반환되는 첫 번째 함수 호출 파트에 생각 서명이 포함됩니다.
- 순차적 (다단계) 함수 호출이 있는 경우 각 함수 호출에는 서명이 포함되며 모든 서명을 다시 전달해야 합니다.
- 함수 호출이 없는 모델 응답의 경우, 모델에서 반환된 마지막 파트 내부에 생각 서명이 포함되어 반환됩니다.

다음 표에서는 턴과 단계의 정의를 위에 소개된 서명 개념과 결합하여 다단계 함수 호출을 시각화합니다.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Turn** | **단계** | **사용자 요청** | **모델 응답** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | 없음 |

## 함수 호출 부분의 서명

Gemini가 `functionCall`를 생성할 때 다음 턴에서 도구의 출력을 올바르게 처리하기 위해 `thought_signature`를 사용합니다.

- **행동**:
  - **단일 함수 호출**: `functionCall` 부분에 `thought_signature`가 포함됩니다.
  - **병렬 함수 호출**: 모델이 응답에서 병렬 함수 호출을 생성하는 경우 `thought_signature`는 **첫 번째**
    `functionCall` 부분에만 연결됩니다. 동일한 대답의 후속 `functionCall` 부분에는 서명이 포함되지 **않습니다**.
- **요구사항**: 대화 기록을 다시 보낼 때는 이 서명을 수신했던 바로 그 파트에 정확히 **반환해야 합니다**.
- **유효성 검사**: 현재 턴 내의 모든 함수 호출에 엄격한 유효성 검사가 적용됩니다 . (현재 턴만 필요하며 이전 턴은 검증하지 않음)
  - API는 기록 (최신에서 오래된 순)으로 돌아가 표준 콘텐츠 (예: `text`)가 포함된 가장 최근 **User** 메시지(현재 턴의 시작)를 찾습니다. `functionResponse`이 **be**.
  - 해당 특정 사용 메시지 이후에 발생하는 **모든** 모델 `functionCall`은 턴의 일부로 간주됩니다.
  - 현재 턴의 **각 단계**의 **첫 번째** `functionCall` 부분에는 `thought_signature`가 포함되어야 **합니다**.
  - 현재 턴의 단계에서 첫 번째 `functionCall` 부분에 필요한 `thought_signature`를 누락하면 400 오류가 발생하여 요청이 실패합니다.
- **올바른 서명이 반환되지 않으면 다음과 같이 오류가 발생합니다**
  - Gemini 3 모델: 서명을 포함하지 않으면 400 오류가 발생합니다. 문구는 다음 형식입니다.
    - `<index of contents array>` 콘텐츠 블록의 `<Function Call>` 함수 호출에 `thought_signature`가 누락되었습니다. 예를 들어 *`1.` 콘텐츠 블록의 `FC1` 함수 호출에 `thought_signature`이 누락되었습니다.*

### 순차적 함수 호출 예시

이 섹션에서는 사용자가 여러 작업이 필요한 복잡한 질문을 하는 여러 함수 호출의 예를 보여줍니다.

사용자가 여러 작업이 필요한 복잡한 질문(`"Check flight status for AA100 and
book a taxi if delayed"`)을 하는 멀티턴 함수 호출 예를 살펴보겠습니다.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Turn** | **단계** | **사용자 요청** | **모델 응답** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

다음 코드는 위 표의 시퀀스를 보여줍니다.

**턴 1, 1단계 (사용자 요청)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "check_flight",
          "description": "Gets the current status of a flight",
          "parameters": {
            "type": "object",
            "properties": {
              "flight": {
                "type": "string",
                "description": "The flight number to check"
              }
            },
            "required": [
              "flight"
            ]
          }
        },
        {
          "name": "book_taxi",
          "description": "Book a taxi",
          "parameters": {
            "type": "object",
            "properties": {
              "time": {
                "type": "string",
                "description": "time to book the taxi"
              }
            },
            "required": [
              "time"
            ]
          }
        }
      ]
    }
  ]
}
```

**턴 1, 1단계 (모델 응답)**

```
{
"content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>"
          }
        ]
  }
}
```

**턴 1, 2단계(사용자 응답 - 도구 출력 전송)** 이 사용자 턴에는 새로운 텍스트 없이 `functionResponse`만 포함되어 있으므로 아직 턴 1입니다. `<Signature_A>`을 보존해야 합니다.

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
                }
              }
            }
        ]
}
```

**1턴, 2단계 (모델)** 이제 모델이 이전 도구 출력을 기반으로 택시를 예약하기로 결정합니다.

```
{
      "content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>"
          }
        ]
      }
}
```

**턴 1, 3단계 (사용자 - 도구 출력 전송)** 택시 예약 확인을 전송하려면 이 루프의 **모든** 함수 호출에 대한 서명(`<Signature A>` + `<Signature B>`)을 반드시 포함해야 합니다.

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
              }
              }
            }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "book_taxi",
              "response": {
                "booking_status": "success"
              }
              }
            }
        ]
    }
}
```

### 병렬 함수 호출 예시

사용자가 모델이 검증을 수행하는 위치를 확인하기 위해 `"Check weather in Paris and London"`에 요청하는 병렬 함수 호출 예시를 살펴보겠습니다.

| **Turn** | **단계** | **사용자 요청** | **모델 응답** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ('파리') + 서명  FC2 ('런던') | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (FC 없음) | 없음 |

다음 코드는 위 표의 시퀀스를 보여줍니다.

**턴 1, 1단계 (사용자 요청)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "get_current_temperature",
          "description": "Gets the current temperature for a given location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco"
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**턴 1, 1단계 (모델 응답)**

```
{
  "content": {
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "Paris"
          }
        },
        "thoughtSignature": "<Signature_A>"// INCLUDED on First FC
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "London"
          }// NO signature on subsequent parallel FCs
        }
      }
    ]
  }
}
```

**턴 1, 2단계 (사용자 응답 - 도구 출력 전송)** 첫 번째 파트에 있는 `<Signature_A>`는 받은 그대로 유지해야 합니다.

```
[
  {
    "role": "user",
    "parts": [
      {
        "text": "Check the weather in Paris and London."
      }
    ]
  },
  {
    "role": "model",
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "Paris"
          }
        },
        "thought_signature": "<Signature_A>" // MUST BE INCLUDED
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "London"
          }
        }
      } // NO SIGNATURE FIELD
    ]
  },
  {
    "role": "user",
    "parts": [
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "15C"
          }
        }
      },
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "12C"
          }
        }
      }
    ]
  }
]
```

## `functionCall`이 아닌 부분의 서명

Gemini는 함수 호출이 아닌 부분의 응답 마지막 부분에 `thought_signatures`를 반환할 수도 있습니다.

- **동작**: 모델에서 반환하는 최종 콘텐츠 부분 (`text, inlineData…`)에 `thought_signature`이 포함될 수 있습니다.
- **권장사항**: 이 서명을 반환하는 것 모델이 특히 복잡한 지침을 따르거나 시뮬레이션된 에이전트형 워크플로에서 고품질 추론을 유지하도록 보장하기 위해 **권장**됩니다.
- **유효성 검사**: API는 유효성 검사를 엄격하게 적용하지 **않습니다**. 이를 생략하더라도 차단 오류는 발생하지는 않지만, 성능이 저하될 수 있습니다.

### 텍스트/맥락 내 추론 (검증 없음)

**턴 1, 1단계 (모델 응답)**

```
{
  "role": "model",
  "parts": [
    {
      "text": "I need to calculate the risk. Let me think step-by-step...",
      "thought_signature": "<Signature_C>" // OPTIONAL (Recommended)
    }
  ]
}
```

**턴 2, 1단계 (사용자)**

```
[
  { "role": "user", "parts": [{ "text": "What is the risk?" }] },
  {
    "role": "model", 
    "parts": [
      {
        "text": "I need to calculate the risk. Let me think step-by-step...",
        // If you omit <Signature_C> here, no error will occur.
      }
    ]
  },
  { "role": "user", "parts": [{ "text": "Summarize it." }] }
]
```

## 사고 보존 및 토큰 사용량

**Gemini 3.5 Flash부터** 모델은 대화 기록에 사고 서명이 있는 경우 이전 모든 턴의 추론 컨텍스트를 사용합니다.

사고 보존을 사용 설정하려면 요청의 `contents` 배열에 **수정되지 않은 전체 대화 기록** (이전 모델 턴에서 반환된 `thought_signature` 필드 포함)을 전달하세요.

### 토큰 사용 관리

여러 턴에 걸쳐 중간 생각을 유지하면 모델이 이전 턴의 생각 서명을 파싱해야 하므로 후속 턴의 입력 토큰 수가 증가합니다.

애플리케이션이 간단한 질문을 수행하거나 긴 대화에서 비용을 최소화하려는 경우 대화 기록에서 이전 생각 서명을 삭제하면 됩니다.

## OpenAI 호환성 서명

다음 예에서는 [OpenAI 호환성](https://ai.google.dev/gemini-api/docs/openai?hl=ko)을 사용하여 채팅 완성 API의 사고 서명을 처리하는 방법을 보여줍니다.

### 순차적 함수 호출 예시

다음은 사용자가 여러 작업이 필요한 복잡한 질문을 하는 다중 함수 호출의 예입니다.

사용자가 `Check flight status for AA100 and book a taxi if delayed`라고 묻는 멀티턴 함수 호출 예를 살펴보고 사용자가 여러 태스크가 필요한 복잡한 질문을 할 때 어떤 일이 일어나는지 확인해 보겠습니다.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Turn** | **단계** | **사용자 요청** | **모델 응답** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

다음 코드는 지정된 시퀀스를 안내합니다.

**턴 1, 1단계 (사용자 요청)**

```
{
  "model": "google/gemini-3.1-pro-preview",
  "messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "check_flight",
        "description": "Gets the current status of a flight",
        "parameters": {
          "type": "object",
          "properties": {
            "flight": {
              "type": "string",
              "description": "The flight number to check."
            }
          },
          "required": [
            "flight"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "book_taxi",
        "description": "Book a taxi",
        "parameters": {
          "type": "object",
          "properties": {
            "time": {
              "type": "string",
              "description": "time to book the taxi"
            }
          },
          "required": [
            "time"
          ]
        }
      }
    }
  ]
}
```

**턴 1, 1단계 (모델 응답)**

```
{
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>"
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    }
```

**턴 1, 2단계 (사용자 응답 - 도구 출력 전송)**

이 사용자 턴에는 새로운 텍스트 없이 `functionResponse`만 포함되어 있으므로 아직 턴 1이며 `<Signature_A>`을 보존해야 합니다.

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    }
  ]
```

**턴 1, 2단계 (모델)**

이제 모델은 이전 도구 출력을 기반으로 택시를 예약하기로 결정합니다.

```
{
"role": "model",
"tool_calls": [
{
"extra_content": {
"google": {
"thought_signature": "<Signature B>"
}
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-2",
            "type": "function"
          }
       ]
}
```

**턴 1, 3단계 (사용자 - 도구 출력 전송)**

택시 예약 확인을 전송하려면 이 루프의 모든 함수 호출 (`<Signature A>` + `<Signature B>`)에 대한 서명을 포함해야 합니다.

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature B>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "book_taxi",
      "tool_call_id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
      "content": "{\"booking_status\":\"success\"}"
    }
  ]
```

### 병렬 함수 호출 예시

사용자가 `"Check weather in Paris and London"`를 요청하는 병렬 함수 호출 예시를 살펴보겠습니다. 모델이 검증을 수행하는 위치를 확인할 수 있습니다.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Turn** | **단계** | **사용자 요청** | **모델 응답** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

다음은 지정된 시퀀스를 안내하는 코드입니다.

**턴 1, 1단계 (사용자 요청)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "get_current_temperature",
          "description": "Gets the current temperature for a given location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco"
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**턴 1, 1단계 (모델 응답)**

```
{
"role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Signature returned
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": {
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function" // No signature on Parallel FC
          }
        ]
}
```

**턴 1, 2단계 (사용자 응답 - 도구 출력 전송)**

첫 번째 파트에 있는 `<Signature_A>`는 받은 그대로 유지해야 합니다.

```
"messages": [
    {
      "role": "user",
      "content": "Check the weather in Paris and London."
    },
    {
      "role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": { //No Signature
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function"
          }
        ]
    },
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
      "content": "{\"temp\":\"15C\"}"
    },    
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
      "content": "{\"temp\":\"12C\"}"
    }
  ]
```

## FAQ

1. **현재 턴과 단계에 함수 호출 부분이 있는 경우 다른 모델의 기록을 Gemini 3로 전송하려면 어떻게 해야 하나요? API에서 생성되지 않아 연결된 사고 서명이 없는 함수 호출 부분을 제공해야 하나요?**

   요청에 맞춤 함수 호출 블록을 삽입하는 것은 적극 권장되지 않지만, 클라이언트에서 결정적으로 실행된 함수 호출 및 응답에 관한 정보를 모델에 제공하거나 생각 서명이 포함되지 않은 다른 모델의 트레이스를 전송하는 등 피할 수 없는 경우에는 생각 서명 필드에 `"context_engineering_is_the_way_to_go"` 또는 `"skip_thought_signature_validator"`의 더미 서명을 설정하여 유효성 검사를 건너뛸 수 있습니다.
2. **인터리브된 병렬 함수 호출 및 응답을 다시 전송하고 있는데 API에서 400을 반환합니다. 이유가 무엇인가요?**

   API가 병렬 함수 호출 'FC1 + 서명, FC2'를 반환하는 경우 예상되는 사용자 응답은 'FC1 + 서명, FC2, FR1, FR2'입니다. 'FC1 + 서명, FR1, FC2, FR2'와 같이 인터리브된 경우 API는 400 오류를 반환합니다.
3. **스트리밍 중이고 모델이 함수 호출을 반환하지 않으면 생각 서명을 찾을 수 없습니다.**

   스트리밍 요청이 있는 FC를 포함하지 않는 모델 응답 중에 모델은 텍스트 콘텐츠 부분이 비어 있는 부분에 생각 서명을 반환할 수 있습니다. 모델에서 `finish_reason`가 반환될 때까지 전체 요청을 파싱하는 것이 좋습니다.

## 다양한 모델의 생각 서명

[Gemini 3 모델](https://ai.google.dev/gemini-api/docs/models?hl=ko#gemini-3)과 Gemini 2.5 모델은 사고 서명과 관련해 다르게 작동합니다.

- **사고 보존**:
  - **Gemini 3.5 Flash부터** 모델은 대화 기록에 사고 서명이 있는 경우 이전 모든 턴의 추론 컨텍스트를 사용합니다.
  - 이전 모델은 동일한 방식으로 이전 턴의 추론 컨텍스트를 사용하지 않습니다.
- **대답에 함수 호출이 있는 경우**:
  - Gemini 3에는 항상 첫 번째 함수 호출 부분에 서명이 있습니다.
    이 부분을 반환하는 것은 **필수**입니다.
  - Gemini 2.5는 유형과 관계없이 첫 번째 부분에 서명이 있습니다. 이 부분을 반환하는 것은 **선택사항**입니다.
- **대답에 함수 호출이 없는 경우**:
  - 모델이 생각을 생성하는 경우 Gemini 3의 서명이 마지막 부분에 표시됩니다.
  - Gemini 2.5에는 어떤 부분에도 서명이 없습니다.

자세한 비교 내용은 [사고](https://ai.google.dev/gemini-api/docs/thinking?hl=ko#signatures) 페이지를 참고하세요.
Gemini 3 Image 모델의 경우 [이미지 생성](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko#thinking-process) 가이드의 사고 과정 섹션을 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-19(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-19(UTC)"],[],[]]
