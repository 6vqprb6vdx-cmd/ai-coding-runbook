---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=ko
fetched_at: 2026-06-29T05:25:42.488480+00:00
title: "API \ubc84\uc804 \uc124\uba85 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [API 참조 문서](https://ai.google.dev/api?hl=ko)

의견 보내기

# API 버전 설명

이 문서에서는 Gemini API의 `v1` 버전과 `v1beta` 버전의 차이점을 간략하게 설명합니다.

- **v1**: 안정적인 API 버전입니다. 안정화 버전의 기능은 메이저 버전의 수명 기간 동안 완전히 지원됩니다. 호환성이 깨지는 변경사항이 있는 경우 API의 다음 메이저 버전이 생성되고 기존 버전은 적절한 기간이 지난 후 지원 중단됩니다.
  메이저 버전을 변경하지 않고 API에 브레이킹 체인지가 아닌 변경사항이 도입될 수 있습니다. 2026년 6월부터 **Interactions API**가 정식 버전으로 제공되며 `v1`에서 지원됩니다.
- **v1beta**: 이 버전에는 활발하게 개발 중인 초기 기능이 포함되어 있습니다. `v1beta`의 기능은 의견을 기반으로 개선되면서 변경될 수 있지만, 안정 버전으로 승격되기 전에 새로운 기능을 사용해 볼 수 있습니다.

| 기능 | v1 | v1beta |
| --- | --- | --- |
| Interactions API |  |  |
| 콘텐츠 생성 - 텍스트 전용 입력 |  |  |
| 콘텐츠 생성 - 텍스트 및 이미지 입력 |  |  |
| 콘텐츠 생성 - 텍스트 출력 |  |  |
| 콘텐츠 생성 - 멀티턴 대화 (채팅) |  |  |
| 콘텐츠 생성 - 함수 호출 |  |  |
| 콘텐츠 생성 - 스트리밍 |  |  |
| 콘텐츠 삽입 - 텍스트 전용 입력 |  |  |
| 답변 생성 |  |  |
| 시맨틱 검색기 |  |  |

- - 지원됨
- - 지원되지 않음

## SDK에서 API 버전 구성

Gemini API SDK는 기본적으로 `v1beta`를 사용하지만 다음 코드 샘플과 같이 API 버전을 설정하여 버전을 명시적으로 지정할 수 있습니다.

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.5-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works"
  }'
```

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-22(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-22(UTC)"],[],[]]
