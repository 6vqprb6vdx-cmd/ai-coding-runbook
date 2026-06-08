---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=pl
fetched_at: 2026-06-08T15:00:40.581029+00:00
title: "Interfejs API interakcji: przewodnik po migracji w zwi\u0105zku ze zmianami powoduj\u0105cymi niezgodno\u015b\u0107 (maj 2026\u00a0r.) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Interfejs API interakcji: przewodnik po migracji w związku ze zmianami powodującymi niezgodność (maj 2026 r.)

Interfejs `v1beta` Interactions API wprowadza zmiany powodujące niezgodność wsteczną, które zmieniają strukturę interfejsu API, aby obsługiwać przyszłe funkcje, takie jak sterowanie w trakcie lotu i asynchroniczne wywołania narzędzi. Na tej stronie wyjaśniamy, co się zmienia, i podajemy przykłady kodu przed i po zmianach, aby ułatwić Ci migrację. Istnieją 2 kategorie zmian:

1. [**Schemat kroków:**](#steps-schema) nowa tablica `steps` zastępuje tablicę `outputs`, zapewniając uporządkowaną oś czasu każdej interakcji.
2. [**Konfiguracja formatu wyjściowego:**](#output-format-config) nowy polimorficzny
   `response_format` konsoliduje wszystkie elementy sterujące formatem wyjściowym i usuwa
   `response_mime_type`.

Aby zaktualizować integrację, wykonaj czynności opisane w sekcji [Jak przeprowadzić migrację do nowego schematu](#how-to-migrate).

## Najważniejsza zmiana: `outputs` na `steps`

Nowy schemat zastępuje tablicę `outputs` tablicą `steps`.

- **Starsza wersja:** odpowiedzi zwracały płaską tablicę `outputs` zawierającą tylko wygenerowaną przez model treść.
- **Nowy schemat:** odpowiedzi zwracają tablicę `steps` zawierającą uporządkowane kroki z dyskryminatorami typu.

`POST /interactions` zwraca tylko kroki wyjściowe. `GET /interactions/{id}`
zwraca pełną oś czasu kroków, w tym początkowy krok `user_input`.

### Podstawowe dane wejściowe/wyjściowe (unarne)

#### Przed (starsza wersja)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
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
    "model": "gemini-3.5-flash",
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

#### Po aktualizacji (nowy schemat)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

// Response access (Recommended sugar)
console.log(interaction.output_text);
```

[sdk-convenience]: /gemini-api/docs/interactions#convenience-properties

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
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

### Wywoływanie funkcji

Struktura żądania pozostaje bez zmian, ale odpowiedź zastępuje płaską treść`outputs` uporządkowanymi krokami.

#### Przed (starsza wersja)

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
        console.log(`Calling {output.name} with {JSON.stringify(output.arguments)}`);
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

#### Po aktualizacji (nowy schemat)

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
        console.log(`Calling {step.name} with {JSON.stringify(step.arguments)}`);
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

### Narzędzia po stronie serwera

Narzędzia po stronie serwera (np. wyszukiwarka Google czy wykonywanie kodu) zwracają teraz w tablicy `steps` określone typy kroków. W starszym schemacie te operacje były zwracane jako określone typy treści w tablicy `outputs`, a w nowym schemacie są przenoszone do tablicy `steps`. W przykładach poniżej używamy wyszukiwarki Google.

#### Przed (starsza wersja)

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
        console.log(`Searched for: {output.arguments.queries}`);
    } else if (output.type === 'google_search_result') {
        console.log(`Found results: {output.result.renderedContent}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
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

#### Po aktualizacji (nowy schemat)

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result.search_suggestions}")
```

### JavaScript

```
// Accessing search results in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'google_search_call') {
        console.log(`Searched for: {step.arguments.queries}`);
    } else if (step.type === 'google_search_result') {
        console.log(`Found results: {step.result.searchSuggestions}`);
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
    "model": "gemini-3.5-flash",
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

Streaming udostępnia nowe typy zdarzeń:

#### Nowe typy zdarzeń

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### Wycofane typy zdarzeń

Te starsze typy zdarzeń zostały zastąpione nowymi zdarzeniami wymienionymi powyżej:

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → zastąpione przez `interaction.in_progress`, `interaction.requires_action` itp.

**Wywoływanie funkcji strumieniowych:** gdy używasz strumieniowania z wywoływaniem funkcji, zdarzenie `step.start` dostarcza nazwę funkcji, a zdarzenia `step.delta` przesyłają argumenty jako częściowe ciągi JSON (za pomocą `arguments_delta`). Aby uzyskać pełne argumenty, musisz zgromadzić te różnice. Różni się to od wywołań binarnych, w których od razu otrzymujesz cały obiekt wywołania funkcji.

#### Przykłady

##### Przed (starsza wersja)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: 'gemini-3.5-flash',
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
    "model": "gemini-3.5-flash",
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

##### Po aktualizacji (Nowy schemat)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.5-flash",
    input="Tell me a story.",
    stream=True,
):
    if event.type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a story.',
    stream: true,
});

for await (const event of stream) {
    if (event.type === 'step.delta') {  // CHANGED: step.delta instead of content.delta
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
     "model": "gemini-3.5-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.5-flash"}, "event_type": "interaction.created"}
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

### Historia rozmowy bezstanowej

Jeśli zarządzasz historią rozmów ręcznie po stronie klienta (przypadek użycia bezstanowego), musisz zaktualizować sposób łączenia poprzednich tur.

- **Starsze**: deweloperzy często zbierali tablicę `outputs` z odpowiedzi i odsyłali ją w polu `input` w kolejnej turze.
- **Nowy schemat:** teraz musisz zebrać tablicę `steps` z odpowiedzi i przekazać ją w polu `input` kolejnego żądania, dodając nową turę użytkownika jako krok `user_input`.

## Konfiguracja formatu wyjściowego: `response_format` zmiany

Zaktualizowany interfejs API łączy wszystkie opcje formatu wyjściowego w ujednolicone, polimorficzne pole `response_format`. Centralizuje to konfigurację danych wyjściowych na najwyższym poziomie i sprawia, że `generation_config` koncentruje się na zachowaniu modelu (np. temperaturze, top\_p i procesie myślowym).

### Najważniejsze zmiany

- **Interfejs API usuwa `response_mime_type`.** Teraz możesz określić typ MIME dla każdego wpisu formatu w sekcji `response_format`.
- **`response_format` jest teraz obiektem polimorficznym (lub tablicą).** Każdy wpis ma wyróżnik `type` (`text`, `audio`, `image`) i pola specyficzne dla typu. Aby poprosić o wiele trybów wyjściowych, przekaż tablicę wpisów formatu.
- **`image_config` przenosi się z `generation_config` do `response_format`.**
  Ustawienia wyjściowe obrazu, takie jak `aspect_ratio` i `image_size`, określasz teraz we wpisie `response_format` z parametrem `"type": "image"`.

### Uporządkowane dane wyjściowe (JSON)

Nowy schemat usuwa pole `response_mime_type`. Zamiast tego określ typ MIME i schemat JSON w obiekcie `response_format` z wartością `"type": "text"`.

#### Przed (starsza wersja)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: 'gemini-3.5-flash',
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
    "model": "gemini-3.5-flash",
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

#### Po aktualizacji (nowy schemat)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: 'gemini-3.5-flash',
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
    "model": "gemini-3.5-flash",
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

### Konfiguracja obrazu

Nowy schemat usuwa `image_config` z `generation_config`. Ustawienia wyjściowe obrazu określasz teraz w `response_format` z `"type": "image"`.

#### Przed (starsza wersja)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: 'gemini-3.5-flash',
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
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### Po aktualizacji (nowy schemat)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: 'gemini-3.5-flash',
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
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

Aby poprosić o wiele trybów wyjściowych (np. tekst i dźwięk), przekaż do funkcji `response_format` tablicę wpisów formatu zamiast pojedynczego obiektu.

## Jak przeprowadzić migrację do nowego schematu

### Użytkownicy pakietu SDK

Uaktualnij pakiet SDK do najnowszej wersji (Python ≥2.0.0, JavaScript ≥2.0.0). Pakiet SDK automatycznie włącza nowy schemat – nie musisz wprowadzać żadnych zmian w kodzie poza aktualizacją sposobu odczytywania odpowiedzi (patrz przykłady powyżej). Pamiętaj, że w tych wersjach pakietu SDK obsługiwany jest tylko nowy schemat. Starsze wersje pakietu SDK (Python 1.x.x, JavaScript 1.x.x) będą działać do momentu usunięcia starszego schematu **8 czerwca 2026 r.**

### Użytkownicy interfejsu API REST

Dodaj do żądań nagłówek `Api-Revision: 2026-05-20`, aby już teraz włączyć nowy schemat. Po **26 maja** nowy schemat stanie się domyślnym schematem wszystkich żądań. Możesz tymczasowo zrezygnować z tej funkcji za pomocą `Api-Revision: 2026-05-07` do **8 czerwca**, kiedy interfejs API trwale usunie starszy schemat.

### Oś czasu

| Data | Faza | Użytkownicy pakietu SDK | Użytkownicy interfejsu API REST |
| --- | --- | --- | --- |
| **7 maja** | Włącz | Dostępna jest nowa wersja pakietu SDK (Python ≥2.0.0, JS ≥2.0.0). Przejdź na wyższą wersję, aby automatycznie uzyskać nowy schemat. | Aby wyrazić zgodę, dodaj nagłówek `Api-Revision: 2026-05-20`. Domyślne ustawienie pozostaje starsze. |
| **26 maja** | Domyślne odwrócenie | Jeśli masz już uaktualnioną wersję, nie musisz nic robić. Starsze pakiety SDK (Python 1.x.x, JS 1.x.x) nadal działają, ale zwracają starsze odpowiedzi. | Nowy schemat jest teraz domyślny. Wyślij nagłówek `Api-Revision: 2026-05-07`, aby zrezygnować. |
| **8 czerwca** | Zachód słońca | Wersje pakietów SDK Python 1.x.x i JS 1.x.x przestaną działać w przypadku wywołań interfejsu Interactions API. | Usunięto starszy schemat interfejsu API interakcji. Nagłówek `Api-Revision` został zignorowany. |

## Lista kontrolna migracji

### Schemat kroków (`steps`)

- Zaktualizuj kod, aby odczytywać treść odpowiedzi z tablicy `steps` zamiast z `outputs`. [Zobacz przykłady](#basic-unary)
- Sprawdź, czy kod obsługuje typy kroków `user_input` i `model_output`. [Zobacz przykłady](#basic-unary)
- (Function Calling) Zaktualizuj kod, aby znaleźć kroki `function_call` w tablicy `steps`. [Zobacz przykłady](#function-calling)
- (Narzędzia po stronie serwera) Zaktualizuj kod, aby obsługiwał kroki specyficzne dla narzędzia (np. `google_search_call`, `google_search_result`). [Zobacz przykłady](#server-side-tools)
- (Historia bezstanowa) Zaktualizuj zarządzanie historią, aby przekazywać tablicę `steps` w polu `input` następnego żądania. [Zobacz szczegóły](#stateless-history)
- (Tylko przesyłanie strumieniowe) Zaktualizuj klienta, aby nasłuchiwał nowych typów zdarzeń SSE (`interaction.created`, `step.delta` itp.). [Zobacz przykłady](#streaming)

### Konfiguracja formatu wyjściowego (`response_format`)

- Zastąp `response_mime_type` polem `mime_type` wewnątrz `response_format`. [Zobacz przykłady](#structured-output)
- Umieść istniejący schemat JSON `response_format` w obiekcie `{"type": "text", "schema": ...}`. [Zobacz przykłady](#structured-output)
- (Generowanie obrazów) Przenieś `image_config` z kampanii `generation_config` do pozycji `{"type": "image", ...}` w sekcji `response_format`. [Zobacz przykłady](#image-config)
- (Multimodal) Konwertuj `response_format` z pojedynczego obiektu na tablicę, gdy prosisz o wiele rodzajów danych wyjściowych.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-01 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-01 UTC."],[],[]]
