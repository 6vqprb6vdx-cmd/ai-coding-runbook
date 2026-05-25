---
source_url: https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=id
fetched_at: 2026-05-25T13:06:58.833034+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Grounding dengan Google Penelusuran

Grounding dengan Google Penelusuran menghubungkan model Gemini ke konten web real-time dan berfungsi dengan semua bahasa yang tersedia. Hal ini memungkinkan Gemini memberikan jawaban yang lebih akurat dan mengutip sumber yang dapat diverifikasi di luar batas pengetahuan.

Grounding membantu Anda membangun aplikasi yang dapat:

- **Meningkatkan akurasi faktual:** Mengurangi halusinasi model dengan mendasarkan respons pada informasi dunia nyata.
- **Mengakses informasi real-time:** Menjawab pertanyaan tentang peristiwa dan topik terbaru.
- **Memberikan kutipan:** Membangun kepercayaan pengguna dengan menampilkan sumber klaim model.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## Cara kerja grounding dengan Google Penelusuran

Saat Anda mengaktifkan alat `google_search`, model akan menangani seluruh alur kerja penelusuran, pemrosesan, dan pengutipan informasi secara otomatis.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=id)

1. **Perintah Pengguna:** Aplikasi Anda mengirimkan perintah pengguna ke Gemini API dengan alat `google_search` yang diaktifkan.
2. **Analisis Perintah:** Model menganalisis perintah dan menentukan apakah Google Penelusuran dapat meningkatkan jawaban.
3. **Google Penelusuran:** Jika diperlukan, model akan otomatis membuat satu atau beberapa kueri penelusuran dan menjalankannya.
4. **Pemrosesan Hasil Penelusuran:** Model memproses hasil penelusuran, mensintesis informasi, dan merumuskan respons.
5. **Respons yang Didasarkan pada Fakta:** API menampilkan respons akhir yang mudah digunakan dan didasarkan pada hasil penelusuran. Respons ini mencakup jawaban teks model dengan `annotations` inline yang berisi kutipan, serta langkah-langkah `google_search_call` dan `google_search_result` dengan kueri penelusuran dan saran penelusuran.

## Memahami respons grounding

Jika respons berhasil didasarkan pada fakta, output teks model akan menyertakan `annotations` inline langsung di blok konten teks. Anotasi ini memberikan informasi kutipan yang menautkan bagian respons ke sumbernya.

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

Kolom utama dalam respons:

- `google_search_call` : Berisi `queries` penelusuran yang dijalankan model.
- `google_search_result` : Berisi `search_suggestions`, cuplikan HTML untuk merender saran penelusuran di UI Anda. Persyaratan penggunaan lengkap dijelaskan dalam [Persyaratan Layanan](https://ai.google.dev/gemini-api/terms?hl=id#grounding-with-google-search).
- `text` dengan `annotations` : Jawaban model yang disintesis dengan kutipan inline. Setiap anotasi `url_citation` menautkan segmen teks (ditentukan oleh `start_index` dan `end_index`) ke URL sumber. Hal ini merupakan kunci untuk membuat kutipan inline.

Grounding dengan Google Penelusuran juga dapat digunakan bersama dengan alat konteks [URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=id) untuk mendasarkan respons pada fakta dalam
data web publik dan URL tertentu yang Anda berikan.

## Memberikan atribusi sumber dengan kutipan inline

API menampilkan anotasi `url_citation` inline di blok konten teks, sehingga Anda memiliki kontrol penuh atas cara menampilkan sumber di antarmuka pengguna.
Setiap anotasi menyertakan `start_index` dan `end_index` untuk mengidentifikasi bagian teks yang dikutip. Berikut cara mengekstrak dan menampilkannya.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

Output akan menampilkan teks yang diikuti dengan kutipannya:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## Harga

Saat Anda menggunakan Grounding dengan Google Penelusuran dengan Gemini 3, project Anda akan ditagih untuk setiap kueri penelusuran yang diputuskan untuk dijalankan oleh model. Jika model memutuskan untuk
menjalankan beberapa kueri penelusuran untuk menjawab satu perintah (misalnya,
menelusuri `"UEFA Euro 2024 winner"` dan `"Spain vs England Euro 2024 final
score"` dalam panggilan API yang sama), hal ini akan dihitung sebagai dua penggunaan alat yang dapat ditagih
untuk permintaan tersebut. Untuk tujuan penagihan, kami mengabaikan kueri penelusuran web kosong saat menghitung kueri unik. Model penagihan ini hanya berlaku untuk model Gemini 3; saat Anda menggunakan grounding penelusuran dengan model Gemini 2.5 atau yang lebih lama, project Anda akan ditagih per perintah.

Untuk mengetahui informasi harga mendetail, lihat halaman harga [Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=id).

## Model yang didukung

Anda dapat menemukan kemampuan lengkap di halaman ringkasan [model
overview](https://ai.google.dev/gemini-api/docs/models?hl=id).

| Model | Grounding dengan Google Penelusuran |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Pratinjau Gambar Gemini 3.1 Flash | ✔️ |
| Pratinjau Gemini 3.1 Pro | ✔️ |
| Pratinjau Gambar Gemini 3 Pro | ✔️ |
| Pratinjau Gemini 3 Flash | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Kombinasi alat yang didukung

Anda dapat menggunakan Grounding dengan Google Penelusuran bersama dengan alat lain seperti
[eksekusi kode](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=id) dan
[konteks URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=id) untuk mendukung kasus penggunaan
yang lebih kompleks.

Model Gemini 3 mendukung kombinasi alat bawaan (seperti Grounding dengan Google Penelusuran) dengan alat kustom (panggilan fungsi). Pelajari lebih lanjut di halaman
[kombinasi alat](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=id).

## Langkah berikutnya

- Pelajari alat lain yang tersedia, seperti [Panggilan Fungsi](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=id).
- Pelajari cara menambah perintah dengan URL tertentu menggunakan [alat konteks URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-19 UTC."],[],[]]
