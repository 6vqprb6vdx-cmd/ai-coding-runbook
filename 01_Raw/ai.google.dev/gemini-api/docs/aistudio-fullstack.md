---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=id
fetched_at: 2026-07-20T04:33:16.726512+00:00
title: "Mengembangkan Aplikasi Full-Stack di Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Mengembangkan Aplikasi Full-Stack di Google AI Studio

Google AI Studio kini mendukung pengembangan full-stack, sehingga Anda dapat membuat aplikasi yang melampaui prototipe sisi klien. Dengan runtime sisi server, Anda dapat mengelola secret, terhubung ke API eksternal, dan membangun pengalaman multiplayer real-time.

## Runtime sisi server

Aplikasi Google AI Studio kini dapat menyertakan komponen sisi server (Node.js).
Hal ini memungkinkan Anda:

- **Menjalankan logika sisi server**: Menjalankan kode yang tidak boleh diekspos ke
  klien.
- **Mengakses paket npm**: [Agen Antigravity](https://antigravity.google/docs/agent?hl=id)
  dapat menginstal dan menggunakan paket dari ekosistem npm yang luas.
- **Menangani secret**: Menggunakan kunci API dan kredensial dengan aman.

### Menggunakan paket npm

Anda tidak perlu menjalankan `npm install` secara manual. Cukup minta Agen untuk menambahkan fungsi yang memerlukan paket, dan Agen akan menangani penginstalan dan impor.

**Contoh**: > "Gunakan `axios` untuk mengambil data dari API eksternal."

## Mengelola secret dengan aman

Dengan kode sisi server dan pengelolaan secret, kini Anda dapat membuat aplikasi yang berinteraksi dengan dunia.

### Kunci Gemini API

Saat Anda membuat aplikasi baru yang menggunakan Gemini API, AI Studio akan otomatis mengonfigurasi `GEMINI_API_KEY` Anda sebagai secret sisi server — tidak diperlukan penyiapan manual. Anda dapat melihat kunci ini di panel **Secrets** di Setelan. Panggilan Gemini API aplikasi Anda dibuat dari kode sisi server menggunakan kunci ini, sehingga tidak pernah diekspos di browser.

### Kunci API pihak ketiga

Untuk layanan lain, Anda dapat menambahkan kunci API secara manual:

- **API pihak ketiga**: Terhubung ke layanan seperti Stripe, SendGrid, atau REST API kustom.
- **Database**: Terhubung ke database eksternal (misalnya, melalui Supabase, Firebase,
  atau MongoDB Atlas) untuk mempertahankan data di luar sesi.

Saat membuat aplikasi dunia nyata, Anda sering kali perlu terhubung ke layanan pihak ketiga (seperti Twilio, Slack, atau database) yang memerlukan kunci API. Anda dapat menambahkan kunci secara manual dengan langkah-langkah berikut:

1. **Menambahkan secret**: Buka menu **Settings** di Google AI Studio dan cari
   bagian Secrets.
2. **Menyimpan kunci**: Tambahkan kunci API atau token secret Anda di sini.
3. **Mengakses dalam kode**: Agen dapat menulis kode sisi server yang mengakses
   secret ini dengan aman (biasanya via variabel lingkungan), memastikan
   secret tidak pernah diekspos ke browser sisi klien.

Jika diperlukan, agen juga akan menampilkan kartu di chat yang meminta Anda untuk menambahkan kunci setiap kali secret baru diperlukan atau saat kunci baru terdeteksi di variabel env project.

### Integrasi Firebase untuk database &autentikasi

Google AI Studio kini memudahkan penambahan database atau autentikasi ke
aplikasi Anda melalui
[integrasi Firebase](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=id).
Agen Antigravity dapat menyediakan dan menyiapkan layanan berikut secara otomatis untuk Anda:

- **Database Firestore**: database cloud NoSQL yang fleksibel dan skalabel untuk menyimpan
  dan menyinkronkan data untuk pengembangan sisi klien dan sisi server.
- **Firebase Authentication**: memungkinkan pengguna Anda login ke
  aplikasi Anda dengan aman menggunakan alur "Login dengan Google".

Cukup minta agen untuk "menambahkan database ke aplikasi saya" atau "menyiapkan Login dengan Google", dan agen akan menangani konfigurasi dan pembuatan kode yang diperlukan untuk Anda.

Firebase memungkinkan Anda memulai secara gratis, dan secara opsional melakukan penskalaan dengan akun berbayar kapan saja Anda siap untuk kuota yang lebih besar atau menggunakan fitur berbayar.

## Google Workspace API

Google AI Studio memungkinkan Anda membuat aplikasi yang terhubung ke Google Workspace API, sehingga pengguna dapat menggunakan data mereka yang sebenarnya: email, spreadsheet, dokumen, acara kalender, dan lainnya, semuanya dalam aplikasi Anda. Anda tidak perlu lagi menyiapkan project Google Cloud, mengonfigurasi OAuth, atau mengelola API secara manual.

### Cara kerjanya

Anda dapat menambahkan integrasi Workspace dengan dua cara:

- **Jelaskan di panel chat**: Cukup beri tahu agen apa yang Anda inginkan di panel chat di bagian bawah. Misalnya, *"Buat pelacak pengeluaran yang mencatat tanda terima ke Google Spreadsheet saya"* atau *"Buat dasbor yang meringkas pesan Gmail saya yang belum dibaca."*
- **Pilih dari panel integrasi**: Buka panel **Integrations** di sidebar kanan mode Build dan aktifkan aplikasi Workspace yang ingin Anda hubungkan.

Saat Anda menambahkan aplikasi Workspace, AI Studio akan otomatis:

1. Menghubungkan Google API yang diperlukan untuk aplikasi Anda.
2. Membuat kode sisi server untuk memanggil API.
3. Menambahkan alur "Login dengan Google" yang aman sehingga pengguna akhir aplikasi Anda dapat mengotorisasi akses ke data mereka sendiri.

### Aplikasi yang didukung

Aplikasi Google Workspace berikut tersedia:

| Aplikasi | Yang dapat Anda buat |
| --- | --- |
| Google Kalender | Membaca, membuat, dan mengelola acara dan kalender |
| Google Chat | Membaca dan berinteraksi dengan percakapan dan ruang grup |
| Google Dokumen | Membuat, membaca, memperbarui, dan memformat dokumen |
| Google Drive | Mengatur, menelusuri, dan mengelola file dan folder |
| Google Formulir | Membuat survei, memperbarui pertanyaan, dan mengambil respons |
| Gmail | Membaca, mengirim, dan mengelola konten email |
| Google Keep | Mengelola catatan, daftar, dan lampiran |
| Google Meet | Menjadwalkan dan mengelola panggilan video |
| Kontak | Menyinkronkan dan mengelola kontak |
| Google Spreadsheet | Membaca, menulis, dan memformat data spreadsheet |
| Google Slide | Membuat dan mengubah presentasi |
| Google Tasks | Membuat, mengelola, dan mengatur tugas |

### Autentikasi dan izin

Sebagai pembuat, Anda tidak perlu mengonfigurasi klien OAuth, mengelola kredensial, atau menyiapkan project Google Cloud. AI Studio akan menangani semuanya untuk Anda.

Aplikasi dengan Workspace API terintegrasi menggunakan "Login dengan Google" untuk mengautentikasi pengguna akhir. Saat pengguna membuka aplikasi Anda, mereka akan diminta untuk login dan memberikan izin tertentu yang diperlukan aplikasi Anda (misalnya, akses hanya baca ke kalender mereka, atau kemampuan untuk mengedit spreadsheet). Aplikasi Anda hanya mengakses data orang yang menggunakannya. Setiap pengguna mengotorisasi akses ke akun mereka sendiri.

### Contoh perintah

Berikut beberapa ide untuk memulai integrasi Workspace:

- *"Buat aplikasi yang membaca Google Kalender saya dan membuat draf email persiapan di
  Gmail untuk setiap rapat."*
- *"Buat alat yang mengambil Google Dokumen dan membuat ringkasan 5 slide
  presentasi di Google Slide."*
- *"Buat pelacak pengeluaran tempat saya mengupload tanda terima, Gemini mengekstrak
  detailnya, dan mencatat baris baru di Google Spreadsheet saya."*

### Menyiapkan OAuth

Salah satu kasus penggunaan utama untuk pengelolaan secret adalah menyiapkan OAuth untuk terhubung ke situs atau aplikasi lain. Jika perintah Anda menyertakan petunjuk tentang cara menghubungkan ke aplikasi pihak ketiga yang memerlukan autentikasi OAuth, agen akan memberikan petunjuk tentang cara menyiapkan OAuth untuk aplikasi tersebut. Petunjuk ini akan menyertakan URL callback yang diperlukan untuk mengonfigurasi Aplikasi OAuth Anda.
Anda juga dapat menemukan URL callback di bagian **Integrations** di panel Settings.

## Membangun pengalaman multiplayer

Runtime full-stack memungkinkan fitur kolaborasi real-time.

- **Status real-time**: Anda dapat meminta Agen untuk membuat fitur seperti "live
  chat", "papan tulis kolaboratif", atau "game multiplayer".
- **Sesi yang disinkronkan**: Server mengelola status, sehingga beberapa pengguna
  dapat berinteraksi dengan instance aplikasi yang sama secara real-time.

**Contoh perintah**: > "Jadikan ini game multiplayer tempat pemain dapat melihat kursor satu sama
lain."

### Tips untuk menguji aplikasi multiplayer

Anda dapat menguji mode multiplayer dengan dua cara sebelum men-deploy aplikasi.

1. Buka aplikasi Anda dalam mode Build Google AI Studio di beberapa tab. Saat mengembangkan dalam mode Build, aplikasi Anda berada dalam container pengembangan. Membuka aplikasi di beberapa tab akan memungkinkan Anda mensimulasikan beberapa pemain yang menggunakan aplikasi Anda.
2. Bagikan aplikasi kepada orang lain menggunakan menu **Share** di kanan atas. Kemudian, gunakan **Shared URL** dari tab **Integrations** di menu **Share** untuk menggunakan aplikasi dengan pemain yang telah Anda bagikan aplikasi Anda.

## Praktik terbaik

- **Panggilan Gemini API**: `GEMINI_API_KEY` Anda otomatis dikonfigurasi sebagai
  secret sisi server. Lakukan panggilan Gemini API dari kode sisi server Anda menggunakan kunci ini. Anda dapat melihatnya di panel **Secrets**.
- **Keamanan secret**: Selalu gunakan pengelola Secret untuk kunci sensitif.
  Jangan pernah meng-hardcode-nya dalam file Anda.
- **Pemisahan tanggung jawab**: Simpan logika UI Anda di framework sisi klien
  (React/Angular) dan penanganan data/logika bisnis Anda di sisi server.
- **Penanganan error**: Pastikan kode sisi server Anda menangani error
  dari panggilan API eksternal dengan kuat untuk mencegah aplikasi mengalami error.

## Apa Langkah Selanjutnya?

- [Membuat Aplikasi di Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=id)
- [Men-deploy dari Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=id)
- [Galeri Aplikasi](https://aistudio.google.com/apps?source=showcase&hl=id)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-19 UTC."],[],[]]
