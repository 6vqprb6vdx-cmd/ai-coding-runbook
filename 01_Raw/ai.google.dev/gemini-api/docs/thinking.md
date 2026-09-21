---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=id
fetched_at: 2026-09-21T05:42:31.199029+00:00
title: "Pemikiran Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Pemikiran Gemini

Model seri [Gemini 3 dan 2.5](https://ai.google.dev/gemini-api/docs/models?hl=id) menggunakan"proses penalaran" yang secara signifikan meningkatkan kemampuan penalaran dan perencanaan multi-langkahnya, sehingga sangat efektif untuk tugas kompleks seperti coding, matematika tingkat lanjut, dan analisis data.

Saat Anda menggunakan model yang berbasis penalaran, Gemini akan melakukan penalaran secara internal sebelum merespons. Interactions API menampilkan penalaran ini melalui langkah `thought`, langkah khusus yang muncul secara kronologis bersama dengan panggilan fungsi, input pengguna, atau output model dalam array `steps`.

Setiap langkah penalaran berisi dua kolom:

| Kolom | Wajib | Deskripsi |
| --- | --- | --- |
| `signature` | ✅ Ya | Representasi terenkripsi dari status penalaran internal model. Selalu ada, bahkan saat model melakukan penalaran minimal. |
| `summary` | ❌ Tidak | Array konten (teks dan/atau gambar) yang meringkas penalaran. Mungkin kosong, bergantung pada konfigurasi [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=id), apakah model melakukan penalaran yang cukup, atau jenis konten (misalnya, latensi gambar mungkin tidak memiliki ringkasan teks). |

## Interaksi dengan penalaran

Memulai interaksi dengan model yang berbasis penalaran mirip dengan permintaan interaksi lainnya. Tentukan salah satu [model dengan dukungan penalaran](#thinking-levels) di kolom `model` field:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Explain the concept of Occam's Razor and provide a simple, everyday example."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## Ringkasan penalaran

Ringkasan penalaran memberikan insight tentang proses penalaran internal model.
Secara default, hanya output akhir yang ditampilkan. Anda dapat mengaktifkan ringkasan penalaran dengan `thinking_summaries`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtStep;
import com.google.genai.gaos.models.interactions.ThoughtSummaryContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Collections;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the sum of the first 50 prime numbers?"))
        .generationConfig(
            GenerationConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ThoughtStep thoughtStep) {
    System.out.println("Thought summary:");
    for (ThoughtSummaryContent contentBlock : thoughtStep.summary().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent) {
        System.out.println(textContent.text().orElse(""));
      }
    }
    System.out.println();
  } else if (step instanceof ModelOutputStep outputStep) {
    for (Content contentBlock : outputStep.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent) {
        System.out.println("Answer:");
        System.out.println(textContent.text().orElse(""));
        System.out.println();
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

Blok penalaran hanya dapat berisi **tanda tangan tanpa ringkasan** dalam kasus berikut:

- Permintaan sederhana, saat model tidak melakukan penalaran yang cukup untuk membuat ringkasan
- `thinking_summaries: "none"`, saat ringkasan dinonaktifkan secara eksplisit
- Jenis konten penalaran tertentu, seperti gambar, mungkin tidak memiliki ringkasan teks

Kode Anda harus selalu menangani blok penalaran saat `summary` kosong atau tidak ada.

## Streaming dengan penalaran

Gunakan streaming untuk menerima ringkasan penalaran inkremental selama pembuatan.
Blok penalaran dikirim menggunakan Peristiwa yang Dikirim Server (SSE) dengan dua jenis delta yang berbeda:

| Jenis delta | Berisi | Waktu pengiriman |
| --- | --- | --- |
| `thought_summary` | Konten ringkasan teks atau gambar | Satu atau beberapa delta dengan ringkasan inkremental |
| `thought_signature` | Tanda tangan kriptografi | delta terakhir sebelum `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.StepDeltaData;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtSummaryDelta;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();

String prompt =
    "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.\n"
        + "Alice does not live in the red house.\n"
        + "Bob does not live in the green house.\n"
        + "Carol does not live in the red or green house.\n"
        + "Which house does each person live in?";

StringBuilder thoughts = new StringBuilder();
StringBuilder answer = new StringBuilder();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .generationConfig(
            GenerationConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .stream(true)
        .build();

CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));

try (EventStream<InteractionSSEStreamEvent> stream = response.events()) {
  for (InteractionSSEStreamEvent streamEvent : stream) {
    InteractionSSEEvent event = streamEvent.data().orElse(null);
    if (event instanceof StepDelta stepDelta) {
      StepDeltaData delta = stepDelta.delta().orElse(null);
      if (delta instanceof ThoughtSummaryDelta thoughtDelta) {
        Content content = thoughtDelta.content().orElse(null);
        if (content instanceof TextContent textContent) {
          if (thoughts.length() == 0) {
            System.out.println("Thinking...");
          }
          String summaryText = textContent.text().orElse("");
          System.out.print("[Thought] " + summaryText);
          thoughts.append(summaryText);
        }
      } else if (delta instanceof TextDelta textDelta) {
        String text = textDelta.text().orElse("");
        if (!text.isEmpty()) {
          if (answer.length() == 0) {
            System.out.println("\nAnswer:");
          }
          System.out.print(text);
          answer.append(text);
        }
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

Respons streaming menggunakan Peristiwa yang Dikirim Server (SSE) dan terdiri dari langkah dan peristiwa, misalnya:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.8-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Mengontrol penalaran

Model Gemini melakukan penalaran dinamis secara default, dan otomatis menyesuaikan jumlah upaya penalaran berdasarkan kompleksitas permintaan. Anda dapat mengontrol perilaku ini menggunakan parameter `thinking_level`.

| Model | Penalaran Default | Level yang Didukung |
| --- | --- | --- |
| gemini-3.8-flash | Aktif (sedang) | rendah, sedang, tinggi |
| gemini-3.7-flash | Aktif (sedang) | rendah, sedang, tinggi |
| gemini-3.6-flash | Aktif (sedang) | minimal, rendah, sedang, tinggi |
| gemini-3.5-flash-lite | Aktif (minimal) | minimal, rendah, sedang, tinggi |
| gemini-3.1-pro-preview | Aktif (tinggi) | rendah, sedang, tinggi |
| gemini-3.1-flash-lite-image | Aktif (minimal) | minimal, tinggi |
| gemini-3-flash-preview | Aktif (tinggi) | minimal, rendah, sedang, tinggi |
| gemini-3-pro-preview | Aktif (tinggi) | rendah, tinggi |
| gemini-3.5-flash | Aktif (sedang) | minimal, rendah, sedang, tinggi |
| gemini-2.5-pro | Aktif | rendah, sedang, tinggi |
| gemini-2.5-flash | Aktif | rendah, sedang, tinggi |
| gemini-2.5-flash-lite | Nonaktif | rendah, sedang, tinggi |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Provide a list of 3 famous physicists and their key contributions"))
        .generationConfig(GenerationConfig.builder().thinkingLevel(ThinkingLevel.LOW).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### Batas token dan `max_output_tokens`

Parameter pembuatan [`max_output_tokens`](https://ai.google.dev/api/interactions-api?hl=id#request-body) menetapkan jumlah maksimum token yang dapat dibuat respons, termasuk
token penalaran.

Jika ditetapkan, parameter ini akan bertindak sebagai batas maksimum yang diterapkan oleh infrastruktur tanpa mengubah cara model mengalokasikan anggaran penalarannya (`thinking_level`).

Jika model mencapai batas ini saat melakukan penalaran, model akan berhenti membuat dengan status
`"incomplete"` dan menampilkan output yang dipotong atau kosong (tetapi tetap menagih
token penalaran yang dibuat). Untuk mengurangi biaya atau latensi tanpa memotong respons, turunkan `thinking_level` (`low` atau `medium`) dan jangan menetapkan `max_output_tokens` yang kecil.

## Tanda tangan penalaran

Tanda tangan penalaran adalah representasi terenkripsi dari penalaran internal model. Tanda tangan ini diperlukan untuk mempertahankan kontinuitas penalaran di seluruh interaksi multi-giliran.

Interactions API membuat penanganan tanda tangan penalaran jauh lebih sederhana daripada `generateContent` API.

### Mode stateful (Direkomendasikan)

Secara default, saat Anda menggunakan Interactions API dalam mode stateful (dengan menetapkan `store: true` dan meneruskan `previous_interaction_id` pada giliran berikutnya), server akan otomatis mengelola status percakapan, termasuk semua blok dan tanda tangan penalaran. Dalam mode ini, Anda tidak perlu melakukan apa pun terkait tanda tangan. Tanda tangan ditangani sepenuhnya di sisi server.

### Mode stateless

Jika Anda mengelola status percakapan sendiri (mode stateless) dan meneruskan histori lengkap input dan output di setiap permintaan:

- Anda **HARUS** selalu mengirim ulang semua blok `thought` persis seperti yang diterima dari model.
- Anda **TIDAK BOLEH** menghapus atau mengubah blok penalaran dari histori, karena blok tersebut berisi tanda tangan yang diperlukan agar model dapat melanjutkan penalarannya.
- Saat beralih model dalam sesi, Anda tetap harus mengirim ulang blok penalaran model sebelumnya. Backend mengelola kompatibilitas.

## Harga

Jika penalaran diaktifkan, harga respons adalah jumlah token output dan token penalaran. Anda bisa mendapatkan jumlah total token penalaran yang dibuat dari kolom `total_thought_tokens`.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Usage;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain the concept of Occam's Razor."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.usage().isPresent()) {
  Usage usage = interaction.usage().get();
  System.out.println("Thoughts tokens: " + usage.totalThoughtTokens().orElse(0));
  System.out.println("Output tokens: " + usage.totalOutputTokens().orElse(0));
}
```

Model penalaran membuat penalaran lengkap untuk meningkatkan kualitas respons akhir, lalu menghasilkan [ringkasan](#summaries) untuk memberikan insight tentang proses penalaran. Harga didasarkan pada token penalaran lengkap yang perlu dibuat model, meskipun hanya ringkasan yang dihasilkan dari API.

Anda dapat mempelajari token lebih lanjut di panduan [Penghitungan token](https://ai.google.dev/gemini-api/docs/tokens?hl=id).

## Praktik terbaik

Gunakan model penalaran secara efisien dengan mengikuti panduan ini.

- **Tinjau penalaran**: Analisis ringkasan penalaran untuk memahami kegagalan dan meningkatkan perintah.
- **Kontrol anggaran penalaran**: Perintahkan model untuk melakukan penalaran yang lebih sedikit untuk output yang panjang guna menghemat token.
- **Tugas sederhana**: Gunakan penalaran minimal atau rendah untuk pengambilan atau klasifikasi fakta (misalnya, "Di mana DeepMind didirikan?").
- **Tugas sedang**: Gunakan penalaran default untuk membandingkan konsep atau penalaran kreatif (misalnya, Bandingkan mobil listrik dan mobil hybrid).
- **Tugas kompleks**: Gunakan penalaran maksimum untuk coding, matematika, atau perencanaan multi-langkah tingkat lanjut (misalnya, Selesaikan soal matematika AIME).

## Langkah berikutnya

- [Pembuatan teks](https://ai.google.dev/gemini-api/docs/text-generation?hl=id): Respons teks dasar
- [Panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id): Menghubungkan ke alat
- [Panduan Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=id): Fitur khusus model

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-18 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-18 UTC."],[],[]]
