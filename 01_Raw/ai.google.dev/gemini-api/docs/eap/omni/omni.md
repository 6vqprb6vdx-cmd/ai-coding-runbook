---
source_url: https://ai.google.dev/gemini-api/docs/eap/omni/omni?hl=it
fetched_at: 2026-11-16T07:28:44.332789+00:00
title: "Genera e modifica video con Gemini Omni Flash 1.1 (programma di accesso in anteprima) \u00a0|\u00a0 Google AI for Developers"
---

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

# Genera e modifica video con Gemini Omni Flash 1.1 (programma di accesso in anteprima)

Gemini Omni Flash 1.1 (`gemini-omni-1.1-eap`) è un modello multimodale ad alte prestazioni progettato per la generazione, la modifica e il controllo cinematografico di video ad alta velocità.
Gemini Omni Flash 1.1 sostituisce completamente le versioni precedenti di Gemini Omni Flash, offrendo una qualità di generazione migliorata, multimodalità nativa e funzionalità di editing video con stato:

- **Multimodalità nativa:** elabora testo, immagini, audio e video contemporaneamente, offrendoti un output più coeso, coerente e controllabile.
- **Editing conversazionale:** abilitato dall'[API
  Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it), ti consente di perfezionare
  e modificare i video in modo iterativo tramite una conversazione in linguaggio naturale. Descrivi ciò che vuoi modificare e il modello applicherà la modifica mantenendo le parti del video che vuoi conservare.
- **Conoscenza del mondo:** Gemini Omni combina una comprensione della fisica con la conoscenza di storia, scienza e contesto culturale di Gemini, colmando il divario tra fotorealismo e narrazione significativa.

## Generazione di video da testo

Genera un video da un prompt di testo. Il modello genera un video con audio basato sulla descrizione del testo. Per ottenere risultati ottimali, scrivi prompt con dettagli come la descrizione della scena, il movimento della videocamera, l'illuminazione e l'atmosfera.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
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
  model: 'gemini-omni-1.1-eap',  
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
 "model": "gemini-omni-1.1-eap",
 "input": "A marble rolling fast on a chain reaction style track, continuous smooth shot."
}'
```

### Schema di risposta REST

Il campo di convenienza `interaction.output_video` è **solo SDK**.
Ottieni l'output video dall'array `steps` quando utilizzi direttamente l'API REST.

**Struttura JSON REST non elaborata:**

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
  "model": "gemini-omni-1.1-eap",
  "object": "interaction"
}
```

### Controllare le proporzioni

Imposta `aspect_ratio` su `"9:16"` per creare video verticali. Il valore predefinito è orizzontale (`16:9`).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
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
  model: 'gemini-omni-1.1-eap',
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
 "model": "gemini-omni-1.1-eap",
 "input": "A futuristic city with neon lights and flying cars, cyberpunk style",
 "response_format": {
   "type": "video",
   "aspect_ratio": "9:16"
 }
}'
```

### Controlli di risoluzione

#### Modalità bozza 360p

Utilizza `resolution: "360p"` in `response_format` per generare clip di anteprima leggere circa 2 volte più velocemente con un consumo di token ridotto.

### Python

```
interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input="A robotic dog exploring a lush enchanted forest.",
    response_format={
        "type": "video",
        "resolution": "360p",
        "aspect_ratio": "16:9"
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: 'A robotic dog exploring a lush enchanted forest.',
  response_format: {
    type: 'video',
    resolution: '360p',
    aspect_ratio: '16:9',
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "input": "A robotic dog exploring a lush enchanted forest.",
    "response_format": {
      "type": "video",
      "resolution": "360p",  # Supported values: "360p", "720p", "1080p", "4k"
      "aspect_ratio": "16:9"
    }
  }'
```

#### Alta risoluzione (1080p e 4K)

Imposta `resolution` su `"1080p"` o `"4k"` in `response_format` per generare video nitidi ad alta risoluzione.

### Python

```
interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input="A cinematic drone shot through misty pine mountains at sunrise.",
    response_format={
        "type": "video",
        "resolution": "1080p",  # Supported values: "360p", "720p", "1080p", "4k"
        "delivery": "uri"
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: 'A cinematic drone shot through misty pine mountains at sunrise.',
  response_format: {
    type: 'video',
    resolution: '1080p', // Supported values: '360p', '720p', '1080p', '4k'
    delivery: 'uri',
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "input": "A cinematic drone shot through misty pine mountains at sunrise.",
    "response_format": {
      "type": "video",
      "resolution": "1080p",
      "delivery": "uri"
    }
  }'
```

## Generazione di video da immagini

Puoi fornire immagini di riferimento con il prompt testuale. A seconda del prompt, il modello deciderà come utilizzare l'immagine, dando vita a scatti di prodotti, illustrazioni o fotografie.

L'esempio seguente mostra come utilizzare un'immagine di riferimento di un disegno di un pesce che salta fuori dall'acqua:

![Disegno di un pesce che salta fuori dall'acqua](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=it)

Con il seguente prompt:

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
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
  model: 'gemini-omni-1.1-eap',
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
 "model": "gemini-omni-1.1-eap",
 "input": [
   {"type": "image", "data": "'"$BASE64_IMAGE"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
 ]
}'
```

### Riferimento argomento

Puoi generare un video che incorpori soggetti specifici forniti come immagini di riferimento.
Ad esempio, il seguente codice mostra come fornire due immagini di un gatto e di un gomitolo di lana per generare un video del gatto che gioca con il gomitolo di lana.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
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
  model: 'gemini-omni-1.1-eap',
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
 "model": "gemini-omni-1.1-eap",
 "input": [
   {"type": "image", "data": "'"$CAT_B64"'", "mime_type": "image/png"},
   {"type": "image", "data": "'"$YARN_B64"'", "mime_type": "image/png"},
   {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
 ]
}'
```

### Parametro attività

Se vuoi, puoi impostare il parametro `task` in `video_config` in `generation_config` per definire esplicitamente l'attività di generazione. Se non è impostato, il modello determina automaticamente la modalità appropriata in base al prompt e ai media di input.

I valori `task` supportati includono:

- `text_to_video`: genera video esclusivamente da un prompt testuale.
- `image_to_video`: genera video da una o due immagini di origine (frame iniziale e frame finale facoltativo).
- `reference_to_video`: genera video utilizzando i media forniti come riferimenti.
- `edit`: modifica un video esistente.
- `extend`: estende un video clip esistente.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
    generation_config={
        "video_config": {
            "task": "image_to_video"
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
  model: 'gemini-omni-1.1-eap',
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
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

### Interpolazione dei fotogrammi chiave

Genera video continui che passano senza problemi da un frame iniziale a un frame finale. Questa soluzione è ideale per orbite della videocamera, effetti di zoom, progressioni di timelapse e clip in loop senza interruzioni.

Fornisci entrambe le immagini nell'array di input insieme a una descrizione del movimento desiderato:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input=[
        {"type": "image", "data": start_frame_b64, "mime_type": "image/png"},
        {"type": "image", "data": end_frame_b64, "mime_type": "image/png"},
        {
            "type": "text",
            "text": "Smooth continuous timelapse from sunrise to sunset over a mountain lake."
        }
    ],
    # The task parameter is optional. If omitted, the model automatically infers the mode.
    generation_config={
        "video_config": {
            "task": "image_to_video"
        }
    },
    response_format={"type": "video"}
)
with open("interpolated.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: [
    { type: 'image', data: startFrameB64, mime_type: 'image/png' },
    { type: 'image', data: endFrameB64, mime_type: 'image/png' },
    {
      type: 'text',
      text: 'Smooth continuous timelapse from sunrise to sunset over a mountain lake.'
    }
  ],
  // The task parameter is optional. If omitted, the model automatically infers the mode.
  generationConfig: {
    videoConfig: {
      task: 'image_to_video',
    },
  },
  response_format: { type: 'video' }
});

if (interaction.output_video?.data) {
  fs.writeFileSync('interpolated.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "input": [
      {"type": "image", "data": "'"$START_FRAME_B64"'", "mime_type": "image/png"},
      {"type": "image", "data": "'"$END_FRAME_B64"'", "mime_type": "image/png"},
      {
        "type": "text",
        "text": "Smooth continuous timelapse from sunrise to sunset over a mountain lake."
      }
    ],
    "generation_config": {
      "video_config": {
        "task": "image_to_video"
      }
    },
    "response_format": {"type": "video"}
  }'
```

## Editing video con stato

Genera un video e modificalo in modo iterativo utilizzando prompt di follow-up. Ogni turno si basa sul risultato precedente. Il modello ricorda il contesto del video, applicando le modifiche e mantenendo gli elementi che non hai menzionato. Utilizza `previous_interaction_id` per monitorare la cronologia delle conversazioni e lo stato del video generato senza ricaricare il video precedente.

L'esempio seguente mostra come generare un primo video e poi modificarlo:

### Python

```
import base64
from google import genai

client = genai.Client()

# Turn 1: Generate initial video
res1 = client.interactions.create(model="gemini-omni-1.1-eap", input="A woman playing violin outdoors.")

# Turn 2: Edit the previous video
res2 = client.interactions.create(
    model="gemini-omni-1.1-eap",
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
  model: 'gemini-omni-1.1-eap',
  input: 'A woman playing violin outdoors.',
});

// Turn 2: Edit the previous video
const res2 = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
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
 "model": "gemini-omni-1.1-eap",
 "previous_interaction_id": "'"$PREVIOUS_ID"'",
 "input": "Make the violin invisible."
}'
```

Esempio di un video iniziale:

Esempio di un video modificato:

Ogni turno della conversazione produce un nuovo video. Il modello comprende il contesto dei turni precedenti, consentendoti di apportare modifiche incrementali come la regolazione dell'illuminazione e la sostituzione degli sfondi, senza dover descrivere nuovamente l'intera scena.

### Modificare i propri video

Carica i tuoi video utilizzando l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it) per modificarli
con Gemini Omni Flash 1.1.

L'esempio seguente mostra come modificare il seguente video originale:

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
    model="gemini-omni-1.1-eap",
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

# Edit your video
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "input": [
      {
        "type": "video",
        "data": "'"$VIDEO_B64"'",
        "mime_type": "video/mp4"
      },
      {
        "type": "text",
        "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person arm turns into reflective mirror material"
      }
    ]
  }'
```

Esempio di un video modificato:

## Estensione della scena

Estendi i video clip esistenti utilizzando il contesto precedente. Gemini Omni Flash 1.1 analizza il movimento precedente e la composizione della scena per mantenere la continuità, l'identità dei personaggi e l'illuminazione ambientale nello scatto esteso.

### Python

```
import base64
from google import genai

client = genai.Client()

# Extend from a previous interaction ID
# The task parameter is optional. If omitted, the model automatically infers the mode.
extended = client.interactions.create(
    model="gemini-omni-1.1-eap",
    previous_interaction_id=res1.id,
    input="Continue the shot: the woman finishes the violin solo and takes a bow.",
    generation_config={
        "video_config": {
            "task": "extend"
        }
    },
    response_format={"type": "video"}
)
with open("extended.mp4", "wb") as f:
    f.write(base64.b64decode(extended.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// The task parameter is optional. If omitted, the model automatically infers the mode.
const extended = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  previous_interaction_id: res1.id,
  input: 'Continue the shot: the woman finishes the violin solo and takes a bow.',
  generationConfig: {
    videoConfig: {
      task: 'extend',
    },
  },
  response_format: { type: 'video' },
});

if (extended.output_video?.data) {
  fs.writeFileSync('extended.mp4', Buffer.from(extended.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "previous_interaction_id": "'"$PREVIOUS_ID"'",
    "input": "Continue the shot: the woman finishes the violin solo and takes a bow.",
    "generation_config": {
      "video_config": {
        "task": "extend"
      }
    },
    "response_format": {
      "type": "video"
    }
  }'
```

## Recuperare i video con un URI

Utilizza il parametro `delivery="uri"` in
`response_format` per recuperare i video generati di dimensioni superiori a 4 MB.
Viene restituito un URI ospitato da Google che puoi eseguire il polling finché il video non è `ACTIVE` prima di scaricarlo.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Request video via URI delivery
interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
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
video_bytes = client.files.download(file=video_output.uri)
with open("output.mp4", "wb") as f:
    f.write(video_bytes)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

// 1. Request video via URI delivery
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
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
console.log("Saved video to output.mp4");
```

### REST

```
#!/bin/bash

# 1. Initial request to generate the video
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-eap",
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

**Struttura JSON REST non elaborata (URI):**

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
  "model": "gemini-omni-1.1-eap",
  "object": "interaction"
}
```

## Best practice

- **Utilizza la distribuzione URI per i video di grandi dimensioni:** per i video di dimensioni superiori a 4 MB (>720p
  , se disponibili), utilizza `delivery="uri"` in `response_format` per evitare i limiti di dimensioni del payload.
- **Prestazioni ottimizzate:** imposta `background=false`, `store=false` e `stream=false` per una generazione unaria sincrona più rapida. Tieni presente che l'impostazione di `store=false` significa che il video generato non sarà modificabile nei turni successivi utilizzando `previous_interaction_id`.
- **Precisione del prompt:** per maggiori dettagli, consulta la sezione relativa alle [indicazioni per i prompt](#prompt-guide).

## Limitazioni

- Il caricamento e la modifica di immagini che contengono minori non sono supportati nello Spazio economico europeo, in Svizzera e nel Regno Unito.
- Il caricamento e la modifica di immagini che contengono determinate persone riconoscibili non sono supportati.
- La modifica dei video caricati non è attualmente disponibile per gli utenti dello Spazio economico europeo (SEE), della Svizzera e del Regno Unito (è supportata la modifica dei video generati dal modello).
- Il caricamento di riferimenti audio non è supportato nella versione attuale dell'API.
- I riferimenti video di durata massima di 3 secondi sono accettati dallo schema dell'API, ma al momento non vengono elaborati correttamente dal modello.
- Non è supportato il riferimento o il ragionamento su più video. Il tentativo di utilizzare prompt per più video potrebbe comportare un peggioramento delle prestazioni del modello o output imprevisti.
- L'estensione e l'interpolazione dei video (generazione di video tra un primo e un ultimo frame) non sono supportate.
- L'editing vocale non è supportato.
- La capacità di trasmissione di cui è stato eseguito il provisioning non è supportata.
- Le istruzioni di sistema, la temperatura, `top_p`, le sequenze di arresto e i prompt negativi non sono supportati (puoi inserire i negativi nel prompt normale, ad es. "Non fare X").
- L'utilizzo di video di YouTube come origine media non è supportato.

## Dettagli tecnici

- Tutti i video generati includono la filigrana SynthID, invisibile per gli spettatori ma rilevabile a livello di programmazione per la verifica della provenienza.
- I tempi di generazione dei video variano in base alla durata, alla risoluzione e al carico attuale dell'API. I video più lunghi e ad alta risoluzione richiedono più tempo per la generazione.
- I filtri di sicurezza dei contenuti vengono applicati sia ai prompt di input sia ai video generati (e dipendono dalla tua regione). I prompt che violano le norme di utilizzo verranno bloccati.
- L'inglese (EN) è completamente supportato, ma le altre lingue non sono state valutate, quindi potrebbero funzionare, ma i risultati possono variare.

## Guida ai prompt di Gemini Omni Flash

Questa sezione contiene suggerimenti ed esempi su come utilizzare i prompt di Gemini Omni Flash in modo efficace.

### Singola scena

Per impostazione predefinita, Omni Flash tenterà di creare un video con alcuni scatti diversi.
Tenterà di creare una narrazione interessante basata sul prompt.

Se vuoi che il video di output contenga una singola scena, devi utilizzare il prompt per questo scopo:

- In una singola scena ininterrotta
- In una singola sequenza continua
- Nessun taglio di scena

Ad esempio:

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### Rimuovere gli elementi indesiderati

Se il video generato contiene elementi che non ti interessano, includi semplici prompt negativi per evitarli:

- Nessun dialogo
- Nessuna decorazione
- Nessun effetto sonoro aggiuntivo

### Prompt per la modifica

I prompt semplici sono i più adatti per l'editing video. I prompt eccessivamente descrittivi possono comportare modifiche indesiderate.

Di seguito sono riportati altri esempi di prompt di editing semplici:

- Trasforma questo video in un anime
- Metti un cappello alla moda a questa persona
- Modifica l'illuminazione per renderla più drammatica
- Modifica il testo sul cartello in modo che dica "Omni Flash"

Quando modifichi un aspetto specifico del video, includi `"Keep everything else the same"` per mantenere la coerenza visiva.

Di seguito sono riportati alcuni esempi che mostrano come applicare questa tecnica:

- **Pratica non consigliata:** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **Semplifica:** `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **Pratica non consigliata:** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **Semplifica:** `Make the phone invisible. Keep everything else the
    same.`

### Prompt per l'audio

Per impostazione predefinita, il modello tenterà di generare una traccia audio appropriata per un video. Potrebbe non essere sempre quello che ti interessa. Puoi utilizzare il prompt per descrivere il tipo di audio che ti interessa. Questo è particolarmente importante se vuoi includere musica nel video:

- Include musica di sottofondo rilassante
- Il video ha un ritmo techno ad alta energia
- L'audio è una trasmissione radiofonica a bassa frequenza in sottofondo che riproduce una canzone

### Eventi di temporizzazione

Puoi utilizzare i prompt per far sì che gli eventi si verifichino in momenti specifici del video. Non è necessaria una sintassi precisa e puoi utilizzare il linguaggio naturale. Questa funzionalità è particolarmente utile per creare tagli di scena, sequenze ritmiche o rapide.
Di seguito sono riportati alcuni esempi:

- Dopo 3 secondi, una donna entra nella scena.
- A 5 secondi inizia il ritornello nell'audio di sottofondo.
- Ogni 2 secondi passa a un nuovo frame.
- In una sequenza rapida, ogni mezzo secondo (12 frame a 24 fps) cambia la scena in una nuova posizione.

Puoi anche utilizzare una sintassi di timecode:

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### Meta prompt

Puoi chiedere a Gemini Omni Flash di prestare attenzione alle qualità o ai principi generali della generazione di video:

- Considera i microdettagli, l'espressione e la tempistica per creare una scena molto ricca, dettagliata ma completamente naturale.
- Sii estremamente dettagliato nelle descrizioni dei personaggi e degli ambienti.
  Applica i principi di progettazione dei costumi ai personaggi. Sii molto specifico riguardo alle persone, agli articoli e agli oggetti nella scena.
- Includi molti dettagli appropriati negli elementi di sfondo per rendere la scena realistica e naturale.
- Crea un video rapido che mostri una diversa `[thing]` rara ogni secondo, musica allegra
  e testo per etichettare la cosa.

### Testo nei video

Puoi utilizzare i prompt per includere testo nel video e Gemini Omni eseguirà il rendering in modo corretto e leggibile. Se nel video è presente testo naturale, anche negli elementi di sfondo, può essere utile definire cosa deve dire.

- Una parola alla volta sullo schermo: "did, you, know, that, Omni, can, do, awesome, text?" Ogni parola viene visualizzata per 1 secondo con uno stile animato diverso. Nessun dialogo.
- C'è un cartello stradale con la scritta: "This is an AI generation by Omni", c'è una vetrina con la scritta: "All you need AI", c'è un'auto con la targa: "OMN111"

### Utilizzare i tag nei prompt per impostare i ruoli delle immagini

Puoi utilizzare i tag per associare i media caricati a ruoli di generazione specifici. In questo modo puoi specificare se ogni immagine è un frame iniziale o un riferimento.

- **`<FIRST_FRAME>`**: utilizza l'immagine come frame iniziale del video, per
  esempio: `<FIRST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**: utilizza l'immagine come riferimento, ad esempio: `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (combina il riferimento di stile
  della prima immagine e il riferimento del soggetto della seconda immagine).
  I riferimenti alle immagini iniziano da 0.

Di seguito è riportato un esempio con immagini di riferimento:

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

## Passaggi successivi

- Inizia a utilizzare Gemini Omni Flash sperimentando in the [Omni Quickstart Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=it).
- Scopri come scrivere prompt ancora migliori con la nostra [Introduzione alla progettazione dei prompt](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=it).

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-10 UTC.

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-10 UTC."],[],[]]
