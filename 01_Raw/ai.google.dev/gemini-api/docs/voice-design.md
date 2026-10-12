---
source_url: https://ai.google.dev/gemini-api/docs/voice-design?hl=es-419
fetched_at: 2026-10-12T06:57:12.647109+00:00
title: "Dise\u00f1o de voz \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Diseño de voz

El diseño de voz te permite crear una personificación vocal persistente y completamente nueva a partir de una descripción en lenguaje natural con el extremo Voices de la API de Gemini (`POST /v1beta/voices`). En lugar de limitarte a voces prediseñadas o a grabar audio de referencia, puedes describir la edad, el timbre, el acento y la forma de hablar de un personaje, y recibir un ID de `voice_...` reutilizable que se guarda en tu proyecto.

La forma más rápida de diseñar, probar y realizar iteraciones en voces personalizadas es con el estudio interactivo **Voice Design** en [Google AI Studio](https://aistudio.google.com/generate-speech?hl=es-419). Puedes generar arquetipos personalizados a partir de instrucciones de texto, probarlos con muestras de secuencias de comandos y copiar el ID de `voice_...` resultante directamente en el código de la aplicación.

[Probar en Google AI Studio](https://aistudio.google.com/generate-speech?hl=es-419)

Tanto [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=es-419) (`gemini-3.8-flash-tts`) como [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=es-419) (`gemini-3.8-flash-lite-tts`) admiten el diseño de voz.

## Crea una voz diseñada

Usa el SDK de GenAI de Google (`google-genai` 2.25.0 o posterior / `@google/genai` 2.24.0 o posterior) o la API de REST para crear una voz personalizada a partir de una descripción de texto. En el caso de las voces de `"prompted"`, tanto `voices.create` (`CreateVoice`) como `voices.get` (`GetVoice`) devuelven un campo `sample_audio` de solo salida (`mime_type: "audio/wav"`, `data` codificado en base64) para que puedas escuchar de inmediato la voz generada:

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## Cómo funciona el diseño de voz

1. **Crea una voz guiada:** Llama a `voices.create` (`POST /v1beta/voices`) con `type="prompted"` y `store=True`.
2. **Recibe una vista previa persistente de `voice_id` y `sample_audio`:** La API genera la identidad vocal, la almacena en tu proyecto y devuelve un ID permanente (por ejemplo, `voice_abc123...`) junto con `sample_audio` (`mime_type: "audio/wav"`, `data` codificado en base64) que contiene el audio de vista previa generado para la voz.
3. **Sintetiza voz:** Pasa el `voice_id` en cualquier lugar donde se acepte un nombre de voz en tus solicitudes de síntesis.

## Sintetiza la voz con la voz que diseñaste

Una vez que hayas creado una voz, pasa su `id` (`voice_...`) a la API de Interactions para generar voz:

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
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "annotations": [{
                "type": "speech_metadata",
                "style": "reflective and awe-inspired",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": created_voice.id},
        ]
    },
)

with open("designed_voice.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash-tts",
  input: [{
    type: "user_input",
    content: [{
      type: "text",
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      annotations: [{
        type: "speech_metadata",
        style: "reflective and awe-inspired",
      }],
    }],
  }],
  response_format: { type: "audio" },
  generation_config: {
    speech_config: [
      { voice: createdVoice.id },
    ],
  },
});

fs.writeFileSync("designed_voice.wav", Buffer.from(interaction.output_audio.data, "base64"));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "annotations": [{
          "type": "speech_metadata",
          "style": "reflective and awe-inspired"
        }]
      }]
    }],
    "response_format": {"type": "audio"},
    "generation_config": {
      "speech_config": [
        {"voice": "voice_YOUR_DESIGNED_VOICE_ID"}
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

## Administra tus voces

Puedes enumerar, filtrar, inspeccionar y borrar tus voces almacenadas en cualquier momento con la API de Voices (consulta [Biblioteca de voces extendida y filtrado](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419#voice-library) para ver todos los parámetros de filtro).

- **Límites de almacenamiento y TTL:** Las voces con estado (`store=True`, compartidas entre las voces replicadas y las generadas a partir de instrucciones) tienen un límite de **200 voces por proyecto** y un **TTL de 1 año** (tiempo de actividad).
- **Disponibilidad de `sample_audio`:** `voices.create()` (`CreateVoice`) y `voices.get()` (`GetVoice`) completan `sample_audio` (`mime_type:
  "audio/wav"`, `data` codificado en base64) para las voces de `"prompted"`. Para que la lista sea liviana, `voices.list()` (`ListVoices`) omite `sample_audio` (y `sample_audio` no se establece para las voces `"replicated"` y `"prebuilt"`).

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Prácticas recomendadas para la creación de instrucciones para el diseño de voz

- **Coloca rasgos vocales permanentes en el diseño de voz, no en `style`:** Define características inmutables, como la edad, el género, el timbre, la textura vocal y el acento regional, cuando crees la voz en `voices.create`.
- **Reserva `speech_metadata.style` para la emoción situacional:** Una vez que se cree tu voz personalizada, usa instrucciones `style` cortas (por ejemplo, `"whispered urgently"` o `"cheerful and energetic"`) para dirigir la actuación paso a paso sin alterar la identidad principal del orador.
- **Sé específico y conciso:** Una descripción clara de 1 o 2 oraciones (como *"Una locutora deportiva enérgica y nítida de unos 30 años con un ligero acento del Medio Oeste"*) produce resultados más limpios y coherentes que los párrafos contradictorios o demasiado largos.

## ¿Qué sigue?

- Obtén información para replicar la voz de un orador existente en [Replicación de voz](https://ai.google.dev/gemini-api/docs/voice-replication?hl=es-419).
- Explora el diseño a nivel de turnos, las etiquetas intercaladas y el diálogo de varios oradores en la [guía de Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-24 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-24 (UTC)"],[],[]]
