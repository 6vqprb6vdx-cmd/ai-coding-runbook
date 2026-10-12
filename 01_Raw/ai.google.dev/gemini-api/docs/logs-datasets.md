---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ko
fetched_at: 2026-10-12T07:07:33.366143+00:00
title: "\ub85c\uadf8 \ubc0f \ub370\uc774\ud130 \uc138\ud2b8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 로그 및 데이터 세트

이 가이드에서는 Google AI Studio 대시보드에서 Gemini API 사용 로그를 확인하여 모델 동작과 사용자가 애플리케이션과 상호작용하는 방식을 더 잘 이해하는 방법을 알아봅니다. 로깅을 사용하여 *개발자 사용 사례 전반에서 Gemini를 개선하는 데 도움이 되도록 선택적으로 Google과 사용 의견을 공유*하고 관찰하고 디버그합니다.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=ko)

모든 `GenerateContent`, `BatchGenerateContent`, `StreamGenerateContent` API 호출과 관리 에이전트를 제외한 [상호작용](https://ai.google.dev/gemini-api/docs/interactions?hl=ko) API 호출이 지원됩니다. 여기에는 [OpenAI 호환성](https://ai.google.dev/gemini-api/docs/openai?hl=ko) 엔드포인트를 통해 이루어진 호출이 포함됩니다.

## 프로젝트 로깅 구성

기본적으로 API는 서버 측 상태 관리 기능의 사용을 간소화하기 위해 모든 상호작용 객체 (`store=true`)를 저장합니다. 반면 Generate Content API는 기본적으로 요청을 저장하지 않으며 AI Studio에서 요청별 또는 프로젝트 수준으로 스토리지를 사용 설정해야 합니다.

Google [AI Studio](https://aistudio.google.com/logs?hl=ko)에서 모든 프로젝트 또는 특정 프로젝트의 로깅을 사용 설정하거나 사용 중지할 수 있으며, [로그 및 데이터 세트](https://aistudio.google.com/logs?hl=ko) 페이지의 **설정** 패널을 통해 언제든지 이러한 환경설정을 변경할 수 있습니다. `generateContent` API와 [상호작용](https://ai.google.dev/gemini-api/docs/interactions?hl=ko) API의 로깅을 개별적으로 사용 설정 또는 사용 중지하여 프로젝트의 기본 저장 동작을 변경할 수 있습니다.

### 요청 수준 로깅

스토리지 및 로깅 동작은 API에 따라 다릅니다.

- **[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ko):** 서버 측 상태 관리를 간소화하기 위해 기본적으로 요청을 저장합니다 (`store=true`).
- **Generate Content API (`generateContent`):** 기본적으로 요청을 저장하지 않습니다 (`store=false`).

`store` 속성을 설정하는 방법은 다음과 같습니다.

**GenerateContent API**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

// The GenerateContent API does not store requests by default
GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        "Explain quantum entanglement in simple terms.",
        GenerateContentConfig.builder().build());

System.out.println(response.text());
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // The GenerateContent API does not store requests by default
    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain quantum entanglement in simple terms."),
        &genai.GenerateContentConfig{},
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

**Interactions API**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain quantum entanglement in simple terms."))
        .store(true) // Set to false to disable logging of this request
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Explain quantum entanglement in simple terms."),
            Store: genai.Ptr(true), // Set to false to disable logging of this request
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

## AI Studio에서 프로젝트 로그 보기

1. [AI Studio](https://aistudio.google.com/logs?hl=ko)의 로그 페이지로 이동합니다.
2. 드롭다운에서 프로젝트를 선택합니다.
3. 로그가 있는 경우 Interactions API의 로그가 표에 시간 역순으로 표시됩니다.
4. Generate Content API의 프로젝트 로그를 관찰하려면 먼저 [설정 패널](#configure-logging)에서 이 기능을 사용 설정하세요.

항목을 클릭하여 페이로드를 미리 봅니다. Gemini의 전체 프롬프트와 대답, 이전 턴의 컨텍스트를 검사할 수 있습니다. **Interactions API** 요청의 경우 로그에 `previous_interaction_id`로 연결되는 직접 링크도 포함됩니다.

## 프로젝트 스토리지 보관 구성

로그는 기본 보관 기간인 55일이 지나면 만료되고 삭제 대상으로 표시됩니다 (만료되지 않는 [데이터 세트에 저장](#create)되지 않는 한).
프로젝트 로그의 보관 기간을 최대 7일, 14일, 28일 또는 55일로 구성할 수 있습니다.

## 데이터 세트 만들기 및 공유하기

로그를 데이터 세트에 저장하여 더 효과적으로 정리하고 내보낼 수 있습니다.

- [로그 페이지](https://aistudio.google.com/logs?hl=ko)에서 상단의 필터 표시줄을 찾아 필터링할 속성을 선택합니다.
- 필터링된 보기에서 체크박스를 사용하여 전체 또는 개별 로그를 선택합니다.
- 목록 상단에 표시되는 **데이터 세트 만들기** 버튼을 클릭합니다.
- 새 데이터 세트에 이름과 설명(선택사항)을 지정합니다.
- 선별된 로그 세트가 포함된 데이터 세트가 표시됩니다.
- 추가 분석을 위해 데이터 세트를 CSV, JSONL 파일 또는 Google Sheets로 내보냅니다.

데이터 세트는 다양한 사용 사례에 유용합니다.

- **챌린지 세트 선별:** AI를 개선하려는 영역을 타겟팅하여 향후 개선을 추진합니다.
- **샘플 세트 선별:** 예를 들어 실제 사용에서 가져온 샘플을 사용하여 다른 모델에서 대답을 생성하거나, 배포 전 루틴 검사를 위한 특이 사례 모음입니다.
- **평가 세트:** 중요한 기능 전반에서 실제 사용을 나타내는 세트로, 다른 모델 또는 시스템 명령 반복 간에 비교합니다.

데모 예시로 데이터 세트를 Google과 공유하도록 선택하여 Gemini 연구 및 개발에 기여할 수 있습니다.

## 제한사항

현재 다음 항목에 대한 로깅은 지원되지 않습니다.

- Imagen 및 Veo 모델
- Gemini 임베딩 모델
- Gemini Robotics 모델
- 동영상, GIF 또는 PDF가 포함된 입력
- Gemini API의 공개 미리보기 에이전트

## 다음 단계

- **세션 기록으로 프로토타입 제작:** [AI Studio 빌드](https://aistudio.google.com/apps?hl=ko)를 사용하여 앱을 바이브 코딩하고 API 키를 추가하여 AI 기능의 Gemini API 로그 기록을 사용 설정합니다.
- **Gemini Batch API로 로그 다시 실행:** [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb)로 로그를 다시 실행하여 응답 샘플링 및 모델 또는 애플리케이션 로직 평가를 위한 데이터 세트를 사용합니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-24(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-24(UTC)"],[],[]]
