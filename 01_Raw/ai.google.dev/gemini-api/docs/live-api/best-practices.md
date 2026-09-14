---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=th
fetched_at: 2026-09-14T05:51:19.945283+00:00
title: "\u0e41\u0e19\u0e27\u0e17\u0e32\u0e07\u0e1b\u0e0f\u0e34\u0e1a\u0e31\u0e15\u0e34\u0e41\u0e19\u0e30\u0e19\u0e33\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# แนวทางปฏิบัติแนะนำสำหรับ Live API

คู่มือนี้จะอธิบายแนวทางปฏิบัติแนะนำที่คุณทำตามได้เพื่อเพิ่มประสิทธิภาพการใช้ Live API
ดูภาพรวมและโค้ดตัวอย่างสำหรับ Use Case ทั่วไปได้ที่หน้า[เริ่มต้นใช้งาน Live API](https://ai.google.dev/gemini-api/docs/live?hl=th)

## ออกแบบวิธีการของระบบให้ชัดเจน

เราขอแนะนำให้กำหนดชุดวิธีการของระบบ (SI) ที่ชัดเจน ซึ่งกำหนดบุคลิกของเอเจนต์ กฎการสนทนา และขอบเขตการทำงานตามลำดับนี้ เพื่อให้ Live API ทำงานได้ดีที่สุด

แยกเอเจนต์แต่ละรายออกเป็น SI ที่แตกต่างกันเพื่อให้ได้ผลลัพธ์ที่ดีที่สุด

1. **ระบุบุคลิกของเอเจนต์:** ระบุรายละเอียดเกี่ยวกับชื่อ บทบาท และลักษณะที่ต้องการของเอเจนต์ หากต้องการระบุสำเนียง ให้ระบุภาษาเอาต์พุตที่ต้องการด้วย (เช่น สำเนียงอังกฤษสำหรับผู้พูดภาษาอังกฤษ)
2. **ระบุกฎการสนทนา:** ใส่กฎเหล่านี้ตามลำดับที่คุณต้องการให้โมเดลทำตาม แยกความแตกต่างระหว่างองค์ประกอบการสนทนาแบบครั้งเดียวกับวงจรการสนทนา เช่น

   - **องค์ประกอบแบบครั้งเดียว:** รวบรวมรายละเอียดของลูกค้าเพียงครั้งเดียว (เช่น ชื่อ สถานที่ หมายเลขบัตรสะสมแต้ม)
   - **วงจรการสนทนา:** ผู้ใช้สามารถพูดคุยเกี่ยวกับคำแนะนำ ราคา การคืนสินค้า และการจัดส่ง และอาจต้องการเปลี่ยนจากหัวข้อหนึ่งไปอีกหัวข้อหนึ่ง แจ้งให้โมเดลทราบว่าสามารถมีส่วนร่วมในวงจรการสนทนานี้ได้ตราบเท่าที่ผู้ใช้ต้องการ
3. **ระบุการเรียกใช้เครื่องมือภายในโฟลว์ในประโยคที่แตกต่างกัน:** เช่น หากขั้นตอนแบบครั้งเดียวในการรวบรวมรายละเอียดของลูกค้าต้องใช้ฟังก์ชัน `get_user_info` คุณอาจพูดว่า *ขั้นตอนแรกคือการรวบรวมข้อมูลผู้ใช้ ก่อนอื่นให้ขอให้ผู้ใช้ระบุชื่อ สถานที่ และหมายเลขบัตรสะสมแต้ม จากนั้น
   เรียกใช้ `get_user_info` พร้อมรายละเอียดเหล่านี้*
4. **เพิ่มขอบเขตการทำงานที่จำเป็น:** ระบุขอบเขตการทำงานการสนทนาทั่วไปที่คุณไม่ต้องการให้โมเดลทำ และระบุตัวอย่างเฉพาะได้หาก *x* เกิดขึ้น คุณต้องการให้โมเดลทำ *y* หากยังไม่ได้ความแม่นยำในระดับที่ต้องการ ให้ใช้คำว่า *อย่างชัดเจน* เพื่อแนะนำให้โมเดลมีความแม่นยำ

## กำหนดเครื่องมืออย่างแม่นยำ

เมื่อใช้เครื่องมือกับ Live API ให้ระบุรายละเอียดในการกำหนดเครื่องมือ
อย่าลืมบอก Gemini ว่าควรเรียกใช้การเรียกใช้เครื่องมือภายใต้เงื่อนไขใด ดูรายละเอียดเพิ่มเติมได้ที่[การกำหนดเครื่องมือ](#tool-definitions-example)ใน
ส่วนตัวอย่าง

## สร้างพรอมต์ที่มีประสิทธิภาพ

- **ใช้พรอมต์ที่ชัดเจน:** ระบุตัวอย่างสิ่งที่โมเดลควรและไม่ควรทำในพรอมต์ และพยายามจำกัดพรอมต์ให้เป็นพรอมต์เดียวต่อบุคลิกหรือบทบาทในแต่ละครั้ง ลองใช้การเชื่อมพรอมต์แทนพรอมต์ที่ยาวหลายหน้า โมเดลจะทำงานได้ดีที่สุดในงานที่มีการเรียกใช้ฟังก์ชันเดียว
- **ระบุคำสั่งและข้อมูลเริ่มต้น:** Live API คาดหวังให้ผู้ใช้ป้อนข้อมูลจากผู้ใช้ก่อนที่จะตอบกลับ หากต้องการให้ Live API เริ่มการสนทนา ให้ใส่พรอมต์ที่ขอให้ทักทายผู้ใช้หรือเริ่มการสนทนา ใส่ข้อมูลเกี่ยวกับผู้ใช้เพื่อให้ Live API ปรับการทักทายให้เป็นแบบเฉพาะบุคคล

## ระบุภาษา

เพื่อให้ได้ประสิทธิภาพสูงสุดใน `gemini-live-2.5-flash` แบบเรียงซ้อนของ Live API ให้ตรวจสอบว่า `language_code` ของ API ตรงกับภาษาที่ผู้ใช้พูด

หากต้องการให้โมเดลตอบกลับเป็นภาษาอื่นที่ไม่ใช่ภาษาอังกฤษ ให้ใส่ข้อมูลต่อไปนี้เป็นส่วนหนึ่งของวิธีการของระบบ

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## การสตรีม

เมื่อใช้เสียงแบบเรียลไทม์ ให้ทำตามแนวทางปฏิบัติแนะนำต่อไปนี้

- **ขนาด Chunk และเวลาในการตอบสนอง**: ส่งเสียงเป็น Chunk ขนาด 20 มิลลิวินาทีถึง 40 มิลลิวินาที
- **การจัดการการขัดจังหวะ**: เมื่อผู้ใช้พูดขณะที่โมเดลกำลังตอบกลับ
  เซิร์ฟเวอร์จะส่งข้อความ `server_content` พร้อม `"interrupted": true` คุณต้องทิ้งบัฟเฟอร์เสียงฝั่งไคลเอ็นต์ทันทีเพื่อป้องกันไม่ให้เอเจนต์พูดทับผู้ใช้

## การจัดการบริบท

ใช้ `ContextWindowCompressionConfig` สำหรับเซสชันที่ยาว เนื่องจากโทเค็นเสียงดั้งเดิมจะสะสมอย่างรวดเร็ว (ประมาณ 25 โทเค็นต่อวินาทีของเสียง)

## การบัฟเฟอร์ของไคลเอ็นต์

อย่าบัฟเฟอร์เสียงอินพุตมากเกินไป (เช่น 1 วินาที) ก่อนส่ง ส่ง Chunk ขนาดเล็ก (20 มิลลิวินาที - 100 มิลลิวินาที) เพื่อลดเวลาในการตอบสนอง

## การสุ่มตัวอย่างใหม่

ตรวจสอบว่าแอปพลิเคชันไคลเอ็นต์สุ่มตัวอย่างอินพุตจากไมโครโฟนใหม่ (มักจะเป็น 44.1kHz หรือ 48kHz) เป็น 16kHz ก่อนส่ง

## การจัดการเซสชัน

ทำตามหลักเกณฑ์ต่อไปนี้เพื่อจัดการวงจรชีวิตของเซสชันและรับประกันประสบการณ์ของผู้ใช้ที่เชื่อถือได้

- **เปิดใช้การบีบอัดหน้าต่างบริบท:** โทเค็นเสียงจะสะสมประมาณ 25 โทเค็นต่อวินาที หากไม่มีการบีบอัด เซสชันเสียงอย่างเดียวจะจำกัดไว้ที่ 15 นาที และเซสชันเสียงและวิดีโอจะจำกัดไว้ที่ 2 นาที เปิดใช้
  [การบีบอัดหน้าต่างบริบท](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=th#context-window-compression)
  เพื่อขยายเซสชันให้มีระยะเวลาไม่จำกัด
- **ใช้การกลับมาทำงานต่อของเซสชัน:** เซิร์ฟเวอร์อาจรีเซ็ตการเชื่อมต่อ WebSocket เป็นระยะ ใช้
  [การกลับมาทำงานต่อของเซสชัน](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=th#session-resumption)
  เพื่อเชื่อมต่ออีกครั้งได้อย่างราบรื่นโดยไม่สูญเสียบริบท เก็บโทเค็นการกลับมาทำงานต่อล่าสุดจากข้อความ `SessionResumptionUpdate` และส่งโทเค็นดังกล่าวเป็นแฮนเดิลเมื่อเชื่อมต่ออีกครั้ง โทเค็นการกลับมาทำงานต่อมีอายุ 2 ชั่วโมงหลังจากเซสชันล่าสุดสิ้นสุดลง
- **จัดการข้อความ GoAway:** เซิร์ฟเวอร์จะส่ง
  [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=th#goaway-message)
  ก่อนที่จะสิ้นสุดการเชื่อมต่อ ฟังข้อความนี้และใช้ช่อง `timeLeft` เพื่อสรุปหรือเชื่อมต่ออีกครั้งอย่างราบรื่นก่อนที่การเชื่อมต่อจะปิด
- **จัดการสัญญาณ generationComplete:** ใช้ข้อความ
  [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=th#generation-complete-message)
  เพื่อดูว่าโมเดลสร้างการตอบกลับเสร็จแล้วเมื่อใด เพื่อให้แอปพลิเคชัน
  อัปเดต UI หรือดำเนินการตามการดำเนินการถัดไปได้

ดูรายละเอียดการนำไปใช้งานได้ที่
[การจัดการเซสชัน](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=th)

## ตัวอย่าง

ตัวอย่างนี้รวมทั้งแนวทางปฏิบัติแนะนำและ
[หลักเกณฑ์สำหรับการออกแบบวิธีการของระบบ](#system-instruction-guidelines)เพื่อ
แนะนำประสิทธิภาพของโมเดลในฐานะโค้ชด้านอาชีพ

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### การกำหนดเครื่องมือ

JSON นี้กำหนดฟังก์ชันที่เกี่ยวข้องซึ่งเรียกใช้ในตัวอย่างโค้ชด้านอาชีพ
เมื่อกำหนดฟังก์ชัน ให้ใส่ชื่อ คำอธิบาย พารามิเตอร์ และเงื่อนไขการเรียกใช้เพื่อให้ได้ผลลัพธ์ที่ดีที่สุด

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

## การกำหนดราคาและการเรียกเก็บเงิน

Gemini Live API จะเรียกเก็บเงินตามการใช้โทเค็นเท่านั้น เนื่องจาก Live API จะรักษาเซสชัน WebSocket แบบถาวรไว้ การเรียกเก็บเงินจึงเป็นไปตามโมเดลแบบทบต้นตามหน้าต่างบริบทที่ใช้งานอยู่

### หน้าต่างบริบทของเซสชัน (ค่าใช้จ่ายแบบทบต้น)

API จะเรียกเก็บเงินต่อรอบสำหรับโทเค็นทั้งหมดที่อยู่ในหน้าต่างบริบทของเซสชัน "รอบ" หมายถึงข้อมูลจากผู้ใช้ 1 รายการและการตอบกลับที่เกี่ยวข้องของโมเดล

- **การสะสม:** หน้าต่างบริบทจะมีโทเค็นใหม่จากรอบปัจจุบัน รวมถึงโทเค็นทั้งหมดที่สะสมจากรอบก่อนหน้า
- **การเรียกเก็บเงินซ้ำ:** ระบบจะประมวลผลโทเค็นที่ผ่านมาอีกครั้งและนำมาพิจารณาในแต่ละรอบใหม่ โดยจะพิจารณาตามขนาดหน้าต่างบริบทที่คุณกำหนดค่าไว้ เมื่อเซสชันยาวขึ้น ค่าใช้จ่ายต่อรอบจะเพิ่มขึ้นเนื่องจากระบบจะประมวลผลประวัติการสนทนาอีกครั้ง

### โทเค็นเสียงและการถอดเสียงเป็นคำ

Live API เป็นแบบหลายรูปแบบโดยกำเนิด โดยจะเก็บประวัติการสนทนาเป็นโทเค็นเสียงดิบเพื่อรักษาความแตกต่างและโทนเสียง

- **การเรียกเก็บเงินสำหรับเสียง:** API จะเรียกเก็บเงินสำหรับโทเค็นเสียงดั้งเดิมที่สะสมในอัตราอินพุตเสียงมาตรฐานในทุกรอบ
- **ค่าบริการเพิ่มเติมสำหรับการถอดเสียงเป็นคำ:** เมื่อเปิดใช้การถอดเสียงเป็นคำจากเสียงเป็นข้อความ (`inputAudioTranscription` หรือ `outputAudioTranscription`) API จะเรียกเก็บเงินสำหรับโทเค็นข้อความทั้งหมดที่สร้างขึ้นสำหรับการถอดเสียงเป็นคำในอัตราเอาต์พุตโทเค็นข้อความ นอกเหนือจากค่าใช้จ่ายโทเค็นเสียงมาตรฐาน

### การจัดการค่าใช้จ่ายด้วยขีดจำกัดบริบท

กำหนดค่าขนาดหน้าต่างบริบทโดยใช้ `contextWindowCompression` เพื่อป้องกันไม่ให้ค่าใช้จ่ายเพิ่มขึ้นอย่างไม่จำกัดในเซสชันที่ยาว

เมื่อตั้งค่าทริกเกอร์การบีบอัด (เช่น 25,000 โทเค็น) และหน้าต่างแบบเลื่อน (เช่น 8,000 โทเค็น) API จะนำโทเค็นเก่าออกโดยอัตโนมัติเมื่อถึงเกณฑ์ จากนั้น API จะเรียกเก็บเงินในรอบถัดไปสำหรับประวัติที่เก็บไว้และโทเค็นใหม่เท่านั้น

### โหมดเสียงเชิงรุก

เมื่อเปิดใช้โหมดเสียงเชิงรุก ระบบจะเรียกเก็บเงินสำหรับโทเค็นอินพุตตลอดเวลาที่ Live API กำลังฟังอยู่ ขณะที่จะเรียกเก็บเงินสำหรับโทเค็นเอาต์พุตเมื่อ API ตอบกลับเท่านั้น

- **หมายเหตุสำหรับ Gemini 3.1:** `gemini-3.1-flash-live-preview` ไม่รองรับโหมดเสียงเชิงรุก สำหรับโมเดลนี้ ระบบจะเรียกเก็บเงินสำหรับเสียงเมื่อมีการสตรีมอินพุตอย่างจริงจังเท่านั้น

ดูข้อมูลการกำหนดราคารายละเอียดได้ที่หน้าการกำหนดราคา [Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-08 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-08 UTC"],[],[]]
