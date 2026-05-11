---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=th
fetched_at: 2026-05-11T12:38:11.367325+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)

# เร่งการค้นพบด้วย Gemini for Research

[รับคีย์ Gemini API](https://aistudio.google.com/apikey?hl=th)

คุณสามารถใช้โมเดล Gemini เพื่อพัฒนาการวิจัยพื้นฐานในหลากหลายสาขาวิชา
โดยมีวิธีต่างๆ ที่คุณสามารถสำรวจ Gemini สำหรับการวิจัยดังนี้

- **วิเคราะห์และควบคุมเอาต์พุตของโมเดล**: คุณสามารถตรวจสอบ
  ผลลัพธ์ที่โมเดลสร้างขึ้นโดยใช้เครื่องมือต่างๆ เช่น
  `CitationMetadata` เพื่อทำการวิเคราะห์เพิ่มเติม นอกจากนี้ คุณยังกำหนดค่าตัวเลือกสำหรับการสร้างและการแสดงผลของโมเดลได้ด้วย เช่น `responseSchema`, `topP` และ `topK` [ดูข้อมูลเพิ่มเติม](https://ai.google.dev/api/generate-content?hl=th)
- **อินพุตหลายรูปแบบ**: Gemini สามารถประมวลผลรูปภาพ เสียง และวิดีโอ ซึ่งช่วยให้คุณสามารถทำการวิจัยที่น่าสนใจได้หลากหลายทิศทาง
  [ดูข้อมูลเพิ่มเติม](https://ai.google.dev/gemini-api/docs/vision?hl=th)
- **ความสามารถในการจัดการบริบทที่ยาว**: Gemini 3.0 Flash และ Pro มาพร้อมหน้าต่างบริบทขนาด 1 ล้านโทเค็น
  [ดูข้อมูลเพิ่มเติม](https://ai.google.dev/gemini-api/docs/long-context?hl=th)
- **Grow with Google**: เข้าถึงโมเดล Gemini ผ่าน API และ Google AI
  Studio ได้อย่างรวดเร็วเพื่อใช้ในกรณีการใช้งานจริง หากคุณกำลังมองหาแพลตฟอร์มที่ใช้ Google Cloud, Gemini Enterprise Agent Platform สามารถมอบโครงสร้างพื้นฐานเพิ่มเติมเพื่อรองรับการใช้งานได้

Google ให้สิทธิ์เข้าถึงเครดิต Gemini API แก่นักวิทยาศาสตร์และนักวิจัยในสถาบันการศึกษาผ่าน
[Gemini Academic Program](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=th#gemini-academic-program)เพื่อสนับสนุนการวิจัยทางวิชาการและขับเคลื่อนการวิจัยที่ล้ำสมัย

## เริ่มต้นใช้งาน Gemini

Gemini API และ Google AI Studio ช่วยให้คุณเริ่มต้นใช้งานโมเดลล่าสุดของ Google และเปลี่ยนไอเดียของคุณให้เป็นแอปพลิเคชันที่ปรับขนาดได้

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## นักวิชาการแนะนำ

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=th)

"งานวิจัยของเราศึกษา Gemini ในฐานะโมเดลภาษาภาพ (VLM) และพฤติกรรมของเอเจนต์ในสภาพแวดล้อมที่หลากหลายจากมุมมองด้านความเสถียรและความปลอดภัย จนถึงตอนนี้ เราได้ประเมินความเสถียรของ Gemini ต่อสิ่งรบกวนต่างๆ เช่น หน้าต่างป๊อปอัป เมื่อเอเจนต์ VLM ทำงานบนคอมพิวเตอร์ และใช้ประโยชน์จาก Gemini เพื่อวิเคราะห์การโต้ตอบทางสังคม เหตุการณ์ตามลำดับเวลา รวมถึงปัจจัยเสี่ยงตามอินพุตวิดีโอ"

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=th)

"Gemini Pro และ Flash ที่มีหน้าต่างบริบทขนาดใหญ่ช่วยเราใน OK-Robot ซึ่งเป็นโปรเจ็กต์การจัดการอุปกรณ์เคลื่อนที่ด้วยคำศัพท์แบบเปิด Gemini ช่วยให้สามารถใช้คำสั่งและการค้นหาด้วยภาษาธรรมชาติที่ซับซ้อนกับ "หน่วยความจำ" ของหุ่นยนต์ได้ ซึ่งในกรณีนี้คือการสังเกตก่อนหน้านี้ที่หุ่นยนต์ทำไว้ในระยะเวลาการทำงานที่ยาวนาน นอกจากนี้ ผมและ Mahi Shafiullah ยังใช้ Gemini เพื่อแยกย่อยงานออกเป็นโค้ดที่หุ่นยนต์สามารถดำเนินการได้ในโลกแห่งความเป็นจริง"

## Gemini Academic Program

นักวิจัยในสถาบันการศึกษาที่มีคุณสมบัติ (เช่น คณาจารย์ เจ้าหน้าที่ และนักศึกษาปริญญาเอก) ใน [ประเทศที่รองรับ](https://ai.google.dev/gemini-api/docs/available-regions?hl=th)สามารถสมัครรับเครดิต Gemini API
และขีดจำกัดอัตราที่สูงขึ้นสำหรับโปรเจ็กต์การวิจัย การสนับสนุนนี้ช่วยให้การทดลองทางวิทยาศาสตร์มีปริมาณงานสูงขึ้นและช่วยพัฒนาการวิจัย

เราสนใจเป็นพิเศษในสาขาการวิจัยในส่วนต่อไปนี้ แต่ยินดีรับใบสมัครจากสาขาวิทยาศาสตร์ที่หลากหลาย

- **การประเมินและเกณฑ์มาตรฐาน**: วิธีการประเมินที่ชุมชนรับรองซึ่งสามารถให้สัญญาณประสิทธิภาพที่แข็งแกร่งในด้านต่างๆ เช่น ข้อเท็จจริง ความปลอดภัย การปฏิบัติตามคำแนะนำ การให้เหตุผล และการวางแผน
- **เร่งการค้นพบทางวิทยาศาสตร์เพื่อประโยชน์ของมนุษยชาติ**: การใช้งาน AI ที่เป็นไปได้ในการวิจัยทางวิทยาศาสตร์แบบสหวิทยาการ ซึ่งรวมถึงด้านต่างๆ เช่น โรคหายากและโรคที่ถูกละเลย ชีววิทยาเชิงทดลอง วิทยาศาสตร์วัสดุ และความยั่งยืน
- **การรวมตัวและการโต้ตอบ**: การใช้โมเดลภาษาขนาดใหญ่เพื่อ
  ตรวจสอบการโต้ตอบใหม่ๆ ในสาขา AI แบบรวมตัว การโต้ตอบแบบรอบข้าง หุ่นยนต์ และการปฏิสัมพันธ์ระหว่างมนุษย์กับคอมพิวเตอร์
- **ความสามารถที่เกิดขึ้นใหม่**: การสำรวจความสามารถด้าน Agentic AI ใหม่ๆ ที่จำเป็นต่อการเพิ่มประสิทธิภาพการให้เหตุผลและการวางแผน รวมถึงวิธีขยายความสามารถระหว่างการอนุมาน (เช่น โดยใช้ Gemini Flash)
- **การโต้ตอบและความเข้าใจแบบหลายรูปแบบ**: การระบุช่องว่างและ
  โอกาสสำหรับโมเดลพื้นฐานแบบหลายรูปแบบสำหรับการวิเคราะห์ การให้เหตุผล
  และการวางแผนในงานที่หลากหลาย

คุณสมบัติ: เฉพาะบุคคล (คณาจารย์ นักวิจัย หรือเทียบเท่า) ในสังกัดสถาบันการศึกษาหรือองค์กรวิจัยทางวิชาการที่ถูกต้องเท่านั้นที่สามารถสมัครได้ โปรดทราบว่า Google จะให้และนำสิทธิ์เข้าถึง API และเครดิตออกตามดุลยพินิจของ Google เราจะตรวจสอบใบสมัครทุกเดือน

### เริ่มทำการวิจัยด้วย Gemini API

[สมัครเลย](https://forms.gle/HMviQstU8PxC5iCt5)

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-04-29 UTC"],[],[]]
