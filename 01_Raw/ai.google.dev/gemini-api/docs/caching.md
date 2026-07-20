---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=id
fetched_at: 2026-07-20T04:43:13.207885+00:00
title: "Context caching \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Context caching

Dalam alur kerja AI biasa, Anda mungkin meneruskan token input yang sama berulang kali ke model. Gemini API menawarkan penyimpanan cache implisit untuk mengoptimalkan performa dan biaya.

## Caching implisit

Penyimpanan cache implisit diaktifkan secara default untuk semua model Gemini 2.5 dan yang lebih baru. Fitur ini didukung untuk mode percakapan [stateful](https://ai.google.dev/gemini-api/docs/text-generation?hl=id#multi-turn-conversations) (menggunakan `previous_interaction_id`) dan [stateless](https://ai.google.dev/gemini-api/docs/text-generation?hl=id#stateless-conversations).
Kami secara otomatis meneruskan penghematan biaya jika permintaan Anda mencapai cache. Anda tidak perlu melakukan tindakan apa pun untuk mengaktifkannya. Jumlah token input
minimum untuk penyiapan cache konteks tercantum dalam tabel berikut untuk setiap model:

| Model | Batas token minimum |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Pratinjau Gemini 3.1 Pro | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

Untuk meningkatkan peluang terjadinya cache hit implisit:

- Coba letakkan konten besar dan umum di awal perintah Anda
- Mencoba mengirim permintaan dengan awalan yang serupa dalam waktu singkat

Anda dapat melihat jumlah token yang merupakan hit cache di kolom
`usage.total_cached_tokens` (Python dan JavaScript) objek respons.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-07 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-07 UTC."],[],[]]
