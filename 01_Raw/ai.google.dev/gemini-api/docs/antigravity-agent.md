---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id
fetched_at: 2026-10-12T07:10:58.988321+00:00
title: "Agen Antigravity \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Agen Antigravity

Agen Antigravity adalah agen terkelola tujuan umum di Gemini API. Satu panggilan API memberi Anda agen yang dapat melakukan penalaran, mengeksekusi kode, mengelola file, dan menjelajahi web di dalam sandbox Linux Anda yang aman, yang dihosting oleh Google.

Plugin ini dibuat dengan Gemini 3.8 Flash dan menggunakan harness yang sama dengan Antigravity IDE. Anda dapat mengonfigurasi model Gemini yang mendasarinya menggunakan `agent_config`. Tersedia melalui [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) dan [Google AI Studio](https://aistudio.google.com?hl=id).

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

## Kemampuan

Setiap panggilan dapat menyediakan sandbox Linux dan memulai loop penggunaan alat. Agen merencanakan, bertindak, mengamati hasil, dan mengulangi hingga tugas selesai.

- **Eksekusi kode:** Jalankan perintah Bash, Python, dan Node.js. Menginstal paket, menjalankan pengujian, membangun aplikasi.
- **Pengelolaan file:** Membaca, menulis, mengedit, menelusuri, dan mencantumkan file di sandbox. File tetap ada di seluruh interaksi.
- **Akses web:** Google Penelusuran dan pengambilan URL untuk data.
- **Pemadatan konteks:** Pemadatan konteks otomatis (dipicu pada ~135 ribu token) untuk mendukung sesi multi-turn yang berjalan lama tanpa kehilangan konteks atau mencapai batas token.

Lihat [Panduan memulai](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=id) untuk penggunaan dan streaming multi-giliran.

## Alat yang didukung

Secara default, agen memiliki akses ke `code_execution`, `google_search`, dan `url_context`. Alat sistem file diaktifkan secara otomatis saat Anda menentukan parameter `environment`. Anda juga dapat menentukan **fungsi kustom** untuk menghubungkan agen ke API dan alat Anda sendiri. Anda hanya perlu menentukan parameter `tools` saat menyesuaikan atau membatasi set default, atau saat menambahkan fungsi kustom.

| Alat | Nilai jenis | Deskripsi |
| --- | --- | --- |
| Eksekusi Kode | `code_execution` | Jalankan perintah shell (bash, Python, Node) dengan pengambilan stdout/stderr. |
| Google Penelusuran | `google_search` | Menelusuri web publik. |
| Konteks URL | `url_context` | Mengambil dan membaca halaman web. |
| Filesystem | *(diaktifkan melalui `environment`)* | Membaca, menulis, mengedit, menelusuri, dan mencantumkan file di sandbox. Sistem akan mengaktifkan alat ini secara otomatis saat Anda menyetel `environment`. |
| Fungsi Kustom | `function` | Tentukan fungsi kustom yang dapat diminta agen untuk dieksekusi. Lihat [Pemanggilan fungsi](#function-calling). |
| Server MCP Jarak Jauh | `mcp_server` | Mendaftarkan server Model Context Protocol (MCP) eksternal sebagai alat. Lihat [server MCP](#mcp-servers). |

Anda dapat mencegat dan memvalidasi eksekusi alat `code_execution` dan `filesystem` langsung di dalam sandbox jarak jauh menggunakan [Hook](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=id) sinkron.

Untuk membatasi agen ke alat tertentu, teruskan hanya alat yang Anda butuhkan:

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

## Input Multimodal

Agen Antigravity mendukung input multimodal. Saat ini, hanya input `text` dan `image` yang didukung. Gambar harus disediakan sebagai string inline berenkode base64 (`data`).

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

## Panggilan fungsi

Panggilan fungsi memungkinkan Anda menghubungkan agen Antigravity ke API dan database eksternal dengan menentukan alat kustom yang dapat dipanggil agen. Untuk mengetahui konsep umumnya, lihat [Panggilan fungsi dengan Gemini API](https://ai.google.dev/gemini-api/docs/function-calling?hl=id).

Contoh berikut menunjukkan interaksi 2 putaran. Agen pertama-tama meminta panggilan fungsi `get_weather` kustom, dan klien mengeksekusinya serta menampilkan hasilnya pada giliran kedua.

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
  agent: "antigravity-preview-09-2026",
  input: "What is the weather in Tokyo?",
  environment: "remote",
  tools: [
    { type: "code_execution" },
    get_weather_tool,
  ],
}, { timeout: 300000 });

if (interaction.status === "requires_action") {
  // Find function calls that do not have a matching function result.
  // Filesystem tools (like write_to_file) are also represented as function calls
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

## Server MCP

Anda dapat menghubungkan agen Antigravity ke alat eksternal dengan mendaftarkan server Model Context Protocol (MCP) jarak jauh. Agen mendukung server MCP jarak jauh melalui HTTP yang dapat di-streaming.

Saat mendaftarkan server MCP, Anda harus menentukan kolom berikut dalam array `tools`:

| Kolom | Jenis | Wajib diisi | Deskripsi |
| --- | --- | --- | --- |
| `type` | string | Ya | Harus berupa `"mcp_server"`. |
| `name` | string | Ya | ID unik untuk server. Harus huruf kecil dan alfanumerik (cocok dengan `^[a-z0-9_-]+$`). |
| `url` | string | Ya | URL endpoint server MCP jarak jauh. |
| `headers` | objek | Tidak | Header kustom (misalnya, autentikasi) yang dikirim dengan permintaan. |
| `allowed_tools` | array | Tidak | Daftar nama alat yang diizinkan untuk dieksekusi. Jika tidak disertakan, semua alat diizinkan. |

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

## Pemilihan model

Untuk `antigravity-preview-09-2026`, model defaultnya adalah **Gemini 3.8 Flash** (`gemini-3.8-flash`). Jika Anda tidak menyertakan `agent_config`, agen akan menggunakan `gemini-3.8-flash` secara default.

Anda dapat mengonfigurasi model Gemini yang mendasarinya menggunakan `agent_config` untuk mengoptimalkan kecepatan, biaya, atau kemampuan penalaran.

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
        "model": "gemini-3.5-flash-lite",
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
        model: "gemini-3.5-flash-lite",
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
            .model("gemini-3.5-flash-lite")
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
                Model: genai.Ptr("gemini-3.5-flash-lite"),
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
          "model": "gemini-3.5-flash-lite"
      }
  }'
```

Nilai yang didukung untuk `agent_config.model` adalah:

| Model | Nilai dalam `agent_config.model` | Deskripsi |
| --- | --- | --- |
| **Gemini 3.8 Flash** (default) | `gemini-3.8-flash` | Model seimbang default untuk penalaran, coding, dan penggunaan alat. |
| **Gemini 3.6 Flash** | `gemini-3.6-flash` | Model Flash seimbang untuk Agentic Workflows umum. |
| **Gemini 3.5 Flash-Lite** | `gemini-3.5-flash-lite` | Model ringan yang dioptimalkan untuk tugas-tugas yang sensitif terhadap biaya dan latensi rendah. |

Saat membuat agen terkelola dengan `agents.create`, Anda mengonfigurasi model dengan cara yang sama persis dengan meneruskan `base_agent` dan `agent_config`. Perhatikan bahwa Anda tidak dapat mengganti model pada waktu interaksi untuk agen terkelola yang dibuat dengan `agents.create`. Model dikunci ke setelan yang ditetapkan saat agen dibuat. Hal ini memastikan perilaku panggilan alat yang dapat diprediksi, proses pen-debug-an yang konsisten, dan kepatuhan terhadap batas keamanan.

## Menyesuaikan agen

Anda dapat memperluas agen Antigravity dengan menyesuaikan petunjuk, alat, dan lingkungannya. Agen mendukung pendekatan penyesuaian yang bersifat native pada sistem file: Anda dapat memuat file seperti `AGENTS.md` untuk petunjuk dan kemampuan di `.agents/skills/` langsung ke sandbox, atau meneruskan konfigurasi inline pada waktu interaksi. Anda dapat melakukan iterasi pada konfigurasi inline, lalu menyimpannya sebagai agen terkelola jika sudah siap.

Untuk mengetahui detail lengkap tentang cara membangun agen kustom, lihat [Membangun Agen Terkelola](https://ai.google.dev/gemini-api/docs/custom-agents?hl=id).

## Eksekusi latar belakang

Tugas agen yang melibatkan penalaran multi-langkah, eksekusi kode, atau operasi file dapat memerlukan waktu beberapa menit untuk diselesaikan. Gunakan `background=True` untuk menjalankan interaksi secara asinkron. API akan langsung menampilkan ID interaksi yang Anda polling hingga statusnya `completed` atau `failed`.

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

Eksekusi latar belakang memerlukan `store=True`, yang merupakan default. Untuk update progres real-time selama eksekusi latar belakang, lihat [Streaming interaksi latar belakang](https://ai.google.dev/gemini-api/docs/background-execution?hl=id#streaming-pattern).

Anda dapat membatalkan interaksi latar belakang yang sedang berjalan menggunakan metode `cancel`.

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

**Multi-turn dengan eksekusi di latar belakang**

Jika interaksi latar belakang melibatkan alat stateful (seperti eksekusi kode di sandbox), gunakan `environment_id` dari interaksi yang telah selesai untuk melanjutkan di lingkungan yang sama. Tindakan ini memastikan agen melanjutkan dari tempat terakhir kali ia berhenti dengan semua file dan status tetap utuh.

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

## Lingkungan

Setiap panggilan membuat atau menggunakan kembali sandbox Linux. Parameter `environment` memiliki tiga bentuk:

| Formulir | Deskripsi |
| --- | --- |
| `"remote"` | Sediakan sandbox baru dengan setelan default. |
| `"env_abc123"` | Menggunakan kembali lingkungan yang ada berdasarkan ID, dengan mempertahankan semua file dan status. |
| `{...}` | `EnvironmentConfig` penuh dengan sumber kustom dan aturan jaringan. |

Lihat [Environments](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id) untuk mengetahui detail tentang sumber (Git, GCS, inline), jaringan, siklus proses, dan batas resource.

## Pemicu

Pemicu memungkinkan Anda menjadwalkan agen untuk berjalan secara otomatis sesuai jadwal cron. Pemicu mengikat agen, lingkungan, perintah, dan jadwal ke dalam resource persisten yang diaktifkan tanpa intervensi manual. Setiap eksekusi menggunakan kembali lingkungan yang sama, sehingga file yang dibuat dalam satu eksekusi akan tetap ada dan dapat dilihat oleh eksekusi berikutnya.

### Buat pemicu

Buat pemicu dengan menentukan jadwal cron, zona waktu, dan konfigurasi interaksi. Pemicu dimulai dalam status `active` dan akan diaktifkan pada waktu cron yang cocok berikutnya. Simpan `id` yang ditampilkan untuk mengelola pemicu dalam panggilan berikutnya.

Karena pemicu berjalan tanpa pengawasan sesuai jadwal, rujuk [kredensial](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=id) yang disimpan, bukan token inline. Proxy keluar menyelesaikannya di setiap proses, dan Anda mengganti rahasia tanpa menyentuh pemicu. Aturan `transform` inline juga berfungsi di sini, Anda hanya perlu memperbarui pemicu setiap kali nilai berubah.

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

Permintaan `CreateTrigger` menerima kolom berikut:

| Kolom | Jenis | Wajib diisi | Deskripsi |
| --- | --- | --- | --- |
| `schedule` | string | Ya | Ekspresi cron (misalnya, `0 * * * *` untuk setiap jam, `0 9 * * 1-5` untuk pagi hari di hari kerja). |
| `time_zone` | string | Ya | Zona waktu IANA (misalnya, `UTC`, `America/Argentina/Buenos_Aires`). |
| `display_name` | string | Tidak | Nama pemicu yang dapat dibaca manusia. |
| `max_consecutive_failures` | bilangan bulat | Tidak | Jumlah maksimum kegagalan sebelum pemicu dijeda secara otomatis. Default: 5. |
| `execution_timeout_seconds` | bilangan bulat | Tidak | Waktu tunggu per eksekusi dalam detik. Default: 600. |
| `interaction` | objek | Ya | `CreateInteractionRequest` yang menentukan agen, input, alat, dan lingkungan. |

Respons mencakup kolom kunci berikut:

| Kolom | Jenis | Deskripsi |
| --- | --- | --- |
| `id` | string | ID unik untuk pemicu. Gunakan ini di semua operasi berikutnya. |
| `status` | string | Status saat ini: `active`, `paused`, atau `disabled`. |
| `next_run_time` | string | Stempel waktu ISO 8601 untuk eksekusi terjadwal berikutnya. |
| `consecutive_failure_count` | bilangan bulat | Jumlah eksekusi gagal berturut-turut sejak keberhasilan terakhir. |

### Mencantumkan pemicu

Mengambil semua pemicu yang terkait dengan project Anda.

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

### Mendapatkan pemicu

Mengambil konfigurasi lengkap dan status saat ini dari satu pemicu.

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

### Jeda dan lanjutkan

Anda dapat menjeda pemicu untuk menghentikan eksekusi terjadwal, dan melanjutkannya untuk mengaktifkan kembali jadwal. Penjedaan tidak memengaruhi eksekusi manual.

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

### Menghapus pemicu

Menghapus pemicu secara permanen. Histori eksekusi sebelumnya tidak dihapus.

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

### Jalankan pemicu segera

Aktifkan pemicu sesuai permintaan tanpa menunggu waktu yang dijadwalkan berikutnya. Tindakan ini berfungsi meskipun pemicu dijeda.

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

### Mencantumkan eksekusi

Melihat histori eksekusi untuk pemicu. Setiap eksekusi mencakup `status`, stempel waktu, `interaction_id` yang dapat Anda gunakan untuk mengambil output interaksi lengkap, dan `environment_id` yang mengonfirmasi bahwa semua proses berbagi sandbox yang sama.

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

## Ketersediaan dan harga

Agen Antigravity tersedia dalam pratinjau melalui
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) di Google AI Studio
dan Gemini API untuk project paket gratis dan paket berbayar.

Harga mengikuti [model bayar sesuai penggunaan](https://ai.google.dev/gemini-api/docs/pricing?hl=id#pricing-for-agents)
berdasarkan token model Gemini yang mendasarinya dan alat yang digunakan agen. Tidak seperti
permintaan chat standar yang menghasilkan satu output, interaksi Antigravitasi adalah alur kerja
agen. Satu permintaan memicu loop otonom dari penalaran, eksekusi alat, menjalankan kode, dan pengelolaan file. Project Paket Gratis mencakup pembatasan kapasitas dan kuota penggunaan gratis.

Interaksi antigravitasi menjalankan loop otonom multi-turn dan dapat menggunakan token dalam jumlah besar. Tetapkan [kontrol anggaran](#budget-controls) pada permintaan Anda untuk membatasi penggunaan token. Anda juga dapat memantau progres secara real time dengan
[streaming SSE](https://ai.google.dev/gemini-api/docs/streaming?hl=id), atau membatalkan permintaan yang sedang berjalan.

### Kontrol anggaran

Selain [pemilihan model](#model-selection), tetapkan `max_total_tokens` di dalam `agent_config` (dengan `"type": "antigravity"`) untuk membatasi
total jumlah token (input + output + penalaran) yang dapat digunakan oleh interaksi.
Token yang di-cache tidak diperhitungkan dalam batas ini. Saat agen mencapai batas, interaksi akan berhenti dan kembali dengan `status: "incomplete"`. Batas ini adalah upaya terbaik:
penggunaan sebenarnya mungkin sedikit melebihi batas tersebut, bergantung pada waktu agen memeriksa anggaran
di antara langkah-langkah.

Tetapkan anggaran pada permintaan interaksi di `agent_config` bersama dengan `agent` dan `input`.

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
        max_total_tokens: 50000
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
console.log(`Tokens used: ${interaction.usage.total_tokens}`);
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

#### Melanjutkan interaksi yang belum selesai

Saat interaksi menampilkan `status: "incomplete"`, tugas dan konteks agen dipertahankan. Kirim interaksi baru yang mereferensikan interaksi asli `id` dan
`environment_id` untuk melanjutkan dari tempat terakhir. Interaksi baru mendapatkan anggaran
`max_total_tokens` sendiri.

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
        max_total_tokens: 50000
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

### Perkiraan biaya

Biaya bervariasi berdasarkan kompleksitas tugas. Agen secara mandiri menentukan jumlah panggilan alat, eksekusi kode, dan operasi file yang diperlukan. Estimasi berikut didasarkan pada proses.

| Kategori tugas | Token input | Token output | Biaya standar |
| --- | --- | --- | --- |
| **Riset & sintesis informasi** | 100 ribu–500 ribu | 10.000–40.000 | Rp4.500–Rp15.000 |
| **Pembuatan dokumen & konten** | 100 ribu–500 ribu | 15 ribu–50 ribu | Rp4.500–Rp19.500 |
| **Desain proses & sistem** | 100 ribu–400 ribu | 10.000–30.000 | $0,25–$0,80 |
| **Pemrosesan & analisis data** | 300 ribu–3 juta | 30 ribu–150 ribu | Rp10.000–Rp45.000 |

50–70% token input biasanya di-cache. Alur kerja agentic yang kompleks dengan banyak panggilan alat dapat mengumpulkan 3–5 juta token dalam satu interaksi, dengan biaya hingga sekitar$5.

**Komputasi lingkungan** (CPU, memori, eksekusi sandbox) **tidak ditagih** selama periode pratinjau.

## Batasan

- **Status pratinjau:** Agen Antigravity dan Interactions API. Fitur dan skema dapat berubah.
- **Konfigurasi pembuatan yang tidak didukung:** Parameter berikut tidak didukung dan menampilkan error 400: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Output terstruktur:** Agen Antigravity tidak mendukung output terstruktur.
- **Alat yang tidak tersedia:** `file_search`, `computer_use`, dan `google_maps` belum didukung.
- **Batasan MCP jarak jauh:** Transpor Peristiwa yang Dikirim Server (SSE) tidak didukung (gunakan HTTP yang Dapat Di-stream). Selain itu, `name` server harus berupa huruf kecil dan alfanumerik (penggunaan huruf besar akan memicu error `400 Bad Request` umum).
- **Alat sistem file:** Saat ini tidak ada alat sistem file. Ini adalah bagian dari `environment`.
- **Persyaratan penyimpanan:** Eksekusi agen menggunakan `background=True` memerlukan `store=True`.
- **Panggilan fungsi hanya stateful:** Panggilan fungsi hanya didukung dalam mode stateful. Anda harus menggunakan `previous_interaction_id` untuk melanjutkan giliran; merekonstruksi histori secara manual (mode tanpa status) tidak didukung.
- **Jenis multimodal tidak didukung.** Input audio, video, dan dokumen saat ini tidak didukung. Hanya teks dan gambar yang diizinkan.

## Langkah berikutnya

- [Panduan memulai](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=id): percakapan multi-turn dan streaming.
- [Membangun Agen Kustom](https://ai.google.dev/gemini-api/docs/custom-agents?hl=id): petunjuk, keterampilan, dan menyimpan agen kustom.
- [Lingkungan](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id): konfigurasi sandbox, sumber, jaringan.
- [Hook](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=id): menerapkan gerbang keamanan dan validasi efek samping di dalam sandbox.
- [Agen Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=id): tugas riset panjang.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id): API yang mendasarinya.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-09 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-09 UTC."],[],[]]
