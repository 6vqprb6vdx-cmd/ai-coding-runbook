---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ko
fetched_at: 2026-09-07T05:31:56.281489+00:00
title: "\ubb38\uc81c \ud574\uacb0 \uac00\uc774\ub4dc \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 문제 해결 가이드

이 가이드를 사용하여 Gemini API를 호출할 때 발생하는 일반적인 문제를 진단하고 해결하세요. Gemini API 백엔드 서비스 또는 클라이언트 SDK에서 문제가 발생할 수 있습니다. 클라이언트 SDK는 다음 저장소에서 오픈소스화됩니다.

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

[API 키 문제가 발생하면
API 키 설정 가이드](https://ai.google.dev/gemini-api/docs/api-key?hl=ko)에 따라 API 키를 올바르게 설정했는지 확인하세요.

## 오류 코드

HTTP 상태 코드, 생성 차단 코드, 콘텐츠 오류 코드를 비롯한 모든 오류 코드의 전체 참조는
[API 오류](https://ai.google.dev/gemini-api/docs/api-errors?hl=ko) 페이지를 참고하세요.

## 재시도 전략

요청을 다시 시도해야 함을 나타내는 오류 (`429 RESOURCE_EXHAUSTED` 또는 `503 UNAVAILABLE` 등)가 발생하면 지수 백오프 전략을 구현하는 것이 좋습니다. 즉, 첫 번째 재시도 전에 잠시 기다린 후 후속 재시도 간의 대기 시간을 점차 늘립니다.

[Python SDK](https://github.com/googleapis/python-genai)와 같은 Gemini API의 공식 클라이언트 SDK에는 시간 초과, 네트워크 문제, 비율 제한 (`429` 및 `5xx` 상태 코드)과 같은 일시적인 오류를 처리하기 위한 지수 백오프가 포함된 자동 재시도 로직이 기본적으로 포함되어 있습니다. 예를 들어 Python SDK는 초기 지연 시간이 약 1초이고 최대 지연 시간이 60초인 일시적인 오류를 최대 4번 자동으로 재시도합니다.

직접 REST API 요청을 하거나 재시도 로직을 맞춤설정하는 경우 다음 권장사항을 따라 요청이 성공할 가능성을 높이고 서비스에 과부하가 걸리지 않도록 하세요.

- **지수 백오프 사용:** 첫 번째 재시도 전에 잠시 기다린 후 (예: 1초) 지수적으로 지연 시간을 늘립니다 (예: 2초, 4초, 8초).
- **지터 추가:** 모든 클라이언트가 정확히 동시에 재시도하지 않도록 지연 시간에 임의의 '지터'를 추가합니다.
- **특정 오류에 대한 재시도:** 일시적인 오류 (`429`, `408` 또는 `5xx` 등)에 대해서만 재시도합니다. 잘못된 API 키 또는 잘못된 구문과 같은 문제를 나타내는 클라이언트 오류 (`400` 또는 `403` 등)에 대해서는 재시도하지 마세요.
- **최대 재시도 횟수 설정:** 무한 루프를 방지하기 위해 최대 재시도 횟수를 정의합니다.

## 모델 매개변수 오류가 있는지 API 호출 확인

모델 매개변수가 다음 값 범위 내에 있는지 확인합니다.

|  |  |
| --- | --- |
| **모델 매개변수** | **값 (범위)** |
| 후보 수 | 1~8 (정수) |
| 온도 | 0.0~1.0 |
| 최대 출력 토큰 | 사용 중인 모델의 최대 토큰 수를 확인하려면 [모델 페이지](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko) 를 사용합니다. |
| TopP | 0.0~1.0 |

매개변수 값을 확인하는 것 외에도 필요한 기능을 지원하는 올바른
[API 버전](https://ai.google.dev/gemini-api/docs/api-versions?hl=ko) (예: `/v1` 또는 `/v1beta`)과
모델을 사용하고 있는지 확인하세요. 예를 들어 기능이 베타 출시된 경우 `/v1beta` API 버전에서만 사용할 수 있습니다.

## 올바른 모델이 있는지 확인

[모델 페이지에 나열된 지원되는 모델을 사용하고 있는지 확인합니다.](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko)

## 생각 모델의 지연 시간 또는 토큰 사용량 증가

Gemini 3.x 모델은 기본적으로 생각 기능이 사용 설정되어 있으므로 지연 시간 또는 토큰 사용량이 증가하는 경우가 많습니다. 지원 중단된 Gemini 2.5 모델도 기본 생각 기능을 사용합니다.

생각 모델은 품질을 개선하기 위해 내부 추론 토큰을 생성합니다. 이 추론 프로세스는 응답 지연 시간과 총 토큰 소비량을 모두 늘립니다.

지연 시간을 줄이거나 비용을 최소화해야 하는 경우 생각 수준을 낮추거나 생각 기능을 사용 중지할 수 있습니다.

구성 세부정보 및 코드 샘플은
[생각 가이드](https://ai.google.dev/gemini-api/docs/thinking?hl=ko#thinking-levels)를 참고하세요.

## 안전 문제

API 호출의 안전 설정으로 인해 프롬프트가 차단된 경우 API 호출에서 설정한 필터를 기준으로 프롬프트를 검토하세요.

`BlockedReason.OTHER`가 표시되면 쿼리 또는 응답이 [서비스
약관](https://ai.google.dev/terms?hl=ko)을 위반하거나 지원되지 않을 수 있습니다.

## 인용 문제

인용 이유로 인해 모델이 출력을 생성하지 않는 경우 모델 출력이 특정 데이터와 유사할 수 있습니다. 이 문제를 해결하려면 프롬프트 / 컨텍스트를 최대한 고유하게 만들고 더 높은 온도를 사용해 보세요.

## 반복 토큰 문제

출력 토큰이 반복되는 경우 다음 제안사항을 시도하여 토큰을 줄이거나 삭제하세요.

| 설명 | 원인 | 추천 해결 방법 |
| --- | --- | --- |
| 마크다운 테이블에서 하이픈 반복 | 모델이 시각적으로 정렬된 마크다운 테이블을 만들려고 할 때 테이블의 콘텐츠가 길면 이 문제가 발생할 수 있습니다. 그러나 마크다운의 정렬은 올바른 렌더링에 필요하지 않습니다. | 프롬프트에 안내를 추가하여 모델에 마크다운 테이블을 생성하기 위한 구체적인 가이드라인 을 제공합니다. 이러한 가이드라인을 따르는 예를 제공합니다. 온도를 조정해 볼 수도 있습니다. 마크다운 테이블과 같은 코드 또는 매우 구조화된 출력을 생성하는 경우 높은 온도 (>= 0.8)가 더 효과적인 것으로 나타났습니다.  다음은 이 문제를 방지하기 위해 프롬프트에 추가할 수 있는 가이드라인의 예입니다:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| 마크다운 테이블에서 토큰 반복 | 반복되는 하이픈과 마찬가지로 모델이 테이블의 콘텐츠를 시각적으로 정렬하려고 할 때 이 문제가 발생합니다. 마크다운의 정렬은 올바른 렌더링에 필요하지 않습니다. | - 시스템 프롬프트에 다음과 같은 안내를 추가해 보세요.      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - 온도를 조정해 보세요. 일반적으로 온도가 높을수록 (>= 0.8)   출력에서 반복 또는 중복을 없애는 데 도움이 됩니다. |
| 구조화된 출력에서 줄바꿈 (`\n`) 반복 | 모델 입력에 유니코드 또는 `\u` 또는 `\t`와 같은 이스케이프 시퀀스가 포함되어 있으면 줄바꿈이 반복될 수 있습니다. | - 프롬프트에서 금지된 이스케이프 시퀀스를 확인하고 UTF-8 문자로 바꿉니다. 예를 들어 JSON 예시의 `\u`   이스케이프 시퀀스로 인해 모델이 출력에서도 이를 사용할 수 있습니다. - 허용되는 이스케이프에 관해 모델에 안내합니다. 다음과 같은 시스템 안내를 추가합니다.      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| 구조화된 출력을 사용하여 텍스트 반복 | 모델 출력의 필드 순서가 정의된 구조화된 스키마와 다른 경우 텍스트가 반복될 수 있습니다. | - 프롬프트에서 필드 순서를 지정하지 마세요. - 모든 출력 필드를 필수 필드로 만듭니다. |
| 반복적인 도구 호출 | 모델이 이전 생각의 컨텍스트를 잃거나 강제로 사용할 수 없는 엔드포인트를 호출하는 경우 이 문제가 발생할 수 있습니다. | 모델에 생각 프로세스 내에서 상태를 유지하도록 안내합니다. 시스템 안내의 끝에 다음을 추가합니다.    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| 구조화된 출력에 포함되지 않은 반복 텍스트 | 모델이 해결할 수 없는 요청에 갇히면 이 문제가 발생할 수 있습니다. | - 생각 기능이 사용 설정된 경우 안내에서 문제를 생각하는 방법에 관한 명시적인 명령어를 제공하지 마세요. 최종   출력만 요청합니다. - 더 높은 온도(>= 0.8)를 사용해 보세요. - '간결하게 작성하세요', '반복하지 마세요', 또는   '답변을 한 번만 제공하세요'와 같은 안내를 추가합니다. |

## 차단되거나 작동하지 않는 API 키

이 섹션에서는 Gemini API 키가 차단되었는지 확인하는 방법과 차단된 경우 취해야 할 조치를 설명합니다.

### 키가 차단되는 이유 이해

일부 API 키가 공개적으로 노출되었을 수 있는 취약점이 확인되었습니다. 데이터를 보호하고 무단 액세스를 방지하기 위해 Google에서는 알려진 유출된 키가 Gemini API에 액세스하지 못하도록 사전에 차단했습니다.

### 키가 영향을 받는지 확인

키가 유출된 것으로 알려진 경우 더 이상 Gemini API에서 해당 키를 사용할 수 없습니다. [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=ko)를 사용하여
Gemini API 호출이 차단된 API 키가 있는지 확인하고 새
키를 생성할 수 있습니다. 이러한 키를 사용하려고 할 때 다음 오류가 반환될 수도 있습니다.

```
Your API key was reported as leaked. Please use another API key.
```

### 차단된 API 키에 대한 조치

Google [AI Studio
를 사용하여 Gemini API 통합을 위한 새 API 키를 생성해야 합니다](https://ai.google.dev/gemini-api/docs/api-keys?hl=ko). 새 키가 안전하게 유지되고 공개적으로 노출되지 않도록 API 키 관리 관행을 검토하는 것이 좋습니다.

### 취약점으로 인한 예기치 않은 청구

[결제 지원 케이스를 제출합니다](https://console.cloud.google.com/support/chat?hl=ko).
결제팀에서 이 문제를 해결하고 있으며 업데이트가 있으면 최대한 빨리 알려드리겠습니다.

### 유출된 키에 대한 Google의 보안 조치

**API 키가 유출된 경우 Google에서 비용 초과 및 악용으로부터 내 계정을 보호하는 데 어떻게 도움을 줄 수 있나요?**

- [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=ko)를 사용하여 새 키를 요청할 때 API 키를 발급하는 방향으로 나아가고 있습니다. 이 키는 기본적으로
  Google AI Studio로만 제한되며 다른 서비스의 키는 허용하지 않습니다.
  이렇게 하면 의도하지 않은 교차 키 사용을 방지할 수 있습니다.
- Gemini API에서 유출되어 사용되는 API 키를 기본적으로 차단하여 비용 및 애플리케이션 데이터의 악용을 방지합니다.
- [Google AI
  Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=ko) 내에서 API 키의 상태를 확인할 수 있으며, 즉각적인 조치를 위해 API 키가 유출된 것으로 확인되면 사전에 알려드리겠습니다.

## 모델 출력 개선

더 높은 품질의 모델 출력을 위해 더 구조화된 프롬프트를 작성해 보세요. 프롬프트 [엔지니어링 가이드](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ko) 페이지에서는 시작하기 위한 몇 가지 기본 개념, 전략, 권장사항을 소개합니다.

## 토큰 한도 이해

[토큰 가이드](https://ai.google.dev/gemini-api/docs/tokens?hl=ko)를 읽고 토큰을 집계하는 방법과 토큰 한도를 자세히 알아보세요.

## 알려진 문제

- API는 일부 선택된 언어만 지원합니다. 지원되지 않는 언어로 프롬프트를 제출하면 예기치 않은 응답이 생성되거나 응답이 차단될 수 있습니다. 업데이트는
  [사용 가능한 언어](https://ai.google.dev/gemini-api/docs/models?hl=ko#supported-languages)를
  참고하세요.

## 버그 신고

궁금한 점이 있으면
[Google AI 개발자 포럼](https://discuss.ai.google.dev?hl=ko)
에서 토론에 참여하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-04(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-04(UTC)"],[],[]]
