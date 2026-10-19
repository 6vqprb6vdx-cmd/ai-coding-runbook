---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=pl
fetched_at: 2026-10-19T05:40:24.324368+00:00
title: "Rozpoznawanie film\u00f3w \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs/generate-content?hl=pl)

Prześlij opinię

# Rozpoznawanie filmów

> Więcej informacji o generowaniu filmów znajdziesz w przewodniku po [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=pl).

Modele Gemini mogą przetwarzać filmy, co umożliwia deweloperom korzystanie z wielu zaawansowanych przypadków użycia, które wcześniej wymagały modeli specyficznych dla danej domeny.
Niektóre funkcje Gemini Vision obejmują możliwość opisywania, segmentowania i wyodrębniania informacji z filmów, odpowiadania na pytania dotyczące treści wideo oraz odwoływania się do konkretnych sygnatur czasowych w filmie.

Filmy możesz przekazywać do Gemini na te sposoby:

| Sposób wprowadzania tekstu | Wielkość maksymalna | Zalecany przypadek użycia |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (płatne) / 2 GB (bezpłatne) | Duże pliki (ponad 100 MB), długie filmy (ponad 10 minut), pliki wielokrotnego użytku. |
| [Rejestracja w Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl#registration) | 2 GB (na plik, bez limitów miejsca na dane) | Duże pliki (ponad 100 MB), długie filmy (ponad 10 minut), trwałe pliki wielokrotnego użytku. |
| [Dane w treści](#inline-video) | < 100 MB | Małe pliki (poniżej 100 MB), krótkie filmy (poniżej 1 minuty), jednorazowe dane wejściowe. |
| [Adresy URL z YouTube](#youtube) | Nie dotyczy | Publiczne filmy na YouTube. |

> **Uwaga:** w większości przypadków zalecamy korzystanie z [File API](#upload-video), zwłaszcza w przypadku plików większych niż 100 MB lub gdy chcesz użyć tego samego pliku w wielu żądaniach.

Więcej informacji o innych metodach wprowadzania plików, takich jak używanie zewnętrznych adresów URL lub plików
przechowywanych w Google Cloud, znajdziesz w przewodniku
[Metody wprowadzania plików](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl).

### Przesyłanie pliku wideo

Ten kod pobiera przykładowy film, przesyła go za pomocą [Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl),
czeka na jego przetworzenie, a następnie używa odniesienia do przesłanego pliku, aby
podsumować film.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
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
    model: "gemini-3.8-flash",
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
    "gemini-3.8-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

Aby zoptymalizować wydajność i wykorzystanie tokenów, rozważ użycie
[przetwarzania wideo przez agenta](#agentic-video-understanding).

Zawsze używaj Files API, gdy łączny rozmiar żądania (w tym pliku, prompta tekstowego, instrukcji systemowych itp.) jest większy niż 20 MB, czas trwania filmu jest znaczący lub gdy zamierzasz użyć tego samego filmu w wielu promptach.
File API bezpośrednio akceptuje formaty plików wideo.

Więcej informacji o pracy z plikami multimedialnymi znajdziesz w artykule
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

### Przekazywanie danych wideo w treści

Zamiast przesyłać plik wideo za pomocą File API, możesz przekazywać mniejsze filmy bezpośrednio w żądaniu do `generateContent`. Jest to odpowiednie w przypadku krótszych filmów, których łączny rozmiar żądania nie przekracza 20 MB.

Oto przykład przekazywania danych wideo w treści:

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
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
  model: "gemini-3.8-flash",
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

### Przekazywanie adresów URL z YouTube

Adresy URL z YouTube możesz przekazywać bezpośrednio do Gemini API w ramach żądania w ten sposób:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
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
  model: "gemini-3.8-flash",
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
      "gemini-3.8-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

**Ograniczenia:**

- W przypadku bezpłatnego planu nie możesz przesyłać więcej niż 8 godzin filmów z YouTube dziennie.
- W przypadku płatnego planu nie ma limitu opartego na długości wideo.
- W przypadku modeli wcześniejszych niż Gemini 2.5 możesz przesłać tylko 1 film na żądanie. W przypadku modeli Gemini 2.5 i nowszych możesz przesłać maksymalnie 10 filmów na żądanie.
- Możesz przesyłać tylko filmy publiczne (nie prywatne ani niepubliczne).

## Analizowanie filmów przez agenta

Domyślnie dane wejściowe wideo są przetwarzane statycznie (wyodrębnianie klatek z szybkością 1 kl./s) we wszystkich modelach, w tym w Gemini 4.
Modele Gemini 4 Argon, 3.8 Flash, 3.6 Flash i 3.5 Flash Lite obsługują też
**agentowe analizowanie filmów**, czyli tryb z akceptacją użytkownika, w którym model dynamicznie analizuje oś czasu filmu, selektywnie sprawdza transkrypcje i na bieżąco dostosowuje liczbę klatek na sekundę
oraz rozdzielczość na podstawie prompta.

| **Tryb** | **Opis** | **Obsługiwane modele** |
| --- | --- | --- |
| **Statyczny** (domyślny) | Wyodrębnia klatki ze stałą szybkością (1 kl./s) i umieszcza je w kontekście w jednym przebiegu. Domyślny dla wszystkich modeli Gemini, w tym Gemini 4. | Wszystkie modele Gemini |
| **Rozwiązania agentowe** | Model dynamicznie porusza się po osi czasu filmu, wczytując tylko te treści, których potrzebuje na podstawie prompta. Do 88% większa wydajność tokenów i o ok. 7% wyższa jakość w przypadku długich treści. | Gemini 4 Argon, 3.8 Flash, 3.6 Flash, 3.5 Flash Lite |

### Wybieranie trybu przetwarzania

Wybierz tryb przetwarzania, który odpowiada długości wideo i typowi zapytania:

- **Statyczny (domyślny):** najlepszy w przypadku krótkich klipów (poniżej 5 minut), ogólnych podsumowań całego filmu, w których istotne jest całe nagranie, zapytań wrażliwych na opóźnienia lub precyzji na poziomie klatek w całym klipie. W przypadku krótkich filmów lub ogólnych promptów, które wymagają sprawdzenia większości filmu, przetwarzanie statyczne pozwala uniknąć dodatkowych tokenów myślenia (`thoughts_token_count`) i wywołań narzędzi w obie strony (`tool_use_prompt_token_count`) związanych z poruszaniem się po osi czasu.
- **Rozwiązania agentowe:** najlepsze w przypadku długich filmów (ponad 5–10 minut), wyszukiwania igły w stogu siana lub zapytań dotyczących konkretnych momentów lub tematów. Model najpierw sprawdza transkrypcje, a następnie wczytuje tylko odpowiednie segmenty wizualne na żądanie, co zmniejsza zużycie tokenów wejściowych wideo nawet o 88% bez wypełniania okna kontekstu.

> **Uwaga:** w przypadku długich filmów lub złożonych promptów, w których przetwarzanie przez agenta zajmuje więcej czasu, użyj przesyłania strumieniowego (`client.models.generate_content_stream`). Dzięki temu połączenie pozostaje aktywne, wyświetlają się pośrednie kroki rozumowania i można uniknąć przekroczenia limitu czasu połączenia lub uwierzytelniania.

### Ustawianie trybu przetwarzania

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=video_file.uri,
            mime_type=video_file.mime_type,
            media_processing="AGENTIC",
        ),
        "What are the three main arguments presented?",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" },
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: videoFile.uri,
            mimeType: videoFile.mimeType,
          },
          mediaProcessing: "AGENTIC",
        },
        { text: "What are the three main arguments presented?" },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/lecture.mp4", nil)
parts := []*genai.Part{
    {
        FileData: &genai.FileData{
            FileURI:  uploadedFile.URI,
            MIMEType: uploadedFile.MIMEType,
        },
        MediaProcessing: genai.MediaProcessingAgentic,
    },
    genai.NewPartFromText("What are the three main arguments presented?"),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${file_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {"text": "What are the three main arguments presented?"}
      ]
    }]
  }'
```

> **Uwaga:** aby sprawdzić, czy użyto przetwarzania przez agenta, sprawdź `response.candidates[0].content.parts`. Obecność części `tool_call` i `tool_response` z typem narzędzia `MEDIA_PROCESSING` wskazuje, że model dynamicznie poruszał się po filmie.

> **Uwaga:** w przeciwieństwie do innych narzędzi po stronie serwera (takich jak wyszukiwarka Google czy kontekst adresu URL) w przypadku filmów przetwarzanych przez agenta nie trzeba ustawiać `include_server_side_tool_invocations=True` w `ToolConfig`, aby wywołania narzędzi i wyniki były zwracane lub przesyłane strumieniowo. Części `tool_call` i `tool_response` dotyczące poruszania się po filmie są zwracane automatycznie, gdy `media_processing="AGENTIC"` jest ustawione w dowolnej części wejściowej.

### Struktura odpowiedzi

Gdy włączone jest przetwarzanie przez agenta, odpowiedź zawiera dodatkowe części, które ujawniają wewnętrzną ścieżkę nawigacji:

- `tool_call` **parts** (`tool_type: "MEDIA_PROCESSING"`): emitowane za każdym razem, gdy model prosi o segment wideo lub transkrypcję audio.
- `tool_response` **parts** (`tool_type: "MEDIA_PROCESSING"`): wynik każdej operacji wczytywania.

Nie musisz ręcznie obsługiwać tych części ani na nie odpowiadać. Przekaż całą odpowiedź jako historię rozmowy, a zostaną one obsłużone automatycznie.

Jeśli w `ThinkingConfig` ustawisz `include_thoughts=True`, kroki rozumowania będą wyświetlane jako części `thought: true` przeplatane parami wywołań i odpowiedzi narzędzi. Gdy myśli są wyłączone, tekst myśli jest pomijany, ale części narzędzi są nadal obecne.

Ten przykład pokazuje ładunek odpowiedzi z przeplatanymi częściami wywołań i odpowiedzi narzędzi:

```
{
  "candidates": [
    {
      "content": {
        "role": "model",
        "parts": [
          {
            "thought": true,
            "text": "Inspecting transcript for key discussion topics..."
          },
          {
            "thought_signature": "sig_A",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_B",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Loading visual frames to verify slide content..."
          },
          {
            "thought_signature": "sig_C",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_D",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Synthesizing answer from gathered evidence..."
          },
          {
            "text": "The three main arguments presented in the lecture are...",
            "thought_signature": "sig_E"
          }
        ]
      }
    }
  ]
}
```

### Łączenie trybów przetwarzania w różnych filmach

W tym samym żądaniu możesz ustawić różne tryby przetwarzania dla każdej części wideo:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=lecture.uri,
            mime_type=lecture.mime_type,
            media_processing="AGENTIC",  # Use agentic video understanding
        ),
        types.Part.from_uri(
            file_uri=experiment.uri,
            mime_type=experiment.mime_type,
            media_processing="STATIC",  # Use static processing
        ),
        "Compare the lecture content with the experiment results.",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" },
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" },
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: lecture.uri,
            mimeType: lecture.mimeType,
          },
          mediaProcessing: "AGENTIC", // Use agentic video understanding
        },
        {
          fileData: {
            fileUri: experiment.uri,
            mimeType: experiment.mimeType,
          },
          mediaProcessing: "STATIC", // Use static processing
        },
        { text: "Compare the lecture content with the experiment results." },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
lecturePart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  lectureFile.URI,
        MIMEType: lectureFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingAgentic, // Use agentic
}
experimentPart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  experimentFile.URI,
        MIMEType: experimentFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingStatic, // Use static
}
parts := []*genai.Part{
    lecturePart,
    experimentPart,
    genai.NewPartFromText("Compare the lecture content with the experiment results."),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${lecture_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {
          "file_data": {
            "file_uri": "'${experiment_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "STATIC"
        },
        {"text": "Compare the lecture content with the experiment results."}
      ]
    }]
  }'
```

## Używanie pamięci podręcznej kontekstu w przypadku długich filmów

W przypadku filmów dłuższych niż 10 minut lub gdy planujesz wysłać wiele żądań
dotyczących tego samego pliku wideo, użyj [buforowania kontekstu](https://ai.google.dev/gemini-api/docs/caching?hl=pl) aby
zmniejszyć koszty i skrócić czas oczekiwania. Pamięć podręczna kontekstu umożliwia jednokrotne przetworzenie filmu i ponowne użycie tokenów w kolejnych zapytaniach, co jest idealne w przypadku sesji czatu lub powtarzanej analizy długich treści.

## Odwoływanie się do sygnatur czasowych w treści

Możesz zadawać pytania dotyczące konkretnych momentów w filmie, używając sygnatur czasowych w formacie `MM:SS`.

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "What are the examples given at 00:05 and 00:10 supposed to show us?",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "What are the examples given at 00:05 and 00:10 supposed to show us?",
  ],
});
console.log(response.text);
```

### Go

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("What are the examples given at 00:05 and 00:10 supposed to show us?"),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "What are the examples given at 00:05 and 00:10 supposed to show us?"}
        ]
      }]
    }' 2> /dev/null
```

## Wyodrębnianie szczegółowych informacji z filmu

Modele Gemini oferują zaawansowane możliwości analizowania treści wideo dzięki przetwarzaniu informacji z **ścieżek audio i wizualnych**. Dzięki temu możesz wyodrębnić bogaty zestaw szczegółów, w tym generować opisy tego, co dzieje się w filmie, i odpowiadać na pytania dotyczące jego treści.

W przypadku opisów wizualnych model próbkuje film z szybkością **1 klatki na sekundę** (FPS). Ta domyślna częstotliwość próbkowania sprawdza się w przypadku większości treści, ale pamiętaj, że może pomijać szczegóły w filmach z szybkim ruchem lub szybkimi zmianami scen.
W przypadku takich treści o dużej dynamice rozważ [ustawienie niestandardowej liczby klatek na sekundę](#custom-frame-rate).

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
  ],
});
console.log(response.text);
```

### Go

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
        "Include timestamps for salient moments."),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."}
        ]
      }]
    }' 2> /dev/null
```

## Dostosowywanie przetwarzania wideo

Przetwarzanie wideo w Gemini API możesz dostosować, ustawiając interwały przycinania lub podając niestandardową liczbę klatek na sekundę. Te opcje dostosowywania
są obsługiwane tylko podczas przetwarzania filmu w trybie `"static"`.

### Ustawianie interwałów przycinania

Możesz przycinać filmy, określając `videoMetadata` z przesunięciami początku i końca.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
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
const model = 'gemini-3.8-flash';

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

### Ustawianie niestandardowej liczby klatek na sekundę

Możesz ustawić niestandardową liczbę klatek próbkowania, przekazując argument `fps` do `videoMetadata`.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
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

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const myfile = await ai.files.upload({
  file: "path/to/sample.mp4",
  mimeType: "video/mp4",
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      fileData: {
        fileUri: myfile.uri,
        mimeType: myfile.mimeType,
      },
      videoMetadata: {
        fps: 5,
      },
    },
    "Please summarize the video in 3 sentences.",
  ],
});

console.log(response.text);
```

Domyślnie z filmu próbkowana jest 1 klatka na sekundę. W przypadku długich filmów możesz ustawić niską liczbę klatek na sekundę (< 1). Jest to szczególnie przydatne w przypadku filmów statycznych (np. wykładów). Użyj wyższej liczby klatek na sekundę w przypadku filmów wymagających szczegółowej analizy czasowej, takich jak analiza szybkich akcji lub śledzenie ruchu z dużą prędkością.

## Obsługiwane formaty wideo

Gemini obsługuje te typy MIME formatów wideo:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Szczegóły techniczne dotyczące filmów

- **Obsługiwane modele i kontekst**: wszystkie modele Gemini mogą przetwarzać dane wideo.
  - Modele z oknem kontekstu o rozmiarze 1 mln tokenów mogą domyślnie przetwarzać filmy o długości do 3 godzin (przy niskiej rozdzielczości mediów) lub do 1 godziny (przy wysokiej rozdzielczości mediów).
- **Tryby przetwarzania**: modele Gemini 4 Argon, 3.8 Flash, 3.6 Flash, 3.5 Flash Lite,
  i nowsze obsługują 2 tryby przetwarzania wideo:
  - **Statyczny**: klatki są wyodrębniane z szybkością 1 FPS i umieszczane w kontekście (domyślne
    dla wszystkich modeli). Dźwięk jest przetwarzany z szybkością 1 kb/s (jeden kanał).
    Sygnatury czasowe są dodawane co sekundę. Najlepsze w przypadku krótkich klipów lub gdy liczy się każda klatka (np. podczas sprawdzania klatka po klatce). Pamiętaj, że sekwencje szybkich akcji mogą utracić szczegóły ze względu na szybkość próbkowania 1 kl./s.
  - **Rozwiązania agentowe**: model dynamicznie porusza się po filmie, wczytując
    transkrypcję, klatki lub dźwięk na żądanie. W przypadku długich treści zużywa to do 88% mniej tokenów, ale poruszanie się po osi czasu może zwiększyć czas do pierwszego tokena (TTFT) i całkowite zużycie tokenów w przypadku krótkich klipów (poniżej 5 minut) lub ogólnych zapytań ze względu na wewnętrzne rozumowanie i wywołania narzędzi.
    Odpowiedzi zawierają części wywołań i odpowiedzi narzędzi `MEDIA_PROCESSING`, aby zachować kontekst rozumowania w kolejnych turach. Najlepsze w przypadku długich filmów i zapytań ukierunkowanych na optymalizację kosztów tokenów i jakości odpowiedzi. Obsługiwane w Gemini 4 Argon, 3.8 Flash, 3.6 Flash i 3.5 Flash Lite. Więcej informacji znajdziesz w sekcji
    [Analizowanie filmów przez agenta](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=pl#agentic-video-understanding).
- **Obliczanie tokenów (tryb statyczny)**: każda sekunda filmu jest tokenizowana w ten sposób:
  w następujący sposób:
  - Pojedyncze klatki (próbkowane z szybkością 1 kl./s):
    - Jeśli `media_resolution` jest ustawiona na niską, klatki są tokenizowane z szybkością 66 tokenów na klatkę.
    - W przeciwnym razie klatki są tokenizowane z szybkością 258 tokenów na klatkę.
  - Dźwięk: 32 tokeny na sekundę.
  - Metadane są też uwzględniane.
  - Łącznie: około 100 tokenów na sekundę filmu przy domyślnej (niskiej) rozdzielczości mediów lub około 300 tokenów na sekundę filmu przy wysokiej rozdzielczości mediów.
- **Obliczanie tokenów (tryb agentowy)**: zużycie tokenów zależy od złożoności treści
  i strategii nawigacji modelu. Tokeny rozumowania nawigacji
  generowane podczas eksploracji filmu są traktowane jako **tokeny myślenia**
  (`thoughts_token_count`), a klatki, dźwięk i transkrypcja wczytywane na
  żądanie są traktowane jako tokeny promptów narzędzi (`tool_use_prompt_token_count`).
  Przetwarzanie przez agenta zwykle zużywa do 88% mniej tokenów niż przetwarzanie
  statyczne w przypadku długich treści, ponieważ model wczytuje tylko transkrypcję,
  klatki lub dźwięk, których potrzebuje do odpowiedzi na prompta (patrz
  [przewodnik po tokenach](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=pl#video-token-usage)).
- **Rozdzielczość mediów**: Gemini 3 wprowadza szczegółową kontrolę nad przetwarzaniem multimodalnym
  za pomocą parametru `media_resolution`. Parametr `media_resolution` określa **maksymalną liczbę tokenów przydzielonych na obraz wejściowy lub klatkę wideo**. Wyższe rozdzielczości zwiększają zdolność modelu do odczytywania drobnego tekstu lub identyfikowania małych szczegółów, ale zwiększają zużycie tokenów i opóźnienia. Parametry `media_resolution` i `media_processing` są niezależne: możesz ustawić oba w tej samej części wideo.

Więcej informacji o obliczaniu tokenów znajdziesz w
[przewodniku po tokenach](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=pl).

- **Format sygnatury czasowej**: gdy w prompcie odwołujesz się do konkretnych momentów w filmie, użyj formatu `MM:SS` (np. `01:15` dla 1 minuty i 15 sekund).
- **Umieszczanie prompta**: jeśli łączysz tekst i pojedynczy film, umieść prompta tekstowego
  *po* części wideo w tablicy `contents`.
- **Limity czasu w przypadku długich żądań**: w przypadku filmów, które wymagają dłuższego
  czasu przetwarzania lub złożonego rozumowania wieloetapowego, użyj przesyłania strumieniowego
  (`client.models.generate_content_stream`). Synchroniczne żądania bez przesyłania strumieniowego,
  które w przypadku dużego zapotrzebowania powodują ponawianie prób przez backend, mogą przekroczyć
  okna ważności połączenia lub tokena uwierzytelniania, co może powodować
  nieoczekiwane `401 Unauthorized` lub przekroczenia limitu czasu. Przesyłanie strumieniowe utrzymuje aktywne połączenie i wyświetla pośrednie kroki rozumowania oraz postęp wywołań narzędzi.

## Co dalej?

- [Rozdzielczość mediów](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=pl): kontroluj
  rozdzielczość klatek wideo, aby zrównoważyć jakość i zużycie tokenów.
- [Tokeny](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=pl): dowiedz się, jak treści wideo są tokenizowane
  w trybie statycznym i agentowym.
- [Instrukcje systemowe](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=pl#system-instructions):
  Instrukcje systemowe pozwalają sterować działaniem modelu na podstawie
  konkretnych potrzeb i przypadków użycia.
- [Interfejs API plików](https://ai.google.dev/gemini-api/docs/files?hl=pl): dowiedz się więcej o przesyłaniu plików i zarządzaniu nimi na potrzeby Gemini.
- [Strategie tworzenia promptów plików](https://ai.google.dev/gemini-api/docs/files?hl=pl#prompt-guide): Gemini API obsługuje tworzenie promptów za pomocą danych tekstowych, graficznych, dźwiękowych i wideo, czyli tworzenie promptów multimodalnych.
- [Wskazówki dotyczące bezpieczeństwa](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pl): modele generatywnej AI
  czasami generują nieoczekiwane wyniki, np. niedokładne,
  stronnicze lub obraźliwe. Przetwarzanie końcowe i ocena przez człowieka są niezbędne, aby ograniczyć ryzyko szkód wynikających z takich danych wyjściowych.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-13 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-13 UTC."],[],[]]
