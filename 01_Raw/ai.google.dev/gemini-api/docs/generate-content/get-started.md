---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th
fetched_at: 2026-06-29T05:29:32.398035+00:00
title: "\u0e01\u0e32\u0e23\u0e40\u0e23\u0e34\u0e48\u0e21\u0e15\u0e49\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การเริ่มต้นใช้งาน

คู่มือนี้จะช่วยให้คุณเริ่มต้นใช้งาน **generateContent** API แบบเดิม สำหรับโปรเจ็กต์และแอปพลิเคชันใหม่ เราขอแนะนำให้ใช้ **Interactions API** ใหม่แทน ซึ่งมีอินเทอร์เฟซที่เรียบง่ายสำหรับเวิร์กโฟลว์แบบเอเจนต์และโมเดลล่าสุด

การเริ่มต้นอย่างรวดเร็วนี้จะแสดงวิธีติดตั้ง
[ไลบรารี](https://ai.google.dev/gemini-api/docs/libraries?hl=th)ของเราและส่งคำขอแรก สตรีม
คำตอบ สร้างบทสนทนาหลายรอบ และใช้เครื่องมือโดยใช้วิธี
`generateContent` มาตรฐาน

## ก่อนเริ่มต้น

หากต้องการใช้ Gemini API คุณต้องมีคีย์ API เพื่อตรวจสอบสิทธิ์คำขอ บังคับใช้ขีดจำกัดด้านความปลอดภัย และติดตามการใช้งานกับบัญชีของคุณ

สร้างคีย์ API ใน AI Studio ฟรีเพื่อเริ่มต้นใช้งาน

[สร้างคีย์ Gemini API](https://aistudio.google.com/apikey?hl=th)

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

ใช้วิธี `models.generate_content` เพื่อ
[สร้างคำตอบเป็นข้อความ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th)

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## สตรีมคำตอบ

โดยค่าเริ่มต้น โมเดลจะแสดงคำตอบหลังจากกระบวนการสร้างทั้งหมดเสร็จสมบูรณ์แล้วเท่านั้น หากต้องการประสบการณ์การใช้งานที่รวดเร็วและโต้ตอบได้มากขึ้น คุณสามารถ
[สตรีมคำตอบ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#stream)เป็นส่วนๆ ขณะที่ระบบ
สร้างคำตอบ

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## การสนทนาไปมา

สำหรับบทสนทนาหลายรอบ SDK จะมีตัวช่วย `chats` ที่
เก็บสถานะไว้เพื่อ[สร้างประสบการณ์การแชทหลายรอบ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#chat)
ที่จัดการประวัติการสนทนาโดยอัตโนมัติ

### Python

```
chat = client.chats.create(model="gemini-3.5-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.5-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## ใช้เครื่องมือ

ขยายขีดความสามารถของโมเดลโดย
[เชื่อมต่อแหล่งข้อมูลคำตอบกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)
เพื่อเข้าถึงเนื้อหาเว็บแบบเรียลไทม์ โมเดลจะตัดสินใจโดยอัตโนมัติว่าจะค้นหาเมื่อใด ดำเนินการค้นหา และสังเคราะห์คำตอบ

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

นอกจากนี้ Gemini API ยังรองรับเครื่องมือในตัวอื่นๆ ด้วย ดังนี้

- **[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)**:
  ช่วยให้โมเดลเขียนและเรียกใช้โค้ด Python เพื่อแก้ปัญหาคณิตศาสตร์ที่ซับซ้อน
- **[บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th)**: ช่วยให้คุณ
  เชื่อมต่อแหล่งข้อมูลคำตอบกับ URL ของหน้าเว็บที่เฉพาะเจาะจงที่คุณระบุ
- **[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)**: ช่วยให้คุณ
  อัปโหลดไฟล์และเชื่อมต่อแหล่งข้อมูลคำตอบกับเนื้อหาของไฟล์โดยใช้การค้นหาความหมาย
- **[Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)**: ช่วยให้คุณ
  เชื่อมต่อแหล่งข้อมูลคำตอบกับข้อมูลสถานที่ และค้นหาสถานที่ เส้นทาง และ
  แผนที่
- **[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)**: ช่วยให้
  โมเดลโต้ตอบกับหน้าจอ แป้นพิมพ์ และเมาส์ของคอมพิวเตอร์เสมือนเพื่อ
  ทำงานต่างๆ

## เรียกฟังก์ชันที่กำหนดเอง

ใช้**[การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)** เพื่อเชื่อมต่อ
โมเดลกับเครื่องมือและ API ที่กำหนดเอง โมเดลจะกำหนดเวลาที่จะเรียกฟังก์ชันและแสดง `functionCall` ในคำตอบเพื่อให้แอปพลิเคชันของคุณดำเนินการ

ตัวอย่างนี้ประกาศฟังก์ชันอุณหภูมิจำลองและตรวจสอบว่าโมเดลต้องการเรียกฟังก์ชันดังกล่าวหรือไม่

### Python

```
from google import genai
from google.genai import types

weather_function = {
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

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.5-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## ขั้นตอนถัดไป

เมื่อเริ่มต้นใช้งาน Gemini API แล้ว ให้สำรวจคำแนะนำต่อไปนี้เพื่อสร้างแอปพลิเคชันขั้นสูงเพิ่มเติม

- [การสร้างข้อความ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th)
- [การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)
- [การทำความเข้าใจรูปภาพ](https://ai.google.dev/gemini-api/docs/image-understanding?hl=th)
- [การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)
- [การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
- [การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)
- [บริบทแบบยาว](https://ai.google.dev/gemini-api/docs/long-context?hl=th)
- [การฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-24 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-24 UTC"],[],[]]
