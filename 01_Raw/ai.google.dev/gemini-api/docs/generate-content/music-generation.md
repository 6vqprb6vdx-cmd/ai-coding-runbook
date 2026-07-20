---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/music-generation?hl=es-419
fetched_at: 2026-07-20T04:37:39.557813+00:00
title: "Genera m\u00fasica con Lyria 3 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Genera música con Lyria 3

Lyria 3 es la familia de modelos de generación de música de Google, disponible a través de la API de Gemini. Con Lyria 3, puedes generar audio estéreo de alta calidad a 44.1 kHz a partir de instrucciones de texto o imágenes. Estos modelos ofrecen coherencia estructural, incluidas las voces, las letras sincronizadas y los arreglos instrumentales completos.

La familia Lyria 3 incluye dos modelos:

| Modelo | ID de modelo | Ideal para | Duración | Salida |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Clips cortos, bucles y adelantos | 30 segundos | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | Canciones completas con versos, estribillos y puentes | Unos minutos (se puede controlar con la instrucción) | MP3 |

Ambos modelos se pueden usar con el método `generateContent` estándar y la nueva [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419), admiten entradas multimodales (texto e imágenes) y producen audio **estéreo de alta fidelidad de 44.1 kHz**.

## Genera un clip musical

El modelo Clip de Lyria 3 siempre genera un clip de **30 segundos**. Para generar un clip, llama al método `generateContent` con una instrucción de texto. La respuesta siempre incluye la letra y la estructura de la canción generadas junto con el audio.

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

## Genera una canción completa

Usa el modelo `lyria-3-pro-preview` para generar canciones de larga duración que duren un par de minutos. El modelo Pro comprende la estructura musical y puede crear composiciones con versos, estribillos y puentes distintos. Puedes influir en la duración especificándola en la instrucción (p.ej., "Crea una canción de 2 minutos") o usando [marcas de tiempo](#timing) para definir la estructura.

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

## Selecciona el formato de salida

De forma predeterminada, los modelos de Lyria 3 generan audio en formato **MP3**. En el caso de Lyria 3 Pro, también puedes solicitar el resultado en formato **WAV** configurando `response_format` en `generationConfig`.

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

## Analiza la respuesta

La respuesta de Lyria 3 contiene varias partes. Las partes de texto contienen la letra generada o una descripción en formato JSON de la estructura de la canción. Las partes con `inline_data` contienen los bytes de audio.

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

## Genera música a partir de imágenes

Lyria 3 admite entradas multimodales: puedes proporcionar hasta **10 imágenes** junto con tu instrucción de texto, y el modelo compondrá música inspirada en el contenido visual.

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

## Proporciona letras personalizadas

Puedes escribir tu propia letra e incluirla en la instrucción. Usa etiquetas de sección, como `[Verse]`, `[Chorus]` y `[Bridge]`, para ayudar al modelo a comprender la estructura de la canción:

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

## Controla la sincronización y la estructura

Puedes especificar exactamente lo que sucede en momentos específicos de la canción con marcas de tiempo. Esto es útil para controlar cuándo entran los instrumentos, cuándo se entregan las letras y cómo progresa la canción:

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

## Genera pistas instrumentales

Para la música de fondo, las bandas sonoras de juegos o cualquier caso de uso en el que no se requieran voces, puedes indicarle al modelo que produzca pistas solo instrumentales:

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

## Genera música en diferentes idiomas

Lyria 3 genera letras en el idioma de tu instrucción. Para generar una canción con letra en francés, escribe la instrucción en ese idioma. El modelo adapta su estilo vocal y pronunciación para que coincidan con el idioma.

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

## Inteligencia del modelo

Lyria 3 analiza el proceso de instrucciones en el que el modelo razona a través de la estructura musical (introducción, estrofa, estribillo, puente, etc.) según tu instrucción.
Esto sucede antes de que se genere el audio y garantiza la coherencia estructural y la musicalidad.

## API de Interactions

Puedes usar los modelos de Lyria 3 con la [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419), una interfaz unificada para interactuar con modelos y agentes de Gemini. Simplifica la administración del estado y las tareas de larga duración para casos de uso multimodales complejos.

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

## Guía de instrucciones

Tu instrucción puede ser tan simple como "una canción folclórica sobre gatos tiernos que evitan los charcos, con voces femeninas y el ruido de la lluvia", o algo detallado y estructurado como lo siguiente:

> Una pista de synth-pop al estilo de los años 80 con un ritmo potente, sintetizadores brillantes y un coro pegadizo y épico. La canción debe tener un estilo retrofuturista, que recuerde a los éxitos pop clásicos de los 80, con un toque de producción moderno. El tempo debe ser alegre y bailable, alrededor de 120 BPM, con una estructura clara de verso y estribillo, y un gancho instrumental memorable. La letra trata sobre la sensación de prepararse para una fiesta.

Las instrucciones simples y complejas pueden brindarte buenos resultados. Te recomendamos que pruebes estas sugerencias para encontrar lo que mejor te funcione.

### Género

Comienza tu instrucción con el género musical que deseas, como hip hop, rock y rap. Puedes especificar una combinación de géneros:

- Una fusión de metal y rap
- Una combinación de death metal y ópera
- Una pieza clásica con elementos electrónicos de zumbido
- Música dance electrónica (EDM) moderna mezclada con Europop

También puedes incorporar una época:

- Hip hop de principios de los 90
- Pop francés ye-yé de los 60
- Experimentación electrónica de los 80
- Pop mainstream de la década del 2000

Si le pides que genere géneros personalizados o variantes regionales, como "tecno de Berlín" o "hyphy del Área de la Bahía", el modelo intentará captar esa esencia, pero es posible que no siempre lo logre.

### Instrumentos

De forma predeterminada, Lyria 3 creará canciones con los instrumentos y las herramientas que esperarías para el género. No es necesario que seas prescriptivo.

Sin embargo, una pista de baile no incluirá un saxofón a menos que lo pidas. Por lo tanto, si quieres un solo de saxofón, debes indicarlo en la instrucción:

> Una pista de baile con un ritmo constante, sintetizadores brillantes y un coro pegadizo y épico. Un solo de saxofón debería aparecer durante el puente.

Tu instrucción puede incluir instrumentos específicos, cómo suenan y cómo interactúan entre sí. Puedes usar esta combinación para crear ciertos estados de ánimo o texturas:

- Una línea de bajo sucia y distorsionada que lucha contra hi-hats limpios y nítidos
- Cálidos pads de sintetizador analógico que se expanden bajo una guitarra acústica íntima y limpia
- Una pared de sonido creada por varias capas de guitarras distorsionadas, con voces distantes y enterradas

### Estructura de la canción

Puedes describir la progresión de una canción en tu instrucción. Usa flechas o una lista para definir el flujo:

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- Comienza con una introducción de piano suave, aumenta el volumen en el verso, baja el volumen hasta el silencio y, luego, explota en el coro.

También puedes especificar cómo cambian los niveles de energía entre estas secciones:

- Genera tensión en el pre-estribillo y, luego, baja el volumen hasta el silencio antes de un estribillo masivo y explosivo.
- Crescendo gradual a lo largo de la canción, en el que se agrega un instrumento a la vez hasta formar una caótica pared de sonido
- Detención repentina después del puente, seguida de un coro a capela

También puedes indicar la hora exacta en la que quieres que suceda algo:

- Aumenta la intensidad hasta que se produzca una caída a los 12 s.
- Alguien dice "¿qué?" cada 2 segundos
- El coro comienza a los 22 s.

### Letra

Las voces y las letras se generan de forma predeterminada. Puedes proporcionar tu propia letra, pedir que no se incluya (o que se incluya una versión instrumental) o dirigir la generación de la letra en la dirección que desees.

La letra estará en el idioma en el que escribas la instrucción. También puedes pedir que la letra esté en otro idioma, como "Escribe la letra en francés".

#### Cómo usar tus propias letras

Para proporcionarle al modelo tu propia letra, inclúyela en la instrucción con el prefijo "Letra:":

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

Puedes agregar un prefijo a partes de la canción con títulos de sección como `[Intro]`, `[Verse 1]`, `[Pre-chorus]`, `[Chorus]` y `[Outro]`.

Si quieres que se repita una palabra o línea, como un eco o con coristas, puedes incluirla entre paréntesis: "Vamos (vamos)".

#### Cómo indicarle al modelo que escriba letras

Si quieres que Lyria 3 escriba la letra por ti, lo mejor es que incluyas detalles sobre el tema de la letra en tu instrucción. De lo contrario, el modelo deberá inferir un tema a partir de tu instrucción musical, y es posible que no sea lo que deseas.

> La letra trata sobre el amor perdido y el dolor del desamor. La cantante recuerda una relación pasada y los recuerdos que vuelven a su mente.

Si quieres un coro que se repita, te recomendamos que lo pidas en la instrucción:

> La letra trata sobre el amor perdido y el dolor del desamor. La cantante recuerda una relación pasada y los recuerdos que vuelven a su mente. Un potente coro se centra en superar el dolor y seguir adelante.

Lyria 3 dirigirá automáticamente la estructura de la letra hacia el tipo de música que solicitas, pero también puedes volver a enfatizar esto en tu instrucción. Por ejemplo:

> Una pista de EDM que repite la misma frase enérgica una y otra vez.

También puedes solicitar efectos vocales que no sean estrictamente letras, por ejemplo:

- Una muestra repetitiva de una película dice "¡No puedo creerlo!" a lo largo de la canción.
- Una pista de tecno de alta energía, justo antes del drop, el sonido se detiene y una voz pequeña dice "No sé qué estoy haciendo aquí", y luego comienza la música.
- La canción comienza con una conversación sobre que las películas de los 90 eran mejores que las de hoy. Luego, la pista se une a una canción pop.

### Canto

Puedes indicar cómo quieres que se entregue la letra. Para obtener los mejores resultados, especifica un perfil detallado del cantante que incluya el género, el timbre y el rango vocal.

- **Soprano femenina**: Timbre claro y cristalino con una calidad ágil y elevada. Es capaz de alcanzar notas altas silbantes con una textura aireada y respirada.
- **Alto femenino**: Rango inferior rico, cálido y ronco. Timbre ahumado con un toque de fry vocal, conmovedor y resonante.
- **Tenor masculino**: Brillante, penetrante y enérgico. Timbre juvenil con un ligero borde nasal, que se destaca en la mezcla con una gran potencia de belting.
- **Barítono masculino**: Profundo, dulce y suave como el terciopelo. Voz de pecho resonante con una interpretación suave y melódica.
- **Rockero curtido (hombre)**: Rasposa y texturizada con un timbre áspero, que recuerda al grunge de los 90. Rango superior forzado para la intensidad emocional.

### Otros parámetros de la instrucción

También puedes incluir estos parámetros para definir mejor tu instrucción:

- **Tonalidad/Escala**: Especifica una tonalidad musical (p.ej., "en sol mayor", "en re menor").
- **Estado de ánimo y atmósfera**: Usa adjetivos descriptivos (p.ej., "nostálgico", "agresivo", "etéreo", "soñador").
- **Duración**: El modelo de Clip siempre produce clips de 30 segundos. En el caso del modelo Pro, especifica la duración deseada en tu instrucción (p.ej., "crea una canción de 2 minutos") o usa marcas de tiempo para controlar la duración.

### Ejemplos de instrucciones

Estos son algunos ejemplos de instrucciones eficaces:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Prácticas recomendadas

- **Primero, itera con Clip.** Usa el modelo `lyria-3-clip-preview` más rápido para experimentar con instrucciones antes de generar un video de larga duración con `lyria-3-pro-preview`.
- **Sea específico.** Las instrucciones vagas producen resultados genéricos. Menciona los instrumentos, los BPM, la clave, el estado de ánimo y la estructura para obtener el mejor resultado.
- **Usa etiquetas de sección.** Las etiquetas `[Verse]`, `[Chorus]` y `[Bridge]` le brindan al modelo una estructura clara que debe seguir.
- **Separa la letra de las instrucciones.** Cuando proporciones letras personalizadas, sepáralas claramente de las instrucciones de dirección musical.

## Limitaciones

- **Seguridad**: Todos los mensajes se verifican con filtros de seguridad. Se bloquearán las instrucciones que activen los filtros. Esto incluye las instrucciones que solicitan voces de artistas específicos o la generación de letras protegidas por derechos de autor.
- **Marcas de agua**: Todo el audio generado incluye una [marca de agua de audio de SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=es-419) para su identificación. Esta marca de agua es imperceptible para el oído humano y no afecta la experiencia de escucha.
- **Edición conversacional continua**: La generación de música es un proceso de un solo turno.
  En la versión actual de Lyria 3, no se admite la edición o el perfeccionamiento iterativos de un clip generado a través de múltiples instrucciones.
- **Duración**: El modelo de Clip siempre genera clips de 30 segundos. El modelo Pro genera canciones que duran un par de minutos. La duración exacta se puede influir a través de la instrucción.
- **Determinismo**: Los resultados pueden variar entre llamadas, incluso con la misma instrucción.

## ¿Qué sigue?

- Consulta los [precios](https://ai.google.dev/gemini-api/docs/generate-content/pricing?hl=es-419) de los modelos de Lyria 3.
- Prueba la [generación de música en tiempo real](https://ai.google.dev/gemini-api/docs/generate-content/realtime-music-generation?hl=es-419) con Lyria RealTime.
- Generar conversaciones con varios oradores con los [modelos de TTS](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=es-419)
- Descubre cómo generar [imágenes](https://ai.google.dev/gemini-api/docs/generate-content/image-generation?hl=es-419) o [videos](https://ai.google.dev/gemini-api/docs/generate-content/video?hl=es-419).
- Descubre cómo Gemini puede [comprender archivos de audio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=es-419).
- Mantén una conversación en tiempo real con Gemini usando la [API de Live](https://ai.google.dev/gemini-api/docs/generate-content/live?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-23 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-23 (UTC)"],[],[]]
