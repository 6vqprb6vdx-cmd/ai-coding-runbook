---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=zh-CN
fetched_at: 2026-09-21T05:53:54.026774+00:00
title: "\u7f51\u5740\u4e0a\u4e0b\u6587 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 网址上下文

借助网址上下文工具，您可以网址的形式向模型提供更多上下文。通过在请求中添加网址，模型将访问这些网页中的内容（只要不是[限制部分](#limitations)中列出的网址类型），以便提供更优质的回答。

网址上下文工具适用于以下任务：

- **提取数据**：从多个网址中提取价格、名称或关键发现等特定信息。
- **比较文档**：分析多份报告、文章或 PDF，以找出差异并跟踪趋势。
- **综合和创建内容**：整合来自多个来源网址的信息，以生成准确的摘要、博文或报告。
- **分析代码和文档**：指向 GitHub 代码库或技术文档，以解释代码、生成设置说明或回答问题。

以下示例展示了如何比较来自不同网站的两份食谱。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## 运作方式

网址上下文工具使用两步检索流程来平衡速度、费用和对最新数据的访问。当您提供网址时，该工具会先尝试从内部索引缓存中提取内容。它充当高度优化的缓存。如果某个网址未编入索引（例如，如果该网址指向的网页是新近发布的），该工具会自动回退到执行实时提取。此工具会直接访问网址，以实时检索其内容。

## 与其他工具结合使用

您可以将网址上下文工具与其他工具结合使用，以创建更强大的工作流。

[Gemini 3 模型](#supported-models)支持将内置工具（例如网址上下文）与自定义工具（函数调用）相结合。如需了解详情，请参阅[工具组合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)页面。

### 依托搜索进行接地

同时启用网址上下文和[依托 Google 搜索进行接地](https://ai.google.dev/gemini-api/docs/grounding?hl=zh-cn)后，模型可以使用其搜索功能在网上查找相关信息，然后使用网址上下文工具更深入地了解找到的网页。对于需要广泛搜索和深入分析特定网页的提示，这种方法非常有效。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## 了解回答

当模型使用网址上下文工具时，其文本回答会在文本内容块中添加内嵌 `url_citation` 注释。每条注释都会将回答文本的某个部分（通过 `start_index` 和 `end_index`）链接到其来源网址。这是在应用中显示引用的主要方式 - 请参阅[上文中的主要示例](#get-started)，了解如何提取引用。

响应中还包含一个 `url_context_result` 步骤，其中包含有关每次网址检索尝试（状态、检索到的网址）的元数据。这主要用于调试。

### 安全检查

系统会对网址执行内容审核检查，以确认其符合安全标准。如果某个网址未通过此检查，相应的 `url_context_result` 步骤将显示 `"unsafe"` 的 `status`。

### Token 计数

从您在提示中指定的网址检索到的内容会作为输入 token 的一部分进行统计。您可以在互动的 `usage` 对象中查看 token 数量。下面给出了一个示例：

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

每个令牌的价格取决于所用模型，详情请参阅[价格](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)页面。

## 支持的模型

| 模型 | 网址上下文 |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-cn) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3 Flash 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-cn) | ✔️ |

## 最佳做法

- **提供具体网址**：为获得最佳结果，请提供您希望模型分析的内容的直接网址。该模型只会从您提供的网址中检索内容，而不会从任何嵌套链接中检索内容。
- **检查可访问性**：验证您提供的网址是否不会指向需要登录或位于付费墙后面的网页。
- **使用完整网址**：提供完整网址，包括协议（例如，https://www.google.com 而不是仅提供 google.com）。

## 限制

- 请求限制：该工具每次请求最多可处理 20 个网址。
- 网址内容大小：从单个网址检索的内容大小上限为 34MB。
- 公开可访问性：网址必须可在网络上公开访问。
  不支持本地主机地址（例如 localhost、127.0.0.1）、专用网络和隧道服务（例如 ngrok、pinggy）。
- 仅限 Gemini API：网址上下文仅在 Gemini API 中可用，无法通过 Gemini Enterprise Agent Platform 使用。

### 支持和不支持的内容类型

该工具可以从具有以下内容类型的网址中提取内容：

- 文本（text/html、application/json、text/plain、text/xml、text/css、text/javascript、text/csv、text/rtf）
- 图片（image/png、image/jpeg、image/bmp、image/webp）
- PDF (application/pdf)

以下内容类型不受支持：

- 付费内容
- YouTube 视频（如需了解如何处理 YouTube 网址，请参阅[视频理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn#youtube)）
- Google Workspace 文件，例如 Google 文档或电子表格
- 视频和音频文件

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-12。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-12。"],[],[]]
