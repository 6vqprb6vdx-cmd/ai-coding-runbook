---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl
fetched_at: 2026-06-01T19:46:36.356085+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Metody wprowadzania plików

W tym przewodniku opisujemy różne sposoby dołączania plików multimedialnych, takich jak obrazy, dźwięk, wideo i dokumenty, podczas wysyłania żądań do Gemini API.
Nowe metody są obsługiwane we wszystkich punktach końcowych Gemini API, w tym w interfejsach
Batch, Interactions i Live API.
Wybór odpowiedniej metody zależy od rozmiaru pliku, miejsca, w którym są obecnie przechowywane dane, oraz częstotliwości korzystania z pliku.

Najprostszym sposobem na dołączenie pliku jako danych wejściowych jest odczytanie pliku lokalnego i dołączenie go do prompta. Poniższy przykład pokazuje, jak odczytać lokalny plik PDF. W przypadku tej metody rozmiar plików PDF jest ograniczony do 50 MB. Pełną listę typów i limitów danych wejściowych znajdziesz w
[tabeli porównania metod wprowadzania](#method-comparison).

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3.5-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt
  ]
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const ai = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = path.join('content', 'my_local_file.pdf'); // Adjust path as needed

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: fs.readFileSync(filePath).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.5-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Summarize this document"}
        ]
      },
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "application/pdf",
              "data": "'"${B64_CONTENT}"'"
            }
          }
        ]
      }
    ]
  }'
```

## Porównanie metod wprowadzania

W tabeli poniżej porównujemy poszczególne metody wprowadzania z limitami plików i najlepszymi przypadkami użycia. Pamiętaj, że limit rozmiaru pliku może się różnić w zależności od typu pliku oraz modelu lub tokenizera używanego do przetwarzania pliku.

| Metoda | Urządzenia | Maks. rozmiar pliku | Trwałość |
| --- | --- | --- | --- |
| **Dane w treści** | Szybkie testowanie, małe pliki, aplikacje działające w czasie rzeczywistym. | 100 MB na żądanie lub ładunek   (**50 MB w przypadku plików PDF**) | Brak (wysyłane z każdym żądaniem) |
| **Przesyłanie plików za pomocą interfejsu File API** | Duże pliki, pliki używane wielokrotnie. | 2 GB na plik,   do 20 GB na projekt | 48 godzin |
| **Rejestracja URI GCS za pomocą interfejsu File API** | Duże pliki, które są już w Google Cloud Storage, pliki używane wielokrotnie. | 2 GB na plik, brak ogólnych limitów miejsca na dane | Brak (pobierane na żądanie). Jednorazowa rejestracja może zapewnić dostęp na maksymalnie 30 dni. |
| **Zewnętrzne adresy URL** | Dane publiczne lub dane w zasobnikach w chmurze (AWS, Azure, GCS) bez ponownego przesyłania. | 100 MB na żądanie lub ładunek | Brak (pobierane na żądanie) |

## Dane w treści

W przypadku mniejszych plików (poniżej 100 MB lub 50 MB w przypadku plików PDF) możesz przekazywać dane bezpośrednio w ładunku żądania. Jest to najprostsza metoda do szybkich testów lub aplikacji obsługujących dane tymczasowe w czasie rzeczywistym. Dane możesz podawać jako ciągi znaków zakodowane w formacie base64 lub odczytując bezpośrednio pliki lokalne.

Przykład odczytywania z pliku lokalnego znajdziesz na początku tej strony.

### Pobieranie z adresu URL

Możesz też pobrać plik z adresu URL, przekonwertować go na bajty i dołączyć do danych wejściowych.

### Python

```
from google import genai
from google.genai import types
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

response = client.models.generate_content(
  model="gemini-3.5-flash",
  contents=[
      types.Part.from_bytes(
        data=doc_data,
        mime_type='application/pdf',
      ),
      prompt
  ]
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl);
      .then((response) => response.arrayBuffer());

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: Buffer.from(pdfResp).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.5-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
```

### REST

```
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Generate content using the base64 encoded PDF
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"inline_data": {"mime_type": "application/pdf", "data": "'"$ENCODED_PDF"'"}},
          {"text": "'$PROMPT'"}
        ]
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Gemini File API

File API jest przeznaczony do większych plików (do 2 GB) lub plików, których chcesz używać w wielu żądaniach.

### Standardowe przesyłanie plików

Prześlij plik lokalny do Gemini API. Pliki przesłane w ten sposób są przechowywane tymczasowo (48 godzin) i przetwarzane w celu efektywnego pobierania przez model.

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[prompt, audio_file]
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
const prompt = "Describe this audio clip";

async function main() {
  const filePath = "path/to/your/sample.mp3"; // Adjust path as needed

  const myfile = await ai.files.upload({
    file: filePath,
    config: { mimeType: "audio/mpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(myfile.uri, myfile.mimeType),
    ]),
  });
  console.log(response.text);

}
await main();
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D "${tmp_header_file}" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

### Rejestrowanie plików w Google Cloud Storage

Jeśli Twoje dane są już w Google Cloud Storage, nie musisz ich pobierać ani przesyłać ponownie. Możesz je zarejestrować bezpośrednio za pomocą File API.

1. Przyznaj **agentowi usługi** dostęp do każdego zasobnika

   1. Włącz Gemini API w projekcie w chmurze Google.
   2. Utwórz agenta usługi:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Przyznaj agentowi usługi Gemini API uprawnienia** do odczytu zasobników pamięci masowej.

      Użytkownik musi przypisać agentowi usługi rolę `Storage Object Viewer`
      [IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=pl#storage.objectViewer)
      w konkretnych zasobnikach, których chce używać.

   Ten dostęp domyślnie nie wygasa, ale można go w każdej chwili zmienić. Do przyznawania uprawnień możesz
   też używać
   [poleceń pakietu SDK Google Cloud Storage IAM](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=pl).
2. Uwierzytelnij usługę

   **Wymagania wstępne**

   - Włącz API
   - Utwórz konto usługi lub agenta z odpowiednimi uprawnieniami.

   Najpierw musisz uwierzytelnić się jako usługa, która ma uprawnienia do wyświetlania obiektów Cloud Storage. Sposób uwierzytelniania zależy od środowiska, w którym będzie działać kod zarządzania plikami.

   **Poza Google Cloud**

   Jeśli kod działa poza Google Cloud, np. na komputerze, pobierz dane logowania konta z konsoli Google Cloud, wykonując te czynności:

   1. Otwórz konsolę [kont usługi](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=pl).
   2. Wybierz odpowiednie konto usługi.
   3. Kliknij kartę **Klucze i wybierz **Dodaj klucz** > Utwórz nowy klucz**.
   4. Wybierz typ klucza **JSON** i zanotuj, gdzie plik został pobrany na komputerze.

   Więcej informacji znajdziesz w oficjalnej dokumentacji Google Cloud na temat [zarządzania kluczami kont usługi](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=pl).

   Następnie użyj tych poleceń, aby się uwierzytelnić. Zakładamy, że plik konta usługi znajduje się w bieżącym katalogu i ma nazwę `service-account.json`.

   ### Python

   ```
   from google.oauth2.service_account import Credentials

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   SERVICE_ACCOUNT_FILE = 'service-account.json'

   credentials = Credentials.from_service_account_file(
       SERVICE_ACCOUNT_FILE,
       scopes=GCS_READ_SCOPES
   )
   ```

   ### JavaScript

   ```
   const { GoogleAuth } = require('google-auth-library');

   const GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ];

   const SERVICE_ACCOUNT_FILE = 'service-account.json';

   const auth = new GoogleAuth({
     keyFile: SERVICE_ACCOUNT_FILE,
     scopes: GCS_READ_SCOPES
   });
   ```

   ### CLI

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **W Google Cloud**

   Jeśli korzystasz bezpośrednio z Google Cloud, np. używasz funkcji [Cloud
   Run](https://cloud.google.com/functions?hl=pl) lub instancji
   [Compute Engine](https://cloud.google.com/products/compute?hl=pl), będziesz
   mieć niejawne dane logowania, ale musisz ponownie się uwierzytelnić, aby przyznać
   odpowiednie zakresy.

   ### Python

   Ten kod zakłada, że usługa działa w środowisku, w którym
   [domyślne uwierzytelnianie aplikacji](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=pl)
   można automatycznie uzyskać, np. w Cloud Run lub Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   Ten kod zakłada, że usługa działa w środowisku, w którym
   [domyślne uwierzytelnianie aplikacji](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=pl)
   można automatycznie uzyskać, np. w Cloud Run lub Compute Engine.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

   ### CLI

   Jest to polecenie interaktywne. W przypadku usług takich jak Compute Engine możesz dołączyć zakresy do działającej usługi na poziomie konfiguracji. [Przykład znajdziesz w dokumentacji usługi zarządzanej przez użytkownika.](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=pl#using)

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Rejestracja pliku (Files API)

   Użyj Files API, aby zarejestrować pliki i utworzyć ścieżkę Files API, której można bezpośrednio używać w Gemini API.

   ### Python

   ```
   from google import genai
   from google.genai.types import Part

   # Note that you must provide an API key in the GEMINI_API_KEY
   # environment variable, but it is unused for the registration endpoint.
   client = genai.Client()

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"],
       # Use the credentials obtained in the previous step.
       auth=credentials
   )
   prompt = "Summarize this file."

   # call generateContent for each file
   for f in registered_gcs_files.files:
     print(f.name)
     response = client.models.generate_content(
       model="gemini-3.5-flash",
       contents=[Part.from_uri(
         file_uri=f.uri,
         mime_type=f.mime_type,
       ),
       prompt],
     )
     print(response.text)
   ```

   ### CLI

   ```
   access_token=$(gcloud auth application-default print-access-token)
   project_id=$(gcloud config get-value project)
   curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
       -H 'Content-Type: application/json' \
       -H "Authorization: Bearer ${access_token}" \
       -H "x-goog-user-project: ${project_id}" \
       -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
   ```

## Zewnętrzne adresy URL HTTP / podpisane adresy URL

Możesz przekazywać publicznie dostępne adresy URL HTTPS lub wstępnie podpisane adresy URL (zgodne z
[wstępnie podpisanymi
adresami URL S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html)
i Azure SAS) bezpośrednio w żądaniu generowania. Gemini API bezpiecznie pobierze treści podczas przetwarzania. Jest to idealne rozwiązanie w przypadku plików o rozmiarze do 100 MB, których nie chcesz przesyłać ponownie.

Możesz używać publicznych lub podpisanych adresów URL jako danych wejściowych, umieszczając je w polu `file_uri`.

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[
        Part.from_uri(
            file_uri=uri,
            mime_type="application/pdf",
        ),
        prompt
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, createPartFromUri } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const response = await client.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: [
      // equivalent to Part.from_uri(file_uri=uri, mime_type="...")
      createPartFromUri(uri, "application/pdf"),
      "summarize this file",
    ],
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "contents":[
            {
              "parts":[
                {"text": "Summarize this pdf"},
                {
                  "file_data": {
                    "mime_type":"application/pdf",
                    "file_uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
                  }
                }
              ]
            }
          ]
        }'
```

### Ułatwienia dostępu

Sprawdź, czy podane adresy URL nie prowadzą do stron, które wymagają logowania lub są umieszczone w sekcji płatnej. W przypadku prywatnych baz danych utwórz podpisany adres URL z odpowiednimi uprawnieniami dostępu i datą ważności.

### Testy zabezpieczeń

System przeprowadza kontrolę moderacji treści pod kątem zgodności z zasadami i standardami bezpieczeństwa (np. treści, które nie są wyłączone i nie są umieszczone w sekcji płatnej). Jeśli podany adres URL nie przejdzie tego testu, otrzymasz wartość `url_retrieval_status` równą `URL_RETRIEVAL_STATUS_UNSAFE`.

### Obsługiwane typy treści

Ta lista obsługiwanych typów plików i ograniczeń ma charakter wstępny i nie jest wyczerpująca. Efektywny zestaw obsługiwanych typów może się zmieniać i różnić w zależności od konkretnego modelu oraz wersji tokenizera. Nieobsługiwane typy spowodują błąd.
Ponadto pobieranie treści w przypadku tych typów plików obsługuje obecnie tylko publicznie dostępne adresy URL.

#### Typy plików tekstowych

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Typy plików aplikacji

- `application/json`
- `application/pdf`

#### Typy plików graficznych

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### Typy plików wideo

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Sprawdzone metody

- **Wybierz odpowiednią metodę:** w przypadku małych, tymczasowych plików używaj danych w treści.
  W przypadku większych lub często używanych plików używaj File API. W przypadku danych, które są już hostowane online, używaj zewnętrznych adresów URL.
- **Określ typy MIME:** zawsze podawaj prawidłowy typ MIME danych pliku, aby zapewnić prawidłowe przetwarzanie.
- **Obsługuj błędy:** zaimplementuj w kodzie obsługę błędów, aby zarządzać potencjalnymi problemami, takimi jak awarie sieci, problemy z dostępem do plików lub błędy interfejsu API.
- **Zarządzaj uprawnieniami GCS:** jeśli używasz rejestracji GCS, przyznaj agentowi usługi Gemini
  API tylko niezbędną rolę `Storage Object Viewer` w konkretnych
  zasobnikach.
- **Zabezpiecz podpisane adresy URL:** upewnij się, że podpisane adresy URL mają odpowiedni czas ważności i ograniczone uprawnienia.

## Ograniczenia

- Limity rozmiaru pliku różnią się w zależności od metody (patrz [tabela porównania](#method-comparison))
  i typu pliku.
- Dane w treści zwiększają rozmiar ładunku żądania.
- Przesyłanie plików za pomocą File API jest tymczasowe i wygasa po 48 godzinach.
- Pobieranie zewnętrznych adresów URL jest ograniczone do 100 MB na ładunek i obsługuje określone typy treści.
- Rejestracja w Google Cloud Storage wymaga prawidłowej konfiguracji IAM i zarządzania tokenami OAuth.

## Co dalej?

- Spróbuj napisać własne prompty multimodalne za pomocą
  [Google AI Studio](http://aistudio.google.com/?hl=pl).
- Informacje o dołączaniu plików do promptów znajdziesz w przewodnikach dotyczących przetwarzania
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=pl),
  [dźwięku](https://ai.google.dev/gemini-api/docs/audio?hl=pl) i
  [dokumentów](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl).
- Więcej wskazówek dotyczących projektowania promptów, np. dostrajania parametrów próbkowania, znajdziesz w
  [przewodniku po strategiach tworzenia promptów](https://ai.google.dev/gemini-api/docs/prompt-strategies?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-01 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-01 UTC."],[],[]]
