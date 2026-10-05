---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=th
fetched_at: 2026-10-05T06:33:59.154475+00:00
title: "\u0e01\u0e32\u0e23\u0e17\u0e33\u0e04\u0e27\u0e32\u0e21\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e27\u0e34\u0e14\u0e35\u0e42\u0e2d \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)

ส่งความคิดเห็น

# การทำความเข้าใจวิดีโอ

Gemini Robotics ER 2 สามารถติดตามความคืบหน้าของงานจากฟีดวิดีโอต่อเนื่องโดยใช้ความสามารถ 2 อย่าง ได้แก่

- การค้นหาช่วงเวลา: ระบุการประทับเวลาที่แม่นยำซึ่งเหตุการณ์สำคัญเกิดขึ้น
- การจัดประเภทความคืบหน้า: กำหนดให้วิดีโอแต่ละรายการอยู่ในช่วงความสมบูรณ์ 5 ช่วง (0–20%, 20–40%, 40–60%, 60–80%, 80–100%)

## การค้นหาช่วงเวลา

การค้นหาช่วงเวลาจะระบุเฟรมวิดีโอที่แน่นอนซึ่งเหตุการณ์สำคัญเกิดขึ้น เช่น เมื่อแก้วเต็มหรือมีการผูกปม หุ่นยนต์ใช้ข้อมูลนี้เพื่อยืนยันความสำเร็จ จัดลำดับขั้นตอน และทริกเกอร์การแก้ไข

ข้อความแจ้งตัวอย่างต่อไปนี้ขอให้โมเดลระบุช่วงเวลาที่งานที่กำหนดในวิดีโอเสร็จสมบูรณ์

```
from google import genai
from google.genai import types

client = genai.Client()

with open("task_video.mp4", "rb") as f:
    video_bytes = f.read()

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(data=video_bytes, mime_type="video/mp4"),
        prompt,
    ],
)

print(response.text)
```

ตัวอย่างต่อไปนี้แสดงเฟรมตัวอย่างจากวิดีโอการค้นหาช่วงเวลา โดยโมเดลจะระบุการประทับเวลาที่งานเสร็จสมบูรณ์

![ตัวอย่างเฟรมวิดีโอที่แสดงเอาต์พุตการค้นหาช่วงเวลาพร้อมโอเวอร์เลย์การประทับเวลา](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=th)

## การจัดประเภทความคืบหน้า

การจัดประเภทความคืบหน้าจะกำหนดให้วิดีโออยู่ในช่วงความสมบูรณ์ 5 ช่วง ได้แก่ 0–20%, 20–40%, 40–60%, 60–80% หรือ 80–100% ซึ่งช่วยให้หุ่นยนต์รับรู้สถานการณ์แบบเรียลไทม์ จึงสามารถปรับการดำเนินการหรือลองขั้นตอนที่ล้มเหลวอีกครั้งได้โดยไม่ต้องรีสตาร์ทเวิร์กโฟลว์ทั้งหมด

ข้อความแจ้งตัวอย่างต่อไปนี้ขอให้โมเดลจัดประเภทระดับความคืบหน้าปัจจุบันจากวิดีโอ

```
from google import genai
from google.genai import types

client = genai.Client()

with open("task_video.mp4", "rb") as f:
    video_bytes = f.read()

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(data=video_bytes, mime_type="video/mp4"),
        prompt,
    ],
)

print(response.text)
```

ตัวอย่างต่อไปนี้แสดงเฟรมตัวอย่างจากวิดีโอการจัดประเภทความคืบหน้า โดยโมเดลจะกำหนดช่วงความคืบหน้า

![ตัวอย่างเฟรมวิดีโอที่แสดงเอาต์พุตการจัดประเภทความคืบหน้าพร้อมป้ายกำกับวงเล็บความคืบหน้า](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=th)

## ตัวอย่าง

ดูตัวอย่างที่เรียกใช้ได้ทั้งหมด รวมถึงการติดตามงานหลายขั้นตอนได้ที่
[คู่มือการใช้งาน Robotics](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)

## ขั้นตอนถัดไป

- [API แบบสดสำหรับ Robotics](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=th) - การสตรีมแบบสองทางแบบเรียลไทม์
- [การจัดระเบียบงาน](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=th) - งานระยะยาวที่มีการใช้เหตุผลเชิงพื้นที่
- [ภาพรวมของ Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=th) - การเปรียบเทียบโมเดลและความสามารถ

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-08 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-08 UTC"],[],[]]
