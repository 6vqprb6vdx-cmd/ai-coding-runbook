---
source_url: https://ai.google.dev/gemini-api/docs/interactions/media-resolution?hl=id
fetched_at: 2026-05-11T12:35:48.379060+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Resolusi media

Parameter `media_resolution` mengontrol cara Gemini API memproses input media seperti gambar, video, dan dokumen PDF dengan menentukan **jumlah token maksimum** yang dialokasikan untuk input media, sehingga Anda dapat menyeimbangkan kualitas respons dengan latensi dan biaya. Untuk mengetahui setelan yang berbeda, nilai default, dan korespondensinya dengan token, lihat bagian [Jumlah token](#token-counts).

Anda dapat mengonfigurasi resolusi media untuk setiap objek media (item konten) dalam permintaan Anda (khusus Gemini 3).

## Resolusi media per item konten (khusus Gemini 3)

Gemini 3 memungkinkan Anda menetapkan resolusi media untuk setiap objek media dalam permintaan Anda, sehingga menawarkan pengoptimalan penggunaan token yang mendetail. Anda dapat menggabungkan tingkat resolusi dalam satu permintaan. Misalnya, menggunakan resolusi tinggi untuk diagram yang kompleks dan resolusi rendah untuk gambar kontekstual yang sederhana.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Nilai resolusi yang tersedia

Gemini API menentukan tingkat resolusi media berikut:

- `unspecified`: Setelan default. Jumlah token untuk tingkat ini sangat bervariasi antara Gemini 3 dan model Gemini sebelumnya.
- `low`: Jumlah token lebih rendah, sehingga menghasilkan pemrosesan yang lebih cepat dan biaya yang lebih rendah, tetapi dengan detail yang lebih sedikit.
- `medium`: Keseimbangan antara detail, biaya, dan latensi.
- `high`: Jumlah token lebih tinggi, memberikan lebih banyak detail untuk digunakan model, dengan mengorbankan peningkatan latensi dan biaya.
- `ultra_high` (Khusus per item konten): Jumlah token tertinggi, diperlukan untuk kasus penggunaan tertentu seperti [penggunaan komputer](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=id).

Perhatikan bahwa `high` memberikan performa optimal untuk sebagian besar kasus penggunaan.

Jumlah token yang dihasilkan untuk setiap tingkat ini bergantung pada **jenis media** (Gambar, Video, PDF) dan **versi model**.

## Jumlah token

Tabel di bawah merangkum perkiraan jumlah token untuk setiap nilai `media_resolution` dan jenis media per kelompok model.

**Model Gemini 3**

| MediaResolution | Gambar | Video | PDF |
| --- | --- | --- | --- |
| `unspecified` (Default) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + Teks Native |
| `medium` | 560 | 70 | 560 + Teks Native |
| `high` | 1120 | 280 | 1120 + Teks Native |
| `ultra_high` | 2240 | T/A | T/A |

## Memilih resolusi yang tepat

- **Default (`unspecified`):** Mulai dengan setelan default. Setelan ini disesuaikan untuk keseimbangan kualitas, latensi, dan biaya yang baik untuk sebagian besar kasus penggunaan umum.
- **`low`:** Gunakan untuk skenario saat biaya dan latensi sangat penting, dan detail mendetail kurang penting.
- **`medium` / `high`:** Tingkatkan resolusi saat tugas memerlukan pemahaman detail yang rumit dalam media. Hal ini sering kali diperlukan untuk analisis visual yang kompleks, pembacaan diagram, atau pemahaman dokumen yang padat.
- **`ultra_high`** - Hanya tersedia untuk setelan per item konten. Direkomendasikan untuk kasus penggunaan tertentu seperti penggunaan komputer atau saat pengujian menunjukkan peningkatan yang jelas dibandingkan `high`.
- **Kontrol per item konten (Gemini 3):** Mengoptimalkan penggunaan token. Misalnya, dalam perintah dengan beberapa gambar, gunakan `high` untuk diagram yang kompleks dan `low` atau `medium` untuk gambar kontekstual yang lebih sederhana.

**Setelan yang direkomendasikan**

Berikut adalah setelan resolusi media yang direkomendasikan untuk setiap jenis media yang didukung.

| Jenis Media | Setelan yang Direkomendasikan | Token Maksimum | Panduan Penggunaan |
| --- | --- | --- | --- |
| **Gambar** | `high` | 1120 | Direkomendasikan untuk sebagian besar tugas analisis gambar guna memastikan kualitas maksimum. |
| **PDF** | `medium` | 560 | Optimal untuk pemahaman dokumen; kualitas biasanya mencapai titik jenuh pada `medium`. Meningkatkan ke `high` jarang meningkatkan hasil OCR untuk dokumen standar. |
| **Video** (Umum) | `low` (atau `medium`) | 70 (per frame) | **Catatan:** Untuk video, setelan `low` dan `medium` diperlakukan sama (70 token) untuk mengoptimalkan penggunaan konteks. Hal ini cukup untuk sebagian besar tugas pengenalan dan deskripsi tindakan. |
| **Video** (Banyak Teks) | `high` | 280 (per frame) | Hanya diperlukan jika kasus penggunaan melibatkan pembacaan teks padat (OCR) atau detail kecil dalam frame video. |

Selalu uji dan evaluasi dampak setelan resolusi yang berbeda pada aplikasi Anda untuk menemukan kompromi terbaik antara kualitas, latensi, dan biaya.

## Ringkasan kompatibilitas versi

- Menetapkan `resolution` pada setiap item konten **khusus untuk model Gemini 3**.

## Langkah berikutnya

- Pelajari lebih lanjut kemampuan multimodal Gemini API dalam panduan [pemahaman gambar](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=id), [pemahaman video](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=id), dan [pemahaman dokumen](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-09 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-09 UTC."],[],[]]
