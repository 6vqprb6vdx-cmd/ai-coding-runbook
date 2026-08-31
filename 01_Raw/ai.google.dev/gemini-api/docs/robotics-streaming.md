---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=de
fetched_at: 2026-08-31T06:30:48.327265+00:00
title: "Robotik mit Streaming \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Robotik mit Streaming

Der `gemini-robotics-er-2-streaming-preview` Modellendpunkt stellt einen dedizierten
Streaming-Endpunkt bereit, der in die [Live
API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=de) eingebunden ist und eine bidirektionale Echtzeitinteraktion zwischen Ihrer Anwendung und dem Roboter ermöglicht. Daher eignet er sich für KI-Agenten, die schnelle Feedbackschleifen und reaktive Antworten auf die Umgebung benötigen.

[In Google AI Studio testen](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=de)
[Beispielanwendungen von GitHub klonen](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## Anwendungsfälle

- **Koordination mehrerer Roboter**: Mehrere Roboter, die den Aufgabenstatus kommunizieren
  und Unteraufgaben über eine gemeinsame Sitzung delegieren.
- **Kontinuierliches Monitoring**: Roboter, die eine Szene beobachten und Aktionen auslösen, wenn bestimmte Ereignisse eintreten, z. B. wenn ein Container einen bestimmten Füllstand erreicht.
- **Lager und Logistik**: Kommissionierungs- und Verpackungs-KI-Agenten, die Artikel
  visuell überprüfen, den Verpackungsfortschritt verfolgen und Fehler beheben.

## Technische Spezifikationen

In der folgenden Tabelle sind die technischen Spezifikationen für die Live API aufgeführt:

| Kategorie | Details |
| --- | --- |
| Eingabemodalitäten | Audio (rohes 16-Bit-PCM-Audio, 16 kHz, Little-Endian), Bilder (JPEG <= 1 FPS), Text |
| Ausgabemodalitäten | Text |
| Protokoll | Zustandsbehaftete WebSocket-Verbindung (WSS) |

## Agentenkonfiguration erstellen

Jeder Robotics-KI-Agent, der auf der Live API basiert, folgt drei Schritten:

1. **Roboterfunktionen als Tools deklarieren.** Jede Aktion, die der Roboter ausführen kann (z. B. navigieren, greifen, sprechen), wird zu einer Funktionsdeklaration mit einem Namen, einer Beschreibung und einem Parameterschema. Für physische Aktionen muss
   `"behavior": "BLOCKING"` verwendet werden, damit das Modell wartet, bis der Roboter die Aktion abgeschlossen hat, bevor
   es den nächsten Schritt auswählt.
2. **Multimodale Eingabe in eine persistente Sitzung streamen.** Öffnen Sie eine `live.connect`-Sitzung und lassen Sie sie für die gesamte Dauer der Aufgabe geöffnet. Senden Sie Videoframes, Audio oder Text, sobald sie von den Sensoren des Roboters empfangen werden.
3. **Toolaufrufe in einer Empfangsschleife verarbeiten.** Jedes Mal, wenn das Modell eine Aktion auswählt, wird eine `tool_call`-Nachricht gesendet. Ihre Empfangsschleife führt die Funktion für Ihr Roboter-SDK aus und sendet eine `tool_response` zurück. Die Sitzung bleibt geöffnet und das Modell wählt die nächste Aktion basierend auf dem Ergebnis aus.

In den folgenden Abschnitten wird beschrieben, wie Sie diese Schritte auf drei gängige Muster anwenden: eine grundlegende Agentenschleife, proaktive Szenenüberwachung mit einem Heartbeat und die Weiterleitung von Sprache über TTS als Tool.

## Roboter über Funktionsaufrufe orchestrieren

Im folgenden Beispiel sind alle drei Schritte in einem einzelnen Python-Skript miteinander verbunden.

Schritt 1 – Tooldefinitionen – deklariert Roboterfunktionen als Funktionsdeklarationen. Die `navigate` Funktion verwendet `"behavior": "BLOCKING"`, damit das
Modell wartet, bis der Roboter den Wegpunkt erreicht hat, bevor ein anderes Tool aufgerufen wird.
Fügen Sie derselben Liste weitere Funktionsdeklarationen hinzu, um zusätzliche Roboterfunktionen verfügbar zu machen.

Schritt 2 – Eingabehilfen – zeigt drei Funktionen, die verschiedene Modalitätseingaben in die Sitzung streamen: `send_text` für Befehle, `send_image` für Kameraframes mit einem optionalen Text-Prompt und `send_audio` für rohes PCM-Audio von einem Mikrofon.

Schritt 3 – die Empfangsschleife – wird gleichzeitig ausgeführt und verarbeitet zwei Arten von Nachrichten: `server_content`-Nachrichten (die Textausgabe des Modells) und `tool_call`-Nachrichten (das Modell fordert eine Roboteraktion an). Wenn ein Toolaufruf eingeht, ruft die Schleife `execute_tool` auf – ein Stub, den Sie durch Ihr echtes Roboter-SDK ersetzen – und sendet dann eine `tool_response` zurück, damit das Modell die nächste Aktion auswählen kann.

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

Die Empfangsschleife bleibt nach jeder Toolantwort aktiv. Das Modell erstellt und überarbeitet einen Plan mit langem Horizont, ohne dass Sie die gesamte Aktionssequenz im Voraus codieren müssen.

## Proaktive räumlich-zeitliche Schlussfolgerungen

Die Live API streamt Videoeingaben, aber Videoframes allein lösen keine neue Schlussfolgerungsrunde aus. Videoframes müssen von einem Text- oder Audio-Prompt begleitet werden, um eine Modellantwort auszulösen. Weitere Informationen finden Sie unter
[Live API-Funktionen](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=de) für
mehr Details.

Implementieren Sie einen **Heartbeat**, um proaktive Schlussfolgerungen zu ermöglichen: Senden Sie regelmäßig den
neuesten Kameraframe, gefolgt von einem kurzen Text-Prompt, der das Modell zwingt, die Szene zu
untersuchen und eine explizite Entscheidung zu treffen. Die Videoeingabe ist auf einen Frame pro Sekunde begrenzt.

Fügen Sie diese Coroutine neben der Empfangsschleife aus dem vorherigen Abschnitt hinzu. Sie wird als separate `asyncio`-Aufgabe in derselben Sitzung ausgeführt:

```
async def heartbeat(session, camera):  # camera is your robot camera API
    while True:
        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )
        await asyncio.sleep(1)
```

Sie müssen den Heartbeat während Roboteraktionen nicht pausieren. Wenn er als
**impliziter Erfolgsdetektor** verwendet wird, kann das Modell die laufende Aktion kontinuierlich
beobachten (z. B. ob ein Griff sicher ist, ein Gießvorgang das Ziel erreicht oder ein Objekt richtig platziert wird) und reagieren, sobald das Ergebnis klar ist.

Heartbeat-Nachrichten fungieren als Nutzerrunden und unterbrechen die laufende Modellgenerierung.
Weitere Informationen zur Verarbeitung dieses Verhaltens durch die Live API finden Sie im
[Leitfaden zur Live API unter Unterbrechungen](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=de#interruptions).

## Audioausgabe über externe TTS

Gemini Robotics ER 2 gibt Text zurück. Ihre Anwendung leitet abgeschlossene Antworten
über einen eingefügten Callback an einen separaten TTS-Anbieter (z. B.
[Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de)) weiter.
So behalten Sie die Kontrolle über die Sprachlatenz, die Auswahl der Stimme und das Unterbrechungsverhalten und können TTS-Back-Ends austauschen, ohne die Agentenlogik zu ändern.

Sie können TTS auch als Tool deklarieren, damit das Modell „etwas sagen“ genauso behandelt wie „den Arm bewegen“. Fügen Sie der Liste `tools` aus dem ersten Abschnitt die folgende Funktionsdeklaration hinzu:

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

Wenn Sie TTS in eine Funktionsdeklaration einbinden, verarbeitet das Modell Sprache über denselben Toolaufruf-Pfad wie jede andere Roboteraktion. Ihre Anwendung führt den Aufruf mit einem eingefügten Callback aus.

## Beispiele auf GitHub

Vollständige Arbeitsbeispiele, einschließlich der Spot-Roboter-Snack-Demo und der Tinybot
Pan-Tilt-Hello-World-Demo, finden Sie unter
[Robotics Live API-Beispiele](https://github.com/google-gemini/robotics-samples/tree/main/live-api).

## Nächste Schritte

- [Videoanalyse](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=de) – Momente finden und Fortschritt klassifizieren.
- [Aufgabenorchestrierung](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=de) – Aufgaben mit langem Horizont ohne Streaming.
- [Übersicht über die Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=de) – vollständige Dokumentation zur Live API.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-31 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-31 (UTC)."],[],[]]
