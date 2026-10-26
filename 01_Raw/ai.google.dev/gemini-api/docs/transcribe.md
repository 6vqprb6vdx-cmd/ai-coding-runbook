---
source_url: https://ai.google.dev/gemini-api/docs/transcribe?hl=es-419
fetched_at: 2026-10-26T05:59:59.028558+00:00
title: "Transcripci\u00f3n de audio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Transcripción de audio

La API de Gemini convierte el habla de los archivos de audio en texto con el modelo Gemini 3.5 Transcribe (`gemini-3.5-transcribe`). Gracias a las capacidades de comprensión de audio de Gemini, ofrece una transcripción precisa con identificación automática del idioma, segmentación por orador, marcas de tiempo a nivel de palabras y sugerencias de vocabulario personalizadas. También proporciona un modo de [transcripción inteligente](#transcription-modes) que incluye la eliminación de las vacilaciones y el formato inteligente.

Para transcribir un archivo de audio, sube el audio y pásalo a `gemini-3.5-transcribe`:

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const audioFile = await client.files.upload({
  file: "path/to/sample.mp3",
  config: { mime_type: "audio/mp3" },
});

const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
});

console.log(interaction.output_text);
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

## Descripción general

Gemini 3.5 Transcribe está optimizado para tareas de voz a texto. Maneja diversos acentos, ruido de fondo y conversaciones en varios idiomas.

Las siguientes son algunas de las funciones clave:

- **Reconocimiento de voz automático (ASR):** Detecta automáticamente idiomas en más de [85 configuraciones regionales](#supported-languages). Maneja el cambio de código dentro de una oración y entre oraciones sin configuración manual.
- **Vocabulario personalizado:** Incluye hasta 1,000 frases para sesgar el reconocimiento hacia términos específicos del dominio, acrónimos y nombres propios.
- **Identificación de interlocutores:** Distingue entre varios interlocutores y atribuye segmentos hablados a etiquetas distintas.
- **Marcas de tiempo a nivel de la palabra:** Genera compensaciones de tiempo de inicio y finalización precisas para cada palabra reconocida.
- **Transcripción inteligente:** Elimina las disfluencias, las muletillas y las repeticiones, y aplica un formato estructurado.
- **Formato y normalización:** Aplica el uso de mayúsculas, la puntuación y la normalización inversa del texto, como convertir "veintiséis millones de dólares" a "USD 26 M".

Para el razonamiento de audio general o la búsqueda de respuestas sobre contenido de audio, usa [Comprensión de audio](https://ai.google.dev/gemini-api/docs/audio?hl=es-419). Para la síntesis de audio de texto a voz, usa [Text-to-speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419).

## Sugerencias y detección de idioma

De forma predeterminada, el modelo detecta automáticamente el idioma hablado. Cambia de idioma de forma dinámica cuando los oradores cambian de código.

Para usar la detección automática, omite `language_codes` o proporciona una lista vacía:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "language_codes": [],
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      language_codes: [],
    },
  },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    LanguageCodes: []string{},
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "language_codes": []
      }
    }
  }'
```

Si conoces el idioma de antemano, especifica los códigos de idioma BCP-47 en `language_codes` para mejorar la precisión de la transcripción (consulta [Idiomas admitidos](#supported-languages)):

### Python

```
generation_config = {
    "transcription_config": {
        "language_codes": ["es-ES"],
    }
}
```

### JavaScript

```
const generationConfig = {
  transcription_config: {
    language_codes: ["es-ES"],
  },
};
```

### Go

```
package main

import (
    "google.golang.org/genai/interactions/models/interactions"
)

func main() {
    generationConfig := &interactions.GenerationConfig{
        TranscriptionConfig: &interactions.TranscriptionConfig{
            LanguageCodes: []string{"es-ES"},
        },
    }
    _ = generationConfig
}
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "language_codes": ["es-ES"]
    }
  }
}
```

## Vocabulario personalizado

Puedes dirigir el modelo de voz hacia palabras poco comunes, jerga técnica, nombres de marcas o nombres propios. Proporciona hasta 1,000 términos en el array `custom_vocabulary` (por lo general, se obtienen los mejores resultados con hasta 100 términos):

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"],
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      custom_vocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    CustomVocabulary: []string{"Gemini", "Kubernetes", "BigQuery"},
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## Identificación de interlocutores

La identificación de interlocutores identifica las diferentes voces en la grabación y etiqueta cada segmento con un identificador de interlocutor, como `spk_1` o `spk_2`. Se admiten hasta 8 oradores (la atribución para 3 o más oradores es experimental).

Para habilitar la identificación del interlocutor, configura `diarization_mode` dentro de `mode`:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "diarization_mode": "speaker",
            },
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        diarization_mode: "speaker",
      },
    },
  },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.NewTranscriptionMode(interactions.VerbatimTranscriptionMode{
                        DiarizationMode: genai.Ptr("speaker"),
                    }))),
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "diarization_mode": "speaker"
        }
      }
    }
  }'
```

## Marcas de tiempo a nivel de la palabra

Las marcas de tiempo a nivel de la palabra proporcionan compensaciones exactas de inicio y finalización para cada palabra reconocida en la transmisión de audio.

Para habilitar las marcas de tiempo, configura `timestamp_granularities` dentro de `mode`:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "timestamp_granularities": ["word"],
            },
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        timestamp_granularities: ["word"],
      },
    },
  },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.NewTranscriptionMode(interactions.VerbatimTranscriptionMode{
                        TimestampGranularities: []string{"word"},
                    }))),
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "timestamp_granularities": ["word"]
        }
      }
    }
  }'
```

Puedes combinar `diarization_mode` y `timestamp_granularities` en `mode` para recibir etiquetas de interlocutor y marcas de tiempo de palabras:

### Python

```
generation_config = {
    "transcription_config": {
        "mode": {
            "type": "verbatim",
            "diarization_mode": "speaker",
            "timestamp_granularities": ["word"],
        },
    }
}
```

### JavaScript

```
const generationConfig = {
  transcription_config: {
    mode: {
      type: "verbatim",
      diarization_mode: "speaker",
      timestamp_granularities: ["word"],
    },
  },
};
```

### Go

```
package main

import (
    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
)

func main() {
    generationConfig := &interactions.GenerationConfig{
        TranscriptionConfig: &interactions.TranscriptionConfig{
            Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.NewTranscriptionMode(interactions.VerbatimTranscriptionMode{
                DiarizationMode:        genai.Ptr("speaker"),
                TimestampGranularities: []string{"word"},
            }))),
        },
    }
    _ = generationConfig
}
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "mode": {
        "type": "verbatim",
        "diarization_mode": "speaker",
        "timestamp_granularities": ["word"]
      }
    }
  }
}
```

## Modos de transcripción

Gemini 3.5 Transcribe admite dos modos de transcripción a través del parámetro `mode`:

- **`verbatim` (predeterminado)**: Devuelve una transcripción exacta palabra por palabra de todo lo que se dice, y conserva las palabras de relleno sin procesar (“eh”, “um”, “como”, “sabes”), las repeticiones, las pausas y los comienzos en falso. Las marcas de tiempo y la identificación de interlocutores se configuran en este modo (`{"type": "verbatim", ...}`).
- **`smart` (Transcripción inteligente)**: Optimiza la transcripción para su lectura aplicando un procesamiento posterior inteligente:
  - **Eliminación de disfluencias**: Elimina las palabras de relleno, los tartamudeos y los inicios en falso de las conversaciones.
  - **Autocorrecciones intercaladas**: Resuelve las correcciones habladas directamente (por ejemplo, *"Reunámonos el martes, no, el miércoles a las dos"* se convierte en *"Reunámonos el miércoles a las 2 p.m."*).
  - **Formato estructurado automático**: Estructura automáticamente los pensamientos hablados en párrafos, listas numeradas, viñetas, fechas con formato, monedas y números.
  - **Limpieza gramatical**: Aplica puntuación, uso de mayúsculas y minúsculas y flujo naturales.

| Audio hablado | Resultado de `verbatim` | Salida de `smart` (transcripción inteligente) |
| --- | --- | --- |
| "Eh, entonces, para la reunión, creo que deberíamos, eh, invitar a Alice y, no, espera, a Bob y Carol". | "Eh, para la reunión, creo que deberíamos invitar a Alicia, no, a Roberto y a Carolina". | "Para la reunión, creo que deberíamos invitar a Bob y a Carol". |
| "Revisar el primer elemento, finalizar el segundo elemento, enviar el resumen del tercer elemento" | "revisar el primer elemento, presupuestar el segundo elemento, finalizar el cronograma, enviar el resumen" | "1. Revisa el presupuesto 2. Finaliza la línea de tiempo 3. Enviar un resumen" |

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": "smart",
        }
    },
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: "smart",
    },
  },
});
console.log(interaction.output_text);
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.TranscriptionConfigModeEnumSmart)),
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": "smart"
      }
    }
  }'
```

## Cómo analizar el resultado de la transcripción

El texto completo de la transcripción se devuelve en `interaction.output_text`.

Cuando se habilitan `timestamp_granularities` o `diarization_mode`, la API también devuelve anotaciones detalladas a nivel de la palabra adjuntas al contenido de la interacción.

A continuación, se explica cómo extraer las marcas de tiempo de las palabras y los turnos de los oradores, y cómo iterar sobre ellos:

### Python

```
def extract_word_annotations(interaction):
    words = []
    for step in getattr(interaction, "steps", []) or []:
        for content in getattr(step, "content", []) or []:
            for annotation in getattr(content, "annotations", []) or []:
                if getattr(annotation, "type", None) == "word_info":
                    words.append(annotation)
    return words

words = extract_word_annotations(interaction)

for w in words:
    speaker = f"[{w.speaker}] " if getattr(w, "speaker", None) else ""
    start = getattr(w, "start_offset", "")
    end = getattr(w, "end_offset", "")
    timing = f"({start} -> {end}) " if start and end else ""
    print(f"{speaker}{timing}{w.text}")
```

### JavaScript

```
function extractWordAnnotations(interaction) {
  const words = [];
  for (const step of interaction.steps ?? []) {
    for (const content of step.content ?? []) {
      for (const annotation of content.annotations ?? []) {
        if (annotation.type === "word_info") {
          words.push(annotation);
        }
      }
    }
  }
  return words;
}

const words = extractWordAnnotations(interaction);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.start_offset && w.end_offset) ? `(${w.start_offset} -> ${w.end_offset}) ` : "";
  console.log(`${speaker}${timing}${w.text}`);
}
```

### Go

```
package main

import (
    "fmt"

    "google.golang.org/genai/interactions/models/interactions"
)

func extractWordAnnotations(interaction *interactions.Interaction) []*interactions.WordInfo {
    var words []*interactions.WordInfo
    if interaction == nil {
        return words
    }
    for _, step := range interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    for _, annotation := range content.TextContent.Annotations {
                        if annotation.WordInfo != nil {
                            words = append(words, annotation.WordInfo)
                        }
                    }
                }
            }
        }
    }
    return words
}

func main() {
    var interaction *interactions.Interaction
    words := extractWordAnnotations(interaction)

    for _, w := range words {
        speaker := ""
        if w.Speaker != nil && *w.Speaker != "" {
            speaker = fmt.Sprintf("[%s] ", *w.Speaker)
        }
        timing := ""
        if w.StartOffset != nil && w.EndOffset != nil {
            timing = fmt.Sprintf("(%s -> %s) ", *w.StartOffset, *w.EndOffset)
        }
        fmt.Printf("%s%s%s\n", speaker, timing, w.GetText())
    }
}
```

### REST

```
{
  "id": "interactions/abc123xyz",
  "status": "completed",
  "steps": [
    {
      "id": "step_001",
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Hello world",
          "annotations": [
            {
              "type": "word_info",
              "text": "Hello",
              "speaker": "spk_1",
              "start_offset": "0.100s",
              "end_offset": "0.400s"
            },
            {
              "type": "word_info",
              "text": "world",
              "speaker": "spk_1",
              "start_offset": "0.500s",
              "end_offset": "0.800s"
            }
          ]
        }
      ]
    }
  ]
}
```

## Idiomas admitidos

Los siguientes idiomas y códigos de idioma BCP-47 son compatibles con Gemini 3.5 Transcribe:

| Idioma | Código BCP-47 | Idioma | Código BCP-47 |
| --- | --- | --- | --- |
| Afrikaans | `af-ZA` | Japonés | `ja-JP` |
| Amárico | `am-ET` | Javanés | `jv-ID` |
| Árabe (Egipto) | `ar-EG` | Kabuverdianu | `kea-CV` |
| Armenio | `hy-AM` | Canarés | `kn-IN` |
| Asamés | `as-IN` | Kazajo | `kk-KZ` |
| Azerí | `az-AZ` | Coreano | `ko-KR` |
| Bielorruso | `be-BY` | Kirguís | `ky-KG` |
| Bengalí (Bangladés) | `bn-BD` | Letón | `lv-LV` |
| Bengalí (India) | `bn-IN` | Lingala | `ln-CD` |
| Bosnio | `bs-BA` | Lituano | `lt-LT` |
| Búlgaro | `bg-BG` | Macedonio | `mk-MK` |
| Búlgaro (arromano) | `rup-BG` | Malayo | `ms-MY` |
| Birmano | `my-MM` | Malayalam | `ml-IN` |
| Cantonés (tradicional) | `yue-Hant-HK` | Maltés | `mt-MT` |
| Catalán | `ca-ES` | Chino mandarín (simplificado) | `cmn-Hans-CN` |
| Cebuano | `ceb` | Maratí | `mr-IN` |
| Camboyano | `km-KH` | Mongol | `mn-MN` |
| Croata | `hr-HR` | Nepalí | `ne-NP` |
| Checo | `cs-CZ` | Noruego | `nb-NO` |
| Danés | `da-DK` | Oriya | `or-IN` |
| Holandés | `nl-NL` | Polaco | `pl-PL` |
| Inglés (Gran Bretaña) | `en-GB` | Portugués (Brasil) | `pt-BR` |
| Inglés (India) | `en-IN` | Portugués (Portugal) | `pt-PT` |
| Inglés (Estados Unidos) | `en-US` | Punyabí | `pa-IN` |
| Estonio | `et-EE` | Panyabí (alfabeto gurmukhi) | `pa-Guru-IN` |
| Persa | `fa-IR` | Rumano | `ro-RO` |
| Filipino | `fil-PH` | Ruso | `ru-RU` |
| Finlandés | `fi-FI` | Serbio | `sr-RS` |
| Francés | `fr-FR` | Sindhi (alfabeto árabe) | `sd-Arab-IN` |
| Gallego | `gl-ES` | Eslovaco | `sk-SK` |
| Georgiano | `ka-GE` | Esloveno | `sl-SI` |
| Alemán | `de-DE` | Español (Latinoamérica) | `es-419` |
| Griego | `el-GR` | Español (Estados Unidos) | `es-US` |
| Gujarati | `gu-IN` | Suajili (Kenia) | `sw-KE` |
| Hausa | `ha-NG` | Sueco | `sv-SE` |
| Hebreo | `he-IL` | Tayiko | `tg-TJ` |
| Hindi | `hi-IN` | Telugu | `te-IN` |
| Húngaro | `hu-HU` | Tailandés | `th-TH` |
| Islandés | `is-IS` | Turco | `tr-TR` |
| tu idioma o tu país | `en-IN` | Ucraniano | `uk-UA` |
| Indonesio | `id-ID` | Uzbeko | `uz-UZ` |
| Italiano | `it-IT` | Vietnamita | `vi-VN` |

## Formatos de audio compatibles

Gemini 3.5 Transcribe admite los siguientes tipos de MIME de formato de audio:

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG - `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16: `audio/l16`
- Opus - `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM - `audio/webm`

Para obtener la lista completa de los tipos MIME y los esquemas de parámetros admitidos, consulta la [referencia de la API de Interactions](https://ai.google.dev/api/interactions-api?hl=es-419#Resource:Content).

## Referencia del parámetro

Configura la transcripción estableciendo campos dentro del objeto `transcription_config` en `generation_config`:

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `language_codes` | Arreglo de strings | Códigos de idioma BCP-47 (p.ej., `["en-US"]`). Si se omite o está vacío (`[]`), el modelo detecta automáticamente el idioma y controla el cambio de código. |
| `custom_vocabulary` | Arreglo de strings | Hasta 1,000 términos, acrónimos o nombres propios personalizados para sesgar el reconocimiento de voz No es compatible con la identificación de interlocutores ni con las marcas de tiempo a nivel de la palabra. |
| `mode` | Objeto o cadena | Es la configuración del modo de transcripción. Acepta `"smart"` o un objeto de modo literal (`{"type": "verbatim", ...}`). El valor predeterminado es la transcripción literal. |
| `mode.type` | String | *(Solo en el modo literal)* Es el identificador del modo. Siempre se establece en `"verbatim"`. |
| `mode.timestamp_granularities` | Arreglo de strings | *(Solo en modo literal)* Es el nivel de detalle de las marcas de tiempo que se devolverán. Pasa `["word"]` para habilitar las compensaciones de inicio y finalización de palabras. No es compatible con el vocabulario personalizado. |
| `mode.diarization_mode` | String | *(Solo en el modo literal)* Modo de diarización. Pasa `"speaker"` para identificar y etiquetar a los distintos interlocutores. No es compatible con el vocabulario personalizado. |

## Prácticas recomendadas

- **Proporciona audio nítido:** Asegúrate de que las grabaciones de audio tengan una separación de voz clara y evita el recorte grave.
- **Proporciona sugerencias de idioma cuando lo sepas:** Si conoces el idioma del audio con anticipación, especifica `language_codes` para maximizar la exactitud.
- **Vocabulario personalizado objetivo:** Incluye solo términos de dominio distintos, nombres de marcas o nombres propios en `custom_vocabulary` en lugar de palabras cotidianas comunes.
- **Usa la API de Files para grabaciones grandes:** Para archivos de más de unos segundos, sube el archivo con `client.files.upload` y pasa el URI del archivo que se devolvió al modelo.

## Limitaciones

- **Duración del audio:** Las solicitudes unarias estándar admiten archivos de audio de hasta 1 hora. El procesamiento de audio se limita a 30 minutos cuando se habilitan funciones como la identificación de interlocutores o las marcas de tiempo a nivel de palabra.
- **Marcas de tiempo a nivel de la palabra:** Habilitar las marcas de tiempo a nivel de la palabra puede reducir la exactitud general de la transcripción.
- **Identificación de interlocutores:** La identificación de interlocutores admite hasta 8 interlocutores. La atribución de oradores para 3 o más oradores es experimental.
- **Vocabulario personalizado:** Puedes proporcionar hasta 1,000 términos en `custom_vocabulary`, pero, por lo general, se obtienen mejores resultados con hasta 100 términos. No puedes combinar `custom_vocabulary` con la segmentación por orador ni con marcas de tiempo a nivel de la palabra. La API rechaza las solicitudes que especifican `custom_vocabulary` junto con cualquiera de estas funciones.
- **Compatibilidad de modos:** La transcripción inteligente (`"smart"`) no se puede combinar con `timestamp_granularities` ni `diarization_mode`.

## ¿Qué sigue?

- Transmite audio en tiempo real con la [guía de transcripción en vivo](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=es-419) a través de la API de Live.
- Explora [Comprensión de audio](https://ai.google.dev/gemini-api/docs/audio?hl=es-419) para analizar, resumir o consultar contenido de audio.
- Aprende a sintetizar audio a partir de texto con [Text-to-speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419).
- Consulta la [página de precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#gemini-3.5-transcribe) para conocer los precios de los modelos y los límites de tokens.
- Consulta la guía de la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419) para obtener detalles sobre cómo subir y administrar archivos multimedia.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-23 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-23 (UTC)"],[],[]]
