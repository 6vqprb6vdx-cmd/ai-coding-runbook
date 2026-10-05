---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=ko
fetched_at: 2026-10-05T06:31:30.987421+00:00
title: "Gemini \uc0dd\uac01 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini 생각

[Gemini 3 및 2.5 시리즈 모델](https://ai.google.dev/gemini-api/docs/models?hl=ko)은 추론 및 다단계 계획 능력을 크게 향상시키는 '사고 과정'을 사용하여 코딩, 고급 수학, 데이터 분석과 같은 복잡한 작업에 매우 효과적입니다.

사고 모델을 사용하면 Gemini가 대답하기 전에 내부적으로 추론합니다. Interactions API는 `thought` 단계를 통해 이 추론을 표시합니다. `thought` 단계는 `steps` 배열의 함수 호출, 사용자 입력 또는 모델 출력과 함께 시간순으로 표시되는 전용 단계입니다.

모든 사고 단계에는 다음 두 필드가 포함됩니다.

| 필드 | 필수 | 설명 |
| --- | --- | --- |
| `signature` | ✅ 예 | 모델의 내부 추론 상태의 암호화된 표현입니다. 모델이 최소한의 추론을 수행하는 경우에도 항상 표시됩니다. |
| `summary` | ❌ 아니요 | 추론을 요약하는 콘텐츠 (텍스트 및/또는 이미지) 배열입니다. [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=ko) 구성, 모델이 충분한 추론을 수행했는지, 콘텐츠 유형에 따라 비어 있을 수 있습니다 (예: 이미지 잠재 변수에는 텍스트 요약이 없을 수 있음). |

## 생각과의 상호작용

사고 모델과의 상호작용을 시작하는 것은 다른 상호작용 요청과 유사합니다. `model` 필드에 [사고 지원 모델](#thinking-levels) 중 하나를 지정합니다.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
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
        .input(
            InteractionsInput.of(
                "Explain the concept of Occam's Razor and provide a simple, everyday example."))
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
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("Explain the concept of Occam's Razor and provide a simple, everyday example."),
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## 사고 요약

사고 요약은 모델의 내부 추론 프로세스에 대한 인사이트를 제공합니다.
기본적으로 최종 출력만 반환됩니다. `thinking_summaries`로 생각 요약을 사용 설정할 수 있습니다.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtStep;
import com.google.genai.gaos.models.interactions.ThoughtSummaryContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Collections;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the sum of the first 50 prime numbers?"))
        .generationConfig(
            GenerationConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ThoughtStep thoughtStep) {
    System.out.println("Thought summary:");
    for (ThoughtSummaryContent contentBlock : thoughtStep.summary().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent) {
        System.out.println(textContent.text().orElse(""));
      }
    }
    System.out.println();
  } else if (step instanceof ModelOutputStep outputStep) {
    for (Content contentBlock : outputStep.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent) {
        System.out.println("Answer:");
        System.out.println(textContent.text().orElse(""));
        System.out.println();
      }
    }
  }
}
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
            Input: interactions.NewInteractionsInput("Provide a list of 3 famous physicists and their key contributions"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelLow.ToPointer(),
            },
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

다음과 같은 경우 생각 블록에 **요약이 없는 서명만** 포함될 수 있습니다.

- 모델이 요약을 생성할 만큼 충분히 추론하지 않은 간단한 요청
- `thinking_summaries: "none"`: 요약이 명시적으로 사용 중지된 경우
- 이미지와 같은 특정 생각 콘텐츠 유형에는 텍스트 요약이 없을 수 있습니다.

`summary`이 비어 있거나 없는 경우 코드는 항상 사고 블록을 처리해야 합니다.

## 사고를 포함한 스트리밍

생성 중에 스트리밍을 사용하여 증분 사고 요약을 수신합니다.
사고 블록은 두 가지 고유한 델타 유형을 사용하여 서버 전송 이벤트 (SSE)를 통해 제공됩니다.

| 델타 유형 | 포함 | 전송 시점 |
| --- | --- | --- |
| `thought_summary` | 텍스트 또는 이미지 요약 콘텐츠 | 증분 요약이 포함된 하나 이상의 델타 |
| `thought_signature` | 암호화 서명 | `step.stop` 전의 마지막 델타 |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.StepDeltaData;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtSummaryDelta;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();

String prompt =
    "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.\n"
        + "Alice does not live in the red house.\n"
        + "Bob does not live in the green house.\n"
        + "Carol does not live in the red or green house.\n"
        + "Which house does each person live in?";

StringBuilder thoughts = new StringBuilder();
StringBuilder answer = new StringBuilder();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .generationConfig(
            GenerationConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .stream(true)
        .build();

CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));

try (EventStream<InteractionSSEStreamEvent> stream = response.events()) {
  for (InteractionSSEStreamEvent streamEvent : stream) {
    InteractionSSEEvent event = streamEvent.data().orElse(null);
    if (event instanceof StepDelta stepDelta) {
      StepDeltaData delta = stepDelta.delta().orElse(null);
      if (delta instanceof ThoughtSummaryDelta thoughtDelta) {
        Content content = thoughtDelta.content().orElse(null);
        if (content instanceof TextContent textContent) {
          if (thoughts.length() == 0) {
            System.out.println("Thinking...");
          }
          String summaryText = textContent.text().orElse("");
          System.out.print("[Thought] " + summaryText);
          thoughts.append(summaryText);
        }
      } else if (delta instanceof TextDelta textDelta) {
        String text = textDelta.text().orElse("");
        if (!text.isEmpty()) {
          if (answer.length() == 0) {
            System.out.println("\nAnswer:");
          }
          System.out.print(text);
          answer.append(text);
        }
      }
    }
  }
}
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
            Input: interactions.NewInteractionsInput("What is the sum of the first 50 prime numbers?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel:     interactions.ThinkingLevelHigh.ToPointer(),
                ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if thought := step.ThoughtStep; thought != nil {
            for _, part := range thought.Summary {
                if part.TextContent != nil {
                    fmt.Printf("Thought summary:\n%s\n\n", part.TextContent.Text)
                }
            }
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Printf("Answer:\n%s\n", *res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

스트리밍 응답은 서버 전송 이벤트 (SSE)를 사용하며 다음과 같이 단계와 이벤트로 구성됩니다.

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.8-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## 사고 제어

Gemini 모델은 기본적으로 동적 사고를 수행하여 요청의 복잡성에 따라 추론 노력을 자동으로 조정합니다. `thinking_level` 매개변수를 사용하여 이 동작을 제어할 수 있습니다.

| 모델 | 기본 사고 | 지원되는 레벨 |
| --- | --- | --- |
| gemini-3.8-flash | 사용 설정 (매체) | 낮음, 중간, 높음 |
| gemini-3.7-flash | 사용 설정 (매체) | 낮음, 중간, 높음 |
| gemini-3.6-flash | 사용 설정 (매체) | 최소, 낮음, 중간, 높음 |
| gemini-3.5-flash-lite | 사용 설정 (최소) | 최소, 낮음, 중간, 높음 |
| gemini-3.1-pro-preview | 켜짐 (높음) | 낮음, 중간, 높음 |
| gemini-3.1-flash-lite-image | 사용 설정 (최소) | 최소, 높음 |
| gemini-3-flash-preview | 켜짐 (높음) | 최소, 낮음, 중간, 높음 |
| gemini-3-pro-preview | 켜짐 (높음) | 낮음, 높음 |
| gemini-3.5-flash | 사용 설정 (매체) | 최소, 낮음, 중간, 높음 |
| gemini-2.5-pro | 사용 | 낮음, 중간, 높음 |
| gemini-2.5-flash | 사용 | 낮음, 중간, 높음 |
| gemini-2.5-flash-lite | 꺼짐 | 낮음, 중간, 높음 |
| gemini-robotics-er-2-preview | 켜짐 (높음) | 최소, 낮음, 중간, 높음 |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Provide a list of 3 famous physicists and their key contributions"))
        .generationConfig(GenerationConfig.builder().thinkingLevel(ThinkingLevel.LOW).build())
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
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("What is the sum of the first 50 prime numbers?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel:     interactions.ThinkingLevelHigh.ToPointer(),
                ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
            },
            Stream: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if thoughtDelta := stepDelta.GetDeltaThoughtSummary(); thoughtDelta != nil {
                if textContent := thoughtDelta.GetContentText(); textContent != nil {
                    fmt.Printf("[Thought Summary] %s\n", textContent.Text)
                }
            }
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### 토큰 한도 및 `max_output_tokens`

[`max_output_tokens`](https://ai.google.dev/api/interactions-api?hl=ko#request-body) 생성 매개변수는 사고 토큰을 포함하여 대답이 생성할 수 있는 최대 토큰 수를 설정합니다.

설정되면 이 매개변수는 모델이 사고 예산(`thinking_level`)을 할당하는 방식을 변경하지 않고 인프라에서 적용하는 하드 컷오프 역할을 합니다.

모델이 추론 중에 이 한도에 도달하면 상태가 `"incomplete"`인 상태로 생성을 중지하고 잘리거나 비어 있는 출력을 반환합니다 (생성된 사고 토큰에 대해서는 계속 청구됨). 대답을 자르지 않고 비용이나 지연 시간을 줄이려면 작은 `max_output_tokens`을 설정하는 대신 `thinking_level` (`low` 또는 `medium`)를 낮추세요.

## 생각 서명

사고 서명은 모델의 내부 추론을 암호화한 표현입니다. 멀티턴 상호작용 전반에서 추론 연속성을 유지해야 합니다.

Interactions API를 사용하면 `generateContent` API보다 훨씬 간단하게 생각 서명을 처리할 수 있습니다.

### 상태 저장 모드 (권장)

기본적으로 상태 저장 모드에서 Interactions API를 사용하면 (`store: true`를 설정하고 후속 턴에서 `previous_interaction_id`를 전달) 서버에서 모든 생각 블록과 서명을 포함한 대화 상태를 자동으로 관리합니다. 이 모드에서는 서명과 관련하여 아무것도 할 필요가 없습니다. 서버 측에서 완전히 처리됩니다.

### 상태 비저장 모드

대화 상태를 직접 관리하고 (스테이트리스 모드) 각 요청에서 입력 및 출력의 전체 기록을 전달하는 경우:

- 항상 모델에서 수신한 그대로 모든 `thought` 블록을 다시 전송**해야 합니다**(MUST).
- 모델이 추론을 계속하는 데 필요한 서명이 포함되어 있으므로 기록에서 사고 블록을 삭제하거나 수정해서는 **안 됩니다**.
- 세션 내에서 모델을 전환할 때도 이전 모델의 생각 블록을 다시 전송해야 합니다. 백엔드에서 호환성을 관리합니다.

## 가격 책정

사고가 사용 설정된 경우 대답 가격은 출력 토큰과 사고 토큰의 합계입니다. `total_thought_tokens` 필드에서 생성된 사고 토큰의 총수를 확인할 수 있습니다.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### 자바스크립트

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Usage;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain the concept of Occam's Razor."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.usage().isPresent()) {
  Usage usage = interaction.usage().get();
  System.out.println("Thoughts tokens: " + usage.totalThoughtTokens().orElse(0));
  System.out.println("Output tokens: " + usage.totalOutputTokens().orElse(0));
}
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

    // Turn 1: Execute a reasoning + tool use interaction
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("Compare the GDP growth of Japan and Germany in 2025."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelHigh.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Turn 2: Pass PreviousInteractionID so thought signatures are automatically preserved
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-pro"),
            PreviousInteractionID: turn1.Interaction.ID,
            Input:                 interactions.NewInteractionsInput("Now summarize that comparison in a 3-row markdown table."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

사고 모델은 최종 대답의 품질을 개선하기 위해 전체 생각을 생성한 다음 [요약](#summaries)을 출력하여 사고 과정에 대한 통계를 제공합니다. 가격은 API에서 요약만 출력되더라도 모델이 생성해야 하는 전체 생각 토큰을 기준으로 합니다.

토큰에 관한 자세한 내용은 [토큰 수 계산](https://ai.google.dev/gemini-api/docs/tokens?hl=ko) 가이드를 참고하세요.

## 권장사항

다음 가이드라인에 따라 사고 모델을 효율적으로 사용하세요.

- **추론 검토**: 생각 요약을 분석하여 실패를 이해하고 프롬프트를 개선합니다.
- **사고 예산 제어**: 토큰을 절약하기 위해 긴 출력의 경우 모델이 생각을 덜 하도록 프롬프트를 사용합니다.
- **간단한 작업**: 사실 검색 또는 분류에 최소한의 사고를 사용합니다 (예: 'DeepMind는 어디에 설립되었어?').
- **작업 조정**: 개념 비교 또는 창의적인 추론 (예: 전기 자동차와 하이브리드 자동차 비교)에는 기본 사고를 사용합니다.
- **복잡한 작업**: 고급 코딩, 수학 또는 다단계 계획 (예: AIME 수학 문제 풀이)을 위해 최대한의 사고를 사용합니다.

## 다음 단계

- [텍스트 생성](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko): 기본 텍스트 응답
- [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko): 도구에 연결
- [Gemini 3 가이드](https://ai.google.dev/gemini-api/docs/gemini-3?hl=ko): 모델별 기능

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-25(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-25(UTC)"],[],[]]
