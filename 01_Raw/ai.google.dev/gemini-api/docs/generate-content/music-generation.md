---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/music-generation?hl=zh-CN
fetched_at: 2026-06-29T05:28:39.965507+00:00
title: "\u4f7f\u7528 Lyria 3 \u751f\u6210\u97f3\u4e50 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 Lyria 3 生成音乐

Lyria 3 是 Google 的音乐创作模型系列，可通过 Gemini API 使用。借助 Lyria 3，您可以根据文本提示或图片生成高质量的 44.1 kHz 立体声音频。这些模型可提供结构连贯的音乐，包括人声、同步歌词及完整的器乐编排。

Lyria 3 系列包含两款模型：

| 模型 | 模型 ID | 适用场景 | 时长 | 输出 |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | 短片、循环播放的短片、预览 | 30 秒 | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | 包含主歌、副歌和桥段的完整歌曲 | 几分钟（可通过提示控制） | MP3 |

这两种模型均可通过标准 `generateContent` 方法和新的 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 使用，支持多模态输入（文本和图片），并生成 **44.1 kHz 高保真立体声**音频。

## 生成音乐片段

Lyria 3 Clip 模型始终生成 **30 秒**的片段。如需生成剪辑，请使用文本提示调用 `generateContent` 方法。响应始终包含生成的歌词和歌曲结构以及音频。

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

## 生成完整歌曲

使用 `lyria-3-pro-preview` 模型生成时长几分钟的完整歌曲。Pro 模型能理解音乐结构，并能创作出具有鲜明主歌、副歌和桥段的乐曲。您可以在提示中指定时长（例如“创作一首 2 分钟的歌曲”），也可以使用[时间戳](#timing)来定义结构，从而影响时长。

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

## 选择输出格式

默认情况下，Lyria 3 模型会生成 **MP3** 格式的音频。对于 Lyria 3 Pro，您还可以通过在 `generationConfig` 中设置 `response_format` 来请求 **WAV** 格式的输出。

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

## 解析响应

Lyria 3 的响应包含多个部分。文本部分包含生成的歌词或歌曲结构的 JSON 说明。带有 `inline_data` 的部分包含音频字节。

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

## 根据图片生成音乐

Lyria 3 支持多模态输入，您可以提供最多 **10 张图片**以及文本提示，模型将根据视觉内容创作音乐。

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

## 提供自定义歌词

您可以自行撰写歌词，并将其添加到提示中。使用 `[Verse]`、`[Chorus]` 和 `[Bridge]` 等部分标记来帮助模型了解歌曲结构：

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

## 控制时间和结构

您可以使用时间戳来精确指定歌曲中特定时刻发生的情况。这有助于控制乐器何时进入、歌词何时出现以及歌曲的进展方式：

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

## 生成纯音乐轨道

对于背景音乐、游戏配乐或不需要人声的任何使用场景，您可以提示模型生成纯乐器曲目：

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

## 生成不同语言的音乐

Lyria 3 会根据您提示的语言生成歌词。如需生成带有法语歌词的歌曲，请使用法语撰写提示。模型会调整其发音风格和发音，以匹配相应语言。

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

## 模型智能

Lyria 3 会分析您的提示流程，其中模型会根据您的提示推断音乐结构（前奏、主歌、副歌、桥段等）。此过程在生成音频之前进行，可确保结构连贯性和音乐性。

## Interactions API

您可以将 Lyria 3 模型与 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 搭配使用；该 API 是与 Gemini 模型和代理交互的统一接口。它可简化复杂多模态用例的状态管理和长时间运行的任务。

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

## 提示指南

您的提示可以很简单，例如“一首关于可爱猫咪躲避水坑的民谣，女声演唱，有雨声”，也可以是详细且结构化的提示，例如：

> 一首 1980 年代风格的合成器流行乐，节奏强劲、合成器音色梦幻，副歌朗朗上口、气势恢宏。这首歌应具有复古未来主义风格，让人想起 80 年代的经典流行金曲，同时又具有现代的制作水准。节奏应欢快且适合跳舞，约为 120 BPM，具有清晰的主歌-副歌结构和令人难忘的器乐钩子。歌词讲述的是准备参加派对时的心情。

无论是简单提示还是复杂提示，都可以生成出色的输出结果。我们建议您尝试这些技巧，找到最适合自己的方法。

### 流派

在提示中首先指定您想要的音乐流派，例如嘻哈、摇滚和说唱。您可以指定多种流派：

- 金属乐和说唱的融合
- 死亡金属与歌剧的结合
- 一首包含电子嗡鸣元素的古典乐曲
- 将现代电子舞曲 (EDM) 与欧陆流行音乐相融合

您还可以添加纪元：

- 90 年代初的嘻哈音乐
- 60 年代法国 ye-ye 流行乐
- 80 年代的电子实验音乐
- 2000 年代主流流行音乐

如果您提示模型生成特定风格或区域变体，例如“柏林 techno”或“湾区 hyphy”，模型会尝试捕捉这些风格的精髓，但可能并不总是能准确把握。

### 乐器

默认情况下，Lyria 3 会使用您预期的乐器和工具来创作相应流派的歌曲。您无需规定具体做法。

不过，除非您要求，否则舞曲不会包含萨克斯管。因此，如果您想要一段萨克斯管独奏，需要提示：

> 一首舞曲，节奏强劲、合成器音效闪耀，副歌旋律抓耳且充满力量。中段应加入一段萨克斯独奏。

您的提示可以包含特定乐器、乐器的声音以及乐器之间的互动方式。您可以利用这种组合来营造特定的氛围或质感：

- 浑浊失真的低音与干净清脆的踩镲相互抗衡
- 温暖的模拟合成器音垫在干涩、亲密的木吉他下方逐渐增强
- 由多层模糊吉他打造的音墙，人声埋在其中，听起来很遥远

### 歌曲结构

您可以在提示中概述歌曲的进展。使用箭头或列表定义流程：

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- 以安静的钢琴前奏开始，逐渐过渡到高亢的主歌，然后突然静音，最后进入高潮。

您还可以指定这些部分之间的能级变化方式：

- 在副歌前段营造紧张感，然后在副歌开始前突然静音，让副歌的爆发更具震撼力
- 整首歌曲逐渐达到高潮，每次添加一种乐器，直到形成混乱的音墙
- 过渡段后突然停止，然后是无伴奏合唱

您还可以提示确切的时间，让设备在指定时间执行操作：

- 在 12 秒时达到高潮
- 每 2 秒钟就有人说“什么”
- 合唱部分从 22 秒开始

### 歌词

默认情况下，系统会生成人声和歌词。您可以提供自己的歌词，也可以要求不提供歌词（或提供纯音乐），还可以引导歌词生成朝着您想要的方向发展。

歌词将采用您撰写提示时所用的语言。您还可以要求以其他语言显示歌词，例如“用法语写歌词”。

#### 使用您自己的歌词

如需向模型提供您自己的歌词，请在提示中添加这些歌词，并在前面加上“歌词：”前缀：

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

您可以在歌曲的各个部分添加前缀，例如 `[Intro]`、`[Verse 1]`、`[Pre-chorus]`、`[Chorus]` 和 `[Outro]` 等部分标题。

如果您希望某个字词或某行文字重复出现，例如像回声一样或由伴唱歌手唱出，您可以将其放在圆括号中，例如“Let's go (go)”。

#### 提示模型撰写歌词

如果您希望 Lyria 3 为您创作歌词，最好在提示中包含有关歌词内容的详细信息。否则，模型需要从音乐提示中推断主题，而这可能不是您想要的。

> 歌词讲述的是失恋和心碎的痛苦。这位歌手回忆起过去的一段感情，以及随之涌现的记忆。

如果您想要重复的合唱，最好在提示中明确提出：

> 歌词讲述的是失恋和心碎的痛苦。这位歌手回忆起过去的一段感情，以及随之涌现的记忆。强劲的合唱部分着重表达了摆脱痛苦、继续前行的决心。

Lyria 3 会自动将歌词结构引导至您请求的音乐类型，但您也可以在提示中再次强调这一点。例如：

> 一首反复播放同一段充满活力的乐句的 EDM 音乐。

您还可以提示添加不属于歌词的音效，例如：

- 电影中的一段重复采样，在整首歌曲中不断重复“我简直不敢相信！”
- 这是一首高能的 Techno 音乐，在 drop 之前，所有声音都停止了，然后一个小声音说“我不知道我在这里做什么”，然后音乐 drop。
- 这首歌以一段关于 90 年代电影比现在更好的对话开场。然后，曲目会过渡到一首流行歌曲。

### 人声

您可以提示系统以何种方式呈现歌词。为获得最佳效果，请指定详细的歌手个人资料，包括性别、音色和音域。

- **女高音**：音色清澈透亮，音质灵活高亢。能够发出空灵、气声感十足的哨音高音。
- **女低音**：低音浑厚、温暖、沙哑。烟嗓，略带气泡音，深情而富有共鸣。
- **男高音**：明亮、穿透力强、充满活力。音色年轻，略带鼻音，高音穿透力强，能穿透混音。
- **男中音**：深沉、醇厚、丝滑。共鸣胸腔声音，以舒缓的低吟方式传递。
- **饱经风霜的摇滚歌手（男）**：音色沙哑粗犷，带有砾石般的音质，让人联想到 90 年代的垃圾摇滚。情感强度过高，声音紧张。

### 其他提示参数

您还可以添加以下参数来进一步优化提示：

- **调/音阶**：指定音乐调（例如“G 大调”“D 小调”）。
- **曲调和氛围**：使用描述性的形容词（例如“怀旧”“激进”“空灵”“梦幻”）。
- **时长**：Clip 模型始终生成 30 秒的片段。对于 Pro 版，请在提示中指定所需的时长（例如“创作一首 2 分钟的歌曲”），或使用时间戳来控制时长。

### 示例提示

以下是一些有效提示的示例：

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## 最佳做法

- **先使用 Clip 进行迭代。**使用速度更快的 `lyria-3-clip-preview` 模型来测试提示，然后再使用 `lyria-3-pro-preview` 生成完整内容。
- **内容要具体。**模糊的提示会产生一般性的结果。提及乐器、BPM、调、基调和结构，以获得最佳输出。
- **使用部分标记。**`[Verse]`、`[Chorus]`、`[Bridge]` 标记为模型提供了清晰的结构，以便模型遵循。
- **将歌词与说明分开。**提供自定义歌词时，请务必将其与音乐指导说明分开。

## 限制

- **安全性**：所有提示都会经过安全过滤器的检查。触发过滤条件的提示将被屏蔽。这包括要求使用特定音乐人声音或生成受版权保护的歌词的提示。
- **水印**：所有生成的音频都包含用于识别的 [SynthID 音频水印](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=zh-cn)。这种水印人耳无法察觉，不会影响聆听体验。
- **多轮编辑**：音乐创作是一个单轮过程。在当前版本的 Lyria 3 中，不支持通过多个提示迭代编辑或优化生成的剪辑。
- **时长**：Clip 模型始终生成 30 秒的片段。Pro 模型生成的歌曲时长为几分钟；确切时长会受到提示的影响。
- **确定性**：即使使用相同的提示，不同调用之间的结果也可能会有所不同。

## 后续步骤

- 查看 Lyria 3 模型的[价格](https://ai.google.dev/gemini-api/docs/generate-content/pricing?hl=zh-cn)，
- 使用 Lyria RealTime 体验[实时流式音乐创作](https://ai.google.dev/gemini-api/docs/generate-content/realtime-music-generation?hl=zh-cn)，
- 使用 [TTS 模型](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=zh-cn)生成多说话人对话，
- 了解如何生成[图片](https://ai.google.dev/gemini-api/docs/generate-content/image-generation?hl=zh-cn)或[视频](https://ai.google.dev/gemini-api/docs/generate-content/video?hl=zh-cn)，
- 了解 Gemini 如何[理解音频文件](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=zh-cn)，
- 使用 [Live API](https://ai.google.dev/gemini-api/docs/generate-content/live?hl=zh-cn) 与 Gemini 进行实时对话。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-23。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-23。"],[],[]]
