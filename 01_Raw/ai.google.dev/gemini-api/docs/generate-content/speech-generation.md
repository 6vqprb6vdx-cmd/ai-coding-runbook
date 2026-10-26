---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=th
fetched_at: 2026-10-26T06:05:20.993429+00:00
title: "\u0e01\u0e32\u0e23\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e01\u0e32\u0e23\u0e2d\u0e48\u0e32\u0e19\u0e2d\u0e2d\u0e01\u0e40\u0e2a\u0e35\u0e22\u0e07\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21 (TTS) \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)

ส่งความคิดเห็น

# การสร้างการอ่านออกเสียงข้อความ (TTS)

Gemini API สามารถเปลี่ยนอินพุตข้อความเป็นเสียงที่มีผู้พูดคนเดียวหรือหลายคน โดยใช้ความสามารถในการสร้างการอ่านออกเสียงข้อความ (TTS) ของ Gemini
การสร้างการอ่านออกเสียงข้อความ*[ควบคุมได้](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=th#controllable)* ซึ่งหมายความว่าคุณสามารถรวมข้อมูลเมตาของเทิร์นที่มีโครงสร้าง (`speech_metadata`) และแท็กเสียงในบรรทัดเพื่อกำหนด*สไตล์* *สำเนียง* *ความเร็ว* และ*โทน*ของเสียงได้

[ลองใช้ใน Google AI Studio](https://aistudio.google.com/generate-speech?hl=th)

ความสามารถของ TTS แตกต่างจากการสร้างคำพูดที่ให้บริการผ่าน [Live API](https://ai.google.dev/gemini-api/docs/live?hl=th) ซึ่งออกแบบมาสำหรับเสียงแบบโต้ตอบที่ไม่มีโครงสร้าง รวมถึงอินพุตและเอาต์พุตแบบหลายรูปแบบ แม้ว่า Live API จะทำงานได้ดี
ในบริบทการสนทนาแบบไดนามิก แต่ TTS ผ่าน Gemini API
ได้รับการปรับแต่งสำหรับสถานการณ์ที่ต้องมีการอ่านข้อความที่แน่นอนพร้อมการควบคุม
สไตล์และเสียงอย่างละเอียด เช่น การสร้างพอดแคสต์หรือหนังสือเสียง

คู่มือนี้จะแสดงวิธีสร้างเสียงแบบลำโพงเดี่ยวและแบบหลายลำโพงจากข้อความโดยใช้ [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=th)
(`gemini-3.8-flash-tts`) และ
[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=th)
(`gemini-3.8-flash-lite-tts`)

## ก่อนเริ่มต้น

ตรวจสอบว่าคุณใช้โมเดล TTS ของ Gemini ที่ระบุไว้ในส่วน[โมเดลที่รองรับ](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=th#supported-models)
โปรดอ่านหัวข้อ
[เมื่อใดควรใช้โมเดลใด](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=th#when-to-use-which-model)
เพื่อเลือกโมเดลที่ดีที่สุดสำหรับปริมาณงานของคุณ

คุณอาจพบว่าการ[ทดสอบโมเดล TTS ของ Gemini ใน AI Studio](https://aistudio.google.com/generate-speech?hl=th)
มีประโยชน์ก่อนที่จะเริ่มสร้าง

## TTS แบบผู้พูดคนเดียว

หากต้องการแปลงข้อความเป็นเสียงแบบลำโพงเดียวด้วยโมเดล TTS ของ Gemini 3.8 ให้ส่ง
ข้อความถอดเสียงตามคำพูดใน `parts[].text` แนบการจัดรูปแบบระดับการพูดใน
`parts[].speech_metadata` และกำหนดค่าเสียงใน
`speechConfig.voiceConfig` คุณสามารถส่งชื่อเสียงที่สร้างไว้ล่วงหน้า, รหัสคลังเสียงแบบขยาย, รหัส[การออกแบบเสียง](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=th)ที่กำหนดเอง (`voice_...`) หรือรหัส[การจำลองเสียง](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=th) (`voice_...` หรือ `voicekey_...` แบบไม่เก็บสถานะที่ไม่บังคับ)

ตัวอย่างนี้จะบันทึกเสียงเอาต์พุตจากโมเดลในไฟล์ WAV

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.wav
```

## TTS แบบหลายผู้พูด

สำหรับการสนทนาที่มีผู้พูดหลายคน ให้กำหนดค่าผู้พูด 2 คนใน `multiSpeakerVoiceConfig.speakerVoiceConfigs` โดยใช้ `prebuiltVoiceConfig` และส่งการสนทนาแต่ละรอบเป็น `part` แยกกัน โดยมี `speech_metadata` ที่ระบุทั้ง `speaker` และ `style` ระดับรอบที่ไม่บังคับ ดังนี้

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [
            {
                "text": "How's it going today Jane?",
                "speech_metadata": {
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                },
            },
            {
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "speech_metadata": {
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                },
            },
        ],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "multi_speaker_voice_config": {
                "speaker_voice_configs": [
                    {
                        "speaker": "Joe",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Puck"}
                        },
                    },
                    {
                        "speaker": "Jane",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Kore"}
                        },
                    },
                ]
            }
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [
            {
               text: "How's it going today Jane?",
               speechMetadata: {
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               },
            },
            {
               text: 'Not too bad, how about you? Ready to test these new voices?',
               speechMetadata: {
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               },
            },
         ],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            multiSpeakerVoiceConfig: {
               speakerVoiceConfigs: [
                  {
                     speaker: 'Joe',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Puck' },
                     },
                  },
                  {
                     speaker: 'Jane',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Kore' },
                     },
                  },
               ],
            },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [
        {
          "text": "How'\''s it going today Jane?",
          "speech_metadata": {
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }
        },
        {
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "speech_metadata": {
            "speaker": "Jane",
            "style": "calm and relaxed"
          }
        }
      ]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "multiSpeakerVoiceConfig": {
          "speakerVoiceConfigs": [
            {
              "speaker": "Joe",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Puck" }
              }
            },
            {
              "speaker": "Jane",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Kore" }
              }
            }
          ]
        }
      }
    }
  }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
      base64 --decode > out.wav
```

## ควบคุมสไตล์การพูดด้วยข้อมูลเมตาและแท็ก

TTS ของ Gemini 3.8 จะถือว่าฟิลด์ `text` เป็นสำเนาที่ตรงตามต้นฉบับอย่างเคร่งครัด หากต้องการ
ควบคุมการนำเสนอโดยไม่ต้องอ่านคำแนะนำบนเวที
ให้แบ่งคำสั่งตามขอบเขตดังนี้

- **การแสดงออกที่คงที่ในระดับเทิร์น (`speech_metadata.style`):** ใส่อารมณ์ รูปแบบการแสดงออก ฉันทลักษณ์ จังหวะ และระดับเสียงที่ใช้ตลอดทั้งเทิร์นใน `speech_metadata.style` (เช่น `"style": "whispered urgently"`, `"style": "out of breath"` หรือ `"style": "warm and enthusiastic"`)
- **เหตุการณ์ ณ จุดใดจุดหนึ่ง (แท็กในบรรทัด):** วางเสียงร้องที่ไม่มีคำพูดหรือหยุดชั่วคราวไว้ในข้อความถอดเสียงโดยตรงโดยใช้เครื่องหมายวงเล็บมุม (เช่น `"Wait... <short pause> did you hear that? <sigh>"` หรือ `"Excuse me <cough> as I was saying..."`)

ดูแนวทางปฏิบัติแนะนำที่ครอบคลุมได้ใน[คู่มือการใช้พรอมต์](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=th#prompting-guide)

## ตัวเลือกเสียง

TTS ของ Gemini 3.8 รองรับการเลือกหรือสร้างเสียง 4 วิธีดังนี้

1. **เสียงของ Studio ที่สร้างไว้ล่วงหน้า:** เสียงที่คัดสรรแล้ว 30 เสียงซึ่งแสดงอยู่ในตารางต่อไปนี้
2. **คลังเสียงเพิ่มเติม:** เสียงเพิ่มเติมอีกหลายร้อยเสียงในภาษา
   สำเนียง และต้นแบบตัวละครต่างๆ ซึ่งเข้าถึงได้โดยใช้ `client.voices.list()`
   (`GET /v1beta/voices`)
3. **[การออกแบบเสียง](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=th):** สร้าง
   ลักษณะเสียงที่กำหนดเองจากคำอธิบายภาษาธรรมชาติใน
   [Google AI Studio](https://aistudio.google.com/generate-speech?hl=th) หรือใช้
   `POST /v1beta/voices` (`type="prompted"` ซึ่งจะแสดงผลรหัส `voice_...` ที่คงอยู่และตัวอย่าง `sample_audio` WAV ใน `CreateVoice` และ
   `GetVoice`)
4. **[การจำลองเสียง](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=th):**
   จำลองเสียงของผู้พูดจากเสียงอ้างอิงและเสียงที่ได้รับความยินยอมใน [Google AI Studio](https://aistudio.google.com/generate-speech?hl=th) หรือใช้ `POST /v1beta/voices` (`type="replicated"`, `store=True` แบบถาวรโดยค่าเริ่มต้น หรือ `store=False` แบบไม่เก็บสถานะ (Stateless) ที่ไม่บังคับ)

### ขีดจำกัดของเสียงที่กำหนดเองและ TTL

| พิมพ์ด้วยเสียง | โหมดจัดเก็บ | โควต้า / ขีดจำกัด | การเก็บรักษา (TTL) |
| --- | --- | --- | --- |
| **เสียงที่มีสถานะ** (`voice_...`, พรอมต์หรือจำลอง) | `store=True` | **200 เสียงต่อโปรเจ็กต์** (ใช้ร่วมกันระหว่างเสียงที่สร้างจากพรอมต์และเสียงที่จำลอง) | **1 ปีนับจากการใช้งานครั้งล่าสุด\*** |
| **คีย์เสียงแบบไม่เก็บสถานะ** (`voicekey_...`, ทำซ้ำ) | `store=False` | จัดการโดยลูกค้า | **7 วัน** |

\* **การขยาย TTL:** หน้าต่างการเก็บรักษา 1 ปีจะรีเซ็ตทุกครั้งที่มีการใช้เสียงอย่างต่อเนื่อง (ไม่ว่าจะโดยการสังเคราะห์เสียงพูดด้วยเสียงนั้นหรือใช้เป็นเสียงฐานสำหรับการรีมิกซ์) ระบบจะลบเสียงที่ไม่มีกิจกรรมเป็นเวลา 1 ปีโดยอัตโนมัติ

### เสียงที่สร้างไว้ล่วงหน้า

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *สว่าง* | **Puck** -- *Upbeat* | **Charon** -- *มีสาระประโยชน์* |
| **Kore** -- *Firm* | **Fenrir** -- *ตื่นเต้นง่าย* | **Leda** -- *วัยรุ่น* |
| **Orus** -- *บริษัท* | **Aoede** -- *Breezy* | **Callirrhoe** -- *สบายๆ* |
| **Autonoe** -- *สว่าง* | **Enceladus** -- *Breathy* | **Iapetus** -- *Clear* |
| **Umbriel** -- *สบายๆ* | **Algieba** -- *ราบรื่น* | **Despina** - *Smooth* |
| **Erinome** -- *ชัดเจน* | **Algenib** -- *แหบเล็กน้อย* | **Rasalgethi** -- *ให้ข้อมูล* |
| **Laomedeia** -- *Upbeat* | **Achernar** -- *นุ่มนวล* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *สุขุม* | **Pulcherrima** -- *มั่นใจ* |
| **Achird** -- *เป็นมิตร* | **Zubenelgenubi** -- *สบายๆ* | **Vindemiatrix** -- *อ่อนโยน* |
| **Sadachbia** -- *มีชีวิตชีวา* | **Sadaltager** -- *มีความรู้* | **Sulafat** -- *อบอุ่น* |

### คลังเสียงและการกรองที่ครอบคลุมมากขึ้น

นอกเหนือจากเสียงในสตูดิโอที่แนะนำ 30 เสียงในตารางก่อนหน้า **คลังเสียงเพิ่มเติม**ยังมีเสียงอื่นๆ อีกหลายร้อยเสียงในภาษาต่างๆ สำเนียงตามภูมิภาค บุคลิกของตัวละคร และโดเมน คุณสามารถเรียกดู กรอง และทดลองฟังเสียงในคลังเสียงทั้งหมดแบบอินเทอร์แอกทีฟได้ใน [Google AI Studio](https://aistudio.google.com/generate-speech?hl=th) หรือค้นหาแบบเป็นโปรแกรมโดยใช้ `client.voices.list()` (`GET /v1beta/voices` โดยใช้ `google-genai` 2.25.0 ขึ้นไป / `@google/genai` 2.24.0 ขึ้นไป)

`ListVoices` จะแสดงเสียงที่จัดเก็บไว้แบบกำหนดเอง (เรียงลำดับจากใหม่ที่สุดก่อน) ตามด้วยเสียงในแคตตาล็อกที่สร้างไว้ล่วงหน้าซึ่งตรงกับเกณฑ์ตัวกรองของคุณ เมื่อมีการส่งค่าหลายค่าสำหรับตัวกรองรายการ ระบบจะแสดงผลเสียงที่ตรงกับค่า**ใดก็ได้**ในตัวกรองนั้น (`OR`) ขณะที่พารามิเตอร์ตัวกรองที่แตกต่างกันจะรวมกับ `AND`:

| พารามิเตอร์ | ประเภท | คำอธิบาย |
| --- | --- | --- |
| `language_code` | `list[str]` | แท็กภาษา BCP-47 (เช่น `["en-US", "en-GB"]`) การทำงานแบบตรงทั้งหมดโดยไม่คำนึงถึงตัวพิมพ์เล็กและตัวพิมพ์ใหญ่ |
| `region_code` | `list[str]` | รหัสภูมิภาค ISO 3166-1 alpha-2 หรือ UN M.49 (เช่น `["US", "GB"]`) |
| `accent` | `list[str]` | คำอธิบายสำเนียงในภูมิภาค (เช่น `["American", "British"]`) |
| `gender` | `list[str]` | การแสดงออกทางเพศที่รับรู้ (`"female"`, `"male"` หรือ `"neutral"`) |
| `pitch` | `list[str]` | การจัดประเภทระดับเสียงร้อง (`"low"`, `"medium"` หรือ `"high"`) |
| `persona` | `list[str]` | บุคลิกหรือต้นแบบตัวละครที่มีเสียงร้อง (เช่น `["Warm, Friendly"]`, `["Narrator"]`) |
| `contexts` (`context` ใน REST) | `list[str]` | โดเมนการใช้งานที่เหมาะสม (เช่น `["Audiobook", "Conversational", "News"]`) |
| `type` (`type_` ใน Python) | `list[str]` | กรองตามแหล่งที่มาของเสียง: `"prebuilt"`, `"prompted"` ([การออกแบบเสียง](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=th)) หรือ `"replicated"` ([การจำลองเสียง](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=th)) |
| `search` | `str` | การค้นหาสตริงย่อยแบบข้อความอิสระจะจับคู่โดยไม่คำนึงถึงตัวพิมพ์เล็กและตัวพิมพ์ใหญ่กับทั้ง `display_name` และ `description` |
| `page_size` | `int` | จำนวนเสียงสูงสุดที่แสดงต่อหน้า (ค่าเริ่มต้น `50`, สูงสุด `1000`) |
| `page_token` | `str` | โทเค็นจาก `response.next_page_token` เพื่อดึงข้อมูลผลการค้นหาหน้าถัดไป |

### Python

```
from google import genai

client = genai.Client()

# Filter the Voice Library by language, gender, pitch, domain context, and keyword
response = client.voices.list(
    language_code=["en-US", "en-GB"],
    gender=["female"],
    pitch=["medium", "low"],
    contexts=["Audiobook", "Conversational"],
    type_=["prebuilt"],
    search="warm",
    page_size=50,
)

for voice in response.voices or []:
    print(
        f"{voice.id} | {voice.display_name} ({voice.language_code},"
        f" {voice.accent}, {voice.gender}, pitch={voice.pitch}):"
        f" {voice.description}"
    )
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// Filter the Voice Library by language, gender, pitch, domain context, and keyword
const response = await ai.voices.list({
  language_code: ["en-US", "en-GB"],
  gender: ["female"],
  pitch: ["medium", "low"],
  contexts: ["Audiobook", "Conversational"],
  type: ["prebuilt"],
  search: "warm",
  page_size: 50,
});

for (const voice of response.voices ?? []) {
  console.log(
    `${voice.id} | ${voice.display_name} (${voice.language_code}, ${voice.accent}, ${voice.gender}, pitch=${voice.pitch}): ${voice.description}`
  );
}
```

### REST

```
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB" \
  --data-urlencode "gender=female" \
  --data-urlencode "pitch=medium" \
  --data-urlencode "context=Audiobook" \
  --data-urlencode "type=prebuilt" \
  --data-urlencode "search=warm" \
  --data-urlencode "page_size=50"
```

## ภาษาที่รองรับ

โมเดล TTS จะตรวจหาภาษาที่ป้อนโดยอัตโนมัติ
[TTS ของ Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=th)
(`gemini-3.8-flash-tts`) รองรับ**กว่า 130 ภาษา** และ
[TTS ของ Gemini 3.8 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=th)
(`gemini-3.8-flash-lite-tts`) รองรับ**กว่า 100 ภาษา**

| ภาษา | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| อาเจะฮ์ (อักษรอาหรับ) | ✔️ | ✔️ |
| อาฟรีกานส์ | ✔️ | ✔️ |
| อะคัน | ✔️ | ✔️ |
| อัมฮาริก | ✔️ | ✔️ |
| อาร์เมเนีย | ✔️ | ✔️ |
| อัสสัม | ✔️ | ✔️ |
| อวธี | ✔️ | ✔️ |
| บาหลี | ✔️ | ✔️ |
| เบงกอล | ✔️ | ✔️ |
| บันจาร์ (อักษรอาหรับ) | ✔️ | — |
| บันจาร์ (อักษรละติน) | ✔️ | ✔️ |
| แบชเคียร์ | ✔️ | — |
| บาสก์ | ✔️ | ✔️ |
| Belarusian | ✔️ | ✔️ |
| เบมบา | ✔️ | — |
| โภชปุระ | ✔️ | ✔️ |
| บอสเนีย | ✔️ | ✔️ |
| บูกิส | ✔️ | ✔️ |
| บัลแกเรีย | ✔️ | ✔️ |
| พม่า | ✔️ | — |
| จีนกวางตุ้ง | ✔️ | ✔️ |
| คาตาลัน | ✔️ | ✔️ |
| ซีบัวโน | ✔️ | ✔️ |
| เคิร์ดตอนกลาง | ✔️ | ✔️ |
| ฉัตติสครห์ | ✔️ | ✔️ |
| จีน (อักษร Hans) | ✔️ | ✔️ |
| จีน (อักษร Hant) | ✔️ | ✔️ |
| ตาตาร์ไครเมีย | ✔️ | — |
| โครเอเชีย | ✔️ | ✔️ |
| เช็ก | ✔️ | ✔️ |
| เดนมาร์ก | ✔️ | ✔️ |
| ดัตช์ | ✔️ | ✔️ |
| ดิวลา | ✔️ | — |
| ซองคา | ✔️ | — |
| อาหรับอียิปต์ | ✔️ | ✔️ |
| อังกฤษ | ✔️ | ✔️ |
| เอสโตเนีย | ✔️ | ✔️ |
| ฟิลิปปินส์ | ✔️ | ✔️ |
| ฟินแลนด์ | ✔️ | — |
| ฝรั่งเศส | ✔️ | ✔️ |
| กาลิเชียน | ✔️ | ✔️ |
| กันดา | ✔️ | ✔️ |
| จอร์เจีย | ✔️ | ✔️ |
| เยอรมัน | ✔️ | ✔️ |
| กรีก | ✔️ | ✔️ |
| กวารานี | ✔️ | — |
| คุชราต | ✔️ | ✔️ |
| เฮติครีโอล | ✔️ | ✔️ |
| มองโกเลียคาลคา | ✔️ | ✔️ |
| เฮาซา | ✔️ | ✔️ |
| ฮีบรู | ✔️ | ✔️ |
| ฮินดี | ✔️ | ✔️ |
| ฮังการี | ✔️ | ✔️ |
| ไอซ์แลนด์ | ✔️ | ✔️ |
| อิกโบ | ✔️ | — |
| อีโลโก | ✔️ | ✔️ |
| อินโดนีเซีย | ✔️ | ✔️ |
| เปอร์เซีย (อิหร่าน) | ✔️ | ✔️ |
| อิตาลี | ✔️ | ✔️ |
| ญี่ปุ่น | ✔️ | ✔️ |
| ชวา | ✔️ | ✔️ |
| คาไบล์ | ✔️ | — |
| คัมบา | ✔️ | ✔️ |
| กันนาดา | ✔️ | ✔️ |
| แคชเมียร์ (อักษรอาหรับ) | ✔️ | ✔️ |
| แคชเมียร์ (อักษรเทวนาครี) | ✔️ | ✔️ |
| คาซัค | ✔️ | ✔️ |
| เขมร | ✔️ | ✔️ |
| คิคูยู | ✔️ | ✔️ |
| คินยารวันดา | ✔️ | ✔️ |
| คองโก | ✔️ | ✔️ |
| เกาหลี | ✔️ | ✔️ |
| คีร์กิซ | ✔️ | ✔️ |
| ภาษาลาว | ✔️ | ✔️ |
| ลัตกาเรียน | ✔️ | — |
| ลิงกาลา | ✔️ | ✔️ |
| ลิทัวเนีย | ✔️ | — |
| ลักเซมเบิร์ก | ✔️ | — |
| มาซีโดเนีย | ✔️ | ✔️ |
| มคธี | ✔️ | ✔️ |
| ไมถิลี | ✔️ | ✔️ |
| มาลายาลัม | ✔️ | ✔️ |
| มอลตา | ✔️ | ✔️ |
| มานิพูรี | ✔️ | ✔️ |
| มราฐี | ✔️ | ✔️ |
| มินังกาเบา (อักษรอาหรับ) | ✔️ | ✔️ |
| มินังกาเบา (สคริปต์ละติน) | ✔️ | — |
| มิโซ | ✔️ | ✔️ |
| เนปาล (ภาษาเดี่ยว) | ✔️ | ✔️ |
| ฟุลฟุลเดไนจีเรีย | ✔️ | ✔️ |
| อาเซอร์ไบจานเหนือ | ✔️ | ✔️ |
| โซโทเหนือ | ✔️ | ✔️ |
| อุซเบกเหนือ | ✔️ | ✔️ |
| นอร์เวย์บุคมอล | ✔️ | ✔️ |
| นีนอสก์ของนอร์เวย์ | ✔️ | ✔️ |
| เนียนจา | ✔️ | ✔️ |
| ออกซิแทน | ✔️ | — |
| โอเดีย (ภาษาเดี่ยว) | ✔️ | ✔️ |
| ปังกาซินัน | ✔️ | — |
| เปอร์เซีย (อัฟกานิสถาน) | ✔️ | ✔️ |
| โปแลนด์ | ✔️ | ✔️ |
| โปรตุเกส | ✔️ | ✔️ |
| ปัญจาบ | ✔️ | ✔️ |
| โรมาเนีย | ✔️ | ✔️ |
| รัสเซีย | ✔️ | ✔️ |
| สันถาลี | ✔️ | ✔️ |
| เซอร์เบีย | ✔️ | ✔️ |
| สินธี | ✔️ | — |
| สิงหล | ✔️ | ✔️ |
| สโลวัก | ✔️ | ✔️ |
| สโลวีเนีย | ✔️ | — |
| โซมาลี | ✔️ | — |
| อาเซอร์ไบจานใต้ | ✔️ | ✔️ |
| ปาทานใต้ | ✔️ | ✔️ |
| โซโทใต้ | ✔️ | — |
| สเปน | ✔️ | ✔️ |
| อาหรับมาตรฐาน (อักษรอาหรับ) | ✔️ | ✔️ |
| อาหรับมาตรฐาน (อักษรละติน) | ✔️ | ✔️ |
| ลัตเวียมาตรฐาน | ✔️ | ✔️ |
| ภาษามลายูมาตรฐาน | ✔️ | ✔️ |
| สวาฮีลี (ภาษาเดียว) | ✔️ | — |
| สวาติ | ✔️ | — |
| สวีเดน | ✔️ | — |
| ทาจิก | ✔️ | — |
| ทมิฬ | ✔️ | ✔️ |
| เตลูกู | ✔️ | ✔️ |
| ไทย | ✔️ | — |
| ทิกรินยา | ✔️ | — |
| แอลบาเนียนแบบทอสก์ | ✔️ | — |
| ตุรกี | ✔️ | ✔️ |
| อุยกูร์ | ✔️ | — |
| เวียดนาม | ✔️ | ✔️ |

## รุ่นที่รองรับ

| รุ่น | ผู้พูดคนเดียว | หลายลำโพง | การออกแบบเสียง | การจำลองเสียง |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=th) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [TTS ของ Gemini 3.8 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=th) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [ตัวอย่าง TTS ของ Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=th) | ✔️ | ✔️ | — | — |
| [TTS เวอร์ชันตัวอย่างของ Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=th) | ✔️ | ✔️ | — | — |

### ควรใช้โมเดลใดเมื่อใด

โมเดล TTS ของ Gemini 3.8 ทั้ง 2 โมเดลใช้สคีมา API และรูปแบบพรอมต์เดียวกัน
ซึ่งช่วยให้คุณสลับไปมาระหว่างโมเดลทั้ง 2 ได้ด้วยการเปลี่ยนพารามิเตอร์เพียงรายการเดียว

- **ใช้ [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=th)
  (`gemini-3.8-flash-tts`)** เมื่อความเที่ยงตรงของเสียงสูงสุด การแสดงที่ละเอียดอ่อน
  และการควบคุมการแสดงออกเป็นสิ่งสำคัญที่สุด เหมาะสำหรับงานสร้างสรรค์ระดับสตูดิโอ บทสนทนาที่มีผู้พูดหลายคนและซับซ้อน แท็กเสียงร้องที่หนักหน่วง การออกเสียงที่ยาก ภาษาถิ่นหรือภาษาของชนกลุ่มน้อย และการบรรยายแบบยาวที่ต้องการเสียงที่หนักแน่นและความเสถียรของเสียงในห้อง
- **ใช้ [TTS ของ Gemini 3.8 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=th)
  (`gemini-3.8-flash-lite-tts`)** เป็นเครื่องมือที่รวดเร็วและคุ้มค่า
  แทน `gemini-3.1-flash-tts-preview` โดยได้รับการเพิ่มประสิทธิภาพสำหรับการสร้างเสียงจำนวนมาก, การส่งต่อข้อมูลของตัวแทนเสียงแบบสนทนา, ฟีเจอร์อ่านออกเสียง, การจำลองเสียงที่เชื่อถือได้ และเสียงพูดของผู้พูดคนเดียวในชีวิตประจำวันในภาษาหลักๆ

### คำแนะนำในการย้ายข้อมูล

เมื่ออัปเกรดจากโมเดลเวอร์ชันตัวอย่างก่อนหน้า (`gemini-3.1-flash-tts-preview` หรือ `gemini-2.5-pro-preview-tts`) เป็น Gemini 3.8 TTS (`gemini-3.8-flash-tts` หรือ `gemini-3.8-flash-lite-tts`) โปรดตรวจสอบการเปลี่ยนแปลงที่สำคัญ 5 รายการต่อไปนี้

1. **แยกสไตล์ออกจากข้อความถอดเสียง:** ย้ายคำสั่งการแสดง น้ำเสียง ท่วงทำนอง และจังหวะที่ต่อเนื่อง (เช่น `"whispering"`, `"out of breath"` หรือ `"speaking slowly"`) ออกจากข้อความธรรมดาและใส่ไว้ใน `speech_metadata.style`
   โปรดเก็บ `text` ไว้เป็นข้อความถอดเสียงแบบคำต่อคำอย่างเคร่งครัด พร้อมแท็กเสียงร้องในบรรทัด
2. **ออกแบบตัวตนล่วงหน้าด้วย Voice Design:** แทนที่บล็อก `"Audio Profile"` หรือ `"Director's Notes"` หลายย่อหน้าด้วยเสียงที่กำหนดเองซึ่งสร้างขึ้นใน [Voice Design](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=th) จากนั้นส่งรหัส `voice_...` นั้นผ่านคำขอ TTS โดยใช้สตริง `style` ที่มีค่าน้อยที่สุดหรือว่างเปล่า
3. **ใช้การสนทนาแบบมีโครงสร้าง:** สำหรับการสนทนาที่มีผู้พูดหลายคน ให้ส่ง `part` 1 รายการต่อการพูดของผู้พูดแต่ละคนด้วย `speech_metadata.speaker` แทนการฝังคำนำหน้า `Speaker: ...` ไว้ในบล็อกข้อความเดียว
4. **ใช้วงเล็บปีกกาสำหรับแท็กเสียงร้องในบรรทัด:** ใช้วงเล็บปีกกา (`<laugh>`,
   `<sigh>`, `<cough>`, `<breath>`, `<short pause>`) สำหรับเสียงร้องและหยุดชั่วคราวของมนุษย์ ณ จุดใดจุดหนึ่ง หลีกเลี่ยงแท็กเอฟเฟกต์เสียงที่ไม่มีเสียงร้อง (เช่น
   เสียงปรบมือหรือเสียงทุ้ม)
5. **บัญชีสำหรับเอาต์พุต WAV (`AUDIO_WAV`) เริ่มต้นในคำขอแบบเอกภาคี:** `gemini-3.1-flash-tts-preview``AUDIO_L16`โมเดล TTS ของ Gemini 3.8 จะแสดงเสียง **WAV
   (`AUDIO_WAV`)** ที่สมบูรณ์พร้อมส่วนหัว RIFF (24 kHz, โมโน, 16 บิต PCM) ในคำขอแบบเอกภาคี ดังนี้
   - หากก่อนหน้านี้โค้ดของคุณห่อไบต์ PCM ดิบไว้ในส่วนหัวของ WAV (เช่น ใช้โมดูล `wave` ของ Python หรือแพ็กเกจ `wav` ของ Node) ให้นำ
     ส่วนหัวที่ห่อด้วยตนเองออก แล้วเขียนไบต์เสียงที่ถอดรหัสแล้วลงในไฟล์ `.wav` โดยตรง
   - หากไปป์ไลน์ที่มีอยู่ต้องใช้เสียง PCM ดิบแบบไม่มีส่วนหัว, mu-law หรือ A-law
     ให้ตั้งค่า `generationConfig.responseFormat.audio.mimeType`
     เป็น `"AUDIO_L16"`, `"AUDIO_MULAW"` หรือ `"AUDIO_ALAW"` อย่างชัดเจนโดยใช้ REST API
     (เช่น `{"responseFormat": {"audio": {"mimeType": "AUDIO_L16"}}}`
     ใน `generateContent` รองรับการลบล้าง `responseFormat` ที่กำหนดเองใน
     `generateContent` โดยใช้ REST API ขณะที่ Python และ
     JavaScript SDK รองรับ `response_format` ใน `GenerateContentConfig`
     อยู่ระหว่างดำเนินการ หรือใช้
     `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}` ใน
     Interactions API) ดู[รูปแบบเอาต์พุตเสียง](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=th#audio-output-formats)

## คู่มือการเขียนพรอมต์

โมเดล TTS ของ Gemini 3.8 จะถือว่าข้อความอินพุตเป็น**ข้อความถอดเสียงตามคำพูด**อย่างเคร่งครัด
Gemini 3.8 TTS แตกต่างจากโมเดลเวอร์ชันตัวอย่างก่อนหน้านี้ที่ฝังคำสั่งการแสดงไว้ในข้อความธรรมดา โดยจะแยกคำสั่งระดับเทิร์นแบบต่อเนื่อง (`speech_metadata`) ออกจากแท็กเสียงพูดในบรรทัด ณ จุดเวลาหนึ่งๆ

### ฟิลด์รูปแบบเทียบกับแท็กในบรรทัด

แยกคำสั่งประสิทธิภาพตามขอบเขต

- **การนำเสนอระดับคำพูด (`speech_metadata.style`):** ใส่แอตทริบิวต์การนำเสนอที่ต่อเนื่อง เช่น อารมณ์ ความผันแปรของระดับเสียง จังหวะโดยรวม หรือสไตล์การนำเสนอ (เช่น `"whispering"`, `"out of breath"`, `"muttering"` หรือ `"sarcastic"`) ลงในฟิลด์ `style` ของ `speech_metadata` หากต้องการสร้างตัวละครและการแสดงที่สม่ำเสมอในแต่ละเทิร์น ให้ออกแบบตัวละครล่วงหน้าใน[การออกแบบเสียง](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=th) และใช้ `style` สำหรับการปรับแต่งระดับเทิร์นที่ไม่บังคับเท่านั้น
- **เหตุการณ์ที่เกิดขึ้น ณ จุดใดจุดหนึ่ง (แท็กในบรรทัด):** ใส่เสียงที่ไม่ใช่คำพูดชั่วขณะ เสียงหายใจ หรือการหยุดชั่วคราวในบรรทัดภายในข้อความถอดเสียงโดยใช้วงเล็บมุม (`<cough>`, `<breath>`, `<sigh>`, `<short pause>`) ใช้วงเล็บมุม (`<...>`) เพื่อคุณภาพเสียงสูงสุด และใช้การเปล่งเสียงของมนุษย์แทนเอฟเฟกต์เสียงที่ไม่ใช่เสียงพูด

| ขอบเขต | ตำแหน่งที่ควรวาง | ตัวอย่าง |
| --- | --- | --- |
| **ระดับการเลี้ยว** (คงที่ตลอดการเลี้ยว) | `speech_metadata.style` | `"angry tone"` `"speaking rapidly"` `"out of breath"` `"whispers"` `"sarcastic"` |
| **ช่วงเวลา** (เกิดขึ้นที่คำที่เฉพาะเจาะจง) | แทรกในบรรทัดใน `text` (`<...>`) | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### จังหวะการดำเนินเรื่องและการหยุดชั่วคราว

คุณควบคุมจังหวะและความเงียบได้ 3 ระดับ ดังนี้

- **เครื่องหมายวรรคตอนและจุดไข่ปลา:** ใช้คอมมา ขีดกลาง (`--`) และจุดไข่ปลา (`...`) เพื่อแสดงความลังเลในการสนทนาอย่างเป็นธรรมชาติ
- **แท็กหยุดชั่วคราวในบรรทัด:** แทรก `<short pause>` หรือ `<long pause>` ในจุดที่แน่นอนในสคริปต์ที่ผู้พูดควรหยุดชั่วคราว
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **ความเร็วระดับเทิร์น:** ตั้งค่า `"style": "speaking rapidly"` หรือ `"style": "speaking slowly"` ใน `speech_metadata` เพื่อควบคุมอัตราการพูดตลอดทั้งเทิร์น

### ทำนองและระดับเสียง

ใช้ **`speech_metadata.style`** เพื่อควบคุมการออกเสียง ระดับเสียง และการผันคำใน
แต่ละเทิร์น (เช่น `"style": "high pitch, cheerful and excited inflection"` หรือ
`"style": "monotone and flat"`) หากอารมณ์หรือการออกเสียงเปลี่ยนไประหว่างบทสนทนา
ให้แยกสคริปต์เป็นเทิร์นแยกกันโดยมีค่า `style` ที่แตกต่างกันสำหรับแต่ละเทิร์น

### การเน้น

ใช้อักษรตัวพิมพ์ใหญ่กับคำที่เฉพาะเจาะจงในข้อความถอดเสียง ร่วมกับเครื่องหมายวรรคตอนและแท็กเสียงในบรรทัด เพื่อเน้นเสียงอย่างเป็นธรรมชาติในคำสำคัญ ดังนี้

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### เสียงร้องและเสียงที่ไม่ใช่เสียงพูด

วางเสียงร้องของมนุษย์ที่ไม่ใช่คำพูดในบรรทัดโดยใช้วงเล็บมุม (`<...>`) ที่
จุดที่ควรมีเสียง แท็กเสียงร้องที่แนะนำมีดังนี้

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>` / `<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>` / `<laughter>` | `<moan>` | `<pant>` | `<pff>` / `<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>` / `<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>` / `<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### การตอบรับและเสียงพูดทับซ้อนกัน

ในการสนทนาที่มีผู้พูดหลายคน ให้ใส่ปฏิกิริยาของผู้ฟังในอักขระไปป์
(`|reaction|`) ภายในเทิร์นของผู้พูดเพื่อสร้างช่องทางย้อนกลับที่เป็นธรรมชาติหรือ
การพูดที่ทับซ้อนกันโดยไม่ต้องแบ่งเป็นเทิร์นแยกต่างหากต่อรีแอ็กชัน

- **การแลกเปลี่ยนสั้นๆ ในช่องสื่อสารเบื้องหลัง:** ใส่รีแอ็กชันสั้นๆ ของ Listener (`|oh hmm|`, `|oh really?|`, `|absolutely|`) ไว้ในเทิร์นของผู้ที่กำลังพูด:
  - **เทิร์นที่ 1 (ผู้พูด A):** `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **เทิร์นที่ 2 (ผู้พูด ข):** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **เทิร์นที่ 3 (ผู้พูด A):** `"Then let's ship it |absolutely| and watch the dashboards."`
- **คำพูดที่ทับซ้อนกันและสลับกัน:** ใช้ส่วนไปป์หลายส่วนเพื่อจำลองคำพูดที่เกิดขึ้นพร้อมกันหรือสลับกันระหว่างผู้พูด 2 คน (ทำงานได้ดีที่สุดกับ `gemini-3.8-flash-tts`)
  - **การนับถอยหลัง/การร้องประสานเสียงพร้อมกัน:** `"Let's surprise him on three |ok| ready?"` ตามด้วย `"one. two. three. |happy| happy |birthday| birthday!"`
  - **ผู้พูดทับซ้อนกันทั้งหมด:** `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### ความสอดคล้องกันในแต่ละรุ่นและสิ่งที่ควรหลีกเลี่ยง

ทำตามหลักเกณฑ์ต่อไปนี้เพื่อให้เสียงพูดมีความสม่ำเสมอในแต่ละรอบ

- **ออกแบบตัวตนล่วงหน้าในการออกแบบเสียงแทนที่จะใช้บล็อกสไตล์ยาวๆ:**
  ย่อหน้า `"Audio Profile"` แบบยาวและหัวข้อย่อยหลายรายการ `"Director's Notes"`
  ที่ยกมาจากโมเดลก่อนหน้าเป็นสาเหตุที่พบบ่อยที่สุดของการเบี่ยงเบนของเสียง
  ใช้สัญชาตญาณด้านครีเอทีฟโฆษณาเดียวกันนั้นตั้งแต่ต้นใน[การออกแบบเสียง](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=th)เพื่อสร้าง`voice_...`ลักษณะตัวละครที่กำหนดเองอย่างต่อเนื่อง จากนั้นใช้รหัสเสียงนั้นผ่านการเรียก TTS
- **ใช้เสียงอ้างอิงเพื่อความเสถียร (ละเว้นคำสั่งเมตา):**
  โมเดล TTS ของ Gemini 3.8 ได้รับการฝึกให้ยึดตามเสียงอ้างอิงเป็นอันดับแรก
  อย่าใส่คำสั่งที่บอกให้โมเดลคงเสียงให้สม่ำเสมอ (เช่น `"do not switch speaker identity"` หรือ `"maintain identical timbre"`) เนื่องจากข้อความพรอมต์ที่มากเกินไปจะเพิ่มความคลาดเคลื่อน ละเว้นคำสั่งสไตล์ที่ไม่จำเป็นและปล่อยให้โมเดล
  เปลี่ยนแปลงไปตามธรรมชาติรอบจุดที่เสถียรซึ่งอ้างอิงจากเสียง
- **อย่าพยายามเปลี่ยนลักษณะของผู้พูดที่ไม่สามารถเปลี่ยนแปลงได้ใน `style`:** หลีกเลี่ยงการใส่อายุ เพศ ชื่อ หรือการเปลี่ยนสำเนียงถาวรใน `speech_metadata.style`
  แต่ให้เลือกเสียงตามภูมิภาคจากคลังเสียงเพิ่มเติมหรือสร้างเสียงด้วย[การออกแบบเสียง](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=th)แทน

### เวิร์กโฟลว์ที่แนะนำ

1. **สร้างตัวละครครั้งเดียว:** สร้างตัวละครใน[การออกแบบเสียง](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=th)หรือเลือกเสียงตามภูมิภาคจากคลังเสียงเพิ่มเติมที่ตรงกับภาษาเป้าหมายและตัวละครของคุณ
2. **เขียนข้อความถอดเสียงที่พูดอย่างเป็นธรรมชาติโดยมีคำพูดติดขัด:** เพื่อให้เป็นธรรมชาติมากที่สุด ให้เขียน `text` เป็นข้อความถอดเสียงที่พูดจริง ซึ่งรวมถึงคำพูดติดขัดและการลังเลในการสนทนาที่เป็นธรรมชาติ (เช่น `"Oh uh yeah I think... hm, so that's interesting"`)
3. **ทดสอบ TTS แบบธรรมดาก่อน:** สังเคราะห์ข้อความถอดเสียงโดยใช้ฟิลด์ `style`
   ที่ว่างเปล่าก่อน เนื่องจากคำขอส่วนใหญ่ไม่จำเป็นต้องมีคำสั่ง `style`
4. **เพิ่มพรอมต์ `style` สั้นๆ สำหรับการปรับแต่งเท่านั้น:** เพิ่มสตริง `style` ที่กระชับ (เช่น `"casual, friendly"` หรือ `"muttering, then reassuring"`) สำหรับเทิร์นที่ต้องการการปรับแต่งการนำส่งที่เฉพาะเจาะจงเท่านั้น และใช้สตริงสั้นๆ เดียวกันนั้นซ้ำในเทิร์นต่างๆ เมื่อต้องการให้มีพื้นฐานที่สอดคล้องกัน

### ตัวแทนการสนทนาไปมาและตัวแทนเสียง

เมื่อสร้าง Agent เสียงแบบสนทนาเรียลไทม์หรือแอปพลิเคชันแบบสนทนาไปมา ให้ทำดังนี้

- โทรหา **TTS 1 ครั้งต่อเทิร์น**เมื่อข้อความ LLM มาถึง
- ปล่อยให้ `voice` ที่กำหนดค่าไว้ (สร้างไว้ล่วงหน้า ออกแบบ `voice_...` หรือจำลอง `voice_...` / `voicekey_...`) ระบุตัวตนของลำโพงในแต่ละรอบการสนทนา โดยไม่ต้องส่งตัวตนของตัวละครแบบยาวซ้ำในแต่ละรอบ
- ปล่อยช่อง `style` ต่อเทิร์นว่างไว้ หรือส่งสตริงคงที่สั้นๆ 1 รายการ (เช่น `"casual, friendly"`) สำหรับการสนทนาทั้งหมด
- แบ่งคำตอบที่ยาวของ Agent ออกเป็นเทิร์นสั้นๆ แทนที่จะใช้พรอมต์สไตล์ที่เข้มงวดขึ้น

## การสร้างเสียงพูดแบบสตรีมมิง

คุณสามารถสตรีมเสียงที่สร้างขึ้นขณะที่โมเดลกำลังสังเคราะห์เสียงได้ ต่างจากคำขอแบบ Unary (ซึ่งแสดงผลไฟล์ WAV ที่สมบูรณ์พร้อมส่วนหัว RIFF) **คำขอสตรีมมิงจะแสดงผลกลุ่ม PCM เชิงเส้นแบบ Little-Endian แบบมีเครื่องหมาย 16 บิตดิบที่ไม่มีส่วนหัว (`AUDIO_L16` / `audio/L16;codec=pcm;rate=24000`, 24 kHz, โมโน) โดยค่าเริ่มต้น** เพื่อให้สามารถเล่นหรือต่อกลุ่มเสียงเข้าด้วยกันได้อย่างต่อเนื่องโดยไม่ต้องมีส่วนหัวของคอนเทนเนอร์

### Python

```
from google import genai

client = genai.Client()

response_stream = client.models.generate_content_stream(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

for chunk in response_stream:
    try:
        data = chunk.candidates[0].content.parts[0].inline_data.data
        # data contains raw PCM bytes (24kHz, 1-channel, 16-bit)
    except (IndexError, AttributeError):
        pass
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const ai = new GoogleGenAI({});

   const responseStream = await ai.models.generateContentStream({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   for await (const chunk of responseStream) {
      const data = chunk.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
      if (data) {
         const audioBuffer = Buffer.from(data, 'base64');
         // Process the audio buffer
      }
   }
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }'
```

## รูปแบบเอาต์พุตเสียง

โมเดล TTS ของ Gemini 3.8 ใช้รูปแบบเสียงเริ่มต้นที่แตกต่างกัน โดยขึ้นอยู่กับว่าคำขอเป็นแบบ Unary หรือสตรีมมิง

- **คำขอแบบ Unary (`models.generate_content`):** แสดงผลเสียง **WAV (`AUDIO_WAV`)** ที่สมบูรณ์พร้อมส่วนหัว RIFF (24 kHz, โมโน, PCM แบบ Little-Endian ที่มีเครื่องหมาย 16 บิต) คุณเขียนไบต์เสียงที่ถอดรหัสแล้วลงใน`.wav`ไฟล์ได้โดยตรงโดยไม่ต้องเพิ่มคอนเทนเนอร์ WAV ด้วยตนเอง
- **คำขอสตรีมมิง (`models.generate_content_stream` / `streamGenerateContent`):**
  ส่งคืนก้อน**Linear PCM แบบดิบที่ไม่มีส่วนหัว (`AUDIO_L16`)** (24 kHz, โมโน,
  PCM แบบ Little-Endian ที่มีเครื่องหมาย 16 บิต) โดยค่าเริ่มต้นเพื่อให้สตรีมหรือ
  ต่อก้อนอย่างต่อเนื่องได้โดยไม่ต้องมีส่วนหัวของคอนเทนเนอร์ในแต่ละก้อน

คุณลบล้างการเข้ารหัสเสียงเอาต์พุตและอัตราการสุ่มตัวอย่างได้โดยใช้
`generationConfig.responseFormat.audio`

| ค่า `mimeType` | รูปแบบ | คำอธิบาย |
| --- | --- | --- |
| `"AUDIO_WAV"` *(ค่าเริ่มต้นแบบเอกภาค)* | WAV (`audio/wav`) | ไฟล์ WAV ที่สมบูรณ์พร้อมส่วนหัว RIFF (24 kHz, โมโน, 16-bit PCM) |
| `"AUDIO_L16"` *(ค่าเริ่มต้นสำหรับการสตรีม)* | Linear PCM (`audio/l16`) | PCM เชิงเส้นแบบ 16 บิตที่ลงนามแบบ Little-Endian ดิบที่ไม่มีส่วนหัว เหมาะที่สุดสำหรับการสตรีม ไปป์ไลน์เสียงที่กำหนดเอง หรือการเชื่อมโยงคลิปการสนทนาไปมา |
| `"AUDIO_MULAW"` | μ-law (`audio/basic` / `audio/mulaw`) | เสียงที่บีบอัดตามกฎ μ ของ G.711 ใช้กันโดยทั่วไปในระบบโทรศัพท์ของอเมริกาเหนือและญี่ปุ่น (8 kHz) |
| `"AUDIO_ALAW"` | A-law (`audio/alaw`) | เสียงที่บีบอัดด้วยกฎ G.711 A-law ใช้กันโดยทั่วไปในการโทรศัพท์ในยุโรปและระหว่างประเทศ (8 kHz) |

นอกจากนี้ คุณยังระบุ `sampleRate` (เช่น `24000`, `16000` หรือ `8000` Hz โดยค่าเริ่มต้นจะเป็น `24000` Hz) ได้ด้วย

คำขอตัวอย่าง REST ต่อไปนี้จะขอ PCM แบบ 16 บิตดิบที่ไม่มีส่วนหัว (`AUDIO_L16`) ที่
24 kHz

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "responseFormat": {
            "audio": {
              "mimeType": "AUDIO_L16",
              "sampleRate": 24000
            }
          },
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.pcm
```

## ข้อจำกัด

- โมเดล TTS จะรับอินพุตที่เป็นข้อความเท่านั้นและสร้างเอาต์พุตที่เป็นเสียงเท่านั้น
- การสร้างเสียงผู้พูดหลายคนในคำขอเดียว (`multiSpeakerVoiceConfig`) รองรับผู้พูดสูงสุด 2 คนโดยใช้เสียงที่สร้างไว้ล่วงหน้า หากต้องการรวมเสียงที่ออกแบบเอง
  (`voice_...`) หรือจำลอง (`voice_...` / `voicekey_...`) ใน
  บทสนทนาที่มีหลายตัวละคร ให้สังเคราะห์เสียงพูดของแต่ละคนแยกกัน
  เนื่องจากคำขอแบบ Unary จะแสดงผล `audio/wav` พร้อมส่วนหัว RIFF ขนาด 44 ไบต์โดยค่าเริ่มต้น ให้ขอ PCM ดิบ (`AUDIO_L16`) หรือตัดส่วนหัว WAV ออกจากแต่ละเทิร์นก่อนที่จะเชื่อมโยงเฟรมเสียง PCM ขนาด 24kHz
- **ขีดจำกัดพื้นที่เก็บข้อมูลเสียงที่กำหนดเองและ TTL:**
  - **เสียงแบบเก็บสถานะ (`store=True`, พรอมต์หรือจำลอง):** สูงสุด **200 เสียงต่อโปรเจ็กต์** โดยมี **TTL 1 ปี** (Time to Live)
  - **คีย์เสียงแบบไม่เก็บสถานะ (`store=False`, `voicekey_...`):** **TTL 7 วัน**
    (Time to Live)
- ตรวจสอบส่วน[ภาษาที่รองรับ](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=th#languages)เพื่อดูความครอบคลุมของภาษา

## ขั้นตอนถัดไป

- สร้างตัวตนของเสียงร้องที่กำหนดเองจากภาษาธรรมชาติด้วย[การออกแบบเสียง](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=th)
- จำลองเสียงของผู้พูดที่มีอยู่โดยใช้[การจำลองเสียง](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=th)
- เปรียบเทียบข้อมูลจำเพาะของโมเดลในหน้าโมเดล
  [TTS ของ Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=th) และ
  [TTS ของ Gemini 3.8 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=th)
- สำรวจเสียงแบบ 2 ทิศทางที่โต้ตอบได้ด้วย [Live API](https://ai.google.dev/gemini-api/docs/live?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-12 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-12 UTC"],[],[]]
