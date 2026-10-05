---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=th
fetched_at: 2026-10-05T06:31:19.009254+00:00
title: "\u0e01\u0e32\u0e23\u0e41\u0e04\u0e0a\u0e1a\u0e23\u0e34\u0e1a\u0e17 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การแคชบริบท

ในเวิร์กโฟลว์ AI ทั่วไป คุณอาจส่งโทเค็นอินพุตเดียวกันซ้ำๆ ไปยังโมเดล Gemini API มีการแคชแบบไม่เจาะจงเพื่อเพิ่มประสิทธิภาพและลดต้นทุน

## การแคชแบบไม่เจาะจง

ระบบจะเปิดใช้การแคชแบบไม่เจาะจงโดยค่าเริ่มต้นสำหรับโมเดล Gemini 2.5 และใหม่กว่าทั้งหมด
โดยรองรับทั้งโหมดการสนทนา[แบบเก็บสถานะ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#multi-turn-conversations) (ใช้ `previous_interaction_id`)
และ[แบบไม่เก็บสถานะ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#stateless-conversations)
เราจะส่งต่อการประหยัดต้นทุนโดยอัตโนมัติหากคำขอของคุณตรงกับแคช คุณไม่จำเป็นต้องดำเนินการใดๆ เพื่อเปิดใช้ฟีเจอร์นี้ จำนวนโทเค็นอินพุตขั้นต่ำสำหรับการแคชบริบทแสดงอยู่ในตารางต่อไปนี้สำหรับแต่ละโมเดล

| โมเดล | ขีดจำกัดโทเค็นขั้นต่ำ |
| --- | --- |
| Gemini 3.8 Flash | 4,096 |
| Gemini 3.7 Flash | 4,096 |
| Gemini 3.6 Flash | 4,096 |
| Gemini 3.5 Flash | 4,096 |
| Gemini 3.1 Pro Preview | 4,096 |
| Gemini 2.5 Flash | 2,048 |
| Gemini 2.5 Pro | 2,048 |

วิธีเพิ่มโอกาสที่จะพบแคชแบบไม่เจาะจง:

- ลองวางเนื้อหาขนาดใหญ่และเนื้อหาทั่วไปไว้ที่จุดเริ่มต้นของพรอมต์
- ลองส่งคำขอที่มีคำนำหน้าที่คล้ายกันภายในระยะเวลาสั้นๆ

คุณสามารถดูจำนวนโทเค็นที่ตรงกับแคชได้ในช่อง `usage.total_cached_tokens` (Python และ JavaScript) ของออบเจ็กต์การตอบกลับ

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-10 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-10 UTC"],[],[]]
