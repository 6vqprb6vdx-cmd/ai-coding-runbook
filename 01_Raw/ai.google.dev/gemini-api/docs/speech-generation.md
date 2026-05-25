---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=th
fetched_at: 2026-05-25T12:56:59.126883+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การสร้างการอ่านออกเสียงข้อความ (TTS)

Gemini API สามารถเปลี่ยนอินพุตข้อความเป็นเสียงแบบผู้พูดคนเดียวหรือหลายคน
โดยใช้ความสามารถในการสร้างข้อความเป็นเสียง (TTS) ของ Gemini
การสร้างการอ่านออกเสียงข้อความ (TTS) เป็นแบบ*[ควบคุมได้](#controllable)*
ซึ่งหมายความว่าคุณสามารถใช้ภาษาธรรมชาติเพื่อจัดโครงสร้างการโต้ตอบและกำหนด*สไตล์* *สำเนียง* *จังหวะ* และ*โทนเสียง*ของเสียงได้

[ลองใช้ใน Google AI Studio](https://aistudio.google.com/apps/bundled/voice-library?showPreview=truew&hl=th)

ความสามารถของ TTS แตกต่างจากการสร้างคำพูดที่ให้บริการผ่าน [Live API](https://ai.google.dev/gemini-api/docs/live?hl=th) ซึ่งออกแบบมาสำหรับเสียงแบบโต้ตอบที่ไม่มีโครงสร้าง รวมถึงอินพุตและเอาต์พุตแบบมัลติโมดัล แม้ว่า Live API จะยอดเยี่ยม
ในบริบทการสนทนาแบบไดนามิก แต่ TTS ผ่าน Gemini API
ได้รับการปรับแต่งสำหรับสถานการณ์ที่ต้องมีการอ่านข้อความที่แน่นอนพร้อมการควบคุม
สไตล์และเสียงอย่างละเอียด เช่น การสร้างพอดแคสต์หรือหนังสือเสียง

คู่มือนี้จะแสดงวิธีสร้างเสียงแบบผู้พูดคนเดียวและแบบผู้พูดหลายคนจากข้อความ

## ก่อนเริ่มต้น

ตรวจสอบว่าคุณใช้โมเดล Gemini ที่มีฟีเจอร์การอ่านออกเสียงข้อความ (TTS) ของ Gemini ตามที่ระบุไว้ในส่วน[โมเดลที่รองรับ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th#supported-models) โปรดพิจารณาว่าโมเดลใดเหมาะกับกรณีการใช้งานเฉพาะของคุณมากที่สุดเพื่อให้ได้ผลลัพธ์ที่ดีที่สุด

คุณอาจเห็นว่า[การทดสอบโมเดล TTS ของ Gemini ใน AI Studio](https://aistudio.google.com/generate-speech?hl=th) มีประโยชน์ก่อนที่จะเริ่มสร้าง

## TTS แบบผู้พูดคนเดียว

หากต้องการแปลงข้อความเป็นเสียงแบบลำโพงเดียว ให้ตั้งค่ารูปแบบการตอบกลับเป็น "เสียง"
และส่งออบเจ็กต์ `SpeechConfig` ที่ตั้งค่า `VoiceConfig` แล้ว
คุณจะต้องเลือกชื่อเสียงจาก[เสียงเอาต์พุต](#voices)ที่สร้างไว้ล่วงหน้า

ตัวอย่างนี้จะบันทึกเสียงเอาต์พุตจากโมเดลในไฟล์ Wave

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents="Say cheerfully: Have a wonderful day!",
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: 'Say cheerfully: Have a wonderful day!' }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               voiceConfig: {
                  prebuiltVoiceConfig: { voiceName: 'Kore' },
               },
            },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "parts":[{
            "text": "Say cheerfully: Have a wonderful day!"
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }
        },
        "model": "gemini-3.1-flash-tts-preview",
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode >out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## TTS แบบหลายผู้พูด

สำหรับเสียงแบบหลายลำโพง คุณจะต้องมีออบเจ็กต์ `MultiSpeakerVoiceConfig` ที่กำหนดค่าลำโพงแต่ละตัว (สูงสุด 2 ตัว) เป็น `SpeakerVoiceConfig`
คุณจะต้องกําหนดแต่ละ `speaker` ด้วยชื่อเดียวกันกับที่ใช้ใน[พรอมต์](#controllable)

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=prompt,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Joe',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Jane',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const ai = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: prompt }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               multiSpeakerVoiceConfig: {
                  speakerVoiceConfigs: [
                        {
                           speaker: 'Joe',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Kore' }
                           }
                        },
                        {
                           speaker: 'Jane',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Puck' }
                           }
                        }
                  ]
               }
            }
      }
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
  "contents": [{
    "parts":[{
      "text": "TTS the following conversation between Joe and Jane:
                Joe: Hows it going today Jane?
                Jane: Not too bad, how about you?"
    }]
  }],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {
      "multiSpeakerVoiceConfig": {
        "speakerVoiceConfigs": [{
            "speaker": "Joe",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }, {
            "speaker": "Jane",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Puck"
              }
            }
          }]
      }
    }
  },
  "model": "gemini-3.1-flash-tts-preview",
}' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
    base64 --decode > out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## การควบคุมรูปแบบการพูดด้วยพรอมต์

คุณควบคุมสไตล์ น้ำเสียง สำเนียง และจังหวะได้โดยใช้พรอมต์ภาษาธรรมชาติ
หรือ[แท็กเสียง](#transcript-tags)สำหรับ TTS แบบเสียงเดียวและหลายเสียง
ตัวอย่างเช่น ในพรอมต์ที่มีผู้พูดคนเดียว คุณอาจพูดว่า

```
Say in an spooky voice:
"By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes"
```

ในพรอมต์ที่มีผู้พูดหลายคน ให้ระบุชื่อของผู้พูดแต่ละคนและ
ข้อความถอดเสียงที่เกี่ยวข้องแก่โมเดล นอกจากนี้ คุณยังให้คำแนะนำแก่ผู้พูดแต่ละคนได้ด้วย โดยทำดังนี้

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what's on the agenda today?
Speaker2: You're never going to guess!
```

ลองใช้[ตัวเลือกเสียง](#voices)ที่สอดคล้องกับสไตล์หรืออารมณ์ที่คุณต้องการสื่อ เพื่อเน้นย้ำให้ชัดเจนยิ่งขึ้น เช่น ในพรอมต์ก่อนหน้า เสียงลมของ *Enceladus* อาจเน้นคำว่า "เหนื่อย" และ "เบื่อ" ในขณะที่
*Puck* มีน้ำเสียงที่ร่าเริงซึ่งอาจเสริมคำว่า "ตื่นเต้น" และ "มีความสุข"

## กำลังสร้างพรอมต์เพื่อแปลงเป็นเสียง

โมเดล TTS จะแสดงผลเฉพาะเสียง แต่คุณสามารถใช้[โมเดลอื่นๆ](https://ai.google.dev/gemini-api/docs/models?hl=th) เพื่อสร้างข้อความถอดเสียงก่อน
แล้วส่งข้อความถอดเสียงนั้นไปยังโมเดล TTS เพื่ออ่านออกเสียง

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

transcript = client.models.generate_content(
   model="gemini-3.5-flash",
   contents="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam.""").text

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=transcript,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Dr. Anya',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Liam',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

# ...Code to handle audio output
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {

const transcript = await ai.models.generateContent({
   model: "gemini-3.5-flash",
   contents: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const response = await ai.models.generateContent({
   model: "gemini-3.1-flash-tts-preview",
   contents: transcript,
   config: {
      responseModalities: ['AUDIO'],
      speechConfig: {
         multiSpeakerVoiceConfig: {
            speakerVoiceConfigs: [
                   {
                     speaker: "Dr. Anya",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Kore"},
                     }
                  },
                  {
                     speaker: "Liam",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Puck"},
                    }
                  }
                ]
              }
            }
      }
  });
}
// ..JavaScript code for exporting .wav file for output audio

await main();
```

## ตัวเลือกเสียง

โมเดล TTS รองรับตัวเลือกเสียง 30 แบบต่อไปนี้ในช่อง `voice_name`

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *สว่าง* | **Puck** -- *Upbeat* | **Charon** - *ให้ข้อมูล* |
| **เกาหลี** - *หนักแน่น* | **Fenrir** - *ตื่นเต้นง่าย* | **Leda** -- *อ่อนเยาว์* |
| **Orus** -- *Firm* | **Aoede** -- *Breezy* | **Callirrhoe** -- *สบายๆ* |
| **Autonoe** -- *Bright* | **Enceladus** -- *Breathy* | **Iapetus** -- *Clear* |
| **Umbriel** -- *สบายๆ* | **Algieba** - *Smooth* | **Despina** -- *Smooth* |
| **Erinome** -- *ล้าง* | **Algenib** -- *แหบเล็กน้อย* | **Rasalgethi** -- *ให้ข้อมูล* |
| **Laomedeia** -- *Upbeat* | **Achernar** -- *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *ผู้ใหญ่* | **Pulcherrima** -- *มั่นใจ* |
| **Achird** -- *เป็นมิตร* | **Zubenelgenubi** -- *สบายๆ* | **Vindemiatrix** -- *อ่อนโยน* |
| **Sadachbia** -- *มีชีวิตชีวา* | **Sadaltager** -- *มีความรู้* | **Sulafat** -- *Warm* |

คุณสามารถฟังตัวเลือกเสียงทั้งหมดได้ใน [AI Studio](https://aistudio.google.com/generate-speech?hl=th)

## ภาษาที่รองรับ

โมเดล TTS จะตรวจหาภาษาที่ป้อนโดยอัตโนมัติ ภาษาที่รองรับมีดังนี้

| ภาษา | รหัส BCP-47 | ภาษา | รหัส BCP-47 |
| --- | --- | --- | --- |
| อาหรับ | ar | ฟิลิปปินส์ | fil |
| เบงกอล | bn | ฟินแลนด์ | fi |
| ดัตช์ | nl | กาลิเชียน | gl |
| อังกฤษ | en | จอร์เจีย | ka |
| ฝรั่งเศส | fr | กรีก | el |
| เยอรมัน | de | คุชราต | gu |
| ฮินดี | hi | เฮติครีโอล | ht |
| อินโดนีเซีย | id | ฮีบรู | เขา |
| อิตาลี | it | ฮังการี | hu |
| ญี่ปุ่น | ja | ไอซ์แลนด์ | is |
| เกาหลี | ko | ชวา | jv |
| มราฐี | mr | กันนาดา | kn |
| โปแลนด์ | pl | กงกณี | kok |
| โปรตุเกส | pt | ภาษาลาว | lo |
| โรมาเนีย | ro | ลาติน | ลา |
| รัสเซีย | ru | ลัตเวีย | lv |
| สเปน | es | ลิทัวเนีย | lt |
| ทมิฬ | ta | ลักเซมเบิร์ก | ปอนด์ |
| เตลูกู | te | มาซีโดเนีย | mk |
| ไทย | th | ไมถิลี | mai |
| ตุรกี | tr | มาลากาซี | มก. |
| ยูเครน | uk | มาเลย์ | มิลลิวินาที |
| เวียดนาม | vi | มาลายาลัม | ml |
| แอฟริคานส์ | af | มองโกเลีย | mn |
| แอลเบเนีย | sq | เนปาล | ne |
| อัมฮาริก | am | นอร์เวย์ (บ็อกมอล) | nb |
| อาร์เมเนีย | hy | นอร์เวย์ (นีนอสก์) | nn |
| อาร์เซอร์ไบจัน | az | โอเดีย | หรือ |
| บาสก์ | eu | พาชตู | ps |
| เบลารุส | be | เปอร์เซีย | fa |
| บัลแกเรีย | bg | ปัญจาบ | pa |
| พม่า | my | เซอร์เบีย | sr |
| คาตาลัน | ca | สินธี | SD |
| เซบู | ceb | สิงหล | si |
| จีนกลาง | cmn | สโลวัก | sk |
| โครเอเชีย | ชม. | สโลวีเนีย | sl |
| เช็ก | cs | สวาฮิลี | sw |
| เดนมาร์ก | da | สวีเดน | sv |
| เอสโตเนีย | et | อูรดู | ur |

## โมเดลที่รองรับ

| รุ่น | ผู้พูดคนเดียว | Multispeaker |
| --- | --- | --- |
| [ตัวอย่าง TTS ของ Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=th) | ✔️ | ✔️ |
| [TTS ของ Gemini 2.5 Flash (เวอร์ชันตัวอย่าง)](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=th) | ✔️ | ✔️ |
| [TTS ของ Gemini 2.5 Pro เวอร์ชันตัวอย่าง](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=th) | ✔️ | ✔️ |

## คำแนะนำในการเขียนพรอมต์

โมเดล**การสร้างเสียงแบบเนทีฟของ Gemini Native Audio Generation Text-to-Speech (TTS)** แตกต่างจากโมเดล TTS แบบเดิมตรงที่ใช้โมเดลภาษาขนาดใหญ่ที่***ไม่เพียงรู้ว่าจะพูดอะไร แต่ยังรู้วิธีพูดด้วย***

โมเดลจะตีความข้อความถอดเสียงโดยกำเนิดและกำหนดวิธี
ส่งคำพูดของคุณ ข้อความถอดเสียงแบบง่ายๆ โดยไม่ต้องมี
การแจ้งเตือนเพิ่มเติมจะฟังดูเป็นธรรมชาติ แต่ TTS ของ Gemini ยังมีเครื่องมือที่คุณใช้เพื่อ
ควบคุมได้ด้วย

จุดประสงค์ของคู่มือนี้คือการให้แนวทางพื้นฐานและจุดประกายไอเดียเมื่อ
พัฒนาประสบการณ์การใช้งานเสียง เราจะเริ่มด้วย**แท็ก**เพื่อการควบคุมแบบอินไลน์อย่างรวดเร็ว
จากนั้นจะไปดู**โครงสร้างพรอมต์**ขั้นสูงเพื่อกำหนดทิศทางประสิทธิภาพอย่างเต็มที่

### แท็กเสียง

แท็กคือตัวแก้ไขในบรรทัด เช่น `[whispers]` หรือ `[laughs]` ที่ช่วยให้คุณควบคุมการนำส่งได้อย่างละเอียด คุณสามารถใช้เครื่องหมายเหล่านี้เพื่อเปลี่ยนน้ำเสียง จังหวะ และอารมณ์ของบรรทัดหรือส่วนของข้อความถอดเสียงได้ คุณยังใช้เสียงเหล่านี้เพื่อ
ใส่เสียงแทรกและเสียงอื่นๆ ที่ไม่ใช่คำพูดลงในการแสดงได้ด้วย เช่น
`[cough]`, `[sighs]` หรือ `[gasp]`

ไม่มีรายการที่ครอบคลุมว่าแท็กใดใช้ได้และใช้ไม่ได้ เราขอแนะนำให้
ทดลองใช้อารมณ์และคำพูดต่างๆ เพื่อดูว่าเอาต์พุต
เปลี่ยนแปลงไปอย่างไร

หากข้อความถอดเสียงไม่ได้เป็นภาษาอังกฤษ เราขอแนะนำให้คุณ
ยังคงใช้แท็กเสียงภาษาอังกฤษเพื่อให้ได้ผลลัพธ์ที่ดีที่สุด

**ใช้แท็กเสียงอย่างสร้างสรรค์**

เพื่อแสดงให้เห็นถึงความหลากหลายที่คุณจะได้รับจากแท็กเสียง ต่อไปนี้คือชุด
ตัวอย่างที่แต่ละตัวอย่างพูดถึงสิ่งเดียวกัน แต่การนำส่งจะเปลี่ยนแปลงไปตาม
แท็กที่ใช้

คุณเปลี่ยนการเน้นการนำส่งได้โดยเพิ่มแท็กที่จุดเริ่มต้นของ
บรรทัดเพื่อให้ผู้พูดตื่นเต้น เบื่อ หรือไม่เต็มใจ

- `[excitedly]` สวัสดี ฉันเป็นโมเดลแปลงข้อความเป็นคำพูดตัวใหม่ และพูดได้หลายแบบ
  วันนี้มีอะไรให้ช่วยบ้าง
- `[bored]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงพูดตัวใหม่…
- `[reluctantly]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงพูดตัวใหม่…

นอกจากนี้ คุณยังใช้แท็กเพื่อเปลี่ยนจังหวะการอ่านหรือรวมจังหวะ
กับการเน้นได้ด้วย

- `[very fast]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงพูดตัวใหม่…
- `[very slow]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงพูดตัวใหม่…
- `[sarcastically, one painfully slow word at a time]` สวัสดี ฉันเป็นโมเดลใหม่สำหรับ
  การแปลงข้อความเป็นคำพูด…

นอกจากนี้ คุณยังควบคุมส่วนต่างๆ ได้อย่างแม่นยำ ซึ่งหมายความว่าคุณสามารถกระซิบ
ส่วนหนึ่งและตะโกนอีกส่วนหนึ่งได้

- `[whispers]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงตัวใหม่ `[shouting]` และพูดได้หลายแบบ
  `[whispers]` วันนี้จะให้เราช่วยอะไร

นอกจากนี้ คุณยังทดลองใช้ไอเดียครีเอทีฟโฆษณาที่ต้องการได้ด้วย

- `[like a cartoon dog]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงพูดตัวใหม่…
- `[like dracula]` สวัสดี ฉันเป็นโมเดลข้อความเป็นเสียงพูดตัวใหม่…

แท็กที่ใช้กันโดยทั่วไป ได้แก่

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

แท็กช่วยให้คุณควบคุมการส่งข้อความถอดเสียงได้อย่างรวดเร็วและง่ายดาย หากต้องการควบคุมมากยิ่งขึ้น คุณสามารถใช้ร่วมกับพรอมต์บริบทเพื่อกำหนดโทนโดยรวม
และบรรยากาศของประสิทธิภาพได้

### การเขียนพรอมต์ขั้นสูง

คุณอาจมองว่าพรอมต์ขั้นสูงเป็นคำสั่งของระบบที่โมเดลต้อง
ทำตาม ซึ่งเป็นวิธีให้บริบทแก่โมเดลมากขึ้นและควบคุมประสิทธิภาพได้

พรอมต์ที่มีประสิทธิภาพควรมีองค์ประกอบต่อไปนี้ซึ่งทำงานร่วมกันเพื่อ
สร้างประสิทธิภาพที่ยอดเยี่ยม

- **โปรไฟล์เสียง** - สร้างลักษณะตัวตนสำหรับเสียง โดยกำหนดเอกลักษณ์ของตัวละคร ต้นแบบ และลักษณะอื่นๆ เช่น อายุ ภูมิหลัง ฯลฯ
- **ฉาก** - กำหนดบริบท อธิบายทั้งสภาพแวดล้อมทางกายภาพและ"บรรยากาศ"
- **หมายเหตุของผู้กำกับ** - คำแนะนำด้านประสิทธิภาพที่คุณสามารถแจกแจงคำสั่งที่สำคัญสำหรับพรสวรรค์เสมือนให้จดบันทึกได้ ตัวอย่างเช่น
  สไตล์การพูด การหายใจ การเว้นจังหวะ การออกเสียง และสำเนียง
- **บริบทตัวอย่าง** - ช่วยให้โมเดลมีจุดเริ่มต้นตามบริบท เพื่อให้
  นักแสดงเสมือนปรากฏในฉากที่คุณตั้งค่าไว้อย่างเป็นธรรมชาติ
- **ข้อความถอดเสียง** - ข้อความที่โมเดลจะพูด โปรดทราบว่าหัวข้อของข้อความถอดเสียงและรูปแบบการเขียนควรสอดคล้องกับ
  เส้นทางที่คุณให้ไว้เพื่อให้ได้ประสิทธิภาพที่ดีที่สุด
- **แท็กเสียง** - ตัวแก้ไขที่คุณใส่ในข้อความถอดเสียงเพื่อเปลี่ยนวิธีแสดงข้อความบางส่วน เช่น `[whispers]` หรือ `[shouting]`

ตัวอย่างพรอมต์แบบเต็ม

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions — no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
[excitedly] Yes, massive vibes in the studio! You are locked in and it is
absolutely popping off in London right now. If you're stuck on the tube, or
just sat there pretending to work... stop it. Seriously, I see you.
[shouting] Turn this up! We've got the project roadmap landing in three,
two... let's go!
```

### กลยุทธ์การแจ้งโดยละเอียด

มาดูรายละเอียดของแต่ละองค์ประกอบในพรอมต์กัน

#### โปรไฟล์เสียง

อธิบายตัวตนของตัวละครโดยย่อ

- **ชื่อ** การตั้งชื่อตัวละครจะช่วยให้โมเดลและ
  การแสดงเชื่อมโยงกันอย่างใกล้ชิด โปรดอ้างอิงถึงตัวละครด้วยชื่อเมื่อตั้งค่าฉากและ
  บริบท
- **บทบาท** ตัวตนหลักและต้นแบบของตัวละครที่กำลังแสดงในฉาก เช่น ดีเจวิทยุ ครีเอเตอร์พอดแคสต์ ผู้รายงาน เป็นต้น

ตัวอย่าง

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### บรรยากาศ

กำหนดบริบทของฉาก รวมถึงสถานที่ อารมณ์ และรายละเอียดด้านสิ่งแวดล้อม ที่กำหนดโทนและบรรยากาศ อธิบายสิ่งที่เกิดขึ้นรอบตัว
ตัวละครและผลกระทบที่มีต่อตัวละคร ฉากจะให้บริบทด้านสิ่งแวดล้อม
สำหรับการโต้ตอบทั้งหมดและเป็นแนวทางในการแสดง
อย่างเป็นธรรมชาติ

ตัวอย่าง

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### หมายเหตุของผู้กำกับ

ส่วนสำคัญนี้มีคำแนะนำด้านประสิทธิภาพที่เฉพาะเจาะจง คุณข้ามองค์ประกอบอื่นๆ ทั้งหมดได้ แต่เราขอแนะนำให้รวมองค์ประกอบนี้ไว้

กำหนดเฉพาะสิ่งที่สำคัญต่อประสิทธิภาพ โดยระมัดระวังไม่ให้
กำหนดมากเกินไป กฎที่เข้มงวดมากเกินไปจะจำกัดความคิดสร้างสรรค์ของโมเดลและอาจ
ส่งผลให้ประสิทธิภาพแย่ลง ปรับสมดุลบทบาทและคำอธิบายฉากด้วย
กฎการแสดงเฉพาะ

คำแนะนำที่พบบ่อยที่สุดคือ**สไตล์ จังหวะ และสำเนียง** แต่โมเดลไม่ได้จำกัดอยู่เพียงคำแนะนำเหล่านี้ และไม่จำเป็นต้องใช้คำแนะนำเหล่านี้ คุณสามารถใส่คำสั่งที่กำหนดเองเพื่อระบุรายละเอียดเพิ่มเติมที่สำคัญต่อประสิทธิภาพ และ
ระบุรายละเอียดมากหรือน้อยตามที่จำเป็น

เช่น

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**รูปแบบ:**

กำหนดโทนและสไตล์ของคำพูดที่สร้างขึ้น ระบุอารมณ์ เช่น สนุกสนาน
กระตือรือร้น ผ่อนคลาย เบื่อ ฯลฯ เพื่อเป็นแนวทางในการแสดง อธิบายและ
ให้รายละเอียดมากที่สุดเท่าที่จำเป็น: *"ความกระตือรือร้นที่แพร่หลาย ผู้ฟัง
ควรรู้สึกเหมือนเป็นส่วนหนึ่งของกิจกรรมชุมชนที่ยิ่งใหญ่และน่าตื่นเต้น"* ดีกว่าการพูดว่า *"กระตือรือร้นและมีพลัง"*

หรือจะลองใช้คำที่ได้รับความนิยมในอุตสาหกรรมเสียงบรรยาย เช่น "เสียง
ยิ้ม" ก็ได้ คุณซ้อนลักษณะสไตล์ได้มากเท่าที่ต้องการ

ตัวอย่าง

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

ความลึกมากขึ้น

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

ซับซ้อน

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**เครื่องหมายแสดงการเน้นเสียง:**

อธิบายสำเนียงที่ต้องการ ยิ่งเจาะจงมากเท่าไหร่ ผลลัพธ์ที่ได้ก็จะยิ่งดีขึ้นเท่านั้น เช่น ใช้ "*สำเนียงภาษาอังกฤษแบบอังกฤษที่ได้ยินในครอยดอน
ประเทศอังกฤษ*" เทียบกับ "*สำเนียงอังกฤษ*"

ตัวอย่าง

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a DJ from Brixton, London
...
```

**การกำหนดอัตราการแสดงโฆษณา:**

การกำหนดจังหวะโดยรวมและความผันแปรของจังหวะตลอดทั้งชิ้นงาน

ตัวอย่าง

เรียบง่าย

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

ความลึกเพิ่มเติม

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

ซับซ้อน

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

#### แท็กข้อความถอดเสียงและแท็กเสียง

ข้อความถอดเสียงคือคำที่โมเดลจะพูด แท็กเสียงคือคำ
ในวงเล็บเหลี่ยมที่ระบุวิธีพูด การเปลี่ยน
โทนเสียง หรือคำอุทาน

```
### TRANSCRIPT

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
```

**ลองใช้เลย**

ลองใช้ตัวอย่างเหล่านี้ด้วยตัวคุณเองใน
[AI Studio](https://aistudio.google.com/generate-speech?hl=th) เล่นกับ
[แอป TTS](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=th) ของเรา แล้วให้
Gemini พาคุณไปนั่งเก้าอี้ผู้กำกับ อย่าลืมคำนึงถึงเคล็ดลับต่อไปนี้เพื่อสร้างการแสดงเสียงร้องที่ยอดเยี่ยม

- อย่าลืมทำให้พรอมต์ทั้งหมดสอดคล้องกัน โดยสคริปต์และคำสั่งจะทำงานร่วมกันในการสร้างการแสดงที่ยอดเยี่ยม
- คุณไม่จำเป็นต้องอธิบายทุกอย่าง บางครั้งการเว้นช่องว่างให้โมเดลเติมเต็มจะช่วยให้ดูเป็นธรรมชาติมากขึ้น (เหมือนนักแสดงมากความสามารถ)
- หากคุณรู้สึกว่าตัน ให้ Gemini ช่วยคุณร่างสคริปต์หรือการแสดง

## ข้อจำกัด

- โมเดล TTS รับได้เฉพาะข้อความที่ป้อนและสร้างเอาต์พุตเสียงเท่านั้น
- เซสชัน TTS มีขีดจำกัด[หน้าต่างบริบท](https://ai.google.dev/gemini-api/docs/long-context?hl=th)อยู่ที่ 32,000 โทเค็น
- ดูส่วน[ภาษา](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th#languages)เพื่อดูการรองรับภาษา
- TTS ไม่รองรับการสตรีม

ข้อจำกัดต่อไปนี้จะมีผลเฉพาะเมื่อใช้โมเดลตัวอย่าง TTS ของ Gemini 3.1 Flash
สำหรับการสร้างคำพูด

- **เสียงไม่สอดคล้องกับวิธีการในพรอมต์:** เอาต์พุตของโมเดลอาจไม่
  ตรงกับเสียงของลำโพงที่เลือกเสมอ ทำให้เสียงที่ได้
  แตกต่างจากที่คาดไว้ หากไม่ต้องการให้เสียงพูดไม่ตรงกัน (เช่น เสียงผู้ชายทุ้ม
  พยายามพูดเหมือนเด็กผู้หญิง) ให้ตรวจสอบว่าโทนและบริบทที่เขียนในพรอมต์สอดคล้องกับโปรไฟล์ของผู้พูดที่เลือกอย่างเป็นธรรมชาติ
- **คุณภาพของเอาต์พุตที่ยาวขึ้น:** คุณภาพและความสอดคล้องของคำพูดอาจเริ่ม
  เปลี่ยนแปลงไปเมื่อเอาต์พุตที่สร้างขึ้นยาวกว่า 2-3 นาที เราขอแนะนำให้แบ่งข้อความถอดเสียงออกเป็นส่วนเล็กๆ
- **การแสดงผลโทเค็นข้อความเป็นครั้งคราว:** โมเดลจะแสดงผลโทเค็นข้อความแทนโทเค็นเสียงเป็นครั้งคราว
  ซึ่งทำให้เซิร์ฟเวอร์ไม่สามารถดำเนินการตามคำขอได้โดยมีข้อผิดพลาด `500`
  เนื่องจากข้อผิดพลาดนี้เกิดขึ้นแบบสุ่มในคำขอบางส่วนเท่านั้น คุณจึงควรใช้ตรรกะการลองใหม่โดยอัตโนมัติในแอปพลิเคชันเพื่อจัดการกับข้อผิดพลาดเหล่านี้
- **การปฏิเสธที่ผิดพลาดของตัวแยกประเภทพรอมต์:** พรอมต์ที่คลุมเครืออาจไม่ทริกเกอร์
  ตัวแยกประเภทการสังเคราะห์เสียงพูด ทำให้คำขอถูกปฏิเสธ
  (`PROHIBITED_CONTENT`) หรือทำให้โมเดลอ่านคำสั่งสไตล์และหมายเหตุของผู้กำกับ
  ออกมา ตรวจสอบความถูกต้องของพรอมต์โดยเพิ่มคำนำที่ชัดเจน
  เพื่อสั่งให้โมเดลสังเคราะห์คำพูด และติดป้ายกำกับอย่างชัดเจนว่า
  ข้อความถอดเสียงที่พูดจริงเริ่มต้นที่ใด

## ขั้นตอนถัดไป

- ลองใช้[สูตรการสร้างเสียง](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb?hl=th)
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=th) ของ Gemini มีตัวเลือกการสร้างเสียงแบบอินเทอร์แอกทีฟ
  ที่คุณสามารถสลับกับรูปแบบอื่นๆ ได้
- หากต้องการทำงานกับ*อินพุต*เสียง โปรดไปที่คู่มือ[การทำความเข้าใจเสียง](https://ai.google.dev/gemini-api/docs/audio?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-19 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-19 UTC"],[],[]]
