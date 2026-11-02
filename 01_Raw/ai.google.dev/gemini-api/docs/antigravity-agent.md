---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi
fetched_at: 2026-11-02T07:27:12.471112+00:00
title: "T\u00e1c nh\u00e2n Antigravity \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tác nhân Antigravity

Tác nhân Antigravity là một tác nhân được quản lý đa năng trên Gemini API. Một lệnh gọi API duy nhất sẽ cung cấp cho bạn một tác nhân có khả năng suy luận, thực thi mã, quản lý tệp và duyệt web trong hộp cát Linux bảo mật của riêng bạn, do Google lưu trữ.

Công cụ này được xây dựng bằng Gemini 3.8 Flash và sử dụng cùng một bộ khung như Antigravity IDE. Bạn có thể định cấu hình mô hình Gemini cơ bản bằng `agent_config`. Có thể sử dụng thông qua [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) và [Google AI Studio](https://aistudio.google.com?hl=vi).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Read Hacker News, summarize the top 10 stories, and save the results as a PDF."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Read Hacker News, summarize the top 10 stories, and save the results as a PDF."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
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
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Tính năng

Mỗi lệnh gọi có thể cung cấp một hộp cát Linux và bắt đầu một vòng lặp sử dụng công cụ. Tác nhân lập kế hoạch, hành động, quan sát kết quả và lặp lại cho đến khi hoàn thành nhiệm vụ.

- **Thực thi mã:** Chạy các lệnh Bash, Python và Node.js. Cài đặt gói, chạy kiểm thử, tạo ứng dụng.
- **Quản lý tệp:** Đọc, ghi, chỉnh sửa, tìm kiếm và liệt kê các tệp trong hộp cát. Các tệp vẫn tồn tại trong suốt quá trình tương tác.
- **Quyền truy cập vào web:** Google Tìm kiếm và tính năng tìm nạp URL để lấy dữ liệu.
- **Nén bối cảnh:** Tự động nén bối cảnh (kích hoạt ở khoảng 135.000 mã thông báo) để hỗ trợ các phiên dài, nhiều lượt mà không làm mất bối cảnh hoặc vượt quá giới hạn mã thông báo.

Hãy xem phần [Bắt đầu nhanh](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi) để biết cách sử dụng nhiều lượt và phát trực tuyến.

## Công cụ được hỗ trợ

Theo mặc định, tác nhân có quyền truy cập vào `code_execution`, `google_search` và `url_context`. Các công cụ hệ thống tệp sẽ tự động được bật khi bạn chỉ định tham số `environment`. Bạn cũng có thể xác định **hàm tuỳ chỉnh** để kết nối tác nhân với các API và công cụ của riêng bạn. Bạn chỉ cần chỉ định tham số `tools` khi tuỳ chỉnh hoặc hạn chế tập hợp mặc định, hoặc khi thêm các hàm tuỳ chỉnh.

| Công cụ | Nhập giá trị | Mô tả |
| --- | --- | --- |
| Thực thi mã | `code_execution` | Chạy lệnh shell (bash, Python, Node) bằng tính năng ghi lại stdout/stderr. |
| Google Tìm kiếm | `google_search` | Tìm kiếm trên web công khai. |
| Bối cảnh từ URL | `url_context` | Tìm nạp và đọc các trang web. |
| Hệ thống tệp | *(được bật thông qua `environment`)* | Đọc, ghi, chỉnh sửa, tìm kiếm và liệt kê các tệp trong hộp cát. Hệ thống sẽ tự động bật các công cụ này khi bạn đặt `environment`. |
| Hàm tuỳ chỉnh | `function` | Xác định các hàm tuỳ chỉnh mà tác nhân có thể yêu cầu thực thi. Xem phần [Gọi hàm](#function-calling). |
| Máy chủ MCP từ xa | `mcp_server` | Đăng ký máy chủ Giao thức ngữ cảnh mô hình (MCP) bên ngoài làm công cụ. Xem [máy chủ MCP](#mcp-servers). |

Bạn có thể chặn và xác thực quá trình thực thi công cụ `code_execution` và `filesystem` ngay trong hộp cát từ xa bằng cách sử dụng [Hooks](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=vi) đồng bộ.

Để giới hạn tác nhân ở một số công cụ cụ thể, chỉ truyền những công cụ bạn cần:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.URLContext;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Search for the latest AI research papers on reasoning and summarize them."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .tools(List.of(
        GoogleSearch.builder().build(),
        URLContext.builder().build()
    ))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Search for the latest AI research papers on reasoning and summarize them."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
                interactions.NewTool(interactions.URLContext{}),
            },
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
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## Thông tin đầu vào đa phương thức

Tác nhân Antigravity hỗ trợ dữ liệu đầu vào đa phương thức. Hiện tại, chúng tôi chỉ hỗ trợ dữ liệu đầu vào `text` và `image`. Bạn phải cung cấp hình ảnh dưới dạng chuỗi được mã hoá base64 cùng dòng (`data`).

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("path/to/chart.png"));
String base64Image = Base64.getEncoder().encodeToString(imageBytes);

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.ofContent(List.of(
        TextContent.builder().text("Analyze this chart and summarize the trends.").build(),
        ImageContent.builder()
            .data(base64Image)
            .mimeType(ImageContentMimeType.IMAGE_PNG)
            .build()
    )))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interactionInline = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interactionInline.outputText().orElse(""));
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

    imageBytes, err := os.ReadFile("path/to/chart.png")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Analyze this chart and summarize the trends.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Image),
                    MimeType: interactions.ImageContentMimeTypeImagePng.ToPointer(),
                }),
            }),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
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
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-09-2026\",
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

Tính năng gọi hàm cho phép bạn kết nối tác nhân Antigravity với các API và cơ sở dữ liệu bên ngoài bằng cách xác định các công cụ tuỳ chỉnh mà tác nhân có thể gọi. Để biết các khái niệm chung, hãy xem phần [Gọi hàm bằng Gemini API](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi).

Ví dụ sau đây minh hoạ một lượt tương tác gồm 2 lượt. Trước tiên, tác nhân yêu cầu một lệnh gọi hàm `get_weather` tuỳ chỉnh, sau đó ứng dụng thực thi lệnh gọi đó và trả về kết quả ở lượt thứ hai.

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
    agent="antigravity-preview-09-2026",
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
    # Filesystem tools (like write_to_file) are also represented as function calls
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
            agent="antigravity-preview-09-2026",
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

// 1. Call the agent with the custom tool (Turn 1)
const interaction = await client.interactions.create({
  agent: "antigravity-preview-09-2026",
  input: "What is the weather in Tokyo?",
  environment: "remote",
  tools: [
    { type: "code_execution" },
    {
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
    },
  ],
}, { timeout: 300000 });

if (interaction.status === "requires_action") {
  // Find function calls that do not have a matching function result.
  // Filesystem tools (like write_to_file) are also represented as function calls
  // but are executed automatically by the environment.
  const executedCalls = new Set(
    (interaction.steps || [])
      .filter(s => s.type === "function_result")
      .map(s => s.call_id)
  );
  const pendingCalls = (interaction.steps || []).filter(
    s => s.type === "function_call" && !executedCalls.has(s.id)
  );

  if (pendingCalls.length > 0) {
    const fcStep = pendingCalls[0];
    if (fcStep.type === "function_call") {
      console.log(`Function to call: ${fcStep.name} (ID: ${fcStep.id})`);

      // Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
      const functionResult = {
        temperature: 23,
        unit: "celsius"
      };

      const finalInteraction = await client.interactions.create({
        agent: "antigravity-preview-09-2026",
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
    }
  } else {
    console.log("No pending function calls.");
  }
} else {
  console.log(`Interaction completed with status: ${interaction.status}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

Client client = new Client();

// 1. Define the custom function
Function getWeatherTool = Function.builder()
    .name("get_weather")
    .description("Gets the current weather for a given location.")
    .parameters(Map.of(
        "type", "object",
        "properties", Map.of(
            "location", Map.of(
                "type", "string",
                "description", "The city and country, e.g. San Francisco, USA"
            )
        ),
        "required", List.of("location")
    ))
    .build();

// 2. Call the agent with the custom tool (Turn 1)
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("What is the weather in Tokyo?"))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .tools(List.of(
        CodeExecution.builder().build(), // Enable default code execution
        getWeatherTool                   // Add custom function
    ))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Check if the agent requested a function call
if (interaction.status().orElse(null) == InteractionStatus.REQUIRES_ACTION) {
    // Find function calls that do not have a matching function result.
    List<Step> steps = interaction.steps().orElse(List.of());
    Set<String> executedCalls = steps.stream()
        .filter(step -> step instanceof FunctionResultStep)
        .map(step -> ((FunctionResultStep) step).callId().orElse(""))
        .collect(Collectors.toSet());

    List<FunctionCallStep> pendingCalls = steps.stream()
        .filter(step -> step instanceof FunctionCallStep)
        .map(step -> (FunctionCallStep) step)
        .filter(fc -> !executedCalls.contains(fc.id().orElse("")))
        .collect(Collectors.toList());

    if (!pendingCalls.isEmpty()) {
        FunctionCallStep fcStep = pendingCalls.get(0);
        System.out.println("Function to call: " + fcStep.name().orElse("") + " (ID: " + fcStep.id().orElse("") + ")");
        System.out.println("Arguments: " + fcStep.arguments().orElse(Map.of()));

        // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        FunctionResultStep resultStep = FunctionResultStep.builder()
            .name(fcStep.name().orElse(""))
            .callId(fcStep.id().orElse(""))
            .result(FunctionResultStepResultUnion.of("{\"temperature\": 23, \"unit\": \"celsius\"}"))
            .build();

        CreateAgentInteraction followupParams = CreateAgentInteraction.builder()
            .agent(AgentOption.of("antigravity-preview-09-2026"))
            .previousInteractionId(interaction.id().orElse(""))
            .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
            .input(InteractionsInput.ofStep(List.of(resultStep)))
            .build();

        Interaction finalInteraction = client.interactions.create(CreateInteractionRequestBody.of(followupParams)).interaction().get();
        System.out.println(finalInteraction.outputText().orElse(""));
        // Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    } else {
        System.out.println("No pending function calls.");
    }
} else {
    System.out.println("Interaction completed with status: " + interaction.status().orElse(null));
}
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

    // 1. Define the custom function
    getWeatherTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_weather"),
        Description: genai.Ptr("Gets the current weather for a given location."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "location": map[string]any{
                    "type":        "string",
                    "description": "The city and country, e.g. San Francisco, USA",
                },
            },
            "required": []string{"location"},
        },
    })

    // 2. Call the agent with the custom tool (Turn 1)
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("What is the weather in Tokyo?"),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}), // Enable default code execution
                getWeatherTool, // Add custom function
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction

    // Check if the agent requested a function call
    if interaction.Status == interactions.InteractionStatusRequiresAction {
        executedCalls := make(map[string]bool)
        for _, step := range interaction.Steps {
            if fr := step.FunctionResultStep; fr != nil {
                executedCalls[fr.CallID] = true
            }
        }

        var pendingCalls []*interactions.FunctionCallStep
        for _, step := range interaction.Steps {
            if fc := step.FunctionCallStep; fc != nil && !executedCalls[fc.ID] {
                pendingCalls = append(pendingCalls, fc)
            }
        }

        if len(pendingCalls) > 0 {
            fcStep := pendingCalls[0]
            fmt.Printf("Function to call: %s (ID: %s)\n", fcStep.Name, fcStep.ID)
            fmt.Printf("Arguments: %v\n", fcStep.Arguments)

            // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
            resultStep := interactions.FunctionResultStep{
                Name:   genai.Ptr(fcStep.Name),
                CallID: fcStep.ID,
                Result: interactions.NewFunctionResultStepResultUnion(`{"temperature": 23, "unit": "celsius"}`),
            }

            followupRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
                    Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
                    PreviousInteractionID: interaction.ID,
                    Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
                    Input: interactions.NewInteractionsInput([]interactions.Step{
                        interactions.NewStep(resultStep),
                    }),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            if followupRes.Interaction.OutputText != nil {
                fmt.Println(*followupRes.Interaction.OutputText)
            }
        } else {
            fmt.Println("No pending function calls.")
        }
    } else {
        fmt.Printf("Interaction completed with status: %s\n", interaction.Status)
    }
}
```

### REST

```
# 1. Turn 1: Request function call
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
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
      \"agent\": \"antigravity-preview-09-2026\",
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

Bạn có thể kết nối tác nhân Antigravity với các công cụ bên ngoài bằng cách đăng ký các máy chủ Giao thức ngữ cảnh mô hình (MCP) từ xa. Tác nhân hỗ trợ máy chủ MCP từ xa qua HTTP có thể truyền trực tuyến.

Khi đăng ký máy chủ MCP, bạn phải chỉ định các trường sau trong mảng `tools`:

| Trường | Loại | Bắt buộc | Mô tả |
| --- | --- | --- | --- |
| `type` | chuỗi | Có | Phải là `"mcp_server"`. |
| `name` | chuỗi | Có | Giá trị nhận dạng riêng biệt của máy chủ. Phải hoàn toàn là chữ thường và chữ và số (khớp với `^[a-z0-9_-]+$`). |
| `url` | chuỗi | Có | URL điểm cuối của máy chủ MCP từ xa. |
| `headers` | đối tượng | Không | Tiêu đề tuỳ chỉnh (ví dụ: xác thực) được gửi cùng với các yêu cầu. |
| `allowed_tools` | mảng | Không | Danh sách tên công cụ được phép thực thi. Nếu bạn bỏ qua, tất cả các công cụ đều được cho phép. |

### Python

```
from google import genai

client = genai.Client()

# Register a remote HTTP MCP server
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.MCPServer;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

// Register a remote HTTP MCP server
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("What is the weather in Tokyo?"))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .tools(List.of(
        MCPServer.builder()
            .name("weather") // Must be lowercase
            .url("https://gemini-api-demos.uc.r.appspot.com/mcp")
            .build()
    ))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
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

    // Register a remote HTTP MCP server
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("What is the weather in Tokyo?"),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.MCPServer{
                    Name: genai.Ptr("weather"), // Must be lowercase
                    URL:  genai.Ptr("https://gemini-api-demos.uc.r.appspot.com/mcp"),
                }),
            },
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
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [{
          "type": "mcp_server",
          "name": "weather",
          "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
      }]
  }'
```

## Lựa chọn mô hình

Đối với `antigravity-preview-09-2026`, mô hình mặc định là **Gemini 3.8 Flash** (`gemini-3.8-flash`). Nếu bạn bỏ qua `agent_config`, tác nhân sẽ mặc định là `gemini-3.8-flash`.

Bạn có thể định cấu hình mô hình Gemini cơ bản bằng `agent_config` để tối ưu hoá tốc độ, chi phí hoặc khả năng suy luận. Ví dụ: đặt `model` thành **Gemini 4 Argon** (`gemini-4-argon`) cho các nhiệm vụ suy luận và kỹ thuật phần mềm phức tạp:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Summarize the key differences between functional and object-oriented programming.",
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-4-argon",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Summarize the key differences between functional and object-oriented programming.",
    environment: "remote",
    agent_config: {
        type: "antigravity",
        model: "gemini-4-argon",
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.AntigravityAgentConfig;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Summarize the key differences between functional and object-oriented programming."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .agentConfig(
        AntigravityAgentConfig.builder()
            .model("gemini-4-argon")
            .build()
    )
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Summarize the key differences between functional and object-oriented programming."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            AgentConfig: genai.Ptr(interactions.NewCreateAgentInteractionAgentConfig(interactions.AntigravityAgentConfig{
                Model: genai.Ptr("gemini-4-argon"),
            })),
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
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": "Summarize the key differences between functional and object-oriented programming.",
      "environment": "remote",
      "agent_config": {
          "type": "antigravity",
          "model": "gemini-4-argon"
      }
  }'
```

Sau đây là các giá trị được hỗ trợ cho `agent_config.model`:

| Mô hình | Giá trị tính bằng `agent_config.model` | Mô tả |
| --- | --- | --- |
| **Gemini 3.8 Flash** (mặc định) | `gemini-3.8-flash` | Mô hình cân bằng mặc định để suy luận, lập trình và sử dụng công cụ. |
| **Gemini 4 Argon** | `gemini-4-argon` | Mô hình suy luận tiên phong cho kỹ thuật phần mềm phức tạp, giải quyết vấn đề chuyên sâu và các tác vụ có thời hạn dài. |
| **Gemini 3.6 Flash** | `gemini-3.6-flash` | Mô hình Flash cân bằng cho các quy trình làm việc chung của tác nhân. |
| **Gemini 3.5 Flash-Lite** | `gemini-3.5-flash-lite` | Mô hình gọn nhẹ được tối ưu hoá cho các tác vụ có độ trễ thấp và nhạy cảm về chi phí. |

Khi tạo một tác nhân được quản lý bằng `agents.create`, bạn sẽ định cấu hình mô hình theo cách giống hệt bằng cách truyền `base_agent` và `agent_config`. Xin lưu ý rằng bạn không thể ghi đè mô hình tại thời điểm tương tác cho một tác nhân được quản lý được tạo bằng `agents.create`. Mô hình bị khoá theo những gì được thiết lập khi tác nhân được tạo. Điều này đảm bảo hành vi gọi công cụ có thể dự đoán, gỡ lỗi nhất quán và tuân thủ các ranh giới bảo mật.

## Tuỳ chỉnh tác nhân

Bạn có thể mở rộng tác nhân Antigravity bằng cách tuỳ chỉnh hướng dẫn, công cụ và môi trường của tác nhân đó. Tác nhân này hỗ trợ phương pháp tuỳ chỉnh gốc của hệ thống tệp: bạn có thể gắn các tệp như `AGENTS.md` cho hướng dẫn và kỹ năng trong `.agents/skills/` trực tiếp vào hộp cát hoặc truyền cấu hình cùng dòng tại thời điểm tương tác. Bạn có thể lặp lại cấu hình của mình ngay trong dòng rồi lưu cấu hình đó dưới dạng tác nhân được quản lý khi bạn đã sẵn sàng.

Để biết thông tin chi tiết về cách tạo các tác nhân tuỳ chỉnh, hãy xem bài viết [Tạo tác nhân được quản lý](https://ai.google.dev/gemini-api/docs/custom-agents?hl=vi).

## Thực thi trong nền

Các nhiệm vụ của tác nhân liên quan đến suy luận đa bước, thực thi mã hoặc thao tác với tệp có thể mất vài phút để hoàn thành. Sử dụng `background=True` để chạy lượt tương tác không đồng bộ. API này trả về ngay lập tức kèm theo một mã nhận dạng hoạt động tương tác mà bạn thăm dò ý kiến cho đến khi trạng thái là `completed` hoặc `failed`.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the interaction in the background
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();

// 1. Start the interaction in the background
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Run a complex analysis on the repository."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .background(true)
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Interaction started in background: " + interaction.id().orElse(""));

// 2. Poll for completion
while (interaction.status().orElse(null) == InteractionStatus.IN_PROGRESS) {
    Thread.sleep(5000);
    interaction = client.interactions.get(new GetInteractionByIdRequest(interaction.id().orElse(""))).interaction().get();
}

if (interaction.status().orElse(null) == InteractionStatus.COMPLETED) {
    System.out.println(interaction.outputText().orElse(""));
} else {
    System.out.println("Finished with status: " + interaction.status().orElse(null));
}
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

    // 1. Start the interaction in the background
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Run a complex analysis on the repository."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Background:  genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    fmt.Printf("Interaction started in background: %s\n", *interaction.ID)

    // 2. Poll for completion
    for interaction.Status == interactions.InteractionStatusInProgress {
        time.Sleep(5 * time.Second)
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = getRes.Interaction
    }

    if interaction.Status == interactions.InteractionStatusCompleted {
        if interaction.OutputText != nil {
            fmt.Println(*interaction.OutputText)
        }
    } else {
        fmt.Printf("Finished with status: %s\n", interaction.Status)
    }
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
      "agent": "antigravity-preview-09-2026",
      "input": "Run a complex analysis on the repository.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll for results (repeat until status is "completed")
curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

Chế độ thực thi trong nền yêu cầu `store=True` (đây là chế độ mặc định). Để biết thông tin cập nhật về tiến trình theo thời gian thực trong quá trình thực thi ở chế độ nền, hãy xem phần [Tương tác ở chế độ nền khi truyền trực tuyến](https://ai.google.dev/gemini-api/docs/background-execution?hl=vi#streaming-pattern).

Bạn có thể huỷ một hoạt động tương tác đang chạy ở chế độ nền bằng phương thức `cancel`.

### Python

```
client.interactions.cancel(id="INTERACTION_ID")
```

### JavaScript

```
await client.interactions.cancel("INTERACTION_ID");
```

### Java

```
import com.google.genai.Client;

Client client = new Client();
client.interactions.cancel("INTERACTION_ID");
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Interactions.Cancel(ctx, operations.CancelInteractionByIDRequest{
        ID: "INTERACTION_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID:cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

**Đa lượt với tính năng thực thi trong nền**

Khi một lượt tương tác trong nền liên quan đến các công cụ có trạng thái (như thực thi mã trong hộp cát), hãy sử dụng `environment_id` từ lượt tương tác đã hoàn tất để tiếp tục trong cùng một môi trường. Điều này đảm bảo rằng tác nhân sẽ tiếp tục từ nơi đã dừng lại với tất cả các tệp và trạng thái còn nguyên vẹn.

### Python

```
import time
from google import genai

client = genai.Client()

# First turn: run a task in the background
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Clone https://github.com/google/generative-ai-python and run its tests.",
    environment="remote",
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Second turn: continue in the same environment
followup = client.interactions.create(
    agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();

// First turn: run a task in the background
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Clone https://github.com/google/generative-ai-python and run its tests."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .background(true)
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

while (interaction.status().orElse(null) == InteractionStatus.IN_PROGRESS) {
    Thread.sleep(5000);
    interaction = client.interactions.get(new GetInteractionByIdRequest(interaction.id().orElse(""))).interaction().get();
}

// Second turn: continue in the same environment
CreateAgentInteraction followupParams = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Fix any failing tests and re-run them."))
    .previousInteractionId(interaction.id().orElse(""))
    .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
    .background(true)
    .build();

Interaction followup = client.interactions.create(CreateInteractionRequestBody.of(followupParams)).interaction().get();

while (followup.status().orElse(null) == InteractionStatus.IN_PROGRESS) {
    Thread.sleep(5000);
    followup = client.interactions.get(new GetInteractionByIdRequest(followup.id().orElse(""))).interaction().get();
}

System.out.println(followup.outputText().orElse(""));
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

    // First turn: run a task in the background
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Clone https://github.com/google/generative-ai-python and run its tests."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Background:  genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    for interaction.Status == interactions.InteractionStatusInProgress {
        time.Sleep(5 * time.Second)
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = getRes.Interaction
    }

    // Second turn: continue in the same environment
    followupRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Fix any failing tests and re-run them."),
            PreviousInteractionID: interaction.ID,
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
            Background:            genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    followup := followupRes.Interaction
    for followup.Status == interactions.InteractionStatusInProgress {
        time.Sleep(5 * time.Second)
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *followup.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        followup = getRes.Interaction
    }

    if followup.OutputText != nil {
        fmt.Println(*followup.OutputText)
    }
}
```

### REST

```
# 1. Start first interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-09-2026",
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
      \"agent\": \"antigravity-preview-09-2026\",
      \"input\": \"Fix any failing tests and re-run them.\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"background\": true
  }"
```

## Môi trường

Mỗi lệnh gọi sẽ tạo hoặc dùng lại một hộp cát Linux. Tham số `environment` có 3 dạng:

| Biểu mẫu | Mô tả |
| --- | --- |
| `"remote"` | Cung cấp một hộp cát mới với các chế độ cài đặt mặc định. |
| `"env_abc123"` | Sử dụng lại một môi trường hiện có theo mã nhận dạng, giữ nguyên tất cả tệp và trạng thái. |
| `{...}` | `EnvironmentConfig` đầy đủ với các nguồn và quy tắc mạng tuỳ chỉnh. |

Hãy xem phần [Môi trường](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi) để biết thông tin chi tiết về các nguồn (Git, GCS, nội tuyến), mạng, vòng đời và hạn mức tài nguyên.

## Điều kiện kích hoạt

Trình kích hoạt cho phép bạn lên lịch để tác nhân tự động chạy theo lịch biểu cron. Điều kiện kích hoạt liên kết một tác nhân, môi trường, lời nhắc và lịch biểu thành một tài nguyên liên tục sẽ kích hoạt mà không cần can thiệp thủ công. Mỗi lần thực thi sẽ sử dụng lại cùng một môi trường, vì vậy, các tệp được tạo trong một lần chạy sẽ vẫn tồn tại và hiển thị cho lần chạy tiếp theo.

### Tạo trình kích hoạt

Tạo một điều kiện kích hoạt bằng cách chỉ định lịch biểu cron, múi giờ và cấu hình tương tác. Trình kích hoạt bắt đầu ở trạng thái `active` và sẽ kích hoạt vào thời gian cron trùng khớp tiếp theo. Lưu `id` được trả về để quản lý điều kiện kích hoạt trong các lệnh gọi tiếp theo.

Vì điều kiện kích hoạt chạy tự động theo lịch, hãy tham chiếu đến [thông tin xác thực](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=vi) được lưu trữ thay vì mã thông báo cùng dòng. Proxy truyền dữ liệu ra sẽ phân giải bí mật này trong mỗi lần chạy và bạn sẽ xoay vòng bí mật mà không cần chạm vào trình kích hoạt. Các quy tắc `transform` cùng dòng cũng hoạt động tại đây, bạn chỉ cần cập nhật điều kiện kích hoạt bất cứ khi nào giá trị thay đổi.

### Python

```
from google import genai

client = genai.Client()

trigger = client.triggers.create(
    schedule="0 9 * * *",
    time_zone="America/Argentina/Buenos_Aires",
    display_name="issue-solver",
    interaction={
        "agent": "antigravity-preview-09-2026",
        "input": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        "environment": {
            "type": "remote",
            "network": {
                "allowlist": [
                    {
                        "domain": "api.github.com",
                        "credential": "github-production",
                    },
                    {"domain": "github.com"},
                ]
            },
        },
    },
)

print(f"Trigger created: {trigger.id}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const trigger = await client.triggers.create({
    schedule: "0 9 * * *",
    time_zone: "America/Argentina/Buenos_Aires",
    display_name: "issue-solver",
    interaction: {
        agent: "antigravity-preview-09-2026",
        input: [{
            type: "text",
            text: "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        }],
        environment: {
            type: "remote",
            network: {
                allowlist: [
                    {
                        domain: "api.github.com",
                        credential: "github-production",
                    },
                    { domain: "github.com" },
                ],
            },
        },
    },
});

console.log(`Trigger created: ${trigger.id}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.Trigger;
import com.google.genai.gaos.models.triggers.TriggerCreateParams;
import java.util.List;
import java.util.Map;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

Environment env = Environment.builder()
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    )))
                    .build(),
                AllowlistEntry.builder()
                    .domain("github.com")
                    .build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction interactionTemplate = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

TriggerCreateParams params = TriggerCreateParams.builder()
    .schedule("0 9 * * *")
    .timeZone("America/Argentina/Buenos_Aires")
    .displayName("issue-solver")
    .interaction(interactionTemplate)
    .build();

Trigger trigger = client.triggers().create(params).trigger().get();
System.out.println("Trigger created: " + trigger.id().orElse(""));
System.out.println("Next run: " + trigger.nextRunTime().orElse(null));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
    "google.golang.org/genai/interactions/models/triggers"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    env := interactions.Environment{
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "api.github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    })),
                },
                {
                    Domain: "github.com",
                },
            })),
        })),
    }

    interactionTemplate := interactions.CreateAgentInteraction{
        Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
        Input:       interactions.NewInteractionsInput("Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."),
        Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
    }

    res, err := sdk.Triggers.Create(ctx, operations.CreateTriggerRequest{
        Body: triggers.TriggerCreateParams{
            Schedule:    "0 9 * * *",
            TimeZone:    "America/Argentina/Buenos_Aires",
            DisplayName: genai.Ptr("issue-solver"),
            Interaction: interactionTemplate,
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    trigger := res.Trigger
    fmt.Printf("Trigger created: %s\n", trigger.ID)
    fmt.Printf("Next run: %v\n", trigger.NextRunTime)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "schedule": "0 9 * * *",
      "time_zone": "America/Argentina/Buenos_Aires",
      "display_name": "issue-solver",
      "interaction": {
          "agent": "antigravity-preview-09-2026",
          "input": [{"type": "text", "text": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled accepted, skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."}],
          "environment": {
              "type": "remote",
              "network": {
                  "allowlist": [
                      {
                          "domain": "api.github.com",
                          "credential": "github-production"
                      },
                      {"domain": "github.com"}
                  ]
              }
          }
      }
  }'
```

Yêu cầu `CreateTrigger` chấp nhận các trường sau:

| Trường | Loại | Bắt buộc | Mô tả |
| --- | --- | --- | --- |
| `schedule` | chuỗi | Có | Biểu thức cron (ví dụ: `0 * * * *` cho hằng giờ, `0 9 * * 1-5` cho các buổi sáng trong tuần). |
| `time_zone` | chuỗi | Có | Múi giờ IANA (ví dụ: `UTC`, `America/Argentina/Buenos_Aires`). |
| `display_name` | chuỗi | Không | Tên dễ đọc của điều kiện kích hoạt. |
| `max_consecutive_failures` | số nguyên | Không | Số lần không thành công tối đa trước khi trình kích hoạt tự động tạm dừng. Mặc định: 5. |
| `execution_timeout_seconds` | số nguyên | Không | Thời gian chờ cho mỗi lần thực thi (tính bằng giây). Mặc định: 600. |
| `interaction` | đối tượng | Có | `CreateInteractionRequest` xác định tác nhân, dữ liệu đầu vào, công cụ và môi trường. |

Phản hồi bao gồm các trường khoá sau:

| Trường | Loại | Mô tả |
| --- | --- | --- |
| `id` | chuỗi | Giá trị nhận dạng riêng biệt của điều kiện kích hoạt. Hãy sử dụng mã này trong tất cả các thao tác tiếp theo. |
| `status` | chuỗi | Trạng thái hiện tại: `active`, `paused` hoặc `disabled`. |
| `next_run_time` | chuỗi | Dấu thời gian ISO 8601 của lần thực thi theo lịch tiếp theo. |
| `consecutive_failure_count` | số nguyên | Số lần thực thi không thành công liên tiếp kể từ lần thành công gần đây nhất. |

### Liệt kê các điều kiện kích hoạt

Truy xuất tất cả các điều kiện kích hoạt được liên kết với dự án của bạn.

### Python

```
triggers = client.triggers.list()
for trigger in triggers.triggers:
    print(f"{trigger.id}: {trigger.display_name} ({trigger.status})")
```

### JavaScript

```
const triggers = await client.triggers.list();
for (const trigger of triggers.triggers) {
    console.log(`${trigger.id}: ${trigger.display_name} (${trigger.status})`);
}
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.Trigger;
import java.util.List;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

List<Trigger> triggers = client.triggers().listDirect().listTriggersResponse().get().triggers().orElse(List.of());
for (Trigger trigger : triggers) {
    System.out.println(trigger.id().orElse("") + ": " + trigger.displayName().orElse("") + " (" + trigger.status().orElse(null) + ")");
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    res, err := sdk.Triggers.List(ctx, operations.ListTriggersRequest{})
    if err != nil {
        log.Fatal(err)
    }

    if res.ListTriggersResponse != nil {
        for _, trigger := range res.ListTriggersResponse.Triggers {
            fmt.Printf("%s: %s (%v)\n", trigger.ID, *trigger.GetDisplayName(), trigger.Status)
        }
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Nhận điều kiện kích hoạt

Tìm nạp cấu hình đầy đủ và trạng thái hiện tại của một trình kích hoạt.

### Python

```
trigger = client.triggers.get(id="TRIGGER_ID")
print(f"Schedule: {trigger.schedule}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
const trigger = await client.triggers.get("TRIGGER_ID");
console.log(`Schedule: ${trigger.schedule}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.Trigger;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

Trigger trigger = client.triggers().get("TRIGGER_ID").trigger().get();
System.out.println("Schedule: " + trigger.schedule().orElse(""));
System.out.println("Next run: " + trigger.nextRunTime().orElse(null));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    res, err := sdk.Triggers.Get(ctx, operations.GetTriggerRequest{
        ID: "TRIGGER_ID",
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Schedule: %s\n", res.Trigger.Schedule)
    fmt.Printf("Next run: %v\n", res.Trigger.NextRunTime)
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Tạm dừng và tiếp tục

Bạn có thể tạm dừng một điều kiện kích hoạt để dừng các lần thực thi theo lịch và tiếp tục điều kiện kích hoạt đó để kích hoạt lại lịch biểu. Việc tạm dừng không ảnh hưởng đến các lần thực thi thủ công.

### Python

```
# Pause
client.triggers.update(id="TRIGGER_ID", status="paused")

# Resume
client.triggers.update(id="TRIGGER_ID", status="active")
```

### JavaScript

```
// Pause
await client.triggers.update("TRIGGER_ID", { status: "paused" });

// Resume
await client.triggers.update("TRIGGER_ID", { status: "active" });
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.TriggerUpdate;
import com.google.genai.gaos.models.triggers.TriggerUpdateStatus;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

// Pause
client.triggers().update("TRIGGER_ID", TriggerUpdate.builder().status(TriggerUpdateStatus.PAUSED).build());

// Resume
client.triggers().update("TRIGGER_ID", TriggerUpdate.builder().status(TriggerUpdateStatus.ACTIVE).build());
```

### Go

```
package main

import (
    "context"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
    "google.golang.org/genai/interactions/models/triggers"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    // Pause
    _, err := sdk.Triggers.Update(ctx, operations.UpdateTriggerRequest{
        ID: "TRIGGER_ID",
        Body: triggers.TriggerUpdate{
            Status: triggers.TriggerUpdateStatusPaused.ToPointer(),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    // Resume
    _, err = sdk.Triggers.Update(ctx, operations.UpdateTriggerRequest{
        ID: "TRIGGER_ID",
        Body: triggers.TriggerUpdate{
            Status: triggers.TriggerUpdateStatusActive.ToPointer(),
        },
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
# Pause
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "paused"}'

# Resume
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "active"}'
```

### Xoá điều kiện kích hoạt

Xoá vĩnh viễn một điều kiện kích hoạt. Nhật ký thực thi trước đây sẽ không bị xoá.

### Python

```
client.triggers.delete(id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.delete("TRIGGER_ID");
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

client.triggers().delete("TRIGGER_ID");
```

### Go

```
package main

import (
    "context"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    _, err := sdk.Triggers.Delete(ctx, operations.DeleteTriggerRequest{
        ID: "TRIGGER_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Chạy một điều kiện kích hoạt ngay lập tức

Kích hoạt một điều kiện kích hoạt theo yêu cầu mà không cần đợi thời gian lên lịch tiếp theo. Điều này vẫn hoạt động ngay cả khi trình kích hoạt bị tạm dừng.

### Python

```
client.triggers.run(trigger_id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.run("TRIGGER_ID");
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

client.triggers().run("TRIGGER_ID");
```

### Go

```
package main

import (
    "context"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    _, err := sdk.Triggers.Run(ctx, operations.RunTriggerRequest{
        TriggerID: "TRIGGER_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Liệt kê các lần thực thi

Xem nhật ký thực thi của một điều kiện kích hoạt. Mỗi lần thực thi bao gồm một `status`, dấu thời gian, một `interaction_id` mà bạn có thể dùng để tìm nạp toàn bộ kết quả tương tác và một `environment_id` xác nhận rằng tất cả các lần chạy đều có chung một hộp cát.

### Python

```
executions = client.triggers.list_executions(trigger_id="TRIGGER_ID")
for ex in executions.trigger_executions:
    print(f"{ex.id}: {ex.status} ({ex.start_time} - {ex.end_time})")

# Fetch the full interaction for an execution
interaction = client.interactions.get(id=ex.interaction_id)
print(interaction.output_text)
```

### JavaScript

```
const executions = await client.triggers.listExecutions("TRIGGER_ID");
for (const ex of executions.trigger_executions) {
    console.log(`${ex.id}: ${ex.status} (${ex.start_time} - ${ex.end_time})`);
}

// Fetch the full interaction for an execution
const interaction = await client.interactions.get(ex.interaction_id);
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.TriggerExecution;
import java.util.List;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

List<TriggerExecution> executions = client.triggers().listExecutions("TRIGGER_ID")
    .listTriggerExecutionsResponse().get()
    .triggerExecutions().orElse(List.of());

for (TriggerExecution ex : executions) {
    System.out.println(ex.id().orElse("") + ": " + ex.status().orElse(null)
        + " (" + ex.startTime().orElse(null) + " - " + ex.endTime().orElse(null) + ")");

    // Fetch the full interaction for an execution
    if (ex.interactionId().isPresent()) {
        Interaction interaction = client.interactions().get(new GetInteractionByIdRequest(ex.interactionId().get())).interaction().get();
        System.out.println(interaction.outputText().orElse(""));
    }
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    res, err := sdk.Triggers.ListExecutions(ctx, operations.ListTriggerExecutionsRequest{
        TriggerID: "TRIGGER_ID",
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.ListTriggerExecutionsResponse != nil {
        for _, ex := range res.ListTriggerExecutionsResponse.TriggerExecutions {
            fmt.Printf("%s: %v (%v - %v)\n", ex.ID, ex.Status, ex.StartTime, ex.EndTime)

            // Fetch the full interaction for an execution
            if ex.InteractionID != nil {
                intRes, err := sdk.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
                    ID: *ex.InteractionID,
                })
                if err != nil {
                    log.Fatal(err)
                }
                if intRes.Interaction.OutputText != nil {
                    fmt.Println(*intRes.Interaction.OutputText)
                }
            }
        }
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Tình trạng còn hàng và giá

Tác nhân Antigravity hiện có trong bản xem trước thông qua
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) trong Google AI Studio
và Gemini API cho cả dự án cấp miễn phí và cấp có tính phí.

Giá cả được tính theo [mô hình trả tiền theo mức dùng](https://ai.google.dev/gemini-api/docs/pricing?hl=vi#pricing-for-agents) dựa trên số token của mô hình Gemini cơ bản và các công cụ mà tác nhân sử dụng. Không giống như yêu cầu trò chuyện tiêu chuẩn tạo ra một đầu ra duy nhất, hoạt động tương tác Antigravity là một quy trình làm việc dựa trên tác nhân. Một yêu cầu duy nhất sẽ kích hoạt một vòng lặp tự động gồm suy luận, thực thi công cụ, chạy mã và quản lý tệp. Các dự án thuộc gói miễn phí có giới hạn tốc độ và hạn mức sử dụng miễn phí.

Các lượt tương tác với Antigravity chạy các vòng lặp tự động nhiều lượt và có thể tiêu tốn
nhiều mã thông báo. Đặt [chế độ kiểm soát ngân sách](#budget-controls) cho yêu cầu của bạn để giới hạn mức sử dụng mã thông báo. Bạn cũng có thể theo dõi tiến trình theo thời gian thực bằng tính năng [truyền trực tuyến SSE](https://ai.google.dev/gemini-api/docs/streaming?hl=vi) hoặc huỷ các yêu cầu đang chạy.

### Chế độ kiểm soát ngân sách

Ngoài [lựa chọn mô hình](#model-selection), hãy đặt `max_total_tokens` bên trong `agent_config` (với `"type": "antigravity"`) để giới hạn tổng số mã thông báo (đầu vào + đầu ra + suy nghĩ) mà một lượt tương tác có thể sử dụng.
Mã thông báo được lưu vào bộ nhớ đệm không được tính vào giới hạn này. Khi tác nhân đạt đến giới hạn, hoạt động tương tác sẽ dừng và trả về `status: "incomplete"`. Hạn mức này là mức tối đa có thể:
mức sử dụng thực tế có thể vượt quá một chút tuỳ thuộc vào thời điểm tác nhân kiểm tra ngân sách
giữa các bước.

Đặt ngân sách cho yêu cầu tương tác trong `agent_config` cùng với `agent` và `input`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    },
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": "/workspace/data.csv",
                "content": "id,name,value\n1,alpha,100\n2,beta,200\n",
            }
        ],
    }
)
print(f"Status: {interaction.status}")  # "incomplete" if budget was hit
print(f"Tokens used: {interaction.usage.total_tokens}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config: {
        type: "antigravity",
        max_total_tokens: "50000"
    },
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: "/workspace/data.csv",
                content: "id,name,value\n1,alpha,100\n2,beta,200\n",
            },
        ],
    },
});
console.log(`Status: ${interaction.status}`);
console.log(`Tokens used: ${interaction.usage?.total_tokens}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.AntigravityAgentConfig;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target("/workspace/data.csv")
            .content("id,name,value\n1,alpha,100\n2,beta,200\n")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the dataset in /workspace/data.csv and generate a summary report."))
    .agentConfig(
        AntigravityAgentConfig.builder()
            .maxTotalTokens("50000")
            .build()
    )
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Status: " + interaction.status().orElse(null)); // "incomplete" if budget was hit
interaction.usage().ifPresent(usage -> System.out.println("Tokens used: " + usage.totalTokens().orElse(0)));
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

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("/workspace/data.csv"),
                Content: genai.Ptr("id,name,value\n1,alpha,100\n2,beta,200\n"),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Analyze the dataset in /workspace/data.csv and generate a summary report."),
            AgentConfig: genai.Ptr(interactions.NewCreateAgentInteractionAgentConfig(interactions.AntigravityAgentConfig{
                MaxTotalTokens: genai.Ptr(int64(50000)),
            })),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    fmt.Printf("Status: %s\n", interaction.Status) // "incomplete" if budget was hit
    if interaction.Usage != nil && interaction.Usage.TotalTokens != nil {
        fmt.Printf("Tokens used: %d\n", *interaction.Usage.TotalTokens)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    },
    "environment": {
      "type": "remote",
      "sources": [
        {
          "type": "inline",
          "target": "/workspace/data.csv",
          "content": "id,name,value\n1,alpha,100\n2,beta,200\n"
        }
      ]
    }
  }'
```

#### Tiếp tục một lượt tương tác chưa hoàn thành

Khi một lượt tương tác trả về `status: "incomplete"`, công việc và bối cảnh của tác nhân sẽ được giữ nguyên. Gửi một lượt tương tác mới tham chiếu đến lượt tương tác ban đầu `id` và
`environment_id` để tiếp tục từ nơi đã dừng lại. Lượt tương tác mới sẽ có
ngân sách `max_total_tokens` riêng.

### Python

```
# Continue from where the agent stopped
continuation = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="continue",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    }
)
print(f"Status: {continuation.status}")
```

### JavaScript

```
const continuation = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "continue",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    agent_config: {
        type: "antigravity",
        max_total_tokens: "50000"
    }
});
console.log(`Status: ${continuation.status}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.AntigravityAgentConfig;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();
String interactionId = "INTERACTION_ID";
String environmentId = "ENVIRONMENT_ID";

// Continue from where the agent stopped
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("continue"))
    .previousInteractionId(interactionId)
    .environment(CreateAgentInteractionEnvironment.of(environmentId))
    .agentConfig(
        AntigravityAgentConfig.builder()
            .maxTotalTokens("50000")
            .build()
    )
    .build();

Interaction continuation = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Status: " + continuation.status().orElse(null));
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

    interactionID := "INTERACTION_ID"
    environmentID := "ENVIRONMENT_ID"

    // Continue from where the agent stopped
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("continue"),
            PreviousInteractionID: genai.Ptr(interactionID),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(environmentID)),
            AgentConfig: genai.Ptr(interactions.NewCreateAgentInteractionAgentConfig(interactions.AntigravityAgentConfig{
                MaxTotalTokens: genai.Ptr(int64(50000)),
            })),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Status: %s\n", res.Interaction.Status)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-09-2026",
    "input": "continue",
    "previous_interaction_id": "INTERACTION_ID",
    "environment": "ENVIRONMENT_ID",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    }
  }'
```

### Chi phí ước tính

Chi phí sẽ khác nhau tuỳ thuộc vào độ phức tạp của nhiệm vụ. Tác nhân tự động xác định số lượng lệnh gọi công cụ, lượt thực thi mã và thao tác với tệp cần thiết. Các số liệu ước tính sau đây dựa trên số lần chạy.

| Danh mục việc cần làm | Mã thông báo nhập | Mã thông báo xuất | Chi phí thông thường |
| --- | --- | --- | --- |
| **Nghiên cứu và tổng hợp thông tin** | 100.000 – 500.000 | 10.000 – 40.000 | 0,3 – 1 USD |
| **Tạo tài liệu và nội dung** | 100.000 – 500.000 | 15.000 – 50.000 | 0,30 – 1,30 USD |
| **Thiết kế quy trình và hệ thống** | 100 nghìn – 400 nghìn | 10 nghìn – 30 nghìn | $0,25 –$0,8 |
| **Xử lý và phân tích dữ liệu** | 300.000 – 3.000.000 | 30.000 – 150.000 | 0,7 – 3,25 USD |

Thông thường, 50–70% mã thông báo đầu vào được lưu vào bộ nhớ đệm. Quy trình làm việc phức tạp của tác nhân với nhiều lệnh gọi công cụ có thể tích luỹ 3 – 5 triệu mã thông báo trong một lượt tương tác, với chi phí lên đến ~5 USD.

**Điện toán môi trường** (CPU, bộ nhớ, thực thi hộp cát) **không được tính phí** trong thời gian xem trước.

## Các điểm hạn chế

- **Trạng thái của bản xem trước:** Tác nhân Antigravity và Interactions API. Các tính năng và giản đồ có thể thay đổi.
- **Cấu hình tạo không được hỗ trợ:** Các tham số sau không được hỗ trợ và trả về lỗi 400: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Kết quả có cấu trúc:** Tác nhân Antigravity không hỗ trợ kết quả có cấu trúc.
- **Công cụ không dùng được:** `file_search`, `computer_use` và `google_maps` chưa được hỗ trợ.
- **Các hạn chế của MCP từ xa:** Không hỗ trợ truyền tải Sự kiện do máy chủ gửi (SSE) (sử dụng HTTP có thể truyền trực tuyến). Ngoài ra, máy chủ `name` phải hoàn toàn là chữ thường và chữ và số (việc sử dụng chữ hoa sẽ gây ra lỗi chung `400 Bad Request`).
- **Công cụ hệ thống tệp:** Hiện không có công cụ hệ thống tệp. Đây là một phần của `environment`.
- **Yêu cầu của cửa hàng:** Việc thực thi tác nhân bằng `background=True` yêu cầu `store=True`.
- **Chỉ gọi hàm có trạng thái:** Tính năng gọi hàm chỉ được hỗ trợ ở chế độ có trạng thái. Bạn phải sử dụng `previous_interaction_id` để tiếp tục lượt; hệ thống không hỗ trợ việc tạo lại nhật ký theo cách thủ công (chế độ không lưu trạng thái).
- **Các loại dữ liệu đa phương thức không được hỗ trợ.** Hiện không hỗ trợ dữ liệu đầu vào dạng âm thanh, video và tài liệu. Chỉ cho phép văn bản và hình ảnh.

## Bước tiếp theo

- [Bắt đầu nhanh](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi): cuộc trò chuyện nhiều lượt và truyền trực tuyến.
- [Tạo tác nhân tuỳ chỉnh](https://ai.google.dev/gemini-api/docs/custom-agents?hl=vi): chỉ dẫn tuỳ chỉnh, kỹ năng và lưu tác nhân.
- [Môi trường](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi): cấu hình hộp cát, nguồn, kết nối mạng.
- [Hook](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=vi): thực thi các cổng bảo mật và xác thực tác dụng phụ bên trong hộp cát.
- [Tác nhân Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi): các nhiệm vụ nghiên cứu dài.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi): API cơ bản.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-16 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-16 UTC."],[],[]]
