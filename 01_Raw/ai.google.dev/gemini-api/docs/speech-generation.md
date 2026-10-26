---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=sq
fetched_at: 2026-10-26T05:59:26.669008+00:00
title: "Gjenerimi i tekstit n\u00eb ligj\u00ebrim (TTS) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs?hl=sq)

Dërgo komente

# Gjenerimi i tekstit në ligjërim (TTS)

Gemini API mund ta transformojë hyrjen me tekst në audio me një ose disa altoparlantë
duke përdorur aftësitë e gjenerimit të tekstit në ligjërim (TTS) të Gemini.
Gjenerimi i tekstit në ligjërim është
*[i kontrollueshëm](https://ai.google.dev/gemini-api/docs/speech-generation?hl=sq#controllable)*, që do të thotë se mund të kombinosh metadatat e strukturuara të radhës (`speech_metadata`) dhe etiketat zanore të integruara për të udhëzuar *stilin*, *theksin*, *ritmin* dhe *tonin* e audios.

Aftësia e TTS-së ndryshon nga gjenerimi i ligjërimit që ofrohet nëpërmjet
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=sq), i cili është projektuar për hyrje dhe dalje ndërvepruese,
audio të pastrukturuar dhe multimodale. Ndërkohë që Live API është i shkëlqyer
në kontekste dinamike bisedore, TTS nëpërmjet Gemini API
është i personalizuar për skenarë që kërkojnë recitim të saktë të tekstit me kontroll
të detajuar mbi stilin dhe tingullin, si p.sh. gjenerimi i podkasteve ose librave me audio.

Ky udhëzues të tregon se si të gjenerosh audio me një folës të vetëm dhe me shumë folës nga teksti duke përdorur [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=sq)
(`gemini-3.8-flash-tts`) dhe
[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=sq)
(`gemini-3.8-flash-lite-tts`).

## Para se të fillosh

Sigurohu që të përdorësh një model Gemini TTS të listuar në seksionin [Modelet e mbështetura](https://ai.google.dev/gemini-api/docs/speech-generation?hl=sq#supported-models) dhe përmirësoje në SDK-në më të fundit të IA-së gjeneruese të Google (`google-genai >= 2.25.0` për Python ose `@google/genai >= 2.24.0` për JavaScript/TypeScript) ose përdor API-në REST.
Për rezultate optimale, rishiko
[Kur të përdorësh cilin model](https://ai.google.dev/gemini-api/docs/speech-generation?hl=sq#when-to-use-which-model)
për të zgjedhur modelin më të mirë për ngarkesën tënde të punës.

Mund të të duket e dobishme të
[testosh modelet TTS të Gemini në AI Studio](https://aistudio.google.com/generate-speech?hl=sq)
para se të fillosh të ndërtosh.

## TTS me një folës

Për të konvertuar tekstin në audio me një folës me modelet TTS të Gemini 3.8, kalo transkriptin tekstual në `input`, bashkëngjit stilimin në nivel radhe duke përdorur një shënim të `speech_metadata` dhe konfiguro zërin tënd në `generation_config.speech_config`. Mund të zgjedhësh një zë nga
[Opsionet e zërit](https://ai.google.dev/gemini-api/docs/speech-generation?hl=sq#voices) të integruara, biblioteka e zgjeruar e zërave (`GET /v1beta/voices`), një ID e personalizuar e
[Dizajnit të zërit](https://ai.google.dev/gemini-api/docs/voice-design?hl=sq) (`voice_...`) ose një ID e
[Kopjimit të zërit](https://ai.google.dev/gemini-api/docs/voice-replication?hl=sq) (`voice_...` ose `voicekey_...` opsionale pa gjendje).

Ky shembull ruan audion e parazgjedhur të daljes WAV (`audio/wav`) nga modeli drejtpërdrejt në një skedar:

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

### QETËSI

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

Në SDK-të e Python dhe JavaScript, mund t'i marrësh të dhënat e gjeneruara të audios duke përdorur karakteristikën e përshtatshme `interaction.output_audio`, e cila kthen bllokun e fundit të audios së gjeneruar (në përgjigjet e papërpunuara REST JSON, audioja e enkoduar me base64 ruhet në `steps[].content[].data`). Për detaje për karakteristikat e përshtatshme, shiko [Përmbledhjen e ndërveprimeve](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=sq#convenience-properties).

## TTS me shumë folës

Për dialogun me shumë altoparlantë, konfiguro dy altoparlantë në `speech_config.speakers` dhe kalo çdo radhë si një artikull të veçantë teksti me një shënim `speech_metadata` që specifikon `speaker` dhe `style` opsionale në nivel radhe. Ki parasysh se
`speech_config` pranon një grup (`[{"voice": "..."}]`) për gjenerimin me një altoparlant të vetëm dhe një objekt (`{"speakers": [...]}`) për gjenerimin me shumë altoparlantë:

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

## Kontrollo stilin e ligjërimit me metadatat dhe etiketat

Gemini 3.8 TTS e trajton fushën `text` në mënyrë strikte si një transkriptim fjalë për fjalë. Për të kontrolluar dërgimin pa pasur udhëzime skenike të lexuara me zë, ndaji udhëzimet e tua sipas fushëveprimit:

- **Dorëzimi i vazhdueshëm në nivel radhe (`speech_metadata.style`):** Vendos emocionet,
  stilin e dorëzimit, prozodinë, ritmin dhe volumin që zbatohen në të gjithë radhën
  në fushën `style` (për shembull, `"style": "whispered urgently"`,
  `"style": "out of breath"` ose `"style": "warm and enthusiastic"`).
- **Ngjarjet në një moment të caktuar (etiketat e integruara):** Vendos shpërthime ose pauza të përkohshme vokale jo të ligjërimit drejtpërdrejt brenda transkriptit duke përdorur kllapa këndore (për shembull, `"Wait... <short pause> did you hear that? <sigh>"` ose
  `"Excuse me <cough> as I was saying..."`).

Shiko [Udhëzuesin për kërkesat](https://ai.google.dev/gemini-api/docs/speech-generation?hl=sq#prompting-guide)
për praktikat më të mira gjithëpërfshirëse.

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
                "text": "Wait... <short pause> look under that fallen log! Is that a blue-spotted salamander?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Dr. Anya",
                    "style": "whispered urgently",
                }],
            },
            {
                "type": "text",
                "text": "<gasp> No way! <laugh> We've been searching for this species all season!",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Liam",
                    "style": "warm and enthusiastic",
                }],
            },
        ],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": {
            "speakers": [
                {"speaker": "Dr. Anya", "voice": "Kore"},
                {"speaker": "Liam", "voice": "Puck"},
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
               text: 'Wait... <short pause> look under that fallen log! Is that a blue-spotted salamander?',
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Dr. Anya',
                  style: 'whispered urgently',
               }],
            },
            {
               type: 'text',
               text: "<gasp> No way! <laugh> We've been searching for this species all season!",
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Liam',
                  style: 'warm and enthusiastic',
               }],
            },
         ],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: {
            speakers: [
               { speaker: 'Dr. Anya', voice: 'Kore' },
               { speaker: 'Liam', voice: 'Puck' },
            ],
         },
      },
   });

   if (interaction.output_audio?.data) {
      const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
      fs.writeFileSync('out.wav', audioBuffer);
   }
}

await main();
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
          "text": "Wait... <short pause> look under that fallen log! Is that a blue-spotted salamander?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Dr. Anya",
            "style": "whispered urgently"
          }]
        },
        {
          "type": "text",
          "text": "<gasp> No way! <laugh> We'\''ve been searching for this species all season!",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Liam",
            "style": "warm and enthusiastic"
          }]
        }
      ]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": {
        "speakers": [
          { "speaker": "Dr. Anya", "voice": "Kore" },
          { "speaker": "Liam", "voice": "Puck" }
        ]
      }
    }
  }'
```

## Gjenerimi i ligjërimit me transmetim

Mund ta transmetosh audion e gjeneruar ndërkohë që sintetizohet duke caktuar
`stream: true`. Ndryshe nga kërkesat unare (që kthejnë një skedar të plotë WAV me një kokë RIFF), **kërkesat e transmetimit kthejnë pjesë të papërpunuara të PCM linear 16-bitësh të nënshkruar me renditje të vogël (`audio/l16`, 24 kHz, mono) pa kokë si parazgjedhje** në mënyrë që pjesët e audios të mund të luhen ose të lidhen në mënyrë të vazhdueshme pa koka të kontejnerit.

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

## Formatet e daljes së audios

Modelet Gemini 3.8 TTS përdorin formate të ndryshme të parazgjedhura audio në varësi të faktit nëse kërkesa është unare apo transmetim:

- **Kërkesat unare (`stream=False`):** Kthe audio të plotë **WAV (`audio/wav`)**
  me një kokë standarde RIFF (24 kHz, mono, 16-bit signed little-endian
  PCM). Mund t'i ruash bajtet e audios së dekoduar drejtpërdrejt në një skedar `.wav` pa
  shtuar manualisht një kokë WAV.
- **Kërkesat për transmetim (`stream=True`):** Kthe pjesë **Linear PCM të papërpunuara pa kokë (`audio/l16`)** (24 kHz, mono, PCM 16-bitësh me shenjë me skaj të vogël) si parazgjedhje në mënyrë që pjesët të mund të transmetohen ose të bashkohen vazhdimisht pa koka kontejneri në çdo pjesë.

Për të kërkuar një enkodim ose shpejtësi kampionimi tjetër të audios, konfiguro `mime_type` dhe
`sample_rate` opsionale brenda `response_format`:

| Formati | Vlerë prej `mime_type` | Përshkrimi |
| --- | --- | --- |
| **WAV** *(unary default)* | `"audio/wav"` | Skedar WAV i pakompresuar me një kokë RIFF (PCM 16-bitësh i nënshkruar me endian të vogël, mono, parazgjedhje 24 kHz). Parazgjedhja për kërkesat unare. |
| **Raw PCM (L16)** *(parazgjedhja e transmetimit)* | `"audio/l16"` | Audio PCM lineare e pangjeshur, pa kokë, 16-bitëshe, e nënshkruar, me endian të vogël (24 kHz, mono). Parazgjedhje për kërkesat për transmetim. |
| **Mu-law** | `"audio/mulaw"` | Audio e enkoduar me mu-law G.711 8-bit (përdoret zakonisht në sistemet e telefonisë/IVR në Amerikën e Veriut dhe Japoni). |
| **Ligji A** | `"audio/alaw"` | Audio e enkoduar me ligjin A G.711 8-bitësh (përdoret zakonisht në sistemet telefonike evropiane dhe ndërkombëtare). |

Mund të specifikosh gjithashtu `sample_rate` në herc (për shembull, `24000`, `16000` ose
`8000`).

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

### QETËSI

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

## Opsionet e zërit

Teksti në ligjërim i Gemini 3.8 mbështet katër mënyra për të zgjedhur ose krijuar zëra:

1. **Zërat e parakonstruksionit të studios:** 30 zëra të kuruar të listuar në tabelën e mëposhtme.
2. **Biblioteka e zgjeruar e zërave:** Qindra zëra shtesë në gjuhë, thekse dhe arketipe të ndryshme personazhesh, të qasshme duke përdorur `client.voices.list()` (`GET /v1beta/voices`).
3. **[Dizajni i zërit](https://ai.google.dev/gemini-api/docs/voice-design?hl=sq):** Gjenero një personazh vokal të personalizuar nga një përshkrim në gjuhë natyrale në [Google AI Studio](https://aistudio.google.com/generate-speech?hl=sq) ose duke përdorur `POST /v1beta/voices` (`type="prompted"`, që kthen një ID të vazhdueshme të `voice_...` dhe një version paraprak WAV të `sample_audio` në `CreateVoice` dhe `GetVoice`).
4. **[Kopjimi i zërit](https://ai.google.dev/gemini-api/docs/voice-replication?hl=sq):** Kopjo zërin e një folësi nga audioja e referencës dhe e pëlqimit në [Google AI Studio](https://aistudio.google.com/generate-speech?hl=sq) ose duke përdorur `POST /v1beta/voices` (`type="replicated"`, `store=True` i vazhdueshëm si parazgjedhje ose `store=False` opsional pa gjendje).

### Kufijtë e zërit të personalizuar dhe TTL-ja

| Shkrimi me zë | Modaliteti i hapësirës ruajtëse | Kuota / kufiri | Ruajtja (TTL) |
| --- | --- | --- | --- |
| **Zërat me gjendje** (`voice_...`, të kërkuar ose të përsëritur) | `store=True` | **200 zëra për projekt** (të ndarë në zërat e kërkuar dhe të replikuar) | **1 vit nga përdorimi i fundit\*** |
| **Çelësat e zërit pa gjendje** (`voicekey_...`, të replikuar) | `store=False` | Menaxhuar nga klienti | **7 ditë** |

\* **Zgjatja e TTL-së:** Periudha e ruajtjes prej 1 viti rivendoset sa herë që zëri përdoret në mënyrë aktive (duke sintetizuar ligjërimin me zërin ose duke e përdorur atë si zë bazë për remiksimin). Zërat pa aktivitet për 1 vit fshihen automatikisht.

### Zërat e krijuar paraprakisht

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** -- *Upbeat* | **Charon** -- *Informative* |
| **Kore** -- *Firmë* | **Fenrir** -- *I emocionueshëm* | **Leda** -- *Youthful* |
| **Orus** -- *Firm* | **Aoede** -- *Breezy* | **Callirrhoe** -- *E lehtë* |
| **Autonoe** -- *Bright* | **Enceladus** -- *Me frymëmarrje* | **Iapetus** -- *Pastro* |
| **Umbriel** -- *I qetë* | **Algieba** -- *Smooth* | **Despina** -- *E lëmuar* |
| **Erinome** -- *Clear* | **Algenib** -- *Gravelly* | **Rasalgethi** -- *Informative* |
| **Laomedeia** -- *Upbeat* | **Achernar** -- *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *Për të rritur* | **Pulcherrima** -- *Përpara* |
| **Achird** -- *Miqësor* | **Zubenelgenubi** -- *Casual* | **Vindemiatrix** -- *I butë* |
| **Sadachbia** -- *Lively* | **Sadaltager** -- *I ditur* | **Sulafat** -- *Ngrohtë* |

### Biblioteka e zgjeruar e zërave dhe filtrimi

Përtej 30 zërave të paraqitur të studios në tabelën e mësipërme, **Biblioteka e zgjeruar e zërave** ofron qindra zëra shtesë në gjuhë, thekse rajonale, persona personazhesh dhe domene të ndryshme. Mund të shfletosh, filtrosh dhe
të dëgjosh bibliotekën e plotë të zërave në mënyrë ndërvepruese në
[Google AI Studio](https://aistudio.google.com/generate-speech?hl=sq) ose ta kërkosh atë
në mënyrë programatike duke përdorur `client.voices.list()` (`GET /v1beta/voices`, duke përdorur
`google-genai` 2.25.0+ / `@google/genai` 2.24.0+).

`ListVoices` kthen zërat e personalizuar të ruajtur (renditur nga më i riu i pari) të ndjekur nga zërat e katalogut të parakonstruksionit që përputhen me kriteret e filtrit. Kur kalohen disa vlera për një filtër liste, kthehen zërat që përputhen me **çdo** vlerë në atë filtër (`OR`), ndërsa parametrat e ndryshëm të filtrit kombinohen me `AND`:

| Parametri | Lloji | Përshkrimi |
| --- | --- | --- |
| `language_code` | `list[str]` | Etiketat e gjuhës BCP-47 (për shembull, `["en-US", "en-GB"]`). Përputhje e saktë pa dallim mes gërmave të vogla dhe të mëdha. |
| `region_code` | `list[str]` | Kodet e rajoneve ISO 3166-1 alpha-2 ose UN M.49 (për shembull, `["US", "GB"]`). |
| `accent` | `list[str]` | Përshkruesit e theksit rajonal (për shembull, `["American", "British"]`). |
| `gender` | `list[str]` | Prezantimi i gjinisë së perceptuar (`"female"`, `"male"` ose `"neutral"`). |
| `pitch` | `list[str]` | Klasifikimi i lartësisë së zërit (`"low"`, `"medium"` ose `"high"`). |
| `persona` | `list[str]` | Personazhi vokal ose arketipi i personazhit (për shembull, `["Warm, Friendly"]`, `["Narrator"]`). |
| `contexts` (`context` në REST) | `list[str]` | Domeni i përdorimit optimal (për shembull, `["Audiobook", "Conversational", "News"]`). |
| `type` (`type_` në Python) | `list[str]` | Filtro sipas burimit të zërit: `"prebuilt"`, `"prompted"` ([Dizajni i zërit](https://ai.google.dev/gemini-api/docs/voice-design?hl=sq)) ose `"replicated"` ([Kopjimi i zërit](https://ai.google.dev/gemini-api/docs/voice-replication?hl=sq)). |
| `search` | `str` | Kërkimi i nënvargut të tekstit pa pagesë përputhet pa dallim mes shkronjave të vogla dhe të mëdha me `display_name` dhe `description`. |
| `page_size` | `int` | Numri maksimal i zërave të kthyer për faqe (parazgjedhur `50`, maksimumi `1000`). |
| `page_token` | `str` | Token nga `response.next_page_token` për të marrë faqen tjetër të rezultateve. |

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

## Gjuhët e mbështetura

Modelet TTS zbulojnë automatikisht gjuhën e hyrjes.
[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=sq)
(`gemini-3.8-flash-tts`) mbështet **mbi 130 gjuhë** dhe
[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=sq)
(`gemini-3.8-flash-lite-tts`) mbështet **mbi 100 gjuhë**:

| Gjuha | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| Acenisht (shkrimi arab) | ✔️ | ✔️ |
| Afrikanisht | ✔️ | ✔️ |
| Akan | ✔️ | ✔️ |
| Amarikisht | ✔️ | ✔️ |
| Armenisht | ✔️ | ✔️ |
| Asamezisht | ✔️ | ✔️ |
| Avadisht | ✔️ | ✔️ |
| Balinezisht | ✔️ | ✔️ |
| bengalisht | ✔️ | ✔️ |
| Banxharisht (shkrimi arab) | ✔️ | — |
| Banxharisht (shkrimi latin) | ✔️ | ✔️ |
| Bashkirisht | ✔️ | — |
| Baskisht | ✔️ | ✔️ |
| Bjellorusisht | ✔️ | ✔️ |
| Bembisht | ✔️ | — |
| Boxhpurisht | ✔️ | ✔️ |
| Boshnjakisht | ✔️ | ✔️ |
| Buginez | ✔️ | ✔️ |
| Bullgarisht | ✔️ | ✔️ |
| Birmanisht | ✔️ | — |
| Kantonisht | ✔️ | ✔️ |
| Katalonisht | ✔️ | ✔️ |
| Sibuanoisht | ✔️ | ✔️ |
| Kurdishte qendrore | ✔️ | ✔️ |
| Çatisgarisht | ✔️ | ✔️ |
| Kinezisht (shkrimi Hans) | ✔️ | ✔️ |
| Kinezisht (shkrimi Hant) | ✔️ | ✔️ |
| Tatarisht (Krimea) | ✔️ | — |
| Kroatisht | ✔️ | ✔️ |
| Çekisht | ✔️ | ✔️ |
| Danisht | ✔️ | ✔️ |
| Holandisht | ✔️ | ✔️ |
| Diulaisht | ✔️ | — |
| Xhonkisht | ✔️ | — |
| Arabisht (egjiptiane) | ✔️ | ✔️ |
| Anglisht | ✔️ | ✔️ |
| Estonisht | ✔️ | ✔️ |
| Filipinisht | ✔️ | ✔️ |
| Finlandisht | ✔️ | — |
| Frëngjisht | ✔️ | ✔️ |
| Galicisht | ✔️ | ✔️ |
| Ganda | ✔️ | ✔️ |
| Gjeorgjisht | ✔️ | ✔️ |
| Gjermanisht | ✔️ | ✔️ |
| Greqisht | ✔️ | ✔️ |
| Guarani | ✔️ | — |
| Guxharatisht | ✔️ | ✔️ |
| Kreolishte haitiane | ✔️ | ✔️ |
| Mongolisht (Halh) | ✔️ | ✔️ |
| Hausisht | ✔️ | ✔️ |
| Hebraisht | ✔️ | ✔️ |
| Hindisht | ✔️ | ✔️ |
| Hungarisht | ✔️ | ✔️ |
| Islandisht | ✔️ | ✔️ |
| Igboisht | ✔️ | — |
| Ilokoisht | ✔️ | ✔️ |
| Indonezisht | ✔️ | ✔️ |
| Persisht iranian | ✔️ | ✔️ |
| Italisht | ✔️ | ✔️ |
| Japonisht | ✔️ | ✔️ |
| Javanisht | ✔️ | ✔️ |
| Kabilisht | ✔️ | — |
| Kambaisht | ✔️ | ✔️ |
| Kanadisht | ✔️ | ✔️ |
| Kashmirisht (shkrim arab) | ✔️ | ✔️ |
| Kashmirisht (shkrimi deva) | ✔️ | ✔️ |
| Kazakisht | ✔️ | ✔️ |
| Kmerisht | ✔️ | ✔️ |
| Kikujuisht | ✔️ | ✔️ |
| Kiniaruandisht | ✔️ | ✔️ |
| Kongo | ✔️ | ✔️ |
| Koreanisht | ✔️ | ✔️ |
| Kirgizisht | ✔️ | ✔️ |
| Laosisht | ✔️ | ✔️ |
| Latgalianisht | ✔️ | — |
| Lingala | ✔️ | ✔️ |
| Lituanisht | ✔️ | — |
| Luksemburgisht | ✔️ | — |
| Maqedonisht | ✔️ | ✔️ |
| Magahi | ✔️ | ✔️ |
| Maitilisht | ✔️ | ✔️ |
| Malajalamisht | ✔️ | ✔️ |
| Maltisht | ✔️ | ✔️ |
| Manipurisht | ✔️ | ✔️ |
| Maratisht | ✔️ | ✔️ |
| Minangkabau (shkrimi arab) | ✔️ | ✔️ |
| Minangkabau (shkrimi latin) | ✔️ | — |
| Mizoisht | ✔️ | ✔️ |
| Nepalisht (gjuhë individuale) | ✔️ | ✔️ |
| Fulfuldisht nigeriane | ✔️ | ✔️ |
| Azerbajxhanisht veriore | ✔️ | ✔️ |
| Sotoishte veriore | ✔️ | ✔️ |
| Uzbekishtja veriore | ✔️ | ✔️ |
| Norvegjisht bokmål | ✔️ | ✔️ |
| Norvegjishte nynorsk | ✔️ | ✔️ |
| Nianxhaisht | ✔️ | ✔️ |
| Oksitanisht | ✔️ | — |
| Odia (gjuhë individuale) | ✔️ | ✔️ |
| Pangasinanisht | ✔️ | — |
| Persisht (Afganistan) | ✔️ | ✔️ |
| Polonisht | ✔️ | ✔️ |
| Portugalisht | ✔️ | ✔️ |
| Punxhabi | ✔️ | ✔️ |
| Rumanisht | ✔️ | ✔️ |
| Rusisht | ✔️ | ✔️ |
| Santalisht | ✔️ | ✔️ |
| Serbisht | ✔️ | ✔️ |
| Si'ndi | ✔️ | — |
| Sinhalisht | ✔️ | ✔️ |
| Sllovakisht | ✔️ | ✔️ |
| Sllovenisht | ✔️ | — |
| Somalisht | ✔️ | — |
| Azerbajxhanishtja jugore | ✔️ | ✔️ |
| Pashtoishtja jugore | ✔️ | ✔️ |
| Sotoishte jugore | ✔️ | — |
| Spanjisht | ✔️ | ✔️ |
| Arabisht standarde (shkrim arab) | ✔️ | ✔️ |
| Arabisht standarde (shkrimi latin) | ✔️ | ✔️ |
| Letonisht standarde | ✔️ | ✔️ |
| Malajzisht standarde | ✔️ | ✔️ |
| Suahilisht (gjuhë individuale) | ✔️ | — |
| Suatisht | ✔️ | — |
| Suedisht | ✔️ | — |
| Taxhikisht | ✔️ | — |
| Tamilisht | ✔️ | ✔️ |
| Teluguisht | ✔️ | ✔️ |
| Tajlandisht | ✔️ | — |
| Tigrinja | ✔️ | — |
| Shqip toskërisht | ✔️ | — |
| Turqisht | ✔️ | ✔️ |
| Ujgurisht | ✔️ | — |
| Vietnamisht | ✔️ | ✔️ |

## Modelet e mbështetura

| Modeli | Një folës i vetëm | Me shumë altoparlantë | Dizajn për zërin | Kopjimi i zërit |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=sq) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=sq) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Versioni paraprak i Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=sq) | ✔️ | ✔️ | — | — |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=sq) | ✔️ | ✔️ | — | — |

### Kur të përdorësh cilin model

Të dy modelet Gemini 3.8 TTS ndajnë saktësisht të njëjtën skemë të API-së dhe format të kërkesave,
duke të të lejuar të kalosh nga njëri te tjetri me një ndryshim të vetëm parametri:

- **Përdor [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=sq)
  (`gemini-3.8-flash-tts`)** kur përparësi kryesore janë besnikëria maksimale akustike, interpretimi i nuancuar dhe kontrolli shprehës. Është ideal për punë krijuese të nivelit të studios, dialogë kompleksë me shumë folës, etiketa të rënda të shpërthimeve vokale, shqiptime të vështira, dialekte rajonale ose të pakicave dhe rrëfime të gjata që kërkojnë zë të qëndrueshëm dhe qëndrueshmëri të tonit të dhomës.
- **Përdor [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=sq)
  (`gemini-3.8-flash-lite-tts`)** si zëvendësimin tënd të shpejtë dhe kosto-efektiv për `gemini-3.1-flash-tts-preview`. Ai është i optimizuar për prodhim në masë me volum të lartë, kaskada agjentësh zanorë bisedorë, veçori të leximit me zë, kopjim të besueshëm të zërit dhe ligjërim të përditshëm me një folës në gjuhët kryesore.

### Udhëzuesi i migrimit

Nëse po migron nga modelet `gemini-3.1-flash-tts-preview` ose më të hershme të Gemini TTS
në Gemini 3.8 TTS:

1. **Transfero udhëzimet e nivelit të kthesës te `speech_metadata`:** Gemini 3.8 TTS i trajton tekstet hyrëse rreptësisht si transkript fjalë për fjalë. Zhvendos udhëzimet e vazhdueshme të dërgimit (`style` - si p.sh. `"whispering"`, `"out of breath"` ose `"speaking slowly"`) dhe etiketat e folësve (`speaker`) në shënime të strukturuara `speech_metadata` në vend që të integrosh udhëzimet e skenës në tekstin e transkriptit.
2. **Përdor etiketat e brendshme me kllapa këndore vetëm për ngjarjet vokale në një moment të caktuar:** Mbaji
   vokalizimet jo të folura të çastit dhe pauzat në transkript duke përdorur
   kllapat këndore (si p.sh. `<laugh>`, `<sigh>`, `<cough>`, `<breath>` ose
   `<short pause>`). Shmang etiketat e efekteve zanore (si p.sh. duartrokitjet ose zhurmat e mbytur) dhe
   vendosi stilet e thënies në `speech_metadata.style`.
3. **Specifiko `speaker` në çdo radhë në kërkesat me shumë folës:** Çdo radhë në një kërkesë me shumë folës duhet të përfshijë në mënyrë eksplicite `speaker` brenda `speech_metadata` që përputhet me një nga folësit e konfiguruar.
4. **Dizajno personazhet paraprakisht me "Dizajnin e zërit":** Zëvendëso blloqet me shumë paragrafe të `"Audio Profile"` ose `"Director's Notes"` me një zë të personalizuar të krijuar në [Dizajnin e zërit](https://ai.google.dev/gemini-api/docs/voice-design?hl=sq), më pas kaloje atë ID të `voice_...` nëpërmjet kërkesave të tua të TTS me vargje minimale ose bosh të `style`.
5. **Llogarit për WAV (`audio/wav`) të parazgjedhur në kërkesat unare:** Ndryshe nga
   `gemini-3.1-flash-tts-preview` dhe modelet e mëparshme TTS (të cilat kthenin
   PCM `audio/l16` të papërpunuar pa kokë si parazgjedhje), Gemini 3.8 TTS kthen audio WAV
   (`audio/wav`) me një kokë standarde RIFF si parazgjedhje për kërkesat unare.
   - Nëse kodi yt më parë mbështillte bajtet e papërpunuara PCM në një kokë WAV (për shembull, duke përdorur modulin `wave` të Python ose `ffmpeg`), hiq mbështjellësin manual të kokës dhe shkruaj bajtet e kthyera drejtpërdrejt në një skedar `.wav`.
   - Nëse kanali yt kërkon audio të papërpunuar PCM, mu-law ose A-law pa kokë,
     cakto në mënyrë eksplicite `response_format.mime_type` në `"audio/l16"`, `"audio/mulaw"` ose
     `"audio/alaw"` (për shembull, `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}`
     në Interactions API ose `AUDIO_L16` në `generateContent`). Shiko
     [Formatet e nxjerrjes së audios](https://ai.google.dev/gemini-api/docs/speech-generation?hl=sq#audio-output-formats).

## Udhëzuesi për kërkesat

Modelet TTS të Gemini 3.8 e trajtojnë tekstin hyrës në mënyrë strikte si një **transkript fjalë për fjalë**.
Ndryshe nga modelet e mëparshme të versionit paraprak ku udhëzimet e skenës ishin të integruara në tekst të thjeshtë,
Gemini 3.8 TTS ndan udhëzimet e vazhdueshme në nivel radhe (`speech_metadata`)
nga etiketat zanore të integruara në moment.

### Fusha e stilit kundrejt etiketave të ndërfutura

Ndaji udhëzimet e tua të performancës sipas fushëveprimit:

- **Dorëzimi në nivel radhe (`speech_metadata.style`):** Vendos atributet e dorëzimit të vazhdueshëm, si p.sh. emocionin, prozodinë, ritmin e përgjithshëm ose stilin e dorëzimit (si p.sh. `"whispering"`, `"out of breath"`, `"muttering"` ose `"sarcastic"`) në fushën `style` të `speech_metadata`. Për të krijuar një personazh dhe performancë të qëndrueshme nëpër radhë, dizajno personazhin paraprakisht te [Dizajni i zërit](https://ai.google.dev/gemini-api/docs/voice-design?hl=sq) dhe përdor `style` vetëm për rregullime opsionale në nivel radhe.
- **Ngjarjet në një moment në kohë (etiketat në rresht):** Vendos shpërthime vokale të çastit që nuk janë të folura, frymëmarrje ose pauza në rresht brenda transkriptit duke përdorur kllapa këndore (`<cough>`, `<breath>`, `<sigh>`, `<short pause>`). Përdor kllapa këndore (`<...>`) për cilësinë më të lartë të audios dhe përdor vokalizimet njerëzore në vend të efekteve zanore jovokale.

| Fushëveprimi | Ku ta vendosësh | Shembuj |
| --- | --- | --- |
| **Niveli i kthesës** (i mbajtur gjatë kthesës) | `speech_metadata.style` | `"angry tone"`, `"speaking rapidly"`, `"out of breath"`, `"whispers"`, `"sarcastic"` |
| **Pikë në kohë** (ndodh në një fjalë specifike) | Në linjë në `text` (`<...>`) | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### Ritmi dhe pauzat

Mund të kontrollosh ritmin dhe heshtjen në tri nivele të granularitetit:

- **Shenjat e pikësimit dhe elipsat:** Përdor presjet, vizat (`--`) dhe elipsat (`...`)
  për hezitim të natyrshëm bisedor.
- **Etiketat e ndërprerjes së rreshtit:** Fut `<short pause>` ose `<long pause>` në pikat e sakta në skript ku folësi duhet të ndalojë:
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **Ritmi i nivelit të radhës:** Cakto `"style": "speaking rapidly"` ose
  `"style": "speaking slowly"` në `speech_metadata` për të kontrolluar shpejtësinë e të folurit në të gjithë radhën.

### Prozodia dhe tonaliteti

Përdor **`speech_metadata.style`** për të kontrolluar prozodinë, lartësinë e zërit dhe lakimin gjatë një radhe (për shembull, `"style": "high pitch, cheerful and excited inflection"` ose `"style": "monotone and flat"`). Nëse emocioni ose prozodia ndryshon në mes të dialogut, ndaje skenarin në radhë të veçanta me vlera të dallueshme të `style` për çdo radhë.

### Theksimi

Shkruaj me shkronja të mëdha fjalë specifike në transkript, të kombinuara me shenjat e pikësimit dhe etiketat zanore të integruara, për të vendosur theksin natyral zanor në fjalët kyçe:

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### Shpërthime vokale dhe tinguj jo të ligjërimit

Vendos vokalizimet njerëzore jo të të folurit në rresht duke përdorur kllapat këndore (`<...>`) në
pikën e saktë ku duhet të ndodhë tingulli. Etiketat vokale të rekomanduara përfshijnë:

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>` / `<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>` / `<laughter>` | `<moan>` | `<pant>` | `<pff>` / `<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>` / `<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>` / `<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### Kanalet dytësore dhe ligjërimi i mbivendosur

Në dialogun me shumë folës, mbështilli reagimet e dëgjuesit me simbole tubi
(`|reaction|`) brenda radhës së një folësi për të krijuar reagime natyrale ose
mbivendosje të ligjërimit pa e ndarë në një radhë të veçantë për çdo reagim.

- **Shkëmbime të shkurtra të kanalit të pasmë:** Shtreso reagimet e shkurtra të dëgjuesit (`|oh hmm|`,
  `|oh really?|`, `|absolutely|`) brenda radhës së folësit aktiv:
  - **Radha 1 (Folësi A):** `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **Radha 2 (Folësi B):** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **Radha 3 (Folësi A):** `"Then let's ship it |absolutely| and watch the dashboards."`
- **Fjalimi i mbivendosur dhe i ndërthurur:** Përdor disa segmente tubash për të simuluar fjalimin e njëkohshëm ose të ndërthurur midis dy folësve (funksionon më mirë me `gemini-3.8-flash-tts`):
  - **Numërimi mbrapsht/refreni i njëkohshëm:** `"Let's surprise him on three |ok| ready?"` ndjekur nga `"one. two. three. |happy| happy |birthday| birthday!"`
  - **Mbivendosje e plotë e altoparlantit:** `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### Konsistenca në të gjitha gjenerimet dhe çfarë duhet të shmangësh

Ndiq këto udhëzime për ta mbajtur identitetin vokal të qëndrueshëm gjatë ndërveprimeve:

- **Dizajno personazhet paraprakisht në "Dizajnin e zërit" në vend të blloqeve të gjata të stilit:**
  Paragrafët me formë të gjatë `"Audio Profile"` dhe me shumë pika `"Director's Notes"`
  të bartura nga modelet e mëparshme janë shkaku më i zakonshëm i devijimit të zërit.
  Përdor të njëjtin intuitë krijuese paraprakisht në
  [Dizajnin e zërit](https://ai.google.dev/gemini-api/docs/voice-design?hl=sq) për të gjeneruar një personazh të personalizuar
  të vazhdueshëm të `voice_...` dhe më pas kaloje atë ID të zërit nëpërmjet telefonatave të tua të TTS-së.
- **Mbështetu te referenca e zërit për qëndrueshmëri (hiq udhëzimet meta):**
  Modelet TTS të Gemini 3.8 janë trajnuar që të mbështeten fillimisht te referenca e audios.
  Mos përfshi udhëzime që i thonë modelit ta mbajë të qëndrueshme zërin (si `"do not switch speaker identity"` ose `"maintain identical timbre"`) - teksti shtesë i kërkesës rrit devijimin. Hiq udhëzimet e panevojshme për stilin dhe lejo që modeli të variojë në mënyrë natyrale rreth pikës së qëndrueshme të ofruar nga referenca zanore.
- **Mos u përpiq të ndryshosh tiparet e pandryshueshme të folësit në `style`:** Shmang vendosjen e moshës, gjinisë, emrave ose ndryshimeve të përhershme të theksit në `speech_metadata.style`.
  Në vend të kësaj, zgjidh një zë rajonal nga "Biblioteka e zgjeruar e zërave" ose krijo një të tillë me [Dizajnin e zërit](https://ai.google.dev/gemini-api/docs/voice-design?hl=sq).

### Fluksi i rekomanduar i punës

1. **Ndërto personazhin një herë:** Krijo personazhin tënd te
   [Dizajni i zërit](https://ai.google.dev/gemini-api/docs/voice-design?hl=sq) ose zgjidh një zë rajonal nga
   "Biblioteka e zgjeruar e zërave" që përputhet me gjuhën e synuar dhe personazhin tënd.
2. **Shkruaj transkripte të folura natyrale me pasiguri në të folur:** Për natyralitet maksimal, shkruaje `text` si një transkript të folur real - duke përfshirë pasiguri në të folur dhe hezitime natyrale në bisedë (për shembull, `"Oh uh yeah I think... hm, so that's interesting"`).
3. **Testo së pari TTS-në e thjeshtë:** Sintetizo transkriptin tënd me një fushë bosh `style`
   në fillim - shumica e kërkesave nuk kanë nevojë për asnjë udhëzim `style`.
4. **Shto vetëm kërkesa të shkurtra në `style` për modifikime:** Shto një varg të shkurtër `style` (si p.sh. `"casual, friendly"` ose `"muttering, then reassuring"`) vetëm për radhët që kanë nevojë për një rregullim specifik të paraqitjes dhe ripërdor atë varg të shkurtër të saktë nëpër radhë kur dëshiron një nivel bazë të qëndrueshëm.

### Agjentët e dialogut dhe zërit me shumë kthesa

Kur krijon agjentë zanorë bisedorë në kohë reale ose aplikacione me shumë kthesa:

- Bëj **një telefonatë TTS për çdo radhë** ndërkohë që vijnë pjesët e tekstit të LLM-së.
- Lejo që `voice` e konfiguruar (e parakonstruksionuar, e projektuar `voice_...` ose e replikuar
  `voice_...` / `voicekey_...`) të mbartë identitetin e folësit nëpër radhë - mos dërgo kurrë më një personazh të gjatë me karaktere në çdo radhë.
- Lëre bosh fushën `style` për radhë ose dërgo një varg të shkurtër konstant (si p.sh. `"casual, friendly"`) për të gjithë bisedën.
- Ndaji përgjigjet e gjata të agjentit në kthesa më të shkurtra në vend që të kërkosh kërkesa me stil më të fortë.

## Kufizimet

- Modelet TTS pranojnë vetëm hyrje me tekst dhe gjenerojnë vetëm dalje audio.
- Gjenerimi me shumë folës me një kërkesë të vetme (`speech_config.speakers`) mbështet deri në 2 folës duke përdorur zëra të parakonstruksionuar. Për të kombinuar zërat e personalizuar
  (`voice_...`) ose të replikuar (`voice_...` / `voicekey_...`) në dialogun me shumë personazhe, sintetizo radhën e çdo folësi në mënyrë individuale.
  Duke qenë se kërkesat unare kthejnë `audio/wav` me një kokë RIFF 44-bitëshe si parazgjedhje, kërko PCM të papërpunuar (`{"type": "audio", "mime_type": "audio/l16"}`) ose hiq kokën WAV nga çdo radhë para se të bashkosh kuadrot e audios PCM 24 kHz.
- **Kufijtë e personalizuar të hapësirës ruajtëse të zërit dhe TTL:**
  - **Zërat me gjendje (`store=True`, të kërkuar ose të replikuar):** Maksimumi prej
    **200 zërash për projekt** me një **TTL 1-vjeçare** (jetëgjatësia).
  - **Çelësat zanorë pa gjendje (`store=False`, `voicekey_...`):** **TTL 7-ditor**
    (time-to-live).
- Rishiko seksionin [Gjuhët e mbështetura](https://ai.google.dev/gemini-api/docs/speech-generation?hl=sq#languages)
  për mbulimin e gjuhëve.

## Çfarë ka më pas

- Krijo persona të personalizuar vokalë nga gjuha natyrale me
  [Dizajnin e zërit](https://ai.google.dev/gemini-api/docs/voice-design?hl=sq).
- Repliko zërin e një folësi ekzistues në
  [Kopjimi i zërit](https://ai.google.dev/gemini-api/docs/voice-replication?hl=sq).
- Krahaso specifikimet e modelit në faqet e modeleve
  [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=sq) dhe
  [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=sq).
- Eksploro audion interaktive dydrejtimëshe me
  [API-në e transmetimit të drejtpërdrejtë](https://ai.google.dev/gemini-api/docs/live?hl=sq).

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-12 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-12 UTC."],[],[]]
