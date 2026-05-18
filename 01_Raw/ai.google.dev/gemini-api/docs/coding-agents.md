---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=th
fetched_at: 2026-05-18T13:10:11.118252+00:00
title: "\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32\u0e1c\u0e39\u0e49\u0e0a\u0e48\u0e27\u0e22\u0e40\u0e02\u0e35\u0e22\u0e19\u0e42\u0e04\u0e49\u0e14\u0e14\u0e49\u0e27\u0e22 Gemini MCP \u0e41\u0e25\u0e30\u0e17\u0e31\u0e01\u0e29\u0e30 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ตั้งค่าผู้ช่วยเขียนโค้ดด้วย Gemini MCP และทักษะ

ผู้ช่วยเขียนโค้ดด้วย AI มีประสิทธิภาพสูงแต่ก็มีข้อจำกัด เช่น ข้อมูลฝึกฝนจะสิ้นสุด ณ วันที่ที่กำหนด ฟีเจอร์ใหม่ของ API และการเปลี่ยนแปลงต่างๆ จะไม่รวมอยู่ด้วย หากไม่มีสิทธิ์เข้าถึงเอกสารประกอบเฉพาะของ Gemini, Agent อาจแนะนำรูปแบบทั่วไปแทนที่จะเป็นแนวทางที่ปรับให้เหมาะสม

เราขอแนะนำให้ตั้งค่า **Gemini Docs MCP** และเพิ่มประสิทธิภาพสภาพแวดล้อมด้วย **Gemini API Skills** เพื่อให้ผู้ช่วยเขียนโค้ดของคุณทันต่อ Gemini API ที่มีการพัฒนาอยู่เสมอและวิธีการใช้งานที่แนะนำ แม้ว่าเครื่องมือเหล่านี้จะใช้งานแยกกันได้ แต่ก็ได้รับการออกแบบมาให้ทำงานร่วมกันเพื่อให้ครอบคลุมการใช้งานทั้งหมด

## เชื่อมต่อ Gemini Docs MCP

Gemini โฮสต์เซิร์ฟเวอร์ Model Context Protocol (MCP) สาธารณะที่ `https://gemini-api-docs-mcp.dev` การเชื่อมต่อ Agent เขียนโค้ดกับเซิร์ฟเวอร์นี้จะช่วยให้มั่นใจได้ว่าการค้นหาทั้งหมดจะเข้าถึง API, การอัปเดตโค้ด และตัวอย่างการกำหนดค่าที่เหมาะสมที่สุดได้

เรียกใช้คำสั่งต่อไปนี้ในเทอร์มินัลของ Agent หรือรูทของโปรเจ็กต์เพื่อติดตั้งเซิร์ฟเวอร์

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

เซิร์ฟเวอร์นี้จะเพิ่มฟังก์ชัน `search_documentation` ที่ Agent ใช้เพื่อดึงข้อมูลคำจำกัดความของ API และรูปแบบการผสานรวมแบบเรียลไทม์จากไฟล์เอกสารประกอบอย่างเป็นทางการของ Gemini ได้

## เพิ่มทักษะการพัฒนา API

ทักษะเหล่านี้มี**กฎและแนวทางปฏิบัติแนะนำในตัว** (เช่น การบังคับใช้ SDK เวอร์ชันที่ถูกต้องและโมเดลเวอร์ชันปัจจุบัน) ในบริบทของผู้ช่วยโดยตรง ทักษะนี้ทำงานร่วมกับบริการ Gemini Docs MCP โดยหากคุณติดตั้งทั้ง 2 อย่างไว้ ทักษะจะใช้บริการ MCP สำหรับเอกสารประกอบ แต่แม้ว่าจะไม่ได้ติดตั้ง MCP ไว้ ทักษะก็จะดึงข้อมูล `llms.txt` จาก `ai.google.dev` เป็นข้อมูลสำรอง

หากต้องการติดตั้งทักษะเหล่านี้ คุณสามารถใช้เครื่องมือที่รองรับอย่างใดอย่างหนึ่งต่อไปนี้ โดยเราได้ระบุวิธีการติดตั้งสำหรับทั้ง 2 อย่างไว้ใต้โมดูลทักษะแต่ละโมดูล

- **[skills.sh](https://skills.sh)**: แนะนำ มาตรฐานเปิดสำหรับลักษณะการทำงานของ Agent แบบพกพา
- **[Context7](https://context7.com)**

### gemini-api-dev

ทักษะพื้นฐานสำหรับการพัฒนา Gemini แบบอเนกประสงค์ ทักษะนี้มีเอกสารประกอบและแนวทางปฏิบัติแนะนำสำหรับสิ่งต่อไปนี้

- การกำหนดเส้นทางพรอมต์ไปยังโมเดลปัจจุบัน (เช่น Gemini 3.1 Pro/Flash) และหลีกเลี่ยงโมเดลที่เลิกใช้งานแล้ว
- การเขียนพรอมต์แบบหลายรูปแบบ การเรียกใช้ฟังก์ชัน เอาต์พุตที่มีโครงสร้าง และรูปแบบการผสานรวมทั่วไป

#### ติดตั้งด้วย skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### ติดตั้งด้วย Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

ทักษะสำหรับการสร้างแอปพลิเคชัน AI สำหรับการสนทนาแบบเรียลไทม์ด้วย Gemini Live API ทักษะนี้มีเอกสารประกอบและแนวทางปฏิบัติแนะนำสำหรับสิ่งต่อไปนี้

- การเชื่อมต่อ WebSocket สำหรับการสตรีมที่มีเวลาในการตอบสนองต่ำ
- การสตรีมเสียง วิดีโอ และข้อความ
- การตรวจหากิจกรรมเสียงและการรองรับการขัดจังหวะ

#### ติดตั้งด้วย skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### ติดตั้งด้วย Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

ทักษะสำหรับการสร้างแอปด้วย
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=th) Interactions API เป็นอินเทอร์เฟซแบบรวมสำหรับการโต้ตอบกับโมเดลและ Agent ของ Gemini ซึ่งออกแบบมาสำหรับแอปพลิเคชันแบบ Agent ทักษะนี้ครอบคลุมสิ่งต่อไปนี้

- การสร้างข้อความ การแชทหลายรอบ และการสตรีม
- การเรียกใช้ฟังก์ชัน เอาต์พุตที่มีโครงสร้าง และการสร้างรูปภาพ
- การดำเนินการในเบื้องหลังและ Agent ของ Deep Research
- การจัดการสถานะการสนทนาฝั่งเซิร์ฟเวอร์
- รูปแบบ SDK ของ Python และ TypeScript

#### ติดตั้งด้วย skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### ติดตั้งด้วย Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## ยืนยันการติดตั้ง

หลังจากติดตั้งแล้ว ให้ยืนยันว่าผู้ช่วยเขียนโค้ดของคุณเชื่อมต่อกับเซิร์ฟเวอร์ Gemini Docs MCP และใช้ทักษะที่คุณติดตั้งไว้ได้

### 1. ยืนยันลักษณะการทำงานของ Agent

วิธีที่เชื่อถือได้มากที่สุดในการยืนยันคือการถามคำถามทางเทคนิคเกี่ยวกับ Gemini API กับ Agent

**พรอมต์:** "ฉันจะใช้การแคชบริบทกับ Gemini API ได้อย่างไร"

การตั้งค่าที่สำเร็จจะมีลักษณะดังนี้

- **ให้โค้ดที่ถูกต้อง**: อ้างอิงเมธอดเฉพาะของ Gemini เช่น `cacheContent` หรือ `cachedContents.create` จากปลายทางล่าสุด
- **ใช้เครื่องมือ MCP**: แสดงว่าเครื่องมือเชื่อมต่อกับ **เซิร์ฟเวอร์ Gemini Docs MCP** หรือใช้เครื่องมือ `search_documentation` เพื่อดึงข้อมูล
- **เรียกใช้ทักษะที่โหลดไว้**: แสดงตัวบ่งชี้ว่า "กำลังใช้ทักษะ: gemini-api-dev" (หากใช้ Wrapper รอง)

### 2. ยืนยันการแสดงและเครื่องมือ

หาก Agent ให้คำตอบทั่วไป ให้ใช้คำสั่ง Discovery หรือ Status เฉพาะสำหรับสภาพแวดล้อมของคุณเพื่อยืนยันว่าได้โหลด Docs MCP หรือทักษะลงในหน่วยความจำแล้ว

| สภาพแวดล้อม | การยืนยัน MCP | การยืนยันทักษะ |
| --- | --- | --- |
| **Claude Code** | พิมพ์ `/mcp` ในเทอร์มินัลเพื่อดูเซิร์ฟเวอร์ที่ใช้งานอยู่และเครื่องมือ `search_documentation` | พิมพ์ `/skills` ในเทอร์มินัลเพื่อแสดงรายการการแสดงทั้งหมดที่ใช้งานอยู่ |
| **Cursor** | ไปที่**การตั้งค่า > ฟีเจอร์ > MCP** ตรวจสอบว่าเซิร์ฟเวอร์ "เชื่อมต่อแล้ว" | เปิด**การตั้งค่า > กฎ** ตรวจสอบว่าทักษะปรากฏในส่วน "Agent ตัดสินใจ" |
| **Antigravity** | ตรวจสอบแถบด้านข้าง**การปรับแต่ง > การเชื่อมต่อ** เพื่อดูสถานะ MCP | พิมพ์ `/skills list` หรือตรวจสอบแถบด้านข้าง**การปรับแต่ง > กฎ** |
| **Gemini CLI** | เรียกใช้ `gemini mcp list` หรือใช้ `/mcp list` | เรียกใช้ `gemini skills list` หรือใช้คำสั่งเครื่องหมายทับ `/skills` ในเซสชัน |
| **Copilot** | พิมพ์ `@gemini /mcp` เพื่อแสดงรายการเครื่องมือเชื่อมต่อข้อมูลที่ใช้งานอยู่ | พิมพ์ `@gemini /skills` (หรือ `/skills`) เพื่อดูส่วนขยายที่ใช้งานอยู่ |

## การแก้ปัญหา

หาก Agent ให้ข้อมูลทั่วไปเท่านั้นหรือจดจำเมธอดเฉพาะของ Gemini ไม่ได้ ให้ตรวจสอบสิ่งต่อไปนี้

### Agent ไม่พบทักษะ

Agent ส่วนใหญ่จะจัดทำดัชนีทักษะเมื่อเริ่มต้นเท่านั้น

**วิธีแก้ไข:** รีสตาร์ท IDE (Cursor/VS Code) อย่างสมบูรณ์ หรือออกจาก Agent ที่ใช้เทอร์มินัล (Claude Code) แล้วเปิดอีกครั้ง

### ความขัดแย้งส่วนกลางกับส่วนท้องถิ่น

หากคุณติดตั้งด้วยแฟล็ก `--global` Agent อาจละเว้นแฟล็กนี้และใช้กฎเฉพาะของโปรเจ็กต์แทน

**วิธีแก้ไข:** ลองติดตั้งทักษะลงในรูทของโปรเจ็กต์โดยตรงโดยไม่ใช้แฟล็กส่วนกลาง

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## แหล่งข้อมูล

- [ทักษะ Gemini API ใน GitHub](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=th)
- [การเริ่มต้นอย่างรวดเร็ว](https://ai.google.dev/gemini-api/docs/quickstart?hl=th)
- [ไลบรารี](https://ai.google.dev/gemini-api/docs/libraries?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-04-29 UTC"],[],[]]
