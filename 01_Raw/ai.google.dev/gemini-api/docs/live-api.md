---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=th
fetched_at: 2026-11-02T07:24:48.856210+00:00
title: "\u0e20\u0e32\u0e1e\u0e23\u0e27\u0e21\u0e02\u0e2d\u0e07 Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ภาพรวมของ Gemini Live API

Live API ช่วยให้โต้ตอบด้วยเสียงและภาพกับ Gemini แบบเรียลไทม์ที่มีเวลาในการตอบสนองต่ำได้
โดยจะประมวลผลสตรีมเสียง รูปภาพ และข้อความอย่างต่อเนื่องเพื่อส่งมอบ
คำตอบที่พูดออกมาทันทีและเหมือนมนุษย์ ซึ่งจะสร้างประสบการณ์การสนทนาที่เป็นธรรมชาติ
สำหรับผู้ใช้

![ภาพรวม Live API](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=th)

[ลองใช้ Live API ใน Google AI Studiomic](https://aistudio.google.com/live?hl=th)
[โคลนแอปตัวอย่างจาก GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[ใช้ทักษะของเอเจนต์การเขียนโค้ดterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th)

## กรณีการใช้งาน

คุณใช้ Live API เพื่อสร้างเอเจนต์เสียงแบบเรียลไทม์สำหรับ
อุตสาหกรรมต่างๆ ได้ เช่น

- **อีคอมเมิร์ซและการค้าปลีก:** ผู้ช่วยช็อปปิ้งที่ให้คำแนะนำที่ปรับเปลี่ยนในแบบของคุณ
  และตัวแทนฝ่ายสนับสนุนที่แก้ไขปัญหาของลูกค้า
- **เกม:** ตัวละครที่ไม่ใช่ผู้เล่น (NPC) แบบอินเทอร์แอกทีฟ ผู้ช่วยในเกม
  และคำแปลแบบเรียลไทม์ของเนื้อหาในเกม
- **อินเทอร์เฟซรุ่นถัดไป:** ประสบการณ์ที่เปิดใช้เสียงและวิดีโอในหุ่นยนต์
  แว่นตาอัจฉริยะ และยานพาหนะ
- **การดูแลสุขอนามัย:** เพื่อนร่วมดูแลสุขภาพเพื่อสนับสนุนและให้ความรู้แก่ผู้ป่วย
- **บริการทางการเงิน:** ที่ปรึกษา AI สำหรับการจัดการความมั่งคั่งและคำแนะนำด้านการลงทุน
- **การศึกษา:** ที่ปรึกษาและเพื่อนร่วมเรียนรู้ AI ที่ให้คำแนะนำและความคิดเห็นที่ปรับเปลี่ยน
  ในแบบของคุณ
- **การแปลและการแปลภาษา:** การแปลการสนทนาด้วยเสียงแบบเรียลไทม์ที่มีเวลาในการตอบสนองต่ำ ซึ่งช่วยให้การสื่อสารหลายภาษาเป็นไปอย่างราบรื่น
- **การถอดเสียงและการใส่คำบรรยายสด:** การสตรีมมิงการแปลงคำพูดเป็นข้อความแบบเรียลไทม์สำหรับ
  คำบรรยายสด การถอดเสียงการประชุม การป้อนตามคำบอกด้วยเสียง และการบันทึกการโทรของลูกค้า

## ฟีเจอร์หลัก

Live API มีชุดฟีเจอร์ที่ครอบคลุมสำหรับการสร้าง
เอเจนต์เสียงที่แข็งแกร่ง ดังนี้

- [**การรองรับหลายภาษา**](https://ai.google.dev/gemini-api/docs/live-guide?hl=th#supported-languages)
  สนทนาในภาษาที่รองรับ 70 ภาษา
- [**การขัดจังหวะ**](https://ai.google.dev/gemini-api/docs/live-guide?hl=th#interruptions)
  ผู้ใช้สามารถขัดจังหวะโมเดลได้ทุกเมื่อเพื่อการโต้ตอบที่ตอบสนอง
- [**การใช้เครื่องมือ**](https://ai.google.dev/gemini-api/docs/live-tools?hl=th):
  ผสานรวมเครื่องมือต่างๆ เช่น การเรียกใช้ฟังก์ชันและ Google Search เพื่อการโต้ตอบแบบไดนามิก
- [**การถอดเสียงเป็นคำ**](https://ai.google.dev/gemini-api/docs/live-guide?hl=th#audio-transcription):
  แสดงข้อความถอดเสียงทั้งข้อมูลจากผู้ใช้และเอาต์พุตโมเดล
- [**เสียงเชิงรุก**](https://ai.google.dev/gemini-api/docs/live-guide?hl=th#proactive-audio):
  ช่วยให้คุณควบคุมเวลาที่โมเดลตอบกลับและบริบทที่โมเดลตอบกลับ
- [**การตอบโต้ที่แสดงอารมณ์**](https://ai.google.dev/gemini-api/docs/live-guide?hl=th#affective-dialog):
  ปรับรูปแบบและระดับภาษาของคำตอบให้ตรงกับการแสดงออกของผู้ใช้
- [**การถอดเสียงแบบเรียลไทม์**](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=th):
  การสตรีมการแปลงเสียงพูดเป็นข้อความแบบต่อเนื่องแบบเรียลไทม์พร้อมการตรวจหาภาษาอัตโนมัติและคำศัพท์ที่กำหนดเอง
- [**การแปลสด**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=th):
  การแปลเสียงพูดเป็นเสียงพูดแบบเรียลไทม์ในกว่า 70 ภาษา

## ข้อกำหนดทางเทคนิค

ตารางต่อไปนี้แสดงข้อกำหนดทางเทคนิคสำหรับ Live API

| หมวดหมู่ | รายละเอียด |
| --- | --- |
| รูปแบบอินพุต | เสียง (เสียง PCM แบบ 16 บิตดิบ, 16kHz, little-endian), รูปภาพ (JPEG <= 1FPS), ข้อความ |
| รูปแบบเอาต์พุต | เสียง (เสียง PCM แบบ 16 บิตดิบ, 24kHz, Little-Endian) |
| โปรโตคอล | การเชื่อมต่อ WebSocket แบบมีสถานะ (WSS) |

## เลือกวิธีการติดตั้งใช้งาน

เมื่อผสานรวมกับ Live API คุณจะต้องเลือกแนวทางการติดตั้งใช้งานอย่างใดอย่างหนึ่งต่อไปนี้

- **เซิร์ฟเวอร์ต่อเซิร์ฟเวอร์**: แบ็กเอนด์จะเชื่อมต่อกับ Live API โดยใช้
  [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) โดยปกติแล้ว ไคลเอ็นต์จะส่งข้อมูลสตรีม (เสียง วิดีโอ
  ข้อความ) ไปยังเซิร์ฟเวอร์ของคุณ ซึ่งจะส่งต่อข้อมูลไปยัง Live API
- **ไคลเอ็นต์ไปยังเซิร์ฟเวอร์**: โค้ดส่วนหน้าจะเชื่อมต่อกับ Live API โดยตรง
  โดยใช้ [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) เพื่อสตรีมข้อมูลโดยข้ามส่วนหลัง

## เริ่มต้นใช้งาน

เลือกคู่มือที่ตรงกับสภาพแวดล้อมในการพัฒนาซอฟต์แวร์ของคุณ

เซิร์ฟเวอร์ต่อเซิร์ฟเวอร์

### [บทแนะนำเกี่ยวกับ GenAI SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=th)

เชื่อมต่อกับ Gemini Live API โดยใช้ GenAI SDK เพื่อสร้างแอปพลิเคชันมัลติโมดัลแบบเรียลไทม์ด้วยแบ็กเอนด์ Python

ไคลเอ็นต์ต่อเซิร์ฟเวอร์

### [บทแนะนำเกี่ยวกับ WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=th)

เชื่อมต่อกับ Gemini Live API โดยใช้ WebSockets เพื่อสร้างแอปพลิเคชันแบบเรียลไทม์หลายรูปแบบด้วยฟรอนท์เอนด์ JavaScript และโทเค็นชั่วคราว

ชุดพัฒนา Agent

### [บทแนะนำ ADK](https://google.github.io/adk-docs/streaming/)

สร้าง Agent และใช้การสตรีม Agent Development Kit (ADK) เพื่อเปิดใช้การสื่อสารด้วยเสียงและวิดีโอ

## การผสานรวมพาร์ทเนอร์

หากต้องการเพิ่มประสิทธิภาพการพัฒนาแอปเสียงและวิดีโอแบบเรียลไทม์ คุณสามารถใช้
การผสานรวมของบุคคลที่สามที่รองรับ Gemini Live
API ผ่าน WebRTC หรือ WebSockets

[LiveKit

ใช้ Gemini Live API กับ LiveKit Agent](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat โดย Daily

สร้างแชทบอท AI แบบเรียลไทม์โดยใช้ Gemini Live และ Pipecat](https://docs.pipecat.ai/guides/features/gemini-live)
[Fishjam โดย Software Mansion

สร้างแอปพลิเคชันสตรีมมิงวิดีโอสดและเสียงด้วย Fishjam](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Vision Agent ตามสตรีม

สร้างแอปพลิเคชัน AI สำหรับเสียงและวิดีโอแบบเรียลไทม์ด้วย Vision Agent](https://visionagents.ai/integrations/gemini)
[Voximplant

เชื่อมต่อการโทรขาเข้าและขาออกกับ Live API ด้วย Voximplant](https://voximplant.com/products/gemini-client)
[Agora

สร้างแอปพลิเคชัน AI แบบสนทนาแบบเรียลไทม์ด้วย Agora](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

เริ่มต้นใช้งาน Gemini Live API โดยใช้ Firebase AI Logic](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-07 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-07 UTC"],[],[]]
