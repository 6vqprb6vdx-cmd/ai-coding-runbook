---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=zh-CN
fetched_at: 2026-07-27T04:46:08.426033+00:00
title: "Gemini \u601d\u8003 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini 思考

[Gemini 3 和 2.5 系列模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)采用“思考过程”，可显著提升推理和多步规划能力，因此非常适合处理编码、高等数学和数据分析等复杂任务。

当您使用思考模型时，Gemini 会在回答之前进行内部推理。Interactions API 通过 `thought` 步骤（按时间顺序显示在 `steps` 数组中的专用步骤）呈现这种推理过程。

每个思考步骤都包含两个字段：

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `signature` | ✅ 是 | 模型内部推理状态的加密表示形式。始终存在，即使模型执行的推理最少也是如此。 |
| `summary` | ❌ 否 | 总结推理过程的内容（文本和/或图片）数组。可能会为空，具体取决于 [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=zh-cn) 配置、模型是否进行了充分的推理，或者内容类型（例如，图片潜在空间可能没有文本摘要）。 |

## 与思考的互动

与思维模型互动与任何其他互动请求类似。在 `model` 字段中指定[支持思考的模型](#thinking-levels)之一：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## 思考摘要

思考总结可提供对模型内部推理过程的洞见。
默认情况下，仅返回最终输出。您可以使用 `thinking_summaries` 启用思路总结：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

在以下情况下，思想块可能**仅包含签名，而不包含摘要**：

- 简单请求，模型推理不足，无法生成摘要
- `thinking_summaries: "none"`，其中明确停用了摘要
- 某些类型的想法内容（例如图片）可能没有文字摘要

您的代码应始终处理 `summary` 为空或缺失的思路块。

## 包含思考的流式传输

使用流式传输在生成期间接收增量思维摘要。
系统会使用服务器发送的事件 (SSE) 传送思路块，其中包含两种不同的增量类型：

| 增量类型 | 包含 | 发送时间 |
| --- | --- | --- |
| `thought_summary` | 文字或图片摘要内容 | 一个或多个增量（带有增量摘要） |
| `thought_signature` | 加密签名 | `step.stop` 之前的最后一个增量 |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

流式回答使用服务器发送的事件 (SSE)，由步骤和事件组成，例如：

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.5-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## 控制性思维

Gemini 模型默认采用动态思维，会根据请求的复杂程度自动调整推理力度。您可以使用 `thinking_level` 参数控制此行为。

| 模型 | 默认思维 | 支持的级别 |
| --- | --- | --- |
| gemini-3.1-pro-preview | 开启（高） | 低、中、高 |
| gemini-3.1-flash-lite-image | 开启（极简） | 极简、高 |
| gemini-3-flash-preview | 开启（高） | 极低、低、中、高 |
| gemini-3-pro-preview | 开启（高） | 低、高 |
| gemini-3.5-flash | 开启（中） | 极低、低、中、高 |
| gemini-2.5-pro | 开启 | 低、中、高 |
| gemini-2.5-flash | 开启 | 低、中、高 |
| gemini-2.5-flash-lite | 关闭 | 低、中、高 |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## 思维签名

思考特征是模型内部推理的加密表示形式。它们需要在多轮对话中保持推理的连续性。

与 `generateContent` API 相比，Interactions API 可让处理意念签名变得更加简单。

### 有状态模式（推荐）

默认情况下，当您在有状态模式下使用 Interactions API（通过设置 `store: true` 并在后续轮次中传递 `previous_interaction_id`）时，服务器会自动管理对话状态，包括所有思考块和签名。在此模式下，您无需针对签名执行任何操作。它们完全在服务器端处理。

### 无状态模式

如果您自行管理对话状态（无状态模式），并在每次请求中传递完整的输入和输出历史记录，请执行以下操作：

- 您**必须**始终完全按照从模型收到的方式重新发送所有 `thought` 代码块。
- 您**不应**从历史记录中移除或修改思考块，因为它们包含模型继续推理所需的签名。
- 在会话中切换模型时，您仍应重新发送之前模型的思考块。后端管理兼容性。

## 价格

开启思考功能后，回答价格是输出 token 和思考 token 的总和。您可以从 `total_thought_tokens` 字段获取生成的思考令牌总数。

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

思考模型会生成完整的想法，以提高最终回答的质量，然后输出[总结](#summaries)，以便深入了解思考过程。定价基于模型需要生成的完整思考令牌，尽管 API 只输出摘要。

如需详细了解令牌，请参阅[令牌计数](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn)指南。

## 最佳做法

遵循以下准则，可高效使用思考模型。

- **查看推理过程**：分析思维总结，了解失败原因并改进提示。
- **控制思考预算**：提示模型减少思考，以节省 token。
- **简单任务**：使用最少或少量思考来检索事实或进行分类（例如“DeepMind 是在哪里成立的？”）。
- **中等任务**：使用默认的思考模式来比较概念或进行创意推理（例如，比较电动汽车和混合动力汽车）。
- **复杂任务**：使用最大思考量来完成高级编码、数学或多步规划任务（例如，解决 AIME 数学问题）。

## 后续步骤

- [文本生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn)：基本文本回答
- [函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)：连接到工具
- [Gemini 3 指南](https://ai.google.dev/gemini-api/docs/gemini-3?hl=zh-cn)：特定于模型的功能

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-06。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-06。"],[],[]]
