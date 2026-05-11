---
source_url: https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=zh-CN
fetched_at: 2026-05-11T12:31:36.839175+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 图片理解

Gemini 模型从一开始就具有多模态特性，可执行各种图像处理和计算机视觉任务，包括但不限于图片说明、分类和视觉问答，而无需训练专门的机器学习模型。

除了通用的多模态功能外，Gemini 模型还通过额外的训练，针对特定应用场景（例如[对象检测](#object-detection)和[细分](#segmentation)）提供**更高的准确性**。

## 向 Gemini 传递图片

您可以使用多种方法将图片作为输入内容提供给 Gemini：

- [使用网址传递图片](#url-image)：非常适合可公开访问的图片。
- [传递内嵌图片数据](#inline-image)：用于传递 base64 编码的图片数据。
- [使用 File API 上传图片](#upload-image)：建议用于较大的文件或在多个请求中重复使用图片。

### 使用网址传递图片

您可以使用 [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=zh-cn) 上传图片，并在请求中传递该图片：

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const uploadedFile = await client.files.upload({
    file: "path/to/organ.jpg",
    config: { mime_type: "image/jpeg" }
});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### 传递内嵌图片数据

您可以以 base64 编码的字符串形式提供图片数据：

### Python

```
import base64
from google import genai

with open('path/to/small-sample.jpg', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("path/to/small-sample.jpg", {
  encoding: "base64",
});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            data: base64ImageFile,
            mime_type: "image/jpeg"
        }
    ]
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
IMG_PATH="/path/to/your/image1.jpg"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### 使用 File API 上传图片

对于大型文件，或者为了能够重复使用同一图片文件，请使用 Files API。请参阅 [Files API 指南](https://ai.google.dev/gemini-api/docs/interactions/files?hl=zh-cn)。

### Python

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": my_file.uri,
            "mime_type": my_file.mime_type
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const myfile = await client.files.upload({
    file: "path/to/sample.jpg",
    config: { mimeType: "image/jpeg" },
});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: myfile.uri,
            mime_type: myfile.mimeType
        }
    ]
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
# First upload the file (see Files API guide for details)
# Then use the file URI in the request:

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## 使用多张图片进行提示

您可以在单个提示中提供多张图片，只需在 `input` 数组中添加多个图片对象即可：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "What is different between these two images?"},
        {
            "type": "image",
            "uri": "https://example.com/image1.jpg",
            "mime_type": "image/jpeg"
        },
        {
            "type": "image",
            "uri": "https://example.com/image2.jpg",
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
        {type: "text", text: "What is different between these two images?"},
        {
            type: "image",
            uri: "https://example.com/image1.jpg",
            mime_type: "image/jpeg"
        },
        {
            type: "image",
            uri: "https://example.com/image2.jpg",
            mime_type: "image/jpeg"
        }
    ]
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "What is different between these two images?"},
      {
        "type": "image",
        "uri": "https://example.com/image1.jpg",
        "mime_type": "image/jpeg"
      },
      {
        "type": "image",
        "uri": "https://example.com/image2.jpg",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## 对象检测

模型经过训练，可检测图片中的对象并获取其边界框坐标。相对于图片尺寸的坐标会缩放到 [0, 1000]。您需要根据原始图片大小对这些坐标进行反缩放。

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    }
)

bounding_boxes = BoundingBoxes.model_validate_json(interaction.steps[-1].content[0].text)
print(bounding_boxes)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.";

const boundingBoxesJsonSchema = {
  type: "object",
  properties: {
    boxes: {
      type: "array",
      items: {
        type: "object",
        properties: {
          box_2d: { type: "array", items: { type: "integer" }, description: "The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000." },
          mask: { type: "array", items: { type: "array", items: { type: "integer" } }, description: "The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000." },
          label: { type: "string", description: "A descriptive label for the item." }
        },
        required: ["box_2d", "mask", "label"]
      }
    }
  },
  required: ["boxes"]
};

const boundingBoxesSchema = z.fromJSONSchema(boundingBoxesJsonSchema);

const interaction = await client.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: boundingBoxesJsonSchema
  },
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    }
  }'
```

如需查看更多示例，请参阅 [Gemini 实战宝典](https://github.com/google-gemini/cookbook)中的以下笔记本：

## 细分

从 Gemini 2.5 开始，模型不仅可以检测项目，还可以对项目进行分割并提供其轮廓遮罩。

模型会预测一个 JSON 列表，其中每个项都表示一个分割掩码。每个商品都有一个边界框 (“`box_2d`”)，格式为 `[y0, x0, y1, x1]`，其中包含介于 0 到 1000 之间的归一化坐标；一个用于标识对象的标签 (“`label`”)；最后是边界框内的分割掩码，以 base64 编码的 PNG 格式表示，是一个介于 0 到 255 之间的概率图。

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()

prompt = """
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
"""

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    },
    generation_config={
        "thinking_level": "minimal"  # Minimize thinking for better detection results
    }
)

items = BoundingBoxes.model_validate_json(interaction.steps[-1].content[0].text)
print("Segmentation results:", items)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = `
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
`;

const boundingBoxesJsonSchema = {
  type: "object",
  properties: {
    boxes: {
      type: "array",
      items: {
        type: "object",
        properties: {
          box_2d: { type: "array", items: { type: "integer" }, description: "The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000." },
          mask: { type: "array", items: { type: "array", items: { type: "integer" } }, description: "The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000." },
          label: { type: "string", description: "A descriptive label for the item." }
        },
        required: ["box_2d", "mask", "label"]
      }
    }
  },
  required: ["boxes"]
};

const boundingBoxesSchema = z.fromJSONSchema(boundingBoxesJsonSchema);

const interaction = await client.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: boundingBoxesJsonSchema
  },
  generationConfig: {
    thinking_level: "minimal"
  }
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "Give the segmentation masks for the wooden and glass items.\nOutput a JSON list of segmentation masks where each entry contains the 2D\nbounding box in the key \"box_2d\", the segmentation mask in key \"mask\", and\nthe text label in the key \"label\". Use descriptive labels."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    },
    "config": {
      "thinking_level": "minimal"
    }
  }'
```

![一张摆放着纸杯蛋糕的桌子，其中木质和玻璃物体被突出显示](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=zh-cn)

包含对象和分割掩码的分割输出示例

## 支持的图片格式

Gemini 支持以下图片格式 MIME 类型：

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

如需了解其他文件输入方法，请参阅[文件输入方法](https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=zh-cn)指南。

## 功能

所有 Gemini 模型版本都是多模态模型，可用于各种图像处理和计算机视觉任务，包括但不限于图片说明、视觉问答、图片分类、对象检测和分割。

Gemini 可以减少对专用机器学习模型的需求，具体取决于您的质量和性能要求。

最新版本的模型经过专门训练，除了通用功能外，还可提高专业化任务的准确率，例如增强的[对象检测](#object-detection)和[细分](#segmentation)。

## 限制和关键技术信息

### 文件数量限制

Gemini 模型支持每个请求最多上传 3,600 个图片文件。

### token 计算

- 如果两个维度均小于或等于 384 像素，则为 258 个 token。
  较大的图片会被分块为 768x768 像素的图块，每个图块需花费 258 个 token。

计算图块数量的粗略公式如下：

- 计算裁剪单元大小（大致为：`floor(min(width, height)` / 1.5）。
- 将每个维度除以裁剪单元大小，然后将结果相乘，即可得到图块数量。

例如，对于尺寸为 960x540 的图片，剪裁单元尺寸为 360。将每个维度除以 360，得到的图块数量为 3 \* 2 = 6。

### 媒体分辨率

Gemini 3 引入了 `media_resolution` 参数，可对多模态视觉处理进行精细控制。`media_resolution` 参数用于确定**为每个输入图片或视频帧分配的 token 数量上限**。分辨率越高，模型读取细小文字或识别细微细节的能力就越强，但 token 用量和延迟时间也会增加。

## 技巧和最佳做法

- 验证图片是否已正确旋转。
- 使用清晰且不模糊的图片。
- 如果使用包含文本的单张图片，请在 `input` 数组中将文本提示放在图片之前。

## 后续步骤

本指南将介绍如何上传图片文件并根据图片输入生成文本输出。如需了解详情，请参阅以下资源：

- [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=zh-cn)：详细了解如何上传和管理文件以供 Gemini 使用。
- [系统指令](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=zh-cn#system-instructions)：系统指令可让您根据自己的特定需求和使用情形来控制模型的行为。
- [文件提示策略](https://ai.google.dev/gemini-api/docs/interactions/files?hl=zh-cn#prompt-guide)：Gemini API 支持使用文本、图片、音频和视频数据进行提示，也称为多模态提示。
- [安全指南](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=zh-cn)：有时，生成式 AI 模型会生成意料之外的输出，例如不准确、有偏见或令人反感的输出。后处理和人工评估对于限制此类输出造成的危害风险至关重要。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-09。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-09。"],[],[]]
