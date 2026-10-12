---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=th
fetched_at: 2026-10-12T07:01:06.203900+00:00
title: "\u0e40\u0e23\u0e34\u0e48\u0e21\u0e15\u0e49\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19 Gemini Live API \u0e42\u0e14\u0e22\u0e43\u0e0a\u0e49 Google GenAI SDK \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# เริ่มต้นใช้งาน Gemini Live API โดยใช้ Google GenAI SDK

Gemini Live API ช่วยให้โต้ตอบกับโมเดล Gemini ได้แบบเรียลไทม์และสองทาง โดยรองรับอินพุตเสียง วิดีโอ และข้อความ รวมถึงเอาต์พุตเสียงแบบเนทีฟ คู่มือนี้อธิบายวิธีผสานรวมกับ API โดยใช้ Google GenAI SDK บนเซิร์ฟเวอร์

[ลองใช้ Live API ใน Google AI Studiomic](https://aistudio.google.com/live?hl=th)
[Clone the example app from GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[Use coding agent skillsterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th)

## ภาพรวม

Gemini Live API ใช้ WebSockets สำหรับการสื่อสารแบบเรียลไทม์ SDK `google-genai` มีอินเทอร์เฟซแบบอะซิงโครนัสระดับสูงสำหรับการจัดการการเชื่อมต่อเหล่านี้

แนวคิดหลัก

- **เซสชัน**: การเชื่อมต่อกับโมเดลแบบต่อเนื่อง
- **การกำหนดค่า**: การตั้งค่าโมดัลลิตี (เสียง/ข้อความ) เสียง และคำแนะนำของระบบ
- **อินพุตแบบเรียลไทม์**: การส่งเฟรมเสียงและวิดีโอเป็น Blob

## การเชื่อมต่อกับ Live API

เริ่มเซสชัน Live API ด้วยคีย์ API โดยทำดังนี้

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

model = "gemini-3.8-live"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY"});
const model = 'gemini-3.8-live';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## การส่งข้อความ

คุณสามารถส่งข้อความได้โดยใช้ `send_realtime_input` (Python) หรือ `sendRealtimeInput` (JavaScript)

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

## การส่งเสียง

คุณต้องส่งเสียงเป็นข้อมูล PCM ดิบ (เสียง PCM ดิบ 16 บิต, 16kHz, little-endian)

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

ดูตัวอย่างวิธีรับเสียงจากอุปกรณ์ไคลเอ็นต์ (เช่น เบราว์เซอร์)
ได้ที่ตัวอย่างแบบครบวงจรใน [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70)

## การส่งวิดีโอ

ระบบจะส่งเฟรมวิดีโอเป็นรูปภาพแต่ละรูป (เช่น JPEG หรือ PNG) ที่อัตราเฟรมที่เฉพาะเจาะจง (สูงสุด 1 เฟรมต่อวินาที)

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

ดูตัวอย่างวิธีรับวิดีโอจากอุปกรณ์ไคลเอ็นต์ (เช่น เบราว์เซอร์)
ได้ที่ตัวอย่างแบบครบวงจรใน [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120)

## การรับเสียง

ระบบจะรับคำตอบเสียงของโมเดลเป็นข้อมูลแบบเป็นช่วงๆ

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

ดูแอปตัวอย่างใน GitHub เพื่อดูวิธี[รับเสียงบนเซิร์ฟเวอร์](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98)และ[เล่นเสียงในเบราว์เซอร์](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174)

## การรับข้อความ

การถอดเสียงสำหรับทั้งข้อมูลจากผู้ใช้และเอาต์พุตโมเดลจะอยู่ในเนื้อหาของเซิร์ฟเวอร์

### Python

```
async for response in session.receive():
    content = response.server_content
    if content:
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.inputTranscription) {
  console.log('User:', content.inputTranscription.text);
}
if (content?.outputTranscription) {
  console.log('Gemini:', content.outputTranscription.text);
}
```

## การจัดการการเรียกใช้เครื่องมือ

API รองรับการเรียกใช้เครื่องมือ (การเรียกใช้ฟังก์ชัน) เมื่อโมเดลขอการเรียกใช้เครื่องมือ คุณต้องเรียกใช้ฟังก์ชันและส่งคำตอบกลับ

### Python

```
async for response in session.receive():
    if response.tool_call:
        function_responses = []
        for fc in response.tool_call.function_calls:
            # 1. Execute the function locally
            result = my_tool_function(**fc.args)

            # 2. Prepare the response
            function_responses.append(types.FunctionResponse(
                name=fc.name,
                id=fc.id,
                response={"result": result}
            ))

        # 3. Send the tool response back to the session
        await session.send_tool_response(function_responses=function_responses)
```

### JavaScript

```
// Inside the onmessage callback
if (response.toolCall) {
  const functionResponses = [];
  for (const fc of response.toolCall.functionCalls) {
    const result = myToolFunction(fc.args);
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }
  session.sendToolResponse({ functionResponses });
}
```

## ขั้นตอนถัดไป

- อ่านคู่มือความสามารถของ Live API [ฉบับเต็ม](https://ai.google.dev/gemini-api/docs/live-guide?hl=th) เพื่อดูความสามารถและการกำหนดค่าที่สำคัญ ซึ่งรวมถึงการตรวจจับกิจกรรมเสียงและฟีเจอร์เสียงแบบเนทีฟ
- อ่านคู่มือ[การใช้เครื่องมือ](https://ai.google.dev/gemini-api/docs/live-tools?hl=th)เพื่อดูวิธีผสานรวม Live API กับเครื่องมือและการเรียกใช้ฟังก์ชัน
- อ่านคู่มือ[การจัดการเซสชัน](https://ai.google.dev/gemini-api/docs/live-session?hl=th)เพื่อดูวิธีจัดการการสนทนาที่ใช้เวลานาน
- อ่านคู่มือ[โทเค็นชั่วคราว](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=th)เพื่อดูการตรวจสอบสิทธิ์ที่ปลอดภัยในแอปพลิเคชันแบบ[ไคลเอ็นต์ต่อเซิร์ฟเวอร์](https://ai.google.dev/gemini-api/docs/live-api?hl=th#implementation-approach)
- ดูข้อมูลเพิ่มเติมเกี่ยวกับ WebSockets API ที่อยู่เบื้องหลังได้ที่[ข้อมูลอ้างอิง WebSockets API](https://ai.google.dev/api/live?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-17 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-17 UTC"],[],[]]
