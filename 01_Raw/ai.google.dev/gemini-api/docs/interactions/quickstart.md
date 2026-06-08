---
source_url: https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=th
fetched_at: 2026-06-08T15:00:32.360526+00:00
title: "\u0e01\u0e32\u0e23\u0e40\u0e23\u0e34\u0e48\u0e21\u0e15\u0e49\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19 Gemini API \u0e2d\u0e22\u0e48\u0e32\u0e07\u0e23\u0e27\u0e14\u0e40\u0e23\u0e47\u0e27 \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การเริ่มต้นใช้งาน Gemini API อย่างรวดเร็ว

การเริ่มต้นอย่างรวดเร็วนี้จะแสดงวิธีติดตั้ง[ไลบรารี](https://ai.google.dev/gemini-api/docs/libraries?hl=th)
ของเราและส่งคำขอแรก สตรีมคำตอบ สร้างการสนทนาหลายรอบ
และใช้เครื่องมือ

คุณสามารถใช้ 2 วิธีต่อไปนี้เพื่อส่งคำขอไปยัง Gemini API

- ***(แนะนำ)*** [Interactions API](https://ai.google.dev/api/interactions-api?hl=th) เป็น Primitive ใหม่ที่มีการรองรับในตัวสำหรับการใช้เครื่องมือหลายขั้นตอน การจัดการเป็นกลุ่ม และขั้นตอนการให้เหตุผลที่ซับซ้อนผ่านขั้นตอนการดำเนินการที่พิมพ์ ในอนาคต โมเดลใหม่ๆ นอกเหนือจากตระกูลหลัก รวมถึงความสามารถและเครื่องมือใหม่ๆ ของเอเจนต์จะเปิดตัวใน Interactions API เท่านั้น
- [`generateContent`](https://ai.google.dev/gemini-api/docs/quickstart?hl=th) มีวิธีสร้างคำตอบแบบไม่เก็บสถานะจากโมเดล แม้ว่าเราจะแนะนำให้ใช้ Interactions API แต่ `generateContent` ก็ได้รับการรองรับอย่างเต็มที่

การเริ่มต้นอย่างรวดเร็วเวอร์ชันนี้ใช้ Interactions API เพื่อส่งคำขอไปยัง Gemini API

## ก่อนเริ่มต้น

หากต้องการใช้ Gemini API คุณต้องมีคีย์ API เพื่อตรวจสอบสิทธิ์คำขอ บังคับใช้ขีดจำกัดด้านความปลอดภัย และติดตามการใช้งานในบัญชี

สร้างคีย์ API ใน AI Studio ฟรีเพื่อเริ่มต้นใช้งาน

[สร้างคีย์ Gemini API](https://aistudio.google.com/app/apikey?hl=th)

## ติดตั้ง Google GenAI SDK

### Python

ใช้ [Python 3.9+](https://www.python.org/downloads/) ขึ้นไป แล้วติดตั้งแพ็กเกจ
[`google-genai` โดยใช้
[คำสั่ง pip](https://packaging.python.org/en/latest/tutorials/installing-packages/) ต่อไปนี้](https://pypi.org/project/google-genai/)

```
pip install -q -U google-genai
```

### JavaScript

ใช้ [Node.js v18+](https://nodejs.org/en/download/package-manager) แล้วติดตั้ง [Google Gen AI SDK สำหรับ TypeScript และ JavaScript](https://www.npmjs.com/package/@google/genai) โดยใช้ [คำสั่ง npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) ต่อไปนี้:

```
npm install @google/genai
```

## สร้างข้อความ

ใช้เมธอด `interactions.create` เพื่อ
[สร้างคำตอบเป็นข้อความ](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=th)

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in a few words",
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## สตรีมคำตอบ

โดยค่าเริ่มต้น โมเดลจะแสดงคำตอบหลังจากกระบวนการสร้างทั้งหมดเสร็จสมบูรณ์แล้วเท่านั้น หากต้องการประสบการณ์การใช้งานที่รวดเร็วและมีการโต้ตอบมากขึ้น คุณสามารถ
[สตรีมคำตอบ](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=th)เป็น Chunk ขณะที่ระบบ
สร้างคำตอบ

### Python

```
stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in detail",
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const stream = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in detail",
    stream: true,
  });

  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

main();
```

### REST

```
# Use alt=sse for streaming
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in detail",
    "stream": true
  }'
```

## การสนทนาหลายรอบ

Gemini API มีการรองรับในตัวสำหรับการสร้าง
[การสนทนาหลายรอบ](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=th#multi-turn-conversations)
เพียงส่ง `id` ที่ได้รับจากการโต้ตอบครั้งก่อนเป็นพารามิเตอร์
`previous_interaction_id` แล้วเซิร์ฟเวอร์จะจัดการ
ประวัติการสนทนาโดยอัตโนมัติ

### Python

```
interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house."
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const interaction2 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
  });
  console.log("Response 2:", interaction2.output_text);
}

main();
```

### REST

```
# Turn 1: Start the conversation
RESPONSE1=$(curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "I have 2 dogs in my house."
  }')

# Extract the interaction ID
INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

# Turn 2: Continue the conversation
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3-flash-preview\",
    \"input\": \"How many paws are in my house?\",
    \"previous_interaction_id\": \"$INTERACTION_ID\"
  }"
```

## ใช้เครื่องมือ

ขยายความสามารถของโมเดลโดย
[การเชื่อมต่อแหล่งข้อมูลคำตอบกับ Google Search](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=th)
เพื่อเข้าถึงเนื้อหาเว็บแบบเรียลไทม์ โมเดลจะตัดสินใจโดยอัตโนมัติว่าจะค้นหาเมื่อใด ดำเนินการค้นหา และสังเคราะห์คำตอบพร้อมการอ้างอิง

ตัวอย่างต่อไปนี้แสดงวิธีเปิดใช้ Google Search

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  - [{annotation.title}]({annotation.url})")
```

### JavaScript

```
async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
  });

  console.log(interaction.output_text);

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text' && contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              console.log(`  - [${annotation.title}](${annotation.url})`);
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

นอกจากนี้ Gemini API ยังรองรับเครื่องมืออื่นๆ ในตัวด้วย ดังนี้

- **[การดำเนินการโค้ด](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=th)**:
  ช่วยให้โมเดลเขียนและเรียกใช้โค้ด Python เพื่อแก้ปัญหาทางคณิตศาสตร์ที่ซับซ้อน
- **[บริบท URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=th)**: ช่วยให้คุณ
  เชื่อมต่อแหล่งข้อมูลคำตอบกับ URL ของหน้าเว็บที่เฉพาะเจาะจงที่คุณระบุ
- **[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=th)**: ช่วยให้คุณ
  อัปโหลดไฟล์และเชื่อมต่อแหล่งข้อมูลคำตอบกับเนื้อหาของไฟล์โดยใช้การค้นหาเชิงความหมาย
- **[Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=th)**: ช่วยให้คุณ
  เชื่อมต่อแหล่งข้อมูลคำตอบกับข้อมูลสถานที่ และค้นหาสถานที่ เส้นทาง และ
  แผนที่
- **[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=th)**: ช่วยให้
  โมเดลโต้ตอบกับหน้าจอ แป้นพิมพ์ และเมาส์ของคอมพิวเตอร์เสมือนเพื่อ
  ทำงานต่างๆ

## เรียกฟังก์ชันที่กำหนดเอง

ใช้**[การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=th)**
เพื่อเชื่อมต่อโมเดลกับเครื่องมือและ API ที่กำหนดเอง โมเดลจะกำหนดเวลาที่จะเรียกฟังก์ชันและแสดงขั้นตอน `function_call` พร้อมอาร์กิวเมนต์เพื่อให้แอปพลิเคชันของคุณดำเนินการ

ตัวอย่างนี้ประกาศฟังก์ชันอุณหภูมิจำลองและตรวจสอบว่าโมเดลต้องการเรียกฟังก์ชันนี้หรือไม่

### Python

```
import json

weather_function = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What's the temperature in London?",
    tools=[weather_function],
)

fc_step = None
for step in interaction.steps:
    if step.type == "function_call":
        fc_step = step
        break

if fc_step:
    print(f"Model requested function: {fc_step.name} with args {fc_step.arguments}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {
                "type": "function_result",
                "name": fc_step.name,
                "call_id": fc_step.id,
                "result": [{"type": "text", "text": json.dumps(mock_result)}],
            }
        ],
        tools=[weather_function],
        previous_interaction_id=interaction.id,
    )
    print("Final Response:", final_interaction.output_text)
```

### JavaScript

```
async function main() {
  const weatherFunction = {
    type: 'function',
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: 'object',
      properties: {
        location: {
          type: 'string',
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const interaction = await ai.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "What's the temperature in London?",
    tools: [weatherFunction],
  });

  const fcStep = interaction.steps.find(s => s.type === 'function_call');
  if (fcStep) {
    console.log(`Model requested function: ${fcStep.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    const finalInteraction = await ai.interactions.create({
      model: 'gemini-3-flash-preview',
      input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [{ type: 'text', text: JSON.stringify(mockResult) }]
      }],
      tools: [weatherFunction],
      previous_interaction_id: interaction.id,
    });

    console.log("Final Response:", finalInteraction.output_text);
  }
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What'\''s the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

## ขั้นตอนถัดไป

เมื่อเริ่มต้นใช้งาน Gemini API แล้ว ให้สำรวจคำแนะนำต่อไปนี้เพื่อสร้างแอปพลิเคชันที่ซับซ้อนมากขึ้น

- [การสร้างข้อความ](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=th)
- [การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=th)
- [การทำความเข้าใจรูปภาพ](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=th)
- [การคิด](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=th)
- [การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=th)
- [การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=th)
- [บริบทแบบยาว](https://ai.google.dev/gemini-api/docs/long-context?hl=th)
- [การฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-01 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-01 UTC"],[],[]]
