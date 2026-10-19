---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=bn
fetched_at: 2026-10-19T05:32:57.340227+00:00
title: "\u09ab\u09be\u0987\u09b2 \u0987\u09a8\u09aa\u09c1\u099f \u09aa\u09a6\u09cd\u09a7\u09a4\u09bf \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# ফাইল ইনপুট পদ্ধতি

Gemini API-তে অনুরোধ করার সময় আপনি কীভাবে ছবি, অডিও, ভিডিও ও ডকুমেন্টের মতো
মিডিয়া ফাইল যোগ করতে পারেন, তা এই গাইড থেকে জানতে পারবেন।
নতুন পদ্ধতিগুলি Batch, Interactions এবং Live API সহ Gemini API-এর সমস্ত এন্ডপয়েন্টে কাজ করে।
কোন পদ্ধতিটি সঠিক তা আপনার ফাইলের সাইজ, ডেটা কোথায়
সেভ করা আছে এবং কত ঘনঘন ফাইলটি ব্যবহার করার পরিকল্পনা করেছেন তার উপর নির্ভর করে।

ইনপুট হিসেবে কোনও ফাইল যোগ করার সবচেয়ে সহজ উপায় হল, কোনও লোকাল ফাইল পড়ে
সেটি প্রম্পটে যোগ করা। নিচের উদাহরণ থেকে কীভাবে লোকাল PDF
ফাইল পড়তে হয় তা দেখুন। এই পদ্ধতির জন্য পিডিএফ ফাইল ৫০ এমবির মধ্যে হতে হবে। ফাইলের
ইনপুট ধরন ও সীমা সম্পর্কে সম্পূর্ণ তালিকা পেতে
[ইনপুট পদ্ধতি তুলনা টেবিল](#method-comparison) দেখুন।

### Python

```
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = 'my_local_file.pdf';

    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: fs.readFileSync(filePath).toString("base64"),
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

byte[] pdfBytes = Files.readAllBytes(Paths.get("my_local_file.pdf"));
String base64Pdf = Base64.getEncoder().encodeToString(pdfBytes);

String prompt = "Summarize this document";

Content textContent = TextContent.builder().text(prompt).build();
Content docContent =
    DocumentContent.builder()
        .data(base64Pdf)
        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
        .build();

List<Content> contents = Arrays.asList(textContent, docContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### খুলুন

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

    pdfBytes, err := os.ReadFile("my_local_file.pdf")
    if err != nil {
        log.Fatal(err)
    }
    base64Pdf := base64.StdEncoding.EncodeToString(pdfBytes)

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.DocumentContent{
                    Data:     genai.Ptr(base64Pdf),
                    MimeType: interactions.DocumentContentMimeTypeApplicationPdf.ToPointer(),
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
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
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

## ইনপুট পদ্ধতির তুলনা

নিচের সারণীতে প্রতিটি ইনপুট পদ্ধতির সাথে ফাইল সীমা এবং সবচেয়ে ভাল ব্যবহার
সংক্রান্ত কেস তুলনা করা হয়েছে। মনে রাখবেন, ফাইলের ধরন এবং ফাইল প্রসেস করার জন্য ব্যবহৃত
মডেল বা টোকেনাইজারের উপর নির্ভর করে ফাইলের সাইজ সংক্রান্ত সীমা পরিবর্তিত হতে পারে।

| পদ্ধতি | এগুলির জন্য সেরা | ফাইলের সর্বাধিক সাইজ | পারসিস্টেন্স |
| --- | --- | --- | --- |
| **ইনলাইন ডেটা** | দ্রুত পরীক্ষা, ছোট ফাইল, রিয়েল-টাইম অ্যাপ্লিকেশন। | প্রতিটি অনুরোধ বা পেলোডের জন্য ১০০ এমবি   (**PDF-এর জন্য ৫০ এমবি**) | কোনওটিই নয় (প্রতিটি অনুরোধের সাথে পাঠানো হয়) |
| **File API আপলোড** | বড় ফাইল, একাধিকবার ব্যবহার করা ফাইল। | প্রতিটি ফাইলের জন্য ২ জিবি,   প্রতিটি প্রোজেক্টের জন্য সর্বাধিক ২০ জিবি | ৪৮ ঘণ্টা |
| **File API GCS URI রেজিস্ট্রেশন** | Google Cloud Storage-এ আগে থেকেই থাকা বড় ফাইল, একাধিকবার ব্যবহার করা ফাইল। | প্রতিটি ফাইলের জন্য ২ জিবি, সামগ্রিক স্টোরেজ সীমাহীন | কোনওটিই নয় (প্রতিটি অনুরোধের জন্য ফেচ করা হয়)। একবার রেজিস্ট্রেশন করলে ৩০ দিন পর্যন্ত অ্যাক্সেস পাওয়া যায়। |
| **এক্সটার্নাল URL** | আবার আপলোড না করেই ক্লাউড বাকেটে (AWS, Azure, GCS) থাকা সর্বজনীন ডেটা বা ডেটা। | প্রতিটি ফাইলের জন্য ১৫ এমবি | কোনওটিই নয় (প্রতিটি অনুরোধের জন্য ফেচ করা হয়) |

## ইনলাইন ডেটা

ছোট ফাইলের (১০০ এমবির কম অথবা PDF-এর ক্ষেত্রে ৫০ এমবি) জন্য, আপনি সরাসরি অনুরোধের পেলোডে ডেটা
পাস করতে পারবেন। দ্রুত পরীক্ষা বা রিয়েল-টাইম, ক্ষণস্থায়ী ডেটা ম্যানেজ করা
অ্যাপ্লিকেশনের জন্য এটি সবচেয়ে সহজ পদ্ধতি। আপনি ডেটা
base64 এনকোড করা স্ট্রিং হিসেবে প্রদান করতে পারেন অথবা সরাসরি লোকাল ফাইল রিড করে নিতে পারেন।

লোকাল ফাইল থেকে রিড করার উদাহরণের জন্য, এই পৃষ্ঠার
শুরুতে দেওয়া উদাহরণ দেখুন।

### URL থেকে ফেচ করা

এছাড়াও, আপনি কোনও URL থেকে ফাইল ফেচ করতে, এটিকে বাইটে কনভার্ট করতে এবং
ইনপুটে অন্তর্ভুক্ত করতে পারবেন।

### Python

```
from google import genai
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: Buffer.from(pdfResp).toString("base64"),
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
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

String docUrl = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf";
HttpClient httpClient = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder().uri(URI.create(docUrl)).build();
byte[] docData = httpClient.send(request, HttpResponse.BodyHandlers.ofByteArray()).body();
String base64Pdf = Base64.getEncoder().encodeToString(docData);

String prompt = "Summarize this document";

Content docContent =
    DocumentContent.builder()
        .data(base64Pdf)
        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
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

### খুলুন

```
package main

import (
    "context"
    "encoding/base64"
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

    docURL := "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
    resp, err := http.Get(docURL)
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
    docData, err := io.ReadAll(resp.Body)
    if err != nil {
        log.Fatal(err)
    }
    base64Pdf := base64.StdEncoding.EncodeToString(docData)

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    Data:     genai.Ptr(base64Pdf),
                    MimeType: interactions.DocumentContentMimeTypeApplicationPdf.ToPointer(),
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
"model": "gemini-3.8-flash",
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

File API বড় ফাইল (২ জিবি পর্যন্ত) বা একাধিক অনুরোধে ব্যবহার করার জন্য
উদ্দেশ্যপূর্ণ ফাইলের জন্য ডিজাইন করা হয়েছে।

### স্ট্যান্ডার্ড ফাইল আপলোড

Gemini API-তে একটি লোকাল ফাইল আপলোড করুন। এইভাবে আপলোড করা ফাইল
সাময়িকভাবে (৪৮ ঘণ্টা) স্টোর করা হয় এবং মডেলের মাধ্যমে দক্ষতার সাথে রিট্রিভ করার জন্য প্রসেস করা হয়।

### Python

```
from google import genai

client = genai.Client()

doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

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
    model: "gemini-3.8-flash",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
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

File docFile =
    client.files.upload(
        new java.io.File("path/to/your/sample.pdf"),
        UploadFileConfig.builder().mimeType("application/pdf").build());

String prompt = "Summarize this document";

Content textContent = TextContent.builder().text(prompt).build();
Content docContent =
    DocumentContent.builder()
        .uri(docFile.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(docFile.mimeType().orElse("application/pdf")))
        .build();

List<Content> contents = Arrays.asList(textContent, docContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### খুলুন

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

    docFile, err := client.Files.UploadFromPath(ctx, "path/to/your/sample.pdf", &genai.UploadFileConfig{
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
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(docFile.URI),
                    MimeType: interactions.DocumentContentMimeType(docFile.MIMEType).ToPointer(),
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
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### Google Cloud Storage ফাইল রেজিস্টার করা

আপনার ডেটা আগে থেকেই Google Cloud Storage-এ থাকলে, আপনাকে এটি
ডাউনলোড করে আবার আপলোড করতে হবে না। আপনি এটি সরাসরি File API-এর সাথে রেজিস্টার করতে পারবেন।

1. প্রতিটি বাকেটে **পরিষেবা এজেন্ট**-কে অ্যাক্সেস দিন

   1. আপনার Google Cloud প্রোজেক্টে Gemini API চালু করুন।
   2. পরিষেবা এজেন্ট তৈরি করুন:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. আপনার স্টোরেজ
      বাকেট পড়ার জন্য **Gemini API পরিষেবা এজেন্টকে অনুমতি দিন**।

      ব্যবহারকারীকে এই পরিষেবা এজেন্টের জন্য নির্দিষ্ট স্টোরেজ বাকেটে `Storage Object Viewer`
      [IAM ভূমিকা](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=bn#storage.objectViewer)
      অ্যাসাইন করতে হবে।

   এই অ্যাক্সেসের মেয়াদ ডিফল্ট হিসেবে শেষ হয় না, তবে যেকোনও সময় পরিবর্তন করা যায়। অনুমতি দেওয়ার জন্য আপনি
   [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=bn)
   কমান্ডও
   ব্যবহার করতে পারেন।
2. আপনার পরিষেবা যাচাই করা

   **পূর্বশর্ত**

   - এপিআই চালু করুন
   - উপযুক্ত অনুমতি সহ একটি পরিষেবা অ্যাকাউন্ট বা এজেন্ট তৈরি করুন।

   আপনাকে প্রথমে সেই পরিষেবা হিসেবে যাচাই করিয়ে নিতে হবে যার কাছে স্টোরেজ অবজেক্ট ভিউয়ার
   অনুমতি আছে। আপনার ফাইল
   ম্যানেজমেন্ট কোড যে এনভায়রনমেন্টে রান করবে তার উপর নির্ভর করে এটি কীভাবে হবে।

   **Google Cloud-এর বাইরে**

   আপনার কোড Google Cloud-এর বাইরে, যেমন আপনার ডেস্কটপ থেকে রান করলে,
   নিচের ধাপগুলি অনুসরণ করে Google Cloud Console থেকে অ্যাকাউন্ট ক্রেডেনশিয়াল ডাউনলোড করুন:

   1. [পরিষেবা অ্যাকাউন্ট কনসোলে](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=bn) ব্রাউজ করুন
   2. প্রাসঙ্গিক পরিষেবা অ্যাকাউন্ট বেছে নিন
   3. **কী** ট্যাব বেছে নিন এবং **কী যোগ করুন, নতুন কী তৈরি করুন** বিকল্প বেছে নিন
   4. **JSON** কীয়ের ধরন বেছে নিন এবং আপনার মেশিনে ফাইলটি কোথায় ডাউনলোড করা হয়েছে তা
      নোট করুন।

   আরও বিবরণের জন্য, [পরিষেবা অ্যাকাউন্ট কী ম্যানেজমেন্ট](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=bn) সংক্রান্ত অফিসিয়াল Google Cloud ডকুমেন্টেশন দেখুন।

   তারপর যাচাই করার জন্য নিম্নলিখিত কমান্ড ব্যবহার করুন। এইসব কমান্ড ধরে নেয় যে আপনার
   সার্ভিস অ্যাকাউন্ট ফাইল বর্তমান ডিরেক্টরিতে আছে এবং এর নাম
   `service-account.json`।

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

   ### Javascript

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

   **Google Cloud-এ**

   আপনি যদি সরাসরি Google Cloud-এ রান করেন, যেমন [Cloud
   Run ফাংশন](https://cloud.google.com/functions?hl=bn) বা
   [Compute Engine ইনস্ট্যান্স](https://cloud.google.com/products/compute?hl=bn) ব্যবহার করে, তাহলে আপনার কাছে
   অন্তর্নিহিত ক্রেডেনশিয়াল থাকবে, কিন্তু উপযুক্ত স্কোপ দেওয়ার জন্য আপনাকে আবার
   যাচাই করতে হবে।

   ### Python

   এই কোড আশা করে যে পরিষেবাটি এমন একটি এনভায়রনমেন্টে চলছে যেখানে
   [অ্যাপ্লিকেশন ডিফল্ট ক্রেডেনশিয়াল](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=bn)
   অটোমেটিক পাওয়া যেতে পারে, যেমন Cloud Run বা Compute Engine।

   ```
   import google.auth

   GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### জাভাস্ক্রিপ্ট

   এই কোড আশা করে যে পরিষেবাটি এমন একটি এনভায়রনমেন্টে চলছে যেখানে
   [অ্যাপ্লিকেশন ডিফল্ট ক্রেডেনশিয়াল](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=bn)
   অটোমেটিক পাওয়া যেতে পারে, যেমন Cloud Run বা Compute Engine।

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

### Java

```
import com.google.auth.oauth2.GoogleCredentials;
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.List;

List<String> gcsReadScopes =
    Arrays.asList(
        "https://www.googleapis.com/auth/devstorage.read_only",
        "https://www.googleapis.com/auth/cloud-platform");

String serviceAccountFile = "service-account.json";

GoogleCredentials credentials =
    GoogleCredentials.fromStream(new FileInputStream(serviceAccountFile))
        .createScoped(gcsReadScopes);
```

### খুলুন

```
package main

import (
    "log"

    "google.golang.org/genai"
)

func main() {
    cc := &genai.ClientConfig{}
    if err := cc.UseDefaultCredentials(); err != nil {
        log.Fatal(err)
    }
    _ = cc.Credentials
}
```

### CLI

এটি একটি ইন্ট্যার‍্যাক্টিভ কমান্ড। Compute Engine-এর মতো পরিষেবার জন্য, আপনি কনফিগারেশন লেভেলে
চলমান পরিষেবার সাথে স্কোপ অ্যাটাচ করতে পারবেন। একটি উদাহরণের জন্য [ব্যবহারকারী-ম্যানেজ করা পরিষেবা
ডকুমেন্ট](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=bn#using)
দেখুন।

```
gcloud auth application-default login \
--scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
```

1. ফাইল রেজিস্ট্রেশন (Files API)
   Files API ব্যবহার করে ফাইল রেজিস্টার করুন এবং Files API পাথ তৈরি করুন যা
   সরাসরি Gemini API-তে ব্যবহার করা যেতে পারে।

   ### Python

   ```
   from google import genai

   client = genai.Client(credentials=credentials)

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
   )
   prompt = "Summarize this file."

   for f in registered_gcs_files.files:
     print(f.name)
     interaction = client.interactions.create(
       model="gemini-3.8-flash",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     print(interaction.output_text)
   ```

   ### জাভাস্ক্রিপ্ট

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
               model: "gemini-3.8-flash",
               input: [
                   { type: "text", text: prompt },
                   { type: "document", uri: file.uri, mime_type: file.mimeType }
               ]
           });

           console.log(interaction.output_text);
       }
   }

   main();
   ```

### Java

```
import com.google.auth.oauth2.GoogleCredentials;
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
import com.google.genai.types.RegisterFilesResponse;
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

GoogleCredentials credentials =
    GoogleCredentials.fromStream(new FileInputStream("service-account.json"))
        .createScoped(
            Arrays.asList(
                "https://www.googleapis.com/auth/devstorage.read_only",
                "https://www.googleapis.com/auth/cloud-platform"));

Client client = Client.builder().credentials(credentials).build();

RegisterFilesResponse registeredGcsFiles =
    client.files.registerFiles(
        credentials,
        Arrays.asList("gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"),
        null);

String prompt = "Summarize this file.";

for (File f : registeredGcsFiles.files().orElse(Collections.emptyList())) {
  System.out.println(f.name().orElse(""));

  Content textContent = TextContent.builder().text(prompt).build();
  Content docContent =
      DocumentContent.builder()
          .uri(f.uri().orElse(""))
          .mimeType(DocumentContentMimeType.of(f.mimeType().orElse("application/pdf")))
          .build();

  CreateModelInteraction params =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3.8-flash"))
          .input(InteractionsInput.ofContent(Arrays.asList(textContent, docContent)))
          .build();

  Interaction interaction =
      client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
  System.out.println(interaction.outputText().orElse(""));
}
```

### খুলুন

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
    cc := &genai.ClientConfig{}
    if err := cc.UseDefaultCredentials(); err != nil {
        log.Fatal(err)
    }
    client, err := genai.NewClient(ctx, cc)
    if err != nil {
        log.Fatal(err)
    }

    registeredGcsFiles, err := client.Files.RegisterFiles(
        ctx,
        []string{"gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"},
        cc.Credentials,
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Summarize this file."

    for _, f := range registeredGcsFiles.Files {
        fmt.Println(f.Name)
        res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput([]interactions.Content{
                    interactions.NewContent(interactions.TextContent{
                        Text: prompt,
                    }),
                    interactions.NewContent(interactions.DocumentContent{
                        URI:      genai.Ptr(f.URI),
                        MimeType: interactions.DocumentContentMimeType(f.MIMEType).ToPointer(),
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
}
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

## এক্সটার্নাল HTTP / সাইন-ইন করা URL

আপনি সর্বজনীনভাবে অ্যাক্সেস করা যায় এমন HTTPS URL বা আগে থেকে সাইন করা URL সরাসরি আপনার
অনুরোধে পাস করতে পারবেন। প্রসেসিং চলাকালীন Gemini API নিরাপদে কন্টেন্ট ফেচ করবে।
আপনি আবার আপলোড করতে চান না এমন ফাইলের জন্য এটি আদর্শ। প্রতিটি ফাইল সর্বাধিক
১৫ এমবি হতে পারে। বড় ফাইলের জন্য, [File API](#file-api) ব্যবহার করুন।

### Python

```
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### Javascript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: [
      { type: "document", uri: uri, mime_type: "application/pdf" },
      { type: "text", text: "summarize this file" }
    ]
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "model": "gemini-3.8-flash",
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

### অ্যাক্সেসিবিলিটি

আপনি যেসব URL দিয়েছেন সেগুলি যেন লগ-ইন করতে হয় এমন পৃষ্ঠায় বা
পেওয়ালের পিছনে না থাকে তা নিশ্চিত করুন। প্রাইভেট ডেটাবেসের ক্ষেত্রে, সঠিক অ্যাক্সেস অনুমতি ও মেয়াদ সহ
স্বাক্ষরিত URL তৈরি করেছেন কিনা তা নিশ্চিত করুন।

### নিরাপত্তা সংক্রান্ত পরীক্ষা

URL-এ কন্টেন্ট মডারেশন চেক করে দেখা হয় যে সেটি
নিরাপত্তা ও নীতি সংক্রান্ত স্ট্যান্ডার্ড মেনে চলছে কিনা। URL এই চেক পাস করতে না পারলে, আপনি একটি
`url_retrieval_status` পাবেন `URL_RETRIEVAL_STATUS_UNSAFE`.

### যে ধরনের কন্টেন্ট কাজ করে

এই কাজ করে এমন ফাইলের ধরন ও সীমাবদ্ধতার তালিকা প্রাথমিক
নির্দেশিকা হিসেবে দেওয়া হয়েছে এবং এটি সম্পূর্ণ তালিকা নয়। কার্যকর
সাপোর্ট করা ধরনের সেট পরিবর্তন করা যেতে পারে এবং এটি নির্দিষ্ট
মডেল ও ব্যবহৃত টোকেনাইজার ভার্সনের উপর নির্ভর করে আলাদা হতে পারে। কাজ করে না এমন ধরনের ফলে সমস্যা হবে।
এছাড়াও, এই ধরনের ফাইলের জন্য কন্টেন্ট রিট্রিভ করার ক্ষেত্রে
শুধুমাত্র সর্বজনীনভাবে অ্যাক্সেস করা যায় এমন URL কাজ করে।

#### টেক্সট ফাইলের ধরন

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### অ্যাপ্লিকেশন ফাইলের ধরন

- `application/json`
- `application/pdf`

#### ইমেজ ফাইলের ধরন

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### ভিডিও ফাইলের ধরন

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## পেশাদার পদ্ধতি

- **সঠিক পদ্ধতি বেছে নিন:** ছোট, ক্ষণস্থায়ী ফাইলের জন্য ইনলাইন ডেটা ব্যবহার করুন।
  বড় বা প্রায়শই ব্যবহার করা ফাইলের জন্য File API ব্যবহার করুন। আগে থেকেই অনলাইনে হোস্ট করা ডেটার জন্য
  এক্সটার্নাল URL ব্যবহার করুন।
- **MIME-এর ধরন নির্দিষ্ট করুন:** সঠিক প্রসেসিং নিশ্চিত করতে, সবসময় ফাইল
  ডেটার জন্য সঠিক MIME-এর ধরন দিন।
- **সমস্যা সমাধান করা:** নেটওয়ার্ক কাজ না করা, ফাইল অ্যাক্সেস সংক্রান্ত সমস্যা বা API
  সংক্রান্ত সমস্যার মতো সম্ভাব্য সমস্যা ম্যানেজ করতে আপনার কোডে
  সমস্যা সমাধান করার সুবিধা প্রয়োগ করুন।

## সীমাবদ্ধতা

- পদ্ধতি ([তুলনামূলক সারণী](#method-comparison) দেখুন)
  ও ফাইলের ধরন অনুযায়ী ফাইলের সাইজ সংক্রান্ত সীমা আলাদা আলাদা হয়।
- ইনলাইন ডেটা অনুরোধের পেলোড সাইজ বাড়িয়ে দেয়।
- File API-এর মাধ্যমে আপলোড করা ফাইল সাময়িক এবং ৪৮ ঘণ্টা পরে সেটির মেয়াদ শেষ হয়ে যায়।
- এক্সটার্নাল URL থেকে ডেটা ফেচ করার ক্ষেত্রে, প্রতিটি ফাইলের জন্য ১৫ এমবি সীমা নির্ধারণ করা আছে এবং এটি নির্দিষ্ট
  কন্টেন্টের ধরন সমর্থন করে।

## এর পরে কী করতে হবে

- [Google AI Studio](http://aistudio.google.com/?hl=bn) ব্যবহার করে আপনার নিজস্ব মাল্টিমোডাল প্রম্পট লেখার চেষ্টা করুন।
- আপনার প্রম্পটে ফাইল যোগ করা সংক্রান্ত তথ্যের জন্য, এইসব
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=bn),
  [অডিও](https://ai.google.dev/gemini-api/docs/audio?hl=bn) এবং
  [ডকুমেন্ট প্রসেসিং](https://ai.google.dev/gemini-api/docs/document-processing?hl=bn)
  গাইড দেখুন।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-07 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-07 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
