---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=ko
fetched_at: 2026-10-12T07:17:22.155270+00:00
title: "Gemini API \ucd5c\uc801\ud654 \ubc0f \ucd94\ub860 \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini API 최적화 및 추론

Gemini API는 특정 워크로드 요구사항에 따라 속도, 비용, 안정성의 균형을 맞출 수 있도록 다양한 최적화 메커니즘을 제공합니다.
실시간 대화형 봇을 빌드하든 오프라인에서 대량의 데이터 처리 파이프라인을 실행하든 올바른 패러다임을 선택하면 비용을 크게 절감하거나 성능을 향상할 수 있습니다.

| 기능 | 표준 | Flex | 우선순위 | 일괄 | 캐싱 |
| --- | --- | --- | --- | --- | --- |
| **가격 책정** | 정상가 | 50% 할인 | 표준보다 75~100% 더 많음 | 50% 할인 | 90% 할인 + 토큰 스토리지 일할 계산 |
| **지연 시간** | 수 초에서 수 분 | 분 (목표 1~15분) | 초 | 최대 24시간 | 첫 번째 토큰까지의 시간 단축 |
| **안정성** | 높음 / 중간~높음 | 최대한 노력 (삭제 가능) | 높음 (제거 불가) | 높음 (처리량) | 해당 사항 없음 |
| **인터페이스** | 동기식 | 동기식 | 동기식 | 비동기식 | 저장된 상태 |
| **최적의 사용 사례** | 일반 애플리케이션 워크플로 | 비긴급 순차적 체인 | 프로덕션, 사용자 대상 앱 | 대규모 데이터 세트, 오프라인 평가 | 동일한 파일에 대한 반복 쿼리 |

## 추론 서비스 등급 (동기)

표준 생성 호출에서 `service_tier` 매개변수를 전달하여 안정성 최적화 동기 트래픽과 비용 최적화 동기 트래픽 간에 전환할 수 있습니다.

### 표준 추론 (기본값)

표준 등급은 순차적 콘텐츠 생성의 기본 옵션입니다.
추가 요금이나 대기열 없이 정상적인 응답 시간을 제공합니다.

- **안정성:** 표준 심각도
- **가격:** 표준 가격 책정
- **적합한 용도:** 가장 상호작용이 많은 일상적인 애플리케이션

### 우선순위 추론 (지연 시간 최적화)

[우선순위](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko) 처리는 요청을 심각도가 높은 컴퓨팅 대기열로 라우팅합니다.
이 트래픽은 엄격하게 삭제할 수 없으며 (다른 계층에 의해 선점되지 않음) 가장 높은 신뢰성을 제공합니다. 동적 우선순위 한도를 초과하면 시스템에서 오류와 함께 실패하는 대신 요청을 표준 처리로 정상적으로 다운그레이드합니다.

- **신뢰성:** 가장 높은 심각도
- **가격:** 표준 요율보다 75~100% 높음
- **권장사항:** 고객 챗봇, 실시간 사기 감지, 비즈니스에 중요한 코파일럿

### Flex 추론 (비용 최적화)

[유연한 추론](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ko)은 기회주의적이고 사용량이 적은 시간대의 컴퓨팅 용량을 활용하여 표준 요금에 비해 50% 할인된 가격으로 제공됩니다. 요청은 동기적으로 처리되므로 일괄 객체를 관리하기 위해 코드를 다시 작성할 필요가 없습니다.
'삭제 가능한' 트래픽이므로 시스템에 표준 트래픽 급증이 발생하면 요청이 선점될 수 있습니다.

- **신뢰성:** 보장되지 않으며, 중요도를 낮출 수 있음
- **가격:** 표준 가격의 50%(토큰당 청구)
- **적합한 경우:** N번째 호출의 출력, 백그라운드 CRM 업데이트, 오프라인 평가에 N+1번째 호출이 종속되는 다단계 Agentic Workflows

## Batch API (대량, 비동기)

[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)는 표준 비용의 50% 로 대량의 요청을 비동기식으로 처리하도록 설계되었습니다. 인라인 사전으로 요청을 제출하거나 JSONL 입력 파일 (최대 2GB)을 사용하여 요청을 제출할 수 있습니다. 목표 처리 시간이 24시간인 백그라운드 처리량 대기열을 사용하여 요청을 처리합니다.

- **안정성:** 삭제 가능하지만 24시간 자동 재시도 및 대기열 시스템이 있음
- **가격:** Standard 가격의 50%
- **최적의 사용 사례:** 대규모 데이터 세트 전처리, 주기적인 회귀 테스트 모음 실행, 대량 이미지 또는 임베딩 생성

## 컨텍스트 캐싱 (입력 비용 절감)

[컨텍스트 캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)은 짧은 요청에서 상당한 양의 초기 컨텍스트를 반복적으로 참조하는 경우에 사용됩니다.

- **암시적 캐싱:** Gemini 2.5 이상 모델에서 자동으로 사용 설정됩니다.
  요청이 일반적인 프롬프트 접두사를 기반으로 기존 캐시에 도달하면 시스템에서 비용 절감을 전달합니다.
- **명시적 캐싱:** 특정 TTL (수명)을 사용하여 캐시 객체를 수동으로 만들 수 있습니다. 생성된 후에는 동일한 말뭉치 페이로드를 반복적으로 전달하지 않도록 후속 요청에서 캐시된 토큰을 참조합니다.
- **가격:** 캐시 토큰 수와 스토리지 기간 (TTL)을 기준으로 청구됩니다.
- **최적의 사용 사례:** 다양한 시스템 안내를 제공하는 챗봇, 긴 동영상 파일의 반복 분석, 대규모 문서 세트에 대한 쿼리

## 에이전트 기반 처리로 동영상 입력 비용 절감

긴 형식 동영상 콘텐츠의 경우 에이전트 처리로 입력 토큰 비용을 최대 88% 까지 절감하면서 대답 품질을 개선할 수 있습니다. 1FPS로 모든 프레임을 추출하는 대신 (정적 처리) 모델은 동영상을 통해 동적으로 검색하여 프롬프트와 관련된 스크립트, 프레임 또는 오디오를 로드합니다. 지연 시간이 중요한 짧은 클립 (5분 미만)의 경우 에이전트 모드는 생성 전에 내부 추론 및 도구 왕복이 발생하므로 정적 처리가 첫 번째 토큰까지의 시간 (TTFT)을 더 빠르게 제공할 수 있습니다.

Gemini 3.8 Flash, 3.6 Flash 또는 3.5 Flash Lite로 에이전트 처리 기능을 사용하려면 동영상 입력에 `processing: "agentic"` (Interactions API) 또는 `media_processing: "AGENTIC"` (GenerateContent API)를 설정하세요. 모델이 에이전트 처리 기능을 지원하지 않으면 오류가 반환됩니다.

코드 예시는 [에이전트형 동영상 이해](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ko#agentic-video-understanding)를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-10-09(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-10-09(UTC)"],[],[]]
