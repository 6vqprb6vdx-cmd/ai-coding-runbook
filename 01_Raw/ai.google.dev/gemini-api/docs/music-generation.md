---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=hi
fetched_at: 2026-05-11T12:32:37.600776+00:00
title: "Lyria 3 \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u092e\u094d\u092f\u0942\u091c\u093c\u093f\u0915 \u091c\u0928\u0930\u0947\u091f \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Lyria 3 की मदद से म्यूज़िक जनरेट करना

Lyria 3, संगीत जनरेट करने वाले Google के मॉडल का परिवार है. यह Gemini API के ज़रिए उपलब्ध है. Lyria 3 की मदद से, टेक्स्ट प्रॉम्प्ट या इमेज से अच्छी क्वालिटी वाला 44.1 kHz स्टीरियो ऑडियो जनरेट किया जा सकता है. ये मॉडल, स्ट्रक्चरल कोहेरेंस देते हैं. इनमें वोकल, समय के हिसाब से गाने के बोल, और पूरा इंस्ट्रुमेंटल अरेंजमेंट शामिल है.

Lyria 3 फ़ैमिली में दो मॉडल शामिल हैं:

| मॉडल | मॉडल आईडी | इन स्थितियों में बेहतर है | कुल समय | आउटपुट |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | छोटी क्लिप, लूप, झलक | 30 सेकंड | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | पूरे गाने, जिनमें वर्स, कोरस, और ब्रिज शामिल हों | कुछ मिनट (प्रॉम्प्ट के ज़रिए कंट्रोल किया जा सकता है) | MP3 |

दोनों मॉडल का इस्तेमाल, स्टैंडर्ड `generateContent` तरीके और नए [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=hi) का इस्तेमाल करके किया जा सकता है. ये मल्टीमॉडल इनपुट (टेक्स्ट और इमेज) के साथ काम करते हैं और **44.1 kHz हाई-फ़िडेलिटी स्टीरियो** ऑडियो जनरेट करते हैं.

## म्यूज़िक क्लिप जनरेट करना

Lyria 3 Clip मॉडल हमेशा **30 सेकंड** की क्लिप जनरेट करता है. क्लिप जनरेट करने के लिए, टेक्स्ट प्रॉम्प्ट के साथ `generateContent` तरीके को कॉल करें. जवाब में हमेशा ऑडियो के साथ-साथ, जनरेट किए गए बोल और गाने का स्ट्रक्चर शामिल होता है.

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

### ऐप पर जाएं

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

## पूरा गाना जनरेट करना

`lyria-3-pro-preview` मॉडल का इस्तेमाल करके, पूरे गाने जनरेट करें. इनकी अवधि कुछ मिनट होती है. Pro मॉडल, संगीत की संरचना को समझता है. साथ ही, अलग-अलग वर्स, कोरस, और ब्रिज के साथ कंपोज़िशन बना सकता है. अपने प्रॉम्प्ट में अवधि तय करके (जैसे, "दो मिनट का गाना बनाओ") या स्ट्रक्चर तय करने के लिए [टाइमस्टैंप](#timing) का इस्तेमाल करके, अवधि पर असर डाला जा सकता है.

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

### ऐप पर जाएं

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

## आउटपुट फ़ॉर्मैट चुनें

डिफ़ॉल्ट रूप से, Lyria 3 मॉडल **MP3** फ़ॉर्मैट में ऑडियो जनरेट करते हैं. Lyria 3 Pro के लिए, `generationConfig` में `response_format` सेट करके, आउटपुट को **WAV** फ़ॉर्मैट में भी पाने का अनुरोध किया जा सकता है.

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

### ऐप पर जाएं

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

## जवाब को पार्स करना

Lyria 3 से मिले जवाब में कई हिस्से होते हैं. टेक्स्ट वाले हिस्सों में, जनरेट किए गए बोल या गाने के स्ट्रक्चर की JSON फ़ाइल होती है. `inline_data` वाले हिस्सों में ऑडियो बाइट शामिल होते हैं.

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

### ऐप पर जाएं

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

## इमेज से संगीत जनरेट करना

Lyria 3 में, टेक्स्ट, इमेज वग़ैरह को प्रोसेस करने वाले मोडल के इनपुट इस्तेमाल किए जा सकते हैं. टेक्स्ट प्रॉम्प्ट के साथ-साथ, **10 इमेज** तक दी जा सकती हैं. इसके बाद, मॉडल विज़ुअल कॉन्टेंट से मिलता-जुलता संगीत तैयार करेगा.

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

### ऐप पर जाएं

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

## गाने के बोल अपने हिसाब से उपलब्ध कराना

आपके पास अपने बोल लिखने और उन्हें प्रॉम्प्ट में शामिल करने का विकल्प होता है. सेक्शन टैग, जैसे कि `[Verse]`, `[Chorus]`, और `[Bridge]` का इस्तेमाल करें, ताकि मॉडल को गाने के स्ट्रक्चर को समझने में मदद मिल सके:

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

### ऐप पर जाएं

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

## समय और स्ट्रक्चर को कंट्रोल करना

टाइमस्टैंप का इस्तेमाल करके, यह बताया जा सकता है कि गाने के किसी खास हिस्से में क्या हो रहा है. इससे यह कंट्रोल किया जा सकता है कि इंस्ट्रुमेंट कब शुरू हों, गाने के बोल कब दिखें, और गाना कैसे आगे बढ़े:

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

### ऐप पर जाएं

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

## इंस्ट्रुमेंटल ट्रैक जनरेट करना

बैकग्राउंड संगीत, गेम के साउंडट्रैक या ऐसे किसी भी इस्तेमाल के उदाहरण के लिए जहां वोकल की ज़रूरत नहीं है, मॉडल को सिर्फ़ इंस्ट्रुमेंटल ट्रैक बनाने के लिए कहा जा सकता है:

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

### ऐप पर जाएं

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

## अलग-अलग भाषाओं में संगीत जनरेट करना

Lyria 3, प्रॉम्प्ट में इस्तेमाल की गई भाषा में गाने के बोल जनरेट करता है. फ़्रेंच भाषा में बोल वाला गाना जनरेट करने के लिए, प्रॉम्प्ट को फ़्रेंच भाषा में लिखें. यह मॉडल, भाषा के हिसाब से अपनी आवाज़ और उच्चारण को बदलता है.

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

### ऐप पर जाएं

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

## मॉडल इंटेलिजेंस

Lyria 3, आपके प्रॉम्प्ट का विश्लेषण करता है. इसमें मॉडल, आपके प्रॉम्प्ट के आधार पर म्यूज़िकल स्ट्रक्चर (इंट्रो, वर्स, कोरस, ब्रिज वगैरह) के बारे में बताता है.
यह प्रोसेस, ऑडियो जनरेट होने से पहले होती है. इससे यह पक्का किया जाता है कि ऑडियो में स्ट्रक्चरल कोहेरेंस और म्यूज़िकैलिटी हो.

## Interactions API

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=hi) के साथ Lyria 3 मॉडल इस्तेमाल किए जा सकते हैं.
यह Gemini मॉडल और एजेंटों के साथ इंटरैक्ट करने के लिए एक यूनीफ़ाइड इंटरफ़ेस है. यह जटिल मल्टीमॉडल इस्तेमाल के उदाहरणों के लिए, स्टेट मैनेजमेंट और लंबे समय तक चलने वाले टास्क को आसान बनाता है.

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

## प्रॉम्प्ट से जुड़ी गाइड

आपका प्रॉम्प्ट इतना आसान हो सकता है, जैसे कि "प्यारी बिल्लियों के बारे में एक लोक गीत, जिसमें वे गड्ढों से बच रही हैं, महिला की आवाज़ में गाया गया हो और बारिश की आवाज़ सुनाई दे रही हो". इसके अलावा, यह ज़्यादा जानकारी वाला और स्ट्रक्चर्ड भी हो सकता है. जैसे:

> यह 1980 के दशक के सिंथ-पॉप स्टाइल का ट्रैक है. इसमें दमदार बीट, चमकते हुए सिंथेसाइज़र, और एक आकर्षक, ऐंथम जैसा कोरस है. गाने में रेट्रो-फ़्यूचरिस्टिक फ़ील होना चाहिए. साथ ही, इसमें 80 के दशक के क्लासिक पॉप हिट गानों की झलक होनी चाहिए. हालांकि, इसे मॉडर्न प्रोडक्शन के साथ बनाया जाना चाहिए. टेंपो तेज़ और डांस करने लायक होना चाहिए. बीपीएम 120 के आस-पास होना चाहिए. वर्स-कोरस स्ट्रक्चर साफ़ तौर पर समझ में आना चाहिए. साथ ही, इंस्ट्रुमेंटल हुक यादगार होना चाहिए. गाने के बोल में, पार्टी के लिए तैयार होने के बारे में बताया गया है.

आसान और मुश्किल, दोनों तरह के प्रॉम्प्ट से आपको अच्छे नतीजे मिल सकते हैं. हमारा सुझाव है कि आप इन सलाहों को आज़माकर देखें, ताकि आपको पता चल सके कि आपके लिए सबसे सही तरीका कौनसा है.

### शैली

अपने प्रॉम्प्ट की शुरुआत, अपनी पसंद के संगीत की शैली से करें. जैसे, हिप हॉप, रॉक, और रैप. अलग-अलग शैलियों को चुना जा सकता है:

- मेटल और रैप का फ़्यूज़न
- डेथ मेटल और ओपेरा का कॉम्बिनेशन
- इलेक्ट्रॉनिक ड्रोन वाले एलिमेंट के साथ क्लासिकल पीस
- यूरोपॉप के साथ मॉडर्न इलेक्ट्रॉनिक डांस म्यूज़िक (ईडीएम)

इसमें कोई युग भी शामिल किया जा सकता है:

- 90 के दशक की शुरुआत का हिप-हॉप
- 60 के दशक का फ़्रेंच ये-ये पॉप
- 80 के दशक में इलेक्ट्रॉनिक संगीत पर किए गए एक्सपेरिमेंट
- 2000 के दशक के मुख्यधारा के पॉप गाने

अगर आपने किसी खास शैली या क्षेत्र के हिसाब से संगीत बनाने के लिए प्रॉम्प्ट दिया है, जैसे कि "बर्लिन टेक्नो" या "बे एरिया हाइफ़ी", तो मॉडल उस शैली या क्षेत्र के हिसाब से संगीत बनाने की कोशिश करेगा. हालांकि, ऐसा हो सकता है कि वह हमेशा सही संगीत न बना पाए.

### इंस्ट्रुमेंट

डिफ़ॉल्ट रूप से Lyria 3, संगीत की शैली के हिसाब से इंस्ट्रुमेंट और टूल का इस्तेमाल करके गाने बनाएगा. आपको किसी भी तरह का सुझाव देने की ज़रूरत नहीं है.

हालांकि, अगर आपने सैक्सोफ़ोन का इस्तेमाल करने के लिए नहीं कहा है, तो डांस ट्रैक में सैक्सोफ़ोन का इस्तेमाल नहीं किया जाएगा. इसलिए, अगर आपको सैक्सोफ़ोन सोलो चाहिए, तो आपको यह प्रॉम्प्ट देना होगा:

> यह एक डांस ट्रैक है, जिसमें दमदार बीट, चमकते सिंथेसाइज़र, और एक आकर्षक, ऐंथम जैसा कोरस है. ब्रिज के दौरान सैक्सोफ़ोन सोलो होना चाहिए.

आपके प्रॉम्प्ट में, खास इंस्ट्रुमेंट, उनकी आवाज़, और उनके एक-दूसरे के साथ इंटरैक्ट करने का तरीका शामिल हो सकता है. इस कॉम्बिनेशन का इस्तेमाल करके, कुछ मूड या टेक्सचर बनाए जा सकते हैं:

- इस गाने में, गंदी और खराब बासलाइन को साफ़ और क्रिस्प हाई-हैट के साथ सुना जा सकता है
- सूखे और सुकून भरे अकूस्टिक गिटार के नीचे, ऐनालॉग सिंथेसाइज़र पैड की गूंज
- फ़ज़ी गिटार की कई लेयर से बनी आवाज़ की दीवार. इसमें दबी हुई, दूर से सुनाई देने वाली आवाज़ें हैं

### गाने की संरचना

अपने प्रॉम्प्ट में, किसी गाने के प्रोग्रेशन की जानकारी दी जा सकती है. फ़्लो तय करने के लिए, ऐरो या सूची का इस्तेमाल करें:

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- गाने की शुरुआत पियानो के धीमे इंट्रो से होती है. इसके बाद, वर्स में आवाज़ तेज़ हो जाती है. फिर, कुछ देर के लिए आवाज़ धीमी हो जाती है और आखिर में कोरस में आवाज़ तेज़ हो जाती है.

यह भी तय किया जा सकता है कि इन सेक्शन के बीच ऊर्जा के लेवल में किस तरह बदलाव होता है:

- प्री-कोरस में तनाव पैदा करें. इसके बाद, ज़ोरदार और धमाकेदार कोरस से पहले, संगीत को शांत कर दें
- पूरे गाने में धीरे-धीरे आवाज़ बढ़ती है. इसमें एक-एक करके इंस्ट्रुमेंट जोड़े जाते हैं. आखिर में, आवाज़ बहुत तेज़ हो जाती है
- पुल के बाद अचानक रुक जाना और फिर एकैपेला कोरस

आपके पास यह तय करने का विकल्प भी होता है कि कोई काम कब पूरा होना चाहिए:

- 12 सेकंड में ड्रॉप होने वाला प्रॉडक्ट लॉन्च बनाएं
- कोई व्यक्ति हर दो सेकंड में "क्या" कहता है
- कोरस 22 सेकंड पर शुरू होता है

### गाने के बोल

आवाज़ और गाने के बोल डिफ़ॉल्ट रूप से जनरेट होते हैं. आपके पास अपने बोल देने, बोल न लिखने (या इंस्ट्रुमेंटल ट्रैक बनाने) का अनुरोध करने या बोल जनरेट करने की प्रोसेस को अपनी पसंद के हिसाब से कंट्रोल करने का विकल्प होता है.

आपके लिखे गए प्रॉम्प्ट की भाषा में ही बोल लिखे जाएंगे. "फ़्रेंच में गाने के बोल लिखो" जैसे निर्देश देकर, किसी दूसरी भाषा में भी गाने के बोल लिखने के लिए कहा जा सकता है.

#### अपने बोल इस्तेमाल करना

मॉडल को अपने गाने के बोल देने के लिए, उन्हें प्रॉम्प्ट में "Lyrics:" प्रीफ़िक्स के साथ शामिल करें:

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

गाने के अलग-अलग हिस्सों को `[Intro]`, `[Verse 1]`, `[Pre-chorus]`, `[Chorus]`, और `[Outro]` जैसे सेक्शन के टाइटल के साथ प्रीफ़िक्स किया जा सकता है.

अगर आपको किसी शब्द या लाइन को दोहराना है, जैसे कि गूंज या बैकग्राउंड में गाने वाले लोगों की आवाज़, तो उसे ब्रैकेट में शामिल करें: "Let's go (go)".

#### मॉडल को गाने के बोल लिखने के लिए प्रॉम्प्ट करना

अगर आपको Lyria 3 से गाने के बोल लिखवाने हैं, तो बेहतर होगा कि आप अपने प्रॉम्प्ट में इस बारे में जानकारी दें कि बोल किस बारे में होंगे. ऐसा न करने पर, मॉडल को आपके संगीत के प्रॉम्प्ट से किसी विषय का अनुमान लगाना होगा. ऐसा हो सकता है कि वह विषय आपकी पसंद का न हो.

> इस गाने के बोल में, प्यार में मिली हार और दिल टूटने के दर्द के बारे में बताया गया है. गायक, अपने पुराने रिश्ते और उससे जुड़ी यादों के बारे में बता रहा है.

अगर आपको गाने में एक ही कोरस को बार-बार दोहराना है, तो अपने प्रॉम्प्ट में इसके बारे में बताएं:

> इस गाने के बोल में, प्यार में मिली हार और दिल टूटने के दर्द के बारे में बताया गया है. गायक, अपने पुराने रिश्ते और उससे जुड़ी यादों के बारे में बता रहा है. कोरस में, दर्द से उबरने और आगे बढ़ने पर ज़ोर दिया गया है.

Lyria 3, आपके अनुरोध के हिसाब से, बोल के स्ट्रक्चर को अपने-आप सेट कर देगा. हालांकि, प्रॉम्प्ट में भी इसे फिर से सेट किया जा सकता है. उदाहरण के लिए:

> एक ऐसा ईडीएम ट्रैक जिसमें एक ही जोशीले वाक्यांश को बार-बार दोहराया जाता है.

ऐसे वोकल इफ़ेक्ट के लिए भी प्रॉम्प्ट दिया जा सकता है जो पूरी तरह से बोल नहीं हैं. उदाहरण के लिए:

- गाने में किसी फ़िल्म का एक सैंपल बार-बार इस्तेमाल किया गया है. इसमें "मुझे यकीन नहीं हो रहा!" शब्द का इस्तेमाल किया गया है
- यह एक हाई एनर्जी टेक्नो ट्रैक है. ड्रॉप से ठीक पहले, आवाज़ पूरी तरह से बंद हो जाती है और एक छोटी सी आवाज़ कहती है "मुझे नहीं पता कि मैं यहां क्या कर रहा हूं". इसके बाद, संगीत शुरू हो जाता है.
- इस ट्रैक की शुरुआत में, 90 के दशक की फ़िल्मों को आज की फ़िल्मों से बेहतर बताया गया है. इसके बाद, ट्रैक एक पॉप गाने में बदल जाता है.

### बोल

आपके पास यह बताने का विकल्प होता है कि आपको गाने के बोल किस तरह से चाहिए. बेहतर नतीजों के लिए, गायक की प्रोफ़ाइल के बारे में पूरी जानकारी दें. जैसे, जेंडर, आवाज़ का टेक्स्चर, और वोकल रेंज.

- **सोप्रानो**: साफ़, क्रिस्टल जैसी आवाज़, जो तेज़ी से ऊपर की ओर बढ़ती है. यह हवादार और सांस लेने में आसान बनावट के साथ, सीटी जैसी ऊंची आवाज़ में गाने में सक्षम है.
- **मादा ऑल्टो**: रिच, वॉर्म, और हस्की लोअर रेंज. धुएं जैसी आवाज़, जिसमें वोकल फ़्राई का हल्का सा टच है. यह आवाज़ दिल को छू लेने वाली और गूंजने वाली है.
- **पुरुष टेनर**: तेज़, तीखा, और ऊर्जा से भरपूर. युवाओं जैसी आवाज़, जिसमें थोड़ी सी नाक से निकलने वाली ध्वनि है. यह आवाज़, मिक्स में तेज़ बेल्टिंग पावर के साथ सुनाई देती है.
- **पुरुष की बैरिटोन आवाज़**: गहरी, चॉकलेट जैसी, और मखमली. आरामदायक और मधुर आवाज़ में गाना.
- **वेदर रॉकर (पुरुष)**: यह आवाज़, 90 के दशक के ग्रंज संगीत की याद दिलाती है. इसमें खुरदुरापन और बनावट है. साथ ही, यह थोड़ी कर्कश है. ज़्यादा भावनाएं ज़ाहिर करने के लिए, आवाज़ की ऊपरी रेंज का इस्तेमाल किया गया है.

### प्रॉम्प्ट के अन्य पैरामीटर

अपने प्रॉम्प्ट को और बेहतर बनाने के लिए, इन पैरामीटर को भी शामिल किया जा सकता है:

- **की/स्केल**: म्यूज़िकल की के बारे में बताएं. जैसे, "जी मेजर में", "डी माइनर".
- **मूड और माहौल**: जानकारी देने वाले विशेषणों का इस्तेमाल करें. जैसे, "यादें ताज़ा करने वाला", "आक्रामक", "अलौकिक", "सपनों जैसा".
- **अवधि**: क्लिप मॉडल हमेशा 30 सेकंड की क्लिप जनरेट करता है. Pro मॉडल के लिए, अपने प्रॉम्प्ट में मनचाही अवधि बताएं.उदाहरण के लिए, "दो मिनट का गाना बनाओ". इसके अलावा, अवधि को कंट्रोल करने के लिए टाइमस्टैंप का इस्तेमाल करें.

### प्रॉम्प्ट के उदाहरण

यहां कुछ असरदार प्रॉम्प्ट के उदाहरण दिए गए हैं:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## सबसे सही तरीके

- **सबसे पहले, Clip की मदद से दोहराएं.** `lyria-3-pro-preview` की मदद से पूरा कॉन्टेंट जनरेट करने से पहले, प्रॉम्प्ट आज़माने के लिए `lyria-3-clip-preview` मॉडल का इस्तेमाल करें.
- **सटीक जानकारी दें.** अस्पष्ट प्रॉम्प्ट से सामान्य नतीजे मिलते हैं. बेहतरीन आउटपुट पाने के लिए, इंस्ट्रूमेंट, बीपीएम, की, मूड, और स्ट्रक्चर के बारे में जानकारी दें.
- **सेक्शन टैग इस्तेमाल करें.** `[Verse]`, `[Chorus]`, `[Bridge]` टैग की मदद से, मॉडल को जवाब देने के लिए एक साफ़ स्ट्रक्चर मिलता है.
- **बोल को निर्देशों से अलग करें.** अपनी पसंद के मुताबिक़ बोल देते समय, उन्हें संगीत से जुड़े निर्देशों से अलग रखें.

## सीमाएं

- **सुरक्षा**: सभी प्रॉम्प्ट की जांच सुरक्षा फ़िल्टर करते हैं. ऐसे प्रॉम्प्ट ब्लॉक कर दिए जाएंगे जिनसे फ़िल्टर ट्रिगर होते हैं. इसमें ऐसे प्रॉम्प्ट शामिल हैं जिनमें किसी खास कलाकार की आवाज़ में गाने बनाने या कॉपीराइट वाले बोल जनरेट करने का अनुरोध किया गया हो.
- **वॉटरमार्क लगाना**: जनरेट किए गए सभी ऑडियो में, पहचान के लिए [SynthID ऑडियो वॉटरमार्क](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=hi) शामिल होता है. यह वॉटरमार्क लोगों को सुनाई नहीं देता. साथ ही, इससे सुनने के अनुभव पर कोई असर नहीं पड़ता.
- **एक से ज़्यादा बार बदलाव करना**: संगीत जनरेट करने की प्रोसेस एक बार में पूरी हो जाती है.
  Lyria 3 के मौजूदा वर्शन में, जनरेट की गई क्लिप में कई बार बदलाव करने या उसे बेहतर बनाने के लिए, कई प्रॉम्प्ट इस्तेमाल नहीं किए जा सकते.
- **अवधि**: क्लिप मॉडल हमेशा 30 सेकंड की क्लिप जनरेट करता है. Pro मॉडल, कुछ मिनट की अवधि वाले गाने जनरेट करता है. हालांकि, प्रॉम्प्ट में अवधि के बारे में जानकारी देकर, गाने की अवधि को बदला जा सकता है.
- **निश्चितता**: एक ही प्रॉम्प्ट के लिए, कॉल के हिसाब से नतीजे अलग-अलग हो सकते हैं.

## आगे क्या करना है

- Lyria 3 मॉडल के लिए [कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) देखें,
- Lyria RealTime की मदद से, [रीयल टाइम में म्यूज़िक जनरेट करने](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=hi) की सुविधा आज़माएं,
- [टीटीएस मॉडल](https://ai.google.dev/gemini-api/docs/audio-generation?hl=hi) की मदद से, एक से ज़्यादा स्पीकर वाली बातचीत जनरेट करें,
- [इमेज](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi) या [वीडियो](https://ai.google.dev/gemini-api/docs/video?hl=hi) जनरेट करने का तरीका जानें,
- जानें कि Gemini [ऑडियो फ़ाइलों को कैसे समझ सकता है](https://ai.google.dev/gemini-api/docs/audio?hl=hi),
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi) का इस्तेमाल करके, Gemini के साथ रीयल-टाइम में बातचीत करें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-07 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-07 (UTC) को अपडेट किया गया."],[],[]]
