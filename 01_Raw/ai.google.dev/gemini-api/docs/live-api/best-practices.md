---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=ko
fetched_at: 2026-05-25T12:57:41.806425+00:00
title: "Live API best practices \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Live API best practices

이 가이드에서는 Live API 사용을 최적화하기 위해 따를 수 있는 권장사항을 설명합니다.
일반적인 사용 사례의 개요 및 샘플 코드는 [Live API 시작하기](https://ai.google.dev/gemini-api/docs/live?hl=ko)
페이지를 참고하세요.

## 명확한 시스템 요청 사항 설계

Live API를 최대한 활용하려면 에이전트 페르소나, 대화 규칙, 가드레일을 이 순서대로 정의하는 명확하게 정의된 시스템 요청 사항 집합 (SIs)이 있어야 합니다.

최상의 결과를 얻으려면 각 에이전트를 별도의 SI로 분리하세요.

1. **에이전트 페르소나 지정:** 에이전트의 이름, 역할, 선호하는 특징에 관한 세부정보를 제공합니다. 억양을 지정하려면 선호하는 출력 언어(예: 영어 화자의 경우 영국 억양)도 지정해야 합니다.
2. **대화 규칙 지정:** 모델이 따라야 하는 순서대로 이러한 규칙을 입력합니다. 대화의 일회성 요소와 대화형 루프를 구분합니다. 예를 들면 다음과 같습니다.

   - **일회성 요소:** 고객의 세부정보(예: 이름, 위치, 포인트 카드 번호)를 한 번 수집합니다.
   - **대화형 루프:** 사용자는 추천, 가격, 반품, 배송에 대해 논의할 수 있으며 주제를 전환하고 싶어 할 수 있습니다. 사용자가 원하는 한 이 대화형 루프에 참여해도 된다고 모델에게 알립니다.
3. **흐름 내에서 도구 호출을 별도의 문장으로 지정:** 예를 들어 고객 세부정보를 수집하는 일회성 단계에서 `get_user_info` 함수를 호출해야 하는 경우 다음과 같이 말할 수 있습니다. *첫 번째 단계는 사용자 정보를 수집하는 것입니다. 먼저 사용자에게 이름, 위치, 포인트 카드 번호를 제공해 달라고 요청합니다. 그런 다음 이러한 세부정보를 사용하여 `get_user_info`를 호출합니다.*
4. **필요한 가드레일 추가:** 모델이 수행하지 않기를 바라는 일반적인 대화형 가드레일을 제공합니다. *x*가 발생하면 모델이 *y*를 수행하기를 바라는 구체적인 예시를 제공해도 됩니다. 여전히 원하는 수준의 정밀도를 얻지 못한다면 *분명하게*라는 단어를 사용하여 모델이 정확하도록 안내합니다.

## 도구 정확하게 정의

Live API에서 도구를 사용할 때는 도구 정의를 구체적으로 작성하세요.
어떤 조건에서 도구 호출이 실행되어야 하는지 Gemini에게 명확하게 전달해야 합니다. 자세한 내용은 예시 섹션의 [도구 정의](#tool-definitions-example)를 참조하세요.

## 효과적인 프롬프트 작성

- **명확한 프롬프트 사용:** 프롬프트에서 모델이 해야 하는 일과 하지 말아야 하는 일의 예시를 제공하고, 한 번에 페르소나 또는 역할당 하나의 프롬프트로 제한합니다. 길고 여러 페이지로 구성된 프롬프트 대신 프롬프트 체이닝을 사용하는 것이 좋습니다. 모델은 단일 함수 호출이 있는 태스크에서 가장 우수한 성능을 발휘합니다.
- **시작 명령어와 정보 제공:** Live API는 응답하기 전에 사용자 입력을 기다립니다. Live API가 대화를 시작하도록 하려면 사용자에게 인사하거나 대화를 시작하라는 프롬프트를 포함합니다. Live API가 인사말을 맞춤설정할 수 있도록 사용자에 관한 정보를 포함합니다.

## 언어 지정

Live API 단계식 `gemini-live-2.5-flash`에서 최적의 성능을 얻으려면 API의 `language_code`가 사용자가 말하는 언어와 일치해야 합니다.

모델이 영어 이외의 언어로 응답해야 하는 경우 시스템 요청 사항에 다음을 포함하세요.

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## 스트리밍

실시간 오디오를 구현할 때는 다음 권장사항을 따르세요.

- **청크 크기 및 지연 시간**: 오디오를 20ms~40ms 청크로 전송합니다.
- **중단 처리**: 모델이 대답하는 동안 사용자가 말하면 서버는 `"interrupted": true`가 포함된 `server_content` 메시지를 전송합니다. 에이전트의 말이 사용자의 말과 겹치지 않도록 클라이언트 측 오디오 버퍼를 즉시 삭제해야 합니다.

## 컨텍스트 관리

기본 오디오 토큰이 빠르게 누적되므로(오디오 초당 약 25개 토큰) 긴 세션에는 `ContextWindowCompressionConfig`를 사용하세요.

## 클라이언트 버퍼링

전송하기 전에 입력 오디오를 크게(예: 1초) 버퍼링하지 마세요. 지연 시간을 최소화하기 위해 작은 청크(20ms~100ms)를 전송합니다.

## 리샘플링

클라이언트 애플리케이션이 전송 전에 마이크 입력 (일반적으로 44.1kHz 또는 48kHz)을 16kHz로 리샘플링하는지 확인합니다.

## 세션 관리

세션 수명 주기를 처리하고 안정적인 사용자 환경을 보장하려면 다음 가이드라인을 따르세요.

- **컨텍스트 윈도우 압축 사용 설정:** 오디오 토큰은 초당 약 25개 토큰으로 누적됩니다. 압축이 없으면 오디오 전용 세션은 15분으로 제한되고 오디오-동영상 세션은 2분으로 제한됩니다. [컨텍스트 윈도우 압축을 사용 설정하여 세션을 무제한으로 연장합니다.](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ko#context-window-compression)
- **세션 재개 구현:** 서버는 WebSocket 연결을 주기적으로 재설정할 수 있습니다. [세션 재개를 사용하여 컨텍스트를 잃지 않고 원활하게 다시 연결합니다.](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ko#session-resumption) `SessionResumptionUpdate` 메시지에서 최신 재개 토큰을 보관하고 다시 연결할 때 핸들로 전달합니다. 재개 토큰은 마지막 세션이 종료된 후 2시간 동안 유효합니다.
- **GoAway 메시지 처리:** 서버는 연결을 종료하기 전에
  [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ko#goaway-message) 메시지를
  전송합니다. 이 메시지를 수신 대기하고 `timeLeft` 필드를 사용하여 연결이 닫히기 전에 정상적으로 래핑하거나 다시 연결합니다.
- **generationComplete 신호 처리:** 모델이 응답 생성을 완료한 시점을 알 수 있도록
  [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ko#generation-complete-message)
  메시지를 사용하여
  애플리케이션이 UI를 업데이트하거나 다음 작업을 진행할 수 있도록 합니다.

구현 세부정보는
[세션 관리](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ko)를 참고하세요.

## 예

이 예시에서는 권장사항과
[시스템 요청 사항 설계 가이드라인](#system-instruction-guidelines)을 결합하여
모델이 커리어 코치로서의 성능을 발휘하도록 안내합니다.

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### 도구 정의

이 JSON은 커리어 코치 예시에서 호출되는 관련 함수를 정의합니다.
함수를 정의할 때 최상의 결과를 얻으려면 이름, 설명, 파라미터, 호출 조건을 포함하세요.

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

## 가격 책정 및 결제

Gemini Live API는 토큰 사용량에 따라 엄격하게 청구합니다. Live API는 영구 WebSocket 세션을 유지하므로 결제는 활성 컨텍스트 윈도우를 기반으로 하는 복리 모델을 따릅니다.

### 세션 컨텍스트 윈도우 (복리 비용)

API는 세션 컨텍스트 윈도우에 있는 모든 토큰에 대해 턴당 요금을 청구합니다. '턴'은 하나의 사용자 입력과 모델의 해당 응답으로 정의됩니다.

- **누적:** 컨텍스트 윈도우에는 현재 턴의 새 토큰과 이전 턴에서 누적된 모든 토큰이 포함됩니다.
- **재청구:** 이전 토큰은 구성된 컨텍스트 윈도우 크기까지 각 새 턴에서 다시 처리되고 계산됩니다. 세션이 길어지면 대화 기록이 다시 처리되므로 턴당 비용이 증가합니다.

### 오디오 토큰 및 스크립트

Live API는 기본적으로 멀티모달입니다. 음향 뉘앙스와 톤을 보존하기 위해 대화 기록을 원시 오디오 토큰으로 유지합니다.

- **오디오 결제:** API는 모든 턴에서 표준 오디오 입력 요금으로 누적된 기본 오디오 토큰에 대해 청구합니다.
- **스크립트 추가 요금:** 오디오-텍스트 스크립트가 사용 설정된 경우 (`inputAudioTranscription` 또는 `outputAudioTranscription`) API는 표준 오디오 토큰 비용 외에도 텍스트 토큰 출력 요금으로 스크립트 생성을 위해 생성된 모든 텍스트 토큰에 대해 청구합니다.

### 컨텍스트 한도로 비용 관리

긴 세션에서 무제한 비용 증가를 방지하려면 `contextWindowCompression`을 사용하여 컨텍스트 윈도우 크기를 구성하세요.

압축 트리거 (예: 25,000개 토큰)와 슬라이딩 윈도우 (예: 8,000개 토큰)를 설정하면 API는 기준점에 도달하는 즉시 이전 토큰을 자동으로 삭제합니다. 그런 다음 API는 보관된 기록과 새 토큰에 대해서만 후속 턴에 청구합니다.

### 능동적 오디오 모드

능동적 오디오 모드가 사용 설정되면 Live API가 수신 대기하는 동안 입력 토큰에 요금이 청구되고 출력 토큰은 API가 응답할 때만 청구됩니다.

- **Gemini 3.1 참고사항:** 능동적 오디오 모드는 `gemini-3.1-flash-live-preview`에서 지원되지 않습니다. 이 모델의 경우 입력을 적극적으로 스트리밍할 때만 오디오 요금이 청구됩니다.

자세한 가격 책정 정보는 [Gemini API 가격 책정 페이지](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-11(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-11(UTC)"],[],[]]
