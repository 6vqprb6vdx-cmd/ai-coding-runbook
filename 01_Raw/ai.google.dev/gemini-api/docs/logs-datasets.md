---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ko
fetched_at: 2026-06-08T14:55:10.444716+00:00
title: "\ub85c\uadf8 \ubc0f \ub370\uc774\ud130 \uc138\ud2b8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 로그 및 데이터 세트

이 가이드에는 기존 Gemini API 애플리케이션의 로깅을 사용 설정하는 데 필요한 모든 내용이 포함되어 있습니다. 이 가이드에서는 Google AI Studio 대시보드에서 기존 또는 새 애플리케이션의 로그를 확인하여 모델 동작과 사용자가 애플리케이션과 상호작용하는 방식을 더 잘 이해하는 방법을 알아봅니다. 로깅을 사용하여 *개발자 사용 사례 전반에서 Gemini를 개선하기 위해 선택적으로 Google과 사용 의견을 공유*하고 관찰하고 디버그합니다.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=ko)

[OpenAI 호환성](https://ai.google.dev/gemini-api/docs/openai?hl=ko) 엔드포인트를 통해 이루어진 호출을 비롯한 모든 `GenerateContent` 및 `StreamGenerateContent` API 호출이 지원됩니다.

## 1. Google AI Studio에서 로깅 사용 설정

시작하기 전에 소유한 결제 사용 설정 프로젝트가 있는지 확인합니다.

1. Google [AI Studio](https://aistudio.google.com/logs?hl=ko)에서 로그 페이지를 엽니다.
2. 드롭다운에서 프로젝트를 선택하고 사용 설정 버튼을 눌러 기본적으로 모든 요청에 로깅을 사용 설정합니다.

![](https://ai.google.dev/static/gemini-api/docs/images/logs-state.png?hl=ko)

모든 프로젝트 또는 특정 프로젝트에 대해 로깅을 사용 설정 또는 사용 중지할 수 있으며, Google AI Studio를 통해 언제든지 이러한 환경설정을 변경할 수 있습니다.

## 2. AI Studio에서 로그 보기

1. [AI Studio](https://aistudio.google.com/logs?hl=ko)로 이동합니다.
2. 로깅을 사용 설정한 프로젝트를 선택합니다.
3. 로그가 표에 시간 역순으로 표시됩니다.

![](https://storage.googleapis.com/generativeai-downloads/images/nano-banana-logs.gif)

항목을 클릭하여 요청 및 응답 쌍의 전체 페이지 조회(수)를 확인합니다. 전체 프롬프트, Gemini의 전체 대답, 이전 턴의 컨텍스트를 검사할 수 있습니다. 각 프로젝트의 기본 저장소 한도는 최대 1,000개의 로그이며 데이터 세트에 저장되지 않은 로그는 55일 후에 만료됩니다. 프로젝트가 스토리지 한도에 도달하면 로그를 삭제하라는 메시지가 표시됩니다.

## 3. 데이터 세트 선별 및 공유

- 로그 표에서 상단의 필터 표시줄을 찾아 필터링할 속성을 선택합니다.
- 필터링된 로그 보기에서 체크박스를 사용하여 일부 또는 모든 로그를 선택합니다.
- 목록 상단에 표시되는 '데이터 세트 만들기' 버튼을 클릭합니다.
- 새 데이터 세트에 설명이 포함된 이름과 설명(선택사항)을 지정합니다.
- 선별된 로그 세트가 포함된 데이터 세트가 표시됩니다.
- 추가 분석을 위해 데이터 세트를 CSV, JSONL 파일 또는 Google Sheets로 내보냅니다.

![](https://storage.googleapis.com/generativeai-downloads/images/sales-dataset.gif)

데이터 세트는 다양한 사용 사례에 유용합니다.

- **챌린지 세트 선별:** AI를 개선하려는 영역을 타겟팅하여 향후 개선을 추진합니다.
- **샘플 세트 선별:** 예를 들어 다른 모델에서 대답을 생성하기 위한 실제 사용의 샘플이나 배포 전 일상적인 검사를 위한 이상치 모음이 있습니다.
- **평가 세트:** 중요한 기능 전반에서 실제 사용을 나타내는 세트로, 다른 모델 또는 시스템 명령 반복 간에 비교합니다.

데이터 세트를 데모 예시로 공유하면 AI 연구, Gemini API, Google AI Studio의 발전에 기여할 수 있습니다. 이를 통해 다양한 맥락에서 모델을 개선하고 여러 분야와 애플리케이션에서 개발자에게 유용한 AI 시스템을 만들 수 있습니다.

## 다음 단계 및 테스트할 항목

이제 로깅을 사용 설정했으므로 다음을 시도해 보세요.

- **세션 기록으로 프로토타입 제작:** [AI Studio 빌드](https://aistudio.google.com/apps?hl=ko)를 활용하여 앱의 바이브 코드를 작성하고 API 키를 추가하여 사용자 로그 기록을 사용 설정합니다.
- **Gemini Batch API로 로그 다시 실행:** [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb)를 통해 로그를 다시 실행하여 응답 샘플링 및 모델 또는 애플리케이션 로직 평가에 데이터 세트를 사용합니다.

## 호환성

현재 다음 항목에 대한 로깅은 지원되지 않습니다.

- Imagen 및 Veo 모델
- Gemini 임베딩 모델
- 동영상, GIF 또는 PDF가 포함된 입력

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-01(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-01(UTC)"],[],[]]
