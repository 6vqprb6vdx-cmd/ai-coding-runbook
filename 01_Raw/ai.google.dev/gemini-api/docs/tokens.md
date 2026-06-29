---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=ko
fetched_at: 2026-06-29T05:33:59.185386+00:00
title: "\ud1a0\ud070 \uc774\ud574 \ubc0f \uacc4\uc0b0 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 토큰 이해 및 계산

Gemini 및 기타 생성형 AI 모델은 *토큰* 이라는 세분화된 수준에서 입력과 출력을 처리합니다.

**Gemini 모델의 경우 토큰은 약 4자와 같습니다.
토큰 100개는 영어 단어 약 60~80개와 같습니다.**

## 토큰 정보

토큰은 단일 문자(예: `z`) 또는 전체 단어(예: `cat`)일 수 있습니다. 긴 단어는 여러 토큰으로 나뉩니다. 모델에서 사용하는 모든 토큰 집합을 어휘라고 하며, 텍스트를 토큰으로 분할하는 프로세스를 *토큰화* 라고 합니다.

결제가 사용 설정된 경우 [Gemini API 호출 비용](https://ai.google.dev/pricing?hl=ko)은
입력 및 출력 토큰 수에 따라 결정되므로 토큰 수를
계산하는 방법을 알아두면 유용합니다.

## 토큰 집계

Gemini API의 모든 입력 및 출력은 텍스트, 이미지 파일, 기타 텍스트가 아닌 양식을 포함하여 토큰화됩니다.

다음과 같은 방법으로 토큰을 집계할 수 있습니다.

- **요청의 입력으로 `count_tokens`를 호출합니다.** *입력에만* 있는 총 토큰 수를 반환합니다. 입력을 보내기 전에 이 호출을 실행하여 요청의 크기를 확인합니다.
- **상호작용 응답에서 `usage`를 사용합니다.** 입력 (`total_input_tokens`), 출력 (`total_output_tokens`), 생각 (`total_thought_tokens`), 캐시된 콘텐츠(`total_cached_tokens`), 도구 사용 (`total_tool_use_tokens`), 총 (`total_tokens`)의 토큰 수를 반환합니다.

### 텍스트 토큰 집계

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
const countResponse = await client.models.countTokens({
    model: "gemini-3.5-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### 멀티턴 토큰 집계

`previous_interaction_id`를 사용하여 대화 기록에서 토큰을 집계합니다.

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's my name?",
    previous_interaction_id=interaction1.id
)

# Usage includes tokens from both turns
print(f"Input tokens: {interaction2.usage.total_input_tokens}")
print(f"Output tokens: {interaction2.usage.total_output_tokens}")
print(f"Total tokens: {interaction2.usage.total_tokens}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// First interaction
const interaction1 = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### 멀티모달 토큰 집계

이미지, 동영상, 오디오를 비롯한 Gemini API의 모든 입력은 토큰화됩니다.
토큰화에 관한 핵심 사항은 다음과 같습니다.

- **이미지**: 두 치수가 모두 384픽셀 이하인 이미지는 토큰 258개로 집계됩니다. 더 큰 이미지는 768x768픽셀 타일로 바둑판식으로 배열되며 각 타일은 토큰 258개로 집계됩니다.
- **동영상**: 초당 토큰 263개
- **오디오**: 초당 토큰 32개

#### 이미지 토큰

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Tell me about this image"},
        {"type": "image", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type}
    ]
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const uploadedFile = await client.files.upload({
    file: "path/to/image.jpg",
    config: { mimeType: "image/jpeg" }
});

// Count tokens
const countResponse = await client.models.countTokens({
    model: "gemini-3.5-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

**인라인 데이터 예시:**

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.usage)
```

#### 동영상 토큰

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 263 * 60 = 15,780 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### 오디오 토큰

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### 시스템 안내 토큰 집계

시스템 안내는 입력 토큰의 일부로 집계됩니다.

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### 도구 토큰 집계

도구 (함수, 코드 실행, Google 검색)도 집계됩니다.

### Python

```
# This will only work for SDK newer than 2.0.0
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## 컨텍스트 윈도우

각 Gemini 모델에는 처리할 수 있는 최대 토큰 수가 있습니다. 컨텍스트 윈도우는 입력 및 출력 토큰의 결합된 한도를 정의합니다.

### 프로그래매틱 방식으로 컨텍스트 윈도우 크기 가져오기

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.5-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.5-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

[모델 페이지에서 컨텍스트 윈도우 크기를 확인합니다.](https://ai.google.dev/gemini-api/docs/models?hl=ko)

## 다음 단계

- [텍스트 생성](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko): 생성 기본사항
- [캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko): 캐싱으로 비용 절감
- [가격 책정](https://ai.google.dev/gemini-api/docs/pricing?hl=ko): 비용 이해

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-22(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-22(UTC)"],[],[]]
