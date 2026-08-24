---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=id
fetched_at: 2026-08-24T02:25:16.520911+00:00
title: "Pembuatan video di Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Pembuatan video di Gemini API

Gemini API menawarkan dua model untuk membuat video,
[Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=id) dan [Veo](https://ai.google.dev/gemini-api/docs/veo?hl=id).
Setiap model dirancang untuk alur kerja yang berbeda.

Gunakan Gemini Omni Flash sebagai model default untuk pembuatan video. Model ini memberikan koherensi video yang unggul, penalaran multi-input (mendukung input teks, gambar, audio, dan video secara bersamaan), konsistensi karakter, akurasi faktual, dan pengeditan via percakapan multi-giliran (misalnya, penggantian elemen atau perubahan perspektif). Gunakan Veo 3.1 jika kemampuan tertentu seperti ekstensi adegan, kontrol frame terakhir, atau integrasi dengan pipeline lama diperlukan.

## Gemini Omni Flash

Gemini Omni Flash adalah model multimodal yang cepat untuk pembuatan video dan pengeditan video percakapan. Model ini unggul dalam mengubah perintah teks dan gambar menjadi video pendek dengan cepat, dan memungkinkan Anda menyempurnakan hasil di beberapa giliran menggunakan Interactions API.

[Mulai menggunakan Gemini Omni Flash →](https://ai.google.dev/gemini-api/docs/omni?hl=id)

## Veo 3.1

Veo 3.1 adalah model untuk membuat video dengan audio asli. Model ini mendukung fitur seperti ekstensi video, pembuatan khusus frame, dan arah berbasis gambar melalui `generateContent` API.

[Mulai menggunakan Veo 3.1 →](https://ai.google.dev/gemini-api/docs/veo?hl=id)

## Pemahaman video

Jika Anda perlu menyerap dan menganalisis konten video yang ada, bukan membuat
video baru, lihat [panduan Pemahaman video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-30 UTC."],[],[]]
