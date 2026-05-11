---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=id
fetched_at: 2026-05-11T12:40:47.550583+00:00
title: "Menggunakan Alat dengan Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Menggunakan Alat dengan Gemini API

Alat memperluas kemampuan model Gemini, sehingga memungkinkan model mengambil tindakan di dunia, mengakses informasi real-time, dan melakukan tugas komputasi yang kompleks. Model dapat menggunakan alat dalam interaksi respons permintaan standar dan
sesi streaming real-time menggunakan [Live API](https://ai.google.dev/gemini-api/docs/live-tools?hl=id).

Alat adalah kemampuan tertentu (seperti Google Penelusuran atau Eksekusi Kode) yang dapat digunakan model untuk menjawab kueri. Gemini API menyediakan rangkaian alat bawaan yang dikelola sepenuhnya
, atau Anda dapat menentukan alat kustom menggunakan [Panggilan
Fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id).

Untuk membuat sistem multi-langkah yang berorientasi pada tujuan, lihat [Ringkasan
Agen](https://ai.google.dev/gemini-api/docs/agents?hl=id).

## Alat bawaan yang tersedia

| Alat | Deskripsi | Kasus Penggunaan |
| --- | --- | --- |
| [Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id) | Mendasarkan respons pada peristiwa dan fakta terkini dari web untuk mengurangi halusinasi. | \- Menjawab pertanyaan tentang peristiwa terbaru   \- Memverifikasi fakta dengan berbagai sumber |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id) | Membuat asisten yang mengetahui lokasi dan dapat menemukan tempat, mendapatkan rute, serta memberikan konteks lokal yang lengkap. | \- Merencanakan itinerari perjalanan dengan beberapa perhentian   \- Menemukan bisnis lokal berdasarkan kriteria pengguna |
| [Eksekusi Kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id) | Memungkinkan model menulis dan menjalankan kode Python untuk menyelesaikan masalah matematika atau memproses data secara akurat. | \- Menyelesaikan persamaan matematika yang kompleks   \- Memproses dan menganalisis data teks secara akurat |
| [Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id) | Mengarahkan model untuk membaca dan menganalisis konten dari halaman web atau dokumen tertentu. | \- Menjawab pertanyaan berdasarkan URL atau dokumen tertentu   \- Mengambil informasi di berbagai halaman web |
| [Penggunaan Komputer (Pratinjau)](https://ai.google.dev/gemini-api/docs/computer-use?hl=id) | Memungkinkan Gemini melihat layar dan membuat tindakan untuk berinteraksi dengan UI browser web (Eksekusi sisi klien). | \- Mengotomatiskan alur kerja berbasis web yang berulang   \- Menguji antarmuka pengguna aplikasi web |
| [Penelusuran File](https://ai.google.dev/gemini-api/docs/file-search?hl=id) | Mengindeks dan menelusuri dokumen Anda sendiri untuk mengaktifkan Retrieval Augmented Generation (RAG). | \- Menelusuri panduan teknis   \- Menjawab pertanyaan tentang data eksklusif |

Lihat halaman [Harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id#pricing_for_tools) untuk mengetahui detail
biaya yang terkait dengan alat tertentu.

## Cara kerja eksekusi alat

Alat memungkinkan model meminta tindakan selama percakapan. Alurnya berbeda bergantung pada apakah alat tersebut bawaan (dikelola oleh Google) atau kustom (dikelola oleh Anda).

### Alur alat bawaan

Untuk alat bawaan (Google Penelusuran, Google Maps, Konteks URL, Penelusuran File, Eksekusi Kode), seluruh proses terjadi dalam satu panggilan API:

1. **Anda** mengirim perintah: "Berapa akar kuadrat dari harga saham GOOG terbaru?"
2. **Gemini** memutuskan bahwa model memerlukan alat dan menjalankannya di server Google (misalnya, menelusuri harga saham, lalu menjalankan kode Python untuk menghitung akar kuadrat).
3. **Gemini** mengirim kembali jawaban akhir yang didasarkan pada hasil alat.

### Alur alat kustom (Panggilan fungsi)

Untuk alat kustom dan Penggunaan Komputer, aplikasi Anda menangani eksekusi:

1. **Anda** mengirim perintah beserta deklarasi fungsi (alat).
2. **Gemini** dapat mengirim kembali JSON terstruktur untuk memanggil fungsi tertentu
   (misalnya, `{"name": "get_order_status", "args": {"order_id": "123"}}`),
   selalu dengan `id` unik.
3. **Anda** menjalankan fungsi di aplikasi atau lingkungan Anda.
4. **Anda** mengirim hasil fungsi, dengan `id` yang sama dengan panggilan fungsi, kembali ke Gemini.
5. **Gemini** menggunakan hasil untuk membuat respons akhir atau panggilan alat lainnya.

Pelajari lebih lanjut dalam panduan [Panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id).

### Menggabungkan alur alat bawaan dan alat kustom

[Untuk permintaan yang menggabungkan alat bawaan dan alat kustom (panggilan fungsi), model menggunakan sirkulasi konteks alat untuk mengoordinasikan eksekusi di berbagai lingkungan:](https://ai.google.dev/gemini-api/docs/toold-combination?hl=id)

1. **Anda** mengirim perintah dan mendeklarasikan alat bawaan dan fungsi kustom yang ingin diaktifkan, dengan menetapkan flag untuk mengaktifkan dukungan kombinasi.
2. **Gemini** menjalankan alat bawaan dan memberikan hasil kepada pengguna jika ada panggilan fungsi sisi klien yang dibuat (yang dijalankan terlebih dahulu bergantung pada perintah dan keputusan model). Model akan mengirim kembali respons dengan:
   - Konfirmasi panggilan alat
   - Hasil respons alat (ini mungkin muncul setelah JSON jika model membuat dua panggilan fungsi paralel)
   - JSON terstruktur untuk memanggil fungsi Anda
   - Tanda tangan pemikiran terenkripsi untuk mempertahankan konteks
3. **Anda** menjalankan fungsi di aplikasi atau lingkungan Anda.
4. **Anda** menampilkan semua bagian respons Gemini, ditambah hasil panggilan fungsi Anda.
5. **Gemini** membuat respons akhir menggunakan semua konteks gabungan.

Baca [panduan Kombinasi alat](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id) untuk mempelajari
cara mengaktifkan dukungan untuk kombinasi alat bawaan dan alat kustom serta contoh
sirkulasi konteks.

## Output terstruktur vs. panggilan fungsi

Gemini menawarkan dua metode untuk membuat output terstruktur. Gunakan [Panggilan
fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id) jika model perlu melakukan
langkah perantara dengan menghubungkan ke alat atau sistem data Anda sendiri. Gunakan
[Output Terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id) jika Anda benar-benar memerlukan
respons akhir model untuk mematuhi skema tertentu, seperti untuk merender
UI kustom.

## Output terstruktur dengan alat

Anda dapat menggabungkan [Output Terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id) dengan
alat bawaan untuk memastikan bahwa respons model yang didasarkan pada data atau
komputasi eksternal tetap mematuhi skema yang ketat.

Lihat [Output terstruktur dengan alat](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=id#structured_outputs_with_tools)
untuk contoh kode.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-29 UTC."],[],[]]
