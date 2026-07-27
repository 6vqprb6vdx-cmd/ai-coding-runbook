---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/computer-use?hl=id
fetched_at: 2026-07-27T04:33:58.659482+00:00
title: "Penggunaan Komputer \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Penggunaan Komputer

Alat Penggunaan Komputer memungkinkan Anda membuat agen kontrol browser, seluler, dan desktop yang berinteraksi dengan dan mengotomatiskan tugas. Dengan menggunakan screenshot, model dapat "melihat" layar komputer, dan "bertindak" dengan membuat tindakan UI tertentu seperti klik mouse dan input keyboard. Mirip dengan panggilan fungsi, Anda harus menerapkan lingkungan eksekusi sisi klien untuk menerima dan mengeksekusi tindakan Penggunaan Komputer.

Untuk mengetahui daftar model yang didukung, lihat [Versi model](#model-versions). Model Gemini 3.x mendukung beberapa kemampuan lanjutan:

- **Dukungan multi-lingkungan:** bangun agen untuk lingkungan [browser, seluler, dan desktop](#supported-environments).
- **Tindakan yang disederhanakan dengan maksud:** tindakan mencakup kolom `intent` yang menjelaskan alasan model di balik setiap langkah.
- **Kebijakan keamanan yang dapat dikonfigurasi:** sesuaikan [perilaku keamanan](#safety-policies) dengan kategori dan penggantian kebijakan bawaan.
- **Deteksi injeksi perintah:** aktifkan [pemindaian screenshot](#prompt-injection) untuk mendeteksi petunjuk berbahaya yang tersembunyi.

Dengan Penggunaan Komputer, Anda dapat membuat agen yang:

- Mengotomatiskan entri data atau pengisian formulir yang berulang di situs.
- Melakukan pengujian otomatis aplikasi web dan alur pengguna
- Melakukan riset di berbagai situs (misalnya, mengumpulkan informasi produk, harga, dan ulasan dari situs e-commerce untuk membantu pembelian)

Berikut adalah contoh minimal untuk mengaktifkan alat Penggunaan Komputer:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Search for 'Gemini API' on Google.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(
            computer_use=types.ComputerUse(
                environment=types.Environment.ENVIRONMENT_BROWSER,
            )
        )]
    )
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: 'gemini-3.6-flash',
  contents: "Search for 'Gemini API' on Google.",
  config: {
    tools: [{
      computerUse: {
        environment: "ENVIRONMENT_BROWSER",
      }
    }]
  }
});

console.log(response.text);
```

## Cara kerja Penggunaan Komputer

Untuk membuat agen dengan model Penggunaan Komputer, Anda perlu menyiapkan loop berkelanjutan antara aplikasi dan API. Berikut adalah fungsi kode Anda di setiap langkah:

1. [**Mengirim permintaan ke model**](#send-request)
   - Aplikasi Anda mengirimkan permintaan API yang berisi alat Penggunaan Komputer, setelan konfigurasi Anda (seperti lingkungan target), perintah pengguna, dan screenshot layar saat ini.
2. [**Menerima respons model**](#model-response)
   - Model menganalisis layar dan perintah, lalu menampilkan respons
     yang mencakup `function_call` yang disarankan yang merepresentasikan tindakan UI (seperti
     klik, scroll, atau penekanan tombol).
   - Untuk **model Gemini 3.x**, respons juga mencakup alasan `intent`
     yang menjelaskan mengapa model memilih tindakan tersebut.
   - Respons juga dapat mencakup `safety_decision` dari sistem keamanan internal yang mengklasifikasikan tindakan sebagai reguler/diizinkan, `require_confirmation` (memerlukan persetujuan pengguna), atau diblokir.
3. [**Jalankan tindakan yang diterima**](#execute-actions)
   - Jika tindakan diizinkan (atau pengguna mengonfirmasinya), kode
     sisi klien Anda akan mengurai `function_call`, menskalakan koordinat yang dinormalisasi agar sesuai
     dengan area tampilan, dan menjalankan tindakan di lingkungan target menggunakan
     alat otomatisasi (seperti Playwright). Jika tindakan diblokir, klien Anda harus menghentikan eksekusi atau menangani gangguan.
4. [**Merekam status lingkungan baru**](#capture-state)
   - Setelah tindakan selesai dieksekusi, aplikasi Anda akan mengambil screenshot baru dan mengirimkannya kembali ke model dalam `function_result` untuk meminta langkah berikutnya.

Kemudian, proses ini diulang dari langkah 2, terus-menerus meminta tindakan berikutnya
dari model hingga tugas selesai atau dihentikan.

![Ringkasan Penggunaan Komputer](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=id)

## Cara menerapkan Penggunaan Komputer

Sebelum membangun dengan alat Penggunaan Komputer, Anda harus menyiapkan:

- **Lingkungan eksekusi yang aman:** Jalankan agen Anda di VM atau container sandbox untuk mengisolasinya dari sistem host Anda dan membatasi potensi dampaknya.
  [Penerapan referensi](https://github.com/google/computer-use-preview/)
  mencakup sandbox berbasis Docker yang siap digunakan dan dapat Anda gunakan sebagai titik awal.
- **Handler tindakan sisi klien:** Terapkan logika sisi klien untuk menjalankan koordinat, mengetik teks, dan mengambil screenshot.

Contoh di bawah menggunakan browser web sebagai lingkungan eksekusi dan
[Playwright](https://playwright.dev/) sebagai handler sisi klien.

### 0. Menyiapkan Playwright

Pertama, instal paket yang diperlukan:

```
pip install google-genai playwright
playwright install chromium
```

Kemudian, inisialisasi instance browser Playwright untuk digunakan dalam eksekusi:

```
from playwright.sync_api import sync_playwright

# 1. Configure screen dimensions for the target environment
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# 2. Start the Playwright browser
# In production, utilize a sandboxed environment.
playwright = sync_playwright().start()
# Set headless=False to see the actions performed on your screen
browser = playwright.chromium.launch(headless=False)

# 3. Create a context and page with the specified dimensions
context = browser.new_context(
    viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT}
)
page = context.new_page()

# 4. Navigate to an initial page to start the task
page.goto("https://www.google.com")

# The 'page', 'SCREEN_WIDTH', and 'SCREEN_HEIGHT' variables
# will be used in the steps below.
```

### 1. Mengirim permintaan ke model

Lakukan inisialisasi library klien dan konfigurasi alat Penggunaan Komputer. Perhatikan bahwa tidak perlu menentukan ukuran tampilan saat mengeluarkan permintaan; model memprediksi koordinat piksel yang diskalakan ke tinggi dan lebar layar.

### Gemini 3.x

### Python

Gunakan `google-genai` Python SDK (versi `2.7.0` atau yang lebih tinggi) untuk mengonfigurasi permintaan yang menargetkan lingkungan browser:

```
from google import genai
from google.genai.types import (
    Content,
    Part,
    GenerateContentConfig,
    Tool,
    ComputerUse,
    Environment,
    ThinkingConfig,
)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        Content(
            role="user",
            parts=[
                Part(text="Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th"),
            ],
        )
    ],
    config=GenerateContentConfig(
        tools=[
            Tool(
                computer_use=ComputerUse(
                    environment=Environment.ENVIRONMENT_BROWSER,
                    enable_prompt_injection_detection=True,
                ),
            ),
        ],
        thinking_config=ThinkingConfig(
            include_thoughts=True
        ),
    )
)

print(response.text)
```

### JavaScript

Gunakan `@google/genai` Node.js SDK untuk mengonfigurasi permintaan yang menargetkan lingkungan browser:

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: 'gemini-3.6-flash',
  contents: [
    {
      role: 'user',
      parts: [{ text: "Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th" }]
    }
  ],
  config: {
    tools: [{
      computerUse: {
        environment: "ENVIRONMENT_BROWSER",
        enable_prompt_injection_detection: true
      }
    }],
    thinkingConfig: {
      includeThoughts: true
    }
  }
});

console.log(response.text);
```

### REST

Gunakan curl untuk mengirim permintaan:

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": {
          "text": "Find me a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th. Start by navigating directly to flights.google.com"
        }
      }
    ],
    "tools": [
      {
        "computer_use": {
          "environment": "ENVIRONMENT_BROWSER",
          "enable_prompt_injection_detection": true
        }
      }
    ]
  }'
```

### Gemini 2.5 (Versi Lama)

### Python

```
from google import genai
from google.genai import types
from google.genai.types import Content, Part

client = genai.Client()

# Specify predefined functions to exclude (optional)
excluded_functions = ["drag_and_drop"]

generate_content_config = genai.types.GenerateContentConfig(
    tools=[
        types.Tool(
            computer_use=types.ComputerUse(
                environment=types.Environment.ENVIRONMENT_BROWSER,
                excluded_predefined_functions=excluded_functions
                )
              ),
          ],
  )

contents=[
    Content(
        role="user",
        parts=[
            Part(text="Search for highly rated smart fridges on Google Shopping."),
        ],
    )
]

response = client.models.generate_content(
    model='gemini-2.5-computer-use-preview-10-2025',
    contents=contents,
    config=generate_content_config,
)

print(response)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

// Specify predefined functions to exclude (optional)
const excludedFunctions = ["drag_and_drop"];

const response = await ai.models.generateContent({
  model: 'gemini-2.5-computer-use-preview-10-2025',
  contents: [
    {
      role: 'user',
      parts: [{ text: "Search for highly rated smart fridges on Google Shopping." }]
    }
  ],
  config: {
    tools: [{
      computerUse: {
        environment: "ENVIRONMENT_BROWSER",
        excluded_predefined_functions: excludedFunctions
      }
    }]
  }
});

console.log(response);
```

### 2. Menerima respons model

Model respons menyarankan panggilan fungsi. Untuk **model Gemini 3.x**, respons berisi maksud penalaran yang disesuaikan bersama dengan koordinat. Berikut
contoh kedua respons:

### Gemini 3.x

```
{
  "function_call": {
    "name": "click",
    "args": {
      "x": 450,
      "y": 120,
      "intent": "Click the search box to type the destination."
    }
  }
}
```

### Gemini 2.5 (Versi Lama)

```
{
  "content": {
    "parts": [
      {
        "text": "I will type the search query into the search bar."
      },
      {
        "function_call": {
          "name": "type_text_at",
          "args": {
            "x": 371,
            "y": 470,
            "text": "highly rated smart fridges",
            "press_enter": true
          }
        }
      }
    ]
  }
}
```

### 3. Menjalankan tindakan yang diterima

Kode aplikasi Anda perlu mengurai respons model, menjalankan tindakan, dan mengumpulkan hasilnya.

Kode di bawah menangani perintah alat lama (`click_at`, `type_text_at`) dan perintah yang disederhanakan modern (`click`, `type`).

### Python

```
from typing import Any, List, Tuple
import time

def denormalize_x(x: int, screen_width: int) -> int:
    """Convert normalized x coordinate (0-1000) to actual pixel coordinate."""
    return int(x / 1000 * screen_width)

def denormalize_y(y: int, screen_height: int) -> int:
    """Convert normalized y coordinate (0-1000) to actual pixel coordinate."""
    return int(y / 1000 * screen_height)

def execute_function_calls(interaction, page, screen_width, screen_height):
    results = []
    function_calls = []

    # Parse content parts (Handling legacy and Gemini 3 response structures)
    parts = candidate.content.parts if hasattr(candidate, 'content') else []
    if not parts and hasattr(candidate, 'function_calls'):
        function_calls = candidate.function_calls
    else:
        for part in parts:
            if part.function_call:
                function_calls.append(part.function_call)

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.args
        print(f"  -> Executing: {fname} (Intent: {args.get('intent', 'N/A')})")

        try:
            if fname in ("open_web_browser", "open_app"):
                pass # Handled / already open
            elif fname in ("click", "click_at", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"):
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)

                if fname in ("click", "click_at"):
                    page.mouse.click(actual_x, actual_y)
                elif fname == "double_click":
                    page.mouse.dblclick(actual_x, actual_y)
                elif fname == "right_click":
                    page.mouse.click(actual_x, actual_y, button="right")
                elif fname == "middle_click":
                    page.mouse.click(actual_x, actual_y, button="middle")
                elif fname == "move":
                    page.mouse.move(actual_x, actual_y)
            elif fname in ("type", "type_text_at"):
                actual_x = denormalize_x(args["x"], screen_width) if "x" in args else None
                actual_y = denormalize_y(args["y"], screen_height) if "y" in args else None
                text = args["text"]
                press_enter = args.get("press_enter", False)

                if actual_x is not None and actual_y is not None:
                    page.mouse.click(actual_x, actual_y)
                # Clear field first
                page.keyboard.press("Meta+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(text)
                if press_enter:
                    page.keyboard.press("Enter")
            elif fname == "navigate":
                page.goto(args["url"])
            elif fname == "go_back":
                page.go_back()
            elif fname == "go_forward":
                page.go_forward()
            elif fname == "wait":
                time.sleep(args.get("seconds", 1))
            else:
                print(f"Warning: Custom or unhandled function {fname}")

            page.wait_for_load_state(timeout=5000)
            time.sleep(1)

        except Exception as e:
            print(f"Error executing {fname}: {e}")
            action_result = {"error": str(e)}

        results.append((fname, function_call.id, action_result))

    return results
```

### JavaScript

```
function denormalizeX(x, screenWidth) {
    // Convert normalized x coordinate (0-1000) to actual pixel coordinate.
    return Math.floor((x / 1000) * screenWidth);
}

function denormalizeY(y, screenHeight) {
    // Convert normalized y coordinate (0-1000) to actual pixel coordinate.
    return Math.floor((y / 1000) * screenHeight);
}

async function executeFunctionCalls(candidate, page, screenWidth, screenHeight) {
    const results = [];
    let functionCalls = [];

    // Parse function calls from candidate response
    const parts = candidate.content?.parts || [];
    if (parts.length === 0 && candidate.functionCalls) {
        functionCalls = candidate.functionCalls;
    } else {
        for (const part of parts) {
            if (part.functionCall) {
                functionCalls.push(part.functionCall);
            }
        }
    }

    for (const functionCall of functionCalls) {
        const actionResult = {};
        const fname = functionCall.name;
        const args = functionCall.args;
        console.log(`  -> Executing: ${fname} (Intent: ${args.intent || 'N/A'})`);

        try {
            if (fname === "open_web_browser" || fname === "open_app") {
                // Handled / already open
            } else if (["click", "click_at", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"].includes(fname)) {
                const actualX = denormalizeX(args.x, screenWidth);
                const actualY = denormalizeY(args.y, screenHeight);

                if (fname === "click" || fname === "click_at") {
                    await page.mouse.click(actualX, actualY);
                } else if (fname === "double_click") {
                    await page.mouse.dblclick(actualX, actualY);
                } else if (fname === "right_click") {
                    await page.mouse.click(actualX, actualY, { button: "right" });
                } else if (fname === "middle_click") {
                    await page.mouse.click(actualX, actualY, { button: "middle" });
                } else if (fname === "move") {
                    await page.mouse.move(actualX, actualY);
                }
            } else if (fname === "type" || fname === "type_text_at") {
                const actualX = args.x !== undefined ? denormalizeX(args.x, screenWidth) : null;
                const actualY = args.y !== undefined ? denormalizeY(args.y, screenHeight) : null;
                const text = args.text;
                const pressEnter = args.press_enter || false;

                if (actualX !== null && actualY !== null) {
                    await page.mouse.click(actualX, actualY);
                }
                // Clear field first
                await page.keyboard.press("Meta+A");
                await page.keyboard.press("Backspace");
                await page.keyboard.type(text);
                if (pressEnter) {
                    await page.keyboard.press("Enter");
                }
            } else if (fname === "navigate") {
                await page.goto(args.url);
            } else if (fname === "go_back") {
                await page.goBack();
            } else if (fname === "go_forward") {
                await page.goForward();
            } else if (fname === "wait") {
                await new Promise(resolve => setTimeout(resolve, (args.seconds || 1) * 1000));
            } else {
                console.log(`Warning: Custom or unhandled function ${fname}`);
            }

            await page.waitForLoadState('load', { timeout: 5000 }).catch(() => {});
            await new Promise(resolve => setTimeout(resolve, 1000));
        } catch (e) {
            console.log(`Error executing ${fname}: ${e}`);
            actionResult.error = e.message;
        }

        results.push([fname, functionCall.id, actionResult]);
    }

    return results;
}
```

### 4. Merekam status lingkungan baru

Merekam representasi layar dan menampilkannya ke model.

### Python

```
def get_function_responses(page, results):
    screenshot_bytes = page.screenshot(type="png")
    current_url = page.url
    function_responses = []
    for name, call_id, result in results:
        function_responses.append({
            "type": "function_result",
            "name": name,
            "call_id": call_id,
            "result": [
                {
                    "type": "text",
                    "text": json.dumps({"url": current_url, **result})
                },
                {
                    "type": "image",
                    "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
                    "mime_type": "image/png"
                }
            ]
        })
    return function_responses
```

### JavaScript

```
async function getFunctionResponses(page, results) {
    const screenshotBuffer = await page.screenshot({ type: 'png' });
    const screenshotBase64 = screenshotBuffer.toString('base64');
    const currentUrl = page.url();
    const functionResponses = [];

    for (const [name, callId, result] of results) {
        functionResponses.push({
            type: "function_result",
            name: name,
            call_id: callId,
            result: [
                {
                    type: "text",
                    text: JSON.stringify({ url: currentUrl, ...result })
                },
                {
                    type: "image",
                    data: screenshotBase64,
                    mime_type: "image/png"
                }
            ]
        });
    }
    return functionResponses;
}
```

Setelah menentukan cara merekam dan memformat status lingkungan, Anda dapat menggabungkan semua langkah ini ke dalam loop eksekusi berkelanjutan.

## Membangun loop agen

Untuk mengaktifkan interaksi multi-langkah, gabungkan empat langkah dari bagian [Cara menerapkan Penggunaan Komputer](#implement-computer-use) menjadi satu loop. Loop ini terus meminta tindakan dan mengirimkan kembali hasilnya ke model hingga tugas selesai.

Jangan lupa untuk mengelola histori percakapan dengan benar dengan menambahkan respons model dan respons fungsi Anda ke histori di setiap langkah.

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright
from google import genai
from google.genai import types

client = genai.Client()

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

print("Initializing browser...")
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT})
page = context.new_page()

# Paste helper functions execute_function_calls and get_function_responses here

try:
    page.goto("https://ai.google.dev/gemini-api/docs")

    config = types.GenerateContentConfig(
        tools=[types.Tool(computer_use=types.ComputerUse(
            environment=types.Environment.ENVIRONMENT_BROWSER,
            enable_prompt_injection_detection=True
        ))],
        thinking_config=types.ThinkingConfig(include_thoughts=True),
    )

    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    contents = [
        types.Content(role="user", parts=[
            types.Part(text=USER_PROMPT),
            types.Part.from_bytes(data=initial_screenshot, mime_type='image/png')
        ])
    ]

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")
        print("Thinking...")
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=contents,
            config=config,
        )

        candidate = response.candidates[0]
        contents.append(candidate.content)

        has_function_calls = any(part.function_call for part in candidate.content.parts)
        if not has_function_calls:
            text_response = " ".join(
                part.text for part in candidate.content.parts if hasattr(part, 'text')
            )
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(candidate, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        contents.append(
            types.Content(role="user", parts=[types.Part(function_response=fr) for fr in function_responses])
        )

finally:
    print("Closing browser...")
    browser.close()
    playwright.stop()
```

### JavaScript

```
import { chromium } from 'playwright';
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

// Constants for screen dimensions
const SCREEN_WIDTH = 1440;
const SCREEN_HEIGHT = 900;

console.log("Initializing browser...");
const browser = await chromium.launch({ headless: false });
const context = await browser.newContext({
    viewport: { width: SCREEN_WIDTH, height: SCREEN_HEIGHT }
});
const page = await context.newPage();

// Define helper functions. Copy/paste from steps 3 and 4:
// function denormalizeX(...)
// function denormalizeY(...)
// async function executeFunctionCalls(...)
// async function getFunctionResponses(...)

try {
    await page.goto("https://ai.google.dev/gemini-api/docs");

    const config = {
        tools: [{
            computerUse: {
                environment: "ENVIRONMENT_BROWSER",
                enable_prompt_injection_detection: true
            }
        }],
        thinkingConfig: { includeThoughts: true }
    };

    const initialScreenshotBuffer = await page.screenshot({ type: 'png' });
    const initialScreenshotBase64 = initialScreenshotBuffer.toString('base64');
    const USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing.";
    console.log(`Goal: ${USER_PROMPT}`);

    const contents = [
        {
            role: "user",
            parts: [
                { text: USER_PROMPT },
                {
                    inlineData: {
                        data: initialScreenshotBase64,
                        mimeType: "image/png"
                    }
                }
            ]
        }
    ];

    // Agent Loop
    const turnLimit = 5;
    for (let i = 0; i < turnLimit; i++) {
        console.log(`\n--- Turn ${i + 1} ---`);
        console.log("Thinking...");
        const response = await ai.models.generateContent({
            model: 'gemini-3.6-flash',
            contents: contents,
            config: config
        });

        const candidate = response.candidates[0];
        contents.push(candidate.content);

        const hasFunctionCalls = candidate.content.parts.some(part => part.functionCall);
        if (!hasFunctionCalls) {
            const textResponse = candidate.content.parts
                .filter(part => part.text)
                .map(part => part.text)
                .join(" ");
            console.log("Agent finished:", textResponse);
            break;
        }

        console.log("Executing actions...");
        const results = await executeFunctionCalls(candidate, page, SCREEN_WIDTH, SCREEN_HEIGHT);

        console.log("Capturing state...");
        const functionResponses = await getFunctionResponses(page, results);

        contents.push({
            role: "user",
            parts: functionResponses.map(fr => ({
                ...fr
            }))
        });
    }
} finally {
    console.log("Closing browser...");
    await browser.close();
}
```

## Lingkungan yang didukung (Gemini 3.x)

Model Gemini 3.x mendukung tiga lingkungan yang ditentukan dalam konfigurasi `computer_use`:

### Lingkungan browser (`ENVIRONMENT_BROWSER`)

Tindakan Action di bagian alat browser:

| Nama perintah | Deskripsi | Argumen (dalam panggilan fungsi) |
| --- | --- | --- |
| **click** | Klik kiri pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | Klik dua kali pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | Klik tiga kali pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | Klik tengah pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | Klik kanan pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | Menekan dan menahan tombol mouse pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | Melepaskan tombol mouse pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **pindah** | Memindahkan kursor ke posisi yang ditentukan. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **jenis** | Mengetik teks. | `text`: str `press_enter`: bool (Opsional, default `false`) `intent`: str |
| **drag\_and\_drop** | Menarik item dari koordinat awal ke koordinat akhir. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | Menjeda eksekusi selama jumlah detik yang ditentukan. | `seconds`: int (Opsional, default `1`) `intent`: str |
| **press\_key** | Menekan tombol yang ditentukan, lalu melepaskannya. | `key`: str `intent`: str |
| **key\_down** | Menekan dan menahan tombol yang ditentukan. | `key`: str `intent`: str |
| **key\_up** | Melepaskan kunci yang ditentukan. | `key`: str `intent`: str |
| **tombol pintas** | Menekan kombinasi tombol yang ditentukan. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | Menampilkan screenshot layar saat ini. | `intent`: str |
| **scroll** | Men-scroll ke atas, bawah, kiri, atau kanan pada koordinat dengan jarak piksel. | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, Opsional, default `300`) `intent`: str |
| **go\_back** | Kembali ke halaman web sebelumnya dalam histori browser. | `intent`: str |
| **navigate** | Membuka langsung URL tertentu. | `url`: str `intent`: str |
| **go\_forward** | Membuka halaman web berikutnya dalam histori browser. | `intent`: str |

### Lingkungan seluler (`ENVIRONMENT_MOBILE`)

Tindakan lingkungan yang dioptimalkan untuk Android:

| Nama perintah | Deskripsi | Argumen (dalam panggilan fungsi) |
| --- | --- | --- |
| **open\_app** | Membuka aplikasi berdasarkan namanya. | `app_name`: str `intent`: str |
| **click** | Klik kiri pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **list\_apps** | Mencantumkan aplikasi yang tersedia di perangkat, menampilkan nama dan nama paketnya. | `intent`: str |
| **wait** | Menjeda eksekusi selama jumlah detik yang ditentukan. | `seconds`: int (Opsional, default `1`) `intent`: str |
| **go\_back** | Kembali ke layar atau halaman web sebelumnya. | `intent`: str |
| **jenis** | Mengetik teks. | `text`: str `press_enter`: bool (Opsional, default `false`) `intent`: str |
| **drag\_and\_drop** | Menarik item dari koordinat awal ke koordinat akhir. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **long\_press** | Melakukan tekan lama pada koordinat di layar. | `y`: int (0-999) `x`: int (0-999) `seconds`: int (Opsional, default `2`) `intent`: str |
| **press\_key** | Menekan tombol yang ditentukan, lalu melepaskannya. | `key`: str `intent`: str |
| **take\_screenshot** | Menampilkan screenshot layar saat ini. | `intent`: str |

### Lingkungan desktop (`ENVIRONMENT_DESKTOP`)

Perintah kursor tingkat OS lingkungan desktop:

| Nama perintah | Deskripsi | Argumen (dalam panggilan fungsi) |
| --- | --- | --- |
| **click** | Klik kiri pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | Klik dua kali pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | Klik tiga kali pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | Klik tengah pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | Klik kanan pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | Menekan dan menahan tombol mouse pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | Melepaskan tombol mouse pada koordinat. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **pindah** | Memindahkan kursor ke posisi yang ditentukan. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **jenis** | Mengetik teks. | `text`: str `press_enter`: bool (Opsional, default `false`) `intent`: str |
| **drag\_and\_drop** | Menarik item dari koordinat awal ke koordinat akhir. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | Menjeda eksekusi selama jumlah detik yang ditentukan. | `seconds`: int (Opsional, default `1`) `intent`: str |
| **press\_key** | Menekan tombol yang ditentukan, lalu melepaskannya. | `key`: str `intent`: str |
| **key\_down** | Menekan dan menahan tombol yang ditentukan. | `key`: str `intent`: str |
| **key\_up** | Melepaskan kunci yang ditentukan. | `key`: str `intent`: str |
| **tombol pintas** | Menekan kombinasi tombol yang ditentukan. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | Menampilkan screenshot layar saat ini. | `intent`: str |
| **scroll** | Men-scroll ke atas, bawah, kiri, atau kanan pada koordinat dengan jarak piksel. | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, Opsional, default `300`) `intent`: str |

## Tindakan UI yang Didukung Lama (Gemini 2.5)

Untuk model lama (`gemini-2.5-computer-use-preview-10-2025`), tindakan berikut didukung:

| Nama perintah | Deskripsi | Argumen (dalam panggilan fungsi) | Contoh panggilan fungsi |
| --- | --- | --- | --- |
| **open\_web\_browser** | Membuka browser web. | Tidak ada | `{"name": "open_web_browser", "args": {}}` |
| **wait\_5\_seconds** | Menjeda eksekusi selama 5 detik. | Tidak ada | `{"name": "wait_5_seconds", "args": {}}` |
| **go\_back** | Membuka halaman sebelumnya dalam histori. | Tidak ada | `{"name": "go_back", "args": {}}` |
| **go\_forward** | Membuka halaman berikutnya dalam histori. | Tidak ada | `{"name": "go_forward", "args": {}}` |
| **search** | Membuka mesin telusur default. | Tidak ada | `{"name": "search", "args": {}}` |
| **navigate** | Membuka URL yang ditentukan secara langsung di browser. | `url`: str | `{"name": "navigate", "args": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | Mengklik pada koordinat tertentu. | `y`: int (0-999), `x`: int (0-999) | `{"name": "click_at", "args": {"y": 300, "x": 500}}` |
| **hover\_at** | Mengarahkan kursor ke koordinat tertentu. | `y`: int (0-999), `x`: int (0-999) | `{"name": "hover_at", "args": {"y": 150, "x": 250}}` |
| **type\_text\_at** | Mengetik teks pada koordinat. | `y`: int (0-999), `x`: int (0-999), `text`: str, `press_enter`: bool (Opsional, default Benar), `clear_before_typing`: bool (Opsional, default Benar) | `{"name": "type_text_at", "args": {"y": 250, "x": 400, "text": "search", "press_enter": false}}` |
| **key\_combination** | Tekan tombol atau kombinasi tombol. | `keys`: str | `{"name": "key_combination", "args": {"keys": "Control+A"}}` |
| **scroll\_document** | Men-scroll seluruh halaman web. | `direction`: str | `{"name": "scroll_document", "args": {"direction": "down"}}` |
| **scroll\_at** | Men-scroll di koordinat (x,y). | `y`: int, `x`: int, `direction`: str, `magnitude`: int (Opsional, default 800) | `{"name": "scroll_at", "args": {"y": 500, "x": 500, "direction": "down"}}` |
| **drag\_and\_drop** | Menarik di antara dua koordinat. | `y`: int, `x`: int, `destination_y`: int, `destination_x`: int | `{"name": "drag_and_drop", "args": {"y": 100, "destination_y": 500, "destination_x": 500, "x": 100}}` |

## Fungsi kustom yang ditentukan pengguna

Anda dapat memperluas fungsi model dengan menyertakan fungsi kustom yang ditentukan pengguna. Misalnya, dalam skenario human-in-the-loop (HITL), Anda dapat mengecualikan tindakan default yang telah ditentukan sebelumnya dan mendaftarkan tindakan kustom.

#### Alat Kustom Gemini 3.x

### Python

Mengecualikan tindakan browser standar yang telah ditentukan sebelumnya (seperti `click`) dan mendaftarkan alat `yield_to_user` kustom:

```
from google import genai
from google.genai import types

client = genai.Client()

yield_to_user_tool = types.FunctionDeclaration(
    name="yield_to_user",
    description="Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.",
    parameters=types.Schema(
        type="OBJECT",
        properties={
            "reason": types.Schema(
                type="STRING",
                description="The reason why the agent is yielding control to the human."
            )
        },
        required=["reason"]
    )
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Click the submit button. If you need a second factor authentication code, ask me.",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment="ENVIRONMENT_MOBILE",
                    excluded_predefined_functions=["click"]
                )
            ),
            yield_to_user_tool
        ]
    )
)
```

#### Alat Kustom Gemini 2.5 (Versi Lama)

### Python

```
from typing import Optional, Dict, Any
from google import genai
from google.genai import types

client = genai.Client()

# Define custom tools here
custom_functions = [...] # Describe parameters as FunctionDeclaration object

def make_generate_content_config():
    excluded_functions = ["open_web_browser", "wait_5_seconds", "go_back", "go_forward", "search", "navigate", "hover_at", "scroll_document", "key_combination", "drag_and_drop"]
    generate_content_config = types.GenerateContentConfig(
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment=types.Environment.ENVIRONMENT_BROWSER,
                    excluded_predefined_functions=excluded_functions
                )
            ),
            types.Tool(function_declarations=custom_functions)
        ]
    )
    return generate_content_config
```

## Mengelola tingkat penalaran (Gemini 3.x)

Untuk agen penggunaan komputer, Anda dapat mengonfigurasi tingkat pemikiran yang berbeda untuk menyeimbangkan kualitas tindakan dan kecepatan eksekusi. Tingkat pemikiran yang lebih rendah umumnya mencapai keseimbangan yang baik untuk tugas otomatisasi standar.

## Keselamatan dan keamanan

### Mengonfigurasi kebijakan keamanan (Gemini 3.x)

Model Gemini 3.x mencakup kategori layanan keamanan bawaan yang secara otomatis menentukan apakah konfirmasi pengguna diperlukan.

| Kategori kebijakan keselamatan | Deskripsi |
| --- | --- |
| `FINANCIAL_TRANSACTIONS` | Memblokir atau memicu konfirmasi untuk tindakan yang melibatkan pembayaran, checkout retail, atau barang yang diatur oleh hukum. |
| `SENSITIVE_DATA_MODIFICATION` | Melindungi catatan kesehatan, keuangan, atau pemerintah dari modifikasi yang tidak sah. |
| `COMMUNICATION_TOOL` | Membatasi agen agar tidak mengirim email, pesan chat, atau draf secara mandiri. |
| `ACCOUNT_CREATION` | Membatasi agen agar tidak mendaftarkan akun baru secara mandiri di situs. |
| `DATA_MODIFICATION` | Mengatur modifikasi sistem file secara keseluruhan, berbagi data, dan penghapusan penyimpanan. |
| `USER_CONSENT_MANAGEMENT` | Memerlukan pengambilalihan pengguna untuk banner izin cookie dan dialog privasi. |
| `LEGAL_TERMS_AND_AGREEMENTS` | Mencegah model menerima Persyaratan Layanan atau kontrak yang mengikat secara hukum secara mandiri. |

#### Penggantian keamanan

Anda dapat mengganti kebijakan tertentu dengan meneruskan penggantian:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Clean up the local folder by archiving old logs.",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment=types.Environment.ENVIRONMENT_DESKTOP,
                    disabled_safety_policies=[
                        types.SafetyPolicy.DATA_MODIFICATION
                    ]
                )
            )
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: 'gemini-3.6-flash',
  contents: "Clean up the local folder by archiving old logs.",
  config: {
    tools: [{
      computerUse: {
        environment: "ENVIRONMENT_DESKTOP",
        disabledSafetyPolicies: [
          "DATA_MODIFICATION"
        ]
      }
    }]
  }
});
```

### Deteksi injeksi perintah (Gemini 3.x)

Mekanisme keamanan keikutsertaan yang memindai piksel screenshot untuk mendeteksi petunjuk perintah berbahaya yang tersembunyi (misalnya, "Abaikan perintah sebelumnya") dan memblokir eksekusi saat terdeteksi.

### Mengonfirmasi keputusan keamanan

Respons dapat menyertakan parameter `safety_decision` dalam argumen panggilan fungsi:

```
{
  "function_call": {
    "name": "click_at",
    "args": {
      "x": 60,
      "y": 100,
      "safety_decision": {
        "explanation": "Must check check-box",
        "decision": "require_confirmation"
      }
    }
  }
}
```

Jika `safety_decision` adalah `require_confirmation`, minta pengguna akhir. Jika
pengguna mengonfirmasi, tetapkan `safety_acknowledgement` di `FunctionResponse`.

### Python

```
def get_safety_confirmation(safety_decision):
    # Prompt user for confirmation
    print(f"Safety confirmation required: {safety_decision.get('explanation', '')}")
    return "CONTINUE" # Or TERMINATE

# Inside execute_function_calls, check for safety_decision:
if 'safety_decision' in function_call.args:
    decision = get_safety_confirmation(function_call.args['safety_decision'])
    if decision == "TERMINATE":
        break
    # Include safety_acknowledgement inside the action result
    action_result["safety_acknowledgement"] = True
```

### Praktik terbaik keamanan

Penggunaan Komputer menimbulkan risiko keamanan dan operasional yang unik, karena model yang bertindak atas nama pengguna dapat menemukan konten yang tidak tepercaya di layar atau melakukan kesalahan dalam menjalankan tindakan. Terapkan praktik terbaik berikut untuk melindungi data dan sistem pengguna:

1. **Human-in-the-Loop (HITL):**

   - **Menerapkan konfirmasi pengguna:** Jika respons keselamatan menunjukkan
     `require_confirmation` (atau keputusan keselamatan lama memerlukannya), minta persetujuan pengguna.
   - **Memberikan petunjuk keamanan kustom:** Terapkan petunjuk sistem kustom untuk menentukan dan menerapkan batas keamanan Anda sendiri. Contoh:

     ### Python

     ```
     from google import genai
     from google.genai import types

     system_instruction = """
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**
     * **For Consequential Actions:** Perform all preparatory steps (e.g., navigating,
       filling out forms, typing a message). You will ask for confirmation **AFTER**
       all necessary information is entered on the screen, but **BEFORE** you perform
       the final, irreversible action (e.g., before clicking "Send", "Submit",
       "Confirm Purchase", "Share").
     * **For Prohibited Actions:** If the action is strictly forbidden (e.g., accepting
       legal terms, solving a CAPTCHA), you must first inform the user about the
       required action and ask for their confirmation to proceed.

     **USER_CONFIRMATION Categories:**

     *   **Consent and Agreements:** You are FORBIDDEN from accepting, selecting, or
         agreeing to any of the following on the user's behalf. You must ask the
         user to confirm before performing these actions.
         *   Terms of Service
         *   Privacy Policies
         *   Cookie consent banners
         *   End User License Agreements (EULAs)
         *   Any other legally significant contracts or agreements.
     *   **Robot Detection:** You MUST NEVER attempt to solve or bypass the
         following. You must ask the user to confirm before performing these actions.
         *   CAPTCHAs (of any kind)
         *   Any other anti-robot or human-verification mechanisms, even if you are
             capable.
     *   **Financial Transactions:**
         *   Completing any purchase.
         *   Managing or moving money (e.g., transfers, payments).
         *   Purchasing regulated goods or participating in gambling.
     *   **Sending Communications:**
         *   Sending emails.
         *   Sending messages on any platform (e.g., social media, chat apps).
         *   Posting content on social media or forums.
     *   **Accessing or Modifying Sensitive Information:**
         *   Health, financial, or government records (e.g., medical history, tax
             forms, passport status).
         *   Revealing or modifying sensitive personal identifiers (e.g., SSN, bank
             account number, credit card number).
     *   **User Data Management:**
         *   Accessing, downloading, or saving files from the web.
         *   Sharing or sending files/data to any third party.
         *   Transferring user data between systems.
     *   **Browser Data Usage:**
         *   Accessing or managing Chrome browsing history, bookmarks, autofill data,
             or saved passwords.
     *   **Security and Identity:**
         *   Logging into any user account.
         *   Any action that involves misrepresentation or impersonation (e.g.,
             creating a fan account, posting as someone else).
     *   **Insurmountable Obstacles:** If you are technically unable to interact with
         a user interface element or are stuck in a loop you cannot resolve, ask the
         user to take over.
     ---

     ## **RULE 2: Default Behavior (ACTUATE)**

     If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`,
     your default behavior is to **Actuate**.

     **Actuation Means:**  You MUST proactively perform all necessary steps to move
     the user's request forward. Continue to actuate until you either complete the
     non-consequential task or encounter a condition defined in Rule 1.

     *   **Example 1:** If asked to send money, you will navigate to the payment
         portal, enter the recipient's details, and enter the amount. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Send" button.
     *   **Example 2:** If asked to post a message, you will navigate to the site,
         open the post composition window, and write the full message. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Post" button.

         After the user has confirmed, remember to get the user's latest screen
         before continuing to perform actions.

     # Final Response Guidelines:
     Write final response to the user in the following cases:
     - User confirmation
     - When the task is complete or you have enough information to respond to the user
     """

     client = genai.Client()
     response = client.models.generate_content(
         model="gemini-3.6-flash",
         contents="Prepare a draft but do not send.",
         config=types.GenerateContentConfig(
             system_instruction=system_instruction,
             tools=[types.Tool(computer_use=types.ComputerUse(environment="ENVIRONMENT_BROWSER"))]
         )
     )
     ```

     ### JavaScript

     ```
     import { GoogleGenAI } from '@google/genai';

     const ai = new GoogleGenAI();

     const systemInstruction = `
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**
     * **For Consequential Actions:** Perform all preparatory steps (e.g., navigating,
       filling out forms, typing a message). You will ask for confirmation **AFTER**
       all necessary information is entered on the screen, but **BEFORE** you perform
       the final, irreversible action (e.g., before clicking "Send", "Submit",
       "Confirm Purchase", "Share").
     * **For Prohibited Actions:** If the action is strictly forbidden (e.g., accepting
       legal terms, solving a CAPTCHA), you must first inform the user about the
       required action and ask for their confirmation to proceed.

     **USER_CONFIRMATION Categories:**

     *   **Consent and Agreements:** You are FORBIDDEN from accepting, selecting, or
         agreeing to any of the following on the user's behalf. You must ask the
         user to confirm before performing these actions.
         *   Terms of Service
         *   Privacy Policies
         *   Cookie consent banners
         *   End User License Agreements (EULAs)
         *   Any other legally significant contracts or agreements.
     *   **Robot Detection:** You MUST NEVER attempt to solve or bypass the
         following. You must ask the user to confirm before performing these actions.
         *   CAPTCHAs (of any kind)
         *   Any other anti-robot or human-verification mechanisms, even if you are
             capable.
     *   **Financial Transactions:**
         *   Compleying any purchase.
         *   Managing or moving money (e.g., transfers, payments).
         *   Purchasing regulated goods or participating in gambling.
     *   **Sending Communications:**
         *   Sending emails.
         *   Sending messages on any platform (e.g., social media, chat apps).
         *   Posting content on social media or forums.
     *   **Accessing or Modifying Sensitive Information:**
         *   Health, financial, or government records (e.g., medical history, tax
             forms, passport status).
         *   Revealing or modifying sensitive personal identifiers (e.g., SSN, bank
             account number, credit card number).
     *   **User Data Management:**
         *   Accessing, downloading, or saving files from the web.
         *   Sharing or sending files/data to any third party.
         *   Transferring user data between systems.
     *   **Browser Data Usage:**
         *   Accessing or managing Chrome browsing history, bookmarks, autofill data,
             or saved passwords.
     *   **Security and Identity:**
         *   Logging into any user account.
         *   Any action that involves misrepresentation or impersonation (e.g.,
             creating a fan account, posting as someone else).
     *   **Insurmountable Obstacles:** If you are technically unable to interact with
         a user interface element or are stuck in a loop you cannot resolve, ask the
         user to take over.
     ---

     ## **RULE 2: Default Behavior (ACTUATE)**

     If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`,
     your default behavior is to **Actuate**.

     **Actuation Means:**  You MUST proactively perform all necessary steps to move
     the user's request forward. Continue to actuate until you either complete the
     non-consequential task or encounter a condition defined in Rule 1.

     *   **Example 1:** If asked to send money, you will navigate to the payment
         portal, enter the recipient's details, and enter the amount. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Send" button.
     *   **Example 2:** If asked to post a message, you will navigate to the site,
         open the post composition window, and write the full message. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Post" button.

         After the user has confirmed, remember to get the user's latest screen
         before continuing to perform actions.

     # Final Response Guidelines:
     Write final response to the user in the following cases:
     - User confirmation
     - When the task is complete or you have enough information to respond to the user
     `;

     const response = await ai.models.generateContent({
       model: 'gemini-3.6-flash',
       contents: "Prepare a draft but do not send.",
       config: {
         systemInstruction: systemInstruction,
         tools: [{
           computerUse: {
             environment: "ENVIRONMENT_BROWSER"
           }
         }]
       }
     });
     ```
2. **Lingkungan eksekusi yang aman:** Jalankan agen Anda di lingkungan yang aman dan sandbox untuk membatasi potensi dampaknya. Hal ini dapat berupa mesin virtual (VM) sandbox, container (misalnya, Docker), atau profil browser khusus dengan izin terbatas. Lihat
   [implementasi referensi GitHub](https://github.com/google/computer-use-preview/)
   untuk panduan penyiapan sandbox menggunakan Docker.
3. **Pembersihan input:** Bersihkan semua teks buatan pengguna dalam perintah untuk
   memitigasi risiko perintah yang tidak diinginkan atau injeksi perintah. Ini adalah lapisan keamanan yang berguna, tetapi bukan pengganti lingkungan eksekusi yang aman.
4. **Pembatasan konten:** Gunakan pembatasan dan API keamanan konten untuk mengevaluasi input pengguna, input dan output alat, serta respons agen untuk kesesuaian, deteksi injeksi perintah, dan jailbreak.
5. **Daftar yang diizinkan dan daftar yang tidak diizinkan:** Terapkan mekanisme pemfilteran untuk mengontrol ke mana model dapat membuka dan apa yang dapat dilakukannya. Daftar situs yang dilarang adalah titik awal yang baik, sementara daftar yang diizinkan yang lebih ketat akan lebih aman.
6. **Observabilitas dan logging:** Pertahankan log mendetail untuk proses debug, audit, dan respons insiden. Klien Anda harus mencatat perintah, screenshot, tindakan yang disarankan model (`function_call`), respons keamanan, dan semua tindakan yang akhirnya dilakukan oleh klien.
7. **Pengelolaan lingkungan:** Pastikan lingkungan GUI konsisten.
   Pop-up, notifikasi, atau perubahan tata letak yang tidak terduga dapat membingungkan model. Mulai dari status bersih yang diketahui untuk setiap tugas baru jika memungkinkan.

## Versi model

Anda dapat menggunakan Penggunaan Komputer dengan model berikut:

- [**Gemini 3.6 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=id) (`gemini-3.6-flash`): Model yang direkomendasikan untuk penggunaan komputer, yang menampilkan tindakan yang disederhanakan dengan maksud, dukungan untuk lingkungan browser, seluler, dan desktop, kebijakan keamanan yang dapat dikonfigurasi, dan deteksi injeksi perintah.
- [**Gemini 3.5 Flash-Lite**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=id) (`gemini-3.5-flash-lite`): Model hemat biaya dengan latensi rendah yang mendukung penggunaan komputer.
- [**Gemini 3.5 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=id) (`gemini-3.5-flash`): Model stabil sebelumnya yang mendukung penggunaan komputer.
- [**Pratinjau Gemini 3 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=id) (`gemini-3-flash-preview`): Model pratinjau yang mendukung penggunaan komputer.
- [**Gemini 2.5 (Pratinjau Lama)**](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025?hl=id) (`gemini-2.5-computer-use-preview-10-2025`): Model pratinjau lama yang dioptimalkan untuk penggunaan komputer berbasis browser.

## Langkah berikutnya

- Bereksperimen dengan Penggunaan Komputer di [lingkungan demo Browserbase](http://gemini.browserbase.com).
- Lihat [Implementasi referensi](https://github.com/google/computer-use-preview) untuk melihat contoh kode.
- Pelajari alat Gemini API lainnya:
  - [Pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)
  - [Grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/grounding?hl=id)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-23 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-23 UTC."],[],[]]
