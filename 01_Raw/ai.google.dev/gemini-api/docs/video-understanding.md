---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl
fetched_at: 2026-08-24T02:19:24.764717+00:00
title: "Rozpoznawanie film\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Rozpoznawanie filmów

> Więcej informacji o generowaniu filmów znajdziesz w przewodniku [Veo](https://ai.google.dev/gemini-api/docs/video?hl=pl).

Modele Gemini mogą przetwarzać filmy, co umożliwia programistom korzystanie z wielu nowych przypadków użycia, które wcześniej wymagałyby modeli specyficznych dla danej domeny.
Niektóre funkcje Gemini Vision obejmują możliwość opisywania, segmentowania i wyodrębniania informacji z filmów, odpowiadania na pytania dotyczące treści filmów oraz odwoływania się do konkretnych sygnatur czasowych w filmie.

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
import base64
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
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
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

Zawsze używaj Files API, gdy łączny rozmiar żądania (w tym pliku, prompta tekstowego, instrukcji systemowych itp.) jest większy niż 20 MB, czas trwania filmu jest znaczący lub jeśli zamierzasz użyć tego samego filmu w wielu promptach.
File API bezpośrednio akceptuje formaty plików wideo.

Więcej informacji o pracy z plikami multimedialnymi znajdziesz w artykule
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

### Przekazywanie danych wideo w treści

Zamiast przesyłać plik wideo za pomocą File API, możesz przekazywać mniejsze filmy bezpośrednio w żądaniu. Jest to odpowiednie w przypadku krótszych filmów o łącznym rozmiarze żądania poniżej 20 MB.

Oto przykład przekazywania danych wideo w treści:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.6-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### Przekazywanie adresów URL z YouTube

Adresy URL z YouTube możesz przekazywać bezpośrednio do Gemini API w ramach żądania w ten sposób:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.6-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**Ograniczenia:**

- W przypadku bezpłatnego planu nie możesz przesyłać więcej niż 8 godzin filmów na YouTube dziennie.
- W przypadku płatnego planu nie ma limitu opartego na długości wideo.
- W przypadku modeli wcześniejszych niż Gemini 2.5 możesz przesłać tylko 1 film na żądanie. W przypadku modeli Gemini 2.5 i nowszych możesz przesłać maksymalnie 10 filmów na żądanie.
- Możesz przesyłać tylko filmy publiczne (nie prywatne ani niepubliczne).

## Odwoływanie się do sygnatur czasowych w treści

Możesz zadawać pytania dotyczące konkretnych momentów w filmie, używając sygnatur czasowych w formacie `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Wyodrębnianie szczegółowych informacji z filmu

Modele Gemini oferują zaawansowane możliwości rozumienia treści wideo dzięki przetwarzaniu informacji z **ścieżek audio i wizualnych**. Dzięki temu możesz wyodrębnić bogaty zestaw szczegółów, w tym generować opisy tego, co dzieje się w filmie, i odpowiadać na pytania dotyczące jego treści.

W przypadku opisów wizualnych model próbkuje film z szybkością **1 klatki na sekundę** (FPS). Ta domyślna szybkość próbkowania sprawdza się w przypadku większości treści, ale pamiętaj, że może pomijać szczegóły w filmach z szybkim ruchem lub szybkimi zmianami scen.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Obsługiwane formaty wideo

Gemini obsługuje te typy MIME formatów wideo:

- `video/mp4`
- `video/mpeg`
- `video/mov`
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
  - Te stawki mogą ulec zmianie w przyszłości w celu poprawy wnioskowania.
- **Obliczanie tokenów**: każda sekunda filmu jest tokenizowana w ten sposób:
  - Pojedyncze klatki (próbkowane z szybkością 1 klatki na sekundę):
    - Jeśli `media_resolution` jest ustawiona na low, klatki są tokenizowane z szybkością 66 tokenów na klatkę.
    - W przeciwnym razie klatki są tokenizowane z szybkością 258 tokenów na klatkę.
  - Dźwięk: 32 tokeny na sekundę.
  - Metadane są też uwzględniane.
  - Łącznie: około 300 tokenów na sekundę filmu w domyślnej rozdzielczości multimediów lub 100 tokenów na sekundę filmu w niskiej rozdzielczości multimediów.
- **Rozdzielczość multimediów**: Gemini 3 wprowadza szczegółową kontrolę nad przetwarzaniem multimodalnym
  za pomocą parametru `media_resolution`. Parametr `media_resolution` określa **maksymalną liczbę tokenów przydzielonych na obraz wejściowy lub klatkę wideo**.
  Wyższe rozdzielczości zwiększają zdolność modelu do odczytywania drobnego tekstu lub identyfikowania małych szczegółów, ale zwiększają też zużycie tokenów i opóźnienie.

  Więcej informacji o obliczaniu tokenów znajdziesz w przewodniku [Tokeny](https://ai.google.dev/gemini-api/docs/tokens?hl=pl).
- **Format sygnatury czasowej**: gdy w prompcie odwołujesz się do konkretnych momentów w filmie, użyj formatu `MM:SS` (np. `01:15` oznacza 1 minutę i 15 sekund).
- **Sprawdzone metody**:

  - Aby uzyskać optymalne wyniki, używaj tylko 1 filmu na żądanie prompta.
  - Jeśli łączysz tekst i pojedynczy film, umieść prompt tekstowy *po* części wideo w tablicy `input`.
  - Pamiętaj, że szybkie sekwencje akcji mogą utracić szczegóły ze względu na szybkość próbkowania wynoszącą 1 klatkę na sekundę. W razie potrzeby rozważ spowolnienie takich klipów.

## Co dalej?

Z tego przewodnika dowiesz się, jak przesyłać pliki wideo i generować dane wyjściowe w postaci tekstu na podstawie danych wejściowych wideo. Więcej informacji znajdziesz w tych materiałach:

- [Instrukcje systemowe](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#system-instructions):
  Instrukcje systemowe pozwalają sterować zachowaniem modelu na podstawie konkretnych potrzeb i przypadków użycia.
- [Interfejs API plików](https://ai.google.dev/gemini-api/docs/files?hl=pl): dowiedz się więcej o przesyłaniu plików i zarządzaniu nimi na potrzeby Gemini.
- [Strategie tworzenia promptów plików](https://ai.google.dev/gemini-api/docs/files?hl=pl#prompt-guide): Gemini API obsługuje tworzenie promptów za pomocą danych tekstowych, obrazów, dźwięku i wideo, czyli tworzenie promptów multimodalnych.
- [Wskazówki dotyczące bezpieczeństwa](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pl): modele generatywnej
  AI czasami generują nieoczekiwane dane wyjściowe, np. nieprawidłowe,
  stronnicze lub obraźliwe. Przetwarzanie końcowe i ocena przez człowieka są niezbędne, aby
  ograniczyć ryzyko szkód wynikających z takich danych wyjściowych.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
