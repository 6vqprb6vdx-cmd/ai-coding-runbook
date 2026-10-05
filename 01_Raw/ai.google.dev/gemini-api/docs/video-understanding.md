---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=id
fetched_at: 2026-10-05T06:35:03.231998+00:00
title: "Pemahaman video \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Pemahaman video

> Untuk mempelajari pembuatan video, lihat panduan [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=id).

Model Gemini dapat memproses video, sehingga memungkinkan banyak kasus penggunaan developer yang canggih yang sebelumnya memerlukan model khusus domain.
Beberapa kemampuan penglihatan Gemini mencakup kemampuan untuk: mendeskripsikan, menyegmentasikan, dan mengekstrak informasi dari video, menjawab pertanyaan tentang konten video, dan merujuk ke stempel waktu tertentu dalam video.

Anda dapat memberikan video sebagai input ke Gemini dengan cara berikut:

| Metode masukan | Ukuran maks | Kasus penggunaan yang direkomendasikan |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (berbayar) / 2 GB (gratis) | File besar (100 MB+), video panjang (10 menit+), file yang dapat digunakan kembali. |
| [Pendaftaran Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=id#registration) | 2 GB (per file, tanpa batas penyimpanan) | File besar (100 MB+), video panjang (10 menit+), file persisten yang dapat digunakan kembali. |
| [Data Sebaris](#inline-video) | < 100MB | File kecil (<100 MB), durasi singkat (<1 menit), input satu kali. |
| [URL YouTube](#youtube) | T/A | Video YouTube publik. |

> **Catatan:** [File API](#upload-video) direkomendasikan untuk sebagian besar kasus penggunaan, terutama untuk file yang berukuran lebih dari 100 MB atau saat Anda ingin menggunakan kembali file di beberapa permintaan.

Untuk mempelajari metode input file lainnya, seperti menggunakan URL eksternal atau file yang disimpan di Google Cloud, lihat panduan [Metode input file](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=id).

### Mengupload file video

Kode berikut mendownload video sampel, menguploadnya menggunakan [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id), menunggu pemrosesannya selesai, lalu menggunakan referensi file yang diupload untuk meringkas video.

### Python

```
from google import genai
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
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
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.FileState;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File myfile =
    client.files.upload(
        "path/to/sample.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());

while (!myfile.state().isPresent()
    || myfile.state().get().knownEnum() != FileState.Known.ACTIVE) {
  System.out.println("Processing video...");
  Thread.sleep(5000);
  myfile = client.files.get(myfile.name().get(), null);
}

Content videoContent =
    VideoContent.builder()
        .uri(myfile.uri().get())
        .mimeType(VideoContentMimeType.of(myfile.mimeType().get()))
        .build();
Content textContent =
    TextContent.builder()
        .text(
            "Summarize this video. Then create a quiz with an answer key based on the information in this video.")
        .build();

List<Content> contents = Arrays.asList(videoContent, textContent);

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
    "time"

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

    myfile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", &genai.UploadFileConfig{
        MIMEType: "video/mp4",
    })
    if err != nil {
        log.Fatal(err)
    }

    for myfile.State != genai.FileStateActive {
        fmt.Println("Processing video...")
        time.Sleep(5 * time.Second)
        myfile, err = client.Files.Get(ctx, myfile.Name, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI:      genai.Ptr(myfile.URI),
            MimeType: interactions.VideoContentMimeType(myfile.MIMEType).ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
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
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

Untuk mengoptimalkan efisiensi dan performa token, pertimbangkan untuk menggunakan
[Pemrosesan video berbasis agen](#agentic-video-understanding).

Selalu gunakan Files API jika total ukuran permintaan (termasuk file, perintah teks, petunjuk sistem, dll.) lebih besar dari 20 MB, durasi video signifikan, atau jika Anda ingin menggunakan video yang sama dalam beberapa perintah.
File API menerima format file video secara langsung.

Untuk mempelajari lebih lanjut cara menggunakan file media, lihat
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=id).

### Meneruskan data video secara inline

Daripada mengupload file video menggunakan File API, Anda dapat meneruskan video yang lebih kecil langsung dalam permintaan. Opsi ini cocok untuk
video yang lebih pendek dengan total ukuran permintaan di bawah 20 MB.

Berikut contoh cara memberikan data video inline:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
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
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

String videoFileName = "/path/to/your/video.mp4";
byte[] videoBytes = Files.readAllBytes(Paths.get(videoFileName));
String base64Video = Base64.getEncoder().encodeToString(videoBytes);

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .data(base64Video)
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

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

    videoFileName := "/path/to/your/video.mp4"
    videoBytes, err := os.ReadFile(videoFileName)
    if err != nil {
        log.Fatal(err)
    }
    base64Video := base64.StdEncoding.EncodeToString(videoBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            Data:     genai.Ptr(base64Video),
            MimeType: interactions.VideoContentMimeTypeVideoMp4.ToPointer(),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
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
      "model": "gemini-3.8-flash",
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

### Meneruskan URL YouTube

Anda dapat meneruskan URL YouTube langsung ke Gemini API sebagai bagian dari permintaan Anda sebagai berikut:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
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
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .uri("https://www.youtube.com/watch?v=9hE5-98ZeCg")
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

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

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            URI: genai.Ptr("https://www.youtube.com/watch?v=9hE5-98ZeCg"),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**Batasan:**

- Untuk paket gratis, Anda tidak dapat mengupload lebih dari 8 jam video YouTube per hari.
- Untuk paket berbayar, tidak ada batasan berdasarkan durasi video.
- Untuk model sebelum Gemini 2.5, Anda hanya dapat mengupload 1 video per permintaan. Untuk model Gemini 2.5 dan yang lebih baru, Anda dapat mengupload maksimal 10 video per permintaan.
- Anda hanya dapat mengupload video publik (bukan video pribadi atau tidak publik).

## Pemahaman video agentik

Secara default, input video menggunakan pemrosesan statis (mengekstraksi frame pada 1 FPS).
Model Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, dan 3.5 Flash Lite juga mendukung
**pemahaman video berbasis agen**, di mana model secara dinamis menjelajahi linimasa video, memeriksa transkrip secara selektif, dan menyesuaikan kecepatan frame serta resolusi secara adaptif dengan cepat berdasarkan perintah.

| **Mode** | **Deskripsi** | **Model yang didukung** |
| --- | --- | --- |
| **Statis** (default) | Mengekstrak frame dengan kecepatan tetap (1 FPS) dan menempatkannya ke dalam konteks dalam satu langkah. Berfungsi baik untuk klip pendek. | Semua model Gemini |
| **Agentic** | Model ini secara dinamis menavigasi linimasa video, hanya memuat konten yang diperlukan berdasarkan perintah. Hingga 88% lebih efisien token dan kualitas ~7% lebih tinggi pada konten panjang. | Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite |

### Memilih mode pemrosesan

Sebagai panduan umum, mulailah dengan mode **berperan sebagai agen**, terutama saat mengoptimalkan
kualitas respons atau efisiensi token.

- **Agen:** Video panjang atau kueri yang menargetkan momen tertentu. Model
  secara dinamis menavigasi linimasa untuk menargetkan informasi yang relevan secara kontekstual
  tanpa mengisi jendela konteks.
- **Statis:** Kueri yang sensitif terhadap latensi pada klip pendek (di bawah 5 menit), atau
  kasus yang memerlukan presisi tingkat frame di seluruh klip.

> **Catatan:** Untuk video panjang atau perintah kompleks yang memerlukan waktu lebih lama untuk diproses secara mandiri, gunakan streaming (`stream=True`) atau eksekusi di latar belakang (`background=True`). Hal ini akan menjaga koneksi tetap aktif, menampilkan langkah-langkah penalaran sementara, dan menghindari waktu tunggu koneksi atau autentikasi habis.

### Menetapkan mode pemrosesan

### Python

```
import time
from google import genai

client = genai.Client()

# Upload a long video
video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

# Use agentic processing
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": "agentic"
        },
        {"type": "text", "text": "What are the three main arguments presented?"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Upload a long video
let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" }
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Use agentic processing
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: "agentic"
    },
    { type: "text", text: "What are the three main arguments presented?" }
  ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {"type": "text", "text": "What are the three main arguments presented?"}
    ]
  }' 2> /dev/null
```

> **Catatan:** Untuk memverifikasi bahwa pemrosesan berbasis agen digunakan, periksa `interaction.steps`. Kehadiran `processing_call` dan `processing_result` menunjukkan bahwa model menavigasi video secara dinamis.

### Langkah-langkah respons

Pemrosesan dengan agen menambahkan dua jenis langkah baru ke array `steps`:

- `processing_call`: model meminta segmen video atau transkrip audio, yang diidentifikasi oleh `id`.
- `processing_result`: hasil pemuatan tersebut, ditautkan oleh `call_id`.

Ringkasan ini muncul berselang-seling dengan langkah-langkah `thought` (jika ringkasan diaktifkan) dan mendahului langkah `model_output` terakhir. Objek ini dapat digunakan untuk menampilkan rekaman aktivitas progres di UI Anda, tetapi tidak memerlukan respons.

Contoh berikut menunjukkan payload respons dengan langkah-langkah pemrosesan yang disisipkan:

```
{
  "steps": [
    {
      "type": "thought",
      "signature": "sig_thought_1",
      "summary": [
        {
          "type": "text",
          "text": "Inspecting transcript for key discussion topics..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_01",
      "signature": "sig_call_01"
    },
    {
      "type": "processing_result",
      "call_id": "call_01",
      "signature": "sig_result_01"
    },
    {
      "type": "thought",
      "signature": "sig_thought_2",
      "summary": [
        {
          "type": "text",
          "text": "Loading visual frames to verify slide content..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_02",
      "signature": "sig_call_02"
    },
    {
      "type": "processing_result",
      "call_id": "call_02",
      "signature": "sig_result_02"
    },
    {
      "type": "thought",
      "signature": "sig_thought_3",
      "summary": [
        {
          "type": "text",
          "text": "Synthesizing answer from gathered evidence..."
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The three main arguments presented in the lecture are..."
        }
      ]
    }
  ]
}
```

### Mencampur mode pemrosesan di seluruh video

Anda dapat menetapkan mode pemrosesan yang berbeda untuk setiap video dalam permintaan yang sama:

### Python

```
from google import genai

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": lecture.uri,
            "mime_type": lecture.mime_type,
            "processing": "agentic"  # Use agentic video understanding
        },
        {
            "type": "video",
            "uri": experiment.uri,
            "mime_type": experiment.mime_type,
            "processing": "static"  # Use static processing
        },
        {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" }
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" }
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: lecture.uri,
      mime_type: lecture.mimeType,
      processing: "agentic" // Use agentic video understanding
    },
    {
      type: "video",
      uri: experiment.uri,
      mime_type: experiment.mimeType,
      processing: "static" // Use static processing
    },
    { type: "text", text: "Compare the lecture content with the experiment results." }
  ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${lecture_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {
        "type": "video",
        "uri": "'${experiment_uri}'",
        "mime_type": "video/mp4",
        "processing": "static"
      },
      {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ]
  }' 2> /dev/null
```

### Percakapan video multi-giliran

Konteks video dipertahankan di seluruh giliran dalam percakapan. Saat menggunakan pemrosesan
dengan agen:

- **Mode stateful** (menggunakan `previous_interaction_id`): Server mempertahankan konteks video. Tidak diperlukan penanganan tambahan.
- **Mode tanpa status** (menggunakan `step_list`): Dalam mode tanpa status, respons
  mencakup langkah-langkah `processing_call` dan `processing_result` yang mengenkode
  konteks video. Anda harus menyertakan semua langkah dari respons dalam `step_list` permintaan berikutnya untuk mempertahankan konteks video. Meskipun saat ini tidak menampilkan error API, konteks video akan hilang, sehingga mengurangi kualitas respons pada pertanyaan lanjutan secara signifikan. Perhatikan bahwa langkah-langkah yang ditampilkan
  yang dikirim dalam permintaan berikutnya berkontribusi pada jumlah token input.

## Merujuk pada stempel waktu dalam konten

Anda dapat mengajukan pertanyaan tentang titik waktu tertentu dalam video menggunakan stempel waktu dalam bentuk `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Java

```
String prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
prompt := "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Mengekstrak insight mendetail dari video

Model Gemini menawarkan kemampuan canggih untuk memahami konten video dengan memproses informasi dari aliran **audio dan visual**. Dengan demikian, Anda dapat mengekstrak serangkaian detail yang kaya, termasuk membuat deskripsi tentang apa yang terjadi dalam video dan menjawab pertanyaan tentang kontennya.

Untuk deskripsi visual, model mengambil sampel video dengan kecepatan **1 frame per detik** (FPS). Frekuensi sampling default ini berfungsi dengan baik untuk sebagian besar konten, tetapi perhatikan bahwa frekuensi ini mungkin tidak menangkap detail dalam video dengan gerakan cepat atau perubahan adegan yang cepat.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Java

```
String prompt =
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
prompt := "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Menyesuaikan pemrosesan video

Anda dapat menyesuaikan pemrosesan video di Gemini API dengan menyetel interval kliping atau memberikan pengambilan sampel kecepatan frame kustom. Opsi penyesuaian ini hanya didukung saat memproses video dalam mode `"static"`.

### Menetapkan interval kliping

Anda dapat menggunting video dengan menentukan `start_offset` dan `end_offset` dalam objek konfigurasi `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "start_offset": 1200,
                "end_offset": 1500,
            },
        },
        {"type": "text", "text": "Summarize this section of the video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        start_offset: 1200,
        end_offset: 1500,
      },
    },
    { type: "text", text: "Summarize this section of the video." },
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
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "start_offset": 1200,
          "end_offset": 1500
        }
      },
      {"type": "text", "text": "Summarize this section of the video."}
    ]
  }' 2> /dev/null
```

### Menetapkan kecepatan frame kustom

Anda dapat menyetel pengambilan sampel kecepatan frame kustom dengan meneruskan argumen `fps` dalam objek konfigurasi `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "fps": 0.5,  # Sample 1 frame every 2 seconds
            },
        },
        {"type": "text", "text": "Describe the scene changes in this video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        fps: 0.5, // Sample 1 frame every 2 seconds
      },
    },
    { type: "text", text: "Describe the scene changes in this video." },
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
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "fps": 0.5
        }
      },
      {"type": "text", "text": "Describe the scene changes in this video."}
    ]
  }' 2> /dev/null
```

## Format video yang didukung

Gemini mendukung jenis MIME format video berikut:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Detail teknis tentang video

- **Model dan konteks yang didukung**: Semua model Gemini dapat memproses data video.
  - Model dengan jendela konteks 1 juta dapat memproses video berdurasi hingga 3 jam secara default (pada resolusi media rendah), atau hingga 1 jam pada resolusi media tinggi.
- **Mode pemrosesan**: Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite, dan model yang lebih baru mendukung dua mode pemrosesan video:
  - **Statis**: Frame diekstrak pada 1 FPS dan ditempatkan ke dalam konteks (default untuk semua model). Audio diproses pada 1 Kbps (satu saluran).
    Stempel waktu ditambahkan setiap detik. Paling cocok untuk klip pendek atau saat setiap frame
    penting (seperti pemeriksaan frame demi frame). Perhatikan bahwa urutan tindakan cepat
    mungkin kehilangan detail karena kecepatan pengambilan sampel 1 FPS.
  - **Agentik**: Model menavigasi video secara dinamis, memuat
    transkrip dan/atau frame dan/atau audio sesuai permintaan. Fitur ini menggunakan hingga 88% lebih sedikit token untuk konten panjang, meskipun navigasi dapat sedikit meningkatkan Waktu ke Token Pertama (TTFT) pada klip pendek (<5 menit) karena penalaran internal dan perjalanan pulang pergi alat sebelum pembuatan dimulai. Terbaik
    untuk video panjang guna mengoptimalkan biaya token dan kualitas respons.
    Didukung di Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, dan 3.5 Flash Lite.
    Lihat [Pemahaman video agentik](#agentic-video-understanding) untuk mengetahui detailnya.
- **Penghitungan token (mode statis)**: Setiap detik video di-tokenisasi sebagai
  berikut:
  - Frame individual (diambil sampel pada 1 FPS):
    - Jika `media_resolution` disetel ke rendah, frame akan di-tokenisasi pada 66 token per frame.
    - Jika tidak, frame akan di-tokenisasi pada 258 token per frame.
  - Audio: 32 token per detik.
  - Metadata juga disertakan.
  - Total: Sekitar 100 token per detik video pada resolusi media default (rendah), atau sekitar 300 token per detik video pada resolusi media tinggi.
- **Penghitungan token (mode agentik)**: Penggunaan token bervariasi berdasarkan kompleksitas konten dan strategi navigasi model. Token penalaran navigasi
  yang dihasilkan selama eksplorasi video dihitung sebagai **token pemikiran**
  (`total_thought_tokens`), sedangkan frame, audio, dan transkrip yang dimuat sesuai permintaan
  dihitung sebagai token penggunaan alat (`total_tool_use_tokens`).
  Pemrosesan agentik biasanya menggunakan total token hingga 88% lebih sedikit daripada pemrosesan statis untuk konten panjang karena model hanya memuat transkrip dan/atau frame dan/atau audio yang diperlukan untuk menjawab perintah (lihat [panduan token](https://ai.google.dev/gemini-api/docs/tokens?hl=id#video-token-usage)).
- **Resolusi media**: Gemini 3 memperkenalkan kontrol terperinci atas pemrosesan visi multimodal dengan parameter `media_resolution`. Parameter
  `media_resolution` menentukan **jumlah maksimum token
  yang dialokasikan per frame video atau gambar input.** Resolusi yang lebih tinggi meningkatkan kemampuan model untuk membaca teks kecil atau mengidentifikasi detail kecil, tetapi meningkatkan penggunaan token dan latensi. Parameter `media_resolution` dan `processing` bersifat independen: Anda dapat menyetel keduanya pada input video yang sama.

Untuk mengetahui detail selengkapnya tentang penghitungan token, lihat panduan
[token](https://ai.google.dev/gemini-api/docs/tokens?hl=id).

- **Format stempel waktu**: Saat merujuk ke momen tertentu dalam video di dalam perintah Anda, gunakan format `MM:SS` (misalnya, `01:15` untuk 1 menit 15 detik).
- **Penempatan perintah**: Jika menggabungkan teks dan satu video, tempatkan perintah teks
  *setelah* bagian video dalam array `input`.
- **Waktu tunggu untuk permintaan yang panjang**: Untuk video yang memerlukan waktu pemrosesan yang lebih lama atau penalaran multi-langkah yang kompleks, gunakan streaming (`stream=True`) atau eksekusi di latar belakang (`background=True`). Permintaan sinkron yang tidak melakukan streaming yang mengalami percobaan ulang backend saat permintaan tinggi dapat melampaui periode validitas token autentikasi atau koneksi, yang dapat muncul sebagai error `401 Unauthorized` atau waktu tunggu yang tidak terduga.
  Streaming membuat koneksi tetap aktif dan menampilkan penalaran perantara dan progres panggilan alat.

## Langkah berikutnya

- [Resolusi media](https://ai.google.dev/gemini-api/docs/media-resolution?hl=id): Kontrol resolusi frame video untuk menyeimbangkan kualitas dan penggunaan token.
- [Token](https://ai.google.dev/gemini-api/docs/tokens?hl=id): Pahami cara konten video di-tokenisasi dalam mode pemrosesan statis dan agentic.
- [Petunjuk sistem](https://ai.google.dev/gemini-api/docs/text-generation?hl=id#system-instructions):
  Petunjuk sistem memungkinkan Anda mengarahkan perilaku model berdasarkan kebutuhan dan kasus penggunaan spesifik Anda.
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id): Pelajari lebih lanjut cara mengupload dan mengelola file untuk digunakan dengan Gemini.
- [Strategi multimodal prompting file](https://ai.google.dev/gemini-api/docs/files?hl=id#prompt-guide): Gemini API mendukung multimodal prompting dengan data teks, gambar, audio, dan video, yang juga dikenal sebagai multimodal prompting.
- [Panduan keamanan](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=id): Terkadang model AI generatif menghasilkan output yang tidak terduga, seperti output yang tidak akurat, bias, atau menyinggung. Pemrosesan pasca-dan evaluasi manusia sangat penting untuk membatasi risiko bahaya dari output tersebut.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-24 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-24 UTC."],[],[]]
