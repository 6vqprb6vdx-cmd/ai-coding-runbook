---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=th
fetched_at: 2026-10-26T06:06:06.356486+00:00
title: "\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e40\u0e1e\u0e25\u0e07\u0e14\u0e49\u0e27\u0e22 Lyria 3.5 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# สร้างเพลงด้วย Lyria 3.5

Lyria 3.5 คือกลุ่มโมเดลการสร้างเพลงของ Google ซึ่งพร้อมให้บริการผ่าน Gemini API Lyria 3.5 ช่วยให้คุณสร้างเสียงสเตอริโอ 44.1 kHz คุณภาพสูงจากพรอมต์ข้อความหรือจากรูปภาพได้ โมเดลเหล่านี้ให้ความสอดคล้องเชิงโครงสร้าง ซึ่งรวมถึงเสียงร้อง เนื้อเพลงที่กำหนดเวลา และการเรียบเรียงดนตรีบรรเลงทั้งหมด

ตระกูล Lyria มีโมเดลต่อไปนี้

| รุ่น | รหัสโมเดล | เหมาะสำหรับ | ระยะเวลา | เอาต์พุต |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | คลิปสั้น วิดีโอวนซ้ำ ตัวอย่าง | 30 วินาที | MP3 |
| **Lyria 3.5** | `lyria-3.5` | เพลงแบบเต็มความยาวที่มีท่อนร้อง คอรัส และบริดจ์ | 2-3 นาที (ควบคุมได้โดยใช้พรอมต์) | MP3 |

คุณใช้ทั้ง 2 โมเดลได้โดยใช้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) ใหม่ ซึ่งรองรับอินพุตแบบหลายโมดัล (ข้อความและรูปภาพ) และสร้างเสียง**สเตอริโอที่มีความเที่ยงตรงสูง 44.1 kHz**

## สร้างมิวสิกคลิป

โมเดลคลิป Lyria 3 จะสร้างคลิปความยาว **30 วินาที**เสมอ หากต้องการสร้าง
คลิป ให้เรียกใช้เมธอด `interactions.create` ด้วยพรอมต์ข้อความ คำตอบ
จะมีเนื้อเพลงและโครงสร้างเพลงที่สร้างขึ้นพร้อมกับเสียงใน
สคีมา `steps` เสมอ

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-clip-preview"))
        .input(InteractionsInput.of("A short instrumental acoustic guitar piece."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputAudio().isPresent() && interaction.outputAudio().get().data().isPresent()) {
  byte[] audioBytes = Base64.getDecoder().decode(interaction.outputAudio().get().data().get());
  Files.write(Paths.get("music.mp3"), audioBytes);
}

interaction.outputText().ifPresent(lyrics -> System.out.println("Lyrics:\n" + lyrics));
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3-clip-preview"),
            Input: interactions.NewInteractionsInput("A short instrumental acoustic guitar piece."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        audioBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("music.mp3", audioBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Printf("Lyrics:\n%s\n", *res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

คุณสามารถดึงข้อมูลเพลงที่สร้างขึ้นได้โดยใช้พร็อพเพอร์ตี้ `interaction.output_audio`
ซึ่งจะแสดงบล็อกเสียงที่สร้างล่าสุด นอกจากนี้ คุณยังดึงข้อมูล
เนื้อเพลงและโครงสร้างของเพลงได้โดยใช้พร็อพเพอร์ตี้ `interaction.output_text`
ดูรายละเอียดเกี่ยวกับพร็อพเพอร์ตี้ความสะดวกได้ที่[ภาพรวมของการโต้ตอบ](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th#convenience-properties)

## สร้างเพลงแบบเต็มความยาว

ใช้โมเดล `lyria-3.5` เพื่อสร้างเพลงแบบเต็มความยาว 2-3 นาที โมเดล Pro เข้าใจโครงสร้างดนตรีและสามารถสร้าง
ผลงานที่มีท่อน Verse, Chorus และ Bridge ที่แตกต่างกันได้ คุณกำหนดระยะเวลาได้โดยระบุในพรอมต์ (เช่น "สร้างเพลง 2 นาที") หรือโดยใช้[การประทับเวลา](#timing)เพื่อกำหนดโครงสร้าง

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(
            InteractionsInput.of(
                "An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(
                "An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3.5",
    "input": "A beautiful piano melody."
}'
```

## เลือกรูปแบบเอาต์พุต

โดยค่าเริ่มต้น โมเดล Lyria 3.5 จะสร้างเสียงในรูปแบบ **MP3** สำหรับ Lyria 3.5 คุณยังขอเอาต์พุตในรูปแบบ **WAV** ได้ด้วยโดยตั้งค่า
`response_format`

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioResponseFormat;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of("A beautiful piano melody."))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(AudioResponseFormat.builder().build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput("A beautiful piano melody."),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## แยกวิเคราะห์คำตอบ

การตอบกลับจาก Lyria 3.5 มีบล็อกเนื้อหาหลายรายการภายในสคีมา `steps`
การโต้ตอบจะแสดงผลลำดับขั้นตอน โดยขั้นตอน `model_output` จะมีเนื้อหาที่สร้างขึ้น
บล็อกเนื้อหาข้อความจะมีเนื้อเพลงที่สร้างขึ้นหรือคำอธิบาย JSON ของโครงสร้างเพลง
บล็อกเนื้อหาที่มี`audio`ประเภทจะมีข้อมูลเสียงที่เข้ารหัส Base64

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of("A song about a starry night."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputAudio().isPresent() && interaction.outputAudio().get().data().isPresent()) {
  byte[] audioBytes = Base64.getDecoder().decode(interaction.outputAudio().get().data().get());
  Files.write(Paths.get("output.mp3"), audioBytes);
}

if (interaction.outputText().isPresent()) {
  System.out.println("Lyrics:\n" + interaction.outputText().get());
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput("A song about a starry night."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        audioBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("output.mp3", audioBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Printf("Lyrics:\n%s\n", *res.Interaction.OutputText)
    }
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### เนื้อเพลงและเพลงที่สลับกัน

เนื่องจากเอาต์พุตจาก Lyria 3.5 มีความซับซ้อน โดยมีขั้นตอนและบล็อกแยกกันสำหรับเนื้อเพลง (ข้อความ) และตัวเพลง (เสียง) ที่สร้างขึ้น คุณสมบัติความสะดวกจึงเป็นทางลัดที่รวดเร็วและแนะนำ

อย่างไรก็ตาม หากต้องการควบคุมไทม์ไลน์แบบดิบของขั้นตอนต่างๆ อย่างเต็มรูปแบบโดยใช้โปรแกรม
ที่เซิร์ฟเวอร์ส่งคืน (เช่น การบันทึกบล็อกเนื้อหาแต่ละรายการเมื่อได้รับ
) คุณสามารถวนซ้ำ `steps` ด้วยตนเองแทนได้

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

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

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of("A song about a starry night."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

List<String> lyrics = new ArrayList<>();
byte[] audioData = null;

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof AudioContent) {
            AudioContent audioBlock = (AudioContent) contentBlock;
            if (audioBlock.data().isPresent()) {
              audioData = Base64.getDecoder().decode(audioBlock.data().get());
            }
          } else if (contentBlock instanceof TextContent) {
            TextContent textBlock = (TextContent) contentBlock;
            textBlock.text().ifPresent(lyrics::add);
          }
        }
      }
    }
  }
}

if (!lyrics.isEmpty()) {
  System.out.println("Lyrics:\n" + String.join("\n", lyrics));
}

if (audioData != null) {
  Files.write(Paths.get("output.mp3"), audioData);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"
    "strings"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput("A song about a starry night."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var lyrics []string
    var audioData []byte

    for _, step := range res.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, contentBlock := range step.ModelOutputStep.Content {
                if contentBlock.AudioContent != nil && contentBlock.AudioContent.Data != nil {
                    decoded, err := base64.StdEncoding.DecodeString(*contentBlock.AudioContent.Data)
                    if err != nil {
                        log.Fatal(err)
                    }
                    audioData = decoded
                } else if contentBlock.TextContent != nil {
                    lyrics = append(lyrics, contentBlock.TextContent.Text)
                }
            }
        }
    }

    if len(lyrics) > 0 {
        fmt.Printf("Lyrics:\n%s\n", strings.Join(lyrics, "\n"))
    }

    if audioData != nil {
        if err := os.WriteFile("output.mp3", audioData, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

## สร้างเพลงจากรูปภาพ

Lyria 3.5 รองรับอินพุตแบบมัลติโมดัล คุณสามารถระบุรูปภาพได้สูงสุด **10 ภาพ**
พร้อมกับพรอมต์ข้อความในรายการ `input` และโมเดลจะแต่งเพลง
โดยได้แรงบันดาลใจจากเนื้อหาภาพ

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3.5",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### JavaScript

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3.5",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("desert_sunset.jpg"));
String imageB64 = Base64.getEncoder().encodeToString(imageBytes);

Content textContent =
    TextContent.builder()
        .text("An atmospheric ambient track inspired by the mood and colors in this image.")
        .build();
Content imageContent =
    ImageContent.builder()
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .data(imageB64)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction response =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    imageBytes, err := os.ReadFile("desert_sunset.jpg")
    if err != nil {
        log.Fatal(err)
    }
    imageB64 := base64.StdEncoding.EncodeToString(imageBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        }),
        interactions.NewContent(interactions.ImageContent{
            MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
            Data:     genai.Ptr(imageB64),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3.5",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## ระบุเนื้อเพลงที่กำหนดเอง

คุณสามารถเขียนเนื้อเพลงของคุณเองและใส่ไว้ในพรอมต์ได้ ใช้แท็กส่วน
เช่น `[Verse]`, `[Chorus]` และ `[Bridge]` เพื่อช่วยให้โมเดลเข้าใจ
โครงสร้างเพลง

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

interaction = client.interactions.create(
    model="lyria-3.5",
    input=prompt,
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

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

String prompt =
    "Create a dreamy indie pop song with the following lyrics:\n\n"
        + "[Verse 1]\n"
        + "Walking through the neon glow,\n"
        + "city lights reflect below,\n"
        + "every shadow tells a story,\n"
        + "every corner, fading glory.\n\n"
        + "[Chorus]\n"
        + "We are the echoes in the night,\n"
        + "burning brighter than the light,\n"
        + "hold on tight, don't let me go,\n"
        + "we are the echoes down below.\n\n"
        + "[Verse 2]\n"
        + "Footsteps lost on empty streets,\n"
        + "rhythms sync to heartbeats,\n"
        + "whispers carried by the breeze,\n"
        + "dancing through the autumn leaves.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of(prompt))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Create a dreamy indie pop song with the following lyrics:\n\n" +
        "[Verse 1]\n" +
        "Walking through the neon glow,\n" +
        "city lights reflect below,\n" +
        "every shadow tells a story,\n" +
        "every corner, fading glory.\n\n" +
        "[Chorus]\n" +
        "We are the echoes in the night,\n" +
        "burning brighter than the light,\n" +
        "hold on tight, don't let me go,\n" +
        "we are the echoes down below.\n\n" +
        "[Verse 2]\n" +
        "Footsteps lost on empty streets,\n" +
        "rhythms sync to heartbeats,\n" +
        "whispers carried by the breeze,\n" +
        "dancing through the autumn leaves."

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(prompt),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## ควบคุมเวลาและโครงสร้าง

คุณสามารถระบุสิ่งที่เกิดขึ้นในท่อนเพลงที่ต้องการได้อย่างแม่นยำโดยใช้
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

interaction = client.interactions.create(
    model="lyria-3.5",
    input=prompt,
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

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

String prompt =
    "[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled vinyl crackle.\n"
        + "[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody and gentle vocals singing about a rainy morning.\n"
        + "[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring synth leads. The lyrics are hopeful and uplifting.\n"
        + "[0:50 - 1:00] Outro: Fade out with the piano melody alone.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of(prompt))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := "[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled vinyl crackle.\n" +
        "[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody and gentle vocals singing about a rainy morning.\n" +
        "[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring synth leads. The lyrics are hopeful and uplifting.\n" +
        "[0:50 - 1:00] Outro: Fade out with the piano melody alone."

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(prompt),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## สร้างแทร็กบรรเลง

สำหรับเพลงเบื้องหลัง ซาวด์แทร็กเกม หรือกรณีการใช้งานใดๆ ที่ไม่จำเป็นต้องมีเสียงร้อง
คุณสามารถแจ้งให้โมเดลสร้างแทร็กที่มีเฉพาะดนตรีได้โดยทำดังนี้

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-clip-preview"))
        .input(
            InteractionsInput.of(
                "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3-clip-preview"),
            Input: interactions.NewInteractionsInput(
                "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## สร้างเพลงในภาษาต่างๆ

Lyria 3.5 จะสร้างเนื้อเพลงในภาษาของพรอมต์ หากต้องการสร้างเพลง
ที่มีเนื้อร้องเป็นภาษาฝรั่งเศส ให้เขียนพรอมต์เป็นภาษาฝรั่งเศส โมเดลจะปรับรูปแบบการร้อง
และการออกเสียงให้ตรงกับภาษา

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(
            InteractionsInput.of(
                "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("lyria-3.5"),
            Input: interactions.NewInteractionsInput(
                "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## ความสามารถของโมเดล

Lyria 3.5 จะวิเคราะห์กระบวนการพรอมต์ของคุณ โดยโมเดลจะพิจารณาโครงสร้างดนตรี (ท่อนนำ ท่อนร้อง คอรัส บริดจ์ ฯลฯ)
ตามพรอมต์ของคุณ
ซึ่งจะเกิดขึ้นก่อนที่จะสร้างเสียง และช่วยให้มั่นใจได้ถึงความสอดคล้องเชิงโครงสร้างและความเป็นดนตรี

## คำแนะนำในการเขียนพรอมต์

ดูวิธีสร้างพรอมต์ที่มีประสิทธิภาพสำหรับแนวเพลง เครื่องดนตรี โครงสร้างเพลง เนื้อเพลงที่กำหนดเอง และสไตล์การร้องได้ที่[คู่มือการใช้พรอมต์ของ Lyria](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=th)

## แนวทางปฏิบัติแนะนำ

- **ทำซ้ำด้วยคลิปก่อน** ใช้`lyria-3-clip-preview`โมเดลที่เร็วกว่าเพื่อ
  ทดลองใช้พรอมต์ก่อนที่จะสร้างวิดีโอแบบเต็มด้วย
  `lyria-3.5`
- **ใช้คำที่เฉพาะเจาะจง** พรอมต์ที่คลุมเครือจะให้ผลลัพธ์ทั่วไป ระบุเครื่องดนตรี
  BPM, คีย์, อารมณ์ และโครงสร้างเพื่อให้ได้ผลลัพธ์ที่ดีที่สุด
- **เลือกภาษาที่ต้องการ** ป้อนพรอมต์ในภาษาที่คุณต้องการให้เนื้อเพลงเป็น
- **ใช้แท็กส่วน** แท็ก `[Verse]`, `[Chorus]`, `[Bridge]` ช่วยให้โมเดลมีโครงสร้างที่ชัดเจน
  ให้ทำตาม
- **แยกเนื้อเพลงออกจากคำสั่ง** เมื่อระบุเนื้อเพลงที่กำหนดเอง ให้แยกเนื้อเพลงออกจากคำสั่งเกี่ยวกับทิศทางดนตรีอย่างชัดเจน

## ข้อจำกัด

- **ความปลอดภัย**: ตัวกรองความปลอดภัยจะตรวจสอบพรอมต์ทั้งหมด ระบบจะบล็อกพรอมต์ที่ทริกเกอร์
  ตัวกรอง ซึ่งรวมถึงพรอมต์ที่ขอเสียงของศิลปิน
  ที่เฉพาะเจาะจงหรือการสร้างเนื้อเพลงที่มีลิขสิทธิ์
- **การใส่ลายน้ำ**: เสียงที่สร้างขึ้นทั้งหมดจะมี[ลายน้ำเสียง SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=th) สำหรับการระบุตัวตน ลายน้ำนี้จะมองไม่เห็นด้วยตาเปล่าและ
  ไม่มีผลต่อประสบการณ์การฟัง
- **การตัดต่อแบบต่อเนื่อง**: การสร้างเพลงเป็นกระบวนการแบบรอบเดียว
  Lyria 3.5 เวอร์ชันปัจจุบันไม่รองรับการแก้ไขซ้ำๆ หรือการปรับแต่งคลิปที่สร้างขึ้นผ่านพรอมต์หลายรายการ
- **ความยาว**: โมเดลคลิปจะสร้างคลิปความยาว 30 วินาทีเสมอ โมเดล Pro
  สร้างเพลงที่มีความยาว 2-3 นาที โดยระยะเวลาที่แน่นอนจะ
  ขึ้นอยู่กับพรอมต์ของคุณ
- **ความแน่นอน**: ผลลัพธ์อาจแตกต่างกันไปในแต่ละการเรียกใช้ แม้จะใช้พรอมต์เดียวกันก็ตาม

## ขั้นตอนถัดไป

- ดู[ราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th)สำหรับโมเดล Lyria 3.5
- ลอง[สร้างเพลงแบบเรียลไทม์และสตรีมมิง](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=th)ด้วย
  Lyria RealTime
- สร้างการสนทนาแบบหลายผู้พูดด้วย[โมเดล TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)
- ดูวิธีสร้าง[รูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th)หรือ
  [วิดีโอ](https://ai.google.dev/gemini-api/docs/video?hl=th)
- ดูวิธีที่ Gemini [เข้าใจไฟล์เสียง](https://ai.google.dev/gemini-api/docs/audio?hl=th)
- สนทนากับ Gemini แบบเรียลไทม์โดยใช้
  [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-01 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-01 UTC"],[],[]]
