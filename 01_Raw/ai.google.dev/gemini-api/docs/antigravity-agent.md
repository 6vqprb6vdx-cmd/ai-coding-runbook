---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi
fetched_at: 2026-07-06T05:21:18.289590+00:00
title: "T\u00e1c nh\u00e2n Antigravity \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tác nhân Antigravity

Tác nhân Antigravity là một tác nhân được quản lý đa năng trên API Gemini. Một lệnh gọi API duy nhất sẽ cung cấp cho bạn một tác nhân có khả năng suy luận, thực thi mã, quản lý tệp và duyệt web trong hộp cát Linux bảo mật của riêng bạn, do Google lưu trữ.

Gemini Spark được hỗ trợ bởi Gemini 3.5 Flash và sử dụng cùng một cơ chế như Antigravity IDE. Có trong [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) và [Google AI Studio](https://aistudio.google.com?hl=vi).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Tính năng

Mỗi lệnh gọi có thể cung cấp một hộp cát Linux và bắt đầu một vòng lặp sử dụng công cụ. Tác nhân lập kế hoạch, hành động, quan sát kết quả và lặp lại cho đến khi hoàn thành nhiệm vụ.

- **Thực thi mã:** Chạy các lệnh Bash, Python và Node.js. Cài đặt gói, chạy kiểm thử, tạo ứng dụng.
- **Quản lý tệp:** Đọc, ghi, chỉnh sửa, tìm kiếm và liệt kê các tệp trong hộp cát. Các tệp vẫn tồn tại trong các lượt tương tác.
- **Quyền truy cập vào web:** Google Tìm kiếm và tìm nạp URL để lấy dữ liệu.
- **Nén bối cảnh:** Tự động nén bối cảnh (được kích hoạt ở khoảng 135.000 mã thông báo) để hỗ trợ các phiên kéo dài nhiều lượt mà không làm mất bối cảnh hoặc vượt quá giới hạn mã thông báo.

Hãy xem phần [Bắt đầu nhanh](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi) để biết cách sử dụng nhiều lượt và phát trực tuyến.

## Các công cụ được hỗ trợ

Theo mặc định, tác nhân có quyền truy cập vào `code_execution`, `google_search` và `url_context`. Các công cụ hệ thống tệp sẽ tự động được bật khi bạn chỉ định tham số `environment`. Bạn cũng có thể xác định **các hàm tuỳ chỉnh** để kết nối tác nhân với các API và công cụ của riêng mình. Bạn chỉ cần chỉ định tham số `tools` khi tuỳ chỉnh hoặc hạn chế bộ mặc định, hoặc khi thêm các hàm tuỳ chỉnh.

| Công cụ | Giá trị loại | Mô tả |
| --- | --- | --- |
| Thực thi mã | `code_execution` | Chạy các lệnh shell (bash, Python, Node) với tính năng ghi lại stdout/stderr. |
| Google Tìm kiếm | `google_search` | Tìm kiếm trên web công khai. |
| Ngữ cảnh URL | `url_context` | Tìm nạp và đọc các trang web. |
| Hệ thống tệp | *(được bật thông qua `environment`)* | Đọc, ghi, chỉnh sửa, tìm kiếm và liệt kê các tệp trong hộp cát. Không có loại công cụ riêng biệt; tự động bật khi bạn đặt `environment`. |
| Hàm tuỳ chỉnh | `function` | Xác định các hàm tuỳ chỉnh mà tác nhân có thể yêu cầu thực thi. Xem phần [Gọi hàm](#function-calling). |
| Máy chủ MCP từ xa | `mcp_server` | Đăng ký các máy chủ Giao thức ngữ cảnh mô hình (MCP) bên ngoài dưới dạng công cụ. Xem phần [Máy chủ MCP](#mcp-servers). |

Để giới hạn tác nhân ở các công cụ cụ thể, hãy chỉ truyền những công cụ bạn cần:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## Đầu vào đa phương thức

Tác nhân Antigravity hỗ trợ thông tin đầu vào đa phương thức. Hiện tại, chỉ có đầu vào `text` và `image` được hỗ trợ. Bạn phải cung cấp hình ảnh dưới dạng chuỗi được mã hoá base64 cùng dòng (`data`).

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### REST

```
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## Gọi hàm

Tính năng gọi hàm cho phép bạn kết nối tác nhân Antigravity với các API và cơ sở dữ liệu bên ngoài bằng cách xác định các công cụ tuỳ chỉnh mà tác nhân có thể gọi. Để biết các khái niệm chung, hãy xem phần [Gọi hàm bằng Gemini API](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=vi).

Ví dụ sau đây minh hoạ một lượt tương tác gồm 2 lượt. Trước tiên, tác nhân yêu cầu một lệnh gọi hàm `get_weather` tuỳ chỉnh, sau đó máy khách thực thi lệnh gọi hàm đó và trả về kết quả trong lượt thứ hai.

### Python

```
from google import genai

client = genai.Client()

# 1. Define the custom function
get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and country, e.g. San Francisco, USA",
            }
        },
        "required": ["location"],
    },
}

# 2. Call the agent with the custom tool (Turn 1)
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[
        {"type": "code_execution"},  # Enable default code execution
        get_weather_tool,            # Add custom function
    ],
)

# Check if the agent requested a function call
if interaction.status == "requires_action":
    # Find function calls that do not have a matching function result.
    # Filesystem tools (like write_file) are also represented as function calls
    # but are executed automatically by the environment.
    executed_calls = {step.call_id for step in interaction.steps if step.type == "function_result"}
    pending_calls = [step for step in interaction.steps if step.type == "function_call" and step.id not in executed_calls]

    if pending_calls:
        fc_step = pending_calls[0]
        print(f"Function to call: {fc_step.name} (ID: {fc_step.id})")
        print(f"Arguments: {fc_step.arguments}")

        # 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        function_result = {
            "temperature": 23,
            "unit": "celsius"
        }

        final_interaction = client.interactions.create(
            agent="antigravity-preview-05-2026",
            previous_interaction_id=interaction.id,  # Reference the interaction ID
            environment=interaction.environment_id,
            input=[
                {
                    "type": "function_result",
                    "name": fc_step.name,
                    "call_id": fc_step.id,
                    "result": function_result,
                }
            ],
        )

        print(final_interaction.output_text)
        # Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    else:
        print("No pending function calls.")
else:
    print(f"Interaction completed with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// 1. Define the custom function
const get_weather_tool = {
  type: "function",
  name: "get_weather",
  description: "Gets the current weather for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city and country, e.g. San Francisco, USA",
      },
    },
    required: ["location"],
  },
};

// 2. Call the agent with the custom tool (Turn 1)
const interaction = await client.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "What is the weather in Tokyo?",
  environment: "remote",
  tools: [
    { type: "code_execution" },
    get_weather_tool,
  ],
}, { timeout: 300000 });

if (interaction.status === "requires_action") {
  // Find function calls that do not have a matching function result.
  // Filesystem tools (like write_file) are also represented as function calls
  // but are executed automatically by the environment.
  const executedCalls = new Set(
    interaction.steps
      .filter(s => s.type === "function_result")
      .map(s => s.call_id)
  );
  const pendingCalls = interaction.steps.filter(
    s => s.type === "function_call" && !executedCalls.has(s.id)
  );

  if (pendingCalls.length > 0) {
    const fcStep = pendingCalls[0];
    console.log(`Function to call: ${fcStep.name} (ID: ${fcStep.id})`);

    // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
    const functionResult = {
      temperature: 23,
      unit: "celsius"
    };

    const finalInteraction = await client.interactions.create({
      agent: "antigravity-preview-05-2026",
      previous_interaction_id: interaction.id, // Reference the interaction ID
      environment: interaction.environment_id,
      input: [
        {
          type: "function_result",
          name: fcStep.name,
          call_id: fcStep.id,
          result: functionResult,
        }
      ],
    }, { timeout: 300000 });

    console.log(finalInteraction.output_text);
  } else {
    console.log("No pending function calls.");
  }
} else {
  console.log(`Interaction completed with status: ${interaction.status}`);
}
```

### REST

```
# 1. Turn 1: Request function call
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [
          {"type": "code_execution"},
          {
              "type": "function",
              "name": "get_weather",
              "description": "Gets the current weather for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string"}
                  },
                  "required": ["location"]
              }
          }
      ]
  }')

# Extract interaction ID, environment ID, and call ID (requires jq)
INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')
ENVIRONMENT_ID=$(echo $RESPONSE | jq -r '.environment_id')
CALL_ID=$(echo $RESPONSE | jq -r '.steps[] | select(.type=="function_call") | .id')

# 2. Turn 2: Send function result back using variables
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"input\": [
          {
              \"type\": \"function_result\",
              \"name\": \"get_weather\",
              \"call_id\": \"$CALL_ID\",
              \"result\": {
                  \"temperature\": 23,
                  \"unit\": \"celsius\"
              }
          }
      ]
  }"
```

## Máy chủ MCP

Bạn có thể kết nối tác nhân Antigravity với các công cụ bên ngoài bằng cách đăng ký các máy chủ Giao thức ngữ cảnh mô hình (MCP) từ xa. Tác nhân hỗ trợ các máy chủ MCP từ xa qua HTTP có thể truyền phát.

Khi đăng ký máy chủ MCP, bạn phải chỉ định các trường sau trong mảng `tools`:

| Trường | Loại | Bắt buộc | Mô tả |
| --- | --- | --- | --- |
| `type` | chuỗi | Có | Phải là `"mcp_server"`. |
| `name` | chuỗi | Có | Giá trị nhận dạng riêng biệt của máy chủ. Phải là chữ thường và bao gồm cả chữ và số (phù hợp với `^[a-z0-9_-]+$`). |
| `url` | chuỗi | Có | URL điểm cuối của máy chủ MCP từ xa. |
| `headers` | đối tượng | Không | Tiêu đề tuỳ chỉnh (ví dụ: xác thực) được gửi cùng với các yêu cầu. |
| `allowed_tools` | mảng | Không | Danh sách tên công cụ được phép thực thi. Nếu bạn bỏ qua, tất cả các công cụ đều được phép. |

### Python

```
from google import genai

client = genai.Client()

# Register a remote HTTP MCP server
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "weather", # Must be lowercase
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "What is the weather in Tokyo?",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "weather", // Must be lowercase
        url: "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [{
          "type": "mcp_server",
          "name": "weather",
          "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
      }]
  }'
```

## Tuỳ chỉnh tác nhân

Bạn có thể mở rộng tác nhân Antigravity bằng cách tuỳ chỉnh các chỉ dẫn, công cụ và môi trường của nó. Tác nhân này hỗ trợ phương pháp tuỳ chỉnh gốc của hệ thống tệp: bạn có thể gắn các tệp như `AGENTS.md` cho hướng dẫn và kỹ năng trong `.agents/skills/` trực tiếp vào hộp cát hoặc truyền cấu hình nội tuyến tại thời điểm tương tác. Bạn có thể lặp lại cấu hình nội tuyến rồi lưu cấu hình đó dưới dạng một tác nhân được quản lý khi đã sẵn sàng.

Để biết đầy đủ thông tin chi tiết về cách tạo các tác nhân tuỳ chỉnh, hãy xem bài viết [Tạo tác nhân được quản lý](https://ai.google.dev/gemini-api/docs/custom-agents?hl=vi).

## Chạy ở chế độ nền

Các nhiệm vụ của tác nhân liên quan đến suy luận đa bước, thực thi mã hoặc thao tác với tệp có thể mất vài phút để hoàn thành. Sử dụng `background=True` để chạy lượt tương tác không đồng bộ. API này sẽ trả về ngay lập tức một mã nhận dạng lượt tương tác mà bạn sẽ thăm dò cho đến khi trạng thái là `completed` hoặc `failed`.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the interaction in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run a complex analysis on the repository.",
    environment="remote",
    background=True,
)

print(f"Interaction started in background: {interaction.id}")

# 2. Poll for completion
while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run a complex analysis on the repository.",
    environment: "remote",
    background: true,
});

console.log(`Interaction started in background: ${interaction.id}`);

let result = interaction;
while (result.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    result = await client.interactions.get(interaction.id);
}

if (result.status === "completed") {
    console.log(result.output_text);
} else {
    console.log(`Finished with status: ${result.status}`);
}
```

### REST

```
# 1. Start the interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Run a complex analysis on the repository.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll for results (repeat until status is "completed")
curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

Chế độ thực thi trong nền yêu cầu `store=True` (đây là chế độ mặc định). Để biết thông tin cập nhật tiến trình theo thời gian thực trong quá trình thực thi ở chế độ nền, hãy xem phần [Truyền trực tuyến các hoạt động tương tác ở chế độ nền](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=vi#streaming-background).

Bạn có thể huỷ một hoạt động tương tác đang chạy ở chế độ nền bằng phương thức `cancel`.

### Python

```
client.interactions.cancel(id="INTERACTION_ID")
```

### JavaScript

```
await client.interactions.cancel({ id: "INTERACTION_ID" });
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID:cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

**Nhiều lượt với tính năng thực thi trong nền**

Khi một hoạt động tương tác ở chế độ nền liên quan đến các công cụ có trạng thái (chẳng hạn như thực thi mã trong hộp cát), hãy sử dụng `environment_id` từ hoạt động tương tác đã hoàn tất để tiếp tục trong cùng một môi trường. Điều này đảm bảo rằng tác nhân sẽ tiếp tục từ nơi đã dừng lại với tất cả các tệp và trạng thái còn nguyên vẹn.

### Python

```
import time
from google import genai

client = genai.Client()

# First turn: run a task in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Clone https://github.com/google/generative-ai-python and run its tests.",
    environment="remote",
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Second turn: continue in the same environment
followup = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Fix any failing tests and re-run them.",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    background=True,
)

while followup.status == "in_progress":
    time.sleep(5)
    followup = client.interactions.get(id=followup.id)

print(followup.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First turn: run a task in the background
let interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Clone https://github.com/google/generative-ai-python and run its tests.",
    environment: "remote",
    background: true,
});

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

// Second turn: continue in the same environment
let followup = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Fix any failing tests and re-run them.",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    background: true,
});

while (followup.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    followup = await client.interactions.get(followup.id);
}

console.log(followup.output_text);
```

### REST

```
# 1. Start first interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Clone https://github.com/google/generative-ai-python and run its tests.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll until completed (repeat until status is "completed")
RESULT=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY")

ENVIRONMENT_ID=$(echo $RESULT | jq -r '.environment_id')

# 3. Continue in the same environment
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"input\": \"Fix any failing tests and re-run them.\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"background\": true
  }"
```

## Môi trường

Mỗi lệnh gọi sẽ tạo hoặc sử dụng lại một hộp cát Linux. Tham số `environment` có 3 dạng:

| Biểu mẫu | Mô tả |
| --- | --- |
| `"remote"` | Cung cấp một hộp cát mới với chế độ cài đặt mặc định. |
| `"env_abc123"` | Tái sử dụng một môi trường hiện có theo mã nhận dạng, giữ nguyên mọi tệp và trạng thái. |
| `{...}` | `EnvironmentConfig` đầy đủ với các quy tắc mạng và nguồn tuỳ chỉnh. |

Hãy xem phần [Môi trường](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi) để biết thông tin chi tiết về các nguồn (Git, GCS, nội tuyến), mạng, vòng đời và hạn mức tài nguyên.

## Tình trạng còn hàng và giá

Bạn có thể dùng thử tác nhân Antigravity thông qua [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) trong Google AI Studio và Gemini API.

Giá được tính theo [mô hình trả tiền theo mức dùng](https://ai.google.dev/gemini-api/docs/pricing?hl=vi#pricing-for-agents) dựa trên số lượng token của mô hình Gemini cơ bản và các công cụ mà tác nhân sử dụng. Không giống như yêu cầu trò chuyện tiêu chuẩn tạo ra một đầu ra duy nhất, tương tác Antigravity là một quy trình làm việc dựa trên tác nhân. Một yêu cầu duy nhất sẽ kích hoạt một vòng lặp tự động gồm suy luận, thực thi công cụ, chạy mã và quản lý tệp.

### Chi phí ước tính

Chi phí sẽ khác nhau tuỳ thuộc vào độ phức tạp của nhiệm vụ. Tác nhân tự động xác định số lượng lệnh gọi công cụ, lượt thực thi mã và thao tác tệp cần thiết. Các số liệu ước tính sau đây dựa trên các lần chạy.

| Danh mục việc cần làm | Mã thông báo nhập | Mã thông báo xuất | Chi phí thông thường |
| --- | --- | --- | --- |
| **Nghiên cứu và tổng hợp thông tin** | 100.000 – 500.000 | 10.000 – 40.000 | 0,30 – 1,00 USD |
| **Tạo tài liệu và nội dung** | 100.000 – 500.000 | 15.000 – 50.000 | 0,30 USD – 1,30 USD |
| **Thiết kế quy trình và hệ thống** | 100.000 – 400.000 | 10.000 – 30.000 | 0,25 – 0,80 USD |
| **Xử lý và phân tích dữ liệu** | 300.000 – 3.000.000 | 30.000 – 150.000 | 0,70 USD – 3,25 USD |

Thông thường, 50–70% mã thông báo đầu vào được lưu vào bộ nhớ đệm. Các quy trình công việc phức tạp của tác nhân với nhiều lệnh gọi công cụ có thể tích luỹ từ 3 đến 5 triệu mã thông báo trong một lượt tương tác duy nhất, với chi phí lên đến khoảng 5 USD.

**Điện toán môi trường** (CPU, bộ nhớ, thực thi hộp cát) **không được tính phí** trong thời gian xem trước.

## Các điểm hạn chế

- **Trạng thái xem trước:** Tác nhân Antigravity và Interactions API. Các tính năng và giản đồ có thể thay đổi.
- **Cấu hình tạo không được hỗ trợ:** Các tham số sau không được hỗ trợ và trả về lỗi 400: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Đầu ra có cấu trúc:** Tác nhân Antigravity không hỗ trợ đầu ra có cấu trúc.
- **Các công cụ không dùng được:** `file_search`, `computer_use` và `google_maps` hiện chưa được hỗ trợ.
- **Các hạn chế đối với MCP từ xa:** Không hỗ trợ phương thức truyền Sự kiện được gửi bởi máy chủ (SSE) (hãy dùng HTTP có thể truyền trực tuyến). Ngoài ra, `name` của máy chủ phải hoàn toàn là chữ thường và chữ và số (việc sử dụng chữ hoa sẽ kích hoạt lỗi `400 Bad Request` chung).
- **Công cụ hệ thống tệp:** Hiện không có công cụ hệ thống tệp. Đây là một phần của `environment`.
- **Yêu cầu về cửa hàng:** Việc thực thi tác nhân bằng `background=True` yêu cầu `store=True`.
- **Chỉ gọi hàm có trạng thái:** Tính năng gọi hàm chỉ được hỗ trợ ở chế độ có trạng thái. Bạn phải sử dụng `previous_interaction_id` để tiếp tục lượt trò chuyện; hệ thống không hỗ trợ việc khôi phục nhật ký theo cách thủ công (chế độ không trạng thái).
- **Các loại nội dung đa phương thức không được hỗ trợ.** Hiện tại, chúng tôi không hỗ trợ dữ liệu đầu vào là âm thanh, video và tài liệu. Bạn chỉ được phép sử dụng văn bản và hình ảnh.

## Bước tiếp theo

- [Bắt đầu nhanh](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi): cuộc trò chuyện nhiều lượt và truyền phát trực tuyến.
- [Tạo tác nhân tuỳ chỉnh](https://ai.google.dev/gemini-api/docs/custom-agents?hl=vi): hướng dẫn, kỹ năng tuỳ chỉnh và lưu tác nhân.
- [Môi trường](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi): cấu hình hộp cát, nguồn, mạng.
- [Tác nhân Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi): các nhiệm vụ nghiên cứu dài.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi): API cơ bản.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-26 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-26 UTC."],[],[]]
