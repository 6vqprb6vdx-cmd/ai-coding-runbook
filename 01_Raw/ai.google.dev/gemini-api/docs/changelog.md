---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=th
fetched_at: 2026-11-02T07:18:57.291546+00:00
title: "\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e1b\u0e23\u0e30\u0e08\u0e33\u0e23\u0e38\u0e48\u0e19 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# บันทึกประจำรุ่น

หน้านี้มีบันทึกการอัปเดตของ Gemini API

## 30 ตุลาคม 2569

- **การใช้คอมพิวเตอร์เวอร์ชันสำหรับผู้ใช้ทั่วไป (GA)**: เปิดตัวเครื่องมือ[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)ให้พร้อมใช้งานในเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ใน Interactions API และ GenerateContent API

## 27 ตุลาคม 2026

- **Gemini API CLI (`gemini-api`) เวอร์ชันเบต้า**: เปิดตัว [Gemini API CLI](https://ai.google.dev/gemini-api/docs/cli?hl=th) (`gemini-api`) ซึ่งเป็นไคลเอ็นต์บรรทัดคำสั่งแบบไม่เก็บสถานะและไม่มีทรัพยากร Dependency สำหรับเอเจนต์การเขียนโค้ด AI, สคริปต์ และไปป์ไลน์ CI ใช้ `gemini-api` ใน [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=th) เพื่อสร้างข้อความที่สร้างขึ้นและสื่อ วิเคราะห์ไฟล์ และเรียกใช้[ตัวแทนที่จัดการโดย Gemini](https://ai.google.dev/gemini-api/docs/agents?hl=th) ดู[คู่มือ CLI ของ Gemini API](https://ai.google.dev/gemini-api/docs/cli?hl=th) เพื่อเริ่มต้นใช้งาน

## 26 ตุลาคม 2026

- **เปิดใช้พื้นที่เก็บข้อมูล Generate Content API โดยค่าเริ่มต้น**: ตอนนี้โปรเจ็กต์ใหม่ที่ใช้ Generate Content API (`generateContent`, `streamGenerateContent` และ `batchGenerateContent`) ในระดับการใช้งานแบบชำระเงินจะจัดเก็บคำขอโดยค่าเริ่มต้น (`store=true`) ซึ่งตรงกับ Interactions API โปรเจ็กต์ที่มีอยู่จะใช้การตั้งค่าปัจจุบันต่อไป หากต้องการเลือกไม่ใช้ ให้ตั้งค่า `store=false` ในคำขอแต่ละรายการหรือปิดการบันทึก Generate Content API ในแผง**การตั้งค่า**ของแดชบอร์ด[บันทึกและชุดข้อมูล](https://aistudio.google.com/logs?hl=th) ดูรายละเอียดได้ที่[บันทึกและชุดข้อมูล](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=th#configure-logging)

## 13 ตุลาคม 2569

- **Gemini 4 Argon (`gemini-4-argon`) เวอร์ชันสำหรับผู้ใช้ทั่วไป (GA)**: เปิดตัวแล้ว
  [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=th) (`gemini-4-argon`)
  โมเดลที่มากความสามารถที่สุดของเราซึ่งสร้างขึ้นสำหรับงานเขียนโค้ดที่ซับซ้อน งานที่ใช้ Agent งานคณิตศาสตร์ และงานวิทยาศาสตร์

  ดูการเปลี่ยนแปลงของ API, ราคา และคำแนะนำในการย้ายข้อมูลได้ที่[มีอะไรใหม่ใน Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/latest-model?hl=th)

## 8 ตุลาคม 2569

- **การเลิกใช้งาน Gemini 3.7 Flash**:
  [`gemini-3.7-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.7?hl=th) เลิกใช้งานแล้วและแทนที่ด้วย [`gemini-3.8-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=th)
  คุณไม่สามารถเลือกโมเดลนี้ใน Google AI Studio ได้อีกต่อไป และระบบจะกำหนดเส้นทางคำขอ API ไปยัง `gemini-3.7-flash` ไปยัง `gemini-3.8-flash` โดยอัตโนมัติ อัปเดตสตริงโมเดลเป็น `gemini-3.8-flash` และดู[คู่มือ Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=th)
- **การเลิกใช้งาน Gemini 3.5 Flash**:
  [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=th) เลิกใช้งานแล้วและแทนที่ด้วย [`gemini-3.6-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=th)
  คุณไม่สามารถเลือกโมเดลนี้ใน Google AI Studio ได้อีกต่อไป และระบบจะกำหนดเส้นทางคำขอ API ไปยัง `gemini-3.5-flash` ไปยัง `gemini-3.6-flash` โดยอัตโนมัติ อัปเดตสตริงโมเดลเป็น `gemini-3.6-flash` (หรือ [`gemini-3.8-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=th)) และดู[คู่มือ Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=th)
- **การเลิกใช้งาน Deep Research Agent `deep-research-pro-preview-12-2025`**:
  เราเลิกใช้งาน Agent `deep-research-pro-preview-12-2025` แล้ว และจะ[ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th#managed-agents)ในวันที่ **23 ตุลาคม 2026**

  ย้ายคำขอไปยัง Agent [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) เวอร์ชันใหม่กว่าเวอร์ชันใดเวอร์ชันหนึ่งต่อไปนี้

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=th):
    ออกแบบมาเพื่อความเร็วและประสิทธิภาพ เหมาะสำหรับการสตรีมกลับไปยัง UI ของไคลเอ็นต์
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=th):
    ความครอบคลุมสูงสุดสำหรับการรวบรวมและสังเคราะห์บริบทแบบอัตโนมัติ

  หากต้องการย้ายข้อมูล ให้อัปเดตพารามิเตอร์ `agent` ในคำขอ `interactions.create` จาก `deep-research-pro-preview-12-2025` เป็น `deep-research-preview-04-2026` (หรือ `deep-research-max-preview-04-2026`)

## 6 ตุลาคม 2569

- **Gemini Nano Banana 2.1 เวอร์ชันสำหรับผู้ใช้ทั่วไป (GA)**: เปิดตัว
  [Gemini Nano Banana 2.1](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1?hl=th)
  (`gemini-nano-banana-2.1`) โมเดลการสร้างรูปภาพและการแก้ไขโดยใช้การสนทนาที่มีประสิทธิภาพสูงล่าสุด การอัปเดต Nano Banana 2
  ([`gemini-3.1-flash-image`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=th))
  ยังคงรักษาความเร็วและประสิทธิภาพด้านต้นทุนในระดับ Flash ไว้ได้ พร้อมทั้งปรับปรุงคุณภาพของภาพ การทำตามพรอมต์ ความสม่ำเสมอของตัวละครแบบหลายเทิร์น การแสดงผลข้อความ และการสร้างสัดส่วนภาพแบบกว้างและพาโนรามา (`1:4`, `4:1`, `1:8`, `8:1`) ในความละเอียด `1K`, `2K` และ `4K`

  ดู[คู่มือการสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)เพื่อเริ่มต้นใช้งาน
- **ประกาศการเลิกใช้งาน**: โมเดล `gemini-3.1-flash-image` เลิกใช้งานแล้ว (ไม่มีการประกาศวันที่ปิดตัว) ย้ายข้อมูลไปยัง [`gemini-nano-banana-2.1`](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1?hl=th)

## 22 กันยายน 2569

- **Gemini 3.8 Flash TTS และ Gemini 3.8 Flash-Lite TTS พร้อมให้บริการเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA)**: เปิดตัวโมเดลเสียงการอ่านออกเสียงข้อความ (TTS) รุ่นถัดไปและปลายทาง Gemini API Voices (`/v1beta/voices`) ดังนี้

  - **[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=th)
    (`gemini-3.8-flash-tts`)**: โมเดล TTS เชิงสร้างสรรค์ที่โดดเด่นซึ่งออกแบบมาเพื่อความเที่ยงตรงของเสียงระดับสตูดิโอ การแสดงที่ละเอียดอ่อน ภาษาถิ่น และความเสถียรแบบหลายรอบในรูปแบบยาว
  - **[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=th)
    (`gemini-3.8-flash-lite-tts`)**: โมเดล TTS ที่รวดเร็วและคุ้มค่าซึ่งสร้างขึ้นเพื่อแทนที่ `gemini-3.1-flash-tts-preview` สำหรับการใช้งานจริงที่มีอัตราการส่งข้อมูลสูงและการส่งต่อข้อมูลแบบเรียลไทม์ของ Voice Agent
  - **[การออกแบบเสียง](https://ai.google.dev/gemini-api/docs/voice-design?hl=th),
    [การจำลองเสียง](https://ai.google.dev/gemini-api/docs/voice-replication?hl=th) และ
    [คลังเสียงเพิ่มเติม](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th#voice-library)**:
    สร้างตัวตนเสียงที่กำหนดเองแบบถาวรจากพรอมต์ข้อความ จำลองเสียงด้วยการยืนยันความยินยอม และค้นหาเสียงที่สร้างไว้ล่วงหน้าและเสียงที่กำหนดเองมากกว่า 150 เสียง

  ดู[คู่มือการอ่านออกเสียงข้อความ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)เพื่อเริ่มต้นใช้งาน

## 18 กันยายน 2026

- **การอัปเดตสิทธิ์เข้าถึงโมเดล Gemini 2.5**: เพื่อให้ทุกคนได้รับประสิทธิภาพที่เชื่อถือได้ เราจึงจำกัดสิทธิ์เข้าถึงโมเดล 2.5 ไว้สำหรับผู้ใช้ที่เคยใช้งานโมเดลเหล่านี้อย่างสม่ำเสมอ โมเดลเหล่านี้ยังไม่เลิกใช้งานและจะยังคงแสดงต่อไปจนกว่าจะมีประกาศเพิ่มเติมผ่าน API สำหรับโปรเจ็กต์ใหม่ๆ ให้ใช้โมเดลล่าสุดของเรา ซึ่งได้แก่ 3.5 Flash-Lite หรือ 3.8 Flash ซึ่งจะช่วยให้เราคงความสามารถในการรองรับเวิร์กโฟลว์เดิมที่ดำเนินอยู่และแอปพลิเคชันใหม่ได้อย่างเพียงพอ

## 17 กันยายน 2569

- **Agent ของ Antigravity 09-2026**: เปิดตัว `antigravity-preview-09-2026` ซึ่งจะมาแทนที่และเลิกใช้งาน `antigravity-preview-05-2026`

  หากคุณเรียกใช้ในแซนด์บ็อกซ์ระยะไกล (`environment: "remote"`) และอ่านเฉพาะขั้นตอน `output_text` หรือ `model_output` ให้อัปเดตสตริง Agent โดยไม่มีการเปลี่ยนแปลงอื่นๆ

  หากคุณเรียกใช้เครื่องมือในเครื่อง (`local_environment`) หรือแยกวิเคราะห์ขั้นตอน `function_call` เครื่องมือในตัวจะเปลี่ยนไป พารามิเตอร์ใช้ PascalCase แทน snake\_case และการแก้ไขไฟล์ใช้การแทนที่ช่วงบรรทัดแทนการเขียนใหม่ทั้งหมด

  | ความสามารถ | 05-2026 | 09-2026 |
  | --- | --- | --- |
  | การสร้างไฟล์ | `write_file(path, content)` | `write_to_file(TargetFile, CodeContent, Overwrite, Description)` |
  | การแก้ไขไฟล์ | `write_file(path, content)` เขียนใหม่ทั้งหมด | `replace_file_content(TargetFile, StartLine, EndLine, TargetContent, ReplacementContent)` |
  | การอ่านไฟล์ | `read_file(path, offset, limit)`, ออฟเซ็ตไบต์ | `view_file(AbsolutePath, StartLine, EndLine, ContentOffset)` |
  | รายการไดเรกทอรี | `list_files(path)` | `list_dir(DirectoryPath)` |
  | การค้นหาไฟล์และ Code Search | ไม่มี ตัวแทนใช้คำสั่ง Shell | `find_by_name(SearchDirectory, Pattern, MaxDepth)` และ `grep_search(SearchPath, Query, IsRegex)` |
  | การดำเนินการ Shell | `code_execution(command, timeout_seconds)` | ไม่มีการเปลี่ยนแปลง |
  | ค้นเว็บ | `google_search(queries)` | ไม่มีการเปลี่ยนแปลง |

  ดูคู่มือ [Agent ของ Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th)
  `antigravity-preview-05-2026` จะปิดให้บริการในวันที่ 5 ตุลาคม 2569 โดยติดตามได้ในหน้า[การเลิกใช้งาน](https://ai.google.dev/gemini-api/docs/deprecations?hl=th#managed-agents)

## 15 กันยายน 2569

- **Gemini 3.8 Live และ Gemini 3.8 Live Extended Thinking พร้อมให้บริการโดยทั่วไป (GA)**: เปิดตัวโมเดลเสียงต่อเสียงใหม่ 2 โมเดลสำหรับแอปพลิเคชันเสียงแบบเรียลไทม์ที่ใช้ Live API ดังนี้

  - **Gemini 3.8 Live** ([`gemini-3.8-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=th)): ตัวเลือกเริ่มต้นสำหรับประสบการณ์การใช้งานเอเจนต์เสียงที่มีเวลาในการตอบสนองต่ำและการสนทนาแบบเรียลไทม์โดยไม่มีความล่าช้าในการให้เหตุผล มีฟีเจอร์การให้เหตุผลแบบสลับกัน การเรียกใช้ฟังก์ชันแบบอะซิงโครนัสโดยค่าเริ่มต้น และการอัปเดตเนื้อหาไคลเอ็นต์แบบเต็มเซสชัน
  - **Gemini 3.8 Live Extended Thinking**
    ([`gemini-3.8-live-extended-thinking`](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=th)): โมเดลเสียงต่อเสียงที่มีการให้เหตุผลสูงซึ่งรองรับการให้เหตุผลในเบื้องหลังระหว่างการโต้ตอบด้วยเสียงแบบเรียลไทม์ แนะนำให้ใช้เมื่อต้องการการให้เหตุผลในเบื้องหลังที่สูงขึ้น

  หากต้องการเริ่มต้นใช้งาน โปรดดู[คู่มือ Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th), [คู่มือความสามารถ](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=th) และ[คู่มือการคิด](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=th)

## 3 กันยายน 2569

- **Lyria 3.5 เวอร์ชันสำหรับผู้ใช้ทั่วไป (GA)**: เปิดตัวโมเดลการสร้างเพลงรุ่นถัดไปของ Google

  - [`lyria-3.5`](https://ai.google.dev/gemini-api/docs/models/lyria-3.5?hl=th):
    การสร้างเพลงแบบเต็มเพลงที่มีความสอดคล้องกันทางดนตรีที่ดีขึ้น เสียงร้องที่เป็นธรรมชาติ รวมถึงการควบคุมระยะเวลาและโครงสร้างที่ละเอียด

  โมเดลนี้รองรับอินพุตข้อความและรูปภาพ และสร้างเสียงสเตอริโอ 44.1 kHz ที่มีความแม่นยำสูง ดูรายละเอียดและตัวอย่างโค้ดได้ในคู่มือ[การสร้างเพลง](https://ai.google.dev/gemini-api/docs/music-generation?hl=th)

## 2 กันยายน 2569

- **Gemini 3.8 Flash พร้อมให้บริการเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA)**: เปิดตัว `gemini-3.8-flash` ซึ่งเป็นโมเดล Flash ที่ชาญฉลาดที่สุดของเรา ออกแบบมาสำหรับวิศวกรรมซอฟต์แวร์ระยะยาว เอเจนต์อัตโนมัติ และเวิร์กโฟลว์ที่ซับซ้อนขององค์กร

  หากต้องการเริ่มต้นใช้งาน โปรดดูหน้าโมเดล [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=th) และ[คู่มือ Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=th)

## 1 กันยายน 2569

- **ความเข้าใจวิดีโอแบบ Agentic**: เปิดตัวความเข้าใจวิดีโอแบบ Agentic สำหรับ Gemini 3.7 Flash, 3.6 Flash และ 3.5 Flash-Lite ใน Interactions API และ GenerateContent API โมเดลจะไปยังส่วนต่างๆ ของไทม์ไลน์วิดีโอแบบไดนามิก โดยขอข้อความถอดเสียง เฟรม หรือแทร็กเสียงตามต้องการ แนวทางนี้ใช้โทเค็นน้อยลงสูงสุด 88% สำหรับเนื้อหาแบบยาวเมื่อเทียบกับการประมวลผลแบบคงที่

  หากต้องการเริ่มต้นใช้งาน โปรดดูคู่มือ[ความเข้าใจวิดีโอแบบ Agentic](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th#agentic-video-understanding)

## 27 สิงหาคม 2026

- **Gemini Omni Flash เวอร์ชันสำหรับผู้ใช้ทั่วไป (GA)**: เปิดตัวเมื่อวันที่ `gemini-omni-1.1-flash` เวอร์ชัน GA ของโมเดลการสร้างและตัดต่อวิดีโอแบบสนทนาที่รวดเร็ว รุ่นนี้มาพร้อมความสามารถใหม่ที่สำคัญดังนี้

  - **ส่วนขยายวิดีโอ**: ขยายวิดีโอที่มีอยู่ได้อย่างราบรื่นโดยสร้างความต่อเนื่องที่ส่วนท้ายของคลิปโดยใช้ `extend` หรือใช้พรอมต์โดยตรง
  - **การประมาณค่าในช่วง (เฟรมแรก + เฟรมสุดท้าย)**: สร้างวิดีโอที่เปลี่ยนระหว่างรูปภาพ 2 รูปโดยใช้งาน `image_to_video` ที่มีรูปภาพสูงสุด 2 รูป
  - **การควบคุมความละเอียด**: พารามิเตอร์ `resolution` ใหม่ใน `video_config` รองรับเอาต์พุต `360p`, `720p` (ค่าเริ่มต้น), `1080p` และ `4k`
    เอาต์พุต 1080p และ 4K สร้างขึ้นโดยใช้การเพิ่มความละเอียด

  เราจะเลิกใช้งานปลายทาง `gemini-omni-flash-preview` ที่มีอยู่ในวันที่ 30 กันยายน 2026

  หากต้องการเริ่มต้นใช้งาน โปรดดูหน้าโมเดล [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=th) และ[คู่มือ Omni](https://ai.google.dev/gemini-api/docs/omni?hl=th)

## 26 สิงหาคม 2026

- **Gemini 3.5 Transcribe พร้อมใช้งานสำหรับผู้ใช้ทั่วไป (GA)**: เปิดตัวโมเดลการแปลงเสียงพูดเป็นข้อความโดยเฉพาะ 2 โมเดลที่อิงตามความเข้าใจด้านเสียงของ Gemini ดังนี้

  - **Gemini 3.5 Transcribe** (`gemini-3.5-transcribe`): การแปลงเสียงพูดเป็นข้อความแบบไม่สตรีมมิงที่มีความแม่นยำสูงและเวลาในการตอบสนองต่ำ พร้อมการตรวจจับภาษาตามคำพูดในกว่า 85 ภาษา, การแยกเสียงผู้พูด, การประทับเวลาระดับคำ และการให้น้ำหนักคำศัพท์ที่กำหนดเอง (สูงสุด 1,000 คำ)
  - **Gemini 3.5 Transcribe Live** (`gemini-3.5-transcribe-live`):
    การแปลงเสียงพูดเป็นข้อความแบบสตรีมมิง 2 ทิศทางที่มีเวลาในการตอบสนองต่ำผ่าน WebSockets โดยใช้ Live API ซึ่งรองรับเหตุการณ์การถอดเสียงชั่วคราวและแบบสรุป โหมดการถอดเสียงอัจฉริยะ และกลยุทธ์การตรวจจับกิจกรรมเสียงพูด (VAD) หลายรายการ

  หากต้องการเริ่มต้นใช้งาน โปรดดู[คู่มือการถอดเสียงเป็นคำ](https://ai.google.dev/gemini-api/docs/transcribe?hl=th) [คู่มือ Live Transcribe](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=th) และ[หน้าโมเดล Gemini 3.5 Transcribe](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=th)

## 13 สิงหาคม 2026

- **Gemini 3.7 Flash พร้อมให้บริการเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA)**: เปิดตัวโมเดลที่ชาญฉลาดที่สุดของเราสำหรับการเขียนโค้ดและ Agent

  - **Gemini 3.7 Flash** (`gemini-3.7-flash`): การปรับปรุงที่สำคัญในด้านวิศวกรรมซอฟต์แวร์ การพัฒนาเว็บ และเวิร์กโฟลว์แบบ Agentic พร้อมให้บริการในราคาช่วงแนะนำจนถึงวันที่ 31 ธันวาคม 2026

  หากต้องการเริ่มต้นใช้งาน โปรดดูหน้าโมเดล [Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=th) และ[คู่มือโมเดลล่าสุด](https://ai.google.dev/gemini-api/docs/latest-model?hl=th)

## 30 กรกฎาคม 2569

- **Gemini Robotics ER 2 ในเวอร์ชันตัวอย่างแบบสาธารณะ**: เปิดตัวปลายทางโมเดลการให้เหตุผลแบบ Embodied ใหม่ 2 รายการสำหรับวิทยาการหุ่นยนต์ ได้แก่

  - `gemini-robotics-er-2-preview`: การให้เหตุผลเชิงพื้นที่ขั้นสูง, การเรียกใช้โค้ดแบบ Agentic, การจัดเรียงเครื่องมือแบบหลายขั้นตอน, การค้นหาช่วงเวลาในวิดีโอ, การแยกประเภทความคืบหน้า และการประสานงานของหุ่นยนต์หลายตัว
  - `gemini-robotics-er-2-streaming-preview`: เพิ่มประสิทธิภาพสำหรับการสตรีมข้อความแบบเรียลไทม์โดยใช้ Live API ซึ่งช่วยให้เอเจนต์หุ่นยนต์มีเวลาในการตอบสนองต่ำด้วยอินพุตเสียงและวิดีโอแบบ 2 ทิศทาง

  ปลายทางของโมเดลทั้ง 2 แบบรองรับอินพุตข้อความ รูปภาพ วิดีโอ และเสียง รวมถึงรองรับการเรียกใช้ฟังก์ชันที่มีลักษณะการทำงานแบบบล็อกสำหรับการดำเนินการของหุ่นยนต์จริง
  หากต้องการเริ่มต้นใช้งาน โปรดดู[ภาพรวม ER ของ Gemini Robotics](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=th) สำหรับกรณีการใช้งานการสตรีมแบบเรียลไทม์ โปรดดู[วิทยาการหุ่นยนต์ที่มีการสตรีม](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=th)
- **ประกาศการเลิกใช้งาน**: โมเดล `gemini-robotics-er-1.6-preview` จะ[ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 31 สิงหาคม 2026

## 21 กรกฎาคม 2026

- **Gemini 3.6 Flash และ Gemini 3.5 Flash-Lite พร้อมใช้งานสำหรับผู้ใช้ทั่วไป (GA)**:
  เปิดตัวโมเดล 3.x Flash เวอร์ชันล่าสุดที่เสถียรและพร้อมใช้งานจริง ดังนี้

  - **Gemini 3.6 Flash** (`gemini-3.6-flash`): มีประสิทธิภาพการใช้โทเค็นที่ดีขึ้น รวมถึงความสามารถในการเขียนโค้ด/การวางแผนแบบ Agentic ในราคาที่ต่ำกว่า 3.5 Flash ซึ่งช่วยแก้ปัญหาความคิดเห็นของนักพัฒนาซอฟต์แวร์เกี่ยวกับความละเอียดของเอาต์พุต
  - **Gemini 3.5 Flash-Lite** (`gemini-3.5-flash-lite`): ตัวเลือก Sub-Agent ที่มีเวลาในการตอบสนองต่ำและคุ้มค่าอย่างมาก ซึ่งออกแบบมาเพื่อการทำงานอัตโนมัติปริมาณมาก

  ดูข้อมูลเพิ่มเติมได้ที่[คู่มือ Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=th)
- **พารามิเตอร์ที่เลิกใช้งาน**: เลิกใช้งานพารามิเตอร์การสุ่มตัวอย่าง `temperature`, `top_p` และ `top_k` แล้ว ดูรายละเอียดได้ที่
  [คู่มือ Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=th#sampling-parameter-deprecation)

## 6 กรกฎาคม 2026

- การรองรับ[บันทึกของนักพัฒนาซอฟต์แวร์](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=th)สำหรับ Interactions API: ตอนนี้คุณสามารถดูบันทึกสำหรับการเรียก Interactions API ที่รองรับได้ใน[แดชบอร์ด AI Studio](https://aistudio.google.com/logs?hl=th)

## 30 มิถุนายน 2026

- **Gemini Omni Flash ในเวอร์ชันตัวอย่างแบบสาธารณะ**: เปิดตัวเมื่อวันที่ `gemini-omni-flash-preview` เป็นโมเดลหลายรูปแบบประสิทธิภาพสูงที่ออกแบบมาเพื่อการสร้างวิดีโอความเร็วสูงและการตัดต่อวิดีโอแบบสนทนา เมื่อใช้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) คุณจะสร้างวิดีโอความยาว 3-10 วินาทีที่ความละเอียด 720p จากคำอธิบายข้อความหรือสร้างภาพเคลื่อนไหวจากภาพนิ่งได้ จากนั้นก็แก้ไขและปรับแต่งเอาต์พุตได้ผ่านการสนทนา หากต้องการเริ่มต้นใช้งาน โปรดดูคู่มือ [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=th) และการ์ดโมเดล [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=th)
- เปิดตัว `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite) เป็นเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ซึ่งเป็นโมเดลหลายรูปแบบในตัวที่เพิ่มประสิทธิภาพเพื่อเวลาในการตอบสนองต่ำมาก รวมถึงโปรแกรมสร้างรูปภาพและแก้ไขรูปภาพที่คุ้มค่า ดูการ์ดโมเดล [Gemini 3.1 Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=th) และคู่มือ[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)

## 24 มิถุนายน 2026

- **การใช้คอมพิวเตอร์**: เปิดตัวการรองรับเวอร์ชันตัวอย่างแบบสาธารณะสำหรับเครื่องมือ[การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)ใน Gemini 3.5 Flash รุ่นนี้ประกอบด้วยการดำเนินการที่เรียบง่ายขึ้นด้วย Intent, การรองรับในตัวสำหรับสภาพแวดล้อมเบราว์เซอร์ อุปกรณ์เคลื่อนที่ และเดสก์ท็อป, นโยบายความปลอดภัยที่กำหนดค่าได้ และการตรวจจับการแทรกพรอมต์ขั้นสูง

## 17 มิถุนายน 2026

- **การรองรับสตรีมมิงสำหรับการสร้างคำพูด**: ตอนนี้โมเดล `gemini-3.1-flash-tts-preview` รองรับสตรีมมิงผ่าน `streamGenerateContent` (และ `stream: true` ใน Interactions API) แล้ว ดูข้อมูลเพิ่มเติมได้ที่คู่มือ[การอ่านออกเสียงข้อความ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th#streaming)

## 15 มิถุนายน 2026

- **ประกาศการเลิกใช้งาน**: เราจะเลิกใช้งานโมเดลการสร้างรูปภาพต่อไปนี้และจะ[ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ **17 สิงหาคม 2026**

  - **โมเดลรูปภาพ Imagen 4 และ Gemini 3**
    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

  หากต้องการย้ายข้อมูลโค้ดไปยังปลายทางเวอร์ชันตัวอย่างหรือเวอร์ชันเสถียรที่ใหม่กว่า โปรดดูหน้า[การเลิกใช้งาน Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=th#imagen-models)
- **ประกาศการเลิกใช้งาน**: เราจะเลิกใช้งานโมเดลการสร้างวิดีโอต่อไปนี้และจะ[ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ **30 มิถุนายน 2026**

  - **โมเดล Veo**
    - `veo-2.0-generate-001`
    - `veo-3.0-generate-001`
    - `veo-3.0-fast-generate-001`

  อัปเดตการผสานรวมเพื่อใช้รหัสโมเดลเวอร์ชันตัวอย่างของ Veo 3.1 (`veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`) หรือโมเดล 3.1 GA ที่พร้อมใช้งานผ่าน[แพลตฟอร์ม Gemini Enterprise Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=th) เพื่อหลีกเลี่ยงการหยุดชะงักของบริการ
- **ประกาศการเลิกใช้งาน**: เครื่องมือมุมมองภาพรวมของ GMP เวอร์ชันทดลอง (อินเทอร์เฟซแบบคงที่สำหรับเอาต์พุตการเชื่อมต่อแหล่งข้อมูลกับ Google Maps) จะ[ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ **15 มิถุนายน 2026**

## 1 มิถุนายน 2026

- โมเดล Gemini 2.0 ต่อไปนี้[ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)แล้ว

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  โปรดใช้ [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=th) หรือ [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) แทน

## 28 พฤษภาคม 2026

- เปิดตัว `gemini-3.1-flash-image` (Nano Banana 2) และ `gemini-3-pro-image` (Nano Banana Pro) ซึ่งเป็นโมเดลภาพแบบเนทีฟเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ได้แก่ [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=th) และ [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=th)
- **การรองรับการสร้างวิดีโอเป็นรูปภาพ**: ตอนนี้คุณสามารถส่งไฟล์วิดีโอ (ผ่านการอัปโหลดโดยตรงหรือเป็น URL สาธารณะของ YouTube) เป็นบริบทแบบหลายโมดัลพร้อมกับพรอมต์ข้อความเพื่อสร้างภาพปกคุณภาพสูง โปสเตอร์ภาพยนตร์แนวภาพยนตร์ หรืออินโฟกราฟิกสรุปได้แล้ว ฟีเจอร์นี้รองรับเฉพาะในรุ่น `gemini-3.1-flash-image` เท่านั้น ดูข้อมูลเพิ่มเติมได้ที่คู่มือ[การสร้างวิดีโอเป็นรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th#video-to-image)
- ประกาศการเลิกใช้งาน: โมเดล `gemini-3.1-flash-image-preview` และ `gemini-3-pro-image-preview` เลิกใช้งานแล้ว และจะ[ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 25 มิถุนายน 2026

## 25 พฤษภาคม 2026

- โมเดล `gemini-3.1-flash-lite-preview` [ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)แล้ว โปรดใช้ [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) แทน

## 19 พฤษภาคม 2026

- เปิดตัว `gemini-3.5-flash` ซึ่งเป็นเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ของ [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=th) โมเดลที่ชาญฉลาดที่สุดของเราเพื่อประสิทธิภาพระดับแนวหน้าที่ยั่งยืนในงานด้านเอเจนต์และการเขียนโค้ด ตอนนี้โมเดลนี้เป็นโมเดลที่อยู่เบื้องหลัง `gemini-flash-latest`
- เปิดตัว **Agent ที่ได้รับการจัดการใน Gemini API** ในเวอร์ชันตัวอย่างแบบสาธารณะ ซึ่งช่วยให้นักพัฒนาซอฟต์แวร์สามารถสร้างและติดตั้งใช้งาน Agent แบบเก็บสถานะและทำงานอัตโนมัติที่ทำงานในสภาพแวดล้อมแซนด์บ็อกซ์ Linux ที่โฮสต์โดย Google ซึ่งปลอดภัยและแยกต่างหาก ดูข้อมูลเพิ่มเติมได้ที่หน้า[ภาพรวม Agent](https://ai.google.dev/gemini-api/docs/agents?hl=th) และ[คู่มือเริ่มใช้งานฉบับย่อ](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th)
- เปิดตัว Agent ที่มีการจัดการ**ของ Antigravity** อเนกประสงค์ [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=th) ในเวอร์ชันตัวอย่างแบบสาธารณะ
  Agent ของ Antigravity สามารถวางแผน วิเคราะห์ เขียนและเรียกใช้โค้ด จัดการไฟล์ และท่องเว็บภายในคอนเทนเนอร์แซนด์บ็อกซ์ได้โดยอัตโนมัติ ดูตัวอย่างโค้ดและข้อกำหนดได้ในคู่มือ [Agent ของ Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th)

## 7 พฤษภาคม 2569

- เปิดตัว `gemini-3.1-flash-lite` ซึ่งเป็นเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ของ [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) ที่เพิ่มประสิทธิภาพด้านความเร็ว ขนาด และความคุ้มค่า
- ประกาศการเลิกใช้งาน: โมเดล `gemini-3.1-flash-lite-preview` จะเลิกใช้งานในวันที่ 11 พ.ค. 2026 และจะ[ปิดตัวลง](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 25 พฤษภาคม 2026

## 6 พฤษภาคม 2026

- **การเปลี่ยนแปลงที่ส่งผลกับส่วนอื่นในระบบที่กำลังจะเกิดขึ้น**: สคีมาคำขอและการตอบกลับ (`outputs` → `steps`) รวมถึงการกำหนดค่ารูปแบบเอาต์พุต (`response_format`) ของ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) กำลังจะมีการเปลี่ยนแปลง สคีมาใหม่จะกลายเป็นค่าเริ่มต้นในวันที่ **26 พฤษภาคม** และระบบจะนำสคีมาเดิมออกในวันที่ **8 มิถุนายน**
  ดูรายละเอียดได้จาก[คำแนะนำในการย้ายข้อมูล](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=th)

## 5 พฤษภาคม 2026

- อัปเดต**การค้นหาไฟล์**เพื่อรองรับการค้นหาแบบหลายโมดัล ตอนนี้คุณสามารถฝังและค้นหาผ่านรูปภาพได้โดยตรงโดยใช้โมเดล `gemini-embedding-2`
  ตอนนี้ข้อมูลเมตาของการอ้างอิงข้อมูลจะมี `media_id` สำหรับการอ้างอิงภาพและ `page_numbers` ที่ระบุแหล่งที่มาของข้อมูล ดูข้อมูลเพิ่มเติมได้ที่คู่มือ[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)

## 4 พฤษภาคม 2569

- เปิดตัวการรองรับ [Webhook](https://ai.google.dev/gemini-api/docs/webhooks?hl=th) ที่ขับเคลื่อนด้วยเหตุการณ์ใน Gemini API เพื่อแทนที่เวิร์กโฟลว์การโพลสำหรับ Batch API และการดำเนินการที่ใช้เวลานาน

## 30 เมษายน 2026

- โมเดล `gemini-robotics-er-1.5-preview` [ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)แล้ว โปรดใช้ [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=th) แทน

## 22 เมษายน 2026

- เปิดตัว `gemini-embedding-2` เป็นเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ดูข้อมูลเพิ่มเติมได้ที่หน้า[การฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th)

## 21 เมษายน 2026

- เปิดตัว Agent ของ [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) เวอร์ชันใหม่ที่มาพร้อมการวางแผนร่วมกัน การรองรับการแสดงข้อมูลผ่านภาพ การผสานรวมเซิร์ฟเวอร์ MCP และการค้นหาไฟล์ ดังนี้

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=th): ออกแบบมาเพื่อความเร็วและประสิทธิภาพ เหมาะสำหรับการสตรีมกลับไปยัง UI ของไคลเอ็นต์
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=th): ความครอบคลุมสูงสุดสำหรับการรวบรวมและสังเคราะห์บริบทแบบอัตโนมัติ

## 15 เมษายน 2569

- เปิดตัว [Gemini 3.1 Flash TTS เวอร์ชันตัวอย่าง](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=th) ซึ่งเป็นโมเดลการอ่านออกเสียงข้อความที่คุ้มค่า แสดงอารมณ์ได้ และควบคุมได้ อ่านเอกสารประกอบเกี่ยวกับ[การอ่านออกเสียงข้อความ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)เพื่อดูข้อมูลเพิ่มเติม

## 14 เมษายน 2026

- เปิดตัว `gemini-robotics-er-1.6-preview` โมเดลหุ่นยนต์ที่อัปเดตแล้ว
  ตอนนี้โมเดลมีความสามารถใหม่ๆ เช่น การอ่านเครื่องมือวัด ความสามารถในการให้เหตุผลเชิงพื้นที่และเชิงกายภาพที่ดียิ่งขึ้น ดูข้อมูลเพิ่มเติมได้ที่หน้า [Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=th) และ[บล็อก](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=th)
- ประกาศการเลิกใช้งาน: โมเดล `gemini-robotics-er-1.5-preview` จะ[ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 30 เมษายน 2026 เวลา 09:00 น. PST

## 2 เมษายน 2026

- เปิดตัว `gemma-4-26b-a4b-it` และ `gemma-4-31b-it` ซึ่งพร้อมให้ใช้งานใน [AI Studio](https://aistudio.google.com?hl=th) และผ่าน Gemini API โดยเป็นส่วนหนึ่งของการเปิดตัว [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=th)

## 1 เมษายน 2026

- เปิดตัวระดับการอนุมานแบบ[Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=th)และ[Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)ใหม่ ซึ่งมีตัวเลือกเพิ่มเติมสำหรับการเพิ่มประสิทธิภาพต้นทุนหรือเวลาในการตอบสนอง

## 31 มีนาคม 2026

- เปิดตัวเวอร์ชันตัวอย่างของ Veo 3.1 Lite [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=th) โมเดล[การสร้างวิดีโอ](https://ai.google.dev/gemini-api/docs/video?hl=th)ที่คุ้มค่าที่สุดของเรา ซึ่งออกแบบมาเพื่อการทำซ้ำอย่างรวดเร็วและการสร้างแอปพลิเคชันจำนวนมาก
- โมเดล `gemini-2.5-flash-lite-preview-09-2025` ปิดให้บริการแล้ว โปรดใช้ [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=th) แทน

## 26 มีนาคม 2026

- เปิดตัว [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=th) ซึ่งเป็นโมเดลเสียงต่อเสียง (A2A) ล่าสุดที่ออกแบบมาสำหรับการสนทนาแบบเรียลไทม์และแอปพลิเคชัน AI ที่เน้นเสียงเป็นหลัก อ่านเอกสารประกอบเกี่ยวกับ [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th) เพื่อเริ่มต้นใช้งาน

## 25 มีนาคม 2026

- เปิดตัวโมเดลการสร้างเพลง [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=th): [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=th) (คลิป 30 วินาที) และ [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=th) (เพลงเต็ม) ทั้ง 2 โมเดลรองรับอินพุตข้อความและรูปภาพ และสร้างเสียงสเตอริโอ 48kHz คุณภาพสูง ดูรายละเอียดและตัวอย่างโค้ดได้ในคู่มือ[การสร้างเพลง](https://ai.google.dev/gemini-api/docs/music-generation?hl=th)

## 23 มีนาคม 2026

- เปิดตัว[แพ็กเกจการเรียกเก็บเงินแบบชำระเงินล่วงหน้าและชำระเงินภายหลัง](https://ai.google.dev/gemini-api/docs/billing?hl=th)ใน AI Studio บัญชีที่มีอยู่อาจได้รับผลกระทบ โปรดอ่านเอกสารประกอบเกี่ยวกับ[การเรียกเก็บเงิน](https://ai.google.dev/gemini-api/docs/billing?hl=th)เพื่อดูข้อมูลเพิ่มเติม

## 18 มีนาคม 2026

- เปิดตัวฟีเจอร์ใหม่[การรวมเครื่องมือในตัวและการเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/tool-combination?hl=th) ซึ่งช่วยให้ใช้เครื่องมือในตัวของ Gemini ควบคู่ไปกับเครื่องมือการเรียกใช้ฟังก์ชันที่กำหนดเองในการเรียก API ครั้งเดียวได้
- ตอนนี้โมเดล Gemini 3 รองรับ[การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th#supported_models) แล้ว

## 16 มีนาคม 2026

- เปิดตัว[ระดับการใช้งาน](https://ai.google.dev/gemini-api/docs/billing?hl=th#about-billing)และ[วงเงินใช้จ่ายของบัญชีสำหรับการเรียกเก็บเงิน](https://ai.google.dev/gemini-api/docs/billing?hl=th#tier-spend-caps)ที่ปรับปรุงใหม่เพื่อประสบการณ์การเรียกเก็บเงินของผู้ใช้ที่ดียิ่งขึ้น

## 12 มีนาคม 2026

- เปิดตัว[ขีดจำกัดการใช้จ่ายระดับโปรเจ็กต์](https://ai.google.dev/gemini-api/docs/billing?hl=th#project-spend-caps)สำหรับการเรียกเก็บเงินใน AI Studio

## 10 มีนาคม 2026

- เปิดตัว `gemini-embedding-2-preview` ซึ่งเป็นโมเดลการฝังแบบหลายโมดัลโมเดลแรกของเรา
  โดยรองรับอินพุตข้อความ รูปภาพ วิดีโอ เสียง และ PDF ซึ่งจะแมปข้อมูลทุกรูปแบบลงในพื้นที่การฝังแบบรวม ดูข้อมูลเพิ่มเติมได้ที่[การฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th)
- ประกาศการเลิกใช้งาน: โมเดล `gemini-2.5-flash-lite-preview-09-2025` จะ[ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 31 มีนาคม 2026

## 9 มีนาคม 2026

- โมเดล Gemini 3 Pro เวอร์ชันตัวอย่าง[ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)แล้ว ตอนนี้ `gemini-3-pro-preview` ชี้ไปยัง [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th) แล้ว

## 3 มีนาคม 2026

- เปิดตัว Gemini 3.1 Flash-Lite เวอร์ชันตัวอย่าง ซึ่งเป็นโมเดล Flash-Lite รุ่นแรกในซีรีส์ Gemini 3 อ่าน[หน้าโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=th)เพื่อดูข้อมูลจำเพาะ การอัปเดตที่เฉพาะเจาะจง และคำแนะนำสำหรับนักพัฒนาซอฟต์แวร์

## 26 กุมภาพันธ์ 2026

- เปิดตัว Nano Banana 2, [Gemini 3.1 Flash Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=th) ซึ่งเป็นโมเดลประสิทธิภาพสูงที่เพิ่มประสิทธิภาพเพื่อความเร็วและกรณีการใช้งานปริมาณมาก
- ประกาศการเลิกใช้งาน: Gemini 3 Pro เวอร์ชันตัวอย่าง (`gemini-3-pro-preview`) จะ[ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 9 มีนาคม 2026

## 19 กุมภาพันธ์ 2026

- เปิดตัว [Gemini 3.1 Pro เวอร์ชันตัวอย่าง](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th) ซึ่งเป็นโมเดลเวอร์ชันล่าสุดในตระกูล Gemini 3 ซีรีส์ใหม่
- เปิดตัวปลายทาง `gemini-3.1-pro-preview-customtools` แยกต่างหาก ซึ่งจัดลำดับความสำคัญของเครื่องมือที่กำหนดเองได้ดีกว่าสำหรับผู้ใช้ที่สร้างด้วย Bash และเครื่องมือผสมกัน

## 18 กุมภาพันธ์ 2026

- ประกาศการเลิกใช้งาน: โมเดลต่อไปนี้จะ[ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 1 มิถุนายน 2026

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## 17 กุมภาพันธ์ 2026

- โมเดลต่อไปนี้[ปิดตัวลง](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## 29 มกราคม 2569

- เปิดตัวการรองรับเครื่องมือการใช้คอมพิวเตอร์ใน `gemini-3-pro-preview` และ `gemini-3-flash-preview`

## 21 มกราคม 2026

- เปลี่ยนชื่อแทน `latest`:

  - `gemini-pro-latest` เปลี่ยนเป็น `gemini-3-pro-preview` แล้ว
  - `gemini-flash-latest` เปลี่ยนเป็น `gemini-3-flash-preview` แล้ว

## 15 มกราคม 2026

- ประกาศการเลิกใช้งาน: โมเดลต่อไปนี้จะ[ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)ในวันที่ 17 กุมภาพันธ์ 2026

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- โมเดล `gemini-2.5-flash-image-preview` ปิดให้บริการแล้ว

## 14 มกราคม 2026

- โมเดล `text-embedding-004` [ปิดให้บริการ](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)แล้ว

## 13 มกราคม 2026

- เพิ่มความละเอียดเอาต์พุตระดับ 4K สำหรับ [Veo](https://ai.google.dev/gemini-api/docs/video?hl=th) และรองรับวิดีโอแนวตั้งในทุกความละเอียดมากขึ้น

## 12 มกราคม 2026

- เปิดตัวฟีเจอร์วงจรของโมเดล ตอนนี้โมเดลบางรายการจะระบุระยะของวงจรและไทม์ไลน์การเลิกใช้งาน ดูข้อมูลเพิ่มเติมได้ในเอกสารประกอบต่อไปนี้

  - [ระยะของโมเดล](https://ai.google.dev/api/generate-content?hl=th#ModelStatus)

## 8 มกราคม 2026

- เปิดตัวการรองรับที่เก็บข้อมูล Cloud Storage และ URL ที่รับรองล่วงหน้าของฐานข้อมูลสาธารณะและส่วนตัวเป็นแหล่งข้อมูลอินพุตสำหรับ Gemini API นอกจากนี้ ขนาดไฟล์สูงสุดยังเพิ่มขึ้นจาก 20 MB เป็น 100 MB ด้วย โปรดดูรายละเอียดที่[คู่มือวิธีการป้อนข้อมูลไฟล์](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=th)

## 19 ธันวาคม 2025

- เปิดตัวการเปลี่ยนแปลงที่ส่งผลกับส่วนอื่นในระบบสำหรับ Interactions API ใน v1beta ฟิลด์ `total_reasoning_tokens` ได้เปลี่ยนชื่อเป็น `total_thought_tokens` เพื่อให้สอดคล้องกับแนวคิด "ความคิด" ในโมเดลการคิดมากขึ้น

## 17 ธันวาคม 2025

- เปิดตัว Gemini 3 Flash Preview, `gemini-3-flash-preview` ซึ่งให้ประสิทธิภาพระดับแนวหน้าที่รวดเร็วเทียบเท่ากับโมเดลขนาดใหญ่กว่าในราคาที่ถูกกว่ามาก มาพร้อมความสามารถในการให้เหตุผลเชิงภาพและเชิงพื้นที่ที่อัปเกรดแล้ว รวมถึงความสามารถในการเขียนโค้ดแบบ Agent อ่านเอกสารประกอบเกี่ยวกับฟีเจอร์ใหม่ๆ ซึ่งรวมถึงรายการต่อไปนี้

  - [การตอบกลับฟังก์ชันแบบหลายโมดัล](https://ai.google.dev/gemini-api/docs/function-calling?hl=th#multimodal)
  - [การเรียกใช้โค้ดกับรูปภาพ](https://ai.google.dev/gemini-api/docs/code-execution?hl=th#images)

## 12 ธันวาคม 2025

- เปิดตัว `gemini-2.5-flash-native-audio-preview-12-2025`
  ซึ่งเป็นโมเดลเสียงแบบเนทีฟใหม่สำหรับ Live API การอัปเดตนี้จะปรับปรุงความสามารถของโมเดลในการจัดการเวิร์กโฟลว์ที่ซับซ้อน ดูข้อมูลเพิ่มเติมได้ที่[คู่มือ Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=th) และ[เสียงแบบเนทีฟของ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=th)

## 11 ธันวาคม 2025

- เปิดตัว Interactions API API นี้มีอินเทอร์เฟซแบบรวมสำหรับการโต้ตอบกับโมเดลและ Agent ของ Gemini ดูข้อมูลเพิ่มเติมได้ที่คู่มือ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th)
- เปิดตัว Agent ของ Gemini Deep Research ในเวอร์ชันตัวอย่าง ฟีเจอร์นี้สามารถวางแผน ดำเนินการ และสังเคราะห์ผลลัพธ์สำหรับงานวิจัยแบบหลายขั้นตอนได้โดยอัตโนมัติ ดูรายละเอียดได้ในคู่มือ [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th)

## 10 ธันวาคม 2025

- เปิดตัวการปรับปรุง[โมเดลการอ่านออกเสียงข้อความ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th), เวอร์ชันตัวอย่าง Gemini 2.5 Flash TTS (เพิ่มประสิทธิภาพเพื่อเวลาในการตอบสนองต่ำ) และเวอร์ชันตัวอย่าง Gemini 2.5 Pro TTS (เพิ่มประสิทธิภาพเพื่อคุณภาพ) ซึ่งรวมถึงการแสดงออกที่ดียิ่งขึ้น จังหวะที่แม่นยำ และการสนทนาที่ราบรื่น

## 9 ธันวาคม 2025

- โมเดล Gemini Live API ต่อไปนี้ปิดตัวลงแล้ว
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 5 ธันวาคม 2025

- การเรียกเก็บเงินสำหรับ Gemini 3 ในส่วน[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th) จะเริ่มในวันที่ 5 มกราคม 2026

## 4 ธันวาคม 2568

- ประกาศการเลิกใช้งาน: โมเดล `gemini-2.5-flash-image-preview` จะปิดตัวลงในวันที่ 15 มกราคม 2026

## 3 ธันวาคม 2025

- ประกาศการเลิกใช้งาน: โมเดล `text-embedding-004` จะปิดให้บริการในวันที่ 14 มกราคม 2026

## 20 พฤศจิกายน 2025

- เปิดตัว Gemini 3 Pro Image Preview, `gemini-3-pro-image-preview`, ซึ่งเป็นโมเดล Nano Banana เวอร์ชันถัดไป อ่านรายละเอียดเพิ่มเติมได้ที่หน้า[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)

## 18 พฤศจิกายน 2025

- เปิดตัวโมเดล Gemini 3 ซีรีส์แรกอย่าง `gemini-3-pro-preview` ซึ่งเป็นโมเดลการให้เหตุผลและความเข้าใจข้อมูลหลายรูปแบบที่ล้ำสมัย พร้อมความสามารถด้านการเขียนโค้ดและ Agent ที่ทรงพลัง

  นอกเหนือจากการปรับปรุงด้านความชาญฉลาดและประสิทธิภาพแล้ว
  Gemini 3 Pro เวอร์ชันตัวอย่างยังมีการเปลี่ยนแปลงลักษณะการทำงานใหม่ๆ ดังนี้

  - [ความละเอียดของสื่อ](https://ai.google.dev/gemini-api/docs/media-resolution?hl=th)
  - [ลายเซ็นความคิด](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=th)
  - [ระดับการคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th#thinking-levels)

  อ่าน[คู่มือนักพัฒนาซอฟต์แวร์ Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=th) เพื่อดูข้อมูลเกี่ยวกับการย้ายข้อมูล ฟีเจอร์ใหม่ และข้อมูลจำเพาะ

## 11 พฤศจิกายน 2025

- ประกาศการเลิกใช้งาน: ระบบจะปิดโมเดลต่อไปนี้

  - 12 พฤศจิกายน:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - 14 พฤศจิกายน:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## 10 พฤศจิกายน 2025

- โมเดลต่อไปนี้ปิดตัวลงแล้ว

  - `imagen-3.0-generate-002`

  โปรดใช้ [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=th#imagen-4) แทน ดูรายละเอียดเพิ่มเติมได้ที่[ตารางการเลิกใช้งาน Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)

## 6 พฤศจิกายน 2025

- เปิดตัว File Search API เป็นเวอร์ชันตัวอย่างแบบสาธารณะ ซึ่งช่วยให้นักพัฒนาซอฟต์แวร์สามารถอ้างอิงคำตอบตามข้อมูลของตนเองได้ อ่านข้อมูลเพิ่มเติมได้ที่หน้า[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)ใหม่

## 4 พฤศจิกายน 2025

- สำหรับ [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=th) จำนวนโทเค็นอินพุตสำหรับรูปภาพลดลงจาก 1,290 เป็น 258 ซึ่งช่วยลดค่าใช้จ่ายในการแก้ไขรูปภาพ
- ประกาศการเลิกใช้งาน: ระบบจะปิดโมเดลต่อไปนี้

  - 18 พฤศจิกายน:

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - 2 ธันวาคม:

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - 9 ธันวาคม:

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## 29 ตุลาคม 2025

- เปิดตัวเครื่องมือ[การบันทึกและชุดข้อมูล](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=th)ใหม่สำหรับ Gemini API

## 20 ตุลาคม 2025

- โมเดล Gemini Live API ต่อไปนี้ปิดตัวลงแล้ว

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  คุณใช้ `gemini-2.5-flash-native-audio-preview-09-2025` แทนได้
- ประกาศการเลิกใช้งาน: การปิดใช้งาน `gemini-2.0-flash-live-001` และ `gemini-live-2.5-flash-preview` จะมีผลในวันที่ 9 ธันวาคม 2025

## 17 ตุลาคม 2025

- **การเชื่อมต่อแหล่งข้อมูลกับ Google Maps** พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว ดูข้อมูลเพิ่มเติมได้ที่เอกสารประกอบ[การเชื่อมต่อแหล่งข้อมูลกับ Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)

## 15 ตุลาคม 2025

- เปิดตัวโมเดล [Veo 3.1 และ 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=th#veo-3.1) ในเวอร์ชันตัวอย่างแบบสาธารณะพร้อมฟีเจอร์ใหม่ๆ ดังนี้

  - กำลังขยายวิดีโอที่ Veo สร้างขึ้น
  - อ้างอิงรูปภาพสูงสุด 3 รูปเพื่อสร้างวิดีโอ
  - การระบุรูปภาพเฟรมแรกและเฟรมสุดท้ายเพื่อสร้างวิดีโอ

  การเปิดตัวครั้งนี้ยังเพิ่มตัวเลือกเพิ่มเติมสำหรับความยาววิดีโอเอาต์พุต Veo 3 ได้แก่ 4, 6 และ 8 วินาที
- ประกาศการเลิกใช้งาน: การปิดระบบสำหรับ `veo-3.0-generate-preview` และ `veo-3.0-fast-generate-preview` จะมีขึ้นในวันที่ 12 พฤศจิกายน 2025

## 7 ตุลาคม 2025

- เปิดตัว [Gemini 2.5 Computer Use เวอร์ชันตัวอย่าง](https://ai.google.dev/gemini-api/docs/computer-use?hl=th)

## 2 ตุลาคม 2025

- เปิดตัว Gemini 2.5 Flash Image GA: [การสร้างรูปภาพด้วย Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)

## 29 กันยายน 2025

- โมเดล Gemini 1.5 ต่อไปนี้ปิดตัวลงแล้ว
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 25 กันยายน 2025

- เปิดตัวโมเดล Gemini Robotics ER 1.5 ในเวอร์ชันตัวอย่าง ดู[ภาพรวมของวิทยาการหุ่นยนต์](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=th)เพื่อดูวิธีใช้โมเดลสำหรับแอปพลิเคชันวิทยาการหุ่นยนต์
- เปิดตัวโมเดลเวอร์ชันตัวอย่างต่อไปนี้

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  ดูรายละเอียดได้ที่หน้า[โมเดล](https://ai.google.dev/gemini-api/docs/models?hl=th)

## 23 กันยายน 2025

- เปิดตัว `gemini-2.5-flash-native-audio-preview-09-2025` ซึ่งเป็นโมเดลเสียงแบบเนทีฟใหม่สำหรับ Live API ที่มีการเรียกใช้ฟังก์ชันและการจัดการการตัดคำพูดที่ดียิ่งขึ้น ดูข้อมูลเพิ่มเติมได้ที่[คู่มือ Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=th) และ[เสียงแบบเนทีฟของ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-native-audio)

## 16 กันยายน 2025

- ประกาศการเลิกใช้งาน: โมเดลต่อไปนี้จะปิดให้บริการในเดือนตุลาคม 2025

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  ดูรายละเอียดเกี่ยวกับโมเดลการฝังล่าสุดได้ที่หน้า[การฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th)

## 10 กันยายน 2025

- เปิดตัวการรองรับ[โมเดลการฝังใน Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th#batch-embedding) และเพิ่ม Batch API ลงใน[ไลบรารีความเข้ากันได้กับ OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=th#batch) เพื่อให้เริ่มต้นใช้งานการค้นหาแบบกลุ่มได้ง่ายยิ่งขึ้น

## 9 กันยายน 2025

- เปิดตัว Veo 3 และ Veo 3 Fast เวอร์ชัน GA พร้อมราคาที่ถูกลงและตัวเลือกใหม่สำหรับสัดส่วนภาพ ความละเอียด และการกำหนดค่าเริ่มต้น (Seeding) อ่านข้อมูลเพิ่มเติมได้ใน[เอกสารประกอบของ Veo](https://ai.google.dev/gemini-api/docs/video?hl=th#model-features)

## 26 สิงหาคม 2025

- เปิดตัว [Gemini 2.5 Image Preview](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-image-preview) ซึ่งเป็นโมเดลการสร้างรูปภาพแบบเนทีฟล่าสุดของเรา

## 18 สิงหาคม 2025

- เปิดตัว[เครื่องมือบริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th) เป็นเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ซึ่งเป็นเครื่องมือสำหรับระบุ URL เป็นบริบทเพิ่มเติมให้กับพรอมต์ การรองรับการใช้บริบท URL กับโมเดล `gemini-2.0-flash`
  (พร้อมใช้งานในช่วงเวอร์ชันทดลอง) จะปิดให้บริการในอีก 1 สัปดาห์

## 14 สิงหาคม 2025

- เปิดตัวโมเดล Imagen 4 Ultra, Standard และ Fast เป็นเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ดูข้อมูลเพิ่มเติมได้ที่หน้า [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=th)

## 7 สิงหาคม 2025

- การตั้งค่า `allow_adult` ในการสร้างวิดีโอจากภาพเผยแพร่แล้วในภูมิภาคที่ถูกจำกัด ดูรายละเอียดได้ที่หน้า [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=th#veo-model-parameters)

## 31 กรกฎาคม 2025

- เปิดตัวการสร้างวิดีโอจากรูปภาพสำหรับโมเดล Veo 3 เวอร์ชันตัวอย่าง
- เปิดตัวโมเดล Veo 3 Fast เวอร์ชันตัวอย่าง
- ดูข้อมูลเพิ่มเติมเกี่ยวกับ Veo 3 ได้ที่หน้า [Veo](https://ai.google.dev/gemini-api/docs/video?hl=th)

## 22 กรกฎาคม 2025

- เปิดตัว `gemini-2.5-flash-lite` โมเดล Gemini 2.5 ที่รวดเร็ว ต้นทุนต่ำ และมีประสิทธิภาพสูง ดูข้อมูลเพิ่มเติมได้ที่ [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-lite)

## July 17, 2025

- เปิดตัว `veo-3.0-generate-preview` ซึ่งเป็นการอัปเดตล่าสุดของ Veo ที่เปิดตัวการสร้างวิดีโอพร้อมเสียง ดูข้อมูลเพิ่มเติมเกี่ยวกับ Veo 3 ได้ที่หน้า [Veo](https://ai.google.dev/gemini-api/docs/video?hl=th)
- เพิ่มขีดจำกัดอัตราคำขอสำหรับ Imagen 4 Standard และ Ultra ดูรายละเอียดเพิ่มเติมได้ที่หน้า[การจำกัดอัตราคำขอ](https://ai.google.dev/gemini-api/docs/rate-limits?hl=th)

## 14 กรกฎาคม 2025

- เปิดตัว `gemini-embedding-001` ซึ่งเป็นเวอร์ชันเสถียรของโมเดลการฝังข้อความ ดูข้อมูลเพิ่มเติมได้ที่[การฝัง](https://ai.google.dev/gemini-api/docs/embeddings?hl=th) เราจะเลิกใช้งานโมเดล `gemini-embedding-exp-03-07` ในวันที่ 14 สิงหาคม 2025

## 7 กรกฎาคม 2025

- เปิดตัวโหมดกลุ่มของ Gemini API จัดกลุ่มคำขอและส่งไปประมวลผลแบบอะซิงโครนัส ดูข้อมูลเพิ่มเติมได้ที่[โหมดกลุ่ม](https://ai.google.dev/gemini-api/docs/batch-mode?hl=th)

## 26 มิถุนายน 2025

- ตอนนี้โมเดลเวอร์ชันตัวอย่าง `gemini-2.5-pro-preview-05-06` และ `gemini-2.5-pro-preview-03-25` จะเปลี่ยนเส้นทางไปยังเวอร์ชันเสถียรล่าสุด `gemini-2.5-pro`
- `gemini-2.5-pro-exp-03-25` ปิดอยู่

## 24 มิถุนายน 2025

- เปิดตัวโมเดล Imagen 4 Ultra และ Standard เวอร์ชันตัวอย่าง ดูข้อมูลเพิ่มเติมได้ที่หน้า[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)

## 17 มิถุนายน 2025

- เปิดตัว `gemini-2.5-pro` ซึ่งเป็นเวอร์ชันเสถียรของโมเดลที่ทรงพลังที่สุดของเรา ซึ่งตอนนี้มาพร้อมกับการคิดแบบปรับเปลี่ยนได้ ดูข้อมูลเพิ่มเติมได้ที่ [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-pro) และ[การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th) `gemini-2.5-pro-preview-05-06`
  จะเปลี่ยนเส้นทางไปยัง `gemini-2.5-pro` ในวันที่ 26 มิถุนายน 2025
- เปิดตัว `gemini-2.5-flash` ซึ่งเป็นโมเดล 2.5 Flash ที่เสถียรโมเดลแรกของเรา ดูข้อมูลเพิ่มเติมได้ที่ [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash)
  เราจะเลิกใช้งาน `gemini-2.5-flash-preview-04-17` ในวันที่ 15 กรกฎาคม 2025
- เปิดตัว `gemini-2.5-flash-lite-preview-06-17` ซึ่งเป็นโมเดล Gemini 2.5 ที่มีประสิทธิภาพสูงและต้นทุนต่ำ ดูข้อมูลเพิ่มเติมได้ที่ [Gemini 2.5 Flash-Lite เวอร์ชันตัวอย่าง](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-lite)

## 5 มิถุนายน 2025

- เปิดตัว `gemini-2.5-pro-preview-06-05` ซึ่งเป็นโมเดลที่ทรงพลังที่สุดเวอร์ชันใหม่ของเราที่มาพร้อมกับการคิดแบบปรับเปลี่ยนได้ ดูข้อมูลเพิ่มเติมได้ที่[เวอร์ชันตัวอย่างของ Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-pro-preview-06-05) และ[การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)
  ระบบจะเปลี่ยนเส้นทาง `gemini-2.5-pro-preview-05-06` ไปยัง `gemini-2.5-pro` ในวันที่ 26 มิถุนายน 2025

## 27 พฤษภาคม 2025

- โมเดลการปรับแต่งที่พร้อมใช้งานล่าสุดอย่าง Gemini 1.5 Flash 001 ได้ปิดตัวลงแล้ว
  ระบบไม่รองรับการปรับแต่งในโมเดลใดๆ อีกต่อไป
  ดู[การปรับแต่งอย่างละเอียดด้วย Gemini API](https://ai.google.dev/gemini-api/docs/model-tuning?hl=th)

## 20 พ.ค. 2025

**การอัปเดต API:**

- เปิดตัวการรองรับ[การประมวลผลวิดีโอที่กำหนดเองล่วงหน้า](https://ai.google.dev/gemini-api/docs/video-understanding?hl=th#customize-video-processing)โดยใช้ช่วงการตัดคลิปและการสุ่มตัวอย่างอัตราเฟรมที่กำหนดค่าได้
- เปิดตัวการใช้เครื่องมือหลายอย่าง ซึ่งรองรับการกำหนดค่า[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)และ[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/grounding?hl=th) ในคำขอ `generateContent` เดียวกัน
- เปิดตัวการรองรับ[การเรียกใช้ฟังก์ชันแบบอะซิงโครนัส](https://ai.google.dev/gemini-api/docs/live-tools?hl=th#async-function-calling)ใน Live API
- เปิดตัว[เครื่องมือบริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th) เวอร์ชันทดลองเพื่อระบุ URL เป็นบริบทเพิ่มเติมสำหรับพรอมต์

**การอัปเดตโมเดล:**

- เปิดตัว `gemini-2.5-flash-preview-05-20` ซึ่งเป็นโมเดล[เวอร์ชันตัวอย่าง](https://ai.google.dev/gemini-api/docs/models?hl=th#model-versions)ของ Gemini ที่เพิ่มประสิทธิภาพด้านความคุ้มค่าและการคิดแบบปรับเปลี่ยนได้ ดูข้อมูลเพิ่มเติมได้ที่[เวอร์ชันตัวอย่างของ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-preview) และ[การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)
- เปิดตัวโมเดล [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-pro-preview-tts) และ [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-preview-tts) ซึ่งสามารถ[สร้างเสียงพูด](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)ด้วยผู้พูด 1 หรือ 2 คน
- เปิดตัวโมเดล `lyria-realtime-exp` ซึ่ง[สร้างเพลง](https://ai.google.dev/gemini-api/docs/music-generation?hl=th)แบบเรียลไทม์
- เปิดตัว `gemini-2.5-flash-preview-native-audio-dialog` และ `gemini-2.5-flash-exp-native-audio-thinking-dialog` ซึ่งเป็นโมเดล Gemini ใหม่สำหรับ Live API ที่มีความสามารถด้านเอาต์พุตเสียงแบบเนทีฟ ดูข้อมูลเพิ่มเติมได้ที่[คู่มือ Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=th#native-audio-output) และ[เสียงแบบเนทีฟของ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-native-audio)
- เปิดตัวเวอร์ชันตัวอย่างของ `gemma-3n-e4b-it` ซึ่งพร้อมใช้งานใน [AI Studio](https://aistudio.google.com?hl=th) และผ่าน Gemini API โดยเป็นส่วนหนึ่งของการเปิดตัว [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=th)

## 7 พฤษภาคม 2025

- เปิดตัว `gemini-2.0-flash-preview-image-generation` ซึ่งเป็นโมเดลเวอร์ชันตัวอย่างสำหรับการสร้างและแก้ไขรูปภาพ ดูข้อมูลเพิ่มเติมได้ที่[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)และ[การสร้างรูปภาพด้วย Gemini 2.0 Flash เวอร์ชันตัวอย่าง](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.0-flash-preview-image-generation)

## 6 พฤษภาคม 2025

- เปิดตัว `gemini-2.5-pro-preview-05-06` ซึ่งเป็นโมเดลที่ทรงพลังที่สุดเวอร์ชันใหม่ของเรา พร้อมการปรับปรุงด้านโค้ดและการเรียกใช้ฟังก์ชัน `gemini-2.5-pro-preview-03-25`
  จะชี้ไปยังโมเดลเวอร์ชันใหม่โดยอัตโนมัติ

## 17 เมษายน 2025

- เปิดตัว `gemini-2.5-flash-preview-04-17` ซึ่งเป็นโมเดล[เวอร์ชันตัวอย่าง](https://ai.google.dev/gemini-api/docs/models?hl=th#model-versions)ของ Gemini ที่เพิ่มประสิทธิภาพด้านความคุ้มค่าและการคิดแบบปรับเปลี่ยนได้ ดูข้อมูลเพิ่มเติมได้ที่[เวอร์ชันตัวอย่างของ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-flash-preview) และ[การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th)

## 16 เมษายน 2025

- เปิดตัวการแคชบริบทสำหรับ [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.0-flash)

## 9 เมษายน 2025

**การอัปเดตโมเดล:**

- เปิดตัว `veo-2.0-generate-001` ซึ่งเป็นโมเดลการสร้างวิดีโอจากข้อความและรูปภาพที่พร้อมใช้งานสำหรับผู้ใช้ทั่วไป (GA) โดยสามารถสร้างวิดีโอที่มีรายละเอียดและมีความแตกต่างทางศิลปะ ดูข้อมูลเพิ่มเติมได้ที่[เอกสารประกอบของ Veo](https://ai.google.dev/gemini-api/docs/video?hl=th)
- เปิดตัว `gemini-2.0-flash-live-001` ซึ่งเป็นโมเดล [Live API](https://ai.google.dev/gemini-api/docs/live?hl=th) เวอร์ชันตัวอย่างแบบสาธารณะที่เปิดใช้การเรียกเก็บเงิน

  - **การจัดการเซสชันและความน่าเชื่อถือที่ได้รับการปรับปรุง**

    - **การกลับมาทำงานของเซสชัน:** รักษาเซสชันให้ทำงานต่อไปได้แม้เครือข่ายจะหยุดชะงักชั่วคราว ตอนนี้ API รองรับพื้นที่เก็บข้อมูลสถานะเซสชันฝั่งเซิร์ฟเวอร์ (สูงสุด 24 ชั่วโมง) และมีแฮนเดิล (session\_resumption) เพื่อเชื่อมต่อใหม่และดำเนินการต่อจากจุดที่ค้างไว้
    - **เซสชันที่ยาวนานขึ้นผ่านการบีบอัดบริบท:** เปิดใช้การโต้ตอบที่ยาวนานขึ้นเกินขีดจำกัดเวลาก่อนหน้า กำหนดค่าการบีบอัดหน้าต่างบริบทด้วยกลไกหน้าต่างแบบเลื่อนเพื่อจัดการความยาวบริบทโดยอัตโนมัติ ซึ่งจะช่วยป้องกันการสิ้นสุดอย่างกะทันหันเนื่องจากขีดจำกัดบริบท
    - **การแจ้งเตือนการยกเลิกการเชื่อมต่ออย่างราบรื่น:** รับข้อความเซิร์ฟเวอร์ `GoAway` ที่ระบุว่าการเชื่อมต่อกำลังจะปิดลง ซึ่งช่วยให้จัดการได้อย่างราบรื่นก่อนที่จะสิ้นสุดการเชื่อมต่อ
  - **ควบคุมการโต้ตอบได้มากขึ้น**
  - **การตรวจจับกิจกรรมเสียงพูด (VAD) ที่กำหนดค่าได้:** เลือกระดับความไวหรือปิดใช้ VAD อัตโนมัติทั้งหมด แล้วใช้เหตุการณ์ใหม่ของไคลเอ็นต์ (`activityStart`, `activityEnd`) สำหรับการควบคุมการเปลี่ยนด้วยตนเอง
  - **การจัดการการขัดจังหวะที่กำหนดค่าได้:** ตัดสินใจว่าข้อมูลที่ผู้ใช้ป้อนควรขัดจังหวะคำตอบของโมเดลหรือไม่
  - **ความครอบคลุมของเทิร์นที่กำหนดค่าได้:** เลือกว่า API จะประมวลผลอินพุตเสียงและวิดีโอทั้งหมดอย่างต่อเนื่อง หรือจะบันทึกเฉพาะเมื่อตรวจพบว่าผู้ใช้ปลายทางกำลังพูด
  - **ความละเอียดของสื่อที่กำหนดค่าได้:** เพิ่มประสิทธิภาพการใช้งานโทเค็นหรือคุณภาพโดยการเลือกความละเอียดสำหรับสื่ออินพุต
  - **เอาต์พุตและฟีเจอร์ที่สมบูรณ์ยิ่งขึ้น**
  - **ตัวเลือกเสียงและภาษาที่เพิ่มขึ้น:** เลือกเสียงใหม่ 2 เสียงและภาษาใหม่ 30 ภาษาสำหรับเอาต์พุตเสียง ตอนนี้คุณสามารถกำหนดค่าภาษาเอาต์พุตได้ภายใน `speechConfig`
  - **การสตรีมข้อความ:** รับคำตอบแบบข้อความเพิ่มขึ้นเรื่อยๆ ตามที่สร้างขึ้น ซึ่งช่วยให้แสดงต่อผู้ใช้ได้เร็วขึ้น
  - **การรายงานการใช้งานโทเค็น:** รับข้อมูลเชิงลึกเกี่ยวกับการใช้งานด้วยจำนวนโทเค็นโดยละเอียดที่ระบุไว้ในช่อง `usageMetadata` ของข้อความเซิร์ฟเวอร์ โดยแยกตามรูปแบบและระยะพรอมต์หรือการตอบสนอง

## 4 เมษายน 2025

- เปิดตัว `gemini-2.5-pro-preview-03-25` ซึ่งเป็นเวอร์ชันตัวอย่างแบบสาธารณะของ Gemini 2.5 Pro ที่เปิดใช้การเรียกเก็บเงิน คุณยังคงใช้ `gemini-2.5-pro-exp-03-25` ในรุ่นฟรีต่อไปได้

## 25 มีนาคม 2025

- เปิดตัว `gemini-2.5-pro-exp-03-25` ซึ่งเป็นโมเดล Gemini เวอร์ชันทดลองแบบสาธารณะที่เปิดโหมดการคิดไว้โดยค่าเริ่มต้นเสมอ
  ดูข้อมูลเพิ่มเติมได้ที่ [Gemini 2.5 Pro Experimental](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-2.5-pro-preview-03-25)

## 12 มีนาคม 2025

**การอัปเดตโมเดล:**

- เปิดตัวโมเดล [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=th#gemini) เวอร์ชันทดลองที่สามารถสร้างและแก้ไขรูปภาพได้
- เปิดตัว `gemma-3-27b-it` ซึ่งพร้อมให้บริการใน [AI Studio](https://aistudio.google.com?hl=th) และผ่าน Gemini API โดยเป็นส่วนหนึ่งของการเปิดตัว [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=th)

**การอัปเดต API:**

- เพิ่มการรองรับ [URL ของ YouTube](https://ai.google.dev/gemini-api/docs/vision?hl=th#youtube) เป็นแหล่งที่มาของสื่อ
- เพิ่มการรองรับการรวม[วิดีโอในบรรทัด](https://ai.google.dev/gemini-api/docs/vision?hl=th#inline-video)ที่มีขนาดน้อยกว่า 20 MB

## 11 มีนาคม 2025

**การอัปเดต SDK:**

- เปิดตัว [Google Gen AI SDK สำหรับ TypeScript และ JavaScript](https://googleapis.github.io/js-genai) เป็นเวอร์ชันตัวอย่างแบบสาธารณะ

## 7 มีนาคม 2025

**การอัปเดตโมเดล:**

- เปิดตัว `gemini-embedding-exp-03-07` ซึ่งเป็นโมเดลการฝังที่ใช้ Gemini [เวอร์ชันทดลอง](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=th)ในเวอร์ชันตัวอย่างแบบสาธารณะ

## 28 กุมภาพันธ์ 2025

**การอัปเดต API:**

- เพิ่มการรองรับ[การค้นหาเป็นเครื่องมือ](https://ai.google.dev/gemini-api/docs/grounding?hl=th)ใน `gemini-2.0-pro-exp-02-05` ซึ่งเป็นโมเดลทดลองที่อิงตาม Gemini 2.0 Pro

## 25 กุมภาพันธ์ 2025

**การอัปเดตโมเดล:**

- เปิดตัว `gemini-2.0-flash-lite` ซึ่งเป็นเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ของ [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-2.0-flash-lite) ที่ได้รับการเพิ่มประสิทธิภาพด้านความเร็ว ความสามารถในการปรับขนาด และความคุ้มค่า

## 19 กุมภาพันธ์ 2025

**ข้อมูลอัปเดตเกี่ยวกับ AI Studio**

- รองรับ[ภูมิภาคเพิ่มเติม](https://ai.google.dev/gemini-api/docs/available-regions?hl=th) (โคโซโว กรีนแลนด์ และหมู่เกาะแฟโร)

**การอัปเดต API:**

- รองรับ[ภูมิภาคเพิ่มเติม](https://ai.google.dev/gemini-api/docs/available-regions?hl=th) (โคโซโว กรีนแลนด์ และหมู่เกาะแฟโร)

## 18 กุมภาพันธ์ 2025

**การอัปเดตโมเดล:**

- ระบบไม่รองรับ Gemini 1.0 Pro อีกต่อไป ดูรายการโมเดลที่รองรับได้ที่[โมเดล Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th)

## 11 กุมภาพันธ์ 2025

**การอัปเดต API:**

- ข้อมูลอัปเดตเกี่ยวกับ[ความเข้ากันได้กับไลบรารี OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=th)

## 6 กุมภาพันธ์ 2025

**การอัปเดตโมเดล:**

- เปิดตัว `imagen-3.0-generate-002` ซึ่งเป็นเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ของ [Imagen 3 ใน Gemini API](https://ai.google.dev/gemini-api/docs/imagen?hl=th)

**การอัปเดต SDK:**

- เปิดตัว [Google Gen AI SDK สำหรับ Java](https://github.com/googleapis/java-genai) ในเวอร์ชันตัวอย่างแบบสาธารณะ

## 5 กุมภาพันธ์ 2025

**การอัปเดตโมเดล:**

- เปิดตัว `gemini-2.0-flash-001` ซึ่งเป็นเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) ของ [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-2.0-flash) ที่รองรับเอาต์พุตแบบข้อความเท่านั้น
- เปิดตัว `gemini-2.0-pro-exp-02-05`
  ซึ่งเป็นเวอร์ชันตัวอย่างสาธารณะ[เวอร์ชันทดลอง](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=th)ของ Gemini 2.0 Pro
- เปิดตัว `gemini-2.0-flash-lite-preview-02-05` ซึ่งเป็น[โมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-2.0-flash-lite)เวอร์ชันตัวอย่างสาธารณะแบบทดลองที่เพิ่มประสิทธิภาพด้านต้นทุน

**การอัปเดต API:**

- เพิ่มการรองรับ[อินพุตไฟล์และเอาต์พุตกราฟ](https://ai.google.dev/gemini-api/docs/code-execution?hl=th#input-output)ในการเรียกใช้โค้ด

**การอัปเดต SDK:**

- เปิดตัว [Google Gen AI SDK สำหรับ Python](https://googleapis.github.io/python-genai/) เป็นเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA)

## 21 มกราคม 2025

**การอัปเดตโมเดล:**

- เปิดตัว `gemini-2.0-flash-thinking-exp-01-21` ซึ่งเป็นเวอร์ชันตัวอย่างล่าสุดของโมเดลที่อยู่เบื้องหลัง[โมเดล Gemini 2.0 Flash Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=th)

## 19 ธันวาคม 2024

**การอัปเดตโมเดล:**

- เปิดตัว Gemini 2.0 Flash Flash Thinking เวอร์ชันตัวอย่างแบบสาธารณะ โหมดการคิดเป็นโมเดลการประมวลผลเวลาทดสอบที่ช่วยให้คุณเห็นกระบวนการคิดของโมเดลขณะสร้างคำตอบ และสร้างคำตอบที่มีความสามารถในการให้เหตุผลที่ดียิ่งขึ้น

  อ่านเพิ่มเติมเกี่ยวกับโหมด Gemini 2.0 Flash Thinking ใน[หน้าภาพรวม](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=th)

## 11 ธันวาคม 2024

**การอัปเดตโมเดล:**

- เปิดตัว [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-2.0-flash) เวอร์ชันตัวอย่างแบบสาธารณะ รายการฟีเจอร์บางส่วนของ Gemini 2.0 Flash Experimental มีดังนี้
  - เร็วกว่า Gemini 1.5 Pro ถึง 2 เท่า
  - สตรีมมิงแบบ 2 ทิศทางด้วย Live API ของเรา
  - การสร้างคำตอบแบบหลายโมดัลในรูปแบบข้อความ รูปภาพ และเสียงพูด
  - การใช้เครื่องมือในตัวพร้อมการให้เหตุผลแบบหลายเทิร์นเพื่อใช้ฟีเจอร์ต่างๆ เช่น การเรียกใช้โค้ด, Search, การเรียกใช้ฟังก์ชัน และอื่นๆ

อ่านข้อมูลเพิ่มเติมเกี่ยวกับ Gemini 2.0 Flash ใน[หน้าภาพรวม](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=th)

## 21 พฤศจิกายน 2024

**การอัปเดตโมเดล:**

- เปิดตัว `gemini-exp-1121` ซึ่งเป็นโมเดล Gemini API เวอร์ชันทดลองที่มีประสิทธิภาพยิ่งขึ้น

**การอัปเดตโมเดล:**

- อัปเดตชื่อแทนโมเดล `gemini-1.5-flash-latest` และ `gemini-1.5-flash` ให้ใช้ `gemini-1.5-flash-002`
  - การเปลี่ยนแปลงพารามิเตอร์ `top_k`: โมเดล `gemini-1.5-flash-002` รองรับค่า `top_k` ระหว่าง 1 ถึง 41 (ไม่รวม)
    ระบบจะเปลี่ยนค่าที่มากกว่า 40 เป็น 40

## 14 พฤศจิกายน 2024

**การอัปเดตโมเดล:**

- เปิดตัว `gemini-exp-1114` ซึ่งเป็นโมเดล Gemini API เวอร์ชันทดลองที่มีประสิทธิภาพ

## 8 พฤศจิกายน 2024

**การอัปเดต API:**

- เพิ่ม[การรองรับ Gemini](https://ai.google.dev/gemini-api/docs/openai?hl=th) ในไลบรารี OpenAI / REST API

## 31 ตุลาคม 2024

**การอัปเดต API:**

- เพิ่ม[การรองรับการเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/grounding?hl=th)

## 3 ตุลาคม 2024

**การอัปเดตโมเดล:**

- เปิดตัว `gemini-1.5-flash-8b-001` ซึ่งเป็นเวอร์ชันเสถียรของโมเดล Gemini API ที่เล็กที่สุดของเรา

## 24 กันยายน 2024

**การอัปเดตโมเดล:**

- เปิดตัว `gemini-1.5-pro-002` และ `gemini-1.5-flash-002` ซึ่งเป็น Gemini 1.5 Pro และ 1.5 Flash เวอร์ชันเสถียรใหม่ 2 เวอร์ชันสำหรับผู้ใช้ทั่วไป
- อัปเดตรหัสโมเดล `gemini-1.5-pro-latest` ให้ใช้ `gemini-1.5-pro-002` และรหัสโมเดล `gemini-1.5-flash-latest` ให้ใช้ `gemini-1.5-flash-002`
- เปิดตัว `gemini-1.5-flash-8b-exp-0924` เพื่อแทนที่ `gemini-1.5-flash-8b-exp-0827`
- เปิดตัว[ตัวกรองความปลอดภัยเพื่อความซื่อสัตย์ของพลเมือง](https://ai.google.dev/gemini-api/docs/safety-settings?hl=th#safety-filters)สำหรับ Gemini API และ AI Studio
- เปิดตัวการรองรับพารามิเตอร์ใหม่ 2 รายการสำหรับ Gemini 1.5 Pro และ 1.5 Flash ใน Python และ NodeJS ได้แก่ [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=th#FIELDS.frequency_penalty) และ [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=th#FIELDS.presence_penalty)

## 19 กันยายน 2024

**ข้อมูลอัปเดตเกี่ยวกับ AI Studio**

- เพิ่มปุ่มชอบและไม่ชอบลงในคำตอบของโมเดลเพื่อให้ผู้ใช้แสดงความคิดเห็นเกี่ยวกับคุณภาพของคำตอบได้

**การอัปเดต API:**

- เพิ่มการรองรับเครดิต Google Cloud ซึ่งตอนนี้สามารถใช้กับการใช้งาน Gemini API ได้แล้ว

## 17 กันยายน 2024

**ข้อมูลอัปเดตเกี่ยวกับ AI Studio**

- เพิ่มปุ่ม**เปิดใน Colab** ซึ่งจะส่งออกพรอมต์และโค้ดสำหรับเรียกใช้พรอมต์ไปยัง Colab Notebook ฟีเจอร์นี้ยังไม่รองรับการใช้พรอมต์ด้วยเครื่องมือ (โหมด JSON, การเรียกใช้ฟังก์ชัน หรือการเรียกใช้โค้ด)

## 13 กันยายน 2024

**ข้อมูลอัปเดตเกี่ยวกับ AI Studio**

- เพิ่มการรองรับโหมดเปรียบเทียบ ซึ่งช่วยให้คุณเปรียบเทียบคำตอบจากโมเดลและพรอมต์ต่างๆ เพื่อค้นหาคำตอบที่เหมาะกับ Use Case ของคุณมากที่สุด

## 30 สิงหาคม 2024

**การอัปเดตโมเดล:**

- Gemini 1.5 Flash รองรับ[การระบุสคีมา JSON ผ่านการกำหนดค่าโมเดล](https://ai.google.dev/gemini-api/docs/json-mode?hl=th#supply-schema-in-config)

## 27 สิงหาคม 2024

**การอัปเดตโมเดล:**

- เปิดตัว[โมเดลทดลอง](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=th)ต่อไปนี้
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## 9 สิงหาคม 2024

**การอัปเดต API:**

- เพิ่มการรองรับ[การประมวลผล PDF](https://ai.google.dev/gemini-api/docs/document-processing?hl=th)

## 5 สิงหาคม 2024

**การอัปเดตโมเดล:**

- เปิดตัวการรองรับการปรับแต่งโมเดลสำหรับ Gemini 1.5 Flash

## 1 สิงหาคม 2024

**การอัปเดตโมเดล:**

- เปิดตัว `gemini-1.5-pro-exp-0801` ซึ่งเป็นเวอร์ชันทดลองใหม่ของ [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-1.5-pro)

## 12 กรกฎาคม 2024

**การอัปเดตโมเดล:**

- นำการรองรับ Gemini 1.0 Pro Vision ออกจากบริการและเครื่องมือของ Google AI

## 27 มิถุนายน 2024

**การอัปเดตโมเดล:**

- การเปิดตัวเวอร์ชันสำหรับผู้ใช้ทั่วไปของหน้าต่างบริบทขนาด 2 ล้านโทเค็นของ Gemini 1.5 Pro

**การอัปเดต API:**

- เพิ่มการรองรับ[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)

## 18 มิถุนายน 2024

**การอัปเดต API:**

- เพิ่มการรองรับ[การแคชบริบท](https://ai.google.dev/gemini-api/docs/caching?hl=th)

## 12 มิถุนายน 2024

**การอัปเดตโมเดล:**

- เลิกใช้งาน Gemini 1.0 Pro Vision แล้ว

## 23 พฤษภาคม 2024

**การอัปเดตโมเดล:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-1.5-pro)
  (`gemini-1.5-pro-001`) พร้อมให้บริการในเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) แล้ว
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-1.5-flash) (`gemini-1.5-flash-001`) พร้อมให้บริการเวอร์ชันสำหรับผู้ใช้ทั่วไป (GA) แล้ว

## 14 พฤษภาคม 2024

**การอัปเดต API:**

- เปิดตัวหน้าต่างบริบทขนาด 2 ล้านโทเค็นสำหรับ Gemini 1.5 Pro (คิวรอ)
- เปิดตัว[การเรียกเก็บเงิน](https://ai.google.dev/gemini-api/docs/billing?hl=th)แบบจ่ายเมื่อใช้สำหรับ Gemini 1.0 Pro โดยการเรียกเก็บเงินสำหรับ Gemini 1.5 Pro และ Gemini 1.5 Flash จะพร้อมให้บริการเร็วๆ นี้
- เพิ่มขีดจำกัดอัตราการใช้งานสำหรับ Gemini 1.5 Pro ระดับชำระเงินที่กำลังจะเปิดตัว
- เพิ่มการรองรับวิดีโอในตัวลงใน [File API](https://ai.google.dev/api/rest/v1beta/files?hl=th)
- เพิ่มการรองรับข้อความธรรมดาใน [File API](https://ai.google.dev/api/rest/v1beta/files?hl=th)
- เพิ่มการรองรับการเรียกใช้ฟังก์ชันแบบขนาน ซึ่งจะแสดงผลการเรียกใช้มากกว่า 1 รายการต่อครั้ง

## 10 พฤษภาคม 2024

**การอัปเดตโมเดล:**

- เปิดตัว [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-1.5-flash) (`gemini-1.5-flash-latest`) ในเวอร์ชันตัวอย่าง

## 9 เมษายน 2024

**การอัปเดตโมเดล:**

- เปิดตัว [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-1.5-pro) (`gemini-1.5-pro-latest`) ในเวอร์ชันตัวอย่าง
- เปิดตัวโมเดลการฝังข้อความใหม่ `text-embeddings-004` ซึ่งรองรับขนาด[การฝังแบบยืดหยุ่น](https://ai.google.dev/gemini-api/docs/embeddings?hl=th#elastic-embedding)ที่ต่ำกว่า 768

**การอัปเดต API:**

- เปิดตัว [File API](https://ai.google.dev/api/rest/v1beta/files?hl=th) สำหรับจัดเก็บไฟล์สื่อชั่วคราวเพื่อใช้ในการสร้างพรอมต์
- เพิ่มการรองรับการเขียนพรอมต์ด้วยข้อมูลข้อความ รูปภาพ และเสียง หรือที่เรียกว่าการเขียนพรอมต์*แบบหลายรูปแบบ* ดูข้อมูลเพิ่มเติมได้ที่[การใช้พรอมต์กับสื่อ](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=th)
- เปิดตัว[คำสั่งของระบบ](https://ai.google.dev/gemini-api/docs/system-instructions?hl=th)ในเวอร์ชันเบต้า
- เพิ่ม[โหมดการเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th#function_calling_mode) ซึ่งกำหนดลักษณะการทำงานของการเรียกใช้ฟังก์ชัน
- เพิ่มการรองรับตัวเลือกการกำหนดค่า `response_mime_type` ซึ่งช่วยให้คุณขอคำตอบใน[รูปแบบ JSON](https://ai.google.dev/gemini-api/docs/api-overview?hl=th#json) ได้

## 19 มีนาคม 2024

**การอัปเดตโมเดล:**

- เพิ่มการรองรับ[การปรับแต่ง Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/) ใน Google AI Studio หรือด้วย Gemini API

## 13 ธันวาคม 2023

**การอัปเดตโมเดล:**

- gemini-pro: โมเดลข้อความใหม่สำหรับงานที่หลากหลาย สมดุลระหว่างความสามารถและประสิทธิภาพ
- gemini-pro-vision: โมเดลหลายรูปแบบใหม่สำหรับงานที่หลากหลาย
  สมดุลระหว่างความสามารถและประสิทธิภาพ
- embedding-001: โมเดลการฝังใหม่
- aqa: โมเดลที่ปรับแต่งมาเป็นพิเศษใหม่ซึ่งได้รับการฝึกให้ตอบคำถามโดยใช้ข้อความเพื่ออ้างอิงคำตอบที่สร้างขึ้น

ดูรายละเอียดเพิ่มเติมได้ที่[โมเดล Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th)

**การอัปเดตเวอร์ชัน API:**

- v1: ช่องทาง API ที่เสถียร
- v1beta: เวอร์ชันเบต้า ช่องนี้มีฟีเจอร์ที่อาจอยู่ระหว่างการพัฒนา

ดูรายละเอียดเพิ่มเติมได้ที่[หัวข้อเวอร์ชัน API](https://ai.google.dev/gemini-api/docs/api-versions?hl=th)

**การอัปเดต API:**

- `GenerateContent` เป็นปลายทางแบบรวมศูนย์เดียวสำหรับแชทและข้อความ
- สตรีมมิงพร้อมให้บริการผ่านวิธีการ `StreamGenerateContent`
- ความสามารถแบบหลายรูปแบบ: รูปภาพเป็นรูปแบบใหม่ที่รองรับ
- ฟีเจอร์ใหม่ในเวอร์ชันเบต้ามีดังนี้
  - [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
  - Attributed Question Answering (AQA)
- อัปเดตจำนวนคำตอบที่เป็นไปได้: โมเดล Gemini จะแสดงคำตอบที่เป็นไปได้เพียง 1 รายการเท่านั้น
- การตั้งค่าความปลอดภัยและหมวดหมู่ SafetyRating ต่างๆ ดูรายละเอียดเพิ่มเติมได้ที่[การตั้งค่าความปลอดภัย](https://ai.google.dev/gemini-api/docs/safety-settings?hl=th)
- โมเดล Gemini ยังไม่รองรับการปรับแต่งโมเดล (อยู่ระหว่างดำเนินการ)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-30 UTC"],[],[]]
