---
source_url: https://ai.google.dev/gemini-api/docs/interactions/music-generation?hl=es-419
fetched_at: 2026-06-01T19:43:02.996537+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Genera música con Lyria 3

Lyria 3 es la familia de modelos de generación de música de Google, disponible a través de la API de Gemini. Con Lyria 3, puedes generar audio estéreo de alta calidad a 44.1 kHz a partir de instrucciones de texto o imágenes. Estos modelos ofrecen coherencia estructural, incluidas las voces, las letras sincronizadas y los arreglos instrumentales completos.

La familia Lyria 3 incluye dos modelos:

| Modelo | ID de modelo | Ideal para | Duración | Salida |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Clips cortos, bucles y adelantos | 30 segundos | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | Canciones completas con versos, estribillos y puentes | Unos minutos (se puede controlar con la instrucción) | MP3 |

Ambos modelos se pueden usar con la nueva [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419), que admite entradas multimodales (texto e imágenes) y produce audio **estéreo de alta fidelidad de 44.1 kHz**.

## Genera un clip musical

El modelo Lyria 3 Clip siempre genera un clip de **30 segundos**. Para generar un clip, llama al método `interactions.create` con una instrucción de texto. La respuesta siempre incluye la letra y la estructura de la canción generadas junto con el audio en el esquema `steps`.

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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "Api-Revision: 2026-05-20" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

Puedes recuperar los datos de música generados con la propiedad `interaction.output_audio`, que devuelve el último bloque de audio generado. También puedes recuperar la letra y la estructura de la canción con la propiedad `interaction.output_text`. Para obtener detalles sobre las propiedades de conveniencia, consulta la [descripción general de las interacciones](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419#convenience-properties).

## Genera una canción completa

Usa el modelo `lyria-3-pro-preview` para generar canciones de larga duración que duren un par de minutos. El modelo Pro comprende la estructura musical y puede crear composiciones con versos, estribillos y puentes distintos. Puedes influir en la duración especificándola en la instrucción (p.ej., "Crea una canción de 2 minutos") o usando [marcas de tiempo](#timing) para definir la estructura.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "Api-Revision: 2026-05-20" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## Selecciona el formato de salida

De forma predeterminada, los modelos de Lyria 3 generan audio en formato **MP3**. En el caso de Lyria 3 Pro, también puedes solicitar el resultado en formato **WAV** configurando `response_format`.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## Analiza la respuesta

La respuesta de Lyria 3 contiene varios bloques de contenido dentro del esquema `steps`.
Las interacciones devuelven una secuencia de pasos, en la que los pasos `model_output` contienen el contenido generado.
Los bloques de contenido de texto contienen la letra generada o una descripción en JSON de la estructura de la canción.
Los bloques de contenido con el tipo `audio` contienen los datos de audio codificados en Base64.

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

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### Letras y música intercaladas

Dado que el resultado de Lyria 3 es complejo y contiene pasos y bloques separados para las letras generadas (texto) y la canción en sí (audio), las propiedades de conveniencia ofrecen un atajo rápido y recomendado.

Sin embargo, si deseas tener un control programático completo sobre la línea de tiempo sin procesar de los pasos que devuelve el servidor (por ejemplo, registrar bloques de contenido individuales a medida que se reciben), puedes iterar manualmente sobre `steps`:

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

## Genera música a partir de imágenes

Lyria 3 admite entradas multimodales: puedes proporcionar hasta **10 imágenes** junto con tu instrucción de texto en la lista de `input`, y el modelo compondrá música inspirada en el contenido visual.

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3-pro-preview",
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
    model: "lyria-3-pro-preview",
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

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

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

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
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
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

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

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
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
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## Genera pistas instrumentales

Para la música de fondo, las bandas sonoras de juegos o cualquier caso de uso en el que no se requieran voces, puedes indicarle al modelo que produzca pistas solo instrumentales:

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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## Genera música en diferentes idiomas

Lyria 3 genera letras en el idioma de tu instrucción. Para generar una canción con letra en francés, escribe la instrucción en ese idioma. El modelo adapta su estilo vocal y pronunciación para que coincidan con el idioma.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## Inteligencia del modelo

Lyria 3 analiza el proceso de tu instrucción, en el que el modelo razona a través de la estructura musical (introducción, estrofa, coro, puente, etc.) según tu instrucción.
Esto sucede antes de que se genere el audio y garantiza la coherencia estructural y la musicalidad.

## Guía de instrucciones

Cuanto más específica sea la instrucción, mejores serán los resultados. Esto es lo que puedes incluir para guiar la generación:

- **Género**: Especifica un género o una combinación de géneros (p.ej., "hip hop lo-fi", "fusión de jazz", "orquestal cinematográfico").
- **Instrumentos**: Nombra instrumentos específicos (p.ej., "piano Fender Rhodes", "guitarra slide", "caja de ritmos TR-808").
- **BPM**: Establece el tempo (p.ej., "120 BPM", "tempo lento de alrededor de 70 BPM").
- **Tonalidad/Escala**: Especifica una tonalidad musical (p.ej., "en sol mayor", "re menor").
- **Estado de ánimo y atmósfera**: Usa adjetivos descriptivos (p.ej., "nostálgico", "agresivo", "etéreo", "soñador").
- **Estructura**: Usa etiquetas como `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]`, `[Outro]` o marcas de tiempo para controlar la progresión de la canción.
- **Duración**: El modelo de Clip siempre produce clips de 30 segundos. En el caso del modelo Pro, especifica la duración deseada en tu instrucción (p.ej., "crea una canción de 2 minutos") o usa marcas de tiempo para controlar la duración.

### Ejemplos de instrucciones

Estos son algunos ejemplos de instrucciones eficaces:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Prácticas recomendadas

- **Primero, itera con Clip.** Usa el modelo `lyria-3-clip-preview` más rápido para experimentar con instrucciones antes de generar una versión completa con `lyria-3-pro-preview`.
- **Sea específico.** Las instrucciones vagas producen resultados genéricos. Menciona los instrumentos, los BPM, la clave, el estado de ánimo y la estructura para obtener el mejor resultado.
- **Coincide con tu idioma.** Escribe la instrucción en el idioma en el que quieres que aparezca la letra.
- **Usa etiquetas de sección.** Las etiquetas `[Verse]`, `[Chorus]` y `[Bridge]` le brindan al modelo una estructura clara que debe seguir.
- **Separa la letra de las instrucciones.** Cuando proporciones letras personalizadas, sepáralas claramente de las instrucciones de dirección musical.

## Limitaciones

- **Seguridad**: Todos los mensajes se verifican con filtros de seguridad. Se bloquearán las instrucciones que activen los filtros. Esto incluye las instrucciones que solicitan voces de artistas específicos o la generación de letras protegidas por derechos de autor.
- **Marcas de agua**: Todo el audio generado incluye una [marca de agua de audio de SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=es-419) para su identificación. Esta marca de agua es imperceptible para el oído humano y no afecta la experiencia de escucha.
- **Edición en varios turnos**: La generación de música es un proceso de un solo turno.
  En la versión actual de Lyria 3, no se admite la edición iterativa ni el perfeccionamiento de un clip generado a través de múltiples instrucciones.
- **Duración**: El modelo de Clip siempre genera clips de 30 segundos. El modelo Pro genera canciones que duran un par de minutos. La duración exacta se puede determinar con la instrucción.
- **Determinismo**: Los resultados pueden variar entre llamadas, incluso con la misma instrucción.

## ¿Qué sigue?

- Consulta los [precios](https://ai.google.dev/gemini-api/docs/interactions/pricing?hl=es-419) de los modelos de Lyria 3.
- Prueba la [generación de música en tiempo real y por transmisión](https://ai.google.dev/gemini-api/docs/interactions/realtime-music-generation?hl=es-419) con Lyria RealTime.
- Generar conversaciones con varios oradores con los [modelos de TTS](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=es-419)
- Descubre cómo generar [imágenes](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=es-419) o [videos](https://ai.google.dev/gemini-api/docs/interactions/video?hl=es-419).
- Descubre cómo Gemini puede [comprender archivos de audio](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=es-419).
- Mantén una conversación en tiempo real con Gemini usando la [API de Live](https://ai.google.dev/gemini-api/docs/interactions/live?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-01 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-01 (UTC)"],[],[]]
