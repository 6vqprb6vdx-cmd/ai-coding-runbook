---
source_url: https://ai.google.dev/gemini-api/docs/eap/omni/omni?hl=fr
fetched_at: 2026-11-09T07:27:37.466689+00:00
title: "G\u00e9n\u00e9rez et modifiez des vid\u00e9os avec Gemini Omni\u00a0Flash 1.1 (programme d'acc\u00e8s anticip\u00e9) \u00a0|\u00a0 Google AI for Developers"
---

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

# Générez et modifiez des vidéos avec Gemini Omni Flash 1.1 (programme d'accès anticipé)

Gemini Omni Flash 1.1 (`gemini-omni-1.1-eap`) est un modèle multimodal hautes performances conçu pour la génération, le montage et le contrôle cinématographique de vidéos à haute vitesse.
Gemini Omni Flash 1.1 remplace complètement les versions précédentes de Gemini Omni Flash, offrant une qualité de génération améliorée, une multimodalité native et des fonctionnalités de montage vidéo avec état :

- **Multimodalité native** : il traite simultanément le texte, les images, l'audio et la vidéo, ce qui vous offre une sortie plus cohérente, homogène et contrôlable.
- **Retouche conversationnelle** : activé par l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr), il vous permet d'affiner et de modifier vos vidéos de manière itérative grâce à une conversation en langage naturel. Décrivez ce que vous souhaitez modifier, et le modèle applique la modification tout en conservant les parties de la vidéo que vous souhaitez conserver.
- **Connaissances du monde** : Gemini Omni combine une compréhension de la physique avec les connaissances de Gemini en matière d'histoire, de sciences et de contexte culturel, comblant ainsi le fossé entre le photoréalisme et la narration significative.

## Génération de vidéos à partir de texte

Générez une vidéo à partir d'un prompt textuel. Le modèle génère une vidéo avec audio en fonction de votre description textuelle. Pour obtenir les meilleurs résultats, rédigez des prompts contenant des détails tels que la description de la scène, le mouvement de la caméra, l'éclairage et l'ambiance.

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

### Schéma de réponse REST

Le champ pratique `interaction.output_video` est **réservé au SDK**.
Obtenez la sortie vidéo à partir du tableau `steps` lorsque vous utilisez directement l'API REST.

**Structure JSON REST brute :**

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

### Contrôler le format

Définissez `aspect_ratio` sur `"9:16"` pour créer des vidéos en mode portrait. Le mode paysage (`16:9`) est le mode par défaut.

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

### Contrôles de résolution

#### Mode brouillon 360p

Utilisez `resolution: "360p"` dans `response_format` pour générer des extraits d'aperçu légers environ deux fois plus rapidement, avec une consommation de jetons réduite.

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

#### Haute résolution (1080p et 4K)

Définissez `resolution` sur `"1080p"` ou `"4k"` dans `response_format` pour générer des vidéos haute résolution nettes.

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

## Génération de vidéos à partir d'une image

Vous pouvez fournir des images de référence avec votre prompt textuel. En fonction de votre prompt, le modèle décidera comment utiliser l'image : il donnera vie à des photos de produits, des illustrations ou des photographies.

L'exemple suivant montre comment utiliser une image de référence d'un poisson sautant hors de l'eau :

![Dessin d'un poisson qui saute hors de l'eau](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=fr)

Avec le prompt suivant :

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

### Référence de sujet

Vous pouvez générer une vidéo intégrant des sujets spécifiques fournis sous forme d'images de référence.
Par exemple, le code suivant montre comment fournir deux images d'un chat et d'une pelote de laine pour générer une vidéo du chat jouant avec la pelote de laine.

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

### Paramètre "Tasks"

Vous pouvez éventuellement définir le paramètre `task` dans `video_config` sous `generation_config` pour définir explicitement la tâche de génération. Si ce paramètre n'est pas défini, le modèle détermine automatiquement le mode approprié en fonction du prompt et du contenu multimédia d'entrée.

Les valeurs `task` compatibles incluent les suivantes :

- `text_to_video` : génère une vidéo uniquement à partir d'un prompt textuel.
- `image_to_video` : génère une vidéo à partir d'une ou deux images sources (image de début et image de fin facultative).
- `reference_to_video` : génère une vidéo à l'aide du contenu multimédia fourni comme référence.
- `edit` : modifie une vidéo existante.
- `extend` : prolonge un extrait vidéo existant.

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

### Interpolation d'images clés

Générez une vidéo continue qui passe en douceur d'une image de début à une image de fin. Cette fonctionnalité est idéale pour les orbites de caméra, les effets de zoom, les progressions en accéléré et les extraits en boucle sans interruption.

Fournissez les deux images dans le tableau d'entrée, ainsi qu'une description du mouvement souhaité :

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

## Montage vidéo avec état

Générez une vidéo et modifiez-la de manière itérative à l'aide de prompts de suivi. Chaque tour s'appuie sur le résultat précédent. Le modèle mémorise le contexte de la vidéo, applique vos modifications tout en conservant les éléments que vous n'avez pas mentionnés. Utilisez `previous_interaction_id` pour suivre l'historique des conversations et l'état de la vidéo générée sans avoir à importer à nouveau la vidéo précédente.

L'exemple suivant montre comment générer une première vidéo, puis la modifier :

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

Exemple de vidéo initiale :

Exemple de vidéo modifiée :

Chaque tour de la conversation produit une nouvelle vidéo. Le modèle comprend le contexte des tours précédents, ce qui vous permet d'apporter des modifications incrémentielles, comme ajuster l'éclairage et échanger les arrière-plans, sans avoir à redécrire l'ensemble de la scène.

### Modifier vos propres vidéos

Importez vos vidéos à l'aide de l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr) pour les modifier
avec Gemini Omni Flash 1.1.

L'exemple suivant montre comment modifier la vidéo d'origine suivante :

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

Exemple de vidéo modifiée :

## Prolongation de scènes

Prolongez les extraits vidéo existants à l'aide du contexte précédent. Gemini Omni Flash 1.1 analyse le mouvement et la composition de la scène précédents pour maintenir la continuité, l'identité des personnages et l'éclairage environnemental tout au long du plan prolongé.

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

## Récupérer des vidéos avec un URI

Utilisez le paramètre `delivery="uri"` dans
`response_format` pour récupérer les vidéos générées de plus de 4 Mo.
Cette opération renvoie un URI hébergé par Google que vous pouvez interroger jusqu'à ce que la vidéo soit `ACTIVE` avant de la télécharger.

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

**Structure JSON REST brute (URI) :**

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

## Bonnes pratiques

- **Utiliser la diffusion d'URI pour les vidéos volumineuses** : pour les vidéos de plus de 4 Mo (> 720p
  lorsqu'elles sont disponibles), utilisez `delivery="uri"` dans `response_format` pour éviter les limites de taille de la charge utile.
- **Performances optimisées** : définissez `background=false`, `store=false` et `stream=false` pour une génération unaire synchrone plus rapide. Notez que si vous définissez `store=false`, la vidéo générée ne pourra pas être modifiée lors des tours suivants à l'aide de `previous_interaction_id`.
- **Précision du prompt** : pour en savoir plus, consultez la section [Conseils pour la création de requêtes](#prompt-guide).

## Limites

- L'importation et la modification d'images contenant des mineurs ne sont pas disponibles dans l'Espace économique européen, en Suisse ni au Royaume-Uni.
- L'importation et la modification d'images contenant certaines personnes reconnaissables ne sont pas disponibles.
- La modification des vidéos importées n'est actuellement pas disponible pour les utilisateurs de l'Espace économique européen (EEE), de la Suisse et du Royaume-Uni (la modification des vidéos générées par le modèle est disponible).
- L'importation de références audio n'est pas disponible dans la version actuelle de l'API.
- Les références vidéo d'une durée maximale de trois secondes sont acceptées par le schéma de l'API, mais ne sont pas correctement traitées par le modèle pour le moment.
- Il n'est pas possible de référencer ou de raisonner sur plusieurs vidéos. Si vous tentez d'utiliser des prompts pour plusieurs vidéos, les performances du modèle risquent de se dégrader ou des sorties inattendues peuvent se produire.
- L'extension vidéo et l'interpolation vidéo (génération de vidéo entre une première et une dernière image) ne sont pas disponibles.
- La modification vocale n'est pas disponible.
- Le débit provisionné n'est pas disponible.
- Les instructions système, la température, `top_p`, les séquences d'arrêt et les prompts négatifs ne sont pas disponibles (vous pouvez placer vos négatifs dans le prompt normal, par exemple "Ne fais pas X").
- L'utilisation de vidéos YouTube comme source multimédia n'est pas disponible.

## Détails techniques

- Toutes les vidéos générées incluent un filigrane SynthID, invisible pour les spectateurs, mais qui peut être détecté par programmation pour vérifier la provenance.
- Les délais de génération des vidéos varient en fonction de la durée, de la résolution et de la charge actuelle de l'API. Les vidéos plus longues et en plus haute résolution prennent plus de temps à générer.
- Les filtres de sécurité du contenu sont appliqués aux prompts d'entrée et à la vidéo générée (et dépendent de votre région). Les prompts qui ne respectent pas les règles d'utilisation seront bloqués.
- L'anglais (EN) est entièrement disponible, mais les autres langues n'ont pas été évaluées. Elles peuvent donc fonctionner, mais les résultats peuvent varier.

## Guide sur les prompts pour Gemini Omni Flash

Cette section contient des conseils et des exemples sur la façon d'utiliser efficacement les prompts pour Gemini Omni Flash.

### Scène unique

Par défaut, Omni Flash tente de créer une vidéo avec quelques plans différents.
Il essaie de créer un récit intéressant basé sur le prompt.

Si vous avez besoin que la vidéo de sortie contienne une seule scène, vous devez le spécifier dans le prompt :

- Dans une seule scène ininterrompue
- Dans un seul plan séquence
- Sans coupure de scène

Exemple :

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### Supprimer les éléments indésirables

Si la vidéo générée contient des éléments que vous ne souhaitez pas inclure, ajoutez des prompts négatifs simples pour les éviter :

- Sans dialogue
- Sans embellissement
- Sans effets sonores supplémentaires

### Prompts pour la modification

Les prompts simples sont plus efficaces pour le montage vidéo. Les prompts trop descriptifs peuvent entraîner des modifications involontaires.

Voici d'autres exemples de prompts de modification simples :

- Fais de cette vidéo un anime
- Mets un chapeau à la mode sur la tête de cette personne
- Rends l'éclairage plus spectaculaire
- Remplace le texte sur le panneau par "Omni Flash"

Lorsque vous modifiez un aspect spécifique de la vidéo, incluez `"Keep everything else the same"` pour maintenir la cohérence visuelle.

Voici quelques exemples pour montrer comment appliquer cette technique :

- **À éviter** : `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **Simplifier** : `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **À éviter** : `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **Simplifier** `Make the phone invisible. Keep everything else the
    same.`

### Prompts pour l'audio

Par défaut, le modèle tente de générer une piste audio appropriée pour une vidéo. Ce n'est pas toujours ce que vous souhaitez. Vous pouvez utiliser votre prompt pour décrire le type d'audio que vous souhaitez. Cela est particulièrement important si vous souhaitez ajouter de la musique à votre vidéo :

- Ajoute une musique de fond calme
- La vidéo contient un rythme techno énergique
- L'audio est une émission de radio de mauvaise qualité en arrière-plan, qui diffuse une chanson

### Événements de synchronisation

Vous pouvez demander que des événements se produisent à des moments spécifiques de la vidéo. Aucune syntaxe précise n'est requise et vous pouvez utiliser le langage naturel. Cela est particulièrement utile pour créer vos propres coupures de scène, votre propre rythme ou vos propres séquences rapides.
Voici quelques exemples :

- Après trois secondes, une femme entre dans la scène.
- À 5 secondes, le refrain commence dans l'audio en arrière-plan.
- Toutes les deux secondes, passe à une nouvelle image.
- Dans une séquence rapide, toutes les demi-secondes (12 images à 24 images par seconde), change la scène pour un nouvel emplacement.

Vous pouvez également utiliser une syntaxe de code temporel :

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### Meta-prompting

Vous pouvez demander à Gemini Omni Flash de prêter attention aux qualités ou principes généraux de la génération de vidéos :

- Tenez compte des micro-détails, de l'expression et du timing pour créer une scène très riche, détaillée, mais entièrement naturelle.
- Soyez extrêmement précis dans vos descriptions des personnages et des environnements.
  Appliquez les principes de conception de costumes aux personnages. Soyez très précis sur les personnes, les éléments et les objets de la scène.
- Incluez de nombreux détails appropriés dans les éléments d'arrière-plan pour que la scène soit réaliste et naturelle.
- Crée une vidéo rapide qui montre une `[thing]` rare différente toutes les secondes, avec une musique entraînante
  et du texte pour étiqueter la chose.

### Texte dans les vidéos

Vous pouvez demander à inclure du texte dans votre vidéo, et Gemini Omni le rendra de manière correcte et lisible. Si votre vidéo contient du texte naturel, même dans les éléments d'arrière-plan, il peut être utile de définir ce qu'il doit dire.

- Un mot à la fois à l'écran : "did, you, know, that, Omni, can, do, awesome, text?" Chaque mot apparaît pendant une seconde avec un style animé différent. Aucun dialogue.
- Un panneau de signalisation indique : "This is an AI generation by Omni" (Il s'agit d'une génération d'IA par Omni), une vitrine indique : "All you need AI" (Tout ce dont vous avez besoin, c'est de l'IA), une voiture porte la plaque d'immatriculation "OMN111".

### Utiliser des tags dans les prompts pour définir les rôles des images

Vous pouvez utiliser des tags pour lier le contenu multimédia importé à des rôles de génération spécifiques. Cela vous permet de spécifier si chaque image est une image initiale ou une référence.

- **`<FIRST_FRAME>`** : utilisez l'image comme image de début de la vidéo, pour
  exemple : `<FIRST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`** : utilisez l'image comme référence, par exemple : `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (combine la référence de style
  de la première image et la référence de sujet de la deuxième image).
  Les références d'image commencent à 0.

Voici un exemple avec des images de référence :

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

## Étape suivante

- Commencez à utiliser Gemini Omni Flash en testant le [Colab de démarrage rapide Omni](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=fr).
- Découvrez comment rédiger des prompts encore plus efficaces grâce à notre [Introduction à la conception de requêtes](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=fr).

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/10 (UTC).

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/10 (UTC)."],[],[]]
