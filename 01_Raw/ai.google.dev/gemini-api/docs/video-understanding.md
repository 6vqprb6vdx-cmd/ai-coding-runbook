---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-CN
fetched_at: 2026-10-26T05:40:10.074987+00:00
title: "\u89c6\u9891\u7406\u89e3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 视频理解

> 如需了解视频生成，请参阅 [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=zh-cn) 指南。

Gemini 模型可以处理视频，从而实现许多前沿开发者用例，而这些用例在过去需要使用特定于领域的模型。
Gemini 的一些视觉功能包括：能够描述视频、对视频进行分段和提取视频中的信息、回答有关视频内容的问题，以及引用视频中的特定时间戳。

您可以通过以下方式向 Gemini 提供视频作为输入：

| 输入法 | 最大大小 | 推荐的使用场景 |
| --- | --- | --- |
| [File API](#upload-video) | 20GB（付费）/2GB（免费） | 大文件（100MB+）、长视频（10 分钟以上）、可重复使用的文件。 |
| [Cloud Storage 注册](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-cn#registration) | 2GB（每个文件，无存储空间限制） | 大文件（100MB+）、长视频（10 分钟以上）、持久性文件、可重复使用的文件。 |
| [内嵌数据](#inline-video) | < 100MB | 小文件（<100MB）、时长较短（<1 分钟）、一次性输入。 |
| [YouTube 网址](#youtube) | 不适用 | 公开 YouTube 视频。 |

> **注意** ：对于大多数使用场景，尤其是对于大于 100MB 的文件或您想在多个请求中重复使用文件时，建议使用 [File API](#upload-video)。

如需了解其他文件输入方法（例如使用外部网址或存储在 Google Cloud 中的文件），请参阅
[文件输入方法](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-cn)指南。

### 上传视频文件

以下代码会下载示例视频，使用 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn) 上传该视频，
等待其处理完毕，然后使用上传的文件引用来
总结视频。

### Python

```
from google import genai
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.FileState;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File myfile =
    client.files.upload(
        "path/to/sample.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());

while (!myfile.state().isPresent()
    || myfile.state().get().knownEnum() != FileState.Known.ACTIVE) {
  System.out.println("Processing video...");
  Thread.sleep(5000);
  myfile = client.files.get(myfile.name().get(), null);
}

Content videoContent =
    VideoContent.builder()
        .uri(myfile.uri().get())
        .mimeType(VideoContentMimeType.of(myfile.mimeType().get()))
        .build();
Content textContent =
    TextContent.builder()
        .text(
            "Summarize this video. Then create a quiz with an answer key based on the information in this video.")
        .build();

List<Content> contents = Arrays.asList(videoContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
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
    "time"

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

    myfile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", &genai.UploadFileConfig{
        MIMEType: "video/mp4",
    })
    if err != nil {
        log.Fatal(err)
    }

    for myfile.State != genai.FileStateActive {
        fmt.Println("Processing video...")
        time.Sleep(5 * time.Second)
        myfile, err = client.Files.Get(ctx, myfile.Name, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI:      genai.Ptr(myfile.URI),
            MimeType: interactions.VideoContentMimeType(myfile.MIMEType).ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
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
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

如需优化 token 效率和性能，请考虑使用
[智能体视频处理](#agentic-video-understanding)。

当总请求大小（包括文件、文本提示、系统说明等）大于 20 MB、视频时长较长，或者您打算在多个提示中使用同一视频时，请务必使用 Files API。
File API 直接接受视频文件格式。

如需详细了解如何使用媒体文件，请参阅
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn)。

### 以内嵌方式传递视频数据

您可以直接在请求中传递较小的视频，而无需使用 File API 上传视频文件。此方法适用于总请求大小不超过 20 MB 的较短视频。

以下是提供内嵌视频数据的示例：

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

String videoFileName = "/path/to/your/video.mp4";
byte[] videoBytes = Files.readAllBytes(Paths.get(videoFileName));
String base64Video = Base64.getEncoder().encodeToString(videoBytes);

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .data(base64Video)
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
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
    "encoding/base64"
    "fmt"
    "log"
    "os"

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

    videoFileName := "/path/to/your/video.mp4"
    videoBytes, err := os.ReadFile(videoFileName)
    if err != nil {
        log.Fatal(err)
    }
    base64Video := base64.StdEncoding.EncodeToString(videoBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            Data:     genai.Ptr(base64Video),
            MimeType: interactions.VideoContentMimeTypeVideoMp4.ToPointer(),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
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
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### 传递 YouTube 网址

您可以将 YouTube 网址直接传递给 Gemini API，作为请求的一部分，如下所示：

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .uri("https://www.youtube.com/watch?v=9hE5-98ZeCg")
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
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

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            URI: genai.Ptr("https://www.youtube.com/watch?v=9hE5-98ZeCg"),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
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
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**限制** ：

- 对于免费层级，您每天上传的 YouTube 视频时长不得超过 8 小时。
- 对于付费层级，没有基于视频时长的限制。
- 对于 Gemini 2.5 之前的模型，您每次请求只能上传 1 个视频。对于 Gemini 2.5 及更高版本的模型，您每次请求最多能上传 10 个视频。
- 您只能上传公开视频（不能上传私享视频或未公开列出的视频）。

## 智能体视频理解

默认情况下，视频输入在所有模型（包括 Gemini 4）中都使用静态处理（以 1 FPS 的速率提取帧）。Gemini 4 Argon、3.8 Flash、3.6 Flash 和 3.5 Flash Lite 模型还支持
**智能体视频理解**，这是一种选择启用模式，在该模式下，模型会动态探索视频
时间轴，有选择地检查脚本，并根据提示即时自适应地调整帧
速率和分辨率。

| **Mode** | **说明** | **支持的模型** |
| --- | --- | --- |
| **静态** （默认） | 以固定速率（1 帧/秒）提取帧，并将其一次性放入上下文中。所有 Gemini 模型（包括 Gemini 4）的默认设置。 | 所有 Gemini 模型 |
| **智能体** | 模型会动态浏览视频时间轴，仅加载根据提示所需的内容。在长篇内容上，token 效率最多可提高 88%，质量可提高约 7%。 | Gemini 4 Argon、3.8 Flash、3.6 Flash、3.5 Flash Lite |

### 选择处理模式

选择与您的视频时长和查询类型相匹配的处理模式：

- **静态（默认）** ：最适合短片（5 分钟以内）、需要对整个录制内容进行总结的广泛的全视频摘要、对延迟时间敏感的查询，或需要在整个剪辑中实现帧级精度。对于需要检查视频大部分内容的短视频或广泛提示，静态处理可避免时间轴导航产生的额外思考 token (`total_thought_tokens`) 和工具调用往返 (`total_tool_use_tokens`)。
- **智能体** ：最适合长视频（5-10 分钟以上）、大海捞针式检索，或针对特定时刻或主题的查询。模型会先检查脚本，然后仅按需加载相关的视觉片段，从而将视频输入 token 用量减少多达 88%，而无需填充上下文窗口。

> **注意**：对于智能体处理需要更多时间的长视频或复杂提示，请使用流式传输 (`stream=True`) 或[后台执行](https://ai.google.dev/gemini-api/docs/background-execution?hl=zh-cn) (`background=True`)。这样可以保持连接处于有效状态，显示中间推理步骤，并避免连接或身份验证超时。

### 设置处理模式

如需使用智能体视频理解，请在视频
部分的 `input` 数组中设置 `"processing": "agentic"`。

对于长视频，智能体视频处理可能需要更长时间，因为模型会执行多次检查传递以浏览时间轴。为避免网络连接中断时丢失进度，此示例使用 `background=True` 在服务器上异步运行任务。
您也可以省略 `background` 参数，在不进行后台执行的情况下同步运行请求，这非常适合较短的视频。

如需详细了解轮询、检索结果和管理后台任务，请参阅
[后台执行](https://ai.google.dev/gemini-api/docs/background-execution?hl=zh-cn)指南。

### Python

```
import time
from google import genai

client = genai.Client()

# Upload a long video
video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

# Use agentic processing with background execution
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": "agentic"
        },
        {"type": "text", "text": "What are the three main arguments presented?"}
    ],
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(interaction.id)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Upload a long video
let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" }
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Use agentic processing with background execution
let interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: "agentic"
    },
    { type: "text", text: "What are the three main arguments presented?" }
  ],
  background: true,
});

while (interaction.status === "in_progress") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await ai.interactions.get(interaction.id);
}

console.log(interaction.output_text);
```

### REST

```
# 1. Start the interaction in the background
interaction=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {"type": "text", "text": "What are the three main arguments presented?"}
    ],
    "background": true
  }')

id=$(echo "$interaction" | jq -r '.id')

# 2. Poll until the interaction finishes
while [ "$(echo "$interaction" | jq -r '.status')" = "in_progress" ]; do
  sleep 5
  interaction=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$id" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
done

echo "$interaction" | jq '.'
```

> **注意** ：如需验证是否使用了智能体处理，请检查 `interaction.steps`。如果存在 `processing_call` 和 `processing_result`，则表示模型动态浏览了视频。

### 响应步骤

智能体处理会向 `steps` 数组添加两种新的步骤类型：

- `processing_call`：模型请求了视频片段或音频脚本，由 `id` 标识。
- `processing_result`：该加载的结果，由 `call_id` 链接。

这些步骤会与 `thought` 步骤（启用摘要时）交错出现，并位于最终 `model_output` 步骤之前。它们可用于在界面中显示进度跟踪，但不需要响应。

以下示例展示了包含交错处理步骤的响应载荷：

```
{
  "steps": [
    {
      "type": "thought",
      "signature": "sig_thought_1",
      "summary": [
        {
          "type": "text",
          "text": "Inspecting transcript for key discussion topics..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_01",
      "signature": "sig_call_01"
    },
    {
      "type": "processing_result",
      "call_id": "call_01",
      "signature": "sig_result_01"
    },
    {
      "type": "thought",
      "signature": "sig_thought_2",
      "summary": [
        {
          "type": "text",
          "text": "Loading visual frames to verify slide content..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_02",
      "signature": "sig_call_02"
    },
    {
      "type": "processing_result",
      "call_id": "call_02",
      "signature": "sig_result_02"
    },
    {
      "type": "thought",
      "signature": "sig_thought_3",
      "summary": [
        {
          "type": "text",
          "text": "Synthesizing answer from gathered evidence..."
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The three main arguments presented in the lecture are..."
        }
      ]
    }
  ]
}
```

### 在不同视频之间混合处理模式

为同一请求中的每个视频设置不同的处理模式：

### Python

```
import time
from google import genai

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

# Use agentic processing with background execution
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": lecture.uri,
            "mime_type": lecture.mime_type,
            "processing": "agentic"  # Use agentic video understanding
        },
        {
            "type": "video",
            "uri": experiment.uri,
            "mime_type": experiment.mime_type,
            "processing": "static"  # Use static processing
        },
        {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ],
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(interaction.id)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" }
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" }
});

// Use agentic processing with background execution
let interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: lecture.uri,
      mime_type: lecture.mimeType,
      processing: "agentic" // Use agentic video understanding
    },
    {
      type: "video",
      uri: experiment.uri,
      mime_type: experiment.mimeType,
      processing: "static" // Use static processing
    },
    { type: "text", text: "Compare the lecture content with the experiment results." }
  ],
  background: true,
});

while (interaction.status === "in_progress") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await ai.interactions.get(interaction.id);
}

console.log(interaction.output_text);
```

### REST

```
# 1. Start the interaction in the background
interaction=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${lecture_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {
        "type": "video",
        "uri": "'${experiment_uri}'",
        "mime_type": "video/mp4",
        "processing": "static"
      },
      {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ],
    "background": true
  }')

id=$(echo "$interaction" | jq -r '.id')

# 2. Poll until the interaction finishes
while [ "$(echo "$interaction" | jq -r '.status')" = "in_progress" ]; do
  sleep 5
  interaction=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$id" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
done

echo "$interaction" | jq '.'
```

### 多轮视频对话

在对话中，视频上下文会在轮次之间保留。使用智能体处理时：

- **有状态模式** （使用 `previous_interaction_id`）：服务器会保留视频上下文。无需进行额外处理。
- **无状态模式** （使用 `step_list`）：在无状态模式下，响应包含对视频上下文进行编码的 `processing_call` 和 `processing_result` 步骤。您必须在下一个请求的 `step_list` 中包含响应中的所有步骤，以保留视频上下文。虽然省略这些步骤目前不会返回 API 错误，但视频上下文会丢失，从而显著降低后续问题的回答质量。请注意，在后续请求中发送的返回步骤会增加输入 token 计数。

## 引用内容中的时间戳

您可以使用 `MM:SS` 格式的时间戳，针对视频中的特定时间点提出问题。

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Java

```
String prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
prompt := "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## 从视频中提取详细的数据洞见

Gemini 模型通过处理**音频和视觉** 流中的信息，提供强大的视频内容理解功能。这样，您就可以提取丰富的信息，包括生成视频中发生情况的描述，以及回答有关视频内容的问题。

对于视觉描述，模型会以 **1 帧/秒** (FPS) 的速率对视频进行采样。此默认采样率适用于大多数内容，但请注意，它可能会遗漏快速移动或场景快速变化的视频中的细节。

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Java

```
String prompt =
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
prompt := "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## 自定义视频处理

您可以在 Gemini API 中通过设置剪辑间隔或提供自定义帧速率采样来自定义视频处理。这些自定义选项
仅在 `"static"` 模式下处理视频时受支持。

### 设置剪辑间隔

您可以通过在 `processing` 配置对象中指定 `start_offset` 和 `end_offset` 来剪辑视频。

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "start_offset": 1200,
                "end_offset": 1500,
            },
        },
        {"type": "text", "text": "Summarize this section of the video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        start_offset: 1200,
        end_offset: 1500,
      },
    },
    { type: "text", text: "Summarize this section of the video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "start_offset": 1200,
          "end_offset": 1500
        }
      },
      {"type": "text", "text": "Summarize this section of the video."}
    ]
  }' 2> /dev/null
```

### 设置自定义帧速率

您可以通过在 `processing` 配置对象中传递 `fps` 实参来设置自定义帧速率采样。

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "fps": 0.5,  # Sample 1 frame every 2 seconds
            },
        },
        {"type": "text", "text": "Describe the scene changes in this video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        fps: 0.5, // Sample 1 frame every 2 seconds
      },
    },
    { type: "text", text: "Describe the scene changes in this video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "fps": 0.5
        }
      },
      {"type": "text", "text": "Describe the scene changes in this video."}
    ]
  }' 2> /dev/null
```

## 支持的视频格式

Gemini 支持以下视频格式 MIME 类型：

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## 有关视频技术方面的详细信息

- **支持的模型和上下文**：所有 Gemini 模型都可以处理视频数据。
  - 上下文窗口为 100 万个 token 的模型默认可以处理时长不超过 3 小时（低媒体分辨率）或 1 小时（高媒体分辨率）的视频。
- **处理模式**：Gemini 4 Argon、3.8 Flash、3.6 Flash、3.5 Flash Lite、
  及更高版本的模型支持两种视频处理模式：
  - **静态**：以 1 帧/秒的速率提取帧并将其放入上下文中（所有模型的默认设置
    ）。音频的处理速率为 1Kbps（单声道）。
    每秒都会添加时间戳。最适合短片或每个帧都很重要的情况（例如逐帧检查）。请注意，如果采样率为 1 FPS，快速动作序列可能会丢失细节。
  - **智能体**：模型会动态浏览视频，并按需加载
    脚本和/或帧和/或音频。对于长篇内容，此模式使用的 token 最多可减少 88%，但由于内部推理和工具往返，对于短片（<5 分钟）或广泛查询，浏览可能会增加首次 token 响应时间 (TTFT) 和总 token 用量。最适合长视频和定向查询，以优化 token 费用和回答质量。Gemini 4 Argon、3.8 Flash、3.6 Flash 和 3.5 Flash Lite 支持此模式。
    如需了解详情，请参阅[智能体视频理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn#agentic-video-understanding)。
- **token 计算（静态模式）**：视频的每一秒都按如下方式计算 token：
  - 各帧（采样率为 1 FPS）：
    - 如果 `media_resolution` 设置为低，则每帧按 66 个 token 计算。
    - 否则，每帧按 258 个 token 计算。
  - 音频：每秒 32 个 token。
  - 元数据也包含在内。
  - 总计：默认（低）媒体分辨率下，每秒视频大约需要 100 个 token；高媒体分辨率下，每秒视频大约需要 300 个 token。
- **token 计算（智能体模式）**：token 用量因内容
  复杂性和模型的浏览策略而异。在视频探索期间生成的浏览推理 token
  计为**思考 token**
  (`total_thought_tokens`)，而按需加载的帧、音频和脚本计为工具使用 token (`total_tool_use_tokens`)。
  对于长篇内容，智能体处理通常使用的总 token 比静态
  处理少 88%，因为模型仅加载回答提示所需的脚本
  和/或帧和/或音频（请参阅
  [token 指南](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn#video-token-usage)）。
- **媒体分辨率**：Gemini 3 引入了使用 `media_resolution` 参数对多模态
  视觉处理进行精细控制的功能。`media_resolution` 参数用于确定**为每个输入图片或视频帧分配的 token 数量上限** 。分辨率越高，模型读取精细文本或识别小细节的能力就越强，但 token 用量和延迟时间也会增加。`media_resolution` 和 `processing` 参数是独立的：您可以在同一视频输入中同时设置这两个参数。

如需详细了解 token 计算，请参阅
[token](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn) 指南。

- **时间戳格式**：在提示中引用视频中的特定时刻时，请使用 `MM:SS` 格式（例如，`01:15` 表示 1 分 15 秒）。
- **提示位置**：如果将文本与单个视频相结合，请在 `input` 数组中将文本提示放在视频部分
  *之后*。
- **长时间请求的超时**：对于需要较长
  处理时间或复杂的多步推理的视频，请使用流式传输
  （`stream=True`）或[后台执行](https://ai.google.dev/gemini-api/docs/background-execution?hl=zh-cn)
  （`background=True`）。
  在高需求下遇到后端重试的同步非流式请求可能会超出连接或身份验证令牌有效期窗口，
  这可能会显示为意外的`401 Unauthorized`或超时错误。流式传输可保持连接处于有效状态，并显示中间推理和工具调用进度。

## 后续步骤

- [媒体分辨率](https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-cn)：控制视频帧的
  分辨率，以平衡质量和 token 用量。
- [token](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn)：了解在静态和智能体处理模式下如何对视频内容进行 token 化
  。
- [后台执行](https://ai.google.dev/gemini-api/docs/background-execution?hl=zh-cn)：异步运行
  长时间运行的视频理解任务，以避免连接
  超时。
- [系统说明](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn#system-instructions)：
  系统说明可让您根据其
  特定需求和使用情形来控制模型的行为。
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn)：详细了解如何上传和管理
  文件以供 Gemini 使用。
- [文件提示策略](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn#prompt-guide)：Gemini
  API 支持使用文本、图片、音频和视频数据进行提示，也称为
  多模态提示。
- [安全指南](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=zh-cn)：有时，生成式 AI
  模型会生成意外的输出，例如不准确、
  有偏见或令人反感的输出。后处理和人工评估对于限制此类输出造成的危害风险至关重要。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-13。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-13。"],[],[]]
