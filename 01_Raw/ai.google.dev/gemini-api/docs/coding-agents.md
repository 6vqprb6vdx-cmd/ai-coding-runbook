---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=ko
fetched_at: 2026-07-20T04:37:01.617520+00:00
title: "Gemini MCP \ubc0f \uc2a4\ud0ac\ub85c \ucf54\ub529 \uc5b4\uc2dc\uc2a4\ud134\ud2b8 \uc124\uc815 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini MCP 및 스킬로 코딩 어시스턴트 설정

AI 코딩 어시스턴트는 강력하지만 한계가 있습니다. 학습 데이터가 특정 날짜에 중단되어 새로운 API 기능과 변경사항이 누락됩니다. Gemini 관련 문서에 액세스할 수 없으면 상담사가 최적화된 접근 방식 대신 일반적인 패턴을 제안할 수 있습니다.

코딩 어시스턴트가 진화하는 Gemini API와 권장 사용법을 최신 상태로 유지하려면 **Gemini Docs MCP**를 설정하고 **Gemini API Skills**로 환경을 개선하는 것이 좋습니다. 이러한 도구는 독립적으로 사용할 수 있지만, 완전한 검사를 제공하기 위해 함께 작동하도록 설계되었습니다.

## Gemini Docs MCP 연결

Gemini는 `https://gemini-api-docs-mcp.dev`에서 공개 모델 컨텍스트 프로토콜 (MCP) 서버를 호스팅합니다. 코딩 에이전트를 이 서버에 연결하면 모든 쿼리가 최신 API, 코드 업데이트, 최적의 구성 예시에 액세스할 수 있습니다.

에이전트의 터미널 또는 프로젝트 루트에서 다음 명령어를 실행하여 서버를 설치합니다.

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

이 서버는 에이전트가 공식 Gemini 문서 파일에서 실시간 API 정의와 통합 패턴을 가져오는 데 사용할 수 있는 `search_documentation` 함수를 추가합니다.

## API 개발 기술 추가

이러한 스킬은 어시스턴트의 컨텍스트에서 직접 **내장된 규칙과 권장사항** (예: 올바른 SDK 및 현재 모델 버전 적용)을 제공합니다. 이 스킬은 Gemini Docs MCP 서비스와 함께 작동합니다. 두 서비스가 모두 설치되어 있으면 스킬에서 문서에 MCP 서비스를 사용하지만 MCP가 설치되어 있지 않아도 `ai.google.dev`에서 `llms.txt`를 대체로 가져옵니다.

이러한 스킬을 설치하려면 지원되는 다음 도구 중 하나를 사용하면 됩니다. 두 가지 모두의 설치 안내는 각 기술 모듈 아래에 제공됩니다.

- **[skills.sh](https://skills.sh)**: 권장 이식 가능한 에이전트 동작을 위한 개방형 표준입니다.
- **[Context7](https://context7.com)**: 이미 Context7 생태계를 활용하는 사용자에게 지원됩니다.

### gemini-api-dev

범용 Gemini 개발을 위한 기본 기술입니다. 이 스킬은 다음에 대한 문서와 권장사항을 제공합니다.

- 현재 모델 (예: Gemini 3.1 Pro/Flash)로 프롬프트 라우팅 및 지원 중단된 모델 방지
- 멀티모달 프롬프트, 함수 호출, 구조화된 출력, 일반적인 통합 패턴

#### skills.sh로 설치

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### Context7로 설치

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

Gemini Live API로 실시간 대화형 AI 애플리케이션을 빌드하는 기술 이 스킬은 다음에 대한 문서와 권장사항을 제공합니다.

- 짧은 지연 시간 스트리밍을 위한 WebSocket 연결
- 오디오, 동영상, 텍스트 스트리밍
- 음성 활동 감지 및 끼어들기 지원

#### skills.sh로 설치

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### Context7로 설치

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

[상호작용 API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)로 앱을 빌드하는 기술 Interactions API는 Gemini 모델 및 에이전트를 사용하여 빌드하는 가장 간단하고 효과적인 방법입니다. 이 스킬에서는 다음을 다룹니다.

- 텍스트 생성, 멀티턴 채팅, 스트리밍
- 함수 호출, 구조화된 출력, 이미지 생성
- 백그라운드 실행 및 Deep Research 에이전트
- 서버 측 대화 상태 관리
- Python 및 TypeScript SDK 패턴

#### skills.sh로 설치

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### Context7로 설치

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## 설치 확인

설치 후 코딩 어시스턴트가 Gemini Docs MCP 서버에 연결하고 설치된 스킬을 사용할 수 있는지 확인합니다.

### 1. 에이전트 동작 확인

가장 확실한 방법은 에이전트에게 Gemini API에 관한 기술적인 질문을 하는 것입니다.

**프롬프트:** 'Gemini API로 컨텍스트 캐싱을 사용하려면 어떻게 해야 하나요?'

설정이 완료되면 다음이 충족됩니다.

- **정확한 코드 제공**: 최신 엔드포인트에서 `cacheContent` 또는 `cachedContents.create`과 같은 특정 Gemini 메서드를 참조합니다.
- **MCP 도구 사용**: **Gemini Docs MCP 서버**에 연결되어 있거나 `search_documentation` 도구를 사용하여 데이터를 가져오고 있음을 보여줍니다.
- **로드된 스킬 호출**: 보조 래퍼를 사용하는 경우 '스킬 사용: gemini-api-dev'라는 표시기를 표시합니다.

### 2. 매니페스트 및 도구 확인

에이전트가 일반적인 답변을 제공하는 경우 환경에 맞는 구체적인 검색 또는 상태 명령어를 사용하여 Docs MCP 또는 스킬이 메모리에 로드되었는지 확인합니다.

| 환경 | MCP 인증 | 기술 확인 |
| --- | --- | --- |
| **Claude Code** | 터미널에 `/mcp`를 입력하여 활성 서버와 `search_documentation` 도구를 확인합니다. | 터미널에 `/skills`를 입력하여 활성 매니페스트를 모두 나열합니다. |
| **Cursor** | **설정 > 기능 > MCP**로 이동합니다. 서버가 '연결됨'인지 확인합니다. | **설정 > 규칙**을 엽니다. 기술이 '상담사가 결정'에 표시되는지 확인합니다. |
| **Antigravity** | **맞춤설정 > 연결** 사이드바에서 MCP 상태를 확인합니다. | `/skills list`를 입력하거나 **맞춤설정 > 규칙** 사이드바를 확인합니다. |
| **Gemini CLI** | `gemini mcp list`를 실행하거나 `/mcp list`을 사용합니다. | `gemini skills list`를 실행하거나 세션에서 `/skills` 슬래시 명령어를 사용합니다. |
| **Copilot** | `@gemini /mcp`를 입력하여 활성 데이터 커넥터를 나열합니다. | `@gemini /skills` (또는 `/skills`)를 입력하여 활성 확장 프로그램을 확인합니다. |

## 문제 해결

에이전트가 일반 정보만 제공하거나 Gemini 전용 메서드를 인식하지 못하는 경우 다음을 확인하세요.

### 에이전트가 스킬을 검색하지 못함

대부분의 에이전트는 시작 시에만 스킬을 색인으로 만듭니다.

**해결:** IDE (Cursor/VS Code)를 완전히 다시 시작하거나 터미널 기반 에이전트 (Claude Code)를 종료했다가 다시 엽니다.

### 전역 충돌과 로컬 충돌

`--global` 플래그를 사용하여 설치한 경우 에이전트가 프로젝트별 규칙을 우선하여 무시할 수 있습니다.

**수정:** 전역 플래그 없이 프로젝트 루트에 스킬을 직접 설치해 보세요.

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## 리소스

- [GitHub의 Gemini API 기술](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)
- [시작하기](https://ai.google.dev/gemini-api/docs/get-started?hl=ko)
- [라이브러리](https://ai.google.dev/gemini-api/docs/libraries?hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-08(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-08(UTC)"],[],[]]
