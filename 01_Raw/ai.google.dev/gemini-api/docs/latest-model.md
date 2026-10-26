---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=id
fetched_at: 2026-10-26T05:55:39.473468+00:00
title: "Yang baru di Gemini 4 Argon \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Yang baru di Gemini 4 Argon

Gemini 4 Argon (`gemini-4-argon`) adalah model terbaru dan tercanggih kami. Model ini dapat melakukan penalaran lebih lama pada masalah sulit untuk memberikan hasil yang lebih baik pada tugas coding, agentic, matematika, dan sains yang kompleks. Gemini 4 Argon tersedia melalui Gemini API dan di Google AI Studio.

Gemini 4 Argon mendukung jendela konteks 1 juta token terpadu, dekode panjang hingga 1 juta token, dan level penalaran yang dapat disesuaikan (`low`, `medium`, `high`).

[experiment

Coba di AI Studio

Bangun aplikasi dari awal dengan Gemini 4 Argon dan AI Studio.](https://aistudio.google.com/apps?model=gemini-4-argon&hl=id)
[smart\_toy

Galeri Aplikasi

Mainkan dan remix aplikasi, yang dibuat dengan Gemini 4 Argon.](https://aistudio.google.com/learn/gemini-4-argon-showcase?hl=id)
[rocket\_launch

Mulai

Mulai gunakan Gemini 4 Argon dengan perintah pemicu.](https://aistudio.google.com/learn/gemini-4-argon?hl=id)

Panduan ini menjelaskan hal-hal baru di Gemini 4 Argon, perubahan API, contoh kode, dan panduan migrasi.

## Model baru

| Model | ID Model | Tingkat penalaran default | Harga | Deskripsi |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | `gemini-4-argon` | `medium` | Tersedia hingga 30 November 2026 dengan harga perkenalan $2/1 juta token input dan $10/1 juta token output (setelahnya $4/1 juta token input dan $20/1 juta token output). Lihat [harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id) untuk mengetahui detail selengkapnya. | Model tercanggih kami, yang dibuat untuk memecahkan masalah tersulit dengan mendalam dan presisi di berbagai tugas rekayasa software dan pekerjaan pengetahuan di dunia nyata. |

Untuk mengetahui detail selengkapnya, lihat [halaman model Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=id). Untuk mengetahui detail harga perkenalan, lihat [bagian harga](#pricing) di bagian bawah halaman ini atau [halaman harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id#gemini-4-argon).

## Panduan memulai

Gunakan contoh berikut untuk mengirim permintaan ke `gemini-4-argon` dengan `thinking_level` default yang direkomendasikan (`medium`) dan batas token output 64K:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Write a three.js script that renders a realistic 3D black hole with gravitational lensing."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
});

console.log(interaction.output_text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a three.js script that renders a realistic 3D black hole with gravitational lensing."
  }'
```

## Yang baru di Gemini 4 Argon

- **Batas token input-output 1 juta terpadu:** Input, penalaran, dan output berbagi satu jendela berisi 1.048.576 token.
- **Dekode panjang:** Satu respons kini dapat melampaui 64 ribu token, hingga 1 juta token dikurangi input Anda. Lihat [Dekode panjang](https://ai.google.dev/gemini-api/docs/long-decode?hl=id).
- **Pemahaman video agentic tersedia secara umum:** [Pemahaman video agentic](https://ai.google.dev/gemini-api/docs/video-understanding?hl=id#agentic-video-understanding) kini tersedia secara umum.
- **Didukung di Agen Terkelola:** [Agen Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id) di Agen Terkelola Gemini kini mendukung Gemini 4 Argon.

Untuk mengetahui spesifikasi lengkapnya, lihat [halaman model Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=id). Untuk mengetahui detail harga, lihat [halaman harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id#gemini-4-argon).

## Output lebih besar dan dekode panjang

Gemini 4 Argon dapat berpikir lebih lama untuk menyelesaikan soal matematika, sains, dan coding yang sulit.

- **Gunakan `thinking_level` untuk mengontrol kedalaman penalaran:** Tingkat penalaran menentukan seberapa dalam model melakukan penalaran sebelum menjawab. `max_output_tokens` adalah batas tetap: respons akan berhenti setelah penalaran dan output mencapai batas tersebut, jadi tetapkan nilai yang cukup tinggi agar jawaban tidak terpotong.
- **Buat hingga 1 juta token dengan eksekusi latar belakang:** Gunakan eksekusi latar belakang dengan `max_output_tokens` lebih besar dari 65.536 untuk memungkinkan satu respons melampaui 64 ribu token, hingga 1 juta token. Model ini menghasilkan respons panjang dalam lompatan hingga 64 ribu token, dan setiap lompatan berlanjut dari tempat lompatan sebelumnya berhenti. Dengan eksekusi latar belakang, server kami menjalankan hop kelanjutan ini untuk Anda. Karena setiap hop menambahkan langkah `model_output` ke `interaction.steps`, gabungkan teks di semua langkah `model_output` saat interaksi selesai.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Write a complete, rigorous proof of the prime number theorem.",
    background=True,
    generation_config={
        "max_output_tokens": 262144,
        "thinking_level": "high",
    },
)

while interaction.status in ("in_progress", "queued"):
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Each hop adds a model_output step, so join the text of all of them.
text = "".join(
    content.text
    for step in interaction.steps
    if step.type == "model_output"
    for content in step.content
    if content.type == "text"
)
print(text)
print("Status:", interaction.status)
print("Usage:", interaction.usage)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Write a complete, rigorous proof of the prime number theorem.",
  background: true,
  generation_config: {
    max_output_tokens: 262144,
    thinking_level: "high",
  },
});

while (interaction.status === "in_progress" || interaction.status === "queued") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await client.interactions.get(interaction.id);
}

// Each hop adds a model_output step, so join the text of all of them.
const text = interaction.steps
  .filter((step) => step.type === "model_output")
  .flatMap((step) => step.content ?? [])
  .filter((content) => content.type === "text")
  .map((content) => content.text)
  .join("");
console.log(text);
console.log("Status:", interaction.status);
console.log("Usage:", interaction.usage);
```

### REST

```
ID=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a complete, rigorous proof of the prime number theorem.",
    "background": true,
    "generation_config": {
      "max_output_tokens": 262144,
      "thinking_level": "high"
    }
  }' | jq -r '.id')

while true; do
  RESP=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
  STATUS=$(echo "$RESP" | jq -r '.status')
  if [[ "$STATUS" != "in_progress" && "$STATUS" != "queued" ]]; then
    echo "$RESP" | jq -r '[.steps[]? | select(.type == "model_output") | .content[]? | select(.type == "text") | .text] | join("")'
    break
  fi
  sleep 5
done
```

Eksekusi latar belakang adalah cara termudah untuk menjalankan dekode yang panjang. Fungsi ini menjalankan loop lanjutan di sisi server hingga model selesai atau mencapai `max_output_tokens`. Jika Anda memerlukan kontrol yang lebih mendetail atas percobaan ulang, backoff, dan penanganan error (atau tidak ingin interaksi Anda disimpan), Anda dapat menggunakan kelanjutan sisi klien di [GenerateContent API](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=id). Kelanjutan sisi klien juga akan segera hadir di Interactions API. Untuk streaming, koneksi ulang, penghitungan token, dan kapan harus menggunakan dekode panjang, lihat [panduan dekode panjang](https://ai.google.dev/gemini-api/docs/long-decode?hl=id).

### Menetapkan batas token output

`max_output_tokens` menetapkan total token penalaran dan output untuk respons. Tetapkan nilai yang cukup tinggi agar penalaran tidak memotong jawaban, dan cukup rendah untuk membatasi pengeluaran saat perintah yang sulit menggunakan semuanya.

Gunakan nilai ini sebagai titik awal:

- **Tugas standar:** Pertahankan nilai default 65.536 atau jangan tetapkan nilai apa pun.
- **Aplikasi yang sudah ada dengan batas lebih rendah dari 32K:** Naikkan `max_output_tokens` menjadi minimal 32.768. Gemini 4 Argon dapat menggunakan lebih banyak batas untuk berpikir dibandingkan model sebelumnya. Untuk menggunakan lebih sedikit token, turunkan tingkat penalaran.
- **Penalaran dan coding yang kompleks:** Tetapkan `background: true` dan tetapkan `max_output_tokens` ke 131.072 atau 262.144, hingga 1.048.576 dikurangi token input Anda.

## Memahami tingkat penalaran

[Tingkat penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id) adalah kontrol utama Anda atas kualitas, latensi, dan penggunaan token di Gemini 4 Argon:

| Tingkat penalaran | Penggunaan token | Kapan digunakan |
| --- | --- | --- |
| `low` | Token paling sedikit, latensi terendah | Tugas yang lebih sederhana dan pekerjaan yang sensitif terhadap biaya. Juga berfungsi untuk tugas analisis dan penulisan yang memerlukan pemikiran ringan. Kualitas dapat menurun pada tugas yang sulit. |
| `medium` (default) | Seimbang | Direkomendasikan untuk sebagian besar tugas, termasuk kode yang kompleks dan kasus penggunaan agentic. |
| `high` | Token terbanyak, token pertama paling lambat | Penalaran kompleks, matematika dan sains yang sulit, serta tugas kode atau agen yang paling sulit. Cocok dengan dekode panjang untuk output panjang. |

Jalankan evaluasi di ketiga level, lalu pilih level terendah yang memenuhi standar kualitas Anda. Untuk mempelajari lebih lanjut, lihat [panduan penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    generation_config={
        "thinking_level": "medium"  # Balanced reasoning effort for complex tasks
    }
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  generation_config: {
    thinking_level: "medium", // Balanced reasoning effort for complex tasks
  },
});

console.log(interaction.output_text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-4-argon",
    "input": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    "generation_config": {
      "thinking_level": "medium"
    }
  }'
```

## Gemini 4 Argon di Agen Terkelola

[Agen Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id) di Agen Terkelola Gemini mendukung Gemini 4 Argon. Untuk menggunakannya, tetapkan model di `agent_config`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input=(
        "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
        "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
        "Check search indexing with Google Search for site:web.dev. "
        "Format the output as a side-by-side scorecard table with prioritized fixes."
    ),
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-4-argon",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  agent: "antigravity-preview-09-2026",
  input:
    "Audit https://web.dev for performance, Core Web Vitals, and SEO. " +
    "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. " +
    "Check search indexing with Google Search for site:web.dev. " +
    "Format the output as a side-by-side scorecard table with prioritized fixes.",
  environment: "remote",
  agent_config: {
    type: "antigravity",
    model: "gemini-4-argon",
  },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google'\''s PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
    "environment": "remote",
    "agent_config": {
      "type": "antigravity",
      "model": "gemini-4-argon"
    }
  }'
```

Untuk opsi lainnya, lihat [pemilihan model](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id#model-selection) di panduan agen Antigravity.

## Checklist migrasi

```
  `/gemini-api-dev migrate my app to Gemini 4 Argon`
```

### Bermigrasi ke gemini-4-argon

- **Memperbarui ID model:** Ubah string model target Anda menjadi `gemini-4-argon`.
- **Tinjau `max_output_tokens`:** Jika Anda menetapkannya secara eksplisit saat ini, pertimbangkan untuk menaikkannya. Sebaiknya gunakan minimal 32.768, karena Gemini 4 Argon dapat menggunakan lebih banyak batas untuk penalaran.
- **Konfigurasi tingkat penalaran:** Pilih `low`, `medium` (default), atau `high`, dan uji workload Anda di ketiga tingkat tersebut.
- **Beralih dari cache konteks eksplisit:** Cache eksplisit (`cachedContents` / `caches.create`) tidak didukung di Gemini 4 Argon. Hapus panggilan yang membuat atau mereferensikan `cached_content` dari permintaan Anda. [Penyimpanan ke cache implisit](https://ai.google.dev/gemini-api/docs/caching?hl=id) diaktifkan secara default untuk perintah dengan minimal 4.096 token dan memberikan diskon 95% untuk token input yang di-cache saat cache ditemukan.
- **Hapus parameter pengambilan sampel:** Hapus `temperature`, `top_p`, dan `top_k` dari permintaan Anda. Jika disediakan, parameter tersebut akan diabaikan.
- **Gunakan eksekusi latar belakang untuk output panjang:** Untuk tugas yang memerlukan lebih dari 64 ribu token, tetapkan `background` ke true dan `max_output_tokens` lebih besar dari 65.536.
- **Tingkatkan waktu tunggu klien:** Perintah sulit dapat memerlukan waktu beberapa menit. Gunakan eksekusi latar belakang, atau tetapkan waktu tunggu klien HTTP minimal 15 menit.
- **Menyimpan status percakapan di server:** Gunakan `previous_interaction_id` untuk percakapan multi-turn dan panggilan fungsi.

## Harga

Gemini 4 Argon tersedia dengan harga perkenalan hingga 30 November 2026:

- **Token input:** $2,00 per 1 juta token ($4,00 mulai 1 Desember 2026)
  - **Token input yang di-cache:** Cache implisit mendiskon input yang di-cache sebesar 95%, menjadi $0,10 per 1 juta token ($0,20 mulai 1 Desember 2026).
- **Token output, termasuk token penalaran:** $10,00 per 1 juta token ($20,00 mulai 1 Desember 2026)

Gemini 4 Argon tidak tersedia di paket Gratis. Untuk mengetahui tingkat harga lengkap, lihat [halaman harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id#gemini-4-argon).

## Model lainnya

- [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=id)
- [Gemini 3.6 Flash dan 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=id)
- [Lihat semua model](https://ai.google.dev/gemini-api/docs/models?hl=id)

## Langkah berikutnya

- Baca [panduan dekode panjang](https://ai.google.dev/gemini-api/docs/long-decode?hl=id) untuk streaming, koneksi ulang, dan penghitungan token.
- Pelajari cara kerja tingkat penalaran dan ringkasan penalaran dalam [panduan penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id).
- Pelajari tugas yang berjalan lama di [panduan eksekusi latar belakang](https://ai.google.dev/gemini-api/docs/background-execution?hl=id).
- Menguji dan menyempurnakan perintah di [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-16 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-16 UTC."],[],[]]
