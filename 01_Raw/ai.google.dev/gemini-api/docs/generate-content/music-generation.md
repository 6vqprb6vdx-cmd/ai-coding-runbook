---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/music-generation?hl=th
fetched_at: 2026-08-24T02:27:26.659215+00:00
title: "\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e40\u0e1e\u0e25\u0e07\u0e14\u0e49\u0e27\u0e22 Lyria 3 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# สร้างเพลงด้วย Lyria 3

Lyria 3 คือกลุ่มโมเดลการสร้างเพลงของ Google ซึ่งพร้อมให้บริการ
ผ่าน Gemini API Lyria 3 ช่วยให้คุณสร้างเสียงสเตอริโอคุณภาพสูง 44.1 kHz
จากพรอมต์ข้อความหรือจากรูปภาพได้ โมเดลเหล่านี้ให้ความสอดคล้องเชิงโครงสร้าง
ซึ่งรวมถึงเสียงร้อง เนื้อเพลงที่กำหนดเวลา และการเรียบเรียงดนตรีบรรเลงทั้งหมด

ตระกูล Lyria 3 มีโมเดล 2 รายการ ได้แก่

| รุ่น | รหัสโมเดล | เหมาะสำหรับ | ระยะเวลา | เอาต์พุต |
| --- | --- | --- | --- | --- |
| **คลิป Lyria 3** | `lyria-3-clip-preview` | คลิปสั้น ลูป ตัวอย่าง | 30 วินาที | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | เพลงเต็มความยาวที่มีท่อนร้อง คอรัส และบริดจ์ | 2-3 นาที (ควบคุมได้ผ่านพรอมต์) | MP3 |

คุณสามารถใช้ทั้ง 2 โมเดลได้โดยใช้เมธอดมาตรฐาน `generateContent` และ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) ใหม่ ซึ่งรองรับอินพุตแบบมัลติโมดัล (ข้อความและรูปภาพ) และสร้างเสียง **สเตอริโอความเที่ยงตรงสูง 44.1 kHz**

## สร้างมิวสิกคลิป

โมเดลคลิป Lyria 3 จะสร้างคลิปความยาว **30 วินาที**เสมอ หากต้องการสร้าง
คลิป ให้เรียกใช้เมธอด `generateContent` ด้วยพรอมต์ข้อความ คำตอบจะมีเนื้อเพลงและโครงสร้างเพลงที่สร้างขึ้นพร้อมกับเสียงเสมอ

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="lyria-3-clip-preview",
    contents="Create a 30-second cheerful acoustic folk song with "
             "guitar and harmonica.",
)

# Parse the response
for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        with open("clip.mp3", "wb") as f:
            f.write(part.inline_data.data)
        print("Audio saved to clip.mp3")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "lyria-3-clip-preview",
    contents: "Create a 30-second cheerful acoustic folk song with " +
              "guitar and harmonica.",

  });

  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const buffer = Buffer.from(part.inlineData.data, "base64");
      fs.writeFileSync("clip.mp3", buffer);
      console.log("Audio saved to clip.mp3");
    }
  }
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "lyria-3-clip-preview",
        genai.Text("Create a 30-second cheerful acoustic folk song " +
                   "with guitar and harmonica."),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }

    for _, part := range result.Candidates[0].Content.Parts {
        if part.Text != "" {
            fmt.Println(part.Text)
        } else if part.InlineData != nil {
            err := os.WriteFile("clip.mp3", part.InlineData.Data, 0644)
            if err != nil {
                log.Fatal(err)
            }
            fmt.Println("Audio saved to clip.mp3")
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class GenerateMusicClip {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentResponse response = client.models.generateContent(
          "lyria-3-clip-preview",
          "Create a 30-second cheerful acoustic folk song with "
              + "guitar and harmonica.");

      for (Part part : response.parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("clip.mp3"), blob.data().get());
            System.out.println("Audio saved to clip.mp3");
          }
        }
      }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-clip-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a 30-second cheerful acoustic folk song with guitar and harmonica."}
      ]
    }]
  }'
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;
using System.IO;

public class GenerateMusicClip {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "lyria-3-clip-preview",
      contents: "Create a 30-second cheerful acoustic folk song with guitar and harmonica."
    );

    foreach (var part in response.Candidates[0].Content.Parts) {
      if (part.Text != null) {
        Console.WriteLine(part.Text);
      } else if (part.InlineData != null) {
        await File.WriteAllBytesAsync("clip.mp3", part.InlineData.Data);
        Console.WriteLine("Audio saved to clip.mp3");
      }
    }
  }
}
```

## สร้างเพลงแบบเต็มความยาว

ใช้โมเดล `lyria-3-pro-preview` เพื่อสร้างเพลงแบบเต็มความยาว 2-3 นาที โมเดล Pro เข้าใจโครงสร้างดนตรีและสามารถสร้าง
ผลงานที่มีท่อนร้อง คอรัส และบริดจ์ที่แตกต่างกัน คุณสามารถกำหนดระยะเวลาได้โดยระบุในพรอมต์ (เช่น "สร้างเพลง 2 นาที") หรือโดยใช้[การประทับเวลา](#timing)เพื่อกำหนดโครงสร้าง

### Python

```
response = client.models.generate_content(
    model="lyria-3-pro-preview",
    contents="An epic cinematic orchestral piece about a journey home. "
             "Starts with a solo piano intro, builds through sweeping "
             "strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "lyria-3-pro-preview",
  contents: "An epic cinematic orchestral piece about a journey home. " +
            "Starts with a solo piano intro, builds through sweeping " +
            "strings, and climaxes with a massive wall of sound.",

});
```

### Go

```
result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3-pro-preview",
    genai.Text("An epic cinematic orchestral piece about a journey " +
               "home. Starts with a solo piano intro, builds through " +
               "sweeping strings, and climaxes with a massive wall of sound."),
    nil,
)
```

### Java

```
GenerateContentResponse response = client.models.generateContent(
    "lyria-3-pro-preview",
    "An epic cinematic orchestral piece about a journey home. "
        + "Starts with a solo piano intro, builds through sweeping "
        + "strings, and climaxes with a massive wall of sound.");
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound."}
      ]
    }]
  }'
```

### C#

```
var response = await client.Models.GenerateContentAsync(
  model: "lyria-3-pro-preview",
  contents: "An epic cinematic orchestral piece about a journey home. " +
            "Starts with a solo piano intro, builds through sweeping " +
            "strings, and climaxes with a massive wall of sound."
);
```

## เลือกรูปแบบเอาต์พุต

โดยค่าเริ่มต้น โมเดล Lyria 3 จะสร้างเสียงในรูปแบบ **MP3** สำหรับ
Lyria 3 Pro คุณยังขอเอาต์พุตในรูปแบบ **WAV** ได้ด้วยโดยตั้งค่า
`response_format` ใน `generationConfig`

### Python

```
response = client.models.generate_content(
    model="lyria-3-pro-preview",
    contents="An atmospheric ambient track.",
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO", "TEXT"],
        response_format={"audio": {"mime_type": "audio/wav"}},
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "lyria-3-pro-preview",
  contents: "An atmospheric ambient track.",
  config: {
    responseModalities: ["AUDIO", "TEXT"],
    responseFormat: { audio: { mimeType: "audio/wav" } },
  },
});
```

### Go

```
config := &genai.GenerateContentConfig{
    ResponseModalities: []string{"AUDIO", "TEXT"},
    ResponseMIMEType:   "audio/wav",
}

result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3-pro-preview",
    genai.Text("An atmospheric ambient track."),
    config,
)
```

### Java

```
GenerateContentConfig config = GenerateContentConfig.builder()
    .responseModalities("AUDIO", "TEXT")
    .responseFormat(ResponseFormat.builder().audio(AudioFormat.builder().mimeType("audio/wav").build()).build())
    .build();

GenerateContentResponse response = client.models.generateContent(
    "lyria-3-pro-preview",
    "An atmospheric ambient track.",
    config);
```

### C#

```
var config = new GenerateContentConfig {
  ResponseModalities = { "AUDIO", "TEXT" },
  ResponseMimeType = "audio/wav"
};

var response = await client.Models.GenerateContentAsync(
  model: "lyria-3-pro-preview",
  contents: "An atmospheric ambient track.",
  config: config
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "An atmospheric ambient track."}
      ]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO", "TEXT"],
      "responseFormat": { "audio": { "mimeType": "audio/wav" } }
    }
  }'
```

## แยกวิเคราะห์คำตอบ

การตอบกลับจาก Lyria 3 มีหลายส่วน ส่วนข้อความมีเนื้อเพลงที่
สร้างขึ้นหรือคำอธิบาย JSON ของโครงสร้างเพลง ส่วนที่มี
`inline_data` จะมีไบต์เสียง

### Python

```
lyrics = []
audio_data = None

for part in response.parts:
    if part.text is not None:
        lyrics.append(part.text)
    elif part.inline_data is not None:
        audio_data = part.inline_data.data

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const part of response.candidates[0].content.parts) {
  if (part.text) {
    lyrics.push(part.text);
  } else if (part.inlineData) {
    audioData = Buffer.from(part.inlineData.data, "base64");
  }
}

if (lyrics.length) {
  console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
  fs.writeFileSync("output.mp3", audioData);
}
```

### Go

```
var lyrics []string
var audioData []byte

for _, part := range result.Candidates[0].Content.Parts {
    if part.Text != "" {
        lyrics = append(lyrics, part.Text)
    } else if part.InlineData != nil {
        audioData = part.InlineData.Data
    }
}

if len(lyrics) > 0 {
    fmt.Println("Lyrics:\n" + strings.Join(lyrics, "\n"))
}

if audioData != nil {
    err := os.WriteFile("output.mp3", audioData, 0644)
    if err != nil {
        log.Fatal(err)
    }
}
```

### Java

```
List<String> lyrics = new ArrayList<>();
byte[] audioData = null;

for (Part part : response.parts()) {
  if (part.text().isPresent()) {
    lyrics.add(part.text().get());
  } else if (part.inlineData().isPresent()) {
    audioData = part.inlineData().get().data().get();
  }
}

if (!lyrics.isEmpty()) {
  System.out.println("Lyrics:\n" + String.join("\n", lyrics));
}

if (audioData != null) {
  Files.write(Paths.get("output.mp3"), audioData);
}
```

### C#

```
var lyrics = new List<string>();
byte[] audioData = null;

foreach (var part in response.Candidates[0].Content.Parts) {
  if (part.Text != null) {
    lyrics.Add(part.Text);
  } else if (part.InlineData != null) {
    audioData = part.InlineData.Data;
  }
}

if (lyrics.Count > 0) {
  Console.WriteLine("Lyrics:\n" + string.Join("\n", lyrics));
}

if (audioData != null) {
  await File.WriteAllBytesAsync("output.mp3", audioData);
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.candidates[0].content.parts[] | select(.inlineData) | .inlineData.data' | base64 -d > output.mp3
```

## สร้างเพลงจากรูปภาพ

Lyria 3 รองรับอินพุตหลายรูปแบบ โดยคุณสามารถระบุ**รูปภาพได้สูงสุด 10 ภาพ**
พร้อมกับพรอมต์ข้อความ แล้วโมเดลจะแต่งเพลงที่ได้รับแรงบันดาลใจจาก
เนื้อหาภาพ

### Python

```
from PIL import Image

image = Image.open("desert_sunset.jpg")

response = client.models.generate_content(
    model="lyria-3-pro-preview",
    contents=[
        "An atmospheric ambient track inspired by the mood and "
        "colors in this image.",
        image,
    ],
)
```

### JavaScript

```
const imageData = fs.readFileSync("desert_sunset.jpg");
const base64Image = imageData.toString("base64");

const response = await ai.models.generateContent({
  model: "lyria-3-pro-preview",
  contents: [
    { text: "An atmospheric ambient track inspired by the mood " +
            "and colors in this image." },
    {
      inlineData: {
        mimeType: "image/jpeg",
        data: base64Image,
      },
    },
  ],

});
```

### Go

```
imgData, err := os.ReadFile("desert_sunset.jpg")
if err != nil {
    log.Fatal(err)
}

parts := []*genai.Part{
    genai.NewPartFromText("An atmospheric ambient track inspired " +
        "by the mood and colors in this image."),
    &genai.Part{
        InlineData: &genai.Blob{
            MIMEType: "image/jpeg",
            Data:     imgData,
        },
    },
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3-pro-preview",
    contents,
    nil,
)
```

### Java

```
GenerateContentResponse response = client.models.generateContent(
    "lyria-3-pro-preview",
    Content.fromParts(
        Part.fromText("An atmospheric ambient track inspired by "
            + "the mood and colors in this image."),
        Part.fromBytes(
            Files.readAllBytes(Path.of("desert_sunset.jpg")),
            "image/jpeg")));
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"contents\": [{
      \"parts\":[
          {\"text\": \"An atmospheric ambient track inspired by the mood and colors in this image.\"},
          {
            \"inline_data\": {
              \"mime_type\":\"image/jpeg\",
              \"data\": \"<BASE64_IMAGE_DATA>\"
            }
          }
      ]
    }]
  }"
```

### C#

```
var response = await client.Models.GenerateContentAsync(
  model: "lyria-3-pro-preview",
  contents: new List<Part> {
    Part.FromText("An atmospheric ambient track inspired by the mood and colors in this image."),
    Part.FromBytes(await File.ReadAllBytesAsync("desert_sunset.jpg"), "image/jpeg")
  }
);
```

![](https://storage.googleapis.com/generativeai-downloads/images/desert_sunset.jpg)

## ระบุเนื้อเพลงที่กำหนดเอง

คุณสามารถเขียนเนื้อเพลงของคุณเองและใส่ไว้ในพรอมต์ได้ ใช้แท็กส่วน
เช่น `[Verse]`, `[Chorus]` และ `[Bridge]` เพื่อช่วยให้โมเดลเข้าใจโครงสร้างเพลง

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

response = client.models.generate_content(
    model="lyria-3-pro-preview",
    contents=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const response = await ai.models.generateContent({
  model: "lyria-3-pro-preview",
  contents: prompt,

});
```

### Go

```
prompt := `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`

result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3-pro-preview",
    genai.Text(prompt),
    nil,
)
```

### Java

```
String prompt = """
    Create a dreamy indie pop song with the following lyrics:

    [Verse 1]
    Walking through the neon glow,
    city lights reflect below,
    every shadow tells a story,
    every corner, fading glory.

    [Chorus]
    We are the echoes in the night,
    burning brighter than the light,
    hold on tight, don't let me go,
    we are the echoes down below.

    [Verse 2]
    Footsteps lost on empty streets,
    rhythms sync to heartbeats,
    whispers carried by the breeze,
    dancing through the autumn leaves.
    """;

GenerateContentResponse response = client.models.generateContent(
    "lyria-3-pro-preview",
    prompt);
```

### C#

```
var prompt = @"
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
";

var response = await client.Models.GenerateContentAsync(
  model: "lyria-3-pro-preview",
  contents: prompt
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a dreamy indie pop song with the following lyrics: ..."}
      ]
    }]
  }'
```

[

](https://storage.googleapis.com/generativeai-downloads/songs/Neon%20Echoes_Lyrics.webm)

## ควบคุมเวลาและโครงสร้าง

คุณสามารถระบุสิ่งที่เกิดขึ้นในช่วงเวลาที่เฉพาะเจาะจงในเพลงได้โดยใช้
การประทับเวลา ซึ่งมีประโยชน์ในการควบคุมเวลาที่เครื่องดนตรีเริ่มเล่น เวลาที่เนื้อเพลง
ปรากฏ และวิธีที่เพลงดำเนินไป ดังนี้

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

response = client.models.generate_content(
    model="lyria-3-pro-preview",
    contents=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const response = await ai.models.generateContent({
  model: "lyria-3-pro-preview",
  contents: prompt,

});
```

### Go

```
prompt := `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`

result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3-pro-preview",
    genai.Text(prompt),
    nil,
)
```

### Java

```
String prompt = """
    [0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
                  vinyl crackle.
    [0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
                  and gentle vocals singing about a rainy morning.
    [0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
                  synth leads. The lyrics are hopeful and uplifting.
    [0:50 - 1:00] Outro: Fade out with the piano melody alone.
    """;

GenerateContentResponse response = client.models.generateContent(
    "lyria-3-pro-preview",
    prompt);
```

### C#

```
var prompt = @"
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
";

var response = await client.Models.GenerateContentAsync(
  model: "lyria-3-pro-preview",
  contents: prompt
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "[0:00 - 0:10] Intro: ..."}
      ]
    }]
  }'
```

## สร้างแทร็กบรรเลง

สำหรับเพลงประกอบ เกมซาวด์แทร็ก หรือกรณีการใช้งานใดๆ ที่ไม่จำเป็นต้องมีเสียงร้อง
คุณสามารถแจ้งให้โมเดลสร้างแทร็กเฉพาะดนตรีได้โดยทำดังนี้

### Python

```
response = client.models.generate_content(
    model="lyria-3-clip-preview",
    contents="A bright chiptune melody in C Major, retro 8-bit "
             "video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "lyria-3-clip-preview",
  contents: "A bright chiptune melody in C Major, retro 8-bit " +
            "video game style. Instrumental only, no vocals.",

});
```

### Go

```
result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3-clip-preview",
    genai.Text("A bright chiptune melody in C Major, retro 8-bit " +
               "video game style. Instrumental only, no vocals."),
    nil,
)
```

### Java

```
GenerateContentResponse response = client.models.generateContent(
    "lyria-3-clip-preview",
    "A bright chiptune melody in C Major, retro 8-bit "
        + "video game style. Instrumental only, no vocals.");
```

### C#

```
var response = await client.Models.GenerateContentAsync(
  model: "lyria-3-clip-preview",
  contents: "A bright chiptune melody in C Major, retro 8-bit " +
            "video game style. Instrumental only, no vocals."
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-clip-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."}
      ]
    }]
  }'
```

## สร้างเพลงในภาษาต่างๆ

Lyria 3 จะสร้างเนื้อเพลงในภาษาของพรอมต์ หากต้องการสร้างเพลง
ที่มีเนื้อร้องเป็นภาษาฝรั่งเศส ให้เขียนพรอมต์เป็นภาษาฝรั่งเศส โมเดลจะปรับรูปแบบการร้อง
และการออกเสียงให้ตรงกับภาษา

### Python

```
response = client.models.generate_content(
    model="lyria-3-pro-preview",
    contents="Crée une chanson pop romantique en français sur un "
             "coucher de soleil à Paris. Utilise du piano et de "
             "la guitare acoustique.",
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "lyria-3-pro-preview",
  contents: "Crée une chanson pop romantique en français sur un " +
            "coucher de soleil à Paris. Utilise du piano et de " +
            "la guitare acoustique.",

});
```

### Go

```
result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3-pro-preview",
    genai.Text("Crée une chanson pop romantique en français sur un " +
               "coucher de soleil à Paris. Utilise du piano et de " +
               "la guitare acoustique."),
    nil,
)
```

### Java

```
GenerateContentResponse response = client.models.generateContent(
    "lyria-3-pro-preview",
    "Crée une chanson pop romantique en français sur un "
        + "coucher de soleil à Paris. Utilise du piano et de "
        + "la guitare acoustique.");
```

### C#

```
var response = await client.Models.GenerateContentAsync(
  model: "lyria-3-pro-preview",
  contents: "Crée une chanson pop romantique en français sur un " +
            "coucher de soleil à Paris. Utilise du piano et de " +
            "la guitare acoustique."
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."}
      ]
    }]
  }'
```

## ความสามารถของโมเดล

Lyria 3 จะวิเคราะห์กระบวนการพรอมต์ของคุณ โดยโมเดลจะพิจารณาโครงสร้างดนตรี (ท่อนนำ ท่อนร้อง คอรัส บริดจ์ ฯลฯ)
ตามพรอมต์ของคุณ
ซึ่งจะเกิดขึ้นก่อนที่จะสร้างเสียง และช่วยให้มั่นใจได้ถึงความสอดคล้องของโครงสร้างและความเป็นดนตรี

## Interactions API

คุณสามารถใช้โมเดล Lyria 3 กับ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) ซึ่งเป็นอินเทอร์เฟซแบบรวมสำหรับการโต้ตอบกับโมเดลและเอเจนต์ของ Gemini ซึ่งช่วยลดความซับซ้อนในการจัดการสถานะและงานที่ใช้เวลานานสำหรับกรณีการใช้งานหลายรูปแบบที่ซับซ้อน

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="A melancholic jazz fusion track in D minor, " +
          "featuring a smooth saxophone melody, walking bass line, " +
          "and complex drum rhythms.",
)

for output in interaction.outputs:
    if output.text:
        print(output.text)
    elif output.inline_data:
         with open("interaction_output.mp3", "wb") as f:
            f.write(output.inline_data.data)
         print("Audio saved to interaction_output.mp3")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: 'lyria-3-pro-preview',
  input: 'A melancholic jazz fusion track in D minor, ' +
         'featuring a smooth saxophone melody, walking bass line, ' +
         'and complex drum rhythms.',
});

for (const output of interaction.outputs) {
  if (output.text) {
    console.log(output.text);
  } else if (output.inlineData) {
    const buffer = Buffer.from(output.inlineData.data, 'base64');
    fs.writeFileSync('interaction_output.mp3', buffer);
    console.log('Audio saved to interaction_output.mp3');
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A melancholic jazz fusion track in D minor, featuring a smooth saxophone melody, walking bass line, and complex drum rhythms."
}'
```

## คำแนะนำในการเขียนพรอมต์

พรอมต์ของคุณอาจเรียบง่าย เช่น "เพลงโฟล์กเกี่ยวกับแมวน่ารักที่หลบหลีกแอ่งน้ำ
เสียงร้องของผู้หญิงและเสียงฝน" หรืออาจมีรายละเอียดและโครงสร้าง
เช่น

> แทร็กซินธ์ป๊อปสไตล์ยุค 80 ที่มีบีทเร้าใจ ซินธิไซเซอร์ที่เปล่งประกาย
> และท่อนคอรัสที่ติดหูและเป็นเพลงประจำตัว เพลงควรให้ความรู้สึกย้อนยุคแบบอนาคต
> ชวนให้นึกถึงเพลงป๊อปฮิตคลาสสิกในยุค 80 พร้อมการปรับงานสร้างให้ทันสมัย
> เทมโปควรสนุกสนานและเต้นได้ โดยอยู่ที่ประมาณ 120 BPM พร้อม
> โครงสร้างท่อน-คอรัสที่ชัดเจนและท่อนฮุกที่เป็นเครื่องดนตรีที่น่าจดจำ เนื้อเพลงพูดถึง
> ความรู้สึกของการเตรียมตัวไปปาร์ตี้

ทั้งพรอมต์ที่เรียบง่ายและซับซ้อนสามารถให้เอาต์พุตที่ดีได้ เราขอแนะนำให้
ทดลองใช้เคล็ดลับเหล่านี้เพื่อค้นหาสิ่งที่เหมาะกับคุณมากที่สุด

### ประเภท

นำหน้าพรอมต์ด้วยแนวเพลงที่คุณต้องการ เช่น ฮิปฮอป ร็อก และ
แร็ป คุณระบุแนวเพลงผสมได้ดังนี้

- การผสมผสานระหว่างเมทัลกับแร็ป
- การผสมผสานระหว่างเดธเมทัลและโอเปร่า
- เพลงคลาสสิกที่มีองค์ประกอบเสียงโดรนอิเล็กทรอนิกส์
- เพลงอิเล็กทรอนิกส์แดนซ์ (EDM) สมัยใหม่ผสมกับเพลงป๊อปยุโรป

นอกจากนี้ คุณยังระบุยุคได้ด้วย

- ฮิปฮอปช่วงต้นยุค 90
- เพลงป๊อปเยเย่ฝรั่งเศสยุค 60
- การทดลองอิเล็กทรอนิกส์ในยุค 80
- เพลงป๊อปกระแสหลักยุค 2000

หากคุณป้อนพรอมต์สำหรับแนวเพลงเฉพาะหรือแนวเพลงย่อยในภูมิภาค เช่น "เทคโนเบอร์ลิน" หรือ "ไฮฟีในเบย์แอเรีย" โมเดลจะพยายามจับแก่นแท้ของแนวเพลงนั้นๆ แต่อาจไม่ถูกต้องเสมอไป

### เครื่องดนตรี

โดยค่าเริ่มต้น Lyria 3 จะสร้างเพลงด้วยเครื่องดนตรีและเครื่องมือที่คุณ
คาดหวังสำหรับแนวเพลงนั้นๆ คุณไม่จำเป็นต้องกำหนดแนวทาง

แต่แทร็กแดนซ์จะไม่มีแซกโซโฟน เว้นแต่คุณจะขอ ดังนั้นหากต้องการให้มีเสียงแซกโซโฟน คุณต้องป้อนพรอมต์ดังนี้

> แทร็กเต้นรำที่มีบีทหนักแน่น ซินธิไซเซอร์ที่เปล่งประกาย และท่อนฮุกที่ติดหู
> ราวกับเป็นเพลงชาติ โซโลแซกโซโฟนควรเริ่มเล่นในช่วงท่อนบริดจ์

พรอมต์ของคุณอาจรวมถึงเครื่องดนตรีที่เฉพาะเจาะจง เสียงของเครื่องดนตรี และวิธีที่เครื่องดนตรี
โต้ตอบกัน คุณใช้การผสมผสานนี้เพื่อสร้างอารมณ์หรือพื้นผิวบางอย่างได้

- เสียงเบสที่สกปรกและบิดเบี้ยวต่อสู้กับเสียงไฮแฮตที่สะอาดและคมชัด
- ซินธ์แพดแบบอนาล็อกที่อบอุ่นซึ่งขยายตัวอยู่ใต้เสียงกีตาร์โปร่งที่แห้งและใกล้ชิด
- กำแพงเสียงที่สร้างขึ้นจากกีตาร์แตกพร่าหลายเลเยอร์ พร้อมเสียงร้องที่ฝังอยู่
  ไกลๆ

### โครงสร้างเพลง

คุณสามารถระบุความคืบหน้าของเพลงในพรอมต์ได้ ใช้ลูกศรหรือรายการ
เพื่อกำหนดโฟลว์

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- เริ่มด้วยอินโทรเปียโนที่เงียบสงบ ค่อยๆ เพิ่มระดับเสียงจนถึงท่อนร้องที่ดัง จากนั้นลดระดับเสียงลงจน
  เงียบ แล้วระเบิดออกมาเป็นท่อนคอรัส

นอกจากนี้ คุณยังระบุวิธีที่ระดับพลังงานเปลี่ยนแปลงระหว่างส่วนต่างๆ เหล่านี้ได้ด้วย

- สร้างความตึงเครียดในท่อนก่อนฮุก แล้วปล่อยให้เงียบก่อนจะเข้าท่อนฮุกที่หนักแน่น
  และทรงพลัง
- ค่อยๆ เพิ่มความเข้มข้นของเพลงทีละน้อย
  จนกระทั่งเกิดกำแพงเสียงที่วุ่นวาย
- หยุดกะทันหันหลังท่อนบริดจ์ ตามด้วยคอรัสแบบอะแคปเปลลา

นอกจากนี้ คุณยังป้อนเวลาที่ต้องการให้เกิดเหตุการณ์ได้ด้วย

- สร้างการดรอปที่ 12 วินาที
- มีคนพูดว่า "อะไรนะ" ทุกๆ 2 วินาที
- ท่อนคอรัสเริ่มที่ 22 วินาที

### เนื้อเพลง

ระบบจะสร้างเสียงร้องและเนื้อเพลงโดยค่าเริ่มต้น คุณสามารถระบุเนื้อเพลงของคุณเอง
ขอไม่ให้มีเนื้อเพลง (หรือขอเป็นเพลงบรรเลง) หรือกำหนดทิศทางการสร้างเนื้อเพลง
ตามที่คุณต้องการได้

เนื้อเพลงจะเป็นภาษาเดียวกับที่คุณใช้เขียนพรอมต์ นอกจากนี้ คุณยังขอให้เขียนเนื้อเพลงเป็นภาษาอื่นได้ด้วย เช่น "เขียนเนื้อเพลงเป็นภาษาฝรั่งเศส"

#### การใช้เนื้อเพลงของคุณเอง

หากต้องการให้โมเดลใช้เนื้อเพลงของคุณเอง ให้ใส่เนื้อเพลงในพรอมต์โดยมีคำนำหน้า "เนื้อเพลง:"

```
Lyrics:

[Intro]
Oooh, oooh

[Verse 1]
Let's go
Let's go
Go with the flow

[Chorus]
...
```

คุณสามารถใส่คำนำหน้าส่วนต่างๆ ของเพลงด้วยชื่อส่วน เช่น `[Intro]`,
`[Verse 1]`, `[Pre-chorus]`, `[Chorus]` และ `[Outro]`

หากต้องการให้คำหรือบรรทัดซ้ำ เช่น เสียงก้องหรือนักร้องประสานเสียง
คุณสามารถใส่ไว้ในวงเล็บได้ เช่น "ไปกันเลย (ไป)"

#### การป้อนพรอมต์ให้โมเดลเขียนเนื้อเพลง

หากต้องการให้ Lyria 3 สร้างเนื้อเพลงให้คุณ คุณควรใส่รายละเอียด
เกี่ยวกับเนื้อหาของเนื้อเพลงในพรอมต์ ไม่เช่นนั้น โมเดลจะต้องอนุมานเรื่องจากพรอมต์เพลงของคุณ ซึ่งอาจไม่ใช่สิ่งที่คุณต้องการ

> เนื้อเพลงพูดถึงความรักที่สูญเสียไปและความเจ็บปวดจากความอกหัก นักร้องกำลัง
> หวนรำลึกถึงความสัมพันธ์ในอดีตและความทรงจำที่
> หลั่งไหลกลับมา

หากต้องการให้มีท่อนคอรัสซ้ำๆ คุณควรระบุในพรอมต์

> เนื้อเพลงพูดถึงความรักที่สูญเสียไปและความเจ็บปวดจากความอกหัก นักร้องกำลัง
> หวนรำลึกถึงความสัมพันธ์ในอดีตและความทรงจำที่
> หลั่งไหลกลับมา ท่อนคอรัสที่ทรงพลังมุ่งเน้นไปที่การก้าวข้ามความเจ็บปวดและเดินหน้าต่อไป

Lyria 3 จะกำหนดโครงสร้างของเนื้อเพลงให้สอดคล้องกับ
ประเภทเพลงที่คุณขอโดยอัตโนมัติ แต่คุณสามารถเน้นย้ำเรื่องนี้ในพรอมต์ได้ด้วย
เช่น

> แทร็ก EDM ที่ใช้วลีเดียวกันซ้ำๆ

นอกจากนี้ คุณยังป้อนพรอมต์เพื่อขอเอฟเฟกต์เสียงร้องที่ไม่ใช่เนื้อเพลงโดยตรงได้ด้วย เช่น

- ตัวอย่างที่เล่นซ้ำจากภาพยนตร์พูดว่า "ฉันไม่อยากจะเชื่อเลย" ตลอดทั้งเพลง
- เพลงเทคโนที่มีพลังสูง ก่อนที่ดนตรีจะเริ่มเล่น เสียงทั้งหมดจะหยุดลงและมีเสียงเล็กๆ พูดว่า "ฉันไม่รู้ว่ามาทำอะไรที่นี่" แล้วดนตรีก็เริ่มเล่น
- โดยเพลงนี้เปิดด้วยการพูดคุยเกี่ยวกับภาพยนตร์ในยุค 90 ที่
  ดีกว่าปัจจุบัน จากนั้นเพลงจะเปลี่ยนเป็นเพลงป๊อป

### เสียงร้อง

คุณสามารถป้อนพรอมต์เพื่อระบุวิธีที่ต้องการให้แสดงเนื้อเพลงได้ ระบุโปรไฟล์นักร้องแบบละเอียดซึ่งครอบคลุมเพศ โทนเสียง และช่วงเสียงร้องเพื่อให้ได้ผลลัพธ์ที่ดีที่สุด

- **เสียงโซปราโนหญิง**: เสียงใสราวคริสตัลที่มีคุณภาพสูงและคล่องแคล่ว
  ร้องโน้ตสูงที่หวีดหวิวได้ด้วยเนื้อเสียงที่โปร่งและมีลม
- **อัลโตหญิง**: เสียงทุ้มที่อบอุ่นและแหบพร่า เสียงทุ้มต่ำที่มี
  การสั่นของเส้นเสียงเล็กน้อย มีพลังและก้องกังวาน
- **เสียงเทเนอร์ชาย**: สดใส ก้องกังวาน และมีพลัง เสียงที่สดใสพร้อม
  เสียงขึ้นจมูกเล็กน้อยที่โดดเด่นในมิกซ์ด้วยพลังเสียงสูง
- **บาริโทนชาย**: เสียงทุ้ม นุ่มนวล และลื่นไหล เสียงทุ้มก้องกังวาน
  พร้อมการขับร้องที่นุ่มนวลและกล่อมเกลา
- **ร็อกเกอร์รุ่นเก๋า (ชาย)**: เสียงแหบแห้งและมีเนื้อเสียงหยาบ
  ชวนให้นึกถึงเพลงกรันจ์ยุค 90 ช่วงเสียงสูงที่ตึงเครียดสำหรับความเข้มข้นทางอารมณ์

### พารามิเตอร์พรอมต์อื่นๆ

คุณยังใส่พารามิเตอร์ต่อไปนี้เพื่อปรับแต่งพรอมต์เพิ่มเติมได้ด้วย

- **คีย์/สเกล**: ระบุคีย์เพลง (เช่น "ในคีย์ G เมเจอร์" "ในคีย์ D ไมเนอร์")
- **อารมณ์และบรรยากาศ**: ใช้คำคุณศัพท์ที่อธิบายรายละเอียด (เช่น "หวนรำลึก"
  "ดุดัน" "เหนือจริง" "เหมือนฝัน")
- **ระยะเวลา**: โมเดลคลิปจะสร้างคลิปความยาว 30 วินาทีเสมอ สำหรับโมเดล Pro
  ให้ระบุความยาวที่ต้องการในพรอมต์ (เช่น "สร้างเพลงยาว 2 นาที")
  หรือใช้การประทับเวลาเพื่อควบคุมระยะเวลา

### ตัวอย่างพรอมต์

ตัวอย่างพรอมต์ที่มีประสิทธิภาพมีดังนี้

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## แนวทางปฏิบัติแนะนำ

- **ทำซ้ำด้วยฟีเจอร์คลิปก่อน** ใช้`lyria-3-clip-preview`โมเดลที่เร็วกว่า`lyria-3-pro-preview`เพื่อทดลองใช้พรอมต์ก่อนที่จะสร้างเนื้อหาแบบเต็มด้วย`lyria-3-clip-preview`
- **ใช้คำที่เฉพาะเจาะจง** พรอมต์ที่คลุมเครือจะให้ผลลัพธ์ทั่วไป ระบุเครื่องดนตรี
  BPM, คีย์, อารมณ์ และโครงสร้างเพื่อให้ได้ผลลัพธ์ที่ดีที่สุด
- **ใช้แท็กส่วน** แท็ก `[Verse]`, `[Chorus]`, `[Bridge]` ช่วยให้โมเดลมีโครงสร้างที่ชัดเจน
  ให้ทำตาม
- **แยกเนื้อเพลงออกจากวิธีการ** เมื่อระบุเนื้อเพลงที่กำหนดเอง ให้แยกเนื้อเพลงออกจากคำสั่งเกี่ยวกับทิศทางดนตรีอย่างชัดเจน

## ข้อจำกัด

- **ความปลอดภัย**: ตัวกรองความปลอดภัยจะตรวจสอบพรอมต์ทั้งหมด ระบบจะบล็อกพรอมต์ที่ทริกเกอร์
  ตัวกรอง ซึ่งรวมถึงพรอมต์ที่ขอเสียงของศิลปินที่เฉพาะเจาะจง
  หรือการสร้างเนื้อเพลงที่มีลิขสิทธิ์
- **การใส่ลายน้ำ**: เสียงที่สร้างขึ้นทั้งหมดจะมี
  [ลายน้ำที่เป็นเสียง SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=th) สำหรับ
  การระบุ ลายน้ำนี้จะมองไม่เห็นด้วยตาเปล่าและ
  ไม่ส่งผลต่อประสบการณ์การฟัง
- **การแก้ไขแบบผ่านการสนทนาไปมา**: การสร้างเพลงเป็นกระบวนการแบบผ่านการสนทนาไปมา
  การแก้ไขซ้ำๆ หรือการปรับแต่งคลิปที่สร้างขึ้นผ่านพรอมต์หลายรายการ
  ไม่รองรับใน Lyria 3 เวอร์ชันปัจจุบัน
- **ความยาว**: โมเดลคลิปจะสร้างคลิปความยาว 30 วินาทีเสมอ โมเดล Pro
  สร้างเพลงที่มีความยาว 2-3 นาที โดยระยะเวลาที่แน่นอนอาจ
  ได้รับอิทธิพลจากพรอมต์ของคุณ
- **การกำหนด**: ผลลัพธ์อาจแตกต่างกันไปในแต่ละการเรียกใช้ แม้จะใช้พรอมต์เดียวกันก็ตาม

## ขั้นตอนถัดไป

- ดู[ราคา](https://ai.google.dev/gemini-api/docs/generate-content/pricing?hl=th)สำหรับโมเดล Lyria 3
- ลอง[การสร้างเพลงแบบเรียลไทม์และสตรีมมิง](https://ai.google.dev/gemini-api/docs/generate-content/realtime-music-generation?hl=th)ด้วย
  Lyria RealTime
- สร้างการสนทนาแบบหลายคนพูดด้วย[โมเดล TTS](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=th)
- ดูวิธีสร้าง[รูปภาพ](https://ai.google.dev/gemini-api/docs/generate-content/image-generation?hl=th)หรือ[วิดีโอ](https://ai.google.dev/gemini-api/docs/generate-content/video?hl=th)
- ดูวิธีที่ Gemini [เข้าใจไฟล์เสียง](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=th)
- สนทนากับ Gemini แบบเรียลไทม์โดยใช้
  [Live API](https://ai.google.dev/gemini-api/docs/generate-content/live?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
