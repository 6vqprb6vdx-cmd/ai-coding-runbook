---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=id
fetched_at: 2026-07-20T04:35:32.779920+00:00
title: "Versi API dijelaskan \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Referensi API](https://ai.google.dev/api?hl=id)

Kirim masukan

# Versi API dijelaskan

Dokumen ini memberikan ringkasan umum tentang perbedaan antara versi `v1`
dan `v1beta` Gemini API.

- **v1**: Versi API yang stabil. Fitur dalam versi stabil didukung sepenuhnya selama masa aktif versi utama. Jika ada perubahan yang dapat menyebabkan gangguan, versi utama API berikutnya akan dibuat dan versi yang ada akan tidak digunakan lagi setelah jangka waktu yang wajar.
  Perubahan yang tidak menyebabkan gangguan dapat diperkenalkan ke API tanpa mengubah versi utama. Mulai Juni 2026, **Interactions API** tersedia secara Umum dan didukung di `v1`.
- **v1beta**: Versi ini mencakup fitur dan kemampuan awal yang sedang dikembangkan secara
  aktif. Meskipun fitur di `v1beta` dapat berubah saat kami menyempurnakannya berdasarkan masukan, fitur ini memungkinkan Anda mencoba kemampuan baru sebelum dipromosikan ke versi stabil.

| Fitur | v1 | v1beta |
| --- | --- | --- |
| Interactions API |  |  |
| Membuat Konten - Input khusus teks |  |  |
| Membuat Konten - Input teks dan gambar |  |  |
| Membuat Konten - Output teks |  |  |
| Membuat Konten - Percakapan multi-giliran (chat) |  |  |
| Membuat Konten - Panggilan fungsi |  |  |
| Membuat Konten - Streaming |  |  |
| Menyematkan Konten - Input khusus teks |  |  |
| Membuat Jawaban |  |  |
| Pengambil semantik |  |  |

- - Didukung
- - Tidak akan pernah didukung

## Mengonfigurasi versi API di SDK

Gemini API SDK secara default menggunakan `v1beta`, tetapi Anda dapat menentukan versi secara eksplisit dengan menetapkan versi API seperti yang ditunjukkan dalam contoh kode berikut:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.5-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works"
  }'
```

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-22 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-22 UTC."],[],[]]
