---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-CN
fetched_at: 2026-09-07T05:38:43.451405+00:00
title: "\u5a92\u4f53\u5206\u8fa8\u7387 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 媒体分辨率

`media_resolution` 参数用于确定为媒体输入内容分配的 **token 数量上限**，从而控制 Gemini API 处理图片、视频和 PDF 文档等媒体输入内容的方式，让您可以在回答质量与延迟时间和费用之间取得平衡。如需了解不同设置、默认值以及它们与令牌的对应关系，请参阅[令牌数量](#token-counts)部分。

您可以在请求中为各个媒体对象（内容项）配置媒体分辨率（仅限 Gemini 3）。

## 按内容项设置的媒体分辨率（仅限 Gemini 3）

Gemini 3 可让您为请求中的各个媒体对象设置媒体分辨率，从而实现精细的令牌用量优化。您可以在单个请求中混合使用不同的分辨率级别。例如，为复杂的图表使用高分辨率，为简单的上下文相关图片使用低分辨率。

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
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

- `unspecified`：默认设置。此级别的 token 数量在 Gemini 3 与更早的 Gemini 模型之间存在显著差异。
- `low`：token 数量较少，因此处理速度更快，费用更低，但细节较少。
- `medium`：在细节、费用和延迟之间取得平衡。
- `high`：token 数量较多，可为模型提供更多细节，但延迟时间和费用也会增加。
- `ultra_high`（仅限每个内容项）：最高令牌数，适用于特定使用场景，例如[计算机使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)。

请注意，`high` 可为大多数使用场景提供最佳性能。

为每个级别生成的 token 的确切数量取决于**媒体类型**（图片、视频、PDF）和**模型版本**。

## token 数量

下表总结了每个模型系列中每个 `media_resolution` 值和媒体类型对应的大致 token 数量。

**Gemini 3 模型**

| MediaResolution | 图片 | 视频 | PDF |
| --- | --- | --- | --- |
| `unspecified`（默认） | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + 原生文字 |
| `medium` | 560 | 70 | 560 + 原生文字 |
| `high` | 1120 | 280 | 1120 + 原生文本 |
| `ultra_high` | 2240 | 不适用 | 不适用 |

## 选择合适的分辨率

- **默认 (`unspecified`)**：从默认设置开始。它经过调整，可在大多数常见应用场景中实现质量、延迟时间和费用之间的良好平衡。
- **`low`**：适用于成本和延迟时间至关重要，而细粒度细节不太重要的场景。
- **`medium` / `high`**：如果任务需要了解媒体中的复杂细节，请提高分辨率。这对于复杂的视觉分析、图表阅读或密集文档理解通常是必需的。
- **`ultra_high`** - 仅适用于按内容项设置。建议用于特定使用场景，例如计算机使用场景，或者测试表明其性能明显优于 `high` 的场景。
- **按内容项控制（Gemini 3）**：优化令牌使用情况。例如，在包含多张图片的提示中，使用 `high` 表示复杂的图表，使用 `low` 或 `medium` 表示简单的上下文图片。

**推荐设置**

下表列出了每种受支持的媒体类型的推荐媒体分辨率设置。

| 媒体类型 | 推荐设置 | 最大token数 | 使用指南 |
| --- | --- | --- | --- |
| **图片** | `high` | 1120 | 建议用于大多数图片分析任务，以确保获得最高质量的结果。 |
| **PDF** | `medium` | 560 | 非常适合文档理解；质量通常在 `medium` 时达到饱和。将该值增加到 `high` 很少能提高标准文档的 OCR 结果。 |
| **视频**（常规） | `low`（或 `medium`） | 70（每帧） | **注意**：对于视频，`low` 和 `medium` 设置的处理方式相同（70 个 token），以优化上下文使用。这对于大多数动作识别和描述任务来说已经足够。 |
| **视频**（文字较多） | `high` | 280（每帧） | 仅当用例涉及读取视频帧中的密集文本 (OCR) 或细微细节时才需要。 |

请务必测试并评估不同分辨率设置对应用的影响，以便在质量、延迟时间和费用之间找到最佳平衡点。

## 版本兼容性摘要

- 为各个内容项设置 `resolution` 仅适用于 **Gemini 3 模型**。

## 后续步骤

- 如需详细了解 Gemini API 的多模态功能，请参阅[图片理解](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-cn)、[视频理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn)和[文档理解](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-cn)指南。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-30。"],[],[]]
