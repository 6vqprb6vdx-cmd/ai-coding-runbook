---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=th
fetched_at: 2026-10-05T06:39:54.531823+00:00
title: "\u0e2b\u0e38\u0e48\u0e19\u0e22\u0e19\u0e15\u0e4c\u0e17\u0e35\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e2a\u0e15\u0e23\u0e35\u0e21 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# หุ่นยนต์ที่มีการสตรีม

มาตรฐาน

`gemini-robotics-er-2-streaming-preview`ปลายทางของโมเดลจะแสดงปลายทางการสตรีมเฉพาะ
ที่ผสานรวมกับ [Live
API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=th) ซึ่งช่วยให้แอปพลิเคชันและหุ่นยนต์โต้ตอบกันได้แบบเรียลไทม์
ทั้ง 2 ทาง จึงเหมาะสำหรับเอเจนต์ที่ต้องการวงจรความคิดเห็นที่รวดเร็วและการตอบสนองต่อสภาพแวดล้อมแบบรีแอกทีฟ

[ลองใช้ใน Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=th)
[โคลนแอปตัวอย่างจาก GitHub](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## กรณีการใช้งาน

- **การประสานงานของหุ่นยนต์หลายตัว**: หุ่นยนต์หลายตัวที่สื่อสารสถานะของงาน
  และมอบหมายงานย่อยผ่านเซสชันที่แชร์
- **การตรวจสอบอย่างต่อเนื่อง**: หุ่นยนต์ที่สังเกตฉากและทริกเกอร์การดำเนินการ
  เมื่อเกิดเหตุการณ์ที่เฉพาะเจาะจง เช่น คอนเทนเนอร์ถึงระดับการเติม
- **คลังสินค้าและโลจิสติกส์**: ตัวแทนที่เลือกและแพ็กสินค้าซึ่งตรวจสอบสินค้าด้วยภาพ ติดตามความคืบหน้าในการแพ็ก และกู้คืนจากข้อผิดพลาด

## ข้อกำหนดทางเทคนิค

ตารางต่อไปนี้แสดงข้อกำหนดทางเทคนิคสำหรับ Live API

| หมวดหมู่ | รายละเอียด |
| --- | --- |
| รูปแบบอินพุต | เสียง (เสียง PCM แบบ 16 บิตดิบ, 16kHz, little-endian), รูปภาพ (JPEG <= 1FPS), ข้อความ |
| รูปแบบเอาต์พุต | ข้อความ |
| โปรโตคอล | การเชื่อมต่อ WebSocket แบบมีสถานะ (WSS) |

## สร้างการตั้งค่าแบบเอเจนต์

เอเจนต์หุ่นยนต์ทุกตัวที่สร้างขึ้นบน Live API จะทำตาม 3 ขั้นตอนต่อไปนี้

1. **ประกาศความสามารถของหุ่นยนต์เป็นเครื่องมือ** การดำเนินการแต่ละอย่างที่หุ่นยนต์ทำได้ เช่น
   นำทาง จับ พูด จะกลายเป็นการประกาศฟังก์ชันที่มีชื่อ
   คำอธิบาย และสคีมาพารามิเตอร์ การกระทำทางกายภาพต้องใช้ `"behavior": "BLOCKING"` เพื่อให้โมเดลรอให้หุ่นยนต์ทำงานเสร็จก่อน
   เลือกขั้นตอนถัดไป
2. **สตรีมอินพุตหลายรูปแบบไปยังเซสชันแบบถาวร** เปิด`live.connect`เซสชันและเปิดไว้ตลอดอายุของงาน ส่งเฟรมวิดีโอ เสียง
   หรือข้อความเมื่อเซ็นเซอร์ของหุ่นยนต์ส่งมา
3. **จัดการการเรียกใช้เครื่องมือในลูปการรับ** ทุกครั้งที่โมเดลเลือกการดำเนินการ ระบบจะส่งข้อความ `tool_call` ลูปรับจะเรียกใช้ฟังก์ชัน
   กับ SDK ของหุ่นยนต์และส่งกลับ `tool_response` เซสชันจะ
   เปิดอยู่ และโมเดลจะเลือกการดำเนินการถัดไปตามผลลัพธ์

ส่วนต่อไปนี้จะแสดงวิธีใช้ขั้นตอนเหล่านี้กับรูปแบบทั่วไป 3 รูปแบบ ได้แก่ ลูปเอเจนต์พื้นฐาน การตรวจสอบฉากเชิงรุกด้วยสัญญาณชีพ และการกำหนดเส้นทางการพูดผ่าน TTS เป็นเครื่องมือ

## ประสานงานหุ่นยนต์ผ่านการเรียกใช้ฟังก์ชัน

ตัวอย่างต่อไปนี้แสดงขั้นตอนทั้ง 3 ที่เชื่อมต่อกันในสคริปต์ Python
เดียว

ขั้นตอนที่ 1 - คำจำกัดความของเครื่องมือ - ประกาศความสามารถของหุ่นยนต์เป็นการประกาศฟังก์ชัน
ฟังก์ชัน `navigate` ใช้ `"behavior": "BLOCKING"` เพื่อให้โมเดลรอให้หุ่นยนต์ไปถึงจุดอ้างอิงก่อนที่จะเรียกใช้เครื่องมืออื่น
เพิ่มการประกาศฟังก์ชันในรายการเดียวกันเพื่อแสดงความสามารถเพิ่มเติมของหุ่นยนต์

ขั้นตอนที่ 2 - ตัวช่วยป้อนข้อมูล - แสดงฟังก์ชัน 3 อย่างที่สตรีมอินพุตรูปแบบต่างๆ
ลงในเซสชัน: `send_text` สำหรับคำสั่ง `send_image` สำหรับเฟรมกล้อง
พร้อมพรอมต์ข้อความที่ไม่บังคับ และ `send_audio` สำหรับเสียง PCM ดิบจาก
ไมโครโฟน

ขั้นตอนที่ 3 ซึ่งเป็นลูปการรับจะทำงานพร้อมกันและจัดการข้อความ 2 ประเภท ได้แก่ ข้อความ `server_content` (เอาต์พุตข้อความของโมเดล) และข้อความ `tool_call` (โมเดลขอให้หุ่นยนต์ดำเนินการ) เมื่อมีการเรียกใช้เครื่องมือ ลูปจะเรียกใช้
`execute_tool` ซึ่งเป็น Stub ที่คุณแทนที่ด้วย SDK ของหุ่นยนต์จริง แล้วส่งกลับ
`tool_response` เพื่อให้โมเดลเลือกการดำเนินการถัดไปได้

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

ลูปการรับจะยังคงใช้งานได้หลังจากที่เครื่องมือตอบกลับแต่ละครั้ง โมเดลจะสร้าง
และแก้ไขแผนระยะยาวโดยที่คุณไม่ต้องเข้ารหัสลําดับการกระทําทั้งหมด
ล่วงหน้า

## การให้เหตุผลเชิงรุกเกี่ยวกับมิติเชิงพื้นที่และเวลา

Live API จะสตรีมวิดีโอ แต่เฟรมวิดีโอเพียงอย่างเดียวจะไม่ทริกเกอร์รอบการให้เหตุผลใหม่ เฟรมวิดีโอต้องมาพร้อมกับพรอมต์ข้อความหรือเสียงเพื่อกระตุ้นการตอบกลับของโมเดล ดูรายละเอียดเพิ่มเติมได้ที่
[ความสามารถของ Live API](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=th)

หากต้องการเปิดใช้การให้เหตุผลเชิงรุก ให้ใช้**สัญญาณชีพ**: ส่งเฟรมกล้องล่าสุดเป็นระยะๆ ตามด้วยพรอมต์ข้อความสั้นๆ ที่บังคับให้โมเดลตรวจสอบฉากและตัดสินใจอย่างชัดเจน อินพุตวิดีโอถูกจำกัดอัตราเป็น
1 เฟรมต่อวินาที

### ใช้ฮาร์ตบีต

โครูทีน Heartbeat จะทำงานเป็น`asyncio` งานแยกต่างหากในเซสชันเดียวกัน
โดยจะกำหนดเป้าหมายเป็นความถี่ 1 Hz (ตรงกับขีดจำกัดอัตราการป้อนข้อมูลวิดีโอ) อย่างเหมาะสม
ขณะรอให้แต่ละเลี้ยวเสร็จสมบูรณ์ (`er_turn_done`) เพื่อไม่ให้ขัดขวาง
การให้เหตุผลระหว่างการนำทาง

```
async def heartbeat(session, camera, er_turn_done: asyncio.Event):
    TARGET_INTERVAL_SEC = 1.0

    while True:
        start_time = asyncio.get_running_loop().time()

        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )

        # Wait for the model to finish responding before sending the next heartbeat
        await er_turn_done.wait()
        er_turn_done.clear()

        # Sleep only the remaining time to maintain ~1 Hz cadence
        elapsed = asyncio.get_running_loop().time() - start_time
        remaining = TARGET_INTERVAL_SEC - elapsed
        if remaining > 0:
            await asyncio.sleep(remaining)
```

### อัปเดตลูปรับ

หากต้องการส่งสัญญาณเมื่อโมเดลพูดจบแล้ว ให้อัปเดต `receive_loop`
เพื่อตั้งค่า `er_turn_done` ดังนี้

```
# In receive_loop: signal when the model finishes its turn
if sc.turn_complete:
    er_turn_done.set()
```

## เอาต์พุตเสียงผ่าน TTS ภายนอก

Gemini Robotics ER 2 จะแสดงข้อความ แอปพลิเคชันของคุณจะกำหนดเส้นทางการตอบกลับที่เสร็จสมบูรณ์
ไปยังผู้ให้บริการ TTS แยกต่างหาก (เช่น
[Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)) ผ่านการเรียกกลับที่แทรก
ซึ่งจะช่วยให้คุณควบคุมเวลาในการตอบสนองของคำพูด การเลือกเสียง และลักษณะการทำงานของการหยุดชะงักได้ และช่วยให้คุณสลับแบ็กเอนด์ TTS ได้โดยไม่ต้องเปลี่ยนตรรกะของเอเจนต์

นอกจากนี้ คุณยังประกาศ TTS เป็นเครื่องมือเพื่อให้โมเดลถือว่า "พูดอะไรบางอย่าง" เหมือนกับ "ขยับแขน" ได้ด้วย
เพิ่มการประกาศฟังก์ชันต่อไปนี้ลงในรายการ `tools`
จากส่วนแรก

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

การรวม TTS ไว้ในการประกาศฟังก์ชันจะช่วยให้โมเดลจัดการคำพูดผ่านเส้นทางการเรียกใช้เครื่องมือเดียวกันกับที่ใช้สำหรับการดำเนินการของหุ่นยนต์อื่นๆ แอปพลิเคชันของคุณจะดำเนินการ
เรียกใช้ด้วยการเรียกกลับที่แทรก

## ตัวอย่างใน GitHub

ดูตัวอย่างการทำงานทั้งหมด รวมถึงการสาธิตการหยิบขนมของหุ่นยนต์ Spot และการสาธิตการแพนกล้องและก้มเงยของ Tinybot ได้ที่
[ตัวอย่าง Robotics Live API](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## ขั้นตอนถัดไป

- [การทำความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=th) - การค้นหาช่วงเวลาและการจัดประเภทความคืบหน้า
- [การจัดการเป็นกลุ่มของงาน](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=th) - งานระยะยาวที่ไม่มีการสตรีม
- [ภาพรวมของ Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=th) - เอกสารประกอบเกี่ยวกับ Live API แบบเต็ม

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-16 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-16 UTC"],[],[]]
