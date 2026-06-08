---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=de
fetched_at: 2026-06-08T14:55:52.908204+00:00
title: "Langlebiger KI-Agent mit Gemini und Temporal \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Langlebiger KI-Agent mit Gemini und Temporal

In dieser Anleitung erfahren Sie, wie Sie eine
[ReAct-ähnliche](https://arxiv.org/abs/2210.03629) agentische Schleife erstellen, die die
Gemini API für die Schlussfolgerung und [Temporal](https://temporal.io/) für die Dauerhaftigkeit verwendet.
Der vollständige Quellcode für diese Anleitung ist auf
[GitHub](https://github.com/temporal-community/durable-react-agent-gemini) verfügbar.

Der Agent kann Tools aufrufen, z. B. um Wetterwarnungen zu suchen oder eine IP-Adresse zu geolokalisieren. Er wird so lange wiederholt, bis er genügend Informationen für eine Antwort hat.

Was sich von einer typischen Agent-Demo unterscheidet, ist die **Dauerhaftigkeit**. Jeder LLM-Aufruf, jeder Tool-Aufruf und jeder Schritt der agentischen Schleife wird von Temporal gespeichert. Wenn der Prozess abstürzt, die Netzwerkverbindung unterbrochen wird oder ein API-Aufruf eine Zeitüberschreitung verursacht, wiederholt Temporal den Vorgang automatisch und setzt ihn beim letzten abgeschlossenen Schritt fort. Der Unterhaltungsverlauf geht nicht verloren und Tool-Aufrufe werden nicht fälschlicherweise wiederholt.

## Architektur

Die Architektur besteht aus drei Teilen:

- **Workflow**:Die agentische Schleife, die die Ausführungslogik orchestriert.
- **Aktivitäten**:Einzelne Arbeitseinheiten (LLM-Aufrufe, Tool-Aufrufe), die von Temporal dauerhaft gemacht werden.
- **Worker**:Der Prozess, der die Workflows und Aktivitäten ausführt.

In diesem Beispiel werden alle drei Teile in einer einzigen Datei (`durable_agent_worker.py`) platziert. In einer realen Implementierung würden Sie sie trennen, um verschiedene Vorteile bei der Bereitstellung und Skalierbarkeit zu nutzen. Der Code, der dem Agent einen Prompt liefert, wird in einer zweiten Datei (`start_workflow.py`) platziert.

## Vorbereitung

Für diese Anleitung benötigen Sie Folgendes:

- Einen Gemini API-Schlüssel. Sie können einen kostenlos in
  [Google AI Studio](https://aistudio.google.com/apikey?hl=de) erstellen.
- [Python](https://www.python.org/downloads/)-Version 3.10 oder höher.
- Die [Temporal CLI](https://docs.temporal.io/cli) zum Ausführen eines lokalen
  Entwicklungsservers.

## Einrichtung

Bevor Sie beginnen, muss ein
[Temporal-Entwicklungsserver](https://docs.temporal.io/cli#start-dev-server)
lokal ausgeführt werden:

```
temporal server start-dev
```

Installieren Sie als Nächstes die erforderlichen Abhängigkeiten:

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

Erstellen Sie in Ihrem Projektverzeichnis eine `.env`-Datei mit Ihrem Gemini API-Schlüssel. Sie
können einen API-Schlüssel von
[Google AI Studio](https://aistudio.google.com/apikey?hl=de)abrufen.

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## Implementierung

Im weiteren Verlauf dieser Anleitung wird `durable_agent_worker.py` von oben nach unten durchgegangen und der Agent Schritt für Schritt erstellt. Erstellen Sie die Datei und folgen Sie der Anleitung.

### Importe und Sandbox-Einrichtung

Beginnen Sie mit den Importen, die im Voraus definiert werden müssen. Der Block `workflow.unsafe.imports_passed_through()` weist die Workflow-Sandbox von Temporal an, bestimmte Module ohne Einschränkung durchzulassen. Das ist erforderlich, da mehrere Bibliotheken (insbesondere `httpx`, das von `urllib.request.Request` abgeleitet wird) Muster verwenden, die von der Sandbox andernfalls blockiert würden.

```
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    import pydantic_core  # noqa: F401
    import annotated_types  # noqa: F401

    import httpx
    from pydantic import BaseModel, Field
    from google import genai
    from google.genai import types
```

### Systemanweisungen

Definieren Sie als Nächstes die Persönlichkeit des Agenten. Die Systemanweisungen geben an, wie sich das Modell verhalten soll. Dieser Agent wird angewiesen, in Haikus zu antworten, wenn keine Tools erforderlich sind.

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### Tooldefinitionen

Definieren Sie nun die Tools, die der Agent verwenden kann. Jedes Tool ist eine asynchrone Funktion mit einem beschreibenden Docstring. Tools, die Parameter verwenden, haben ein Pydantic-Modell als einziges Argument. Das ist eine Best Practice von Temporal, mit der die Aktivitätssignaturen stabil bleiben, wenn Sie im Laufe der Zeit optionale Felder hinzufügen.

```
import json

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

class GetWeatherAlertsRequest(BaseModel):
    """Request model for getting weather alerts."""

    state: str = Field(description="Two-letter US state code (e.g. CA, NY)")

async def get_weather_alerts(request: GetWeatherAlertsRequest) -> str:
    """Get weather alerts for a US state.

    Args:
        request: The request object containing:
            - state: Two-letter US state code (e.g. CA, NY)
    """
    headers = {"User-Agent": USER_AGENT, "Accept": "application/geo+json"}
    url = f"{NWS_API_BASE}/alerts/active/area/{request.state}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=5.0)
        response.raise_for_status()
        return json.dumps(response.json())
```

Definieren Sie als Nächstes Tools für die Geolokalisierung von IP-Adressen:

```
class GetLocationRequest(BaseModel):
    """Request model for getting location info from an IP address."""

    ipaddress: str = Field(description="An IP address")

async def get_ip_address() -> str:
    """Get the public IP address of the current machine."""
    async with httpx.AsyncClient() as client:
        response = await client.get("https://icanhazip.com")
        response.raise_for_status()
        return response.text.strip()

async def get_location_info(request: GetLocationRequest) -> str:
    """Get the location information for an IP address including city, state, and country.

    Args:
        request: The request object containing:
            - ipaddress: An IP address to look up
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://ip-api.com/json/{request.ipaddress}")
        response.raise_for_status()
        result = response.json()
        return f"{result['city']}, {result['regionName']}, {result['country']}"
```

### Tool-Registry

Erstellen Sie als Nächstes eine Registry, die Tool-Namen Handler-Funktionen zuordnet. Die
`get_tools()` Funktion generiert Gemini-kompatible `FunctionDeclaration` Objekte
aus den Callables mit `FunctionDeclaration.from_callable_with_api_option()`.

```
from typing import Any, Awaitable, Callable

ToolHandler = Callable[..., Awaitable[Any]]

def get_handler(tool_name: str) -> ToolHandler:
    """Get the handler function for a given tool name."""
    if tool_name == "get_location_info":
        return get_location_info
    if tool_name == "get_ip_address":
        return get_ip_address
    if tool_name == "get_weather_alerts":
        return get_weather_alerts
    raise ValueError(f"Unknown tool name: {tool_name}")

def get_tools() -> types.Tool:
    """Get the Tool object containing all available function declarations.

    Uses FunctionDeclaration.from_callable_with_api_option() from the Google GenAI SDK
    to generate tool definitions from the handler functions.
    """
    return types.Tool(
        function_declarations=[
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_weather_alerts, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_location_info, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_ip_address, api_option="GEMINI_API"
            ),
        ]
    )
```

### LLM-Aktivität

Definieren Sie nun die Aktivität, die die Gemini API aufruft. Die Dataclasses `GeminiChatRequest` und `GeminiChatResponse` definieren den Vertrag.

Sie deaktivieren den automatischen Funktionsaufruf, damit der LLM-Aufruf und der Tool-Aufruf als separate Aufgaben behandelt werden. Dadurch wird die Dauerhaftigkeit Ihres Agenten erhöht. Außerdem deaktivieren Sie die integrierten Wiederholungen des SDK (`attempts=1`), da Temporal Wiederholungen dauerhaft verarbeitet.

```
import os
from dataclasses import dataclass

from temporalio import activity

@dataclass
class GeminiChatRequest:
    """Request parameters for a Gemini chat completion."""

    model: str
    system_instruction: str
    contents: list[types.Content]
    tools: list[types.Tool]

@dataclass
class GeminiChatResponse:
    """Response from a Gemini chat completion."""

    text: str | None
    function_calls: list[dict[str, Any]]
    raw_parts: list[types.Part]

@activity.defn
async def generate_content(request: GeminiChatRequest) -> GeminiChatResponse:
    """Execute a Gemini chat completion with tool support."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")
    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(attempts=1),
        ),
    )

    config = types.GenerateContentConfig(
        system_instruction=request.system_instruction,
        tools=request.tools,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    )

    response = await client.aio.models.generate_content(
        model=request.model,
        contents=request.contents,
        config=config,
    )

    function_calls = []
    raw_parts = []
    text_parts = []

    if response.candidates and response.candidates[0].content:
        for part in response.candidates[0].content.parts:
            raw_parts.append(part)
            if part.function_call:
                function_calls.append(
                    {
                        "name": part.function_call.name,
                        "args": dict(part.function_call.args) if part.function_call.args else {},
                    }
                )
            elif part.text:
                text_parts.append(part.text)

    text = "".join(text_parts) if text_parts and not function_calls else None

    return GeminiChatResponse(
        text=text,
        function_calls=function_calls,
        raw_parts=raw_parts,
    )
```

### Dynamische Tool-Aktivität

Definieren Sie als Nächstes die Aktivität, die Tools ausführt. Dabei wird die dynamische Aktivitätsfunktion von Temporal verwendet: Der Tool-Handler (ein Callable) wird über die Funktion `get_handler` aus der Tool-Registry abgerufen. So können verschiedene Agenten definiert werden, indem einfach eine andere Gruppe von Tools und Systemanweisungen angegeben wird. Der Workflow, der die agentische Schleife implementiert, muss nicht geändert werden.

Die Aktivität prüft die Signatur des Handlers, um zu bestimmen, wie Argumente übergeben werden. Wenn der Handler ein Pydantic-Modell erwartet, verarbeitet er das verschachtelte Ausgabeformat, das von Gemini erzeugt wird (z. B. `{"request": {"state": "CA"}}` anstelle von `{"state": "CA"}`).

```
import inspect
from collections.abc import Sequence

from temporalio.common import RawValue

@activity.defn(dynamic=True)
async def dynamic_tool_activity(args: Sequence[RawValue]) -> dict:
    """Execute a tool dynamically based on the activity name."""
    tool_name = activity.info().activity_type
    tool_args = activity.payload_converter().from_payload(args[0].payload, dict)
    activity.logger.info(f"Running dynamic tool '{tool_name}' with args: {tool_args}")

    handler = get_handler(tool_name)

    if not inspect.iscoroutinefunction(handler):
        raise TypeError("Tool handler must be async (awaitable).")

    sig = inspect.signature(handler)
    params = list(sig.parameters.values())

    if len(params) == 0:
        result = await handler()
    else:
        param = params[0]
        param_name = param.name
        ann = param.annotation

        if isinstance(ann, type) and issubclass(ann, BaseModel):
            nested_args = tool_args.get(param_name, tool_args)
            result = await handler(ann(**nested_args))
        else:
            result = await handler(**tool_args)

    activity.logger.info(f"Tool '{tool_name}' result: {result}")
    return result
```

### Der Workflow der agentischen Schleife

Jetzt haben Sie alle Teile, um den Agenten fertigzustellen. Die Klasse `AgentWorkflow` implementiert einen Workflow, der die agentische Schleife enthält. In dieser Schleife wird das LLM über eine Aktivität aufgerufen (wodurch es dauerhaft wird), die Ausgabe wird geprüft und wenn ein Tool vom LLM ausgewählt wurde, wird es über `dynamic_tool_activity` aufgerufen.

In diesem einfachen ReAct-Agent wird die Schleife als abgeschlossen betrachtet und das endgültige LLM-Ergebnis zurückgegeben, sobald das LLM kein Tool mehr verwendet.

```
from datetime import timedelta

@workflow.defn
class AgentWorkflow:
    """Agentic loop workflow that uses Gemini for LLM calls and executes tools."""

    @workflow.run
    async def run(self, input: str) -> str:
        contents: list[types.Content] = [
            types.Content(role="user", parts=[types.Part.from_text(text=input)])
        ]

        tools = [get_tools()]

        while True:
            result = await workflow.execute_activity(
                generate_content,
                GeminiChatRequest(
                    model="gemini-3.5-flash",
                    system_instruction=SYSTEM_INSTRUCTIONS,
                    contents=contents,
                    tools=tools,
                ),
                start_to_close_timeout=timedelta(seconds=60),
            )

            if result.function_calls:
                # Sending the complete raw_parts here ensures Gemini 3 thought
                # signatures are propagated correctly.
                contents.append(types.Content(role="model", parts=result.raw_parts))

                for function_call in result.function_calls:
                    tool_result = await self._handle_function_call(function_call)

                    contents.append(
                        types.Content(
                            role="user",
                            parts=[
                                types.Part.from_function_response(
                                    name=function_call["name"],
                                    response={"result": tool_result},
                                )
                            ],
                        )
                    )
            else:
                return result.text
            # Leave this in place. You will un-comment it during a durability
            # test later on.
            # await asyncio.sleep(10)

    async def _handle_function_call(self, function_call: dict) -> str:
        """Execute a tool via dynamic activity and return the result."""
        tool_name = function_call["name"]
        tool_args = function_call.get("args", {})

        result = await workflow.execute_activity(
            tool_name,
            tool_args,
            start_to_close_timeout=timedelta(seconds=30),
        )

        return result
```

Die agentische Schleife ist vollständig dauerhaft. Wenn der Agent-Worker nach mehreren Iterationen in der Schleife abstürzt, setzt Temporal genau dort fort, wo er aufgehört hat, ohne bereits ausgeführte LLM-Aufrufe oder Tool-Aufrufe wiederholen zu müssen.

### Worker-Start

Verbinden Sie nun alle Teile miteinander. Der Code implementiert die erforderliche Geschäftslogik so, dass es so aussieht, als würde er in einem einzigen Prozess ausgeführt. Durch die Verwendung von Temporal wird er jedoch zu einem ereignisgesteuerten System (insbesondere Event-Sourcing), bei dem die Kommunikation zwischen dem Workflow und den Aktivitäten über Messaging erfolgt, das von Temporal bereitgestellt wird.

Der Temporal-Worker stellt eine Verbindung zum Temporal-Dienst her und fungiert als Scheduler für die Workflow- und Aktivitätsaufgaben. Der Worker registriert den Workflow und beide Aktivitäten und wartet dann auf Aufgaben.

```
import asyncio
from concurrent.futures import ThreadPoolExecutor

from dotenv import load_dotenv
from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter
from temporalio.envconfig import ClientConfig
from temporalio.worker import Worker

async def main():
    config = ClientConfig.load_client_connect_config()
    config.setdefault("target_host", "localhost:7233")
    client = await Client.connect(
        **config,
        data_converter=pydantic_data_converter,
    )

    worker = Worker(
        client,
        task_queue="gemini-agent-python-task-queue",
        workflows=[
            AgentWorkflow,
        ],
        activities=[
            generate_content,
            dynamic_tool_activity,
        ],
        activity_executor=ThreadPoolExecutor(max_workers=10),
    )
    await worker.run()

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
```

## Das Clientskript

Erstellen Sie das Clientskript (`start_workflow.py`). Es sendet eine Abfrage und wartet auf das Ergebnis. Es stellt eine Verbindung zur selben Aufgabenwarteschlange her, auf die im Agent-Worker verwiesen wird. Das Skript `start_workflow` sendet eine Workflow-Aufgabe mit dem Nutzer-Prompt an diese Aufgabenwarteschlange und startet so die Ausführung des Agenten.

```
import asyncio
import sys
import uuid

from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter

async def main():
    client = await Client.connect(
        "localhost:7233",
        data_converter=pydantic_data_converter,
    )

    query = sys.argv[1] if len(sys.argv) > 1 else "Tell me about recursion"

    result = await client.execute_workflow(
        "AgentWorkflow",
        query,
        id=f"gemini-agent-id-{uuid.uuid4()}",
        task_queue="gemini-agent-python-task-queue",
    )
    print(f"\nResult:\n{result}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Agenten ausführen

Starten Sie den Temporal-Entwicklungsserver, falls noch nicht geschehen:

```
temporal server start-dev
```

Starten Sie in einem neuen Terminalfenster den Agent-Worker:

```
python -m durable_agent_worker
```

Senden Sie in einem dritten Terminalfenster eine Abfrage an Ihren Agenten:

```
python -m start_workflow "are there any weather alerts for where I am?"
```

Beachten Sie die Ausgabe im Terminal von `durable_agent_worker`, die die Aktionen zeigt, die in jeder Iteration der agentischen Schleife ausgeführt werden. Das LLM kann die Nutzeranfrage erfüllen, indem es eine Reihe von Tools aufruft, die ihm zur Verfügung stehen. Die ausgeführten Schritte können Sie in der Temporal UI unter `http://localhost:8233/namespaces/default/workflows` sehen.

Probieren Sie verschiedene Prompts aus, um zu sehen, wie der Agent Schlussfolgerungen zieht und Tools aufruft:

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

Für den letzten Prompt sind keine Tools erforderlich. Daher antwortet der Agent in einem Haiku basierend auf den `SYSTEM_INSTRUCTIONS`.

## Dauerhaftigkeit testen (optional)

Durch die Verwendung von Temporal kann Ihr Agent Fehler nahtlos überstehen. Sie können dies mit zwei verschiedenen Tests prüfen.

### Netzwerkausfall simulieren

In diesem Test deaktivieren Sie vorübergehend die Internetverbindung Ihres Computers, senden einen Workflow, beobachten, wie Temporal den Vorgang automatisch wiederholt, und stellen dann die Netzwerkverbindung wieder her, um zu sehen, wie der Vorgang wiederhergestellt wird.

1. Trennen Sie Ihren Computer vom Internet (z. B. deaktivieren Sie das WLAN).
2. Senden Sie einen Workflow:

   ```
   python -m start_workflow "tell me a joke"
   ```
3. Prüfen Sie die Temporal UI (`http://localhost:8233`). Sie sehen, dass die LLM-Aktivität fehlschlägt und Temporal die Wiederholungen automatisch im Hintergrund verwaltet.
4. Stellen Sie die Internetverbindung wieder her.
5. Beim nächsten automatischen Wiederholungsversuch wird die Gemini API erfolgreich erreicht und das endgültige Ergebnis wird im Terminal ausgegeben.

### Worker-Absturz überstehen

In diesem Test beenden Sie den Worker während der Ausführung und starten ihn neu. Temporal wiederholt den Workflow-Verlauf (Event-Sourcing) und setzt ihn bei der letzten abgeschlossenen Aktivität fort. Bereits abgeschlossene LLM-Aufrufe und Tool-Aufrufe werden nicht wiederholt.

1. Um Zeit zu haben, den Worker zu beenden, öffnen Sie `durable_agent_worker.py` und heben Sie vorübergehend die Auskommentierung von `await asyncio.sleep(10)` in der `run`-Schleife von `AgentWorkflow` auf.
2. Starten Sie den Worker neu:

   ```
   python -m durable_agent_worker
   ```
3. Senden Sie eine Abfrage, die mehrere Tools auslöst:

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. Beenden Sie den Worker-Prozess jederzeit vor Abschluss (`Ctrl-C` im Worker-Terminal oder mit `kill %1`, wenn er im Hintergrund ausgeführt wird).
5. Starten Sie den Worker neu:

   ```
   python -m durable_agent_worker
   ```

Temporal wiederholt den Workflow-Verlauf. Die bereits abgeschlossenen LLM-Aufrufe und Tool-Aufrufe werden **nicht** noch einmal ausgeführt. Ihre Ergebnisse werden sofort aus dem Verlauf (dem Ereignisprotokoll) wiedergegeben. Der Workflow wird erfolgreich abgeschlossen.

## Weitere Ressourcen

- [Temporal-Dokumentation](https://docs.temporal.io/)
- [Temporal Python SDK](https://docs.temporal.io/develop/python)
- [Google GenAI SDK](https://googleapis.github.io/python-genai/)
- [Quellcode für diese Anleitung](https://github.com/temporal-community/durable-react-agent-gemini)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-05-19 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-05-19 (UTC)."],[],[]]
