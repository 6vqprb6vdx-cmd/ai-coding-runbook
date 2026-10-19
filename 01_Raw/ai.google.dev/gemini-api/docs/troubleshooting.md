---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=id
fetched_at: 2026-10-19T05:33:34.645623+00:00
title: "Panduan pemecahan masalah \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Panduan pemecahan masalah

Gunakan panduan ini untuk membantu Anda mendiagnosis dan menyelesaikan masalah umum yang muncul saat
Anda memanggil Gemini API. Anda mungkin mengalami masalah dari
layanan backend Gemini API atau SDK klien. SDK klien kami
bersifat open source di repositori berikut:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

Jika Anda mengalami masalah kunci API, pastikan Anda telah menyiapkan
kunci API dengan benar sesuai [panduan penyiapan kunci API](https://ai.google.dev/gemini-api/docs/api-key?hl=id).

## Kode error

Untuk mengetahui referensi lengkap semua kode error, termasuk kode status HTTP, kode pemblokiran pembuatan, dan kode error konten, lihat halaman [Error API](https://ai.google.dev/gemini-api/docs/api-errors?hl=id).

## Strategi percobaan ulang

Jika Anda menerima error yang menunjukkan bahwa Anda harus mencoba lagi permintaan (seperti `429 RESOURCE_EXHAUSTED` atau `503 UNAVAILABLE`), sebaiknya terapkan strategi backoff eksponensial. Artinya, Anda menunggu sebentar sebelum percobaan ulang pertama, lalu secara bertahap meningkatkan waktu tunggu antara percobaan ulang berikutnya.

SDK klien resmi untuk Gemini API, seperti [Python SDK](https://github.com/googleapis/python-genai), menyertakan logika coba lagi otomatis dengan backoff eksponensial secara default untuk menangani error sementara seperti waktu tunggu habis, masalah jaringan, dan pembatasan kapasitas (kode status `429` dan `5xx`). Misalnya, Python SDK secara otomatis mencoba lagi error sementara hingga empat kali dengan penundaan awal sekitar 1 detik dan penundaan maksimum 60 detik.

Jika Anda membuat permintaan REST API langsung atau menyesuaikan logika percobaan ulang, ikuti praktik terbaik berikut untuk meningkatkan kemungkinan keberhasilan permintaan dan mencegah layanan kewalahan:

- **Gunakan backoff eksponensial:** Tunggu sebentar sebelum percobaan ulang pertama (misalnya, 1 detik), lalu tingkatkan penundaan secara eksponensial (misalnya, 2 dtk, 4 dtk, 8 dtk).
- **Tambahkan jitter:** Tambahkan "jitter" acak ke penundaan untuk membantu mencegah semua klien mencoba ulang pada waktu yang sama persis.
- **Coba lagi pada error tertentu:** Hanya coba lagi pada error sementara (seperti `429`, `408`, atau `5xx`). Jangan coba lagi pada error klien (seperti `400`, `402`, atau `403`) karena error tersebut menunjukkan masalah seperti kunci API yang tidak valid, kredit Prabayar yang habis, atau sintaksis yang buruk.
- **Menetapkan percobaan ulang maksimum:** Tentukan jumlah maksimum upaya percobaan ulang untuk mencegah loop tanpa henti.

## Memeriksa panggilan API Anda untuk menemukan error parameter model

Pastikan parameter model Anda berada dalam nilai berikut:

|  |  |
| --- | --- |
| **Parameter model** | **Nilai (rentang)** |
| Jumlah kandidat | 1-8 (bilangan bulat) |
| Suhu | 0,0-1,0 |
| Token output maks | Gunakan [halaman model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id) untuk menentukan jumlah maksimum token untuk model yang Anda gunakan. |
| TopP | 0.0-1.0 |

Selain memeriksa nilai parameter, pastikan Anda menggunakan
[versi API](https://ai.google.dev/gemini-api/docs/api-versions?hl=id) yang benar (misalnya, `/v1` atau `/v1beta`) dan
model yang mendukung fitur yang Anda butuhkan. Misalnya, jika fitur dalam rilis Beta, fitur tersebut hanya akan tersedia di versi API `/v1beta`.

## Memeriksa apakah Anda memiliki model yang tepat

Pastikan Anda menggunakan model yang didukung yang tercantum di [halaman model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id) kami.

## Latensi atau penggunaan token yang lebih tinggi dengan model yang berbasis penalaran

Latensi atau penggunaan token yang lebih tinggi sering terjadi karena model Gemini 3.x mengaktifkan kemampuan berpikir secara default. Model Gemini 2.5 yang tidak digunakan lagi juga menggunakan pemikiran
default.

Model yang berbasis penalaran menghasilkan token penalaran internal untuk meningkatkan kualitas. Proses
penalaran ini meningkatkan latensi respons dan total konsumsi token.

Jika Anda memprioritaskan latensi yang lebih rendah atau perlu meminimalkan biaya, Anda dapat menurunkan tingkat pemikiran atau menonaktifkan pemikiran.

Untuk mengetahui detail konfigurasi dan contoh kode, lihat
[panduan penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id#thinking-levels).

## Masalah keamanan

Jika Anda melihat perintah diblokir karena setelan keamanan dalam panggilan API Anda,
tinjau perintah tersebut sehubungan dengan filter yang Anda tetapkan dalam panggilan API.

Jika Anda melihat `BlockedReason.OTHER`, kueri atau respons mungkin melanggar [persyaratan
layanan](https://ai.google.dev/terms?hl=id) atau tidak didukung.

## Masalah pembacaan

Jika Anda melihat model berhenti menghasilkan output karena alasan RECITATION, ini
berarti output model mungkin menyerupai data tertentu. Untuk memperbaikinya, coba buat perintah / konteks seunik mungkin dan gunakan nilai Temperature yang lebih tinggi.

## Masalah token berulang

Jika Anda melihat token output yang berulang, coba saran berikut untuk membantu mengurangi atau menghilangkannya.

| Deskripsi | Penyebab | Solusi alternatif yang disarankan |
| --- | --- | --- |
| Tanda hubung berulang dalam tabel Markdown | Hal ini dapat terjadi jika konten tabel panjang karena model mencoba membuat tabel Markdown yang selaras secara visual. Namun, perataan di Markdown tidak diperlukan untuk rendering yang benar. | Tambahkan petunjuk dalam perintah Anda untuk memberikan panduan khusus kepada model dalam membuat tabel Markdown. Berikan contoh yang mengikuti panduan tersebut. Anda juga dapat mencoba menyesuaikan suhu. Untuk membuat kode atau output yang sangat terstruktur seperti tabel Markdown, suhu tinggi terbukti berfungsi lebih baik (>= 0,8).  Berikut adalah contoh kumpulan panduan yang dapat Anda tambahkan ke perintah untuk mencegah masalah ini:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Token berulang dalam tabel Markdown | Mirip dengan tanda hubung berulang, hal ini terjadi saat model mencoba menyelaraskan konten tabel secara visual. Perataan di Markdown tidak diperlukan untuk rendering yang benar. | - Coba tambahkan petunjuk seperti berikut ke perintah sistem Anda:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Coba sesuaikan suhu. Suhu yang lebih tinggi (>= 0,8)   umumnya membantu menghilangkan pengulangan atau duplikasi dalam   output. |
| Baris baru berulang (`\n`) dalam output terstruktur | Jika input model berisi urutan escape atau unicode seperti `\u` atau `\t`, hal ini dapat menyebabkan baris baru berulang. | - Periksa dan ganti urutan escape yang dilarang dengan karakter UTF-8   dalam perintah Anda. Misalnya, urutan escape `\u`   dalam contoh JSON dapat menyebabkan model menggunakannya   dalam outputnya juga. - Memberi petunjuk pada model tentang karakter escape yang diizinkan. Tambahkan petunjuk sistem seperti   ini:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Teks berulang dalam penggunaan output terstruktur | Jika output model memiliki urutan kolom yang berbeda dengan skema terstruktur yang ditentukan, hal ini dapat menyebabkan teks berulang. | - Jangan tentukan urutan kolom dalam perintah Anda. - Buat semua kolom output wajib diisi. |
| Panggilan alat berulang | Hal ini dapat terjadi jika model kehilangan konteks pemikiran sebelumnya dan/atau memanggil endpoint yang tidak tersedia yang dipaksakan. | Perintahkan model untuk mempertahankan status dalam proses pemikirannya. Tambahkan ini ke akhir petunjuk sistem Anda:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Teks berulang yang bukan bagian dari output terstruktur | Hal ini dapat terjadi jika model mengalami error saat memproses permintaan yang tidak dapat diselesaikan. | - Jika fitur berpikir diaktifkan, hindari memberikan perintah eksplisit tentang cara   memecahkan masalah dalam petunjuk. Cukup minta output akhir. - Coba suhu yang lebih tinggi >= 0,8. - Tambahkan petunjuk seperti "Singkat", "Jangan mengulangi diri sendiri", atau   "Berikan jawaban satu kali". |

## Kunci API yang diblokir atau tidak berfungsi

Bagian ini menjelaskan cara memeriksa apakah kunci API Gemini Anda diblokir
dan apa yang harus dilakukan.

### Memahami alasan kunci diblokir

Kami telah mengidentifikasi kerentanan yang menyebabkan beberapa kunci API mungkin terekspos secara publik. Untuk melindungi data Anda dan mencegah akses tidak sah, kami telah
secara proaktif memblokir kunci yang diketahui bocor ini agar tidak dapat mengakses Gemini API.

### Memastikan apakah kunci Anda terpengaruh

Jika kunci Anda diketahui bocor, Anda tidak dapat lagi menggunakan kunci tersebut dengan
Gemini API. Anda dapat menggunakan [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=id) untuk melihat apakah ada kunci API Anda yang diblokir agar tidak memanggil Gemini API dan membuat kunci baru. Anda mungkin juga melihat error berikut yang ditampilkan saat mencoba menggunakan
kunci ini:

```
Your API key was reported as leaked. Please use another API key.
```

### Tindakan untuk kunci API yang diblokir

Anda harus membuat kunci API baru untuk integrasi Gemini API menggunakan [Google
AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=id). Sebaiknya tinjau praktik pengelolaan kunci API Anda untuk memastikan kunci baru Anda tetap aman dan tidak terekspos secara publik.

### Tagihan tak terduga karena kerentanan

[Kirim kasus dukungan penagihan](https://console.cloud.google.com/support/chat?hl=id).
Tim penagihan kami sedang menanganinya, dan kami akan menyampaikan info terbaru sesegera mungkin.

### Langkah-langkah keamanan Google untuk kunci yang bocor

**Bagaimana cara Google membantu mengamankan akun saya dari kelebihan biaya dan penyalahgunaan jika kunci API saya bocor?**

- Kami akan beralih ke penerbitan kunci API saat Anda meminta kunci baru menggunakan
  [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=id) yang secara default akan
  dibatasi hanya untuk Google AI Studio dan tidak menerima kunci dari layanan lain.
  Tindakan ini akan membantu mencegah penggunaan kunci silang yang tidak diinginkan.
- Secara default, kami memblokir kunci API yang bocor dan digunakan dengan Gemini API, sehingga membantu mencegah penyalahgunaan biaya dan data aplikasi Anda.
- Anda akan dapat menemukan status kunci API Anda dalam [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=id) dan kami akan berupaya berkomunikasi secara proaktif saat kami mengidentifikasi bahwa kunci API Anda bocor untuk segera ditindaklanjuti.

## Meningkatkan kualitas output model

Untuk output model yang lebih berkualitas, pelajari cara menulis perintah yang lebih terstruktur. Halaman
[panduan rekayasa perintah](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=id)
memperkenalkan beberapa konsep dasar, strategi, dan praktik terbaik untuk membantu Anda
memulai.

## Memahami batas token

Baca [Panduan token](https://ai.google.dev/gemini-api/docs/tokens?hl=id) kami untuk lebih memahami cara
menghitung token dan batasnya.

## Masalah umum

- API ini hanya mendukung sejumlah bahasa tertentu. Mengirimkan perintah dalam bahasa yang tidak didukung dapat menghasilkan respons yang tidak terduga atau bahkan diblokir. Lihat
  [bahasa yang tersedia](https://ai.google.dev/gemini-api/docs/models?hl=id#supported-languages) untuk
  mengetahui info terbaru.

## Laporkan bug

Bergabunglah dalam diskusi di
[forum developer Google AI](https://discuss.ai.google.dev?hl=id)
jika ada pertanyaan.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-13 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-13 UTC."],[],[]]
