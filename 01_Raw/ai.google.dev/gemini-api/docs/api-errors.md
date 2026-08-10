---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=id
fetched_at: 2026-08-10T03:26:03.378748+00:00
title: "Error API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Error API

Halaman ini memberikan referensi untuk semua kode error Interactions API, menjelaskan format respons error, dan menjelaskan cara API menyampaikan error untuk berbagai jenis permintaan.

## Kode error API standar

Kode error tingkat permintaan umum ini sesuai dengan kode status HTTP standar.
Gunakan kolom `code` dalam logika aplikasi Anda untuk menangani error secara terprogram.

| Kode | Status HTTP | Deskripsi | Tindakan yang disarankan |
| --- | --- | --- | --- |
| `invalid_request` | 400 Bad Request (400 Permintaan Tidak Valid) | Permintaan salah format atau berisi parameter yang tidak valid. | Periksa input Anda berdasarkan [referensi API](https://ai.google.dev/api/interactions-api?hl=id). |
| `parameter_unknown` | 400 Bad Request (400 Permintaan Tidak Valid) | Permintaan berisi parameter yang tidak diketahui. | Hapus parameter yang tidak dikenal, lalu coba lagi. |
| `authentication` | 401 Tidak Sah | Kunci API tidak ada atau tidak valid. | Verifikasi [kunci API](https://ai.google.dev/gemini-api/docs/api-key?hl=id) Anda. |
| `permission_denied` | 403 Terlarang | Kunci API Anda tidak memiliki izin untuk resource ini. | Periksa izin kunci API dan akses project Anda. |
| `not_found` | 404 Tidak Ditemukan | Resource yang diminta tidak ditemukan. | Verifikasi jalur dan parameter resource. |
| `model_not_found` | 404 Tidak Ditemukan | Model yang ditentukan tidak ditemukan. | Verifikasi nama model atau beralih ke model lain. |
| `rate_limit_exceeded` | 429 Too Many Requests | Anda telah melampaui batas permintaan atau token per menit atau per detik. | Tunggu dan coba lagi dengan backoff eksponensial. |
| `quota_exceeded` | 429 Too Many Requests | Anda telah melampaui kuota harian. | Tunggu hingga kuota direset atau minta penambahan kuota. |
| `cancelled` | 499 Client Closed Request | Klien membatalkan permintaan sebelum selesai. | Tidak perlu tindakan apa pun. Hal ini biasanya berarti klien terputus. |
| `api_error` | 500 Error Server Internal | Terjadi error tak terduga di server. | Coba lagi permintaan tersebut. Jika masalah berlanjut, hubungi dukungan. |
| `service_unavailable` | 503 Layanan Tidak Tersedia | Layanan sedang kelebihan beban atau tidak berfungsi untuk sementara. | Tunggu dan coba lagi dengan backoff eksponensial. |

## Kode yang diblokir pembuatan

Kode error ini menunjukkan bahwa pembatasan kebijakan, keamanan, atau konten memblokir output model. Saat Anda menerima salah satu kode ini, ubah input Anda dan coba lagi.

| Kode | Deskripsi |
| --- | --- |
| `safety` | Pelanggaran keamanan (konten berbahaya) memblokir permintaan. |
| `recitation` | Pembatasan hak cipta atau pembacaan memblokir permintaan. |
| `language` | Bahasa yang tidak didukung memblokir permintaan. |
| `prohibited_content` | Pedoman konten terlarang memblokir permintaan. |
| `spii` | Pembatasan Informasi Identitas Pribadi yang Bersifat Sensitif memblokir permintaan. |
| `blocklist` | Istilah terlarang dalam daftar blokir memblokir permintaan. |
| `image_safety` | Pelanggaran keamanan memblokir pembuatan gambar. |
| `image_prohibited_content` | Pedoman konten terlarang memblokir pembuatan gambar. |
| `image_recitation` | Pembatasan hak cipta atau pembacaan memblokir pembuatan gambar. |
| `image_other` | Alasan yang tidak ditentukan memblokir pembuatan gambar. |
| `content_blocked` | Permintaan diblokir karena alasan kebijakan yang tidak ditentukan. |

## Kode error pembuatan

Kode error ini menunjukkan masalah struktural pada output yang dihasilkan model (seperti panggilan fungsi yang salah bentuk atau panggilan alat yang tidak dideklarasikan).

| Kode | Deskripsi |
| --- | --- |
| `malformed_function_call` | Model menghasilkan panggilan fungsi yang tidak dapat diuraikan. |
| `malformed_tool_call` | Model menghasilkan panggilan alat yang tidak dapat diuraikan. |
| `unexpected_tool_call` | Model memanggil alat yang tidak dideklarasikan dalam permintaan. |
| `no_image` | Model tidak dapat membuat gambar. |
| `too_many_tool_calls` | Model menghasilkan lebih banyak panggilan alat daripada yang diizinkan. |
| `missing_thought_signature` | Respons tidak memiliki tanda tangan pemikiran yang diperlukan. |

## Format respons error

Semua error dari Interactions API menampilkan objek `error` yang berisi `code` dan `message`. Misalnya, meneruskan jenis alat yang tidak didukung akan menampilkan:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| Kolom | Jenis | Deskripsi |
| --- | --- | --- |
| `code` | string | Kode error yang dapat dibaca mesin dalam `snake_case`. |
| `message` | string | Deskripsi yang dapat dibaca manusia tentang apa yang salah. |

## Cara error dikirimkan

API memberikan error secara berbeda, bergantung pada apakah Anda membuat permintaan HTTP standar atau permintaan streaming (SSE).

### Permintaan HTTP standar

Untuk permintaan standar (non-streaming), API menetapkan kode status respons HTTP (seperti `400 Bad Request`, `401 Unauthorized`, atau `429 Too Many Requests`) dan menampilkan objek `error` dalam isi respons JSON:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### Permintaan streaming (SSE)

Untuk permintaan streaming (`stream: true`), API mengirim peristiwa error melalui aliran Server-Sent Events (SSE) dengan `event_type` disetel ke `"error"`. Kolom `error` berisi struktur `code` dan `message` yang sama:

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

Untuk skema peristiwa SSE lengkap, lihat [Referensi Interactions API](https://ai.google.dev/api/interactions-api?hl=id).

## Langkah berikutnya

- [Pemecahan masalah API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=id): Atasi masalah dan skenario error umum.
- [Batas kecepatan](https://ai.google.dev/gemini-api/docs/rate-limits?hl=id): Pelajari batas permintaan dan penanganan kuota.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
