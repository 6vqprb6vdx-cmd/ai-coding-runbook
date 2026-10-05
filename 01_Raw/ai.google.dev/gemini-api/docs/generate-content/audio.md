---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=id
fetched_at: 2026-10-05T06:29:16.385042+00:00
title: "Pemahaman audio \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs/generate-content?hl=id)

Kirim masukan

# Pemahaman audio

Gemini dapat menganalisis input audio dan menghasilkan respons teks.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=["Describe this audio clip", myfile]
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
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mp3" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
}

await main();
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

    localAudioPath := "/path/to/sample.mp3"
    uploadedFile, _ := client.Files.UploadFromPath(
        ctx,
        localAudioPath,
        nil,
    )

    parts := []*genai.Part{
        genai.NewPartFromText("Describe this audio clip"),
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
}
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
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header.tmp \
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

## Ringkasan

Gemini dapat menganalisis dan memahami input audio serta menghasilkan respons teks untuk input tersebut,
sehingga memungkinkan kasus penggunaan seperti berikut:

- Mendeskripsikan, meringkas, atau menjawab pertanyaan tentang konten audio.
- Memberikan transkripsi dan terjemahan audio (speech to text).
- Mendeteksi emosi dalam ucapan dan musik.
- Menganalisis segmen audio tertentu, dan memberikan stempel waktu.

Saat ini, Gemini API tidak mendukung kasus penggunaan transkripsi real-time.
Untuk interaksi suara dan video real-time, lihat [Live API](https://ai.google.dev/gemini-api/docs/live?hl=id).
Untuk model speech-to-text khusus dengan dukungan untuk transkripsi real-time,
gunakan [Google Cloud Speech-to-Text API](https://cloud.google.com/speech-to-text?hl=id).

## Mentranskripsikan ucapan ke teks

Aplikasi contoh ini menunjukkan cara meminta Gemini API untuk mentranskripsikan, menerjemahkan, dan meringkas ucapan, termasuk stempel waktu dan deteksi emosi menggunakan [output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

YOUTUBE_URL = "https://www.youtube.com/watch?v=ku-N-eS1lgM"

def main():
  prompt = """
    Process the audio file and generate a detailed transcription.

    Requirements:
    1. Provide accurate timestamps for each segment (Format: MM:SS).
    2. Detect the primary language of each segment.
    3. If the segment is in a language different than English, also provide the English translation.
    4. Identify the primary emotion of the speaker in this segment. You MUST choose exactly one of the following: Happy, Sad, Angry, Neutral.
    5. Provide a brief summary of the entire audio at the beginning.
  """

  response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
      types.Content(
        parts=[
          types.Part(
            file_data=types.FileData(
              file_uri=YOUTUBE_URL
            )
          ),
          types.Part(
            text=prompt
          )
        ]
      )
    ],
    config=types.GenerateContentConfig(
      response_format={"text": {"mime_type": "application/json"}},
      response_schema=types.Schema(
        type=types.Type.OBJECT,
        properties={
          "summary": types.Schema(
            type=types.Type.STRING,
            description="A concise summary of the audio content.",
          ),
          "segments": types.Schema(
            type=types.Type.ARRAY,
            description="List of transcribed segments with timestamp.",
            items=types.Schema(
              type=types.Type.OBJECT,
              properties={
                "timestamp": types.Schema(type=types.Type.STRING),
                "content": types.Schema(type=types.Type.STRING),
                "language": types.Schema(type=types.Type.STRING),
                "language_code": types.Schema(type=types.Type.STRING),
                "translation": types.Schema(type=types.Type.STRING),
                "emotion": types.Schema(
                  type=types.Type.STRING,
                  enum=["happy", "sad", "angry", "neutral"]
                ),
              },
              required=["timestamp", "content", "language", "language_code", "emotion"],
            ),
          ),
        },
        required=["summary", "segments"],
      ),
    ),
  )

  print(response.text)

if __name__ == "__main__":
  main()
```

### JavaScript

```
import {
  GoogleGenAI,
  Type
} from "@google/genai";

const ai = new GoogleGenAI({});

const YOUTUBE_URL = "https://www.youtube.com/watch?v=ku-N-eS1lgM";

async function main() {
  const prompt = `
      Process the audio file and generate a detailed transcription.

      Requirements:
      1. Provide accurate timestamps for each segment (Format: MM:SS).
      2. Detect the primary language of each segment.
      3. If the segment is in a language different than English, also provide the English translation.
      4. Identify the primary emotion of the speaker in this segment. You MUST choose exactly one of the following: Happy, Sad, Angry, Neutral.
      5. Provide a brief summary of the entire audio at the beginning.
    `;

  const Emotion = {
    Happy: 'happy',
    Sad: 'sad',
    Angry: 'angry',
    Neutral: 'neutral'
  };

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: {
      parts: [
        {
          fileData: {
            fileUri: YOUTUBE_URL,
          },
        },
        {
          text: prompt,
        },
      ],
    },
    config: {
      responseFormat: { text: { mimeType: "application/json" } },
      responseSchema: {
        type: Type.OBJECT,
        properties: {
          summary: {
            type: Type.STRING,
            description: "A concise summary of the audio content.",
          },
          segments: {
            type: Type.ARRAY,
            description: "List of transcribed segments with timestamp.",
            items: {
              type: Type.OBJECT,
              properties: {
                timestamp: { type: Type.STRING },
                content: { type: Type.STRING },
                language: { type: Type.STRING },
                language_code: { type: Type.STRING },
                translation: { type: Type.STRING },
                emotion: {
                  type: Type.STRING,
                  enum: Object.values(Emotion)
                },
              },
              required: ["timestamp", "content", "language", "language_code", "emotion"],
            },
          },
        },
        required: ["summary", "segments"],
      },
    },
  });
  const json = JSON.parse(response.text);
  console.log(json);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [
        {
          "parts": [
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=ku-N-eS1lgM",
                "mime_type": "video/mp4"
              }
            },
            {
              "text": "Process the audio file and generate a detailed transcription.\n\nRequirements:\n1. Provide accurate timestamps for each segment (Format: MM:SS).\n2. Detect the primary language of each segment.\n3. If the segment is in a language different than English, also provide the English translation.\n4. Identify the primary emotion of the speaker in this segment. You MUST choose exactly one of the following: Happy, Sad, Angry, Neutral.\n5. Provide a brief summary of the entire audio at the beginning."
            }
          ]
        }
      ],
      "generation_config": {
        "response_format": {"text": {"mime_type": "application/json"}},
        "response_schema": {
          "type": "OBJECT",
          "properties": {
            "summary": {
              "type": "STRING",
              "description": "A concise summary of the audio content."
            },
            "segments": {
              "type": "ARRAY",
              "description": "List of transcribed segments with timestamp.",
              "items": {
                "type": "OBJECT",
                "properties": {
                  "timestamp": { "type": "STRING" },
                  "content": { "type": "STRING" },
                  "language": { "type": "STRING" },
                  "language_code": { "type": "STRING" },
                  "translation": { "type": "STRING" },
                  "emotion": {
                    "type": "STRING",
                    "enum": ["happy", "sad", "angry", "neutral"]
                  }
                },
                "required": ["timestamp", "content", "language", "language_code", "emotion"]
              }
            }
          },
          "required": ["summary", "segments"]
        }
      }
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

Anda dapat meminta [AI Studio Build](https://aistudio.google.com/apps?e=0&hl=id) untuk membuat
aplikasi seperti
[aplikasi transkripsi contoh ini](https://aistudio.google.com/apps/bundled/echoscript?hl=id)
, hanya dengan mengklik tombol.

![Aplikasi Gemini transkripsi audio multibahasa](https://ai.google.dev/static/gemini-api/docs/images/audio_understanding_demo.gif?hl=id)

## Input audio

Anda dapat memberikan data audio ke Gemini dengan cara berikut:

- [Upload file audio](#upload-audio) sebelum membuat permintaan ke
  `generateContent`.
- [Teruskan data audio inline](#inline-audio) dengan permintaan ke
  `generateContent`.

Untuk mempelajari metode input file lainnya, lihat panduan
[Metode input file](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=id).

### Mengupload file audio

Anda dapat menggunakan [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id) untuk mengupload file audio.
Selalu gunakan Files API jika ukuran total permintaan (termasuk file, perintah teks, petunjuk sistem, dll.) lebih besar dari 20 MB.

Kode berikut mengupload file audio, lalu menggunakan file tersebut dalam panggilan ke
`generateContent`.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=["Describe this audio clip", myfile]
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
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mp3" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
}

await main();
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

  localAudioPath := "/path/to/sample.mp3"
  uploadedFile, _ := client.Files.UploadFromPath(
      ctx,
      localAudioPath,
      nil,
  )

  parts := []*genai.Part{
      genai.NewPartFromText("Describe this audio clip"),
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
}
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
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header.tmp \
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

Untuk mempelajari lebih lanjut cara menggunakan file media, lihat
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=id).

### Meneruskan data audio inline

Daripada mengupload file audio, Anda dapat meneruskan data audio inline dalam permintaan ke `generateContent`:

### Python

```
from google import genai
from google.genai import types

with open('path/to/small-sample.mp3', 'rb') as f:
    audio_bytes = f.read()

client = genai.Client()
response = client.models.generate_content(
  model='gemini-3.6-flash',
  contents=[
    'Describe this audio clip',
    types.Part.from_bytes(
      data=audio_bytes,
      mime_type='audio/mp3',
    )
  ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64AudioFile = fs.readFileSync("path/to/small-sample.mp3", {
  encoding: "base64",
});

const contents = [
  { text: "Please summarize the audio." },
  {
    inlineData: {
      mimeType: "audio/mp3",
      data: base64AudioFile,
    },
  },
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

  audioBytes, _ := os.ReadFile("/path/to/small-sample.mp3")

  parts := []*genai.Part{
      genai.NewPartFromText("Describe this audio clip"),
    &genai.Part{
      InlineData: &genai.Blob{
        MIMEType: "audio/mp3",
        Data:     audioBytes,
      },
    },
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

Beberapa hal yang perlu diingat tentang data audio inline:

- Ukuran permintaan maksimum adalah 20 MB, yang mencakup perintah teks,
  petunjuk sistem, dan file yang disediakan secara inline. Jika ukuran file Anda akan membuat *ukuran total permintaan* melebihi 20 MB, maka gunakan Files API untuk [mengupload file audio](#upload-audio) untuk digunakan dalam permintaan.
- Jika Anda menggunakan sampel audio beberapa kali, akan lebih efisien
  untuk [mengupload file audio](#upload-audio).

## Mendapatkan transkrip

Untuk mendapatkan transkrip data audio, cukup minta di perintah:

### Python

```
from google import genai

client = genai.Client()
myfile = client.files.upload(file='path/to/sample.mp3')
prompt = 'Generate a transcript of the speech.'

response = client.models.generate_content(
  model='gemini-3.6-flash',
  contents=[prompt, myfile]
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
const myfile = await ai.files.upload({
  file: "path/to/sample.mp3",
  config: { mimeType: "audio/mpeg" },
});

const result = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: createUserContent([
    createPartFromUri(myfile.uri, myfile.mimeType),
    "Generate a transcript of the speech.",
  ]),
});
console.log("result.text=", result.text);
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

  localAudioPath := "/path/to/sample.mp3"
  uploadedFile, _ := client.Files.UploadFromPath(
      ctx,
      localAudioPath,
      nil,
  )

  parts := []*genai.Part{
      genai.NewPartFromText("Generate a transcript of the speech."),
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
}
```

## Merujuk pada stempel waktu

Anda dapat merujuk ke bagian tertentu dari file audio menggunakan stempel waktu dalam bentuk
`MM:SS`. Misalnya, perintah berikut meminta transkrip yang

- Dimulai pada 2 menit 30 detik dari awal file.
- Berakhir pada 3 menit 29 detik dari awal file.

### Python

```
# Create a prompt containing timestamps.
prompt = "Provide a transcript of the speech from 02:30 to 03:29."
```

### JavaScript

```
// Create a prompt containing timestamps.
const prompt = "Provide a transcript of the speech from 02:30 to 03:29."
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

  localAudioPath := "/path/to/sample.mp3"
  uploadedFile, _ := client.Files.UploadFromPath(
      ctx,
      localAudioPath,
      nil,
  )

  parts := []*genai.Part{
      genai.NewPartFromText("Provide a transcript of the speech " +
                            "between the timestamps 02:30 and 03:29."),
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
}
```

## Menjumlahkan token

Panggil metode `countTokens` untuk mendapatkan jumlah token dalam file audio. Contoh:

### Python

```
from google import genai

client = genai.Client()
response = client.models.count_tokens(
  model='gemini-3.6-flash',
  contents=[myfile]
)

print(response)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});
const myfile = await ai.files.upload({
  file: "path/to/sample.mp3",
  config: { mimeType: "audio/mpeg" },
});

const countTokensResponse = await ai.models.countTokens({
  model: "gemini-3.6-flash",
  contents: createUserContent([
    createPartFromUri(myfile.uri, myfile.mimeType),
  ]),
});
console.log(countTokensResponse.totalTokens);
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

  localAudioPath := "/path/to/sample.mp3"
  uploadedFile, _ := client.Files.UploadFromPath(
      ctx,
      localAudioPath,
      nil,
  )

  parts := []*genai.Part{
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
  }
  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  tokens, _ := client.Models.CountTokens(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Printf("File %s is %d tokens\n", localAudioPath, tokens.TotalTokens)
}
```

## Format audio yang didukung

Gemini mendukung jenis MIME format audio berikut:

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG Vorbis - `audio/ogg`
- FLAC - `audio/flac`

## Detail teknis tentang audio

- Gemini merepresentasikan setiap detik audio sebagai 32 token; misalnya,
  satu menit audio direpresentasikan sebagai 1.920 token.
- Gemini dapat "memahami" komponen non-ucapan, seperti kicauan burung atau sirene.
- Durasi maksimum data audio yang didukung dalam satu perintah adalah 9,5 jam.
  Gemini tidak membatasi *jumlah* file audio dalam satu perintah; namun,
  total durasi gabungan semua file audio dalam satu perintah tidak boleh melebihi
  9,5 jam.
- Gemini melakukan downsampling file audio ke resolusi data 16 Kbps.
- Jika sumber audio berisi beberapa saluran, Gemini akan menggabungkan saluran tersebut menjadi satu saluran.

## Langkah berikutnya

Panduan ini menunjukkan cara membuat teks sebagai respons terhadap data audio. Untuk mempelajari lebih lanjut,
lihat referensi berikut:

- [Strategi perintah file](https://ai.google.dev/gemini-api/docs/files?hl=id#prompt-guide): Gemini API mendukung perintah dengan data teks, gambar, audio, dan video, yang juga dikenal sebagai perintah multimodal.
- [Petunjuk sistem](https://ai.google.dev/gemini-api/docs/text-generation?hl=id#system-instructions):
  Petunjuk sistem memungkinkan Anda mengarahkan perilaku model berdasarkan kebutuhan dan kasus penggunaan spesifik Anda.
- [Panduan keamanan](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=id): Terkadang model AI generatif menghasilkan output yang tidak terduga, seperti output yang tidak akurat, bias, atau menyinggung. Pemrosesan pasca-dan evaluasi manusia sangat penting untuk membatasi risiko bahaya dari output tersebut.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-12 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-12 UTC."],[],[]]
