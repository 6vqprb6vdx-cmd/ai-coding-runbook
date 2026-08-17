---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=id
fetched_at: 2026-08-17T02:34:05.294257+00:00
title: "Inferensi fleksibel \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Inferensi fleksibel

Gemini Flex API adalah tingkat inferensi yang menawarkan pengurangan biaya sebesar 50% dibandingkan tarif standar, dengan imbalan latensi variabel dan ketersediaan upaya terbaik. API ini dirancang untuk workload yang toleran terhadap latensi yang memerlukan pemrosesan sinkron, tetapi tidak memerlukan performa real-time dari API standar.

## Cara menggunakan Flex

Untuk menggunakan tingkat Flex, tentukan `service_tier` sebagai `flex` dalam permintaan Anda. Secara default, permintaan menggunakan tingkat standar jika kolom ini dihilangkan.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.6-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## Cara kerja inferensi Flex

Inferensi Gemini Flex menjembatani kesenjangan antara API standar dan waktu tunggu 24 jam
dari [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id). Inferensi ini menggunakan kapasitas komputasi di luar jam sibuk yang dapat "dihapus" untuk memberikan solusi hemat biaya untuk tugas latar belakang dan alur kerja berurutan.

| Fitur | Flex | Prioritas | Standar | Batch |
| --- | --- | --- | --- | --- |
| **Harga** | Diskon 50% | 75-100% lebih banyak dari Standar | Harga penuh | Diskon 50% |
| **Latensi** | Menit (target 1–15 menit) | Rendah (Detik) | Detik hingga menit | Hingga 24 jam |
| **Keandalan** | Upaya terbaik (Dapat dihapus) | Tinggi (Tidak dapat dihapus) | Tinggi / Sedang-tinggi | Tinggi (untuk throughput) |
| **Antarmuka** | Sinkron | Sinkron | Sinkron | Asinkron |

### Manfaat utama

- **Efisiensi biaya**: Penghematan yang signifikan untuk evaluasi non-produksi, agen latar belakang, dan pengayaan data.
- **Gesekan rendah**: Cukup tambahkan satu parameter ke permintaan yang ada.
- **Alur kerja sinkron**: Ideal untuk rantai API berurutan yang permintaan berikutnya bergantung pada output permintaan sebelumnya, sehingga lebih fleksibel daripada Batch untuk alur kerja agen.

### Kasus penggunaan

- **Evaluasi offline**: Menjalankan pengujian regresi atau papan peringkat "LLM-as-a-judge".
- **Agen latar belakang**: Tugas berurutan seperti pembaruan CRM, pembuatan profil, atau moderasi konten yang dapat ditunda selama beberapa menit.
- **Penelitian dengan anggaran terbatas**: Eksperimen akademis yang memerlukan volume token tinggi dengan anggaran terbatas.

### Batas kapasitas

Traffic inferensi Flex dihitung terhadap [batas kapasitas](https://aistudio.google.com/rate-limit?hl=id) umum Anda; traffic ini tidak
menawarkan batas kapasitas yang diperluas seperti [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=id).

### Kapasitas yang dapat dihapus

Traffic Flex diperlakukan dengan prioritas yang lebih rendah. Jika ada lonjakan traffic standar, permintaan Flex dapat didahulukan atau dikeluarkan untuk memastikan kapasitas bagi pengguna prioritas tinggi. Jika Anda mencari inferensi prioritas tinggi, lihat
[Inferensi prioritas](https://ai.google.dev/gemini-api/docs/priority-inference?hl=id)

### Kode error

Jika kapasitas Flex tidak tersedia atau sistem mengalami kemacetan, API akan menampilkan kode error standar:

- **503 Layanan Tidak Tersedia**: Saat ini, sistem telah mencapai batas kapasitas.
- **429 Terlalu Banyak Permintaan**: Batas kapasitas atau kehabisan resource.

### Tanggung jawab klien

- **Tidak ada penggantian sisi server**: Untuk mencegah biaya yang tidak terduga, sistem tidak akan
  otomatis mengupgrade permintaan Flex ke tingkat Standar jika kapasitas Flex
  penuh.
- **Percobaan ulang**: Anda harus menerapkan logika percobaan ulang sisi klien sendiri dengan
  backoff eksponensial.
- **Waktu tunggu**: Karena permintaan Flex mungkin berada dalam antrean, sebaiknya
  tingkatkan waktu tunggu sisi klien menjadi 10 menit atau lebih untuk menghindari
  penutupan koneksi yang terlalu cepat.

## Menyesuaikan periode waktu tunggu

Anda dapat mengonfigurasi waktu tunggu per permintaan untuk REST API dan library klien.
Selalu pastikan waktu tunggu sisi klien Anda mencakup periode waktu tunggu server yang diinginkan (misalnya, 600 detik+ untuk antrean tunggu Flex). SDK mengharapkan nilai waktu tunggu dalam milidetik.

### Waktu tunggu per permintaan

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.6-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

## Menerapkan percobaan ulang

Karena Flex dapat dihapus dan gagal dengan error 503, berikut adalah contoh penerapan logika percobaan ulang secara opsional untuk melanjutkan permintaan yang gagal:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.6-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.6-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.6-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## Harga

Inferensi Flex dihargai 50% dari [API standar](https://ai.google.dev/gemini-api/docs/pricing?hl=id)
dan ditagih per token.

## Model yang didukung

Model berikut mendukung inferensi Flex:

| Model | Inferensi Flex |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=id) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=id) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=id) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id) | ✔️ |
| [Pratinjau Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id) | ✔️ |
| [Pratinjau Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=id) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=id) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=id) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=id) | ✔️ |

## Langkah berikutnya

- [Inferensi prioritas](https://ai.google.dev/gemini-api/docs/priority-inference?hl=id) untuk latensi ultra-rendah.
- [Token](https://ai.google.dev/gemini-api/docs/tokens?hl=id): Memahami token.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
