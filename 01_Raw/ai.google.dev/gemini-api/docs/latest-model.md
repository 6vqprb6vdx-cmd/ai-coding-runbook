---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=ko
fetched_at: 2026-08-17T02:15:48.045807+00:00
title: "\ucd5c\uc2e0 Gemini \ubaa8\ub378 \uc0ac\uc6a9 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 최신 Gemini 모델 사용

[이 페이지](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=ko)

Gemini 3.6 Flash (`gemini-3.6-flash`) 및 Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`)는 정식 버전 (GA)으로 출시되어 프로덕션에 사용할 수 있습니다.

- **Gemini 3.6 Flash**: 3.5 Flash보다 낮은 가격으로 토큰 사용량을 줄이면서 복잡한 에이전트형 및 멀티모달 작업에서 더 강력한 성능을 제공합니다.
- **Gemini 3.5 Flash-Lite**: 3.5 제품군에서 가장 빠르고 비용이 저렴한 모델입니다. 높은 처리량 실행을 위해 이전 Flash-Lite 세대를 능가합니다.

이 가이드에서는 각 모델의 새로운 기능, 코드에 영향을 미치는 API 변경사항, 마이그레이션 방법을 설명합니다.

### Gemini 3.6 Flash

1. 기술 설치:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. 스킬 적용:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. 기술 설치:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. 스킬 적용:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## 새 모델

| 모델 | 모델 ID | 기본 사고 수준 | 가격 책정 | 설명 |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | 입력 토큰 100만 개당 $1.50, 출력 토큰 100만 개당 $7.50 | 에이전트형 및 멀티모달 작업의 속도와 인텔리전스의 균형을 맞춥니다. |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | 입력 토큰 100만 개당 $0.30, 출력 토큰 100만 개당 $2.50 | 높은 처리량 실행을 위한 가장 빠르고 비용이 저렴한 3.5 모델입니다. |

두 모델 모두 100만 토큰 컨텍스트 윈도우, 최대 64,000개의 출력 토큰, 사고, [컴퓨터 사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko)을 비롯한 전체 제품군 기본 제공 도구를 지원합니다.

전체 사양은 모델 페이지를 참고하세요.

- [Gemini 3.6 Flash 모델 페이지](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ko)
- [Gemini 3.5 Flash-Lite 모델 페이지](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ko)

자세한 가격 책정은 [가격 책정 페이지](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)를 참고하세요.

## 빠른 시작

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a three.js script that renders an interactive 3D robot."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Write a three.js script that renders an interactive 3D robot.",
  });
  console.log(interaction.outputText);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.6-flash",
    "input": {
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }
  }'
```

## Gemini 3.6 Flash의 새로운 기능

- **토큰 및 턴 감소:** Gemini 3.5보다 적은 추론 단계, 대화 턴, 도구 호출로 다단계 워크플로를 완료합니다. 또한 실행 루프가 나선형으로 증가하는 현상을 줄입니다.
- **코드 생성 개선:** 원치 않는 수정사항과 디버깅 루프를 줄여 프로덕션에 바로 사용할 수 있는 고품질 코드를 생성합니다.
- **더 나은 안내 따르기**: 진단 작업 중에 원치 않는 파일 변경사항을 줄입니다.
- **강력한 멀티모달 및 공간 추론:** 차트 해석, 시각적 청사진 변환, 다중 요소 웹 레이아웃 생성에서 성능이 개선되었습니다.
- **사전 프로그래매틱 검사:** Gemini 3.5 Flash보다 변경하기 전에 진단 코드 스크립트를 실행하는 것을 더 선호합니다. 이렇게 하면 복잡한 작업의 정확성이 향상되지만 간단한 프런트엔드 작업에 추가 탐색 단계가 추가될 수 있습니다.
- **컴퓨터 사용 지원:** 에이전트형 UI 자동화의 기본 도구로 지원됩니다.
- **UI 스타일 지정 환경설정**: 인간 평가자는 시각적 레이아웃 및 스타일 지정에 이전 모델을 선호했지만 기능 코드를 더 잘 생성합니다. 명시적인 디자인 가이드라인을 제공하여 이 문제를 완화할 수 있습니다.
- **기본 사고 노력 (중간):** Gemini 3.5 Flash와 동일한 `medium` 기본 사고 수준을 사용합니다.
- **가격 인하**: 출력 토큰 비용이 낮아졌습니다 (3.5 Flash의 경우 100만 개당 $7.50, 100만 개당 $9.00). 입력 토큰은 100만 개당 $1.50으로 유지됩니다.

## Gemini 3.5 Flash-Lite의 새로운 기능

- **작업 실행 지연 시간 감소:** 대용량 데이터 파싱 및 문서 추출을 위한 3.5 제품군에서 가장 높은 처리량을 제공합니다.
- **추론 및 멀티모달 성능 향상:** Gemini 2.5 Flash에서 강력한 마이그레이션 경로를 제공하며 HLE (18.0% 대 11.0%)와 같은 추론 작업과 CharXIV (74.5% 대 63.7%)와 같은 멀티모달 벤치마크에서 더 높은 점수를 얻습니다.
- **하위 에이전트 조정 및 도구 안정성:** 코드 실행, 검색, MCP 워크플로의 도구 실행 안정성을 개선합니다. 자율 계획 및 복잡한 하위 에이전트 작업의 사고 수준을 높입니다.
- **문서 이해 개선:** 문서 파싱 및 구조화된 데이터 추출의 정확성을 개선합니다. 문서 복잡성에 따라 최소 및 높은 사고 수준을 모두 실험해 보세요.
- **대화형 웹 코딩 및 표 형식 데이터 처리:** 경량 코드 실행을 통해 계획하여 프런트엔드 자바스크립트 및 표 형식 데이터 처리에서 강력한 성능을 발휘합니다.
- **챗봇 및 페르소나 지속성:** Gemini 3.1 Flash-Lite보다 멀티턴 안내 따르기 및 페르소나 일관성이 더 강력합니다.
- **컴퓨터 사용 지원:** 에이전트형 UI 자동화의 기본 도구로 지원됩니다.

## 적합한 Flash 또는 Flash-Lite 모델 선택

이 표를 사용하여 워크로드에 적합한 모델과 마이그레이션 경로를 선택하세요.

두 모델 모두 지원 중단된 샘플링 매개변수 (`temperature`, `top_p`, `top_k`)와 미리 채워진 모델 턴을 삭제해야 합니다. 자세한 내용은 [API 변경사항](#api-changes-and-parameter-updates)을 참고하세요.

| 모델 | 주요 사용 사례 | 권장되는 마이그레이션 대상 |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | 코드 생성, 공간/멀티모달 추론, 다단계 에이전트형 워크플로 | **Gemini 3.5 Flash**, **Gemini 3 Flash (프리뷰)** 또는 **Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite** `gemini-3.5-flash-lite` | 자율 하위 에이전트 실행, 대용량 데이터 분석 및 문서 추출, 구조화된 JSON 파싱 | **Gemini 3.1 Flash-Lite** 또는 **Gemini 2.5 Flash** |

## 업데이트된 Antigravity 에이전트

성능이 개선되어 이제 Gemini 3.6 Flash가 Gemini 관리형 에이전트의 [Antigravity 에이전트](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ko)를 지원하는 새로운 기본 모델입니다. API에서 새 필드를 설정하여 이를 변경할 수 있습니다.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## API 변경사항 및 매개변수 업데이트

Gemini 3.6 Flash 및 Gemini 3.5 Flash-Lite부터 다음 API 변경사항이 이러한 모델과 향후 모든 Gemini 모델 출시에 적용됩니다.

- **샘플링 매개변수 지원 중단**: `temperature`, `top_p`, `top_k`가 지원 중단됩니다. API는 이러한 매개변수를 무시하고 향후 모델 생성에서 오류를 반환합니다.
- **미리 채워진 모델 턴 검증**: 모델 턴 미리 채우기가 더 이상 지원되지 않습니다. 요청의 마지막으로 비어 있지 않은 턴이 `model` 턴인 경우 API는 `400` 오류를 반환합니다.

아래에는 각 API 변경사항에 대한 자세한 설명과 코드 샘플이 나와 있습니다.

### 1. 샘플링 매개변수 지원 중단 (`temperature`, `top_p`, `top_k`)

`temperature`, `top_p`, `top_k`가 지원 중단되고 무시됩니다. 향후 모델 생성에서 이러한 매개변수를 제공하면 HTTP 400 오류가 반환됩니다. **모든 요청에서 이러한 매개변수를 삭제합니다.**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

결정성을 개선하려면 특정 사용 사례에 대한 명시적 규칙으로 시스템 안내를 정의하세요.

### 2. 미리 채워진 모델 턴 검증

비어 있지 않은 모델 역할 턴으로 끝나는 API 요청은 허용되지 않으며 **HTTP 400 오류** 를 반환합니다.

#### ⚠️ 제외

이전 `generateContent` 또는 원시 REST 페이로드에서 모델 역할 턴으로 끝나는 것은 이제 허용되지 않습니다.

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ 권장되는 마이그레이션 (Interactions API)

Interactions API에서는 모델 턴이 수동으로 미리 채워지지 않습니다. 이전에 애플리케이션에서 모델 턴을 미리 채워 서문을 억제하거나 JSON 형식을 강제 적용한 경우 system\_instruction 또는 [구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)을 대신 사용하세요.

```
# ✅ RECOMMENDED: Use system_instruction in the Interactions API to specify output format
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Translate 'Hello world' to Spanish.",
    system_instruction="Output only the translation without introductory text.",
)
```

## 마이그레이션 체크리스트

### Gemini 3.6 Flash

1. 기술 설치:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. 스킬 적용:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. 기술 설치:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. 스킬 적용:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### gemini-3.6-flash로 마이그레이션

- **모델 ID 업데이트:** 타겟 모델 문자열을 `gemini-3.6-flash`로 변경합니다.
- **지원 중단된 샘플링 매개변수 삭제:**
  - 생성 구성에서 `temperature`, `top_p`, `top_k`를 삭제합니다.
  - `thinking_budget`을(를) `"medium"` 또는 `"high"`으로 설정된 문자열 enum `thinking_level`로 바꿉니다.
  - `candidate_count` (Gemini 3.x에서 지원되지 않음)를 삭제합니다.
- **턴 검증 규칙 적용:**
  - 서버 측 `previous_interaction_id`에서 멀티턴 대화를 표준화합니다.
  - 미리 채워진 모델 턴을 삭제합니다.
- **함수 호출 감사:**
  - 응답 페이로드 내에 멀티모달 애셋을 배치합니다.
  - `\n\n`를 사용하여 인라인 안내 형식을 지정합니다.
  - 도구 이전 텍스트와 연결된 `Malformed_Function_Call` 오류가 표시되면 [도구 이전 텍스트 요구사항의 해결 방법을 참고하세요](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko#workarounds-for-pre-tool-text-requirements).
  - generateContent API를 사용하는 경우에만 모든 `FunctionResponse` 객체에 `call_id` 및 `name`이 포함되어 있는지 확인합니다.
- **기본 Gemini 3.x 요구사항:** SDK 업데이트 및 사고 모델 서명 보존은 [Gemini 3.5 마이3그레이션 체크리스트](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=ko#migration)를 참고하세요.

### gemini-3.5-flash-lite로 마이그레이션

- **모델 ID 업데이트:** 타겟 모델 문자열을 `gemini-3.5-flash-lite`로 변경합니다.
- **사고 노력 수준 구성:**
  - 대용량 추출, 라우팅 또는 분류의 경우 최대 처리량을 위해 `thinking_level`을 `"minimal"` (기본값)로 둡니다.
  - 도구 호출, 코드 실행 또는 다단계 추론이 있는 자율 하위 에이전트의 경우 `thinking_level`을 `"medium"` 또는 `"high"`로 설정하여 도구가 조기에 종료되지 않도록 합니다.
- **지원 중단된 매개변수 삭제 및 함수 호출 검증:** [3.6 Flash와 동일한 규칙을 적용합니다](#migrate-to-gemini-3-6-flash).
- **기본 Gemini 3.x 요구사항:** [Gemini 3.5 마이그레이션 체크리스트](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=ko#migration)를 참고하세요.

## 다음 단계

- [모델 개요에서 API 사양을 검토합니다.](https://ai.google.dev/gemini-api/docs/models?hl=ko)
- [상호작용 API 가이드에서 멀티 에이전트 조정을 살펴봅니다.](https://ai.google.dev/gemini-api/docs/interactions?hl=ko)
- [Google AI Studio](https://aistudio.google.com/?hl=ko)에서 프롬프트를 테스트하고 개선합니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-30(UTC)"],[],[]]
