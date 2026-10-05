---
source_url: https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-TW
fetched_at: 2026-10-05T06:34:25.727571+00:00
title: "\u6587\u4ef6\u89e3\u8b80 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 文件解讀

Gemini 模型可以處理 PDF 格式的文件，並運用原生視覺功能解讀整份文件的內容。這項功能不僅能擷取文字，還可讓 Gemini 執行下列動作：

- 分析及解讀內容，包括文字、圖片、圖表、圖表和表格，即使是長達 1000 頁的文件也沒問題。
- 以[結構化輸出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw)格式擷取資訊。
- 根據文件中的視覺和文字元素摘要內容及回答問題。
- 轉錄文件內容 (例如轉錄為 HTML)，保留版面配置和格式，供下游應用程式使用。

您也可以用相同方式傳送非 PDF 文件，但 Gemini 會將這些文件視為一般文字，因此不會顯示圖表或格式等脈絡資訊。

## 內嵌傳遞 PDF 資料

您可以在要求中內嵌傳遞 PDF 資料。這種方法最適合用於小型文件或臨時處理，因為您不需要在後續要求中參照該檔案。如果文件較大，建議使用 [Files API](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-tw#large-pdfs)，以便在多輪互動中參照文件，進而縮短要求延遲時間並減少頻寬用量。

以下範例說明如何內嵌傳遞 PDF 資料：

### Python

```
from google import genai
import base64

client = genai.Client()

with open('path/to/document.pdf', 'rb') as f:
    pdf_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "document",
            "data": base64.b64encode(pdf_bytes).decode('utf-8'),
            "mime_type": "application/pdf"
        },
        {"type": "text", "text": "Summarize this document"}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function main() {
    const pdfData = fs.readFileSync("path/to/document.pdf", {
        encoding: "base64"
    });

    const interaction = await ai.interactions.create({
        model: "gemini-3.8-flash",
        input: [
            { type: "text", text: "Summarize this document" },
            {
                type: "document",
                data: pdfData,
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] pdfBytes = Files.readAllBytes(Paths.get("path/to/document.pdf"));
String base64Pdf = Base64.getEncoder().encodeToString(pdfBytes);

Content docContent =
    DocumentContent.builder()
        .data(base64Pdf)
        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
        .build();
Content textContent = TextContent.builder().text("Summarize this document").build();

List<Content> contents = Arrays.asList(docContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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

    pdfBytes, err := os.ReadFile("path/to/document.pdf")
    if err != nil {
        log.Fatal(err)
    }
    base64Pdf := base64.StdEncoding.EncodeToString(pdfBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    Data:     genai.Ptr(base64Pdf),
                    MimeType: interactions.DocumentContentMimeTypeApplicationPdf.ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: "Summarize this document",
                }),
            }),
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
PDF_PATH="path/to/document.pdf"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "document",
        "data": "'$(base64 $B64FLAGS $PDF_PATH)'",
        "mime_type": "application/pdf"
      },
      {"type": "text", "text": "Summarize this document"}
    ]
  }'
```

你也可以上傳本機 PDF 檔案進行處理：

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="file.pdf")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type},
        {"type": "text", "text": "Summarize this document"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
    const uploadedFile = await ai.files.upload({
        file: "file.pdf",
        config: { mime_type: "application/pdf" }
    });

    const interaction = await ai.interactions.create({
        model: "gemini-3.8-flash",
        input: [
            { type: "text", text: "Summarize this document" },
            {
                type: "document",
                uri: uploadedFile.uri,
                mime_type: uploadedFile.mime_type
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File uploadedFile =
    client.files.upload(
        new java.io.File("file.pdf"),
        UploadFileConfig.builder().mimeType("application/pdf").build());

Content docContent =
    DocumentContent.builder()
        .uri(uploadedFile.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(uploadedFile.mimeType().orElse("application/pdf")))
        .build();
Content textContent = TextContent.builder().text("Summarize this document").build();

List<Content> contents = Arrays.asList(docContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
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

    uploadedFile, err := client.Files.UploadFromPath(ctx, "file.pdf", &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(uploadedFile.URI),
                    MimeType: interactions.DocumentContentMimeType(uploadedFile.MIMEType).ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: "Summarize this document",
                }),
            }),
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
PDF_PATH="file.pdf"
NUM_BYTES=$(wc -c < "${PDF_PATH}")
DISPLAY_NAME="file.pdf"
tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: application/pdf" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${PDF_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now create an interaction using that file
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "document", "uri": "'$file_uri'", "mime_type": "application/pdf"},
        {"type": "text", "text": "Summarize this document"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq -r ".steps[-1].content[0].text" response.json
```

## 使用 Files API 上傳 PDF

如果檔案較大，或您打算在多個要求中重複使用文件，建議使用 Files API。這項功能可將檔案上傳作業與模型要求分離，藉此縮短要求延遲時間並減少頻寬用量。

### 透過網址上傳大型 PDF 檔案

使用 File API 簡化從網址上傳及處理大型 PDF 檔案的程序：

### Python

```
from google import genai
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://arxiv.org/pdf/2312.11805"

doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

sample_doc = client.files.upload(
  file=doc_io,
  config=dict(
    mime_type='application/pdf')
)

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "uri": sample_doc.uri, "mime_type": sample_doc.mime_type},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {

    const pdfBuffer = await fetch("https://arxiv.org/pdf/2312.11805")
        .then((response) => response.arrayBuffer());

    const fileBlob = new Blob([pdfBuffer], { type: 'application/pdf' });

    const file = await ai.files.upload({
        file: fileBlob,
        config: {
            displayName: 'A17_FlightPlan.pdf',
        },
    });

    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    const interaction = await ai.interactions.create({
        model: 'gemini-3.8-flash',
        input: [
            { type: "document", uri: file.uri, mime_type: file.mime_type },
            { type: "text", text: "Summarize this document" }
        ],
    });

    console.log(interaction.output_text);

}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

String longContextPdfPath = "https://arxiv.org/pdf/2312.11805";
HttpClient httpClient = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder().uri(URI.create(longContextPdfPath)).build();
byte[] pdfBytes = httpClient.send(request, HttpResponse.BodyHandlers.ofByteArray()).body();

File sampleDoc =
    client.files.upload(
        pdfBytes, UploadFileConfig.builder().mimeType("application/pdf").build());

String prompt = "Summarize this document";

Content docContent =
    DocumentContent.builder()
        .uri(sampleDoc.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(sampleDoc.mimeType().orElse("application/pdf")))
        .build();
Content textContent = TextContent.builder().text(prompt).build();

List<Content> contents = Arrays.asList(docContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "bytes"
    "context"
    "fmt"
    "io"
    "log"
    "net/http"

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

    longContextPdfPath := "https://arxiv.org/pdf/2312.11805"
    resp, err := http.Get(longContextPdfPath)
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
    pdfBytes, err := io.ReadAll(resp.Body)
    if err != nil {
        log.Fatal(err)
    }

    sampleDoc, err := client.Files.Upload(ctx, bytes.NewReader(pdfBytes), &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(sampleDoc.URI),
                    MimeType: interactions.DocumentContentMimeType(sampleDoc.MIMEType).ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
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
PDF_PATH="https://arxiv.org/pdf/2312.11805"
DISPLAY_NAME="Gemini_paper"
PROMPT="Summarize this document"

# Download the PDF from the provided URL
wget -O "${DISPLAY_NAME}.pdf" "${PDF_PATH}"

MIME_TYPE=$(file -b --mime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c < "${DISPLAY_NAME}.pdf")

echo "MIME_TYPE: ${MIME_TYPE}"
echo "NUM_BYTES: ${NUM_BYTES}"

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -D upload-header.tmp \
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
  --data-binary "@${DISPLAY_NAME}.pdf" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Create payload JSON file for safety
cat << EOF > payload.json
{
  "model": "gemini-3.8-flash",
  "input": [
    {"type": "text", "text": "${PROMPT}"},
    {"type": "document", "uri": "${file_uri}", "mime_type": "application/pdf"}
  ]
}
EOF

# Now create an interaction using that file
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".steps[-1].content[0].text" response.json

# Clean up
rm "${DISPLAY_NAME}.pdf"
rm payload.json
```

### 儲存在本機的大型 PDF

### Python

```
from google import genai
import pathlib

client = genai.Client()

file_path = pathlib.Path('large_file.pdf')
sample_file = client.files.upload(
    file=file_path,
)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "uri": sample_file.uri, "mime_type": sample_file.mime_type},
        {"type": "text", "text": "Summarize this document"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
    const file = await ai.files.upload({
        file: 'large_file.pdf',
        config: {
            displayName: 'A17_FlightPlan.pdf',
        },
    });

    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    const interaction = await ai.interactions.create({
        model: 'gemini-3.8-flash',
        input: [
            { type: "document", uri: file.uri, mime_type: file.mime_type },
            { type: "text", text: "Summarize this document" }
        ],
    });

    console.log(interaction.output_text);

}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File sampleFile =
    client.files.upload(
        new java.io.File("large_file.pdf"),
        UploadFileConfig.builder().mimeType("application/pdf").build());

Content docContent =
    DocumentContent.builder()
        .uri(sampleFile.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(sampleFile.mimeType().orElse("application/pdf")))
        .build();
Content textContent = TextContent.builder().text("Summarize this document").build();

List<Content> contents = Arrays.asList(docContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
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

    sampleFile, err := client.Files.UploadFromPath(ctx, "large_file.pdf", &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(sampleFile.URI),
                    MimeType: interactions.DocumentContentMimeType(sampleFile.MIMEType).ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: "Summarize this document",
                }),
            }),
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
PDF_PATH="large_file.pdf"
NUM_BYTES=$(wc -c < "${PDF_PATH}")
DISPLAY_NAME=TEXT
tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: application/pdf" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${PDF_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now create an interaction using that file
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "document", "uri": "'$file_uri'", "mime_type": "application/pdf"},
        {"type": "text", "text": "Can you add a few more lines to this poem?"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq -r ".steps[-1].content[0].text" response.json
```

您可以呼叫 [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=zh-tw)，確認 API 是否已成功儲存上傳的檔案，並取得檔案的中繼資料。只有 `name` (以及延伸的 `uri`) 是獨一無二的。

### Python

```
from google import genai
import pathlib

client = genai.Client()

fpath = pathlib.Path('example.pdf')
fpath.write_text('hello')

file = client.files.upload(file='example.pdf')

file_info = client.files.get(name=file.name)
print(file_info.model_dump_json(indent=4))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function main() {
    fs.writeFileSync("example.pdf", "hello");

    const file = await ai.files.upload({
        file: "example.pdf",
        config: { mime_type: "application/pdf" }
    });

    const fileInfo = await ai.files.get({ name: file.name });
    console.log(fileInfo);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

Client client = new Client();

Path fpath = Paths.get("example.pdf");
Files.write(fpath, "hello".getBytes(StandardCharsets.UTF_8));

File file =
    client.files.upload(
        fpath.toFile(), UploadFileConfig.builder().mimeType("application/pdf").build());

File fileInfo = client.files.get(file.name().orElse(""), null);
System.out.println(fileInfo.toJson());
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
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    if err := os.WriteFile("example.pdf", []byte("hello"), 0644); err != nil {
        log.Fatal(err)
    }

    file, err := client.Files.UploadFromPath(ctx, "example.pdf", &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }

    fileInfo, err := client.Files.Get(ctx, file.Name, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(fileInfo)
}
```

### REST

```
name=$(jq -r ".file.name" file_info.json)
# Get the file of interest to check state
curl "https://generativelanguage.googleapis.com/v1beta/$name?key=$GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq -r ".name" file_info.json)
echo name=$name
file_uri=$(jq -r ".uri" file_info.json)
echo file_uri=$file_uri
```

## 傳遞多個 PDF

只要文件和文字提示的總大小不超過模型的脈絡窗口，Gemini API 就能在單一要求中處理多個 PDF 文件 (最多 1000 頁)。

### Python

```
from google import genai
import io
import httpx

client = genai.Client()

doc_url_1 = "https://arxiv.org/pdf/2312.11805"
doc_url_2 = "https://arxiv.org/pdf/2403.05530"

doc_data_1 = io.BytesIO(httpx.get(doc_url_1).content)
doc_data_2 = io.BytesIO(httpx.get(doc_url_2).content)

sample_pdf_1 = client.files.upload(
  file=doc_data_1,
  config=dict(mime_type='application/pdf')
)
sample_pdf_2 = client.files.upload(
  file=doc_data_2,
  config=dict(mime_type='application/pdf')
)

prompt = "What is the difference between each of the main benchmarks between these two papers? Output these in a table."

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "uri": sample_pdf_1.uri, "mime_type": sample_pdf_1.mime_type},
        {"type": "document", "uri": sample_pdf_2.uri, "mime_type": sample_pdf_2.mime_type},
        {"type": "text", "text": prompt}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function uploadRemotePDF(url, displayName) {
    const pdfBuffer = await fetch(url)
        .then((response) => response.arrayBuffer());

    const fileBlob = new Blob([pdfBuffer], { type: 'application/pdf' });

    const file = await ai.files.upload({
        file: fileBlob,
        config: {
            displayName: displayName,
        },
    });

    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    return file;
}

async function main() {
    const file1 = await uploadRemotePDF("https://arxiv.org/pdf/2312.11805", "PDF 1");
    const file2 = await uploadRemotePDF("https://arxiv.org/pdf/2403.05530", "PDF 2");

    const interaction = await ai.interactions.create({
        model: 'gemini-3.8-flash',
        input: [
            { type: "document", uri: file1.uri, mime_type: file1.mime_type },
            { type: "document", uri: file2.uri, mime_type: file2.mime_type },
            { type: "text", text: "What is the difference between each of the main benchmarks between these two papers? Output these in a table." }
        ],
    });

    console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

String docUrl1 = "https://arxiv.org/pdf/2312.11805";
String docUrl2 = "https://arxiv.org/pdf/2403.05530";

HttpClient httpClient = HttpClient.newHttpClient();
byte[] docData1 =
    httpClient
        .send(HttpRequest.newBuilder().uri(URI.create(docUrl1)).build(), HttpResponse.BodyHandlers.ofByteArray())
        .body();
byte[] docData2 =
    httpClient
        .send(HttpRequest.newBuilder().uri(URI.create(docUrl2)).build(), HttpResponse.BodyHandlers.ofByteArray())
        .body();

File samplePdf1 =
    client.files.upload(
        docData1, UploadFileConfig.builder().mimeType("application/pdf").build());
File samplePdf2 =
    client.files.upload(
        docData2, UploadFileConfig.builder().mimeType("application/pdf").build());

String prompt =
    "What is the difference between each of the main benchmarks between these two papers? Output these in a table.";

Content doc1Content =
    DocumentContent.builder()
        .uri(samplePdf1.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(samplePdf1.mimeType().orElse("application/pdf")))
        .build();
Content doc2Content =
    DocumentContent.builder()
        .uri(samplePdf2.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(samplePdf2.mimeType().orElse("application/pdf")))
        .build();
Content textContent = TextContent.builder().text(prompt).build();

List<Content> contents = Arrays.asList(doc1Content, doc2Content, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "bytes"
    "context"
    "fmt"
    "io"
    "log"
    "net/http"

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

    docURL1 := "https://arxiv.org/pdf/2312.11805"
    docURL2 := "https://arxiv.org/pdf/2403.05530"

    resp1, err := http.Get(docURL1)
    if err != nil {
        log.Fatal(err)
    }
    defer resp1.Body.Close()
    docData1, err := io.ReadAll(resp1.Body)
    if err != nil {
        log.Fatal(err)
    }

    resp2, err := http.Get(docURL2)
    if err != nil {
        log.Fatal(err)
    }
    defer resp2.Body.Close()
    docData2, err := io.ReadAll(resp2.Body)
    if err != nil {
        log.Fatal(err)
    }

    samplePdf1, err := client.Files.Upload(ctx, bytes.NewReader(docData1), &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }
    samplePdf2, err := client.Files.Upload(ctx, bytes.NewReader(docData2), &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }

    prompt := "What is the difference between each of the main benchmarks between these two papers? Output these in a table."

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(samplePdf1.URI),
                    MimeType: interactions.DocumentContentMimeType(samplePdf1.MIMEType).ToPointer(),
                }),
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(samplePdf2.URI),
                    MimeType: interactions.DocumentContentMimeType(samplePdf2.MIMEType).ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
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
DOC_URL_1="https://arxiv.org/pdf/2312.11805"
DOC_URL_2="https://arxiv.org/pdf/2403.05530"
DISPLAY_NAME_1="Gemini_paper"
DISPLAY_NAME_2="Gemini_1.5_paper"
PROMPT="What is the difference between each of the main benchmarks between these two papers? Output these in a table."

# Function to download and upload a PDF
upload_pdf() {
  local doc_url="$1"
  local display_name="$2"

  echo "Downloading ${display_name} from ${doc_url}..." >&2
  # Download the PDF
  wget -O "${display_name}.pdf" "${doc_url}" 2> /dev/null

  local MIME_TYPE=$(file -b --mime-type "${display_name}.pdf")
  local NUM_BYTES=$(wc -c < "${display_name}.pdf")

  echo "MIME_TYPE: ${MIME_TYPE}" >&2
  echo "NUM_BYTES: ${NUM_BYTES}" >&2

  local tmp_header_file="upload-header-${display_name}.tmp"

  # Initial resumable request
  # Using GEMINI_API_KEY instead of GOOGLE_API_KEY
  curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
    -D "${tmp_header_file}" \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
    -H "Content-Type: application/json" \
    -d "{'file': {'display_name': '${display_name}'}}" 2> /dev/null

  local upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
  rm "${tmp_header_file}"

  echo "Upload URL for ${display_name}: ${upload_url}" >&2

  # Upload the PDF
  curl "${upload_url}" \
    -H "Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@${display_name}.pdf" 2> /dev/null > "file_info_${display_name}.json"

  local file_uri=$(jq -r ".file.uri" "file_info_${display_name}.json")
  echo "file_uri for ${display_name}: ${file_uri}" >&2

  # Clean up the downloaded PDF
  rm "${display_name}.pdf"

  echo "${file_uri}"
}

# Upload the first PDF
file_uri_1=$(upload_pdf "${DOC_URL_1}" "${DISPLAY_NAME_1}")

# Upload the second PDF
file_uri_2=$(upload_pdf "${DOC_URL_2}" "${DISPLAY_NAME_2}")

# Create payload JSON file for safety
cat << EOF > payload_multi.json
{
  "model": "gemini-3.8-flash",
  "input": [
    {"type": "document", "uri": "${file_uri_1}", "mime_type": "application/pdf"},
    {"type": "document", "uri": "${file_uri_2}", "mime_type": "application/pdf"},
    {"type": "text", "text": "${PROMPT}"}
  ]
}
EOF

# Now create an interaction using both files
# Using GEMINI_API_KEY instead of GOOGLE_API_KEY
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d @payload_multi.json 2> /dev/null > response.json

cat response.json
echo

jq ".steps[-1].content[0].text" response.json

# Clean up
rm payload_multi.json
rm "file_info_${DISPLAY_NAME_1}.json"
rm "file_info_${DISPLAY_NAME_2}.json"
```

## 技術詳細資料

Gemini 支援的 PDF 檔案大小上限為 50 MB 或 1000 頁。這項限制適用於內嵌資料和 Files API 上傳作業。每頁文件相當於 258 個權杖。

除了模型的[內容視窗](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-tw)外，文件中的像素數量沒有具體限制，但較大的頁面會縮放至 3072 x 3072 像素的最高解析度，同時保留原始顯示比例，較小的頁面則會放大至 768 x 768 像素。如果網頁尺寸較小，除了頻寬外，不會有任何成本降低；如果網頁解析度較高，也不會提升效能。

### Gemini 3 模型

Gemini 3 推出 `media_resolution` 參數，可精細控管多模態視覺處理作業。現在你可以為每個媒體部分設定低、中或高解析度。新增這項功能後，處理 PDF 文件的方式也隨之更新：

1. **納入原生文字：**系統會擷取 PDF 中內嵌的原生文字，並提供給模型。
2. **帳單和權杖報表：**
   - 系統**不會**針對從 PDF 擷取的**原生文字**產生的權杖收費。
   - 在 API 回應的 `usage_metadata` 部分，處理 PDF 頁面 (以圖片形式) 所產生的權杖現在會計入 `IMAGE` 模態，而不是像某些舊版一樣計入個別的 `DOCUMENT` 模態。

如要進一步瞭解媒體解析度參數，請參閱「[媒體解析度](https://ai.google.dev/gemini-api/docs/interactions/media-resolution?hl=zh-tw)」指南。

### 文件類型

從技術上來說，您可以傳遞其他 MIME 類型，以瞭解文件內容，例如 TXT、Markdown、HTML、XML 等。不過，文件視覺 ***只能有意義地解讀 PDF***。其他類型則會以純文字形式擷取，模型無法解讀這些檔案的顯示內容。所有檔案類型專屬內容都會遺失，例如圖表、HTML 標記、Markdown 格式等。

如要瞭解其他檔案輸入方法，請參閱「[檔案輸入方法](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-tw)」指南。

### 最佳做法

為確保最佳成效：

- 上傳前，請先將頁面旋轉至正確方向。
- 避免頁面模糊不清。
- 如果使用單一頁面，請將文字提示詞放在該頁面之後。

## 後續步驟

如要進一步瞭解相關內容，請參閱下列資源：

- [檔案提示策略](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw#prompt-guide)：Gemini API 支援使用文字、圖片、音訊和影片資料提示，也稱為多模態提示。
- [系統指令](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-tw#system-instructions)：
  系統指令可根據特定需求和用途，引導模型行為。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-24 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-24 (世界標準時間)。"],[],[]]
