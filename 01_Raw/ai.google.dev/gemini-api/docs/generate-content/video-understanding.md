---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=es-419
fetched_at: 2026-07-06T05:09:33.803345+00:00
title: "Comprensi\u00f3n de videos \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Comprensión de videos

> Para obtener información sobre la generación de videos, consulta la guía de [Veo](https://ai.google.dev/gemini-api/docs/video?hl=es-419).

Los modelos de Gemini pueden procesar videos, lo que permite muchos casos de uso de desarrolladores de vanguardia que históricamente habrían requerido modelos específicos del dominio.
Algunas de las capacidades de visión de Gemini incluyen la capacidad de describir, segmentar y extraer información de videos, responder preguntas sobre el contenido de los videos y hacer referencia a marcas de tiempo específicas dentro de un video.

Puedes proporcionar videos como entrada a Gemini de las siguientes maneras:

| Método de entrada | Tamaño máximo | Caso de uso recomendado |
| --- | --- | --- |
| [API de File](#upload-video) | 20 GB (pagado) o 2 GB (gratis) | Archivos grandes (más de 100 MB), videos largos (más de 10 minutos) y archivos reutilizables |
| [Registro de Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=es-419#registration) | 2 GB (por archivo, sin límites de almacenamiento) | Archivos grandes (más de 100 MB), videos largos (más de 10 minutos) y archivos persistentes y reutilizables |
| [Datos intercalados](#inline-video) | < 100 MB | Archivos pequeños (menos de 100 MB), duración corta (menos de 1 min) y entradas únicas. |
| [URLs de YouTube](#youtube) | N/A | Videos públicos de YouTube |

> **Nota:** Se recomienda la [API de File](#upload-video) para la mayoría de los casos de uso, en especial para los archivos de más de 100 MB o cuando deseas reutilizar el archivo en varias solicitudes.

Para obtener información sobre otros métodos de entrada de archivos, como el uso de URLs externas o archivos almacenados en Google Cloud, consulta la guía [Métodos de entrada de archivos](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=es-419).

### Cómo subir un archivo de video

El siguiente código descarga un video de muestra, lo sube con la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419), espera a que se procese y, luego, usa la referencia del archivo subido para resumir el video.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.5-flash",
    contents,
    nil,
)

fmt.Println(result.Text())
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

Siempre usa la API de Files cuando el tamaño total de la solicitud (incluido el archivo, la instrucción de texto, las instrucciones del sistema, etcétera) sea superior a 20 MB, la duración del video sea significativa o si tienes la intención de usar el mismo video en varias instrucciones.
La API de File acepta formatos de archivos de video directamente.

Para obtener más información sobre cómo trabajar con archivos multimedia, consulta la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419).

### Pasa datos de video intercalados

En lugar de subir un archivo de video con la API de File, puedes pasar videos más pequeños directamente en la solicitud a `generateContent`. Esto es adecuado para videos más cortos con un tamaño total de solicitud inferior a 20 MB.

A continuación, se muestra un ejemplo de cómo proporcionar datos de video intercalados:

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "video/mp4",
      data: base64VideoFile,
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: contents,
});
console.log(response.text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"video/mp4",
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"
              }
            },
            {"text": "Please summarize the video in 3 sentences."}
        ]
      }]
    }' 2> /dev/null
```

### Pasa URLs de YouTube

Puedes pasar URLs de YouTube directamente a la API de Gemini como parte de tu solicitud de la siguiente manera:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [
  {
    fileData: {
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: contents,
});
console.log(response.text);
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.5-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Please summarize the video in 3 sentences."},
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
              }
            }
        ]
      }]
    }' 2> /dev/null
```

**Limitaciones:**

- En el nivel gratuito, no puedes subir más de 8 horas de videos de YouTube por día.
- En el nivel pagado, no hay límites basados en la duración del video.
- En el caso de los modelos anteriores a Gemini 2.5, solo puedes subir 1 video por solicitud. En el caso de Gemini 2.5 y modelos posteriores, puedes subir un máximo de 10 videos por solicitud.
- Solo puedes subir videos públicos (no privados ni no listados).

## Usa el almacenamiento de contexto en caché para videos largos

Para los videos de más de 10 minutos o cuando planees realizar varias solicitudes en el mismo archivo de video, usa el [almacenamiento en caché de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=es-419) para reducir los costos y mejorar la latencia. El almacenamiento de contexto en caché te permite procesar el video una vez y reutilizar los tokens para las consultas posteriores, lo que lo hace ideal para las sesiones de chat o el análisis repetido de contenido de formato largo.

## Consulta las marcas de tiempo en el contenido

Puedes hacer preguntas sobre momentos específicos del video usando marcas de tiempo con el formato `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
         // Adjusted timestamps for the NASA video
        genai.NewPartFromText("What are the examples given at 00:05 and " +
            "00:10 supposed to show us?"),
    }
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Extrae estadísticas detalladas de los videos

Los modelos de Gemini ofrecen potentes capacidades para comprender el contenido de video, ya que procesan información de los flujos de **audio y visuales**. Esto te permite extraer un conjunto enriquecido de detalles, lo que incluye generar descripciones de lo que sucede en un video y responder preguntas sobre su contenido.

En el caso de las descripciones visuales, el modelo muestrea el video a una velocidad de **1 fotograma por segundo** (FPS). Esta frecuencia de muestreo predeterminada funciona bien para la mayoría del contenido, pero ten en cuenta que es posible que no capte los detalles en los videos con movimiento rápido o cambios de escena rápidos.
Para este tipo de contenido con mucho movimiento, considera [establecer una velocidad de fotogramas personalizada](#custom-frame-rate).

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
        genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
      "Include timestamps for salient moments."),
    }
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Personaliza el procesamiento de video

Puedes personalizar el procesamiento de video en la API de Gemini configurando intervalos de recorte o proporcionando un muestreo de velocidad de fotogramas personalizado.

### Cómo establecer intervalos de recorte

Puedes cortar videos especificando `videoMetadata` con compensaciones de inicio y finalización.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3.5-flash';

async function main() {
const contents = [
  {
    role: 'user',
    parts: [
      {
        fileData: {
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',
          mimeType: 'video/*',
        },
        videoMetadata: {
          startOffset: '40s',
          endOffset: '80s',
        }
      },
      {
        text: 'Please summarize the video in 3 sentences.',
      },
    ],
  },
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### Cómo establecer una velocidad de fotogramas personalizada

Puedes establecer un muestreo de la velocidad de fotogramas personalizado pasando un argumento `fps` a `videoMetadata`.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

De forma predeterminada, se muestrea 1 fotograma por segundo (FPS) del video. Te recomendamos que establezcas un valor de FPS bajo (inferior a 1) para los videos largos. Esto es especialmente útil para los videos que son casi estáticos (p.ej., conferencias). Usa un FPS más alto para los videos que requieren un análisis temporal detallado, como la comprensión de acciones rápidas o el seguimiento de movimiento de alta velocidad.

## Formatos de video compatibles

Gemini admite los siguientes tipos de MIME de formato de video:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Detalles técnicos sobre los videos

- **Modelos y contexto compatibles**: Todos los modelos de Gemini pueden procesar datos de video.
  - Los modelos con una ventana de contexto de 1 millón de tokens pueden procesar videos de hasta 1 hora de duración con la resolución de medios predeterminada o de hasta 3 horas con una resolución de medios baja.
- **Procesamiento de la API de File**: Cuando se usa la API de File, los videos se almacenan a 1 fotograma por segundo (FPS) y el audio se procesa a 1 Kbps (canal único).
  Las marcas de tiempo se agregan cada segundo.
  - Estas tasas están sujetas a cambios en el futuro para mejorar la inferencia.
  - Puedes anular la tasa de muestreo de 1 FPS [estableciendo una velocidad de fotogramas personalizada](#custom-frame-rate).
- **Cálculo de tokens**: Cada segundo de video se tokeniza de la siguiente manera:
  - Fotogramas individuales (muestreados a 1 FPS):
    - Si [`mediaResolution`](https://ai.google.dev/api/generate-content?hl=es-419#MediaResolution) se establece en un valor bajo, los fotogramas se tokenizan en 66 tokens por fotograma.
    - De lo contrario, los fotogramas se tokenizan a 258 tokens por fotograma.
  - Audio: 32 tokens por segundo
  - También se incluyen los metadatos.
  - Total: Aproximadamente 300 tokens por segundo de video en la resolución de medios predeterminada o 100 tokens por segundo de video en la resolución de medios baja.
- **Resolución media**: Gemini 3 introduce un control detallado sobre el procesamiento de visión multimodal con el parámetro `media_resolution`. El parámetro `media_resolution` determina la **cantidad máxima de tokens asignados por imagen de entrada o fotograma de video.**
  Las resoluciones más altas mejoran la capacidad del modelo para leer texto pequeño o identificar detalles pequeños, pero aumentan el uso de tokens y la latencia.

  Para obtener más detalles sobre el parámetro y cómo puede afectar los cálculos de tokens, consulta la guía de [resolución de medios](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=es-419).
- **Formato de marca de tiempo**: Cuando te refieras a momentos específicos de un video en tu instrucción, usa el formato `MM:SS` (p.ej., `01:15` para 1 minuto y 15 segundos).
- **Recomendaciones:**

  - Para obtener resultados óptimos, usa solo un video por solicitud de instrucción.
  - Si combinas texto y un solo video, coloca la instrucción de texto *después* de la parte del video en el array `contents`.
  - Ten en cuenta que las secuencias de acción rápidas pueden perder detalles debido a la frecuencia de muestreo de 1 FPS. Si es necesario, considera reducir la velocidad de esos clips.

## ¿Qué sigue?

En esta guía, se muestra cómo subir archivos de video y generar resultados de texto a partir de entradas de video. Para obtener más información, consulta los siguientes recursos:

- [Instrucciones del sistema](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419#system-instructions):
  Las instrucciones del sistema te permiten dirigir el comportamiento del modelo según tus necesidades y casos de uso específicos.
- [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419): Obtén más información para subir y administrar archivos para usar con Gemini.
- [Estrategias de instrucciones con archivos](https://ai.google.dev/gemini-api/docs/files?hl=es-419#prompt-guide): La API de Gemini admite instrucciones con datos de texto, imagen, audio y video, también conocidas como instrucciones multimodales.
- [Orientación sobre seguridad](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=es-419): A veces, los modelos de IA generativa producen resultados inesperados, como resultados inexactos, sesgados u ofensivos. El procesamiento posterior y la evaluación humana son fundamentales para limitar el riesgo de daño que pueden causar estos resultados.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-23 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-23 (UTC)"],[],[]]
