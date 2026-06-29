---
source_url: https://ai.google.dev/gemini-api/docs/live-api/tools?hl=th
fetched_at: 2026-06-29T05:26:59.665974+00:00
title: "\u0e01\u0e32\u0e23\u0e43\u0e0a\u0e49\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e21\u0e37\u0e2d\u0e01\u0e31\u0e1a Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การใช้เครื่องมือกับ Live API

การใช้เครื่องมือช่วยให้ Live API ทำได้มากกว่าแค่การสนทนา โดยช่วยให้ API
ดำเนินการในโลกแห่งความจริงและดึงบริบทภายนอกเข้ามาได้ในขณะที่ยังคง
การเชื่อมต่อแบบเรียลไทม์
คุณกำหนดเครื่องมือต่างๆ เช่น [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
และ [Google Search](https://ai.google.dev/gemini-api/docs/grounding?hl=th) ได้ด้วย Live API

## ภาพรวมของเครื่องมือที่รองรับ

ต่อไปนี้เป็นภาพรวมโดยย่อของเครื่องมือที่ใช้ได้สำหรับโมเดล Live API

| เครื่องมือ | เวอร์ชันตัวอย่าง Gemini 3.1 Flash Live | เวอร์ชันตัวอย่างของ Gemini 2.5 Flash |
| --- | --- | --- |
| **ค้นหา** | สิ่งที่ทำได้ | สิ่งที่ทำได้ |
| **การเรียกใช้ฟังก์ชัน** | รองรับ (ซิงโครนัสเท่านั้น) | รองรับ (แบบเรียลไทม์และ[ไม่เรียลไทม์](#async-function-calling)) |
| **Google Maps** | สิ่งที่ทำไม่ได้ | สิ่งที่ทำไม่ได้ |
| **การรันโค้ด** | สิ่งที่ทำไม่ได้ | สิ่งที่ทำไม่ได้ |
| **บริบทของ URL** | สิ่งที่ทำไม่ได้ | สิ่งที่ทำไม่ได้ |

## การเรียกใช้ฟังก์ชัน

Live API รองรับการเรียกใช้ฟังก์ชันเช่นเดียวกับคำขอการสร้างเนื้อหาปกติ
การเรียกใช้ฟังก์ชันช่วยให้ Live API โต้ตอบกับข้อมูลและโปรแกรมภายนอกได้ ซึ่งจะช่วยเพิ่มความสามารถของแอปพลิเคชันได้อย่างมาก

คุณกําหนดการประกาศฟังก์ชันเป็นส่วนหนึ่งของการกําหนดค่าเซสชันได้
หลังจากได้รับฟังก์ชันคอลแล้ว ไคลเอ็นต์ควรตอบกลับด้วยรายการออบเจ็กต์
`FunctionResponse`โดยใช้เมธอด `session.send_tool_response`

ดูข้อมูลเพิ่มเติมได้ที่[บทแนะนำการเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)

### Python

```
import asyncio
import wave
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.1-flash-live-preview"

# Simple function definitions
turn_on_the_lights = {"name": "turn_on_the_lights"}
turn_off_the_lights = {"name": "turn_off_the_lights"}

tools = [{"function_declarations": [turn_on_the_lights, turn_off_the_lights]}]
config = {"response_modalities": ["AUDIO"], "tools": tools}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        prompt = "Turn on the lights please"
        await session.send_client_content(turns={"parts": [{"text": prompt}]})

        wf = wave.open("audio.wav", "wb")
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)  # Output is 24kHz

        async for response in session.receive():
            if response.data is not None:
                wf.writeframes(response.data)
            elif response.tool_call:
                print("The tool was called")
                function_responses = []
                for fc in response.tool_call.function_calls:
                    function_response = types.FunctionResponse(
                        id=fc.id,
                        name=fc.name,
                        response={ "result": "ok" } # simple, hard-coded function response
                    )
                    function_responses.append(function_response)

                await session.send_tool_response(function_responses=function_responses)

        wf.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';  // npm install wavefile
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

// Simple function definitions
const turn_on_the_lights = { name: "turn_on_the_lights" } // , description: '...', parameters: { ... }
const turn_off_the_lights = { name: "turn_off_the_lights" }

const tools = [{ functionDeclarations: [turn_on_the_lights, turn_off_the_lights] }]

const config = {
  responseModalities: [Modality.AUDIO],
  tools: tools
}

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      } else if (message.toolCall) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
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

  const inputTurns = 'Turn on the lights please';
  session.sendClientContent({ turns: inputTurns });

  let turns = await handleTurn();

  for (const turn of turns) {
    if (turn.toolCall) {
      console.debug('A tool was called');
      const functionResponses = [];
      for (const fc of turn.toolCall.functionCalls) {
        functionResponses.push({
          id: fc.id,
          name: fc.name,
          response: { result: "ok" } // simple, hard-coded function response
        });
      }

      console.debug('Sending tool response...\n');
      session.sendToolResponse({ functionResponses: functionResponses });
    }
  }

  // Check again for new messages
  turns = await handleTurn();

  // Combine audio data strings and save as wave file
  const combinedAudio = turns.reduce((acc, turn) => {
      if (turn.data) {
          const buffer = Buffer.from(turn.data, 'base64');
          const intArray = new Int16Array(buffer.buffer, buffer.byteOffset, buffer.byteLength / Int16Array.BYTES_PER_ELEMENT);
          return acc.concat(Array.from(intArray));
      }
      return acc;
  }, []);

  const audioBuffer = new Int16Array(combinedAudio);

  const wf = new WaveFile();
  wf.fromScratch(1, 24000, '16', audioBuffer);  // output is 24kHz
  fs.writeFileSync('audio.wav', wf.toBuffer());

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

โมเดลสามารถสร้างการเรียกใช้ฟังก์ชันหลายรายการและโค้ดที่จำเป็นต่อการเชื่อมโยงเอาต์พุตจากพรอมต์เดียว โค้ดนี้จะดำเนินการในสภาพแวดล้อมแซนด์บ็อกซ์
เพื่อสร้างข้อความ [BidiGenerateContentToolCall](https://ai.google.dev/api/live?hl=th#bidigeneratecontenttoolcall) ที่ตามมา

## การเรียกใช้ฟังก์ชันแบบอะซิงโครนัส

การเรียกใช้ฟังก์ชันจะดำเนินการตามลำดับโดยค่าเริ่มต้น ซึ่งหมายความว่าการดำเนินการจะหยุดชั่วคราว
จนกว่าผลลัพธ์ของการเรียกใช้ฟังก์ชันแต่ละรายการจะพร้อมใช้งาน ซึ่งจะช่วยให้ประมวลผลตามลำดับได้ ซึ่งหมายความว่าคุณจะโต้ตอบกับโมเดลต่อไม่ได้ในขณะที่ฟังก์ชันกำลังทำงาน

หากไม่ต้องการบล็อกการสนทนา คุณสามารถบอกโมเดลให้เรียกใช้ฟังก์ชันแบบไม่พร้อมกันได้ โดยคุณต้องเพิ่ม `behavior` ใน
คำจำกัดความของฟังก์ชันก่อน

### Python

```
# Non-blocking function definitions
turn_on_the_lights = {"name": "turn_on_the_lights", "behavior": "NON_BLOCKING"} # turn_on_the_lights will run asynchronously
turn_off_the_lights = {"name": "turn_off_the_lights"} # turn_off_the_lights will still pause all interactions with the model
```

### JavaScript

```
import { GoogleGenAI, Modality, Behavior } from '@google/genai';

// Non-blocking function definitions
const turn_on_the_lights = {name: "turn_on_the_lights", behavior: Behavior.NON_BLOCKING}

// Blocking function definitions
const turn_off_the_lights = {name: "turn_off_the_lights"}

const tools = [{ functionDeclarations: [turn_on_the_lights, turn_off_the_lights] }]
```

`NON-BLOCKING` ช่วยให้ฟังก์ชันทำงานแบบไม่พร้อมกันในขณะที่คุณโต้ตอบกับโมเดลต่อไปได้

จากนั้นคุณต้องบอกโมเดลว่าควรทำงานอย่างไรเมื่อได้รับ
`FunctionResponse` โดยใช้พารามิเตอร์ `scheduling` โดยอาจเป็นอย่างใดอย่างหนึ่งต่อไปนี้

- ขัดจังหวะสิ่งที่กำลังทำอยู่และแจ้งให้คุณทราบเกี่ยวกับคำตอบที่ได้รับทันที
  (`scheduling="INTERRUPT"`)
- รอจนกว่าจะเสร็จสิ้นกับสิ่งที่กำลังทำอยู่
  (`scheduling="WHEN_IDLE"`)
- หรือจะปล่อยไว้และใช้ความรู้นั้นในการสนทนาในภายหลังก็ได้
  (`scheduling="SILENT"`)

### Python

```
# for a non-blocking function definition, apply scheduling in the function response:
  function_response = types.FunctionResponse(
      id=fc.id,
      name=fc.name,
      response={
          "result": "ok",
          "scheduling": "INTERRUPT" # Can also be WHEN_IDLE or SILENT
      }
  )
```

### JavaScript

```
import { GoogleGenAI, Modality, Behavior, FunctionResponseScheduling } from '@google/genai';

// for a non-blocking function definition, apply scheduling in the function response:
const functionResponse = {
  id: fc.id,
  name: fc.name,
  response: {
    result: "ok",
    scheduling: FunctionResponseScheduling.INTERRUPT  // Can also be WHEN_IDLE or SILENT
  }
}
```

## การเชื่อมต่อแหล่งข้อมูลกับ Google Search

คุณเปิดใช้การอ้างอิงจาก Google Search ได้โดยเป็นส่วนหนึ่งของการกำหนดค่าเซสชัน
ซึ่งจะช่วยเพิ่มความแม่นยำของ Live API และป้องกัน
การหลอน ดูข้อมูลเพิ่มเติมได้ที่[บทแนะนำการกราวด์](https://ai.google.dev/gemini-api/docs/grounding?hl=th)

### Python

```
import asyncio
import wave
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.1-flash-live-preview"

tools = [{'google_search': {}}]
config = {"response_modalities": ["AUDIO"], "tools": tools}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        prompt = "When did the last Brazil vs. Argentina soccer match happen?"
        await session.send_client_content(turns={"parts": [{"text": prompt}]})

        wf = wave.open("audio.wav", "wb")
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)  # Output is 24kHz

        async for chunk in session.receive():
            if chunk.server_content:
                if chunk.data is not None:
                    wf.writeframes(chunk.data)

                # The model might generate and execute Python code to use Search
                model_turn = chunk.server_content.model_turn
                if model_turn:
                    for part in model_turn.parts:
                        if part.executable_code is not None:
                            print(part.executable_code.code)

                        if part.code_execution_result is not None:
                            print(part.code_execution_result.output)

        wf.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';  // npm install wavefile
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const tools = [{ googleSearch: {} }]
const config = {
  responseModalities: [Modality.AUDIO],
  tools: tools
}

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      } else if (message.toolCall) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
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

  const inputTurns = 'When did the last Brazil vs. Argentina soccer match happen?';
  session.sendClientContent({ turns: inputTurns });

  let turns = await handleTurn();

  let combinedData = '';
  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.modelTurn && turn.serverContent.modelTurn.parts) {
      for (const part of turn.serverContent.modelTurn.parts) {
        if (part.executableCode) {
          console.debug('executableCode: %s\n', part.executableCode.code);
        }
        else if (part.codeExecutionResult) {
          console.debug('codeExecutionResult: %s\n', part.codeExecutionResult.output);
        }
        else if (part.inlineData && typeof part.inlineData.data === 'string') {
          combinedData += atob(part.inlineData.data);
        }
      }
    }
  }

  // Convert the base64-encoded string of bytes into a Buffer.
  const buffer = Buffer.from(combinedData, 'binary');

  // The buffer contains raw bytes. For 16-bit audio, we need to interpret every 2 bytes as a single sample.
  const intArray = new Int16Array(buffer.buffer, buffer.byteOffset, buffer.byteLength / Int16Array.BYTES_PER_ELEMENT);

  const wf = new WaveFile();
  // The API returns 16-bit PCM audio at a 24kHz sample rate.
  wf.fromScratch(1, 24000, '16', intArray);
  fs.writeFileSync('audio.wav', wf.toBuffer());

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## การรวมเครื่องมือหลายอย่าง

คุณสามารถรวมเครื่องมือหลายอย่างภายใน Live API เพื่อเพิ่มความสามารถของแอปพลิเคชันให้มากยิ่งขึ้นได้

### Python

```
prompt = """
Hey, I need you to do two things for me.

1. Use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024?
2. Then turn on the lights

Thanks!
"""

tools = [
    {"google_search": {}},
    {"function_declarations": [turn_on_the_lights, turn_off_the_lights]},
]

config = {"response_modalities": ["AUDIO"], "tools": tools}

# ... remaining model call
```

### JavaScript

```
const prompt = `Hey, I need you to do two things for me.

1. Use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024?
2. Then turn on the lights

Thanks!
`

const tools = [
  { googleSearch: {} },
  { functionDeclarations: [turn_on_the_lights, turn_off_the_lights] }
]

const config = {
  responseModalities: [Modality.AUDIO],
  tools: tools
}

// ... remaining model call
```

## ขั้นตอนถัดไป

- ดูตัวอย่างเพิ่มเติมของการใช้เครื่องมือกับ Live API ได้ใน
  [ตำราการใช้เครื่องมือ](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=th)
- ดูเรื่องราวทั้งหมดเกี่ยวกับฟีเจอร์และการกำหนดค่าได้จาก[คู่มือความสามารถของ Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-01 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-01 UTC"],[],[]]
