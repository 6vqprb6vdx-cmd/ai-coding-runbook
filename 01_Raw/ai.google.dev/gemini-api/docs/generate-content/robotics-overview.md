---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-overview?hl=id
fetched_at: 2026-08-24T02:29:46.885032+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Gemini Robotics ER

Model Gemini Robotics ER (penalaran berwujud) adalah model bahasa visual (VLM) yang memungkinkan robot memahami dan berinteraksi dengan dunia fisik. Mereka menafsirkan data visual, melakukan penalaran spasial dan temporal, merencanakan tugas multi-langkah, serta mengatur robot dan alat.

## Model

Model Gemini Robotics ER 2 adalah model terbaru di Gemini Robotics.
Model penalaran yang diperbarui ini memungkinkan robot memahami lingkungan mereka dengan tepat. Model ini dikhususkan untuk kemampuan penalaran berwujud, seperti orkestrasi agen robot (misalnya, menggunakan VLA), pemahaman video robot termasuk pemahaman progres dan deteksi keberhasilan, pembacaan instrumen, penunjuk, dan penalaran spasial.

Model Gemini Robotics ER 2 memperkenalkan dua endpoint model:

- **`gemini-robotics-er-2-preview`**: Model ER 2 standar. Dibuat berdasarkan
  Gemini 3.5 Flash dengan penalaran spasial yang ditingkatkan, penemuan momen video,
  klasifikasi progres video, orkestrasi multi-robot, dan penggunaan alat
  multi-langkah.
- **`gemini-robotics-er-2-streaming-preview`**: Dioptimalkan untuk streaming real-time melalui [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=id). Gunakan model ini untuk agen robot latensi rendah yang memproses input audio dan video berkelanjutan.

Jika Anda menggunakan Gemini Robotics ER 1.6, upgrade ke Gemini Robotics ER 2 dengan mengganti
`model="gemini-robotics-er-1.6-preview"` dengan
`model="gemini-robotics-er-2-preview"` atau
`model="gemini-robotics-er-2-streaming-preview"` dalam panggilan API Anda. Perhatikan bahwa model Gemini Robotics ER 1.6 akan dinonaktifkan pada [akhir Agustus](https://ai.google.dev/gemini-api/docs/deprecations?hl=id#robotics-models).

[Mencoba Gemini Robotics ER 2 di Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=id)

## Kemampuan robotika

Gemini Robotics ER mendukung berbagai kemampuan penalaran berwujud.
Pilih kemampuan untuk mempelajari lebih lanjut:

| Kemampuan | Deskripsi | Panduan |
| --- | --- | --- |
| Penalaran spasial | Arahkan ke objek, lacak dalam video, deteksi dengan kotak pembatas, rencanakan lintasan. | [Penalaran spasial](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=id) |
| Visi agentic | Gunakan eksekusi kode untuk meningkatkan kemampuan lain dengan memanfaatkan alat manipulasi gambar. | [Visi agentik](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=id) |
| Orkestrasi tugas | Menggabungkan penalaran spasial dengan API robot kustom untuk menyelesaikan tugas dengan cakupan waktu yang panjang. | [Orkestrasi tugas](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=id) |
| Streaming (khusus endpoint Streaming Gemini Robotics ER 2) | Streaming dua arah untuk agen robot real-time dengan panggilan fungsi berlatensi rendah. | [Streaming untuk robotika](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=id) |
| Progres video (khusus Gemini Robotics ER 2) | Penemuan momen dan klasifikasi progres dari feed video berkelanjutan. | [Pemahaman video](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=id) |

## Memulai

Contoh berikut menemukan objek dalam gambar dan menampilkan koordinat 2D dan labelnya yang dinormalisasi. Anda dapat meneruskan output ini langsung ke robotics API atau model VLA untuk menghasilkan tindakan robot.

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_uri(
            file_uri=uploaded_file.uri,
            mime_type=uploaded_file.mime_type
        ),
        PROMPT
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    ),
)

print(response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "'"${IMAGE_BASE64}"'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

Outputnya akan berupa array JSON yang berisi objek, yang masing-masing memiliki `point`
(koordinat `[y, x]` yang dinormalisasi) dan `label` yang mengidentifikasi objek.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

Gambar berikut adalah contoh cara titik-titik ini dapat ditampilkan:

![Contoh yang menampilkan titik objek dalam gambar](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=id)

## Cara kerjanya

Gemini Robotics ER menerima input gambar, video, atau audio dengan perintah bahasa alami. Model ini mengidentifikasi objek, memahami konteks adegan dan hubungan spasial, serta menampilkan output terstruktur seperti koordinat atau kotak pembatas.

Gemini Robotics ER juga bersifat agentik: Gemini memecah tugas yang kompleks menjadi sub-tugas dan mengeksekusinya dengan memanggil fungsi robot Anda atau menjalankan kode yang dihasilkan. Misalnya, "taruh apel di mangkuk" menjadi urutan langkah-langkah menemukan, menggenggam, dan
menempatkan.

Lihat [Panggilan
fungsi](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=id#how-it-works) untuk
mengetahui detail tentang cara Gemini mengeksekusi panggilan alat.

## Keamanan

Meskipun Gemini Robotics ER dibuat dengan mempertimbangkan keselamatan, Anda bertanggung jawab untuk menjaga lingkungan yang aman di sekitar robot. Model AI generatif dapat membuat kesalahan, dan robot fisik dapat menyebabkan kerusakan. Untuk mempelajari lebih lanjut,
buka
[halaman keamanan robotik Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=id).

## Praktik terbaik

1. Gunakan bahasa yang sederhana dan alami. Jelaskan tindakan yang Anda inginkan dari robot seperti yang Anda lakukan kepada orang lain. Jika suatu istilah tidak berfungsi, coba sinonim umum.
2. Mengoptimalkan input visual. Pangkas atau perbesar objek kecil atau tidak jelas sebelum
   mengirim gambar. Pencahayaan dan kontras warna yang rendah dapat memengaruhi deteksi.
3. Membagi tugas kompleks menjadi beberapa langkah. Kirim setiap langkah sebagai perintah terpisah untuk
   mempertahankan fokus model dan meningkatkan akurasi.
4. Lakukan kueri beberapa kali dan hitung rata-rata hasilnya untuk tugas dengan presisi tinggi. Pendekatan konsensus ini mengurangi varians pada output spasial.

## Batasan

Pertimbangkan batasan berikut saat mengembangkan dengan Gemini Robotics ER:

- **Pembatasan kunci API:** Gemini API tidak menerima permintaan dari kunci API yang tidak dibatasi dan menampilkan error `403 Forbidden`. Amankan kunci API Anda dengan menambahkan pembatasan di [AI Studio](https://aistudio.google.com/api-keys?hl=id).
  Lihat [Mengamankan kunci API yang tidak dibatasi](https://ai.google.dev/gemini-api/docs/api-key?hl=id#secure-unrestricted-keys)
  untuk mengetahui detailnya.
- **Latensi vs. performa:** Kueri yang kompleks, input beresolusi tinggi, atau tingkat pemikiran yang tinggi dapat menyebabkan peningkatan waktu pemrosesan. Untuk level pemikiran, gunakan sedang untuk keseimbangan yang baik antara latensi dan performa.
- **Halusinasi:** Seperti semua model bahasa besar, model Gemini Robotics ER terkadang dapat "berhalusinasi" atau memberikan informasi yang salah, terutama untuk perintah yang ambigu atau input di luar distribusi.
- **Ketergantungan pada kualitas perintah:** Kualitas output bergantung pada kejelasan perintah input. Gunakan perintah yang spesifik dan terstruktur dengan baik.
- **Biaya komputasi:** Menjalankan model, terutama dengan input video atau
  `thinking_budget` tinggi, akan menggunakan resource komputasi dan menimbulkan biaya.
  Lihat halaman [Pemikiran](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=id) untuk mengetahui detail selengkapnya.
- **Jenis input:** Lihat topik berikut untuk mengetahui detail batasan untuk setiap mode.
  - [Input gambar](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=id#technical-details-image)
  - [Input video](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=id#supported-formats)
  - [Input audio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=id#supported-formats)

## Pemberitahuan Privasi

Anda memahami bahwa model yang dirujuk dalam dokumen ini ("Model Robotik") memanfaatkan data video dan audio untuk mengoperasikan dan menggerakkan hardware Anda sesuai dengan petunjuk Anda. Oleh karena itu, Anda dapat mengoperasikan Model Robotik sehingga data dari orang yang dapat diidentifikasi, seperti data suara, gambar, dan kemiripan ("Data Pribadi"), akan dikumpulkan oleh Model Robotik. Jika Anda memilih untuk mengoperasikan Model Robotik dengan cara yang mengumpulkan Data Pribadi, Anda setuju bahwa Anda tidak akan mengizinkan orang yang dapat diidentifikasi untuk berinteraksi dengan, atau berada di area sekitar, Model Robotik, kecuali dan hingga orang yang dapat diidentifikasi tersebut telah diberi tahu dan menyetujui secara memadai bahwa Data Pribadi mereka dapat diberikan kepada dan digunakan oleh Google sebagaimana diuraikan dalam Persyaratan Layanan Tambahan Gemini API yang dapat ditemukan di [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=id) (selanjutnya disebut "Persyaratan"), termasuk sesuai dengan bagian yang berjudul "Cara Google Menggunakan Data Anda". Anda akan memastikan bahwa pemberitahuan tersebut mengizinkan pengumpulan dan penggunaan Data Pribadi sebagaimana diuraikan dalam Persyaratan, dan Anda akan menggunakan upaya yang wajar secara komersial untuk meminimalkan pengumpulan dan distribusi Data Pribadi dengan menggunakan teknik seperti mengaburkan wajah dan mengoperasikan Model Robotik di area yang tidak berisi orang yang dapat diidentifikasi sejauh yang dapat dilakukan.

## Harga

Untuk mengetahui informasi mendetail tentang harga dan wilayah yang tersedia, lihat halaman
[harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id).

## Endpoint model

### Pratinjau Gemini Robotics ER 2

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | `gemini-robotics-er-2-preview` |
| saveJenis data yang didukung | **Input**  Teks, gambar, video, audio  **Output**  Teks |
| token\_autoBatas token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=id) | **Batas token input**  131.072  **Batas token output**  65.536 |
| handymanKemampuan | **[Pembuatan audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id)**  Tidak didukung  **[Caching](https://ai.google.dev/gemini-api/docs/caching?hl=id)**  Didukung  **[Eksekusi kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id)**  Didukung  **[Penggunaan komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id)**  Didukung  **[Penelusuran file](https://ai.google.dev/gemini-api/docs/file-search?hl=id)**  Didukung  **[Pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)**  Didukung  **[Melakukan grounding dengan Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id)**  Didukung  **[Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id)**  Tidak didukung  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=id)**  Tidak didukung  **[Grounding penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id)**  Didukung  **[Output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id)**  Didukung  **[Penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id)**  Didukung  **[Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id)**  Didukung |
| speedOpsi pemakaian | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id)**  Didukung  **[Inferensi fleksibel](https://ai.google.dev/gemini-api/docs/flex-inference?hl=id)**  Tidak didukung  **[Inferensi prioritas](https://ai.google.dev/gemini-api/docs/priority-inference?hl=id)**  Tidak didukung |
| Versi 123 | Baca [pola versi model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#model-versions) untuk mengetahui detail selengkapnya.  - Pratinjau: `gemini-robotics-er-2-preview` |
| calendar\_monthPembaruan terbaru | Juli 2026 |
| Kartu model id\_card | [Kartu model](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=id) |

### Pratinjau Streaming Gemini Robotics ER 2

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | `gemini-robotics-er-2-streaming-preview` |
| saveJenis data yang didukung | **Input**  Teks, gambar, video, audio  **Output**  Teks |
| token\_autoBatas token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=id) | **Batas token input**  131.072  **Batas token output**  65.536 |
| handymanKemampuan | **[Pembuatan audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id)**  Tidak didukung  **[Caching](https://ai.google.dev/gemini-api/docs/caching?hl=id)**  Tidak didukung  **[Eksekusi kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id)**  Tidak didukung  **[Penggunaan komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id)**  Tidak didukung  **[Penelusuran file](https://ai.google.dev/gemini-api/docs/file-search?hl=id)**  Tidak didukung  **[Pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)**  Didukung  **[Melakukan grounding dengan Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id)**  Tidak didukung  **[Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id)**  Tidak didukung  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=id)**  Didukung  **[Grounding penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id)**  Didukung  **[Output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id)**  Tidak didukung  **[Penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id)**  Didukung  **[Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id)**  Tidak didukung |
| speedOpsi pemakaian | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id)**  Tidak didukung  **[Inferensi fleksibel](https://ai.google.dev/gemini-api/docs/flex-inference?hl=id)**  Tidak didukung  **[Inferensi prioritas](https://ai.google.dev/gemini-api/docs/priority-inference?hl=id)**  Tidak didukung |
| Versi 123 | Baca [pola versi model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#model-versions) untuk mengetahui detail selengkapnya.  - Pratinjau: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthPembaruan terbaru | Juli 2026 |
| Kartu model id\_card | [Kartu model](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=id) |

### Pratinjau Gemini Robotics ER 1.6

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | `gemini-robotics-er-1.6-preview` |
| saveJenis data yang didukung | **Input**  Teks, gambar, video, audio  **Output**  Teks |
| token\_autoBatas token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=id) | **Batas token input**  131.072  **Batas token output**  65.536 |
| handymanKemampuan | **[Pembuatan audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id)**  Tidak didukung  **[Caching](https://ai.google.dev/gemini-api/docs/caching?hl=id)**  Didukung  **[Eksekusi kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id)**  Didukung  **[Penggunaan komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id)**  Didukung  **[Penelusuran file](https://ai.google.dev/gemini-api/docs/file-search?hl=id)**  Didukung  **[Pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)**  Didukung  **[Melakukan grounding dengan Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id)**  Didukung  **[Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id)**  Tidak didukung  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=id)**  Tidak didukung  **[Grounding penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id)**  Didukung  **[Output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id)**  Didukung  **[Penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id)**  Didukung  **[Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id)**  Didukung |
| speedOpsi pemakaian | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id)**  Didukung  **[Inferensi fleksibel](https://ai.google.dev/gemini-api/docs/flex-inference?hl=id)**  Tidak didukung  **[Inferensi prioritas](https://ai.google.dev/gemini-api/docs/priority-inference?hl=id)**  Tidak didukung |
| Versi 123 | Baca [pola versi model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#model-versions) untuk mengetahui detail selengkapnya.  - Pratinjau: `gemini-robotics-er-1.6-preview` |
| calendar\_monthPembaruan terbaru | Desember 2025 |
| cognition\_2Batas informasi | Januari 2025 |

## Langkah berikutnya

- [Penalaran spasial](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=id) — penunjuk, pelacakan, kotak pembatas, lintasan.
- [Kemampuan seperti agen](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=id) — eksekusi kode, pembacaan instrumen, anotasi gambar.
- [Orkestrasi tugas](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=id) — tugas dengan cakupan panjang menggunakan API robot kustom.
- [Robotika dengan streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=id) — streaming dua arah real-time (khusus Gemini Robotics ER 2).
- [Pemahaman video](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=id) — penemuan momen dan klasifikasi progres (khusus Gemini Robotics ER 2).
- [Keamanan robotika Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=id) — riset keamanan di balik rangkaian model.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
