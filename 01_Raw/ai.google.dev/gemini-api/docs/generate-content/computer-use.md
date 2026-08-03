---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/computer-use?hl=it
fetched_at: 2026-08-03T04:32:12.767793+00:00
title: "Uso del computer \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Uso del computer

Lo strumento Utilizzo del computer ti consente di creare agenti di controllo per browser, dispositivi mobili e computer
che interagiscono con le attività e le automatizzano. Utilizzando gli screenshot, il modello può "vedere" uno schermo del computer e "agire" generando azioni specifiche della UI come clic del mouse e input da tastiera. Analogamente alla chiamata di funzioni, devi implementare l'ambiente di esecuzione lato client per ricevere ed eseguire le azioni di Utilizzo del computer.

Per l'elenco dei modelli supportati, consulta [Versioni dei modelli](#model-versions). I modelli Gemini 3.x supportano diverse funzionalità avanzate:

- **Supporto multi-ambiente**:crea agenti per ambienti [browser, mobile e desktop](#supported-environments).
- Le **azioni semplificate con intent** includono un campo `intent` che spiega il ragionamento del modello alla base di ogni passaggio.
- **Policy di sicurezza configurabili**:perfeziona il [comportamento di sicurezza](#safety-policies) con categorie e override delle policy integrate.
- **Rilevamento di prompt injection**:attiva la [scansione degli screenshot](#prompt-injection) per rilevare istruzioni avversarie nascoste.

Con Utilizzo del computer, puoi creare agenti che:

- Automatizza l'inserimento di dati ripetitivi o la compilazione di moduli sui siti web.
- Eseguire test automatici di applicazioni web e flussi utente
- Eseguire ricerche su vari siti web (ad es. raccogliere informazioni, prezzi e recensioni sui prodotti da siti di e-commerce per informare un acquisto)

Ecco un esempio minimo di attivazione dello strumento Utilizzo del computer:

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

## Come funziona Uso del computer

Per creare un agente con il modello Computer Use, devi configurare un
ciclo continuo tra la tua applicazione e l'API. Ecco cosa farà il tuo codice
in ogni passaggio:

1. [**Invia una richiesta al modello**](#send-request)
   - La tua applicazione invia una richiesta API contenente lo strumento Utilizzo del computer,
     le impostazioni di configurazione (come l'ambiente di destinazione), il prompt dell'utente e uno screenshot della schermata corrente.
2. [**Ricevi la risposta del modello**](#model-response)
   - Il modello analizza lo schermo e il prompt, restituendo una risposta
     che include un `function_call` suggerito che rappresenta un'azione dell'interfaccia utente (ad esempio
     un clic, uno scorrimento o una sequenza di tasti).
   - Per i **modelli Gemini 3.x**, la risposta include anche un ragionamento `intent`
     che spiega perché il modello ha scelto quell'azione.
   - La risposta può includere anche un `safety_decision` di un sistema di sicurezza interno che classifica l'azione come regolare/consentita, `require_confirmation` (che richiede l'approvazione dell'utente) o bloccata.
3. [**Esegui l'azione ricevuta**](#execute-actions)
   - Se l'azione è consentita (o l'utente la conferma), il codice lato client analizza `function_call`, ridimensiona le coordinate normalizzate in modo che corrispondano alla finestra e esegue l'azione nell'ambiente di destinazione utilizzando strumenti di automazione (come Playwright). Se l'azione è bloccata, il
     client deve interrompere l'esecuzione o gestire l'interruzione.
4. [**Acquisizione del nuovo stato dell'ambiente**](#capture-state)
   - Al termine dell'esecuzione dell'azione, l'applicazione acquisisce un nuovo
     screenshot e lo invia di nuovo al modello in un `function_result` per
     richiedere il passaggio successivo.

Questo processo si ripete quindi dal passaggio 2, sollecitando continuamente l'azione successiva dal modello finché l'attività non viene completata o interrotta.

![Panoramica di Uso del computer](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=it)

## Come implementare l'uso del computer

Prima di creare con lo strumento Utilizzo del computer, devi configurare:

- **Ambiente di esecuzione sicuro**:esegui l'agente in una VM o in un container sandbox per isolarlo dal sistema host e limitarne il potenziale impatto.
  L'[implementazione di riferimento](https://github.com/google/computer-use-preview/)
  include una sandbox basata su Docker pronta all'uso che puoi utilizzare come punto di partenza.
- **Gestore di azioni lato client:** implementa la logica lato client per eseguire le coordinate, digitare il testo e acquisire screenshot.

Gli esempi riportati di seguito utilizzano un browser web come ambiente di esecuzione e
[Playwright](https://playwright.dev/) come gestore lato client.

### 0. Configurare Playwright

Innanzitutto, installa i pacchetti richiesti:

```
pip install google-genai playwright
playwright install chromium
```

Quindi, inizializza un'istanza del browser Playwright da utilizzare per l'esecuzione:

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

### 1. Inviare una richiesta al modello

Inizializza la libreria client e configura lo strumento Utilizzo del computer. Tieni presente che non è necessario specificare le dimensioni di visualizzazione quando invii una richiesta. Il modello prevede le coordinate dei pixel scalate in base all'altezza e alla larghezza dello schermo.

### Gemini 3.x

### Python

Utilizza l'SDK Python `google-genai` (versione `2.7.0` o successive) per configurare una richiesta che ha come target l'ambiente del browser:

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

Utilizza l'SDK Node.js `@google/genai` per configurare una richiesta che ha come target l'ambiente browser:

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

Utilizza curl per inviare una richiesta:

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

### Gemini 2.5 (legacy)

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

### 2. Ricevere la risposta del modello

Il modello di risposta suggerisce una chiamata di funzione. Per i **modelli Gemini 3.x**, la
risposta contiene un intent di ragionamento personalizzato insieme alle coordinate. Di seguito sono riportati esempi di entrambe le risposte:

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

### Gemini 2.5 (legacy)

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

### 3. Esegui le azioni ricevute

Il codice dell'applicazione deve analizzare la risposta del modello, eseguire le azioni
e raccogliere i risultati.

Il codice riportato di seguito gestisce sia i comandi degli strumenti legacy (`click_at`, `type_text_at`) sia i comandi moderni semplificati (`click`, `type`).

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

### 4. Acquisire il nuovo stato dell'ambiente

Acquisire una rappresentazione dello schermo e restituirla al modello.

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

Una volta definito come acquisire e formattare lo stato dell'ambiente, puoi combinare tutti questi passaggi in un ciclo di esecuzione continuo.

## Crea un loop dell'agente

Per attivare le interazioni in più passaggi, combina i quattro passaggi della sezione [Come implementare l'utilizzo del computer](#implement-computer-use) in un unico ciclo. Questo ciclo continua a richiedere azioni e a restituire i risultati al modello finché l'attività non viene completata.

Ricorda di gestire correttamente la cronologia della conversazione aggiungendo sia le risposte del modello sia le risposte della funzione alla cronologia a ogni passaggio.

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

## Ambienti supportati (Gemini 3.x)

I modelli Gemini 3.x supportano tre ambienti specificati nelle configurazioni `computer_use`:

### Ambiente browser (`ENVIRONMENT_BROWSER`)

Azioni di azione nello strumento del browser:

| Nome comando | Descrizione | Argomenti (nella chiamata di funzione) |
| --- | --- | --- |
| **fare clic** | I clic sinistri in corrispondenza della coordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | Doppio clic sulla coordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | Tre clic in corrispondenza delle coordinate. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | Il cursore fa clic al centro delle coordinate. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | Fai clic con il tasto destro del mouse sulla coordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | Premere e tenere premuto il tasto del mouse in corrispondenza della coordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | Rilascia il tasto del mouse in corrispondenza della coordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **move** | Sposta il cursore nella posizione specificata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | Digita il testo. | `text`: str `press_enter`: bool (facoltativo, valore predefinito `false`) `intent`: str |
| **drag\_and\_drop** | Trascina un elemento dalla coordinata iniziale a quella finale. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | Mette in pausa l'esecuzione per un numero specificato di secondi. | `seconds`: int (facoltativo, valore predefinito `1`) `intent`: str |
| **press\_key** | Premi il tasto specificato e lo rilascia. | `key`: str `intent`: str |
| **key\_down** | Premere e tenere premuto il tasto specificato. | `key`: str `intent`: str |
| **key\_up** | Rilascia la chiave specificata. | `key`: str `intent`: str |
| **tasto di scelta rapida** | Premi la combinazione di tasti specificata. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | Restituisce uno screenshot della schermata corrente. | `intent`: str |
| **scroll** | Scorre verso l'alto, verso il basso, a sinistra o a destra in una coordinata di una distanza in pixel. | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, facoltativo, valore predefinito `300`) `intent`: str |
| **go\_back** | Torna alla pagina web precedente nella cronologia del browser. | `intent`: str |
| **navigate** | Consente di andare direttamente a un URL specificato. | `url`: str `intent`: str |
| **go\_forward** | Passa alla pagina web successiva nella cronologia del browser. | `intent`: str |

### Ambiente mobile (`ENVIRONMENT_MOBILE`)

Azioni dell'ambiente ottimizzate per Android:

| Nome comando | Descrizione | Argomenti (nella chiamata di funzione) |
| --- | --- | --- |
| **open\_app** | Apre un'applicazione in base al nome. | `app_name`: str `intent`: str |
| **fare clic** | I clic sinistri in corrispondenza della coordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **list\_apps** | Elenca le applicazioni disponibili sul dispositivo, restituendone i nomi e i nomi dei pacchetti. | `intent`: str |
| **wait** | Mette in pausa l'esecuzione per un numero specificato di secondi. | `seconds`: int (facoltativo, valore predefinito `1`) `intent`: str |
| **go\_back** | Torna alla schermata o alla pagina web precedente. | `intent`: str |
| **type** | Digita il testo. | `text`: str `press_enter`: bool (facoltativo, valore predefinito `false`) `intent`: str |
| **drag\_and\_drop** | Trascina un elemento dalla coordinata iniziale a quella finale. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **long\_press** | Esegue una pressione prolungata in una coordinata sullo schermo. | `y`: int (0-999) `x`: int (0-999) `seconds`: int (facoltativo, valore predefinito `2`) `intent`: str |
| **press\_key** | Premi il tasto specificato e lo rilascia. | `key`: str `intent`: str |
| **take\_screenshot** | Restituisce uno screenshot della schermata corrente. | `intent`: str |

### Ambiente desktop (`ENVIRONMENT_DESKTOP`)

Comandi del cursore a livello di sistema operativo degli ambienti desktop:

| Nome comando | Descrizione | Argomenti (nella chiamata di funzione) |
| --- | --- | --- |
| **fare clic** | I clic sinistri in corrispondenza della coordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | Doppio clic sulla coordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | Tre clic in corrispondenza delle coordinate. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | Il cursore fa clic al centro delle coordinate. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | Fai clic con il tasto destro del mouse sulla coordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | Premere e tenere premuto il tasto del mouse in corrispondenza della coordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | Rilascia il tasto del mouse in corrispondenza della coordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **move** | Sposta il cursore nella posizione specificata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | Digita il testo. | `text`: str `press_enter`: bool (facoltativo, valore predefinito `false`) `intent`: str |
| **drag\_and\_drop** | Trascina un elemento dalla coordinata iniziale a quella finale. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | Mette in pausa l'esecuzione per un numero specificato di secondi. | `seconds`: int (facoltativo, valore predefinito `1`) `intent`: str |
| **press\_key** | Premi il tasto specificato e lo rilascia. | `key`: str `intent`: str |
| **key\_down** | Premere e tenere premuto il tasto specificato. | `key`: str `intent`: str |
| **key\_up** | Rilascia la chiave specificata. | `key`: str `intent`: str |
| **tasto di scelta rapida** | Premi la combinazione di tasti specificata. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | Restituisce uno screenshot della schermata corrente. | `intent`: str |
| **scroll** | Scorre verso l'alto, verso il basso, a sinistra o a destra in una coordinata di una distanza in pixel. | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, facoltativo, valore predefinito `300`) `intent`: str |

## Azioni dell'interfaccia utente supportate legacy (Gemini 2.5)

Per i modelli legacy (`gemini-2.5-computer-use-preview-10-2025`), sono supportate le seguenti azioni:

| Nome comando | Descrizione | Argomenti (nella chiamata di funzione) | Esempio di chiamata di funzione |
| --- | --- | --- | --- |
| **open\_web\_browser** | Apre il browser web. | Nessuno | `{"name": "open_web_browser", "args": {}}` |
| **wait\_5\_seconds** | Mette in pausa l'esecuzione per 5 secondi. | Nessuno | `{"name": "wait_5_seconds", "args": {}}` |
| **go\_back** | Conduce alla pagina precedente della cronologia. | Nessuno | `{"name": "go_back", "args": {}}` |
| **go\_forward** | Conduce alla pagina successiva della cronologia. | Nessuno | `{"name": "go_forward", "args": {}}` |
| **search** | Viene visualizzato il motore di ricerca predefinito. | Nessuno | `{"name": "search", "args": {}}` |
| **navigate** | Il browser passa direttamente all'URL specificato. | `url`: str | `{"name": "navigate", "args": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | Clic a una coordinata specifica. | `y`: int (0-999), `x`: int (0-999) | `{"name": "click_at", "args": {"y": 300, "x": 500}}` |
| **hover\_at** | Passa il mouse su una coordinata specifica. | `y`: int (0-999), `x`: int (0-999) | `{"name": "hover_at", "args": {"y": 150, "x": 250}}` |
| **type\_text\_at** | Digita il testo in una coordinata. | `y`: int (0-999), `x`: int (0-999), `text`: str, `press_enter`: bool (facoltativo, valore predefinito True), `clear_before_typing`: bool (facoltativo, valore predefinito True) | `{"name": "type_text_at", "args": {"y": 250, "x": 400, "text": "search", "press_enter": false}}` |
| **key\_combination** | Premi i tasti o le combinazioni. | `keys`: str | `{"name": "key_combination", "args": {"keys": "Control+A"}}` |
| **scroll\_document** | Scorre l'intera pagina web. | `direction`: str | `{"name": "scroll_document", "args": {"direction": "down"}}` |
| **scroll\_at** | Scorre alla coordinata (x,y). | `y`: int, `x`: int, `direction`: str, `magnitude`: int (facoltativo, valore predefinito 800) | `{"name": "scroll_at", "args": {"y": 500, "x": 500, "direction": "down"}}` |
| **drag\_and\_drop** | Trascina tra due coordinate. | `y`: int, `x`: int, `destination_y`: int, `destination_x`: int | `{"name": "drag_and_drop", "args": {"y": 100, "destination_y": 500, "destination_x": 500, "x": 100}}` |

## Funzioni definite dall'utente personalizzate

Puoi estendere la funzionalità del modello includendo funzioni personalizzate definite dall'utente. Ad esempio, negli scenari human-in-the-loop (HITL) puoi escludere le azioni predefinite predefinite e registrare azioni personalizzate.

#### Strumenti personalizzati Gemini 3.x

### Python

Escludi le azioni predefinite standard del browser (ad esempio `click`) e registra uno strumento `yield_to_user` personalizzato:

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

#### Strumenti personalizzati Gemini 2.5 (legacy)

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

## Gestire i livelli di pensiero (Gemini 3.x)

Per gli agenti di utilizzo del computer, puoi configurare diversi livelli di pensiero per bilanciare la qualità dell'azione e la velocità di esecuzione. I livelli di pensiero più bassi generalmente raggiungono un buon equilibrio per le attività di automazione standard.

## Protezione e sicurezza

### Configurazione delle policy di sicurezza (Gemini 3.x)

I modelli Gemini 3.x includono categorie di servizi di sicurezza integrate che determinano automaticamente se è necessaria la conferma dell'utente.

| Categoria norma di sicurezza | Descrizione |
| --- | --- |
| `FINANCIAL_TRANSACTIONS` | Blocca o attiva la conferma per le azioni che riguardano pagamenti, acquisti al dettaglio o beni regolamentati. |
| `SENSITIVE_DATA_MODIFICATION` | Protegge i documenti sanitari, finanziari o governativi da modifiche non autorizzate. |
| `COMMUNICATION_TOOL` | Impedisce all'agente di inviare autonomamente email, messaggi di chat o bozze. |
| `ACCOUNT_CREATION` | Impedisce all'agente di registrare autonomamente nuovi account sui siti web. |
| `DATA_MODIFICATION` | Regola le modifiche complessive del file system, la condivisione dei dati e l'eliminazione dell'archiviazione. |
| `USER_CONSENT_MANAGEMENT` | Richiede l'intervento dell'utente per i banner del consenso all'uso dei cookie e le richieste di consenso alla privacy. |
| `LEGAL_TERMS_AND_AGREEMENTS` | Impedisce al modello di accettare autonomamente i Termini di servizio o i contratti legalmente vincolanti. |

#### Override di sicurezza

Puoi eseguire l'override di criteri selezionati passando gli override:

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

### Rilevamento di prompt injection (Gemini 3.x)

Meccanismo di sicurezza di attivazione che analizza i pixel degli screenshot alla ricerca di istruzioni di prompt avversarie nascoste (ad es. "Ignora i comandi precedenti") e blocca l'esecuzione quando vengono rilevate.

### Riconoscere la decisione relativa alla sicurezza

La risposta potrebbe includere un parametro `safety_decision` negli argomenti della chiamata di funzione:

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

Se `safety_decision` è `require_confirmation`, chiedi all'utente finale. Se l'utente conferma, imposta `safety_acknowledgement` in `FunctionResponse`.

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

### Best practice per la sicurezza

L'utilizzo del computer presenta rischi operativi e di sicurezza unici, in quanto un modello che agisce per conto di un utente potrebbe imbattersi in contenuti non attendibili sugli schermi o commettere errori nell'esecuzione delle azioni. Implementa le seguenti best practice per proteggere i dati e i sistemi degli utenti:

1. **Human-in-the-loop (HITL):**

   - **Imponi la conferma dell'utente**:quando la risposta di sicurezza indica
     `require_confirmation` (o la decisione di sicurezza precedente lo richiede), chiedi l'approvazione all'utente.
   - **Fornisci istruzioni di sicurezza personalizzate**:implementa un'istruzione di sistema personalizzata per definire e applicare i tuoi limiti di sicurezza. Ad esempio:

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
2. **Ambiente di esecuzione sicuro**:esegui l'agente in un ambiente sandbox sicuro per limitarne il potenziale impatto. Può trattarsi di una macchina virtuale (VM) in sandbox, di un container (ad es. Docker) o di un profilo browser dedicato con autorizzazioni limitate. Consulta l'[implementazione di riferimento di GitHub](https://github.com/google/computer-use-preview/) per indicazioni sulla configurazione della sandbox utilizzando Docker.
3. **Sanificazione dell'input**:sanifica tutto il testo generato dagli utenti nei prompt per ridurre il rischio di istruzioni non intenzionali o di prompt injection. Si tratta di un
   livello di sicurezza utile, ma non sostituisce un ambiente di esecuzione
   sicuro.
4. **Protezioni dei contenuti:** utilizza le protezioni e le API Content Safety per valutare
   l'idoneità degli input dell'utente, degli input e degli output degli strumenti e delle risposte dell'agente,
   il prompt injection e il rilevamento del jailbreak.
5. **Liste consentite e liste bloccate**:implementa meccanismi di filtraggio per controllare
   dove il modello può navigare e cosa può fare. Una lista bloccata di siti web vietati è un buon punto di partenza, mentre una lista consentita più restrittiva è
   ancora più sicura.
6. **Osservabilità e logging**:mantieni log dettagliati per il debug,
   il controllo e la risposta agli incidenti. Il tuo cliente deve registrare i prompt, gli screenshot, le azioni suggerite dal modello (`function_call`), le risposte di sicurezza e tutte le azioni eseguite dal cliente.
7. **Gestione dell'ambiente**:assicurati che l'ambiente GUI sia coerente.
   Pop-up, notifiche o modifiche impreviste al layout possono confondere il modello. Se possibile, inizia ogni nuova attività da uno stato pulito e noto.

## Versioni modello

Puoi utilizzare Computer Use con i seguenti modelli:

- [**Gemini 3.6 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=it) (`gemini-3.6-flash`): il modello consigliato per l'utilizzo del computer, con azioni semplificate con intent, supporto per ambienti browser, mobile e desktop, norme di sicurezza configurabili e rilevamento dell'iniezione di prompt.
- [**Gemini 3.5 Flash-Lite**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=it) (`gemini-3.5-flash-lite`): un modello economico a bassa latenza che supporta l'utilizzo del computer.
- [**Gemini 3.5 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=it) (`gemini-3.5-flash`): modello stabile precedente che supporta l'utilizzo del computer.
- [**Gemini 3 Flash (anteprima)**](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=it) (`gemini-3-flash-preview`): modello di anteprima
  che supporta l'utilizzo del computer.
- [**Gemini 2.5 (anteprima legacy)**](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025?hl=it) (`gemini-2.5-computer-use-preview-10-2025`): modello di anteprima legacy ottimizzato per l'utilizzo del computer basato su browser.

## Passaggi successivi

- Sperimenta con l'utilizzo del computer nell'[ambiente demo di Browserbase](http://gemini.browserbase.com).
- Consulta l'[implementazione di riferimento](https://github.com/google/computer-use-preview) per il codice di esempio.
- Scopri di più sugli altri strumenti dell'API Gemini:
  - [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)
  - [Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/grounding?hl=it)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
