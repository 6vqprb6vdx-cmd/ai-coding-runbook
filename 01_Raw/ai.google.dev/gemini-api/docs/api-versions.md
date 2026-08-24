---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=th
fetched_at: 2026-08-24T02:28:05.220511+00:00
title: "\u0e04\u0e33\u0e2d\u0e18\u0e34\u0e1a\u0e32\u0e22\u0e40\u0e27\u0e2d\u0e23\u0e4c\u0e0a\u0e31\u0e19 API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [การอ้างอิง API](https://ai.google.dev/api?hl=th)

ส่งความคิดเห็น

# คำอธิบายเวอร์ชัน API

เอกสารนี้จะกล่าวถึงภาพรวมระดับสูงของความแตกต่างระหว่าง Gemini API เวอร์ชัน `v1`
กับ `v1beta`

- **v1**: API เวอร์ชันที่เสถียร ฟีเจอร์ในเวอร์ชันเสถียรจะได้รับการรองรับอย่างเต็มที่ตลอดอายุการใช้งานของเวอร์ชันหลัก หากมีการเปลี่ยนแปลงที่ทำให้ใช้งานไม่ได้ เราจะสร้าง API เวอร์ชันหลักใหม่และเลิกใช้งานเวอร์ชันที่มีอยู่หลังจากผ่านไประยะเวลาที่เหมาะสม
  เราอาจนำการเปลี่ยนแปลงที่ไม่ทำให้เกิดข้อขัดข้องมาใช้กับ API โดยไม่ต้องเปลี่ยน
  เวอร์ชันหลัก **Interactions API** และฟีเจอร์หลักพร้อมให้บริการโดยทั่วไปใน `v1`
- **v1beta**: เวอร์ชันนี้มีฟีเจอร์และความสามารถในช่วงแรกที่
  อยู่ระหว่างการพัฒนา แม้ว่าฟีเจอร์ใน `v1beta` อาจมีการเปลี่ยนแปลงเมื่อเราปรับปรุงตามความคิดเห็น แต่ก็ช่วยให้คุณได้ลองใช้ความสามารถใหม่ๆ ก่อนที่จะได้รับการเลื่อนขั้นเป็นเวอร์ชันเสถียร

## การรองรับความสามารถและฟีเจอร์

ตารางต่อไปนี้แสดงรายละเอียดความพร้อมใช้งานของความสามารถต่างๆ ใน `v1` (GA)
และ `v1beta` (เบต้า) ความสามารถและเครื่องมือหลักของ API ใช้ได้กับทั้ง Interactions API และ `generateContent` เว้นแต่จะระบุไว้เป็นอย่างอื่น

| ฟีเจอร์ | v1 | v1beta |
| --- | --- | --- |
| **ความสามารถหลักของ API** |  |  |
| [Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=th) |  |  |
| [การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th) |  |  |
| [เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th) |  |  |
| [การคิด / การให้เหตุผล](https://ai.google.dev/gemini-api/docs/thinking?hl=th) |  |  |
| [คำสั่งของระบบ](https://ai.google.dev/gemini-api/docs/system-instructions?hl=th) |  |  |
| [เอาต์พุตเสียง (การกำหนดค่าการพูด)](https://ai.google.dev/gemini-api/docs/audio?hl=th) |  |  |
| [ระดับบริการ (Priority / Flex)](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th) |  |  |
| **เครื่องมือ** |  |  |
| [เครื่องมือการรันโค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th) |  |  |
| [การอ้างอิงของ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th) |  |  |
| [การอ้างอิงจาก Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th) |  |  |
| [เครื่องมือบริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th) |  |  |
| [เครื่องมือค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th) |  |  |
| [เครื่องมือการใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th) |  |  |
| [เครื่องมือเซิร์ฟเวอร์ MCP](https://ai.google.dev/gemini-api/docs/eap/remote_mcp?hl=th) |  |  |
| **Realtime API** |  |  |
| [Live API (WebSockets)](https://ai.google.dev/gemini-api/docs/live-api?hl=th) |  |  |
| [Live Music API](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=th) |  |  |
| [โทเค็นชั่วคราว (Live API)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=th) |  |  |
| **API ของแพลตฟอร์ม** |  |  |
| [Models API](https://ai.google.dev/gemini-api/docs/models?hl=th) |  |  |
| [เส้นทางบริการไฟล์](https://ai.google.dev/gemini-api/docs/files?hl=th) |  |  |
| [เส้นทางของร้านค้าที่ค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th) |  |  |
| [Agents API](https://ai.google.dev/gemini-api/docs/agents?hl=th) |  |  |
| [Webhooks API](https://ai.google.dev/gemini-api/docs/webhooks?hl=th) |  |  |
| [การแคชบริบท](https://ai.google.dev/gemini-api/docs/caching?hl=th) |  |  |

- - รองรับ

## กำหนดค่าเวอร์ชัน API ใน SDK

SDK ของ Gemini API จะมีค่าเริ่มต้นเป็น `v1beta` แต่คุณสามารถระบุเวอร์ชันอย่างชัดเจน
ได้โดยการตั้งค่าเวอร์ชัน API ตามที่แสดงในตัวอย่างโค้ดต่อไปนี้

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.6-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works",
  }'
```

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-28 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-28 UTC"],[],[]]
