---
source_url: https://ai.google.dev/gemini-api/docs/omni?hl=de
fetched_at: 2026-08-31T06:39:42.579317+00:00
title: "Videos mit Gemini Omni Flash generieren und bearbeiten \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Videos mit Gemini Omni Flash generieren und bearbeiten

Gemini Omni Flash (`gemini-omni-1.1-flash`) ist ein leistungsstarkes multimodales Modell, das für die schnelle Videogenerierung, ‑bearbeitung und filmische Steuerung entwickelt wurde.
Gemini Omni basiert auf den folgenden Kernfunktionen, die es von früheren Videomodellen unterscheiden:

- **Native Multimodalität**:Das Modell verarbeitet Text, Bilder, Audio und Video gleichzeitig und liefert so kohärentere, konsistentere und besser steuerbare Ausgaben.
- **Dialogorientierte Bearbeitung**:Diese Funktion wird durch die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ermöglicht und erlaubt es Ihnen, Ihre Videos durch Konversation in natürlicher Sprache iterativ zu verfeinern und zu bearbeiten. Beschreiben Sie, was Sie ändern möchten, und das Modell nimmt die Bearbeitung vor, wobei die Teile des Videos, die Sie behalten möchten, erhalten bleiben.
- **Weltwissen**:Gemini Omni kombiniert ein Verständnis von Physik mit dem Wissen von Gemini über Geschichte, Wissenschaft und kulturellen Kontext und schlägt so die Brücke vom Fotorealismus zum aussagekräftigen Storytelling.

## Text-zu-Video-Generierung

Video aus einem Text-Prompt generieren Das Modell generiert anhand Ihrer Textbeschreibung ein Video mit Audio. Für optimale Ergebnisse sollten Sie Prompts mit Details wie Szenenbeschreibung, Kamerabewegung, Beleuchtung und Stimmung verfassen.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A marble rolling fast on a chain reaction style track, continuous smooth shot."
)
with open("marble.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A marble rolling fast on a chain reaction style track, continuous smooth shot.',
});

if (interaction.output_video?.data) {
  fs.writeFileSync('marble.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A marble rolling fast on a chain reaction style track, continuous smooth shot."
}'
```

### REST-Antwortschema

Das Convenience-Feld `interaction.output_video` ist **nur für das SDK** verfügbar.
Wenn Sie die REST API direkt verwenden, rufen Sie die Videoausgabe aus dem `steps`-Array ab.

**Rohe REST-JSON-Struktur:**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "AAAAIGZ0eXBpc29t..." // Base64 encoded video data
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-1.1-flash",
  "object": "interaction"
}
```

### Seitenverhältnis anpassen

Stelle das `aspect_ratio` auf `"9:16"` ein, um Videos im Hochformat zu erstellen. Das Standardformat ist das Querformat (16:9).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A futuristic city with neon lights and flying cars, cyberpunk style",
    response_format={
        "type": "video",  # optional
        "aspect_ratio": "9:16"  # Supported values: "9:16", "16:9"
    }
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A futuristic city with neon lights and flying cars, cyberpunk style',
  response_format: {
    type: 'video', // optional
    aspect_ratio: '9:16' // Supported values: '9:16', '16:9'
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A futuristic city with neon lights and flying cars, cyberpunk style",
 "response_format": {
   "type": "video",
   "aspect_ratio": "9:16"
 }
}'
```

### Ausgabeauflösung

Mit dem Parameter `resolution` in `response_format` können Sie die Ausgabauflösung Ihres generierten Videos festlegen. Die Standardauflösung ist 720p.

| Wert | Beschreibung |
| --- | --- |
| `360p` | Ausgabeauflösung: 360p |
| `720p` | Ausgabeauflösung: 720p (Standard) |
| `1080p` | 1080p-Ausgabe (hochskaliert) |
| `4k` | 4K-Ausgabe (hochskaliert) |

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A drone shot of a mountain landscape at sunrise.",
    response_format={
        "type": "video",
        "resolution": "1080p",
    },
)
with open("hires.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A drone shot of a mountain landscape at sunrise.',
  response_format: {
    type: 'video',
    resolution: '1080p',
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('hires.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A drone shot of a mountain landscape at sunrise.",
 "response_format": {
   "type": "video",
   "resolution": "1080p"
 }
}'
```

## Bild-zu-Video-Generierung

Sie können Ihrem Text-Prompt ein Referenzbild hinzufügen. Je nach Prompt entscheidet das Modell, wie das Bild verwendet werden soll. Das ist nützlich, um Produktaufnahmen, Illustrationen oder Fotos zum Leben zu erwecken.

Im folgenden Beispiel wird gezeigt, wie Sie das Referenzbild einer Zeichnung eines Fisches verwenden, der aus dem Wasser springt:

![Zeichnung eines Fisches, der aus dem Wasser springt](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=de)

Mit dem folgenden Prompt:

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

Ein realistisches Video der Zeichnung generieren

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
)
with open("clownfish.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('clownfish.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$BASE64_IMAGE"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
 ]
}'
```

### Interpolation des ersten und letzten Frames

Gemini Omni Flash unterstützt die Videointerpolation. So können Sie ein Video erstellen, das nahtlos zwischen einem Startbild (erstes Frame) und einem Endbild (letztes Frame) übergeht.

Stellen Sie zwei Bilder in der Liste `input` bereit und beschreiben Sie den gewünschten Übergang in Ihrem Prompt. Das Modell animiert die Szene vom ersten bis zum letzten Frame.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": first_frame_b64, "mime_type": "image/jpeg"},
        {"type": "image", "data": last_frame_b64, "mime_type": "image/jpeg"},
        {"type": "text", "text": "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky."}
    ],
)
with open("interpolation.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: firstFrameB64, mime_type: 'image/jpeg' },
    { type: 'image', data: lastFrameB64, mime_type: 'image/jpeg' },
    { type: 'text', text: 'A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('interpolation.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$FIRST_FRAME_B64"'", "mime_type": "image/jpeg"},
   {"type": "image", "data": "'"$LAST_FRAME_B64"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky."}
 ]
}'
```

### Motivreferenz

Sie können ein Video mit bestimmten Motiven generieren, die als Referenzbilder bereitgestellt werden.
Im folgenden Codebeispiel sehen Sie, wie Sie zwei Bilder einer Katze und eines Wollknäuels bereitstellen, um ein Video zu generieren, in dem die Katze mit dem Wollknäuel spielt.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": cat_b64, "mime_type": "image/png"},
        {"type": "image", "data": yarn_b64, "mime_type": "image/png"},
        {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
    ],
)
with open("cat.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: catData, mime_type: 'image/png' },
    { type: 'image', data: yarnData, mime_type: 'image/png' },
    { type: 'text', text: 'A cat playfully batting at a ball of yarn.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('cat.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$CAT_B64"'", "mime_type": "image/png"},
   {"type": "image", "data": "'"$YARN_B64"'", "mime_type": "image/png"},
   {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
 ]
}'
```

### Parameter „Tasks“

Verwenden Sie den Parameter `task` in `video_config`, um das gewünschte Verhalten explizit anzugeben. Wenn Sie beispielsweise möchten, dass das Modell ein Video aus einem Bild generiert, können Sie den Parameter auf `image_to_video` festlegen. Wenn dies nicht festgelegt ist, leitet das Modell ab, was Sie vom Prompt erwarten.

Folgende Werte sind zulässig:

- `text_to_video`
- `image_to_video`
- `reference_to_video`
- `edit`
- `extend`

Im folgenden Beispiel wird gezeigt, wie Sie dies für das oben gezeigte Beispiel für Bild zu Video festlegen.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
    generation_config={
      "video_config": {
        "task": "image_to_video",
      }
    },
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ],
  generationConfig: {
    videoConfig: {
      task: 'image_to_video',
    }
  }
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-flash",
    "input": [
      {
        "type": "image",
        "data": "'"$BASE64_IMAGE"'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "text",
        "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"
      }
    ],
    "generation_config": {
      "video_config": {
        "task": "image_to_video"
      }
    }
  }'
```

## Zustandsbehaftete Videobearbeitung

Videos generieren und mithilfe von Folge-Prompts iterativ bearbeiten Jeder Zug baut auf dem vorherigen Ergebnis auf. Das Modell merkt sich den Videokontext und wendet Ihre Änderungen an, ohne Elemente zu verändern, die Sie nicht erwähnt haben. Verwenden Sie den `previous_interaction_id`, um den Unterhaltungsverlauf und den generierten Videostatus zu verfolgen, ohne das vorherige Video noch einmal hochzuladen.

Das folgende Beispiel zeigt, wie Sie zuerst ein Video generieren und es dann bearbeiten:

### Python

```
import base64
from google import genai

client = genai.Client()

# Turn 1: Generate initial video
res1 = client.interactions.create(model="gemini-omni-1.1-flash", input="A woman playing violin outdoors.")

# Turn 2: Edit the previous video
res2 = client.interactions.create(
    model="gemini-omni-1.1-flash",
    previous_interaction_id=res1.id,
    input="Make the violin invisible."
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(res2.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Turn 1: Generate initial video
const res1 = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A woman playing violin outdoors.',
});

// Turn 2: Edit the previous video
const res2 = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  previous_interaction_id: res1.id,
  input: 'Make the violin invisible.',
});

if (res2.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(res2.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "previous_interaction_id": "'"$PREVIOUS_ID"'",
 "input": "Make the violin invisible."
}'
```

Beispiel für ein ursprüngliches Video:

Beispiel für ein bearbeitetes Video:

Bei jeder Unterhaltungsrunde wird ein neues Video erstellt. Das Modell berücksichtigt den Kontext aus vorherigen Anfragen. So können Sie inkrementelle Änderungen vornehmen, z. B. die Beleuchtung anpassen oder den Hintergrund ändern, ohne die gesamte Szene neu zu beschreiben.

### Eigene Videos bearbeiten

Laden Sie Ihre Videos über die [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de) hoch, um sie mit Gemini Omni Flash zu bearbeiten.

Das folgende Beispiel zeigt, wie das folgende Originalvideo bearbeitet wird:

### Python

```
import time
import base64
from google import genai

client = genai.Client()

# Upload video using the file API
video_file = client.files.upload(file="Video.mp4")

while video_file.state == "PROCESSING":
    print('Waiting for video to be processed.')
    time.sleep(10)
    video_file = client.files.get(name=video_file.name)

if video_file.state == "FAILED":
  raise ValueError(video_file.state)
print(f'Video processing complete: ' + video_file.uri)

# Edit your video
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "text", "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"}
    ],
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload video using the file API
let videoFile = await ai.files.upload({
  file: 'Video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  console.log('Waiting for video to be processed.');
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

if (videoFile.state === 'FAILED') {
  throw new Error(videoFile.state);
}
console.log('Video processing complete: ' + videoFile.uri);

// Edit your video
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material" }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
#!/bin/bash
VIDEO_B64=$(encode_file "$VIDEO_FILE")

curl -sS -w "\n[HTTP %{http_code}]\n" "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d @- <<EOF > video_editing_response.json
{
  "model": "gemini-omni-1.1-flash",
  "input": [
    {
      "type": "user_input",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "$VIDEO_B64"
        },
        {
          "type": "text",
          "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"
        }
      ]
    }
  ],
  "response_format": { "type": "video" }
}
EOF
```

Beispiel für ein bearbeitetes Video:

## Videos mit einem URI abrufen

Verwenden Sie den Parameter `delivery="uri"` in `response_format`, um generierte Videos abzurufen, die größer als 4 MB sind.
Dadurch wird ein von Google gehosteter URI zurückgegeben, den Sie abfragen können, bis das Video `ACTIVE` ist, bevor Sie es herunterladen.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Request video via URI delivery
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A beautiful sunset.",
    response_format={"type": "video", "delivery": "uri"}
)

# 2. Extract file name and poll for ACTIVE state
video_output = interaction.output_video
file_name = video_output.uri.split("/")[-1] # Extract ID

print("Waiting for video processing...")
while True:
    f_info = client.files.get(name=f"files/{file_name}")
    if f_info.state.name == "ACTIVE":
        break
    elif f_info.state.name == "FAILED":
        raise RuntimeError("Generation failed.")
    time.sleep(5)

# 3. Download the final video
client.files.download(file=video_output.uri, destination="output.mp4")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

// 1. Request video via URI delivery
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A beautiful sunset.',
  response_format: { type: 'video', delivery: 'uri' },
});

// 2. Extract file name and poll for ACTIVE state
const videoOutput = interaction.output_video;
const fileId = videoOutput.uri.match(/files\/([a-zA-Z0-9]+)/)[1];
const name = `files/${fileId}`;

console.log("Waiting for video processing...");
while (true) {
  const fInfo = await ai.files.get({ name });
  if (fInfo.state.name === 'ACTIVE') break;
  if (fInfo.state.name === 'FAILED') throw new Error("Generation failed.");
  await new Promise(r => setTimeout(r, 5000));
}

// 3. Download the final video
await ai.files.download({
  file: videoOutput,
  downloadPath: 'output.mp4',
});
console.log("💾 Saved video to output.mp4");
```

### REST

```
#!/bin/bash

# 1. Initial request to generate the video
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A beautiful sunset over a calm ocean.",
 "response_format": {"type": "video", "delivery": "uri"}
}')

# Extract FILE_ID from the URI (e.g., "files/abc-123" -> "abc-123")
FILE_URI=$(echo $RESPONSE | jq -r '.output_video.uri')
FILE_ID=$(echo $FILE_URI | cut -d'/' -f2)

echo "Video requested (ID: $FILE_ID). Waiting for processing..."

# 2. Polling loop
while true; do
 # Get current file status
 STATUS_JSON=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID?key=$API_KEY")
 STATE=$(echo $STATUS_JSON | jq -r '.state')

 if [ "$STATE" == "ACTIVE" ]; then
   echo "Processing complete! Downloading..."
   break
 elif [ "$STATE" == "FAILED" ]; then
   echo "Error: Generation failed."
   exit 1
 else
   echo "Current state: $STATE... (waiting 5s)"
   sleep 5
 fi
done

# 3. Final download
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID:download?alt=media&key=$API_KEY" \
--output "output.mp4"

echo "Done! Video saved to output.mp4"
```

**Rohe REST-JSON-Struktur (URI):**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "uri": "https://generativelanguage.googleapis.com/v1beta/files/...:download?alt=media"
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-1.1-flash",
  "object": "interaction"
}
```

## Videoverlängerung

Ein vorhandenes Video verlängern, indem Sie am Ende des Clips eine nahtlose Fortsetzung generieren. Beschreiben Sie in Ihrem Prompt, wie das Video weitergehen soll, z. B. `"Extend this video"` oder `"Continue the scene: the camera pans across the mountains"`.
Das Modell analysiert das eingegebene Video, um eine Fortsetzung von 3 bis 10 Sekunden zu generieren.

Sie können Folgendes verlängern:

- **Vom Modell generierte Videos (Mehrfachdialog)**: Sie können ein zuvor generiertes Video erweitern, indem Sie auf seinen `previous_interaction_id` verweisen.
- **Hochgeladene Videos**: Stellen Sie eine hochgeladene Videodatei (über die Files API) zusammen mit Ihrem Erweiterungsprompt bereit.

### Python

```
import base64
from google import genai

client = genai.Client()

# Upload your video using the Files API
video_file = client.files.upload(file="my_video.mp4")

# Extend the video using prompt-based extension
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "text", "text": "Continue the scene."}
    ],
)
with open("extended.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload your video using the Files API
let videoFile = await ai.files.upload({
  file: 'my_video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Extend the video using prompt-based extension
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: 'Continue the scene.' }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('extended.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY"     -H "Content-Type: application/json"     -d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "document", "uri": "'"$VIDEO_URI"'"},
   {"type": "text", "text": "Continue the scene."}
 ]
}'
```

### Mit Referenzmedien erweitern

Sie können im `input`-Array zusammen mit Ihrem Prompt Referenzbilder angeben, um neue Charaktere oder Elemente in das erweiterte Video einzufügen:

### Python

```
import base64
from google import genai

client = genai.Client()

# Upload base video and reference image using the Files API
video_file = client.files.upload(file="my_video.mp4")
character_img = client.files.upload(file="character.png")

# Extend the video while introducing the reference character
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "document", "uri": character_img.uri},
        {"type": "text", "text": "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave."}
    ],
)
with open("extended_with_character.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload base video and reference image using the Files API
let videoFile = await ai.files.upload({ file: 'my_video.mp4' });
let characterImg = await ai.files.upload({ file: 'character.png' });

while (videoFile.state === 'PROCESSING' || characterImg.state === 'PROCESSING') {
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
  characterImg = await ai.files.get({ name: characterImg.name });
}

// Extend the video while introducing the reference character
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'document', uri: characterImg.uri },
    { type: 'text', text: 'Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave.' }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('extended_with_character.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY"     -H "Content-Type: application/json"     -d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "document", "uri": "'$VIDEO_URI'"},
   {"type": "document", "uri": "'$CHARACTER_IMG_URI'"},
   {"type": "text", "text": "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave."}
 ]
}'
```

### Einschränkungen und Richtlinien für Erweiterungen

Beachten Sie beim Verlängern von Videos die folgenden Regeln und Einschränkungen:

- **Gesprochene Dialoge in hochgeladenen Videos**: Derzeit können Sie ein hochgeladenes Video, in dem jemand spricht, nicht verlängern, um zusätzliche Dialoge hinzuzufügen. Das ist nur möglich, wenn die Figur stumm bleibt oder wenn durch den Prompt keine Dialoge hinzugefügt werden.
- **Sprach-Erweiterung im Mehrfachdialog**: Das Generieren von gesprochenen Dialogen oder Sprache wird unterstützt, wenn zuvor generierte Videos im Mehrfachdialog (`previous_interaction_id`) erweitert werden.
- **Nur am Ende des Clips**: Die Erweiterung kann nur am Ende des Videos angehängt werden.
  Sie können keine Inhalte vor einen Clip setzen oder die Mitte eines Clips verlängern.
- **Dauerbeschränkung**: Eingabe-Videos für Erweiterungen dürfen beim Hochladen nicht länger als 10 Sekunden sein (es sei denn, Sie verwenden Mehrfachdialog).
- **Regionale Verfügbarkeit**: Das Verlängern hochgeladener Videos ist derzeit nicht für Nutzer im Europäischen Wirtschaftsraum (EWR), in der Schweiz und im Vereinigten Königreich verfügbar. Das Verlängern von Videos, die vom Modell generiert wurden, wird in allen verfügbaren Regionen unterstützt.

## Best Practices

- **URI-Bereitstellung für große Videos verwenden**:Verwenden Sie für Videos, die größer als 4 MB sind (bei Verfügbarkeit > 720p), `delivery="uri"` in `response_format`, um Beschränkungen der Nutzlastgröße zu vermeiden.
- **Optimierte Leistung**:Legen Sie `background=false`, `store=false` und `stream=false` für eine schnellere, synchrone unäre Generierung fest. Wenn Sie `store=false` festlegen, kann das generierte Video in nachfolgenden Zügen nicht mit dem `previous_interaction_id` bearbeitet werden.
- **Prompt-Präzision**:Weitere Informationen finden Sie im Abschnitt [Anleitung für Prompts](#prompt-guide).

## Beschränkungen

- Das Hochladen und Bearbeiten von Bildern, auf denen Minderjährige zu sehen sind, wird im Europäischen Wirtschaftsraum, in der Schweiz und im Vereinigten Königreich nicht unterstützt.
- Das Hochladen und Bearbeiten von Bildern, auf denen bestimmte erkennbare Personen zu sehen sind, wird nicht unterstützt.
- Das Bearbeiten oder Verlängern hochgeladener Videos ist derzeit für Nutzer im Europäischen Wirtschaftsraum (EWR), in der Schweiz und im Vereinigten Königreich nicht verfügbar. Das Bearbeiten oder Verlängern von Videos, die vom Modell generiert wurden, wird unterstützt.
- Eingabevideos für die Bearbeitung und Verlängerung dürfen beim Hochladen maximal 10 Sekunden lang sein, es sei denn, es handelt sich um Videos, die vom Modell im Mehrfachdialog generiert wurden.
- Die Videoerweiterung ist auf das Anhängen an das Ende eines Videos beschränkt. Das Voranstellen oder Erweitern der Mitte eines Clips wird nicht unterstützt.
- Sie können ein hochgeladenes Video, in dem jemand spricht, nicht verlängern, um zusätzlichen Dialog hinzuzufügen. Die Charaktere können stumm bleiben oder es kann eine Mehrfachdialog-Erweiterung mit `previous_interaction_id` verwendet werden.
- Die Bearbeitung von Sprache wird nicht unterstützt.
- Das Hochladen von Audio-Referenzen wird in der aktuellen Version der API nicht unterstützt.
- Video-Referenzen funktionieren am besten mit Abbildungen. Audio in einer Video-Referenz wird ignoriert. Für Videoreferenzen können maximal drei Clips mit einer Länge von jeweils bis zu drei Sekunden verwendet werden.
- Das Verweisen auf oder Begründen mit mehreren Videos wird nicht unterstützt. Wenn Sie versuchen, mehrere Videos als Prompt zu verwenden, kann dies zu einer schlechteren Modellleistung oder unerwarteten Ausgaben führen.
- Bereitgestellter Durchsatz wird nicht unterstützt.
- Systemanweisungen, Temperatur, `top_p`, Stoppsequenzen und negative Prompts werden nicht unterstützt. Sie können Ihre negativen Prompts in den regulären Prompt einfügen, z. B. „Do not do X“ (Mache nicht X).
- YouTube-Videos können nicht als Media-Quelle verwendet werden.

## Technische Details

- Alle generierten Videos enthalten ein SynthID-Wasserzeichen, das für Zuschauer unsichtbar ist, aber programmatisch zur Überprüfung der Herkunft erkannt werden kann.
- Die Zeit, die für die Videogenerierung benötigt wird, hängt von der Dauer, der Auflösung und der aktuellen API-Last ab. Das Generieren längerer Videos mit höherer Auflösung dauert länger.
- Omni wendet Inhaltsfilter auf Eingabeaufforderungen und generierte Videos an. Diese Filter variieren je nach Region. Prompts, die gegen die Nutzungsrichtlinien verstoßen, werden blockiert.
- Englisch (EN) wird vollständig unterstützt. Andere Sprachen wurden nicht getestet. Sie funktionieren möglicherweise, aber die Ergebnisse können variieren.

## Anleitung zu Prompts für Gemini Omni Flash

Dieser Abschnitt enthält Tipps und Beispiele für effektive Prompts für Gemini Omni Flash.

### Einzelne Szene

Standardmäßig versucht Omni Flash, ein Video mit mehreren verschiedenen Aufnahmen zu erstellen.
Es wird versucht, basierend auf dem Prompt eine interessante Geschichte zu erstellen.

Wenn das Ausgabevideo nur eine Szene enthalten soll, müssen Sie das im Prompt angeben:

- In einer einzigen ununterbrochenen Szene
- In einer einzigen durchgehenden Aufnahme
- Keine Szenenschnitte

Beispiel:

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### Unerwünschte Elemente entfernen

Wenn das generierte Video Elemente enthält, die Sie nicht möchten, können Sie einfache negative Prompts verwenden, um sie zu vermeiden:

- Kein Dialog
- Keine Verzierungen
- Keine zusätzlichen Soundeffekte

### Aufforderungen zum Bearbeiten

Einfache Prompts eignen sich am besten für die Videobearbeitung. Zu detaillierte Prompts können zu unbeabsichtigten Änderungen führen.

Hier sind weitere Beispiele für einfache Bearbeitungsprompts:

- Verwandle dieses Video in einen Anime
- Setze dieser Person einen modischen Hut auf
- Ändere die Beleuchtung, damit sie dramatischer wirkt.
- Ändere den Text auf dem Schild in „Omni Flash“.

Wenn Sie einen bestimmten Aspekt des Videos bearbeiten, fügen Sie `"Keep everything else the same"` ein, um die visuelle Konsistenz beizubehalten.

Im Folgenden finden Sie einige Beispiele für die Anwendung dieser Technik:

- **Zu vermeiden**:`In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **Vereinfachen**:`Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **Zu vermeiden**:`Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **Vereinfachen**:`Make the phone invisible. Keep everything else the
    same.`

### Audio-Prompt

Standardmäßig versucht das Modell, einen geeigneten Audiotrack für ein Video zu generieren. Das ist möglicherweise nicht immer das, was Sie möchten. Mit Ihrem Prompt können Sie die Art von Audio beschreiben, die Sie möchten. Das ist besonders wichtig, wenn du Musik in deinem Video verwenden möchtest:

- Ruhige Hintergrundmusik einfügen
- Das Video hat einen energiegeladenen Techno-Beat
- Im Hintergrund ist eine leise, blecherne Radiosendung zu hören, in der ein Song gespielt wird.

### Zeitangaben

Sie können festlegen, dass bestimmte Dinge zu bestimmten Zeiten im Video passieren sollen. Dazu ist keine genaue Syntax erforderlich. Sie können natürliche Sprache verwenden. Das ist besonders nützlich, wenn Sie eigene Szenenschnitte, Rhythmus- oder Rapid-Fire-Sequenzen erstellen möchten.
Hier einige Beispiele:

- Nach 3 Sekunden betritt eine Frau die Szene.
- Bei 5 Sekunden beginnt der Refrain im Hintergrund-Audio.
- Alle 2 Sekunden wird ein neuer Frame eingeblendet.
- Bei einer Schnellfeuersequenz sollte alle halbe Sekunde (12 Frames bei 24 fps) die Szene an einen neuen Ort wechseln.

Sie können auch eine Timecode-Syntax verwenden:

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### Meta-Prompting

Sie können Gemini Omni Flash bitten, auf allgemeine Aspekte oder Grundsätze der Videogenerierung zu achten:

- Achten Sie auf Mikrodetails, Mimik und Timing, um eine sehr detaillierte, aber völlig natürliche Szene zu schaffen.
- Beschreiben Sie Charaktere und Umgebungen sehr detailliert.
  Grundsätze des Kostümdesigns auf Charaktere anwenden Beschreiben Sie die Personen, Elemente und Objekte in der Szene so genau wie möglich.
- Fügen Sie den Hintergrundelementen viele passende Details hinzu, damit die Szene realistisch und natürlich wirkt.
- Erstelle ein Video mit schnellen Schnitten, in dem alle 1 Sekunde ein anderes seltenes `[thing]` zu sehen ist. Verwende fröhliche Musik und füge Text hinzu, um die Dinge zu beschriften.

### Text in Videos

Sie können einen Prompt eingeben, um Text in Ihr Video einzufügen. Gemini Omni rendert den Text dann so, dass er korrekt und lesbar ist. Wenn in Ihrem Video Text vorkommt, auch in Hintergrundelementen, kann es hilfreich sein, festzulegen, was dort stehen soll.

- Es wird jeweils ein Wort auf dem Bildschirm angezeigt: „Wusstest, du, dass, Omni, tollen, Text, erstellen, kann?“ Jedes Wort wird eine Sekunde lang in einem anderen animierten Stil angezeigt. Keine Dialoge.
- Es gibt ein Straßenschild mit der Aufschrift „This is an AI generation by Omni“, ein Schaufenster mit der Aufschrift „All you need AI“ und ein Auto mit dem Nummernschild „OMNI1.1“.

### Prompts zum Verlängern eines Videos

Mit Gemini Omni 1.1 Flash können Sie Videos mit Prompts wie `"Extend this video"` oder `"The scene continues"` verlängern. Sie können Videos um jeweils 10 Sekunden verlängern, bis zu einer Gesamtlänge von 40 Sekunden.

Omni erstellt eine Erweiterung, bei der Video, Bewegung, Charaktere und Audio mithilfe der letzten 10 Sekunden Ihres Originalvideos als Kontext kohärent bleiben. Einige der letzten Frames in Ihrem Eingabevideo werden bearbeitet, um den Übergang nahtlos zu gestalten.

Wenn Sie die Funktion erweitern, gelten weiterhin alle Tipps für Omni-Prompts aus diesem Leitfaden:

- Beschreiben Sie die Audioinhalte in der erweiterten Szene, insbesondere wenn sie sich ändern sollen: `"The music continues into the chorus"`
- Beschreibe, ob die Szene fortgesetzt wird oder ob es einen Schnitt zu einer neuen Szene gibt (vielleicht mit denselben Figuren): `"Show the same characters in the next scene"`
- Fügen Sie Bilder und Videos als Referenzen hinzu, um die Genauigkeit der Ausgaben zu erhöhen oder neue Charaktere einzuführen: `"The person shown in the reference image enters the scene"`, `"The dog in the reference video <VIDEO_REF_0> jumps onto the sofa"`
- Wenn Sie Zeitstempel oder eine Timecode-Syntax verwenden, bezieht sich „0s“ auf den Beginn des erweiterten Teils des Videos. Wenn Sie ein 10‑Sekunden-Video verlängern, erfolgt der Szenenschnitt in diesem Prompt nach 12 Sekunden: `"After 2s cut to a new scene with the same characters"`

### Mit Tags in Prompts Bild- und Videorollen festlegen

Mit Tags können Sie hochgeladene Medien an bestimmte Generierungsrollen binden. So können Sie angeben, ob jedes Bild oder Video ein Startframe, ein Endframe oder eine Referenz ist.

#### 1. Einfache Tags (empfohlen)

In einfachen Fällen, in denen die Media-Rollen aus dem Prompt hervorgehen, können Sie Bilder und Videos direkt an Rollen binden:

- **`<FIRST_FRAME>`**: Verwenden Sie das Bild als Startframe des Videos, z. B. `<FIRST_FRAME> a woman is walking`.
- **`<LAST_FRAME>`**: Das Bild wird als letzter Frame des Videos verwendet, zu dem übergegangen wird. Muss zusammen mit `<FIRST_FRAME>` verwendet werden, z. B. `<FIRST_FRAME> <LAST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**: Verwenden Sie das Bild als Referenz, z. B. `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (kombiniert die Stilreferenz aus dem ersten Bild und die Motivreferenz aus dem zweiten Bild).
  Bildreferenzen beginnen bei 0.
- **`<VIDEO_REF_N>`**: Verwenden Sie das Video als Referenz für eine Figur oder ein Objekt, z. B.:
  `the person in <VIDEO_REF_0> is playing the violin`. Auch Videoreferenzen beginnen bei 0.

Hier ein Beispiel mit sechs Referenzbildern:

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

#### 2. Quellen und Referenzen angeben

Bei komplexeren Fällen mit mehreren Media-Eingaben und mehreren Rollen können Sie explizite Präfix-Tags in Kombination mit Anweisungen in natürlicher Sprache verwenden. Sie sollten diese Quellen und Referenzen am Anfang Ihres Prompts angeben.

- `[# Sources <FIRST_FRAME>@Image1]` verwendet das erste Bild als Startframe.
- `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image2]` verwendet das erste Bild als Startframe und das zweite Bild als Endframe.
- Bei `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image1]` wird das erste Bild sowohl als erster als auch als letzter Frame verwendet, sodass ein Video mit Endlosschleife entsteht.
- `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]` verwendet das erste Bild als Startframe und das zweite Bild als Referenz.
- `[# Sources <VIDEO_0>@Video1]` verwendet das Video als primäres Quellvideo zum Bearbeiten oder Ändern.
- `[# Sources <PREVIOUS_VIDEO>@Video1]` verwendet das Video aus dem vorherigen Zug, um es zu verlängern.
- `[# References <IMAGE_REF_0>@Image1]` verwendet das erste Bild als Referenz.
- `[# References <IMAGE_REF_1>@Image2]` verwendet das zweite Bild als Referenz.
- `[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]` verwendet beide Bilder als Referenzen.
- `[# References <VIDEO_REF_0>@Video1]` verwendet das erste Video als Referenz.
- `[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1]` verwendet sowohl ein Bild als auch ein Video als Referenz.

Fügen Sie am Ende des Prompts eine Anleitung hinzu:

- Für einen Startframe: `"Use this image as the starting frame."`
- Für ein Video, das über Start- und End-Frames wiederholt wird: `"Use this image as the first frame and the last frame."`
- Referenzbilder: `"Use the given image(s) as references for video generation. The images should not be used as literal initial frames."`
- Referenzvideos: `"Use the given video(s) as references. Do not use them as a source for video editing."`

Beispiele für Prompts mit Quell- und Referenzangaben:

**Start-Frame in Kombination mit einem Referenzbild**:

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2] a woman <IMAGE_REF_0> is walking. Use Image1 as the starting frame. Use Image2 as a reference for the video generation.
```

**Referenzvideo für die Figur in Kombination mit einem Referenzbild für das Objekt:**

```
[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1] The woman in <VIDEO_REF_0> is playing the violin shown in <IMAGE_REF_0>. Use Video1 as a character reference and Image1 as an object reference.
```

## Nächste Schritte

- Beginnen Sie mit Gemini Omni Flash, indem Sie im [Omni Quickstart Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=de) experimentieren.
- [Einführung in das Prompt-Design](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-08-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-08-30 (UTC)."],[],[]]
