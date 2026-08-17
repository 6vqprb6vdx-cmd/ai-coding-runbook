---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=th
fetched_at: 2026-08-17T02:21:33.811398+00:00
title: "\u0e01\u0e32\u0e23\u0e14\u0e33\u0e40\u0e19\u0e34\u0e19\u0e01\u0e32\u0e23\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e2d\u0e22\u0e39\u0e48\u0e40\u0e1a\u0e37\u0e49\u0e2d\u0e07\u0e2b\u0e25\u0e31\u0e07 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การดำเนินการเมื่ออยู่เบื้องหลัง

สำหรับงานที่ใช้เวลานาน เช่น การค้นหาเชิงลึก การให้เหตุผลที่ซับซ้อน หรือการดำเนินการของเอเจนต์แบบหลายขั้นตอน การหมดเวลาการเชื่อมต่ออาจขัดจังหวะคำขอ HTTP มาตรฐาน (ซึ่งโดยปกติจะปิดหลังจากผ่านไป 60 วินาที) [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) มี**การดำเนินการในเบื้องหลัง** เพื่อเรียกใช้งานเหล่านี้แบบไม่พร้อมกัน

หากต้องการให้การโต้ตอบทำงานจนกว่าจะทำงานบนเซิร์ฟเวอร์เสร็จสมบูรณ์ ให้ตั้งค่า `"background": true` เมื่อสร้างการโต้ตอบ API จะแสดงรหัสการโต้ตอบทันที ซึ่งแอปพลิเคชันไคลเอ็นต์สามารถใช้เพื่อสำรวจสถานะ สตรีมความคืบหน้า หรือเชื่อมต่อกับสตรีมที่ขาดการเชื่อมต่ออีกครั้ง

การดำเนินการในเบื้องหลังรองรับโมเดล Gemini มาตรฐาน (เช่น `gemini-3.6-flash` และ `gemini-3.1-pro-preview`) และ Agent ที่ได้รับการจัดการ (เช่น `antigravity-preview-05-2026`)

## สร้างการโต้ตอบในเบื้องหลัง

หากต้องการเริ่มการโต้ตอบในเบื้องหลัง ให้ตั้งค่าพารามิเตอร์ `background` เป็น `true` เมื่อสร้างทรัพยากร

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a guide on space exploration.",
    background=True,
)
print(f"Created background interaction ID: {interaction.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Write a guide on space exploration.",
    background: true,
});
console.log(`Created background interaction ID: ${interaction.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Write a guide on space exploration.",
    "background": true
  }'
```

## วิธีการทำงานของการดำเนินการในเบื้องหลัง

เมื่อคุณสร้างการโต้ตอบในเบื้องหลัง งานจะทำงานแบบไม่พร้อมกันบนเซิร์ฟเวอร์ การโต้ตอบจะเปลี่ยนไปตามสถานะการดำเนินการต่างๆ ดังนี้

- `in_progress`: เซิร์ฟเวอร์กำลังดำเนินการโต้ตอบอย่างแข็งขัน (เช่น การเรียกใช้โค้ดหรือการค้นคว้า)
- `requires_action`: การโต้ตอบหยุดชั่วคราวและรออินพุตจากไคลเอ็นต์ (เช่น การยืนยันการดำเนินการของเครื่องมือหรือการตอบคำถาม)
- `completed`: การโต้ตอบเสร็จสมบูรณ์แล้วและเอาต์พุตพร้อมใช้งาน
- `failed`: เกิดข้อผิดพลาดระหว่างการดำเนินการ (เช่น เครื่องมือล้มเหลวหรือถึงขีดจำกัดอัตรา)
- `cancelled`: คำขอจากไคลเอ็นต์หยุดการดำเนินการ

### กรณีการใช้งาน

ใช้การดำเนินการในเบื้องหลังสำหรับกรณีต่อไปนี้

- **การดำเนินการของเอเจนต์:** งานที่ต้องมีการดำเนินการโค้ด การท่องเว็บ หรือการจัดระเบียบเอเจนต์ย่อย (เช่น `antigravity-preview-05-2026`)
- **การค้นหาเชิงลึก:** ทำงานโดยใช้ `deep-research-preview-04-2026` หรือ `deep-research-max-preview-04-2026` ซึ่งใช้เวลาหลายนาที
- **การให้เหตุผลที่ซับซ้อน:** งานที่ขั้นตอนการคิดของโมเดลเกินขีดจำกัดการเชื่อมต่อ HTTP มาตรฐาน

## ดึงข้อมูลผลลัพธ์

รับผลลัพธ์การโต้ตอบในเบื้องหลังโดยใช้**การสำรวจ** หรือ**การสตรีม**

### รูปแบบการสำรวจ (แบบไม่บล็อก)

การสำรวจจะตรวจสอบสถานะการโต้ตอบเป็นระยะโดยใช้คำขอ GET แบบไม่บล็อกจนกว่าจะถึงสถานะสิ้นสุด

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.get(id="YOUR_INTERACTION_ID")

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.get("YOUR_INTERACTION_ID");

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

if (interaction.status === "completed") {
    console.log(interaction.output_text);
} else {
    console.log(`Finished with status: ${interaction.status}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### รูปแบบการสตรีม

หากการหยุดชะงักของเครือข่ายทำให้สตรีมขาดการเชื่อมต่อ การสตรีมจะกลับมาทำงานต่อจากเหตุการณ์ที่ได้รับล่าสุด Delta แต่ละรายการจะมี `event_id` ที่ไม่ซ้ำกันในเพย์โหลด การส่งรหัสนี้เป็น `last_event_id` จะทำให้สตรีมกลับมาทำงานต่อจากเหตุการณ์นั้น

### Python

```
import time
from google import genai

client = genai.Client()
interaction_id = "YOUR_INTERACTION_ID"

def stream_with_reconnect(interaction_id: str):
    last_event_id = None
    while True:
        try:
            # Retrieve the stream. If resuming, pass last_event_id
            stream = client.interactions.get(
                id=interaction_id,
                stream=True,
                last_event_id=last_event_id
            )

            for event in stream:
                # Log event updates and capture event_id if present
                if event.event_id:
                    last_event_id = event.event_id

                if event.event_type == "step.delta" and event.delta.type == "text":
                    print(event.delta.text, end="", flush=True)

                if event.event_type == "interaction.completed":
                    return

        except Exception as e:
            print(f"\n[Connection lost: {e}. Reconnecting in 3s...]")
            time.sleep(3)

stream_with_reconnect(interaction_id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const interactionId = "YOUR_INTERACTION_ID";

async function streamWithReconnect(id) {
    let lastEventId = undefined;
    while (true) {
        try {
            // Retrieve the stream. If resuming, pass last_event_id in options
            const stream = await client.interactions.get(id, {
                stream: true,
                last_event_id: lastEventId
            });

            for await (const event of stream) {
                // Capture event_id if present
                const idVal = event.event_id || event.id;
                if (idVal) {
                    lastEventId = idVal;
                }

                if (event.event_type === "step.delta" && event.delta?.type === "text") {
                    process.stdout.write(event.delta.text);
                }

                if (event.event_type === "interaction.completed") {
                    return;
                }
            }
        } catch (error) {
            console.log(`\n[Connection lost: ${error.message}. Reconnecting in 3s...]`);
            await new Promise(resolve => setTimeout(resolve, 3000));
        }
    }
}

await streamWithReconnect(interactionId);
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## การสนทนาไปมา

การโต้ตอบในภายหลังสามารถเชื่อมโยงกับการสนทนาในเบื้องหลังได้โดยใช้ `previous_interaction_id` โดยขึ้นอยู่กับข้อจำกัดต่อไปนี้

1. **การดำเนินการที่ใช้งานอยู่จะถูกบล็อก:** การเชื่อมโยงการโต้ตอบในภายหลังกับการโต้ตอบที่มีสถานะ `in_progress` จะแสดงข้อผิดพลาด `400 Bad Request` รอให้การโต้ตอบไปถึงสถานะ `completed` ก่อนที่จะเริ่มการโต้ตอบถัดไป
2. **พารามิเตอร์สภาพแวดล้อมสำหรับ Agent ที่ได้รับการจัดการ:** เมื่อเชื่อมโยงการโต้ตอบสำหรับ Agent ที่ได้รับการจัดการ (เช่น `antigravity-preview-05-2026`) คำขอต้องมีทั้ง `previous_interaction_id` และ `environment`

ตัวอย่างต่อไปนี้แสดงวิธีเชื่อมโยงการโต้ตอบ

### Python

```
import time
from google import genai

client = genai.Client()
agent_model = "antigravity-preview-05-2026"

# First interaction: Provision sandbox environment and execute first instruction
interaction1 = client.interactions.create(
    model=agent_model,
    input="Create a folder named project/ and write hello.py inside.",
    environment="remote",
    background=True
)

# Wait for completion
while True:
    check = client.interactions.get(id=interaction1.id)
    if check.status != "in_progress":
        break
    time.sleep(2)

# Second interaction: Chain using previous_interaction_id and environment
interaction2 = client.interactions.create(
    model=agent_model,
    input="List all files in the project/ directory.",
    previous_interaction_id=interaction1.id,
    environment="remote",
    background=True
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const agentModel = "antigravity-preview-05-2026";

// First interaction: Provision sandbox environment and execute first instruction
const interaction1 = await client.interactions.create({
    model: agentModel,
    input: "Create a folder named project/ and write hello.py inside.",
    environment: "remote",
    background: true
});

// Wait for completion
while (true) {
    const check = await client.interactions.get(interaction1.id);
    if (check.status !== "in_progress") {
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// Second interaction: Chain using previous_interaction_id and environment
const interaction2 = await client.interactions.create({
    model: agentModel,
    input: "List all files in the project/ directory.",
    previous_interaction_id: interaction1.id,
    environment: "remote",
    background: true
});
```

### REST

```
# Chain second interaction (Make sure FIRST_INTERACTION_ID has status 'completed')
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "antigravity-preview-05-2026",
    "input": "List all files in the project/ directory.",
    "previous_interaction_id": "FIRST_INTERACTION_ID",
    "environment": "remote",
    "background": true
  }'
```

## การยกเลิกและการลบ

ควบคุมการดำเนินการที่กำลังทำงานและจัดการพื้นที่เก็บข้อมูลโดยใช้คำขอยกเลิกและลบ

- **ยกเลิก (`POST /interactions/{id}/cancel`):** หยุดงานที่กำลังทำงาน สถานะจะเปลี่ยนเป็น `cancelled` การดำเนินการล้างข้อมูลบนเซิร์ฟเวอร์อาจทำให้เกิดความล่าช้าเล็กน้อยก่อนที่สถานะจะอัปเดตในคำขอ GET
- **ลบ (`DELETE /interactions/{id}`):** นำบันทึกการโต้ตอบออกจากเซิร์ฟเวอร์ คำขอ GET ในภายหลังจะแสดงข้อผิดพลาด `404 Not Found`

### Python

```
from google import genai

client = genai.Client()

# Cancel a running interaction
client.interactions.cancel(id="YOUR_INTERACTION_ID")

# Delete the interaction record entirely
client.interactions.delete(id="YOUR_INTERACTION_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Cancel a running interaction
await client.interactions.cancel("YOUR_INTERACTION_ID");

// Delete the interaction record entirely
await client.interactions.delete("YOUR_INTERACTION_ID");
```

### REST

```
# Cancel the interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID/cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"

# Delete the interaction
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## ขั้นตอนถัดไป

- อ่าน[ภาพรวมของ Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) เพื่อทำความเข้าใจการจัดการเซสชันและสถานะ
- ดูรายละเอียดเกี่ยวกับการอัปเดตเหตุการณ์แบบเรียลไทม์ได้ที่คู่มือการโต้ตอบแบบสตรีม [Streaming interactions](https://ai.google.dev/gemini-api/docs/streaming?hl=th)
- สำรวจ[การเริ่มต้นใช้งานฉบับย่อของเอเจนต์ที่มีการจัดการ](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th)เพื่อสร้างเอเจนต์แบบหลายรอบที่มีสถานะ

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
