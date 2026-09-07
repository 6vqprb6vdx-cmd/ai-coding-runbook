---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-input-methods?hl=id
fetched_at: 2026-09-07T05:43:46.123709+00:00
title: "Metode input file \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Metode input file

Panduan ini menjelaskan berbagai cara untuk menyertakan file media seperti gambar, audio, video, dan dokumen saat membuat permintaan ke Gemini API.
Metode baru ini didukung di semua endpoint Gemini API, termasuk
Batch, Interactions, dan Live API.
Memilih metode yang tepat bergantung pada ukuran file, tempat data Anda saat ini disimpan, dan seberapa sering Anda berencana menggunakan file tersebut.

Cara paling sederhana untuk menyertakan file sebagai input adalah dengan membaca file lokal dan
menyertakannya dalam perintah. Contoh berikut menunjukkan cara membaca file PDF lokal. PDF dibatasi hingga 50 MB untuk metode ini. Lihat
[Tabel perbandingan metode input](#method-comparison) untuk mengetahui daftar lengkap jenis dan batas input file.

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3.6-flash",
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
        model: "gemini-3.6-flash",
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

## Perbandingan metode input

Tabel berikut membandingkan setiap metode input dengan batas file dan kasus penggunaan terbaik. Perhatikan bahwa batas ukuran file dapat bervariasi, bergantung pada jenis file dan
model/tokenizer yang digunakan untuk memproses file.

| Metode | Paling cocok untuk | Ukuran file maks. | Persistensi |
| --- | --- | --- | --- |
| **Data inline** | Pengujian cepat, file kecil, aplikasi real-time. | 100 MB per permintaan/payload   (**50 MB untuk PDF**) | Tidak ada (dikirim dengan setiap permintaan) |
| **Upload File API** | File besar, file yang digunakan beberapa kali. | 2 GB per file,   hingga 20 GB per project | 48 Jam |
| **Pendaftaran URI GCS File API** | File besar yang sudah ada di Google Cloud Storage, file yang digunakan beberapa kali. | 2 GB per file, tanpa batas penyimpanan keseluruhan | Tidak ada (diambil per permintaan). Pendaftaran satu kali dapat memberikan akses hingga 30 hari. |
| **URL eksternal** | Data publik atau data di bucket cloud (AWS, Azure, GCS) tanpa mengupload ulang. | 100 MB per permintaan/payload | Tidak ada (diambil per permintaan) |

## Data inline

Untuk file yang lebih kecil (di bawah 100 MB, atau 50 MB untuk PDF), Anda dapat meneruskan data langsung di payload permintaan. Ini adalah metode paling sederhana untuk pengujian cepat atau aplikasi yang menangani data sementara real-time. Anda dapat menyediakan data sebagai
string berenkode base64 atau dengan membaca file lokal secara langsung.

Untuk contoh membaca dari file lokal, lihat contoh di awal halaman ini.

### Mengambil dari URL

Anda juga dapat mengambil file dari URL, mengonversinya menjadi byte, dan menyertakannya dalam
input.

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
  model="gemini-3.6-flash",
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
        model: "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

File API dirancang untuk file yang lebih besar (hingga 2 GB) atau file yang ingin Anda gunakan dalam beberapa permintaan.

### Upload file standar

Mengupload file lokal ke Gemini API. File yang diupload dengan cara ini disimpan
untuk sementara (48 jam) dan diproses agar dapat diambil secara efisien oleh model.

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

### Mendaftarkan file Google Cloud Storage

Jika data Anda sudah ada di Google Cloud Storage, Anda tidak perlu mendownload dan menguploadnya ulang. Anda dapat mendaftarkannya langsung dengan File API.

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
   - Buat akun/agen layanan dengan izin yang sesuai.

   Anda harus melakukan autentikasi terlebih dahulu sebagai layanan yang memiliki izin penampil objek penyimpanan. Cara ini terjadi bergantung pada lingkungan tempat kode pengelolaan file Anda akan berjalan.

   **Di luar Google Cloud**

   Jika kode Anda berjalan dari luar Google Cloud, seperti desktop Anda, download kredensial akun dari Konsol Google Cloud dengan langkah-langkah berikut:

   1. Buka [konsol Akun Layanan](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=id)
   2. Pilih akun layanan yang relevan
   3. Pilih tab **Keys**, lalu pilih **Add key, Create new key**
   4. Pilih jenis kunci **JSON**, dan catat lokasi file didownload di komputer Anda.

   Untuk mengetahui detail selengkapnya, lihat dokumentasi resmi Google Cloud tentang [pengelolaan kunci akun layanan](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=id).

   Kemudian, gunakan perintah berikut untuk mengautentikasi. Perintah ini mengasumsikan bahwa file akun layanan Anda ada di direktori saat ini, bernama `service-account.json`.

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

   ### CLI

   Ini adalah perintah interaktif. Untuk layanan seperti Compute Engine, Anda dapat melampirkan cakupan ke
   layanan yang sedang berjalan di tingkat konfigurasi. Lihat [dokumen layanan yang dikelola pengguna](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=id#using) untuk melihat contohnya.

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Pendaftaran file (Files API)

   Gunakan Files API untuk mendaftarkan file dan menghasilkan jalur Files API yang dapat langsung digunakan di Gemini API.

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
       model="gemini-3.6-flash",
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

## HTTP Eksternal / URL Bertanda Tangan

Anda dapat meneruskan URL HTTPS yang dapat diakses secara publik atau URL yang telah ditandatangani sebelumnya (kompatibel dengan
[URL yang Ditandatangani Sebelumnya S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html)
dan SAS Azure) langsung dalam permintaan pembuatan Anda. Gemini API akan mengambil
konten secara aman selama pemrosesan. Cara ini ideal untuk file hingga 100 MB yang tidak ingin Anda upload ulang.

Anda dapat menggunakan URL publik atau yang ditandatangani sebagai input dengan menggunakan URL di kolom
`file_uri`.

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent \
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

### Aksesibilitas

Pastikan URL yang Anda berikan tidak mengarah ke halaman yang memerlukan login atau berada di balik penghalang konten berbayar. Untuk database pribadi, pastikan Anda membuat URL bertanda tangan
dengan izin akses dan waktu habis masa berlaku yang benar.

### Pemeriksaan keamanan

Sistem melakukan pemeriksaan moderasi konten pada URL untuk mengonfirmasi bahwa URL tersebut memenuhi standar keamanan dan kebijakan (misalnya, konten yang tidak dikecualikan & berbayar). Jika URL yang Anda berikan gagal dalam pemeriksaan ini, Anda akan mendapatkan
`url_retrieval_status` dari `URL_RETRIEVAL_STATUS_UNSAFE`.

### Jenis konten yang didukung

Daftar jenis file yang didukung dan batasan ini dimaksudkan sebagai panduan awal dan tidak lengkap. Kumpulan jenis yang didukung yang efektif dapat berubah dan bervariasi berdasarkan model dan versi tokenizer tertentu yang digunakan. Jenis yang tidak didukung akan menyebabkan error.
Selain itu, pengambilan konten untuk jenis file ini saat ini hanya mendukung URL yang dapat diakses secara publik.

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
- **Menangani Error:** Terapkan penanganan error dalam kode Anda untuk mengelola
  potensi masalah seperti kegagalan jaringan, masalah akses file, atau error
  API.
- **Mengelola Izin GCS:** Saat menggunakan pendaftaran GCS, berikan peran `Storage Object Viewer` yang diperlukan saja kepada Agen Layanan API Gemini di bucket tertentu.
- **Keamanan URL Bertanda Tangan:** Pastikan URL bertanda tangan memiliki waktu habis masa berlaku yang sesuai dan izin terbatas.

## Batasan

- Batas ukuran file bervariasi menurut metode (lihat [tabel perbandingan](#method-comparison))
  dan jenis file.
- Data inline meningkatkan ukuran payload permintaan.
- Upload File API bersifat sementara dan akan berakhir setelah 48 jam.
- Pengambilan URL eksternal dibatasi hingga 100 MB per payload dan mendukung jenis konten tertentu.
- Pendaftaran Google Cloud Storage memerlukan penyiapan IAM yang tepat dan pengelolaan token OAuth.

## Langkah berikutnya

- Coba tulis perintah multimodal Anda sendiri menggunakan
  [Google AI Studio](http://aistudio.google.com/?hl=id).
- Untuk mengetahui informasi tentang cara menyertakan file dalam perintah Anda, lihat panduan
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=id),
  [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=id), dan
  [Pemrosesan dokumen](https://ai.google.dev/gemini-api/docs/document-processing?hl=id).
- Untuk panduan selengkapnya tentang desain perintah, seperti menyesuaikan parameter pengambilan sampel, lihat panduan [Strategi perintah](https://ai.google.dev/gemini-api/docs/prompt-strategies?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
