---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=id
fetched_at: 2026-10-05T06:33:31.713402+00:00
title: "Metode input file \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Metode input file

Panduan ini menjelaskan berbagai cara Anda dapat menyertakan file media seperti gambar, audio, video, dan dokumen saat membuat permintaan ke Gemini API.
Metode baru ini didukung di semua endpoint Gemini API, termasuk
Batch, Interactions, dan Live API.
Memilih metode yang tepat bergantung pada ukuran file, tempat data Anda disimpan, dan seberapa sering Anda berencana menggunakan file tersebut.

Cara paling sederhana untuk menyertakan file sebagai input adalah dengan membaca file lokal dan
menyertakannya dalam perintah. Contoh berikut menunjukkan cara membaca file PDF lokal. PDF dibatasi hingga 50 MB untuk metode ini. Lihat
[Tabel perbandingan metode input](#method-comparison) untuk mengetahui daftar lengkap jenis dan batas input file.

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

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

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

    pdfBytes, err := os.ReadFile("my_local_file.pdf")
    if err != nil {
        log.Fatal(err)
    }
    base64Pdf := base64.StdEncoding.EncodeToString(pdfBytes)

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.DocumentContent{
                    Data:     genai.Ptr(base64Pdf),
                    MimeType: interactions.DocumentContentMimeTypeApplicationPdf.ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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

## Perbandingan metode input

Tabel berikut membandingkan setiap metode input dengan batas file dan kasus penggunaan terbaik. Perhatikan bahwa batas ukuran file dapat bervariasi, bergantung pada jenis file dan
model atau tokenizer yang digunakan untuk memproses file.

| Metode | Paling cocok untuk | Ukuran file maks. | Persistensi |
| --- | --- | --- | --- |
| **Data inline** | Pengujian cepat, file kecil, aplikasi real-time. | 100 MB per permintaan atau payload   (**50 MB untuk PDF**) | Tidak ada (dikirim dengan setiap permintaan) |
| **Upload File API** | File besar, file yang digunakan beberapa kali. | 2 GB per file,   hingga 20 GB per project | 48 Jam |
| **Pendaftaran URI GCS File API** | File besar yang sudah ada di Google Cloud Storage, file yang digunakan beberapa kali. | 2 GB per file, tanpa batas penyimpanan keseluruhan | Tidak ada (diambil per permintaan). Pendaftaran satu kali dapat memberikan akses hingga 30 hari. |
| **URL eksternal** | Data publik atau data di bucket cloud (AWS, Azure, GCS) tanpa mengupload ulang. | 100 MB per permintaan/payload | Tidak ada (diambil per permintaan) |

## Data inline

Untuk file yang lebih kecil (di bawah 100 MB, atau 50 MB untuk PDF), Anda dapat meneruskan data secara langsung di payload permintaan. Ini adalah metode paling sederhana untuk pengujian cepat atau
aplikasi yang menangani data sementara real-time. Anda dapat menyediakan data sebagai
string berenkode base64 atau dengan membaca file lokal secara langsung.

Untuk contoh membaca dari file lokal, lihat contoh di awal halaman ini.

### Mengambil dari URL

Anda juga dapat mengambil file dari URL, mengonversinya menjadi byte, dan menyertakannya dalam
input.

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

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "io"
    "log"
    "net/http"

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

    docURL := "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
    resp, err := http.Get(docURL)
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
    docData, err := io.ReadAll(resp.Body)
    if err != nil {
        log.Fatal(err)
    }
    base64Pdf := base64.StdEncoding.EncodeToString(docData)

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    Data:     genai.Ptr(base64Pdf),
                    MimeType: interactions.DocumentContentMimeTypeApplicationPdf.ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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

File API dirancang untuk file yang lebih besar (hingga 2 GB) atau file yang ingin Anda gunakan dalam beberapa permintaan.

### Upload file standar

Mengupload file lokal ke Gemini API. File yang diupload dengan cara ini disimpan
untuk sementara (48 jam) dan diproses agar dapat diambil secara efisien oleh model.

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

    docFile, err := client.Files.UploadFromPath(ctx, "path/to/your/sample.pdf", &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(docFile.URI),
                    MimeType: interactions.DocumentContentMimeType(docFile.MIMEType).ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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

### Mendaftarkan file Google Cloud Storage

Jika data Anda sudah ada di Google Cloud Storage, Anda tidak perlu mendownload dan menguploadnya kembali. Anda dapat mendaftarkannya langsung dengan File API.

1. Memberikan akses **Agen Layanan** ke setiap bucket

   1. Aktifkan Gemini API di project Google Cloud Anda.
   2. Buat Agen Layanan:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Beri Agen Layanan Gemini API izin** untuk membaca bucket penyimpanan Anda.

      Pengguna perlu menetapkan `Storage Object Viewer`
      [peran IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=id#storage.objectViewer)
      kepada agen layanan ini di bucket penyimpanan tertentu yang ingin mereka gunakan.

   Akses ini tidak memiliki masa berlaku secara default, tetapi dapat diubah kapan saja. Anda juga dapat menggunakan perintah [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=id) untuk memberikan izin.
2. Mengautentikasi layanan Anda

   **Prasyarat**

   - Aktifkan API
   - Buat akun layanan atau agen dengan izin yang sesuai.

   Anda harus melakukan autentikasi terlebih dahulu sebagai layanan yang memiliki izin penampil objek penyimpanan. Cara ini terjadi bergantung pada lingkungan tempat kode pengelolaan file Anda akan berjalan.

   **Di luar Google Cloud**

   Jika kode Anda berjalan dari luar Google Cloud, seperti desktop Anda,
   download kredensial akun dari Konsol Google Cloud dengan
   langkah-langkah berikut:

   1. Buka [konsol Akun Layanan](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=id)
   2. Pilih akun layanan yang relevan
   3. Pilih tab **Keys**, lalu pilih **Add key, Create new key**
   4. Pilih jenis kunci **JSON**, dan catat tempat file didownload di komputer Anda.

   Untuk mengetahui detail selengkapnya, lihat dokumentasi resmi Google Cloud tentang
   [pengelolaan kunci akun layanan](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=id).

   Kemudian, gunakan perintah berikut untuk mengautentikasi. Perintah ini mengasumsikan file akun layanan Anda berada di direktori saat ini, bernama `service-account.json`.

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

   **Di Google Cloud**

   Jika Anda menjalankan secara langsung di Google Cloud, misalnya dengan menggunakan [fungsi Cloud Run](https://cloud.google.com/functions?hl=id) atau
   [instance Compute Engine](https://cloud.google.com/products/compute?hl=id), Anda akan
   memiliki kredensial implisit, tetapi harus melakukan autentikasi ulang untuk memberikan cakupan yang sesuai.

   ### Python

   Kode ini mengharapkan layanan berjalan di lingkungan tempat
   [Kredensial Default Aplikasi](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=id)
   dapat diperoleh secara otomatis, seperti Cloud Run atau Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   Kode ini mengharapkan layanan berjalan di lingkungan tempat
   [Kredensial Default Aplikasi](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=id)
   dapat diperoleh secara otomatis, seperti Cloud Run atau Compute Engine.

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

```
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
        .createScoped(gcsReadScopes);
```

### Go

```
package main

import (
    "log"

    "google.golang.org/genai"
)

func main() {
    cc := &genai.ClientConfig{}
    if err := cc.UseDefaultCredentials(); err != nil {
        log.Fatal(err)
    }
    _ = cc.Credentials
}
```

### CLI

Ini adalah perintah interaktif. Untuk layanan seperti Compute Engine, Anda dapat melampirkan cakupan ke
layanan yang sedang berjalan di tingkat konfigurasi. Lihat [dokumen layanan yang dikelola pengguna](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=id#using) untuk melihat contohnya.

```
gcloud auth application-default login \
--scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
```

1. Pendaftaran file (Files API)
   Gunakan Files API untuk mendaftarkan file dan menghasilkan jalur Files API yang dapat langsung digunakan di Gemini API.

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
    cc := &genai.ClientConfig{}
    if err := cc.UseDefaultCredentials(); err != nil {
        log.Fatal(err)
    }
    client, err := genai.NewClient(ctx, cc)
    if err != nil {
        log.Fatal(err)
    }

    registeredGcsFiles, err := client.Files.RegisterFiles(
        ctx,
        []string{"gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"},
        cc.Credentials,
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Summarize this file."

    for _, f := range registeredGcsFiles.Files {
        fmt.Println(f.Name)
        res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput([]interactions.Content{
                    interactions.NewContent(interactions.TextContent{
                        Text: prompt,
                    }),
                    interactions.NewContent(interactions.DocumentContent{
                        URI:      genai.Ptr(f.URI),
                        MimeType: interactions.DocumentContentMimeType(f.MIMEType).ToPointer(),
                    }),
                }),
            }),
        })
        if err != nil {
            log.Fatal(err)
        }
        if res.Interaction.OutputText != nil {
            fmt.Println(*res.Interaction.OutputText)
        }
    }
}
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

## HTTP Eksternal / URL Bertanda Tangan

Anda dapat meneruskan URL HTTPS yang dapat diakses secara publik atau URL yang telah ditandatangani sebelumnya secara langsung dalam permintaan Anda. Gemini API akan mengambil konten secara aman selama pemrosesan.
Cara ini ideal untuk file berukuran hingga 100 MB yang tidak ingin Anda upload ulang.

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

### Aksesibilitas

Pastikan URL yang Anda berikan tidak mengarah ke halaman yang memerlukan login atau berada di balik penghalang konten berbayar. Untuk database pribadi, pastikan Anda membuat URL bertanda tangan
dengan izin akses dan waktu habis masa berlaku yang benar.

### Pemeriksaan keamanan

Sistem melakukan pemeriksaan moderasi konten pada URL untuk mengonfirmasi bahwa URL tersebut memenuhi standar keamanan dan kebijakan. Jika URL gagal dalam pemeriksaan ini, Anda akan mendapatkan
`url_retrieval_status` `URL_RETRIEVAL_STATUS_UNSAFE`.

### Jenis konten yang didukung

Daftar jenis file yang didukung dan batasan ini dimaksudkan sebagai panduan awal dan tidak lengkap. Kumpulan jenis yang didukung yang efektif dapat berubah dan bervariasi berdasarkan model dan versi tokenizer tertentu yang digunakan. Jenis yang tidak didukung akan menyebabkan error.
Selain itu, pengambilan konten untuk jenis file ini hanya mendukung URL yang dapat diakses secara publik.

#### Jenis file teks

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Jenis file aplikasi

- `application/json`
- `application/pdf`

#### Jenis file gambar

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### Jenis file video

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Praktik terbaik

- **Pilih metode yang tepat:** Gunakan data inline untuk file kecil dan sementara.
  Gunakan File API untuk file yang lebih besar atau sering digunakan. Gunakan URL eksternal
  untuk data yang sudah dihosting secara online.
- **Tentukan Jenis MIME:** Selalu berikan jenis MIME yang benar untuk data file guna memastikan pemrosesan yang tepat.
- **Menangani Error:** Terapkan penanganan error dalam kode Anda untuk mengelola potensi masalah seperti kegagalan jaringan, masalah akses file, atau error API.

## Batasan

- Batas ukuran file bervariasi menurut metode (lihat [tabel perbandingan](#method-comparison))
  dan jenis file.
- Data inline meningkatkan ukuran payload permintaan.
- Upload File API bersifat sementara dan akan berakhir setelah 48 jam.
- Pengambilan URL eksternal dibatasi hingga 100 MB per payload dan mendukung jenis konten tertentu.

## Langkah berikutnya

- Coba tulis perintah multimodal Anda sendiri menggunakan
  [Google AI Studio](http://aistudio.google.com/?hl=id).
- Untuk mengetahui informasi tentang cara menyertakan file dalam perintah Anda, lihat panduan
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=id),
  [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=id), dan
  [Pemrosesan dokumen](https://ai.google.dev/gemini-api/docs/document-processing?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-24 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-24 UTC."],[],[]]
