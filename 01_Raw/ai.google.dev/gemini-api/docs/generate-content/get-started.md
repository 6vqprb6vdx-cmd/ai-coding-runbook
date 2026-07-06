---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ko
fetched_at: 2026-07-06T05:17:59.440022+00:00
title: "\uc2dc\uc791\ud558\uae30 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 시작하기

이 가이드는 기존 **generateContent** API를 시작하는 데 도움이 됩니다. 새 프로젝트 및 애플리케이션의 경우 에이전트 워크플로와 최신 모델을 위한 간소화된 인터페이스를 제공하는 새로운 **Interactions API** 를 대신 사용하는 것이 좋습니다.

[이 빠른 시작에서는 표준
`generateContent` 메서드를 사용하여 라이브러리를 설치하고 첫 번째 요청을 하고, 대답을 스트리밍하고, 멀티턴 대화를 빌드하고, 도구를 사용하는 방법을 보여줍니다.](https://ai.google.dev/gemini-api/docs/libraries?hl=ko)

## API 키 가져오기

Gemini API를 사용하려면 요청을 인증하고, 보안 한도를 적용하고, 계정 사용량을 추적하는 데 사용할 API 키가 있어야 합니다.

- Google AI Studio는 신규 사용자를 위해 프로젝트와 API 키를 자동으로 만듭니다.
  [API 키](https://aistudio.google.com/api-keys?hl=ko) 페이지에서 복사할 수 있습니다.
- 새 키가 필요한 경우 AI Studio에서 **API 키 만들기** 를 클릭하고 대화상자에 따라 새 키-프로젝트 쌍을 추가합니다.

[Gemini API 키 만들기](https://aistudio.google.com/apikey?hl=ko)

키를 환경 변수로 설정합니다.

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### 유료 등급으로 업그레이드

유료 등급으로 업그레이드하면 비율 한도가 증가하며 Cloud Billing을 설정해야 합니다.

- AI Studio
  [API 키](https://aistudio.google.com/api-keys?hl=ko) 또는
  [프로젝트](https://aistudio.google.com/projects?hl=ko) 페이지에서 **결제 설정**을 클릭합니다.
- Cloud Billing 대화상자에 따라 결제 계정을 만들거나 연결하고, 결제 수단을 추가하고, 유료 크레딧으로 최소 $10 (또는 통화 상당액)을 선불합니다.
- [Google AI Studio](https://aistudio.google.com/usage?hl=ko)
  의 **대시보드** > **사용량**에서 API 사용량을 확인합니다.

자세한 내용은 [결제 페이지](https://ai.google.dev/gemini-api/docs/billing?hl=ko)를 참고하세요.

## Google GenAI SDK 설치

### Python

[Python 3.9+](https://www.python.org/downloads/) 이상을 사용하여 다음
[pip 명령어](https://packaging.python.org/en/latest/tutorials/installing-packages/)를 사용하여
[`google-genai` 패키지](https://pypi.org/project/google-genai/)를 설치합니다.

```
pip install -q -U google-genai
```

### JavaScript

[Node.js v18+](https://nodejs.org/en/download/package-manager)을 사용하여 다음
[npm 명령어](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)를 사용하여
[TypeScript 및 JavaScript용 Google 생성형 AI SDK](https://www.npmjs.com/package/@google/genai)를 설치합니다.

```
npm install @google/genai
```

## 텍스트 생성

`models.generate_content` 메서드를 사용하여
[텍스트 대답을 생성합니다](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko).

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## 대답 스트리밍

기본적으로 모델은 전체 생성 프로세스가 완료된 후에만 대답을 반환합니다. 더 빠르고 상호작용이 가능한 환경을 위해
[대답](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko#stream) 청크가 생성될 때
스트리밍할 수 있습니다.

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## 멀티턴 대화

[멀티턴 대화의 경우 SDK는 대화 기록을 자동으로 관리하는 멀티턴 채팅 환경을 빌드하는 상태 저장 `chats` 도우미를
제공합니다.](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko#chat)

### Python

```
chat = client.chats.create(model="gemini-3.5-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.5-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## 도구 사용하기

Google 검색으로 대답을
[그라운딩하여](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)
실시간 웹 콘텐츠에 액세스함으로써 모델의 기능을 확장합니다. 모델은 검색 시점을 자동으로 결정하고, 쿼리를 실행하고, 대답을 합성합니다.

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

Gemini API는 다음과 같은 다른 기본 제공 도구도 지원합니다.

- **[코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)**:
  모델이 Python 코드를 작성하고 실행하여 복잡한 수학 문제를 해결할 수 있도록 합니다.
- **[URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko)**: 제공하는 특정 웹페이지 URL에서 대답을 그라운딩할 수 있습니다.
- **[파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko)**: 파일을 업로드하고 시맨틱 검색을 사용하여 콘텐츠에서 대답을 그라운딩할 수 있습니다.
- **[Google 지도](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko)**: 위치 데이터에서 대답을 그라운딩하고 장소, 길찾기, 지도를 검색할 수 있습니다.
- **[컴퓨터 사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko)**: 모델이 가상 컴퓨터 화면, 키보드, 마우스와 상호작용하여 작업을 수행할 수 있도록 합니다.

## 커스텀 함수 호출

**[함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)**을 사용하여
모델을 커스텀 도구 및 API에 연결합니다. 모델은 함수를 호출할 시점을 결정하고 애플리케이션이 실행할 수 있도록 대답에 `functionCall`을 반환합니다.

이 예에서는 모의 온도 함수를 선언하고 모델이 이 함수를 호출할지 확인합니다.

### Python

```
from google import genai
from google.genai import types

weather_function = {
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.5-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## 다음 단계

이제 Gemini API를 시작했으므로 다음 가이드를 살펴보고 더 고급 애플리케이션을 빌드하세요.

- [텍스트 생성](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko)
- [이미지 생성](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)
- [이미지 이해](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ko)
- [사고](https://ai.google.dev/gemini-api/docs/thinking?hl=ko)
- [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)
- [Google 검색을 사용한 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)
- [긴 컨텍스트](https://ai.google.dev/gemini-api/docs/long-context?hl=ko)
- [임베딩](https://ai.google.dev/gemini-api/docs/embeddings?hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-01(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-01(UTC)"],[],[]]
