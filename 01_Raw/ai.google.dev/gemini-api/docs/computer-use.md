---
source_url: https://ai.google.dev/gemini-api/docs/computer-use?hl=it
fetched_at: 2026-06-22T06:24:09.244913+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) is now available in preview with collaborative planning, visualization, MCP support, and more.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Uso del computer

L'utilizzo del computer ti consente di creare agenti di controllo del browser che interagiscono
con le attività e le automatizzano. Utilizzando gli screenshot, il modello può "vedere" lo schermo di un computer e "agire" generando azioni specifiche della UI, come clic del mouse e input da tastiera. Analogamente alla chiamata di funzione, devi scrivere il codice dell'applicazione lato client per ricevere ed eseguire le azioni di utilizzo del computer.

Con Utilizzo del computer, puoi creare agenti che:

- Automatizza l'inserimento di dati ripetitivi o la compilazione di moduli sui siti web.
- Esegui test automatici di applicazioni web e flussi utente
- Eseguire ricerche su vari siti web (ad es. raccogliere informazioni, prezzi e recensioni sui prodotti da siti di e-commerce per informare un acquisto)

Il modo più semplice per testare la funzionalità Utilizzo del computer è tramite l'[implementazione
di riferimento](https://github.com/google/computer-use-preview/) o
l'[ambiente demo Browserbase](http://gemini.browserbase.com).

## Come funziona Uso del computer

Per creare un agente di controllo del browser con il modello Utilizzo del computer, implementa
un ciclo dell'agente che esegue le seguenti operazioni:

1. [**Invia una richiesta al modello**](#send-request)

   - Aggiungi lo strumento Utilizzo del computer ed eventualmente qualsiasi funzione personalizzata definita dall'utente
     o funzione esclusa alla tua richiesta API.
   - Richiedi al modello Computer Use la richiesta dell'utente.
2. [**Ricevere la risposta del modello**](#model-response)

   - Il modello di utilizzo del computer analizza la richiesta e lo screenshot dell'utente e genera una risposta che include un `function_call` suggerito che rappresenta un'azione dell'interfaccia utente (ad es. "fai clic sulla coordinata (x,y)" o "digita "testo""). Per una descrizione di tutte le azioni dell'interfaccia utente supportate dal modello di utilizzo del computer, consulta [Azioni supportate](#supported-actions).
   - La risposta dell'API può includere anche un `safety_decision` di un sistema
     di sicurezza interno che controlla l'azione proposta dal modello. Questo
     `safety_decision` classifica l'azione come:
     - **Regolare / consentita**:l'azione è considerata sicura. Ciò può anche
       essere rappresentato dall'assenza di `safety_decision`.
     - **Richiede conferma (`require_confirmation`)**: il modello sta per eseguire un'azione
       che potrebbe essere rischiosa (ad es. fare clic su un "banner dei cookie").
3. [**Esegui l'azione ricevuta**](#execute-actions)

   - Il codice lato client riceve `function_call` e qualsiasi `safety_decision`
     di accompagnamento.
     - **Regolare / consentito**:se `safety_decision` indica regolare/consentito (o se non è presente alcun `safety_decision`), il codice lato client può eseguire `function_call` specificato nell'ambiente di destinazione (ad es. un browser web).
     - **Richiede conferma**:se `safety_decision` indica
       richiede conferma, la tua applicazione deve chiedere all'utente finale
       la conferma prima di eseguire `function_call`. Se l'utente
       conferma, procedi con l'esecuzione dell'azione. Se l'utente nega l'autorizzazione, non
       eseguire l'azione.
4. [**Acquisire il nuovo stato dell'ambiente**](#capture-state)

   - Se l'azione è stata eseguita, il client acquisisce una nuova schermata
     della GUI e l'URL corrente da inviare al modello Computer Use come
     parte di un `function_response`.
   - Se un'azione è stata bloccata dal sistema di sicurezza o la conferma è stata negata dall'utente, l'applicazione potrebbe inviare un altro tipo di feedback al modello o terminare l'interazione.

Questo processo si ripete dal passaggio 2 con il modello che utilizza la nuova
istantanea e l'obiettivo in corso per suggerire l'azione successiva. Il ciclo continua
finché l'attività non viene completata, si verifica un errore o il processo viene terminato
(ad esempio a causa di una risposta di sicurezza "blocca" o di una decisione dell'utente).

![Panoramica dell&#39;uso del computer](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=it)

## Come implementare l'uso del computer

Prima di creare con lo strumento Utilizzo del computer, devi configurare quanto segue:

- **Ambiente di esecuzione sicuro:** per motivi di sicurezza, devi eseguire l'agente
  Computer Use in un ambiente sicuro e controllato (ad es. una macchina virtuale
  sandbox, un container o un profilo browser dedicato con autorizzazioni
  limitate).
- **Gestore delle azioni lato client:** dovrai implementare la logica lato client
  per eseguire le azioni generate dal modello e
  acquisire screenshot dell'ambiente dopo ogni azione.

Gli esempi in questa sezione utilizzano un browser come ambiente di esecuzione
e [Playwright](https://playwright.dev/) come gestore di azioni lato client. Per
eseguire questi esempi, devi installare le dipendenze necessarie e inizializzare un'istanza del browser
Playwright:

### 0. Installare Playwright

```
pip install google-genai playwright
playwright install chromium
```

### 0. Inizializza l'istanza del browser Playwright

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

Il codice campione per l'estensione a un ambiente Android è incluso nella sezione [Utilizzo di funzioni personalizzate definite dall'utente](#custom-functions).

### 1. Inviare una richiesta al modello

Aggiungi lo strumento Utilizzo del computer alla richiesta API e invia un prompt al modello
che includa l'obiettivo dell'utente. Devi utilizzare uno dei modelli di utilizzo del computer supportati
o riceverai un errore:

- `gemini-2.5-computer-use-preview-10-2025`
- `gemini-3-flash-preview`

Puoi anche aggiungere facoltativamente i seguenti parametri:

- **Azioni escluse**:se ci sono azioni nell'elenco delle [azioni dell'interfaccia utente
  supportate](#supported-actions) che non vuoi che il modello esegua,
  specifica queste azioni come `excluded_predefined_functions`.
- **Funzioni definite dall'utente**:oltre allo strumento Utilizzo del computer, potresti
  voler includere funzioni personalizzate definite dall'utente.

Tieni presente che non è necessario specificare le dimensioni di visualizzazione quando invii una richiesta;
il modello prevede le coordinate dei pixel scalate in base all'altezza e alla larghezza dello
schermo.

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

Per un esempio con funzioni personalizzate, consulta [Utilizzo di funzioni personalizzate definite dall'utente](#custom-functions).

### 2. Ricevere la risposta del modello

Quando lo strumento Utilizzo del computer è attivato, il modello risponderà con uno o più
`FunctionCalls` se determina che sono necessarie azioni dell'interfaccia utente per completare l'attività.
L'utilizzo del computer supporta la chiamata di funzioni parallele, il che significa che il modello può restituire
più azioni in un singolo turno.

Ecco un esempio di risposta del modello.

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

### 3. Esegui le azioni ricevute

Il codice dell'applicazione deve analizzare la risposta del modello, eseguire le azioni
e raccogliere i risultati.

Il codice di esempio riportato di seguito estrae le chiamate di funzione dalla risposta del modello Computer Use e le traduce in azioni che possono essere eseguite con Playwright.
Il modello restituisce coordinate normalizzate (0-999) indipendentemente dalle dimensioni dell'immagine di input, quindi parte del passaggio di traduzione consiste nel convertire queste coordinate normalizzate di nuovo in valori di pixel effettivi.

Le dimensioni dello schermo consigliate per l'utilizzo
con il modello di utilizzo del computer sono (1440, 900). Il modello funzionerà con qualsiasi
risoluzione, anche se la qualità dei risultati potrebbe risentirne.

Tieni presente che questo esempio include solo l'implementazione per le tre azioni della UI più comuni: `open_web_browser`, `click_at` e `type_text_at`. Per i casi d'uso di produzione, dovrai implementare tutte le altre azioni della UI dall'elenco [Azioni supportate](#supported-actions), a meno che non le aggiunga esplicitamente come `excluded_predefined_functions`.

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

### 4. Acquisire il nuovo stato dell'ambiente

Dopo aver eseguito le azioni, invia il risultato dell'esecuzione della funzione al modello in modo che possa utilizzare queste informazioni per generare l'azione successiva. Se
sono state eseguite più azioni (chiamate parallele), devi inviare un
`FunctionResponse` per ciascuna nel turno successivo dell'utente.

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

## Crea un loop dell'agente

Per attivare le interazioni in più passaggi, combina i quattro passaggi della sezione [Come implementare l'utilizzo del computer](#implement-computer-use) in un ciclo. Ricorda di gestire correttamente la cronologia della conversazione aggiungendo sia le risposte del modello sia le risposte della funzione.

Per eseguire questo esempio di codice devi:

- Installa le [dipendenze Playwright necessarie](#expandable-1).
- Definisci le funzioni di assistenza dai passaggi [(3) Esegui le azioni ricevute](#execute-actions) e [(4) Acquisisci il nuovo stato dell'ambiente](#capture-state).

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

## Utilizzare funzioni definite dall'utente personalizzate

Se vuoi, puoi includere funzioni personalizzate definite dall'utente nella richiesta per estendere la funzionalità del modello. L'esempio riportato di seguito adatta il modello e lo strumento Utilizzo del computer per i casi d'uso mobile includendo azioni personalizzate definite dall'utente come `open_app`, `long_press_at` e `go_home`, escludendo al contempo le azioni specifiche del browser. Il modello può chiamare in modo intelligente queste funzioni personalizzate insieme alle azioni standard della UI per completare le attività in ambienti non browser.

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

## Azioni dell'interfaccia utente supportate

Il modello può richiedere le seguenti azioni dell'interfaccia utente tramite un
`FunctionCall`. Il codice lato client deve implementare la logica di esecuzione per
queste azioni. Per esempi, consulta l'[implementazione
di riferimento](https://github.com/google/computer-use-preview).

| Nome comando | Descrizione | Argomenti (in Chiamata funzione) | Esempio di chiamata di funzione |
| --- | --- | --- | --- |
| **open\_web\_browser** | Apre il browser web. | Nessuno | `{"name": "open_web_browser", "args": {}}` |
| **wait\_5\_seconds** | Mette in pausa l'esecuzione per 5 secondi per consentire il caricamento dei contenuti dinamici o il completamento delle animazioni. | Nessuno | `{"name": "wait_5_seconds", "args": {}}` |
| **go\_back** | Conduce alla pagina precedente nella cronologia del browser. | Nessuno | `{"name": "go_back", "args": {}}` |
| **go\_forward** | Conduce alla pagina successiva nella cronologia del browser. | Nessuno | `{"name": "go_forward", "args": {}}` |
| **search** | Viene visualizzata la home page del motore di ricerca predefinito (ad es. Google). Utile per avviare una nuova attività di ricerca. | Nessuno | `{"name": "search", "args": {}}` |
| **navigate** | Il browser passa direttamente all'URL specificato. | `url`: str | `{"name": "navigate", "args": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | Clic in una coordinata specifica della pagina web. I valori x e y si basano su una griglia 1000x1000 e vengono scalati in base alle dimensioni dello schermo. | `y`: int (0-999), `x`: int (0-999) | `{"name": "click_at", "args": {"y": 300, "x": 500}}` |
| **hover\_at** | Passa il mouse su una coordinata specifica della pagina web. Utile per visualizzare i sottomenu. x e y si basano su una griglia 1000x1000. | `y`: int (0-999) `x`: int (0-999) | `{"name": "hover_at", "args": {"y": 150, "x": 250}}` |
| **type\_text\_at** | Digita il testo in una coordinata specifica. Per impostazione predefinita, cancella prima il campo e preme INVIO dopo la digitazione, ma queste azioni possono essere disattivate. x e y si basano su una griglia 1000x1000. | `y`: int (0-999), `x`: int (0-999), `text`: str, `press_enter`: bool (facoltativo, valore predefinito True), `clear_before_typing`: bool (facoltativo, valore predefinito True) | `{"name": "type_text_at", "args": {"y": 250, "x": 400, "text": "search query", "press_enter": false}}` |
| **key\_combination** | Premi tasti o combinazioni di tasti della tastiera, ad esempio "Control+C" o "Invio". Utile per attivare azioni (come l'invio di un modulo con "Invio") o operazioni degli appunti. | `keys`: str (ad es. "invio", "control+c"). | `{"name": "key_combination", "args": {"keys": "Control+A"}}` |
| **scroll\_document** | Scorre l'intera pagina web "verso l'alto", "verso il basso", "verso sinistra" o "verso destra". | `direction`: str ("up", "down", "left" o "right") | `{"name": "scroll_document", "args": {"direction": "down"}}` |
| **scroll\_at** | Scorre un elemento o un'area specifica in corrispondenza delle coordinate (x, y) nella direzione specificata di una determinata entità. Le coordinate e l'entità (valore predefinito 800) si basano su una griglia 1000x1000. | `y`: int (0-999), `x`: int (0-999), `direction`: str ("up", "down", "left", "right"), `magnitude`: int (0-999, facoltativo, valore predefinito 800) | `{"name": "scroll_at", "args": {"y": 500, "x": 500, "direction": "down", "magnitude": 400}}` |
| **drag\_and\_drop** | Trascina un elemento da una coordinata iniziale (x, y) e lo rilascia in una coordinata di destinazione (destination\_x, destination\_y). Tutte le coordinate si basano su una griglia 1000x1000. | `y`: int (0-999), `x`: int (0-999), `destination_y`: int (0-999), `destination_x`: int (0-999) | `{"name": "drag_and_drop", "args": {"y": 100, "x": 100, "destination_y": 500, "destination_x": 500}}` |

## Protezione e sicurezza

### Riconoscere la decisione relativa alla sicurezza

A seconda dell'azione, la risposta del modello potrebbe includere anche un
`safety_decision` di un sistema di sicurezza interno che controlla l'azione
proposta dal modello.

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

Se `safety_decision` è `require_confirmation`, devi
chiedere all'utente finale di confermare prima di procedere con l'esecuzione dell'azione. Ai sensi dei
[termini di servizio](https://ai.google.dev/gemini-api/terms?hl=it), non è consentito
aggirare le richieste di conferma umana.

Questo esempio di codice chiede all'utente finale una conferma prima di eseguire l'azione. Se l'utente non conferma l'azione, il ciclo termina. Se l'utente conferma l'azione, questa viene eseguita e il campo
`safety_acknowledgement` viene contrassegnato come `True`.

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

Se l'utente conferma, devi includere la conferma di sicurezza nel tuo `FunctionResponse`.

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

### Best practice per la sicurezza

Utilizzo del computer è un nuovo strumento che presenta nuovi rischi di cui gli sviluppatori devono essere
consapevoli:

- **Contenuti non attendibili e truffe**:mentre cerca di raggiungere l'obiettivo dell'utente, il modello potrebbe fare affidamento su fonti di informazioni e istruzioni non attendibili sullo schermo. Ad esempio, se l'obiettivo dell'utente è acquistare uno smartphone Pixel e il modello si imbatte in una truffa del tipo "Pixel senza costi se completi un sondaggio", è possibile che il modello completi il sondaggio.
- **Azioni involontarie occasionali:** il modello può interpretare in modo errato l'obiettivo di un utente o i contenuti di una pagina web, causando azioni errate come il clic sul pulsante sbagliato o la compilazione del modulo errato. Ciò può comportare il mancato completamento delle attività o l'esfiltrazione di dati.
- **Violazioni delle norme**:le funzionalità dell'API potrebbero essere indirizzate, intenzionalmente o meno, verso attività che violano le norme di Google ([Norme relative all'uso vietato dell'AI generativa](https://policies.google.com/terms/generative-ai/use-policy?hl=it) e i [Termini di servizio aggiuntivi dell'API Gemini](https://ai.google.dev/gemini-api/terms?hl=it)). Sono incluse azioni che
  potrebbero interferire con l'integrità di un sistema, compromettere la sicurezza, aggirare
  le misure di sicurezza,
  controllare dispositivi medici e così via.

Per affrontare questi rischi, puoi implementare le seguenti misure di sicurezza e best practice:

1. **Human-in-the-loop (HITL):**

   - **Implementa la conferma dell'utente**:quando la risposta di sicurezza indica
     `require_confirmation`, devi implementare la conferma dell'utente prima
     dell'esecuzione. Per il codice campione, consulta la sezione [Riconoscere la decisione di sicurezza](#safety-decisions).
   - **Fornisci istruzioni di sicurezza personalizzate**:oltre ai controlli di conferma utente integrati, gli sviluppatori possono facoltativamente aggiungere un'[istruzione di sistema](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#system-instructions) personalizzata che applichi le proprie norme di sicurezza, per bloccare determinate azioni del modello o richiedere la conferma dell'utente prima che il modello intraprenda determinate azioni irreversibili ad alto rischio. Ecco un esempio di istruzione personalizzata
     del sistema di sicurezza che puoi includere quando interagisci con il modello.

     **Esempio di istruzioni di sicurezza:**

     Imposta le tue regole di sicurezza personalizzate come istruzione di sistema:

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
2. **Ambiente di esecuzione sicuro:** esegui l'agente in un ambiente sicuro e limitato tramite sandbox per limitarne il potenziale impatto (ad es. una macchina virtuale (VM) limitata tramite sandbox, un container (ad es. Docker) o un profilo browser dedicato con autorizzazioni limitate).
3. **Sanitizzazione dell'input**:sanitizza tutto il testo generato dagli utenti nei prompt per
   mitigare il rischio di istruzioni non intenzionali o di prompt injection. Si tratta di un
   livello di sicurezza utile, ma non sostituisce un ambiente di esecuzione
   sicuro.
4. **Misure di protezione dei contenuti**:utilizza misure di protezione e [API
   per la sicurezza dei contenuti](https://ai.google.dev/gemma/docs/shieldgemma?hl=it) per valutare gli input degli utenti, gli input e gli output degli strumenti, la risposta di un agente per l'adeguatezza, l'injection di prompt e il rilevamento del jailbreaking.
5. **Liste consentite e liste bloccate:** implementa meccanismi di filtro per controllare
   dove il modello può navigare e cosa può fare. Una lista bloccata di siti web vietati è un buon punto di partenza, mentre una lista consentita più restrittiva è
   ancora più sicura.
6. **Osservabilità e logging**:mantieni log dettagliati per il debug,
   il controllo e la risposta agli incidenti. Il client deve registrare i prompt,
   gli screenshot, le azioni suggerite dal modello (function\_call), le risposte di sicurezza e
   tutte le azioni eseguite dal client.
7. **Gestione dell'ambiente**:assicurati che l'ambiente GUI sia coerente.
   Pop-up, notifiche o modifiche impreviste al layout possono confondere il modello. Se possibile, inizia ogni nuova attività da uno stato pulito e noto.

## Versioni modello

Tieni presente che `gemini-3-flash-preview` supporta
l'uso del computer; non è necessario un modello separato per accedere allo strumento.

| Proprietà | Descrizione |
| --- | --- |
| Codice modello id\_card | **API Gemini**  `gemini-2.5-computer-use-preview-10-2025` |
| saveTipi di dati supportati | **Ingresso**  Immagine, testo  **Output**  Testo |
| token\_autoLimiti dei token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=it) | **Limite di token di input**  128.000  **Limite di token di output**  64.000 |
| Versioni 123 | Per ulteriori dettagli, leggi i [pattern delle versioni del modello](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#model-versions).  - Anteprima: `gemini-2.5-computer-use-preview-10-2025` |
| calendar\_monthUltimo aggiornamento | Ottobre 2025 |

## Passaggi successivi

- Sperimenta l'utilizzo del computer nell'[ambiente demo di Browserbase](http://gemini.browserbase.com).
- Consulta l'[implementazione
  di riferimento](https://github.com/google/computer-use-preview) per un esempio
  di codice.
- Scopri di più sugli altri strumenti dell'API Gemini:
  - [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)
  - [Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/grounding?hl=it)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-19 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-19 UTC."],[],[]]
