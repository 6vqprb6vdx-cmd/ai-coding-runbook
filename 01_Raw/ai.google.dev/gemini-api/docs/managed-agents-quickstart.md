---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=id
fetched_at: 2026-06-08T15:01:26.646333+00:00
title: "Panduan Memulai Agen Terkelola \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Panduan Memulai Agen Terkelola

Panduan ini akan memandu Anda membuat dan menggunakan Agen Terkelola di Gemini API, menggunakan [agen Antigravitasi](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=id). Anda akan melakukan panggilan agen pertama, melanjutkan percakapan bolak-balik, melakukan streaming respons, mendownload file dari sandbox, dan menggunakan agen terkelola Antigravity.

## Menjalankan interaksi agen pertama Anda

Satu panggilan ke [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=id) menyediakan sandbox Linux, menjalankan loop agen, dan menampilkan hasilnya. Anda akan menentukan tiga parameter:

- Teruskan `agent` sebagai `"antigravity-preview-05-2026",` yang merupakan versi saat ini dari agen terkelola tujuan umum dan yang telah ditentukan sebelumnya.
- Tentukan `environment="remote"`, untuk menyediakan lingkungan sandbox baru yang bersih.
- Buat input, yang menentukan tindakan yang Anda inginkan dari agen.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

Respons menampilkan objek `Interaction`. Simpan `interaction.id` dan `interaction.environment_id` untuk melanjutkan percakapan di sandbox yang sama. Gunakan `interaction.output_text` untuk mengakses respons akhir agen. `interaction.steps` mencantumkan setiap langkah yang dilakukan agen (penalaran, panggilan alat, eksekusi kode).

## Lanjutkan percakapan (multi-giliran)

API melacak dua dimensi status independen:

- **Konteks percakapan:** histori chat, jejak penalaran, penggunaan alat, menggunakan `previous_interaction_id`.
- [**Status lingkungan:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id) file, paket yang diinstal, dan status sandbox, menggunakan `environment`.

Teruskan keduanya di tempatnya masing-masing untuk melanjutkan:

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

File dari giliran 1 (`fibonacci.txt`) tetap ada di giliran 2. Agen juga mempertahankan konteks percakapan.

Anda dapat memadupadankan hal-hal ini secara terpisah:

- **Hapus percakapan, simpan file:** Hilangkan `previous_interaction_id`, hanya teruskan ID lingkungan menggunakan `environment` untuk percakapan baru di ruang kerja yang sama.
- **Lanjutkan percakapan, ruang kerja baru:** Teruskan `previous_interaction_id`, tetapkan `environment="remote"` untuk sandbox baru.

### Pemadatan konteks otomatis

Dalam percakapan multi-turn yang berjalan lama, histori mentah langkah-langkah penalaran, panggilan alat, dan konten file besar dapat berkembang dengan cepat dan menggunakan ruang konteks yang signifikan. Untuk mencegah error batas token dan mempertahankan fokus agen (mencegah "context rot"), Managed Agents API menampilkan langkah pemadatan konteks native pada sekitar 135 ribu token. Hal ini terjadi secara otomatis.

## Streaming respons

Untuk tugas yang berjalan lama, Anda dapat melakukan streaming respons untuk melihat pekerjaan agen secara real time:

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

Streaming menampilkan iterable delta langkah, yang merupakan teks inkremental, token penalaran, dan update panggilan alat. Pelajari lebih lanjut cara melakukan streaming respons di [panduan Streaming](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=id).

## Mendownload file dari lingkungan

Saat agen membuat file di dalam sandbox. Download menggunakan Files API dengan permintaan HTTP langsung (belum ada metode SDK):

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

tar -xf snapshot.tar -C extracted_snapshot
```

## Menyimpan agen terkelola

Pada langkah sebelumnya, kita menggunakan agen Antigravity default dan menyesuaikannya secara inline. Setelah melakukan iterasi pada konfigurasi (petunjuk, kemampuan, dan lingkungan), Anda dapat menyimpannya sebagai agen terkelola. Dengan begitu, Anda dapat memanggilnya berdasarkan ID tanpa mengulangi konfigurasi.

Saat menyimpan agen, Anda menentukan `base_environment` (baik dari sumber atau dengan membuat cabang lingkungan yang ada). Agen akan menggunakan lingkungan ini untuk setiap interaksi baru.

**Dari sumber:** Tentukan sumber secara inline, atau dari sumber lain seperti GitHub atau Cloud Storage.

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## Memanggil agen terkelola

Setelah menyimpan agen terkelola, Anda dapat memanggilnya berdasarkan ID. Setiap pemanggilan membuat cabang lingkungan dasar, sehingga setiap eksekusi dimulai dengan bersih:

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## Langkah berikutnya

- [Agen Antigravitasi](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id): kemampuan, alat yang didukung, input multimodal, harga, dan batasan.
- [Membangun Agen Terkelola](https://ai.google.dev/gemini-api/docs/custom-agents?hl=id): perluas Antigravity dengan petunjuk, keterampilan, dan data Anda sendiri.
- [Lingkungan](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id): sumber, jaringan, siklus proses, batas resource.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=id): API pokok untuk model dan agen.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-20 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-20 UTC."],[],[]]
