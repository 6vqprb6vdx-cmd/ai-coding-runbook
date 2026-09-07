---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=id
fetched_at: 2026-09-07T05:41:08.120478+00:00
title: "Yang baru di Gemini 3.8 Flash \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Yang baru di Gemini 3.8 Flash

[Lihat semua model](https://ai.google.dev/gemini-api/docs/models?hl=id)

Gemini 3.8 Flash (`gemini-3.8-flash`) tersedia secara umum (GA) dan siap digunakan untuk produksi. Model Flash ini adalah model tercerdas kami, yang dirancang untuk rekayasa software dengan cakupan panjang, agen otonom, dan alur kerja perusahaan yang kompleks.

Panduan ini menjelaskan hal-hal baru di Gemini 3.8 Flash, perubahan API, contoh kode, dan panduan migrasi.

## Model baru

| Model | ID Model | Tingkat penalaran default | Harga | Deskripsi |
| --- | --- | --- | --- | --- |
| Gemini 3.8 Flash | `gemini-3.8-flash` | `medium` | 3.8 Flash tersedia hingga akhir tahun dengan harga perkenalan $0,75/1 juta token input dan $3,75/1 juta token output; lihat [harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id) untuk mengetahui detail selengkapnya. | Model Flash tercerdas kami, yang dirancang untuk rekayasa software dengan cakupan waktu panjang, agen otonom, dan alur kerja perusahaan yang kompleks. |

Gemini 3.8 Flash mendukung jendela konteks 1 juta token, token output maksimal 64 ribu, tingkat pemikiran yang dapat disesuaikan (`low`, `medium`, `high`), dan rangkaian alat bawaan yang sama.

Untuk mengetahui spesifikasi lengkapnya, lihat [halaman model Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=id). Untuk mengetahui detail harga perkenalan, lihat [bagian harga](#pricing) di bawah atau [halaman harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id#gemini-3.8-flash).

## Panduan memulai

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Write a three.js script that renders a realistic 3D black hole."
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Write a three.js script that renders a realistic 3D black hole.",
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders a realistic 3D black hole."}]
    }]
  }'
```

## Yang baru di Gemini 3.8 Flash

- **Rekayasa software dengan cakupan luas:** Memberikan hasil yang kuat pada benchmark coding dunia nyata, refactoring multi-file yang kompleks, dan eksekusi alat deterministik. Lihat [metodologi evaluasi](https://deepmind.google/models/evals-methodology/gemini-3-8-flash/?hl=id) untuk mengetahui detailnya.
- **Agen otonom:** Memungkinkan Anda membangun alur kerja perencanaan multilangkah dan orkestrasi alat yang tangguh, sehingga secara signifikan mengurangi kegagalan loop dan error.
- **Alur kerja perusahaan yang kompleks:** Memberikan akurasi yang lebih baik, penalaran yang mendalam, dan ketelitian faktual yang tinggi di seluruh tugas domain yang menuntut dan pipeline data skala besar.
- **Model default untuk Agen Terkelola:** Agen default untuk agen terkelola: [Agen Antigravitasi](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id), kini menggunakan Gemini 3.8 Flash. [Antigravity SDK](https://antigravity.google/docs/sdk/overview/?hl=id) juga menggunakan Gemini 3.8 Flash secara default.
- **Harga perkenalan:** Gemini 3.8 Flash tersedia dengan tarif perkenalan sebesar $0,75/1 juta token input dan $3,75/1 juta token output hingga 31 Desember 2026. Harga standar sebesar $1,50/1 Jt token input dan $7,50/1 Jt token output akan berlaku mulai 1 Januari 2027.

Gemini 3.8 Flash dapat menggunakan lebih banyak token pada tugas yang berjalan lebih lama dan kompleks, berdasarkan desainnya. Untuk memberikan hasil yang berkualitas lebih tinggi pada tujuan multi-langkah yang sulit, model mengambil langkah-langkah penalaran yang lebih kecil, memanggil alat secara berulang, dan memverifikasi pekerjaannya di sepanjang proses. Tidak semua alur kerja memerlukan tingkat verifikasi ini. Untuk tugas sehari-hari, Anda dapat menurunkan upaya [penalaran](#understanding-reasoning-levels) untuk mengurangi konsumsi token. Atau, Gemini 3.7 Flash tetap didukung sepenuhnya.

## Memahami tingkat penalaran

Gemini 3.8 Flash memberi Anda kontrol yang fleksibel atas latensi dan kecerdasan dengan menyesuaikan tingkat penalaran model:

- **Upaya berpikir yang rendah**: Mengurangi waktu untuk menjawab tugas-tugas penting dengan latensi rendah seperti pipeline respons insiden, chat real-time, penulisan draf, dan analisis data cepat.
- **Sedang (default):** Kualitas terbaik untuk sebagian besar tugas. Direkomendasikan untuk kode kompleks dan kasus penggunaan agentic, yang memberikan akurasi lintasan pertama yang lebih tinggi.
- **Upaya penalaran tinggi**: Memaksimalkan kemampuan penalaran dan orkestrasi alat model. Terbaik untuk penalaran mendalam, matematika, dan tugas multi-langkah yang sulit.

Contoh berikut menetapkan `thinking_level` ke `medium` untuk permintaan analisis kode kompleks:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="medium"  # Balanced reasoning effort for complex tasks
        ),
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  config: {
    thinkingConfig: {
      thinkingLevel: "medium", // Balanced reasoning effort for complex tasks
    },
  },
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely."}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "medium"
      }
    }
  }'
```

## Agen Antigravity yang diperbarui

## Checklist migrasi

```
  `/gemini-api-dev migrate my app to Gemini 3.8 Flash`
```

### Bermigrasi ke gemini-3.8-flash

- **Perbarui ID Model:** Ubah string model target Anda menjadi `gemini-3.8-flash`.
- **Menghapus parameter pengambilan sampel yang tidak digunakan lagi:**
  - Hapus `temperature`, `top_p`, dan `top_k` dari konfigurasi pembuatan.
  - Ganti `thinking_budget` dengan enum string `thinking_level`. Perhatikan bahwa `minimal` tidak didukung di Flash 3.8.
  - Menghapus `candidate_count` (tidak didukung di Gemini 3 dan yang lebih baru).
- **Menerapkan aturan validasi belokan:**
  - Menghapus giliran model yang telah diisi otomatis.
  - Pastikan giliran pengguna akhir berisi teks yang tidak kosong.
- **Mengaudit pemanggilan fungsi:**
  - Tempatkan aset multimodal di dalam payload respons.
  - Format petunjuk inline menggunakan `\n\n`.
  - Jika Anda melihat error `Malformed_Function_Call` yang terkait dengan teks sebelum alat, lihat [Solusi untuk persyaratan teks sebelum alat](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=id#workarounds-for-pre-tool-text-requirements).
  - Khusus jika menggunakan generateContent API: Pastikan semua objek `FunctionResponse` menyertakan `call_id` dan `name`.
- **Persyaratan dasar Gemini 3:** Untuk pembaruan SDK dan pelestarian tanda tangan pemikiran, lihat [Daftar Periksa Migrasi Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=id#migration).

## Harga

Manfaatkan harga perkenalan di Google AI Studio dan Gemini Enterprise Agent Platform hingga 31 Desember 2026 untuk Gemini 3.8 Flash, Gemini 3.7 Flash, dan Gemini 3.6 Flash. Harga standar akan berlaku mulai 1 Januari 2027. Untuk mengetahui tingkat harga lengkap, lihat [halaman harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id#gemini-3.8-flash).

## Langkah berikutnya

- Tinjau spesifikasi API di [Ringkasan Model](https://ai.google.dev/gemini-api/docs/models?hl=id).
- Pelajari orkestrasi multi-agen di [Ringkasan Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id).
- Uji dan sempurnakan perintah di [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-03 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-03 UTC."],[],[]]
