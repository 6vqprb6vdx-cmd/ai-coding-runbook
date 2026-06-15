---
source_url: https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=th
fetched_at: 2026-06-15T06:26:59.883274+00:00
title: "\u0e40\u0e2d\u0e40\u0e08\u0e19\u0e15\u0e4c Deep Research \u0e02\u0e2d\u0e07 Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# เอเจนต์ Deep Research ของ Gemini

Agent ของ Deep Research ใน Gemini จะวางแผน ดำเนินการ และสังเคราะห์
งานวิจัยแบบหลายขั้นตอนโดยอัตโนมัติ ฟีเจอร์นี้ขับเคลื่อนโดย Gemini และจะสำรวจข้อมูลที่ซับซ้อน
เพื่อสร้างรายงานแบบละเอียดพร้อมอ้างอิง ความสามารถใหม่
ช่วยให้คุณวางแผนร่วมกับเอเจนต์ เชื่อมต่อกับ
เครื่องมือภายนอกโดยใช้เซิร์ฟเวอร์ MCP รวมถึง
การแสดงข้อมูลด้วยภาพ (เช่น แผนภูมิและกราฟ) และระบุเอกสารโดยตรง
เป็นอินพุต

งานค้นคว้าข้อมูลเกี่ยวข้องกับการค้นหาและการอ่านซ้ำๆ และอาจใช้เวลาหลายนาทีจึงจะเสร็จสมบูรณ์ คุณต้องใช้การดำเนินการในเบื้องหลัง (ตั้งค่า `background=true`)
เพื่อเรียกใช้ Agent แบบอะซิงโครนัสและสำรวจผลลัพธ์หรือสตรีมการอัปเดต ดูรายละเอียดเพิ่มเติมได้ที่
[การจัดการงานที่ใช้เวลานาน](#long-running-tasks)

ตัวอย่างต่อไปนี้แสดงวิธีเริ่มงานวิจัยในเบื้องหลัง
และสำรวจผลลัพธ์

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.output_text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.output_text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## เวอร์ชันที่รองรับ

เอเจนต์ Deep Research มี 2 เวอร์ชัน ได้แก่

- **Deep Research** (`deep-research-preview-04-2026`): ออกแบบมาเพื่อความเร็วและประสิทธิภาพ เหมาะสำหรับการสตรีมกลับไปยัง UI ของไคลเอ็นต์
- **Deep Research Max** (`deep-research-max-preview-04-2026`): ความครอบคลุมสูงสุดสำหรับการรวบรวมและสังเคราะห์บริบทโดยอัตโนมัติ

## การวางแผนร่วมกัน

การวางแผนร่วมกันช่วยให้คุณควบคุมทิศทางการวิจัยได้
ก่อนที่เอเจนต์จะเริ่มทำงาน เมื่อเปิดใช้แล้ว Agent จะแสดงแผนการค้นคว้าข้อมูลที่เสนอแทนที่จะดำเนินการทันที จากนั้นคุณจะ
ตรวจสอบ แก้ไข หรืออนุมัติแผนผ่านการโต้ตอบหลายรอบได้

### ขั้นตอนที่ 1: ขอแพ็กเกจ

ตั้งค่า `collaborative_planning=True` ในการโต้ตอบแรก เอเจนต์
จะแสดงแผนการค้นคว้าข้อมูลแทนรายงานฉบับเต็ม

### Python

```
from google import genai

client = genai.Client()

plan_interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Do some research on Google TPUs.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    background=True,
)

while (result := client.interactions.get(id=plan_interaction.id)).status != "completed":
    time.sleep(5)
print(result.output_text)
```

### JavaScript

```
const planInteraction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Do some research on Google TPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    background: true
});

let result;
while ((result = await client.interactions.get(planInteraction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Do some research on Google TPUs.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "background": true
}'
```

### ขั้นตอนที่ 2: ปรับแต่งแผน (ไม่บังคับ)

ใช้ `previous_interaction_id` เพื่อสนทนาต่อและทำซ้ำ
ในแผน กด `collaborative_planning=True` ค้างไว้เพื่ออยู่ในโหมดการวางแผน

### Python

```
refined_plan = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    previous_interaction_id=plan_interaction.id,
    background=True,
)

while (result := client.interactions.get(id=refined_plan.id)).status != "completed":
    time.sleep(5)
print(result.output_text)
```

### JavaScript

```
const refinedPlan = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Focus more on the differences between Google TPUs and competitor hardware, and less on the history.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    previous_interaction_id: planInteraction.id,
    background: true
});

let result;
while ((result = await client.interactions.get(refinedPlan.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

### ขั้นตอนที่ 3: อนุมัติและดำเนินการ

ตั้งค่า `collaborative_planning=False` (หรือละเว้น) เพื่ออนุมัติแผนและ
เริ่มการค้นคว้า

### Python

```
final_report = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Plan looks good!",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": False,
    },
    previous_interaction_id=refined_plan.id,
    background=True,
)

while (result := client.interactions.get(id=final_report.id)).status != "completed":
    time.sleep(5)
print(result.output_text)
```

### JavaScript

```
const finalReport = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Plan looks good!',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: false
    },
    previous_interaction_id: refinedPlan.id,
    background: true
});

let result;
while ((result = await client.interactions.get(finalReport.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Plan looks good!",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": false
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

## การแสดงข้อมูลผ่านภาพ

เมื่อตั้งค่า `visualization` เป็น `"auto"` เอเจนต์จะสร้างแผนภูมิ กราฟ และองค์ประกอบภาพอื่นๆ เพื่อสนับสนุนผลการวิจัยได้
รูปภาพที่สร้างขึ้นจะรวมอยู่ในขั้นตอนการตอบกลับและสตรีมเป็น`image`เดลต้า โปรดขอภาพอย่างชัดเจนในคำค้นหาเพื่อให้ได้ผลลัพธ์ที่ดีที่สุด เช่น "ใส่แผนภูมิที่แสดงแนวโน้มในช่วงเวลาต่างๆ" หรือ "สร้างกราฟิกที่เปรียบเทียบส่วนแบ่งการตลาด" การตั้งค่า `visualization` เป็น
`"auto"` จะเปิดใช้ความสามารถนี้ แต่เอเจนต์จะสร้างภาพก็ต่อเมื่อ
พรอมต์ขอเท่านั้น

### Python

```
import base64

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Analyze global semiconductor market trends. Include graphics showing market share changes.",
    agent_config={
        "type": "deep-research",
        "visualization": "auto",
    },
    background=True,
)

print(f"Research started: {interaction.id}")

while (result := client.interactions.get(id=interaction.id)).status != "completed":
    time.sleep(5)

for step in result.steps:
    if step.type == "model_output":
        for content_item in step.content:
            if content_item.type == "text":
                print(content_item.text)
            elif content_item.type == "image" and content_item.data:
                image_bytes = base64.b64decode(content_item.data)
                print(f"Received image: {len(image_bytes)} bytes")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Analyze global semiconductor market trends. Include graphics showing market share changes.',
    agent_config: {
        type: 'deep-research',
        visualization: 'auto'
    },
    background: true
});

console.log(`Research started: ${interaction.id}`);

let result;
while ((result = await client.interactions.get(interaction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}

for (const step of result.steps) {
    if (step.type === 'model_output') {
        for (const contentItem of step.content) {
            if (contentItem.type === 'text') {
                console.log(contentItem.text);
            } else if (contentItem.type === 'image' && contentItem.data) {
                console.log(`[Image Output: ${contentItem.data.substring(0, 20)}...]`);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Analyze global semiconductor market trends. Include graphics showing market share changes.",
    "agent_config": {
        "type": "deep-research",
        "visualization": "auto"
    },
    "background": true
}'
```

## เครื่องมือที่รองรับ

Deep Research รองรับเครื่องมือในตัวและเครื่องมือภายนอกหลายอย่าง โดยค่าเริ่มต้น (เมื่อไม่มีการระบุพารามิเตอร์ `tools`) เอเจนต์จะมีสิทธิ์เข้าถึง Google
Search, บริบท URL และการดำเนินการโค้ด คุณสามารถ
ระบุเครื่องมืออย่างชัดเจนเพื่อจำกัดหรือขยายความสามารถของเอเจนต์ได้

| เครื่องมือ | ประเภทค่า | คำอธิบาย |
| --- | --- | --- |
| Google Search | `google_search` | ค้นหาเว็บสาธารณะ เปิดใช้โดยค่าเริ่มต้น |
| บริบท URL | `url_context` | อ่านและสรุปเนื้อหาหน้าเว็บ เปิดใช้โดยค่าเริ่มต้น |
| การเรียกใช้โค้ด | `code_execution` | เรียกใช้โค้ดเพื่อทำการคำนวณและวิเคราะห์ข้อมูล เปิดใช้โดยค่าเริ่มต้น |
| เซิร์ฟเวอร์ MCP | `mcp_server` | เชื่อมต่อกับเซิร์ฟเวอร์ MCP ระยะไกลเพื่อเข้าถึงเครื่องมือภายนอก |
| ค้นหาไฟล์ | `file_search` | ค้นหาคลังข้อมูลเอกสารที่อัปโหลด |

### Google Search

เปิดใช้ Google Search อย่างชัดเจนเป็นเครื่องมือเดียว

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'What are the latest developments in quantum computing?',
    tools: [{ type: 'google_search' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### บริบท URL

ให้ความสามารถแก่เอเจนต์ในการอ่านและสรุปหน้าเว็บที่เฉพาะเจาะจง

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Summarize the content of https://www.wikipedia.org/.',
    tools: [{ type: 'url_context' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### การรันโค้ด

อนุญาตให้ตัวแทนเรียกใช้โค้ดสำหรับการคำนวณและการวิเคราะห์ข้อมูล

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Calculate the 50th Fibonacci number.",
    "agent": "deep-research-preview-04-2026",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### เซิร์ฟเวอร์ MCP

ระบุเซิร์ฟเวอร์ `name` และ `url` ในการกำหนดค่าเครื่องมือ นอกจากนี้ คุณยังส่งข้อมูลเข้าสู่ระบบสำหรับการตรวจสอบสิทธิ์และจำกัดเครื่องมือที่เอเจนต์เรียกใช้ได้ด้วย

| ช่อง | ประเภท | ต้องระบุ | คำอธิบาย |
| --- | --- | --- | --- |
| `type` | `string` | ใช่ | ต้องเป็น `"mcp_server"` |
| `name` | `string` | ไม่ | ชื่อที่แสดงสำหรับเซิร์ฟเวอร์ MCP |
| `url` | `string` | ไม่ | URL แบบเต็มสำหรับอุปกรณ์ปลายทางของเซิร์ฟเวอร์ MCP |
| `headers` | `object` | ไม่ | คู่คีย์-ค่าที่ส่งเป็นส่วนหัว HTTP พร้อมกับคำขอทุกรายการไปยังเซิร์ฟเวอร์ (เช่น โทเค็นการตรวจสอบสิทธิ์) |
| `allowed_tools` | `array` | ไม่ | จำกัดเครื่องมือจากเซิร์ฟเวอร์ที่ตัวแทนอาจเรียกใช้ |

#### การใช้งานพื้นฐาน

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ],
    "background": true
}'
```

### ค้นหาไฟล์

ให้สิทธิ์เข้าถึงข้อมูลของคุณเองแก่ Agent โดยใช้เครื่องมือ[ค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=th)

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Compare our 2025 fiscal year report against current public web news.",
    agent="deep-research-preview-04-2026",
    background=True,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": ['fileSearchStores/my-store-name']
        }
    ]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Compare our 2025 fiscal year report against current public web news.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    tools: [
        { type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] },
    ]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## การควบคุมและการจัดรูปแบบ

คุณสามารถควบคุมเอาต์พุตของเอเจนต์ได้โดยระบุวิธีการจัดรูปแบบที่เฉพาะเจาะจง
ในพรอมต์ ซึ่งช่วยให้คุณจัดโครงสร้างรายงานเป็นส่วนและ
ส่วนย่อยที่เฉพาะเจาะจง รวมถึงตารางข้อมูล หรือปรับน้ำเสียงสำหรับกลุ่มเป้าหมายต่างๆ (เช่น
"เทคนิค" "ผู้บริหาร" "ทั่วไป")

กำหนดรูปแบบเอาต์พุตที่ต้องการอย่างชัดเจนในข้อความอินพุต

### Python

```
prompt = """
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
"""

interaction = client.interactions.create(
    input=prompt,
    agent="deep-research-preview-04-2026",
    background=True
)
```

### JavaScript

```
const prompt = `
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
`;

const interaction = await client.interactions.create({
    input: prompt,
    agent: 'deep-research-preview-04-2026',
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## อินพุตหลายรูปแบบ

Deep Research รองรับอินพุตหลายรูปแบบ ซึ่งรวมถึงรูปภาพและเอกสาร (PDF) ทำให้เอเจนต์สามารถวิเคราะห์เนื้อหาภาพและทำการค้นคว้าบนเว็บโดยอิงตามบริบทของอินพุตที่ระบุ

### Python

```
import time
from google import genai

client = genai.Client()

prompt = """Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground."""

interaction = client.interactions.create(
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"
        }
    ],
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.output_text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const prompt = `Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground.`;

const interaction = await client.interactions.create({
    input: [
        { type: 'text', text: prompt },
        {
            type: 'image',
            mime_type: "image/jpeg",
            uri: 'https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg'
        }
    ],
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.output_text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task with image input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "mime_type": "image/jpeg", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### การทำความเข้าใจเอกสาร

ส่งเอกสารเป็นอินพุตมัลติโมดัลโดยตรง เอเจนต์จะวิเคราะห์เอกสารที่ระบุและทำการวิจัยโดยอิงตามเนื้อหาของเอกสาร

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "https://arxiv.org/pdf/1706.03762",
            "mime_type": "application/pdf",
        },
    ],
    background=True,
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'https://arxiv.org/pdf/1706.03762',
            mime_type: 'application/pdf'
        }
    ],
    background: true
});
```

### REST

```
# 1. Start the research task with document input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## การจัดการงานที่ใช้เวลานาน

Deep Research เป็นกระบวนการหลายขั้นตอนที่เกี่ยวข้องกับการวางแผน การค้นหา การอ่าน
และการเขียน โดยปกติแล้ววงจรนี้จะเกินขีดจำกัดการหมดเวลามาตรฐานของ
การเรียก API แบบซิงโครนัส

ตัวแทนต้องใช้ `background=True` API จะแสดงผลออบเจ็กต์
`Interaction` บางส่วนทันที คุณใช้พร็อพเพอร์ตี้ `id` เพื่อดึงข้อมูล
การโต้ตอบสำหรับการทำโพลได้ สถานะการโต้ตอบจะเปลี่ยนจาก
`in_progress` เป็น `completed` หรือ `failed`

### สตรีมมิง

Deep Research รองรับการสตรีมเพื่อรับข้อมูลอัปเดตแบบเรียลไทม์เกี่ยวกับความคืบหน้าของการวิจัย
ซึ่งรวมถึงสรุปความคิด ข้อความเอาต์พุต และรูปภาพที่สร้างขึ้น
คุณต้องตั้งค่า `stream=True` และ `background=True` ดูคำแนะนำแบบครอบคลุมเกี่ยวกับการสตรีม รวมถึงประเภทกิจกรรม การสตรีมเครื่องมือ และการพิจารณาได้ที่[การโต้ตอบในการสตรีม](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=th)

หากต้องการรับขั้นตอนการให้เหตุผลขั้นกลาง (ความคิด) และข้อมูลอัปเดตความคืบหน้า
คุณต้องเปิดใช้**สรุปความคิด**โดยตั้งค่า `thinking_summaries` เป็น
`"auto"` ใน `agent_config` หากไม่มีข้อมูลนี้ สตรีมอาจให้เฉพาะ
ผลลัพธ์สุดท้าย

#### ประเภทเหตุการณ์สตรีม

| ประเภทของกิจกรรม | ประเภทเดลต้า | คำอธิบาย |
| --- | --- | --- |
| `step.delta` | `thought` | ขั้นตอนการให้เหตุผลระดับกลางจาก Agent |
| `step.delta` | `text` | ส่วนหนึ่งของเอาต์พุตข้อความสุดท้าย |
| `step.delta` | `image` | รูปภาพที่สร้างขึ้น (เข้ารหัส Base64) |

ตัวอย่างต่อไปนี้จะเริ่มงานวิจัยและประมวลผลสตรีมด้วย
การเชื่อมต่อใหม่โดยอัตโนมัติ โดยจะติดตาม `interaction_id` และ `last_event_id` เพื่อให้หากการเชื่อมต่อขาดหายไป (เช่น หลังจากหมดเวลา 600 วินาที) ก็จะสามารถ
ดำเนินการต่อจากจุดที่ค้างไว้ได้

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for event in stream:
        if event.event_type == "interaction.created":
            interaction_id = event.interaction.id
        if event.event_id:
            last_event_id = event.event_id
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
            elif event.delta.type == "thought":
                print(f"Thought: {event.delta.text}", flush=True)
        elif event.event_type in ("interaction.completed", "error"):
            is_complete = True

stream = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"},
)
process_stream(stream)

while not is_complete and interaction_id:
    status = client.interactions.get(interaction_id)
    if status.status != "in_progress":
        break
    stream = client.interactions.get(
        id=interaction_id, stream=True, last_event_id=last_event_id,
    )
    process_stream(stream)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interactionId;
let lastEventId;
let isComplete = false;

async function processStream(stream) {
    for await (const event of stream) {
        if (event.type === 'interaction.created') {
            interactionId = event.interaction.id;
        }
        if (event.event_id) lastEventId = event.event_id;
        if (event.type === 'step.delta') {
            if (event.delta.type === 'text') {
                process.stdout.write(event.delta.text);
            } else if (event.delta.type === 'thought') {
                console.log(`Thought: ${event.delta.text}`);
            }
        } else if (['interaction.completed', 'error'].includes(event.type)) {
            isComplete = true;
        }
    }
}

const stream = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    stream: true,
    agent_config: { type: 'deep-research', thinking_summaries: 'auto' },
});
await processStream(stream);

while (!isComplete && interactionId) {
    const status = await client.interactions.get(interactionId);
    if (status.status !== 'in_progress') break;
    const resumeStream = await client.interactions.get(interactionId, {
        stream: true, last_event_id: lastEventId,
    });
    await processStream(resumeStream);
}
```

### REST

```
# 1. Start the stream (save the INTERACTION_ID from the interaction.start event
#    and the last "event_id" you receive)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "stream": true,
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
}'

# 2. If the connection drops, reconnect with your saved IDs
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID?stream=true&last_event_id=LAST_EVENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## คำถามติดตามผลและการโต้ตอบ

คุณสนทนาต่อได้หลังจากที่ตัวแทนส่งรายงานสุดท้ายกลับมาโดยใช้`previous_interaction_id` ซึ่งช่วยให้คุณขอคำชี้แจง
สรุป หรือขยายความในส่วนที่เฉพาะเจาะจงของงานวิจัยได้โดยไม่ต้อง
เริ่มงานใหม่ทั้งหมด

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Can you elaborate on the second point in the report?",
    model="gemini-3.1-pro-preview",
    previous_interaction_id="COMPLETED_INTERACTION_ID"
)

print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Can you elaborate on the second point in the report?",
    "model": "gemini-3.1-pro-preview",
    "previous_interaction_id": "COMPLETED_INTERACTION_ID"
}'
```

## กรณีที่ควรใช้เอเจนต์ Gemini Deep Research

Deep Research เป็น**เอเจนต์** ไม่ใช่แค่โมเดล เหมาะที่สุดสำหรับภาระงาน
ที่ต้องใช้แนวทาง "นักวิเคราะห์ในกล่อง" มากกว่าแชทที่มีเวลาในการตอบสนองต่ำ

| ฟีเจอร์ | โมเดล Gemini มาตรฐาน | เอเจนต์ Deep Research ของ Gemini |
| --- | --- | --- |
| **เวลาในการตอบสนอง** | วินาที | นาที (ไม่พร้อมกัน/เบื้องหลัง) |
| **กระบวนการ** | สร้าง -> เอาต์พุต | วางแผน -> ค้นหา -> อ่าน -> ทำซ้ำ -> ผลลัพธ์ |
| **เอาต์พุต** | ข้อความสนทนา โค้ด สรุปสั้นๆ | รายงานโดยละเอียด การวิเคราะห์แบบยาว ตารางเปรียบเทียบ |
| **เหมาะสำหรับ** | แชทบ็อต การแยกข้อมูล การเขียนเชิงสร้างสรรค์ | การวิเคราะห์ตลาด การสอบทานธุรกิจ การทบทวนวรรณกรรม การวางตำแหน่งทางการแข่งขัน |

## การกำหนดค่า Agent

Deep Research ใช้พารามิเตอร์ `agent_config` เพื่อควบคุมลักษณะการทำงาน
ส่งเป็นพจนานุกรมที่มีช่องต่อไปนี้

| ช่อง | ประเภท | ค่าเริ่มต้น | คำอธิบาย |
| --- | --- | --- | --- |
| `type` | `string` | ต้องระบุ | ต้องเป็น `"deep-research"` |
| `thinking_summaries` | `string` | `"none"` | ตั้งค่าเป็น `"auto"` เพื่อรับขั้นตอนการให้เหตุผลระดับกลางระหว่างการสตรีม ตั้งค่าเป็น `"none"` เพื่อปิดใช้ |
| `visualization` | `string` | `"auto"` | ตั้งค่าเป็น `"auto"` เพื่อเปิดใช้แผนภูมิและรูปภาพที่ Agent สร้างขึ้น ตั้งค่าเป็น `"off"` เพื่อปิดใช้ |
| `collaborative_planning` | `boolean` | `false` | ตั้งค่าเป็น `true` เพื่อเปิดใช้การตรวจสอบแผนแบบหลายรอบก่อนเริ่มการวิจัย |

### Python

```
agent_config = {
    "type": "deep-research",
    "thinking_summaries": "auto",
    "visualization": "auto",
    "collaborative_planning": False,
}

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the competitive landscape of cloud GPUs.",
    agent_config=agent_config,
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Research the competitive landscape of cloud GPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        visualization: 'auto',
        collaborative_planning: false,
    },
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of cloud GPUs.",
    "agent": "deep-research-preview-04-2026",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "visualization": "auto",
        "collaborative_planning": false
    },
    "background": true
}'
```

## ความพร้อมให้บริการและการกำหนดราคา

คุณเข้าถึงเอเจนต์ Deep Research ของ Gemini ได้โดยใช้ Interactions API ใน Google AI Studio และ Gemini API

ราคาเป็นไปตาม[รูปแบบการจ่ายเมื่อใช้](https://ai.google.dev/gemini-api/docs/pricing?hl=th#pricing-for-agents)โดยอิงตามโมเดล Gemini พื้นฐานและเครื่องมือเฉพาะที่เอเจนต์ใช้ งาน Deep Research เป็นเวิร์กโฟลว์แบบ Agentic ซึ่งแตกต่างจากคำขอแชทมาตรฐานที่คำขอหนึ่งๆ จะนำไปสู่เอาต์พุต 1 รายการ คำขอเดียวจะทริกเกอร์ลูปการวางแผน การค้นหา การอ่าน และการให้เหตุผลแบบอัตโนมัติ

### ค่าใช้จ่ายโดยประมาณ

ค่าใช้จ่ายจะแตกต่างกันไปตามความลึกของการวิจัยที่จำเป็น Agent จะพิจารณาด้วยตนเองว่าต้องอ่านและค้นหามากน้อยเพียงใดจึงจะตอบพรอมต์ของคุณได้

- **Deep Research** (`deep-research-preview-04-2026`): สำหรับคำค้นหาทั่วไปที่ต้องมีการวิเคราะห์ปานกลาง เอเจนต์อาจใช้คำค้นหาประมาณ 80 รายการ โทเค็นอินพุตประมาณ 250,000 รายการ (แคชประมาณ 50-70%) และโทเค็นเอาต์พุตประมาณ 60,000 รายการ
  - **ยอดรวมโดยประมาณ:** ประมาณ$1.00 - $3.00 ต่องาน
- **Deep Research Max** (`deep-research-max-preview-04-2026`): สำหรับการวิเคราะห์ภูมิทัศน์การแข่งขันอย่างละเอียดหรือการสอบทานธุรกิจอย่างครอบคลุม เอเจนต์อาจใช้คำค้นหาได้สูงสุดประมาณ 160 รายการ, โทเค็นอินพุตประมาณ 900, 000 รายการ (แคชประมาณ 50-70%) และโทเค็นเอาต์พุตประมาณ 80,000 รายการ
  - **ยอดรวมโดยประมาณ:** ประมาณ$3.00 - $7.00 ต่องาน

## ข้อควรพิจารณาด้านความปลอดภัย

การให้สิทธิ์ตัวแทนเข้าถึงเว็บและไฟล์ส่วนตัวของคุณต้องพิจารณาความเสี่ยงด้านความปลอดภัยอย่างรอบคอบ

- **การแทรกพรอมต์โดยใช้ไฟล์:** เอเจนต์จะอ่านเนื้อหาของไฟล์ที่คุณระบุ
  ตรวจสอบว่าเอกสารที่อัปโหลด (PDF, ไฟล์ข้อความ) มาจากแหล่งที่มาที่เชื่อถือได้ ไฟล์ที่เป็นอันตรายอาจมีข้อความที่ถูกซ่อนซึ่งออกแบบมาเพื่อ
  บิดเบือนเอาต์พุตของเอเจนต์
- **ความเสี่ยงของเนื้อหาบนเว็บ:** เอเจนต์จะค้นหาเว็บสาธารณะ แม้ว่าเราจะใช้
  ตัวกรองความปลอดภัยที่มีประสิทธิภาพ แต่ก็ยังมีความเสี่ยงที่เอเจนต์อาจพบและ
  ประมวลผลหน้าเว็บที่เป็นอันตราย เราขอแนะนำให้คุณตรวจสอบ`citations`ที่ระบุ
  ในการตอบกลับเพื่อยืนยันแหล่งที่มา
- **การขโมยข้อมูล:** โปรดระมัดระวังเมื่อขอให้เอเจนต์สรุปข้อมูลภายในที่ละเอียดอ่อน
  หากคุณอนุญาตให้เอเจนต์ท่องเว็บด้วย

## แนวทางปฏิบัติแนะนำ

- **แจ้งให้ทราบถึงข้อมูลที่ไม่รู้จัก:** สั่งให้ตัวแทนทราบวิธีจัดการข้อมูลที่ขาดหายไป
  เช่น เพิ่ม *"หากไม่มีตัวเลขที่เฉพาะเจาะจงสำหรับปี 2025
  ให้ระบุอย่างชัดเจนว่าเป็นค่าประมาณหรือไม่มีข้อมูล
  แทนการประมาณ"* ลงในพรอมต์
- **ระบุบริบท:** สร้างพื้นฐานการค้นคว้าของเอเจนต์โดยให้ข้อมูลพื้นฐานหรือข้อจำกัดในพรอมต์อินพุตโดยตรง
- **ใช้การวางแผนร่วมกัน:** สำหรับคำค้นหาที่ซับซ้อน ให้เปิดใช้การวางแผนร่วมกัน เพื่อตรวจสอบและปรับแต่งแผนการค้นคว้าข้อมูลก่อนดำเนินการ
- **อินพุตหลายรูปแบบ:** Deep Research Agent รองรับอินพุตหลายรูปแบบ
  โปรดใช้อย่างระมัดระวัง เนื่องจากจะเพิ่มต้นทุนและเสี่ยงต่อการล้นหน้าต่างบริบท

## ข้อจำกัด

- **สถานะเบต้า**: Interactions API อยู่ในเวอร์ชันเบต้าแบบสาธารณะ ฟีเจอร์และ
  สคีมาอาจมีการเปลี่ยนแปลง
- **เครื่องมือที่กำหนดเอง:** ปัจจุบันคุณไม่สามารถระบุเครื่องมือเรียกใช้ฟังก์ชันที่กำหนดเองได้
  แต่ใช้เซิร์ฟเวอร์ MCP (Model Context Protocol) ระยะไกลกับเอเจนต์ Deep Research ได้
- **เอาต์พุตที่มีโครงสร้าง:** ปัจจุบัน Deep Research Agent ยังไม่รองรับเอาต์พุตที่มีโครงสร้าง
- **เวลาค้นคว้าสูงสุด:** เอเจนต์ Deep Research มีเวลาค้นคว้าสูงสุด 60 นาที
  งานส่วนใหญ่จะเสร็จสมบูรณ์ภายใน 20 นาที
- **ข้อกำหนดของร้านค้า:** การดำเนินการของเอเจนต์โดยใช้ `background=True` ต้องมี
  `store=True`
- **Google Search:** [Google
  Search](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=th) จะเปิดใช้โดย
  ค่าเริ่มต้นและ[ข้อจำกัด
  เฉพาะ](https://ai.google.dev/gemini-api/terms?hl=th#use-restrictions2)
  จะมีผลกับผลการค้นหาที่อิงตามข้อมูลพื้นฐาน

## ขั้นตอนถัดไป

- ดูข้อมูลเพิ่มเติมเกี่ยวกับ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=th)
- ดูวิธีใช้ข้อมูลของคุณเองโดยใช้เครื่องมือ[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-29 UTC"],[],[]]
