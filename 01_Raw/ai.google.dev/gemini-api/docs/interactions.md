---
source_url: https://ai.google.dev/gemini-api/docs/interactions?hl=th
fetched_at: 2026-05-11T12:34:41.075107+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# Interactions API

Interactions API เป็นมาตรฐานใหม่สำหรับการสร้างด้วย Gemini ซึ่งแนะนำให้ใช้กับโปรเจ็กต์ใหม่ทั้งหมด โดยได้รับการปรับให้เหมาะกับเวิร์กโฟลว์แบบ Agent, การจัดการสถานะฝั่งเซิร์ฟเวอร์ และการสนทนาแบบหลายรอบที่ซับซ้อนแบบ Multimodal `[`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=th)` API เดิมยังคงได้รับการสนับสนุนอย่างเต็มที่

## เหตุใดจึงต้องใช้ Interactions API

- **การจัดการประวัติฝั่งเซิร์ฟเวอร์**: ลดความซับซ้อนของโฟลว์แบบหลายรอบผ่าน `previous_interaction_id` เซิร์ฟเวอร์จะเปิดใช้สถานะโดยค่าเริ่มต้น (`store=true`) แต่คุณเลือกใช้ลักษณะการทำงานแบบไม่เก็บสถานะได้โดยตั้งค่า `store=false`
- **ขั้นตอนการดำเนินการที่สังเกตได้**: ขั้นตอนที่พิมพ์ทำให้การแก้ไขข้อบกพร่องของโฟลว์ที่ซับซ้อนและการแสดงผล UI สำหรับเหตุการณ์ระดับกลาง (เช่น ความคิดหรือวิดเจ็ตการค้นหา) เป็นเรื่องง่าย
- **สร้างขึ้นสำหรับเวิร์กโฟลว์แบบ Agentic**: รองรับการใช้เครื่องมือหลายขั้นตอน, การจัดการเป็นกลุ่ม และโฟลว์การให้เหตุผลที่ซับซ้อนผ่านขั้นตอนการดำเนินการที่พิมพ์
- **งานที่ใช้เวลานานและงานเบื้องหลัง**: รองรับการโอนการดำเนินการที่ใช้เวลานาน เช่น [Deep Think](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=th) และ [Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=th) ไปยังกระบวนการเบื้องหลังโดยใช้ `background=true`
- **การเข้าถึงโมเดลและความสามารถใหม่ๆ**: ในอนาคต โมเดลใหม่ๆ นอกเหนือจากตระกูลหลัก รวมถึงความสามารถด้าน Agentic AI และเครื่องมือใหม่ๆ จะเปิดตัวใน Interactions API เท่านั้น

**ใช้ Interactions API** หากคุณกำลังเริ่มโปรเจ็กต์ใหม่ สร้างแอปพลิเคชันแบบ Agent หรือต้องการการจัดการการสนทนาฝั่งเซิร์ฟเวอร์ **ใช้ [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=th)** หากคุณมีการผสานรวมที่มีอยู่ซึ่งตรงกับความต้องการของคุณ หรือหากคุณต้องการฟีเจอร์ที่[ยังไม่พร้อมใช้งาน](#limitations)ใน Interactions API เช่น Batch API หรือการแคชที่ชัดเจน

## เริ่มต้นใช้งาน

- **ตั้งค่า Agent การเขียนโค้ด**: เชื่อมต่อกับ **Gemini Docs MCP** และติดตั้ง
  ทักษะ `gemini-interactions-api` เพื่อให้ Assistant เข้าถึง
  เอกสารประกอบสำหรับนักพัฒนาซอฟต์แวร์และแนวทางปฏิบัติแนะนำล่าสุดได้โดยตรง
  [ตั้งค่า Agent การเขียนโค้ด →](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th)
- **ย้ายข้อมูลจาก `generateContent`**: หากคุณมีการผสานรวมที่มีอยู่
  ให้ทำตาม[คำแนะนำในการย้ายข้อมูล](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=th)เพื่อ
  เปลี่ยนไปใช้ Interactions API
- **ลองใช้ QuickStart**: เริ่มต้นใช้งานด้วยตัวอย่างการทำงานขั้นต่ำใน
  [Interactions API QuickStart](https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=th)

### คำแนะนำฟีเจอร์

สำรวจความสามารถเฉพาะของ Interactions API ผ่านคำแนะนำเหล่านี้ คุณสามารถใช้ปุ่มเปิด/ปิดในหน้าเว็บเหล่านี้เพื่อสลับระหว่าง generateContent กับ Interactions API

- [การสร้างข้อความ](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=th)
- [การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=th)
- [การทำความเข้าใจรูปภาพ](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=th)
- [การทำความเข้าใจเสียง](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=th)
- [การทำความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=th)
- [การประมวลผลเอกสาร](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=th)
- [การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=th)
- [เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=th)
- [Deep Research Agent](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=th)
- [การอนุมานแบบยืดหยุ่น](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=th)
- [การอนุมานตามลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=th)

## วิธีการทำงานของ Interactions API

Interactions API มุ่งเน้นไปที่ทรัพยากรหลักอย่าง [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=th#Resource:Interaction) `Interaction` แสดงถึงการสนทนาหรือการทำงานที่เสร็จสมบูรณ์ โดยทำหน้าที่เป็นบันทึกเซสชันที่มีประวัติทั้งหมดของการโต้ตอบเป็นลำดับ**ขั้นตอนการดำเนินการ** ตามลำดับเวลา ขั้นตอนเหล่านี้รวมถึงความคิดของโมเดล การเรียกเครื่องมือฝั่งเซิร์ฟเวอร์หรือฝั่งไคลเอ็นต์และผลลัพธ์ (เช่น `function_call` และ `function_result`) และ `model_output` สุดท้าย ทรัพยากรที่จัดเก็บไว้ (ดึงข้อมูลผ่าน `interactions.get`) ยังรวมถึงขั้นตอน `user_input` เพื่อให้มีบริบทที่สมบูรณ์ แม้ว่าการตอบกลับ `interactions.create` จะแสดงเฉพาะขั้นตอนที่โมเดลสร้างขึ้น

เมื่อคุณเรียกใช้
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=th#CreateInteraction) คุณกำลัง
สร้างทรัพยากร `Interaction` ใหม่

### การจัดการสถานะฝั่งเซิร์ฟเวอร์

คุณสามารถใช้ `id` ของการโต้ตอบที่เสร็จสมบูรณ์ในการเรียกครั้งถัดไปโดยใช้ `previous_interaction_id` พารามิเตอร์ เพื่อสนทนาต่อ เซิร์ฟเวอร์จะใช้รหัสนี้เพื่อดึงข้อมูลประวัติการสนทนา ซึ่งช่วยให้คุณไม่ต้องส่งประวัติการแชททั้งหมดอีกครั้ง

พารามิเตอร์ `previous_interaction_id` จะเก็บเฉพาะประวัติการสนทนา (อินพุตและเอาต์พุต) โดยใช้ `previous_interaction_id` พารามิเตอร์อื่นๆ มี**ขอบเขตการโต้ตอบ** และใช้ได้กับการโต้ตอบเฉพาะที่คุณกำลังสร้างเท่านั้น ดังนี้

- `tools`
- `system_instruction`
- `generation_config` (รวมถึง `thinking_level`, `temperature` และอื่นๆ)

ซึ่งหมายความว่าคุณต้องระบุพารามิเตอร์เหล่านี้อีกครั้งในการโต้ตอบใหม่แต่ละครั้งหากต้องการให้พารามิเตอร์มีผล การจัดการสถานะฝั่งเซิร์ฟเวอร์นี้เป็นตัวเลือก คุณยังสามารถทำงานในโหมดไม่เก็บสถานะได้โดยส่งประวัติการสนทนาทั้งหมดในแต่ละคำขอ

### การจัดเก็บและการเก็บรักษาข้อมูล

โดยค่าเริ่มต้น API จะจัดเก็บออบเจ็กต์ Interaction ทั้งหมด (`store=true`) เพื่อลดความซับซ้อนในการใช้ฟีเจอร์การจัดการสถานะฝั่งเซิร์ฟเวอร์ (ด้วย `previous_interaction_id`), การดำเนินการเบื้องหลัง (โดยใช้ `background=true`) และวัตถุประสงค์ในการสังเกต

- **ระดับแบบชำระเงิน**: ระบบจะเก็บรักษาการโต้ตอบไว้เป็นเวลา **55 วัน**
- **รุ่นฟรี**: ระบบจะเก็บรักษาการโต้ตอบไว้เป็นเวลา **1 วัน**

หากไม่ต้องการให้ระบบดำเนินการเช่นนี้ คุณสามารถตั้งค่า `store=false` ในคำขอได้ การควบคุมนี้แยกจากการจัดการสถานะ คุณเลือกไม่ใช้การจัดเก็บสำหรับการโต้ตอบใดก็ได้ อย่างไรก็ตาม โปรดทราบว่า `store=false` เข้ากันไม่ได้กับ `background=true` และป้องกันไม่ให้ใช้ `previous_interaction_id` สำหรับการโต้ตอบครั้งถัดไป

คุณสามารถลบการโต้ตอบที่จัดเก็บไว้ได้ทุกเมื่อโดยใช้วิธีการลบที่พบใน
ข้อมูลอ้างอิง [API](https://ai.google.dev/api/interactions-api?hl=th) คุณจะลบการโต้ตอบได้ก็ต่อเมื่อทราบรหัสการโต้ตอบเท่านั้น

ระบบจะลบข้อมูลของคุณโดยอัตโนมัติหลังจากระยะเวลาการเก็บรักษาหมดลง

ระบบจะประมวลผลออบเจ็กต์ Interaction ตาม[ข้อกำหนด](https://ai.google.dev/gemini-api/terms?hl=th)

## แนวทางปฏิบัติแนะนำ

- **อัตราการพบแคช**: การใช้ `previous_interaction_id` เพื่อสนทนาต่อ
  ช่วยให้ระบบใช้การแคชโดยนัยสำหรับ
  ประวัติการสนทนาได้ง่ายขึ้น ซึ่งจะช่วยปรับปรุงประสิทธิภาพและลดค่าใช้จ่าย
- **การโต้ตอบแบบผสม**: คุณสามารถผสมและจับคู่การโต้ตอบแบบ Agent และ
  โมเดลในการสนทนาได้ตามต้องการ ตัวอย่างเช่น คุณสามารถใช้ Agent เฉพาะ เช่น Deep Research Agent สำหรับการเก็บรวบรวมข้อมูลเริ่มต้น แล้วใช้โมเดล Gemini มาตรฐานสำหรับงานติดตามผล เช่น การสรุปหรือการจัดรูปแบบใหม่ โดยลิงก์ขั้นตอนเหล่านี้ด้วย `previous_interaction_id`

## โมเดลและ Agent ที่รองรับ

| ชื่อโมเดล | ประเภท | รหัสโมเดล |
| --- | --- | --- |
| Gemini 3.1 Flash-Lite | โมเดล | `gemini-3.1-flash-lite` |
| Gemini 3.1 Flash-Lite (เวอร์ชันตัวอย่าง) | โมเดล | `gemini-3.1-flash-lite-preview` |
| Gemini 3.1 Pro (เวอร์ชันตัวอย่าง) | โมเดล | `gemini-3.1-pro-preview` |
| Gemini 3 Flash (เวอร์ชันตัวอย่าง) | โมเดล | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | โมเดล | `gemini-2.5-pro` |
| Gemini 2.5 Flash | โมเดล | `gemini-2.5-flash` |
| Gemini 2.5 Flash-Lite | โมเดล | `gemini-2.5-flash-lite` |
| Lyria 3 Clip (เวอร์ชันตัวอย่าง) | โมเดล | `lyria-3-clip-preview` |
| Lyria 3 Pro (เวอร์ชันตัวอย่าง) | โมเดล | `lyria-3-pro-preview` |
| Deep Research (เวอร์ชันตัวอย่าง) | Agent | `deep-research-pro-preview-12-2025` |
| Deep Research (เวอร์ชันตัวอย่าง) | Agent | `deep-research-preview-04-2026` |
| Deep Research Max (เวอร์ชันตัวอย่าง) | Agent | `deep-research-max-preview-04-2026` |

## SDK

คุณสามารถใช้ Google GenAI SDK เวอร์ชันล่าสุดเพื่อเข้าถึง Interactions API ได้

- ใน Python คือแพ็กเกจ `google-genai` ตั้งแต่เวอร์ชัน `1.55.0` เป็นต้นไป
- ใน JavaScript คือแพ็กเกจ `@google/genai` ตั้งแต่เวอร์ชัน `1.33.0` เป็นต้นไป

ดูข้อมูลเพิ่มเติมเกี่ยวกับวิธีติดตั้ง SDK ได้ในหน้า
[ไลบรารี](https://ai.google.dev/gemini-api/docs/libraries?hl=th)

## ข้อจำกัด

- **สถานะเบต้า**: Interactions API อยู่ในเวอร์ชันเบต้า/เวอร์ชันตัวอย่าง ฟีเจอร์และสคีมาอาจมีการเปลี่ยนแปลง
- **MCP ระยะไกล**: Gemini 3 ไม่รองรับ MCP ระยะไกล ซึ่งจะพร้อมใช้งานเร็วๆ นี้

[API รองรับฟีเจอร์ต่อไปนี้ แต่ **ยังไม่
พร้อมใช้งาน** ใน Interactions API](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=th)`generateContent`

- **[ข้อมูลเมตาวิดีโอ](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=th)**: ช่อง `video_metadata` ใช้เพื่อตั้งค่าช่วงเวลาการตัด
  และอัตราเฟรมที่กำหนดเองสำหรับการทำความเข้าใจวิดีโอ
- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)**
- **[การเรียกฟังก์ชันอัตโนมัติ (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=th#automatic_function_calling_python_only)**
- **[การแคชที่ชัดเจน](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=th)**: โปรดทราบว่าการแคชโดยนัยฝั่งเซิร์ฟเวอร์พร้อมใช้งานใน Interactions API
  ผ่าน `previous_interaction_id`

## การเปลี่ยนแปลงที่ส่งผลกับส่วนอื่นในระบบ

ขณะนี้ Interactions API อยู่ในระยะเบต้าระยะเริ่มแรก เรากำลังพัฒนาและปรับแต่งความสามารถของ API, สคีมาทรัพยากร และอินเทอร์เฟซ SDK อย่างต่อเนื่องโดยอิงตามการใช้งานจริงและความคิดเห็นของนักพัฒนาซอฟต์แวร์

ด้วยเหตุนี้ **การเปลี่ยนแปลงที่ส่งผลกับส่วนอื่นในระบบจึงอาจเกิดขึ้นได้**
การอัปเดตอาจรวมถึงการเปลี่ยนแปลงต่อไปนี้

- สคีมาสำหรับอินพุตและเอาต์พุต
- ลายเซ็นเมธอด SDK และโครงสร้างออบเจ็กต์
- ลักษณะการทำงานของฟีเจอร์ที่เฉพาะเจาะจง

สำหรับเวิร์กโหลดการใช้งานจริง คุณควรใช้ API มาตรฐานต่อไป
[`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=th) API นี้ยังคงเป็นเส้นทางที่แนะนำสำหรับการติดตั้งใช้งานที่เสถียร และเราจะพัฒนาและดูแลรักษา API นี้ต่อไป

## ความคิดเห็น

ความคิดเห็นของคุณมีความสำคัญอย่างยิ่งต่อการพัฒนา Interactions API
แชร์ความคิดเห็น รายงานข้อบกพร่อง หรือขอฟีเจอร์ใน
[ฟอรัมชุมชนนักพัฒนาซอฟต์แวร์ Google AI](https://discuss.ai.google.dev/c/gemini-api/4?hl=th)

## ขั้นตอนถัดไป

- ลองใช้ [Notebook QuickStart ของ Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=th)
- ดูข้อมูลเพิ่มเติมเกี่ยวกับ [Gemini Deep Research Agent](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-08 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-08 UTC"],[],[]]
