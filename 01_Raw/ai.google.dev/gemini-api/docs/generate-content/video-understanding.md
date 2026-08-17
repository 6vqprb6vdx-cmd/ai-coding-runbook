---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=zh-CN
fetched_at: 2026-08-17T02:18:42.212153+00:00
title: "\u89c6\u9891\u7406\u89e3 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 视频理解

> 如需了解视频生成，请参阅 [Veo](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn) 指南。

Gemini 模型可以处理视频，从而实现许多前沿开发者用例，而这些用例在过去需要使用特定于领域的模型。
Gemini 的一些视觉功能包括：描述视频、对视频进行分段和提取视频中的信息、回答有关视频内容的问题，以及引用视频中的特定时间戳。

您可以通过以下方式向 Gemini 提供视频作为输入：

| 输入法 | 最大大小 | 推荐的使用场景 |
| --- | --- | --- |
| [File API](#upload-video) | 20GB（付费）/ 2GB（免费） | 大型文件（100MB+）、长视频（10 分钟以上）、可重复使用的文件。 |
| [Cloud Storage 注册](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-cn#registration) | 2GB（每个文件，无存储空间限制） | 大型文件（100MB+）、长视频（10 分钟以上）、持久性文件、可重复使用的文件。 |
| [内嵌数据](#inline-video) | < 100MB | 小型文件（<100MB）、时长较短（<1 分钟）、一次性输入。 |
| [YouTube 网址](#youtube) | 不适用 | 公开的 YouTube 视频。 |

> **注意**：对于大多数用例，尤其是对于大于 100MB 的文件或您想在多个请求中重复使用文件时，建议使用 [File API](#upload-video)。

如需了解其他文件输入方法（例如使用外部网址或存储在 Google Cloud 中的文件），请参阅
[文件输入方法](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-cn)指南。

### 上传视频文件

以下代码会下载示例视频，使用 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn) 上传该视频，
等待其处理完毕，然后使用上传的文件引用来
总结视频。

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
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
    model: "gemini-3.6-flash",
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
    "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

如果总请求大小（包括文件、文本提示、系统说明等）超过 20 MB，视频时长较长，或者您打算在多个提示中使用同一视频，请务必使用 Files API。
File API 直接接受视频文件格式。

如需详细了解如何使用媒体文件，请参阅
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn)。

### 以内嵌方式传递视频数据

您可以直接在对 `generateContent` 的请求中传递较小的视频，而无需使用 File API 上传视频文件。此方法适用于总请求大小不超过 20 MB 的较短视频。

以下是提供内嵌视频数据的示例：

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.6-flash',
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
  model: "gemini-3.6-flash",
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

### 传递 YouTube 网址

您可以将 YouTube 网址直接传递给 Gemini API，作为请求的一部分，如下所示：

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.6-flash',
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
  model: "gemini-3.6-flash",
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
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

**限制** ：

- 对于免费层级，您每天上传的 YouTube 视频时长不能超过 8 小时。
- 对于付费层级，没有基于视频时长的限制。
- 对于 Gemini 2.5 之前的模型，您每次请求只能上传 1 个视频。对于 Gemini 2.5 及更高版本的模型，您每次请求最多能上传 10 个视频。
- 您只能上传公开视频（不能上传私享视频或未公开列出的视频）。

## 对长视频使用上下文缓存

对于时长超过 10 分钟的视频，或者当您计划针对同一视频文件发出多个请求
时，请使用 [上下文缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn) 来
降低费用并缩短延迟时间。借助上下文缓存功能，您可以处理一次视频，并在后续查询中重复使用 token，因此非常适合聊天会话或对长篇内容进行重复分析。

## 引用内容中的时间戳

您可以使用 `MM:SS` 格式的时间戳，针对视频中的特定时间点提出问题。

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

## 从视频中提取详细分析洞见

Gemini 模型通过处理**音频和视觉** 信息流中的信息，提供强大的视频内容理解功能。这让您可以提取丰富的信息，包括生成视频中发生的情况的描述，以及回答有关视频内容的问题。

对于视觉描述，模型会以 **1 帧/秒** (FPS) 的速率对视频进行采样。此默认采样率适用于大多数内容，但请注意，它可能会遗漏快速动作或场景快速变化的视频中的细节。
对于此类高动作内容，请考虑[设置自定义帧速率](#custom-frame-rate)。

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

## 自定义视频处理

您可以在 Gemini API 中通过设置剪辑间隔或提供自定义帧速率选段来自定义视频处理。

### 设置剪辑间隔

您可以通过指定包含开始和结束偏移量的 `videoMetadata` 来剪辑视频。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.6-flash',
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
const model = 'gemini-3.6-flash';

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

### 设置自定义帧速率

您可以通过向 `videoMetadata` 传递 `fps` 实参来设置自定义帧速率选段。

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.6-flash',
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

默认情况下，系统会按 1 帧/秒 (FPS) 的速率从视频中提取选段。对于长视频，您可能需要设置较低的 FPS（低于 1）。这对于偏静态的视频（例如讲座）尤其有用。对于需要精细时间分析（例如快速动作理解或高速动作跟踪）的视频，请使用更高的 FPS。

## 支持的视频格式

Gemini 支持以下视频格式 MIME 类型：

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## 有关视频技术方面的详细信息

- **支持的模型和上下文** ：所有 Gemini 都可以处理视频数据。
  - 上下文窗口为 100 万个 token 的模型可以处理时长不超过 1 小时（默认媒体分辨率）或 3 小时（低媒体分辨率）的视频。
- **File API 处理**：使用 File API 时，视频的存储速率为 1
  帧/秒 (FPS)，音频的处理速率则为 1Kbps（单声道）。
  每秒都会添加时间戳。
  - 为了改进推理，这些速率将来可能会发生变化。
  - 您可以通过[设置自定义帧速率](#custom-frame-rate)来替换 1 FPS 采样率。
- **token 计算**：视频的每一秒都按如下方式计算 token：
  - 各帧（选段率为 1 FPS）：
    - 如果 [`mediaResolution`](https://ai.google.dev/api/generate-content?hl=zh-cn#MediaResolution) 设置
      为低，则每帧按 66 个 token 计算。
    - 否则，每帧按 258 个 token 计算。
  - 音频：每秒 32 个 token。
  - 元数据也包含在内。
  - 总计：默认媒体分辨率下，每秒视频大约需要 300 个 token；低媒体分辨率下，每秒视频大约需要 100 个 token。
- **媒体分辨率**：Gemini 3 引入了使用 `media_resolution` 参数对多模态
  视觉处理进行精细控制的功能。`media_resolution` 参数用于确定**为每个输入图片或视频帧分配的 token 数量上限** 。分辨率越高，模型读取精细文本或识别小细节的能力就越强，但 token 用量和延迟时间也会增加。

  如需详细了解该参数及其对 token
  计算的影响，请参阅[媒体分辨率](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=zh-cn)指南。
- **时间戳格式**：在提示中引用视频中的特定时刻时，请使用 `MM:SS` 格式（例如，`01:15` 表示 1 分 15 秒）。
- **最佳实践**：

  - 为获得最佳效果，每个提示请求仅使用一个视频。
  - 如果将文本与单个视频相结合，请在 `contents` 数组中将文本提示放在视频部分之后 。
  - 请注意，如果选段率为 1 FPS，快速动作序列可能会丢失细节。如有必要，可以考虑放慢此类片段的播放速度。

## 后续步骤

本指南介绍了如何上传视频文件以及如何从视频输入生成文本输出。如需了解详情，请参阅以下资源：

- [系统说明](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn#system-instructions)：
  系统说明可让您根据
  特定需求和使用情形来控制模型的行为。
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn)：详细了解如何上传和管理
  文件以供 Gemini 使用。
- [文件提示策略](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn#prompt-guide)：
  Gemini API 支持使用文本、图片、音频和视频数据进行提示，也
  称为多模态提示。
- [安全指南](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=zh-cn)：有时，生成式
  AI 模型会生成意外输出，例如不准确、
  有偏见或令人反感的输出。后处理和人工评估对于
  限制此类输出造成的危害风险至关重要。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-30。"],[],[]]
