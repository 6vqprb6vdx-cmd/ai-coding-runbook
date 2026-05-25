---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=ko
fetched_at: 2026-05-25T13:00:44.921844+00:00
title: "Gemini API \ucd5c\uc801\ud654 \ubc0f \ucd94\ub860 \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini API 최적화 및 추론

Gemini API는 특정 워크로드 요구사항에 따라 속도, 비용, 안정성의 균형을 맞추는 데 도움이 되는 다양한 최적화 메커니즘을 제공합니다.
실시간 대화형 봇을 빌드하든 대규모 오프라인 데이터 처리 파이프라인을 실행하든 올바른 패러다임을 선택하면 비용을 크게 절감하거나 성능을 높일 수 있습니다.

| 기능 | 표준 | Flex | 우선순위 | 일괄 | 캐싱 |
| --- | --- | --- | --- | --- | --- |
| **가격 책정** | 정상가 | 50% 할인 | 표준보다 75~100% 더 높음 | 50% 할인 | 90% 할인 + 비례 할당 토큰 스토리지 |
| **지연 시간** | 수 초에서 수 분 | 분 (1~15분 목표) | 초 | 최대 24시간 | 첫 번째 토큰까지의 시간 단축 |
| **안정성** | 높음 / 중간-높음 | 최대한 노력 (삭제 가능) | 높음 (삭제 불가) | 높음 (처리량) | 해당 사항 없음 |
| **인터페이스** | 동기식 | 동기식 | 동기식 | 비동기식 | 저장된 상태 |
| **최적의 사용 사례** | 일반 애플리케이션 워크플로 | 급하지 않은 순차적 체인 | 프로덕션, 사용자 대상 앱 | 방대한 데이터 세트, 오프라인 평가 | 동일한 파일에 대한 반복 쿼리 |

## 추론 서비스 등급 (동기식)

표준 생성 호출에서 `service_tier` 매개변수를 전달하여 안정성 최적화 동기식 트래픽과 비용 최적화 동기식 트래픽 간에 전환할 수 있습니다.

### 표준 추론 (기본값)

표준 등급은 순차적 콘텐츠 생성을 위한 기본 옵션입니다.
추가 프리미엄이나 대기열 없이 정상적인 응답 시간을 제공합니다.

- **안정성:** 표준 중요도
- **가격:** 표준 가격 책정
- **최적:** 대부분의 대화형 일상 애플리케이션

### 우선순위 추론 (지연 시간 최적화)

[우선순위](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko) 처리는 요청을
중요도가 높은 컴퓨팅 대기열로 라우팅합니다.
이 트래픽은 엄격하게 삭제할 수 없으며 (다른 등급에 의해 선점되지 않음) 가장 높은 안정성을 제공합니다. 동적 우선순위 한도를 초과하면 시스템은 오류로 인해 실패하는 대신 요청을 표준 처리로 정상적으로 다운그레이드합니다.

- **안정성:** 가장 높은 중요도
- **가격:** 표준 요금보다 75~100% 높음
- **최적:** 고객 챗봇, 실시간 사기 감지, 비즈니스에 중요한 코파일럿

### Flex 추론 (비용 최적화)

[Flex 추론](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ko)은 기회적 비피크 컴퓨팅 용량을 활용하여
표준 요금에 비해 50% 할인을 제공합니다. 요청은 동기식으로 처리되므로 일괄 객체를 관리하기 위해 코드를 다시 작성할 필요가 없습니다.
'삭제 가능' 트래픽이므로 시스템에 표준 트래픽 급증이 발생하면 요청이 선점될 수 있습니다.

- **안정성:** 보장되지 않음, 삭제 가능 중요도
- **가격:** 표준 가격 책정의 50%(토큰당 청구)
- **최적:** 호출 N+1이 호출 N의 출력에 종속되는 다단계 에이전트 워크플로, 백그라운드 CRM 업데이트, 오프라인 평가

## Batch API (대량, 비동기식)

[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)는 표준 비용의 50% 로 대량의 요청을 비동기식으로 처리하도록 설계되었습니다. 요청을 인라인 사전으로 제출하거나 JSONL 입력 파일 (최대 2GB)을 사용하여 제출할 수 있습니다. 목표 처리 시간이 24시간인 백그라운드 처리량 대기열을 사용하여 요청을 처리합니다.

- **안정성:** 삭제 가능하지만 24시간 자동 재시도 및 대기열 시스템 포함
- **가격:** 표준 가격 책정의 50%
- **최적:** 대규모 데이터 세트 전처리, 정기 회귀 테스트 모음 실행, 대량 이미지 또는 임베딩 생성

## 컨텍스트 캐싱 (입력 절감)

[컨텍스트 캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)은 짧은 요청에서 상당한 양의 초기
컨텍스트를 반복적으로 참조할 때 사용됩니다.

- **암시적 캐싱:** Gemini 2.5 이상 모델에서 자동으로 사용 설정됩니다.
  요청이 일반적인 프롬프트 접두어를 기반으로 기존 캐시에 적중하면 시스템에서 비용 절감을 전달합니다.
- **명시적 캐싱:** 특정 TTL (Time-To-Live)로 캐시 객체를 수동으로 만들 수 있습니다. 생성되면 동일한 말뭉치 페이로드를 반복적으로 전달하지 않도록 후속 요청에 대해 캐시된 토큰을 참조합니다.
- **가격:** 캐시 토큰 수 및 스토리지 기간 (TTL)에 따라 청구됩니다.
- **최적:** 다양한 시스템 안내를 제공하는 챗봇, 긴 동영상 파일의 반복 분석, 대규모 문서 세트에 대한 쿼리

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
