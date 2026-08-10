---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=pl
fetched_at: 2026-08-10T03:22:59.493053+00:00
title: "Rozpoznawanie film\u00f3w \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Rozpoznawanie filmów

> Więcej informacji o generowaniu filmów znajdziesz w przewodniku [Veo](https://ai.google.dev/gemini-api/docs/video?hl=pl).

Modele Gemini mogą przetwarzać filmy, co umożliwia programistom korzystanie z wielu nowych przypadków użycia, które wcześniej wymagałyby modeli specyficznych dla danej domeny.
Niektóre funkcje Gemini Vision obejmują możliwość opisywania, segmentowania i wyodrębniania informacji z filmów, odpowiadania na pytania dotyczące treści wideo oraz odwoływania się do konkretnych sygnatur czasowych w filmie.

Filmy możesz przekazywać do Gemini na te sposoby:

| Sposób wprowadzania tekstu | Wielkość maksymalna | Zalecany przypadek użycia |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (płatne) / 2 GB (bezpłatne) | Duże pliki (ponad 100 MB), długie filmy (ponad 10 minut), pliki wielokrotnego użytku. |
| [Rejestracja w Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl#registration) | 2 GB (na plik, bez limitów miejsca na dane) | Duże pliki (ponad 100 MB), długie filmy (ponad 10 minut), trwałe pliki wielokrotnego użytku. |
| [Dane w treści](#inline-video) | < 100 MB | Małe pliki (poniżej 100 MB), krótkie filmy (poniżej 1 minuty), jednorazowe dane wejściowe. |
| [Adresy URL z YouTube](#youtube) | Nie dotyczy | Publiczne filmy w YouTube. |

> **Uwaga:** w większości przypadków zalecamy korzystanie z [File API](#upload-video), zwłaszcza w przypadku plików większych niż 100 MB lub gdy chcesz użyć tego samego pliku w wielu żądaniach.

Więcej informacji o innych metodach wprowadzania plików, takich jak używanie zewnętrznych adresów URL lub plików
przechowywanych w Google Cloud, znajdziesz w przewodniku
[Metody wprowadzania plików](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl).

### Przesyłanie pliku wideo

Poniższy kod pobiera przykładowy film, przesyła go za pomocą [Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl),
czeka na jego przetworzenie, a następnie używa odniesienia do przesłanego pliku, aby
podsumować film.

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

Zawsze używaj Files API, gdy łączny rozmiar żądania (w tym pliku, prompta tekstowego, instrukcji systemowych itp.) przekracza 20 MB, czas trwania filmu jest znaczny lub gdy zamierzasz użyć tego samego filmu w wielu promptach.
File API bezpośrednio akceptuje formaty plików wideo.

Więcej informacji o pracy z plikami multimedialnymi znajdziesz w artykule
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

### Przekazywanie danych wideo w treści

Zamiast przesyłać plik wideo za pomocą File API, możesz przekazywać mniejsze filmy bezpośrednio w żądaniu do `generateContent`. Jest to odpowiednie rozwiązanie w przypadku krótszych filmów, których łączny rozmiar żądania nie przekracza 20 MB.

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

### Przekazywanie adresów URL z YouTube

Adresy URL z YouTube możesz przekazywać bezpośrednio do Gemini API w ramach żądania w ten sposób:

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

**Ograniczenia:**

- W przypadku bezpłatnego planu nie możesz przesyłać więcej niż 8 godzin filmów na YouTube dziennie.
- W przypadku płatnego planu nie ma limitu opartego na długości wideo.
- W przypadku modeli wcześniejszych niż Gemini 2.5 możesz przesłać tylko 1 film na żądanie. W przypadku modeli Gemini 2.5 i nowszych możesz przesłać maksymalnie 10 filmów na żądanie.
- Możesz przesyłać tylko filmy publiczne (nie prywatne ani niepubliczne).

## Używanie buforowania kontekstu w przypadku długich filmów

W przypadku filmów dłuższych niż 10 minut lub gdy planujesz wysłać wiele żądań
dotyczących tego samego pliku wideo, użyj [buforowania kontekstu](https://ai.google.dev/gemini-api/docs/caching?hl=pl) aby
zmniejszyć koszty i skrócić czas oczekiwania. Buforowanie kontekstu umożliwia jednokrotne przetworzenie filmu i ponowne wykorzystanie tokenów w kolejnych zapytaniach, co jest idealne w przypadku sesji czatu lub powtarzanej analizy długich treści.

## Odwoływanie się do sygnatur czasowych w treści

Możesz zadawać pytania dotyczące konkretnych momentów w filmie, używając sygnatur czasowych w formacie `MM:SS`.

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

## Wyodrębnianie szczegółowych informacji z filmu

Modele Gemini oferują zaawansowane możliwości rozumienia treści wideo dzięki przetwarzaniu informacji ze strumieni **audio i wizualnych**. Dzięki temu możesz wyodrębnić bogaty zestaw szczegółów, w tym generować opisy tego, co dzieje się w filmie, i odpowiadać na pytania dotyczące jego treści.

W przypadku opisów wizualnych model próbkuje film z szybkością **1 klatki na sekundę** (FPS). Ta domyślna szybkość próbkowania sprawdza się w przypadku większości treści, ale pamiętaj, że może pomijać szczegóły w filmach z szybkim ruchem lub szybkimi zmianami scen.
W przypadku takich treści z szybkim ruchem rozważ [ustawienie niestandardowej liczby klatek na sekundę](#custom-frame-rate).

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

## Dostosowywanie przetwarzania wideo

Przetwarzanie wideo w Gemini API możesz dostosować, ustawiając interwały przycinania lub podając niestandardową liczbę klatek na sekundę.

 

### Ustawianie interwałów przycinania

Możesz przycinać filmy, określając `videoMetadata` z przesunięciami początku i końca.

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

### Ustawianie niestandardowej liczby klatek na sekundę

Niestandardowe próbkowanie liczby klatek na sekundę możesz ustawić, przekazując argument `fps` do `videoMetadata`.

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

Domyślnie z filmu próbkowana jest 1 klatka na sekundę. W przypadku długich filmów możesz ustawić niską wartość FPS (< 1). Jest to szczególnie przydatne w przypadku filmów statycznych (np. wykładów). Użyj wyższej wartości FPS w przypadku filmów wymagających szczegółowej analizy czasowej, takich jak zrozumienie szybkiej akcji lub śledzenie ruchu z dużą prędkością.

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

- **Obsługiwane modele i kontekst:** wszystkie modele Gemini mogą przetwarzać dane wideo.
  - Modele z oknem kontekstu o rozmiarze 1 mln tokenów mogą przetwarzać filmy o długości do 1 godziny w domyślnej rozdzielczości multimediów lub do 3 godzin w niskiej rozdzielczości multimediów.
- **Przetwarzanie za pomocą File API**: w przypadku korzystania z File API filmy są przechowywane z szybkością 1
  klatki na sekundę, a dźwięk jest przetwarzany z szybkością 1 kb/s (jeden kanał).
  Sygnatury czasowe są dodawane co sekundę.
  - Te wartości mogą ulec zmianie w przyszłości w celu poprawy wnioskowania.
  - Szybkość próbkowania 1 FPS możesz zastąpić, [ustawiając niestandardową liczbę klatek na sekundę](#custom-frame-rate).
- **Obliczanie tokenów**: każda sekunda filmu jest tokenizowana w ten sposób:
  - Pojedyncze klatki (próbkowane z szybkością 1 FPS):
    - Jeśli [`mediaResolution`](https://ai.google.dev/api/generate-content?hl=pl#MediaResolution) jest ustawiona
      na niską, klatki są tokenizowane z szybkością 66 tokenów na klatkę.
    - W przeciwnym razie klatki są tokenizowane z szybkością 258 tokenów na klatkę.
  - Dźwięk: 32 tokeny na sekundę.
  - Metadane są też uwzględniane.
  - Łącznie: około 300 tokenów na sekundę filmu w domyślnej rozdzielczości multimediów lub 100 tokenów na sekundę filmu w niskiej rozdzielczości multimediów.
- **Rozdzielczość multimediów**: Gemini 3 wprowadza szczegółową kontrolę nad przetwarzaniem multimodalnym
  za pomocą parametru `media_resolution`. Parametr `media_resolution` określa **maksymalną liczbę tokenów przydzielonych na obraz wejściowy lub klatkę wideo**.
  Wyższe rozdzielczości zwiększają zdolność modelu do odczytywania drobnego tekstu lub identyfikowania małych szczegółów, ale zwiększają też zużycie tokenów i czas oczekiwania.

  Więcej informacji o tym parametrze i jego wpływie na obliczanie tokenów
  znajdziesz w przewodniku [Rozdzielczość multimediów](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=pl).
- **Format sygnatury czasowej**: gdy w prompcie odwołujesz się do konkretnych momentów w filmie, użyj formatu `MM:SS` (np. `01:15` oznacza 1 minutę i 15 sekund).
- **Sprawdzone metody**:

  - Aby uzyskać optymalne wyniki, używaj tylko 1 filmu na żądanie prompta.
  - Jeśli łączysz tekst i pojedynczy film, umieść prompta tekstowego *po* części wideo w tablicy `contents`.
  - Pamiętaj, że sekwencje szybkiej akcji mogą utracić szczegóły ze względu na szybkość próbkowania 1 FPS. W razie potrzeby rozważ spowolnienie takich klipów.

## Co dalej?

Z tego przewodnika dowiesz się, jak przesyłać pliki wideo i generować dane wyjściowe w postaci tekstu na podstawie danych wejściowych wideo. Więcej informacji znajdziesz w tych materiałach:

- [Instrukcje systemowe](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#system-instructions):
  Instrukcje systemowe pozwalają sterować działaniem modelu na podstawie
  konkretnych potrzeb i przypadków użycia.
- [Interfejs API plików](https://ai.google.dev/gemini-api/docs/files?hl=pl): dowiedz się więcej o przesyłaniu plików i zarządzaniu nimi na potrzeby Gemini.
- [Strategie tworzenia promptów plików](https://ai.google.dev/gemini-api/docs/files?hl=pl#prompt-guide): Gemini API obsługuje tworzenie promptów z danymi tekstowymi, obrazami, dźwiękiem i filmami, czyli tworzenie promptów multimodalnych.
- [Wskazówki dotyczące bezpieczeństwa](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pl): modele generatywnej
  AI czasami generują nieoczekiwane dane wyjściowe, takie jak dane nieprawidłowe,
  obciążone lub obraźliwe. Przetwarzanie końcowe i ocena przez człowieka są niezbędne, aby
  ograniczyć ryzyko szkód spowodowanych przez takie dane wyjściowe.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
