---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ko
fetched_at: 2026-09-14T05:40:00.684995+00:00
title: "\ub3d9\uc601\uc0c1 \uc774\ud574 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs/generate-content?hl=ko)

의견 보내기

# 동영상 이해

> 동영상 생성에 대해 알아보려면 [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=ko) 가이드를 참고하세요.

Gemini 모델은 동영상을 처리할 수 있으므로 이전에는 도메인별 모델이 필요했던 많은 최첨단 개발자 사용 사례를 지원합니다.
Gemini의 비전 기능에는 동영상에서 정보를 설명, 분할, 추출하고, 동영상 콘텐츠에 관한 질문에 답변하고, 동영상 내의 특정 타임스탬프를 참조하는 기능이 포함됩니다.

다음과 같은 방법으로 Gemini에 동영상을 입력으로 제공할 수 있습니다.

| 입력 방법 | 최대 크기 | 권장 사용 사례 |
| --- | --- | --- |
| [File API](#upload-video) | 20GB (유료) / 2GB (무료) | 대용량 파일 (100MB 이상), 긴 동영상 (10분 이상), 재사용 가능한 파일 |
| [Cloud Storage 등록](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ko#registration) | 2GB (파일당, 스토리지 제한 없음) | 대용량 파일 (100MB 이상), 긴 동영상 (10분 이상), 영구적이고 재사용 가능한 파일 |
| [인라인 데이터](#inline-video) | 100MB 미만 | 작은 파일(100MB 미만), 짧은 길이(1분 미만), 일회성 입력 |
| [YouTube URL](#youtube) | 해당 사항 없음 | 공개 YouTube 동영상 |

> **참고:** [File API](#upload-video)는 대부분의 사용 사례, 특히 100MB보다 큰 파일의 경우 또는 여러 요청에서 파일을 재사용하려는 경우에 권장됩니다.

외부 URL 또는 Google Cloud에 저장된 파일 사용과 같은 다른 파일 입력 방법에 대해 알아보려면
[파일 입력 방법](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ko) 가이드를 참고하세요.

### 동영상 파일 업로드

다음 코드는 샘플 동영상을 다운로드하고, [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ko)를 사용하여 업로드하고,
처리가 완료될 때까지 기다린 후, 업로드된 파일 참조를 사용하여
동영상을 요약합니다.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)

fmt.Println(result.Text())
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

토큰 효율성과 성능을 최적화하려면
[에이전트형 동영상 처리](#agentic-video-understanding)를 사용하는 것이 좋습니다.

파일, 텍스트 프롬프트, 시스템 안내 등을 포함한 총 요청 크기가 20MB보다 크거나, 동영상 길이가 길거나, 여러 프롬프트에서 동일한 동영상을 사용하려는 경우 항상 Files API를 사용하세요.
File API는 동영상 파일 형식을 직접 허용합니다.

미디어 파일 작업에 대해 자세히 알아보려면
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ko)를 참고하세요.

### 동영상 데이터를 인라인으로 전달

File API를 사용하여 동영상 파일을 업로드하는 대신 `generateContent` 요청에서 더 작은 동영상을 직접 전달할 수 있습니다. 이는 총 요청 크기가 20MB 미만인 짧은 동영상에 적합합니다.

다음은 인라인 동영상 데이터를 제공하는 예입니다.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "video/mp4",
      data: base64VideoFile,
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"video/mp4",
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"
              }
            },
            {"text": "Please summarize the video in 3 sentences."}
        ]
      }]
    }' 2> /dev/null
```

### YouTube URL 전달

다음과 같이 요청의 일부로 YouTube URL을 Gemini API에 직접 전달할 수 있습니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [
  {
    fileData: {
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Please summarize the video in 3 sentences."},
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
              }
            }
        ]
      }]
    }' 2> /dev/null
```

**제한사항:**

- 무료 등급의 경우 하루에 8시간 이상의 YouTube 동영상을 업로드할 수 없습니다.
- 유료 등급의 경우 동영상 길이에 따른 제한이 없습니다.
- Gemini 2.5 이전 모델의 경우 요청당 동영상 1개만 업로드할 수 있습니다. Gemini 2.5 이상 모델의 경우 요청당 최대 10개의 동영상을 업로드할 수 있습니다.
- 공개 동영상만 업로드할 수 있습니다 (비공개 또는 일부 공개 동영상은 업로드할 수 없음).

## 에이전트형 동영상 이해

기본적으로 동영상 입력은 정적 처리 (1FPS로 프레임 추출)를 사용합니다.
Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite 모델은 모델이 동영상
타임라인을 동적으로 탐색하고, 트랜스크립트를 선택적으로 검사하고, 프롬프트에 따라 즉석에서 프레임
속도와 해상도를 적응적으로 조정하는
**에이전트형 동영상 이해**도 지원합니다.

| **모드** | **설명** | **지원되는 모델** |
| --- | --- | --- |
| **정적** (기본값) | 고정된 속도 (1FPS)로 프레임을 추출하고 단일 패스에서 컨텍스트에 배치합니다. 짧은 클립에 적합합니다. | 모든 Gemini 모델 |
| **에이전트형** | 모델은 동영상 타임라인을 동적으로 탐색하며 프롬프트에 따라 필요한 콘텐츠만 로드합니다. 긴 형식 콘텐츠에서 최대 88% 더 토큰 효율적이고 품질이 약 7% 더 높습니다. | Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite |

### 처리 모드 선택

일반적인 가이드라인으로, 특히 응답 품질 또는 토큰 효율성을 최적화할 때는 **에이전트형** 모드로 시작하세요.

- **에이전트형:** 긴 형식 동영상 또는 특정 순간을 타겟팅하는 쿼리. 모델은 컨텍스트 윈도우를 채우지 않고 타임라인을 동적으로 탐색하여 컨텍스트와 관련된 정보를 타겟팅합니다.
- **정적:** 짧은 클립 (5분 미만)에 대한 지연 시간에 민감한 쿼리 또는 전체 클립에서 프레임 수준의 정밀도가 필요한 경우.

> **참고:** 에이전트형 처리에 시간이 더 오래 걸리는 긴 동영상 또는 복잡한 프롬프트의 경우 스트리밍 (`client.models.generate_content_stream`)을 사용하세요. 이렇게 하면 연결이 활성 상태로 유지되고, 중간 추론 단계가 표시되며, 연결 또는 인증 시간 초과가 방지됩니다.

### 처리 모드 설정

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=video_file.uri,
            mime_type=video_file.mime_type,
            media_processing="AGENTIC",
        ),
        "What are the three main arguments presented?",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" },
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: videoFile.uri,
            mimeType: videoFile.mimeType,
          },
          mediaProcessing: "AGENTIC",
        },
        { text: "What are the three main arguments presented?" },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/lecture.mp4", nil)
parts := []*genai.Part{
    {
        FileData: &genai.FileData{
            FileURI:  uploadedFile.URI,
            MIMEType: uploadedFile.MIMEType,
        },
        MediaProcessing: genai.MediaProcessingAgentic,
    },
    genai.NewPartFromText("What are the three main arguments presented?"),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${file_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {"text": "What are the three main arguments presented?"}
      ]
    }]
  }'
```

> **참고:** 에이전트형 처리가 사용되었는지 확인하려면 `response.candidates[0].content.parts`를 검사하세요. `MEDIA_PROCESSING` 도구 유형이 있는 `tool_call` 및 `tool_response` 부분이 있으면 모델이 동영상을 동적으로 탐색했음을 나타냅니다.

> **참고:** 다른 서버 측 도구 (예: Google 검색 또는 URL 컨텍스트)와 달리 에이전트형 동영상은 도구 호출 및 결과가 반환되거나 스트리밍되도록 `ToolConfig`에서 `include_server_side_tool_invocations=True`를 설정할 필요가 없습니다. 동영상 탐색을 위한 `tool_call` 및 `tool_response` 부분은 입력 부분에 `media_processing="AGENTIC"`이 설정되면 자동으로 반환됩니다.

### 응답 구조

에이전트형 처리가 사용 설정되면 응답에 내부 탐색 추적을 노출하는 추가 부분이 포함됩니다.

- `tool_call` **부분** (`tool_type: "MEDIA_PROCESSING"`): 모델이 동영상 세그먼트 또는 오디오 트랜스크립트를 요청할 때마다 내보내집니다.
- `tool_response` **부분** (`tool_type: "MEDIA_PROCESSING"`): 각 로드 작업의 결과입니다.

이러한 부분을 수동으로 처리하거나 응답할 필요는 없습니다. 전체 응답을 대화 기록으로 다시 전달하면 자동으로 처리됩니다.

`ThinkingConfig`에서 `include_thoughts=True`가 설정되면 추론 단계가 도구 호출/응답 쌍과 인터리브된 `thought: true` 부분으로 표시됩니다. 생각이 사용 중지되면 생각 텍스트는 생략되지만 도구 부분은 계속 표시됩니다.

다음 예는 인터리브된 도구 호출 및 응답 부분이 있는 응답 페이로드를 보여줍니다.

```
{
  "candidates": [
    {
      "content": {
        "role": "model",
        "parts": [
          {
            "thought": true,
            "text": "Inspecting transcript for key discussion topics..."
          },
          {
            "thought_signature": "sig_A",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_B",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Loading visual frames to verify slide content..."
          },
          {
            "thought_signature": "sig_C",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_D",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Synthesizing answer from gathered evidence..."
          },
          {
            "text": "The three main arguments presented in the lecture are...",
            "thought_signature": "sig_E"
          }
        ]
      }
    }
  ]
}
```

### 동영상 간 처리 모드 혼합

동일한 요청에서 각 동영상 부분에 대해 서로 다른 처리 모드를 설정할 수 있습니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=lecture.uri,
            mime_type=lecture.mime_type,
            media_processing="AGENTIC",  # Use agentic video understanding
        ),
        types.Part.from_uri(
            file_uri=experiment.uri,
            mime_type=experiment.mime_type,
            media_processing="STATIC",  # Use static processing
        ),
        "Compare the lecture content with the experiment results.",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" },
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" },
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: lecture.uri,
            mimeType: lecture.mimeType,
          },
          mediaProcessing: "AGENTIC", // Use agentic video understanding
        },
        {
          fileData: {
            fileUri: experiment.uri,
            mimeType: experiment.mimeType,
          },
          mediaProcessing: "STATIC", // Use static processing
        },
        { text: "Compare the lecture content with the experiment results." },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
lecturePart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  lectureFile.URI,
        MIMEType: lectureFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingAgentic, // Use agentic
}
experimentPart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  experimentFile.URI,
        MIMEType: experimentFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingStatic, // Use static
}
parts := []*genai.Part{
    lecturePart,
    experimentPart,
    genai.NewPartFromText("Compare the lecture content with the experiment results."),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${lecture_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {
          "file_data": {
            "file_uri": "'${experiment_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "STATIC"
        },
        {"text": "Compare the lecture content with the experiment results."}
      ]
    }]
  }'
```

## 긴 동영상에 컨텍스트 캐싱 사용

10분보다 긴 동영상의 경우 또는 동일한 동영상 파일에 대해 여러 요청을 계획하는 경우 [컨텍스트 캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)을 사용하여 비용을 절감하고 지연 시간을 개선하세요. 컨텍스트 캐싱을 사용하면 동영상을 한 번 처리하고 후속 쿼리에 토큰을 재사용할 수 있으므로 채팅 세션 또는 긴 형식 콘텐츠의 반복 분석에 적합합니다.

## 콘텐츠의 타임스탬프 참조

`MM:SS` 형식의 타임스탬프를 사용하여 동영상 내의 특정 시점에 관한 질문을 할 수 있습니다.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
          // Adjusted timestamps for the NASA video
        genai.NewPartFromText("What are the examples given at 00:05 and " +
            "00:10 supposed to show us?"),
    }
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## 동영상에서 세부적인 유용한 정보 추출

Gemini 모델은 **오디오 및 시각적** 스트림 모두에서 정보를 처리하여 동영상 콘텐츠를 이해하는 강력한 기능을 제공합니다. 이를 통해 동영상에서 발생하는 상황에 관한 설명을 생성하고 콘텐츠에 관한 질문에 답변하는 등 다양한 세부정보를 추출할 수 있습니다.

시각적 설명의 경우 모델은 **초당 1프레임** (FPS)의 속도로 동영상을 샘플링합니다. 이 기본 샘플링 속도는 대부분의 콘텐츠에 적합하지만, 동작이 빠르거나 장면이 빠르게 바뀌는 동영상의 세부정보는 놓칠 수 있습니다.
이러한 동작이 많은 콘텐츠의 경우 [커스텀 프레임 속도를 설정하는 것](#custom-frame-rate)이 좋습니다.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
        genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
      "Include timestamps for salient moments."),
    }
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## 동영상 처리 맞춤설정

클리핑 간격을 설정하거나 커스텀 프레임 속도 샘플링을 제공하여 Gemini API에서 동영상 처리를 맞춤설정할 수 있습니다. 이러한 맞춤설정 옵션
은 `"static"` 모드에서 동영상을 처리할 때만 지원됩니다.

### 클리핑 간격 설정

시작 및 종료 오프셋으로 `videoMetadata`를 지정하여 동영상을 클립할 수 있습니다.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3.8-flash';

async function main() {
const contents = [
  {
    role: 'user',
    parts: [
      {
        fileData: {
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',
          mimeType: 'video/*',
        },
        videoMetadata: {
          startOffset: '40s',
          endOffset: '80s',
        }
      },
      {
        text: 'Please summarize the video in 3 sentences.',
      },
    ],
  },
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### 커스텀 프레임 속도 설정

`fps` 인수를 `videoMetadata`에 전달하여 커스텀 프레임 속도 샘플링을 설정할 수 있습니다.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

기본적으로 동영상에서 초당 1프레임 (FPS)이 샘플링됩니다. 긴 동영상의 경우 낮은 FPS(< 1)를 설정하는 것이 좋습니다. 이는 대부분 정적 동영상 (예: 강의)에 특히 유용합니다. 빠른 동작 이해 또는 고속 동작 추적과 같이 세분화된 시간 분석이 필요한 동영상의 경우 더 높은 FPS를 사용하세요.

## 지원되는 동영상 형식

Gemini는 다음과 같은 동영상 형식 MIME 유형을 지원합니다.

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## 동영상에 대한 기술 세부정보

- **지원되는 모델 및 컨텍스트**: 모든 Gemini 모델은 동영상 데이터를 처리할 수 있습니다.
  - 1M 컨텍스트 윈도우가 있는 모델은 기본적으로 최대 3시간 길이의 동영상 (낮은 미디어 해상도) 또는 높은 미디어 해상도에서 최대 1시간 길이의 동영상을 처리할 수 있습니다.
- **처리 모드**: Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite,
  및 이후 모델은 두 가지 동영상 처리 모드를 지원합니다.
  - **정적**: 프레임이 1FPS로 추출되어 컨텍스트에 배치됩니다 (모든 모델의 기본값
    ). 오디오는 1Kbps (단일 채널)로 처리됩니다.
    타임스탬프는 매초마다 추가됩니다. 짧은 클립에 적합하거나 모든 프레임이 중요한 경우 (예: 프레임별 검사). 1FPS 샘플링 속도로 인해 빠른 동작 시퀀스의 세부정보가 손실될 수 있습니다.
  - **에이전트형**: 모델은 동영상을 동적으로 탐색하며 요청 시
    트랜스크립트 또는 프레임 또는 오디오를 로드합니다. 생성이 시작되기 전에 내부 추론 및 도구 왕복으로 인해 탐색이 짧은 클립 (5분 미만)에서 첫 번째 토큰까지의 시간(TTFT)을 약간 늘릴 수 있지만, 긴 형식 콘텐츠의 경우 최대 88% 더 적은 토큰을 사용합니다.
    응답에는 턴 간에 추론 컨텍스트를 유지하기 위한 `MEDIA_PROCESSING` 도구 호출 및 응답 부분이 포함됩니다. 토큰 비용과 응답 품질을 최적화하기 위한 긴 형식 동영상에 가장 적합합니다. Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite에서 지원됩니다. 자세한 내용은
    [에이전트형 동영상 이해](#agentic-video-understanding)를 참고하세요.
- **토큰 계산 (정적 모드)**: 동영상의 각 초는 다음과 같이 토큰화됩니다.
  - 개별 프레임 (1FPS로 샘플링됨):
    - `media_resolution`이 낮음으로 설정되면 프레임이 프레임당 66개 토큰으로 토큰화됩니다.
    - 그렇지 않으면 프레임이 프레임당 258개의 토큰으로 토큰화됩니다.
  - 오디오: 초당 토큰 32개
  - 메타데이터도 포함됩니다.
  - 총계: 기본 (낮음) 미디어 해상도 동영상에서 초당 약 100개 토큰 또는 높은 미디어 해상도 동영상에서 초당 약 300개 토큰
- **토큰 계산 (에이전트형 모드)**: 토큰 사용량은 콘텐츠
  복잡성과 모델의 탐색 전략에 따라 다릅니다. 동영상 탐색 중에 생성된 탐색 추론 토큰은 **생각 토큰**(`thoughts_token_count`)으로 계산되는 반면, 요청 시 로드된 프레임, 오디오, 트랜스크립트는 도구 프롬프트 토큰 (`tool_use_prompt_token_count`)으로 계산됩니다. 에이전트형 처리는 일반적으로 모델이 프롬프트에 답변하는 데 필요한 트랜스크립트 또는 프레임 또는 오디오만 로드하므로 긴 형식 콘텐츠의 경우 정적 처리보다 총 토큰을 최대 88% 더 적게 사용합니다 ([토큰 가이드](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=ko#video-token-usage) 참고).
- **미디어 해상도**: Gemini 3는 멀티모달
  비전 처리에 대한 세밀한 제어 기능을 `media_resolution` 파라미터를 통해 제공합니다. `media_resolution` 파라미터는 **입력 이미지 또는 동영상 프레임당 할당되는 최대 토큰 수** 를 결정합니다. 해상도가 높을수록 모델이 작은 텍스트를 읽거나 세부 요소를 식별하는 능력을 향상시키지만, 토큰 사용량과 지연 시간이 증가합니다. `media_resolution` 및 `media_processing` 파라미터는 독립적입니다. 동일한 동영상 부분에 둘 다 설정할 수 있습니다.

토큰 계산에 관한 자세한 내용은
[토큰](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=ko) 가이드를 참고하세요.

- **타임스탬프 형식**: 프롬프트 내에서 동영상의 특정 순간을 언급할 때는 `MM:SS` 형식을 사용하세요 (예: 1분 15초의 경우 `01:15`).
- **프롬프트 배치**: 텍스트와 단일 동영상을 결합하는 경우 `contents` 배열의 동영상 부분
  *뒤에* 텍스트 프롬프트를 배치합니다.
- **긴 요청의 시간 초과**: 처리 시간이 길거나 복잡한 다단계 추론이 필요한 동영상의 경우 스트리밍
  (`client.models.generate_content_stream`)을 사용하세요. 수요가 많은 경우 백엔드 재시도가 발생하는 동기식 비스트리밍
  요청은 연결 또는 인증 토큰 유효성 검사 기간을 초과할 수 있으며, 이로 인해 예기치 않은 `401 Unauthorized` 또는 시간 초과 오류가 발생할 수 있습니다. 스트리밍은 연결을 활성 상태로 유지하고 중간 추론 및 도구 호출 진행 상황을 표시합니다.

## 다음 단계

- [미디어 해상도](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=ko): 동영상 프레임의
  해상도를 제어하여 품질과 토큰 사용량의 균형을 맞춥니다.
- [토큰](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=ko): 정적 및 에이전트형 처리 모드 모두에서 동영상 콘텐츠가 토큰화되는 방식을 이해합니다.
- [시스템 안내](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ko#system-instructions):
  시스템 안내를 사용하면 특정 요구사항 및 사용 사례에 따라 모델의 동작을 조정할 수 있습니다.
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ko): Gemini에서 사용할
  파일을 업로드하고 관리하는 방법을 자세히 알아봅니다.
- [파일 프롬프트 전략](https://ai.google.dev/gemini-api/docs/files?hl=ko#prompt-guide): Gemini API는 멀티모달 프롬프트 사용이라고도 하는 텍스트, 이미지, 오디오, 동영상 데이터로 프롬프트를 지원합니다.
- [안전 가이드](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ko): 생성형 AI
  모델은 때때로 부정확하거나
  편향되거나 불쾌감을 주는 등 예기치 않은 출력을 생성합니다. 후처리 및 인간 평가가 이러한 출력으로 인한 피해 위험을 제한하는 데 필수적입니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-12(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-12(UTC)"],[],[]]
