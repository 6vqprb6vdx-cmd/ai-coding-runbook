---
source_url: https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=th
fetched_at: 2026-05-18T13:09:00.422989+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# วิธีการป้อนไฟล์

คำแนะนำนี้จะอธิบายวิธีต่างๆ ในการรวมไฟล์สื่อ เช่น รูปภาพ เสียง วิดีโอ และเอกสาร เมื่อส่งคำขอไปยัง Gemini API
วิธีการใหม่นี้รองรับในปลายทาง Gemini API ทั้งหมด ซึ่งรวมถึง Batch, Interactions และ Live API
การเลือกวิธีที่เหมาะสมขึ้นอยู่กับขนาดไฟล์ ตำแหน่งที่จัดเก็บข้อมูล และความถี่ที่คุณวางแผนจะใช้ไฟล์

วิธีที่ง่ายที่สุดในการรวมไฟล์เป็นอินพุตคือการอ่านไฟล์ในเครื่องและรวมไว้ในพรอมต์ ตัวอย่างต่อไปนี้แสดงวิธีอ่านไฟล์ PDF ในเครื่อง PDF มีขนาดไม่เกิน 50 MB สำหรับวิธีนี้ ดูรายการประเภทอินพุตไฟล์และขีดจำกัดทั้งหมดใน
[ตารางเปรียบเทียบวิธีการป้อนข้อมูล](#method-comparison)

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
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

# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
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

## การเปรียบเทียบวิธีการป้อนข้อมูล

ตารางต่อไปนี้เปรียบเทียบวิธีการป้อนข้อมูลแต่ละวิธีกับขีดจำกัดของไฟล์และ Use Case ที่ดีที่สุด โปรดทราบว่าขีดจำกัดขนาดไฟล์อาจแตกต่างกันไปตามประเภทไฟล์และโมเดลหรือตัวแยกคำที่ใช้ในการประมวลผลไฟล์

| วิธีการ | เหมาะสำหรับ | ขนาดไฟล์สูงสุด | ความต่อเนื่อง |
| --- | --- | --- | --- |
| **ข้อมูลแบบอินไลน์** | การทดสอบอย่างรวดเร็ว ไฟล์ขนาดเล็ก แอปพลิเคชันแบบเรียลไทม์ | 100 MB ต่อคำขอหรือเพย์โหลด   (**50 MB สำหรับ PDF**) | ไม่มี (ส่งไปพร้อมกับทุกคำขอ) |
| **การอัปโหลด File API** | ไฟล์ขนาดใหญ่ ไฟล์ที่ใช้หลายครั้ง | 2 GB ต่อไฟล์   สูงสุด 20 GB ต่อโปรเจ็กต์ | 48 ชั่วโมง |
| **การลงทะเบียน URI ของ File API GCS** | ไฟล์ขนาดใหญ่ที่อยู่ใน Google Cloud Storage อยู่แล้ว ไฟล์ที่ใช้หลายครั้ง | 2 GB ต่อไฟล์ ไม่มีขีดจำกัดพื้นที่เก็บข้อมูลโดยรวม | ไม่มี (ดึงข้อมูลต่อคำขอ) การลงทะเบียนครั้งเดียวจะให้สิทธิ์เข้าถึงได้นานสูงสุด 30 วัน |
| **URL ภายนอก** | ข้อมูลสาธารณะหรือข้อมูลใน Bucket ของระบบคลาวด์ (AWS, Azure, GCS) โดยไม่ต้องอัปโหลดซ้ำ | 100 MB ต่อคำขอ/เพย์โหลด | ไม่มี (ดึงข้อมูลต่อคำขอ) |

## ข้อมูลแบบอินไลน์

สำหรับไฟล์ขนาดเล็ก (ไม่เกิน 100 MB หรือ 50 MB สำหรับ PDF) คุณสามารถส่งข้อมูลในเพย์โหลดของคำขอได้โดยตรง วิธีนี้เป็นวิธีที่ง่ายที่สุดสำหรับการทดสอบอย่างรวดเร็วหรือแอปพลิเคชันที่จัดการข้อมูลชั่วคราวแบบเรียลไทม์ คุณสามารถระบุข้อมูลเป็นสตริงที่เข้ารหัสแบบ Base64 หรือโดยการอ่านไฟล์ในเครื่องโดยตรง

ดูตัวอย่างการอ่านจากไฟล์ในเครื่องได้ที่ตัวอย่างที่จุดเริ่มต้นของหน้านี้

### ดึงข้อมูลจาก URL

นอกจากนี้ คุณยังดึงข้อมูลไฟล์จาก URL แปลงเป็นไบต์ และรวมไว้ในอินพุตได้ด้วย

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
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
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Gemini File API

File API ออกแบบมาสำหรับไฟล์ขนาดใหญ่ (สูงสุด 2 GB) หรือไฟล์ที่คุณต้องการใช้ในคำขอหลายรายการ

### การอัปโหลดไฟล์มาตรฐาน

อัปโหลดไฟล์ในเครื่องไปยัง Gemini API ระบบจะจัดเก็บไฟล์ที่อัปโหลดด้วยวิธีนี้ไว้ชั่วคราว (48 ชั่วโมง) และประมวลผลเพื่อให้โมเดลดึงข้อมูลได้อย่างมีประสิทธิภาพ

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
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
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### ลงทะเบียนไฟล์ Google Cloud Storage

หากข้อมูลอยู่ใน Google Cloud Storage อยู่แล้ว คุณไม่จำเป็นต้องดาวน์โหลดและอัปโหลดซ้ำ คุณสามารถลงทะเบียนข้อมูลกับ File API ได้โดยตรง

1. ให้สิทธิ์เข้าถึง **Service Agent** แก่แต่ละ Bucket

   1. เปิดใช้ Gemini API ในโปรเจ็กต์ที่อยู่ในระบบคลาวด์ของ Google
   2. สร้าง Service Agent ด้วยคำสั่งต่อไปนี้

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **ให้สิทธิ์ Service Agent ของ Gemini API** ในการอ่าน Bucket พื้นที่เก็บข้อมูล

      ผู้ใช้ต้องกำหนดบทบาท `Storage Object Viewer`
      [IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=th#storage.objectViewer)
      ให้กับตัวแทนบริการนี้ใน Bucket พื้นที่เก็บข้อมูลที่ต้องการใช้

   สิทธิ์เข้าถึงนี้จะไม่มีวันหมดอายุโดยค่าเริ่มต้น แต่คุณสามารถเปลี่ยนแปลงได้ทุกเมื่อ นอกจากนี้ คุณยังใช้
   [คำสั่ง Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=th)
   เพื่อให้สิทธิ์ได้ด้วย
2. ตรวจสอบสิทธิ์บริการ

   **ข้อกำหนดเบื้องต้น**

   - เปิดใช้ API
   - สร้างบัญชีบริการหรือ Agent ที่มีสิทธิ์ที่เหมาะสม

   ก่อนอื่น คุณต้องตรวจสอบสิทธิ์ในฐานะบริการที่มีสิทธิ์เข้าถึง Storage Object Viewer ซึ่งวิธีการตรวจสอบสิทธิ์จะขึ้นอยู่กับสภาพแวดล้อมที่โค้ดการจัดการไฟล์จะทำงาน

   **ภายนอก Google Cloud**

   หากโค้ดทำงานจากภายนอก Google Cloud เช่น จากเดสก์ท็อป ให้ดาวน์โหลดข้อมูลเข้าสู่ระบบบัญชีจากคอนโซล Google Cloud โดยทำตามขั้นตอนต่อไปนี้

   1. ไปที่[คอนโซลบัญชีบริการ](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=th)
   2. เลือกบัญชีบริการที่เกี่ยวข้อง
   3. เลือกแท็บ**คีย์** แล้วเลือก**เพิ่มคีย์ สร้างคีย์ใหม่**
   4. เลือกประเภทคีย์ **JSON** และจดบันทึกตำแหน่งที่ดาวน์โหลดไฟล์ในเครื่อง

   ดูรายละเอียดเพิ่มเติมได้ในเอกสารประกอบอย่างเป็นทางการของ Google Cloud เกี่ยวกับการจัดการคีย์บัญชีบริการ

   จากนั้นใช้คำสั่งต่อไปนี้เพื่อตรวจสอบสิทธิ์ คำสั่งเหล่านี้ถือว่าไฟล์บัญชีบริการอยู่ในไดเรกทอรีปัจจุบันและมีชื่อว่า `service-account.json`

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

   **ใน Google Cloud**

   หากคุณใช้งานใน Google Cloud โดยตรง เช่น โดยใช้ [ฟังก์ชัน Cloud Run](https://cloud.google.com/functions?hl=th) หรือ
   [อินสแตนซ์ Compute Engine](https://cloud.google.com/products/compute?hl=th) คุณจะ
   มีข้อมูลเข้าสู่ระบบโดยนัย แต่จะต้องตรวจสอบสิทธิ์อีกครั้งเพื่อให้
   ขอบเขตที่เหมาะสม

   ### Python

   โค้ดนี้คาดหวังว่าบริการจะทำงานในสภาพแวดล้อมที่
   [ข้อมูลรับรองเริ่มต้นของแอปพลิเคชัน](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=th)
   ได้โดยอัตโนมัติ เช่น Cloud Run หรือ Compute Engine

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   โค้ดนี้คาดหวังว่าบริการจะทำงานในสภาพแวดล้อมที่
   [ข้อมูลรับรองเริ่มต้นของแอปพลิเคชัน](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=th)
   ได้โดยอัตโนมัติ เช่น Cloud Run หรือ Compute Engine

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

   นี่เป็นคำสั่งแบบอินเทอร์แอกทีฟ สำหรับบริการอย่าง Compute Engine คุณสามารถแนบขอบเขตกับบริการที่ทำงานอยู่ที่ระดับการกำหนดค่าได้ ดูตัวอย่างได้ในเอกสารประกอบเกี่ยวกับบริการที่ผู้ใช้จัดการ

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. การลงทะเบียนไฟล์ (Files API)

   ใช้ Files API เพื่อลงทะเบียนไฟล์และสร้างเส้นทาง Files API ที่ใช้ใน Gemini API ได้โดยตรง

   ### Python

   ```
   # This will only work for SDK newer than 2.0.0
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
   // This will only work for SDK newer than 2.0.0
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

## URL HTTP ภายนอก / URL ที่ลงชื่อแล้ว

คุณสามารถส่ง URL HTTPS ที่เข้าถึงได้แบบสาธารณะหรือ URL ที่ลงชื่อไว้ล่วงหน้าในคำขอได้โดยตรง Gemini API จะดึงข้อมูลเนื้อหาอย่างปลอดภัยในระหว่างการประมวลผล
วิธีนี้เหมาะสำหรับไฟล์ขนาดไม่เกิน 100 MB ที่คุณไม่ต้องการอัปโหลดซ้ำ

### Python

```
# This will only work for SDK newer than 2.0.0
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

### Javascript

```
// This will only work for SDK newer than 2.0.0
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
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -H "Api-Revision: 2026-05-20" \
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

### การช่วยเหลือพิเศษ

ตรวจสอบว่า URL ที่คุณระบุไม่ได้นำไปยังหน้าที่ต้องเข้าสู่ระบบหรืออยู่หลังเพย์วอลล์ สำหรับฐานข้อมูลส่วนตัว โปรดตรวจสอบว่าคุณสร้าง URL ที่ลงชื่อแล้วโดยมีสิทธิ์เข้าถึงและวันหมดอายุที่ถูกต้อง

### การตรวจสอบความปลอดภัย

ระบบจะตรวจสอบการกลั่นกรองเนื้อหาใน URL เพื่อยืนยันว่า URL เป็นไปตามมาตรฐานด้านความปลอดภัยและนโยบาย หาก URL ไม่ผ่านการตรวจสอบนี้ คุณจะได้รับ `url_retrieval_status` เป็น `URL_RETRIEVAL_STATUS_UNSAFE`

### ประเภทเนื้อหาที่รองรับ

รายการประเภทไฟล์และข้อจำกัดที่รองรับนี้มีไว้เพื่อเป็นแนวทางเบื้องต้นและไม่ครอบคลุมทั้งหมด ชุดประเภทที่รองรับจริงอาจมีการเปลี่ยนแปลงและแตกต่างกันไปตามโมเดลและเวอร์ชันตัวแยกคำที่ใช้ ประเภทที่ไม่รองรับจะทำให้เกิดข้อผิดพลาด
นอกจากนี้ การดึงข้อมูลเนื้อหาสำหรับไฟล์ประเภทเหล่านี้ยังรองรับเฉพาะ URL ที่เข้าถึงได้แบบสาธารณะ

#### ประเภทไฟล์ข้อความ

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### ประเภทไฟล์แอปพลิเคชัน

- `application/json`
- `application/pdf`

#### ประเภทไฟล์รูปภาพ

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

## แนวทางปฏิบัติแนะนำ

- **เลือกวิธีที่เหมาะสม:** ใช้ข้อมูลแบบอินไลน์สำหรับไฟล์ขนาดเล็กและชั่วคราว
  ใช้ File API สำหรับไฟล์ขนาดใหญ่หรือไฟล์ที่ใช้บ่อย ใช้ URL ภายนอกสำหรับข้อมูลที่โฮสต์ออนไลน์อยู่แล้ว
- **ระบุประเภท MIME:** ระบุประเภท MIME ที่ถูกต้องสำหรับข้อมูลไฟล์เสมอเพื่อให้แน่ใจว่าระบบจะประมวลผลได้อย่างถูกต้อง
- **จัดการข้อผิดพลาด:** ใช้การจัดการข้อผิดพลาดในโค้ดเพื่อจัดการปัญหาที่อาจเกิดขึ้น เช่น เครือข่ายล่ม ปัญหาการเข้าถึงไฟล์ หรือข้อผิดพลาดของ API

## ข้อจำกัด

- ขีดจำกัดขนาดไฟล์จะแตกต่างกันไปตามวิธี (ดู [ตารางเปรียบเทียบ](#method-comparison))
  และประเภทไฟล์
- ข้อมูลแบบอินไลน์จะเพิ่มขนาดเพย์โหลดของคำขอ
- การอัปโหลด File API เป็นแบบชั่วคราวและจะหมดอายุหลังจากผ่านไป 48 ชั่วโมง
- การดึงข้อมูล URL ภายนอกจำกัดไว้ที่ 100 MB ต่อเพย์โหลดและรองรับเนื้อหาบางประเภท

## ขั้นตอนถัดไป

- ลองเขียนพรอมต์มัลติโมดัลของคุณเองโดยใช้
  [Google AI Studio](http://aistudio.google.com/?hl=th)
- ดูข้อมูลเกี่ยวกับการรวมไฟล์ไว้ในพรอมต์ได้ที่คำแนะนำการประมวลผล
  [Vision](https://ai.google.dev/gemini-api/docs/interactions/vision?hl=th),
  [เสียง](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=th) และ
  [เอกสาร](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-12 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-12 UTC"],[],[]]
