---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=id
fetched_at: 2026-06-08T14:58:47.029852+00:00
title: "Membangun Aplikasi Android di Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Membangun Aplikasi Android di Google AI Studio

Google AI Studio memungkinkan Anda membuat aplikasi Android native dari perintah bahasa alami. Deskripsikan aplikasi yang Anda inginkan, dan
[Antigravity Agent](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=id#antigravity-agent)
akan membuat project Kotlin dan [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=id)
yang lengkap. Dari browser, Anda dapat melihat pratinjau aplikasi di emulator Android berbasis browser, menginstalnya di perangkat fisik, dan memublikasikannya untuk pengujian.

## Mulai

Untuk mulai membuat aplikasi Android:

1. Buka [mode Build](https://aistudio.google.com/apps?hl=id) di Google AI Studio menggunakan panel navigasi kiri.
2. Pilih **Android** dari pemilih platform.
3. Masukkan perintah yang menjelaskan aplikasi yang ingin Anda buat (misalnya, *"Buat pelacak tugas harian dengan penyimpanan lokal"* atau *"Buat kalkulator sederhana"*).
4. Agen akan membuat project dan meluncurkannya di emulator Android berbasis browser.

Kemudian, Anda dapat melakukan iterasi pada aplikasi menggunakan panel chat, seperti pengalaman web. Agen mengelola semua file di project Android Anda dan menyebarkan perubahan di seluruh codebase.

## Emulator Android berbasis browser

Emulator Android berjalan sepenuhnya di cloud dan di-streaming ke browser Anda.
Anda tidak perlu menginstal Android SDK, Android Studio, atau emulator lokal.

Emulator menyediakan:

- **Simulasi perangkat seperti Pixel**: ketuk, scroll, dan berinteraksi dengan aplikasi Anda
  seperti di perangkat sungguhan.
- **Dukungan rotasi**: beralih antara orientasi potret dan lanskap.
- **Pratinjau langsung**: saat agen membuat perubahan kode, aplikasi akan di-build ulang dan
  emulator akan dimuat ulang secara otomatis.

### Batasan emulator

Emulator berbasis browser tidak mendukung semua fitur hardware. Fitur berikut tidak tersedia di emulator:

- Pengambilan gambar dan foto kamera
- NFC dan Bluetooth
- GPS (lokasi disimulasikan)
- Layanan Google Play (fitur Login dengan Google, Maps, dan layanan Play lainnya berfungsi di perangkat sungguhan, tetapi tidak di emulator)

## Menginstal di perangkat dengan ADB

Anda dapat menginstal APK yang di-build langsung di perangkat Android fisik yang terhubung ke komputer menggunakan USB. Tindakan ini menggunakan
[WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=id) untuk
berkomunikasi dengan perangkat Anda melalui browser. Tidak diperlukan penginstalan ADB lokal.

### Prasyarat

- Browser Chrome atau Edge yang mendukung WebUSB.
- Perangkat Android dengan
  [Opsi Developer dan Proses Debug USB](https://developer.android.com/studio/debug/dev-options?hl=id)
  diaktifkan.
- Kabel USB yang menghubungkan perangkat ke komputer Anda.

### Menginstal aplikasi di perangkat

1. Klik **Install on Device** di panel pratinjau.
2. Pilih perangkat Android Anda dari pemilih perangkat USB browser.
3. APK akan ditransfer dan diinstal di perangkat Anda.
4. Aplikasi akan diluncurkan secara otomatis.

## Memublikasikan ke Play Store

Anda dapat memublikasikan aplikasi Android ke jalur pengujian internal
[Konsol Google Play](https://play.google.com/console?hl=id)
yang memungkinkan Anda mendistribusikan aplikasi ke maksimal 100 penguji.

### Prasyarat

- Akun Developer [Google Play](https://play.google.com/console/signup?hl=id)
  (memerlukan biaya pendaftaran satu kali sebesar $25).
- Profil developer yang telah diisi di Konsol Play.

### Memublikasikan aplikasi

1. Buka **Settings > Publish** di Google AI Studio.
2. Klik **Publish to Play Store**.
3. Lakukan autentikasi dengan akun Developer Google Play Anda.
4. AI Studio menandatangani APK, membuat listingan aplikasi (atau mengupload versi baru), dan memublikasikan ke jalur pengujian internal.
5. Anda akan menerima link untuk dibagikan kepada penguji.

AI Studio mengelola penandatanganan APK secara otomatis menggunakan keystore terkelola. Anda dapat menyesuaikan listingan aplikasi (ikon, screenshot, deskripsi) nanti di Konsol Play.

## Yang dihasilkan

Saat Anda membuat aplikasi Android, agen akan membuat project berbasis Gradle standar dengan struktur berikut:

- **Konfigurasi build**: `build.gradle.kts` file (tingkat project dan aplikasi)
  menggunakan DSL Kotlin.
- **Lapisan UI**: [komponen Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=id)
  dengan tema [Desain Material 3](https://m3.material.io/).
- **Arsitektur**: arsitektur aktivitas tunggal dengan ViewModel dan class
  data.
- **Sumber Daya**: `AndroidManifest.xml`, drawable, string, dan sumber daya Android lainnya.

Agen mengelola dependensi Gradle secara otomatis, menambahkan paket dari repositori Maven dan Google sesuai kebutuhan.

Anda dapat melihat dan mengedit kode yang dihasilkan menggunakan tab **Code** di panel pratinjau. Untuk melanjutkan pengembangan di Android Studio, download project sebagai **file ZIP**.

## Batasan

Pembuatan aplikasi Android di AI Studio memiliki batasan berikut:

### Batasan platform

- **Hanya sisi klien**: Aplikasi Android tidak menyertakan komponen sisi server.
  Fitur yang memerlukan runtime server (pengelolaan rahasia, multiplayer, Firebase, Google Workspace API) tidak tersedia.
- **Arsitektur aktivitas tunggal**: hanya project aktivitas tunggal dan modul tunggal
  yang didukung.
- **Hanya Jetpack Compose**: aplikasi menggunakan Kotlin dan Jetpack Compose. Tata letak Java dan XML tidak didukung.
- **Tidak ada NDK atau kode native**: kode C dan C++ tidak didukung.
- **Tidak ada Wear OS atau Android TV**: hanya faktor bentuk ponsel dan tablet yang di
  dukung.

### Batasan ekspor

- **Hanya download ZIP**: Anda dapat mendownload project sebagai file ZIP. Ekspor GitHub belum tersedia untuk project Android.

## Langkah berikutnya

- [Membuat aplikasi di Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=id)
- [Mengembangkan Aplikasi Full-Stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=id) (web)
- Lihat contoh di [Galeri Aplikasi](https://aistudio.google.com/apps?source=showcase&hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-19 UTC."],[],[]]
