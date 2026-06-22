---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=id
fetched_at: 2026-06-22T06:31:13.557746+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) is now available in preview with collaborative planning, visualization, MCP support, and more.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Resolusi media

Parameter `media_resolution` mengontrol cara Gemini API memproses input media seperti gambar, video, dan dokumen PDF dengan menentukan **jumlah maksimum token** yang dialokasikan untuk input media, sehingga Anda dapat menyeimbangkan kualitas respons dengan latensi dan biaya. Untuk mengetahui setelan yang berbeda, nilai default, dan korespondensinya dengan token, lihat bagian [Jumlah token](#token-counts).

Anda dapat mengonfigurasi resolusi media dengan dua cara:

- [Per bagian](https://ai.google.dev/gemini-api/docs/media-resolution?hl=id#per-part-media-resolution) (hanya Gemini 3)
- [Secara global](https://ai.google.dev/gemini-api/docs/media-resolution?hl=id#global-media-resolution) untuk seluruh permintaan `generateContent` (semua model multimodal)

## Resolusi media per bagian (hanya Gemini 3)

Gemini 3 memungkinkan Anda menetapkan resolusi media untuk setiap objek media dalam permintaan, sehingga menawarkan pengoptimalan penggunaan token yang mendetail. Anda dapat menggabungkan tingkat resolusi dalam satu permintaan. Misalnya, menggunakan resolusi tinggi untuk diagram yang kompleks dan resolusi rendah untuk gambar kontekstual yang sederhana. Setelan ini menggantikan konfigurasi global untuk bagian tertentu. Untuk mengetahui setelan default, lihat bagian [Jumlah token](https://ai.google.dev/gemini-api/docs/media-resolution?hl=id#token-counts).

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is currently only available in the v1alpha API version. (experimental)
client = genai.Client(
  http_options={
      'api_version': 'v1alpha',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1alpha' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1alpha/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## Resolusi media global

Anda dapat menetapkan resolusi default untuk semua bagian media dalam permintaan menggunakan `GenerationConfig`. Hal ini didukung oleh semua model multimodal. Jika permintaan
menyertakan setelan global dan [per bagian](https://ai.google.dev/gemini-api/docs/media-resolution?hl=id#per-part-media-resolution), setelan per bagian akan diprioritaskan untuk item tertentu tersebut.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3.5-flash',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## Nilai resolusi yang tersedia

Gemini API menentukan tingkat berikut untuk resolusi media:

- `MEDIA_RESOLUTION_UNSPECIFIED`: Setelan default. Jumlah token untuk tingkat ini sangat bervariasi antara Gemini 3 dan model Gemini sebelumnya.
- `MEDIA_RESOLUTION_LOW`: Jumlah token lebih rendah, sehingga menghasilkan pemrosesan yang lebih cepat dan biaya yang lebih rendah, tetapi dengan detail yang lebih sedikit.
- `MEDIA_RESOLUTION_MEDIUM`: Keseimbangan antara detail, biaya, dan latensi.
- `MEDIA_RESOLUTION_HIGH`: Jumlah token lebih tinggi, memberikan lebih banyak detail untuk digunakan model, dengan mengorbankan peningkatan latensi dan biaya.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (Hanya per bagian): Jumlah token tertinggi, diperlukan untuk kasus penggunaan tertentu seperti [penggunaan komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id).

Perhatikan bahwa `MEDIA_RESOLUTION_HIGH` memberikan performa optimal untuk sebagian besar kasus penggunaan.

Jumlah token yang dihasilkan untuk setiap tingkat ini bergantung pada **jenis media** (Gambar, Video, PDF) dan **versi model**.

## Jumlah token

Tabel di bawah merangkum perkiraan jumlah token untuk setiap nilai `media_resolution` dan jenis media per kelompok model.

**Model Gemini 3**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **Gambar** | **Video** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (Default) | 1120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 280 + Teks Native |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 560 + Teks Native |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 1120 + Teks Native |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | T/A | T/A |

**Model Gemini 2.5**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **Gambar** | **Video** | **PDF (Dipindai)** | **PDF (Native)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (Default) | 256 + Geser &Pindai (~2048) | 256 | 256 + OCR | 256 + Teks Native |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 64 + OCR | 64 + Teks Native |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 256 + OCR | 256 + Teks Native |
| `MEDIA_RESOLUTION_HIGH` | 256 + Geser &Pindai | 256 | 256 + OCR | 256 + Teks Native |

## Memilih resolusi yang tepat

- **Default (`UNSPECIFIED`):** Mulai dengan setelan default. Setelan ini disesuaikan untuk keseimbangan kualitas, latensi, dan biaya yang baik untuk sebagian besar kasus penggunaan umum.
- **`LOW`:** Gunakan untuk skenario saat biaya dan latensi sangat penting, dan detail yang mendetail kurang penting.
- **`MEDIUM` / `HIGH`:** Tingkatkan resolusi saat tugas memerlukan pemahaman detail yang rumit dalam media. Hal ini sering diperlukan untuk analisis visual yang kompleks, pembacaan diagram, atau pemahaman dokumen yang padat.
- **`ULTRA HIGH`** - Hanya tersedia untuk setelan per bagian. Direkomendasikan untuk kasus penggunaan tertentu seperti penggunaan komputer atau saat pengujian menunjukkan peningkatan yang jelas dibandingkan `HIGH`.
- **Kontrol per bagian (Gemini 3):** Mengoptimalkan penggunaan token. Misalnya, dalam perintah dengan beberapa gambar, gunakan `HIGH` untuk diagram yang kompleks dan `LOW` atau `MEDIUM` untuk gambar kontekstual yang lebih sederhana.

**Setelan yang direkomendasikan**

Berikut adalah setelan resolusi media yang direkomendasikan untuk setiap jenis media yang didukung.

|  |  |  |  |
| --- | --- | --- | --- |
| **Jenis Media** | **Setelan yang Direkomendasikan** | **Token Maksimum** | **Panduan Penggunaan** |
| **Gambar** | `MEDIA_RESOLUTION_HIGH` | 1120 | Direkomendasikan untuk sebagian besar tugas analisis gambar guna memastikan kualitas maksimum. |
| **PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | Optimal untuk pemahaman dokumen; kualitas biasanya mencapai titik jenuh pada `medium`. Meningkatkan ke `high` jarang meningkatkan hasil OCR untuk dokumen standar. |
| **Video** (Umum) | `MEDIA_RESOLUTION_LOW` (atau `MEDIA_RESOLUTION_MEDIUM`) | 70 (per frame) | **Catatan:** Untuk video, setelan `low` dan `medium` diperlakukan secara identik (70 token) untuk mengoptimalkan penggunaan konteks. Hal ini cukup untuk sebagian besar tugas pengenalan dan deskripsi tindakan. |
| **Video** (Banyak Teks) | `MEDIA_RESOLUTION_HIGH` | 280 (per frame) | Hanya diperlukan jika kasus penggunaan melibatkan pembacaan teks padat (OCR) atau detail kecil dalam frame video. |

Selalu uji dan evaluasi dampak setelan resolusi yang berbeda pada aplikasi spesifik Anda untuk menemukan kompromi terbaik antara kualitas, latensi, dan biaya.

## Ringkasan kompatibilitas versi

- Enum `MediaResolution` tersedia untuk semua model yang mendukung input media.
- Jumlah token yang terkait dengan setiap tingkat enum **berbeda** antara model Gemini 3 dan versi Gemini sebelumnya.
- Menetapkan `media_resolution` pada setiap objek `Part` **khusus untuk model Gemini 3**.

## Langkah berikutnya

- Pelajari lebih lanjut kemampuan multimodal Gemini API dalam panduan
  [pemahaman gambar](https://ai.google.dev/gemini-api/docs/image-understanding?hl=id), [pemahaman video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=id) dan
  [pemahaman dokumen](https://ai.google.dev/gemini-api/docs/document-processing?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-19 UTC."],[],[]]
