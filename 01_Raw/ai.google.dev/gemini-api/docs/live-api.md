---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=ko
fetched_at: 2026-06-01T19:36:13.304410+00:00
title: "Gemini Live API \uac1c\uc694 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini Live API 개요

Live API는 Gemini와의 지연 시간이 짧은 실시간 음성 및 시각 상호작용을 지원합니다. 연속적인 오디오, 이미지, 텍스트 스트림을 처리하여 즉각적이고 사람과 유사한 음성 대답을 제공하므로 사용자에게 자연스러운 대화형 환경을 제공합니다.

![Live API 개요](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=ko)

[Google AI Studio에서 Live API 사용해 보기mic](https://aistudio.google.com/live?hl=ko)
[GitHub에서 예시 앱 클론code](https://github.com/google-gemini/gemini-live-api-examples)
[코딩 에이전트 기술 사용terminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ko)

## 사용 사례

Live API를 사용하여 다음을 비롯한 다양한 업계의 실시간 음성 에이전트를 빌드할 수 있습니다.

- **전자상거래 및 소매:** 맞춤형 추천을 제공하는 쇼핑 어시스턴트와 고객 문제를 해결하는 지원 에이전트
- **게임:** 대화형 논플레이어 캐릭터(NPC), 인게임 도움말 어시스턴트, 인게임 콘텐츠의 실시간 번역
- **차세대 인터페이스:** 로봇 공학, 스마트 글라스, 차량에서 음성 및 동영상 지원 환경
- **의료:** 환자 지원 및 교육을 위한 건강 도우미
- **금융 서비스:** 자산 관리 및 투자 안내를 위한 AI 자문가
- **교육:** 맞춤형 안내와 의견을 제공하는 AI 멘토 및 학습자 도우미

## 주요 특징

Live API는 강력한 음성 에이전트를 빌드하기 위한 포괄적인 기능 세트를 제공합니다.

- [**다국어 지원**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ko#supported-languages):
  지원되는 70개 언어로 대화할 수 있습니다.
- [**통화 참여**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ko#interruptions):
  사용자는 언제든지 모델을 중단하여 응답형 상호작용을 할 수 있습니다.
- [**도구 사용**](https://ai.google.dev/gemini-api/docs/live-tools?hl=ko):
  함수 호출 및 Google 검색과 같은 도구를 통합하여 역동적인 상호작용을 지원합니다.
- [**오디오 스크립트 작성**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ko#audio-transcription):
  사용자 입력과 모델 출력의 텍스트 스크립트를 제공합니다.
- [**능동적 오디오**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ko#proactive-audio):
  모델이 응답하는 시점과 컨텍스트를 제어할 수 있습니다.
- [**공감형 대화**](https://ai.google.dev/gemini-api/docs/live-guide?hl=ko#affective-dialog):
  사용자의 입력 표현에 맞게 대답 스타일과 어조를 조정합니다.

## 기술 사양

다음 표에는 Live API의 기술 사양이 나와 있습니다.

| 카테고리 | 세부정보 |
| --- | --- |
| 입력 모달리티 | 오디오 (원시 16비트 PCM 오디오, 16kHz, 리틀 엔디안), 이미지 (JPEG <= 1FPS), 텍스트 |
| 출력 모달리티 | 오디오 (원시 16비트 PCM 오디오, 24kHz, 리틀 엔디안) |
| 프로토콜 | 스테이트풀 WebSocket 연결(WSS) |

## 구현 접근 방식 선택

Live API와 통합할 때는 다음 구현 접근 방식 중 하나를 선택해야 합니다.

- **서버 간**: 백엔드가 [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)를 사용하여 Live API에 연결됩니다. 일반적으로 클라이언트는 스트림 데이터 (오디오, 동영상, 텍스트)를 서버로 전송하고 서버는 이를 Live API로 전달합니다.
- **클라이언트-서버**: 프런트엔드 코드가 [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)을 사용하여 Live API에 직접 연결하여 데이터를 스트리밍하고 백엔드를 우회합니다.

## 시작하기

개발 환경에 맞는 가이드를 선택합니다.

서버 간

### [생성형 AI SDK 튜토리얼](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ko)

생성형 AI SDK를 사용하여 Gemini Live API에 연결하여 Python 백엔드로 실시간 멀티모달 애플리케이션을 빌드합니다.

클라이언트-서버

### [WebSocket 튜토리얼](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=ko)

WebSocket을 사용하여 Gemini Live API에 연결하여 JavaScript 프런트엔드와 일회성 토큰으로 실시간 멀티모달 애플리케이션을 빌드합니다.

에이전트 개발 키트

### [ADK 튜토리얼](https://google.github.io/adk-docs/streaming/)

에이전트를 만들고 에이전트 개발 키트(ADK) 스트리밍을 사용하여 음성 및 영상 커뮤니케이션을 사용 설정합니다.

## 파트너 연동

실시간 오디오 및 동영상 앱의 개발을 간소화하려면 WebRTC 또는 WebSocket을 통해 Gemini Live API를 지원하는 서드 파티 통합을 사용하면 됩니다.

[LiveKit

LiveKit 에이전트와 함께 Gemini Live API를 사용합니다.](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Daily의 Pipecat

Gemini Live 및 Pipecat을 사용하여 실시간 AI 챗봇을 만드세요.](https://docs.pipecat.ai/guides/features/gemini-live)
[Software Mansion의 Fishjam

Fishjam으로 라이브 동영상 및 오디오 스트리밍 애플리케이션을 만드세요.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[스트림의 Vision Agents

Vision Agent로 실시간 음성 및 동영상 AI 애플리케이션을 빌드하세요.](https://visionagents.ai/integrations/gemini)
[Voximplant

Voximplant를 사용하여 인바운드 및 아웃바운드 통화를 Live API에 연결합니다.](https://voximplant.com/products/gemini-client)
[Agora

Agora로 실시간 대화형 AI 애플리케이션을 빌드하세요.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

Firebase AI Logic을 사용하여 Gemini Live API를 시작하세요.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-01(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-01(UTC)"],[],[]]
