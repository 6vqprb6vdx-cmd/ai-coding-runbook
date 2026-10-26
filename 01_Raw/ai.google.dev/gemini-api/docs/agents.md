---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=id
fetched_at: 2026-10-26T06:04:59.532259+00:00
title: "Ringkasan agen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Ringkasan agen

Agen terkelola di Gemini API memberi Anda platform agen
yang dapat dikonfigurasi. Satu panggilan API menyediakan sandbox Linux tempat agen melakukan penalaran,
mengeksekusi kode, mengelola file, dan menjelajahi web secara mandiri.

[rocket\_launch

Panduan memulai

Lakukan panggilan agen pertama Anda, streaming respons, dan bangun agen kustom.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=id)
[smart\_toy

Agen Antigravity

Kemampuan, alat, input multimodal, dan harga untuk agen default.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id)
[experiment

Agen di AI Studio

Playground visual untuk membuat prototipe agen tanpa menulis kode.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=id)

## Agen terkelola yang tersedia

- **[Agen Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id)**: Agen Terkelola tujuan umum yang dibuat dengan Gemini 3.8 Flash. Menjalankan kode, mengelola file, dan
  menelusuri web di dalam sandbox Linux yang aman dan dihosting oleh Google. Anda dapat
  mengonfigurasi model pokok (seperti Gemini 3.6 Flash atau Gemini 3.5
  Flash-Lite) menggunakan `agent_config`, dan memperluasnya dengan petunjuk,
  kemampuan, dan data Anda sendiri untuk
  [membuat agen kustom](https://ai.google.dev/gemini-api/docs/custom-agents?hl=id).
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=id)**: Agen riset mandiri yang merencanakan, menjalankan, dan menyintesis tugas riset multilangkah untuk kasus penggunaan seperti analisis pasar, uji tuntas, dan tinjauan literatur.

## Keamanan dan praktik terbaik

Setiap agen berjalan di lingkungan sandbox yang terisolasi di tingkat OS.
Sandbox memiliki akses jaringan keluar tanpa batas secara default. Anda dapat
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
dari sumber tepercaya dan batasi izin ke minimum yang diperlukan. Simpan
secret sebagai kredensial terkelola dan rujuk berdasarkan ID, sehingga proxy keluar
memasukkannya pada waktu permintaan dan tidak pernah terekspos di dalam sandbox. Agen
dapat menggunakan kredensial apa pun yang aksesnya telah diberikan, jadi hanya berikan kredensial yang cakupan
penuhnya bersedia Anda berikan.

- Gunakan akun layanan atau kunci API dengan hak istimewa terendah.
- Lebih memilih token berumur pendek daripada kunci berumur panjang.
- Hanya berikan kredensial yang cakupan penuhnya bersedia Anda berikan.
- Merotasi kredensial sesuai jadwal rutin.

Untuk mengetahui jenis kredensial dan operasi pengelolaan, lihat bagian
[Kredensial](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=id). Anda juga dapat menetapkan header
secara inline pada aturan daftar yang diizinkan, lihat [Konfigurasi
jaringan](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id#network-configuration).

### Pengawasan manusia

Selalu verifikasi output (kode yang dihasilkan, transformasi data, perubahan konfigurasi) sebelum men-deploy-nya, terutama untuk tugas yang mengubah data atau berinteraksi dengan sistem eksternal.

## Harga

Agen terkelola menggunakan [model bayar sesuai penggunaan](https://ai.google.dev/gemini-api/docs/pricing?hl=id#pricing-for-agents)
berdasarkan token model Gemini dan penggunaan alat. Satu interaksi dapat memicu beberapa reasoning loop, yang biasanya menggunakan 100 ribu hingga 3 juta token. Komputasi
lingkungan **tidak ditagih** selama pratinjau. Lihat [perkiraan biaya](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id#availability-and-pricing)
untuk perincian per tugas. Agen terkelola juga tersedia di paket gratis dengan batas frekuensi dan kuota penggunaan gratis.

## Batas

| Batas | Deskripsi |
| --- | --- |
| **Masa Aktif Lingkungan** | Lingkungan akan dihapus secara permanen setelah 7 hari tidak aktif. |
| **Penonaktifan VM** | VM dimatikan setelah tidak aktif selama beberapa saat untuk menghemat resource. Permintaan berikutnya memulihkan status (dengan cold start). |
| **Software yang Sudah Diinstal Sebelumnya** | Lingkungan berbasis Ubuntu dengan Python 3.12 dan Node.js 22. Untuk mengetahui informasi selengkapnya tentang image dasar lingkungan, lihat [Software yang telah diinstal sebelumnya](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id#pre-installed-software). |
| **Agen maksimum** | Anda dapat memiliki hingga 1.000 agen terkelola. |

## Framework agen

Anda juga dapat membuat agen dengan Gemini menggunakan framework dan SDK berikut:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=id): Bangun alur aplikasi yang kompleks dan memiliki status, serta sistem multi-agen menggunakan struktur grafik.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=id): Hubungkan agen Gemini ke
  data pribadi Anda untuk alur kerja yang ditingkatkan RAG.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=id): Mengorkestrasi agen AI otonom yang kolaboratif dan memainkan peran.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=id): Buat
  antarmuka pengguna dan agen yang didukung AI di JavaScript/TypeScript.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): Framework
  open source untuk membangun dan mengatur agen AI yang dapat beroperasi.
- [**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=id): Bangun agen AI otonom menggunakan alat, loop agen, dan pengelolaan konteks yang sama dengan yang mendukung Google Antigravity, yang dapat diprogram di Python.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-09 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-09 UTC."],[],[]]
