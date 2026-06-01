---
source_url: https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=de
fetched_at: 2026-06-01T19:37:16.628332+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Computernutzung

Mit der Computernutzung können Sie Browsersteuerungs-Agents erstellen, die mit Aufgaben interagieren und diese automatisieren. Anhand von Screenshots kann das Modell einen Computerbildschirm „sehen“ und „agieren“, indem es bestimmte UI-Aktionen wie Mausklicks und Tastatureingaben generiert. Ähnlich wie beim Funktionsaufruf müssen Sie den clientseitigen Anwendungscode schreiben, um die Aktionen zur Computernutzung zu empfangen und auszuführen.

Mit „Computer Use“ können Sie Agents erstellen, die Folgendes können:

- Wiederholte Dateneingaben oder das Ausfüllen von Formularen auf Websites automatisieren
- Automatisierte Tests von Webanwendungen und User Flows durchführen
- Recherchen auf verschiedenen Websites durchführen (z.B. Produktinformationen, Preise und Rezensionen von E-Commerce-Websites abrufen, um eine Kaufentscheidung zu treffen)

Am einfachsten lässt sich die Funktion „Computer Use“ über die [Referenzimplementierung](https://github.com/google/computer-use-preview/) oder die [Browserbase-Demo-Umgebung](http://gemini.browserbase.com) testen.

## So funktioniert die Computernutzung

Wenn Sie einen Browser-Steuerungs-Agent mit dem Modell „Computer Use“ erstellen möchten, implementieren Sie eine Agentschleife, die Folgendes ausführt:

1. [**Anfrage an das Modell senden**](#send-request)

   - Fügen Sie Ihrer API-Anfrage das Tool „Computer Use“ und optional benutzerdefinierte Funktionen oder ausgeschlossene Funktionen hinzu.
   - Stellen Sie dem Modell für die Computernutzung die Anfrage des Nutzers als Prompt zur Verfügung.
2. [**Modellantwort erhalten**](#model-response)

   - Das Modell „Computer Use“ analysiert die Nutzeranfrage und den Screenshot und generiert eine Antwort mit einer vorgeschlagenen `function_call`, die eine UI-Aktion darstellt (z.B. „Klicke auf die Koordinate (x,y)“ oder „Gib ‚text‘ ein“). Eine Beschreibung aller UI-Aktionen, die vom Modell „Computer verwenden“ unterstützt werden, finden Sie unter [Unterstützte Aktionen](#supported-actions).
   - Die API-Antwort kann auch ein `safety_decision` von einem internen Sicherheitssystem enthalten, das die vom Modell vorgeschlagene Aktion prüft. Dadurch wird die Aktion als Folgendes klassifiziert:
     `safety_decision`- **Regulär / Zulässig**:Die Aktion gilt als sicher. Das kann auch dadurch dargestellt werden, dass kein `safety_decision` vorhanden ist.
     - **Bestätigung erforderlich (`require_confirmation`)**: Das Modell ist dabei, eine möglicherweise riskante Aktion auszuführen, z.B. auf ein Cookie-Banner zu klicken.
3. [**Erhaltene Aktion ausführen**](#execute-actions)

   - Ihr clientseitiger Code empfängt die `function_call` und alle zugehörigen `safety_decision`.
     - **Regulär / zulässig**:Wenn `safety_decision` „regulär / zulässig“ angibt (oder wenn kein `safety_decision` vorhanden ist), kann Ihr clientseitiger Code die angegebene `function_call` in Ihrer Zielumgebung (z.B. einem Webbrowser) ausführen.
     - **Bestätigung erforderlich**:Wenn `safety_decision` angibt, dass eine Bestätigung erforderlich ist, muss Ihre Anwendung den Endnutzer vor der Ausführung von `function_call` zur Bestätigung auffordern. Wenn der Nutzer bestätigt, fahre mit der Ausführung der Aktion fort. Wenn der Nutzer die Ausführung ablehnt, führen Sie die Aktion nicht aus.
4. [**Neuen Umgebungsstatus erfassen**](#capture-state)

   - Wenn die Aktion ausgeführt wurde, erstellt Ihr Client einen neuen Screenshot der Benutzeroberfläche und der aktuellen URL, die als Teil eines `function_result` an das Modell für die Computernutzung zurückgesendet werden.
   - Wenn eine Aktion vom Sicherheitssystem blockiert oder die Bestätigung durch den Nutzer verweigert wurde, kann Ihre Anwendung eine andere Art von Feedback an das Modell senden oder die Interaktion beenden.

Dieser Vorgang wird ab Schritt 2 wiederholt. Das Modell verwendet den neuen Screenshot und das laufende Ziel, um die nächste Aktion vorzuschlagen. Die Schleife wird fortgesetzt, bis die Aufgabe abgeschlossen ist, ein Fehler auftritt oder der Prozess beendet wird (z.B. aufgrund einer Sicherheitsantwort vom Typ „Block“ oder einer Nutzerentscheidung).

![Computernutzung – Übersicht](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=de)

## Implementierung von „Computer Use“

Bevor Sie das Tool zur Computernutzung verwenden können, müssen Sie Folgendes einrichten:

- **Sichere Ausführungsumgebung**:Aus Sicherheitsgründen sollten Sie Ihren Computer Use-Agent in einer sicheren und kontrollierten Umgebung ausführen, z.B. in einer Sandbox-VM, einem Container oder einem dedizierten Browserprofil mit eingeschränkten Berechtigungen.
- **Clientseitiger Aktionshandler**:Sie müssen clientseitige Logik implementieren, um die vom Modell generierten Aktionen auszuführen und nach jeder Aktion Screenshots der Umgebung zu erstellen.

In den Beispielen in diesem Abschnitt wird ein Browser als Ausführungsumgebung und [Playwright](https://playwright.dev/) als clientseitiger Aktionshandler verwendet. Damit Sie diese Beispiele ausführen können, müssen Sie die erforderlichen Abhängigkeiten installieren und eine Playwright-Browserinstanz initialisieren.

#### Playwright installieren

```
    pip install google-genai playwright
    playwright install chromium
```

#### Playwright-Browserinstanz initialisieren

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

Beispielcode für die Erweiterung auf eine Android-Umgebung finden Sie im Abschnitt [Benutzerdefinierte benutzerdefinierte Funktionen verwenden](#custom-functions).

### 1. Anfrage an das Modell senden

Fügen Sie Ihrer API-Anfrage das Tool „Computer Use“ hinzu und senden Sie einen Prompt an das Modell, der das Ziel des Nutzers enthält. Sie müssen eines der unterstützten Modelle für die Computernutzung verwenden, da sonst ein Fehler auftritt:

- `gemini-2.5-computer-use-preview-10-2025`
- `gemini-3-flash-preview`

Optional können Sie auch die folgenden Parameter hinzufügen:

- **Ausgeschlossene Aktionen**:Wenn es Aktionen aus der Liste der [unterstützten UI-Aktionen](#supported-actions) gibt, die das Modell nicht ausführen soll, geben Sie diese Aktionen als `excluded_predefined_functions` an.
- **Benutzerdefinierte Funktionen**:Zusätzlich zum Tool „Computer Use“ können Sie benutzerdefinierte Funktionen einfügen.

Die Anzeigegröße muss bei einer Anfrage nicht angegeben werden. Das Modell sagt Pixelkoordinaten voraus, die auf die Höhe und Breite des Bildschirms skaliert werden.

### Python

```
from google import genai

client = genai.Client()

# Specify predefined functions to exclude (optional)
excluded_functions = ["drag_and_drop"]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    input="Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        }
    ]
)

print(interaction)
```

Ein Beispiel mit benutzerdefinierten Funktionen finden Sie unter [Benutzerdefinierte benutzerdefinierte Funktionen verwenden](#custom-functions).

### 2. Antwort des Modells erhalten

Wenn das Tool „Computer verwenden“ aktiviert ist, antwortet das Modell mit einem oder mehreren `function_call`-Schritten, wenn es feststellt, dass UI-Aktionen erforderlich sind, um die Aufgabe zu erledigen.
Die Funktion „Computer Use“ unterstützt parallele Funktionsaufrufe. Das bedeutet, dass das Modell in einem einzigen Zug mehrere Aktionen zurückgeben kann.

Hier ist ein Beispiel für eine Modellantwort.

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I will type the search query into the search bar. The search bar is in the center of the page."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "type_text_at",
      "arguments": {
        "x": 371,
        "y": 470,
        "text": "highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping",
        "press_enter": true
      }
    }
  ]
}
```

### 3. Erhaltene Aktionen ausführen

Ihr Anwendungscode muss die Modellantwort parsen, die Aktionen ausführen und die Ergebnisse erfassen.

Im folgenden Beispielcode werden Funktionsaufrufe aus der Antwort des Modells „Computer Use“ extrahiert und in Aktionen übersetzt, die mit Playwright ausgeführt werden können.
Das Modell gibt normalisierte Koordinaten (0–999) unabhängig von den Abmessungen des Eingabebilds aus. Daher müssen diese normalisierten Koordinaten im Übersetzungsschritt wieder in tatsächliche Pixelwerte umgewandelt werden.

Die empfohlene Bildschirmgröße für die Verwendung mit dem Modell „Computer Use“ ist (1440, 900). Das Modell funktioniert mit jeder Auflösung, die Qualität der Ergebnisse kann jedoch beeinträchtigt werden.

Dieses Beispiel enthält nur die Implementierung für die drei häufigsten UI-Aktionen: `open_web_browser`, `click_at` und `type_text_at`. Für Produktionsanwendungsfälle müssen Sie alle anderen UI-Aktionen aus der Liste [Unterstützte Aktionen](#supported-actions) implementieren, sofern Sie sie nicht explizit als `excluded_predefined_functions` hinzufügen.

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
    function_calls = [
        step for step in interaction.steps if step.type == "function_call"
    ]

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.arguments
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

        results.append((fname, function_call.id, action_result))

    return results
```

### 4. Neuen Umgebungsstatus erfassen

Senden Sie nach der Ausführung der Aktionen das Ergebnis der Funktionsausführung zurück an das Modell, damit es diese Informationen zum Generieren der nächsten Aktion verwenden kann. Wenn mehrere Aktionen (parallele Aufrufe) ausgeführt wurden, müssen Sie im nächsten Nutzerzug für jede Aktion ein `function_result` senden.

### Python

```
import json
import base64

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

## Agent-Schleife erstellen

Um mehrstufige Interaktionen zu ermöglichen, kombinieren Sie die vier Schritte aus dem Abschnitt [Computer Use implementieren](#implement-computer-use) in einer Schleife.
Denken Sie daran, den Unterhaltungsverlauf richtig zu verwalten, indem Sie sowohl Modellantworten als auch Ihre Funktionsantworten anhängen.

So führen Sie dieses Codebeispiel aus:

- Installieren Sie die [erforderlichen Playwright-Abhängigkeiten](#implement-computer-use).
- Definieren Sie die Hilfsfunktionen aus den Schritten [(3) Empfangene Aktionen ausführen](#execute-actions) und [(4) Neuen Umgebungsstatus erfassen](#capture-state).

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright

from google import genai

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

    # Take initial screenshot
    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    # First interaction
    interaction = client.interactions.create(
        model='gemini-2.5-computer-use-preview-10-2025',
        input=[
            {"type": "text", "text": USER_PROMPT},
            {"type": "image", "data": base64.b64encode(initial_screenshot).decode("utf-8"), "mime_type": "image/png"}
        ],
        tools=[{
            "type": "computer_use",
            "environment": "browser"
        }]
    )

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")

        has_function_calls = any(
            step.type == "function_call"
            for step in interaction.steps
        )
        if not has_function_calls:
            text_response = " ".join([
                content_block.text for step in interaction.steps if step.type == "model_output"
                for content_block in step.content if content_block.type == "text"
            ])
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(interaction, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        # Continue conversation with function responses
        interaction = client.interactions.create(
            model='gemini-2.5-computer-use-preview-10-2025',
            previous_interaction_id=interaction.id,
            input=function_responses,
            tools=[{
                "type": "computer_use",
                "environment": "browser"
            }]
        )

finally:
    # Cleanup
    print("\nClosing browser...")
    browser.close()
    playwright.stop()
```

## Benutzerdefinierte Funktionen verwenden

Optional können Sie benutzerdefinierte Funktionen in Ihre Anfrage einfügen, um die Funktionalität des Modells zu erweitern. Im folgenden Beispiel werden das Modell und das Tool für die Computernutzung an mobile Anwendungsfälle angepasst. Dazu werden benutzerdefinierte Aktionen wie `open_app`, `long_press_at` und `go_home` einbezogen, während browserspezifische Aktionen ausgeschlossen werden. Das Modell kann diese benutzerdefinierten Funktionen zusammen mit Standard-UI-Aktionen intelligent aufrufen, um Aufgaben in Nicht-Browser-Umgebungen auszuführen.

### Python

```
from typing import Optional, Dict, Any

from google import genai

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

# Custom function definitions for mobile
custom_functions = [
    {
        "type": "function",
        "name": "open_app",
        "description": "Opens an app by name.",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {"type": "string", "description": "Name of the app to open"},
                "intent": {"type": "string", "description": "Optional deep-link or action"}
            },
            "required": ["app_name"]
        }
    },
    {
        "type": "function",
        "name": "long_press_at",
        "description": "Long-press at a specific screen coordinate.",
        "parameters": {
            "type": "object",
            "properties": {
                "x": {"type": "integer", "description": "X coordinate"},
                "y": {"type": "integer", "description": "Y coordinate"}
            },
            "required": ["x", "y"]
        }
    },
    {
        "type": "function",
        "name": "go_home",
        "description": "Navigates to the device home screen.",
        "parameters": {"type": "object", "properties": {}}
    }
]

# Exclude browser-specific functions
excluded_functions = [
    "open_web_browser",
    "search",
    "navigate",
    "hover_at",
    "scroll_document",
    "go_forward",
    "key_combination",
    "drag_and_drop",
]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    system_instruction=SYSTEM_PROMPT,
    input="Open Chrome, then long-press at 200,400.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        },
        *custom_functions
    ]
)

print(interaction)
```

## Unterstützte UI-Aktionen

Das Modell kann die folgenden UI-Aktionen mit einem `function_call` anfordern. In Ihrem clientseitigen Code muss die Ausführungslogik für diese Aktionen implementiert werden. [Referenzimplementierung](https://github.com/google/computer-use-preview)

| Befehlsname | Beschreibung | Argumente (im Funktionsaufruf) | Beispiel für Funktionsaufruf |
| --- | --- | --- | --- |
| **open\_web\_browser** | Öffnet den Webbrowser. | Keine | `{"name": "open_web_browser", "arguments": {}}` |
| **wait\_5\_seconds** | Die Ausführung wird für 5 Sekunden pausiert, damit dynamische Inhalte geladen oder Animationen abgeschlossen werden können. | Keine | `{"name": "wait_5_seconds", "arguments": {}}` |
| **go\_back** | Navigiert zur vorherigen Seite im Browserverlauf. | Keine | `{"name": "go_back", "arguments": {}}` |
| **go\_forward** | Navigiert zur nächsten Seite im Browserverlauf. | Keine | `{"name": "go_forward", "arguments": {}}` |
| **search** | Ruft die Startseite der Standardsuchmaschine auf (z.B. Google). Nützlich, um eine neue Suchaufgabe zu starten. | Keine | `{"name": "search", "arguments": {}}` |
| **navigate** | Leitet den Browser direkt zur angegebenen URL weiter. | `url`: str | `{"name": "navigate", "arguments": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | Klicks an einer bestimmten Koordinate auf der Webseite. Die x- und y-Werte basieren auf einem 1.000 × 1.000-Raster und werden auf die Bildschirmabmessungen skaliert. | `y`: int (0–999), `x`: int (0–999) | `{"name": "click_at", "arguments": {"y": 300, "x": 500}}` |
| **hover\_at** | Bewegt den Mauszeiger zu einer bestimmten Koordinate auf der Webseite. Nützlich zum Einblenden von Untermenüs. x und y basieren auf einem 1.000 × 1.000-Raster. | `y`: int (0–999) `x`: int (0–999) | `{"name": "hover_at", "arguments": {"y": 150, "x": 250}}` |
| **type\_text\_at** | Gibt Text an einer bestimmten Koordinate ein. Standardmäßig wird das Feld zuerst gelöscht und nach der Eingabe die Eingabetaste gedrückt. Diese Einstellungen können jedoch deaktiviert werden. „x“ und „y“ basieren auf einem 1000 × 1000-Raster. | `y`: int (0–999), `x`: int (0–999), `text`: str, `press_enter`: bool (optional, Standardwert: True), `clear_before_typing`: bool (optional, Standardwert: True) | `{"name": "type_text_at", "arguments": {"y": 250, "x": 400, "text": "search query", "press_enter": false}}` |
| **key\_combination** | Drücken Sie Tasten oder Tastenkombinationen wie „Strg+C“ oder „Eingabetaste“. Nützlich zum Auslösen von Aktionen (z. B. zum Senden eines Formulars mit der Eingabetaste) oder für Zwischenablagevorgänge. | `keys`: str (z.B. „enter“, „control+c“). | `{"name": "key_combination", "arguments": {"keys": "Control+A"}}` |
| **scroll\_document** | Scrollt die gesamte Webseite nach „oben“, „unten“, „links“ oder „rechts“. | `direction`: str („up“, „down“, „left“ oder „right“) | `{"name": "scroll_document", "arguments": {"direction": "down"}}` |
| **scroll\_at** | Scrollt ein bestimmtes Element oder einen bestimmten Bereich an der Koordinate (x, y) in der angegebenen Richtung um einen bestimmten Betrag. Koordinaten und Magnitude (Standardwert: 800) basieren auf einem 1.000 × 1.000-Raster. | `y`: int (0–999), `x`: int (0–999), `direction`: str („up“, „down“, „left“, „right“), `magnitude`: int (0–999, optional, Standardwert 800) | `{"name": "scroll_at", "arguments": {"y": 500, "x": 500, "direction": "down", "magnitude": 400}}` |
| **drag\_and\_drop** | Zieht ein Element von einer Startkoordinate (x, y) und legt es an einer Zielkoordinate (destination\_x, destination\_y) ab. Alle Koordinaten basieren auf einem 1.000 × 1.000-Raster. | `y`: int (0–999), `x`: int (0–999), `destination_y`: int (0–999), `destination_x`: int (0–999) | `{"name": "drag_and_drop", "arguments": {"y": 100, "x": 100, "destination_y": 500, "destination_x": 500}}` |

## Sicherheit

### Sicherheitsentscheidung bestätigen

Je nach Aktion kann die Modellantwort auch ein `safety_decision` von einem internen Sicherheitssystem enthalten, das die vorgeschlagene Aktion des Modells prüft.

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I have evaluated step 2. It seems Google detected unusual traffic and is asking me to verify I'm not a robot. I need to click the 'I'm not a robot' checkbox located near the top left (y=98, x=95)."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "click_at",
      "arguments": {
        "x": 60,
        "y": 100,
        "safety_decision": {
          "explanation": "I have encountered a CAPTCHA challenge that requires interaction. I need you to complete the challenge by clicking the 'I'm not a robot' checkbox and any subsequent verification steps.",
          "decision": "require_confirmation"
        }
      }
    }
  ]
}
```

Wenn `safety_decision` `require_confirmation` ist, müssen Sie den Endnutzer um Bestätigung bitten, bevor Sie mit der Ausführung der Aktion fortfahren. Gemäß den [Nutzungsbedingungen](https://ai.google.dev/gemini-api/terms?hl=de) ist es nicht zulässig, Anfragen zur Bestätigung durch einen Menschen zu umgehen.

In diesem Codebeispiel wird der Endnutzer vor der Ausführung der Aktion um Bestätigung gebeten. Wenn der Nutzer die Aktion nicht bestätigt, wird die Schleife beendet. Wenn der Nutzer die Aktion bestätigt, wird sie ausgeführt und das Feld `safety_acknowledgement` wird als `True` markiert.

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

def execute_function_calls(interaction, page, screen_width, screen_height):

    # ... Extract function calls from response ...

    for function_call in function_calls:
        extra_fr_fields = {}

        # Check for safety decision
        if 'safety_decision' in function_call.arguments:
            decision = get_safety_confirmation(function_call.arguments['safety_decision'])
            if decision == "TERMINATE":
                print("Terminating agent loop")
                break
            extra_fr_fields["safety_acknowledgement"] = True # Safety acknowledgement

        # ... Execute function call and append to results ...
```

Wenn der Nutzer die Bestätigung bestätigt, müssen Sie die Sicherheitsbestätigung in Ihre `function_result` aufnehmen.

```
```python
function_responses.append({
    "type": "function_result",
    "name": name,
    "call_id": function_call.id,
    "result": [
        {
            "type": "text",
            "text": json.dumps({
                "url": current_url,
                "safety_acknowledgement": True,
                **extra_fr_fields
            })
        },
        {
            "type": "image",
            "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
            "mime_type": "image/png"
        }
    ]
})
```
```

### Best Practices für die Sicherheit

Die Computernutzung ist ein neuartiges Tool, das neue Risiken birgt, die Entwickler berücksichtigen sollten:

- **Nicht vertrauenswürdige Inhalte und Betrug:** Da das Modell versucht, das Ziel des Nutzers zu erreichen, kann es auf nicht vertrauenswürdige Informationsquellen und Anweisungen auf dem Bildschirm zurückgreifen. Wenn das Ziel des Nutzers beispielsweise darin besteht, ein Pixel Smartphone zu kaufen, und das Modell auf einen Betrugsstil mit dem Titel „Kostenloses Pixel, wenn Sie an einer Umfrage teilnehmen“ stößt, besteht eine gewisse Wahrscheinlichkeit, dass das Modell die Umfrage ausfüllt.
- **Gelegentliche unbeabsichtigte Aktionen**:Das Modell kann das Ziel eines Nutzers oder den Inhalt einer Webseite falsch interpretieren und dadurch falsche Aktionen ausführen, z. B. auf die falsche Schaltfläche klicken oder das falsche Formular ausfüllen. Dies kann zu fehlgeschlagenen Aufgaben oder zur Daten-Exfiltration führen.
- **Richtlinienverstöße**:Die Funktionen der API könnten entweder absichtlich oder unbeabsichtigt auf Aktivitäten ausgerichtet sein, die gegen die Google-Richtlinien verstoßen ([Richtlinie zur unzulässigen Nutzung von generativer KI](https://policies.google.com/terms/generative-ai/use-policy?hl=de) und [Zusatzbedingungen für die Gemini API](https://ai.google.dev/gemini-api/terms?hl=de)). Dazu gehören Aktionen, die die Integrität eines Systems beeinträchtigen, die Sicherheit gefährden, Sicherheitsmaßnahmen umgehen oder medizinische Geräte steuern könnten.

Um diese Risiken zu minimieren, können Sie die folgenden Sicherheitsmaßnahmen und Best Practices implementieren:

1. **Human-in-the-Loop (HITL)**:

   - **Nutzerbestätigung implementieren**:Wenn die Sicherheitsantwort `require_confirmation` enthält, müssen Sie vor der Ausführung eine Nutzerbestätigung implementieren. [Beispielcode](#safety-decisions)
   - **Benutzerdefinierte Sicherheitshinweise bereitstellen**:Zusätzlich zu den integrierten Prüfungen zur Nutzerbestätigung können Entwickler optional eine benutzerdefinierte [Systemanweisung](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#system-instructions) hinzufügen, mit der sie ihre eigenen Sicherheitsrichtlinien durchsetzen. So können sie bestimmte Modellaktionen blockieren oder eine Nutzerbestätigung anfordern, bevor das Modell bestimmte irreversible Aktionen mit hohem Risiko ausführt. Hier ist ein Beispiel für eine benutzerdefinierte Systemanweisung zur Sicherheit, die Sie bei der Interaktion mit dem Modell einfügen können.

     #### Beispiele für Sicherheitshinweise

     Legen Sie Ihre benutzerdefinierten Sicherheitsregeln als Systemanweisung fest:

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
2. **Sichere Ausführungsumgebung**:Führen Sie Ihren Agent in einer sicheren Sandbox-Umgebung aus, um seine potenziellen Auswirkungen zu begrenzen (z. B. eine Sandbox-VM, ein Container wie Docker oder ein dediziertes Browserprofil mit eingeschränkten Berechtigungen).
3. **Eingabebereinigung**:Bereinigen Sie alle von Nutzern generierten Texte in Prompts, um das Risiko unbeabsichtigter Anweisungen oder Prompt-Injection zu minimieren. Dies ist eine hilfreiche Sicherheitsebene, aber kein Ersatz für eine sichere Ausführungsumgebung.
4. **Inhaltsvorkehrungen**:Verwenden Sie Vorkehrungen und [APIs für die Inhaltssicherheit](https://ai.google.dev/gemma/docs/shieldgemma?hl=de), um Nutzereingaben, Tool-Ein- und -Ausgaben sowie die Antwort eines Agents auf Angemessenheit, Prompt-Injection und Jailbreak-Erkennung zu prüfen.
5. **Zulassungs- und Sperrlisten**:Implementieren Sie Filtermechanismen, um zu steuern, wohin das Modell navigieren und was es tun kann. Eine Sperrliste mit verbotenen Websites ist ein guter Ausgangspunkt. Eine restriktivere Zulassungsliste ist noch sicherer.
6. **Beobachtbarkeit und Protokollierung**:Detaillierte Logs für das Debugging, die Prüfung und die Incident Response führen. Ihr Client sollte Eingabeaufforderungen, Screenshots, vom Modell vorgeschlagene Aktionen (function\_call), Sicherheitsantworten und alle Aktionen protokollieren, die letztendlich vom Client ausgeführt werden.
7. **Umgebungsverwaltung**:Sorgen Sie für eine konsistente GUI-Umgebung.
   Unerwartete Pop-ups, Benachrichtigungen oder Layoutänderungen können das Modell verwirren. Beginnen Sie jede neue Aufgabe nach Möglichkeit mit einem bekannten, sauberen Zustand.

## Modellversionen

`gemini-3-flash-preview` bietet integrierte Unterstützung für die Computernutzung. Sie benötigen kein separates Modell, um auf das Tool zuzugreifen.

| Attribut | Beschreibung |
| --- | --- |
| id\_cardModellcode | **Gemini API**  `gemini-2.5-computer-use-preview-10-2025` |
| saveUnterstützte Datentypen | **Eingabe**  Bild, Text  **Ausgabe**  Text |
| token\_autoToken-Limits[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=de) | **Eingabetokenlimit**  128.000  **Tokenausgabelimit**  64.000 |
| 123-Versionen | Weitere Informationen finden Sie unter [Muster für Modellversionen](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#model-versions).  - Vorschau für: `gemini-2.5-computer-use-preview-10-2025` |
| calendar\_monthLetzte Aktualisierung | Oktober 2025 |

## Nächste Schritte

- [Browserbase-Demo](http://gemini.browserbase.com)
- Beispielcode finden Sie in der [Referenzimplementierung](https://github.com/google/computer-use-preview).
- Weitere Gemini API-Tools:
  - [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=de)
  - [Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-01 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-01 (UTC)."],[],[]]
