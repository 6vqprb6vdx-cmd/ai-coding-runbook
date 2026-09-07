---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=th
fetched_at: 2026-09-07T05:33:54.728605+00:00
title: "\u0e01\u0e32\u0e23\u0e2d\u0e19\u0e38\u0e21\u0e32\u0e19\u0e41\u0e1a\u0e1a\u0e22\u0e37\u0e14\u0e2b\u0e22\u0e38\u0e48\u0e19 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การอนุมานแบบยืดหยุ่น

Gemini Flex API เป็นระดับการอนุมานที่ช่วยลดต้นทุนได้ 50% เมื่อเทียบกับอัตรามาตรฐาน แลกกับการตอบสนองที่ผันแปรและความพร้อมให้บริการอย่างเต็มที่ โดยได้รับการออกแบบมาสำหรับภาระงานที่ยอมรับการตอบสนองที่ล่าช้าได้ ซึ่งต้องมีการประมวลผลแบบซิงโครนัส แต่ไม่จำเป็นต้องมีประสิทธิภาพแบบเรียลไทม์ของ API มาตรฐาน

## วิธีใช้ Flex

หากต้องการใช้ระดับ Flex ให้ระบุ `service_tier` เป็น `flex` ในคำขอ โดยค่าเริ่มต้น คำขอจะใช้ระดับมาตรฐานหากละเว้นช่องนี้

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.6-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## วิธีการอนุมานของ Flex

การอนุมานของ Gemini Flex ช่วยลดช่องว่างระหว่าง API มาตรฐานกับ API แบบกลุ่มที่ใช้เวลาดำเนินการ 24 ชั่วโมง
ของ [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th) โดยใช้ความสามารถในการประมวลผล "ที่ลดได้" ในช่วงเวลาที่ไม่ใช่ช่วงเวลาที่มีการใช้งานสูงสุด เพื่อมอบโซลูชันที่คุ้มค่าสำหรับงานเบื้องหลังและเวิร์กโฟลว์แบบลำดับ

| ฟีเจอร์ | Flex | รายการสำคัญ | มาตรฐาน | กลุ่ม |
| --- | --- | --- | --- | --- |
| **การกำหนดราคา** | ส่วนลด 50% | มากกว่ามาตรฐาน 75-100% | ราคาเต็ม | ส่วนลด 50% |
| **การตอบสนอง** | นาที (เป้าหมาย 1-15 นาที) | ต่ำ (วินาที) | วินาทีถึงนาที | สูงสุด 24 ชั่วโมง |
| **ความเชื่อถือได้** | อย่างเต็มที่ (ลดได้) | สูง (ลดไม่ได้) | สูง / สูงปานกลาง | สูง (สำหรับปริมาณงาน) |
| **อินเทอร์เฟซ** | แบบซิงโครนัส | แบบซิงโครนัส | แบบซิงโครนัส | แบบอะซิงโครนัส |

### สิทธิประโยชน์สำคัญ

- **ความคุ้มค่า**: ประหยัดค่าใช้จ่ายได้อย่างมากสำหรับการประเมินที่ไม่ใช่การใช้งานจริง, เอเจนต์เบื้องหลัง และการเพิ่มคุณค่าของข้อมูล
- **ความยุ่งยากต่ำ**: เพียงเพิ่มพารามิเตอร์เดียวลงในคำขอที่มีอยู่
- **เวิร์กโฟลว์แบบซิงโครนัส**: เหมาะอย่างยิ่งสำหรับเชน API แบบลำดับที่คำขอถัดไปขึ้นอยู่กับเอาต์พุตของคำขอก่อนหน้า ซึ่งทำให้มีความยืดหยุ่นมากกว่า API แบบกลุ่มสำหรับเวิร์กโฟลว์แบบเอเจนต์

### กรณีการใช้งาน

- **การประเมินแบบออฟไลน์**: การเรียกใช้การทดสอบการถดถอยหรือลีดเดอร์บอร์ด "LLM-as-a-judge"
- **เอเจนต์เบื้องหลัง**: งานแบบลำดับ เช่น การอัปเดต CRM, การสร้างโปรไฟล์ หรือการกลั่นกรองเนื้อหาที่ยอมรับความล่าช้าได้เป็นนาที
- **การวิจัยที่มีงบประมาณจำกัด**: การทดลองทางวิชาการที่ต้องใช้โทเค็นจำนวนมากโดยมีงบประมาณจำกัด

### ขีดจำกัดอัตรา

การเข้าชมการอนุมานของ Flex จะนับรวมใน[ขีดจำกัดอัตรา](https://aistudio.google.com/rate-limit?hl=th)ทั่วไป โดยไม่มี
ขีดจำกัดอัตราที่ขยายออกไปเหมือนกับ[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)

### ความสามารถที่ลดได้

ระบบจะถือว่าการเข้าชมของ Flex มีลำดับความสำคัญต่ำกว่า หากมีการเข้าชมมาตรฐานเพิ่มขึ้นอย่างรวดเร็ว ระบบอาจขัดจังหวะหรือนำคำขอของ Flex ออกเพื่อให้มีความสามารถสำหรับผู้ใช้ที่มีลำดับความสำคัญสูง หากต้องการการอนุมานที่มีลำดับความสำคัญสูง ให้ดู
[การอนุมานที่มีลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)

### รหัสข้อผิดพลาด

เมื่อความสามารถของ Flex ไม่พร้อมใช้งานหรือระบบมีการใช้งานหนาแน่น API จะแสดงรหัสข้อผิดพลาดมาตรฐานดังนี้

- **503 ไม่พร้อมให้บริการ**: ขณะนี้ระบบมีผู้ใช้เต็มแล้ว
- **429 มีคำขอมากเกินไป**: ขีดจำกัดอัตราหรือทรัพยากรหมด

### ความรับผิดชอบของไคลเอ็นต์

- **ไม่มีการย้อนกลับฝั่งเซิร์ฟเวอร์**: เพื่อป้องกันค่าใช้จ่ายที่ไม่คาดคิด ระบบจะไม่
  ยกระดับคำขอของ Flex เป็นระดับมาตรฐานโดยอัตโนมัติหากความสามารถของ Flex
  เต็ม
- **การลองอีกครั้ง**: คุณต้องใช้ตรรกะการลองอีกครั้งฝั่งไคลเอ็นต์ของคุณเองด้วย
  Exponential Backoff
- **ระยะหมดเวลา**: เนื่องจากคำขอของ Flex อาจอยู่ในคิว เราจึงแนะนำให้
  เพิ่มระยะหมดเวลาฝั่งไคลเอ็นต์เป็น 10 นาทีขึ้นไปเพื่อหลีกเลี่ยงการ
  ปิดการเชื่อมต่อก่อนเวลา

## ปรับกรอบเวลาหมดเวลา

คุณสามารถกำหนดค่าระยะหมดเวลาต่อคำขอสำหรับ REST API และไลบรารีของไคลเอ็นต์ได้
ตรวจสอบเสมอว่าระยะหมดเวลาฝั่งไคลเอ็นต์ครอบคลุมกรอบเวลาที่เซิร์ฟเวอร์รอได้ตามที่ต้องการ (เช่น 600 วินาทีขึ้นไปสำหรับคิวรอของ Flex) SDK คาดหวังค่าหมดเวลาเป็นมิลลิวินาที

### ระยะหมดเวลาต่อคำขอ

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.6-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

## ใช้การลองอีกครั้ง

เนื่องจาก Flex ลดได้และล้มเหลวด้วยข้อผิดพลาด 503 ต่อไปนี้คือตัวอย่างการใช้ตรรกะการลองอีกครั้ง (ไม่บังคับ) เพื่อดำเนินการต่อกับคำขอที่ล้มเหลว

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.6-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.6-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.6-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## การกำหนดราคา

การอนุมานของ Flex มีราคาอยู่ที่ 50% ของ [API มาตรฐาน](https://ai.google.dev/gemini-api/docs/pricing?hl=th)
และเรียกเก็บเงินต่อโทเค็น

## โมเดลที่รองรับ

โมเดลต่อไปนี้รองรับการอนุมานของ Flex

| โมเดล | การอนุมานของ Flex |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=th) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=th) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=th) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) | ✔️ |
| [Gemini 3.1 Pro เวอร์ชันทดลอง](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th) | ✔️ |
| [Gemini 3 Flash เวอร์ชันทดลอง](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=th) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=th) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=th) | ✔️ |

## ขั้นตอนถัดไป

- [การอนุมานที่มีลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)สำหรับเวลาในการตอบสนองต่ำมาก
- [โทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th): ทำความเข้าใจโทเค็น

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
