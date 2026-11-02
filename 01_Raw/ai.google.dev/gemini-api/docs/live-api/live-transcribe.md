---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=th
fetched_at: 2026-11-02T07:01:32.804170+00:00
title: "\u0e01\u0e32\u0e23\u0e16\u0e2d\u0e14\u0e40\u0e2a\u0e35\u0e22\u0e07\u0e2a\u0e14\u0e14\u0e49\u0e27\u0e22 Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การถอดเสียงสดด้วย Gemini Live API

Gemini Live API รองรับการแปลงเสียงพูดเป็นข้อความแบบเรียลไทม์ที่มีเวลาในการตอบสนองต่ำโดยใช้โมเดล [`gemini-3.5-transcribe-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=th) การเชื่อมต่อกับ Live API ผ่าน WebSockets หรือการใช้ Google Gen AI SDK ช่วยให้คุณสตรีมอินพุตเสียงอย่างต่อเนื่องและรับการถอดข้อความแบบเรียลไทม์ที่เพิ่มขึ้นเรื่อยๆ เมื่อมีการพูดได้

[ลองใช้ Live Transcribe ใน Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-transcribe-live&hl=th)
[เปิด Colab Cookbookcode](https://github.com/google-gemini/cookbook)
[ใช้ทักษะของ Agent การเขียนโค้ดterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th#gemini-live-api-dev)

การใช้ประโยชน์จาก Gemini Live API ช่วยให้แพลตฟอร์มสำหรับนักพัฒนาซอฟต์แวร์ เช่น
[Agora](https://docs.agora.io/en/ai/models/asr/gemini),
[Fishjam](https://docs.fishjam.io/tutorials/gemini-live-integration),
[LiveKit](https://docs.livekit.io/agents/models/stt/gemini/),
[Pipecat](https://docs.pipecat.ai/api-reference/server/services/stt/google),
[Vercel](https://vercel.com/docs/ai-gateway/modalities/speech-to-text) และ
[Vision Agents](https://visionagents.ai/integrations/stt/gemini)
ช่วยให้นักพัฒนาซอฟต์แวร์สร้างและติดตั้งใช้งานอินเทอร์เฟซที่ขับเคลื่อนด้วยเสียงประสิทธิภาพสูงได้อย่างง่ายดาย แพลตฟอร์มเหล่านี้จะจัดการโครงสร้างพื้นฐานสตรีมมิงสื่อแบบเรียลไทม์ที่ซับซ้อนเบื้องหลัง เพื่อให้นักพัฒนาแอปมุ่งเน้นไปที่การสร้างประสบการณ์ของผู้ใช้ได้อย่างเต็มที่

## Live Transcribe เทียบกับเจ้าหน้าที่บริการลูกค้า

แม้ว่าทั้ง 2 อย่างจะใช้การเชื่อมต่อสตรีมมิงแบบ 2 ทิศทางของ Live API แต่ Live Transcription จะทำงานเป็นไปป์ไลน์การจดจำเสียงพูดที่มีเวลาในการตอบสนองต่ำโดยเฉพาะ แทนที่จะเป็น Agent แบบสนทนา

| ฟีเจอร์ | ตัวแทนแบบเรียลไทม์ | Live Transcribe |
| --- | --- | --- |
| **บทบาทหลัก** | ผู้ช่วยแบบสนทนาที่ฟัง ให้เหตุผล และพูดโต้ตอบได้ | ไปป์ไลน์การแปลงเสียงพูดเป็นข้อความแบบเรียลไทม์ที่ถอดเสียงจากเสียงที่เข้ามา |
| **รูปแบบการตอบกลับ** | เสียงพูดและข้อความ (`response_modalities=["AUDIO"]`) | การถอดเสียงเป็นคำแบบสตรีมมิง (`response_modalities=["TEXT"]`) |
| **รูปแบบการโต้ตอบ** | การสนทนาแบบผลัดกันพูดพร้อมการตรวจจับการหยุดชั่วคราวและการขัดจังหวะ | การประมวลผลสตรีมอย่างต่อเนื่องขณะที่ผู้พูดพูด |
| **ฟีเจอร์ที่รองรับ** | การเรียกใช้ฟังก์ชัน, Google Search, คำสั่งของระบบ, การถอดเสียงอินพุตด้วยการให้น้ำหนักคำพูด (`custom_vocabulary`) ใน `gemini-3.8-live` | การให้น้ำหนักเสียงพูด (`custom_vocabulary`), การตรวจจับภาษา, VAD แบบไฮบริดและแบบแมนนวล, การถอดเสียงอัจฉริยะ |
| **สตรีมอินพุต** | หลายรูปแบบ: เสียง วิดีโอ รูปภาพ ข้อความ | อินพุตเสียง (PCM 16 บิตแบบข้อมูลดิบ) |

## เริ่มต้นใช้งาน

ตัวอย่างต่อไปนี้แสดงวิธีเปิดเซสชันสตรีมมิงแบบ 2 ทิศทางด้วย `gemini-3.5-transcribe-live` และรับการถอดเสียงเป็นคำแบบเรียลไทม์

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.5-transcribe-live"

config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],  # Automatic language detection
    ),
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session established with Live Transcription")

        # Receive transcription events
        async for response in session.receive():
            server_content = response.server_content
            if server_content and server_content.input_transcription:
                print("Transcript:", server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-transcribe-live';

const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [], // Automatic language detection
  },
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.log('Connected to Live Transcription'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Transcript:', content.inputTranscription.text);
        }
      },
      onerror: (e) => console.error('Error:', e.message),
      onclose: (e) => console.log('Connection closed:', e.reason),
    },
  });
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-transcribe-live";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['TEXT'],
      },
      inputAudioTranscription: {
        languageCodes: []
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.inputTranscription) {
    console.log('Transcript:', content.inputTranscription.text);
  }
};
```

## การถอดเสียงเป็นคำชั่วคราวและแบบสรุป

เมื่อสตรีมเสียงเข้าสู่ Live API เซิร์ฟเวอร์จะส่งช่องการถอดเสียงเป็นคำ 2 ช่องที่เสริมกันภายใน `server_content` ดังนี้

- **`interim_input_transcription`**: สมมติฐานบางส่วนที่มีเวลาในการตอบสนองต่ำและเป็นการคาดเดา ซึ่งจะอัปเดตขณะที่ผู้พูดกำลังพูดอยู่ การอัปเดตบางส่วนเหล่านี้จะเกิดขึ้นอย่างรวดเร็วโดยมีความล่าช้าเพียงเล็กน้อย ใช้ `interim_input_transcription` เพื่อแสดงผลคำบรรยาย UI แบบสดที่ปรับเปลี่ยนตามอุปกรณ์หรือคำบรรยายตัวอย่าง
- **`input_transcription`**: ข้อความถอดเสียงที่สรุปแล้วซึ่งแสดงเมื่อผู้พูดหยุดชั่วคราว พูดจบ หรือคำพูดได้รับการสรุปแล้ว เมื่อแสดงผลแล้ว ข้อความนี้จะแสดงถึงการถอดเสียงเป็นคำที่เชื่อถือได้ของโมเดลสำหรับส่วนของคำพูดนั้น ในโหมดการถอดเสียงอัจฉริยะ ข้อมูลนี้จะรวมคำตอบที่จัดรูปแบบและปรับให้เหมาะสมแล้ว

ตัวอย่างต่อไปนี้แสดงวิธีแสดงผลลัพธ์บางส่วนชั่วคราวของสตรีมมิงและบันทึกข้อความถอดเสียงสุดท้าย

### Python

```
async def receive_transcripts(session):
    async for response in session.receive():
        server_content = response.server_content
        if not server_content:
            continue

        # Real-time interim hypothesis (updates dynamically as user speaks)
        if server_content.interim_input_transcription:
            interim_text = server_content.interim_input_transcription.text
            print(f"\r[Interim] {interim_text}", end="", flush=True)

        # Finalized transcript (emitted on speech completion)
        if server_content.input_transcription:
            final_text = server_content.input_transcription.text
            print(f"\n[Final] {final_text}")
```

### JavaScript

```
onmessage: (message) => {
  const content = message.serverContent;
  if (!content) return;

  if (content.interimInputTranscription) {
    // Update live subtitle preview on screen
    renderInterimPreview(content.interimInputTranscription.text);
  }

  if (content.inputTranscription) {
    // Append final committed transcript to chat history
    commitFinalTranscript(content.inputTranscription.text);
  }
};
```

### WebSockets

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.interimInputTranscription) {
    console.log('[Interim]:', content.interimInputTranscription.text);
  }
  if (content?.inputTranscription) {
    console.log('[Final]:', content.inputTranscription.text);
  }
};
```

## กำลังส่งเสียง

สตรีมกลุ่มเสียงผ่านการเชื่อมต่อที่ใช้งานอยู่เป็นเสียง PCM แบบข้อมูลดิบ 16 บิต

- **รูปแบบเสียง:** PCM 16 บิตแบบข้อมูลดิบที่ 16kHz (โมโน, Little-Endian)
- **ขนาดกลุ่ม:** ส่งเสียงเป็นกลุ่มๆ ละ 100 มิลลิวินาที (1,024 ถึง 2,048 เฟรม)
- **ประเภท MIME:** `audio/pcm;rate=16000` (หรืออัตราการสุ่มตัวอย่างที่ตรงกัน)

### Python

```
# Stream a raw PCM audio chunk
await session.send_realtime_input(
    audio=types.Blob(
        data=audio_chunk_bytes,
        mime_type="audio/pcm;rate=16000"
    )
)

# Signal the end of the audio stream when finished
await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
// Send base64-encoded PCM audio chunk
session.sendRealtimeInput({
  audio: {
    data: audioChunkBase64,
    mimeType: 'audio/pcm;rate=16000'
  }
});

// Signal stream end
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
// Send base64-encoded PCM audio chunk
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: {
      data: audioChunkBase64,
      mimeType: 'audio/pcm;rate=16000'
    }
  }
}));

// Signal stream end
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

## ฟีเจอร์การถอดเสียงเป็นคำ

### การตรวจหาภาษาอัตโนมัติ

โดยค่าเริ่มต้น การละเว้น `language_codes` หรือการตั้งค่า `language_codes=[]` จะเปิดใช้การระบุภาษาอัตโนมัติ โมเดลจะตรวจจับภาษาที่พูดในคำพูดต่างๆ แบบไดนามิก ซึ่งรวมถึงการสนทนาหลายภาษาและการสลับภาษา

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### คำแนะนำภาษาที่เฉพาะเจาะจง

ระบุรหัสภาษา BCP-47 ที่ชัดเจน (เช่น `["es-ES"]` สำหรับภาษาสเปน หรือ `["fr-FR"]` สำหรับภาษาฝรั่งเศส) เพื่อให้น้ำหนักการจดจำไปยังภาษาที่เฉพาะเจาะจง (ดู[ภาษาที่รองรับ](#supported-languages))

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: ['es-ES'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: ['es-ES'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### การให้น้ำหนักคำศัพท์ที่กำหนดเอง

ระบุรายการวลี คำนามเฉพาะ ชื่อแบรนด์ หรือคำศัพท์ทางเทคนิคได้สูงสุด 1,000 รายการใน `custom_vocabulary` เพื่อให้น้ำหนักการจดจำเสียงพูดกับคำศัพท์เฉพาะ (โดยปกติแล้วจะได้ผลลัพธ์ที่ดีที่สุดเมื่อมีคำศัพท์ไม่เกิน 100 คำ)

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
        custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
    customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
      customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### การถอดเสียงเป็นคำอัจฉริยะ

กำหนดค่าการจัดรูปแบบเอาต์พุตการถอดเสียงเป็นคำโดยใช้พารามิเตอร์ `mode` ใน `input_audio_transcription` ดังนี้

- **`VERBATIM` (ค่าเริ่มต้น)**: สร้างข้อความถอดเสียงตามคำพูดทุกคำอย่างตรงตัว โดยคงคำพูดที่ไม่มีความหมาย ("อืม" "เอ่อ" "แบบว่า") การกล่าวซ้ำๆ และการพูดผิดไว้
- **`SMART` (การถอดเสียงเป็นคำอัจฉริยะ)**: ปรับแต่งและจัดโครงสร้างข้อความถอดเสียงเพื่อให้อ่านง่ายขึ้น

  - **การนำคำติดขัดออก**: นำคำพูดที่ไม่มีความหมาย การพูดติดอ่าง และการพูดผิดแล้วเริ่มใหม่ทั้งหมดออก
  - **การแก้ไขคำพูดของตัวเองในบทสนทนา**: แก้ไขคำพูดได้อย่างเป็นธรรมชาติ
  - **การจัดรูปแบบที่มีโครงสร้าง**: จัดรูปแบบรายการ หัวข้อย่อย ตัวเลข วันที่ และการขึ้นย่อหน้าใหม่โดยอัตโนมัติ
  - **ไวยากรณ์และการใช้อักษรตัวพิมพ์ใหญ่**: ใช้การใช้อักษรตัวพิมพ์ใหญ่และเครื่องหมายวรรคตอนที่เป็นธรรมชาติ

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        mode="SMART",
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    mode: 'SMART',
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      mode: 'SMART',
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

## กลยุทธ์การตรวจจับกิจกรรมเสียงพูด (VAD)

### VAD อัตโนมัติ (ค่าเริ่มต้น)

โดยค่าเริ่มต้น การตรวจจับกิจกรรมเสียงพูดอัตโนมัติฝั่งเซิร์ฟเวอร์จะตรวจจับเมื่อผู้พูดเริ่มและหยุดพูด

### VAD แบบผสมผสาน

[VAD แบบไฮบริด](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=th#hybrid-vad)รวมการตรวจหาการเริ่มพูดอัตโนมัติฝั่งเซิร์ฟเวอร์เข้ากับการตรวจหาการสิ้นสุดการพูดฝั่งไคลเอ็นต์เพื่อสรุปเทิร์นโดยไม่มีเวลาในการตอบสนอง

1. **VAD อัตโนมัติฝั่งเซิร์ฟเวอร์ยังคงเปิดใช้อยู่**เพื่อตรวจหาจุดเริ่มต้นของคำพูดอย่างแม่นยำด้วยการเพิ่มระยะเวลาเสียงนำหน้า เพื่อป้องกันไม่ให้คำแรกถูกตัดออก
2. **VAD ฝั่งไคลเอ็นต์ตรวจพบความเงียบ**: เมื่อ VAD ในอุปกรณ์ตรวจพบว่าผู้พูดหยุดพูด ไคลเอ็นต์จะส่งสัญญาณ `audio_stream_end` ทันที
3. **การสรุปผลอย่างรวดเร็ว**: เซิร์ฟเวอร์จะถือว่า `audio_stream_end` เป็นพรอมต์สรุปผลเทิร์นทันที โดยข้ามเวลารอความเงียบฝั่งเซิร์ฟเวอร์เริ่มต้น และแสดงผลข้อความถอดเสียงที่สรุปผลแล้วโดยมีเวลาในการตอบสนองน้อยที่สุด
4. **สำรอง**: หาก VAD ฝั่งไคลเอ็นต์ไม่ทำงาน VAD ฝั่งเซิร์ฟเวอร์จะทำหน้าที่เป็นตัวสำรองอัตโนมัติ

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Stream audio chunks...
    await session.send_realtime_input(
        audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000")
    )

    # When client-side VAD detects end of speech, send audio_stream_end:
    await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {},
};

// Stream audio...
session.sendRealtimeInput({
  audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
});

// When client VAD detects end of speech, send audioStreamEnd:
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
  }
}));

// When client VAD detects end of speech, send audioStreamEnd:
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

### VAD แบบแมนนวล (กดเพื่อพูด)

สำหรับอินเทอร์เฟซวิทยุสื่อสารหรือปุ่มกดเพื่อพูด ให้ปิดใช้ VAD อัตโนมัติทั้งหมดและควบคุมขอบเขตการพูดอย่างชัดเจนโดยใช้ `activity_start` และ `activity_end` ดังนี้

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    realtime_input_config=types.RealtimeInputConfig(
        automatic_activity_detection=types.AutomaticActivityDetection(
            disabled=True
        )
    ),
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Button pressed: signal speech start
    await session.send_realtime_input(activity_start=types.ActivityStart())

    # Stream audio chunks...
    await session.send_realtime_input(audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000"))

    # Button released: signal speech end
    await session.send_realtime_input(activity_end=types.ActivityEnd())
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    },
  },
  inputAudioTranscription: {},
};

// Signal speech start
session.sendRealtimeInput({ activityStart: {} });

// Stream audio...

// Signal speech end
session.sendRealtimeInput({ activityEnd: {} });
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    realtimeInputConfig: {
      automaticActivityDetection: {
        disabled: true,
      },
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Button pressed: signal speech start
websocket.send(JSON.stringify({
  realtimeInput: {
    activityStart: {},
  },
}));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' },
  },
}));

// Button released: signal speech end
websocket.send(JSON.stringify({
  realtimeInput: {
    activityEnd: {},
  },
}));
```

## โทเค็นแบบชั่วคราวในแอปพลิเคชันไคลเอ็นต์

สำหรับแอปพลิเคชันแบบไคลเอ็นต์กับเซิร์ฟเวอร์ (เช่น แอปบนอุปกรณ์เคลื่อนที่หรือเว็บแอปที่สตรีมจากไมโครโฟนโดยตรง) ให้ใช้[โทเค็นชั่วคราว](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=th)เพื่อหลีกเลี่ยงการเปิดเผยคีย์ API ในโค้ดฝั่งไคลเอ็นต์

สร้างโทเค็นชั่วคราวแบบจำกัดในเซิร์ฟเวอร์ก่อนเริ่มการเชื่อมต่อไคลเอ็นต์ โดยทำดังนี้

### Python

```
import datetime
from google import genai

client = genai.Client()
expire_time = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=30)

token = client.auth_tokens.create(
    config={
        "uses": 1,
        "expire_time": expire_time,
        "live_connect_constraints": {
            "model": "gemini-3.5-transcribe-live",
            "config": {
                "response_modalities": ["TEXT"],
                "input_audio_transcription": {
                    "language_codes": [],
                },
            },
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
  config: {
    uses: 1,
    expireTime: expireTime,
    liveConnectConstraints: {
      model: 'gemini-3.5-transcribe-live',
      config: {
        responseModalities: ['TEXT'],
        inputAudioTranscription: {
          languageCodes: [],
        },
      },
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.5-transcribe-live",
      "config": {
        "responseModalities": ["TEXT"],
        "inputAudioTranscription": {
          "languageCodes": []
        }
      }
    }
  }'
```

## ภาษาที่รองรับ

Gemini 3.5 Transcribe Live รองรับภาษาและรหัสภาษา BCP-47 ต่อไปนี้

| ภาษา | รหัส BCP-47 | ภาษา | รหัส BCP-47 |
| --- | --- | --- | --- |
| อาฟรีกานส์ | `af-ZA` | ญี่ปุ่น | `ja-JP` |
| อัมฮาริก | `am-ET` | ชวา | `jv-ID` |
| อาหรับ (อียิปต์) | `ar-EG` | กาบูแวร์ดีอานู | `kea-CV` |
| อาร์เมเนีย | `hy-AM` | กันนาดา | `kn-IN` |
| อัสสัม | `as-IN` | คาซัค | `kk-KZ` |
| อาร์เซอร์ไบจัน | `az-AZ` | เกาหลี | `ko-KR` |
| Belarusian | `be-BY` | คีร์กิซ | `ky-KG` |
| เบงกาลี (บังกลาเทศ) | `bn-BD` | ลัตเวีย | `lv-LV` |
| เบงกาลี (อินเดีย) | `bn-IN` | ลิงกาลา | `ln-CD` |
| บอสเนีย | `bs-BA` | ลิทัวเนีย | `lt-LT` |
| บัลแกเรีย | `bg-BG` | มาซีโดเนีย | `mk-MK` |
| บัลแกเรีย (อาโรมาเนียน) | `rup-BG` | มาเลย์ | `ms-MY` |
| พม่า | `my-MM` | มาลายาลัม | `ml-IN` |
| จีนกวางตุ้ง (ตัวเต็ม) | `yue-Hant-HK` | ภาษามอลตา | `mt-MT` |
| คาตาลัน | `ca-ES` | จีนกลาง (ตัวย่อ) | `cmn-Hans-CN` |
| ซีบัวโน | `ceb` | มราฐี | `mr-IN` |
| เขมรตอนกลาง | `km-KH` | มองโกเลีย | `mn-MN` |
| โครเอเชีย | `hr-HR` | เนปาล | `ne-NP` |
| เช็ก | `cs-CZ` | นอร์เวย์ | `nb-NO` |
| เดนมาร์ก | `da-DK` | โอริยา | `or-IN` |
| ดัตช์ | `nl-NL` | โปแลนด์ | `pl-PL` |
| อังกฤษ (บริเตนใหญ่) | `en-GB` | โปรตุเกส (บราซิล) | `pt-BR` |
| อังกฤษ (อินเดีย) | `en-IN` | โปรตุเกส (โปรตุเกส) | `pt-PT` |
| อังกฤษ (สหรัฐอเมริกา) | `en-US` | ปัญจาบ | `pa-IN` |
| เอสโตเนีย | `et-EE` | ปัญจาบ (อักษรคุรมุขี) | `pa-Guru-IN` |
| ฟาร์ซี | `fa-IR` | โรมาเนีย | `ro-RO` |
| ฟิลิปปินส์ | `fil-PH` | รัสเซีย | `ru-RU` |
| ฟินแลนด์ | `fi-FI` | เซอร์เบีย | `sr-RS` |
| ฝรั่งเศส | `fr-FR` | สินธี (อักษรอาหรับ) | `sd-Arab-IN` |
| กาลิเชียน | `gl-ES` | สโลวัก | `sk-SK` |
| จอร์เจีย | `ka-GE` | สโลวีเนีย | `sl-SI` |
| เยอรมัน | `de-DE` | สเปน (ลาตินอเมริกา) | `es-419` |
| กรีก | `el-GR` | สเปน (สหรัฐอเมริกา) | `es-US` |
| คุชราต | `gu-IN` | สวาฮีลี (เคนยา) | `sw-KE` |
| เฮาซา | `ha-NG` | สวีเดน | `sv-SE` |
| ฮีบรู | `he-IL` | ทาจิก | `tg-TJ` |
| ฮินดี | `hi-IN` | เตลูกู | `te-IN` |
| ฮังการี | `hu-HU` | ไทย | `th-TH` |
| ไอซ์แลนด์ | `is-IS` | ตุรกี | `tr-TR` |
| อังกฤษแบบอินเดีย | `en-IN` | ยูเครน | `uk-UA` |
| อินโดนีเซีย | `id-ID` | อุซเบก | `uz-UZ` |
| อิตาลี | `it-IT` | เวียดนาม | `vi-VN` |

## ข้อมูลอ้างอิงพารามิเตอร์

กำหนดค่า Live Transcribe โดยใช้ช่องใน `input_audio_transcription` และ `realtime_input_config` ดังนี้

| พารามิเตอร์ | ประเภท | คำอธิบาย |
| --- | --- | --- |
| `language_codes` | อาร์เรย์ของสตริง | รหัสภาษา BCP-47 (เช่น `["en-US"]`) หากละเว้นหรือเว้นว่างไว้ (`[]`) โมเดลจะตรวจจับภาษาและจัดการคำพูดหลายภาษาโดยอัตโนมัติ |
| `custom_vocabulary` | อาร์เรย์ของสตริง | คำที่กำหนดเอง ตัวย่อ ชื่อแบรนด์ หรือคำนามเฉพาะสูงสุด 1,000 คำเพื่อให้น้ำหนักกับการจดจำคำพูด |
| `mode` | สตริง | โหมดการถอดเสียงเป็นคำ: `"VERBATIM"` (ค่าเริ่มต้น) หรือ `"SMART"` (การถอดเสียงเป็นคำอัจฉริยะ) เมื่อตั้งค่าเป็น `"SMART"` โมเดลจะนำคำพูดที่ไม่มีความหมายออก จัดรูปแบบรายการ และแก้ไขความไม่คล่องแคล่ว |
| `automatic_activity_detection.disabled` | บูลีน | ตั้งค่าเป็น `true` เพื่อปิดใช้การตรวจจับกิจกรรมเสียงพูดโดยอัตโนมัติ และส่งสัญญาณ `activityStart` และ `activityEnd` ด้วยตนเอง |

### ช่องการตอบกลับของเซิร์ฟเวอร์

| ช่อง | คำอธิบาย |
| --- | --- |
| `server_content.interim_input_transcription` | สมมติฐานการถอดเสียงเป็นคำบางส่วนชั่วคราวที่มีเวลาในการตอบสนองต่ำซึ่งส่งออกมาอย่างต่อเนื่องขณะที่ผู้ใช้กำลังพูดอยู่ |
| `server_content.input_transcription` | ระบบจะแสดงข้อความถอดเสียงที่เชื่อถือได้และสรุปแล้วเมื่อการพูดจบลง |

## ข้อจำกัด

- **ระยะเวลาเซสชัน:** เซสชัน Live Transcribe รองรับการสตรีมต่อเนื่องสูงสุด 10 นาที
- **การระบุตัวผู้พูด:** ระบบไม่รองรับการระบุตัวผู้พูดในเซสชันไลฟ์สด สำหรับการแยกเสียงผู้พูด ให้ใช้ปลายทาง[การถอดเสียง](https://ai.google.dev/gemini-api/docs/transcribe?hl=th#speaker-diarization)ที่ไม่ใช่สตรีมมิง
- **การประทับเวลาระดับคำ:** Live API ไม่รองรับการประทับเวลาระดับคำ Live API จะแสดงการประทับเวลาระดับคำพูด (`interim_input_transcription` และ `input_transcription`)
- **คำศัพท์ที่กำหนดเอง:** คุณสามารถระบุคำศัพท์ได้สูงสุด 1,000 คำใน `custom_vocabulary` แต่โดยทั่วไปแล้วผลลัพธ์ที่ดีที่สุดจะได้จากคำศัพท์ไม่เกิน 100 คำ
- **ความเข้ากันได้ของโหมด:** การถอดเสียงอัจฉริยะ (`"mode": "SMART"`) จะนำคำพูดที่ไม่มีความหมายออกและจัดรูปแบบข้อความที่คำนึงถึงเจตนา แต่ไม่สามารถใช้ร่วมกับคำอธิบายประกอบคำได้

## ขั้นตอนถัดไป

- อ่าน[เอกสารประกอบของ Gemini Transcribe](https://ai.google.dev/gemini-api/docs/transcribe?hl=th) สำหรับไฟล์เสียงที่ไม่ใช่สตรีมมิง
- อ่าน[ภาพรวมของ Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th) สำหรับตัวแทนเสียงแบบสนทนา
- อ่าน[คู่มือการแปลสด](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=th)สำหรับการแปลเสียงพูดเป็นเสียงพูดแบบเรียลไทม์
- ดูราคาการสตรีม Live API ได้ที่[หน้าการกำหนดราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th#gemini-3.5-transcribe-live)
- สำรวจ[คู่มือความสามารถของ Live API](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-29 UTC"],[],[]]
