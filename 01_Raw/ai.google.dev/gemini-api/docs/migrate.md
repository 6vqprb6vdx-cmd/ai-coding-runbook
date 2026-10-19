---
source_url: https://ai.google.dev/gemini-api/docs/migrate?hl=zh-CN
fetched_at: 2026-10-19T05:44:58.151495+00:00
title: "\u8fc1\u79fb\u5230 Google GenAI SDK \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 迁移到 Google GenAI SDK

从 2024 年底发布的 Gemini 2.0 开始，我们推出了一组名为 [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn) 的新库。它通过[更新的客户端架构](https://ai.google.dev/gemini-api/docs/migrate?hl=zh-cn#client)提供改进的开发者体验，并[简化开发者工作流程与企业工作流程之间的过渡](https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=zh-cn)。

Google GenAI SDK 现已在所有受支持的平台上[正式版 (GA)](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn#new-libraries)。如果您使用的是我们的某个[旧版库](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn#previous-sdks)，我们强烈建议您进行迁移。

本指南提供了迁移前后的代码示例，可帮助您入门。

## 安装

**之前**

### Python

```
pip install -U -q "google-generativeai"
```

### JavaScript

```
npm install @google/generative-ai
```

### Go

```
go get github.com/google/generative-ai-go
```

### Java

```
<dependency>
    <groupId>com.google.ai.client.generativeai</groupId>
    <artifactId>generativeai</artifactId>
    <version>0.9.0</version>
</dependency>
```

**之后**

### Python

```
pip install -U -q "google-genai"
```

### JavaScript

```
npm install @google/genai
```

### Go

```
go get google.golang.org/genai
```

### Java

```
<dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.67.0</version>
</dependency>
```

## API 访问权限

旧版 SDK 会在后台使用各种临时方法隐式处理 API 客户端。这导致客户端和凭证难以管理。
现在，您可以通过中央 `Client` 对象进行互动。此 `Client` 对象充当各种 API 服务（例如 `models`、`chats`、`files`、`tunings`）的单一入口点，有助于在不同的 API 调用中保持一致性，并简化凭据和配置管理。

**之前（API 访问权限集中度较低）**

### Python

旧版 SDK 未明确使用顶级客户端对象来处理大多数 API 调用。您将直接实例化 `GenerativeModel` 对象并与之交互。

```
import google.generativeai as genai

# Directly create and use model objects
model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content(...)
chat = model.start_chat(...)
```

### JavaScript

虽然 `GoogleGenerativeAI` 是模型和聊天功能的中心点，但文件和缓存管理等其他功能通常需要导入和实例化完全独立的客户端类。

```
import { GoogleGenerativeAI } from "@google/generative-ai";
import { GoogleAIFileManager, GoogleAICacheManager } from "@google/generative-ai/server"; // For files/caching

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const fileManager = new GoogleAIFileManager("GEMINI_API_KEY");
const cacheManager = new GoogleAICacheManager("GEMINI_API_KEY");

// Get a model instance, then call methods on it
const model = genAI.getGenerativeModel({ model: "gemini-3.8-flash" });
const result = await model.generateContent(...);
const chat = model.startChat(...);

// Call methods on separate client objects for other services
const uploadedFile = await fileManager.uploadFile(...);
const cache = await cacheManager.create(...);
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

// Previously, model operations were called on separate model instances
Client client = new Client();
GenerateContentResponse response =
    client.models.generateContent("gemini-3.8-flash", "Tell me a story.", null);
Chat chat = client.chats.create("gemini-3.8-flash");
```

### Go

`genai.NewClient` 函数创建了一个客户端，但生成模型操作通常是在从此客户端获取的单独 `GenerativeModel` 实例上调用的。其他服务可能已通过不同的软件包或模式进行访问。

```
import (
      "github.com/google/generative-ai-go/genai"
      "github.com/google/generative-ai-go/genai/fileman" // For files
      "google.golang.org/api/option"
)

client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
fileClient, err := fileman.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))

// Get a model instance, then call methods on it
model := client.GenerativeModel("gemini-3.8-flash")
resp, err := model.GenerateContent(...)
cs := model.StartChat()

// Call methods on separate client objects for other services
uploadedFile, err := fileClient.UploadFile(...)
```

**添加后（集中式客户端对象）**

### Python

```
from google import genai

# Create a single client object
client = genai.Client()

# Access API methods through services on the client object
response = client.models.generate_content(...)
chat = client.chats.create(...)
my_file = client.files.upload(...)
tuning_job = client.tunings.tune(...)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// Create a single client object
const ai = new GoogleGenAI({apiKey: "GEMINI_API_KEY"});

// Access API methods through services on the client object
const response = await ai.models.generateContent(...);
const chat = ai.chats.create(...);
const uploadedFile = await ai.files.upload(...);
const cache = await ai.caches.create(...);
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.CachedContent;
import com.google.genai.types.CreateCachedContentConfig;
import com.google.genai.types.File;
import com.google.genai.types.GenerateContentResponse;

// Create a single client object
Client client = new Client();

// Access API methods through services on the client object
GenerateContentResponse response =
    client.models.generateContent("gemini-3.8-flash", "Tell me a story.", null);
Chat chat = client.chats.create("gemini-3.8-flash");
File uploadedFile = client.files.upload("sample.txt", null);
CachedContent cache =
    client.caches.create("gemini-3.8-flash", CreateCachedContentConfig.builder().build());
```

### Go

```
import "google.golang.org/genai"

// Create a single client object
client, err := genai.NewClient(ctx, nil)

// Access API methods through services on the client object
result, err := client.Models.GenerateContent(...)
chat, err := client.Chats.Create(...)
uploadedFile, err := client.Files.Upload(...)
tuningJob, err := client.Tunings.Tune(...)
```

## 身份验证

旧版库和新版库均使用 API 密钥进行身份验证。您可以在 Google AI Studio 中[创建](https://aistudio.google.com/apikey?hl=zh-cn) API 密钥。

**之前**

### Python

旧版 SDK 会隐式处理 API 客户端对象。

```
import google.generativeai as genai

genai.configure(api_key=...)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
```

### Java

```
import com.google.genai.Client;

// Passing the API key explicitly to the client builder
Client client = Client.builder().apiKey("GEMINI_API_KEY").build();
```

### Go

导入 Google 库：

```
import (
      "github.com/google/generative-ai-go/genai"
      "google.golang.org/api/option"
)
```

创建客户端：

```
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
```

**之后**

### Python

使用 Google GenAI SDK 时，您需要先创建一个 API 客户端，用于调用 API。如果您未将 API 密钥传递给客户端，新 SDK 将从 `GEMINI_API_KEY` 环境变量中获取您的 API 密钥。

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

```
from google import genai

client = genai.Client() # Set the API key using the GEMINI_API_KEY env var.
                        # Alternatively, you could set the API key explicitly:
                        # client = genai.Client(api_key="YOUR_API_KEY")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({apiKey: "GEMINI_API_KEY"});
```

### Java

```
import com.google.genai.Client;

// The client automatically picks up the GEMINI_API_KEY environment variable,
// or you can pass it explicitly via Client.builder().apiKey("GEMINI_API_KEY").build()
Client client = new Client();
```

### Go

导入 GenAI 库：

```
import "google.golang.org/genai"
```

创建客户端：

```
client, err := genai.NewClient(ctx, &genai.ClientConfig{
        Backend:  genai.BackendGeminiAPI,
})
```

## 生成内容

### 文本

**之前**

### Python

之前，没有客户端对象，您直接通过 `GenerativeModel` 对象访问 API。

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content(
    'Tell me a story in 300 words'
)
print(response.text)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-3.8-flash" });
const prompt = "Tell me a story in 300 words";

const result = await model.generateContent(prompt);
console.log(result.response.text());
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();
String prompt = "Tell me a story in 300 words";

GenerateContentResponse response =
    client.models.generateContent("gemini-3.8-flash", prompt, null);
System.out.println(response.text());
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-3.8-flash")
resp, err := model.GenerateContent(ctx, genai.Text("Tell me a story in 300 words."))
if err != nil {
    log.Fatal(err)
}

printResponse(resp) // utility for printing response parts
```

**之后**

### Python

新的 Google GenAI SDK 通过 `Client` 对象提供对所有 API 方法的访问权限。除了少数有状态的特殊情况（`chat` 和 live-api `session`）之外，这些都是无状态函数。为了实用性和一致性，返回的对象是 `pydantic` 类。

```
from google import genai
client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='Tell me a story in 300 words.'
)
print(response.text)

print(response.model_dump_json(
    exclude_none=True, indent=4))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Tell me a story in 300 words.",
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash", "Tell me a story in 300 words.", null);
System.out.println(response.text());
```

### Go

```
ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me a story in 300 words."), nil)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result
```

### 映像

**之前**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content([
    'Tell me a story based on this image',
    Image.open(image_path)
])
print(response.text)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({ model: "gemini-3.8-flash" });

function fileToGenerativePart(path, mimeType) {
  return {
    inlineData: {
      data: Buffer.from(fs.readFileSync(path)).toString("base64"),
      mimeType,
    },
  };
}

const prompt = "Tell me a story based on this image";

const imagePart = fileToGenerativePart(
  `path/to/organ.jpg`,
  "image/jpeg",
);

const result = await model.generateContent([prompt, imagePart]);
console.log(result.response.text());
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("path/to/organ.jpg"));
Part imagePart = Part.fromBytes(imageBytes, "image/jpeg");

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        Content.fromParts(Part.fromText("Tell me a story based on this image"), imagePart),
        null);
System.out.println(response.text());
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-3.8-flash")

imgData, err := os.ReadFile("path/to/organ.jpg")
if err != nil {
    log.Fatal(err)
}

resp, err := model.GenerateContent(ctx,
    genai.Text("Tell me about this instrument"),
    genai.ImageData("jpeg", imgData))
if err != nil {
    log.Fatal(err)
}

printResponse(resp) // utility for printing response
```

**之后**

### Python

新版 SDK 中也提供了许多相同的便捷功能。例如，系统会自动转换 `PIL.Image` 对象。

```
from google import genai
from PIL import Image

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=[
        'Tell me a story based on this image',
        Image.open(image_path)
    ]
)
print(response.text)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const organ = await ai.files.upload({
  file: "path/to/organ.jpg",
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    createUserContent([
      "Tell me a story based on this image",
      createPartFromUri(organ.uri, organ.mimeType)
    ]),
  ],
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.File;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

Client client = new Client();

File organ = client.files.upload("path/to/organ.jpg", null);

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        Content.fromParts(
            Part.fromText("Tell me a story based on this image"),
            Part.fromUri(organ.uri().orElse(""), organ.mimeType().orElse("image/jpeg"))),
        null);
System.out.println(response.text());
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

imgData, err := os.ReadFile("path/to/organ.jpg")
if err != nil {
    log.Fatal(err)
}

parts := []*genai.Part{
    {Text: "Tell me a story based on this image"},
    {InlineData: &genai.Blob{Data: imgData, MIMEType: "image/jpeg"}},
}
contents := []*genai.Content{
    {Parts: parts},
}

result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result
```

### 流式

**之前**

### Python

```
import google.generativeai as genai

response = model.generate_content(
    "Write a cute story about cats.",
    stream=True)
for chunk in response:
    print(chunk.text)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({ model: "gemini-3.8-flash" });

const prompt = "Write a story about a magic backpack.";

const result = await model.generateContentStream(prompt);

// Print text as it comes in.
for await (const chunk of result.stream) {
  const chunkText = chunk.text();
  process.stdout.write(chunkText);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();
String prompt = "Write a story about a magic backpack.";

try (ResponseStream<GenerateContentResponse> stream =
    client.models.generateContentStream("gemini-3.8-flash", prompt, null)) {
  for (GenerateContentResponse chunk : stream) {
    System.out.print(chunk.text());
  }
}
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-3.8-flash")
iter := model.GenerateContentStream(ctx, genai.Text("Write a story about a magic backpack."))
for {
    resp, err := iter.Next()
    if err == iterator.Done {
        break
    }
    if err != nil {
        log.Fatal(err)
    }
    printResponse(resp) // utility for printing the response
}
```

**之后**

### Python

```
from google import genai

client = genai.Client()

for chunk in client.models.generate_content_stream(
  model='gemini-3.8-flash',
  contents='Tell me a story in 300 words.'
):
    print(chunk.text)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContentStream({
  model: "gemini-3.8-flash",
  contents: "Write a story about a magic backpack.",
});
let text = "";
for await (const chunk of response) {
  console.log(chunk.text);
  text += chunk.text;
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.ResponseStream;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

try (ResponseStream<GenerateContentResponse> response =
    client.models.generateContentStream(
        "gemini-3.8-flash", "Tell me a story in 300 words.", null)) {
  for (GenerateContentResponse chunk : response) {
    System.out.println(chunk.text());
  }
}
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

for result, err := range client.Models.GenerateContentStream(
    ctx,
    "gemini-3.8-flash",
    genai.Text("Write a story about a magic backpack."),
    nil,
) {
    if err != nil {
        log.Fatal(err)
    }
    fmt.Print(result.Candidates[0].Content.Parts[0].Text)
}
```

## 配置

**之前**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel(
  'gemini-3.8-flash',
    system_instruction='you are a story teller for kids under 5 years old',
    generation_config=genai.GenerationConfig(
      max_output_tokens=400,
      top_k=2,
      top_p=0.5,
      temperature=0.5,
      response_mime_type='application/json',
      stop_sequences=['\n'],
    )
)
response = model.generate_content('tell me a story in 100 words')
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-3.8-flash",
  generationConfig: {
    candidateCount: 1,
    stopSequences: ["x"],
    maxOutputTokens: 20,
    temperature: 1.0,
  },
});

const result = await model.generateContent(
  "Tell me a story about a magic backpack.",
);
console.log(result.response.text())
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import java.util.Arrays;

Client client = new Client();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .systemInstruction(
            Content.fromParts(Part.fromText("you are a story teller for kids under 5 years old")))
        .maxOutputTokens(400)
        .topK(2.0f)
        .topP(0.5f)
        .temperature(0.5f)
        .responseMimeType("application/json")
        .stopSequences(Arrays.asList("\n"))
        .build();

GenerateContentResponse response =
    client.models.generateContent("gemini-3.8-flash", "tell me a story in 100 words", config);
System.out.println(response.text());
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-3.8-flash")
model.SetTemperature(0.5)
model.SetTopP(0.5)
model.SetTopK(2.0)
model.SetMaxOutputTokens(100)
model.ResponseMIMEType = "application/json"
resp, err := model.GenerateContent(ctx, genai.Text("Tell me about New York"))
if err != nil {
    log.Fatal(err)
}
printResponse(resp) // utility for printing response
```

**之后**

### Python

对于新 SDK 中的所有方法，必需实参均作为关键字实参提供。所有可选输入均在 `config` 参数中提供。配置参数可以指定为 Python 字典或 `google.genai.types` 命名空间中的 `Config` 类。为了实用性和统一性，`types` 模块中的所有定义都是 `pydantic` 类。

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
  model='gemini-3.8-flash',
  contents='Tell me a story in 100 words.',
  config=types.GenerateContentConfig(
      system_instruction='you are a story teller for kids under 5 years old',
      max_output_tokens= 400,
      top_k= 2,
      top_p= 0.5,
      temperature= 0.5,
      response_mime_type= 'application/json',
      stop_sequences= ['\n'],
      seed=42,
  ),
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Tell me a story about a magic backpack.",
  config: {
    candidateCount: 1,
    stopSequences: ["x"],
    maxOutputTokens: 20,
    temperature: 1.0,
  },
});

console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import java.util.Arrays;

Client client = new Client();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .candidateCount(1)
        .stopSequences(Arrays.asList("x"))
        .maxOutputTokens(20)
        .temperature(1.0f)
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash", "Tell me a story about a magic backpack.", config);
System.out.println(response.text());
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

result, err := client.Models.GenerateContent(ctx,
    "gemini-3.8-flash",
    genai.Text("Tell me about New York"),
    &genai.GenerateContentConfig{
        Temperature:      genai.Ptr[float32](0.5),
        TopP:             genai.Ptr[float32](0.5),
        TopK:             genai.Ptr[float32](2.0),
        ResponseMIMEType: "application/json",
        StopSequences:    []string{"Yankees"},
        CandidateCount:   2,
        Seed:             genai.Ptr[int32](42),
        MaxOutputTokens:  128,
        PresencePenalty:  genai.Ptr[float32](0.5),
        FrequencyPenalty: genai.Ptr[float32](0.5),
    },
)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing response
```

## 安全设置

通过安全设置生成回答：

**之前**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content(
    'say something bad',
    safety_settings={
        'HATE': 'BLOCK_ONLY_HIGH',
        'HARASSMENT': 'BLOCK_ONLY_HIGH',
  }
)
```

### JavaScript

```
import { GoogleGenerativeAI, HarmCategory, HarmBlockThreshold } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-3.8-flash",
  safetySettings: [
    {
      category: HarmCategory.HARM_CATEGORY_HARASSMENT,
      threshold: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    },
  ],
});

const unsafePrompt =
  "I support Martians Soccer Club and I think " +
  "Jupiterians Football Club sucks! Write an ironic phrase telling " +
  "them how I feel about them.";

const result = await model.generateContent(unsafePrompt);

try {
  result.response.text();
} catch (e) {
  console.error(e);
  console.log(result.response.candidates[0].safetyRatings);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.HarmBlockThreshold;
import com.google.genai.types.HarmCategory;
import com.google.genai.types.SafetySetting;
import java.util.Arrays;

Client client = new Client();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .safetySettings(
            Arrays.asList(
                SafetySetting.builder()
                    .category(HarmCategory.Known.HARM_CATEGORY_HARASSMENT)
                    .threshold(HarmBlockThreshold.Known.BLOCK_LOW_AND_ABOVE)
                    .build()))
        .build();

GenerateContentResponse response =
    client.models.generateContent("gemini-3.8-flash", "say something bad", config);
System.out.println(response.text());
```

**之后**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
  model='gemini-3.8-flash',
  contents='say something bad',
  config=types.GenerateContentConfig(
      safety_settings= [
          types.SafetySetting(
              category='HARM_CATEGORY_HATE_SPEECH',
              threshold='BLOCK_ONLY_HIGH'
          ),
      ]
  ),
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const unsafePrompt =
  "I support Martians Soccer Club and I think " +
  "Jupiterians Football Club sucks! Write an ironic phrase telling " +
  "them how I feel about them.";

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: unsafePrompt,
  config: {
    safetySettings: [
      {
        category: "HARM_CATEGORY_HARASSMENT",
        threshold: "BLOCK_ONLY_HIGH",
      },
    ],
  },
});

console.log("Finish reason:", response.candidates[0].finishReason);
console.log("Safety ratings:", response.candidates[0].safetyRatings);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.HarmBlockThreshold;
import com.google.genai.types.HarmCategory;
import com.google.genai.types.SafetySetting;
import java.util.Arrays;

Client client = new Client();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .safetySettings(
            Arrays.asList(
                SafetySetting.builder()
                    .category(HarmCategory.Known.HARM_CATEGORY_HATE_SPEECH)
                    .threshold(HarmBlockThreshold.Known.BLOCK_ONLY_HIGH)
                    .build()))
        .build();

GenerateContentResponse response =
    client.models.generateContent("gemini-3.8-flash", "say something bad", config);
System.out.println("Finish reason: " + response.finishReason());
```

## 异步

**之前**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content_async(
    'tell me a story in 100 words'
)
```

**之后**

### Python

如需将新 SDK 与 `asyncio` 搭配使用，请在 `client.aio` 下单独实现每个方法（`async`）。

```
from google import genai

client = genai.Client()

response = await client.aio.models.generate_content(
    model='gemini-3.8-flash',
    contents='Tell me a story in 300 words.'
)
```

## 聊天

开始对话并向模型发送消息：

**之前**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
chat = model.start_chat()

response = chat.send_message(
    "Tell me a story in 100 words")
response = chat.send_message(
    "What happened after that?")
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({ model: "gemini-3.8-flash" });
const chat = model.startChat({
  history: [
    {
      role: "user",
      parts: [{ text: "Hello" }],
    },
    {
      role: "model",
      parts: [{ text: "Great to meet you. What would you like to know?" }],
    },
  ],
});
let result = await chat.sendMessage("I have 2 dogs in my house.");
console.log(result.response.text());
result = await chat.sendMessage("How many paws are in my house?");
console.log(result.response.text());
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();
Chat chat = client.chats.create("gemini-3.8-flash");

GenerateContentResponse response1 = chat.sendMessage("Tell me a story in 100 words");
System.out.println(response1.text());

GenerateContentResponse response2 = chat.sendMessage("What happened after that?");
System.out.println(response2.text());
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-3.8-flash")
cs := model.StartChat()

cs.History = []*genai.Content{
    {
        Parts: []genai.Part{
            genai.Text("Hello, I have 2 dogs in my house."),
        },
        Role: "user",
    },
    {
        Parts: []genai.Part{
            genai.Text("Great to meet you. What would you like to know?"),
        },
        Role: "model",
    },
}

res, err := cs.SendMessage(ctx, genai.Text("How many paws are in my house?"))
if err != nil {
    log.Fatal(err)
}
printResponse(res) // utility for printing the response
```

**之后**

### Python

```
from google import genai

client = genai.Client()

chat = client.chats.create(model='gemini-3.8-flash')

response = chat.send_message(
    message='Tell me a story in 100 words')
response = chat.send_message(
    message='What happened after that?')
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const chat = ai.chats.create({
  model: "gemini-3.8-flash",
  history: [
    {
      role: "user",
      parts: [{ text: "Hello" }],
    },
    {
      role: "model",
      parts: [{ text: "Great to meet you. What would you like to know?" }],
    },
  ],
});

const response1 = await chat.sendMessage({
  message: "I have 2 dogs in my house.",
});
console.log("Chat response 1:", response1.text);

const response2 = await chat.sendMessage({
  message: "How many paws are in my house?",
});
console.log("Chat response 2:", response2.text);
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();
Chat chat = client.chats.create("gemini-3.8-flash");

GenerateContentResponse response1 = chat.sendMessage("I have 2 dogs in my house.");
System.out.println("Chat response 1: " + response1.text());

GenerateContentResponse response2 = chat.sendMessage("How many paws are in my house?");
System.out.println("Chat response 2: " + response2.text());
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

chat, err := client.Chats.Create(ctx, "gemini-3.8-flash", nil, nil)
if err != nil {
    log.Fatal(err)
}

result, err := chat.SendMessage(ctx, genai.Part{Text: "Hello, I have 2 dogs in my house."})
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result

result, err = chat.SendMessage(ctx, genai.Part{Text: "How many paws are in my house?"})
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result
```

## 函数调用

**之前**

### Python

```
import google.generativeai as genai
from enum import Enum

def get_current_weather(location: str) -> str:
    """Get the current whether in a given location.

    Args:
        location: required, The city and state, e.g. San Franciso, CA
        unit: celsius or fahrenheit
    """
    print(f'Called with: {location=}')
    return "23C"

model = genai.GenerativeModel(
    model_name="gemini-3.8-flash",
    tools=[get_current_weather]
)

response = model.generate_content("What is the weather in San Francisco?")
function_call = response.candidates[0].parts[0].function_call
```

**之后**

### Python

在新 SDK 中，自动函数调用是默认设置。在这里，您需要停用它。

```
from google import genai
from google.genai import types

client = genai.Client()

def get_current_weather(location: str) -> str:
    """Get the current whether in a given location.

    Args:
        location: required, The city and state, e.g. San Franciso, CA
        unit: celsius or fahrenheit
    """
    print(f'Called with: {location=}')
    return "23C"

response = client.models.generate_content(
  model='gemini-3.8-flash',
  contents="What is the weather like in Boston?",
  config=types.GenerateContentConfig(
      tools=[get_current_weather],
      automatic_function_calling={'disable': True},
  ),
)

function_call = response.candidates[0].content.parts[0].function_call
```

### 自动函数调用

**之前**

### Python

旧版 SDK 仅支持在聊天中自动调用函数。在更新后的 SDK 中，这是 `generate_content` 中的默认行为。

```
import google.generativeai as genai

def get_current_weather(city: str) -> str:
    return "23C"

model = genai.GenerativeModel(
    model_name="gemini-3.8-flash",
    tools=[get_current_weather]
)

chat = model.start_chat(
    enable_automatic_function_calling=True)
result = chat.send_message("What is the weather in San Francisco?")
```

**之后**

### Python

```
from google import genai
from google.genai import types
client = genai.Client()

def get_current_weather(city: str) -> str:
    return "23C"

response = client.models.generate_content(
  model='gemini-3.8-flash',
  contents="What is the weather like in Boston?",
  config=types.GenerateContentConfig(
      tools=[get_current_weather]
  ),
)
```

## 代码执行

代码执行是一种工具，可让模型生成 Python 代码、运行代码并返回结果。

**之前**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel(
    model_name="gemini-3.8-flash",
    tools="code_execution"
)

result = model.generate_content(
  "What is the sum of the first 50 prime numbers? Generate and run code for "
  "the calculation, and make sure you get all 50.")
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-3.8-flash",
  tools: [{ codeExecution: {} }],
});

const result = await model.generateContent(
  "What is the sum of the first 50 prime numbers? " +
    "Generate and run code for the calculation, and make sure you get " +
    "all 50.",
);

console.log(result.response.text());
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Tool;
import com.google.genai.types.ToolCodeExecution;
import java.util.Arrays;

Client client = new Client();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .tools(
            Arrays.asList(
                Tool.builder().codeExecution(ToolCodeExecution.builder().build()).build()))
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        "What is the sum of the first 50 prime numbers? Generate and run code for "
            + "the calculation, and make sure you get all 50.",
        config);
System.out.println(response.text());
```

**之后**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='What is the sum of the first 50 prime numbers? Generate and run '
            'code for the calculation, and make sure you get all 50.',
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    ),
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: `Write and execute code that calculates the sum of the first 50 prime numbers.
            Ensure that only the executable code and its resulting output are generated.`,
});

// Each part may contain text, executable code, or an execution result.
for (const part of response.candidates[0].content.parts) {
  console.log(part);
  console.log("\n");
}

console.log("-".repeat(80));
// The `.text` accessor concatenates the parts into a markdown-formatted text.
console.log("\n", response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import com.google.genai.types.Tool;
import com.google.genai.types.ToolCodeExecution;
import java.util.Arrays;

Client client = new Client();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .tools(
            Arrays.asList(
                Tool.builder().codeExecution(ToolCodeExecution.builder().build()).build()))
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        "Write and execute code that calculates the sum of the first 50 prime numbers. "
            + "Ensure that only the executable code and its resulting output are generated.",
        config);

if (response.parts() != null) {
  for (Part part : response.parts()) {
    System.out.println(part);
  }
}
System.out.println(response.text());
```

## 搜索接地

`GoogleSearch` (Gemini>=2.0) 和 `GoogleSearchRetrieval` (Gemini < 2.0) 是由 Google 提供支持的工具，可让模型检索公开网络数据以进行接地。

**之前**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content(
    contents="what is the Google stock price?",
    tools='google_search_retrieval'
)
```

**之后**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='What is the Google stock price?',
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch()
            )
        ]
    )
)
```

## JSON 响应

以 JSON 格式生成答案。

**之前**

### Python

通过指定 `response_schema` 并设置 `response_mime_type="application/json"`，用户可以限制模型按照给定结构生成 `JSON` 响应。

```
import google.generativeai as genai
import typing_extensions as typing

class CountryInfo(typing.TypedDict):
    name: str
    population: int
    capital: str
    continent: str
    major_cities: list[str]
    gdp: int
    official_language: str
    total_area_sq_mi: int

model = genai.GenerativeModel(model_name="gemini-3.8-flash")
result = model.generate_content(
    "Give me information of the United States",
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json",
        response_schema = CountryInfo
    ),
)
```

### JavaScript

```
import { GoogleGenerativeAI, SchemaType } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");

const schema = {
  description: "List of recipes",
  type: SchemaType.ARRAY,
  items: {
    type: SchemaType.OBJECT,
    properties: {
      recipeName: {
        type: SchemaType.STRING,
        description: "Name of the recipe",
        nullable: false,
      },
    },
    required: ["recipeName"],
  },
};

const model = genAI.getGenerativeModel({
  model: "gemini-3.8-flash",
  generationConfig: {
    responseMimeType: "application/json",
    responseSchema: schema,
  },
});

const result = await model.generateContent(
  "List a few popular cookie recipes.",
);
console.log(result.response.text());
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Schema;
import com.google.genai.types.Type;
import java.util.Arrays;
import java.util.Map;

Client client = new Client();

Schema schema =
    Schema.builder()
        .description("List of recipes")
        .type(Type.Known.ARRAY)
        .items(
            Schema.builder()
                .type(Type.Known.OBJECT)
                .properties(
                    Map.of(
                        "recipeName",
                        Schema.builder()
                            .type(Type.Known.STRING)
                            .description("Name of the recipe")
                            .build()))
                .required(Arrays.asList("recipeName"))
                .build())
        .build();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .responseMimeType("application/json")
        .responseSchema(schema)
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash", "List a few popular cookie recipes.", config);
System.out.println(response.text());
```

**之后**

### Python

新 SDK 使用 `pydantic` 类来提供架构（不过您也可以传递 `genai.types.Schema` 或等效的 `dict`）。SDK 会尽可能解析返回的 JSON，并在 `response.parsed` 中返回结果。如果您提供了 `pydantic` 类作为架构，SDK 会将该 `JSON` 转换为该类的实例。

```
from google import genai
from pydantic import BaseModel

client = genai.Client()

class CountryInfo(BaseModel):
    name: str
    population: int
    capital: str
    continent: str
    major_cities: list[str]
    gdp: int
    official_language: str
    total_area_sq_mi: int

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='Give me information of the United States.',
    config={
        'response_mime_type': 'application/json',
        'response_schema': CountryInfo,
    },
)

response.parsed
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "List a few popular cookie recipes.",
  config: {
    responseMimeType: "application/json",
    responseSchema: {
      type: "array",
      items: {
        type: "object",
        properties: {
          recipeName: { type: "string" },
          ingredients: { type: "array", items: { type: "string" } },
        },
        required: ["recipeName", "ingredients"],
      },
    },
  },
});
console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Schema;
import com.google.genai.types.Type;
import java.util.Arrays;
import java.util.Map;

Client client = new Client();

Schema schema =
    Schema.builder()
        .type(Type.Known.ARRAY)
        .items(
            Schema.builder()
                .type(Type.Known.OBJECT)
                .properties(
                    Map.of(
                        "recipeName", Schema.builder().type(Type.Known.STRING).build(),
                        "ingredients",
                            Schema.builder()
                                .type(Type.Known.ARRAY)
                                .items(Schema.builder().type(Type.Known.STRING).build())
                                .build()))
                .required(Arrays.asList("recipeName", "ingredients"))
                .build())
        .build();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .responseMimeType("application/json")
        .responseSchema(schema)
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash", "List a few popular cookie recipes.", config);
System.out.println(response.text());
```

## 文件

### 上传

上传文件：

**之前**

### Python

```
import requests
import pathlib
import google.generativeai as genai

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

file = genai.upload_file(path='a11.txt')

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.generate_content([
    'Can you summarize this file:',
    my_file
])
print(response.text)
```

**之后**

### Python

```
import requests
import pathlib
from google import genai

client = genai.Client()

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

my_file = client.files.upload(file='a11.txt')

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=[
        'Can you summarize this file:',
        my_file
    ]
)
print(response.text)
```

### 列出和获取

列出已上传的文件并获取具有文件名的已上传文件：

**之前**

### Python

```
import google.generativeai as genai

for file in genai.list_files():
  print(file.name)

file = genai.get_file(name=file.name)
```

**之后**

### Python

```
from google import genai
client = genai.Client()

for file in client.files.list():
    print(file.name)

file = client.files.get(name=file.name)
```

### 删除

删除文件：

**之前**

### Python

```
import pathlib
import google.generativeai as genai

pathlib.Path('dummy.txt').write_text(dummy)
dummy_file = genai.upload_file(path='dummy.txt')

file = genai.delete_file(name=dummy_file.name)
```

**之后**

### Python

```
import pathlib
from google import genai

client = genai.Client()

pathlib.Path('dummy.txt').write_text(dummy)
dummy_file = client.files.upload(file='dummy.txt')

response = client.files.delete(name=dummy_file.name)
```

## 上下文缓存

借助上下文缓存，用户只需将内容传递给模型一次，即可缓存输入 token，然后在后续调用中引用缓存的 token，从而降低费用。

**之前**

### Python

```
import requests
import pathlib
import google.generativeai as genai
from google.generativeai import caching

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

# Upload file
document = genai.upload_file(path="a11.txt")

# Create cache
apollo_cache = caching.CachedContent.create(
    model="gemini-3.8-flash",
    system_instruction="You are an expert at analyzing transcripts.",
    contents=[document],
)

# Generate response
apollo_model = genai.GenerativeModel.from_cached_content(
    cached_content=apollo_cache
)
response = apollo_model.generate_content("Find a lighthearted moment from this transcript")
```

### JavaScript

```
import { GoogleAICacheManager, GoogleAIFileManager } from "@google/generative-ai/server";
import { GoogleGenerativeAI } from "@google/generative-ai";

const cacheManager = new GoogleAICacheManager("GEMINI_API_KEY");
const fileManager = new GoogleAIFileManager("GEMINI_API_KEY");

const uploadResult = await fileManager.uploadFile("path/to/a11.txt", {
  mimeType: "text/plain",
});

const cacheResult = await cacheManager.create({
  model: "models/gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: uploadResult.file.uri,
            mimeType: uploadResult.file.mimeType,
          },
        },
      ],
    },
  ],
});

console.log(cacheResult);

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModelFromCachedContent(cacheResult);
const result = await model.generateContent(
  "Please summarize this transcript.",
);
console.log(result.response.text());
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.CachedContent;
import com.google.genai.types.Content;
import com.google.genai.types.CreateCachedContentConfig;
import com.google.genai.types.File;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import java.util.Arrays;

Client client = new Client();

File uploadResult = client.files.upload("path/to/a11.txt", null);

CachedContent cacheResult =
    client.caches.create(
        "gemini-3.8-flash",
        CreateCachedContentConfig.builder()
            .contents(
                Arrays.asList(
                    Content.fromParts(
                        Part.fromUri(
                            uploadResult.uri().orElse(""),
                            uploadResult.mimeType().orElse("text/plain")))))
            .systemInstruction(
                Content.fromParts(Part.fromText("You are an expert at analyzing transcripts.")))
            .build());

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        "Please summarize this transcript.",
        GenerateContentConfig.builder().cachedContent(cacheResult.name().orElse("")).build());
System.out.println(response.text());
```

**之后**

### Python

```
import requests
import pathlib
from google import genai
from google.genai import types

client = genai.Client()

# Check which models support caching.
for m in client.models.list():
  for action in m.supported_actions:
    if action == "createCachedContent":
      print(m.name)
      break

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

# Upload file
document = client.files.upload(file='a11.txt')

# Create cache
model='gemini-3.8-flash'
apollo_cache = client.caches.create(
      model=model,
      config={
          'contents': [document],
          'system_instruction': 'You are an expert at analyzing transcripts.',
      },
  )

# Generate response
response = client.models.generate_content(
    model=model,
    contents='Find a lighthearted moment from this transcript',
    config=types.GenerateContentConfig(
        cached_content=apollo_cache.name,
    )
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const filePath = path.join(media, "a11.txt");
const document = await ai.files.upload({
  file: filePath,
  config: { mimeType: "text/plain" },
});
console.log("Uploaded file name:", document.name);
const modelName = "gemini-3.8-flash";

const contents = [
  createUserContent(createPartFromUri(document.uri, document.mimeType)),
];

const cache = await ai.caches.create({
  model: modelName,
  config: {
    contents: contents,
    systemInstruction: "You are an expert analyzing transcripts.",
  },
});
console.log("Cache created:", cache);

const response = await ai.models.generateContent({
  model: modelName,
  contents: "Please summarize this transcript",
  config: { cachedContent: cache.name },
});
console.log("Response text:", response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.CachedContent;
import com.google.genai.types.Content;
import com.google.genai.types.CreateCachedContentConfig;
import com.google.genai.types.File;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import java.util.Arrays;

Client client = new Client();

File document = client.files.upload("a11.txt", null);
String modelName = "gemini-3.8-flash";

CachedContent cache =
    client.caches.create(
        modelName,
        CreateCachedContentConfig.builder()
            .contents(
                Arrays.asList(
                    Content.fromParts(
                        Part.fromUri(
                            document.uri().orElse(""), document.mimeType().orElse("text/plain")))))
            .systemInstruction(
                Content.fromParts(Part.fromText("You are an expert analyzing transcripts.")))
            .build());

GenerateContentResponse response =
    client.models.generateContent(
        modelName,
        "Find a lighthearted moment from this transcript",
        GenerateContentConfig.builder().cachedContent(cache.name().orElse("")).build());
System.out.println(response.text());
```

## 统计 token 数量

统计请求中的 token 数量。

**之前**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-3.8-flash')
response = model.count_tokens(
    'The quick brown fox jumps over the lazy dog.')
```

### JavaScript

```
 import { GoogleGenerativeAI } from "@google/generative-ai";

 const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
 const model = genAI.getGenerativeModel({
   model: "gemini-3.8-flash",
 });

 // Count tokens in a prompt without calling text generation.
 const countResult = await model.countTokens(
   "The quick brown fox jumps over the lazy dog.",
 );

 console.log(countResult.totalTokens); // 11

 const generateResult = await model.generateContent(
   "The quick brown fox jumps over the lazy dog.",
 );

 // On the response for `generateContent`, use `usageMetadata`
 // to get separate input and output token counts
 // (`promptTokenCount` and `candidatesTokenCount`, respectively),
 // as well as the combined token count (`totalTokenCount`).
 console.log(generateResult.response.usageMetadata);
 // candidatesTokenCount and totalTokenCount depend on response, may vary
 // { promptTokenCount: 11, candidatesTokenCount: 124, totalTokenCount: 135 }
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.CountTokensResponse;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();
String prompt = "The quick brown fox jumps over the lazy dog.";

CountTokensResponse countResult = client.models.countTokens("gemini-3.8-flash", prompt, null);
System.out.println(countResult.totalTokens().orElse(0));

GenerateContentResponse generateResult =
    client.models.generateContent("gemini-3.8-flash", prompt, null);
System.out.println(generateResult.usageMetadata());
```

**之后**

### Python

```
from google import genai

client = genai.Client()

response = client.models.count_tokens(
    model='gemini-3.8-flash',
    contents='The quick brown fox jumps over the lazy dog.',
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const prompt = "The quick brown fox jumps over the lazy dog.";
const countTokensResponse = await ai.models.countTokens({
  model: "gemini-3.8-flash",
  contents: prompt,
});
console.log(countTokensResponse.totalTokens);

const generateResponse = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: prompt,
});
console.log(generateResponse.usageMetadata);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.CountTokensResponse;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();
String prompt = "The quick brown fox jumps over the lazy dog.";

CountTokensResponse countTokensResponse =
    client.models.countTokens("gemini-3.8-flash", prompt, null);
System.out.println(countTokensResponse.totalTokens().orElse(0));

GenerateContentResponse generateResponse =
    client.models.generateContent("gemini-3.8-flash", prompt, null);
System.out.println(generateResponse.usageMetadata());
```

## 生成图片

生成图片：

**之前**

### Python

```
#pip install https://github.com/google-gemini/generative-ai-python@imagen
import google.generativeai as genai

imagen = genai.ImageGenerationModel(
    "imagen-3.0-generate-001")
gen_images = imagen.generate_images(
    prompt="Robot holding a red skateboard",
    number_of_images=1,
    safety_filter_level="block_low_and_above",
    person_generation="allow_adult",
    aspect_ratio="3:4",
)
```

**之后**

### Python

```
from google import genai

client = genai.Client()

gen_images = client.models.generate_images(
    model='gemini-2.5-flash-image',
    prompt='Robot holding a red skateboard',
    config=types.GenerateImagesConfig(
        number_of_images= 1,
        safety_filter_level= "BLOCK_LOW_AND_ABOVE",
        person_generation= "ALLOW_ADULT",
        aspect_ratio= "3:4",
    )
)

for n, image in enumerate(gen_images.generated_images):
    pathlib.Path(f'{n}.png').write_bytes(
        image.image.image_bytes)
```

## 嵌入内容

生成内容嵌入。

**之前**

### Python

```
import google.generativeai as genai

response = genai.embed_content(
  model='models/gemini-embedding-001',
  content='Hello world'
)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-embedding-001",
});

const result = await model.embedContent("Hello world!");

console.log(result.embedding);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-001", "Hello world!", null);
System.out.println(response.embeddings());
```

**之后**

### Python

```
from google import genai

client = genai.Client()

response = client.models.embed_content(
  model='gemini-embedding-001',
  contents='Hello world',
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const text = "Hello World!";
const result = await ai.models.embedContent({
  model: "gemini-embedding-001",
  contents: text,
  config: { outputDimensionality: 10 },
});
console.log(result.embeddings);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentConfig;
import com.google.genai.types.EmbedContentResponse;

Client client = new Client();
String text = "Hello World!";

EmbedContentResponse result =
    client.models.embedContent(
        "gemini-embedding-001",
        text,
        EmbedContentConfig.builder().outputDimensionality(10).build());
System.out.println(result.embeddings());
```

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-15。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-15。"],[],[]]
