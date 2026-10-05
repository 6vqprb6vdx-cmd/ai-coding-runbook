---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr
fetched_at: 2026-10-05T06:31:10.364479+00:00
title: "G\u00e9n\u00e9ration de synth\u00e8se vocale \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Génération de synthèse vocale

L'API Gemini peut transformer des entrées de texte en contenu audio à un ou plusieurs intervenants à l'aide des fonctionnalités de génération de synthèse vocale (TTS) de Gemini.
La génération de synthèse vocale est *[contrôlable](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr#controllable)*, ce qui signifie que vous pouvez combiner des métadonnées de tour structurées (`speech_metadata`) et des balises vocales intégrées pour guider le *style*, l'*accent*, le *rythme* et le *ton* de l'audio.

La fonctionnalité TTS diffère de la génération vocale fournie par l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr), qui est conçue pour les entrées et sorties audio interactives, non structurées et multimodales. Alors que l'API Live excelle dans les contextes conversationnels dynamiques, la TTS via l'API Gemini est conçue pour les scénarios qui nécessitent une récitation exacte du texte avec un contrôle précis du style et du son, comme la génération de podcasts ou de livres audio.

Ce guide vous explique comment générer de l'audio à une ou plusieurs voix à partir de texte à l'aide de [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr) (`gemini-3.8-flash-tts`) et [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fr) (`gemini-3.8-flash-lite-tts`).

## Avant de commencer

Assurez-vous d'utiliser un modèle Gemini TTS listé dans la section [Modèles compatibles](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr#supported-models), et passez à la dernière version du SDK Google GenAI (`google-genai >= 2.25.0` pour Python ou `@google/genai >= 2.24.0` pour JavaScript/TypeScript) ou utilisez l'API REST.
Pour obtenir des résultats optimaux, consultez [Quand utiliser tel ou tel modèle](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr#when-to-use-which-model) afin de sélectionner le modèle le mieux adapté à votre charge de travail.

Il peut être utile de [tester les modèles Gemini TTS dans AI Studio](https://aistudio.google.com/generate-speech?hl=fr) avant de commencer à créer.

## TTS à un seul locuteur

Pour convertir du texte en audio à un seul locuteur avec les modèles Gemini 3.8 TTS, transmettez la transcription verbatim dans `input`, ajoutez un style au niveau du tour de parole à l'aide d'une annotation `speech_metadata` et configurez votre voix dans `generation_config.speech_config`. Vous pouvez choisir une voix parmi les [options vocales](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr#voices) prédéfinies, la bibliothèque vocale étendue (`GET /v1beta/voices`), un ID de [conception vocale](https://ai.google.dev/gemini-api/docs/voice-design?hl=fr) personnalisé (`voice_...`) ou un ID de [réplication vocale](https://ai.google.dev/gemini-api/docs/voice-replication?hl=fr) (`voice_...` ou `voicekey_...` sans état facultatif).

Cet exemple enregistre la sortie audio WAV par défaut (`audio/wav`) du modèle directement dans un fichier :

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "encoding/binary"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func saveWaveFile(filename string, pcmData []byte) error {
    f, err := os.Create(filename)
    if err != nil {
        return err
    }
    defer f.Close()

    sampleRate := uint32(24000)
    numChannels := uint16(1)
    bitsPerSample := uint16(16)
    byteRate := sampleRate * uint32(numChannels) * uint32(bitsPerSample/8)
    blockAlign := numChannels * (bitsPerSample / 8)
    dataSize := uint32(len(pcmData))

    f.WriteString("RIFF")
    binary.Write(f, binary.LittleEndian, uint32(36+dataSize))
    f.WriteString("WAVEfmt ")
    binary.Write(f, binary.LittleEndian, uint32(16))
    binary.Write(f, binary.LittleEndian, uint16(1))
    binary.Write(f, binary.LittleEndian, numChannels)
    binary.Write(f, binary.LittleEndian, sampleRate)
    binary.Write(f, binary.LittleEndian, byteRate)
    binary.Write(f, binary.LittleEndian, blockAlign)
    binary.Write(f, binary.LittleEndian, bitsPerSample)
    f.WriteString("data")
    binary.Write(f, binary.LittleEndian, dataSize)
    _, err = f.Write(pcmData)
    return err
}

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Voice: genai.Ptr("Kore")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput("Say cheerfully: Have a wonderful day!"),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        pcmBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := saveWaveFile("out.wav", pcmBytes); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

Dans les SDK Python et JavaScript, vous pouvez récupérer les données audio générées à l'aide de la propriété pratique `interaction.output_audio`, qui renvoie le dernier bloc audio généré (dans les réponses JSON REST brutes, l'audio encodé en base64 est stocké dans `steps[].content[].data`). Pour en savoir plus sur les propriétés pratiques, consultez [Présentation des interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr#convenience-properties).

## TTS multilocuteur

Pour les dialogues à plusieurs locuteurs, configurez deux locuteurs dans `speech_config.speakers` et transmettez chaque tour de parole en tant qu'élément de texte distinct avec une annotation `speech_metadata` spécifiant `speaker` et `style` facultatif au niveau du tour de parole. Notez que `speech_config` accepte un tableau (`[{"voice": "..."}]`) pour la génération à une seule voix et un objet (`{"speakers": [...]}`) pour la génération à plusieurs voix :

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [
            {
                "type": "text",
                "text": "How's it going today Jane?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                }],
            },
            {
                "type": "text",
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                }],
            },
        ],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": {
            "speakers": [
                {"speaker": "Joe", "voice": "Puck"},
                {"speaker": "Jane", "voice": "Kore"},
            ],
        }
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [
            {
               type: 'text',
               text: "How's it going today Jane?",
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               }],
            },
            {
               type: 'text',
               text: 'Not too bad, how about you? Ready to test these new voices?',
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               }],
            },
         ],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: {
            speakers: [
               { speaker: 'Joe', voice: 'Puck' },
               { speaker: 'Jane', voice: 'Kore' },
            ],
         },
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "encoding/binary"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func saveWaveFile(filename string, pcmData []byte) error {
    f, err := os.Create(filename)
    if err != nil {
        return err
    }
    defer f.Close()

    sampleRate := uint32(24000)
    numChannels := uint16(1)
    bitsPerSample := uint16(16)
    byteRate := sampleRate * uint32(numChannels) * uint32(bitsPerSample/8)
    blockAlign := numChannels * (bitsPerSample / 8)
    dataSize := uint32(len(pcmData))

    f.WriteString("RIFF")
    binary.Write(f, binary.LittleEndian, uint32(36+dataSize))
    f.WriteString("WAVEfmt ")
    binary.Write(f, binary.LittleEndian, uint32(16))
    binary.Write(f, binary.LittleEndian, uint16(1))
    binary.Write(f, binary.LittleEndian, numChannels)
    binary.Write(f, binary.LittleEndian, sampleRate)
    binary.Write(f, binary.LittleEndian, byteRate)
    binary.Write(f, binary.LittleEndian, blockAlign)
    binary.Write(f, binary.LittleEndian, bitsPerSample)
    f.WriteString("data")
    binary.Write(f, binary.LittleEndian, dataSize)
    _, err = f.Write(pcmData)
    return err
}

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := "TTS the following conversation between Joe and Jane:\n" +
        "Joe: How's it going today Jane?\n" +
        "Jane: Not too bad, how about you?"

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Speaker: genai.Ptr("Joe"), Voice: genai.Ptr("Kore")},
            {Speaker: genai.Ptr("Jane"), Voice: genai.Ptr("Puck")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput(prompt),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        pcmBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := saveWaveFile("out.wav", pcmBytes); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [
        {
          "type": "text",
          "text": "How'\''s it going today Jane?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }]
        },
        {
          "type": "text",
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Jane",
            "style": "calm and relaxed"
          }]
        }
      ]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": {
        "mode": "conversational",
        "speakers": [
          { "speaker": "Joe", "voice": "Puck" },
          { "speaker": "Jane", "voice": "Kore" }
        ]
      }
    }
  }'
```

## Contrôler le style de parole avec des métadonnées et des tags

Gemini 3.8 TTS traite le champ `text` strictement comme une transcription mot à mot. Pour contrôler la diffusion sans que les indications scéniques soient lues à voix haute, séparez vos instructions par portée :

- **Diffusion soutenue au niveau du tour de parole (`speech_metadata.style`)** : indiquez les émotions, le style de diffusion, la prosodie, le rythme et le volume qui s'appliquent à l'ensemble d'un tour de parole dans le champ `style` (par exemple, `"style": "whispered urgently"`, `"style": "out of breath"` ou `"style": "warm and enthusiastic"`).
- **Événements ponctuels (balises intégrées)** : placez les brèves pauses ou les brèves émissions vocales non verbales directement dans la transcription à l'aide de crochets (par exemple, `"Wait... <short pause> did you hear that? <sigh>"` ou `"Excuse me <cough> as I was saying..."`).

Pour obtenir des bonnes pratiques complètes, consultez le [guide sur les requêtes](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr#prompting-guide).

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

    transcriptRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(
                "Generate a short transcript around 100 words that reads " +
                    "like it was clipped from a podcast by excited herpetologists. " +
                    "The hosts names are Dr. Anya and Liam.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var transcript string
    if transcriptRes.Interaction.OutputText != nil {
        transcript = *transcriptRes.Interaction.OutputText
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Speaker: genai.Ptr("Dr. Anya"), Voice: genai.Ptr("Kore")},
            {Speaker: genai.Ptr("Liam"), Voice: genai.Ptr("Puck")},
        })),
    }

    ttsRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput(transcript),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = ttsRes
}
```

## Génération de voix en flux continu

Vous pouvez diffuser l'audio généré au fur et à mesure de sa synthèse en définissant `stream: true`. Contrairement aux requêtes unaires (qui renvoient un fichier WAV complet avec un en-tête RIFF), **les requêtes de streaming renvoient par défaut des blocs bruts de PCM linéaire little-endian signé 16 bits sans en-tête (`audio/l16`, 24 kHz, mono)**. Les blocs audio peuvent ainsi être lus ou concaténés en continu sans en-tête de conteneur.

### Python

```
import base64
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "audio":
            audio_data = base64.b64decode(event.delta.data)
            # Process the audio chunk (e.g. play it or write to a file)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const stream = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
      stream: true,
   });

   for await (const event of stream) {
      if (event.event_type === 'step.delta') {
         if (event.delta.type === 'audio') {
            const audioBuffer = Buffer.from(event.delta.data, 'base64');
            // Process the audio buffer
         }
      }
   }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    },
    "stream": true
  }'
```

## Formats de sortie audio

Les modèles Gemini 3.8 TTS utilisent différents formats audio par défaut selon que la requête est unaire ou en flux :

- **Requêtes unaires (`stream=False`)** : renvoient un fichier audio **WAV (`audio/wav`)** complet avec un en-tête RIFF standard (PCM 16 bits little-endian signé, mono, 24 kHz). Vous pouvez enregistrer les octets audio décodés directement dans un fichier `.wav` sans ajouter manuellement d'en-tête WAV.
- **Requêtes de flux (`stream=True`)** : renvoient par défaut des blocs **PCM linéaire brut sans en-tête (`audio/l16`)** (PCM 24 kHz, mono, 16 bits signé little-endian). Les blocs peuvent ainsi être diffusés en streaming ou concaténés en continu sans en-tête de conteneur sur chaque bloc.

Pour demander un autre encodage audio ou une autre fréquence d'échantillonnage, configurez `mime_type` et `sample_rate` facultatif dans `response_format` :

| Format | Valeur `mime_type` | Description |
| --- | --- | --- |
| **WAV** *(par défaut pour les valeurs unitaires)* | `"audio/wav"` | Fichier WAV non compressé avec un en-tête RIFF (PCM 16 bits signé little-endian, mono, 24 kHz par défaut). Valeur par défaut pour les requêtes unaires. |
| **PCM brut (L16)** *(paramètre par défaut pour le streaming)* | `"audio/l16"` | Audio PCM linéaire 16 bits signé little-endian sans en-tête et non compressé (24 kHz, mono). Valeur par défaut pour les requêtes de streaming. |
| **Mu-law** | `"audio/mulaw"` | Audio encodé en G.711 MULAW 8 bits (couramment utilisé dans les systèmes de téléphonie/SVI nord-américains et japonais). |
| **A-law** | `"audio/alaw"` | Audio encodé en G.711 A-law 8 bits (couramment utilisé dans les systèmes de téléphonie européens et internationaux). |

Vous pouvez également spécifier `sample_rate` en Hertz (par exemple, `24000`, `16000` ou `8000`).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={
        "type": "audio",
        "mime_type": "audio/l16",  # "audio/wav" (default), "audio/l16", "audio/mulaw", or "audio/alaw"
        "sample_rate": 24000,
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.pcm", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: {
         type: 'audio',
         mime_type: 'audio/l16', // 'audio/wav' (default), 'audio/l16', 'audio/mulaw', or 'audio/alaw'
         sample_rate: 24000,
      },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.pcm', audioBuffer);
}
await main();
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
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

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Voice: genai.Ptr("Kore")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput("Say cheerfully: Have a wonderful day!"),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
            Stream:           genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if audioDelta := stepDelta.GetDeltaAudio(); audioDelta != nil && audioDelta.Data != nil {
                audioData, err := base64.StdEncoding.DecodeString(*audioDelta.Data)
                if err != nil {
                    log.Fatal(err)
                }
                // Process the audio chunk (e.g. play it or write to a file)
                _ = audioData
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio",
      "mime_type": "audio/l16",
      "sample_rate": 24000
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

## Options vocales

Gemini 3.8 TTS permet de sélectionner ou de créer des voix de quatre manières :

1. **Voix Studio prédéfinies** : 30 voix sélectionnées sont listées dans le tableau suivant.
2. **Bibliothèque vocale étendue** : des centaines de voix supplémentaires dans différentes langues, avec différents accents et différents archétypes de personnages sont disponibles à l'aide de `client.voices.list()` (`GET /v1beta/voices`).
3. **[Conception de voix](https://ai.google.dev/gemini-api/docs/voice-design?hl=fr)** : générez une personnalité vocale personnalisée à partir d'une description en langage naturel dans [Google AI Studio](https://aistudio.google.com/generate-speech?hl=fr) ou à l'aide de `POST /v1beta/voices` (`type="prompted"`, qui renvoie un ID `voice_...` persistant et un aperçu WAV `sample_audio` dans `CreateVoice` et `GetVoice`).
4. **[Réplication de la voix](https://ai.google.dev/gemini-api/docs/voice-replication?hl=fr)** : répliquez la voix d'un locuteur à partir d'un contenu audio de référence et de consentement dans [Google AI Studio](https://aistudio.google.com/generate-speech?hl=fr) ou à l'aide de `POST /v1beta/voices` (`type="replicated"`, `store=True` persistant par défaut ou `store=False` sans état facultatif).

### Limites et TTL des voix personnalisées

| Type de voix | Mode de stockage | Quota / Limite | Rétention (TTL) |
| --- | --- | --- | --- |
| **Voix avec état** (`voice_...`, générées ou répliquées) | `store=True` | **200 voix par projet** (partagées entre les voix incitées et répliquées) | **1 an à compter de la dernière utilisation\*** |
| **Clés vocales sans état** (`voicekey_...`, répliquées) | `store=False` | Géré par le client | **7 jours** |

\* **Extension de la durée de vie** : la période de conservation d'un an est réinitialisée chaque fois que la voix est utilisée activement (soit pour synthétiser la parole, soit comme voix de base pour un remix). Les voix qui n'ont pas été utilisées pendant un an sont automatiquement supprimées.

### Voix prédéfinies

|  |  |  |
| --- | --- | --- |
| **Zephyr** : *Lumineux* | **Puck** : *Upbeat* | **Charon** : *informatif* |
| **Kore** : *Ferme* | **Fenrir** : *excitabilité* | **Leda** : *jeune* |
| **Orus** : *ferme* | **Aoede** : *Breezy* | **Callirrhoe** : *tranquille* |
| **Autonoe** : *Lumineux* | **Encelade** : *Souffle* | **Iapetus** : *Effacer* |
| **Umbriel** : *décontracté* | **Algieba** : *Lisse* | **Despina** : *Smooth* |
| **Erinome** : *Effacer* | **Algenib** : *Graveleux* | **Rasalgethi** : *Informations* |
| **Laomedeia** : *Upbeat* | **Achernar** : *Soft* | **Alnilam** -- *Firm* |
| **Schedar** : *pair* | **Gacrux** : *Contenu réservé aux adultes* | **Pulcherrima** -- *Forward* |
| **Achird** : *amical* | **Zubenelgenubi** : *décontracté* | **Vindemiatrix** : *Doux* |
| **Sadachbia** : *Lively* | **Sadaltager** : *connaissances* | **Sulafat** : *chaude* |

### Bibliothèque vocale étendue et filtrage

En plus des 30 voix de studio présentées dans le tableau précédent, la **bibliothèque vocale étendue** propose des centaines de voix supplémentaires dans différentes langues, avec des accents régionaux, des personnages et des domaines variés. Vous pouvez parcourir, filtrer et écouter l'intégralité de la bibliothèque de voix de manière interactive dans [Google AI Studio](https://aistudio.google.com/generate-speech?hl=fr), ou l'interroger de manière programmatique à l'aide de `client.voices.list()` (`GET /v1beta/voices`, en utilisant `google-genai` 2.25.0+ / `@google/genai` 2.24.0+).

`ListVoices` renvoie vos voix stockées personnalisées (de la plus récente à la plus ancienne), suivies des voix de catalogue prédéfinies correspondant à vos critères de filtrage. Lorsque plusieurs valeurs sont transmises pour un filtre de liste, les voix correspondant à **n'importe quelle** valeur de ce filtre sont renvoyées (`OR`), tandis que les paramètres de filtre distincts sont combinés avec `AND` :

| Paramètre | Type | Description |
| --- | --- | --- |
| `language_code` | `list[str]` | Balise(s) de langue BCP-47 (par exemple, `["en-US", "en-GB"]`). Correspondance exacte non sensible à la casse. |
| `region_code` | `list[str]` | Code(s) de région ISO 3166-1 alpha-2 ou UN M.49 (par exemple, `["US", "GB"]`). |
| `accent` | `list[str]` | Descripteur(s) d'accent régional (par exemple, `["American", "British"]`). |
| `gender` | `list[str]` | Genre perçu (`"female"`, `"male"` ou `"neutral"`). |
| `pitch` | `list[str]` | Classification de la hauteur vocale (`"low"`, `"medium"` ou `"high"`). |
| `persona` | `list[str]` | Personnalité vocale ou archétype de personnage (par exemple, `["Warm, Friendly"]`, `["Narrator"]`). |
| `contexts` (`context` dans REST) | `list[str]` | Domaine d'utilisation optimal (par exemple, `["Audiobook", "Conversational", "News"]`). |
| `type` (`type_` en Python) | `list[str]` | Filtrer par source vocale : `"prebuilt"`, `"prompted"` ([Conception de voix](https://ai.google.dev/gemini-api/docs/voice-design?hl=fr)) ou `"replicated"` ([Réplication de voix](https://ai.google.dev/gemini-api/docs/voice-replication?hl=fr)). |
| `search` | `str` | La recherche de sous-chaînes en texte libre correspond à la casse insensible par rapport à `display_name` et `description`. |
| `page_size` | `int` | Nombre maximal de voix renvoyées par page (`50` par défaut, `1000` maximum). |
| `page_token` | `str` | Jeton de `response.next_page_token` permettant d'extraire la page de résultats suivante. |

### Python

```
from google import genai

client = genai.Client()

# Filter the Voice Library by language, gender, pitch, domain context, and keyword
response = client.voices.list(
    language_code=["en-US", "en-GB"],
    gender=["female"],
    pitch=["medium", "low"],
    contexts=["Audiobook", "Conversational"],
    type_=["prebuilt"],
    search="warm",
    page_size=50,
)

for voice in response.voices or []:
    print(
        f"{voice.id} | {voice.display_name} ({voice.language_code},"
        f" {voice.accent}, {voice.gender}, pitch={voice.pitch}):"
        f" {voice.description}"
    )
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// Filter the Voice Library by language, gender, pitch, domain context, and keyword
const response = await ai.voices.list({
  language_code: ["en-US", "en-GB"],
  gender: ["female"],
  pitch: ["medium", "low"],
  contexts: ["Audiobook", "Conversational"],
  type: ["prebuilt"],
  search: "warm",
  page_size: 50,
});

for (const voice of response.voices ?? []) {
  console.log(
    `${voice.id} | ${voice.display_name} (${voice.language_code}, ${voice.accent}, ${voice.gender}, pitch=${voice.pitch}): ${voice.description}`
  );
}
```

### REST

```
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB" \
  --data-urlencode "gender=female" \
  --data-urlencode "pitch=medium" \
  --data-urlencode "context=Audiobook" \
  --data-urlencode "type=prebuilt" \
  --data-urlencode "search=warm" \
  --data-urlencode "page_size=50"
```

## Langues disponibles

Les modèles TTS détectent automatiquement la langue d'entrée.
[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr) (`gemini-3.8-flash-tts`) est compatible avec **plus de 130 langues**, et [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fr) (`gemini-3.8-flash-lite-tts`) est compatible avec **plus de 100 langues** :

| Langue | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| Aceh (écriture arabe) | ✔️ | ✔️ |
| Afrikaans | ✔️ | ✔️ |
| Akan | ✔️ | ✔️ |
| Amharique | ✔️ | ✔️ |
| Arménien | ✔️ | ✔️ |
| Assamais | ✔️ | ✔️ |
| Awadhi | ✔️ | ✔️ |
| Balinais | ✔️ | ✔️ |
| Bengali | ✔️ | ✔️ |
| Banjar (écriture arabe) | ✔️ | — |
| Banjar (alphabet latin) | ✔️ | ✔️ |
| Bachkir | ✔️ | — |
| Basque | ✔️ | ✔️ |
| Belarusian | ✔️ | ✔️ |
| Bemba | ✔️ | — |
| Bhodjpouri | ✔️ | ✔️ |
| Bosniaque | ✔️ | ✔️ |
| Bouguis | ✔️ | ✔️ |
| Bulgare | ✔️ | ✔️ |
| Birman | ✔️ | — |
| Cantonais | ✔️ | ✔️ |
| Catalan | ✔️ | ✔️ |
| Cebuano | ✔️ | ✔️ |
| Sorani | ✔️ | ✔️ |
| Chhattisgarhi | ✔️ | ✔️ |
| Chinois (script Hans) | ✔️ | ✔️ |
| Chinois (script Hant) | ✔️ | ✔️ |
| Tatar de Crimée | ✔️ | — |
| Croate | ✔️ | ✔️ |
| Tchèque | ✔️ | ✔️ |
| Danois | ✔️ | ✔️ |
| Néerlandais | ✔️ | ✔️ |
| Dioula | ✔️ | — |
| Dzongkha | ✔️ | — |
| Arabe (Égypte) | ✔️ | ✔️ |
| Anglais | ✔️ | ✔️ |
| Estonien | ✔️ | ✔️ |
| Tagalog | ✔️ | ✔️ |
| Finnois | ✔️ | — |
| Français | ✔️ | ✔️ |
| Galicien | ✔️ | ✔️ |
| Ganda | ✔️ | ✔️ |
| Géorgien | ✔️ | ✔️ |
| Allemand | ✔️ | ✔️ |
| Grec | ✔️ | ✔️ |
| Guarani | ✔️ | — |
| Gujarati | ✔️ | ✔️ |
| Créole haïtien | ✔️ | ✔️ |
| Mongol khalkha | ✔️ | ✔️ |
| Haoussa | ✔️ | ✔️ |
| Hébreu | ✔️ | ✔️ |
| Hindi | ✔️ | ✔️ |
| Hongrois | ✔️ | ✔️ |
| Islandais | ✔️ | ✔️ |
| Igbo | ✔️ | — |
| Ilocano | ✔️ | ✔️ |
| Indonésien | ✔️ | ✔️ |
| Persan iranien | ✔️ | ✔️ |
| Italien | ✔️ | ✔️ |
| Japonais | ✔️ | ✔️ |
| Javanais | ✔️ | ✔️ |
| Kabyle | ✔️ | — |
| Kamba | ✔️ | ✔️ |
| Kannada | ✔️ | ✔️ |
| Cachemiri (écriture arabe) | ✔️ | ✔️ |
| Cachemiri (Devanagari) | ✔️ | ✔️ |
| Kazakh | ✔️ | ✔️ |
| Khmer | ✔️ | ✔️ |
| Kikuyu | ✔️ | ✔️ |
| Kinyarwanda | ✔️ | ✔️ |
| Kongo | ✔️ | ✔️ |
| Coréen | ✔️ | ✔️ |
| Kirghiz | ✔️ | ✔️ |
| Laotien | ✔️ | ✔️ |
| Latgalien | ✔️ | — |
| Lingala | ✔️ | ✔️ |
| Lituanien | ✔️ | — |
| Luxembourgeois | ✔️ | — |
| Macédonien | ✔️ | ✔️ |
| Magahi | ✔️ | ✔️ |
| Maithili | ✔️ | ✔️ |
| Malayalam | ✔️ | ✔️ |
| Maltais | ✔️ | ✔️ |
| Manipuri | ✔️ | ✔️ |
| Marathi | ✔️ | ✔️ |
| Minangkabau (écriture arabe) | ✔️ | ✔️ |
| Minangkabau (alphabet latin) | ✔️ | — |
| Mizo | ✔️ | ✔️ |
| Népalais (langue individuelle) | ✔️ | ✔️ |
| Peul du Nigeria | ✔️ | ✔️ |
| Azerbaïdjanais du Nord | ✔️ | ✔️ |
| Sotho du Nord | ✔️ | ✔️ |
| Ouzbek du Nord | ✔️ | ✔️ |
| Norvégien bokmål | ✔️ | ✔️ |
| Nynorsk (norvégien) | ✔️ | ✔️ |
| Chichewa | ✔️ | ✔️ |
| Occitan | ✔️ | — |
| Odia (langue individuelle) | ✔️ | ✔️ |
| Pangasinan | ✔️ | — |
| Perse (Afghanistan) | ✔️ | ✔️ |
| Polish | ✔️ | ✔️ |
| Portugais | ✔️ | ✔️ |
| Panjabi | ✔️ | ✔️ |
| Roumain | ✔️ | ✔️ |
| Russe | ✔️ | ✔️ |
| Santali | ✔️ | ✔️ |
| Serbe | ✔️ | ✔️ |
| Sindhî | ✔️ | — |
| Cingalais | ✔️ | ✔️ |
| Slovaque | ✔️ | ✔️ |
| Slovène | ✔️ | — |
| Somali | ✔️ | — |
| Azéri | ✔️ | ✔️ |
| Pachto du Sud | ✔️ | ✔️ |
| Sotho du Sud | ✔️ | — |
| Espagnol | ✔️ | ✔️ |
| Arabe standard (écriture arabe) | ✔️ | ✔️ |
| Arabe standard (alphabet latin) | ✔️ | ✔️ |
| Letton standard | ✔️ | ✔️ |
| Malais standard | ✔️ | ✔️ |
| Swahili (langue individuelle) | ✔️ | — |
| Swati | ✔️ | — |
| Suédois | ✔️ | — |
| Tadjik | ✔️ | — |
| Tamoul | ✔️ | ✔️ |
| Telugu | ✔️ | ✔️ |
| Thaï | ✔️ | — |
| Tigrinya | ✔️ | — |
| Tosque albanais | ✔️ | — |
| Turkish | ✔️ | ✔️ |
| Ouïghour | ✔️ | — |
| Vietnamien | ✔️ | ✔️ |

## Modèles compatibles

| Modèle | Locuteur unique | Plusieurs locuteurs | Conception de la voix | Réplication vocale |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fr) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Preview Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=fr) | ✔️ | ✔️ | — | — |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=fr) | ✔️ | ✔️ | — | — |

### Quand utiliser quel modèle

Les deux modèles TTS Gemini 3.8 partagent exactement le même schéma d'API et le même format d'invite, ce qui vous permet de passer de l'un à l'autre en modifiant un seul paramètre :

- **Utilisez [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr)
  (`gemini-3.8-flash-tts`)** lorsque la fidélité acoustique maximale, le jeu nuancé
  et le contrôle expressif sont prioritaires. Il est idéal pour les travaux créatifs de qualité studio, les dialogues complexes à plusieurs locuteurs, les tags vocaux lourds, les prononciations difficiles, les dialectes régionaux ou minoritaires, et les narrations longues nécessitant une stabilité vocale et de ton de pièce à toute épreuve.
- **Utilisez [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fr)
  (`gemini-3.8-flash-lite-tts`)** comme solution de remplacement rapide et économique pour `gemini-3.1-flash-tts-preview`. Il est optimisé pour la production en masse à grand volume, les cascades d'agents vocaux conversationnels, les fonctionnalités de lecture à voix haute, la réplication vocale fiable et la parole quotidienne à un seul locuteur dans les principales langues.

### Guide de migration

Si vous migrez des modèles Gemini TTS `gemini-3.1-flash-tts-preview` ou antérieurs vers Gemini 3.8 TTS :

1. **Déplacez les instructions au niveau des tours dans `speech_metadata`** : Gemini 3.8 TTS traite le texte saisi strictement comme une transcription mot pour mot. Déplacez les instructions de diffusion continue (`style`, telles que `"whispering"`, `"out of breath"` ou `"speaking slowly"`) et les identifiants des intervenants (`speaker`) dans des annotations structurées `speech_metadata` plutôt que d'intégrer les mises en scène dans le texte de la transcription.
2. **N'utilisez les balises en ligne entre crochets que pour les événements vocaux ponctuels** : conservez les vocalisations et les pauses momentanées non liées à la parole en ligne dans la transcription à l'aide de crochets (par exemple, `<laugh>`, `<sigh>`, `<cough>`, `<breath>` ou `<short pause>`). Évitez les balises d'effets sonores (comme les applaudissements ou les bruits sourds) et placez les styles de diction dans `speech_metadata.style`.
3. **Spécifiez `speaker` à chaque tour dans les requêtes à plusieurs locuteurs** : chaque tour d'une requête à plusieurs locuteurs doit inclure explicitement `speaker` dans `speech_metadata` correspondant à l'un des locuteurs configurés.
4. **Concevez des personas en amont avec la conception vocale** : remplacez les blocs `"Audio Profile"` ou `"Director's Notes"` de plusieurs paragraphes par une voix personnalisée créée dans [Conception vocale](https://ai.google.dev/gemini-api/docs/voice-design?hl=fr), puis transmettez cet ID `voice_...` dans vos requêtes TTS avec des chaînes `style` minimales ou vides.
5. **Tenir compte de la sortie WAV par défaut (`audio/wav`) pour les requêtes unaires** : contrairement aux modèles TTS `gemini-3.1-flash-tts-preview` et antérieurs (qui renvoyaient par défaut un PCM brut `audio/l16` sans en-tête), Gemini 3.8 TTS renvoie par défaut un fichier audio WAV (`audio/wav`) avec un en-tête RIFF standard pour les requêtes unaires.
   - Si votre code encapsulait auparavant des octets PCM bruts dans un en-tête WAV (par exemple, à l'aide du module `wave` ou de `ffmpeg` de Python), supprimez l'encapsulation manuelle de l'en-tête et écrivez les octets renvoyés directement dans un fichier `.wav`.
   - Si votre pipeline nécessite un format audio PCM brut sans en-tête, mu-law ou A-law, définissez explicitement `response_format.mime_type` sur `"audio/l16"`, `"audio/mulaw"` ou `"audio/alaw"` (par exemple, `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}` dans l'API Interactions ou `AUDIO_L16` dans `generateContent`). Consultez [Formats de sortie audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr#audio-output-formats).

## Guide sur les requêtes

Les modèles Gemini 3.8 TTS traitent le texte saisi strictement comme une **transcription mot pour mot**.
Contrairement aux modèles d'aperçu précédents où les indications scéniques étaient intégrées en texte brut, Gemini 3.8 TTS sépare les indications de niveau tour soutenues (`speech_metadata`) des tags vocaux intégrés ponctuels.

### Champ "Style" et balises intégrées

Répartissez vos instructions de performances par portée :

- **Niveau de tour de parole (`speech_metadata.style`)** : placez les attributs de diffusion soutenue (comme l'émotion, la prosodie, le rythme général ou le style de diffusion, comme `"whispering"`, `"out of breath"`, `"muttering"` ou `"sarcastic"`) dans le champ `style` de `speech_metadata`. Pour créer un personnage et une performance stables tout au long des tours, concevez la persona à l'avance dans [Conception de la voix](https://ai.google.dev/gemini-api/docs/voice-design?hl=fr) et n'utilisez `style` que pour les ajustements facultatifs au niveau du tour.
- **Événements ponctuels (tags intégrés)** : insérez les brèves vocalises, respirations ou pauses non verbales dans la transcription à l'aide de crochets (`<cough>`, `<breath>`, `<sigh>`, `<short pause>`). Utilisez des crochets (`<...>`) pour obtenir la meilleure qualité audio possible et limitez-vous aux vocalises humaines plutôt qu'aux effets sonores non vocaux.

| Champ d'application | Où placer | Exemples |
| --- | --- | --- |
| **Au niveau du tour** (soutenu tout au long du tour) | `speech_metadata.style` | `"angry tone"`, `"speaking rapidly"`, `"out of breath"`, `"whispers"`, `"sarcastic"` |
| **À un moment précis** (se produit à un mot spécifique) | En ligne dans `text` (`<...>`) | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### Rythme et pauses

Vous pouvez contrôler le rythme et le silence à trois niveaux de précision :

- **Ponctuation et points de suspension** : utilisez des virgules, des tirets (`--`) et des points de suspension (`...`) pour simuler des hésitations naturelles.
- **Balises de pause intégrées** : insérez `<short pause>` ou `<long pause>` aux endroits exacts du script où l'orateur doit faire une pause :
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **Rythme au niveau du tour** : définissez `"style": "speaking rapidly"` ou `"style": "speaking slowly"` dans `speech_metadata` pour contrôler le débit vocal pour l'ensemble du tour.

### Prosodie et ton

Utilisez **`speech_metadata.style`** pour contrôler la prosodie, la hauteur et l'inflexion de la voix tout au long d'un tour de parole (par exemple, `"style": "high pitch, cheerful and excited inflection"` ou `"style": "monotone and flat"`). Si l'émotion ou la prosodie changent au milieu du dialogue, divisez le script en tours de parole distincts avec des valeurs `style` différentes pour chacun d'eux.

### Mise en valeur

Mettez en majuscules certains mots de la transcription, en les combinant avec de la ponctuation et des balises vocales intégrées, pour mettre l'accent sur les mots clés :

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### Exclamations et sons autres que la parole

Placez les vocalisations humaines non verbales sur la même ligne que le texte, en utilisant des chevrons (`<...>`) à l'endroit exact où le son doit se produire. Voici quelques exemples de tags vocaux recommandés :

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>`/`<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>`/`<laughter>` | `<moan>` | `<pant>` | `<pff>`/`<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>`/`<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>`/`<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### Canaux secondaires et chevauchement des voix

Dans un dialogue à plusieurs locuteurs, entourez les réactions de l'auditeur de barres verticales (`|reaction|`) à l'intérieur du tour de parole d'un locuteur pour créer des retours naturels ou un chevauchement de la parole sans créer un tour de parole distinct par réaction.

- **Échanges brefs en canal arrière** : insérez de brèves réactions de l'auditeur (`|oh hmm|`, `|oh really?|`, `|absolutely|`) dans le tour de parole de l'interlocuteur actif :
  - **Tour 1 (Locuteur A)** : `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **Tour 2 (Locuteur B)** : `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **Tour 3 (Intervenant A) :** `"Then let's ship it |absolutely| and watch the dashboards."`
- **Chevauchement et entrelacement de la parole** : utilisez plusieurs segments de barre verticale pour simuler la parole simultanée ou entrelacée entre deux locuteurs (fonctionne mieux avec `gemini-3.8-flash-tts`) :
  - **Compte à rebours/refrain simultanés** : `"Let's surprise him on three |ok| ready?"` suivi de `"one. two. three. |happy| happy |birthday| birthday!"`
  - **Chevauchement complet des intervenants** : `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### Cohérence entre les générations et ce qu'il faut éviter

Suivez ces consignes pour que l'identité vocale reste stable tout au long de la conversation :

- **Concevez des personas en amont dans la conception vocale au lieu de longs blocs de style** : les longs paragraphes `"Audio Profile"` et les listes à puces multiples `"Director's Notes"` hérités des modèles précédents sont la cause la plus fréquente de dérive vocale.
  Utilisez cette même intuition créative en amont dans la [conception vocale](https://ai.google.dev/gemini-api/docs/voice-design?hl=fr) pour générer une persona `voice_...` personnalisée persistante, puis transmettez cet ID vocal lors de vos appels TTS.
- **S'appuyer sur la référence vocale pour la stabilité (omettre les méta-instructions)** :
  Les modèles Gemini 3.8 TTS sont entraînés pour s'ancrer d'abord sur la référence audio.
  N'incluez pas d'instructions demandant au modèle de maintenir la voix stable (comme `"do not switch speaker identity"` ou `"maintain identical timbre"`). Un texte de requête supplémentaire augmente la dérive. Supprimez les instructions de style inutiles et laissez le modèle varier naturellement autour du point stable fourni par la référence vocale.
- **N'essayez pas de modifier les caractéristiques immuables du locuteur dans `style`** : évitez d'indiquer l'âge, le genre, les noms ou les changements d'accent permanents dans `speech_metadata.style`.
  Choisissez plutôt une voix régionale dans la bibliothèque vocale étendue ou créez-en une avec [Conception de voix](https://ai.google.dev/gemini-api/docs/voice-design?hl=fr).

### Workflow recommandé

1. **Créez le personnage une seule fois** : créez votre personnage dans [Conception de voix](https://ai.google.dev/gemini-api/docs/voice-design?hl=fr) ou sélectionnez une voix régionale dans la bibliothèque de voix étendue qui correspond à votre langue cible et à votre persona.
2. **Rédigez des transcriptions naturelles avec des hésitations** : pour un naturel maximal, rédigez le `text` comme une véritable transcription orale, y compris les hésitations et les disfluences naturelles (par exemple, `"Oh uh yeah I think... hm, so that's interesting"`).
3. **Testez d'abord la synthèse vocale simple** : synthétisez votre transcription avec un champ `style` vide. La plupart des requêtes n'ont pas besoin d'instruction `style`.
4. **N'ajoutez des requêtes `style` courtes que pour les ajustements** : n'ajoutez une chaîne `style` concise (telle que `"casual, friendly"` ou `"muttering, then reassuring"`) que pour les tours qui nécessitent un ajustement de diffusion spécifique, et réutilisez cette chaîne courte exacte pour les tours lorsque vous souhaitez une base de référence cohérente.

### Agents vocaux et de dialogue multitours

Lorsque vous créez des agents vocaux conversationnels en temps réel ou des applications multitours :

- Effectuez **un appel TTS par tour** à mesure que les blocs de texte LLM arrivent.
- Laissez le `voice` configuré (`voice_...` prédéfini, conçu ou répliqué `voice_...` / `voicekey_...`) transmettre l'identité de l'interlocuteur à chaque tour de parole. N'envoyez jamais de persona de personnage long à chaque tour de parole.
- Laissez le champ `style` par tour vide ou envoyez une courte chaîne constante (comme `"casual, friendly"`) pour l'ensemble de la conversation.
- Divisez les longues réponses des agents en tours plus courts au lieu d'utiliser des consignes de style plus fortes.

## Limites

- Les modèles TTS acceptent les entrées textuelles uniquement et génèrent des sorties audio uniquement.
- La génération multilocuteur en une seule requête (`speech_config.speakers`) est compatible avec un maximum de deux locuteurs utilisant des voix prédéfinies. Pour combiner des voix personnalisées (`voice_...`) ou répliquées (`voice_...` / `voicekey_...`) dans un dialogue à plusieurs personnages, synthétisez le tour de parole de chaque locuteur individuellement.
  Étant donné que les requêtes unaires renvoient `audio/wav` avec un en-tête RIFF de 44 octets par défaut, demandez le PCM brut (`{"type": "audio", "mime_type": "audio/l16"}`) ou supprimez l'en-tête WAV de chaque tour avant de concaténer les trames audio PCM de 24 kHz.
- **Limites de stockage et TTL pour les voix personnalisées :**
  - **Voix avec état (`store=True`, incitées ou répliquées)** : maximum de **200 voix par projet** avec une **valeur TTL (Time To Live) d'un an**.
  - **Clés vocales sans état (`store=False`, `voicekey_...`)** : **TTL de 7 jours** (time-to-live).
- Consultez la section [Langues acceptées](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr#languages) pour connaître les langues disponibles.

## Étape suivante

- Créez des personas vocaux personnalisés à partir du langage naturel avec la [conception vocale](https://ai.google.dev/gemini-api/docs/voice-design?hl=fr).
- Répliquez la voix d'un locuteur existant dans la [réplication de voix](https://ai.google.dev/gemini-api/docs/voice-replication?hl=fr).
- Comparez les spécifications des modèles sur les pages [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr) et [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fr).
- Découvrez l'audio bidirectionnel interactif avec l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/02 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/02 (UTC)."],[],[]]
