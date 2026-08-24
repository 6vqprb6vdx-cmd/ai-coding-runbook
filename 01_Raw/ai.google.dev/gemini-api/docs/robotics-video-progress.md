---
source_url: https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=id
fetched_at: 2026-08-24T02:27:12.271762+00:00
title: "Pemahaman video \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Pemahaman video

Gemini Robotics ER 2 dapat melacak progres tugas dari feed video berkelanjutan menggunakan dua kemampuan:

- Penemuan momen: mengidentifikasi stempel waktu yang tepat saat peristiwa utama terjadi.
- Klasifikasi progres: menetapkan setiap video ke salah satu dari lima rentang
  penyelesaian (0–20%, 20–40%, 40–60%, 60–80%, 80–100%).

## Menemukan momen

Penemuan momen mengidentifikasi frame video yang tepat saat peristiwa penting terjadi —
misalnya, saat cangkir terisi penuh atau simpul terikat. Robot menggunakannya untuk memverifikasi keberhasilan, mengurutkan langkah-langkah, dan memicu koreksi.

Contoh perintah berikut meminta model untuk mengidentifikasi momen penyelesaian
untuk tugas tertentu dalam video:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

Berikut ini menunjukkan contoh frame dari video pencarian momen, dengan model mengidentifikasi stempel waktu penyelesaian tugas:

![Contoh frame video yang menunjukkan output penemuan momen dengan overlay stempel waktu](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=id)

## Klasifikasi progres

Klasifikasi progres menetapkan video ke salah satu dari lima rentang penyelesaian:
0–20%, 20–40%, 40–60%, 60–80%, atau 80–100%. Hal ini memberi robot kesadaran situasional real-time sehingga mereka dapat menyesuaikan tindakan atau mencoba kembali langkah-langkah yang gagal tanpa memulai ulang seluruh alur kerja.

Contoh perintah berikut meminta model untuk mengklasifikasikan tingkat progres saat ini dari video:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

Berikut menunjukkan contoh frame dari video klasifikasi progres, dengan model menetapkan rentang progres:

![Contoh frame video yang menampilkan output klasifikasi progres dengan label rentang progres](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=id)

## Contoh

Untuk contoh yang dapat dijalankan sepenuhnya, termasuk pelacakan tugas multi-langkah, lihat
[Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Langkah berikutnya

- [Live API untuk robotik](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=id) — streaming dua arah real-time.
- [Orkestrasi tugas](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=id) — tugas dengan cakrawala panjang dengan penalaran spasial.
- [Ringkasan Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=id) — perbandingan dan kemampuan model.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
