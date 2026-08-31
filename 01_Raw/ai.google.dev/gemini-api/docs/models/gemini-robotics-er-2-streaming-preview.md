---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-streaming-preview?hl=ko
fetched_at: 2026-08-31T06:38:45.584992+00:00
title: "Gemini Robotics ER 2 \uc2a4\ud2b8\ub9ac\ubc0d \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini Robotics ER 2 스트리밍

Gemini Robotics ER 2 Streaming은 Live API를 사용한 실시간 텍스트 스트리밍에 최적화된 로봇공학용 비전 언어 모델 (VLM)입니다. 텍스트, 이미지, 동영상, 오디오 입력을 허용하고 함수 호출을 통한 양방향 스트리밍을 지원합니다.

[Google AI Studio에서 사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=ko)

## 문서

기능과 기능에 관한 전체 내용은 [로보틱스용 Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ko) 페이지를 참고하세요.

## gemini-robotics-er-2-streaming-preview

### Gemini Robotics ER 2 프리뷰

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | `gemini-robotics-er-2-preview` |
| save지원되는 데이터 유형 | **입력**  텍스트, 이미지, 동영상, 오디오  **출력**  텍스트 |
| token\_auto토큰 한도[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ko) | **입력 토큰 한도**  131,072  **출력 토큰 한도**  65,536 |
| handyman기능 | **[오디오 생성](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko)**  지원되지 않음  **[캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)**  지원됨  **[코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)**  지원됨  **[컴퓨터 사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko)**  지원됨  **[파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko)**  지원됨  **[함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)**  지원됨  **[Google 지도 기반 그라운딩](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko)**  지원됨  **[이미지 생성](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)**  지원되지 않음  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ko)**  지원되지 않음  **[검색 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)**  지원됨  **[구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)**  지원됨  **[사고](https://ai.google.dev/gemini-api/docs/thinking?hl=ko)**  지원됨  **[URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko)**  지원됨 |
| speed소비 옵션 | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)**  지원됨  **[유연한 추론](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ko)**  지원되지 않음  **[우선순위 추론](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko)**  지원되지 않음 |
| 123버전 | 자세한 내용은 [모델 버전 패턴](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko#model-versions)을 참고하세요.  - 미리보기: `gemini-robotics-er-2-preview` |
| calendar\_month최신 업데이트 | 2026년 7월 |
| id\_card모델 카드 | [모델 카드](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=ko) |

### Gemini Robotics ER 2 스트리밍 프리뷰

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | `gemini-robotics-er-2-streaming-preview` |
| save지원되는 데이터 유형 | **입력**  텍스트, 이미지, 동영상, 오디오  **출력**  텍스트 |
| token\_auto토큰 한도[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ko) | **입력 토큰 한도**  131,072  **출력 토큰 한도**  65,536 |
| handyman기능 | **[오디오 생성](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko)**  지원되지 않음  **[캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)**  지원되지 않음  **[코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)**  지원되지 않음  **[컴퓨터 사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko)**  지원되지 않음  **[파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko)**  지원되지 않음  **[함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)**  지원됨  **[Google 지도 기반 그라운딩](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko)**  지원되지 않음  **[이미지 생성](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)**  지원되지 않음  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ko)**  지원됨  **[검색 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)**  지원됨  **[구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)**  지원되지 않음  **[사고](https://ai.google.dev/gemini-api/docs/thinking?hl=ko)**  지원됨  **[URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko)**  지원되지 않음 |
| speed소비 옵션 | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)**  지원되지 않음  **[유연한 추론](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ko)**  지원되지 않음  **[우선순위 추론](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko)**  지원되지 않음 |
| 123버전 | 자세한 내용은 [모델 버전 패턴](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko#model-versions)을 참고하세요.  - 미리보기: `gemini-robotics-er-2-streaming-preview` |
| calendar\_month최신 업데이트 | 2026년 7월 |
| id\_card모델 카드 | [모델 카드](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=ko) |

### Gemini Robotics ER 1.6 프리뷰

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | `gemini-robotics-er-1.6-preview` |
| save지원되는 데이터 유형 | **입력**  텍스트, 이미지, 동영상, 오디오  **출력**  텍스트 |
| token\_auto토큰 한도[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ko) | **입력 토큰 한도**  131,072  **출력 토큰 한도**  65,536 |
| handyman기능 | **[오디오 생성](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko)**  지원되지 않음  **[캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)**  지원됨  **[코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)**  지원됨  **[컴퓨터 사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko)**  지원됨  **[파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko)**  지원됨  **[함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)**  지원됨  **[Google 지도 기반 그라운딩](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko)**  지원됨  **[이미지 생성](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)**  지원되지 않음  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ko)**  지원되지 않음  **[검색 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)**  지원됨  **[구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)**  지원됨  **[사고](https://ai.google.dev/gemini-api/docs/thinking?hl=ko)**  지원됨  **[URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko)**  지원됨 |
| speed소비 옵션 | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)**  지원됨  **[유연한 추론](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ko)**  지원되지 않음  **[우선순위 추론](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko)**  지원되지 않음 |
| 123버전 | 자세한 내용은 [모델 버전 패턴](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko#model-versions)을 참고하세요.  - 미리보기: `gemini-robotics-er-1.6-preview` |
| calendar\_month최신 업데이트 | 2025년 12월 |
| cognition\_2지식 단절 | 2025년 1월 |

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-08-19(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-08-19(UTC)"],[],[]]
