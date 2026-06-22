---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=id
fetched_at: 2026-06-22T06:32:20.160993+00:00
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

# Penalaran Gemini

Model seri [Gemini 3 dan 2.5](https://ai.google.dev/gemini-api/docs/models?hl=id) menggunakan
"proses penalaran" internal yang meningkatkan kemampuan penalaran dan perencanaan multi-langkah secara signifikan, sehingga sangat efektif untuk tugas kompleks seperti
coding, matematika tingkat lanjut, dan analisis data.

Panduan ini menunjukkan cara menggunakan kemampuan penalaran Gemini menggunakan Gemini API.

## Membuat konten dengan penalaran

Memulai permintaan dengan model penalaran mirip dengan permintaan pembuatan konten lainnya. Perbedaan utamanya terletak pada penentuan salah satu
[model dengan dukungan penalaran](#supported-models) di kolom `model`, seperti yang
ditunjukkan dalam contoh [pembuatan teks](https://ai.google.dev/gemini-api/docs/text-generation?hl=id#text-input) berikut:

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.5-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## Ringkasan penalaran

Ringkasan penalaran adalah versi ringkasan dari penalaran mentah model dan menawarkan insight tentang proses penalaran internal model. Perhatikan bahwa tingkat dan anggaran penalaran berlaku untuk penalaran mentah model, bukan untuk ringkasan penalaran.

Anda dapat mengaktifkan ringkasan penalaran dengan menetapkan `includeThoughts` ke `true` dalam konfigurasi permintaan. Kemudian, Anda dapat mengakses ringkasan dengan melakukan iterasi melalui `parts` parameter `response`, dan memeriksa boolean `thought`.

Berikut adalah contoh yang menunjukkan cara mengaktifkan dan mengambil ringkasan penalaran tanpa streaming, yang menampilkan satu ringkasan penalaran akhir dengan respons:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.5-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

Berikut adalah contoh penggunaan penalaran dengan streaming, yang menampilkan ringkasan inkremental bergulir selama pembuatan:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.5-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
  }
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.5-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## Mengontrol penalaran

Model Gemini melakukan penalaran dinamis secara default, dan otomatis menyesuaikan jumlah upaya penalaran berdasarkan kompleksitas permintaan pengguna.
Namun, jika Anda memiliki batasan latensi tertentu atau mengharuskan model melakukan penalaran yang lebih mendalam dari biasanya, Anda dapat menggunakan parameter secara opsional untuk mengontrol perilaku penalaran.

### Tingkat penalaran (Gemini 3)

Parameter `thinkingLevel`, yang direkomendasikan untuk model Gemini 3 dan yang lebih baru, memungkinkan Anda mengontrol perilaku penalaran.

Tabel berikut menjelaskan setelan `thinkingLevel` untuk setiap jenis model:

| Tingkat Penalaran | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Gemini 3.5 Flash | Deskripsi |
| --- | --- | --- | --- | --- | --- |
| **`minimal`** | Tidak didukung | Didukung (Default) | Didukung | Didukung | Cocok dengan setelan "tanpa penalaran" untuk sebagian besar kueri. Model mungkin berpikir sangat minimal untuk tugas coding yang kompleks. Meminimalkan latensi untuk aplikasi chat atau throughput tinggi. Perhatikan, `minimal` tidak menjamin bahwa penalaran dinonaktifkan. |
| **`low`** | Didukung | Didukung | Didukung | Didukung | Meminimalkan latensi dan biaya. Paling cocok untuk aplikasi chat, throughput tinggi, atau mengikuti petunjuk sederhana. |
| **`medium`** | Didukung | Didukung | Didukung | Didukung (Default) | Penalaran seimbang untuk sebagian besar tugas. |
| **`high`** | Didukung (Default, Dinamis) | Didukung (Dinamis) | Didukung (Default, Dinamis) | Didukung (Dinamis) | Memaksimalkan kedalaman penalaran. Model mungkin memerlukan waktu yang jauh lebih lama untuk mencapai token output pertama (non-penalaran), tetapi output akan lebih dipertimbangkan dengan cermat. |

Contoh berikut menunjukkan cara menetapkan tingkat penalaran.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Anda tidak dapat menonaktifkan penalaran untuk Gemini 3.1 Pro. Gemini 3 Flash dan Flash-Lite juga tidak mendukung penalaran nonaktif penuh, tetapi setelan `minimal` berarti model kemungkinan tidak akan berpikir (meskipun masih berpotensi).
Jika Anda tidak menentukan tingkat penalaran, Gemini akan menggunakan tingkat penalaran default model Gemini 3 (misalnya, `"high"` untuk Gemini 3.1 Pro, dan `"medium"` untuk Gemini 3.5 Flash).

Model seri Gemini 2.5 tidak mendukung `thinkingLevel`; gunakan `thinkingBudget`.

### Anggaran penalaran

Parameter `thinkingBudget`, yang diperkenalkan dengan seri Gemini 2.5, memandu model tentang jumlah token penalaran tertentu yang akan digunakan untuk penalaran.

Berikut adalah detail konfigurasi `thinkingBudget` untuk setiap jenis model.
Anda dapat menonaktifkan penalaran dengan menetapkan `thinkingBudget` ke 0.
Menetapkan `thinkingBudget` ke -1 akan mengaktifkan **penalaran dinamis**, yang berarti model akan menyesuaikan anggaran berdasarkan kompleksitas permintaan.

| Model | Setelan default (Anggaran penalaran tidak ditetapkan) | Rentang | Nonaktifkan penalaran | Aktifkan penalaran dinamis |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Penalaran dinamis | `128` hingga `32768` | T/A: Tidak dapat menonaktifkan penalaran | `thinkingBudget = -1` (Default) |
| **2.5 Flash** | Penalaran dinamis | `0` hingga `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Default) |
| **2.5 Flash Preview** | Penalaran dinamis | `0` hingga `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Default) |
| **2.5 Flash Lite** | Model tidak berpikir | `512` hingga `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite Preview** | Model tidak berpikir | `512` hingga `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 Preview** | Penalaran dinamis | `0` hingga `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Default) |
| **2.5 Flash Live Native Audio Preview (09-2025)** | Penalaran dinamis | `0` hingga `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Default) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

Bergantung pada perintah, model mungkin meluap atau kekurangan anggaran token.

## Tanda tangan penalaran

Gemini API bersifat stateless, sehingga model memperlakukan setiap permintaan API secara independen dan tidak memiliki akses ke konteks penalaran dari giliran sebelumnya dalam interaksi multi-giliran.

Untuk mengaktifkan pemeliharaan konteks penalaran di seluruh interaksi multi-giliran, Gemini menampilkan tanda tangan penalaran, yang merupakan representasi terenkripsi dari proses penalaran internal model.

- **Model Gemini 2.5** menampilkan tanda tangan penalaran saat penalaran diaktifkan dan
  permintaan menyertakan [panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#thinking),
  khususnya [deklarasi fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#step-2).
- **Model Gemini 3** dapat menampilkan tanda tangan penalaran untuk semua jenis [bagian](https://ai.google.dev/api/caching?hl=id#Part).
  Sebaiknya selalu teruskan semua tanda tangan seperti yang diterima, tetapi hal ini *diperlukan* untuk tanda tangan panggilan fungsi. Baca halaman
  [Tanda Tangan Penalaran](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=id) untuk
  mempelajari lebih lanjut.

Batasan penggunaan lainnya yang perlu dipertimbangkan dengan panggilan fungsi mencakup:

- Tanda tangan ditampilkan dari model dalam bagian lain dalam respons, misalnya panggilan fungsi atau bagian teks.
  [Teruskan seluruh respons](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#step-4)
  dengan semua bagian kembali ke model pada giliran berikutnya.
- Jangan menggabungkan bagian dengan tanda tangan.
- Jangan menggabungkan satu bagian dengan tanda tangan dengan bagian lain tanpa tanda tangan.

## Harga

Saat penalaran diaktifkan, harga respons adalah jumlah token output dan token penalaran. Anda dapat memperoleh jumlah total token penalaran yang dihasilkan dari kolom `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

Model penalaran menghasilkan penalaran lengkap untuk meningkatkan kualitas respons akhir, lalu menghasilkan [ringkasan](#summaries) output untuk memberikan insight tentang proses penalaran. Jadi, harga didasarkan pada token penalaran lengkap yang perlu dihasilkan model untuk membuat ringkasan, meskipun hanya ringkasan yang dihasilkan dari API.

Anda dapat mempelajari token lebih lanjut di [panduan Penghitungan token](https://ai.google.dev/gemini-api/docs/tokens?hl=id).

## Praktik terbaik

Bagian ini mencakup beberapa panduan untuk menggunakan model penalaran secara efisien.
Seperti biasa, mengikuti [panduan perintah dan praktik terbaik](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=id) kami akan memberikan hasil terbaik.

### Proses debug dan pengarahan

- **Tinjau penalaran**: Jika Anda tidak mendapatkan respons yang diharapkan dari model penalaran, Anda dapat menganalisis ringkasan penalaran Gemini dengan cermat.
  Anda dapat melihat cara model memecah tugas dan mencapai kesimpulannya, serta menggunakan informasi tersebut untuk mengoreksi hasil yang benar.
- **Berikan Panduan dalam Penalaran**: Jika Anda mengharapkan output yang sangat panjang, sebaiknya berikan panduan dalam perintah untuk membatasi
  [jumlah penalaran](#set-budget) yang digunakan model. Hal ini memungkinkan Anda mencadangkan lebih banyak output token untuk respons.

### Kompleksitas tugas

- **Tugas Mudah (Penalaran dapat DINONAKTIFKAN):** Untuk permintaan sederhana yang tidak memerlukan penalaran kompleks, seperti pengambilan atau klasifikasi fakta, penalaran tidak diperlukan. Contohnya mencakup:
  - "Di mana DeepMind didirikan?"
  - "Apakah email ini meminta rapat atau hanya memberikan informasi?"
- **Tugas Sedang (Default/Beberapa Penalaran):** Banyak permintaan umum yang diuntungkan dari pemrosesan langkah demi langkah atau pemahaman yang lebih mendalam. Gemini dapat menggunakan kemampuan penalaran secara fleksibel untuk tugas seperti:
  - Membuat analogi fotosintesis dan tumbuh dewasa.
  - Membandingkan dan membedakan mobil listrik dan mobil hybrid.
- **Tugas Sulit (Kemampuan Penalaran Maksimum):** Untuk tantangan yang benar-benar kompleks, seperti menyelesaikan soal matematika yang kompleks atau tugas coding, sebaiknya tetapkan anggaran penalaran yang tinggi. Jenis tugas ini mengharuskan model untuk menggunakan kemampuan penalaran dan perencanaan penuh, yang sering kali melibatkan banyak langkah internal sebelum memberikan jawaban. Contohnya mencakup:
  - Menyelesaikan soal 1 di AIME 2025: Temukan jumlah semua basis bilangan bulat b > 9 untuk
    yang 17b adalah pembagi 97b.
  - Menulis kode Python untuk aplikasi web yang memvisualisasikan data pasar saham real-time, termasuk autentikasi pengguna. Buat seefisien mungkin.

## Model, alat, dan kemampuan yang didukung

Fitur penalaran didukung di semua model seri 3 dan 2.5.
Anda dapat menemukan semua kemampuan model di
[halaman ringkasan model](https://ai.google.dev/gemini-api/docs/models?hl=id).

Model penalaran berfungsi dengan semua alat dan kemampuan Gemini. Hal ini memungkinkan model berinteraksi dengan sistem eksternal, menjalankan kode, atau mengakses informasi real-time, yang menggabungkan hasilnya ke dalam penalaran dan respons akhir.

Anda dapat mencoba contoh penggunaan alat dengan model penalaran di [Buku resep penalaran][Colab].

## Apa langkah selanjutnya?

- Cakupan penalaran tersedia di panduan [Kompatibilitas OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=id#thinking).

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-19 UTC."],[],[]]
