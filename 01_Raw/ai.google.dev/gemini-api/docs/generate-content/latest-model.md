---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=id
fetched_at: 2026-08-31T06:33:01.175882+00:00
title: "Menggunakan model Gemini terbaru \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Menggunakan model Gemini terbaru

[Halaman ini](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=id)

Gemini 3.6 Flash (`gemini-3.6-flash`) dan Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) tersedia secara umum (GA) dan siap digunakan untuk produksi.

- **Gemini 3.6 Flash**: Performa yang lebih baik untuk tugas multimodal dan agentik yang kompleks sekaligus mengurangi penggunaan token, dengan titik harga yang lebih rendah daripada 3.5 Flash.
- **Gemini 3.5 Flash-Lite**: Model tercepat dan paling hemat biaya dalam rangkaian 3.5. Mengungguli generasi Flash-Lite sebelumnya untuk eksekusi throughput tinggi.

Panduan ini menjelaskan hal-hal baru di setiap model, perubahan API yang memengaruhi kode Anda, dan cara melakukan migrasi.

### Gemini 3.6 Flash

1. Instal skill:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Terapkan keahlian:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Instal skill:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Terapkan keahlian:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## Model baru

| Model | ID Model | Tingkat penalaran default | Harga | Deskripsi |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | $1,50/1 Juta token input dan $7,50/1 Juta token output | Menyeimbangkan kecepatan dengan kecerdasan untuk tugas agentic dan multimodal. |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | $0,30/1 Juta token input dan $2,50/1 Juta token output | Model 3.5 tercepat dan berbiaya terendah untuk eksekusi throughput tinggi. |

Kedua model mendukung jendela konteks 1 juta token, token output maksimum 64 ribu, kemampuan berpikir, dan rangkaian lengkap alat bawaan termasuk [Penggunaan Komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id).

Untuk melihat spesifikasi lengkap, lihat halaman model:

- [Halaman model Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=id)
- [Halaman model Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=id)

Untuk mengetahui harga mendetail, lihat [halaman harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id).

## Panduan memulai

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Write a three.js script that renders an interactive 3D robot.",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Write a three.js script that renders an interactive 3D robot.",
  });
  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }]
  }'
```

## Yang baru di Gemini 3.6 Flash

- **Pengurangan token dan giliran:** Menyelesaikan alur kerja multi-langkah dengan lebih sedikit langkah penalaran, giliran percakapan, dan panggilan alat dibandingkan Gemini 3.5. Hal ini juga mengurangi spiral loop eksekusi.
- **Peningkatan pembuatan kode:** Menghasilkan kode siap produksi berkualitas lebih tinggi dengan lebih sedikit pengeditan yang tidak diinginkan dan lebih sedikit loop proses debug.
- **Kualitas mengikuti perintah yang lebih baik**: Mengurangi perubahan file yang tidak diinginkan selama tugas diagnostik.
- **Kemampuan penalaran multimodal dan spasial yang kuat:** Peningkatan performa dalam interpretasi diagram, konversi cetak biru visual, dan pembuatan tata letak web multi-elemen.
- **Pemeriksaan terprogram di awal:** Lebih sering menjalankan skrip kode diagnostik sebelum melakukan perubahan daripada Gemini 3.5 Flash. Hal ini meningkatkan akurasi pada tugas yang kompleks, tetapi dapat menambahkan langkah eksplorasi ekstra pada pekerjaan frontend yang sederhana.
- **Dukungan Penggunaan Komputer:** Didukung sebagai alat native untuk otomatisasi UI berbasis agen.
- **Preferensi gaya UI**: Lebih baik dalam membuat kode fungsional, meskipun evaluator manusia lebih menyukai model sebelumnya untuk tata letak visual dan gaya. Anda dapat memitigasi hal ini dengan memberikan panduan desain yang jelas.
- **Upaya penalaran default (sedang):** Menggunakan tingkat penalaran default `medium` yang sama dengan Gemini 3.5 Flash.
- **Harga yang lebih rendah**: Biaya token output yang lebih rendah ($7,50/1 juta vs. $9,00/1 juta untuk 3.5 Flash). Token input tetap $1,50/1M.

## Yang baru di Gemini 3.5 Flash-Lite

- **Latensi eksekusi tugas yang lebih rendah:** Throughput tertinggi dalam keluarga 3.5 untuk penguraian data dan ekstraksi dokumen dalam volume tinggi.
- **Performa multimodal dan penalaran yang ditingkatkan:** Jalur migrasi yang kuat dari Gemini 2.5 Flash, dengan skor yang lebih tinggi pada tugas penalaran seperti HLE (18,0% vs. 11,0%) dan tolok ukur multimodal seperti CharXIV (74,5% vs. 63,7%).
- **Orkestrasi sub-agen dan keandalan alat:** Meningkatkan keandalan eksekusi alat untuk eksekusi kode, penelusuran, dan alur kerja MCP. Meningkatkan tingkat pemikiran untuk perencanaan otonom dan tugas sub-agen yang kompleks.
- **Peningkatan pemahaman dokumen:** Meningkatkan akurasi penguraian dokumen dan ekstraksi data terstruktur. Bereksperimenlah dengan tingkat penalaran minimal dan tinggi, bergantung pada kompleksitas dokumen.
- **Pemrosesan data tabular dan coding web interaktif:** Berperforma baik dalam pemrosesan data tabular dan JavaScript frontend dengan merencanakan melalui eksekusi kode ringan.
- **Ketekunan chatbot dan persona:** Mengikuti petunjuk multi-turn yang lebih kuat dan konsistensi persona dibandingkan Gemini 3.1 Flash-Lite.
- **Dukungan Penggunaan Komputer:** Didukung sebagai alat native untuk otomatisasi UI berbasis agen.

## Memilih model Flash atau Flash-Lite yang tepat

Gunakan tabel ini untuk memilih model dan jalur migrasi yang tepat untuk workload Anda.

Kedua model memerlukan penghapusan parameter pengambilan sampel yang tidak digunakan lagi (`temperature`, `top_p`, `top_k`) dan giliran model yang telah diisi sebelumnya. Lihat [Perubahan API](#api-changes-and-parameter-updates) untuk mengetahui detailnya.

| Model | Kasus penggunaan utama | Target migrasi yang direkomendasikan |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | Pembuatan kode, penalaran spasial/multimodal, alur kerja agentic multi-langkah | **Gemini 3.5 Flash**, **Gemini 3 Flash (Pratinjau)**, atau **Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite**  `gemini-3.5-flash-lite` | Eksekusi sub-agen otonom, analisis data dan ekstraksi dokumen dalam volume tinggi, penguraian JSON terstruktur | **Gemini 3.1 Flash-Lite** atau **Gemini 2.5 Flash** |

## Agen Antigravity yang diperbarui

Berkat peningkatan performanya, Gemini 3.6 Flash kini menjadi model default baru yang mendukung [agen Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agentn?hl=id) di Agen Terkelola Gemini. Hal ini dapat diubah dengan menyetel kolom baru di API.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Perubahan API dan pembaruan parameter

Mulai dari Gemini 3.6 Flash dan Gemini 3.5 Flash-Lite, perubahan API berikut berlaku untuk model ini dan semua rilis model Gemini mendatang.

- **Penghentian parameter pengambilan sampel**: `temperature`, `top_p`, dan `top_k` tidak digunakan lagi. API mengabaikan parameter ini dan menampilkan error dalam pembuatan model mendatang.
- **Validasi pergantian model yang telah diisi otomatis**: Pengisian otomatis pergantian model tidak lagi didukung. Jika giliran terakhir yang tidak kosong dalam permintaan adalah giliran `model`, API akan menampilkan error `400`.

Berikut penjelasan mendetail dan contoh kode untuk setiap perubahan API.

### 1. Penghentian penggunaan parameter pengambilan sampel (`temperature`, `top_p`, `top_k`)

`temperature`, `top_p`, dan `top_k` tidak digunakan lagi dan diabaikan. Pada generasi model mendatang, penyediaan parameter ini akan menampilkan error HTTP 400. **Hapus parameter ini dari semua permintaan.**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

Untuk meningkatkan determinisme, tentukan petunjuk sistem dengan aturan eksplisit untuk kasus penggunaan spesifik Anda.

### 2. Validasi pergantian model yang sudah diisi otomatis

Permintaan API yang diakhiri dengan giliran peran model yang tidak kosong tidak diizinkan dan akan menampilkan **Error HTTP 400**.

#### ⚠️ Hindari

Dalam payload REST mentah atau `generateContent` lama, mengakhiri dengan pergantian peran model kini tidak diizinkan:

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ Migrasi yang Direkomendasikan

Jika aplikasi Anda sebelumnya mengisi otomatis giliran model untuk menyembunyikan kata pengantar atau memaksakan pemformatan JSON, gunakan `system_instruction` atau [Output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id).

```
# ✅ RECOMMENDED: Use system_instruction to specify output format
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Translate 'Hello world' to Spanish.",
    config={"system_instruction": "Output only the translation without introductory text."},
)
```

## Checklist migrasi

### Gemini 3.6 Flash

1. Instal skill:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Terapkan keahlian:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Instal skill:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Terapkan keahlian:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### Bermigrasi ke gemini-3.6-flash

- **Perbarui ID Model:** Ubah string model target Anda menjadi `gemini-3.6-flash`.
- **Menghapus parameter pengambilan sampel yang tidak digunakan lagi:**
  - Hapus `temperature`, `top_p`, dan `top_k` dari konfigurasi pembuatan.
  - Ganti `thinking_budget` dengan enum string `thinking_level` yang ditetapkan ke `"medium"` atau `"high"`.
  - Menghapus `candidate_count` (tidak didukung di Gemini 3.x).
- **Menerapkan aturan validasi belokan:**
  - Menghapus giliran model yang telah diisi otomatis.
  - Pastikan giliran pengguna akhir berisi teks yang tidak kosong.
- **Mengaudit pemanggilan fungsi:**
  - Pastikan semua objek `FunctionResponse` menyertakan `call_id` dan `name`.
  - Tempatkan aset multimodal di dalam payload respons.
  - Format petunjuk inline menggunakan `\\n\\n`.
  - Jika Anda melihat error `Malformed_Function_Call` yang terkait dengan teks sebelum alat, lihat [Solusi untuk persyaratan teks sebelum alat](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=id#workarounds-for-pre-tool-text-requirements).
- **Persyaratan dasar Gemini 3.x:** Untuk update SDK dan pelestarian tanda tangan pemikiran, lihat [Daftar Periksa Migrasi Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=id#migration).

### Bermigrasi ke gemini-3.5-flash-lite

- **Perbarui ID Model:** Ubah string model target Anda menjadi `gemini-3.5-flash-lite`.
- **Mengonfigurasi tingkat upaya penalaran:**
  - Untuk ekstraksi, pemilihan rute, atau klasifikasi volume tinggi: biarkan `thinking_level` di `"minimal"` (default) untuk throughput maksimum.
  - Untuk sub-agen otonom dengan panggilan alat, eksekusi kode, atau penalaran multi-langkah: tetapkan `thinking_level` ke `"medium"` atau `"high"` untuk mencegah penghentian alat sebelum waktunya.
- **Menghapus parameter yang tidak digunakan lagi dan memvalidasi panggilan fungsi:** Terapkan [aturan yang sama seperti 3.6 Flash](#migrate-to-gemini-3-6-flash).
- **Persyaratan dasar Gemini 3.x:** Lihat [Daftar Periksa Migrasi Gemini 3.5](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=id#migration).

## Langkah berikutnya

- Tinjau spesifikasi API di [Ringkasan Model](https://ai.google.dev/gemini-api/docs/models?hl=id).
- Pelajari orkestrasi multi-agen di [Panduan Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=id).
- Uji dan sempurnakan perintah di [Google AI Studio](https://aistudio.google.com/?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
