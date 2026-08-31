---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tool-combination?hl=id
fetched_at: 2026-08-31T06:30:41.740136+00:00
title: "Menggabungkan alat bawaan dan panggilan fungsi \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Menggabungkan alat bawaan dan panggilan fungsi

Gemini memungkinkan kombinasi [alat bawaan](https://ai.google.dev/gemini-api/docs/tools?hl=id), seperti
`google_search`, dan [panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)
(juga dikenal sebagai *alat kustom*) dalam satu generasi dengan mempertahankan dan mengekspos
histori konteks panggilan alat. Kombinasi alat bawaan dan kustom memungkinkan alur kerja kompleks dan berbasis agen, yang dalam hal ini, misalnya, model dapat mendasarkan diri pada data web real-time sebelum memanggil logika bisnis spesifik Anda.

Berikut adalah contoh yang memungkinkan kombinasi alat bawaan dan kustom dengan `google_search` dan fungsi kustom `getWeather`:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather],  # Custom tool
            ),
        ],
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)
function_call_id = None
for part in response.candidates[0].content.parts:
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")
        function_call_id = part.function_call.id

# Turn 2: Manually build history to circulate both tool and function context
history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    # Response from Turn 1 includes tool_call, tool_response, and thought_signatures
    response.candidates[0].content,
    # Return the function_response
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=function_call_id # Match the ID from the function_call
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3.7-flash",
    contents=history,
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),
                function_declarations=[getWeather]
            ),
        ],
        # This flag needs to be enabled for built-in tool context circulation and tool combination
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)

for part in response_2.candidates[0].content.parts:
    if part.text:
        print(part.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: Type.OBJECT,
        properties: {
            location: {
                type: Type.STRING,
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const response1 = await client.models.generateContent({
        model: "gemini-3.7-flash",
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    for (const part of response1.candidates[0].content.parts) {
        if (part.functionCall) {
            console.log(`Function call: ${part.functionCall.name} (ID: ${part.functionCall.id})`);
        }
    }

   const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    // Turn 2: Manually build history to circulate both tool and function context
    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        // Response from Turn 1 includes tool_call, tool_response, and thought_signatures
        response1.candidates[0].content,
        // Return the function_response
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId // Match the ID from the function_call
                }
            }]
        }
    ];

    const response2 = await client.models.generateContent({
        model: "gemini-3.7-flash",
        contents: history,
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    for (const part of response2.candidates[0].content.parts) {
        if (part.text) {
            console.log(part.text);
        }
    }
}

run();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/generative-ai-go/genai"
    "google.golang.org/api/option"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("GEMINI_API_KEY")))
    if err != nil {
        log.Exit(err)
    }
    defer client.Close()

    getWeather := &genai.FunctionDeclaration{
        Name:        "getWeather",
        Description: "Get the weather in a given location",
        Parameters: &genai.Schema{
            Type: genai.Object,
            Properties: map[string]*genai.Schema{
                "location": {
                    Type:        genai.String,
                    Description: "The city and state, e.g. San Francisco, CA",
                },
            },
            Required: []string{"location"},
        },
    }

    model := client.GenerativeModel("gemini-3.7-flash")
    model.Tools = []*genai.Tool{
        {GoogleSearch: &genai.GoogleSearch{}}, // Built-in tool
        {FunctionDeclarations: []*genai.FunctionDeclaration{getWeather}}, // Custom tool
    }
    ist := true
    model.ToolConfig = &genai.ToolConfig{
        IncludeServerSideToolInvocations: &ist, // This flag needs to be enabled for built-in tool context circulation and tool combination
    }

    chat := model.StartChat()

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    prompt := genai.Text("What is the northernmost city in the United States? What's the weather like there today?")
    resp1, err := chat.SendMessage(ctx, prompt)
    if err != nil {
        log.Exitf("SendMessage failed: %v", err)
    }

    if resp1 == nil || len(resp1.Candidates) == 0 || resp1.Candidates[0].Content == nil {
        log.Exit("empty response from model")
    }

    var functionCallID string
    for _, part := range resp1.Candidates[0].Content.Parts {
        switch p := part.(type) {
        case genai.FunctionCall:
            fmt.Printf("Function call: %s (ID: %s)\n", p.Name, p.ID)
            if p.Name == "getWeather" {
                functionCallID = p.ID
            }
        }
    }

    if functionCallID == "" {
        log.Exit("no getWeather function call in response")
    }

    // Turn 2: Provide function result back to model.
    // Chat history automatically includes tool_call, tool_response, and thought_signatures from Turn 1.
    fr := genai.FunctionResponse{
        Name: "getWeather",
        ID:   functionCallID,
        Response: map[string]any{
            "response": "Very cold. 22 degrees Fahrenheit.",
        },
    }

    resp2, err := chat.SendMessage(ctx, fr)
    if err != nil {
        log.Exitf("SendMessage for turn 2 failed: %v", err)
    }

    if resp2 == nil || len(resp2.Candidates) == 0 || resp2.Candidates[0].Content == nil {
        log.Exit("empty response from model in turn 2")
    }

    for _, part := range resp2.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Println(string(txt))
        }
    }
}
```

### REST

```
# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.7-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What is the northernmost city in the United States? What'\''s the weather like there today?"
    }]
  }],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'

# Turn 2: Manually build history to circulate both tool and function context
# The following request assumes you have captured candidates[0].content from Turn 1 response,
# and extracted function_call.id for getWeather.
# Replace FUNCTION_CALL_ID and insert candidate content from turn 1.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.7-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "What is the northernmost city in the United States? What'\''s the weather like there today?"}]
    },
    YOUR_CANDIDATE_CONTENT_FROM_TURN_1_RESPONSE,
    {
      "role": "user",
      "parts": [{
        "functionResponse": {
          "name": "getWeather",
          "id": "FUNCTION_CALL_ID",
          "response": {"response": "Very cold. 22 degrees Fahrenheit."}
        }
      }]
    }
  ],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'
```

## Cara kerjanya

Model Gemini 3 menggunakan *sirkulasi konteks alat* untuk mengaktifkan kombinasi alat bawaan dan kustom. Sirkulasi konteks alat memungkinkan konteks alat bawaan dipertahankan dan diekspos, serta dibagikan dengan alat kustom dalam panggilan yang sama dari satu giliran ke giliran berikutnya.

### Mengaktifkan kombinasi alat

- Anda harus menetapkan tanda `include_server_side_tool_invocations` ke `true` untuk mengaktifkan sirkulasi konteks alat.
- Sertakan [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#function-declarations), beserta
  alat bawaan yang ingin Anda gunakan, untuk memicu perilaku kombinasi.
  - Jika Anda tidak menyertakan `function_declarations`, sirkulasi konteks alat akan tetap bertindak pada alat bawaan yang disertakan, selama tanda ditetapkan.

### Bagian yang ditampilkan API

Dalam satu respons, API menampilkan bagian `toolCall` dan `toolResponse` untuk panggilan alat bawaan. Untuk panggilan fungsi (alat kustom), API menampilkan bagian panggilan `functionCall`, yang akan diisi pengguna dengan bagian `functionResponse` pada giliran berikutnya.

- `toolCall` dan `toolResponse`: API menampilkan bagian ini untuk mempertahankan konteks alat yang dijalankan di sisi server, dan hasil eksekusinya, untuk giliran berikutnya.
- `functionCall` dan `functionResponse`: API mengirimkan panggilan fungsi kepada
  pengguna untuk diisi, dan pengguna mengirimkan hasilnya kembali dalam
  respons fungsi (bagian ini standar untuk semua [panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id) di Gemini API, bukan hanya untuk fitur kombinasi alat
  ).
- ([Hanya alat](https://ai.google.dev/gemini-api/docs/code-execution?hl=id)eksekusi kode)
  `executableCode` dan `codeExecutionResult`:
  Saat menggunakan alat Eksekusi Kode, bukan `functionCall` dan
  `functionResponse`, API menampilkan `executableCode` (kode yang dibuat
  oleh model yang dimaksudkan untuk dieksekusi) dan `codeExecutionResult` (hasil
  kode yang dapat dieksekusi).

Anda harus menampilkan semua bagian, termasuk semua [kolom](#critical-fields) yang ada di dalamnya, kembali ke model pada setiap giliran untuk mempertahankan konteks dan mengaktifkan kombinasi alat.

### Kolom penting di bagian yang ditampilkan

Bagian [tertentu yang ditampilkan oleh API](#api-returns-parts) akan menyertakan kolom `id`,
`tool_type`, dan `thought_signature`. Kolom ini sangat penting untuk mempertahankan konteks alat (dan oleh karena itu, sangat penting untuk kombinasi alat); Anda harus menampilkan semua bagian *seperti yang diberikan dalam respons* di permintaan berikutnya.

- `id`: ID unik yang memetakan panggilan ke responsnya. **`id` \*\*ditetapkan pada semua respons panggilan fungsi\*\* , terlepas dari sirkulasi konteks alat.**
  Anda *harus* memberikan `id` yang sama dalam respons fungsi yang diberikan API dalam panggilan fungsi. Alat bawaan secara otomatis membagikan `id` antara panggilan alat dan respons alat.
  - Ditemukan di semua bagian terkait alat: `toolCall`, `toolResponse`, `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: Mengidentifikasi alat tertentu yang digunakan; alat bawaan literal atau (misalnya `URL_CONTEXT`) atau nama fungsi (misalnya `getWeather`).
  - Ditemukan di bagian `toolCall` dan `toolResponse`.
- `thought_signature`: Konteks terenkripsi sebenarnya yang disematkan di **setiap bagian yang ditampilkan oleh API**. Konteks tidak dapat direkonstruksi tanpa tanda pikiran; jika Anda tidak menampilkan tanda pikiran untuk semua bagian di setiap giliran, model akan menampilkan error.
  - Ditemukan di *semua* bagian.

### Data khusus alat

Beberapa alat bawaan menampilkan argumen data yang terlihat oleh pengguna yang khusus untuk jenis alat.

| Alat | Argumen panggilan alat yang terlihat oleh pengguna (jika ada) | Respons alat yang terlihat oleh pengguna (jika ada) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` URL yang akan dijelajahi | `urls_metadata` `retrieved_url`: URL yang dijelajahi `url_retrieval_status`: Status penjelajahan |
| **FILE\_SEARCH** | Tidak ada | Tidak ada |

## Contoh struktur permintaan kombinasi alat

Struktur permintaan berikut menunjukkan struktur permintaan perintah: "What is the northernmost city in the United States? What's the weather like there today?". Struktur ini menggabungkan tiga alat: alat Gemini bawaan `google_search` dan `code_execution`, serta fungsi kustom `get_weather`.

```
{
  "model": "models/gemini-3.7-flash",
  "contents": [{
    "parts": [{
      "text": "What is the northernmost city in the United States? What's the weather like there today?"
    }],
    "role": "user"
  }, {
    "parts": [{
      "thoughtSignature": "...",
      "toolCall": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "args": {
          "queries": ["northernmost city in the United States"]
        },
        "id": "a7b3k9p2"
      }
    }, {
      "thoughtSignature": "...",
      "toolResponse": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "response": {
          "search_suggestions": "..."
        },
        "id": "a7b3k9p2"
      }
    }, {
      "functionCall": {
        "name": "getWeather",
        "args": {
          "city": "Utqiaġvik, Alaska"
        },
        "id": "m4q8z1v6"
      },
      "thoughtSignature": "..."
    }],
    "role": "model"
  }, {
    "parts": [{
      "functionResponse": {
        "name": "getWeather",
        "response": {
          "response": "Very cold. 22 degrees Fahrenheit."
        },
        "id": "m4q8z1v6"
      }
    }],
    "role": "user"
  }],
  "tools": [{
    "functionDeclarations": [{
      "name": "getWeather"
    }]
  }, {
    "googleSearch": {
    }
  }, {
    "codeExecution": {
    }
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}
```

## Token dan harga

Perhatikan bahwa bagian `toolCall` dan `toolResponse` dalam permintaan dihitung ke dalam `prompt_token_count`. Karena langkah-langkah alat perantara ini kini terlihat dan ditampilkan kepada Anda, langkah-langkah tersebut merupakan bagian dari histori percakapan. Hal ini hanya berlaku untuk
kasus untuk *permintaan*, bukan *respons*.

Alat Google Penelusuran adalah pengecualian untuk aturan ini. Google Penelusuran sudah
menerapkan model harga sendiri di tingkat kueri, sehingga token tidak
dikenai biaya dua kali (lihat halaman [Harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id)).

Baca halaman [Token](https://ai.google.dev/gemini-api/docs/tokens?hl=id) untuk mengetahui informasi selengkapnya.

## Batasan

- Default ke mode `VALIDATED` (mode `AUTO` tidak didukung) saat tanda `include_server_side_tool_invocations` diaktifkan
- Alat bawaan seperti `google_search` mengandalkan informasi lokasi dan waktu saat ini, jadi jika `system_instruction` atau `function_declaration.description` Anda memiliki informasi lokasi dan waktu yang bertentangan, fitur kombinasi alat mungkin tidak berfungsi dengan baik.

## Alat yang didukung

Sirkulasi konteks alat standar berlaku untuk alat sisi server (bawaan).
Eksekusi Kode juga merupakan alat sisi server, tetapi memiliki solusi bawaan sendiri untuk sirkulasi konteks. Penggunaan Komputer dan panggilan fungsi adalah alat sisi klien, dan juga memiliki solusi bawaan untuk sirkulasi konteks.

| Alat | Sisi eksekusi | Dukungan Sirkulasi Konteks |
| --- | --- | --- |
| [Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id) | Sisi server | Didukung |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id) | Sisi server | Didukung |
| [Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id) | Sisi server | Didukung |
| [Penelusuran File](https://ai.google.dev/gemini-api/docs/file-search?hl=id) | Sisi server | Didukung |
| [Eksekusi Kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id) | Sisi server | Didukung (bawaan, menggunakan bagian `executableCode` dan `codeExecutionResult`) |
| [Penggunaan Komputer](https://ai.google.dev/gemini-api/docs/computer-use?hl=id) | Sisi klien | Didukung (bawaan, menggunakan bagian `functionCall` dan `functionResponse`) |
| [Fungsi kustom](https://ai.google.dev/gemini-api/docs/function-calling?hl=id) | Sisi klien | Didukung (bawaan, menggunakan bagian `functionCall` dan `functionResponse`) |

## Langkah berikutnya

- Pelajari lebih lanjut [Panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id) di Gemini API.
- Jelajahi alat yang didukung:
  - [Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id)
  - [Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id)
  - [Penelusuran File](https://ai.google.dev/gemini-api/docs/file-search?hl=id)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-08-26 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-08-26 UTC."],[],[]]
