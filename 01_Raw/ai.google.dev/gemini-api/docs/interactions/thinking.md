---
source_url: https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=th
fetched_at: 2026-06-01T19:44:45.620419+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การคิดของ Gemini

โมเดลในซีรีส์ [Gemini 3 และ 2.5](https://ai.google.dev/gemini-api/docs/models?hl=th) ใช้
"กระบวนการคิด" ซึ่งช่วยปรับปรุงความสามารถในการใช้เหตุผลและการวางแผนหลายขั้นตอนได้อย่างมาก
ทำให้โมเดลมีประสิทธิภาพสูงสำหรับงานที่ซับซ้อน เช่น
การเขียนโค้ด คณิตศาสตร์ขั้นสูง และการวิเคราะห์ข้อมูล

เมื่อคุณใช้โมเดลการคิด Gemini จะใช้เหตุผลภายในก่อนที่จะตอบ Interactions API จะแสดงเหตุผลนี้ผ่านขั้นตอน `thought` ซึ่งเป็นขั้นตอนเฉพาะที่ปรากฏตามลำดับเวลาควบคู่ไปกับการเรียกใช้ฟังก์ชัน อินพุตของผู้ใช้ หรือเอาต์พุตของโมเดลในอาร์เรย์ `steps`

ขั้นตอนการคิดแต่ละขั้นตอนจะมี 2 ช่อง ดังนี้

| ช่อง | ต้องระบุ | คำอธิบาย |
| --- | --- | --- |
| `signature` | ✅ ใช่ | การแสดงการเข้ารหัสของสถานะการใช้เหตุผลภายในของโมเดล จะปรากฏอยู่เสมอ แม้ว่าโมเดลจะใช้เหตุผลเพียงเล็กน้อยก็ตาม |
| `summary` | ❌ ไม่ | อาร์เรย์ของเนื้อหา (ข้อความและ/หรือรูปภาพ) ที่สรุปการใช้เหตุผล อาจว่างเปล่า ทั้งนี้ขึ้นอยู่กับการกำหนดค่า [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=th) โมเดลใช้การให้เหตุผลเพียงพอหรือไม่ หรือประเภทเนื้อหา (เช่น รูปภาพที่ซ่อนอยู่อาจไม่มีข้อมูลสรุปที่เป็นข้อความ) |

## การโต้ตอบกับการคิด

การเริ่มการโต้ตอบกับโมเดลการคิดจะคล้ายกับคำขอการโต้ตอบอื่นๆ ระบุหนึ่งใน [โมเดลที่รองรับการคิด](#thinking-levels) ในช่อง `model` ดังนี้

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## ข้อมูลสรุปการคิด

ข้อมูลสรุปการคิดจะให้ข้อมูลเชิงลึกเกี่ยวกับกระบวนการให้เหตุผลภายในของโมเดล
โดยค่าเริ่มต้น ระบบจะแสดงเฉพาะเอาต์พุตสุดท้าย คุณสามารถเปิดใช้ข้อมูลสรุปการคิดด้วย `thinking_summaries` ได้ดังนี้

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

บล็อกการคิดอาจมี**เฉพาะลายเซ็นที่ไม่มีข้อมูลสรุป** ในกรณีต่อไปนี้

- คำขออย่างง่ายที่โมเดลใช้เหตุผลไม่เพียงพอที่จะสร้างข้อมูลสรุป
- `thinking_summaries: "none"` ซึ่งปิดใช้ข้อมูลสรุปอย่างชัดแจ้ง
- เนื้อหาการคิดบางประเภท เช่น รูปภาพ อาจไม่มีข้อมูลสรุปที่เป็นข้อความ

โค้ดของคุณควรจัดการบล็อกการคิดที่ `summary` ว่างเปล่าหรือไม่มีอยู่เสมอ

## การสตรีมพร้อมการคิด

ใช้การสตรีมเพื่อรับข้อมูลสรุปการคิดแบบเพิ่มทีละน้อยระหว่างการสร้าง
ระบบจะแสดงบล็อกการคิดโดยใช้ Server-Sent Events (SSE) ที่มีเดลต้า 2 ประเภทที่แตกต่างกัน ดังนี้

| ประเภทเดลต้า | มี | เวลาที่ส่ง |
| --- | --- | --- |
| `thought_summary` | เนื้อหาข้อมูลสรุปที่เป็นข้อความหรือรูปภาพ | เดลต้าอย่างน้อย 1 รายการที่มีข้อมูลสรุปแบบเพิ่มทีละน้อย |
| `thought_signature` | ลายเซ็นการเข้ารหัส | เดลต้าสุดท้ายก่อน `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

การตอบสนองแบบสตรีมมิงใช้ Server-Sent Events (SSE) และประกอบด้วยขั้นตอนและเหตุการณ์ เช่น

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## การควบคุมการคิด

โมเดล Gemini จะคิดแบบไดนามิกโดยค่าเริ่มต้น ซึ่งจะปรับความพยายามในการใช้เหตุผลโดยอัตโนมัติตามความซับซ้อนของคำขอ คุณสามารถควบคุมลักษณะการทำงานนี้ได้โดยใช้พารามิเตอร์ `thinking_level`

| โมเดล | การคิดเริ่มต้น | ระดับที่รองรับ |
| --- | --- | --- |
| gemini-3.1-pro-preview | เปิด (สูง) | ต่ำ ปานกลาง สูง |
| gemini-3-flash-preview | เปิด (สูง) | ต่ำมาก ต่ำ ปานกลาง สูง |
| gemini-3-pro-preview | เปิด (สูง) | ต่ำ สูง |
| gemini-2.5-pro | เปิด | ต่ำ ปานกลาง สูง |
| gemini-2.5-flash | เปิด | ต่ำ ปานกลาง สูง |
| gemini-2.5-flash-lite | ปิด | ต่ำ ปานกลาง สูง |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## ลายเซ็นการคิด

ลายเซ็นการคิดเป็นการแสดงการเข้ารหัสของการใช้เหตุผลภายในของโมเดล คุณต้องใช้ลายเซ็นเหล่านี้เพื่อรักษาความต่อเนื่องของการใช้เหตุผลในการโต้ตอบหลายรอบ

Interactions API ช่วยให้การจัดการลายเซ็นการคิดง่ายกว่า `generateContent` API มาก

### โหมด Stateful (แนะนำ)

โดยค่าเริ่มต้น เมื่อคุณใช้ Interactions API ในโหมด Stateful (โดยตั้งค่า `store: true` และส่ง `previous_interaction_id` ในรอบถัดไป) เซิร์ฟเวอร์จะจัดการสถานะการสนทนาโดยอัตโนมัติ ซึ่งรวมถึงบล็อกการคิดและลายเซ็นทั้งหมด ในโหมดนี้ คุณไม่จำเป็นต้องดำเนินการใดๆ เกี่ยวกับลายเซ็น เนื่องจากระบบจะจัดการลายเซ็นทั้งหมดในฝั่งเซิร์ฟเวอร์

### โหมด Stateless

หากคุณจัดการสถานะการสนทนาด้วยตนเอง (โหมด Stateless) และส่งประวัติอินพุตและเอาต์พุตทั้งหมดในแต่ละคำขอ คุณต้องดำเนินการดังนี้

- คุณ**ต้อง** ส่งบล็อก `thought` ทั้งหมดอีกครั้งตามที่ได้รับจากโมเดลทุกประการ
- คุณ**ไม่ควร** นำบล็อกการคิดออกจากประวัติหรือแก้ไขบล็อกการคิด เนื่องจากบล็อกการคิดมีลายเซ็นที่โมเดลต้องใช้เพื่อใช้เหตุผลต่อไป
- เมื่อเปลี่ยนโมเดลภายในเซสชัน คุณควรส่งบล็อกการคิดของโมเดลก่อนหน้าอีกครั้ง แบ็กเอนด์จะจัดการความเข้ากันได้

## ราคา

เมื่อเปิดการคิด ราคาการตอบสนองจะเป็นผลรวมของโทเค็นเอาต์พุตและโทเค็นการคิด คุณสามารถดูจำนวนโทเค็นการคิดทั้งหมดที่สร้างขึ้นได้จากช่อง `total_thought_tokens`

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

โมเดลการคิดจะสร้างการคิดแบบเต็มเพื่อปรับปรุงคุณภาพของการตอบสนองสุดท้าย
แล้วแสดงข้อมูลสรุปเพื่อแสดงข้อมูลเชิงลึกเกี่ยวกับกระบวนการคิด
ราคาจะอิงตามโทเค็นการคิดแบบเต็มที่โมเดลต้องสร้าง แม้ว่า API จะแสดงเฉพาะข้อมูลสรุปก็ตาม

ดูข้อมูลเพิ่มเติมเกี่ยวกับโทเค็นได้ในคู่มือ[การนับโทเค็น](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=th)

## แนวทางปฏิบัติแนะนำ

ใช้โมเดลการคิดอย่างมีประสิทธิภาพโดยทำตามหลักเกณฑ์ต่อไปนี้

- **ตรวจสอบการใช้เหตุผล**: วิเคราะห์ข้อมูลสรุปการคิดเพื่อทำความเข้าใจข้อผิดพลาดและปรับปรุงพรอมต์
- **ควบคุมงบประมาณการคิด**: แจ้งให้โมเดลคิดน้อยลงสำหรับเอาต์พุตที่ยาวเพื่อประหยัดโทเค็น
- **งานง่ายๆ**: ใช้การคิดน้อยที่สุดสำหรับการดึงข้อมูลข้อเท็จจริงหรือการจัดประเภท (เช่น "DeepMind ก่อตั้งขึ้นที่ไหน")
- **งานปานกลาง**: ใช้การคิดเริ่มต้นเพื่อเปรียบเทียบแนวคิดหรือการใช้เหตุผลเชิงสร้างสรรค์ (เช่น เปรียบเทียบรถยนต์ไฟฟ้าและรถยนต์ไฮบริด)
- **งานที่ซับซ้อน**: ใช้การคิดสูงสุดสำหรับการเขียนโค้ด คณิตศาสตร์ หรือการวางแผนหลายขั้นตอนขั้นสูง (เช่น แก้ปัญหาคณิตศาสตร์ AIME)

## ขั้นตอนถัดไป

- [การสร้างข้อความ](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=th): การตอบสนองที่เป็นข้อความพื้นฐาน
- [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=th): เชื่อมต่อกับเครื่องมือ
- [คู่มือ Gemini 3](https://ai.google.dev/gemini-api/docs/interactions/gemini-3?hl=th): ฟีเจอร์เฉพาะของโมเดล

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-01 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-01 UTC"],[],[]]
