---
source_url: https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-CN
fetched_at: 2026-10-05T06:40:11.591734+00:00
title: "Batch API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Batch API

Gemini Batch API 旨在以标准费用的 [50%](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn) 异步处理大量请求。
目标周转时间为 24 小时，但在大多数情况下，周转时间要短得多。

对于大规模、非紧急任务（例如数据预处理或运行评估，不需要立即响应），请使用 Batch API。

## 创建批量作业

您可以通过以下两种方式在 Batch API 中提交请求：

- **[内嵌请求](#inline-requests)**：直接包含在批量创建请求中的
  [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=zh-cn#GenerateContentRequest)对象列表。此方法适用于总请求大小不超过 20MB 的较小批量。模型返回的**输出** 是 `inlineResponse` 对象列表。
- **[输入文件](#input-file)**： [JSON Lines (JSONL)](https://jsonlines.org/)
  文件，其中每一行都包含一个完整的
  [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=zh-cn#GenerateContentRequest) 对象。
  建议对较大请求使用此方法。模型返回的**输出** 是 JSONL 文件，其中每一行都是 `GenerateContentResponse` 或状态对象。

### 内嵌请求

对于少量请求，您可以将
[`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=zh-cn#GenerateContentRequest)对象
直接嵌入到[`BatchGenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=zh-cn#request-body)中。以下示例使用内嵌请求调用
[`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=zh-cn#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
方法：

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# A list of dictionaries, where each is a GenerateContentRequest
inline_requests = [
    {
        'contents': [{
            'parts': [{'text': 'Tell me a one-sentence joke.'}],
            'role': 'user'
        }]
    },
    {
        'contents': [{
            'parts': [{'text': 'Why is the sky blue?'}],
            'role': 'user'
        }]
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3.8-flash",
    src=inline_requests,
    config={
        'display_name': "inlined-requests-job-1",
    },
)

print(f"Created batch job: {inline_batch_job.name}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

const inlinedRequests = [
    {
        contents: [{
            parts: [{text: 'Tell me a one-sentence joke.'}],
            role: 'user'
        }]
    },
    {
        contents: [{
            parts: [{'text': 'Why is the sky blue?'}],
            role: 'user'
        }]
    }
]

const response = await ai.batches.create({
    model: 'gemini-3.8-flash',
    src: inlinedRequests,
    config: {
        displayName: 'inlined-requests-job-1',
    }
});

console.log(response);
```

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.Content;
import com.google.genai.types.CreateBatchJobConfig;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.Part;
import java.util.List;

Client client = new Client();

// A list of InlinedRequest objects
List<InlinedRequest> inlineRequests =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.builder()
                        .role("user")
                        .parts(Arrays.asList(Part.fromText("Tell me a one-sentence joke.")))
                        .build()))
            .build(),
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.builder()
                        .role("user")
                        .parts(Arrays.asList(Part.fromText("Why is the sky blue?")))
                        .build()))
            .build());

BatchJobSource src = BatchJobSource.builder().inlinedRequests(inlineRequests).build();
CreateBatchJobConfig config =
    CreateBatchJobConfig.builder().displayName("inlined-requests-job-1").build();

BatchJob inlineBatchJob = client.batches.create("gemini-3.8-flash", src, config);

System.out.println("Created batch job: " + inlineBatchJob.name().orElse(""));
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:batchGenerateContent \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-X POST \
-H "Content-Type:application/json" \
-d '{
    "batch": {
        "display_name": "my-batch-requests",
        "input_config": {
            "requests": {
                "requests": [
                    {
                        "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]},
                        "metadata": {
                            "key": "request-1"
                        }
                    },
                    {
                        "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]},
                        "metadata": {
                            "key": "request-2"
                        }
                    }
                ]
            }
        }
    }
}'
```

### 输入文件

对于较大的请求集，请准备一个 JSON Lines (JSONL) 文件。此文件中的每一行都必须是一个 JSON 对象，其中包含用户定义的键和请求
对象，并且请求是有效的
[`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=zh-cn#GenerateContentRequest) 对象。用户定义的键用于在响应中指明哪个输出是哪个请求的结果。例如，键定义为
`request-1` 的请求的响应将使用相同的键名称进行注释。

此文件使用 [File API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn) 上传。输入文件允许的最大文件大小为 2GB。

以下是 JSONL 文件示例。您可以将其保存在名为 `my-batch-requests.json` 的文件中：

```
{"key": "request-1", "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}], "generation_config": {"temperature": 0.7}}}
{"key": "request-2", "request": {"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}}
```

与内嵌请求类似，您可以在每个请求 JSON 中指定其他参数，例如系统说明、工具或其他配置。

您可以使用 [File API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn) 上传此文件，如
以下示例所示。如果您使用的是多模态输入，则可以在 JSONL 文件中引用其他已上传的文件。

### Python

```
import json
from google import genai
from google.genai import types

client = genai.Client()

# Create a sample JSONL file
with open("my-batch-requests.jsonl", "w") as f:
    requests = [
        {"key": "request-1", "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]}},
        {"key": "request-2", "request": {"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}}
    ]
    for req in requests:
        f.write(json.dumps(req) + "\n")

# Upload the file to the File API
uploaded_file = client.files.upload(
    file='my-batch-requests.jsonl',
    config=types.UploadFileConfig(display_name='my-batch-requests', mime_type='jsonl')
)

print(f"Uploaded file: {uploaded_file.name}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from 'url';

const ai = new GoogleGenAI({});
const fileName = "my-batch-requests.jsonl";

// Define the requests
const requests = [
    { "key": "request-1", "request": { "contents": [{ "parts": [{ "text": "Describe the process of photosynthesis." }] }] } },
    { "key": "request-2", "request": { "contents": [{ "parts": [{ "text": "What are the main ingredients in a Margherita pizza?" }] }] } }
];

// Construct the full path to file
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const filePath = path.join(__dirname, fileName); // __dirname is the directory of the current script

async function writeBatchRequestsToFile(requests, filePath) {
    try {
        // Use a writable stream for efficiency, especially with larger files.
        const writeStream = fs.createWriteStream(filePath, { flags: 'w' });

        writeStream.on('error', (err) => {
            console.error(`Error writing to file ${filePath}:`, err);
        });

        for (const req of requests) {
            writeStream.write(JSON.stringify(req) + '\n');
        }

        writeStream.end();

        console.log(`Successfully wrote batch requests to ${filePath}`);

    } catch (error) {
        // This catch block is for errors that might occur before stream setup,
        // stream errors are handled by the 'error' event.
        console.error(`An unexpected error occurred:`, error);
    }
}

// Write to a file.
writeBatchRequestsToFile(requests, filePath);

// Upload the file to the File API.
const uploadedFile = await ai.files.upload({file: 'my-batch-requests.jsonl', config: {
    mimeType: 'jsonl',
}});
console.log(uploadedFile.name);
```

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

Client client = new Client();

// Create a sample JSONL file
List<String> requests =
    Arrays.asList(
        "{\"key\": \"request-1\", \"request\": {\"contents\": [{\"parts\": [{\"text\": \"Describe the process of photosynthesis.\"}]}]}}",
        "{\"key\": \"request-2\", \"request\": {\"contents\": [{\"parts\": [{\"text\": \"What are the main ingredients in a Margherita pizza?\"}]}]}}");
Files.write(Paths.get("my-batch-requests.jsonl"), requests);

// Upload the file to the File API
UploadFileConfig uploadConfig =
    UploadFileConfig.builder()
        .displayName("my-batch-requests")
        .mimeType("jsonl")
        .build();
File uploadedFile = client.files.upload("my-batch-requests.jsonl", uploadConfig);

System.out.println("Uploaded file: " + uploadedFile.name().orElse(""));
```

### REST

```
tmp_batch_input_file=batch_input.tmp
echo -e '{"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}], "generationConfig": {"temperature": 0.7}}\n{"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}' > batch_input.tmp
MIME_TYPE=$(file -b --mime-type "${tmp_batch_input_file}")
NUM_BYTES=$(wc -c < "${tmp_batch_input_file}")
DISPLAY_NAME=BatchInput

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
-D "${tmp_header_file}" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "X-Goog-Upload-Protocol: resumable" \
-H "X-Goog-Upload-Command: start" \
-H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
-H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
-H "Content-Type: application/jsonl" \
-d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
-H "Content-Length: ${NUM_BYTES}" \
-H "X-Goog-Upload-Offset: 0" \
-H "X-Goog-Upload-Command: upload, finalize" \
--data-binary "@${tmp_batch_input_file}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
```

以下示例使用通过 File API 上传的输入文件调用
[`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=zh-cn#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
方法：

### Python

```
from google import genai

# Assumes `uploaded_file` is the file object from the previous step
client = genai.Client()
file_batch_job = client.batches.create(
    model="gemini-3.8-flash",
    src=uploaded_file.name,
    config={
        'display_name': "file-upload-job-1",
    },
)

print(f"Created batch job: {file_batch_job.name}")
```

### JavaScript

```
// Assumes `uploadedFile` is the file object from the previous step
const fileBatchJob = await ai.batches.create({
    model: 'gemini-3.8-flash',
    src: uploadedFile.name,
    config: {
        displayName: 'file-upload-job-1',
    }
});

console.log(fileBatchJob);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.CreateBatchJobConfig;

Client client = new Client();

// Assumes `uploadedFileName` is the file name from the previous step
String uploadedFileName = "files/my-batch-requests-id";

BatchJobSource src = BatchJobSource.builder().fileName(uploadedFileName).build();
CreateBatchJobConfig config =
    CreateBatchJobConfig.builder().displayName("file-upload-job-1").build();

BatchJob fileBatchJob = client.batches.create("gemini-3.8-flash", src, config);

System.out.println("Created batch job: " + fileBatchJob.name().orElse(""));
```

### REST

```
# Set the File ID taken from the upload response.
BATCH_INPUT_FILE='files/123456'
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:batchGenerateContent \
-X POST \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" \
-d "{
    'batch': {
        'display_name': 'my-batch-requests',
        'input_config': {
            'file_name': '${BATCH_INPUT_FILE}'
        }
    }
}"
```

创建批量作业时，系统会返回作业名称。[[您可以使用此名称
监控作业状态，并在作业完成后
检索结果。](#batch-job-status)](#retrieve-batch-results)

以下是包含作业名称的输出示例：

```
Created batch job from file: batches/123456789
```

### 批量嵌入支持

您可以使用 Batch API 与
[Embeddings 模型](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-cn)交互，以获得更高的吞吐量。
如需使用[内嵌请求](#inline-requests)
或[输入文件](#input-file)创建嵌入批量作业，请使用`batches.create_embeddings` API 并
指定嵌入模型。

### Python

```
from google import genai

client = genai.Client()

# Creating an embeddings batch job with an input file request:
file_job = client.batches.create_embeddings(
    model="gemini-embedding-2",
    src={'file_name': uploaded_batch_requests.name},
    config={'display_name': "Input embeddings batch"},
)

# Creating an embeddings batch job with an inline request:
batch_job = client.batches.create_embeddings(
    model="gemini-embedding-2",
    # For a predefined list of requests `inlined_requests`
    src={'inlined_requests': inlined_requests},
    config={'display_name': "Inlined embeddings batch"},
)
```

### JavaScript

```
// Creating an embeddings batch job with an input file request:
let fileJob;
fileJob = await client.batches.createEmbeddings({
    model: 'gemini-embedding-2',
    src: {fileName: uploadedBatchRequests.name},
    config: {displayName: 'Input embeddings batch'},
});
console.log(`Created batch job: ${fileJob.name}`);

// Creating an embeddings batch job with an inline request:
let batchJob;
batchJob = await client.batches.createEmbeddings({
    model: 'gemini-embedding-2',
    // For a predefined a list of requests `inlinedRequests`
    src: {inlinedRequests: inlinedRequests},
    config: {displayName: 'Inlined embeddings batch'},
});
console.log(`Created batch job: ${batchJob.name}`);
```

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.Content;
import com.google.genai.types.CreateEmbeddingsBatchJobConfig;
import com.google.genai.types.EmbedContentBatch;
import com.google.genai.types.EmbeddingsBatchJobSource;
import com.google.genai.types.Part;
import java.util.List;

Client client = new Client();

String uploadedFileName = "files/my-embedding-requests-id";

// Creating an embeddings batch job with an input file request:
BatchJob fileJob =
    client.batches.createEmbeddings(
        "gemini-embedding-2",
        EmbeddingsBatchJobSource.builder().fileName(uploadedFileName).build(),
        CreateEmbeddingsBatchJobConfig.builder().displayName("Input embeddings batch").build());
System.out.println("Created batch job: " + fileJob.name().orElse(""));

// Creating an embeddings batch job with an inline request:
EmbedContentBatch inlinedRequests =
    EmbedContentBatch.builder()
        .contents(Arrays.asList(Content.fromParts(Part.fromText("What is the meaning of life?"))))
        .build();
BatchJob batchJob =
    client.batches.createEmbeddings(
        "gemini-embedding-2",
        EmbeddingsBatchJobSource.builder().inlinedRequests(inlinedRequests).build(),
        CreateEmbeddingsBatchJobConfig.builder().displayName("Inlined embeddings batch").build());
System.out.println("Created batch job: " + batchJob.name().orElse(""));
```

如需查看更多示例，请参阅 [Batch API 食谱](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb)
中的 Embeddings 部分。

### 请求配置

您可以添加在标准非批量请求中使用的任何请求配置。例如，您可以指定温度、系统说明，甚至传入其他模态。以下示例展示了一个内嵌请求示例，其中包含一个请求的系统说明：

### Python

```
inline_requests_list = [
    {'contents': [{'parts': [{'text': 'Write a short poem about a cloud.'}]}]},
    {'contents': [{
        'parts': [{
            'text': 'Write a short poem about a cat.'
            }]
        }],
    'config': {
        'system_instruction': {'parts': [{'text': 'You are a cat. Your name is Neko.'}]}}
    }
]
```

### JavaScript

```
inlineRequestsList = [
    {contents: [{parts: [{text: 'Write a short poem about a cloud.'}]}]},
    {contents: [{parts: [{text: 'Write a short poem about a cat.'}]}],
     config: {systemInstruction: {parts: [{text: 'You are a cat. Your name is Neko.'}]}}}
]
```

### Java

```
import java.util.Arrays;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.Part;
import java.util.List;

List<InlinedRequest> inlineRequestsList =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(Arrays.asList(Content.fromParts(Part.fromText("Write a short poem about a cloud."))))
            .build(),
        InlinedRequest.builder()
            .contents(Arrays.asList(Content.fromParts(Part.fromText("Write a short poem about a cat."))))
            .config(
                GenerateContentConfig.builder()
                    .systemInstruction(
                        Content.fromParts(Part.fromText("You are a cat. Your name is Neko.")))
                    .build())
            .build());
```

同样，您可以指定要用于请求的工具。以下示例
展示了一个启用 [Google 搜索工具](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)的请求：

### Python

```
inlined_requests = [
{'contents': [{'parts': [{'text': 'Who won the euro 1998?'}]}]},
{'contents': [{'parts': [{'text': 'Who won the euro 2025?'}]}],
 'config':{'tools': [{'google_search': {}}]}}]
```

### JavaScript

```
inlineRequestsList = [
    {contents: [{parts: [{text: 'Who won the euro 1998?'}]}]},
    {contents: [{parts: [{text: 'Who won the euro 2025?'}]}],
     config: {tools: [{googleSearch: {}}]}}
]
```

### Java

```
import java.util.Arrays;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GoogleSearch;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.Part;
import com.google.genai.types.Tool;
import java.util.List;

List<InlinedRequest> inlinedRequests =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(Arrays.asList(Content.fromParts(Part.fromText("Who won the euro 1998?"))))
            .build(),
        InlinedRequest.builder()
            .contents(Arrays.asList(Content.fromParts(Part.fromText("Who won the euro 2025?"))))
            .config(
                GenerateContentConfig.builder()
                    .tools(Tool.builder().googleSearch(GoogleSearch.builder().build()).build())
                    .build())
            .build());
```

您还可以指定[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)。
以下示例展示了如何为批量请求指定结构化输出。

### Python

```
import time
from google import genai
from pydantic import BaseModel, TypeAdapter

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

client = genai.Client()

# A list of dictionaries, where each is a GenerateContentRequest
inline_requests = [
    {
        'contents': [{
            'parts': [{'text': 'List a few popular cookie recipes, and include the amounts of ingredients.'}],
            'role': 'user'
        }],
        'config': {
            'response_mime_type': 'application/json',
            'response_schema': list[Recipe]
        }
    },
    {
        'contents': [{
            'parts': [{'text': 'List a few popular gluten free cookie recipes, and include the amounts of ingredients.'}],
            'role': 'user'
        }],
        'config': {
            'response_mime_type': 'application/json',
            'response_schema': list[Recipe]
        }
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3.8-flash",
    src=inline_requests,
    config={
        'display_name': "structured-output-job-1"
    },
)

# wait for the job to finish
job_name = inline_batch_job.name
print(f"Polling status for job: {job_name}")

while True:
    batch_job_inline = client.batches.get(name=job_name)
    if batch_job_inline.state.name in ('JOB_STATE_SUCCEEDED', 'JOB_STATE_FAILED', 'JOB_STATE_CANCELLED', 'JOB_STATE_EXPIRED'):
        break
    print(f"Job not finished. Current state: {batch_job_inline.state.name}. Waiting 30 seconds...")
    time.sleep(30)

print(f"Job finished with state: {batch_job_inline.state.name}")

# print the response
for i, inline_response in enumerate(batch_job_inline.dest.inlined_responses, start=1):
    print(f"\n--- Response {i} ---")

    # Check for a successful response
    if inline_response.response:
        # The .text property is a shortcut to the generated text.
        print(inline_response.response.text)
```

### JavaScript

```
import {GoogleGenAI, Type} from '@google/genai';

const ai = new GoogleGenAI({});

const inlinedRequests = [
    {
        contents: [{
            parts: [{text: 'List a few popular cookie recipes, and include the amounts of ingredients.'}],
            role: 'user'
        }],
        config: {
            responseMimeType: 'application/json',
            responseSchema: {
            type: Type.ARRAY,
            items: {
                type: Type.OBJECT,
                properties: {
                'recipeName': {
                    type: Type.STRING,
                    description: 'Name of the recipe',
                    nullable: false,
                },
                'ingredients': {
                    type: Type.ARRAY,
                    items: {
                    type: Type.STRING,
                    description: 'Ingredients of the recipe',
                    nullable: false,
                    },
                },
                },
                required: ['recipeName'],
            },
            },
        }
    },
    {
        contents: [{
            parts: [{text: 'List a few popular gluten free cookie recipes, and include the amounts of ingredients.'}],
            role: 'user'
        }],
        config: {
            responseMimeType: 'application/json',
            responseSchema: {
            type: Type.ARRAY,
            items: {
                type: Type.OBJECT,
                properties: {
                'recipeName': {
                    type: Type.STRING,
                    description: 'Name of the recipe',
                    nullable: false,
                },
                'ingredients': {
                    type: Type.ARRAY,
                    items: {
                    type: Type.STRING,
                    description: 'Ingredients of the recipe',
                    nullable: false,
                    },
                },
                },
                required: ['recipeName'],
            },
            },
        }
    }
]

const inlinedBatchJob = await ai.batches.create({
    model: 'gemini-3.8-flash',
    src: inlinedRequests,
    config: {
        displayName: 'inlined-requests-job-1',
    }
});
```

### Java

```
import java.util.HashMap;
import java.util.HashSet;
import java.util.Arrays;
import java.util.Collections;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.Content;
import com.google.genai.types.CreateBatchJobConfig;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.InlinedResponse;
import com.google.genai.types.JobState;
import com.google.genai.types.Part;
import com.google.genai.types.Schema;
import com.google.genai.types.Type;
import java.util.List;
import java.util.Map;
import java.util.Set;

Client client = new Client();

Map<String, Schema> properties = new HashMap<>();
properties.put("recipeName", Schema.builder().type(Type.Known.STRING).build());
properties.put(
    "ingredients",
    Schema.builder()
        .type(Type.Known.ARRAY)
        .items(Schema.builder().type(Type.Known.STRING).build())
        .build());

Schema recipeSchema =
    Schema.builder()
        .type(Type.Known.ARRAY)
        .items(
            Schema.builder()
                .type(Type.Known.OBJECT)
                .properties(
properties)
                .required("recipeName")
                .build())
        .build();

GenerateContentConfig jsonConfig =
    GenerateContentConfig.builder()
        .responseMimeType("application/json")
        .responseSchema(recipeSchema)
        .build();

List<InlinedRequest> inlineRequests =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.builder()
                        .role("user")
                        .parts(
                            Arrays.asList(
                                Part.fromText(
                                    "List a few popular cookie recipes, and include the amounts of ingredients.")))
                        .build()))
            .config(jsonConfig)
            .build(),
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.builder()
                        .role("user")
                        .parts(
                            Arrays.asList(
                                Part.fromText(
                                    "List a few popular gluten free cookie recipes, and include the amounts of ingredients.")))
                        .build()))
            .config(jsonConfig)
            .build());

BatchJob inlineBatchJob =
    client.batches.create(
        "gemini-3.8-flash",
        BatchJobSource.builder().inlinedRequests(inlineRequests).build(),
        CreateBatchJobConfig.builder().displayName("structured-output-job-1").build());

// Wait for the job to finish
String jobName = inlineBatchJob.name().get();
System.out.println("Polling status for job: " + jobName);

Set<JobState.Known> completedStates =
    new HashSet<>(Arrays.asList(
        JobState.Known.JOB_STATE_SUCCEEDED,
        JobState.Known.JOB_STATE_FAILED,
        JobState.Known.JOB_STATE_CANCELLED,
        JobState.Known.JOB_STATE_EXPIRED));

BatchJob batchJobInline = client.batches.get(jobName, null);
while (!completedStates.contains(batchJobInline.state().get().knownEnum())) {
  System.out.println(
      "Job not finished. Current state: " + batchJobInline.state().get() + ". Waiting 30 seconds...");
  Thread.sleep(30000);
  batchJobInline = client.batches.get(jobName, null);
}

System.out.println("Job finished with state: " + batchJobInline.state().get());

// Print the response
List<InlinedResponse> responses = batchJobInline.dest().get().inlinedResponses().orElse(Collections.emptyList());
for (int i = 0; i < responses.size(); i++) {
  System.out.println("\n--- Response " + (i + 1) + " ---");
  InlinedResponse inlineResponse = responses.get(i);
  if (inlineResponse.response().isPresent()) {
    System.out.println(inlineResponse.response().get().text());
  }
}
```

以下展示了此作业的输出示例：

```
--- Response 1 ---
[
  {
    "recipe_name": "Chocolate Chip Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "3/4 cup granulated sugar",
      "3/4 cup packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "2 1/4 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1/2 teaspoon salt",
      "1 1/2 cups chocolate chips"
    ]
  },
  {
    "recipe_name": "Oatmeal Raisin Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "1 cup packed light brown sugar",
      "1/2 cup granulated sugar",
      "2 large eggs",
      "1 teaspoon vanilla extract",
      "1 1/2 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1 teaspoon ground cinnamon",
      "1/2 teaspoon salt",
      "3 cups old-fashioned rolled oats",
      "1 cup raisins"
    ]
  },
  {
    "recipe_name": "Sugar Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "1 1/2 cups granulated sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "2 3/4 cups all-purpose flour",
      "1 teaspoon baking powder",
      "1/2 teaspoon salt"
    ]
  }
]

--- Response 2 ---
[
  {
    "recipe_name": "Gluten-Free Chocolate Chip Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "3/4 cup granulated sugar",
      "3/4 cup packed light brown sugar",
      "2 large eggs",
      "1 teaspoon vanilla extract",
      "2 1/4 cups gluten-free all-purpose flour blend (with xanthan gum)",
      "1 teaspoon baking soda",
      "1/2 teaspoon salt",
      "1 1/2 cups chocolate chips"
    ]
  },
  {
    "recipe_name": "Gluten-Free Peanut Butter Cookies",
    "ingredients": [
      "1 cup (250g) creamy peanut butter",
      "1/2 cup (100g) granulated sugar",
      "1/2 cup (100g) packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "1/2 teaspoon baking soda",
      "1/4 teaspoon salt"
    ]
  },
  {
    "recipe_name": "Gluten-Free Oatmeal Raisin Cookies",
    "ingredients": [
      "1/2 cup (1 stick) unsalted butter, softened",
      "1/2 cup granulated sugar",
      "1/2 cup packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "1 cup gluten-free all-purpose flour blend",
      "1/2 teaspoon baking soda",
      "1/2 teaspoon ground cinnamon",
      "1/4 teaspoon salt",
      "1 1/2 cups gluten-free rolled oats",
      "1/2 cup raisins"
    ]
  }
]
```

## 监控作业状态

使用创建批量作业时获得的操作名称轮询其状态。
批量作业的状态字段将指明其当前状态。批量作业可以处于以下状态之一：

- `JOB_STATE_PENDING`：作业已创建，正在等待服务处理。
- `JOB_STATE_RUNNING`：作业正在处理中。
- `JOB_STATE_SUCCEEDED`：作业已成功完成。您现在可以检索结果。
- `JOB_STATE_FAILED`：作业失败。如需了解详情，请查看错误详情。
- `JOB_STATE_CANCELLED`：作业已被用户取消。
- `JOB_STATE_EXPIRED`：作业已过期，因为其运行或待处理时间超过 48 小时。作业将没有任何结果可供检索。
  您可以尝试重新提交作业，或将请求拆分为较小的批量。

您可以定期轮询作业状态，以检查作业是否已完成。

### Python

```
import time
from google import genai

client = genai.Client()

# Use the name of the job you want to check
# e.g., inline_batch_job.name from the previous step
job_name = "YOUR_BATCH_JOB_NAME"  # (e.g. 'batches/your-batch-id')
batch_job = client.batches.get(name=job_name)

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

print(f"Polling status for job: {job_name}")
batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(30) # Wait for 30 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")
if batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
// Use the name of the job you want to check
// e.g., inlinedBatchJob.name from the previous step
let batchJob;
const completedStates = new Set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
]);

try {
    batchJob = await ai.batches.get({name: inlinedBatchJob.name});
    while (!completedStates.has(batchJob.state)) {
        console.log(`Current state: ${batchJob.state}`);
        // Wait for 30 seconds before polling again
        await new Promise(resolve => setTimeout(resolve, 30000));
        batchJob = await client.batches.get({ name: batchJob.name });
    }
    console.log(`Job finished with state: ${batchJob.state}`);
    if (batchJob.state === 'JOB_STATE_FAILED') {
        // The exact structure of `error` might vary depending on the SDK
        // This assumes `error` is an object with a `message` property.
        console.error(`Error: ${batchJob.state}`);
    }
} catch (error) {
    console.error(`An error occurred while polling job ${batchJob.name}:`, error);
}
```

### Java

```
import java.util.HashSet;
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.JobState;
import java.util.Set;

Client client = new Client();

// Use the name of the job you want to check
String jobName = "batches/your-batch-id";

Set<JobState.Known> completedStates =
    new HashSet<>(Arrays.asList(
        JobState.Known.JOB_STATE_SUCCEEDED,
        JobState.Known.JOB_STATE_FAILED,
        JobState.Known.JOB_STATE_CANCELLED,
        JobState.Known.JOB_STATE_EXPIRED));

System.out.println("Polling status for job: " + jobName);
BatchJob batchJob = client.batches.get(jobName, null);
while (!completedStates.contains(batchJob.state().get().knownEnum())) {
  System.out.println("Current state: " + batchJob.state().get());
  Thread.sleep(30000); // Wait for 30 seconds before polling again
  batchJob = client.batches.get(jobName, null);
}

System.out.println("Job finished with state: " + batchJob.state().get());
if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_FAILED) {
  System.out.println("Error: " + batchJob.error().orElse(null));
}
```

### 轮询和网络钩子

**厌倦了轮询？**Gemini 现在支持
[网络钩子](https://ai.google.dev/gemini-api/docs/webhooks?hl=zh-cn)异步处理补全。
您可以直接订阅 `batch.succeeded`，而不是持续调用
`GET / operations`，以便在异步或长时间运行的操作完成时，Gemini API 可以向您的服务器推送实时通知。

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.create(
    name="MyBatchWebhook",
    subscribed_events=["batch.succeeded", "batch.failed"],
    uri="https://my-api.com/gemini-callback",
)

print(f"Created webhook: {webhook.name}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createWebhook() {
  const webhook = await client.webhooks.create({
    name: "MyBatchWebhook",
    subscribed_events: ["batch.succeeded", "batch.failed"],
    uri: "https://my-api.com/gemini-callback",
  });

  console.log(`Created webhook: ${webhook.name}`);
}

createWebhook();
```

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.gaos.models.webhooks.Webhook;
import com.google.genai.gaos.models.webhooks.WebhookInput;
import com.google.genai.gaos.models.webhooks.WebhookSubscribedEvent;
import java.util.List;

Client client = new Client();

WebhookInput input =
    WebhookInput.builder()
        .name("MyBatchWebhook")
        .subscribedEvents(
            Arrays.asList(
                WebhookSubscribedEvent.BATCH_SUCCEEDED,
                WebhookSubscribedEvent.BATCH_FAILED))
        .uri("https://my-api.com/gemini-callback")
        .build();

Webhook webhook = client.webhooks.create(input).webhook().get();
System.out.println("Created webhook: " + webhook.name().orElse(""));
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks?webhook_id=my-example-webhook-123" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GOOGLE_API_KEY" \
  -d '{
    "name": "My Example Webhook",
    "uri": "https://my-api.com/gemini-callback",
    "subscribed_events": ["batch.succeeded", "batch.failed"]
  }'
```

## 检索结果

作业状态指明批量作业已成功后，结果将显示在 `response` 字段中。
默认情况下，批量作业结果会存储 6 周，然后永久删除，在此期间可供下载。

### Python

```
import json
from google import genai

client = genai.Client()

# Use the name of the job you want to check
# e.g., inline_batch_job.name from the previous step
job_name = "YOUR_BATCH_JOB_NAME"
batch_job = client.batches.get(name=job_name)

if batch_job.state.name == 'JOB_STATE_SUCCEEDED':

    # If batch job was created with a file
    if batch_job.dest and batch_job.dest.file_name:
        # Results are in a file
        result_file_name = batch_job.dest.file_name
        print(f"Results are in file: {result_file_name}")

        print("Downloading result file content...")
        file_content = client.files.download(file=result_file_name)
        # Process file_content (bytes) as needed
        print(file_content.decode('utf-8'))

    # If batch job was created with inline request
    # (for embeddings, use batch_job.dest.inlined_embed_content_responses)
    elif batch_job.dest and batch_job.dest.inlined_responses:
        # Results are inline
        print("Results are inline:")
        for i, inline_response in enumerate(batch_job.dest.inlined_responses):
            print(f"Response {i+1}:")
            if inline_response.response:
                # Accessing response, structure may vary.
                try:
                    print(inline_response.response.text)
                except AttributeError:
                    print(inline_response.response) # Fallback
            elif inline_response.error:
                print(f"Error: {inline_response.error}")
    else:
        print("No results found (neither file nor inline).")
else:
    print(f"Job did not succeed. Final state: {batch_job.state.name}")
    if batch_job.error:
        print(f"Error: {batch_job.error}")
```

### JavaScript

```
// Use the name of the job you want to check
// e.g., inlinedBatchJob.name from the previous step
const jobName = "YOUR_BATCH_JOB_NAME";

try {
    const batchJob = await ai.batches.get({ name: jobName });

    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        console.log('Found completed batch:', batchJob.displayName);
        console.log(batchJob);

        // If batch job was created with a file destination
        if (batchJob.dest?.fileName) {
            const resultFileName = batchJob.dest.fileName;
            console.log(`Results are in file: ${resultFileName}`);

            console.log("Downloading result file content...");
            const fileContentBuffer = await ai.files.download({ file: resultFileName });

            // Process fileContentBuffer (Buffer) as needed
            console.log(fileContentBuffer.toString('utf-8'));
        }

        // If batch job was created with inline responses
        else if (batchJob.dest?.inlinedResponses) {
            console.log("Results are inline:");
            for (let i = 0; i < batchJob.dest.inlinedResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    // Accessing response, structure may vary.
                    if (inlineResponse.response.text !== undefined) {
                        console.log(inlineResponse.response.text);
                    } else {
                        console.log(inlineResponse.response); // Fallback
                    }
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        }

        // If batch job was an embedding batch with inline responses
        else if (batchJob.dest?.inlinedEmbedContentResponses) {
            console.log("Embedding results found inline:");
            for (let i = 0; i < batchJob.dest.inlinedEmbedContentResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedEmbedContentResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    console.log(inlineResponse.response);
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        } else {
            console.log("No results found (neither file nor inline).");
        }
    } else {
        console.log(`Job did not succeed. Final state: ${batchJob.state}`);
        if (batchJob.error) {
            console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
        }
    }
} catch (error) {
    console.error(`An error occurred while processing job ${jobName}:`, error);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobDestination;
import com.google.genai.types.InlinedEmbedContentResponse;
import com.google.genai.types.InlinedResponse;
import com.google.genai.types.JobState;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

Client client = new Client();

// Use the name of the job you want to check
String jobName = "batches/your-batch-id";
BatchJob batchJob = client.batches.get(jobName, null);

if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_SUCCEEDED) {
  BatchJobDestination dest = batchJob.dest().orElse(null);

  // If batch job was created with a file destination
  if (dest != null && dest.fileName().isPresent()) {
    String resultFileName = dest.fileName().get();
    System.out.println("Results are in file: " + resultFileName);

    System.out.println("Downloading result file content...");
    client.files.download(resultFileName, "batch_results.jsonl", null);
    String fileContent = Files.readString(Paths.get("batch_results.jsonl"));
    System.out.println(fileContent);
  }
  // If batch job was created with inline requests
  else if (dest != null && dest.inlinedResponses().isPresent()) {
    System.out.println("Results are inline:");
    List<InlinedResponse> responses = dest.inlinedResponses().get();
    for (int i = 0; i < responses.size(); i++) {
      System.out.println("Response " + (i + 1) + ":");
      InlinedResponse inlineResponse = responses.get(i);
      if (inlineResponse.response().isPresent()) {
        System.out.println(inlineResponse.response().get().text());
      } else if (inlineResponse.error().isPresent()) {
        System.out.println("Error: " + inlineResponse.error().get());
      }
    }
  }
  // If batch job was an embedding batch with inline responses
  else if (dest != null && dest.inlinedEmbedContentResponses().isPresent()) {
    System.out.println("Embedding results found inline:");
    List<InlinedEmbedContentResponse> responses = dest.inlinedEmbedContentResponses().get();
    for (int i = 0; i < responses.size(); i++) {
      System.out.println("Response " + (i + 1) + ":");
      InlinedEmbedContentResponse inlineResponse = responses.get(i);
      if (inlineResponse.response().isPresent()) {
        System.out.println(inlineResponse.response().get());
      } else if (inlineResponse.error().isPresent()) {
        System.out.println("Error: " + inlineResponse.error().get());
      }
    }
  } else {
    System.out.println("No results found (neither file nor inline).");
  }
} else {
  System.out.println("Job did not succeed. Final state: " + batchJob.state().get());
  batchJob.error().ifPresent(err -> System.out.println("Error: " + err));
}
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" 2> /dev/null > batch_status.json

if jq -r '.done' batch_status.json | grep -q "false"; then
    echo "Batch has not finished processing"
fi

batch_state=$(jq -r '.metadata.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    if [[ $(jq '.response | has("inlinedResponses")' batch_status.json) = "true" ]]; then
        jq -r '.response.inlinedResponses' batch_status.json
        exit
    fi
    responses_file_name=$(jq -r '.response.responsesFile' batch_status.json)
    curl https://generativelanguage.googleapis.com/download/v1beta/$responses_file_name:download?alt=media \
    -H "x-goog-api-key: $GEMINI_API_KEY" 2> /dev/null
elif [[ $batch_state = "JOB_STATE_FAILED" ]]; then
    jq '.error' batch_status.json
elif [[ $batch_state == "JOB_STATE_CANCELLED" ]]; then
    echo "Batch was cancelled by the user"
elif [[ $batch_state == "JOB_STATE_EXPIRED" ]]; then
    echo "Batch expired after 48 hours"
fi
```

## 列出批量作业

您可以列出最近的批量作业。

### Python

```
batch_jobs = client.batches.list()

# Optional query config:
# batch_jobs = client.batches.list(config={'page_size': 5})

for batch_job in batch_jobs:
    print(batch_job)
```

### JavaScript

```
const batchJobs = await ai.batches.list();

// Optional query config:
// const batchJobs = await ai.batches.list({config: {'pageSize': 5}});

for await (const batchJob of batchJobs) {
    console.log(batchJob);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.Pager;
import com.google.genai.types.BatchJob;
import com.google.genai.types.ListBatchJobsConfig;

Client client = new Client();

Pager<BatchJob> batchJobs = client.batches.list(null);

// Optional query config:
// Pager<BatchJob> batchJobs = client.batches.list(ListBatchJobsConfig.builder().pageSize(5).build());

for (BatchJob batchJob : batchJobs) {
  System.out.println(batchJob);
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/batches \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## 取消批量作业

您可以使用批量作业的名称取消正在进行的批量作业。取消作业后，系统会停止处理新请求。

### Python

```
client.batches.cancel(name=batch_job_to_cancel.name)
```

### JavaScript

```
await ai.batches.cancel({name: batchJobToCancel.name});
```

### Java

```
import com.google.genai.Client;

Client client = new Client();

String batchJobToCancelName = "batches/your-batch-id";
client.batches.cancel(batchJobToCancelName, null);
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

# Cancel the batch
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME:cancel \
-H "x-goog-api-key: $GEMINI_API_KEY" \

# Confirm that the status of the batch after cancellation is JOB_STATE_CANCELLED
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" 2> /dev/null | jq -r '.metadata.state'
```

## 删除批量作业

您可以使用批量作业的名称删除现有批量作业。删除作业后，系统会停止处理新请求，并将其从批量作业列表中移除。

### Python

```
client.batches.delete(name=batch_job_to_delete.name)
```

### JavaScript

```
await ai.batches.delete({name: batchJobToDelete.name});
```

### Java

```
import com.google.genai.Client;

Client client = new Client();

String batchJobToDeleteName = "batches/your-batch-id";
client.batches.delete(batchJobToDeleteName, null);
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

# Delete the batch job
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## 批量生成图片

如果您使用的是 [Gemini Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)，并且需要生成大量
图片，则可以使用 Batch API 来获得更高
[的速率限制](https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-cn)，但周转时间最长为
24 小时。

您可以对小批量请求（不超过 20MB）使用[内嵌请求](#inline-requests-images)，也可以对大批量请求使用
[JSONL 输入文件](#input-file-images)（建议用于图片生成）：

### 图片的内嵌请求

### Python

```
import time
import base64
import json
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# 1. Create batch job with inline requests
inline_requests = [
    {
        'contents': [{'parts': [{'text': 'A big letter A surrounded by animals starting with the A letter'}]}],
        'config': {'response_modalities': ['TEXT', 'IMAGE']}
    },
    {
        'contents': [{'parts': [{'text': 'A big letter B surrounded by animals starting with the B letter'}]}],
        'config': {'response_modalities': ['TEXT', 'IMAGE']}
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3-pro-image-preview",
    src=inline_requests,
    config={
        'display_name': "inlined-image-requests-job-1",
    },
)

print(f"Created batch job: {inline_batch_job.name}")

# 2. Monitor job status
job_name = inline_batch_job.name
print(f"Polling status for job: {job_name}")

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(10) # Wait for 10 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")

# 3. Retrieve results
if batch_job.state.name == 'JOB_STATE_SUCCEEDED':
    print("Results are inline:")
    for i, inline_response in enumerate(batch_job.dest.inlined_responses):
        print(f"Response {i+1}:")
        if inline_response.response:
            for part in inline_response.response.candidates[0].content.parts:
                if part.text:
                    print(part.text)
                elif part.inline_data:
                    print(f"Image mime type: {part.inline_data.mime_type}")
                    image = part.as_image()
                    image.save(f"image_{i+1}.png")
        elif inline_response.error:
            print(f"Error: {inline_response.error}")
elif batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
    // 1. Create batch job with inline requests
    const inlinedRequests = [
        {
            contents: [{parts: [{text: 'A big letter A surrounded by animals starting with the A letter'}]}],
            config: {responseModalities: ['TEXT', 'IMAGE']}
        },
        {
            contents: [{parts: [{text: 'A big letter B surrounded by animals starting with the B letter'}]}],
            config: {responseModalities: ['TEXT', 'IMAGE']}
        }
    ]

    const inlineBatchJob = await ai.batches.create({
        model: 'gemini-3-pro-image-preview',
        src: inlinedRequests,
        config: {
            displayName: 'inlined-image-requests-job-1',
        }
    });

    console.log(inlineBatchJob);

    // 2. Monitor job status
    let batchJob;
    const completedStates = new Set([
        'JOB_STATE_SUCCEEDED',
        'JOB_STATE_FAILED',
        'JOB_STATE_CANCELLED',
        'JOB_STATE_EXPIRED',
    ]);

    try {
        batchJob = await ai.batches.get({name: inlineBatchJob.name});
        while (!completedStates.has(batchJob.state)) {
            console.log(`Current state: ${batchJob.state}`);
            // Wait for 10 seconds before polling again
            await new Promise(resolve => setTimeout(resolve, 10000));
            batchJob = await ai.batches.get({ name: batchJob.name });
        }
        console.log(`Job finished with state: ${batchJob.state}`);
    } catch (error) {
        console.error(`An error occurred while polling job ${inlineBatchJob.name}:`, error);
        return;
    }

    // 3. Retrieve results
    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        if (batchJob.dest?.inlinedResponses) {
            console.log("Results are inline:");
            for (let i = 0; i < batchJob.dest.inlinedResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    for (const part of inlineResponse.response.candidates[0].content.parts) {
                        if (part.text) {
                            console.log(part.text);
                        } else if (part.inlineData) {
                            console.log(`Image mime type: ${part.inlineData.mimeType}`);
                        }
                    }
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        } else {
            console.log("No inline results found.");
        }
    } else if (batchJob.state === 'JOB_STATE_FAILED') {
         console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
    }
}
run();
```

### Java

```
import java.util.HashSet;
import java.util.Arrays;
import java.util.Collections;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.Content;
import com.google.genai.types.CreateBatchJobConfig;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.InlinedResponse;
import com.google.genai.types.JobState;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Set;

Client client = new Client();

// 1. Create batch job with inline requests
GenerateContentConfig imageConfig =
    GenerateContentConfig.builder().responseModalities("TEXT", "IMAGE").build();

List<InlinedRequest> inlineRequests =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.fromParts(
                        Part.fromText(
                            "A big letter A surrounded by animals starting with the A letter"))))
            .config(imageConfig)
            .build(),
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.fromParts(
                        Part.fromText(
                            "A big letter B surrounded by animals starting with the B letter"))))
            .config(imageConfig)
            .build());

BatchJob inlineBatchJob =
    client.batches.create(
        "gemini-3-pro-image-preview",
        BatchJobSource.builder().inlinedRequests(inlineRequests).build(),
        CreateBatchJobConfig.builder().displayName("inlined-image-requests-job-1").build());

System.out.println("Created batch job: " + inlineBatchJob.name().orElse(""));

// 2. Monitor job status
String jobName = inlineBatchJob.name().get();
System.out.println("Polling status for job: " + jobName);

Set<JobState.Known> completedStates =
    new HashSet<>(Arrays.asList(
        JobState.Known.JOB_STATE_SUCCEEDED,
        JobState.Known.JOB_STATE_FAILED,
        JobState.Known.JOB_STATE_CANCELLED,
        JobState.Known.JOB_STATE_EXPIRED));

BatchJob batchJob = client.batches.get(jobName, null);
while (!completedStates.contains(batchJob.state().get().knownEnum())) {
  System.out.println("Current state: " + batchJob.state().get());
  Thread.sleep(10000); // Wait for 10 seconds before polling again
  batchJob = client.batches.get(jobName, null);
}

System.out.println("Job finished with state: " + batchJob.state().get());

// 3. Retrieve results
if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_SUCCEEDED) {
  System.out.println("Results are inline:");
  List<InlinedResponse> responses = batchJob.dest().get().inlinedResponses().orElse(Collections.emptyList());
  for (int i = 0; i < responses.size(); i++) {
    System.out.println("Response " + (i + 1) + ":");
    InlinedResponse inlineResponse = responses.get(i);
    if (inlineResponse.response().isPresent()) {
      for (Part part : inlineResponse.response().get().parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          System.out.println("Image mime type: " + part.inlineData().get().mimeType().orElse(""));
          Files.write(
              Paths.get("image_" + (i + 1) + ".png"),
              part.inlineData().get().data().get());
        }
      }
    } else if (inlineResponse.error().isPresent()) {
      System.out.println("Error: " + inlineResponse.error().get());
    }
  }
} else if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_FAILED) {
  System.out.println("Error: " + batchJob.error().orElse(null));
}
```

### REST

```
# 1. Create batch job
printf -v request_data '{
    "batch": {
        "display_name": "my-batch-image-requests",
        "input_config": {
            "requests": {
                "requests": [
                    {
                        "request": {
                            "contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}],
                            "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}
                        },
                        "metadata": { "key": "request-1" }
                    },
                    {
                        "request": {
                            "contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}],
                            "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}
                        },
                        "metadata": { "key": "request-2" }
                    }
                ]
            }
        }
    }
}'
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:batchGenerateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type:application/json" \
  -d "$request_data" > created_batch.json

BATCH_NAME=$(jq -r '.name' created_batch.json)
echo "Created batch job: $BATCH_NAME"

# 2. Poll job status until completion by repeating the following command
# Replace $BATCH_NAME with the name returned above.
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" > batch_status.json

echo "Current status:"
jq '.' batch_status.json

# 3. If state is JOB_STATE_SUCCEEDED, retrieve results from batch_status.json
batch_state=$(jq -r '.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    echo "Job succeeded. Results:"
    jq -r '.dest.inlinedResponses' batch_status.json
fi
```

### 图片的输入文件

### Python

```
import json
import time
import base64
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# 1. Create and upload file
file_name = "my-batch-image-requests.jsonl"
with open(file_name, "w") as f:
    requests = [
        {"key": "request-1", "request": {"contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}},
        {"key": "request-2", "request": {"contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}
    ]
    for req in requests:
        f.write(json.dumps(req) + "\n")

uploaded_file = client.files.upload(
    file=file_name,
    config=types.UploadFileConfig(display_name='my-batch-image-requests', mime_type='jsonl')
)
print(f"Uploaded file: {uploaded_file.name}")

# 2. Create batch job
file_batch_job = client.batches.create(
    model="gemini-3-pro-image-preview",
    src=uploaded_file.name,
    config={
        'display_name': "file-image-upload-job-1",
    },
)
print(f"Created batch job: {file_batch_job.name}")

# 3. Monitor job status
job_name = file_batch_job.name
print(f"Polling status for job: {job_name}")

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(10) # Wait for 10 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")

# 4. Retrieve results
if batch_job.state.name == 'JOB_STATE_SUCCEEDED':
    result_file_name = batch_job.dest.file_name
    print(f"Results are in file: {result_file_name}")
    print("Downloading result file content...")
    file_content_bytes = client.files.download(file=result_file_name)
    file_content = file_content_bytes.decode('utf-8')
    # The result file is also a JSONL file. Parse and print each line.
    for line in file_content.splitlines():
      if line:
        parsed_response = json.loads(line)
        if 'response' in parsed_response and parsed_response['response']:
            for part in parsed_response['response']['candidates'][0]['content']['parts']:
              if part.get('text'):
                print(part['text'])
              elif part.get('inlineData'):
                print(f"Image mime type: {part['inlineData']['mimeType']}")
                data = base64.b64decode(part['inlineData']['data'])
        elif 'error' in parsed_response:
            print(f"Error: {parsed_response['error']}")
elif batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from 'url';

const ai = new GoogleGenAI({});

async function run() {
    // 1. Create and upload file
    const fileName = "my-batch-image-requests.jsonl";
    const requests = [
        { "key": "request-1", "request": { "contents": [{ "parts": [{ "text": "A big letter A surrounded by animals starting with the A letter" }] }], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]} } },
        { "key": "request-2", "request": { "contents": [{ "parts": [{ "text": "A big letter B surrounded by animals starting with the B letter" }] }], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]} } }
    ];
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    const filePath = path.join(__dirname, fileName);

    try {
        const writeStream = fs.createWriteStream(filePath, { flags: 'w' });
        for (const req of requests) {
            writeStream.write(JSON.stringify(req) + '\n');
        }
        writeStream.end();
        console.log(`Successfully wrote batch requests to ${filePath}`);
    } catch (error) {
        console.error(`An unexpected error occurred writing file:`, error);
        return;
    }

    const uploadedFile = await ai.files.upload({file: fileName, config: { mimeType: 'jsonl' }});
    console.log(`Uploaded file: ${uploadedFile.name}`);

    // 2. Create batch job
    const fileBatchJob = await ai.batches.create({
        model: 'gemini-3-pro-image-preview',
        src: uploadedFile.name,
        config: {
            displayName: 'file-image-upload-job-1',
        }
    });
    console.log(fileBatchJob);

    // 3. Monitor job status
    let batchJob;
    const completedStates = new Set([
        'JOB_STATE_SUCCEEDED',
        'JOB_STATE_FAILED',
        'JOB_STATE_CANCELLED',
        'JOB_STATE_EXPIRED',
    ]);

    try {
        batchJob = await ai.batches.get({name: fileBatchJob.name});
        while (!completedStates.has(batchJob.state)) {
            console.log(`Current state: ${batchJob.state}`);
            // Wait for 10 seconds before polling again
            await new Promise(resolve => setTimeout(resolve, 10000));
            batchJob = await ai.batches.get({ name: batchJob.name });
        }
        console.log(`Job finished with state: ${batchJob.state}`);
    } catch (error) {
        console.error(`An error occurred while polling job ${fileBatchJob.name}:`, error);
        return;
    }

    // 4. Retrieve results
    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        if (batchJob.dest?.fileName) {
            const resultFileName = batchJob.dest.fileName;
            console.log(`Results are in file: ${resultFileName}`);
            console.log("Downloading result file content...");
            const fileContentBuffer = await ai.files.download({ file: resultFileName });
            const fileContent = fileContentBuffer.toString('utf-8');
            for (const line of fileContent.split('\n')) {
                if (line) {
                    const parsedResponse = JSON.parse(line);
                    if (parsedResponse.response) {
                        for (const part of parsedResponse.response.candidates[0].content.parts) {
                            if (part.text) {
                                console.log(part.text);
                            } else if (part.inlineData) {
                                console.log(`Image mime type: ${part.inlineData.mimeType}`);
                            }
                        }
                    } else if (parsedResponse.error) {
                        console.error(`Error: ${parsedResponse.error}`);
                    }
                }
            }
        } else {
            console.log("No result file found.");
        }
    } else if (batchJob.state === 'JOB_STATE_FAILED') {
         console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
    }
}
run();
```

### Java

```
import java.util.HashSet;
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.CreateBatchJobConfig;
import com.google.genai.types.File;
import com.google.genai.types.JobState;
import com.google.genai.types.UploadFileConfig;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Set;

Client client = new Client();

// 1. Create and upload file
String fileName = "my-batch-image-requests.jsonl";
List<String> requests =
    Arrays.asList(
        "{\"key\": \"request-1\", \"request\": {\"contents\": [{\"parts\": [{\"text\": \"A big letter A surrounded by animals starting with the A letter\"}]}], \"generation_config\": {\"responseModalities\": [\"TEXT\", \"IMAGE\"]}}}",
        "{\"key\": \"request-2\", \"request\": {\"contents\": [{\"parts\": [{\"text\": \"A big letter B surrounded by animals starting with the B letter\"}]}], \"generation_config\": {\"responseModalities\": [\"TEXT\", \"IMAGE\"]}}}");
Files.write(Paths.get(fileName), requests);

File uploadedFile =
    client.files.upload(
        fileName,
        UploadFileConfig.builder()
            .displayName("my-batch-image-requests")
            .mimeType("jsonl")
            .build());
System.out.println("Uploaded file: " + uploadedFile.name().orElse(""));

// 2. Create batch job
BatchJob fileBatchJob =
    client.batches.create(
        "gemini-3-pro-image-preview",
        BatchJobSource.builder().fileName(uploadedFile.name().get()).build(),
        CreateBatchJobConfig.builder().displayName("file-image-upload-job-1").build());
System.out.println("Created batch job: " + fileBatchJob.name().orElse(""));

// 3. Monitor job status
String jobName = fileBatchJob.name().get();
System.out.println("Polling status for job: " + jobName);

Set<JobState.Known> completedStates =
    new HashSet<>(Arrays.asList(
        JobState.Known.JOB_STATE_SUCCEEDED,
        JobState.Known.JOB_STATE_FAILED,
        JobState.Known.JOB_STATE_CANCELLED,
        JobState.Known.JOB_STATE_EXPIRED));

BatchJob batchJob = client.batches.get(jobName, null);
while (!completedStates.contains(batchJob.state().get().knownEnum())) {
  System.out.println("Current state: " + batchJob.state().get());
  Thread.sleep(10000); // Wait for 10 seconds before polling again
  batchJob = client.batches.get(jobName, null);
}

System.out.println("Job finished with state: " + batchJob.state().get());

// 4. Retrieve results
if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_SUCCEEDED) {
  String resultFileName = batchJob.dest().get().fileName().get();
  System.out.println("Results are in file: " + resultFileName);
  System.out.println("Downloading result file content...");
  client.files.download(resultFileName, "batch_image_results.jsonl", null);
  for (String line : Files.readAllLines(Paths.get("batch_image_results.jsonl"))) {
    if (!line.isEmpty()) {
      System.out.println(line);
    }
  }
} else if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_FAILED) {
  System.out.println("Error: " + batchJob.error().orElse(null));
}
```

### REST

```
# 1. Create and upload file
echo '{"key": "request-1", "request": {"contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}' > my-batch-image-requests.jsonl
echo '{"key": "request-2", "request": {"contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}' >> my-batch-image-requests.jsonl

# Follow File API guide to upload: https://ai.google.dev/gemini-api/docs/files#upload_a_file
# This example assumes you have uploaded the file and set BATCH_INPUT_FILE to its name (e.g., files/abcdef123)
BATCH_INPUT_FILE="files/your-uploaded-file-name"

# 2. Create batch job
printf -v request_data '{
    "batch": {
        "display_name": "my-batch-file-image-requests",
        "input_config": { "file_name": "%s" }
    }
}' "$BATCH_INPUT_FILE"
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:batchGenerateContent \
  -X POST \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" \
  -d "$request_data" > created_batch.json

BATCH_NAME=$(jq -r '.name' created_batch.json)
echo "Created batch job: $BATCH_NAME"

# 3. Poll job status until completion by repeating the following command:
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" > batch_status.json

echo "Current status:"
jq '.' batch_status.json

# 4. If state is JOB_STATE_SUCCEEDED, download results file
batch_state=$(jq -r '.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    responses_file_name=$(jq -r '.dest.fileName' batch_status.json)
    echo "Job succeeded. Downloading results from $responses_file_name..."
    curl https://generativelanguage.googleapis.com/download/v1beta/$responses_file_name:download?alt=media \
      -H "x-goog-api-key: $GEMINI_API_KEY" > batch_results.jsonl
    echo "Results saved to batch_results.jsonl"
fi
```

## 技术详情

- **支持的模型** ：Batch API 支持一系列 Gemini 模型。
  如需了解每个模型对 Batch API 的支持情况，请参阅[模型页面](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)
  。Batch API 支持的模态与交互式（或非批量）API 支持的模态相同。
- **价格** ：Batch API 的使用费用为同等模型的标准交互式 API 费用的 50%。如需了解详情，请参阅[价格页面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)
  。如需详细了解此功能的速率限制，请参阅[速率限制页面](https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-cn#batch-mode)
  。
- **服务等级目标 (SLO)** ：批量作业旨在在 24 小时内完成。许多作业可能会根据其大小和当前系统负载更快完成。
- **缓存**：[上下文缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)支持批量请求
  。如需重复使用缓存的内容，请在批量中各个请求的配置中指定 `cached_content` 资源名称。
  如果批量中的请求导致缓存命中，您需要支付
  [标准上下文缓存费率](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)。

## 最佳做法

- **对大型请求使用输入文件**：对于大量请求，
  请始终使用文件输入
  方法，以便更好地进行管理，并避免达到
  [`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=zh-cn#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
  调用本身的请求大小限制。请注意，每个输入文件的文件大小限制为 2GB。
- **错误处理** ：作业完成后，检查 `batchStats` 中的 `failedRequestCount`。如果使用文件输出，请解析每一行，以检查其是否为 `GenerateContentResponse` 或指明特定请求错误的 status 对象。如需查看完整的错误代码集，请参阅[问题排查
  指南](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=zh-cn#error-codes)。
- **一次性提交作业** ：批量作业的创建不是幂等的。
  如果您两次发送相同的创建请求，系统将创建两个单独的批量作业。
- **拆分非常大的批量** ：虽然目标周转时间为 24 小时，但实际处理时间可能会因系统负载和作业大小而异。
  对于大型作业，如果需要更快获得中间结果，请考虑将其拆分为较小的批量。

## 后续步骤

- 如需查看更多示例，请参阅[Batch API 笔记本](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb?hl=zh-cn)
  。
- OpenAI 兼容性层支持 Batch API。请参阅
  [OpenAI 兼容性](https://ai.google.dev/gemini-api/docs/openai?hl=zh-cn#batch)页面上的示例。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-18。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-18。"],[],[]]
