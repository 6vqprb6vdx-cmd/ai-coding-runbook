---
source_url: https://ai.google.dev/gemini-api/docs/omni?hl=zh-CN
fetched_at: 2026-09-07T05:30:22.362838+00:00
title: "\u4f7f\u7528 Gemini Omni Flash \u751f\u6210\u548c\u7f16\u8f91\u89c6\u9891 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 Gemini Omni Flash 生成和编辑视频

Gemini Omni Flash (`gemini-omni-1.1-flash`) 是一款高性能多模态模型，专为高速视频生成、编辑和电影级控制而设计。
Gemini Omni 基于以下核心功能构建，这些功能使其有别于之前的视频模型：

- **原生多模态**： 它可同时处理文本、图片、音频和视频，为您提供更具凝聚力、一致性和可控性的输出。
- **对话式编辑**： 通过 [Interactions
  API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 实现，让您可以通过自然语言对话迭代优化
  和编辑视频。描述您想要更改的内容，模型会在应用编辑的同时保留您想要保留的视频部分。
- **世界知识**： Gemini Omni 将对物理的理解与 Gemini 的历史、科学和文化背景知识相结合，弥合了从照片写实主义到有意义的故事讲述之间的差距。

## 文生视频

根据文本提示生成视频。模型会根据您的文本说明生成带音频的视频。撰写提示时，请添加场景说明、镜头移动、光效和氛围等详细信息，以获得最佳效果。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A marble rolling fast on a chain reaction style track, continuous smooth shot."
)
with open("marble.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A marble rolling fast on a chain reaction style track, continuous smooth shot.',
});

if (interaction.output_video?.data) {
  fs.writeFileSync('marble.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A marble rolling fast on a chain reaction style track, continuous smooth shot."
}'
```

### REST 响应 schema

便捷字段 `interaction.output_video` 仅适用于 **SDK** 。
直接使用 REST API 时，请从 `steps` 数组获取视频输出。

**原始 REST JSON 结构**：

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "AAAAIGZ0eXBpc29t..." // Base64 encoded video data
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-1.1-flash",
  "object": "interaction"
}
```

### 控制宽高比

将 `aspect_ratio` 设置为 `"9:16"` 以创建竖屏视频。默认值为横向 (16:9)。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A futuristic city with neon lights and flying cars, cyberpunk style",
    response_format={
        "type": "video",  # optional
        "aspect_ratio": "9:16"  # Supported values: "9:16", "16:9"
    }
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A futuristic city with neon lights and flying cars, cyberpunk style',
  response_format: {
    type: 'video', // optional
    aspect_ratio: '9:16' // Supported values: '9:16', '16:9'
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A futuristic city with neon lights and flying cars, cyberpunk style",
 "response_format": {
   "type": "video",
   "aspect_ratio": "9:16"
 }
}'
```

### 输出分辨率

使用 `response_format` 中的 `resolution` 参数控制生成的视频的输出分辨率。默认分辨率为 720p。

| 值 | 说明 |
| --- | --- |
| `360p` | 360p 输出分辨率 |
| `720p` | 720p 输出分辨率（默认） |
| `1080p` | 1080p 输出（画质提升） |
| `4k` | 4K 输出（画质提升） |

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A drone shot of a mountain landscape at sunrise.",
    response_format={
        "type": "video",
        "resolution": "1080p",
    },
)
with open("hires.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A drone shot of a mountain landscape at sunrise.',
  response_format: {
    type: 'video',
    resolution: '1080p',
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('hires.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A drone shot of a mountain landscape at sunrise.",
 "response_format": {
   "type": "video",
   "resolution": "1080p"
 }
}'
```

## 图生视频

您可以提供参考图片和文本提示。模型会根据您的提示决定如何使用图片。这对于让产品照片、插图或照片栩栩如生非常有用。

以下示例展示了如何使用鱼从水中跳出的绘画的参考图片：

![一张鱼跃出水面的绘画](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=zh-cn)

使用以下提示：

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

生成绘画的逼真视频。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
)
with open("clownfish.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('clownfish.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$BASE64_IMAGE"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
 ]
}'
```

### 第一帧和最后一帧插值

Gemini Omni Flash 支持视频插值，让您能够生成在起始图片（第一帧）和结束图片（最后一帧）之间平滑过渡的视频。

在 `input` 列表中提供两张图片，并在提示中描述所需的转场效果。模型会将场景从第一帧到最后一帧呈现动画效果。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": first_frame_b64, "mime_type": "image/jpeg"},
        {"type": "image", "data": last_frame_b64, "mime_type": "image/jpeg"},
        {"type": "text", "text": "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky."}
    ],
)
with open("interpolation.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: firstFrameB64, mime_type: 'image/jpeg' },
    { type: 'image', data: lastFrameB64, mime_type: 'image/jpeg' },
    { type: 'text', text: 'A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('interpolation.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$FIRST_FRAME_B64"'", "mime_type": "image/jpeg"},
   {"type": "image", "data": "'"$LAST_FRAME_B64"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky."}
 ]
}'
```

### 正文参考

您可以生成包含作为参考图片提供的特定正文的视频。
例如，以下代码展示了如何提供猫和毛线的 2 张图片，以生成猫玩毛线的视频。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": cat_b64, "mime_type": "image/png"},
        {"type": "image", "data": yarn_b64, "mime_type": "image/png"},
        {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
    ],
)
with open("cat.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: catData, mime_type: 'image/png' },
    { type: 'image', data: yarnData, mime_type: 'image/png' },
    { type: 'text', text: 'A cat playfully batting at a ball of yarn.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('cat.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$CAT_B64"'", "mime_type": "image/png"},
   {"type": "image", "data": "'"$YARN_B64"'", "mime_type": "image/png"},
   {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
 ]
}'
```

### 任务参数

使用 `video_config` 中的 `task` 参数明确指定预期行为，例如，如果您希望模型根据图片生成视频，可以将该参数设置为 `image_to_video`。如果未设置此参数，模型将根据提示推断您的意图。

允许的值如下：

- `text_to_video`
- `image_to_video`
- `reference_to_video`
- `edit`
- `extend`

以下示例展示了如何为之前显示的图生视频示例设置此参数。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
    generation_config={
      "video_config": {
        "task": "image_to_video",
      }
    },
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ],
  generationConfig: {
    videoConfig: {
      task: 'image_to_video',
    }
  }
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-flash",
    "input": [
      {
        "type": "image",
        "data": "'"$BASE64_IMAGE"'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "text",
        "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"
      }
    ],
    "generation_config": {
      "video_config": {
        "task": "image_to_video"
      }
    }
  }'
```

## 有状态视频编辑

生成视频并使用后续提示迭代编辑。每个轮次都基于上一个结果。模型会记住视频上下文，应用您的更改，同时保留您未提及的元素。使用 `previous_interaction_id` 跟踪对话历史记录和生成的视频状态，而无需重新上传之前的视频。

以下示例展示了如何先生成第一个视频，然后对其进行编辑：

### Python

```
import base64
from google import genai

client = genai.Client()

# Turn 1: Generate initial video
res1 = client.interactions.create(model="gemini-omni-1.1-flash", input="A woman playing violin outdoors.")

# Turn 2: Edit the previous video
res2 = client.interactions.create(
    model="gemini-omni-1.1-flash",
    previous_interaction_id=res1.id,
    input="Make the violin invisible."
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(res2.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Turn 1: Generate initial video
const res1 = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A woman playing violin outdoors.',
});

// Turn 2: Edit the previous video
const res2 = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  previous_interaction_id: res1.id,
  input: 'Make the violin invisible.',
});

if (res2.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(res2.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "previous_interaction_id": "'"$PREVIOUS_ID"'",
 "input": "Make the violin invisible."
}'
```

初始视频示例：

编辑后的视频示例：

对话中的每个轮次都会生成一个新视频。模型会理解之前轮次的上下文，让您能够进行增量更改，例如调整光效和更换背景，而无需重新描述整个场景。

### 编辑自己的视频

使用 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn) 上传视频，以便使用 Gemini Omni Flash 对其进行编辑
。

以下示例展示了如何编辑以下原始视频：

### Python

```
import time
import base64
from google import genai

client = genai.Client()

# Upload video using the file API
video_file = client.files.upload(file="Video.mp4")

while video_file.state == "PROCESSING":
    print('Waiting for video to be processed.')
    time.sleep(10)
    video_file = client.files.get(name=video_file.name)

if video_file.state == "FAILED":
  raise ValueError(video_file.state)
print(f'Video processing complete: ' + video_file.uri)

# Edit your video
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "text", "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"}
    ],
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload video using the file API
let videoFile = await ai.files.upload({
  file: 'Video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  console.log('Waiting for video to be processed.');
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

if (videoFile.state === 'FAILED') {
  throw new Error(videoFile.state);
}
console.log('Video processing complete: ' + videoFile.uri);

// Edit your video
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material" }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
#!/bin/bash
VIDEO_B64=$(encode_file "$VIDEO_FILE")

curl -sS -w "\n[HTTP %{http_code}]\n" "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d @- <<EOF > video_editing_response.json
{
  "model": "gemini-omni-1.1-flash",
  "input": [
    {
      "type": "user_input",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "$VIDEO_B64"
        },
        {
          "type": "text",
          "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"
        }
      ]
    }
  ],
  "response_format": { "type": "video" }
}
EOF
```

编辑后的视频示例：

## 使用 URI 检索视频

使用 `delivery="uri"` 参数在
`response_format` 中检索大于 4MB 的生成的视频。
这会返回一个 Google 托管的 URI，您可以轮询该 URI，直到视频变为 `ACTIVE` 状态，然后才能下载。

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Request video via URI delivery
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A beautiful sunset.",
    response_format={"type": "video", "delivery": "uri"}
)

# 2. Extract file name and poll for ACTIVE state
video_output = interaction.output_video
file_name = video_output.uri.split("/")[-1] # Extract ID

print("Waiting for video processing...")
while True:
    f_info = client.files.get(name=f"files/{file_name}")
    if f_info.state.name == "ACTIVE":
        break
    elif f_info.state.name == "FAILED":
        raise RuntimeError("Generation failed.")
    time.sleep(5)

# 3. Download the final video
client.files.download(file=video_output.uri, destination="output.mp4")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

// 1. Request video via URI delivery
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A beautiful sunset.',
  response_format: { type: 'video', delivery: 'uri' },
});

// 2. Extract file name and poll for ACTIVE state
const videoOutput = interaction.output_video;
const fileId = videoOutput.uri.match(/files\/([a-zA-Z0-9]+)/)[1];
const name = `files/${fileId}`;

console.log("Waiting for video processing...");
while (true) {
  const fInfo = await ai.files.get({ name });
  if (fInfo.state.name === 'ACTIVE') break;
  if (fInfo.state.name === 'FAILED') throw new Error("Generation failed.");
  await new Promise(r => setTimeout(r, 5000));
}

// 3. Download the final video
await ai.files.download({
  file: videoOutput,
  downloadPath: 'output.mp4',
});
console.log("💾 Saved video to output.mp4");
```

### REST

```
#!/bin/bash

# 1. Initial request to generate the video
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A beautiful sunset over a calm ocean.",
 "response_format": {"type": "video", "delivery": "uri"}
}')

# Extract FILE_ID from the URI (e.g., "files/abc-123" -> "abc-123")
FILE_URI=$(echo $RESPONSE | jq -r '.output_video.uri')
FILE_ID=$(echo $FILE_URI | cut -d'/' -f2)

echo "Video requested (ID: $FILE_ID). Waiting for processing..."

# 2. Polling loop
while true; do
 # Get current file status
 STATUS_JSON=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID?key=$API_KEY")
 STATE=$(echo $STATUS_JSON | jq -r '.state')

 if [ "$STATE" == "ACTIVE" ]; then
   echo "Processing complete! Downloading..."
   break
 elif [ "$STATE" == "FAILED" ]; then
   echo "Error: Generation failed."
   exit 1
 else
   echo "Current state: $STATE... (waiting 5s)"
   sleep 5
 fi
done

# 3. Final download
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID:download?alt=media&key=$API_KEY" \
--output "output.mp4"

echo "Done! Video saved to output.mp4"
```

**原始 REST JSON 结构 (URI)**：

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "uri": "https://generativelanguage.googleapis.com/v1beta/files/...:download?alt=media"
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-1.1-flash",
  "object": "interaction"
}
```

## 视频延长

通过在视频片段的末尾生成无缝延续内容来延长现有视频。在提示中描述您希望视频如何延续，例如
`"Extend this video"` 或 `"Continue the scene: the camera pans across the mountains"`。
模型会分析输入视频，生成 3-10 秒的延续内容。

您可以延长：

- **模型生成的视频（多轮次）**：通过引用先前生成的
  视频的 `previous_interaction_id` 来延长该视频。
- **上传的视频**：提供上传的视频文件（通过 Files API）以及延长提示。

### Python

```
import base64
from google import genai

client = genai.Client()

# Upload your video using the Files API
video_file = client.files.upload(file="my_video.mp4")

# Extend the video using prompt-based extension
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "text", "text": "Continue the scene."}
    ],
)
with open("extended.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload your video using the Files API
let videoFile = await ai.files.upload({
  file: 'my_video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Extend the video using prompt-based extension
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: 'Continue the scene.' }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('extended.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY"     -H "Content-Type: application/json"     -d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "document", "uri": "'"$VIDEO_URI"'"},
   {"type": "text", "text": "Continue the scene."}
 ]
}'
```

### 使用参考媒体延长

您可以在 `input` 数组中提供参考图片以及提示，以便在延长的视频中引入新的人物或元素：

### Python

```
import base64
from google import genai

client = genai.Client()

# Upload base video and reference image using the Files API
video_file = client.files.upload(file="my_video.mp4")
character_img = client.files.upload(file="character.png")

# Extend the video while introducing the reference character
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "document", "uri": character_img.uri},
        {"type": "text", "text": "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave."}
    ],
)
with open("extended_with_character.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload base video and reference image using the Files API
let videoFile = await ai.files.upload({ file: 'my_video.mp4' });
let characterImg = await ai.files.upload({ file: 'character.png' });

while (videoFile.state === 'PROCESSING' || characterImg.state === 'PROCESSING') {
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
  characterImg = await ai.files.get({ name: characterImg.name });
}

// Extend the video while introducing the reference character
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'document', uri: characterImg.uri },
    { type: 'text', text: 'Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave.' }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('extended_with_character.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY"     -H "Content-Type: application/json"     -d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "document", "uri": "'$VIDEO_URI'"},
   {"type": "document", "uri": "'$CHARACTER_IMG_URI'"},
   {"type": "text", "text": "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave."}
 ]
}'
```

### 延长限制和准则

延长视频时，请注意以下规则和限制：

- **上传的视频中的口语对话**：目前，您无法延长
  上传的视频，在其中添加额外的对话（如果人物保持沉默或提示不添加对话，则支持此操作）。
- **多轮次语音延长**：通过多轮次 (`previous_interaction_id`) 延长先前生成的视频时，支持生成口语对话或语音。
- **仅限视频片段末尾**：延长仅限于附加到视频末尾。
  您无法在视频片段开头添加内容或延长视频片段中间的内容。
- **时长限制**：上传用于延长的输入视频时，时长必须不超过 10 秒
  （除非使用多轮次）。
- **地区可用性**：欧洲经济区 (EEA)、瑞士和英国境内的用户目前无法延长上传的视频
  （所有可用地区都支持延长模型生成的视频）。

## 最佳实践

- **对大型视频使用 URI 传送**： 对于大于 4MB 的视频（>720p 如果可用），请在 `response_format` 中使用 `delivery="uri"`，以避免载荷大小限制。
- **优化性能**： 将 `background=false`、`store=false` 和 `stream=false` 设置为更快、同步的一元生成。请注意，将 `store=false` 设置为表示生成的视频无法在后续轮次中使用 `previous_interaction_id` 进行编辑。
- **提示准确性**： 如需了解
  详情，请参阅[提示指南](#prompt-guide)部分。

## 限制

- 欧洲经济区、瑞士和英国不支持上传和编辑包含未成年人的图片。
- 不支持上传和编辑包含某些可识别人物的图片。
- 欧洲经济区 (EEA)、瑞士和英国境内的用户目前无法编辑或延长上传的视频（支持编辑或延长模型生成的视频）。
- 上传用于编辑和延长的输入视频时，时长必须不超过 10 秒（除非在多轮次中延长模型生成的视频）。
- 视频延长仅限于附加到视频末尾；不支持在视频片段开头添加内容或延长视频片段中间的内容。
- 您无法延长上传的视频，在其中添加额外的对话（人物可以保持沉默，也可以使用 `previous_interaction_id` 进行多轮次延长）。
- 不支持语音编辑。
- API 的当前版本不支持上传音频参考。
- 视频参考最适合用于相似性；视频参考中的任何音频都会被忽略。视频参考最多支持 3 个视频片段，每个视频片段最长 3 秒。
- 不支持跨多个视频进行引用或推理。尝试多视频提示可能会导致模型性能下降或产生意外输出。
- 不支持预配吞吐量。
- 不支持系统说明、温度、`top_p`、停止序列和负面提示（您可以将负面提示放在常规提示中：例如，“不要执行 X”）。
- 不支持使用 YouTube 视频作为媒体来源。

## 技术详情

- 所有生成的视频都包含 SynthID 水印，该水印对观看者不可见，但可以通过编程方式检测以进行来源验证。
- 视频生成时间因时长、分辨率和当前 API 负载而异。时长较长、分辨率较高的视频需要更多时间生成。
- Omni 会对输入提示和生成的视频应用内容安全过滤器（因地区而异）。违反使用政策的提示会被屏蔽。
- 完全支持英语 (EN)，但其他语言尚未经过评估，因此可能有效，但结果可能会有所不同。

## Gemini Omni Flash 提示指南

本部分包含有关如何有效提示 Gemini Omni Flash 的提示和示例。

### 单场景

默认情况下，Omni Flash 会尝试创建包含几个不同镜头的视频。
它会尝试根据提示制作有趣的叙事内容。

如果您需要输出视频包含单个场景，则必须提示：

- 在单个不间断的场景中
- 在一个连续镜头中
- 无场景切换

例如：

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### 移除不需要的元素

如果生成的视频包含您不需要的内容，请添加简单的负面提示以避免这些内容：

- 无对话
- 无装饰
- 无额外音效

### 用于编辑的提示

简单的提示最适合用于视频编辑。过于详细的提示可能会导致意外更改。

以下是更多简单的编辑提示示例：

- 将此视频制作成动漫
- 给此人戴上一顶时尚的帽子
- 将光效更改为更具戏剧性
- 将标志上的文字更改为“Omni Flash”

编辑视频的特定方面时，请添加 `"Keep everything else the same"` 以保持视觉一致性。

以下是一些示例，展示了如何应用此技术：

- **应避免以下做法**： `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **化繁为简**： `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **应避免以下做法**： `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **化繁为简**： `Make the phone invisible. Keep everything else the
    same.`

### 提示音频

默认情况下，模型会尝试为视频生成合适的音轨。这可能并不总是您想要的结果。您可以使用提示来描述所需的音频类型。如果您希望视频中包含音乐，这一点尤其重要：

- 包含平静的背景音乐
- 视频具有高能量的电子节拍
- 音频是背景中播放歌曲的低沉的无线电广播

### 定时事件

您可以提示在视频中的特定时间发生某些事件，无需精确的语法，可以使用自然语言。这对于创建自己的场景切换、节奏或快速序列尤其有用。
请参阅以下示例：

- 3 秒后，一名女子进入场景。
- 在 5 秒时，背景音频中开始播放合唱。
- 每 2 秒切换到新帧。
- 在快速序列中，每半秒（24fps 时为 12 帧）将场景更改为新位置。

您还可以使用时间码语法：

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### 元提示

您可以要求 Gemini Omni Flash 注意视频生成的一般质量或原则：

- 考虑微细节、表情和时间，以创建非常丰富、详细但完全自然的场景。
- 在描述人物和环境时要非常详细。
  对人物应用服装设计原则。明确场景中的人物、物品和对象。
- 在背景元素中添加大量适当的细节，使场景感觉真实自然。
- 制作一个快速视频，每 1 秒显示一个不同的稀有 `[thing]`，播放欢快的音乐，并添加文字来标记该事物。

### 视频中的文字

您可以提示在视频中添加文字，Gemini Omni 会以正确且可读的方式呈现。如果视频中会出现自然出现的文字（即使在背景元素中），定义文字内容也会很有帮助。

- 屏幕上一次显示一个字词：“did, you, know, that, Omni, can, do, awesome, text?” 每个字词以不同的动画样式显示 1 秒。无对话。
- 有一个路标写着：“This is an AI generation by Omni”，有一个店面写着：“All you need AI”，有一辆汽车的车牌号是：“OMNI1.1”

### 用于延长视频的提示

借助 Gemini Omni 1.1 Flash，您可以使用 `"Extend this video"` 或 `"The scene continues"` 等提示延长视频。您可以将视频延长 10 秒，总时长最多为 40 秒。

Omni 会使用原始视频的最后 10 秒作为上下文，创建可保持视频、动作、人物和音频连贯性的延长内容。输入视频中的一些最后一帧将被编辑，以实现无缝过渡。

延长时，本指南中的所有 Omni 提示技巧仍然适用：

- 描述延长场景中的音频，尤其是在需要更改音频时：`"The music continues into the chorus"`
- 描述场景是否延续，或者是否切换到新场景（可能包含相同的人物）：`"Show the same characters in the next scene"`
- 延长时添加图片和视频作为参考，有助于保持输出准确，或引入新的人物：`"The person shown in the reference image enters the scene"`、`"The dog in the reference video <VIDEO_REF_0> jumps onto the sofa"`
- 如果使用时间戳或时间码语法，0 秒是指视频延长部分的开头。如果延长 10 秒的视频，此提示中的场景切换将在 12 秒后发生：`"After 2s cut to a new scene with the same characters"`

### 在提示中使用标记来设置图片和视频角色

您可以使用标记将上传的媒体绑定到特定的生成角色。这样，您就可以指定每张图片或每个视频是起始帧、最终帧还是参考。

#### 1. 简单标记（推荐）

对于媒体角色在提示中明确的简单情况，您可以将图片和视频直接绑定到角色：

- **`<FIRST_FRAME>`**：将图片用作视频的起始帧，例如：
  `<FIRST_FRAME> a woman is walking`
- **`<LAST_FRAME>`**：将图片用作视频的最终帧以进行过渡。必须与 `<FIRST_FRAME>` 搭配使用，例如：`<FIRST_FRAME> <LAST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**：将图片用作参考，例如：`in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking`（结合了第一张图片的样式
  参考和第二张图片的正文参考）。
  图片参考从 0 开始。
- **`<VIDEO_REF_N>`**：将视频用作人物或对象参考，例如：
  `the person in <VIDEO_REF_0> is playing the violin`。视频参考也从 0 开始。

以下是包含 6 张参考图片的示例：

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

#### 2. 声明来源和参考

对于包含多个媒体输入和多个角色的更复杂情况，您可以将显式前缀标记与自然语言说明搭配使用。您应在提示开头声明这些来源和参考。

- `[# Sources <FIRST_FRAME>@Image1]` 会将第一张图片用作起始帧。
- `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image2]` 会将第一张图片用作起始帧，将第二张图片用作最终帧。
- `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image1]` 会将第一张图片同时用作第一帧和最后一帧，从而创建一个循环播放的视频。
- `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]` 会将第一张图片用作起始帧，将第二张图片用作参考。
- `[# Sources <VIDEO_0>@Video1]` 会将视频用作要编辑或修改的主要来源视频。
- `[# Sources <PREVIOUS_VIDEO>@Video1]` 会使用上一个轮次的视频进行延长。
- `[# References <IMAGE_REF_0>@Image1]` 会将第一张图片用作参考。
- `[# References <IMAGE_REF_1>@Image2]` 会将第二张图片用作参考。
- `[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]` 会将两张图片都用作参考。
- `[# References <VIDEO_REF_0>@Video1]` 会将第一个视频用作参考。
- `[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1]` 会将图片和视频都用作参考。

在提示末尾添加指导说明：

- 对于起始帧：`"Use this image as the starting frame."`
- 对于通过起始帧和结束帧循环播放的视频：`"Use this image as the first frame and the last frame."`
- 对于参考图片：`"Use the given image(s) as references for video generation. The images should not be used as literal initial frames."`
- 对于参考视频：`"Use the given video(s) as references. Do not use them as a source for video editing."`

以下是一些包含来源和参考声明的提示示例：

**起始帧与参考图片相结合**：

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2] a woman <IMAGE_REF_0> is walking. Use Image1 as the starting frame. Use Image2 as a reference for the video generation.
```

**人物参考视频与对象参考图片相结合**：

```
[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1] The woman in <VIDEO_REF_0> is playing the violin shown in <IMAGE_REF_0>. Use Video1 as a character reference and Image1 as an object reference.
```

## 后续步骤

- 在 [Omni 快速入门 Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=zh-cn) 中进行实验，开始使用 Gemini Omni Flash。
- 通过我们的[提示设计简介](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=zh-cn)，了解如何撰写更好的提示。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-08-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-08-30。"],[],[]]
