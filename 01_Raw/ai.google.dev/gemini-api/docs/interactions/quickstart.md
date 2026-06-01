---
source_url: https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=de
fetched_at: 2026-06-01T19:34:59.352907+00:00
title: "Gemini API \u2013 Kurzanleitung \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini API – Kurzanleitung

In dieser Kurzanleitung erfahren Sie, wie Sie unsere [Bibliotheken](https://ai.google.dev/gemini-api/docs/libraries?hl=de) installieren, Ihre erste Anfrage stellen, Antworten streamen, Unterhaltungen mit mehreren Zügen erstellen und Tools verwenden.

Es gibt zwei Möglichkeiten, eine Anfrage an die Gemini API zu senden:

- ***(Empfohlen)*** Die [Interactions API](https://ai.google.dev/api/interactions-api?hl=de) ist ein neues Primitive mit integrierter Unterstützung für die mehrstufige Verwendung von Tools, Orchestrierung und komplexen Abläufen für die Entscheidungsfindung durch typisierte Ausführungsschritte. Künftig werden neue Modelle, die über die Kernmodelle hinausgehen, sowie neue agentische Funktionen und Tools ausschließlich über die Interactions API eingeführt.
- [`generateContent`](https://ai.google.dev/gemini-api/docs/quickstart?hl=de) bietet eine Möglichkeit, eine zustandslose Antwort von einem Modell zu generieren. Wir empfehlen zwar die Verwendung der Interactions API, `generateContent` wird aber vollständig unterstützt.

In dieser Version der Kurzanleitung wird die Interactions API verwendet, um eine Anfrage an die Gemini API zu senden.

## Hinweis

Wenn Sie die Gemini API verwenden möchten, benötigen Sie einen API-Schlüssel, um Ihre Anfragen zu authentifizieren, Sicherheitslimits durchzusetzen und die Nutzung Ihres Kontos zu verfolgen.

Erstellen Sie kostenlos ein Konto in AI Studio, um loszulegen:

[Gemini API-Schlüssel erstellen](https://aistudio.google.com/app/apikey?hl=de)

## Google GenAI SDK installieren

### Python

Installieren Sie mit [Python 3.9+](https://www.python.org/downloads/) das [`google-genai`-Paket](https://pypi.org/project/google-genai/) mit dem folgenden [pip-Befehl](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```
pip install -q -U google-genai
```

### JavaScript

Installieren Sie mit [Node.js v18+](https://nodejs.org/en/download/package-manager) das [Google Gen AI SDK für TypeScript und JavaScript](https://www.npmjs.com/package/@google/genai) mit dem folgenden [npm-Befehl](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):

```
npm install @google/genai
```

## Text generieren

Verwenden Sie die Methode `interactions.create`, um eine [Textantwort zu generieren](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=de).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in a few words",
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Antworten streamen

Standardmäßig gibt das Modell eine Antwort erst zurück, wenn der gesamte Generierungsprozess abgeschlossen ist. Für eine schnellere, interaktivere Nutzung können Sie die Antwortblöcke [streamen](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=de), während sie generiert werden.

### Python

```
stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in detail",
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const stream = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in detail",
    stream: true,
  });

  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

main();
```

### REST

```
# Use alt=sse for streaming
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in detail",
    "stream": true
  }'
```

## Unterhaltungen über mehrere Themen

Die Gemini API bietet integrierte Unterstützung für die Entwicklung von [Multi-Turn-Unterhaltungen](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=de#multi-turn-conversations).
Übergeben Sie einfach den in der vorherigen Interaktion zurückgegebenen `id` als Parameter `previous_interaction_id`. Der Server verwaltet den Unterhaltungsverlauf automatisch.

### Python

```
interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house."
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const interaction2 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
  });
  console.log("Response 2:", interaction2.output_text);
}

main();
```

### REST

```
# Turn 1: Start the conversation
RESPONSE1=$(curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "I have 2 dogs in my house."
  }')

# Extract the interaction ID
INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

# Turn 2: Continue the conversation
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3-flash-preview\",
    \"input\": \"How many paws are in my house?\",
    \"previous_interaction_id\": \"$INTERACTION_ID\"
  }"
```

## Tools verwenden

Erweitern Sie die Funktionen des Modells, indem Sie [Antworten mit der Google Suche fundieren](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=de), um auf Web-Inhalte in Echtzeit zuzugreifen. Das Modell entscheidet automatisch, wann es suchen soll, führt Abfragen aus und erstellt eine Antwort mit Zitaten.

Das folgende Beispiel zeigt, wie Sie die Google Suche aktivieren:

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  - [{annotation.title}]({annotation.url})")
```

### JavaScript

```
async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
  });

  console.log(interaction.output_text);

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text' && contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              console.log(`  - [${annotation.title}](${annotation.url})`);
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

Die Gemini API unterstützt auch andere integrierte Tools:

- **[Codeausführung](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=de)**:
  Ermöglicht dem Modell, Python-Code zu schreiben und auszuführen, um komplexe mathematische Probleme zu lösen.
- **[URL-Kontext](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=de)**: Damit können Sie Antworten auf bestimmte von Ihnen angegebene Webseiten-URLs stützen.
- **[Dateisuche](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=de)**: Sie können Dateien hochladen und Antworten anhand ihres Inhalts mit semantischer Suche abstützen.
- **[Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=de)**: Damit können Sie Antworten auf Standortdaten stützen und nach Orten, Routen und Karten suchen.
- **[Computernutzung](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=de)**: Ermöglicht dem Modell, mit einem virtuellen Computerbildschirm, einer Tastatur und einer Maus zu interagieren, um Aufgaben auszuführen.

## Benutzerdefinierte Funktionen aufrufen

Verwenden Sie **[Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=de)**, um Modelle mit Ihren benutzerdefinierten Tools und APIs zu verbinden. Das Modell bestimmt, wann Ihre Funktion aufgerufen werden soll, und gibt einen `function_call`-Schritt mit den Argumenten zurück, die Ihre Anwendung ausführen soll.

In diesem Beispiel wird eine Mock-Temperaturfunktion deklariert und geprüft, ob das Modell sie aufrufen möchte.

### Python

```
import json

weather_function = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What's the temperature in London?",
    tools=[weather_function],
)

fc_step = None
for step in interaction.steps:
    if step.type == "function_call":
        fc_step = step
        break

if fc_step:
    print(f"Model requested function: {fc_step.name} with args {fc_step.arguments}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {
                "type": "function_result",
                "name": fc_step.name,
                "call_id": fc_step.id,
                "result": [{"type": "text", "text": json.dumps(mock_result)}],
            }
        ],
        tools=[weather_function],
        previous_interaction_id=interaction.id,
    )
    print("Final Response:", final_interaction.output_text)
```

### JavaScript

```
async function main() {
  const weatherFunction = {
    type: 'function',
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: 'object',
      properties: {
        location: {
          type: 'string',
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const interaction = await ai.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "What's the temperature in London?",
    tools: [weatherFunction],
  });

  const fcStep = interaction.steps.find(s => s.type === 'function_call');
  if (fcStep) {
    console.log(`Model requested function: ${fcStep.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    const finalInteraction = await ai.interactions.create({
      model: 'gemini-3-flash-preview',
      input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [{ type: 'text', text: JSON.stringify(mockResult) }]
      }],
      tools: [weatherFunction],
      previous_interaction_id: interaction.id,
    });

    console.log("Final Response:", finalInteraction.output_text);
  }
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What'\''s the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

## Nächste Schritte

Nachdem Sie nun mit der Gemini API begonnen haben, können Sie sich die folgenden Anleitungen ansehen, um komplexere Anwendungen zu erstellen:

- [Textgenerierung](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=de)
- [Bildgenerierung](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=de)
- [Bildverständnis](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=de)
- [Denken](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=de)
- [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=de)
- [Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=de)
- [Langer Kontext](https://ai.google.dev/gemini-api/docs/long-context?hl=de)
- [Einbettungen](https://ai.google.dev/gemini-api/docs/embeddings?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-01 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-01 (UTC)."],[],[]]
