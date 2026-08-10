---
source_url: https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-CN
fetched_at: 2026-08-10T03:23:34.004165+00:00
title: "\u4ee3\u7801\u6267\u884c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 代码执行

Gemini API 提供了一个代码执行工具，可让模型生成和运行 Python 代码。然后，模型可以根据代码执行结果进行迭代学习，直到获得最终输出。您可以利用代码执行功能来构建可受益于基于代码的推理的应用。例如，您可以使用代码执行功能来求解方程式或处理文本。您还可以使用代码执行环境中包含的[库](#supported-libraries)来执行更专业的任务。

Gemini 只能执行 Python 代码。您仍然可以要求 Gemini 以其他语言生成代码，但模型无法使用代码执行工具来运行该代码。

## 启用代码执行功能

如需启用代码执行功能，请在模型上配置代码执行工具。这样一来，模型便可生成并运行代码。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the sum of the first 50 prime numbers? "
          "Generate and run code for the calculation, and make sure you get all 50.",
    tools=[{"type": "code_execution"}]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
    elif step.type == "code_execution_call":
        print(step.arguments.code)
    elif step.type == "code_execution_result":
        print(step.result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What is the sum of the first 50 prime numbers? " +
           "Generate and run code for the calculation, and make sure you get all 50.",
    tools: [{ type: "code_execution" }]
});

for (const step of interaction.steps) {
    if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log(contentBlock.text);
            }
        }
    } else if (step.type === "code_execution_call") {
        console.log(step.arguments.code);
    } else if (step.type === "code_execution_result") {
        console.log(step.result);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
    "model": "gemini-3.6-flash",
    "input": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50.",
    "tools": [{"type": "code_execution"}]
}'
```

输出结果可能如下所示（为了便于阅读，已进行格式设置）：

```
Okay, I need to calculate the sum of the first 50 prime numbers. Here's how I'll
approach this:

1.  **Generate Prime Numbers:** I'll use an iterative method to find prime
    numbers. I'll start with 2 and check if each subsequent number is divisible
    by any number between 2 and its square root. If not, it's a prime.
2.  **Store Primes:** I'll store the prime numbers in a list until I have 50 of
    them.
3.  **Calculate the Sum:**  Finally, I'll sum the prime numbers in the list.

Here's the Python code to do this:

def is_prime(n):
  """Efficiently checks if a number is prime."""
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

primes = []
num = 2
while len(primes) < 50:
  if is_prime(num):
    primes.append(num)
  num += 1

sum_of_primes = sum(primes)
print(f'{primes=}')
print(f'{sum_of_primes=}')

primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
sum_of_primes=5117

The sum of the first 50 prime numbers is 5117.
```

此输出结合了模型在使用代码执行功能时返回的多个内容部分：

- `text`：模型生成的内嵌文本
- `code_execution_call`：由模型生成且旨在执行的代码
- `code_execution_result`：可执行代码的结果

## 使用图片执行代码 (Gemini 3)

Gemini 3 Flash 模型现在可以编写和执行 Python 代码，主动操纵和检查图片。

**用例**

- **缩放和检查**：模型会隐式检测细节何时过小（例如，读取远处的仪表），并编写代码来裁剪和重新检查更高分辨率的区域。
- **可视化数学**：模型可以使用代码运行多步计算（例如，对收据上的各个商品项求和）。
- **图片注释**：模型可以注释图片以回答问题，例如绘制箭头来显示关系。

## 启用图片代码执行功能

Gemini 3 Flash 正式支持使用图片执行代码。您可以同时启用“将代码执行作为工具”和“思考”来激活此行为。

### Python

```
from google import genai
import requests
import base64
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "image", "data": base64.b64encode(image_bytes).decode('utf-8'), "mime_type": "image/jpeg"},
        {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
    ],
    tools=[{"type": "code_execution"}]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                img = Image.open(io.BytesIO(base64.b64decode(content_block.data)))
                img.show()  # or: img.save("output_image.jpg")
    elif step.type == "code_execution_call":
        print(step.arguments.code)
    elif step.type == "code_execution_result":
        print(step.result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {
  const client = new GoogleGenAI({});

  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
      {
        type: "image",
        data: base64ImageData,
        mime_type: "image/jpeg"
      },
      { type: "text", text: "Zoom into the expression pedals and tell me how many pedals are there?" }
    ],
    tools: [{ type: "code_execution" }]
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log(`\nGenerated Code:\n`, step.arguments.code);
    } else if (step.type === "code_execution_result") {
      console.log(`\nExecution Output:\n`, step.result);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3.6-flash"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# Use jq to create the JSON payload to avoid "Argument list too long" error with large base64 strings
echo -n "$IMAGE_B64" > image_b64.txt
jq -n \
  --rawfile b64 image_b64.txt \
  --arg mime "$MIME_TYPE" \
  '{
    model: "gemini-3.6-flash",
    input: [
      {type: "image", data: $b64, mime_type: $mime},
      {type: "text", text: "Zoom into the expression pedals and tell me how many pedals are there?"}
    ],
    tools: [{type: "code_execution"}]
  }' > payload.json

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d @payload.json
```

## 在多轮交互中使用代码执行功能

您还可以使用 `previous_interaction_id` 在多轮对话中使用代码执行功能。

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="I have a math question for you.",
    tools=[{"type": "code_execution"}]
)
print(interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    previous_interaction_id=interaction1.id,
    input="What is the sum of the first 50 prime numbers? "
          "Generate and run code for the calculation, and make sure you get all 50.",
    tools=[{"type": "code_execution"}]
)

for step in interaction2.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
    elif step.type == "code_execution_call":
        print(step.arguments.code)
    elif step.type == "code_execution_result":
        print(step.result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction1 = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "I have a math question for you.",
    tools: [{ type: "code_execution" }]
});
console.log(interaction1.output_text);

const interaction2 = await client.interactions.create({
    model: "gemini-3.6-flash",
    previous_interaction_id: interaction1.id,
    input: "What is the sum of the first 50 prime numbers? " +
           "Generate and run code for the calculation, and make sure you get all 50.",
    tools: [{ type: "code_execution" }]
});

for (const step of interaction2.steps) {
    if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log(contentBlock.text);
            }
        }
    } else if (step.type === "code_execution_call") {
        console.log(step.arguments.code);
    } else if (step.type === "code_execution_result") {
        console.log(step.result);
    }
}
```

### REST

```
# First turn
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
    "model": "gemini-3.6-flash",
    "input": "I have a math question for you.",
    "tools": [{"type": "code_execution"}]
}')

INTERACTION_ID=$(echo $RESPONSE1 | jq -r '.id')

# Second turn with previous_interaction_id
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
    "model": "gemini-3.6-flash",
    "previous_interaction_id": "'"$INTERACTION_ID"'",
    "input": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50.",
    "tools": [{"type": "code_execution"}]
}'
```

## 输入/输出 (I/O)

在当前的 Gemini 模型（例如 [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#gemini-3.6-flash)）中，代码执行支持文件输入和图表输出。利用这些输入和输出功能，您可以上传 CSV 和文本文件，询问有关这些文件的问题，并让系统在回答中为您生成 [Matplotlib](https://matplotlib.org/) 图表。输出文件以内嵌图片的形式在响应中返回。

### I/O 定价

使用代码执行 I/O 时，您需要为输入 token 和输出 token 支付费用：

**输入 token**：

- 用户提示

**输出 token 数**：

- 模型生成的代码
- 代码环境中的代码执行输出
- 思考 token
- 由模型生成的摘要

### I/O 详情

使用代码执行 I/O 时，请注意以下技术细节：

- 代码环境的最长运行时间为 30 秒。
- 如果代码环境生成错误，模型可能会决定重新生成代码输出。此过程最多可重复 5 次。
- 文件输入大小上限受模型 token 窗口的限制。如果您上传的文件超出了模型的最大上下文窗口，API 将返回错误。
- 代码执行最适合处理文本文件和 CSV 文件。
- 输入文件可以作为内嵌数据传递，也可以使用 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn) 上传，而输出文件始终作为内嵌数据返回。

## 结算

通过 Gemini API 启用代码执行功能不会产生额外的费用。系统会根据您使用的 Gemini 模型，按当前的输入和输出 token 费率向您收费。

以下是关于代码执行结算的一些其他事项：

- 您只需为传递给模型的输入 token 支付一次费用，并需要为模型返回给您的最终输出 token 支付费用。
- 表示生成的代码的 token 会计为输出 token。生成的代码可以包含文本和多模态输出结果（例如图片）。
- 代码执行结果也会计为输出 token。

结算模式如下图所示：

![代码执行结算模式](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=zh-cn)

- 系统会根据您使用的 Gemini 模型，按当前的输入和输出 token 费率向您收费。
- 如果 Gemini 在生成回答时使用了代码执行功能，则原始提示、生成的代码以及已执行代码的相应结果会被标记为*中间 token*，并会按*输入 token* 计费。
- 然后，Gemini 会生成摘要，并返回生成的代码、已执行代码的相应结果以及最终摘要。这些内容会按*输出 token* 计费。
- Gemini API 在 API 响应中包含中间 token 数量，因此您可以了解为什么会获得除初始提示之外的其他输入 token。

## 限制

- 该模型只能生成和执行代码。它无法返回其他制品，例如媒体文件。
- 在某些情况下，启用代码执行功能可能会导致模型输出的其他方面（例如，编写故事）出现回归问题。
- 不同模型成功使用代码执行功能的能力各不相同。

## 支持的工具组合

代码执行工具可以与[依托 Google 搜索进行接地](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)功能结合使用，以处理更复杂的用例。

Gemini 3 模型支持将内置工具（例如代码执行）与自定义工具（函数调用）相结合。

## 受支持的库

代码执行环境包含以下库：

- attrs
- 国际象棋
- contourpy
- fpdf
- geopandas
- imageio
- jinja2
- joblib
- jsonschema
- jsonschema-specifications
- lxml
- matplotlib
- mpmath
- numpy
- opencv-python
- openpyxl
- 打包
- pandas
- pillow
- protobuf
- pylatex
- pyparsing
- PyPDF2
- python-dateutil
- python-docx
- python-pptx
- reportlab
- scikit-learn
- scipy
- seaborn
- six
- striprtf
- sympy
- tabulate
- TensorFlow
- toolz
- xlrd

您无法安装自己的库。

## 后续步骤

- 不妨试试[Interactions API 快速入门](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-cn)。
- 了解其他 Gemini API 工具：
  - [函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)
  - [使用 Google 搜索建立依据](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-30。"],[],[]]
