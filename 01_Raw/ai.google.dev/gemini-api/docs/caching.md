---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=ko
fetched_at: 2026-08-31T06:32:09.403107+00:00
title: "\ucee8\ud14d\uc2a4\ud2b8 \uce90\uc2f1 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 컨텍스트 캐싱

일반적인 AI 워크플로에서는 동일한 입력 토큰을 모델에 반복해서 전달할 수 있습니다. Gemini API는 성능과 비용을 최적화하기 위해 암시적 캐싱을 제공합니다.

## 암시적 캐싱

암시적 캐싱은 모든 Gemini 2.5 이상 모델에서 기본적으로 사용 설정됩니다. [[스테이트풀(Stateful)(`previous_interaction_id`) 및 스테이트리스(Stateless) 대화 모드 모두에서 지원됩니다.](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko#multi-turn-conversations)](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko#stateless-conversations)
요청이 캐시에 적중하면 비용 절감액이 자동으로 전달됩니다. 이를 사용 설정하기 위해 별도로 취해야 할 조치는 없습니다. 컨텍스트 캐싱의 최소 입력 토큰 수는 각 모델의 다음 표에 나와 있습니다.

| 모델 | 최소 토큰 한도 |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Gemini 3.1 Pro 프리뷰 | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

암시적 캐시 적중 발생 가능성을 높이려면 다음 안내를 따르세요.

- 프롬프트 시작 부분에 크고 공통적인 콘텐츠를 배치해 보세요.
- 짧은 시간 내에 유사한 프리픽스를 가진 요청을 전송해 보세요.

응답 객체의 `usage.total_cached_tokens` (Python 및 JavaScript) 필드에서 캐시 적중된 토큰 수를 확인할 수 있습니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-30(UTC)"],[],[]]
