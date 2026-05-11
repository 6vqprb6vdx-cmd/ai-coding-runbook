---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=th
fetched_at: 2026-05-11T12:37:15.602010+00:00
title: "\u0e01\u0e32\u0e23\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e40\u0e1e\u0e25\u0e07\u0e41\u0e1a\u0e1a\u0e40\u0e23\u0e35\u0e22\u0e25\u0e44\u0e17\u0e21\u0e4c\u0e42\u0e14\u0e22\u0e43\u0e0a\u0e49 Lyria RealTime \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การสร้างเพลงแบบเรียลไทม์โดยใช้ Lyria RealTime

Gemini API ซึ่งใช้ [Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=th)
ช่วยให้เข้าถึงโมเดลการสร้างเพลงแบบสตรีมมิงแบบเรียลไทม์ที่ล้ำสมัย
โดยช่วยให้นักพัฒนาแอปสร้างแอปพลิเคชันที่ผู้ใช้
สามารถสร้างแบบอินเทอร์แอกทีฟ ควบคุมอย่างต่อเนื่อง และเล่นดนตรี
บรรเลงได้

การสร้างเพลงแบบเรียลไทม์ของ Lyria ใช้การเชื่อมต่อสตรีมมิงแบบ 2 ทิศทางที่มีความหน่วงต่ำอย่างต่อเนื่องโดยใช้ [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

หากต้องการสัมผัสสิ่งที่สร้างขึ้นได้โดยใช้ Lyria RealTime ให้ลองใช้ใน AI Studio โดยใช้แอป [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=th) หรือ [MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=th)

## สร้างและควบคุมเพลง

Lyria RealTime ทำงานคล้ายกับ [Live API](https://ai.google.dev/gemini-api/docs/live?hl=th)
โดยใช้ WebSockets เพื่อรักษาการสื่อสารแบบเรียลไทม์กับโมเดล

โค้ดต่อไปนี้แสดงวิธีสร้างเพลง

### Python

ตัวอย่างนี้จะเริ่มต้นเซสชัน Lyria RealTime โดยใช้ `client.aio.live.music.connect()` จากนั้นจะส่งข้อความแจ้งเริ่มต้นพร้อมกับ `session.set_weighted_prompts()` รวมถึงการกำหนดค่าเริ่มต้นโดยใช้ `session.set_music_generation_config` เริ่มการสร้างเพลงโดยใช้ `session.play()` และตั้งค่า `receive_audio()` เพื่อประมวลผลกลุ่มเสียงที่ได้รับ

```
  import asyncio
  from google import genai
  from google.genai import types

  client = genai.Client(http_options={'api_version': 'v1alpha'})

  async def main():
      async def receive_audio(session):
        """Example background task to process incoming audio."""
        while True:
          async for message in session.receive():
            audio_data = message.server_content.audio_chunks[0].data
            # Process audio...
            await asyncio.sleep(10**-12)

      async with (
        client.aio.live.music.connect(model='models/lyria-realtime-exp') as session,
        asyncio.TaskGroup() as tg,
      ):
        # Set up task to receive server messages.
        tg.create_task(receive_audio(session))

        # Send initial prompts and config
        await session.set_weighted_prompts(
          prompts=[
            types.WeightedPrompt(text='minimal techno', weight=1.0),
          ]
        )
        await session.set_music_generation_config(
          config=types.LiveMusicGenerationConfig(bpm=90, temperature=1.0)
        )

        # Start streaming music
        await session.play()
  if __name__ == "__main__":
      asyncio.run(main())
```

### JavaScript

ตัวอย่างนี้จะเริ่มต้นเซสชัน Lyria RealTime โดยใช้
`client.live.music.connect()` จากนั้นจะส่ง
พรอมต์เริ่มต้นพร้อมกับ `session.setWeightedPrompts()` รวมถึง
การกำหนดค่าเริ่มต้นโดยใช้ `session.setMusicGenerationConfig` เริ่มการสร้างเพลงโดยใช้ `session.play()` และตั้งค่า
การเรียกกลับ `onMessage` เพื่อประมวลผลกลุ่มเสียงที่ได้รับ

```
import { GoogleGenAI } from "@google/genai";
import Speaker from "speaker";
import { Buffer } from "buffer";

const client = new GoogleGenAI({
  apiKey: GEMINI_API_KEY,
    apiVersion: "v1alpha" ,
});

async function main() {
  const speaker = new Speaker({
    channels: 2,       // stereo
    bitDepth: 16,      // 16-bit PCM
    sampleRate: 44100, // 44.1 kHz
  });

  const session = await client.live.music.connect({
    model: "models/lyria-realtime-exp",
    callbacks: {
      onmessage: (message) => {
        if (message.serverContent?.audioChunks) {
          for (const chunk of message.serverContent.audioChunks) {
            const audioBuffer = Buffer.from(chunk.data, "base64");
            speaker.write(audioBuffer);
          }
        }
      },
      onerror: (error) => console.error("music session error:", error),
      onclose: () => console.log("Lyria RealTime stream closed."),
    },
  });

  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: "Minimal techno with deep bass, sparse percussion, and atmospheric synths", weight: 1.0 },
    ],
  });

  await session.setMusicGenerationConfig({
    musicGenerationConfig: {
      bpm: 90,
      temperature: 1.0,
      audioFormat: "pcm16",  // important so we know format
      sampleRateHz: 44100,
    },
  });

  await session.play();
}

main().catch(console.error);
```

จากนั้นคุณสามารถใช้ `session.play()`, `session.pause()`, `session.stop()` และ
`session.reset_context()` เพื่อเริ่ม หยุดชั่วคราว หยุด หรือรีเซ็ตเซสชัน

## ควบคุมเพลงแบบเรียลไทม์

คุณสามารถควบคุมการสร้างเพลงแบบเรียลไทม์ได้โดยส่งพรอมต์และอัปเดต
พารามิเตอร์การสร้างแบบเรียลไทม์

### พรอมต์ Lyria RealTime

ขณะที่ไลฟ์สดอยู่ คุณจะส่ง`WeightedPrompt`ข้อความใหม่ได้ทุกเมื่อเพื่อเปลี่ยนเพลงที่สร้างขึ้น โมเดลจะเปลี่ยนไปอย่างราบรื่นตามข้อมูลใหม่

พรอมต์ต้องเป็นไปตามรูปแบบที่ถูกต้องโดยมี `text` (พรอมต์จริง) และ `weight` `weight` สามารถใช้ค่าใดก็ได้ยกเว้น `0` `1.0`
มักเป็นจุดเริ่มต้นที่ดี

### Python

```
  from google.genai import types

  await session.set_weighted_prompts(
    prompts=[
      {"text": "Piano", "weight": 2.0},
      types.WeightedPrompt(text="Meditation", weight=0.5),
      types.WeightedPrompt(text="Live Performance", weight=1.0),
    ]
  )
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

โปรดทราบว่าการเปลี่ยนโมเดลอาจเกิดขึ้นอย่างกะทันหันเมื่อเปลี่ยนพรอมต์อย่างมาก
จึงขอแนะนำให้ใช้การเฟดข้ามประเภทหนึ่งโดย
ส่งค่าถ่วงน้ำหนักกลางไปยังโมเดล

### อัปเดตการกำหนดค่า

คุณสามารถควบคุมการสร้างเพลงได้โดยการอัปเดตพารามิเตอร์การสร้างเพลงแบบเรียลไทม์ คุณจะอัปเดตเฉพาะพารามิเตอร์ไม่ได้ แต่ต้องตั้งค่าทั้ง
การกำหนดค่า มิเช่นนั้นระบบจะรีเซ็ตช่องอื่นๆ กลับเป็นค่าเริ่มต้น

เนื่องจากการอัปเดต bpm หรือสเกลเป็นการเปลี่ยนแปลงที่รุนแรงสำหรับโมเดล คุณจึงต้องบอกให้รีเซ็ตบริบทโดยใช้ `reset_context()` เพื่อนำการกำหนดค่าใหม่มาพิจารณาด้วย การดำเนินการนี้จะไม่หยุดสตรีม แต่จะเป็นการเปลี่ยนฉากแบบฮาร์ด คุณไม่จำเป็นต้องทำสำหรับพารามิเตอร์อื่นๆ

### Python

```
  from google.genai import types

  await session.set_music_generation_config(
    config=types.LiveMusicGenerationConfig(
      bpm=128,
      scale=types.Scale.D_MAJOR_B_MINOR,
      music_generation_mode=types.MusicGenerationMode.QUALITY
    )
  )
  await session.reset_context();
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    musicGenerationConfig: { 
      bpm: 120,
      density: 0.75,
      musicGenerationMode: MusicGenerationMode.QUALITY
    },
  });
  await session.reset_context();
```

## คู่มือการใช้พรอมต์สำหรับ Lyria RealTime

ต่อไปนี้คือรายการพรอมต์โดยสังเขปที่คุณใช้เพื่อพรอมต์ Lyria RealTime ได้

- เครื่องดนตรี: `303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone,
  Bagpipes, Balalaika Ensemble, Banjo, Bass Clarinet, Bongos, Boomy Bass,
  Bouzouki, Buchla Synths, Cello, Charango, Clavichord, Conga Drums,
  Didgeridoo, Dirty Synths, Djembe, Drumline, Dulcimer, Fiddle, Flamenco
  Guitar, Funk Drums, Glockenspiel, Guitar, Hang Drum, Harmonica, Harp,
  Harpsichord, Hurdy-gurdy, Kalimba, Koto, Lyre, Mandolin, Maracas, Marimba,
  Mbira, Mellotron, Metallic Twang, Moog Oscillations, Ocarina, Persian Tar,
  Pipa, Precision Bass, Ragtime Piano, Rhodes Piano, Shamisen, Shredding
  Guitar, Sitar, Slide Guitar, Smooth Pianos, Spacey Synths, Steel Drum, Synth
  Pads, Tabla, TR-909 Drum Machine, Trumpet, Tuba, Vibraphone, Viola Ensemble,
  Warm Acoustic Guitar, Woodwinds, ...`
- ประเภทเพลง: `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
  Bhangra, Bluegrass, Blues Rock, Bossa Nova, Breakbeat, Celtic Folk, Chillout,
  Chiptune, Classic Rock, Contemporary R&B, Cumbia, Deep House, Disco Funk,
  Drum & Bass, Dubstep, EDM, Electro Swing, Funk Metal, G-funk, Garage Rock,
  Glitch Hop, Grime, Hyperpop, Indian Classical, Indie Electronic, Indie Folk,
  Indie Pop, Irish Folk, Jam Band, Jamaican Dub, Jazz Fusion, Latin Jazz, Lo-Fi
  Hip Hop, Marching Band, Merengue, New Jack Swing, Minimal Techno, Moombahton,
  Neo-Soul, Orchestral Score, Piano Ballad, Polka, Post-Punk, 60s Psychedelic
  Rock, Psytrance, R&B, Reggae, Reggaeton, Renaissance Music, Salsa, Shoegaze,
  Ska, Surf Rock, Synthpop, Techno, Trance, Trap Beat, Trip Hop, Vaporwave,
  Witch house, ...`
- อารมณ์/คำอธิบาย: `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

นี่เป็นเพียงตัวอย่างบางส่วนเท่านั้น Lyria RealTime ทำได้มากกว่านี้ ทดลอง
กับพรอมต์ของคุณเอง

## แนวทางปฏิบัติแนะนำ

- แอปพลิเคชันไคลเอ็นต์ต้องใช้การบัฟเฟอร์เสียงที่มีประสิทธิภาพเพื่อให้
  การเล่นเป็นไปอย่างราบรื่น ซึ่งจะช่วยอธิบายถึงความผันผวนของเครือข่ายและความแตกต่างเล็กน้อยใน
  เวลาในการตอบสนองของการสร้าง
- การใช้พรอมต์อย่างมีประสิทธิภาพ
  - สื่อความหมาย ใช้คำคุณศัพท์ที่อธิบายอารมณ์ แนวเพลง และเครื่องดนตรี
  - ทำซ้ำและค่อยๆ ปรับเปลี่ยน แทนที่จะเปลี่ยนพรอมต์ทั้งหมด
    ให้ลองเพิ่มหรือแก้ไของค์ประกอบเพื่อเปลี่ยนเพลงให้ราบรื่นยิ่งขึ้น
  - ทดลองใช้ค่าถ่วงน้ำหนักใน `WeightedPrompt` เพื่อกำหนดว่าพรอมต์ใหม่จะส่งผลต่อการสร้างที่กำลังดำเนินอยู่อย่างไร

## รายละเอียดทางเทคนิค

ส่วนนี้จะอธิบายรายละเอียดเกี่ยวกับวิธีใช้การสร้างเพลงด้วย Lyria RealTime

### ข้อกำหนดเฉพาะ

- รูปแบบเอาต์พุต: เสียง PCM 16 บิตแบบดิบ
- อัตราการสุ่มตัวอย่าง: 48 kHz
- ช่องสัญญาณ: 2 (สเตอริโอ)

### การควบคุม

การสร้างเพลงสามารถรับอิทธิพลแบบเรียลไทม์ได้โดยการส่งข้อความที่มีเนื้อหาต่อไปนี้

- `WeightedPrompt`: สตริงข้อความที่อธิบายไอเดียเพลง แนวเพลง เครื่องดนตรี
  อารมณ์ หรือลักษณะ คุณอาจป้อนพรอมต์หลายรายการเพื่อผสมผสาน
  อิทธิพล ดูรายละเอียดเพิ่มเติมเกี่ยวกับวิธีพรอมต์
  Lyria RealTime ให้ได้ผลลัพธ์ดีที่สุดได้[ด้านบน](https://ai.google.dev/gemini-api/docs/:?hl=th#steer-music)
- `MusicGenerationConfig`: การกำหนดค่าสำหรับกระบวนการสร้างเพลง
  ซึ่งมีผลต่อลักษณะของเสียงเอาต์พุต) พารามิเตอร์
  ประกอบด้วย
  - `guidance`: (ลอย) ช่วง: `[0.0, 6.0]` ค่าเริ่มต้น: `4.0`
    ควบคุมความเข้มงวดที่โมเดลปฏิบัติตามพรอมต์ คำแนะนำที่สูงขึ้น
    จะช่วยให้ปฏิบัติตามพรอมต์ได้ดีขึ้น แต่จะทำให้การเปลี่ยนผ่านดูไม่ราบรื่น
  - `bpm`: (int) ช่วง: `[60, 200]`
    ตั้งค่าจังหวะต่อนาทีที่คุณต้องการสำหรับเพลงที่สร้างขึ้น คุณต้อง
    หยุด/เล่นหรือรีเซ็ตบริบทเพื่อให้โมเดลพิจารณา
    BPM ใหม่
  - `density`: (ลอย) ช่วง: `[0.0, 1.0]`
    ควบคุมความหนาแน่นของโน้ต/เสียงดนตรี ค่าที่ต่ำจะทำให้เพลงมีความเบาบางมากขึ้น
    ส่วนค่าที่สูงจะทำให้เพลง "หนักแน่น" มากขึ้น
  - `brightness`: (ลอย) ช่วง: `[0.0, 1.0]`
    ปรับคุณภาพโทนสี ค่าที่สูงขึ้นจะทำให้เสียง "สว่าง" ขึ้น
    โดยทั่วไปจะเน้นความถี่ที่สูงขึ้น
  - `scale`: (Enum)
    ตั้งค่าบันไดเสียง (คีย์และโหมด) สำหรับการสร้าง ใช้ค่า enum ของ [`Scale`](#scale-enum) ที่ SDK ระบุ คุณต้อง
    หยุด/เล่นหรือรีเซ็ตบริบทเพื่อให้โมเดลพิจารณาสเกลใหม่
  - `mute_bass`: (bool) ค่าเริ่มต้น: `False`
    ควบคุมว่าโมเดลจะลดเสียงเบสของเอาต์พุตหรือไม่
  - `mute_drums`: (bool) ค่าเริ่มต้น: `False`
    ควบคุมว่าเอาต์พุตของโมเดลจะลดเสียงกลองของเอาต์พุตหรือไม่
  - `only_bass_and_drums`: (bool) ค่าเริ่มต้น: `False`
    บังคับให้โมเดลพยายามเอาต์พุตเฉพาะเสียงเบสและกลอง
  - `music_generation_mode`: (Enum)
    ระบุให้โมเดลทราบว่าควรโฟกัสที่`QUALITY` (ค่าเริ่มต้น) หรือ`DIVERSITY` ของเพลง นอกจากนี้ ยังตั้งค่าเป็น `VOCALIZATION` เพื่อให้โมเดล
    สร้างเสียงร้องเป็นเครื่องดนตรีอีกชิ้นได้ด้วย (เพิ่มเป็นพรอมต์ใหม่)
- `PlaybackControl`: คำสั่งเพื่อควบคุมลักษณะการเล่น เช่น เล่น หยุดชั่วคราว
  หยุด หรือรีเซ็ตบริบท

สำหรับ `bpm`, `density`, `brightness` และ `scale` หากไม่ได้ระบุค่าไว้ โมเดลจะตัดสินใจว่าค่าใดดีที่สุดตามพรอมต์เริ่มต้นของคุณ

นอกจากนี้ คุณยังปรับแต่งพารามิเตอร์แบบคลาสสิกอื่นๆ เช่น `temperature` (0.0 ถึง 3.0 ค่าเริ่มต้นคือ 1.1), `top_k`
(1 ถึง 1000 ค่าเริ่มต้นคือ 40) และ `seed` (0 ถึง 2147483647 โดยระบบจะเลือกแบบสุ่ม
โดยค่าเริ่มต้น) ได้ใน `MusicGenerationConfig`

#### ค่า Enum ของมาตราส่วน

ค่าสเกลทั้งหมดที่โมเดลยอมรับได้มีดังนี้

| ค่า enum | สเกล / คีย์ |
| --- | --- |
| `C_MAJOR_A_MINOR` | คีย์ C เมเจอร์ / คีย์ A ไมเนอร์ |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | D♭ เมเจอร์ / B♭ ไมเนอร์ |
| `D_MAJOR_B_MINOR` | D major / B minor |
| `E_FLAT_MAJOR_C_MINOR` | E♭ เมเจอร์ / C ไมเนอร์ |
| `E_MAJOR_D_FLAT_MINOR` | อีเมเจอร์ / ซีชาร์ป/ดีแฟลตไมเนอร์ |
| `F_MAJOR_D_MINOR` | F เมเจอร์ / D ไมเนอร์ |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | G♭ เมเจอร์ / E♭ ไมเนอร์ |
| `G_MAJOR_E_MINOR` | G เมเจอร์ / E ไมเนอร์ |
| `A_FLAT_MAJOR_F_MINOR` | A♭ เมเจอร์ / F ไมเนอร์ |
| `A_MAJOR_G_FLAT_MINOR` | A เมเจอร์ / F♯/G♭ ไมเนอร์ |
| `B_FLAT_MAJOR_G_MINOR` | B♭ เมเจอร์ / G ไมเนอร์ |
| `B_MAJOR_A_FLAT_MINOR` | B เมเจอร์ / G♯/A♭ ไมเนอร์ |
| `SCALE_UNSPECIFIED` | ค่าเริ่มต้น / โมเดลตัดสิน |

โมเดลนี้สามารถแนะนำโน้ตที่เล่นได้ แต่ไม่สามารถแยกแยะคีย์ที่สัมพันธ์กันได้ ดังนั้นแต่ละ Enum จึงสอดคล้องกับ
หมายเลขเวอร์ชันหลักและเวอร์ชันย่อยที่เกี่ยวข้อง เช่น `C_MAJOR_A_MINOR` จะสอดคล้องกับคีย์สีขาวทั้งหมด
ของเปียโน และ `F_MAJOR_D_MINOR` จะเป็นคีย์สีขาวทั้งหมด
ยกเว้น B แฟลต

### ข้อจำกัด

- บรรเลงเท่านั้น: โมเดลจะสร้างเพลงบรรเลงเท่านั้น
- ความปลอดภัย: ตัวกรองความปลอดภัยจะตรวจสอบพรอมต์ ระบบจะไม่สนใจพรอมต์ที่ทริกเกอร์ตัวกรอง
  และจะเขียนคำอธิบายไว้ใน`filtered_prompt`ฟิลด์ของเอาต์พุตแทน
- การใส่ลายน้ำ: เสียงเอาต์พุตจะมีลายน้ำเสมอเพื่อการระบุตามหลักการ[AI ที่มีความรับผิดชอบ](https://ai.google/responsibility/principles/?hl=th)

## ขั้นตอนถัดไป

- สร้างเพลงและแทร็กเสียงร้องแบบเต็มด้วย [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=th)
- หากต้องการสร้างการสนทนาแบบหลายคนพูดโดยใช้[โมเดล TTS](https://ai.google.dev/gemini-api/docs/audio-generation?hl=th) แทนเพลง ให้ดูวิธีที่นี่
- ดูวิธีสร้าง[รูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)หรือ[วิดีโอ](https://ai.google.dev/gemini-api/docs/video?hl=th)
- แทนที่จะสร้างเพลงหรือเสียง ลองดูว่า Gemini สามารถ[ทำความเข้าใจไฟล์เสียง](https://ai.google.dev/gemini-api/docs/audio?hl=th)ได้อย่างไร
- สนทนากับ Gemini แบบเรียลไทม์โดยใช้
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=th)

ดูตัวอย่างโค้ดและบทแนะนำเพิ่มเติมได้ใน[ตำราอาหาร](https://github.com/google-gemini/cookbook)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-04-29 UTC"],[],[]]
