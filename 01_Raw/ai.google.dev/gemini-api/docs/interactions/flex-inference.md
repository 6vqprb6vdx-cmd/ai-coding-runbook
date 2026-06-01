---
source_url: https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=th
fetched_at: 2026-06-01T19:41:15.504817+00:00
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

# การอนุมานแบบยืดหยุ่น

Gemini Flex API เป็นระดับการอนุมานที่ช่วยลดต้นทุนได้ 50% เมื่อเทียบกับอัตรามาตรฐาน โดยแลกกับการตอบสนองที่ผันแปรและความพร้อมใช้งาน
ตามความพยายามอย่างเต็มที่ ออกแบบมาสำหรับภาระงานที่ยอมรับเวลาในการตอบสนองได้ซึ่งต้องมีการประมวลผลแบบ
ซิงโครนัส แต่ไม่จำเป็นต้องใช้ประสิทธิภาพแบบเรียลไทม์ของ
API มาตรฐาน

## วิธีใช้ Flex

หากต้องการใช้ระดับ Flex ให้ระบุ `service_tier` เป็น `flex` ในคำขอ โดยค่าเริ่มต้น คำขอจะใช้ระดับมาตรฐานหากละเว้นช่องนี้

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Analyze this dataset for trends...",
        service_tier='flex'
    )
    print(interaction.output_text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: 'gemini-3.5-flash',
            input: 'Analyze this dataset for trends...',
            service_tier: 'flex'
        });
        console.log(interaction.output_text);
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## วิธีการทำงานของการอนุมาน Flex

การอนุมาน Gemini Flex ช่วยลดช่องว่างระหว่าง API มาตรฐานกับเวลาในการตอบกลับ 24 ชั่วโมงของ [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th) โดยจะใช้ความสามารถในการประมวลผลในช่วงนอกเวลาทําการที่ "ลดได้" เพื่อมอบโซลูชันที่คุ้มค่าสําหรับงานเบื้องหลังและเวิร์กโฟลว์แบบลําดับ

| ฟีเจอร์ | พับ | ลำดับความสำคัญ | มาตรฐาน | กลุ่ม |
| --- | --- | --- | --- | --- |
| **การกำหนดราคา** | ส่วนลด 50% | มากกว่ารุ่น Standard 75-100% | ตั๋วราคาเต็ม | ส่วนลด 50% |
| **เวลาในการตอบสนอง** | นาที (เป้าหมาย 1-15 นาที) | ต่ำ (วินาที) | วินาทีถึงนาที | สูงสุด 24 ชั่วโมง |
| **ความน่าเชื่อถือ** | ดีที่สุดเท่าที่ทำได้ (ลดภาระได้) | สูง (ไม่หลุดร่วง) | สูง / สูงปานกลาง | สูง (สำหรับปริมาณงาน) |
| **อินเทอร์เฟซ** | ซิงโครนัส | ซิงโครนัส | ซิงโครนัส | แบบอะซิงโครนัส |

### ประโยชน์สำคัญ

- **ประสิทธิภาพด้านต้นทุน**: ประหยัดค่าใช้จ่ายได้อย่างมากสำหรับการประเมินที่ไม่ใช่การผลิต, เอเจนต์พื้นหลัง และการเพิ่มคุณค่าของข้อมูล
- **ใช้งานง่าย**: เพียงเพิ่มพารามิเตอร์เดียวลงในคำขอที่มีอยู่
- **เวิร์กโฟลว์แบบซิงโครนัส**: เหมาะสำหรับเชน API แบบลำดับที่คำขอถัดไปขึ้นอยู่กับเอาต์พุตของคำขอก่อนหน้า ซึ่งทำให้มีความยืดหยุ่นมากกว่า Batch สำหรับเวิร์กโฟลว์ของเอเจนต์

### กรณีการใช้งาน

- **การประเมินแบบออฟไลน์**: การเรียกใช้การทดสอบการถดถอยหรือลีดเดอร์บอร์ด "LLM ในฐานะผู้พิพากษา"
- **ตัวแทนเบื้องหลัง**: งานตามลำดับ เช่น การอัปเดต CRM การสร้างโปรไฟล์ หรือการกลั่นกรองเนื้อหาที่ยอมรับความล่าช้าได้
- **การวิจัยที่ถูกจำกัดด้วยงบประมาณ**: การทดลองทางวิชาการที่ต้องใช้โทเค็นจำนวนมากโดยมีงบประมาณจำกัด

### ขีดจำกัดอัตรา

การเข้าชมการอนุมานแบบยืดหยุ่นจะนับรวมใน[ขีดจำกัดอัตรา](https://aistudio.google.com/rate-limit?hl=th)ทั่วไปของคุณ โดยจะไม่มีขีดจำกัดอัตราเพิ่มเติมเหมือนกับ [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)

### ความจุที่ลดลงได้

ระบบจะถือว่าการเข้าชมแบบยืดหยุ่นมีความสำคัญต่ำกว่า หากมีการเข้าชมมาตรฐานเพิ่มขึ้นอย่างรวดเร็ว ระบบอาจขัดจังหวะหรือนำคำขอ Flex ออกเพื่อให้มั่นใจว่ามีพื้นที่ว่างสำหรับผู้ใช้ที่มีลำดับความสำคัญสูง หากกำลังมองหาการอนุมานที่มีลำดับความสำคัญสูง ให้ดู[การอนุมานที่มีลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=th)

### รหัสข้อผิดพลาด

เมื่อความจุแบบยืดหยุ่นไม่พร้อมใช้งานหรือระบบมีปริมาณการใช้งานสูง API จะ
แสดงรหัสข้อผิดพลาดมาตรฐาน

- **503 ไม่พร้อมให้บริการ**: ขณะนี้ระบบมีผู้ใช้เต็มแล้ว
- **429 มีคำขอมากเกินไป**: ขีดจำกัดอัตราหรือทรัพยากรหมด

### ความรับผิดชอบของลูกค้า

- **ไม่มีการสำรองข้อมูลฝั่งเซิร์ฟเวอร์**: เพื่อป้องกันการเรียกเก็บเงินที่ไม่คาดคิด ระบบจะไม่
  อัปเกรดคำขอ Flex เป็นระดับมาตรฐานโดยอัตโนมัติหากความจุของ Flex เต็ม
- **การลองใหม่**: คุณต้องใช้ตรรกะการลองใหม่ฝั่งไคลเอ็นต์ของคุณเองด้วย
  Exponential Backoff
- **การหมดเวลา**: เนื่องจากคำขอ Flex อาจอยู่ในคิว เราจึงแนะนำให้
  เพิ่มการหมดเวลาฝั่งไคลเอ็นต์เป็น 10 นาทีขึ้นไปเพื่อหลีกเลี่ยงการปิด
  การเชื่อมต่อก่อนเวลา

## ปรับกรอบเวลาหมดเวลา

คุณสามารถกำหนดค่าการหมดเวลาต่อคำขอสำหรับ REST API และไลบรารีของไคลเอ็นต์ได้
ตรวจสอบเสมอว่าการหมดเวลาฝั่งไคลเอ็นต์ครอบคลุมช่วงเวลาที่เซิร์ฟเวอร์ตั้งใจรอ (เช่น 600 วินาทีขึ้นไปสำหรับคิวรอแบบยืดหยุ่น) SDK คาดหวังค่าการหมดเวลาเป็นมิลลิวินาที

### การหมดเวลาต่อคำขอ

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="why is the sky blue?",
        service_tier="flex",
    )
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: "gemini-3.5-flash",
            input: "why is the sky blue?",
            service_tier: "flex",
        }, {timeout: 900000});
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}

await main();
```

## ใช้การลองใหม่

เนื่องจาก Flex สามารถลดขนาดได้และจะล้มเหลวพร้อมข้อผิดพลาด 503 ต่อไปนี้คือตัวอย่างการใช้ตรรกะการลองใหม่โดยไม่บังคับเพื่อดำเนินการต่อกับคำขอที่ไม่สำเร็จ

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.5-flash",
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
                    model="gemini-3.5-flash",
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
        model: "gemini-3.5-flash",
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
          model: "gemini-3.5-flash",
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

## ราคา

การอนุมานแบบยืดหยุ่นมีราคาอยู่ที่ 50% ของ [API มาตรฐาน](https://ai.google.dev/gemini-api/docs/pricing?hl=th)
และเรียกเก็บเงินต่อโทเค็น

## โมเดลที่รองรับ

รุ่นต่อไปนี้รองรับการอนุมานแบบยืดหยุ่น

| รุ่น | การอนุมานแบบยืดหยุ่น |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=th) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) | ✔️ |
| [ตัวอย่าง Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th) | ✔️ |
| [ตัวอย่าง Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=th) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=th) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=th) | ✔️ |

## ขั้นตอนถัดไป

- [การอนุมานลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=th)สำหรับเวลาในการตอบสนองต่ำมาก
- [โทเค็น](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=th): ทำความเข้าใจโทเค็น

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-28 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-28 UTC"],[],[]]
