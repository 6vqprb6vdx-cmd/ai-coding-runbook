---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=it
fetched_at: 2026-06-29T05:35:00.730902+00:00
title: "Comprensione dei video \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Comprensione dei video

> Per scoprire di più sulla generazione di video, consulta la [Veo](https://ai.google.dev/gemini-api/docs/video?hl=it).

I modelli Gemini possono elaborare i video, consentendo molti casi d'uso per gli sviluppatori all'avanguardia che in passato avrebbero richiesto modelli specifici per il dominio.
Alcune delle funzionalità di visione di Gemini includono la possibilità di: descrivere, segmentare ed estrarre informazioni dai video, rispondere a domande sui contenuti video e fare riferimento a timestamp specifici all'interno di un video.

Puoi fornire video come input a Gemini nei seguenti modi:

| Metodo inserimento | Dimensione massima | Caso d'uso consigliato |
| --- | --- | --- |
| [API File](#upload-video) | 20 GB (a pagamento) / 2 GB (senza costi) | File di grandi dimensioni (più di 100 MB), video lunghi (più di 10 minuti), file riutilizzabili. |
| [Registrazione di Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=it#registration) | 2 GB (per file, senza limiti di spazio di archiviazione) | File di grandi dimensioni (più di 100 MB), video lunghi (più di 10 minuti), file persistenti e riutilizzabili. |
| [Dati in linea](#inline-video) | Meno di 100 MB | File di piccole dimensioni (meno di 100 MB), durata breve (meno di 1 minuto), input una tantum. |
| [URL di YouTube](#youtube) | N/D | Video di YouTube pubblici. |

> **Nota:** l'API [File](#upload-video) è consigliata per la maggior parte dei casi d'uso, in particolare per i file di dimensioni superiori a 100 MB o quando vuoi riutilizzare il file in più richieste.

Per scoprire di più su altri metodi di input dei file, ad esempio l'utilizzo di URL esterni o file
archiviati in Google Cloud, consulta la
[guida Metodi di input dei file](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=it).

### Caricare un file video

Il seguente codice scarica un video di esempio, lo carica utilizzando l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it),
attende l'elaborazione e poi utilizza il riferimento al file caricato per
riassumere il video.

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

### Vai

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

Utilizza sempre l'API Files quando le dimensioni totali della richiesta (inclusi file, prompt di testo, istruzioni di sistema e così via) sono superiori a 20 MB, la durata del video è significativa o se intendi utilizzare lo stesso video in più prompt.
L'API File accetta direttamente i formati di file video.

Per scoprire di più su come lavorare con i file multimediali, consulta
[l'API Files](https://ai.google.dev/gemini-api/docs/files?hl=it).

### Trasmettere i dati video in linea

Anziché caricare un file video utilizzando l'API File, puoi trasmettere video più piccoli direttamente nella richiesta a `generateContent`. Questa opzione è adatta per i video più brevi con dimensioni totali della richiesta inferiori a 20 MB.

Ecco un esempio di fornitura di dati video in linea:

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

### Trasmettere URL di YouTube

Puoi trasmettere gli URL di YouTube direttamente all'API Gemini come parte della richiesta nel seguente modo:

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

### Vai

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

**Limitazioni:**

- Per il livello senza costi, non puoi caricare più di 8 ore di video di YouTube al giorno.
- Per il livello a pagamento, non esistono limiti basati sulla durata del video.
- Per i modelli precedenti a Gemini 2.5, puoi caricare un solo video per richiesta. Per i modelli Gemini 2.5 e successivi, puoi caricare un massimo di 10 video per richiesta.
- Puoi caricare solo video pubblici (non video privati o non in elenco).

## Utilizzare la memorizzazione nella cache del contesto per i video lunghi

Per i video di durata superiore a 10 minuti o quando prevedi di effettuare più richieste
per lo stesso file video, utilizza [la memorizzazione nella cache del contesto](https://ai.google.dev/gemini-api/docs/caching?hl=it) per
ridurre i costi e migliorare la latenza. La memorizzazione nella cache del contesto ti consente di elaborare il video una sola volta e riutilizzare i token per le query successive, il che la rende ideale per le sessioni di chat o l'analisi ripetuta di contenuti di lunga durata.

## Fare riferimento ai timestamp nei contenuti

Puoi porre domande su punti specifici del video utilizzando timestamp nel formato `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Vai

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

## Estrarre insight dettagliati dai video

I modelli Gemini offrono funzionalità avanzate per la comprensione dei contenuti video elaborando le informazioni dagli stream **audio e visivi**. In questo modo puoi estrarre un insieme completo di dettagli, tra cui la generazione di descrizioni di ciò che accade in un video e la risposta a domande sui suoi contenuti.

Per le descrizioni visive, il modello campiona il video a una frequenza di **1 frame al secondo** (FPS). Questa frequenza di campionamento predefinita funziona bene per la maggior parte dei contenuti, ma tieni presente che potrebbe non rilevare i dettagli nei video con movimenti rapidi o cambi di scena veloci.
Per i contenuti con movimenti rapidi, valuta la possibilità di [impostare una frequenza fotogrammi personalizzata](#custom-frame-rate).

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Vai

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

## Personalizzare l'elaborazione dei video

Puoi personalizzare l'elaborazione dei video nell'API Gemini impostando intervalli di ritaglio o fornendo un campionamento della frequenza fotogrammi personalizzato.

 

### Impostare intervalli di ritaglio

Puoi ritagliare il video specificando `videoMetadata` con offset di inizio e fine.

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

### Impostare una frequenza fotogrammi personalizzata

Puoi impostare il campionamento della frequenza fotogrammi personalizzata trasmettendo un argomento `fps` a `videoMetadata`.

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

Per impostazione predefinita, viene campionato 1 frame al secondo (FPS) dal video. Potresti voler impostare una frequenza fotogrammi bassa (inferiore a 1) per i video lunghi. Questa opzione è particolarmente utile per i video per lo più statici (ad es. lezioni). Utilizza una frequenza fotogrammi più alta per i video che richiedono un'analisi temporale granulare, ad esempio la comprensione di azioni rapide o il rilevamento del movimento ad alta velocità.

## Formati video supportati

Gemini supporta i seguenti tipi MIME di formato video:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Dettagli tecnici sui video

- **Modelli e contesto supportati**: tutti i modelli Gemini possono elaborare i dati video.
  - I modelli con una finestra contestuale di 1 milione possono elaborare video di durata massima di 1 ora con la risoluzione multimediale predefinita o di 3 ore con la risoluzione multimediale bassa.
- **Elaborazione dell'API File**: quando utilizzi l'API File, i video vengono archiviati a 1
  frame al secondo (FPS) e l'audio viene elaborato a 1 Kbps (canale singolo).
  I timestamp vengono aggiunti ogni secondo.
  - Queste tariffe sono soggette a modifiche in futuro per migliorare l'inferenza.
  - Puoi sostituire la frequenza di campionamento di 1 FPS [impostando una frequenza fotogrammi personalizzata](#custom-frame-rate).
- **Calcolo dei token**: ogni secondo di video viene tokenizzato nel seguente modo:
  - Frame singoli (campionati a 1 FPS):
    - Se [`mediaResolution`](https://ai.google.dev/api/generate-content?hl=it#MediaResolution) è impostato
      su low, i frame vengono tokenizzati a 66 token per frame.
    - In caso contrario, i frame vengono tokenizzati a 258 token per frame.
  - Audio: 32 token al secondo.
  - Sono inclusi anche i metadati.
  - Totale: circa 300 token al secondo di video con la risoluzione multimediale predefinita o 100 token al secondo di video con la risoluzione multimediale bassa.
- **Risoluzione multimediale**: Gemini 3 introduce il controllo granulare dell'elaborazione della visione multimodale
  con il `media_resolution` parametro. Il parametro `media_resolution` determina il **numero massimo di token allocati per ogni immagine di input o frame video**.
  Le risoluzioni più elevate migliorano la capacità del modello di leggere il testo fine o identificare piccoli dettagli, ma aumentano l'utilizzo dei token e la latenza.

  Per maggiori dettagli sul parametro e su come può influire sui calcoli dei token, consulta la guida alla [risoluzione multimediale](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=it).
- **Formato timestamp**: quando fai riferimento a momenti specifici di un video all'interno del prompt, utilizza il formato `MM:SS` (ad es. `01:15` per 1 minuto e 15 secondi).
- **Best practice**:

  - Per risultati ottimali, utilizza un solo video per richiesta di prompt.
  - Se combini testo e un singolo video, inserisci il prompt testuale *dopo* la parte video nell'array `contents`.
  - Tieni presente che le sequenze di azioni rapide potrebbero perdere dettagli a causa della frequenza di campionamento di 1 FPS. Se necessario, valuta la possibilità di rallentare queste clip.

## Passaggi successivi

Questa guida mostra come caricare file video e generare output di testo da input video. Per scoprire di più, consulta le seguenti risorse:

- [Istruzioni di sistema](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#system-instructions):
  Le istruzioni di sistema ti consentono di indirizzare il comportamento del modello in base alle tue
  esigenze e ai tuoi casi d'uso specifici.
- [API Files](https://ai.google.dev/gemini-api/docs/files?hl=it): scopri di più sul caricamento e sulla gestione dei
  file da utilizzare con Gemini.
- [Strategie di prompting dei file](https://ai.google.dev/gemini-api/docs/files?hl=it#prompt-guide): l'
  API Gemini supporta il prompting con dati di testo, immagini, audio e video, noto
  anche come prompting multimodale.
- [Linee guida per la sicurezza](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=it): a volte i modelli di AI generativa
  producono output imprevisti, ad esempio output imprecisi,
  distorti o offensivi. L'elaborazione post-produzione e la valutazione umana sono essenziali per
  limitare il rischio di danni derivanti da questi output.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-23 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-23 UTC."],[],[]]
