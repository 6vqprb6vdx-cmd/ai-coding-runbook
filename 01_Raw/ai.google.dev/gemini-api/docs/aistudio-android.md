---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=th
fetched_at: 2026-06-01T19:49:06.055874+00:00
title: "\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e41\u0e2d\u0e1b Android \u0e43\u0e19 Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# สร้างแอป Android ใน Google AI Studio

Google AI Studio ช่วยให้คุณสร้างแอป Android แบบเนทีฟจากพรอมต์ภาษาธรรมชาติได้ อธิบายแอปที่คุณต้องการ แล้ว[Antigravity Agent](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=th#antigravity-agent)
จะสร้างโปรเจ็กต์ Kotlin และ [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=th)
ที่สมบูรณ์ จากเบราว์เซอร์ คุณสามารถดูตัวอย่างแอปในโปรแกรมจำลอง Android ที่ใช้เบราว์เซอร์ ติดตั้งแอปในอุปกรณ์จริง และเผยแพร่แอปเพื่อทดสอบ

## เริ่มต้นใช้งาน

วิธีเริ่มสร้างแอป Android

1. ไปที่[โหมดสร้าง](https://aistudio.google.com/apps?hl=th)ใน Google AI Studio โดยใช้แผงการนำทางด้านซ้าย
2. เลือก **Android** จากเครื่องมือเลือกแพลตฟอร์ม
3. ป้อนพรอมต์ที่อธิบายแอปที่คุณต้องการสร้าง (เช่น *"สร้างเครื่องมือติดตามงานประจำวันด้วยพื้นที่เก็บข้อมูลในเครื่อง"* หรือ *"สร้างเครื่องคิดเลขอย่างง่าย"*)
4. Agent จะสร้างโปรเจ็กต์และเปิดใช้ในโปรแกรมจำลอง Android บนเบราว์เซอร์

จากนั้นคุณจะทำซ้ำแอปโดยใช้แผงแชทได้เช่นเดียวกับประสบการณ์การใช้งานบนเว็บ
Agent จะจัดการไฟล์ทั้งหมดในโปรเจ็กต์ Android และเผยแพร่
การเปลี่ยนแปลงในฐานของโค้ด

## โปรแกรมจำลอง Android บนเบราว์เซอร์

โปรแกรมจำลอง Android ทำงานในระบบคลาวด์ทั้งหมดและสตรีมไปยังเบราว์เซอร์ของคุณ
คุณไม่จำเป็นต้องติดตั้ง Android SDK, Android Studio หรือโปรแกรมจำลองในเครื่อง

โปรแกรมจำลองมีฟีเจอร์ต่อไปนี้

- **การจำลองอุปกรณ์ที่คล้าย Pixel**: แตะ เลื่อน และโต้ตอบกับแอป
  เหมือนกับในอุปกรณ์จริง
- **รองรับการหมุน**: สลับระหว่างการวางแนวตั้งและแนวนอน
- **การแสดงตัวอย่างแบบเรียลไทม์**: เมื่อเอเจนต์ทำการเปลี่ยนแปลงโค้ด แอปจะสร้างใหม่และ
  โปรแกรมจำลองจะรีเฟรชโดยอัตโนมัติ

### ข้อจำกัดของโปรแกรมจำลอง

โปรแกรมจำลองที่ใช้เบราว์เซอร์ไม่รองรับฟีเจอร์ฮาร์ดแวร์ทั้งหมด สิ่งต่อไปนี้ไม่พร้อมใช้งานในโปรแกรมจำลอง

- การจับภาพด้วยกล้องและรูปภาพ
- NFC และบลูทูธ
- GPS (จำลองตำแหน่ง)
- บริการ Google Play (Google Sign-In, Maps และฟีเจอร์อื่นๆ ของบริการ Play
  จะทำงานในอุปกรณ์จริง แต่ไม่ทำงานในโปรแกรมจำลอง)

## ติดตั้งในอุปกรณ์ที่มี ADB

คุณติดตั้ง APK ที่สร้างขึ้นโดยตรงบนอุปกรณ์ Android จริงที่เชื่อมต่อกับคอมพิวเตอร์ผ่าน USB ได้ ซึ่งใช้ [WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=th) เพื่อสื่อสารกับอุปกรณ์ผ่านเบราว์เซอร์ ไม่จำเป็นต้องติดตั้ง ADB ในเครื่อง

### ข้อกำหนดเบื้องต้น

- เบราว์เซอร์ Chrome หรือ Edge ที่รองรับ WebUSB
- อุปกรณ์ Android ที่เปิดใช้[ตัวเลือกสำหรับนักพัฒนาแอปและการแก้ไขข้อบกพร่อง USB](https://developer.android.com/studio/debug/dev-options?hl=th)
- สาย USB ที่เชื่อมต่ออุปกรณ์กับคอมพิวเตอร์

### ติดตั้งแอปในอุปกรณ์

1. คลิก**ติดตั้งในอุปกรณ์**ในแผงแสดงตัวอย่าง
2. เลือกอุปกรณ์ Android จากเครื่องมือเลือกอุปกรณ์ USB ของเบราว์เซอร์
3. ระบบจะโอนและติดตั้ง APK ในอุปกรณ์
4. แอปจะเปิดขึ้นโดยอัตโนมัติ

## เผยแพร่ไปยัง Play Store

คุณสามารถเผยแพร่แอป Android ไปยังแทร็กการทดสอบภายในของ [Google Play Console](https://play.google.com/console?hl=th) ซึ่งจะช่วยให้คุณจัดจำหน่ายแอปไปยังผู้ทดสอบได้สูงสุด 100 คน

### ข้อกำหนดเบื้องต้น

- [บัญชีนักพัฒนาแอป Google Play](https://play.google.com/console/signup?hl=th)
  (ต้องชำระค่าลงทะเบียน $25 แบบครั้งเดียว)
- โปรไฟล์นักพัฒนาแอปที่กรอกข้อมูลครบถ้วนใน Play Console

### เผยแพร่แอป

1. เปิด**การตั้งค่า > เผยแพร่**ใน Google AI Studio
2. คลิก**เผยแพร่ไปยัง Play Store**
3. ตรวจสอบสิทธิ์ด้วยบัญชีนักพัฒนาแอป Google Play
4. AI Studio จะลงนามใน APK, สร้างข้อมูลแอป (หรืออัปโหลดเวอร์ชันใหม่)
   และเผยแพร่ไปยังแทร็กการทดสอบภายใน
5. คุณจะได้รับลิงก์เพื่อแชร์กับผู้ทดสอบ

AI Studio จะจัดการการลงนาม APK โดยอัตโนมัติโดยใช้ที่เก็บคีย์ที่จัดการ คุณปรับแต่งข้อมูลแอป (ไอคอน ภาพหน้าจอ คำอธิบาย) ได้ในภายหลังใน Play Console

## สิ่งที่สร้างขึ้น

เมื่อคุณสร้างแอป Android เอเจนต์จะสร้างโปรเจ็กต์มาตรฐานที่ใช้ Gradle โดยมีโครงสร้างดังนี้

- **การกำหนดค่าบิลด์**: ไฟล์ `build.gradle.kts` (ระดับโปรเจ็กต์และแอป)
  โดยใช้ Kotlin DSL
- **เลเยอร์ UI**: คอมโพเนนต์ [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=th) ที่มีธีม [Material 3](https://m3.material.io/)
- **สถาปัตยกรรม**: สถาปัตยกรรมแบบกิจกรรมเดียวที่มี ViewModel และคลาสข้อมูล
- **ทรัพยากร**: `AndroidManifest.xml`, Drawable, สตริง และทรัพยากรอื่นๆ ของ Android

เอเจนต์จะจัดการทรัพยากร Dependency ของ Gradle โดยอัตโนมัติ และเพิ่มแพ็กเกจจากที่เก็บ Maven
และ Google ตามที่จำเป็น

คุณดูและแก้ไขโค้ดที่สร้างขึ้นได้โดยใช้แท็บ**โค้ด**ในแผงแสดงตัวอย่าง
หากต้องการพัฒนาต่อใน Android Studio ให้ดาวน์โหลดโปรเจ็กต์เป็น**ไฟล์ ZIP**

## ข้อจำกัด

การสร้างแอป Android ใน AI Studio มีข้อจำกัดต่อไปนี้

### ข้อจำกัดของแพลตฟอร์ม

- **ฝั่งไคลเอ็นต์เท่านั้น**: แอป Android ไม่มีคอมโพเนนต์ฝั่งเซิร์ฟเวอร์
  ฟีเจอร์ที่ต้องใช้รันไทม์ของเซิร์ฟเวอร์ (การจัดการลับ, ผู้เล่นหลายคน,
  Firebase, Google Workspace API) จะไม่พร้อมใช้งาน
- **สถาปัตยกรรมแบบกิจกรรมเดียว**: รองรับเฉพาะโปรเจ็กต์แบบกิจกรรมเดียวและโมดูลเดียว
- **Jetpack Compose เท่านั้น**: แอปใช้ Kotlin และ Jetpack Compose ไม่รองรับเลย์เอาต์ Java และ XML
- **ไม่มี NDK หรือโค้ดแบบเนทีฟ**: ไม่รองรับโค้ด C และ C++
- **ไม่มี Wear OS หรือ Android TV**: รองรับเฉพาะรูปแบบของโทรศัพท์และแท็บเล็ต

### ข้อจำกัดในการส่งออก

- **ดาวน์โหลด ZIP เท่านั้น**: คุณสามารถดาวน์โหลดโปรเจ็กต์เป็นไฟล์ ZIP ได้ การส่งออก GitHub ยังไม่พร้อมให้บริการสำหรับโปรเจ็กต์ Android

## ขั้นตอนถัดไป

- [สร้างแอปใน Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=th)
- [การพัฒนาแอปแบบ Full Stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=th) (เว็บ)
- ดูตัวอย่างได้ใน [App Gallery](https://aistudio.google.com/apps?source=showcase&hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-19 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-19 UTC"],[],[]]
