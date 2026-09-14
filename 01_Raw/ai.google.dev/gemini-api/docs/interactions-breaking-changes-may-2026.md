---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=de
fetched_at: 2026-09-14T05:48:28.294331+00:00
title: "Interactions API: Migrationsanleitung f\u00fcr Breaking Changes (Mai 2026) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Interactions API: Migrationsanleitung für Breaking Changes (Mai 2026)

Mit der `v1beta` Interactions API werden wichtige Änderungen eingeführt, die die API-Struktur neu organisieren, um zukünftige Funktionen wie die Steuerung während der Ausführung und asynchrone Toolaufrufe zu unterstützen. Auf dieser Seite wird erläutert, was sich ändert, und es werden Codebeispiele vor und nach der Änderung bereitgestellt, um Ihnen bei der Migration zu helfen. Es gibt zwei Kategorien von Änderungen:

1. [**Schritte-Schema**](#steps-schema): Ein neues `steps` Array ersetzt das
   `outputs` Array und bietet eine strukturierte Zeitachse für jede Interaktionsrunde.
2. [**Konfiguration des Ausgabeformats**](#output-format-config): Ein neues polymorphes
   `response_format` fasst alle Steuerelemente für das Ausgabeformat zusammen und entfernt
   `response_mime_type`.

Folgen Sie der Anleitung unter [Zu neuem Schema migrieren](#how-to-migrate), um Ihre Integration zu
aktualisieren.

## Wichtige Änderung: `outputs` zu `steps`

Das neue Schema ersetzt das `outputs`-Array durch ein `steps`-Array.

- **Alt**: Antworten gaben ein flaches `outputs` Array zurück, das nur den vom Modell generierten Inhalt enthielt.
- **Neues Schema**: Antworten geben ein `steps` Array zurück, das strukturierte Schritte mit Typdiskriminatoren enthält.

`POST /interactions` gibt nur Ausgabeschritte zurück. `GET /interactions/{id}`
gibt die vollständige Zeitachse der Schritte zurück, einschließlich des ersten `user_input`-Schritts.

### Einfache Eingabe/Ausgabe (unär)

#### Vorher (alt)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.6-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Tell me a joke."
  }'
```

```
// Response
{
  "id": "int_123",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "Why did the chicken cross the road?"
    }
  ]
}
```

#### Nachher (neues Schema)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.6-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Tell me a joke.'
});

// Response access (Recommended sugar)
console.log(interaction.output_text);
```

[sdk-convenience]: /gemini-api/docs/interactions-overview#sdk-sugar

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Tell me a joke."
  }'
```

```
// POST Response
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}

// GET /v1beta/interactions/int_123 (returns full timeline including input)
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "content": [
        { "type": "text", "text": "Tell me a joke." }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

### Funktionsaufrufe

Die Anfragestruktur bleibt unverändert, aber die Antwort ersetzt den flachen `outputs`-Inhalt durch strukturierte Schritte.

#### Vorher (alt)

### Python

```
# Accessing function call in legacy schema
for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Calling {output.name} with {output.arguments}")
```

### JavaScript

```
// Accessing function call in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Calling ${output.name} with ${JSON.stringify(output.arguments)}`);
    }
}
```

### REST

```
// Response
{
  "id": "int_001",
  "role": "model",
  "status": "requires_action",
  "outputs": [
    {
      "type": "thought",
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

#### Nachher (neues Schema)

### Python

```
# Accessing function call in new steps schema
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Calling {step.name} with {step.arguments}")
```

### JavaScript

```
// Accessing function call in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Calling ${step.name} with ${JSON.stringify(step.arguments)}`);
    }
}
```

### REST

```
// POST Response
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "thought",
      "summary": [{
        "type": "text",
        "text": "I need to check the weather in Boston..."
      }],
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

### Serverseitige Tools

Serverseitige Tools wie die Google Suche oder die Codeausführung liefern jetzt bestimmte Schritttypen im `steps`-Array. Während das alte Schema diese Vorgänge als bestimmte Inhaltstypen im `outputs`-Array zurückgab, verschiebt das neue Schema sie in das `steps`-Array. In den folgenden Beispielen wird die Google Suche verwendet.

#### Vorher (alt)

### Python

```
# Accessing search results in legacy schema
for output in interaction.outputs:
    if output.type == "google_search_call":
        print(f"Searched for: {output.arguments.queries}")
    elif output.type == "google_search_result":
        print(f"Found results: {output.result.rendered_content}")
```

### JavaScript

```
// Accessing search results in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'google_search_call') {
        console.log(`Searched for: ${output.arguments.queries}`);
    } else if (output.type === 'google_search_result') {
        console.log(`Found results: ${output.result.renderedContent}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// Response
{
  "id": "int_456",
  "outputs": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] }
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "rendered_content": "<div>...</div>",
        "url": "https://www.nfl.com/super-bowl"
      }
    },
    {
      "type": "text",
      "text": "The Kansas City Chiefs won the last Super Bowl.",
      "annotations": [
        {
          "start_index": 4,
          "end_index": 22,
          "source": "https://www.nfl.com/super-bowl"
        }
      ]
    }
  ],
  "status": "completed"
}
```

#### Nachher (neues Schema)

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result[0].search_suggestions}")
```

### JavaScript

```
// Accessing search results in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'google_search_call') {
        console.log(`Searched for: ${step.arguments.queries}`);
    } else if (step.type === 'google_search_result') {
        console.log(`Found results: ${step.result[0].search_suggestions}`);
    }
}
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// POST Response
{
  "id": "int_456",
  "steps": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] },
      "signature": "abc123..."
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "search_suggestions": "<div>...</div>"
      },
      "signature": "abc123..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The Kansas City Chiefs won the last Super Bowl.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.nfl.com/super-bowl",
              "title": "NFL.com",
              "start_index": 4,
              "end_index": 22
            }
          ]
        }
      ]
    }
  ],
  "status": "completed"
}
```

### Streaming

Streaming bietet neue Ereignistypen:

#### Neue Ereignistypen

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### Verworfene Ereignistypen

Die folgenden alten Ereignistypen werden durch die oben aufgeführten neuen Ereignisse ersetzt:

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → ersetzt durch `interaction.in_progress`, `interaction.requires_action` usw.

**Streaming-Funktionsaufrufe**: Wenn Sie Streaming mit Funktionsaufrufen verwenden,
liefert das `step.start`-Ereignis den Funktionsnamen und `step.delta`-Ereignisse
streamen die Argumente als teilweise JSON-Strings (mit `arguments_delta`). Sie
müssen diese Deltas zusammenführen, um die vollständigen Argumente zu erhalten. Dies unterscheidet sich von unären Aufrufen, bei denen Sie das vollständige Funktionsaufrufobjekt auf einmal erhalten.

#### Beispiele

##### Vorher (alt)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain quantum entanglement in simple terms.",
    stream=True,
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
```

### JavaScript

```
// Legacy streaming used content.delta
const stream = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Explain quantum entanglement in simple terms.',
    stream: true,
});

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text') {
            process.stdout.write(chunk.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain quantum entanglement in simple terms.",
    "stream": true
  }'
```

```
// Response (SSE Lines)
// event: interaction.start
// data: {"id": "int_123", "status": "in_progress"}
//
// event: content.start
// data: {"index": 0, "type": "text"}
//
// event: content.delta
// data: {"delta": {"type": "text", "text": "Quantum entanglement is..."}}
//
// event: content.stop
// data: {"index": 0}
//
// event: interaction.complete
// data: {"id": "int_123", "status": "done", "usage": {"total_tokens": 42}}
```

##### Nachher (neues Schema)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.6-flash",
    input="Tell me a story.",
    stream=True,
):
    if event.event_type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Tell me a story.',
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.delta') {  // CHANGED: step.delta instead of content.delta
        if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
 # Opt-in needed before May 26th
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "Accept: text/event-stream" \
   -H "Api-Revision: 2026-05-20" \
   -d '{
     "model": "gemini-3.6-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.6-flash"}, "event_type": "interaction.created"}
 //
 // event: interaction.in_progress
 // data: {"interaction_id": "int_xyz", "event_type": "interaction.in_progress"}
 //
 // event: step.start
 // data: {"index": 0, "step": {"type": "thought", "signature": "abc123..."}, "event_type": "step.start"}
 //
 // event: step.stop
 // data: {"index": 0, "event_type": "step.stop"}
 //
 // event: step.start
 // data: {"index": 1, "step": {"content": [{"text": "Once upon", "type": "text"}], "type": "model_output"}, "event_type": "step.start"}
 //
 // event: step.delta
 // data: {"index": 1, "delta": {"text": " a time...", "type": "text"}, "event_type": "step.delta"}
 //
 // event: step.stop
 // data: {"type": "step.stop", "index": 1, "status": "done"}
 //
 // event: interaction.completed
 // data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}} // NEW: Dedicated completion event
```

### Zustandsloser Unterhaltungsverlauf

Wenn Sie den Unterhaltungsverlauf manuell auf der Clientseite verwalten (zustandsloser Anwendungsfall), müssen Sie die Art und Weise aktualisieren, wie Sie vorherige Runden verknüpfen.

- **Alt**: Entwickler haben oft das `outputs` Array aus Antworten erfasst und in der nächsten Runde im Feld `input` zurückgesendet.
- **Neues Schema**: Sie sollten jetzt das `steps`-Array aus der Antwort erfassen und im Feld `input` der nächsten Anfrage übergeben. Hängen Sie Ihre neue Nutzerrunde als `user_input`-Schritt an.

## Konfiguration des Ausgabeformats: Änderungen an `response_format`

Die aktualisierte API fasst alle Steuerelemente für das Ausgabeformat in einem einheitlichen, polymorphen `response_format`-Feld zusammen. Dadurch wird die Ausgabekonfiguration auf oberster Ebene zentralisiert und `generation_config` konzentriert sich auf das Modellverhalten (z. B. Temperatur, top\_p und Denken).

### Wichtigste Änderungen

- **Die API entfernt `response_mime_type`.** Sie geben den MIME-Typ jetzt pro Formateintrag in `response_format` an.
- **`response_format` ist jetzt ein polymorphes Objekt (oder Array).** Jeder Eintrag hat einen `type`-Diskriminator (`text`, `audio`, `image`) und typspezifische Felder. Wenn Sie mehrere Ausgabemodalitäten anfordern möchten, übergeben Sie ein Array von Formateinträgen.
- **`image_config` wird von `generation_config` nach `response_format` verschoben.**
  Sie geben jetzt Einstellungen für die Bildausgabe wie `aspect_ratio` und `image_size`
  in einem `response_format` Eintrag mit `"type": "image"` an.

### Strukturierte Ausgabe (JSON)

Das neue Schema entfernt das Feld `response_mime_type`. Geben Sie stattdessen den
MIME-Typ und das JSON-Schema in einem `response_format` Objekt mit
`"type": "text"` an.

#### Vorher (alt)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Summarize this article.",
    response_mime_type="application/json",
    response_format={
        "type": "object",
        "properties": {
            "summary": {"type": "string"}
        }
    },
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Summarize this article.',
    response_mime_type: 'application/json',
    response_format: {
        type: 'object',
        properties: {
            summary: { type: 'string' }
        }
    },
});

console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Summarize this article.",
    "response_mime_type": "application/json",
    "response_format": {
      "type": "object",
      "properties": {
        "summary": { "type": "string" }
      }
    }
  }'
```

#### Nachher (neues Schema)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Summarize this article.",
    # response_mime_type is removed — specify mime_type inside response_format
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string"}
            }
        }
    },
)

# Print response
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Summarize this article.',
    // response_mime_type is removed — specify mime_type inside response_format
    response_format: {
        type: 'text',
        mime_type: 'application/json',
        schema: {
            type: 'object',
            properties: {
                summary: { type: 'string' }
            }
        }
    },
});

// Print response
console.log(interaction.output_text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Summarize this article.",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "summary": { "type": "string" }
        }
      }
    }
  }'
```

### Image-Konfiguration

Das neue Schema entfernt `image_config` aus `generation_config`. Sie geben jetzt Einstellungen für die Bildausgabe in einem `response_format` Eintrag mit `"type": "image"` an.

#### Vorher (alt)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Generate an image of a sunset over the ocean.",
    generation_config={
        "image_config": {
            "aspect_ratio": "1:1",
            "image_size": "1K"
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Generate an image of a sunset over the ocean.',
    generation_config: {
        image_config: {
            aspect_ratio: '1:1',
            image_size: '1K'
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### Nachher (neues Schema)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Generate an image of a sunset over the ocean.",
    # image_config is removed from generation_config — use response_format
    response_format={
        "type": "image",
        "mime_type": "image/jpeg",
        "aspect_ratio": "1:1",
        "image_size": "1K"
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Generate an image of a sunset over the ocean.',
    // image_config is removed from generation_config — use response_format
    response_format: {
        type: 'image',
        mime_type: 'image/jpeg',
        aspect_ratio: '1:1',
        image_size: '1K'
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

### Audiokonfiguration

Das neue Schema ersetzt `response_modalities: ["audio"]` durch einen `response_format`-Eintrag mit `"type": "audio"`.

#### Vorher (alt)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    response_modalities: ['audio'],
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_modalities": ["audio"],
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

#### Nachher (neues Schema)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    # response_modalities is removed — use response_format
    response_format={
        "type": "audio"
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-tts-preview',
    input: 'Say cheerfully: Have a wonderful day!',
    // response_modalities is removed — use response_format
    response_format: {
        type: 'audio'
    },
    generation_config: {
        speech_config: [
            { voice: 'Kore' }
        ]
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

Wenn Sie mehrere Ausgabemodalitäten anfordern möchten (z. B. Text und Audio zusammen), übergeben Sie ein Array von Formateinträgen an `response_format` anstelle eines einzelnen Objekts.

## Zu neuem Schema migrieren

### SDK-Nutzer

Führen Sie ein Upgrade auf die neueste SDK-Version durch (Python ≥ 2.0.0, JavaScript ≥ 2.0.0). Das SDK aktiviert automatisch das neue Schema. Es sind keine Codeänderungen erforderlich, außer wie Sie Antworten lesen (siehe Beispiele oben). Beachten Sie, dass in diesen SDK-Versionen nur das neue Schema unterstützt wird. Ältere SDK-Versionen (Python 1.x.x, JavaScript 1.x.x) funktionieren weiterhin, bis das alte Schema am **8. Juni 2026** entfernt wird.

### REST API-Nutzer

Fügen Sie Ihren Anfragen den Header `Api-Revision: 2026-05-20` hinzu, um jetzt das neue Schema zu aktivieren. Nach dem **26. Mai** wird das neue Schema für alle
Anfragen zur Standardeinstellung. Sie können sich mit `Api-Revision: 2026-05-07`
vorübergehend abmelden, bis das alte Schema am **8. Juni** dauerhaft aus der API entfernt wird.

### Zeitachse

| Datum | Phase | SDK-Nutzer | REST API-Nutzer |
| --- | --- | --- | --- |
| **7. Mai** | Opt-in | Neue SDK-Version verfügbar (Python ≥ 2.0.0, JS ≥ 2.0.0). Führen Sie ein Upgrade durch, um das neue Schema automatisch zu erhalten. | Fügen Sie den Header `Api-Revision: 2026-05-20` hinzu, um sich anzumelden. Standardmäßig bleibt das alte Schema. |
| **26. Mai** | Standardeinstellung wechseln | Wenn Sie bereits ein Upgrade durchgeführt haben, sind keine Maßnahmen erforderlich. Ältere SDKs (Python 1.x.x, JS 1.x.x) funktionieren weiterhin, geben aber alte Antworten zurück. | Das neue Schema ist jetzt die Standardeinstellung. Senden Sie den Header `Api-Revision: 2026-05-07`, um sich abzumelden. |
| **8. Juni** | Sonnenuntergang | Die SDK-Versionen Python 1.x.x und JS 1.x.x funktionieren nicht mehr für Interactions API-Aufrufe. | Altes Schema für Interactions API entfernt. `Api-Revision`-Header wird ignoriert. |

## Checkliste für die Migration

### Schritte-Schema (`steps`)

- Aktualisieren Sie den Code, um Antwortinhalte aus dem `steps`-Array anstelle von `outputs` zu lesen. [Beispiele ansehen](#basic-unary).
- Prüfen Sie, ob Ihr Code sowohl `user_input`- als auch `model_output`-Schritttypen verarbeitet. [Beispiele ansehen](#basic-unary).
- (Funktionsaufrufe) Aktualisieren Sie den Code, um `function_call`-Schritte im `steps`-Array zu finden. [Beispiele ansehen](#function-calling).
- (Serverseitige Tools) Aktualisieren Sie den Code, um toolspezifische Schritte zu verarbeiten (z.B. `google_search_call`, `google_search_result`). [Beispiele ansehen](#server-side-tools).
- (Zustandsloser Verlauf) Aktualisieren Sie die Verlaufsverwaltung, um das `steps`-Array im Feld `input` der nächsten Anfrage zu übergeben. [Details ansehen](#stateless-history).
- (Nur Streaming) Aktualisieren Sie den Client, um auf neue SSE-Ereignistypen zu warten (`interaction.created`, `step.delta` usw.). [Beispiele ansehen](#streaming).

### Konfiguration des Ausgabeformats (`response_format`)

- Ersetzen Sie `response_mime_type` durch ein `mime_type`-Feld in `response_format`. [Beispiele ansehen](#structured-output).
- Umschließen Sie Ihr vorhandenes `response_format` JSON-Schema mit einem `{"type": "text", "schema": ...}` Objekt. [Beispiele ansehen](#structured-output).
- (Bildgenerierung) Verschieben Sie `image_config` von `generation_config` zu einem `{"type": "image", ...}`-Eintrag in `response_format`. [Beispiele ansehen](#image-config).
- (Sprachgenerierung) Ersetzen Sie `response_modalities=["audio"]` durch einen `{"type": "audio"}`-Eintrag in `response_format`. [Beispiele ansehen](#audio-config).
- (Multimodal) Konvertieren Sie `response_format` von einem einzelnen Objekt in ein Array, wenn Sie mehrere Ausgabemodalitäten anfordern.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-12 (UTC)."],[],[]]
