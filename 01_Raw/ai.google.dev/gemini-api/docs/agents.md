---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=ko
fetched_at: 2026-06-22T06:32:13.716289+00:00
title: "\uc5d0\uc774\uc804\ud2b8 \uac1c\uc694 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 에이전트 개요

Gemini API의 관리형 에이전트는 구성 가능한 에이전트 하네스를 제공합니다. 단일 API 호출은 에이전트가 추론하고, 코드를 실행하고, 파일을 관리하고, 웹을 자율적으로 탐색하는 Linux 샌드박스를 프로비저닝합니다.

[rocket\_launch

빠른 시작

첫 번째 에이전트 호출을 하고, 응답을 스트리밍하고, 커스텀 에이전트를 빌드합니다.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ko)
[smart\_toy

Antigravity 에이전트

기본 에이전트의 기능, 도구, 멀티모달 입력, 가격 책정](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ko)
[experiment

AI Studio의 에이전트

코드를 작성하지 않고 에이전트의 프로토타입을 제작할 수 있는 시각적 플레이그라운드](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=ko)

## 사용 가능한 관리형 에이전트

- **[Antigravity 에이전트](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ko)**: 범용
  관리형 에이전트(Gemini 3.5 Flash 기반)입니다. Google에서 호스팅하는 보안 Linux 샌드박스 내에서 코드를 실행하고, 파일을 관리하고, 웹을 검색합니다. 자체 안내, 기술, 데이터로
  확장하여
  [커스텀 에이전트를 빌드할 수 있습니다](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ko).
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)**: 시장 분석, 실사, 문헌 검토와 같은 사용 사례를 위해 여러 단계로 이루어진 연구 작업을 계획, 실행, 종합하는 자율 연구 에이전트입니다.

## 보안 및 권장사항

모든 에이전트는 OS 수준에서 격리된 샌드박스 환경에서 실행됩니다.
샌드박스는 기본적으로 무제한 아웃바운드 네트워크 액세스 권한을 갖습니다. 허용 목록을 사용하여 네트워크 액세스를 제한하거나 사용 중지할 수 있습니다.

### 네트워크 액세스

기본적으로 환경에는 무제한 아웃바운드 네트워크 액세스 권한이 있습니다. `network` 허용 목록을 사용하여 아웃바운드 트래픽을 특정 도메인 또는 와일드 카드 패턴으로 제한합니다. 구성 세부정보는
[네트워크 허용 목록](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=ko#network_allow_list) (AI
Studio) 또는 [네트워크 규칙](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ko#with_network_rules)
(API)을 참고하세요.

### 외부 도구 및 API

외부 도구 및 API를 연결하여 에이전트를 확장할 수 있습니다. 신뢰할 수 있는 소스의 도구만 사용하고 권한 범위를 필요한 최소한으로 지정하세요. 사용자 인증 정보는 이그레스 프록시 헤더 변환을 통해 안전하게 삽입되며 샌드박스 내에서 노출되지 않습니다. 에이전트는 액세스 권한이 있는 사용자 인증 정보를 사용할 수 있으므로 전체 범위를 부여할 의사가 있는 사용자 인증 정보만 제공하세요.

- 최소 권한 서비스 계정 또는 API 키를 사용합니다.
- 장기 키보다 단기 토큰을 선호합니다.
- 전체 범위를 부여할 의사가 있는 사용자 인증 정보만 제공합니다.
- 정기적인 일정으로 사용자 인증 정보를 순환합니다.

헤더 변환 구성에 관한 자세한 내용은
[사용자 인증 정보](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko#credentials)를 참고하세요.

### 인간의 감독

특히 데이터를 수정하거나 외부 시스템과 상호작용하는 작업의 경우 배포하기 전에 항상 출력 (생성된 코드, 데이터 변환, 구성 변경)을 확인하세요.

## 가격 책정

관리형 에이전트는 [사용한 만큼만 지불 모델](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#pricing-for-agents)을 Gemini 모델 토큰 및 도구 사용량을 기반으로 사용합니다. 단일 상호작용은 여러 추론 루프를 트리거할 수 있으며 일반적으로 100,000~3,000,000개의 토큰을 사용합니다. 미리보기 기간 중에는 환경 컴퓨팅에 **요금이 청구되지 않습니다**. 작업별 분석의 [예상 비용](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ko#availability-and-pricing)을 확인하세요.

## 한도

| 한도 | 설명 |
| --- | --- |
| **환경 전체 기간** | 환경은 7일 동안 활동이 없으면 영구적으로 삭제됩니다. |
| **VM 스핀다운** | VM은 리소스를 절약하기 위해 짧은 기간 동안 활동이 없으면 종료됩니다. 다음 요청은 콜드 스타트와 함께 상태를 복원합니다. |
| **사전 설치된 소프트웨어** | Python 3.12 및 Node.js 22가 포함된 Ubuntu 기반 환경입니다. 환경의 기본 이미지에 관한 자세한 내용은 [사전 설치된 소프트웨어](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko#pre-installed-software)를 참고하세요. |
| **최대 에이전트 수** | 관리형 에이전트는 최대 1,000개까지 사용할 수 있습니다. |

## 에이전트 프레임워크

다음 프레임워크 및 SDK를 사용하여 Gemini로 에이전트를 빌드할 수도 있습니다.

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=ko): 그래프
  구조를 사용하여 상태 저장 복잡한 애플리케이션 흐름과 멀티 에이전트 시스템을 빌드합니다.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=ko): Gemini 에이전트를
  비공개 데이터에 연결하여 RAG가 향상된 워크플로를 만듭니다.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=ko): 협업적이고
  역할극을 하는 자율 AI 에이전트를 조정합니다.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=ko): JavaScript/TypeScript에서 AI 기반 사용자 인터페이스와 에이전트를 빌드합니다.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): 상호 운용 가능한 AI
  에이전트를 빌드하고 조정하기 위한
  오픈소스 프레임워크입니다.
- [**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=ko): Python에서 프로그래밍할 수 있는 Google Antigravity를 지원하는 동일한 도구, 에이전트 루프, 컨텍스트
  관리를 사용하여 자율 AI 에이전트를 빌드합니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-20(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-20(UTC)"],[],[]]
