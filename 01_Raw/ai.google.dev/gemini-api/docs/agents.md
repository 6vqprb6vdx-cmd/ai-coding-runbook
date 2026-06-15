---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=id
fetched_at: 2026-06-15T06:20:15.781490+00:00
title: "Ringkasan Agen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Ringkasan Agen

Agen terkelola di Gemini API memberi Anda platform agen yang dapat dikonfigurasi. Satu panggilan API menyediakan sandbox Linux tempat agen menganalisis, mengeksekusi kode, mengelola file, dan menjelajahi web secara mandiri.

[rocket\_launch

Panduan memulai

Lakukan panggilan agen pertama Anda, streaming respons, dan bangun agen kustom.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=id)
[smart\_toy

Agen Antigravitasi

Kemampuan, alat, input multimodal, dan harga untuk agen default.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id)
[experiment

Agen di AI Studio

Playground visual untuk membuat prototipe agen tanpa menulis kode.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=id)

## Agen terkelola yang tersedia

- **[Agen antigravitasi](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id)**: Agen serbaguna yang dikelola dan didukung oleh Gemini 3.5 Flash. Menjalankan kode, mengelola file, dan menelusuri web di dalam sandbox Linux yang aman dan dihosting oleh Google. Anda dapat memperluasnya dengan petunjuk, keterampilan, dan data Anda sendiri untuk [membangun agen kustom](https://ai.google.dev/gemini-api/docs/custom-agents?hl=id).
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=id)**: Agen riset mandiri
  yang merencanakan, menjalankan, dan menyintesis tugas riset multi-langkah untuk kasus penggunaan
  seperti analisis pasar, uji tuntas, dan tinjauan literatur.

## Keamanan dan praktik terbaik

Setiap agen berjalan di lingkungan sandbox yang diisolasi di tingkat OS.
Sandbox memiliki akses jaringan keluar yang tidak dibatasi secara default. Anda dapat
membatasi atau menonaktifkan akses jaringan menggunakan daftar yang diizinkan.

### Akses jaringan

Secara default, lingkungan memiliki akses jaringan keluar yang tidak dibatasi. Gunakan daftar yang diizinkan
`network` untuk membatasi traffic keluar ke domain tertentu atau
pola wildcard. Untuk mengetahui detail konfigurasi, lihat
[Daftar yang Diizinkan Jaringan](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=id#network_allow_list) (AI
Studio) atau [Aturan jaringan](https://ai.google.dev/gemini-api/docs/custom-agents?hl=id#with_network_rules)
(API).

### Alat dan API eksternal

Anda dapat menghubungkan alat dan API eksternal untuk memperluas agen. Hanya gunakan alat
dari sumber tepercaya dan cakupan izin ke minimum yang diperlukan. Kredensial
dapat disuntikkan secara aman melalui transformasi header proxy keluar dan tidak pernah
diekspos di dalam sandbox. Agen dapat menggunakan kredensial apa pun yang dapat diaksesnya,
jadi hanya berikan kredensial yang cakupan penuhnya bersedia Anda berikan.

- Gunakan akun layanan atau kunci API dengan hak istimewa terendah.
- Lebih memilih token jangka pendek daripada kunci jangka panjang.
- Hanya berikan kredensial yang cakupan penuhnya bersedia Anda berikan.
- Merotasi kredensial sesuai jadwal rutin.

Untuk mengetahui detail tentang cara mengonfigurasi transformasi header, lihat
[Kredensial](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id#credentials).

### Pengawasan manusia

Selalu verifikasi output (kode yang dihasilkan, transformasi data, perubahan konfigurasi) sebelum men-deploy-nya, terutama untuk tugas yang mengubah data atau berinteraksi dengan sistem eksternal.

## Harga

Agen terkelola menggunakan [model bayar sesuai penggunaan](https://ai.google.dev/gemini-api/docs/pricing?hl=id#pricing-for-agents) berdasarkan token model Gemini dan penggunaan alat. Satu interaksi dapat memicu beberapa loop penalaran, biasanya menggunakan 100 ribu hingga 3 juta token. Komputasi lingkungan **tidak ditagih** selama pratinjau. Lihat [perkiraan biaya](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id#availability-and-pricing) untuk perincian per tugas.

## Batas

| Batas | Deskripsi |
| --- | --- |
| **Masa Aktif Lingkungan** | Lingkungan akan dihapus secara permanen setelah 7 hari tidak aktif. |
| **Penonaktifan VM** | VM dimatikan setelah tidak ada aktivitas selama beberapa saat untuk menghemat resource. Permintaan berikutnya akan memulihkan status (dengan cold start). |
| **Software yang Sudah Diinstal Sebelumnya** | Lingkungan berbasis Ubuntu dengan Python 3.12 dan Node.js 22. Untuk mengetahui informasi selengkapnya tentang image dasar lingkungan, lihat [Software yang telah diinstal sebelumnya](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id#pre-installed-software). |
| **Agen maksimum** | Anda dapat memiliki hingga 1.000 agen terkelola. |

## Framework agen

Anda juga dapat membuat agen dengan Gemini menggunakan framework dan SDK berikut:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=id): Bangun alur aplikasi yang kompleks dan memiliki status, serta sistem multi-agen menggunakan struktur grafik.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=id): Hubungkan agen Gemini ke data pribadi Anda untuk alur kerja yang ditingkatkan RAG.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=id): Mengatur agen AI otonom yang kolaboratif dan memainkan peran.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=id): Buat
  antarmuka pengguna dan agen yang didukung AI di JavaScript/TypeScript.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): Framework
  open source untuk membangun dan mengatur agen AI yang dapat beroperasi.
- [**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=id): Bangun agen AI otonom menggunakan alat, loop agen, dan pengelolaan konteks yang sama dengan yang mendukung Google Antigravity, yang dapat diprogram di Python.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-20 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-20 UTC."],[],[]]
