---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=ko
fetched_at: 2026-07-27T04:39:55.299860+00:00
title: "Gemini 3 \uac1c\ubc1c\uc790 \uac00\uc774\ub4dc \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)

의견 보내기

# Gemini 3 개발자 가이드

Gemini 3는 최첨단 추론을 기반으로 구축된, 현재까지 가장 지능적인 모델 제품군입니다. 이 모델은 에이전트형 워크플로, 자율 코딩, 복잡한 멀티모달 작업을 정교하게 처리하여 어떠한 아이디어든 실현할 수 있도록 설계되었습니다.
이 가이드에서는 Gemini 3 모델 제품군의 주요 기능과 이를 최대한 활용하는 방법을 설명합니다.

[Gemini 3 앱 컬렉션](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=ko)을 살펴보고
모델이 고급 추론, 자율 코딩, 복잡한
멀티모달 작업을 처리하는 방법을 알아보세요.

코드 몇 줄로 시작해 보세요.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Gemini 3 시리즈 소개

Gemini 3.1 Pro는 광범위한 세계 지식과 모달리티 전반의 고급 추론이 필요한 복잡한 작업에 가장 적합합니다.

Gemini 3 Flash는 Flash의 속도와 가격으로 Pro 수준의 인텔리전스를 제공하는 최신 3 시리즈 모델입니다.

Nano Banana Pro (Gemini 3 Pro Image라고도 함)는 최고 품질의 이미지 생성 모델이며 Nano Banana 2 (Gemini 3.1 Flash Image라고도 함)는 대용량, 고효율, 저가형 모델입니다.

Gemini 3.1 Flash-Lite는 비용 효율적인 모델과 대용량 작업을 위해 구축된 워크호스 모델입니다.

현재 모든 Gemini 3 모델은 프리뷰 버전으로 제공되고 있습니다.

| 모델 ID | 컨텍스트 윈도우 (입력 / 출력) | 지식 단절 | 가격 책정 (입력 / 출력)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 100만 / 64,000 | 2025년 1월 | $0.25 (텍스트, 이미지, 동영상), $0.50 (오디오) / $1.50 |
| **gemini-3.1-flash-image-preview** | 128,000 / 32,000 | 2025년 1월 | $0.25 (텍스트 입력) / $0.067 (이미지 출력)\*\* |
| **gemini-3.1-pro-preview** | 100만 / 64,000 | 2025년 1월 | $2 / $12(토큰 200,000개 미만)   $4 / $18(토큰 200,000개 초과) |
| **gemini-3-flash-preview** | 100만 / 64,000 | 2025년 1월 | $0.50 / $3 |
| **gemini-3-pro-image-preview** | 65,000 / 32,000 | 2025년 1월 | $2 (텍스트 입력) / $0.134 (이미지 출력)\*\* |

*\* 가격은 별도로 명시되지 않는 한 토큰 100만 개당 가격입니다.*
*\*\* 이미지 가격은 해상도에 따라 다릅니다. 자세한 내용은 [가격 책정 페이지](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)를 참고하세요.*

자세한 한도, 가격 책정, 추가 정보는
[모델 페이지](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko)를 참고하세요.

## Gemini 3의 새로운 API 기능

Gemini 3에는 개발자가 지연 시간, 비용, 멀티모달 충실도를 더 효과적으로 제어할 수 있도록 설계된 새로운 파라미터가 도입되었습니다.

### 사고 수준

Gemini 3 시리즈 모델은 기본적으로 동적 사고를 사용하여 프롬프트를 통해 추론합니다. 대답을 생성하기 전에 모델의 내부 추론 프로세스의 **최대** 깊이를 제어하는 `thinking_level` 파라미터를 사용할 수 있습니다. Gemini 3는 이러한 수준을 엄격한 토큰 보장이 아닌 사고에 대한 상대적 허용치로 취급합니다.

`thinking_level`이 지정되지 않은 경우 Gemini 3는 기본적으로 `high`로 설정됩니다. 복잡한 추론이 필요하지 않은 경우 더 빠르고 지연 시간이 짧은 대답을 위해 모델의 사고 수준을 `low`로 제한할 수 있습니다.

| 사고 수준 | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | 설명 |
| --- | --- | --- | --- | --- |
| **`minimal`** | 지원되지 않음 | 지원됨 (기본값) | 지원됨 | 대부분의 쿼리에 '사고 없음' 설정과 일치합니다. 모델은 복잡한 코딩 작업에 대해 매우 최소한으로 생각할 수 있습니다. 채팅 또는 고처리량 애플리케이션의 지연 시간을 최소화합니다. `minimal`은 사고가 중지됨을 보장하지 않습니다. |
| **`low`** | 지원됨 | 지원됨 | 지원됨 | 지연 시간과 비용을 최소화합니다. 간단한 지시 수행, 채팅 또는 고처리량 애플리케이션에 가장 적합합니다. |
| **`medium`** | 지원됨 | 지원됨 | 지원됨 | 대부분의 작업에 대한 균형 잡힌 사고입니다. |
| **`high`** | 지원됨 (기본값, 동적) | 지원됨 (동적) | 지원됨 (기본값, 동적) | 추론 깊이를 극대화합니다. 모델이 첫 번째 (사고 없음) 출력 토큰에 도달하기까지 시간이 더 오래 걸릴 수 있지만, 출력은 훨씬 더 신중하게 추론됩니다. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### 온도

모든 Gemini 3 모델의 경우 온도 파라미터를 기본값인 `1.0`으로 유지하는 것이 가장 좋습니다.

이전 모델에서는 창의성과 결정성 간 균형을 위해 온도 조정이 도움이 되었지만, Gemini 3의 추론 기능은 기본 설정에 최적화되어 있습니다. 온도를 변경하여 (1.0 미만으로 설정) 복잡한 수학적 또는 추론 작업에서 루핑이나 성능 저하와 같은 예기치 않은 동작이 발생할 수 있습니다.

### 사고 서명

Gemini 3 모델은 사고 서명을 사용하여 API 호출 전반에서 추론 컨텍스트를 유지합니다. 이러한 서명은 모델의 내부 사고 프로세스를 암호화하여 표현한 것입니다.

- **상태 저장 모드 (권장)**: 상태 저장 모드에서 상호작용 API를 사용하는 경우 (`previous_interaction_id` 제공) 서버는 대화 기록과 사고 서명을 자동으로 관리합니다.
- **상태 비저장 모드**: 대화 기록을 수동으로 관리하는 경우 후속 요청에 서명이 포함된 사고 블록을 포함하여 진위 여부를 확인해야 합니다.

자세한 내용은 [사고 서명](https://ai.google.dev/gemini-api/docs/thinking?hl=ko) 페이지를 참고하세요.

### 도구를 사용한 구조화된 출력

Gemini 3 모델을 사용하면 [구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)을
Google 검색으로 [그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko), [URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko), [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko), [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)을 비롯한 기본 제공 도구와 결합할 수 있습니다.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### 이미지 생성

Gemini 3.1 Flash Image 및 Gemini 3 Pro Image를 사용하면 텍스트 프롬프트에서 이미지를 생성하고 수정할 수 있습니다. 추론을 사용하여 프롬프트를 "생각"하고 고충실도
이미지를 생성하기 전에 [Google 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko) 그라운딩을 사용하기 전에 일기 예보 또는 주식 차트와 같은
실시간 데이터를 가져올 수 있습니다.

**새로운 기능 및 개선된 기능:**

- **4K 및 텍스트 렌더링:** 최대 2K 및 4K 해상도로 선명하고 읽기 쉬운 텍스트와 다이어그램을 생성합니다.
- **그라운딩된 생성:** `google_search` 도구를 사용하여 사실을 확인하고 실제 정보를 기반으로 이미지를 생성합니다. Gemini 3.1 Flash Image에서 Google *이미지* 검색으로 그라운딩을 사용할 수 있습니다.
- **대화 기반 수정:** 변경사항을 요청하기만 하면 되는 멀티턴 이미지 수정 (예: '배경을 일몰로 만들어 줘'). 이 워크플로는 **사고 서명** 을 사용하여 턴 간에 시각적 컨텍스트를 유지합니다.

가로세로 비율, 수정 워크플로, 구성
옵션에 관한 자세한 내용은 [이미지 생성 가이드](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)를 참고하세요.

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**응답 예시**

![도쿄 날씨](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=ko)

### 이미지를 사용한 코드 실행

Gemini 3 Flash는 비전을 정적인 시선이 아닌 능동적인 조사로 취급할 수 있습니다. 추론과 [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)을 결합하여 모델은 계획을 수립한 다음 Python 코드를 작성하고
실행하여 이미지를
단계별로 확대/축소, 자르기, 주석 처리 또는 조작하여 대답을 시각적으로 그라운딩합니다.

**사용 사례:**

- **확대/축소 및 검사:** 모델은 세부정보가 너무 작을 때 (예: 멀리 있는 게이지 또는 일련번호 읽기)를 암시적으로 감지하고 코드를 작성하여 영역을 더 높은 해상도로 자르고 다시 검사합니다.
- **시각적 수학 및 플로팅:** 모델은 코드를 사용하여 다단계 계산을 실행할 수 있습니다 (예: 영수증의 품목 합산 또는 추출된 데이터에서 Matplotlib 차트 생성).
- **이미지 주석:** 모델은 이미지에 직접 화살표, 경계 상자 또는 기타 주석을 그려 '이 항목은 어디에 있어야 하나요?'와 같은 공간적 질문에 대답할 수 있습니다.

시각적 사고를 사용 설정하려면 [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)을 도구로 구성하세요. 모델은 필요할 때 코드를 사용하여 이미지를 조작합니다.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

이미지를 사용한 코드 실행에 관한 자세한 내용은 [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko#images)을 참고하세요.

### 멀티모달 함수 응답

[멀티모달 함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko#multimodal)
을 사용하면, 사용자 함수 응답에
멀티모달 객체를 포함할 수 있어, 함수 호출
기능을 더욱 효과적으로 활용할 수 있습니다. 표준 함수 호출은 텍스트 기반 함수 응답만 지원합니다.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### 기본 제공 도구와 함수 호출 결합

[Gemini 3를 사용하면 동일한 API 호출에서 기본 제공 도구 (예: Google 검색, URL
컨텍스트 등)와 커스텀 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko) 도구를 사용할 수 있으므로
더 복잡한 워크플로가 가능합니다.](https://ai.google.dev/gemini-api/docs/tools?hl=ko)

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

## Gemini 2.5에서 마이그레이션

Gemini 3는 현재까지 가장 강력한 모델 제품군이며 Gemini 2.5에 비해 단계별 개선을 제공합니다. 마이그레이션할 때 다음 사항을 고려하세요.

- **사고:** 이전에 Gemini 2.5가 추론하도록 강제하기 위해 복잡한 프롬프트 엔지니어링 (예:
  연쇄 사고)을 사용했다면 Gemini 3를
  `thinking_level: "high"` 및 간소화된 프롬프트로 사용해 보세요.
- **온도 설정:** 기존 코드에서 온도를 명시적으로 설정하고 있다면(특히 결정적 출력을 위해 낮은 값으로 설정한 경우), 해당 파라미터를 삭제하고 Gemini 3의 기본값인 1.0을 사용하는 것이 좋습니다. 이는 복잡한 작업에서 잠재적인 루핑 문제나 성능 저하를 방지하는 위함입니다.
- **PDF 및 문서 이해:** 밀도 높은 문서 파싱을 위해 특정 동작에 의존하고 있었다면, 정확도를 유지하기 위해 새로운 `media_resolution_high` 설정을 테스트해 보세요.
- **토큰 소비량:** Gemini 3 기본값으로 마이그레이션하면 PDF의 토큰 사용량은 **증가** 할 수 있지만 동영상의 토큰 사용량은 **감소** 할 수 있습니다. 기본 해상도 상승으로 인해 요청이 컨텍스트 윈도우를 초과한다면 미디어 해상도를 명시적으로 낮추는 것이 좋습니다.
- **이미지 분할:** 이미지 분할 기능 (객체의 픽셀 수준 마스크 반환)은 Gemini 3 Pro 또는 Gemini 3 Flash에서 지원되지 않습니다. 기본 제공되는 이미지 분할 기능이 필요한
  워크로드의 경우, 사고를 끈 상태의 Gemini 2.5 Flash 또는 [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ko)을 계속 사용하는 것이 좋습니다.
- **컴퓨터 사용:** Gemini 3 Pro 및 Gemini 3 Flash는 [컴퓨터
  사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko)을 지원합니다. 2.5 시리즈와 달리 컴퓨터 사용 도구에 액세스하기 위해 별도의 모델을 사용할 필요가 없습니다.
- **도구 지원**: [기본 제공 도구와 함수 호출을 결합](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko)할 수 있습니다. [지도
  그라운딩](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko)도 이제 Gemini 3
  모델에서 지원됩니다.

## OpenAI 호환성

[OpenAI 호환성 레이어를 사용하는 경우, 표준 파라미터 (OpenAI의 `reasoning_effort`)는 자동으로 Gemini (`thinking_level`)에 상응하는 파라미터로 매핑됩니다.](https://ai.google.dev/gemini-api/docs/openai?hl=ko)

## 프롬프트 권장사항

Gemini 3는 추론 모델이므로 프롬프트 작성 방식에도 변화가 필요합니다.

- **정확한 지시:** 입력 프롬프트는 간결하게 작성하세요. Gemini 3는 직접적이고 명확한 지시에 가장 잘 반응합니다. 이전 모델에서 사용되던 장황하거나 지나치게 복잡한 프롬프트 엔지니어링 기법은 과분석을 유발할 수 있습니다.
- **출력 장황도:** 기본적으로 Gemini 3는 덜 장황하며, 직접적이고 효율적인 답변을 제공하는 것을 선호합니다. 보다 대화형이거나 '수다스러운' 스타일의 응답이 필요하다면, 프롬프트에서 명시적으로 모델을 유도해야 합니다 (예: '친근하고 말이 많은 조수처럼 설명해 주세요').
- **컨텍스트 관리:** 대규모 데이터 세트 (예: 전체 도서, 코드베이스 또는 긴 동영상)로 작업할 때는 데이터 컨텍스트 뒤에 프롬프트 끝에 구체적인 지시 또는 질문을 배치합니다. '이전 정보를 바탕으로...'와 같은 문구로 질문을 시작하여 제공된 데이터에 모델의 추론을 고정합니다.

프롬프트 설계 전략에 관한 자세한 내용은 [프롬프트 엔지니어링 가이드](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ko)를 참고하세요.

## FAQ

1. **Gemini 3의 지식 단절 시점은 언제인가요?** Gemini 3 모델의 지식 단절 시점은 2025년 1월입니다. 최신 정보는
   [검색 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko) 도구를 사용하세요.
2. **컨텍스트 윈도우 한도는 어떻게 되나요?** Gemini 3 모델은 최대 100만 토큰의 입력 컨텍스트 윈도우와 최대 64,000의 토큰 출력을 지원합니다.
3. **Gemini 3에 무료 등급이 있나요?** Gemini 3 Flash `gemini-3-flash-preview`에는 Gemini API에 무료 등급이 있습니다. Google AI Studio에서 Gemini 3.1 Pro 및 3 Flash를 무료로 사용해 볼 수 있지만 Gemini API의 `gemini-3.1-pro-preview`에는 무료 등급이 없습니다.
4. **이전 `thinking_budget` 코드가 계속 작동하나요?** 예, `thinking_budget`은 이전 버전과의 호환성을 위해 계속 지원되지만 더 예측 가능한 성능을 위해 `thinking_level`로 마이그레이션하는 것이 좋습니다. 동일한 요청에서 두 가지를 모두 사용하지 마세요.
5. **Gemini 3는 Batch API를 지원하나요?** 예, Gemini 3는
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)를 지원합니다.
6. **컨텍스트 캐싱이 지원되나요?** 예, [컨텍스트 캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)이 Gemini 3에서 지원됩니다.
7. **Gemini 3에서 지원되는 도구는 무엇인가요?** Gemini 3는
   [Google 검색](https://ai.google.dev/gemini-api/docs/google-search?hl=ko),
   [Google 지도 그라운딩](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko),
   [파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko),
   [코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko), 및
   [URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko)를 지원합니다. 또한 자체 커스텀 도구와
   기본 제공 도구와
   [함께](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko)표준 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)을
   지원합니다.
8. **`gemini-3.1-pro-preview-customtools`이란 무엇인가요?**
   `gemini-3.1-pro-preview`를 사용 중이고 모델이
   bash 명령어를 선호하여 커스텀 도구를 무시하는 경우 대신 `gemini-3.1-pro-preview-customtools` 모델을 사용해 보세요.
   자세한 내용은 [여기][customtools-model]를 참고하세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-08(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-08(UTC)"],[],[]]
