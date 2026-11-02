---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-CN
fetched_at: 2026-11-02T07:09:45.913713+00:00
title: "\u5a92\u4f53\u5206\u8fa8\u7387 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 媒体分辨率

`media_resolution` 形参用于确定为媒体输入分配的 **token 数量上限** ，从而控制 Gemini API 处理图片、视频、音频和 PDF
文档等媒体输入的方式，让您可以在回答质量、延迟时间和费用之间取得平衡。虽然视觉和文档输入会根据分辨率设置来扩缩 token
分配，但音频输入在所有分辨率级别下都以固定的每秒 token 数进行 token 化。如需了解
不同设置的默认值及其对应的 token 数，请参阅
[token 数量](#token-counts)部分。

您可以为请求中的各个媒体对象（内容项）配置媒体分辨率（Gemini 4 和 Gemini 3 模型）。

## 按内容项设置媒体分辨率（Gemini 4 和 Gemini 3 模型）

Gemini 4 和 Gemini 3 模型允许您为请求中的各个媒体对象设置媒体分辨率，从而对 token 使用情况进行精细优化。您可以在单个请求中混合使用不同的分辨率级别。例如，对复杂的图表使用高分辨率，对简单的上下文图片使用低分辨率。

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
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
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
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
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Describe the details in this high-resolution image.").build();
Content imageContent =
    ImageContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/image/scones.jpg")
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

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

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/image.jpg", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe the details in this high-resolution image.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:        genai.Ptr(uploadedFile.URI),
                    MimeType:   interactions.ImageContentMimeType(uploadedFile.MIMEType).ToPointer(),
                    Resolution: interactions.MediaResolutionHigh.ToPointer(),
                }),
            }),
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
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## 可用的分辨率值

Gemini API 为媒体分辨率定义了以下级别：

- `unspecified`：默认设置。此级别的 token 数量在 Gemini 4/3 和更早版本的 Gemini 模型之间差异很大。
- `low`：token 数量较少，处理速度更快，费用更低，但细节较少。
- `medium`：在细节、费用和延迟时间之间取得平衡。
- `high`：token 数量较多，为模型提供了更多细节，但延迟时间和费用也会增加。
- `ultra_high`（仅限按内容项）：token 数量最多，某些使用场景（例如[计算机使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)）需要此级别。

请注意，`high` 可为大多数使用场景提供最佳性能。

为每个级别生成的 token 的确切数量取决于**媒体类型** （图片、视频、音频、PDF）和**模型版本** 。

## token 数量

下表总结了每个模型系列中每个 `media_resolution` 值和媒体类型对应的大致 token 数量。

**Gemini 4 和 Gemini 3 模型**

| MediaResolution | 图片 | 视频 | 音频 | PDF |
| --- | --- | --- | --- | --- |
| `unspecified`（默认） | 1120 | 70 | 25（每秒） | 560 |
| `low` | 280 | 70 | 25（每秒） | 280 + 原生文本 |
| `medium` | 560 | 70 | 25（每秒） | 560 + 原生文本 |
| `high` | 1120 | 280 | 25（每秒） | 1120 + 原生文本 |
| `ultra_high` | 2240 | 不适用 | 不适用 | 不适用 |

## 选择合适的分辨率

- **默认 (`unspecified`)**： 从默认设置开始。它经过调整，可在大多数常见使用场景中实现质量、延迟时间和费用之间的良好平衡。
- **`low`**： 适用于费用和延迟时间至关重要，而精细细节不太重要的场景。
- **`medium` / `high`**： 如果任务需要理解媒体中的复杂细节，请提高分辨率。这通常适用于复杂的视觉分析、图表解读或密集文档理解。
- **`ultra_high`** - 仅适用于按内容项设置。建议用于特定使用场景（例如计算机使用），或测试表明此设置比 `high` 有明显提升时。
- **按内容项控制（Gemini 4 和 Gemini 3）**： 优化 token 使用情况。例如，在包含多张图片的提示中，对复杂的图表使用 `high`，对简单的上下文图片使用 `low` 或 `medium`。

**推荐设置**

以下列出了每种受支持媒体类型的推荐媒体分辨率设置。

| 媒体类型 | 推荐设置 | 最大 token 数 | 使用指南 |
| --- | --- | --- | --- |
| **Google 图片** | `high` | 1120 | 建议用于大多数图片分析任务，以确保获得最高质量。 |
| **PDF** | `medium` | 560 | 最适合文档理解；质量通常在 `medium` 时达到饱和。对于标准文档，将分辨率提高到 `high` 很少能提高 OCR 结果。 |
| **视频** （常规） | `low`（或 `medium`） | 70（每帧） | **注意**： 对于视频，`low` 和 `medium` 设置的处理方式相同（70 个 token），以优化上下文使用。这足以满足大多数动作识别和描述任务的需求。 |
| **视频** （文本密集型） | `high` | 280（每帧） | 仅当使用场景涉及读取密集文本 (OCR) 或视频帧中的小细节时才需要此设置。 |
| **音频** | `unspecified`（默认） | 25（每秒） | 音频在所有受支持的分辨率设置（`unspecified`、`low`、`medium` 和 `high`）下都以固定的每秒 25 个 token 的速率进行 token 化。 |

请务必测试和评估不同分辨率设置对应用的影响，以便在质量、延迟时间和费用之间找到最佳平衡点。

## 与视频处理模式的关系

`media_resolution` 和处理形参控制着视频输入的不同方面：

- `media_resolution` 控制着每个帧的**分辨率** （每个帧的 token 数量）。
- `processing` / `media_processing` 控制着**视频中的哪些内容** 会加载到上下文中。

您可以在同一视频输入中同时设置这两个形参。例如，您可以使用代理处理和低媒体分辨率，以最大限度地减少长视频的总 token 使用量。

如需详细了解视频处理模式，请参阅[代理视频理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn#agentic-video-understanding)指南。

## 版本兼容性摘要

- **Gemini 4 和 Gemini 3 模型支持** 为各个内容项设置 `resolution`。

## 后续步骤

- 如需详细了解 Gemini API 的多模态功能，请参阅
  [图片理解](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-cn)、
  [视频理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn)、[音频理解](https://ai.google.dev/gemini-api/docs/audio?hl=zh-cn)和
  [文档理解](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-cn)指南。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-13。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-13。"],[],[]]
