---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko
fetched_at: 2026-06-01T19:44:30.295427+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Interactions API

현재 기존 `generateContent` API로 빌드하는 경우 새로운 **Interactions API** 는 애플리케이션에 강력한 업그레이드 경로를 제공합니다. 이 API는 모든 새 프로젝트에 권장되며 에이전트 워크플로, 서버 측 상태 관리, 복잡한 멀티모달 다중 턴 대화에 최적화되어 있습니다. 원래 [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ko) API는 계속해서 완전히 지원됩니다.

## Interactions API를 사용하는 이유는 무엇인가요?

- **서버 측 기록 관리**: `previous_interaction_id`를 통해 다중 턴 흐름을 간소화합니다. 서버는 기본적으로 상태를 사용 설정하지만 (`store=true`), `store=false`를 설정하여 상태 비저장 동작을 선택할 수 있습니다.
- **관찰 가능한 실행 단계**: 유형화된 단계를 통해 복잡한 흐름을 쉽게 디버그하고 중간 이벤트 (예: 사고 또는 검색 위젯)의 UI를 렌더링할 수 있습니다.
- **에이전트 워크플로를 위해 빌드됨**: 유형화된 실행 단계를 통해 다단계 도구 사용, 오케스트레이션, 복잡한 추론 흐름을 기본적으로 지원합니다.
- **장기 실행 및 백그라운드 작업**: [Deep Think](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=ko) 및 [Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ko)와 같은 시간 집약적인 작업을 `background=true`를 사용하여 백그라운드 프로세스로 오프로드하는 것을 지원합니다.
- **새 모델 및 기능에 대한 액세스**: 향후 새로운 에이전트 기능 및 도구와 함께 기본 메인라인 제품군을 넘어서는 새로운 모델이 Interactions API에서만 출시될 예정입니다.

새 프로젝트를 시작하거나, 에이전트 애플리케이션을 빌드하거나, 서버 측 대화 관리가 필요한 경우 **Interactions API를 사용** 하세요. **필요에 맞는 기존 통합이 있거나 Batch API 또는 명시적 캐싱과 같이 Interactions API에서 [아직 사용할 수 없는](#limitations) 기능이 필요한 경우 [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ko)**를 사용하세요.

## 시작하기

- **코딩 에이전트 설정**: **Gemini Docs MCP**에 연결하고
  `gemini-interactions-api` 기능을 설치하여 어시스턴트가
  최신 개발자 문서와 권장사항에 직접 액세스할 수 있도록 합니다.
  [코딩 에이전트 설정하기 →](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ko)
- **`generateContent`에서 마이그레이션**: 기존 통합이 있는 경우
  [마이그레이션 가이드](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ko)에 따라
  Interactions API로 전환합니다.
- **빠른 시작 사용해 보기**: [Interactions API 빠른 시작](https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=ko)에서 최소한의 작업 예제를 시작합니다.

### 기능 가이드

이 가이드를 통해 Interactions API의 특정 기능을 살펴보세요. 이 페이지의 전환 버튼을 사용하여 generateContent와 Interactions API 간에 전환할 수 있습니다.

- [텍스트 생성](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ko)
- [이미지 생성](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=ko)
- [이미지 이해](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=ko)
- [오디오 이해](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=ko)
- [동영상 이해](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=ko)
- [문서 처리](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=ko)
- [함수 호출](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ko)
- [구조화된 출력](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=ko)
- [Deep Research 에이전트](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ko)
- [가변 추론](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=ko)
- [우선순위 추론](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=ko)
- [스트리밍](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=ko)

## Interactions API의 작동 방식

Interactions API는 핵심 리소스인 [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=ko#Resource:Interaction)을 중심으로 합니다. `Interaction`은 대화 또는 작업의 전체 턴을 나타냅니다. **실행 단계** 의 시간순서대로 상호작용의 전체 기록을 포함하는 세션 기록 역할을 합니다. 이러한 단계에는 모델 사고, 서버 측 또는 클라이언트 측 도구 호출 및 결과 (`function_call` 및 `function_result`와 같은), 최종 `model_output`이 포함됩니다. 저장된 리소스 (`interactions.get`을 통해 검색됨)에는 전체 컨텍스트를 위한 `user_input` 단계도 포함되지만 `interactions.create` 응답은 모델에서 생성된 단계만 반환합니다.

[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=ko#CreateInteraction)를 호출하면 새 `Interaction` 리소스가 생성됩니다.

### SDK 편의 속성으로 출력에 액세스

Interactions API는 사고, 검색어, 함수 호출과 같은 실행 단계의 구조화된 타임라인을 반환하지만 최종 모델 응답을 가져오기 위해 단계를 수동으로 탐색할 필요는 없습니다.

Google 생성형 AI SDK는 반환된 `Interaction` 객체에 직접 편의 속성을 제공하여 다양한 양식의 출력에 액세스합니다.

| SDK 편의 속성 | 반환 유형 | 설명 |
| --- | --- | --- |
| **`interaction.output_text`** | 문자열 | 모델 응답의 마지막 텍스트 블록을 반환합니다. 응답이 여러 개의 연속된 `TextContent` 블록으로 분할된 경우 자동으로 결합됩니다. 사고, 이미지, 오디오, 도구 호출과 같은 텍스트가 아닌 콘텐츠로 구분된 이전 텍스트 블록은 포함되지 않습니다. 복잡하거나 인터리브된 멀티모달 응답의 경우 `steps`를 수동으로 반복해야 합니다. |
| **`interaction.output_image`** | ImageContent 또는 `None` | 현재 요청에서 모델이 생성한 마지막 이미지 블록을 반환합니다. |
| **`interaction.output_audio`** | AudioContent 또는 `None` | 현재 요청에서 모델이 생성한 마지막 오디오 블록을 반환합니다. |

중간 사고 프로세스 렌더링, 단계별 도구 호출 검사, 디버깅과 같은 고급 사용 사례의 경우 원시 `interaction.steps` 타임라인을 수동으로 검사하고 탐색할 수 있습니다.

### 서버 측 상태 관리

후속 호출에서 완료된 상호작용의 `id`을(를) 사용하여 대화를 계속하려면
`previous_interaction_id` 매개변수를 사용하면 됩니다. 서버는 이 ID를 사용하여 대화 기록을 검색하므로 전체 채팅 기록을 다시 전송할 필요가 없습니다.

`previous_interaction_id` 매개변수는 `previous_interaction_id`를 사용하여 대화 기록 (입력 및 출력)만 보존합니다. 다른 매개변수는 **상호작용 범위** 이며 현재 생성 중인 특정 상호작용에만 적용됩니다.

- `tools`
- `system_instruction`
- `thinking_level`, `temperature` 등을 포함한 `generation_config`

즉, 이러한 매개변수를 적용하려면 각 새 상호작용에서 다시 지정해야 합니다. 이 서버 측 상태 관리는 선택사항입니다. 각 요청에서 전체 대화 기록을 전송하여 상태 비저장 모드로 작동할 수도 있습니다.

### 데이터 저장 및 보관

기본적으로 API는 서버 측 상태 관리 기능 (`previous_interaction_id` 사용), 백그라운드 실행 (`background=true` 사용), 모니터링 가능성 목적의 사용을 간소화하기 위해 모든 상호작용 객체 (`store=true`)를 저장합니다.

- **유료 등급**: 시스템은 상호작용을 **55일** 동안 보관합니다.
- **무료 등급**: 시스템은 상호작용을 **1일** 동안 보관합니다.

원하지 않는 경우 요청에서 `store=false`를 설정할 수 있습니다. 이 컨트롤은 상태 관리와 별개입니다. 모든 상호작용에 대해 저장소를 선택 해제할 수 있습니다. 하지만 `store=false`는 `background=true`와 호환되지 않으며 후속 턴에 `previous_interaction_id`를 사용하는 것을 방지합니다.

[API 참조에 있는 삭제 메서드를 사용하여 언제든지 저장된 상호작용을 삭제할 수 있습니다.](https://ai.google.dev/api/interactions-api?hl=ko) 상호작용 ID를 알고 있는 경우에만 상호작용을 삭제할 수 있습니다.

보관 기간이 만료되면 데이터가 자동으로 삭제됩니다.

시스템은 [약관](https://ai.google.dev/gemini-api/terms?hl=ko)에 따라 상호작용 객체를 처리합니다.

## 권장사항

- **캐시 적중률**: `previous_interaction_id`를 사용하여 대화를 계속하면 시스템에서 대화 기록에 암시적 캐싱을 더 쉽게 활용할 수 있으므로 성능이 개선되고 비용이 절감됩니다.
- **상호작용 혼합**: 대화 내에서 에이전트 및
  모델 상호작용을 자유롭게 혼합하고 일치시킬 수 있습니다. 예를 들어 Deep Research 에이전트와 같은 전문 에이전트를 초기 데이터 수집에 사용한 다음 표준 Gemini 모델을 사용하여 요약 또는 형식 변경과 같은 후속 작업을 수행하고 이러한 단계를 `previous_interaction_id`와 연결할 수 있습니다.

## 지원되는 모델 및 에이전트

| 모델 이름 | 유형 | 모델 ID |
| --- | --- | --- |
| Gemini 3.5 Flash | 모델 | `gemini-3.5-flash` |
| Gemini 3.1 Flash-Lite | 모델 | `gemini-3.1-flash-lite` |
| Gemini 3.1 Pro 프리뷰 | 모델 | `gemini-3.1-pro-preview` |
| Gemini 3 Flash 프리뷰 | 모델 | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | 모델 | `gemini-2.5-pro` |
| Gemini 2.5 Flash | 모델 | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | 모델 | `gemini-2.5-flash-lite` |
| Lyria 3 클립 프리뷰 | 모델 | `lyria-3-clip-preview` |
| Lyria 3 Pro 프리뷰 | 모델 | `lyria-3-pro-preview` |
| Deep Research 프리뷰 | 에이전트 | `deep-research-pro-preview-12-2025` |
| Deep Research 프리뷰 | 에이전트 | `deep-research-preview-04-2026` |
| Deep Research 프리뷰 | 에이전트 | `deep-research-max-preview-04-2026` |

## SDK

Interactions API에 액세스하려면 최신 버전의 Google 생성형 AI SDK를 사용하면 됩니다.

- Python에서는 `1.55.0` 버전부터 `google-genai` 패키지입니다.
- JavaScript에서는 `1.33.0` 버전부터 `@google/genai` 패키지입니다.

[라이브러리](https://ai.google.dev/gemini-api/docs/libraries?hl=ko) 페이지에서 SDK를 설치하는 방법을 자세히 알아볼 수 있습니다.

## 제한사항

- **베타 상태**: Interactions API는 베타/프리뷰 버전입니다. 기능 및 스키마는 변경될 수 있습니다.
- **원격 MCP**: Gemini 3은 원격 MCP를 지원하지 않으며 곧 지원될 예정입니다.

다음 기능은
[`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ko) API에서 지원되지만 Interactions API에서는 **아직
사용할 수 없습니다**.

- **[동영상 메타데이터](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=ko)**: 동영상 이해를 위한 클리핑 간격 및 맞춤 프레임 속도를 설정하는 데 사용되는 `video_metadata` 필드입니다.
- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)**
- **[자동 함수 호출 (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=ko#automatic_function_calling_python_only)**
- **[명시적 캐싱](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=ko)**: 서버 측 암시적 캐싱은 Interactions API
  를 통해 사용할 수 있습니다.`previous_interaction_id`

## 브레이킹 체인지

Interactions API는 현재 초기 베타 단계입니다. Google은 실제 사용 및 개발자 의견을 바탕으로 API 기능, 리소스 스키마, SDK 인터페이스를 적극적으로 개발하고 개선하고 있습니다. 따라서 **브레이킹 체인지가 발생할 수 있습니다**.

기존 브레이킹 체인지:

- **단계 스키마**: 새 단계 배열이 출력 배열을 대체하여 각 상호작용 턴의 구조화된 타임라인을 제공합니다.

최신 브레이킹 체인지에 대해 알아보고 마이그레이션하는 방법을 이해하려면 [브레이킹 체인지 마이그레이션 가이드 (2026년 5월)](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=ko)를 참고하세요.

기타 잠재적 업데이트에는 입력 및 출력 스키마, SDK 메서드 서명 및 객체 구조, 특정 기능 동작 변경사항이 포함될 수 있습니다.

프로덕션 워크로드의 경우 표준
[`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ko) API를 계속 사용해야 합니다. 이 API는 안정적인 배포를 위한 권장 경로로 유지되며 Google은 계속해서 적극적으로 개발하고 유지보수할 것입니다.

## 의견

여러분의 의견은 Interactions API 개발에 매우 중요합니다.
Google AI 개발자 커뮤니티 포럼에서 의견을 공유하거나, 버그를 신고하거나, 기능을 요청해 주세요.

## 다음 단계

- [Interactions API 빠른 시작 노트북](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=ko)을 사용해 보세요.
- 실시간 응답 처리를 위한 [스트리밍 상호작용](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=ko)에 대해 알아봅니다.
- [Gemini Deep Research 에이전트](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ko)에 대해 자세히 알아보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-01(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-01(UTC)"],[],[]]
