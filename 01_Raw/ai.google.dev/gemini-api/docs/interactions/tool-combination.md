---
source_url: https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=th
fetched_at: 2026-05-25T13:00:00.294960+00:00
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

# รวมเครื่องมือในตัวและการเรียกฟังก์ชัน

Gemini อนุญาตให้รวม[เครื่องมือในตัว](https://ai.google.dev/gemini-api/docs/tools?hl=th) เช่น
`google_search` และ[การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=th)
(หรือที่เรียกว่า*เครื่องมือที่กำหนดเอง*) ไว้ในการโต้ตอบครั้งเดียวโดยการเก็บรักษาและแสดง
ประวัติบริบทของการเรียกเครื่องมือ ชุดค่าผสมของเครื่องมือในตัวและเครื่องมือที่กำหนดเองช่วยให้เวิร์กโฟลว์ของ Agent มีความซับซ้อนมากขึ้น เช่น โมเดลสามารถอ้างอิงข้อมูลเว็บแบบเรียลไทม์ก่อนที่จะเรียกตรรกะทางธุรกิจที่เฉพาะเจาะจงของคุณ

ตัวอย่างต่อไปนี้แสดงวิธีเปิดใช้ชุดค่าผสมของเครื่องมือในตัวและเครื่องมือที่กำหนดเองด้วย `google_search` และฟังก์ชันที่กำหนดเอง `getWeather`

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
  "model": "gemini-3.5-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## วิธีการทำงาน

โมเดล Gemini 3 ใช้ *การหมุนเวียนบริบทของเครื่องมือ* เพื่อเปิดใช้ชุดค่าผสมของเครื่องมือในตัวและเครื่องมือที่กำหนดเอง การหมุนเวียนบริบทของเครื่องมือช่วยให้เก็บรักษาและแสดงบริบทของเครื่องมือในตัว รวมถึงแชร์บริบทดังกล่าวกับเครื่องมือที่กำหนดเองในการโต้ตอบเดียวกันได้

### เปิดใช้ชุดค่าผสมของเครื่องมือ

- ใส่ [`function_declarations`](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=th#function-declarations) พร้อมกับเครื่องมือในตัวที่ต้องการใช้เพื่อทริกเกอร์ลักษณะการทำงานของชุดค่าผสม

### ขั้นตอนที่ API แสดงผล

ในการตอบกลับการโต้ตอบ API จะแสดงผลขั้นตอนแยกต่างหากสำหรับการเรียกเครื่องมือในตัวและการเรียกฟังก์ชัน (เครื่องมือที่กำหนดเอง) ดังนี้

- **ขั้นตอนเครื่องมือในตัว**: API จะจัดการขั้นตอนเหล่านี้โดยอัตโนมัติ โดยจะเก็บรักษา
  บริบทไว้ในแต่ละรอบ
- **ขั้นตอนการเรียกฟังก์ชัน**: API จะแสดงผลขั้นตอน `function_call` สำหรับฟังก์ชันที่กำหนดเอง
  คุณต้องรันฟังก์ชันและแสดงผลลัพธ์กลับมา

### ช่องที่สำคัญในขั้นตอนที่แสดงผล

ช่องบางช่องในขั้นตอนที่แสดงผลมีความสำคัญต่อการเก็บรักษาบริบทของเครื่องมือและการเปิดใช้ชุดค่าผสมของเครื่องมือ

- **`id`**: พบในขั้นตอน `function_call` และ `function_response` ตัวระบุที่ไม่ซ้ำกันซึ่งจับคู่การเรียกกับการตอบกลับ
- **`signature`**: พบในขั้นตอน `thought` รวมถึงขั้นตอนการเรียกเครื่องมือทั้งหมด (เช่น `function_call`) และขั้นตอนผลลัพธ์ (เช่น `function_response`) สำหรับโมเดล Gemini 3 ขึ้นไป บริบทที่เข้ารหัสนี้จะเปิดใช้**การหมุนเวียนบริบทของเครื่องมือ** ในการโต้ตอบต่างๆ

**การจัดการช่องเหล่านี้:**

- **โหมด Stateful (แนะนำ)**: เมื่อคุณใช้ `previous_interaction_id` เซิร์ฟเวอร์จะจัดการทั้งช่อง `id` และ `signature` โดยอัตโนมัติ
- **โหมด Stateless**: เมื่อจัดการประวัติการสนทนาด้วยตนเอง คุณต้องส่งทั้งช่อง `id` และ `signature` กลับไปยังโมเดลในคำขอที่ตามมาเพื่อตรวจสอบความถูกต้องและเก็บรักษาบริบท SDK อย่างเป็นทางการจะจัดการขั้นตอนนี้โดยอัตโนมัติหากคุณส่งออบเจ็กต์การตอบกลับแบบเต็มกลับไปยังประวัติ

### ข้อมูลเฉพาะของเครื่องมือ

เครื่องมือในตัวบางรายการจะแสดงผลอาร์กิวเมนต์ข้อมูลที่ผู้ใช้มองเห็นได้ซึ่งเฉพาะเจาะจงกับประเภทเครื่องมือ

| เครื่องมือ | อาร์กิวเมนต์การเรียกเครื่องมือที่ผู้ใช้มองเห็นได้ (หากมี) | การตอบกลับของเครื่องมือที่ผู้ใช้มองเห็นได้ (หากมี) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` URL ที่จะเรียกดู | `status`: สถานะการเรียกดู `retrieved_url`: URL ที่เรียกดู |
| **file\_search** | ไม่มี | ไม่มี |

## โทเค็นและการกำหนดราคา

โปรดทราบว่าระบบจะนับส่วนการเรียกเครื่องมือในตัวในคำขอรวมกับ `prompt_token_count` เนื่องจากตอนนี้คุณสามารถมองเห็นและรับขั้นตอนเครื่องมือระดับกลางเหล่านี้ได้ ขั้นตอนดังกล่าวจึงเป็นส่วนหนึ่งของประวัติการสนทนา กรณีนี้จะเกิดขึ้นกับ
กรณีสำหรับ *คำขอ* เท่านั้น ไม่ใช่ *การตอบกลับ*

เครื่องมือ Google Search เป็นข้อยกเว้นของกฎนี้ Google Search ใช้โมเดลการกำหนดราคาของตัวเองในระดับคําค้นหาอยู่แล้ว ดังนั้นระบบจึงไม่คิดค่าบริการโทเค็นซ้ำ (ดูหน้า [การกำหนดราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th))

อ่านข้อมูลเพิ่มเติมได้ในหน้า[โทเค็น](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=th)

## ข้อจำกัด

- ตั้งค่าเป็นโหมด `validated` โดยค่าเริ่มต้น (ไม่รองรับโหมด `auto`) เมื่อเปิดใช้การหมุนเวียนบริบทของเครื่องมือ
- เครื่องมือในตัว เช่น `google_search` อาศัยข้อมูลตำแหน่งและเวลาปัจจุบัน ดังนั้นหาก `system_instruction` หรือ `function_declaration.description` มีข้อมูลตำแหน่งและเวลาที่ไม่สอดคล้องกัน ฟีเจอร์ชุดค่าผสมของเครื่องมืออาจทำงานได้ไม่ดี

## เครื่องมือที่รองรับ

การหมุนเวียนบริบทของเครื่องมือมาตรฐานใช้ได้กับเครื่องมือฝั่งเซิร์ฟเวอร์ (ในตัว)
การรันโค้ดก็เป็นเครื่องมือฝั่งเซิร์ฟเวอร์เช่นกัน แต่มีโซลูชันในตัวสำหรับการหมุนเวียนบริบท การใช้คอมพิวเตอร์และการเรียกฟังก์ชันเป็นเครื่องมือฝั่งไคลเอ็นต์ และมีโซลูชันในตัวสำหรับการหมุนเวียนบริบทด้วย

| เครื่องมือ | ฝั่งการดำเนินการ | การรองรับการหมุนเวียนบริบท |
| --- | --- | --- |
| [Google Search](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ |
| [Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ |
| [บริบท URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ |
| [การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ |
| [การรันโค้ด](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ (ในตัว ใช้ขั้นตอน `code_execution` และ `code_execution_result`) |
| [การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=th) | ฝั่งไคลเอ็นต์ | รองรับ (ในตัว ใช้ขั้นตอน `function_call` และ `function_response`) |
| [ฟังก์ชันที่กำหนดเอง](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=th) | ฝั่งไคลเอ็นต์ | รองรับ (ในตัว ใช้ขั้นตอน `function_call` และ `function_response`) |

## ขั้นตอนถัดไป

- ดูข้อมูลเพิ่มเติมเกี่ยวกับ[การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=th)ใน Gemini API
- สำรวจเครื่องมือที่รองรับ
  - [Google Search](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=th)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=th)
  - [บริบท URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=th)
  - [การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-19 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-19 UTC"],[],[]]
