---
source_url: https://ai.google.dev/gemini-api/docs/computer-use?hl=id
fetched_at: 2026-06-01T19:48:24.065360+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Penggunaan Komputer

Penggunaan Komputer memungkinkan Anda membuat agen kontrol browser yang berinteraksi dengan dan mengotomatiskan tugas. Dengan menggunakan screenshot, model dapat "melihat" layar komputer, dan "bertindak" dengan membuat tindakan UI tertentu seperti klik mouse dan input keyboard. Mirip dengan panggilan fungsi, Anda perlu menulis kode aplikasi sisi klien untuk menerima dan mengeksekusi tindakan Penggunaan Komputer.

Dengan Penggunaan Komputer, Anda dapat membuat agen yang:

- Mengotomatiskan entri data atau pengisian formulir yang berulang di situs.
- Melakukan pengujian otomatis aplikasi web dan alur pengguna
- Melakukan riset di berbagai situs (misalnya, mengumpulkan informasi produk, harga, dan ulasan dari situs e-commerce untuk membantu pengambilan keputusan pembelian)

Cara termudah untuk menguji kemampuan Penggunaan Komputer adalah melalui [implementasi
referensi](https://github.com/google/computer-use-preview/) atau
[lingkungan demo Browserbase](http://gemini.browserbase.com).

## Cara kerja Penggunaan Komputer

Untuk membuat agen kontrol browser dengan model Penggunaan Komputer, terapkan loop agen yang melakukan hal berikut:

1. [**Mengirim permintaan ke model**](#send-request)

   - Tambahkan alat Penggunaan Komputer dan secara opsional fungsi yang ditentukan pengguna kustom atau fungsi yang dikecualikan ke permintaan API Anda.
   - Berikan perintah pada model Penggunaan Komputer dengan permintaan pengguna.
2. [**Menerima respons model**](#model-response)

   - Model Penggunaan Komputer menganalisis permintaan dan screenshot pengguna, lalu membuat respons yang mencakup `function_call` yang disarankan yang merepresentasikan tindakan UI (misalnya, "klik di koordinat (x,y)" atau "ketik 'text'"). Untuk deskripsi semua tindakan UI yang didukung oleh model Penggunaan Komputer, lihat [Tindakan yang didukung](#supported-actions).
   - Respons API juga dapat menyertakan `safety_decision` dari sistem keamanan internal yang memeriksa tindakan yang diusulkan model. `safety_decision` ini mengklasifikasikan tindakan sebagai:
     - **Reguler / diizinkan:** Tindakan ini dianggap aman. Hal ini juga dapat
       ditunjukkan dengan tidak adanya `safety_decision`.
     - **Memerlukan konfirmasi (`require_confirmation`):** Model akan melakukan tindakan
       yang mungkin berisiko (misalnya, mengklik "banner setuju cookie").
3. [**Menjalankan tindakan yang diterima**](#execute-actions)

   - Kode sisi klien Anda menerima `function_call` dan `safety_decision` yang menyertainya.
     - **Reguler / diizinkan:** Jika `safety_decision` menunjukkan reguler/diizinkan (atau jika tidak ada `safety_decision`), kode sisi klien Anda dapat mengeksekusi `function_call` yang ditentukan di lingkungan target Anda (misalnya, browser web).
     - **Memerlukan konfirmasi:** Jika `safety_decision` menunjukkan
       memerlukan konfirmasi, aplikasi Anda harus meminta konfirmasi dari pengguna akhir
       sebelum menjalankan `function_call`. Jika pengguna
       mengonfirmasi, lanjutkan untuk menjalankan tindakan. Jika pengguna menolak, jangan
       jalankan tindakan.
4. [**Merekam status lingkungan baru**](#capture-state)

   - Jika tindakan telah dieksekusi, klien Anda akan mengambil screenshot baru GUI dan URL saat ini untuk dikirim kembali ke model Penggunaan Komputer sebagai bagian dari `function_response`.
   - Jika tindakan diblokir oleh sistem keamanan atau konfirmasi ditolak oleh
     pengguna, aplikasi Anda dapat mengirimkan bentuk masukan yang berbeda ke
     model atau mengakhiri interaksi.

Proses ini berulang dari langkah 2 dengan model yang menggunakan screenshot baru dan sasaran yang sedang berlangsung untuk menyarankan tindakan berikutnya. Loop berlanjut
hingga tugas selesai, terjadi error, atau proses dihentikan
(misalnya, karena respons keamanan "blokir" atau keputusan pengguna).

![Penggunaan Komputer
Gambaran umum](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=id)

## Cara menerapkan Penggunaan Komputer

Sebelum membangun dengan alat Penggunaan Komputer, Anda harus menyiapkan hal-hal berikut:

- **Lingkungan eksekusi yang aman:** Untuk alasan keamanan, Anda harus menjalankan agen Penggunaan Komputer di lingkungan yang aman dan terkontrol (misalnya, mesin virtual sandbox, penampung, atau profil browser khusus dengan izin terbatas).
- **Handler tindakan sisi klien:** Anda harus menerapkan logika sisi klien
  untuk menjalankan tindakan yang dihasilkan oleh model dan
  mengambil screenshot lingkungan setelah setiap tindakan.

Contoh di bagian ini menggunakan browser sebagai lingkungan eksekusi dan [Playwright](https://playwright.dev/) sebagai pengendali tindakan sisi klien. Untuk
menjalankan contoh ini, Anda harus menginstal dependensi yang diperlukan dan melakukan inisialisasi instance browser
Playwright.

#### Menginstal Playwright

```
    pip install google-genai playwright
    playwright install chromium
```

#### Lakukan inisialisasi instance browser Playwright

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

Kode contoh untuk memperluas ke lingkungan Android disertakan di bagian [Menggunakan fungsi yang ditentukan pengguna kustom](#custom-functions).

### 1. Mengirim permintaan ke model

Tambahkan alat Penggunaan Komputer ke permintaan API Anda dan kirim perintah ke model
yang menyertakan tujuan pengguna. Anda harus menggunakan salah satu model yang didukung Penggunaan Komputer atau Anda akan mendapatkan error:

- `gemini-2.5-computer-use-preview-10-2025`
- `gemini-3-flash-preview`

Anda juga dapat menambahkan parameter berikut secara opsional:

- **Tindakan yang dikecualikan:** Jika ada tindakan dari daftar [Tindakan UI yang didukung](#supported-actions) yang tidak ingin Anda lakukan oleh model, tentukan tindakan ini sebagai `excluded_predefined_functions`.
- **Fungsi yang ditentukan pengguna:** Selain alat Penggunaan Komputer, Anda mungkin ingin menyertakan fungsi kustom yang ditentukan pengguna.

Perhatikan bahwa tidak perlu menentukan ukuran layar saat mengirimkan permintaan;
model memprediksi koordinat piksel yang diskalakan ke tinggi dan lebar
layar.

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
        # 1. Computer Use tool with browser environment
        types.Tool(
            computer_use=types.ComputerUse(
                environment=types.Environment.ENVIRONMENT_BROWSER,
                # Optional: Exclude specific predefined functions
                excluded_predefined_functions=excluded_functions
                )
              ),
        # 2. Optional: Custom user-defined functions
        #types.Tool(
          # function_declarations=custom_functions
          #   )
          ],
  )

# Create the content with user message
contents=[
    Content(
        role="user",
        parts=[
            Part(text="Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout."),
        ],
    )
]

# Generate content with the configured settings
response = client.models.generate_content(
    model='gemini-2.5-computer-use-preview-10-2025',
    contents=contents,
    config=generate_content_config,
)

# Print the response output
print(response)
```

Untuk contoh dengan fungsi kustom, lihat [Menggunakan fungsi
yang ditentukan pengguna kustom](#custom-functions).

### 2. Menerima respons model

Jika alat Penggunaan Komputer diaktifkan, model akan merespons dengan satu atau beberapa
`FunctionCalls` jika menentukan bahwa tindakan UI diperlukan untuk menyelesaikan tugas.
Penggunaan Komputer mendukung panggilan fungsi paralel, yang berarti model dapat menampilkan
beberapa tindakan dalam satu giliran.

Berikut adalah contoh respons model.

```
{
  "content": {
    "parts": [
      {
        "text": "I will type the search query into the search bar. The search bar is in the center of the page."
      },
      {
        "function_call": {
          "name": "type_text_at",
          "args": {
            "x": 371,
            "y": 470,
            "text": "highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping",
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

Contoh kode di bawah mengekstrak panggilan fungsi dari respons model Penggunaan Komputer, dan menerjemahkannya menjadi tindakan yang dapat dieksekusi dengan Playwright.
Model menghasilkan koordinat yang dinormalisasi (0-999) terlepas dari dimensi gambar input, sehingga bagian dari langkah terjemahan adalah mengonversi kembali koordinat yang dinormalisasi ini ke nilai piksel sebenarnya.

Ukuran layar yang direkomendasikan untuk digunakan dengan model Penggunaan Komputer adalah (1440, 900). Model ini akan berfungsi dengan resolusi apa pun, meskipun kualitas hasilnya dapat terpengaruh.

Perhatikan bahwa contoh ini hanya mencakup penerapan untuk 3 tindakan UI yang paling umum: `open_web_browser`, `click_at`, dan `type_text_at`. Untuk
kasus penggunaan produksi, Anda harus menerapkan semua tindakan UI lainnya dari daftar
[Tindakan yang didukung](#supported-actions) kecuali jika Anda menambahkannya secara eksplisit sebagai
`excluded_predefined_functions`.

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

def execute_function_calls(candidate, page, screen_width, screen_height):
    results = []
    function_calls = []
    for part in candidate.content.parts:
        if part.function_call:
            function_calls.append(part.function_call)

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.args
        print(f"  -> Executing: {fname}")

        try:
            if fname == "open_web_browser":
                pass # Already open
            elif fname == "click_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                page.mouse.click(actual_x, actual_y)
            elif fname == "type_text_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                text = args["text"]
                press_enter = args.get("press_enter", False)

                page.mouse.click(actual_x, actual_y)
                # Simple clear (Command+A, Backspace for Mac)
                page.keyboard.press("Meta+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(text)
                if press_enter:
                    page.keyboard.press("Enter")
            else:
                print(f"Warning: Unimplemented or custom function {fname}")

            # Wait for potential navigations/renders
            page.wait_for_load_state(timeout=5000)
            time.sleep(1)

        except Exception as e:
            print(f"Error executing {fname}: {e}")
            action_result = {"error": str(e)}

        results.append((fname, action_result))

    return results
```

### 4. Merekam status lingkungan baru

Setelah menjalankan tindakan, kirim hasil eksekusi fungsi kembali ke model agar model dapat menggunakan informasi ini untuk membuat tindakan berikutnya. Jika
beberapa tindakan (panggilan paralel) dijalankan, Anda harus mengirim
`FunctionResponse` untuk setiap tindakan dalam giliran pengguna berikutnya.

### Python

```
def get_function_responses(page, results):
    screenshot_bytes = page.screenshot(type="png")
    current_url = page.url
    function_responses = []
    for name, result in results:
        response_data = {"url": current_url}
        response_data.update(result)
        function_responses.append(
            types.FunctionResponse(
                name=name,
                response=response_data,
                parts=[types.FunctionResponsePart(
                        inline_data=types.FunctionResponseBlob(
                            mime_type="image/png",
                            data=screenshot_bytes))
                ]
            )
        )
    return function_responses
```

## Membangun loop agen

Untuk mengaktifkan interaksi multi-langkah, gabungkan empat langkah dari bagian [Cara menerapkan Penggunaan Komputer](#implement-computer-use) ke dalam loop.
Jangan lupa untuk mengelola histori percakapan dengan benar dengan menambahkan respons model dan respons fungsi Anda.

Untuk menjalankan contoh kode ini, Anda harus:

- Instal [dependensi Playwright yang diperlukan](#expandable-1).
- Tentukan fungsi helper dari langkah [(3) Jalankan tindakan yang diterima](#execute-actions) dan [(4) Ambil status lingkungan baru](#capture-state).

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright

from google import genai
from google.genai import types
from google.genai.types import Content, Part

client = genai.Client()

# Constants for screen dimensions
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# Setup Playwright
print("Initializing browser...")
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT})
page = context.new_page()

# Define helper functions. Copy/paste from steps 3 and 4
# def denormalize_x(...)
# def denormalize_y(...)
# def execute_function_calls(...)
# def get_function_responses(...)

try:
    # Go to initial page
    page.goto("https://ai.google.dev/gemini-api/docs")

    # Configure the model (From Step 1)
    config = types.GenerateContentConfig(
        tools=[types.Tool(computer_use=types.ComputerUse(
            environment=types.Environment.ENVIRONMENT_BROWSER
        ))],
        thinking_config=types.ThinkingConfig(include_thoughts=True),
    )

    # Initialize history
    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    contents = [
        Content(role="user", parts=[
            Part(text=USER_PROMPT),
            Part.from_bytes(data=initial_screenshot, mime_type='image/png')
        ])
    ]

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")
        print("Thinking...")
        response = client.models.generate_content(
            model='gemini-2.5-computer-use-preview-10-2025',
            contents=contents,
            config=config,
        )

        candidate = response.candidates[0]
        contents.append(candidate.content)

        has_function_calls = any(part.function_call for part in candidate.content.parts)
        if not has_function_calls:
            text_response = " ".join([part.text for part in candidate.content.parts if part.text])
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(candidate, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        contents.append(
            Content(role="user", parts=[Part(function_response=fr) for fr in function_responses])
        )

finally:
    # Cleanup
    print("\nClosing browser...")
    browser.close()
    playwright.stop()
```

## Menggunakan fungsi kustom yang ditentukan pengguna

Secara opsional, Anda dapat menyertakan fungsi kustom yang ditentukan pengguna dalam permintaan untuk memperluas fungsi model. Contoh di bawah mengadaptasi model dan alat Penggunaan Komputer untuk kasus penggunaan seluler dengan menyertakan tindakan kustom yang ditentukan pengguna seperti `open_app`, `long_press_at`, dan `go_home`, sekaligus mengecualikan tindakan khusus browser. Model dapat memanggil fungsi kustom ini secara cerdas bersama dengan tindakan UI standar untuk menyelesaikan tugas di lingkungan non-browser.

### Python

```
from typing import Optional, Dict, Any

from google import genai
from google.genai import types
from google.genai.types import Content, Part

client = genai.Client()

SYSTEM_PROMPT = """You are operating an Android phone. Today's date is October 15, 2023, so ignore any other date provided.
* To provide an answer to the user, *do not use any tools* and output your answer on a separate line. IMPORTANT: Do not add any formatting or additional punctuation/text, just output the answer by itself after two empty lines.
* Make sure you scroll down to see everything before deciding something isn't available.
* You can open an app from anywhere. The icon doesn't have to currently be on screen.
* Unless explicitly told otherwise, make sure to save any changes you make.
* If text is cut off or incomplete, scroll or click into the element to get the full text before providing an answer.
* IMPORTANT: Complete the given task EXACTLY as stated. DO NOT make any assumptions that completing a similar task is correct.  If you can't find what you're looking for, SCROLL to find it.
* If you want to edit some text, ONLY USE THE `type` tool. Do not use the onscreen keyboard.
* Quick settings shouldn't be used to change settings. Use the Settings app instead.
* The given task may already be completed. If so, there is no need to do anything.
"""

def open_app(app_name: str, intent: Optional[str] = None) -> Dict[str, Any]:
    """Opens an app by name.

    Args:
        app_name: Name of the app to open (any string).
        intent: Optional deep-link or action to pass when launching, if the app supports it.

    Returns:
        JSON payload acknowledging the request (app name and optional intent).
    """
    return {"status": "requested_open", "app_name": app_name, "intent": intent}

def long_press_at(x: int, y: int) -> Dict[str, int]:
    """Long-press at a specific screen coordinate.

    Args:
        x: X coordinate (absolute), scaled to the device screen width (pixels).
        y: Y coordinate (absolute), scaled to the device screen height (pixels).

    Returns:
        Object with the coordinates pressed and the duration used.
    """
    return {"x": x, "y": y}

def go_home() -> Dict[str, str]:
    """Navigates to the device home screen.

    Returns:
        A small acknowledgment payload.
    """
    return {"status": "home_requested"}

#  Build function declarations
CUSTOM_FUNCTION_DECLARATIONS = [
    types.FunctionDeclaration.from_callable(client=client, callable=open_app),
    types.FunctionDeclaration.from_callable(client=client, callable=long_press_at),
    types.FunctionDeclaration.from_callable(client=client, callable=go_home),
]

#Exclude browser functions
EXCLUDED_PREDEFINED_FUNCTIONS = [
    "open_web_browser",
    "search",
    "navigate",
    "hover_at",
    "scroll_document",
    "go_forward",
    "key_combination",
    "drag_and_drop",
]

#Utility function to construct a GenerateContentConfig
def make_generate_content_config() -> genai.types.GenerateContentConfig:
    """Return a fixed GenerateContentConfig with Computer Use + custom functions."""
    return genai.types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment=types.Environment.ENVIRONMENT_BROWSER,
                    excluded_predefined_functions=EXCLUDED_PREDEFINED_FUNCTIONS,
                )
            ),
            types.Tool(function_declarations=CUSTOM_FUNCTION_DECLARATIONS),
        ],
    )

# Create the content with user message
contents: list[Content] = [
    Content(
        role="user",
        parts=[
            # text instruction
            Part(text="Open Chrome, then long-press at 200,400."),
        ],
    )
]

# Build your fixed config (from helper)
config = make_generate_content_config()

# Generate content with the configured settings
response = client.models.generate_content(
        model='gemini-2.5-computer-use-preview-10-2025',
        contents=contents,
        config=config,
    )

print(response)
```

## Tindakan UI yang didukung

Model dapat meminta tindakan UI berikut melalui
`FunctionCall`. Kode sisi klien Anda harus menerapkan logika eksekusi untuk
tindakan ini. Lihat [implementasi
referensi](https://github.com/google/computer-use-preview) untuk
contoh.

| Command Name | Deskripsi | Argumen (dalam Panggilan Fungsi) | Contoh Panggilan Fungsi |
| --- | --- | --- | --- |
| **open\_web\_browser** | Membuka browser web. | Tidak ada | `{"name": "open_web_browser", "args": {}}` |
| **wait\_5\_seconds** | Menjeda eksekusi selama 5 detik untuk memungkinkan konten dinamis dimuat atau animasi selesai. | Tidak ada | `{"name": "wait_5_seconds", "args": {}}` |
| **go\_back** | Membuka halaman sebelumnya dalam histori browser. | Tidak ada | `{"name": "go_back", "args": {}}` |
| **go\_forward** | Membuka halaman berikutnya dalam histori browser. | Tidak ada | `{"name": "go_forward", "args": {}}` |
| **search** | Membuka halaman beranda mesin telusur default (misalnya, Google). Berguna untuk memulai tugas penelusuran baru. | Tidak ada | `{"name": "search", "args": {}}` |
| **navigate** | Membuka URL yang ditentukan secara langsung di browser. | `url`: str | `{"name": "navigate", "args": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | Mengklik pada koordinat tertentu di halaman web. Nilai x dan y didasarkan pada petak 1000x1000 dan diskalakan ke dimensi layar. | `y`: int (0-999), `x`: int (0-999) | `{"name": "click_at", "args": {"y": 300, "x": 500}}` |
| **hover\_at** | Mengarahkan kursor ke koordinat tertentu di halaman web. Berguna untuk menampilkan sub-menu. x dan y didasarkan pada petak 1000x1000. | `y`: int (0-999) `x`: int (0-999) | `{"name": "hover_at", "args": {"y": 150, "x": 250}}` |
| **type\_text\_at** | Mengetik teks pada koordinat tertentu, secara default menghapus kolom terlebih dahulu dan menekan ENTER setelah mengetik, tetapi tindakan ini dapat dinonaktifkan. x dan y didasarkan pada petak 1000x1000. | `y`: int (0-999), `x`: int (0-999), `text`: str, `press_enter`: bool (Opsional, default Benar), `clear_before_typing`: bool (Opsional, default Benar) | `{"name": "type_text_at", "args": {"y": 250, "x": 400, "text": "search query", "press_enter": false}}` |
| **key\_combination** | Tekan tombol atau kombinasi tombol keyboard, seperti "Control+C" atau "Enter". Berguna untuk memicu tindakan (seperti mengirimkan formulir dengan "Enter") atau operasi papan klip. | `keys`: str (misalnya, 'enter', 'control+c'). | `{"name": "key_combination", "args": {"keys": "Control+A"}}` |
| **scroll\_document** | Men-scroll seluruh halaman web "ke atas", "ke bawah", "ke kiri", atau "ke kanan". | `direction`: str ("up", "down", "left", atau "right") | `{"name": "scroll_document", "args": {"direction": "down"}}` |
| **scroll\_at** | Men-scroll elemen atau area tertentu pada koordinat (x, y) ke arah yang ditentukan dengan besaran tertentu. Koordinat dan besaran (default 800) didasarkan pada petak 1000x1000. | `y`: int (0-999), `x`: int (0-999), `direction`: str ("up", "down", "left", "right"), `magnitude`: int (0-999, Opsional, default 800) | `{"name": "scroll_at", "args": {"y": 500, "x": 500, "direction": "down", "magnitude": 400}}` |
| **drag\_and\_drop** | Menarik elemen dari koordinat awal (x, y) dan meletakkannya di koordinat tujuan (destination\_x, destination\_y). Semua koordinat didasarkan pada petak 1000x1000. | `y`: int (0-999), `x`: int (0-999), `destination_y`: int (0-999), `destination_x`: int (0-999) | `{"name": "drag_and_drop", "args": {"y": 100, "x": 100, "destination_y": 500, "destination_x": 500}}` |

## Keselamatan dan keamanan

### Mengonfirmasi keputusan keamanan

Bergantung pada tindakan, respons model juga dapat menyertakan
`safety_decision` dari sistem keamanan internal yang memeriksa tindakan yang diusulkan model.

```
{
  "content": {
    "parts": [
      {
        "text": "I have evaluated step 2. It seems Google detected unusual traffic and is asking me to verify I'm not a robot. I need to click the 'I'm not a robot' checkbox located near the top left (y=98, x=95).",
      },
      {
        "function_call": {
          "name": "click_at",
          "args": {
            "x": 60,
            "y": 100,
            "safety_decision": {
              "explanation": "I have encountered a CAPTCHA challenge that requires interaction. I need you to complete the challenge by clicking the 'I'm not a robot' checkbox and any subsequent verification steps.",
              "decision": "require_confirmation"
            }
          }
        }
      }
    ]
  }
}
```

Jika `safety_decision` adalah `require_confirmation`, Anda harus meminta pengguna akhir untuk mengonfirmasi sebelum melanjutkan pelaksanaan tindakan. Berdasarkan
[persyaratan layanan](https://ai.google.dev/gemini-api/terms?hl=id), Anda tidak diizinkan
melewati permintaan konfirmasi manusia.

Contoh kode ini meminta konfirmasi pengguna akhir sebelum menjalankan
tindakan. Jika pengguna tidak mengonfirmasi tindakan, loop akan berakhir. Jika
pengguna mengonfirmasi tindakan, tindakan akan dijalankan dan
kolom `safety_acknowledgement` ditandai sebagai `True`.

### Python

```
import termcolor

def get_safety_confirmation(safety_decision):
    """Prompt user for confirmation when safety check is triggered."""
    termcolor.cprint("Safety service requires explicit confirmation!", color="red")
    print(safety_decision["explanation"])

    decision = ""
    while decision.lower() not in ("y", "n", "ye", "yes", "no"):
        decision = input("Do you wish to proceed? [Y]es/[N]o\n")

    if decision.lower() in ("n", "no"):
        return "TERMINATE"
    return "CONTINUE"

def execute_function_calls(candidate, page, screen_width, screen_height):

    # ... Extract function calls from response ...

    for function_call in function_calls:
        extra_fr_fields = {}

        # Check for safety decision
        if 'safety_decision' in function_call.args:
            decision = get_safety_confirmation(function_call.args['safety_decision'])
            if decision == "TERMINATE":
                print("Terminating agent loop")
                break
            extra_fr_fields["safety_acknowledgement"] = "true" # Safety acknowledgement

        # ... Execute function call and append to results ...
```

Jika pengguna mengonfirmasi, Anda harus menyertakan konfirmasi keselamatan dalam `FunctionResponse` Anda.

### Python

```
function_response_parts.append(
    FunctionResponse(
        name=name,
        response={"url": current_url,
                  **extra_fr_fields},  # Include safety acknowledgement
        parts=[
            types.FunctionResponsePart(
                inline_data=types.FunctionResponseBlob(
                    mime_type="image/png", data=screenshot
                )
             )
           ]
         )
       )
```

### Praktik terbaik keamanan

Penggunaan Komputer adalah alat baru yang menimbulkan risiko baru yang harus diperhatikan oleh developer:

- **Konten yang tidak tepercaya & penipuan:** Saat mencoba mencapai tujuan pengguna, model mungkin mengandalkan sumber informasi dan petunjuk yang tidak tepercaya dari layar. Misalnya, jika sasaran pengguna adalah membeli ponsel Pixel dan model menemukan penipuan "Pixel Gratis jika Anda menyelesaikan survei", ada kemungkinan model akan menyelesaikan survei.
- **Tindakan yang tidak disengaja sesekali:** Model dapat salah menafsirkan tujuan pengguna atau konten halaman web, sehingga menyebabkan model melakukan tindakan yang salah seperti mengklik tombol yang salah atau mengisi formulir yang salah. Hal ini dapat menyebabkan kegagalan tugas atau
  ekstraksi data.
- **Pelanggaran kebijakan:** Kemampuan API dapat diarahkan, baik
  secara sengaja maupun tidak sengaja, ke aktivitas yang melanggar kebijakan
  Google ([Kebijakan Penggunaan Terlarang untuk AI Generatif](https://policies.google.com/terms/generative-ai/use-policy?hl=id) dan
  [Persyaratan Layanan Tambahan Gemini API](https://ai.google.dev/gemini-api/terms?hl=id). Hal ini mencakup tindakan yang dapat mengganggu integritas sistem, membahayakan keamanan, melewati langkah-langkah keamanan, mengontrol perangkat medis, dll.

Untuk mengatasi risiko ini, Anda dapat menerapkan langkah-langkah keamanan dan praktik terbaik berikut:

1. **Human-in-the-Loop (HITL):**

   - **Terapkan konfirmasi pengguna:** Jika respons keamanan menunjukkan
     `require_confirmation`, Anda harus menerapkan konfirmasi pengguna sebelum
     eksekusi. Lihat [Mengonfirmasi keputusan keamanan](#safety-decisions) untuk
     contoh kode.
   - **Memberikan petunjuk keamanan kustom:** Selain pemeriksaan konfirmasi pengguna bawaan, developer dapat secara opsional menambahkan [petunjuk sistem](https://ai.google.dev/gemini-api/docs/text-generation?hl=id#system-instructions) kustom yang menerapkan kebijakan keamanan mereka sendiri, baik untuk memblokir tindakan model tertentu atau mewajibkan konfirmasi pengguna sebelum model melakukan tindakan tidak dapat diubah yang berisiko tinggi. Berikut adalah contoh instruksi sistem keamanan kustom yang dapat Anda sertakan saat berinteraksi dengan model.

     #### Contoh petunjuk keselamatan

     Tetapkan aturan keamanan kustom Anda sebagai petunjuk sistem:

     ```
         ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

         This is your first and most important check. If the next required action falls
         into any of the following categories, you MUST stop immediately, and seek the
         user's explicit permission.

         **Procedure for Seeking Confirmation:**  * **For Consequential Actions:**
         Perform all preparatory steps (e.g., navigating, filling out forms, typing a
         message). You will ask for confirmation **AFTER** all necessary information is
         entered on the screen, but **BEFORE** you perform the final, irreversible action
         (e.g., before clicking "Send", "Submit", "Confirm Purchase", "Share").  * **For
         Prohibited Actions:** If the action is strictly forbidden (e.g., accepting legal
         terms, solving a CAPTCHA), you must first inform the user about the required
         action and ask for their confirmation to proceed.

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
     ```
2. **Lingkungan eksekusi yang aman:** Jalankan agen Anda di lingkungan sandbox yang aman untuk membatasi potensi dampaknya (misalnya, Virtual machine (VM) dalam sandbox, container (misalnya, Docker), atau profil browser khusus dengan izin terbatas).
3. **Pembersihan input:** Bersihkan semua teks buatan pengguna dalam perintah untuk
   memitigasi risiko perintah yang tidak diinginkan atau injeksi perintah. Ini adalah lapisan keamanan yang berguna, tetapi bukan pengganti lingkungan eksekusi yang aman.
4. **Batasan konten:** Gunakan batasan dan [API keamanan konten](https://ai.google.dev/gemma/docs/shieldgemma?hl=id) untuk mengevaluasi input pengguna, input dan output alat, respons agen untuk kesesuaian, injeksi perintah, dan deteksi pelarian dari batasan.
5. **Daftar yang diizinkan dan daftar yang tidak diizinkan:** Terapkan mekanisme pemfilteran untuk mengontrol
   ke mana model dapat membuka dan apa yang dapat dilakukannya. Daftar situs yang tidak diizinkan
   adalah titik awal yang baik, sementara daftar yang diizinkan yang lebih ketat
   bahkan lebih aman.
6. **Observabilitas dan logging:** Pertahankan log mendetail untuk proses debug, audit, dan respons insiden. Klien Anda harus mencatat perintah, screenshot, tindakan yang disarankan model (function\_call), respons keamanan, dan semua tindakan yang akhirnya dieksekusi oleh klien.
7. **Pengelolaan lingkungan:** Pastikan lingkungan GUI konsisten.
   Pop-up, notifikasi, atau perubahan tata letak yang tidak terduga dapat membingungkan model. Mulai dari status bersih yang diketahui untuk setiap tugas baru jika memungkinkan.

## Versi model

Perhatikan bahwa `gemini-3-flash-preview` memiliki dukungan bawaan untuk Penggunaan Komputer; Anda tidak memerlukan model terpisah untuk mengakses alat ini.

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | **Gemini API**  `gemini-2.5-computer-use-preview-10-2025` |
| saveJenis data yang didukung | **Input**  Gambar, teks  **Output**  Teks |
| token\_autoBatas token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=id) | **Batas token input**  128.000  **Batas token output**  64.000 |
| Versi 123 | Baca [pola versi model](https://ai.google.dev/gemini-api/docs/models/gemini?hl=id#model-versions) untuk mengetahui detail selengkapnya.  - Pratinjau: `gemini-2.5-computer-use-preview-10-2025` |
| calendar\_monthPembaruan terbaru | Oktober 2025 |

## Langkah berikutnya

- Bereksperimen dengan Penggunaan Komputer di lingkungan [demo Browserbase](http://gemini.browserbase.com).
- Lihat [Implementasi
  referensi](https://github.com/google/computer-use-preview) untuk contoh
  kode.
- Pelajari alat Gemini API lainnya:
  - [Panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)
  - [Melakukan grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/grounding?hl=id)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-01 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-01 UTC."],[],[]]
