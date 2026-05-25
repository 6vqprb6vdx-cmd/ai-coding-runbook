---
source_url: https://ai.google.dev/gemini-api/docs/interactions/audio?hl=ko
fetched_at: 2026-05-25T13:07:07.099271+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 오디오 이해

Gemini는 오디오 입력을 분석하여 텍스트 응답을 생성할 수 있습니다.

### Python

```
from google import genai
import base64

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this audio clip"},
        {
            "type": "audio",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const uploadedFile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mp3" }
});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        {type: "text", text: "Describe this audio clip"},
        {
            type: "audio",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# First upload the file, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Describe this audio clip"},
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

## 개요

Gemini는 오디오 입력을 분석하고 이해하여 텍스트 응답을 생성할 수 있으므로 다음과 같은 사용 사례가 가능합니다.

- 오디오 콘텐츠에 대해 설명, 요약 또는 질문에 대한 답변
- 자막 생성 및 번역 (음성 텍스트 변환)
- 화자 분할 (서로 다른 화자 식별)
- 음성 및 음악의 감정 감지
- 타임스탬프를 사용하여 특정 세그먼트 분석

실시간 음성 및 동영상 상호작용은 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ko)를 참고하세요.
실시간 스크립트 작성을 지원하는 전용 음성 텍스트 변환 모델의 경우 [Google Cloud Speech-to-Text API](https://cloud.google.com/speech-to-text?hl=ko)를 사용하세요.

## 음성을 텍스트로 변환

이 예에서는 [구조화된 출력](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=ko)을 사용하여 타임스탬프, 화자 분리, 감정 감지가 포함된 음성을 텍스트로 변환하고, 번역하고, 요약하는 방법을 보여줍니다.

### Python

```
from google import genai

client = genai.Client()

YOUTUBE_URL = "https://www.youtube.com/watch?v=ku-N-eS1lgM"

prompt = """
  Process the audio file and generate a detailed transcription.

  Requirements:
  1. Identify distinct speakers (e.g., Speaker 1, Speaker 2).
  2. Provide accurate timestamps for each segment (Format: MM:SS).
  3. Detect the primary language of each segment.
  4. If not English, provide the English translation.
  5. Identify the primary emotion: Happy, Sad, Angry, or Neutral.
  6. Provide a brief summary at the beginning.
"""

response_schema = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "segments": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "speaker": {"type": "string"},
                    "timestamp": {"type": "string"},
                    "content": {"type": "string"},
                    "language": {"type": "string"},
                    "emotion": {
                        "type": "string",
                        "enum": ["happy", "sad", "angry", "neutral"]
                    }
                },
                "required": ["speaker", "timestamp", "content", "emotion"]
            }
        }
    },
    "required": ["summary", "segments"]
}

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "video", "uri": YOUTUBE_URL, "mime_type": "video/mp4"},
        {"type": "text", "text": prompt}
    ],
    response_format=response_schema,
)

print(interaction.output_text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const YOUTUBE_URL = "https://www.youtube.com/watch?v=ku-N-eS1lgM";

const prompt = `
  Process the audio file and generate a detailed transcription.

  Requirements:
  1. Identify distinct speakers (e.g., Speaker 1, Speaker 2).
  2. Provide accurate timestamps for each segment (Format: MM:SS).
  3. Detect the primary language of each segment.
  4. If not English, provide the English translation.
  5. Identify the primary emotion: Happy, Sad, Angry, or Neutral.
  6. Provide a brief summary at the beginning.
`;

const responseSchema = {
    type: "object",
    properties: {
        summary: { type: "string" },
        segments: {
            type: "array",
            items: {
                type: "object",
                properties: {
                    speaker: { type: "string" },
                    timestamp: { type: "string" },
                    content: { type: "string" },
                    language: { type: "string" },
                    emotion: {
                        type: "string",
                        enum: ["happy", "sad", "angry", "neutral"]
                    }
                },
                required: ["speaker", "timestamp", "content", "emotion"]
            }
        }
    },
    required: ["summary", "segments"]
};

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        { type: "video", uri: YOUTUBE_URL, mime_type: "video/mp4" },
        { type: "text", text: prompt }
    ],
    response_format: responseSchema,
});

console.log(JSON.parse(interaction.output_text));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {
        "type": "video",
        "uri": "https://www.youtube.com/watch?v=ku-N-eS1lgM",
        "mime_type": "video/mp4"
      },
      {
        "type": "text",
        "text": "Transcribe with speaker diarization and emotion detection."
      }
    ],
    "response_format": {
        "type": "object",
        "properties": {
          "summary": {"type": "string"},
          "segments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "speaker": {"type": "string"},
                "timestamp": {"type": "string"},
                "content": {"type": "string"},
                "emotion": {"type": "string", "enum": ["happy", "sad", "angry", "neutral"]}
              }
            }
          }
        }
      }
  }'
```

![다국어 오디오 스크립트 작성 Gemini 앱](https://ai.google.dev/static/gemini-api/docs/images/audio_understanding_demo.gif?hl=ko)

## 입력 오디오

다음과 같은 방법으로 오디오 데이터를 제공할 수 있습니다.

- 요청하기 전에 [오디오 파일을 업로드](#upload-audio)하세요.
- 요청과 함께 [인라인 오디오 데이터를 전달](#inline-audio)합니다.

### 오디오 파일 업로드

20MB보다 큰 파일에는 [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=ko)를 사용합니다.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this audio clip"},
        {
            "type": "audio",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const uploadedFile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mp3" }
});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        {type: "text", text: "Describe this audio clip"},
        {
            type: "audio",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Describe this audio clip"},
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

### 오디오 데이터를 인라인으로 전달

총 요청 크기가 20MB 미만인 작은 오디오 파일의 경우:

### Python

```
from google import genai
import base64

client = genai.Client()

with open('path/to/small-sample.mp3', 'rb') as f:
    audio_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this audio clip"},
        {
            "type": "audio",
            "data": base64.b64encode(audio_bytes).decode('utf-8'),
            "mime_type": "audio/mp3"
        }
    ]
)
print(interaction.output_text)
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

const audioData = fs.readFileSync("path/to/small-sample.mp3", {
    encoding: "base64"
});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        {type: "text", text: "Describe this audio clip"},
        {
            type: "audio",
            data: audioData,
            mime_type: "audio/mp3"
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Describe this audio clip"},
      {
        "type": "audio",
        "data": "'$(base64 $B64FLAGS $AUDIO_PATH)'",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

인라인 오디오 데이터 관련 참고사항:
\* 최대 요청 크기는 총 20MB입니다 (프롬프트 및 모든 파일 포함).
\* 재사용하려면 대신 [파일을 업로드](#upload-audio)하세요.

## 스크립트 받기

스크립트를 받으려면 프롬프트에 요청하세요.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Generate a transcript of the speech."},
        {
            "type": "audio",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        { type: "text", text: "Generate a transcript of the speech." },
        {
            type: "audio",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

## 타임스탬프 참고

`MM:SS` 형식을 사용하여 특정 섹션을 참조합니다.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Provide a transcript from 02:30 to 03:29."},
        {
            "type": "audio",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        { type: "text", text: "Provide a transcript from 02:30 to 03:29." },
        { type: "audio", uri: uploadedFile.uri, mime_type: "audio/mp3" }
    ]
});
```

## 토큰 집계

오디오 파일의 토큰 수 계산:

### Python

```
response = client.models.count_tokens(
    model="gemini-3.5-flash",
    contents=[uploaded_file]
)
print(response)
```

### 자바스크립트

```
const response = await client.models.countTokens({
    model: "gemini-3.5-flash",
    contents: [
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(response.totalTokens);
```

## 지원되는 오디오 형식

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG Vorbis - `audio/ogg`
- FLAC - `audio/flac`

## 오디오에 대한 기술 세부정보

- **토큰**: 오디오 초당 토큰 32개 (1분 = 토큰 1,920개)
- **비언어적 소리**: Gemini는 비언어적 소리 (새소리, 사이렌 등)를 이해합니다.
- **최대 길이**: 프롬프트당 오디오 9시간 30분
- **해상도**: 16Kbps로 다운샘플링됨
- **채널**: 다중 채널 오디오가 단일 채널로 결합됨

## 다음 단계

- [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=ko): 오디오 파일 업로드 및 관리
- [시스템 요청 사항](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ko#system-instructions):
  모델 동작 맞춤설정
- [구조화된 출력](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=ko):
  JSON 형식으로 스크립트 결과 가져오기

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-19(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-19(UTC)"],[],[]]
