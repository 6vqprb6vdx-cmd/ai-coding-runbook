---
source_url: https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=th
fetched_at: 2026-05-18T13:09:18.933891+00:00
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

# ค้นหาไฟล์

Gemini API ช่วยให้ Retrieval Augmented Generation ("RAG") ทำงานได้ผ่านเครื่องมือค้นหาไฟล์ การค้นหาไฟล์จะนำเข้า แบ่ง และจัดทำดัชนีข้อมูลของคุณเพื่อ
ให้ดึงข้อมูลที่เกี่ยวข้องได้อย่างรวดเร็วตามพรอมต์ที่ระบุ จากนั้นระบบจะใช้ข้อมูลที่ดึงมานี้เป็นบริบทสำหรับโมเดล ซึ่งจะช่วยให้โมเดล
ให้คำตอบที่ถูกต้องและเกี่ยวข้องมากขึ้นได้ การค้นหาไฟล์ยังสามารถ
มอบความสามารถแบบหลายรูปแบบด้วยการฝังข้อความที่รองรับโดย
`gemini-embedding-001` และการฝังรูปภาพ/แบบหลายรูปแบบที่รองรับโดย `gemini-embedding-2`

การจัดเก็บไฟล์และการสร้างการฝังในเวลาที่ทำการค้นหาไม่มีค่าใช้จ่าย และคุณจะชำระเงิน
สำหรับการสร้างการฝังเมื่อจัดทำดัชนีไฟล์เป็นครั้งแรกเท่านั้น รวมถึงค่าโทเค็นอินพุต / เอาต์พุตของโมเดล Gemini ปกติ
กระบวนทัศน์การเรียกเก็บเงินแบบใหม่นี้ทำให้เครื่องมือค้นหาไฟล์สร้างและปรับขนาดได้ง่ายขึ้นและคุ้มค่ากว่าเดิม ดูรายละเอียดได้ที่ส่วน[ราคา](#pricing)

## อัปโหลดไปยังร้านค้า File Search โดยตรง

ตัวอย่างนี้แสดงวิธีอัปโหลดไฟล์ไปยัง[ที่เก็บไฟล์ค้นหา](https://ai.google.dev/api/file-search/file-search-stores?hl=th#method:-media.uploadtofilesearchstore)โดยตรง

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'your-fileSearchStore-name',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

operation = client.file_search_stores.upload_to_file_search_store(
  file='sample.txt',
  file_search_store_name=file_search_store.name,
  config={
      'display_name' : 'display-file-name',
  }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Can you tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "file_citation":
                            print(f"  - {annotation.file_name}: {annotation.source}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  // File name will be visible in citations
  const fileSearchStore = await ai.fileSearchStores.create({
    config: {
      displayName: 'your-fileSearchStore-name',
      embeddingModel: 'models/gemini-embedding-2'
    }
  });

  let operation = await ai.fileSearchStores.uploadToFileSearchStore({
    file: 'file.txt',
    fileSearchStoreName: fileSearchStore.name,
    config: {
      displayName: 'file-name',
    }
  });

  while (!operation.done) {
    await new Promise(resolve => setTimeout(resolve, 5000));
    operation = await ai.operations.get({ operation });
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Can you tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'file_citation') {
                console.log(`  - ${annotation.file_name}: ${annotation.source}`);
              }
            }
          }
        }
      }
    }
  }
}

run();
```

ดูข้อมูลเพิ่มเติมได้ที่เอกสารอ้างอิง API สำหรับ [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=th#method:-media.uploadtofilesearchstore)

## การนำเข้าไฟล์

หรือจะอัปโหลดไฟล์ที่มีอยู่แล้วและ[นำเข้าไปยังที่เก็บการค้นหาไฟล์](https://ai.google.dev/api/file-search/file-search-stores?hl=th#method:-filesearchstores.importfile)ก็ได้ โดยทำดังนี้

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
sample_file = client.files.upload(file='sample.txt', config={'display_name': 'display_file_name'})

file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'your-fileSearchStore-name',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

operation = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Can you tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  // File name will be visible in citations
  const sampleFile = await ai.files.upload({
    file: 'sample.txt',
    config: { displayName: 'file-name' }
  });

  const fileSearchStore = await ai.fileSearchStores.create({
    config: {
      displayName: 'your-fileSearchStore-name',
      embeddingModel: 'models/gemini-embedding-2'
    }
  });

  let operation = await ai.fileSearchStores.importFile({
    fileSearchStoreName: fileSearchStore.name,
    fileName: sampleFile.name
  });

  while (!operation.done) {
    await new Promise(resolve => setTimeout(resolve, 5000));
    operation = await ai.operations.get({ operation: operation });
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Can you tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
        }
      }
    }
  }
}

run();
```

ดูข้อมูลเพิ่มเติมได้ที่เอกสารอ้างอิง API สำหรับ [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=th#method:-filesearchstores.importfile)

## การกำหนดค่าการแบ่งกลุ่ม

เมื่อนำเข้าไฟล์ไปยังที่เก็บข้อมูลการค้นหาไฟล์ ระบบจะแบ่งไฟล์ออกเป็น
หลายๆ ชิ้น ฝัง จัดทำดัชนี และอัปโหลดไปยังที่เก็บข้อมูลการค้นหาไฟล์โดยอัตโนมัติ หากต้องการควบคุมกลยุทธ์การแบ่งกลุ่มให้มากขึ้น คุณสามารถระบุการตั้งค่า [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=th#request-body_5)
เพื่อกำหนดจำนวนโทเค็นสูงสุดต่อกลุ่มและจำนวนโทเค็นที่ทับซ้อนกันสูงสุดได้

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
from google.genai import types
import time

client = genai.Client()

operation = client.file_search_stores.upload_to_file_search_store(
    file_search_store_name=file_search_store.name,
    file='sample.txt',
    config={
        'chunking_config': {
          'white_space_config': {
            'max_tokens_per_chunk': 200,
            'max_overlap_tokens': 20
          }
        }
    }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

print("Custom chunking complete.")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

let operation = await ai.fileSearchStores.uploadToFileSearchStore({
  file: 'file.txt',
  fileSearchStoreName: fileSearchStore.name,
  config: {
    displayName: 'file-name',
    chunkingConfig: {
      whiteSpaceConfig: {
        maxTokensPerChunk: 200,
        maxOverlapTokens: 20
      }
    }
  }
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 5000));
  operation = await ai.operations.get({ operation });
}
console.log("Custom chunking complete.");
```

หากต้องการใช้ที่เก็บข้อมูลการค้นหาไฟล์ ให้ส่งเป็นเครื่องมือไปยังเมธอด `interactions.create`
ดังที่แสดงในตัวอย่าง[อัปโหลด](#upload)และ[นำเข้า](#importing-files)

## วิธีการทำงาน

การค้นหาไฟล์ใช้เทคนิคที่เรียกว่าการค้นหาเชิงความหมายเพื่อค้นหาข้อมูลที่เกี่ยวข้องกับพรอมต์ของผู้ใช้ การค้นหาเชิงความหมาย จะเข้าใจความหมายและบริบทของคำค้นหา ซึ่งแตกต่างจากการค้นหาตามคีย์เวิร์ดมาตรฐาน

เมื่อนำเข้าไฟล์ ระบบจะแปลงไฟล์เป็นตัวแทนเชิงตัวเลขที่เรียกว่า
[การฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th) ซึ่งจะบันทึกความหมายเชิงความหมายของ
เนื้อหาที่อัปโหลด โดยระบบจะจัดเก็บการฝังเหล่านี้ไว้ในฐานข้อมูลการค้นหาไฟล์เฉพาะ
เมื่อคุณทำการค้นหา ระบบจะแปลงการค้นหานั้นเป็น Embedding ด้วย จากนั้นระบบจะ
ทำการค้นหาไฟล์เพื่อค้นหาเอกสารที่คล้ายกันและเกี่ยวข้องมากที่สุด
จากที่เก็บข้อมูลการค้นหาไฟล์

ไม่มี Time To Live (TTL) สำหรับการฝัง
โดยจะยังคงอยู่จนกว่าจะถูกลบด้วยตนเองหรือเมื่อมีการเลิกใช้งานโมเดล แต่ระบบจะลบไฟล์หลังจากผ่านไป 48 ชั่วโมง

ขั้นตอนการใช้ File Search
`uploadToFileSearchStore` API มีดังนี้

1. **สร้างที่เก็บข้อมูลการค้นหาไฟล์**: ที่เก็บข้อมูลการค้นหาไฟล์มีข้อมูลที่ประมวลผลแล้วจากไฟล์ ซึ่งเป็นคอนเทนเนอร์แบบถาวรสำหรับ Embedding ที่การค้นหาเชิงความหมายจะทำงานด้วย
2. **อัปโหลดไฟล์และนำเข้าไปยังร้านค้า File Search**: อัปโหลดไฟล์พร้อมกัน
   และนำเข้าผลลัพธ์ไปยังร้านค้า File Search ซึ่งจะสร้าง`File`ออบเจ็กต์ชั่วคราว ซึ่งเป็นข้อมูลอ้างอิงถึงเอกสารดิบ จากนั้นระบบจะแบ่งข้อมูลออกเป็นส่วนๆ แปลงเป็นข้อมูลฝังสำหรับการค้นหาไฟล์ และจัดทำดัชนี `File`
   ระบบจะลบออบเจ็กต์หลังจาก 48 ชั่วโมง ส่วนข้อมูลที่นำเข้าไปยังที่เก็บข้อมูลการค้นหาไฟล์
   จะจัดเก็บไว้เรื่อยๆ จนกว่าคุณจะเลือกให้ลบ
3. **ค้นหาด้วยการค้นหาไฟล์**: สุดท้ายนี้ คุณใช้เครื่องมือ `FileSearch` ในการโทร `generateContent` ในการกำหนดค่าเครื่องมือ คุณจะระบุ
   `FileSearchRetrievalResource`ซึ่งชี้ไปยัง `FileSearchStore` ที่ต้องการ
   ค้นหา ซึ่งจะบอกโมเดลให้ทำการค้นหาเชิงความหมายในที่เก็บข้อมูลการค้นหาไฟล์นั้นๆ เพื่อค้นหาข้อมูลที่เกี่ยวข้องมาใช้เป็นพื้นฐานในการตอบ

![กระบวนการจัดทำดัชนีและการค้นหาของเครื่องมือค้นหาไฟล์](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=th)

กระบวนการจัดทำดัชนีและการค้นหาของ File Search

ในแผนภาพนี้ เส้นประจาก*เอกสาร*ไปยัง*โมเดลการฝัง*
(ใช้ [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=th))
แสดงถึง `uploadToFileSearchStore` API (ข้าม*ที่เก็บไฟล์*)
หรือการใช้ [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=th) เพื่อสร้างแยกกัน
แล้วนำเข้าไฟล์จะย้ายกระบวนการจัดทำดัชนีจาก *Documents* ไปยัง
*File storage* แล้วจึงไปยัง *Embedding model*

## File Search stores

ที่เก็บการค้นหาไฟล์คือคอนเทนเนอร์สำหรับการฝังเอกสาร แม้ว่าระบบจะลบไฟล์ดิบที่อัปโหลดผ่าน File API หลังจาก 48 ชั่วโมง แต่ข้อมูลที่นำเข้าไปยังที่เก็บข้อมูลการค้นหาไฟล์จะจัดเก็บไว้เรื่อยๆ จนกว่าคุณจะลบด้วยตนเอง คุณสามารถ
สร้างที่เก็บการค้นหาไฟล์หลายรายการเพื่อจัดระเบียบเอกสารได้
`FileSearchStore` API ช่วยให้คุณสร้าง แสดงรายการ รับ และลบเพื่อจัดการร้านค้า
การค้นหาไฟล์ได้ ชื่อร้านค้าของ File Search จะมีขอบเขตทั่วโลก

ตัวอย่างวิธีจัดการร้านค้าที่ค้นหาไฟล์มีดังนี้

### Python

```
# This will only work for SDK newer than 2.0.0
file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'my-file_search-store-123',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

for file_search_store in client.file_search_stores.list():
    print(file_search_store)

my_file_search_store = client.file_search_stores.get(name='fileSearchStores/my-file_search-store-123')

client.file_search_stores.delete(name='fileSearchStores/my-file_search-store-123', config={'force': True})
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const fileSearchStore = await ai.fileSearchStores.create({
  config: {
    displayName: 'my-file_search-store-123',
    embeddingModel: 'models/gemini-embedding-2'
  }
});

const fileSearchStores = await ai.fileSearchStores.list();
for await (const store of fileSearchStores) {
  console.log(store);
}

const myFileSearchStore = await ai.fileSearchStores.get({
  name: 'fileSearchStores/my-file_search-store-123'
});

await ai.fileSearchStores.delete({
  name: 'fileSearchStores/my-file_search-store-123',
  config: { force: true }
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \
    -H "Content-Type: application/json" \
    -d '{ "displayName": "My Store", "embedding_model": "models/gemini-embedding-2" }'

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"
```

## เอกสารการค้นหาไฟล์

คุณจัดการเอกสารแต่ละรายการในที่เก็บไฟล์ได้ด้วย API [File Search Documents](https://ai.google.dev/api/file-search/documents?hl=th) เพื่อ`list`เอกสารแต่ละรายการ
ในที่เก็บการค้นหาไฟล์ `get`ข้อมูลเกี่ยวกับเอกสาร และ`delete`เอกสาร
ตามชื่อ

### Python

```
# This will only work for SDK newer than 2.0.0
for document_in_store in client.file_search_stores.documents.list(parent='fileSearchStores/my-file_search-store-123'):
  print(document_in_store)

file_search_document = client.file_search_stores.documents.get(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
print(file_search_document)

client.file_search_stores.documents.delete(name='fileSearchStores/my-file_search-store-123/documents/my_doc', config={'force': True})
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const documents = await ai.fileSearchStores.documents.list({
  parent: 'fileSearchStores/my-file_search-store-123'
});
for await (const doc of documents) {
  console.log(doc);
}

const fileSearchDocument = await ai.fileSearchStores.documents.get({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc'
});

await ai.fileSearchStores.documents.delete({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc'
});
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}&force=true"
```

## ข้อมูลเมตาของไฟล์

คุณสามารถเพิ่มข้อมูลเมตาที่กำหนดเองลงในไฟล์เพื่อช่วยกรองไฟล์หรือให้บริบทเพิ่มเติมได้ ข้อมูลเมตาคือชุดคู่คีย์-ค่า

### Python

```
# This will only work for SDK newer than 2.0.0
op = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
    config={
        'custom_metadata': [
            {"key": "author", "string_value": "Robert Graves"},
            {"key": "year", "numeric_value": 1934}
        ]
    }
)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
let operation = await ai.fileSearchStores.importFile({
  fileSearchStoreName: fileSearchStore.name,
  fileName: sampleFile.name,
  config: {
    customMetadata: [
      { key: "author", stringValue: "Robert Graves" },
      { key: "year", numericValue: 1934 }
    ]
  }
});
```

ซึ่งจะมีประโยชน์เมื่อคุณมีเอกสารหลายฉบับในที่เก็บการค้นหาไฟล์และต้องการ
ค้นหาเฉพาะชุดย่อยของเอกสารเหล่านั้น

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me about the book 'I, Claudius'",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name],
        "metadata_filter": 'author="Robert Graves"',
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const interaction = await ai.interactions.create({
  model: "gemini-3-flash-preview",
  input: "Tell me about the book 'I, Claudius'",
  tools: [{
    type: "file_search",
    file_search_store_names: [fileSearchStore.name],
    metadata_filter: 'author="Robert Graves"',
  }]
});

for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
      }
    }
  }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -X POST \
    -d '{
            "model": "gemini-3-flash-preview",
            "input": [{"type": "text", "text": "Tell me about the book I, Claudius"}],
            "tools": [{
                "type": "file_search",
                "file_search_store_names": ["'$STORE_NAME'"],
                "metadata_filter": "author = \"Robert Graves\""
            }]
        }' 2> /dev/null > response.json

cat response.json
```

ดูคำแนะนำในการใช้ไวยากรณ์ตัวกรองรายการสำหรับ `metadata_filter` ได้ที่ [google.aip.dev/160](https://google.aip.dev/160)

## การค้นหาไฟล์หลายรูปแบบ

การค้นหาไฟล์แบบมัลติโมดัลช่วยให้คุณฝังและค้นหารูปภาพได้โดยตรง
ซึ่งจะช่วยให้แอปพลิเคชัน RAG แบบมัลติโมดัลมีความสมบูรณ์ยิ่งขึ้น

### กำหนดค่าโมเดลการฝัง

เมื่อสร้าง `FileSearchStore` คุณต้องลบล้างโมเดลการฝังข้อความเท่านั้นเริ่มต้นเพื่อใช้โมเดลแบบมัลติโมดัล ใช้ `models/gemini-embedding-2` เพื่อ
ประมวลผลทั้งข้อความและรูปภาพ

### Python

```
store = client.file_search_stores.create(
    config={
        "display_name": "Multimodal Catalog",
        "embedding_model": "models/gemini-embedding-2",
    }
)
```

### JavaScript

```
const fileSearchStore = await ai.fileSearchStores.create({
  config: {
    displayName: "Multimodal Catalog",
    embeddingModel: "models/gemini-embedding-2",
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "display_name": "Multimodal Catalog",
      "embedding_model": "models/gemini-embedding-2"
    }'
```

### อัปโหลดรูปภาพ

หลังจากสร้างร้านค้าด้วยโมเดลการฝังแบบมัลติโมดัลแล้ว คุณจะอัปโหลดไฟล์รูปภาพได้โดยตรงโดยใช้ API การอัปโหลดเดียวกันที่อธิบายไว้ใน[อัปโหลดไปยังร้านค้าการค้นหาไฟล์โดยตรง](#upload)หรือ[การนำเข้าไฟล์](#importing-files)

**ข้อกำหนดเกี่ยวกับไฟล์รูปภาพ:**

- ไฟล์รูปภาพต้องมีความละเอียดไม่เกิน 4K x 4K พิกเซล
- รูปแบบที่รองรับ ได้แก่ PNG, JPEG

## การอ้างอิง

เมื่อคุณใช้การค้นหาไฟล์ คำตอบของโมเดลอาจมีการอ้างอิงที่ระบุส่วนของเอกสารที่คุณอัปโหลดซึ่งใช้ในการสร้างคำตอบ ซึ่งจะช่วยในการตรวจสอบข้อเท็จจริงและการยืนยัน

คุณเข้าถึงข้อมูลการอ้างอิงได้ผ่านแอตทริบิวต์ `annotations` ภายในบล็อก `content` ของคำตอบในขั้นตอน `model_output`

### Python

```
# This will only work for SDK newer than 2.0.0
for step in interaction.steps:
    if step.type == 'model_output':
        for content in step.content:
            if content.type == 'text' and content.annotations:
                print(content.annotations)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text' && contentBlock.annotations) {
        console.log(JSON.stringify(contentBlock.annotations, null, 2));
      }
    }
  }
}
```

ดูข้อมูลโดยละเอียดเกี่ยวกับโครงสร้างของการอ้างอิงได้ที่[การอ้างอิง API สำหรับการโต้ตอบ](https://ai.google.dev/api/interactions-api?hl=th#Resource:FileCitation)

### หมายเลขหน้า

เมื่อคุณใช้การค้นหาไฟล์กับเอกสารที่มีหน้า (เช่น PDF) คำตอบของโมเดลอาจมีหมายเลขหน้าที่พบข้อมูล
คุณเข้าถึงข้อมูลนี้ได้ผ่านแอตทริบิวต์ `page_number` ของคำอธิบายประกอบ
`file_citation`

### Python

```
# Iterate through citations and check for page numbers
for step in interaction.steps:
    if step.type == "model_output":
        for content in step.content:
            if content.type == "text" and content.annotations:
                for annotation in content.annotations:
                    if annotation.type == "file_citation" and annotation.page_number:
                        print(f"Cited Page: {annotation.page_number}")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const block of step.content) {
      if (block.type === 'text' && block.annotations) {
        for (const annotation of block.annotations) {
          if (annotation.type === 'file_citation' && annotation.pageNumber) {
            console.log(`Cited Page: ${annotation.pageNumber}`);
          }
        }
      }
    }
  }
}
```

### การอ้างอิงสื่อ

เมื่อโมเดลอ้างอิงก้อนรูปภาพในระหว่างการสร้าง API จะแสดงคำอธิบายประกอบประเภท `file_citation` ในคำอธิบายประกอบซึ่งมี `media_id` คุณใช้รหัสนี้เพื่อดาวน์โหลดก้อนข้อมูลรูปภาพที่โมเดลอ้างอิงได้ `media_id`นี้
จะคงอยู่ในการเรียกค้นหาหลายครั้ง ซึ่งช่วยให้คุณเรียก
รูปภาพเดียวกันหรือแคชรูปภาพได้อย่างน่าเชื่อถือโดยใช้รหัส

ข้อมูลโค้ดต่อไปนี้เป็นตัวอย่างขั้นตอนการตอบกลับ REST

```
{
  "type": "model_output",
  "content": [
    {
      "type": "text",
      "text": "...",
      "annotations": [
        {
          "type": "file_citation",
          "file_name": "product_image",
          "media_id": "fileSearchStores/my-store-123/media/BlobId-456"
        }
      ]
    }
  ]
}
```

ข้อมูลโค้ดต่อไปนี้แสดงวิธีดึงข้อมูล `media_id` และ
ดาวน์โหลดสื่อ

### Python

```
# Iterate through citations and download media if present
for step in interaction.steps:
    if step.type == "model_output":
        for content in step.content:
            if content.type == "text" and content.annotations:
                for annotation in content.annotations:
                    if annotation.type == "file_citation" and annotation.media_id:
                        print(f"Cited Media ID: {annotation.media_id}")
                        # Download the blob using the SDK
                        blob_content = client.file_search_stores.download_media(
                            media_id=annotation.media_id
                        )
                        # Save blob_content to file...
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const block of step.content) {
      if (block.type === 'text' && block.annotations) {
        for (const annotation of block.annotations) {
          if (annotation.type === 'file_citation' && annotation.mediaId) {
            console.log(`Cited Media ID: ${annotation.mediaId}`);
            const blobContent = await ai.fileSearchStores.downloadMedia(annotation.mediaId);
            // Save blobContent to file...
          }
        }
      }
    }
  }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1/fileSearchStores/my-store-123/media/BlobId-456" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## ข้อมูลเมตาที่กำหนดเอง

หากเพิ่มข้อมูลเมตาที่กำหนดเองลงในไฟล์ คุณจะเข้าถึงข้อมูลเมตาดังกล่าวได้ใน
คำอธิบายประกอบของคำตอบของโมเดล ซึ่งมีประโยชน์สำหรับการส่งบริบทเพิ่มเติม (เช่น URL, หมายเลขหน้า หรือผู้เขียน) จากเอกสารต้นฉบับไปยังตรรกะของแอปพลิเคชัน คำอธิบายประกอบการอ้างอิงแต่ละรายการของประเภท `file_citation`
มีข้อมูลเมตาที่กำหนดเองนี้

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.annotations:
                for annotation in content_block.annotations:
                    print(annotation)
```

### JavaScript

```
  // This will only work for SDK newer than 2.0.0
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.annotations) {
          contentBlock.annotations.forEach((annotation) => {
            console.log(annotation);
          });
        }
      }
    }
  }
```

### REST

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "...",
          "annotations": [
            {
              "file_name": "...",
              "source": "...",
              "custom_metadata": [
                {
                  "key": "author",
                  "string_value": "Robert Graves"
                },
                {
                  "key": "year",
                  "numeric_value": 1934
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## เอาต์พุตที่มีโครงสร้าง

ตั้งแต่โมเดล Gemini 3 เป็นต้นไป คุณจะใช้เครื่องมือค้นหาไฟล์ร่วมกับ[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=th)ได้

### Python

```
# This will only work for SDK newer than 2.0.0
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the minimum hourly wage in Tokyo right now?",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Money.model_json_schema()
    },
)
result = Money.model_validate_json(interaction.steps[-1].content[0].text)
print(result)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { z } from "zod";

const moneyJsonSchema = {
  type: "object",
  properties: {
    amount: { type: "string", description: "The numerical part of the amount." },
    currency: { type: "string", description: "The currency of amount." }
  },
  required: ["amount", "currency"]
};

const moneySchema = z.fromJSONSchema(moneyJsonSchema);

async function run() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What is the minimum hourly wage in Tokyo right now?",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name],
    }],
    response_format: {
      type: 'text',
      mime_type: 'application/json',
      schema: moneyJsonSchema
    },
  });

  const result = moneySchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
  console.log(result);
}

run();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -X POST \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the minimum hourly wage in Tokyo right now?",
    "tools": [{
      "type": "file_search",
      "file_search_store_names": ["$FILE_SEARCH_STORE_NAME"]
    }],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "amount": {"type": "string", "description": "The numerical part of the amount."},
          "currency": {"type": "string", "description": "The currency of amount."}
        },
        "required": ["amount", "currency"]
      }
    }
  }'
```

## โมเดลที่รองรับ

รุ่นต่อไปนี้รองรับการค้นหาไฟล์

| รุ่น | ค้นหาไฟล์ |
| --- | --- |
| [ตัวอย่าง Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=th) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) | ✔️ |
| [Gemini 3.1 Flash-Lite (เวอร์ชันตัวอย่าง)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=th) | ✔️ |
| [ตัวอย่าง Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=th) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=th) | ✔️ |

## ชุดเครื่องมือที่รองรับ

โมเดล Gemini 3 รองรับการรวมเครื่องมือในตัว (เช่น การค้นหาไฟล์) กับเครื่องมือที่กำหนดเอง (การเรียกใช้ฟังก์ชัน) ดูข้อมูลเพิ่มเติมได้ที่หน้า[ชุดเครื่องมือ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=th)

## ประเภทไฟล์ที่สนับสนุน

การค้นหาไฟล์รองรับรูปแบบไฟล์หลากหลายรูปแบบตามที่ระบุไว้ในส่วนต่อไปนี้

### ประเภทไฟล์แอปพลิเคชัน

- `application/dart`
- `application/ecmascript`
- `application/json`
- `application/ms-java`
- `application/msword`
- `application/pdf`
- `application/sql`
- `application/typescript`
- `application/vnd.curl`
- `application/vnd.dart`
- `application/vnd.ibm.secure-container`
- `application/vnd.jupyter`
- `application/vnd.ms-excel`
- `application/vnd.oasis.opendocument.text`
- `application/vnd.openxmlformats-officedocument.presentationml.presentation`
- `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.template`
- `application/x-csh`
- `application/x-hwp`
- `application/x-hwp-v5`
- `application/x-latex`
- `application/x-php`
- `application/x-powershell`
- `application/x-sh`
- `application/x-shellscript`
- `application/x-tex`
- `application/x-zsh`
- `application/xml`
- `application/zip`

### ประเภทไฟล์ข้อความ

- `text/1d-interleaved-parityfec`
- `text/RED`
- `text/SGML`
- `text/cache-manifest`
- `text/calendar`
- `text/cql`
- `text/cql-extension`
- `text/cql-identifier`
- `text/css`
- `text/csv`
- `text/csv-schema`
- `text/dns`
- `text/encaprtp`
- `text/enriched`
- `text/example`
- `text/fhirpath`
- `text/flexfec`
- `text/fwdred`
- `text/gff3`
- `text/grammar-ref-list`
- `text/hl7v2`
- `text/html`
- `text/javascript`
- `text/jcr-cnd`
- `text/jsx`
- `text/markdown`
- `text/mizar`
- `text/n3`
- `text/parameters`
- `text/parityfec`
- `text/php`
- `text/plain`
- `text/provenance-notation`
- `text/prs.fallenstein.rst`
- `text/prs.lines.tag`
- `text/prs.prop.logic`
- `text/raptorfec`
- `text/rfc822-headers`
- `text/rtf`
- `text/rtp-enc-aescm128`
- `text/rtploopback`
- `text/rtx`
- `text/sgml`
- `text/shaclc`
- `text/shex`
- `text/spdx`
- `text/strings`
- `text/t140`
- `text/tab-separated-values`
- `text/texmacs`
- `text/troff`
- `text/tsv`
- `text/tsx`
- `text/turtle`
- `text/ulpfec`
- `text/uri-list`
- `text/vcard`
- `text/vnd.DMClientScript`
- `text/vnd.IPTC.NITF`
- `text/vnd.IPTC.NewsML`
- `text/vnd.a`
- `text/vnd.abc`
- `text/vnd.ascii-art`
- `text/vnd.curl`
- `text/vnd.debian.copyright`
- `text/vnd.dvb.subtitle`
- `text/vnd.esmertec.theme-descriptor`
- `text/vnd.exchangeable`
- `text/vnd.familysearch.gedcom`
- `text/vnd.ficlab.flt`
- `text/vnd.fly`
- `text/vnd.fmi.flexstor`
- `text/vnd.gml`
- `text/vnd.graphviz`
- `text/vnd.hans`
- `text/vnd.hgl`
- `text/vnd.in3d.3dml`
- `text/vnd.in3d.spot`
- `text/vnd.latex-z`
- `text/vnd.motorola.reflex`
- `text/vnd.ms-mediapackage`
- `text/vnd.net2phone.commcenter.command`
- `text/vnd.radisys.msml-basic-layout`
- `text/vnd.senx.warpscript`
- `text/vnd.sosi`
- `text/vnd.sun.j2me.app-descriptor`
- `text/vnd.trolltech.linguist`
- `text/vnd.wap.si`
- `text/vnd.wap.sl`
- `text/vnd.wap.wml`
- `text/vnd.wap.wmlscript`
- `text/vtt`
- `text/wgsl`
- `text/x-asm`
- `text/x-bibtex`
- `text/x-boo`
- `text/x-c`
- `text/x-c++hdr`
- `text/x-c++src`
- `text/x-cassandra`
- `text/x-chdr`
- `text/x-coffeescript`
- `text/x-component`
- `text/x-csh`
- `text/x-csharp`
- `text/x-csrc`
- `text/x-cuda`
- `text/x-d`
- `text/x-diff`
- `text/x-dsrc`
- `text/x-emacs-lisp`
- `text/x-erlang`
- `text/x-gff3`
- `text/x-go`
- `text/x-haskell`
- `text/x-java`
- `text/x-java-properties`
- `text/x-java-source`
- `text/x-kotlin`
- `text/x-lilypond`
- `text/x-lisp`
- `text/x-literate-haskell`
- `text/x-lua`
- `text/x-moc`
- `text/x-objcsrc`
- `text/x-pascal`
- `text/x-pcs-gcd`
- `text/x-perl`
- `text/x-perl-script`
- `text/x-python`
- `text/x-python-script`
- `text/x-r-markdown`
- `text/x-rsrc`
- `text/x-rst`
- `text/x-ruby-script`
- `text/x-rust`
- `text/x-sass`
- `text/x-scala`
- `text/x-scheme`
- `text/x-script.python`
- `text/x-scss`
- `text/x-setext`
- `text/x-sfv`
- `text/x-sh`
- `text/x-siesta`
- `text/x-sos`
- `text/x-sql`
- `text/x-swift`
- `text/x-tcl`
- `text/x-tex`
- `text/x-vbasic`
- `text/x-vcalendar`
- `text/xml`
- `text/xml-dtd`
- `text/xml-external-parsed-entity`
- `text/yaml`

## ข้อจำกัด

- **Live API:** ไม่รองรับการค้นหาไฟล์ใน
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=th)
- **เครื่องมือไม่รองรับ:** ขณะนี้การค้นหาไฟล์ใช้ร่วมกับเครื่องมืออื่นๆ ไม่ได้ เช่น [การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=th), [บริบท URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=th) เป็นต้น

### ขีดจำกัดอัตรา

File Search API มีขีดจำกัดต่อไปนี้เพื่อบังคับใช้ความเสถียรของบริการ

- **ขนาดไฟล์สูงสุด / ขีดจำกัดต่อเอกสาร**: 100 MB
- **ขนาดรวมของที่เก็บข้อมูลการค้นหาไฟล์ของโปรเจ็กต์** (อิงตามระดับผู้ใช้)
  - **ฟรี**: 1 GB
  - **ระดับ 1**: 10 GB
  - **ระดับ 2**: 100 GB
  - **ระดับ 3**: 1 TB
- **คำแนะนำ**: จำกัดขนาดของที่เก็บข้อมูลการค้นหาไฟล์แต่ละรายการให้ต่ำกว่า 20 GB เพื่อให้มั่นใจว่าเวลาในการดึงข้อมูลจะเหมาะสมที่สุด

## ราคา

- ระบบจะเรียกเก็บเงินค่า Embedding จากคุณในเวลาที่จัดทำดัชนีตาม[ราคา Embedding](https://ai.google.dev/gemini-api/docs/pricing?hl=th#gemini-embedding-2) ที่มีอยู่
- โดยไม่มีค่าใช้จ่าย
- การฝังเวลาการค้นหาไม่มีค่าใช้จ่าย
- ระบบจะเรียกเก็บเงินสำหรับโทเค็นเอกสารที่ดึงมาเป็น[โทเค็นบริบท](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=th)ปกติ

## ขั้นตอนถัดไป

- ไปที่เอกสารอ้างอิง API สำหรับ[ร้านค้าค้นหาไฟล์](https://ai.google.dev/api/file-search/file-search-stores?hl=th)และ[เอกสาร](https://ai.google.dev/api/file-search/documents?hl=th)การค้นหาไฟล์

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-12 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-12 UTC"],[],[]]
