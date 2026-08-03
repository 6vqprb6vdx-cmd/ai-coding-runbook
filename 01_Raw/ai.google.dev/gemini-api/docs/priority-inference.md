---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=id
fetched_at: 2026-08-03T04:38:09.413185+00:00
title: "Inferensi prioritas \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Inferensi prioritas

Deskripsi: Pelajari cara mengoptimalkan latensi dengan tingkat inferensi Prioritas di Interactions API

Gemini Priority API adalah tingkat inferensi premium yang dirancang untuk
workload penting bisnis yang memerlukan latensi lebih rendah dan
keandalan tertinggi dengan titik harga premium. Traffic tingkat prioritas diprioritaskan di atas traffic API standar dan tingkat Flex.

Inferensi prioritas tersedia di seluruh endpoint Interactions API.

## Cara menggunakan Prioritas

Untuk menggunakan tingkat Prioritas, tetapkan kolom `service_tier` dalam permintaan Anda ke `priority`. Paket defaultnya adalah standar jika kolom ini tidak diisi.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Triage this critical customer support ticket immediately.",
    service_tier='priority'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
    const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Cara kerja Inferensi prioritas

Inferensi prioritas merutekan permintaan ke antrean komputasi dengan kritikalitas tinggi, sehingga menawarkan performa yang cepat dan dapat diprediksi untuk aplikasi yang ditampilkan kepada pengguna. Mekanisme
utamanya adalah downgrade sisi server yang lancar ke pemrosesan standar untuk traffic
yang melebihi batas dinamis, sehingga memastikan stabilitas aplikasi, bukan membuat
permintaan gagal.

| Fitur | Prioritas | Standar | Lipat | Batch |
| --- | --- | --- | --- | --- |
| **Harga** | 75-100% lebih banyak daripada Standard | Harga penuh | Diskon 50% | Diskon 50% |
| **Latensi** | Detik | Detik ke menit | Menit (target 1–15 menit) | Hingga 24 jam |
| **Keandalan** | Tinggi (Tidak rontok) | Tinggi / Sedang-tinggi | Upaya terbaik (Dapat Dibatalkan) | Tinggi (untuk throughput) |
| **Antarmuka** | Sinkron | Sinkron | Sinkron | Asinkron |

### Manfaat utama

- **Latensi rendah**: Dirancang untuk waktu respons dalam hitungan detik untuk alat AI interaktif yang ditujukan bagi pengguna.
- **Keandalan tinggi**: Traffic diperlakukan dengan tingkat kritikalitas tertinggi dan
  sangat tidak dapat dibatalkan.
- **Degradasi halus**: Lonjakan traffic yang melebihi batas dinamis akan diturunkan secara otomatis ke tingkat Standard untuk diproses, bukan gagal, sehingga mencegah gangguan layanan.
- **Gesekan rendah**: Menggunakan metode `create` sinkron yang sama dengan tingkat standar dan Flex.

### Kasus penggunaan

Pemrosesan prioritas sangat ideal untuk alur kerja penting bisnis yang mengutamakan performa dan keandalan.

- **Aplikasi AI interaktif**: Chatbot dan kopilot layanan pelanggan yang
  penggunanya membayar biaya premium dan mengharapkan respons yang cepat dan konsisten.
- **Mesin pengambilan keputusan real-time**: Sistem yang memerlukan hasil yang sangat andal dan berlatensi rendah, seperti triase tiket live atau deteksi penipuan.
- **Fitur pelanggan premium**: Developer yang perlu menjamin tujuan tingkat layanan (SLO) yang lebih tinggi untuk pelanggan berbayar.

### Batas kapasitas

Penggunaan prioritas memiliki batas kapasitasnya sendiri meskipun penggunaan dihitung dalam [batas kapasitas traffic interaktif secara keseluruhan](https://aistudio.google.com/rate-limit?hl=id). Batas frekuensi default
untuk inferensi Prioritas adalah **batas frekuensi standar 0,3x untuk Model / Tingkat**

### Logika downgrade yang lancar

Jika batas Prioritas terlampaui karena kemacetan, permintaan yang meluap akan
**diturunkan secara otomatis dan lancar** ke pemrosesan Standar, bukan
gagal dengan error 503 atau 429. Permintaan yang di-downgrade ditagih dengan tarif standar, bukan tarif premium Prioritas.

### Tanggung jawab klien

- **Pemantauan respons**: Developer harus memantau header `x-gemini-service-tier`
  dalam respons API untuk mendeteksi apakah permintaan sering diturunkan ke
  `standard`.
- **Percobaan ulang**: Klien harus menerapkan logika percobaan ulang/backoff eksponensial untuk
  error standar, seperti `DEADLINE_EXCEEDED`.

## Harga

Inferensi prioritas dihargai 75-100% lebih mahal daripada [API standar](https://ai.google.dev/gemini-api/docs/pricing?hl=id) dan ditagih per token.

## Model yang didukung

Model berikut mendukung Inferensi prioritas:

| Model | Inferensi prioritas |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=id) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=id) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=id) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id) | ✔️ |
| [Pratinjau Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id) | ✔️ |
| [Pratinjau Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=id) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=id) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=id) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=id) | ✔️ |

## Langkah berikutnya

- [Inferensi fleksibel](https://ai.google.dev/gemini-api/docs/flex-inference?hl=id) untuk pengurangan biaya.
- [Token](https://ai.google.dev/gemini-api/docs/tokens?hl=id): Pahami token.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
