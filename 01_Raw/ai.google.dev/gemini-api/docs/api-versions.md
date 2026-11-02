---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=ko
fetched_at: 2026-11-02T07:08:00.229691+00:00
title: "API \ubc84\uc804 \uc124\uba85 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon을 지금 이용 가능합니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [API 참조 문서](https://ai.google.dev/api?hl=ko)

의견 보내기

# API 버전 설명

이 문서에서는 Gemini API의 `v1` 버전과 `v1beta` 버전 간의 차이점을 간략하게 설명합니다.

- **v1**: API의 안정화 버전입니다. 안정화 버전의 기능은 메이저 버전의 전체 수명 주기 동안 완전히 지원됩니다. 브레이킹 체인지가 있는 경우 API의 새로운 메이저 버전이 생성되고 적절한 기간이 지나면 기존 버전이 지원 중단됩니다.
  주 버전을 변경하지 않고도 API에 브레이킹 체인지가 아닌 변경사항이 도입될 수 있습니다. **Interactions API** 및 핵심 기능은 `v1`에서 정식 버전으로 제공됩니다.
- **v1beta**: 이 버전에는 현재 개발 중인 초기 기능이 포함되어 있습니다. `v1beta`의 기능은 의견을 바탕으로 개선하는 과정에서 변경될 수 있지만, 안정화 버전으로 승격되기 전에 새로운 기능을 사용해 볼 수 있습니다.

## 기능 및 특성 지원

다음 표에는 `v1` (정식 버전) 및 `v1beta` (베타)의 기능 사용 가능 여부가 자세히 나와 있습니다. 달리 명시되지 않는 한 핵심 API 기능과 도구는 Interactions API와 `generateContent` 모두에 적용됩니다.

| 기능 | v1 | v1beta |
| --- | --- | --- |
| **핵심 API 기능** |  |  |
| [Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=ko) |  |  |
| [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko) |  |  |
| [구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko) |  |  |
| [사고/추론](https://ai.google.dev/gemini-api/docs/thinking?hl=ko) |  |  |
| [시스템 요청 사항](https://ai.google.dev/gemini-api/docs/system-instructions?hl=ko) |  |  |
| [오디오 출력 (음성 구성)](https://ai.google.dev/gemini-api/docs/audio?hl=ko) |  |  |
| [서비스 등급 (우선순위/Flex)](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko) |  |  |
| **도구** |  |  |
| [코드 실행 도구](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko) |  |  |
| [Google 검색 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko) |  |  |
| [Google 지도 그라운딩](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko) |  |  |
| [URL 컨텍스트 도구](https://ai.google.dev/gemini-api/docs/url-context?hl=ko) |  |  |
| [파일 검색 도구](https://ai.google.dev/gemini-api/docs/file-search?hl=ko) |  |  |
| [컴퓨터 사용 도구](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko) |  |  |
| [MCP 서버 도구](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko#mcp) |  |  |
| **실시간 API** |  |  |
| [Live API (WebSockets)](https://ai.google.dev/gemini-api/docs/live-api?hl=ko) |  |  |
| [Live Music API](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ko) |  |  |
| [임시 토큰 (Live API)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=ko) |  |  |
| **플랫폼 API** |  |  |
| [Models API](https://ai.google.dev/gemini-api/docs/models?hl=ko) |  |  |
| [Files Service Route](https://ai.google.dev/gemini-api/docs/files?hl=ko) |  |  |
| [파일 검색 저장소 경로](https://ai.google.dev/gemini-api/docs/file-search?hl=ko) |  |  |
| [Agents API](https://ai.google.dev/gemini-api/docs/agents?hl=ko) |  |  |
| [Webhooks API](https://ai.google.dev/gemini-api/docs/webhooks?hl=ko) |  |  |
| [컨텍스트 캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko) |  |  |

- - 지원됨

## SDK에서 API 버전 구성

Gemini API SDK는 기본적으로 `v1beta`로 설정되지만 다음 코드 샘플과 같이 API 버전을 설정하여 버전을 명시적으로 지정할 수 있습니다.

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client = Client.builder()
    .httpOptions(HttpOptions.builder().apiVersion("v1").build())
    .build();

CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.6-flash"))
    .input(InteractionsInput.of("Explain how AI works"))
    .build();
var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        HTTPOptions: genai.HTTPOptions{
            APIVersion: "v1",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.6-flash"),
            Input: interactions.NewInteractionsInput("Explain how AI works"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works",
  }'
```

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-10-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-10-30(UTC)"],[],[]]
