---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl
fetched_at: 2026-09-21T05:55:25.558970+00:00
title: "Metody wprowadzania plik\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Metody wprowadzania plików

W tym przewodniku wyjaśniamy różne sposoby dołączania plików multimedialnych, takich jak obrazy, dźwięk, wideo i dokumenty, podczas wysyłania żądań do interfejsu Gemini API.
Nowe metody są obsługiwane we wszystkich punktach końcowych interfejsu Gemini API, w tym w interfejsach Batch, Interactions i Live API.
Wybór odpowiedniej metody zależy od rozmiaru pliku, miejsca przechowywania danych i częstotliwości korzystania z pliku.

Najprostszym sposobem na uwzględnienie pliku jako danych wejściowych jest odczytanie pliku lokalnego i uwzględnienie go w prompcie. Poniższy przykład pokazuje, jak odczytać lokalny plik PDF. W przypadku tej metody rozmiar plików PDF jest ograniczony do 50 MB. Pełną listę typów plików wejściowych i limitów znajdziesz w [tabeli porównawczej metod wprowadzania](#method-comparison).

### Python

```
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = 'my_local_file.pdf';

    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: fs.readFileSync(filePath).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] pdfBytes = Files.readAllBytes(Paths.get("my_local_file.pdf"));
String base64Pdf = Base64.getEncoder().encodeToString(pdfBytes);

String prompt = "Summarize this document";

Content textContent = TextContent.builder().text(prompt).build();
Content docContent =
    DocumentContent.builder()
        .data(base64Pdf)
        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
        .build();

List<Content> contents = Arrays.asList(textContent, docContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Summarize this document"},
      {
        "type": "document",
        "data": "'${B64_CONTENT}'",
        "mime_type": "application/pdf"
      }
    ]
  }'
```

## Porównanie metod wprowadzania

W tabeli poniżej znajdziesz porównanie poszczególnych metod wprowadzania danych z limitami plików i najlepszymi przypadkami użycia. Pamiętaj, że limit rozmiaru pliku może się różnić w zależności od typu pliku oraz modelu lub tokenizera użytego do jego przetworzenia.

| Metoda | Urządzenia | Maks. rozmiar pliku | Trwałość |
| --- | --- | --- | --- |
| **Dane w treści** | Szybkie testowanie, małe pliki, aplikacje działające w czasie rzeczywistym. | 100 MB na żądanie lub ładunek   (**50 MB w przypadku plików PDF**) | Brak (wysyłany z każdym żądaniem) |
| **Przesyłanie plików za pomocą interfejsu API** | Duże pliki, pliki używane wielokrotnie. | 2 GB na plik,   do 20 GB na projekt | 48 godzin |
| **Rejestracja identyfikatora URI GCS interfejsu File API** | duże pliki, które są już w Google Cloud Storage, oraz pliki używane wielokrotnie. | 2 GB na plik, bez ogólnych limitów miejsca na dane | Brak (pobierane na żądanie). Jednorazowa rejestracja może zapewnić dostęp na maksymalnie 30 dni. |
| **Zewnętrzne adresy URL** | dane publiczne lub dane w zasobnikach chmury (AWS, Azure, GCS) bez ponownego przesyłania; | 100 MB na żądanie lub ładunek | Brak (pobierane na żądanie) |

## Dane wbudowane

W przypadku mniejszych plików (poniżej 100 MB lub 50 MB w przypadku plików PDF) możesz przekazać dane bezpośrednio w treści żądania. Jest to najprostsza metoda do szybkich testów lub aplikacji obsługujących dane przejściowe w czasie rzeczywistym. Dane możesz podawać jako ciągi zakodowane w formacie base64 lub przez bezpośrednie odczytywanie plików lokalnych.

Przykład odczytu z pliku lokalnego znajdziesz na początku tej strony.

### Pobieranie z adresu URL

Możesz też pobrać plik z adresu URL, przekonwertować go na bajty i uwzględnić w danych wejściowych.

### Python

```
from google import genai
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: Buffer.from(pdfResp).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

String docUrl = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf";
HttpClient httpClient = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder().uri(URI.create(docUrl)).build();
byte[] docData = httpClient.send(request, HttpResponse.BodyHandlers.ofByteArray()).body();
String base64Pdf = Base64.getEncoder().encodeToString(docData);

String prompt = "Summarize this document";

Content docContent =
    DocumentContent.builder()
        .data(base64Pdf)
        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
        .build();
Content textContent = TextContent.builder().text(prompt).build();

List<Content> contents = Arrays.asList(docContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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

# Create JSON payload file
cat <<EOF > payload.json
{
"model": "gemini-3.8-flash",
"input": [
{"type": "document", "data": "${ENCODED_PDF}", "mime_type": "application/pdf"},
{"type": "text", "text": "${PROMPT}"}
]
}
EOF

# Generate content using interactions
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Gemini File API

Interfejs File API jest przeznaczony do większych plików (do 2 GB) lub plików, których zamierzasz używać w wielu żądaniach.

### Standardowe przesyłanie plików

Prześlij plik lokalny do interfejsu Gemini API. Pliki przesłane w ten sposób są przechowywane tymczasowo (przez 48 godzin) i przetwarzane w celu efektywnego pobierania przez model.

### Python

```
from google import genai

client = genai.Client()

doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
  const filePath = "path/to/your/sample.pdf";

  const myfile = await client.files.upload({
    file: filePath,
    config: { mime_type: "application/pdf" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File docFile =
    client.files.upload(
        new java.io.File("path/to/your/sample.pdf"),
        UploadFileConfig.builder().mimeType("application/pdf").build());

String prompt = "Summarize this document";

Content textContent = TextContent.builder().text(prompt).build();
Content docContent =
    DocumentContent.builder()
        .uri(docFile.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(docFile.mimeType().orElse("application/pdf")))
        .build();

List<Content> contents = Arrays.asList(textContent, docContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
FILE_PATH="path/to/sample.pdf"
MIME_TYPE=$(file -b --mime-type "${FILE_PATH}")
NUM_BYTES=$(wc -c < "${FILE_PATH}")
DISPLAY_NAME=DOCUMENT

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -D "${tmp_header_file}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
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
  --data-binary "@${FILE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)

# Now use in an interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### Rejestrowanie plików Google Cloud Storage

Jeśli dane są już w Google Cloud Storage, nie musisz ich pobierać i ponownie przesyłać. Możesz zarejestrować go bezpośrednio za pomocą interfejsu File API.

1. Przyznaj **agentowi usługi** dostęp do każdego zasobnika.

   1. Włącz interfejs Gemini API w projekcie w chmurze Google.
   2. Utwórz agenta usługi:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Przyznaj agentowi usługi Gemini API uprawnienia** do odczytu zasobników pamięci.

      Użytkownik musi przypisać do tego agenta usługi `Storage Object Viewer`
      [rolę uprawnień](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=pl#storage.objectViewer) w określonych zasobnikach pamięci, których zamierza używać.

   Domyślnie ten dostęp nie wygasa, ale w każdej chwili możesz to zmienić. Możesz też użyć poleceń [pakietu Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=pl), aby przyznać uprawnienia.
2. Uwierzytelnianie usługi

   **Wymagania wstępne**

   - Włącz API
   - Utwórz konto usługi lub agenta z odpowiednimi uprawnieniami.

   Najpierw musisz się uwierzytelnić jako usługa, która ma uprawnienia wyświetlającego obiekty Cloud Storage. Sposób działania zależy od środowiska, w którym będzie uruchamiany kod zarządzania plikami.

   **Poza Google Cloud**

   Jeśli kod jest uruchamiany poza Google Cloud, np. na komputerze, pobierz dane logowania z konsoli Google Cloud, wykonując te czynności:

   1. Otwórz [konsolę konta usługi](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=pl).
   2. Wybierz odpowiednie konto usługi.
   3. Kliknij kartę **Klucze** i wybierz **Dodaj klucz, Utwórz nowy klucz**.
   4. Wybierz typ klucza **JSON** i zanotuj, gdzie plik został pobrany na komputer.

   Więcej informacji znajdziesz w oficjalnej dokumentacji Google Cloud na temat [zarządzania kluczami kont usługi](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=pl).

   Następnie użyj tych poleceń, aby się uwierzytelnić. W tych poleceniach zakłada się, że plik konta usługi znajduje się w bieżącym katalogu i ma nazwę `service-account.json`.

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

   ### Interfejs wiersza poleceń

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **W Google Cloud**

   Jeśli korzystasz z Google Cloud bezpośrednio, np. za pomocą [funkcji Cloud Run](https://cloud.google.com/functions?hl=pl) lub [instancji Compute Engine](https://cloud.google.com/products/compute?hl=pl), masz domyślne dane logowania, ale musisz ponownie się uwierzytelnić, aby przyznać odpowiednie zakresy.

   ### Python

   Ten kod oczekuje, że usługa działa w środowisku, w którym można automatycznie uzyskać [domyślne uwierzytelnianie aplikacji](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=pl), np. w Cloud Run lub Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   Ten kod oczekuje, że usługa działa w środowisku, w którym można automatycznie uzyskać [domyślne uwierzytelnianie aplikacji](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=pl), np. w Cloud Run lub Compute Engine.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

### Java

`java
import com.google.auth.oauth2.GoogleCredentials;
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.List;
List<String> gcsReadScopes =
Arrays.asList(
"https://www.googleapis.com/auth/devstorage.read_only",
"https://www.googleapis.com/auth/cloud-platform");
String serviceAccountFile = "service-account.json";
GoogleCredentials credentials =
GoogleCredentials.fromStream(new FileInputStream(serviceAccountFile))
.createScoped(gcsReadScopes);`

### Interfejs wiersza poleceń

Jest to polecenie interaktywne. W przypadku usług takich jak Compute Engine możesz dołączyć zakresy do działającej usługi na poziomie konfiguracji. Przykład znajdziesz w [dokumentacji usługi zarządzanej przez użytkownika](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=pl#using).

```
gcloud auth application-default login \
--scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
```

1. Rejestracja plików (interfejs Files API)
   Użyj interfejsu Files API, aby zarejestrować pliki i utworzyć ścieżkę interfejsu Files API, której można bezpośrednio używać w interfejsie Gemini API.

   ### Python

   ```
   from google import genai

   client = genai.Client(credentials=credentials)

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
   )
   prompt = "Summarize this file."

   for f in registered_gcs_files.files:
     print(f.name)
     interaction = client.interactions.create(
       model="gemini-3.8-flash",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     print(interaction.output_text)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI } from "@google/genai";

   const ai = new GoogleGenAI({ auth: auth });

   async function main() {
       const registeredGcsFiles = await ai.files.registerFiles({
           uris: ["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
       });

       const prompt = "Summarize this file.";

       for (const file of registeredGcsFiles.files) {
           console.log(file.name);
           const interaction = await ai.interactions.create({
               model: "gemini-3.8-flash",
               input: [
                   { type: "text", text: prompt },
                   { type: "document", uri: file.uri, mime_type: file.mimeType }
               ]
           });

           console.log(interaction.output_text);
       }
   }

   main();
   ```

### Java

```
import com.google.auth.oauth2.GoogleCredentials;
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.RegisterFilesResponse;
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

GoogleCredentials credentials =
    GoogleCredentials.fromStream(new FileInputStream("service-account.json"))
        .createScoped(
            Arrays.asList(
                "https://www.googleapis.com/auth/devstorage.read_only",
                "https://www.googleapis.com/auth/cloud-platform"));

Client client = Client.builder().credentials(credentials).build();

RegisterFilesResponse registeredGcsFiles =
    client.files.registerFiles(
        credentials,
        Arrays.asList("gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"),
        null);

String prompt = "Summarize this file.";

for (File f : registeredGcsFiles.files().orElse(Collections.emptyList())) {
  System.out.println(f.name().orElse(""));

  Content textContent = TextContent.builder().text(prompt).build();
  Content docContent =
      DocumentContent.builder()
          .uri(f.uri().orElse(""))
          .mimeType(DocumentContentMimeType.of(f.mimeType().orElse("application/pdf")))
          .build();

  CreateModelInteraction params =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3.8-flash"))
          .input(InteractionsInput.ofContent(Arrays.asList(textContent, docContent)))
          .build();

  Interaction interaction =
      client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
  System.out.println(interaction.outputText().orElse(""));
}
```

### Interfejs wiersza poleceń

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

W żądaniu możesz przekazywać publicznie dostępne adresy URL HTTPS lub wstępnie podpisane adresy URL. Interfejs Gemini API pobierze treść w bezpieczny sposób podczas przetwarzania.
To idealne rozwiązanie w przypadku plików o rozmiarze do 100 MB, których nie chcesz przesyłać ponownie.

### Python

```
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: [
      { type: "document", uri: uri, mime_type: "application/pdf" },
      { type: "text", text: "summarize this file" }
    ]
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "model": "gemini-3.8-flash",
          "input": [
            {"type": "text", "text": "Summarize this pdf"},
            {
              "type": "document",
              "uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf",
              "mime_type": "application/pdf"
            }
          ]
        }'
```

### Ułatwienia dostępu

Sprawdź, czy podane adresy URL nie prowadzą do stron, które wymagają logowania lub są umieszczone w sekcji płatnej. W przypadku prywatnych baz danych utwórz podpisany URL
z prawidłowymi uprawnieniami dostępu i datą ważności.

### Kontrole bezpieczeństwa

System przeprowadza weryfikację adresu URL pod kątem moderacji treści, aby potwierdzić, że spełnia on standardy bezpieczeństwa i zasad. Jeśli URL nie przejdzie tego testu, otrzymasz `url_retrieval_status` z `URL_RETRIEVAL_STATUS_UNSAFE`.

### Obsługiwane typy treści

Ta lista obsługiwanych typów plików i ograniczeń ma charakter wstępny i nie jest wyczerpująca. Efektywny zestaw obsługiwanych typów może się zmieniać i różnić w zależności od konkretnego modelu i używanej wersji tokenizera. Nieobsługiwane typy spowodują błąd.
Dodatkowo pobieranie treści w przypadku tych typów plików obsługuje tylko publicznie dostępne adresy URL.

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

#### Typy plików graficznych:

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

- **Wybierz odpowiednią metodę:** w przypadku małych, tymczasowych plików używaj danych wbudowanych.
  W przypadku większych lub często używanych plików używaj interfejsu File API. Używaj zewnętrznych adresów URL
  w przypadku danych, które są już hostowane online.
- **Określ typy MIME:** zawsze podawaj prawidłowy typ MIME danych pliku, aby zapewnić prawidłowe przetwarzanie.
- **Obsługa błędów:** zaimplementuj w kodzie obsługę błędów, aby zarządzać potencjalnymi problemami, takimi jak awarie sieci, problemy z dostępem do plików lub błędy interfejsu API.

## Ograniczenia

- Limity rozmiaru plików różnią się w zależności od metody (patrz [tabela porównawcza](#method-comparison)) i typu pliku.
- Dane w tekście zwiększają rozmiar ładunku żądania.
- Przesyłanie za pomocą interfejsu File API jest tymczasowe i wygasa po 48 godzinach.
- Pobieranie zewnętrznych adresów URL jest ograniczone do 100 MB na ładunek i obsługuje określone typy treści.

## Co dalej?

- Wypróbuj pisanie własnych promptów multimodalnych w [Google AI Studio](http://aistudio.google.com/?hl=pl).
- Informacje o tym, jak uwzględniać pliki w promptach, znajdziesz w przewodnikach [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=pl), [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=pl) i [Przetwarzanie dokumentów](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-18 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-18 UTC."],[],[]]
