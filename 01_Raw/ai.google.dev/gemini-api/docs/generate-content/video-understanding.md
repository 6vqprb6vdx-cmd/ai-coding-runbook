---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=de
fetched_at: 2026-08-24T02:28:54.264815+00:00
title: "Videos verstehen \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Videos verstehen

> Informationen zur Videogenerierung finden Sie im [Veo](https://ai.google.dev/gemini-api/docs/video?hl=de) Leitfaden.

Gemini-Modelle können Videos verarbeiten und so viele neue Anwendungsfälle für Entwickler ermöglichen, für die in der Vergangenheit domänenspezifische Modelle erforderlich gewesen wären.
Zu den Vision-Funktionen von Gemini gehören unter anderem die Möglichkeit, Videos zu beschreiben, zu segmentieren und Informationen daraus zu extrahieren, Fragen zu Videoinhalten zu beantworten und auf bestimmte Zeitstempel in einem Video zu verweisen.

Sie können Videos auf folgende Weise als Eingabe für Gemini bereitstellen:

| Eingabemethode | Max. Größe | Empfohlener Anwendungsfall |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (kostenpflichtig) / 2 GB (kostenlos) | Große Dateien (über 100 MB), lange Videos (über 10 Minuten), wiederverwendbare Dateien |
| [Cloud Storage-Registrierung](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=de#registration) | 2 GB (pro Datei, keine Speicherlimits) | Große Dateien (über 100 MB), lange Videos (über 10 Minuten), dauerhafte, wiederverwendbare Dateien |
| [Inlinedaten](#inline-video) | unter 100 MB | Kleine Dateien (unter 100 MB), kurze Dauer (unter 1 Minute), einmalige Eingaben |
| [YouTube-URLs](#youtube) | – | Öffentliche YouTube-Videos |

> **Hinweis:** Die [File API](#upload-video) wird für die meisten Anwendungsfälle empfohlen, insbesondere für Dateien, die größer als 100 MB sind, oder wenn Sie die Datei in mehreren Anfragen wiederverwenden möchten.

Informationen zu anderen Methoden für die Dateieingabe, z. B. die Verwendung externer URLs oder in Google Cloud gespeicherter Dateien, finden Sie im
[Leitfaden zu Methoden für die Dateieingabe](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=de).

### Videodatei hochladen

Mit dem folgenden Code wird ein Beispielvideo heruntergeladen, über die [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de) hochgeladen,
auf die Verarbeitung gewartet und dann die hochgeladene Dateireferenz verwendet, um
das Video zusammenzufassen.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
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
    model: "gemini-3.6-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Ok

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
    "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

Verwenden Sie immer die Files API, wenn die Gesamtgröße der Anfrage (einschließlich Datei, Text-Prompt, Systemanweisungen usw.) größer als 20 MB ist, die Videodauer erheblich ist oder wenn Sie dasselbe Video in mehreren Prompts verwenden möchten.
Die File API akzeptiert Videodateiformate direkt.

Weitere Informationen zum Arbeiten mit Mediendateien finden Sie unter
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=de).

### Videodaten inline übergeben

Anstatt eine Videodatei mit der File API hochzuladen, können Sie kleinere Videos direkt in der Anfrage an `generateContent` übergeben. Dies eignet sich für kürzere Videos mit einer Gesamtgröße der Anfrage von unter 20 MB.

Hier ein Beispiel für die Bereitstellung von Inline-Videodaten:

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.6-flash',
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
  model: "gemini-3.6-flash",
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

### YouTube-URLs übergeben

Sie können YouTube-URLs wie folgt direkt als Teil Ihrer Anfrage an die Gemini API übergeben:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.6-flash',
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
  model: "gemini-3.6-flash",
  contents: contents,
});
console.log(response.text);
```

### Ok

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
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

**Beschränkungen** :

- Im kostenlosen Abo können Sie pro Tag maximal 8 Stunden YouTube-Video hochladen.
- Im kostenpflichtigen Abo gibt es keine Beschränkung basierend auf der Videolänge.
- Bei Modellen vor Gemini 2.5 können Sie pro Anfrage nur ein Video hochladen. Bei Gemini 2.5 und neueren Modellen können Sie pro Anfrage maximal 10 Videos hochladen.
- Sie können nur öffentliche Videos hochladen (keine privaten oder nicht gelisteten Videos).

## Kontext-Caching für lange Videos verwenden

Bei Videos, die länger als 10 Minuten sind, oder wenn Sie mehrere Anfragen
für dieselbe Videodatei stellen möchten, verwenden Sie [Kontext-Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de), um
Kosten zu senken und die Latenz zu verbessern. Mit Kontext-Caching können Sie das Video einmal verarbeiten und die Tokens für nachfolgende Anfragen wiederverwenden. Das ist ideal für Chats oder wiederholte Analysen von Inhalten im Langformat.

## Auf Zeitstempel im Inhalt verweisen

Sie können Fragen zu bestimmten Zeitpunkten im Video stellen, indem Sie Zeitstempel im Format `MM:SS` verwenden.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Ok

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

## Detaillierte Erkenntnisse aus Videos extrahieren

Gemini-Modelle bieten leistungsstarke Funktionen zum Verstehen von Videoinhalten, indem sie Informationen aus den **Audio- und visuellen** Streams verarbeiten. So können Sie eine Vielzahl von Details extrahieren, einschließlich Beschreibungen dessen, was in einem Video passiert, und Antworten auf Fragen zu den Inhalten.

Für visuelle Beschreibungen nimmt das Modell **1 Frame pro Sekunde** auf. Diese Standard-Samplingrate funktioniert für die meisten Inhalte gut, aber es kann sein, dass Details in Videos mit schnellen Bewegungen oder schnellen Szenenwechseln verloren gehen.
Für solche Inhalte mit schnellen Bewegungen sollten Sie [eine benutzerdefinierte Framerate festlegen](#custom-frame-rate).

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Ok

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

## Videoverarbeitung anpassen

Sie können die Videoverarbeitung in der Gemini API anpassen, indem Sie Clipping-Intervalle festlegen oder eine benutzerdefinierte Framerate-Samplingrate angeben.

 

### Clipping-Intervalle festlegen

Sie können Videos clippen, indem Sie `videoMetadata` mit Start- und End-Offsets angeben.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.6-flash',
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
const model = 'gemini-3.6-flash';

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

### Benutzerdefinierte Framerate festlegen

Sie können eine benutzerdefinierte Framerate-Samplingrate festlegen, indem Sie ein `fps`-Argument an `videoMetadata` übergeben.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.6-flash',
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

Standardmäßig wird 1 Frame pro Sekunde aus dem Video gesampelt. Für lange Videos sollten Sie eine niedrige Framerate (unter 1) festlegen. Das ist besonders nützlich für meist statische Videos (z.B. Vorträge). Verwenden Sie eine höhere Framerate für Videos, die eine detaillierte zeitliche Analyse erfordern, z. B. zum Verstehen von schnellen Aktionen oder zur Hochgeschwindigkeits-Bewegungserkennung.

## Unterstützte Videoformate

Gemini unterstützt die folgenden MIME-Typen für Videoformate:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Technische Details zu Videos

- **Unterstützte Modelle und Kontext**: Alle Gemini-Modelle können Videodaten verarbeiten.
  - Modelle mit einem Kontextfenster von 1 Million Tokens können Videos mit einer Länge von bis zu 1 Stunde bei Standard-Mediaauflösung oder 3 Stunden bei niedriger Mediaauflösung verarbeiten.
- **Verarbeitung mit der File API**: Bei Verwendung der File API werden Videos mit 1
  Frame pro Sekunde gespeichert und Audio mit 1 kbit/s (Einzelkanal) verarbeitet.
  Zeitstempel werden jede Sekunde hinzugefügt.
  - Diese Raten können sich in Zukunft ändern, um die Inferenz zu verbessern.
  - Sie können die Samplingrate von 1 FPS überschreiben, indem Sie [eine benutzerdefinierte Framerate festlegen](#custom-frame-rate).
- **Tokenberechnung**: Jede Sekunde Video wird so tokenisiert:
  - Einzelne Frames (gesampelt mit 1 FPS):
    - Wenn [`mediaResolution`](https://ai.google.dev/api/generate-content?hl=de#MediaResolution) auf „low“ gesetzt ist, werden Frames mit 66 Tokens pro Frame tokenisiert.
    - Andernfalls werden Frames mit 258 Tokens pro Frame tokenisiert.
  - Audio: 32 Tokens pro Sekunde.
  - Metadaten sind ebenfalls enthalten.
  - Gesamt: etwa 300 Tokens pro Sekunde Video bei Standard-Mediaauflösung oder 100 Tokens pro Sekunde Video bei niedriger Mediaauflösung.
- **Mediaauflösung**: Gemini 3 bietet mit dem Parameter `media_resolution` eine detaillierte Steuerung der multimodalen
  Vision-Verarbeitung. Der Parameter `media_resolution` bestimmt die **maximale Anzahl von Tokens, die pro Eingabebild oder Video-Frame zugewiesen werden**.
  Höhere Auflösungen verbessern die Fähigkeit des Modells, kleinen Text zu lesen oder kleine Details zu erkennen, erhöhen aber die Tokennutzung und die Latenz.

  Weitere Informationen zum Parameter und zu den Auswirkungen auf die Token
  berechnung finden Sie im [Leitfaden zur Mediaauflösung](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=de).
- **Zeitstempelformat**: Wenn Sie in Ihrem Prompt auf bestimmte Momente in einem Video verweisen, verwenden Sie das `MM:SS` Format (z.B. `01:15` für 1 Minute und 15 Sekunden).
- **Best Practices**:

  - Verwenden Sie für optimale Ergebnisse nur ein Video pro Prompt-Anfrage.
  - Wenn Sie Text und ein einzelnes Video kombinieren, platzieren Sie den Text-Prompt *nach* dem Videoteil im Array `contents`.
  - Beachten Sie, dass bei schnellen Aktionssequenzen aufgrund der Samplingrate von 1 FPS Details verloren gehen können. Verlangsamen Sie solche Clips gegebenenfalls.

## Nächste Schritte

In diesem Leitfaden wird gezeigt, wie Sie Videodateien hochladen und Textausgaben aus Videoeingaben generieren. Weitere Informationen finden Sie in folgenden Dokumenten:

- [Systemanweisungen](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#system-instructions):
  Mit Systemanweisungen können Sie das Verhalten des Modells entsprechend Ihren
  spezifischen Anforderungen und Anwendungsfällen steuern.
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de): Weitere Informationen zum Hochladen und Verwalten von
  Dateien für die Verwendung mit Gemini.
- [Strategien für Prompts mit Dateien](https://ai.google.dev/gemini-api/docs/files?hl=de#prompt-guide): Die
  Gemini API unterstützt Prompts mit Text-, Bild-, Audio- und Videodaten, auch
  multimodale Prompts genannt.
- [Sicherheitshinweise](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=de): Manchmal liefern generative
  KI-Modelle unerwartete Ausgaben, z. B. Ausgaben, die falsch, voreingenommen oder anstößig sind. Nachbearbeitung und menschliche Bewertung sind unerlässlich, um
  das Risiko von Schäden durch solche Ausgaben zu begrenzen.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
