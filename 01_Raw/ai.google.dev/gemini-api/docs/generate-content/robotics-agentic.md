---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=th
fetched_at: 2026-10-26T06:04:48.248379+00:00
title: "\u0e04\u0e27\u0e32\u0e21\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e14\u0e49\u0e32\u0e19\u0e27\u0e34\u0e2a\u0e31\u0e22\u0e17\u0e31\u0e28\u0e19\u0e4c\u0e02\u0e2d\u0e07 Agentic AI \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)

ส่งความคิดเห็น

# ความสามารถด้านวิสัยทัศน์ของ Agentic AI

โมเดล Gemini Robotics ER สามารถเขียนและเรียกใช้โค้ด Python เพื่อจัดการรูปภาพและใช้ตรรกะก่อนตอบคำถาม หน้านี้ครอบคลุมตัวอย่างการเรียกใช้โค้ด ได้แก่ การตรวจจับออบเจ็กต์ด้วยการซูมและครอบตัด การอ่านเครื่องมือ การวัดของเหลว การอ่านแผงวงจร และคำอธิบายประกอบรูปภาพ

หากต้องการปรับตัวอย่างเหล่านี้ให้เข้ากับกรณีการใช้งานของคุณเอง ให้แทนที่ข้อความพรอมต์และไฟล์รูปภาพที่อัปโหลดด้วยข้อความและไฟล์ของคุณเอง นอกจากนี้ คุณยังปรับสคีมา JSON ที่ขอในพรอมต์ให้ตรงกับโครงสร้างเอาต์พุตที่แอปพลิเคชันต้องการ หรือเพิ่ม `system_instruction` เพื่อบังคับใช้รูปแบบและความแม่นยำของเอาต์พุตได้ด้วย

ดูโค้ดที่เรียกใช้ได้ทั้งหมดที่
[คู่มือการใช้งาน Robotics](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)

## ระดับการคิด

คุณสามารถควบคุมระดับการคิดเพื่อแลกความหน่วงแฝงกับความแม่นยำได้ งานเชิงพื้นที่ เช่น การตรวจจับออบเจ็กต์ จะทำงานได้ดีเมื่อมีระดับการคิดต่ำ งานที่ซับซ้อน เช่น การนับหรือการประมาณน้ำหนัก จะได้ประโยชน์จากระดับการคิดที่สูงขึ้น

ตัวอย่างต่อไปนี้กำหนดระดับการคิดเป็น `high` สำหรับงานการนับที่ซับซ้อน

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('scene.jpeg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        "Identify and count all objects on the table."
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    )
)

print(response.text)
```

ดูรายละเอียดได้ที่[การคิด](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=th)

## การตรวจจับออบเจ็กต์ (ซูมและครอบตัด)

ตัวอย่างต่อไปนี้แสดงวิธีใช้การเรียกใช้โค้ดเพื่อซูมและครอบตัดรูปภาพเพื่อให้เห็นชัดเจนขึ้นเมื่อตรวจจับออบเจ็กต์และแสดงกล่องขอบเขต

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Return JSON in the format {label: val, y: val, x: val, y2: val, x2: val} for
the compostable objects in this scene. Please Zoom and crop the image for a
clearer view. Return an annotated image of the final result with the bounding
boxes drawn on it to the API caller as a part of your process.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

เอาต์พุตโมเดลจะมีลักษณะคล้ายกับการตอบกลับ JSON ต่อไปนี้

```
[
  {"label": "compostable", "y": 256, "x": 482, "y2": 295, "x2": 546},
  {"label": "compostable", "y": 317, "x": 478, "y2": 350, "x2": 542},
  {"label": "compostable", "y": 586, "x": 556, "y2": 668, "x2": 595},
  {"label": "compostable", "y": 463, "x": 669, "y2": 511, "x2": 718},
  {"label": "compostable", "y": 178, "x": 565, "y2": 250, "x2": 609}
]
```

รูปภาพต่อไปนี้แสดงกล่องที่โมเดลแสดง

![ตัวอย่างที่แสดงกรอบล้อมรอบสำหรับออบเจ็กต์ที่พบ](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-bounding-boxes.png?hl=th)

## อ่านเกจแบบอนาล็อกและใช้ตรรกะ

ตัวอย่างต่อไปนี้แสดงวิธีใช้โมเดลเพื่ออ่านเกจแบบอนาล็อกและทำการคำนวณเวลา โดยใช้คำแนะนำระบบเพื่อบังคับใช้เอาต์พุต JSON

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('gauge.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read the current value from this gauge. Then, calculate how long
        it will take at the current rate for the value to reach maximum.
        Reply in JSON: {"current_value": val, "max_value": val,
        "time_to_max_minutes": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## วัดของเหลวในภาชนะ

ตัวอย่างต่อไปนี้แสดงวิธีใช้การเรียกใช้โค้ดเพื่อวัดระดับของเหลวในภาชนะ

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('fluid.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Measure the amount of fluid in the container. Reply in JSON:
        {"fluid_level_ml": val, "container_capacity_ml": val,
        "percentage_full": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## อ่านเครื่องหมายบนแผงวงจร

ตัวอย่างต่อไปนี้แสดงวิธีใช้การเรียกใช้โค้ดเพื่ออ่านเครื่องหมายบนแผงวงจร

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('circuit_board.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read all visible component labels and markings on this circuit
        board. Reply in JSON: {"components": [{"label": val,
        "location": [y, x]}]}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

![ตัวอย่างที่แสดงเครื่องหมายบนแผงวงจร](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-circuit-board.png?hl=th)

## คำอธิบายประกอบรูปภาพ

ตัวอย่างต่อไปนี้แสดงวิธีใช้การเรียกใช้โค้ดเพื่อใส่คำอธิบายประกอบรูปภาพ (เช่น การวาดลูกศรสำหรับวิธีการกำจัด) และแสดงรูปภาพที่แก้ไขแล้ว

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Look at this image and return it as an annotated version using arrows of
different colors to represent which items should go in which bins for
disposal. You must return the final image to the API caller.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

ต่อไปนี้เป็นตัวอย่างอินพุตรูปภาพ

![ตัวอย่างที่แสดงนาฬิกาเพื่ออ่าน](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-image-annotation.png?hl=th)

เอาต์พุตโมเดลจะมีลักษณะคล้ายกับเอาต์พุตต่อไปนี้

```
  The annotated image shows the suggested disposal locations for the items on the table:
  - **Green bin (Compost/Organic)**: Green chili, red chili, grapes, and cherries.
  - **Blue bin (Recycling)**: Yellow crushed can and plastic container.
  - **Black bin (Trash)**: Chocolate bar wrapper, Welch's packet, and white tissue.
```

## ขั้นตอนถัดไป

- [การจัดระเบียบงาน](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=th) - งานระยะยาวที่มี API ของหุ่นยนต์ที่กำหนดเอง
- [Robotics พร้อมการสตรีม](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=th) - การสตรีมแบบสองทางแบบเรียลไทม์ (Gemini Robotics ER 2 เท่านั้น)
- [ความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=th) - การค้นหาช่วงเวลาและการจัดประเภทความคืบหน้า (Gemini Robotics ER 2 เท่านั้น)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-10 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-10 UTC"],[],[]]
