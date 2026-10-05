---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=id
fetched_at: 2026-10-05T06:41:54.077400+00:00
title: "Desain suara \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs/generate-content?hl=id)

Kirim masukan

# Desain suara

Desain suara memungkinkan Anda membuat persona vokal persisten yang benar-benar baru dari deskripsi bahasa alami menggunakan endpoint Suara Gemini API (`POST /v1beta/voices`). Daripada terbatas pada suara bawaan atau merekam audio referensi, Anda dapat mendeskripsikan usia, timbre vokal, aksen, dan penyampaian dasar karakter, serta menerima ID `voice_...` yang dapat digunakan kembali dan disimpan ke project Anda.

Cara tercepat untuk mendesain, menguji, dan melakukan iterasi pada suara kustom adalah dengan studio **Desain Suara** interaktif di [Google AI Studio](https://aistudio.google.com/generate-speech?hl=id). Anda dapat
membuat persona kustom dari perintah teks, mengujinya dengan skrip contoh, dan
menyalin ID `voice_...` yang dihasilkan langsung ke kode aplikasi Anda.

[Coba di Google AI Studio](https://aistudio.google.com/generate-speech?hl=id)

[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=id)
(`gemini-3.8-flash-tts`) dan
[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=id)
(`gemini-3.8-flash-lite-tts`) mendukung Desain suara.

## Membuat suara yang didesain

Gunakan Google GenAI SDK (`google-genai` 2.25.0+ / `@google/genai` 2.24.0+) atau REST API
untuk membuat suara kustom dari deskripsi teks. Untuk suara `"prompted"`, `voices.create` (`CreateVoice`) dan `voices.get` (`GetVoice`) menampilkan kolom `sample_audio` hanya output (`mime_type: "audio/wav"`, `data` yang dienkode base64) sehingga Anda dapat langsung mencoba suara yang dihasilkan:

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## Cara kerja desain Voice

1. **Membuat suara yang dipicu:** Panggil `voices.create` (`POST /v1beta/voices`)
   dengan `type="prompted"` dan `store=True`.
2. **Menerima pratinjau `voice_id` dan `sample_audio` persisten:** API
   membuat identitas vokal, menyimpannya di project Anda, dan menampilkan
   ID permanen (misalnya, `voice_abc123...`) bersama dengan `sample_audio`
   (`mime_type: "audio/wav"`, `data` berenkode base64) yang berisi
   audio pratinjau yang dihasilkan untuk suara.
3. **Mensintesis ucapan:** Teruskan `voice_id` di `speechConfig.voiceConfig.voice`
   saat memanggil `generateContent`.

## Menyintesis ucapan dengan suara yang Anda rancang

Teruskan `id` (`voice_...`) yang ditampilkan di `voiceConfig.voice` saat memanggil
`generateContent`:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "speech_metadata": {"style": "reflective and awe-inspired"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": created_voice.id}
        },
    },
)

audio_bytes = response.candidates[0].content.parts[0].inline_data.data
with open("designed_voice.wav", "wb") as f:
    f.write(audio_bytes)
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash-tts",
  contents: [{
    role: "user",
    parts: [{
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      speechMetadata: { style: "reflective and awe-inspired" },
    }],
  }],
  config: {
    responseModalities: ["AUDIO"],
    speechConfig: {
      voiceConfig: { voice: createdVoice.id },
    },
  },
});

const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
if (data) {
  fs.writeFileSync("designed_voice.wav", Buffer.from(data, "base64"));
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [{
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "speech_metadata": {
          "style": "reflective and awe-inspired"
        }
      }]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "voice": "voice_YOUR_DESIGNED_VOICE_ID"
        }
      }
    }
  }'
```

## Mengelola suara Anda

Anda dapat mencantumkan, memfilter, memeriksa, dan menghapus suara tersimpan Anda kapan saja menggunakan
Voices API (lihat
[Library Suara yang Diperluas dan pemfilteran](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=id#voice-library)
untuk semua parameter filter).

- **Batas penyimpanan dan TTL:** Suara stateful (`store=True`, dibagikan di seluruh suara yang diminta dan direplikasi) memiliki batas **200 suara per project**
  dan **TTL 1 tahun** (time-to-live).
- **Ketersediaan `sample_audio`:** `voices.create()` (`CreateVoice`) dan
  `voices.get()` (`GetVoice`) mengisi `sample_audio` (`mime_type:
  "audio/wav"`, `data` berenkode base64) untuk suara `"prompted"`. Agar listingan tetap ringan, `voices.list()` (`ListVoices`) menghilangkan `sample_audio`
  (dan `sample_audio` tidak disetel untuk suara `"replicated"` dan `"prebuilt"`).

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Praktik terbaik perintah untuk desain Voice

- **Masukkan ciri vokal permanen dalam Desain suara, bukan `style`:** Tentukan karakteristik tetap—seperti usia, gender, timbre, karakter suara, dan aksen regional—saat membuat suara di `voices.create`.
- **Cadangkan `speech_metadata.style` untuk emosi situasional:** Setelah suara kustom Anda dibuat, gunakan perintah `style` singkat (misalnya, `"whispered urgently"` atau `"cheerful and energetic"`) untuk mengarahkan akting belokan demi belokan tanpa mengubah identitas inti pembicara.
- **Buat perintah yang spesifik dan ringkas:** Deskripsi 1–2 kalimat yang jelas (seperti
  *"Seorang komentator olahraga yang bersemangat dan fasih di usia 30-an dengan sedikit aksen
  Midwest"*) akan menghasilkan hasil yang lebih bersih dan konsisten daripada paragraf yang
  bertentangan atau terlalu panjang.

## Langkah berikutnya

- Pelajari cara mereplikasi suara penutur yang ada di
  [Replikasi suara](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=id).
- Pelajari gaya tingkat giliran bicara, tag inline, dan dialog multi-penutur dalam
  [Panduan text-to-speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-24 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-24 UTC."],[],[]]
