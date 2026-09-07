---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=th
fetched_at: 2026-09-07T05:42:52.601963+00:00
title: "\u0e40\u0e23\u0e34\u0e48\u0e21\u0e15\u0e49\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19 Gemini Live API \u0e42\u0e14\u0e22\u0e43\u0e0a\u0e49 WebSockets \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# เริ่มต้นใช้งาน Gemini Live API โดยใช้ WebSockets

Gemini Live API ช่วยให้โต้ตอบกับโมเดล Gemini ได้แบบเรียลไทม์และแบบ 2 ทาง โดยรองรับอินพุตเสียง วิดีโอ และข้อความ รวมถึงเอาต์พุตเสียงดั้งเดิม คู่มือนี้อธิบายวิธีผสานรวมกับ API โดยตรงโดยใช้ WebSocket แบบดิบ

[ลองใช้ Live API ใน Google AI Studiomic](https://aistudio.google.com/live?hl=th)
[โคลนแอปตัวอย่างจาก GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[ใช้ทักษะของเอเจนต์การเขียนโค้ดterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th)

## ภาพรวม

Gemini Live API ใช้ WebSockets สำหรับการสื่อสารแบบเรียลไทม์ ซึ่งต่างจากการใช้ SDK ตรงที่วิธีนี้เกี่ยวข้องกับการจัดการการเชื่อมต่อ WebSocket โดยตรงและการส่ง/รับข้อความในรูปแบบ JSON ที่เฉพาะเจาะจงซึ่งกำหนดโดย API

แนวคิดหลัก

- **ปลายทาง WebSocket**: URL ที่เฉพาะเจาะจงเพื่อเชื่อมต่อ
- **รูปแบบข้อความ**: การสื่อสารทั้งหมดจะดำเนินการผ่านข้อความ JSON ที่เป็นไปตามโครงสร้าง [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=th#bidigeneratecontentclientmessage) และ [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=th#bidigeneratecontentservermessage)
- **การจัดการเซสชัน**: คุณมีหน้าที่รับผิดชอบในการรักษาการเชื่อมต่อ WebSocket

## การตรวจสอบสิทธิ์

ระบบจะจัดการการตรวจสอบสิทธิ์โดยการใส่คีย์ API เป็นพารามิเตอร์การค้นหาใน URL ของ WebSocket

รูปแบบของปลายทางคือ

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

แทนที่ `YOUR_API_KEY` ด้วยคีย์ API จริงของคุณ

## การตรวจสอบสิทธิ์ด้วยโทเค็นชั่วคราว

หากใช้[โทเค็นชั่วคราว](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=th) คุณต้องเชื่อมต่อกับปลายทาง `v1beta`
ต้องส่งโทเค็นชั่วคราวเป็นพารามิเตอร์การค้นหา `access_token`

รูปแบบปลายทางสำหรับคีย์ชั่วคราวคือ

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

แทนที่ `{short-lived-token}` ด้วยโทเค็นชั่วคราวจริง

## เชื่อมต่อกับ Live API

หากต้องการเริ่มเซสชันสด ให้สร้างการเชื่อมต่อ WebSocket กับปลายทางที่ได้รับการตรวจสอบสิทธิ์
ข้อความแรกที่ส่งผ่าน WebSocket ต้องเป็น [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=th#bidigeneratecontentsetup) ที่มี `config`
ดูตัวเลือกการกำหนดค่าทั้งหมดได้ที่[เอกสารอ้างอิง Live API - WebSockets API](https://ai.google.dev/api/live?hl=th)

### Python

```
import asyncio
import websockets
import json

API_KEY = "YOUR_API_KEY"
MODEL_NAME = "gemini-3.1-flash-live-preview"
WS_URL = f"wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key={API_KEY}"

async def connect_and_configure():
    async with websockets.connect(WS_URL) as websocket:
        print("WebSocket Connected")

        # 1. Send the initial configuration
        setup_message = {
            "setup": {
                "model": f"models/{MODEL_NAME}",
                "responseModalities": ["AUDIO"],
                "systemInstruction": {
                    "parts": [{"text": "You are a helpful assistant."}]
                }
            }
        }
        await websocket.send(json.dumps(setup_message))
        print("Configuration sent")

        # Keep the session alive for further interactions
        await asyncio.sleep(3600) # Example: keep open for an hour

async def main():
    await connect_and_configure()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.1-flash-live-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  // 1. Send the initial configuration
  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      responseModalities: ['AUDIO'],
      systemInstruction: {
        parts: [{ text: 'You are a helpful assistant.' }]
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
  console.log('Configuration sent');
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);
  // Handle different types of responses here
};

websocket.onerror = (error) => {
  console.error('WebSocket Error:', error);
};

websocket.onclose = () => {
  console.log('WebSocket Closed');
};
```

## ส่งข้อความ

หากต้องการส่งข้อความที่ป้อน ให้สร้างข้อความ [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=th#bidigeneratecontentrealtimeinput) ที่มีช่อง `text`

### Python

```
# Inside the websocket context
async def send_text(websocket, text):
    text_message = {
        "realtimeInput": {
            "text": text
        }
    }
    await websocket.send(json.dumps(text_message))
    print(f"Sent text: {text}")

# Example usage: await send_text(websocket, "Hello, how are you?")
```

### JavaScript

```
function sendTextMessage(text) {
  if (websocket.readyState === WebSocket.OPEN) {
    const textMessage = {
      realtimeInput: {
        text: text
      }
    };
    websocket.send(JSON.stringify(textMessage));
    console.log('Text message sent:', text);
  } else {
    console.warn('WebSocket not open.');
  }
}

// Example usage:
sendTextMessage("Hello, how are you?");
```

## ส่งเสียง

ต้องส่งเสียงเป็นข้อมูล PCM ดิบ (เสียง PCM ดิบ 16 บิต, 16 kHz, little-endian) สร้างข้อความ [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=th#bidigeneratecontentrealtimeinput) ด้วยข้อมูลเสียง `mimeType` เป็นสิ่งสำคัญ

### Python

```
# Inside the websocket context
async def send_audio_chunk(websocket, chunk_bytes):
    import base64
    encoded_data = base64.b64encode(chunk_bytes).decode('utf-8')
    audio_message = {
        "realtimeInput": {
            "audio": {
                "data": encoded_data,
                "mimeType": "audio/pcm;rate=16000"
            }
        }
    }
    await websocket.send(json.dumps(audio_message))
    # print("Sent audio chunk") # Avoid excessive logging

# Assuming 'chunk' is your raw PCM audio bytes
# await send_audio_chunk(websocket, chunk)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
    // console.log('Sent audio chunk');
  }
}
// Example usage: sendAudioChunk(audioBuffer);
```

ดูตัวอย่างวิธีรับเสียงจากอุปกรณ์ไคลเอ็นต์ (เช่น เบราว์เซอร์) ได้ที่ตัวอย่างตั้งแต่ต้นจนจบใน [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74)

## ส่งวิดีโอ

ระบบจะส่งเฟรมวิดีโอเป็นรูปภาพแต่ละรูป (เช่น JPEG หรือ PNG) เช่นเดียวกับเสียง ให้ใช้ `realtimeInput` กับ `Blob` โดยระบุ `mimeType` ที่ถูกต้อง

### Python

```
# Inside the websocket context
async def send_video_frame(websocket, frame_bytes, mime_type="image/jpeg"):
    import base64
    encoded_data = base64.b64encode(frame_bytes).decode('utf-8')
    video_message = {
        "realtimeInput": {
            "video": {
                "data": encoded_data,
                "mimeType": mime_type
            }
        }
    }
    await websocket.send(json.dumps(video_message))
    # print("Sent video frame")

# Assuming 'frame' is your JPEG-encoded image bytes
# await send_video_frame(websocket, frame)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
function sendVideoFrame(frame, mimeType = 'image/jpeg') {
  if (websocket.readyState === WebSocket.OPEN) {
    const videoMessage = {
      realtimeInput: {
        video: {
          data: frame.toString('base64'),
          mimeType: mimeType
        }
      }
    };
    websocket.send(JSON.stringify(videoMessage));
    // console.log('Sent video frame');
  }
}
// Example usage: sendVideoFrame(jpegBuffer);
```

ดูตัวอย่างวิธีรับวิดีโอจากอุปกรณ์ไคลเอ็นต์ (เช่น เบราว์เซอร์) ได้ที่ตัวอย่างตั้งแต่ต้นจนจบใน [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222)

## รับคำตอบ

WebSocket จะส่งข้อความ [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=th#bidigeneratecontentservermessage) กลับมา คุณต้องแยกวิเคราะห์ข้อความ JSON เหล่านี้และจัดการเนื้อหาประเภทต่างๆ

### Python

```
# Inside the websocket context, in a receive loop
async def receive_loop(websocket):
    async for message in websocket:
        response = json.loads(message)
        print("Received:", response)

        if "serverContent" in response:
            server_content = response["serverContent"]
            # Receiving Audio
            if "modelTurn" in server_content and "parts" in server_content["modelTurn"]:
                for part in server_content["modelTurn"]["parts"]:
                    if "inlineData" in part:
                        audio_data_b64 = part["inlineData"]["data"]
                        # Process or play the base64 encoded audio data
                        # audio_data = base64.b64decode(audio_data_b64)
                        print(f"Received audio data (base64 len: {len(audio_data_b64)})")

            # Receiving Text Transcriptions
            if "inputTranscription" in server_content:
                print(f"User: {server_content['inputTranscription']['text']}")
            if "outputTranscription" in server_content:
                print(f"Gemini: {server_content['outputTranscription']['text']}")

        # Handling Tool Calls
        if "toolCall" in response:
            await handle_tool_call(websocket, response["toolCall"])

# Example usage: await receive_loop(websocket)
```

### JavaScript

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);

  if (response.serverContent) {
    const serverContent = response.serverContent;
    // Receiving Audio
    if (serverContent.modelTurn?.parts) {
      for (const part of serverContent.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data; // Base64 encoded string
          // Process or play audioData
          console.log(`Received audio data (base64 len: ${audioData.length})`);
        }
      }
    }

    // Receiving Text Transcriptions
    if (serverContent.inputTranscription) {
      console.log('User:', serverContent.inputTranscription.text);
    }
    if (serverContent.outputTranscription) {
      console.log('Gemini:', serverContent.outputTranscription.text);
    }
  }

  // Handling Tool Calls
  if (response.toolCall) {
    handleToolCall(response.toolCall);
  }
};
```

ดูตัวอย่างวิธีจัดการการตอบกลับได้ที่ตัวอย่างแบบครบวงจรใน [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75)

## จัดการการเรียกใช้เครื่องมือ

เมื่อโมเดลขอการเรียกใช้เครื่องมือ [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=th#bidigeneratecontentservermessage) จะมีฟิลด์ `toolCall` คุณต้องเรียกใช้ฟังก์ชันในเครื่องและส่งผลลัพธ์กลับไปยัง WebSocket โดยใช้ข้อความ [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=th#bidigeneratecontenttoolresponse)

### Python

```
# Placeholder for your tool function
def my_tool_function(args):
    print(f"Executing tool with args: {args}")
    # Implement your tool logic here
    return {"status": "success", "data": "some result"}

async def handle_tool_call(websocket, tool_call):
    function_responses = []
    for fc in tool_call["functionCalls"]:
        # 1. Execute the function locally
        try:
            result = my_tool_function(fc.get("args", {}))
            response_data = {"result": result}
        except Exception as e:
            print(f"Error executing tool {fc['name']}: {e}")
            response_data = {"error": str(e)}

        # 2. Prepare the response
        function_responses.append({
            "name": fc["name"],
            "id": fc["id"],
            "response": response_data
        })

    # 3. Send the tool response back to the session
    tool_response_message = {
        "toolResponse": {
            "functionResponses": function_responses
        }
    }
    await websocket.send(json.dumps(tool_response_message))
    print("Sent tool response")

# This function is called within the receive_loop when a toolCall is detected.
```

### JavaScript

```
// Placeholder for your tool function
function myToolFunction(args) {
  console.log(`Executing tool with args:`, args);
  // Implement your tool logic here
  return { status: 'success', data: 'some result' };
}

function handleToolCall(toolCall) {
  const functionResponses = [];
  for (const fc of toolCall.functionCalls) {
    // 1. Execute the function locally
    let result;
    try {
      result = myToolFunction(fc.args || {});
    } catch (e) {
      console.error(`Error executing tool ${fc.name}:`, e);
      result = { error: e.message };
    }

    // 2. Prepare the response
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }

  // 3. Send the tool response back to the session
  if (websocket.readyState === WebSocket.OPEN) {
    const toolResponseMessage = {
      toolResponse: {
        functionResponses: functionResponses
      }
    };
    websocket.send(JSON.stringify(toolResponseMessage));
    console.log('Sent tool response');
  } else {
    console.warn('WebSocket not open to send tool response.');
  }
}
// This function is called within websocket.onmessage when a toolCall is detected.
```

## ขั้นตอนถัดไป

- อ่านคู่มือ[ความสามารถ](https://ai.google.dev/gemini-api/docs/live-guide?hl=th)ของ Live API ฉบับเต็มเพื่อดูความสามารถและการกำหนดค่าที่สำคัญ รวมถึงการตรวจหากิจกรรมเสียงและฟีเจอร์เสียงดั้งเดิม
- อ่านคำแนะนำ[การใช้เครื่องมือ](https://ai.google.dev/gemini-api/docs/live-tools?hl=th)เพื่อดูวิธีผสานรวม Live API กับเครื่องมือและการเรียกใช้ฟังก์ชัน
- อ่านคู่มือ[การจัดการเซสชัน](https://ai.google.dev/gemini-api/docs/live-session?hl=th)เพื่อจัดการการสนทนาที่ใช้เวลานาน
- อ่านคู่มือ[โทเค็นชั่วคราว](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=th)เพื่อดูการตรวจสอบสิทธิ์ที่ปลอดภัยในแอปพลิเคชัน[ไคลเอ็นต์ต่อเซิร์ฟเวอร์](#implementation-approach)
- ดูข้อมูลเพิ่มเติมเกี่ยวกับ WebSockets API พื้นฐานได้ที่[เอกสารอ้างอิง WebSockets API](https://ai.google.dev/api/live?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-23 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-23 UTC"],[],[]]
