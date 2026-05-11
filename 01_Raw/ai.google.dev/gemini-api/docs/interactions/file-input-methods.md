---
source_url: https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=zh-CN
fetched_at: 2026-05-11T12:37:31.344853+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 文件输入方法

本指南介绍了在向 Gemini API 发出请求时，您可以通过哪些不同的方式添加媒体文件，例如图片、音频、视频和文档。所有 Gemini API 端点（包括 Batch、Interactions 和 Live API）均支持这些新方法。
选择正确的方法取决于文件的大小、数据的存储位置以及您计划使用该文件的频率。

将文件作为输入内容包含在提示中最简单的方法是读取本地文件，然后将其包含在提示中。以下示例展示了如何读取本地 PDF 文件。对于此方法，PDF 的大小上限为 50MB。如需查看文件输入类型和限制的完整列表，请参阅[输入法比较表](#method-comparison)。

### Python

```
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = 'my_local_file.pdf';

    const interaction = await client.interactions.create({
        model: "gemini-3-flash-preview",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: fs.readFileSync(filePath).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    const modelStep = interaction.steps.find(s => s.type === 'model_output');
    if (modelStep) {
      for (const contentBlock of modelStep.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "Summarize this document"},
      {
        "type": "document",
        "data": "'${B64_CONTENT}'",
        "mime_type": "application/pdf"
      }
    ]
  }'
```

## 输入法比较

下表比较了每种输入方法的文件限制和最佳使用情形。请注意，文件大小限制可能会因文件类型以及用于处理文件的模型或分词器而异。

| 方法 | 适用场景 | 文件大小的最大值 | 持久性 |
| --- | --- | --- | --- |
| **内嵌数据** | 快速测试、小文件、实时应用。 | 每个请求或载荷 100 MB  （**PDF 为 50 MB**） | 无（随每个请求发送） |
| **文件 API 上传** | 大型文件、多次使用的文件。 | 每个文件 2 GB， 每个项目最多 20 GB | 48 小时 |
| **文件 API GCS URI 注册** | 已在 Google Cloud Storage 中的大型文件、多次使用的文件。 | 每个文件的大小上限为 2 GB，没有总体存储空间限制 | 无（按请求提取）。一次性注册可提供长达 30 天的访问权限。 |
| **外部网址** | 公共数据或云端存储分区 (AWS、Azure、GCS) 中的数据，无需重新上传。 | 每个请求/载荷 100 MB | 无（按请求提取） |

## 内嵌数据

对于较小的文件（小于 100MB，如果是 PDF 文件则小于 50MB），您可以直接在请求载荷中传递数据。这是最简单的方法，适用于快速测试或处理实时瞬态数据的应用。您可以提供 base64 编码的字符串形式的数据，也可以直接读取本地文件。

如需查看从本地文件读取数据的示例，请参阅本页开头的示例。

### 通过网址提取

您还可以从网址中提取文件，将其转换为字节，然后将其包含在输入中。

### Python

```
from google import genai
import httpx
import base64

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const interaction = await client.interactions.create({
        model: "gemini-3-flash-preview",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: Buffer.from(pdfResp).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    const modelStep = interaction.steps.find(s => s.type === 'model_output');
    if (modelStep) {
      for (const contentBlock of modelStep.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
}

main();
```

### REST

```
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Create JSON payload file
cat <<EOF > payload.json
{
"model": "gemini-3-flash-preview",
"input": [
{"type": "document", "data": "${ENCODED_PDF}", "mime_type": "application/pdf"},
{"type": "text", "text": "${PROMPT}"}
]
}
EOF

# Generate content using interactions
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Gemini File API

File API 专为较大文件（最大 2GB）或您打算在多个请求中使用的文件而设计。

### 标准文件上传

将本地文件上传到 Gemini API。以这种方式上传的文件会暂时存储（48 小时），并经过处理，以便模型高效检索。

### Python

```
from google import genai

client = genai.Client()

# Upload the file
doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

# Use the uploaded file in an interaction
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
  const filePath = "path/to/your/sample.pdf";

  const myfile = await client.files.upload({
    file: filePath,
    config: { mime_type: "application/pdf" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  const modelStep = interaction.steps.find(s => s.type === 'model_output');
  if (modelStep) {
    for (const contentBlock of modelStep.content) {
      if (contentBlock.type === 'text') console.log(contentBlock.text);
    }
  }
}

await main();
```

### REST

```
FILE_PATH="path/to/sample.pdf"
MIME_TYPE=$(file -b --mime-type "${FILE_PATH}")
NUM_BYTES=$(wc -c < "${FILE_PATH}")
DISPLAY_NAME=DOCUMENT

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -D "${tmp_header_file}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${FILE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)

# Now use in an interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### 注册 Google Cloud Storage 文件

如果您的数据已在 Google Cloud Storage 中，则无需下载并重新上传。您可以直接使用 File API 注册该服务。

1. 向**服务代理**授予对每个存储分区的访问权限

   1. 在您的 Google Cloud 云项目中启用 Gemini API。
   2. 创建服务代理：

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **向 Gemini API 服务代理授予读取存储分区的权限**。

      用户需要在他们打算使用的特定存储分区中，为此服务代理分配 `Storage Object Viewer`
      [IAM 角色](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=zh-cn#storage.objectViewer)。

   此访问权限默认不会过期，但可以随时更改。您还可以使用 [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=zh-cn) 命令授予权限。
2. 对您的服务进行身份验证

   **前提条件**

   - 启用 API
   - 创建具有适当权限的服务账号或代理。

   您首先需要以具有存储分区对象查看者权限的服务进行身份验证。具体如何实现取决于文件管理代码将运行的环境。

   **Google Cloud 外部**

   如果您的代码在 Google Cloud 之外（例如在桌面设备上）运行，请按照以下步骤从 Google Cloud 控制台中下载账号凭据：

   1. 浏览到[服务账号控制台](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=zh-cn)
   2. 选择相关服务账号
   3. 选择**密钥**标签页，然后选择**添加密钥、创建新密钥**
   4. 选择 **JSON** 密钥类型，并记下文件下载到您计算机上的哪个位置。

   如需了解详情，请参阅有关[服务账号密钥管理](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=zh-cn)的官方 Google Cloud 文档。

   然后使用以下命令进行身份验证。这些命令假设您的服务账号文件位于当前目录中，且名为 `service-account.json`。

   ### Python

   ```
   from google.oauth2.service_account import Credentials

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   SERVICE_ACCOUNT_FILE = 'service-account.json'

   credentials = Credentials.from_service_account_file(
       SERVICE_ACCOUNT_FILE,
       scopes=GCS_READ_SCOPES
   )
   ```

   ### JavaScript

   ```
   const { GoogleAuth } = require('google-auth-library');

   const GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ];

   const SERVICE_ACCOUNT_FILE = 'service-account.json';

   const auth = new GoogleAuth({
     keyFile: SERVICE_ACCOUNT_FILE,
     scopes: GCS_READ_SCOPES
   });
   ```

   ### CLI

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **在 Google Cloud 上**

   如果您直接在 Google Cloud 中运行（例如使用 [Cloud Run 函数](https://cloud.google.com/functions?hl=zh-cn)或 [Compute Engine 实例](https://cloud.google.com/products/compute?hl=zh-cn)），则会拥有隐式凭据，但需要重新进行身份验证以授予适当的范围。

   ### Python

   此代码假定服务在可以自动获取[应用默认凭证](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=zh-cn)的环境中运行，例如 Cloud Run 或 Compute Engine。

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   此代码假定服务在可以自动获取[应用默认凭证](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=zh-cn)的环境中运行，例如 Cloud Run 或 Compute Engine。

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

   ### CLI

   这是一个互动式命令。对于 Compute Engine 等服务，您可以在配置级层将范围附加到正在运行的服务。如需查看示例，请参阅[用户管理的服务文档](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=zh-cn#using)。

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. 文件注册（Files API）

   使用 Files API 注册文件，并生成可直接在 Gemini API 中使用的 Files API 路径。

   ### Python

   ```
   from google import genai

   # Note that you must provide an API key in the GEMINI_API_KEY
   # environment variable, but it is unused for the registration endpoint.
   client = genai.Client(credentials=credentials)

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
   )
   prompt = "Summarize this file."

   # call interactions.create for each file
   for f in registered_gcs_files.files:
     print(f.name)
     interaction = client.interactions.create(
       model="gemini-3-flash-preview",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     # Print the model's text response
     for step in interaction.steps:
         if step.type == "model_output":
             for content_block in step.content:
                 if content_block.type == "text":
                     print(content_block.text)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI } from "@google/genai";

   const ai = new GoogleGenAI({ auth: auth });

   async function main() {
       const registeredGcsFiles = await ai.files.registerFiles({
           uris: ["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
       });

       const prompt = "Summarize this file.";

       for (const file of registeredGcsFiles.files) {
           console.log(file.name);
           const interaction = await ai.interactions.create({
               model: "gemini-3-flash-preview",
               input: [
                   { type: "text", text: prompt },
                   { type: "document", uri: file.uri, mime_type: file.mimeType }
               ]
           });

           const modelStep = interaction.steps.find(s => s.type === 'model_output');
           if (modelStep) {
               for (const contentBlock of modelStep.content) {
                   if (contentBlock.type === 'text') console.log(contentBlock.text);
               }
           }
       }
   }

   main();
   ```

   ### CLI

   ```
   access_token=$(gcloud auth application-default print-access-token)
   project_id=$(gcloud config get-value project)
   curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
       -H 'Content-Type: application/json' \
       -H "Authorization: Bearer ${access_token}" \
       -H "x-goog-user-project: ${project_id}" \
       -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
   ```

## 外部 HTTP / 签名网址

您可以在请求中直接传递可公开访问的 HTTPS 网址或预签名网址。Gemini API 会在处理过程中安全地提取内容。
此功能非常适合不想重新上传的 100MB 以下的文件。

### Python

```
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: "document", uri: uri, mime_type: "application/pdf" },
      { type: "text", text: "summarize this file" }
    ]
  });

  const modelStep = interaction.steps.find(s => s.type === 'model_output');
  if (modelStep) {
    for (const contentBlock of modelStep.content) {
      if (contentBlock.type === 'text') console.log(contentBlock.text);
    }
  }
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "model": "gemini-3-flash-preview",
          "input": [
            {"type": "text", "text": "Summarize this pdf"},
            {
              "type": "document",
              "uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf",
              "mime_type": "application/pdf"
            }
          ]
        }'
```

### 无障碍

验证您提供的网址是否不会指向需要登录或位于付费墙后的网页。对于私密数据库，请确保您创建的签名网址具有正确的访问权限和到期时间。

### 安全检查

系统会对网址进行内容审核检查，以确认其符合安全和政策标准。如果网址未通过此检查，您将获得 `URL_RETRIEVAL_STATUS_UNSAFE` 的 `url_retrieval_status`。

### 支持的内容类型

此支持的文件类型和限制列表仅为初步指南，并不全面。支持的有效类型集可能会发生变化，并且会因所用的具体模型和分词器版本而异。不支持的类型会导致错误。
此外，对于这些文件类型，内容检索仅支持可公开访问的网址。

#### 文本文件类型

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### 应用文件类型

- `application/json`
- `application/pdf`

#### 图片文件类型

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

## 最佳做法

- **选择合适的方法**：对于小型临时文件，请使用内嵌数据。
  对于较大或经常使用的文件，请使用 File API。使用已在线托管的数据的外部网址。
- **指定 MIME 类型**：请务必为文件数据提供正确的 MIME 类型，以确保正确处理。
- **处理错误**：在代码中实现错误处理，以管理潜在问题，例如网络故障、文件访问问题或 API 错误。

## 限制

- 文件大小限制因方法（请参阅[对照表](#method-comparison)）和文件类型而异。
- 内嵌数据会增加请求载荷大小。
- File API 上传是临时性的，会在 48 小时后过期。
- 外部网址提取功能限制为每个载荷 100 MB，并支持特定内容类型。

## 后续步骤

- 不妨使用 [Google AI Studio](http://aistudio.google.com/?hl=zh-cn) 尝试自行撰写多模态提示。
- 如需了解如何在提示中添加文件，请参阅 [Vision](https://ai.google.dev/gemini-api/docs/interactions/vision?hl=zh-cn)、[Audio](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=zh-cn) 和[文档处理](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=zh-cn)指南。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-09。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-09。"],[],[]]
