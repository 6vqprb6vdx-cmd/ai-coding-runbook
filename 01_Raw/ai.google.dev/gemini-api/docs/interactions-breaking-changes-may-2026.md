---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq
fetched_at: 2026-10-26T05:55:12.842333+00:00
title: "API-ja e nd\u00ebrveprimeve: Udh\u00ebzuesi i migrimit t\u00eb ndryshimeve t\u00eb m\u00ebdha (maj 2026) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs?hl=sq)

Dërgo komente

# API-ja e ndërveprimeve: Udhëzuesi i migrimit të ndryshimeve të mëdha (maj 2026)

API-ja e "Interaksioneve" e `v1beta` po prezanton ndryshime të mëdha që ristrukturojnë formën e API-së për të mbështetur aftësitë e ardhshme si drejtimi gjatë fluturimit dhe thirrjet asinkrone të veglave. Kjo faqe shpjegon se çfarë po ndryshon dhe ofron shembuj kodi para dhe pas për të të ndihmuar të migrosh. Ka dy kategori
ndryshimesh:

1. [**Skema e hapave**](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq#steps-schema):
   Një matricë e re `steps` zëvendëson matricën `outputs`, duke ofruar një kronologji të strukturuar të çdo radhe ndërveprimi.
2. [**Konfigurimi i formatit të daljes**](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq#output-format-config):
   Një `response_format` i ri polimorfik konsolidon të gjitha kontrollet e formatit të daljes
   dhe heq `response_mime_type`.

Ndiq hapat në
[Si të migrosh në skemën e re](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq#how-to-migrate)
për të përditësuar integrimin tënd.

## Ndryshimi kryesor: `outputs` në `steps`

Skema e re zëvendëson matricën `outputs` me një matricë `steps`.

- **Legacy**: Përgjigjet kthyen një grup të sheshtë `outputs` që përmban vetëm përmbajtjen e gjeneruar të modelit.
- **Skema e re**: Përgjigjet kthejnë një matricë `steps` që përmban hapa të strukturuar me dallues të llojit.

`POST /interactions` kthen vetëm hapat e daljes. `GET /interactions/{id}`
rikthen kronologjinë e plotë të hapave, duke përfshirë hapin fillestar `user_input`.

### Hyrja/dalja bazë (unare)

#### Para (versioni i vjetër)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.8-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.outputs[-1].text);
```

### PUSHIM

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
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

#### Pas (skema e re)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.8-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Tell me a joke.'
});

// Response access (Recommended sugar)
console.log(interaction.output_text);
```

[sdk-convenience]: /gemini-api/docs/interactions-overview#sdk-sugar

### PUSHIM

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
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

### Thirrje funksioni

Struktura e kërkesës mbetet e pandryshuar, por përgjigjja zëvendëson përmbajtjen e thjeshtë të `outputs` me hapa të strukturuar.

#### Para (versioni i vjetër)

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

### PUSHIM

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

#### Pas (skema e re)

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

### PUSHIM

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

### Veglat në anën e serverit

Veglat në anën e serverit (si p.sh. "Kërko në Google" ose "Ekzekutimi i kodit") tani japin lloje specifike hapash në matricën `steps`. Ndërkohë që skema e trashëguar i kthente këto operacione si lloje specifike përmbajtjeje brenda matricës `outputs`, skema e re i zhvendos ato në matricën `steps`. Shembujt e mëposhtëm përdorin "Kërko në Google".

#### Para (versioni i vjetër)

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

### PUSHIM

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
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

#### Pas (skema e re)

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

### PUSHIM

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
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

### Transmetimi

Transmetimi ekspozon lloje të reja ngjarjesh:

#### Llojet e reja të ngjarjeve

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### Llojet e ngjarjeve të zhvlerësuara

Llojet e mëposhtme të ngjarjeve të trashëguara zëvendësohen nga ngjarjet e reja të listuara më sipër:

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → zëvendësuar nga `interaction.in_progress`, `interaction.requires_action` etj.

**Thirrjet e funksionit të transmetimit**: Kur përdor transmetimin me thirrjen e funksionit,
ngjarja `step.start` jep emrin e funksionit dhe ngjarjet `step.delta`
transmetojnë argumentet si vargje të pjesshme JSON (duke përdorur `arguments_delta`). Duhet
t'i mbledhësh këto delta për të marrë argumentet e plota. Kjo ndryshon nga thirrjet unare ku ti merr objektin e plotë të thirrjes së funksionit menjëherë.

#### Shembuj

##### Para (i vjetër)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
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

### PUSHIM

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
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

##### Pas (skema e re)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
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
     "model": "gemini-3.8-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.8-flash"}, "event_type": "interaction.created"}
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

### Historiku i bisedave pa gjendje

Nëse e menaxhon historikun e bisedave në mënyrë manuale në anën e klientit (rasti i përdorimit pa gjendje), duhet të përditësosh mënyrën se si i lidh bashkëbisedimet e mëparshme.

- **E vjetër**: Zhvilluesit shpesh mblidhnin matricën `outputs` nga përgjigjet dhe i dërgonin ato mbrapsht në fushën `input` në radhën tjetër.
- **Skema e re**: Tani duhet të mbledhësh matricën `steps` nga përgjigjja dhe ta kalosh atë në fushën `input` të kërkesës tjetër, duke shtuar radhën e përdoruesit të ri si një hap `user_input`.

## Konfigurimi i formatit të daljes: `response_format` ndryshime

API-ja e përditësuar i konsolidon të gjitha kontrollet e formatit të daljes në një fushë të unifikuar dhe polimorfike `response_format`. Kjo e centralizon konfigurimin e daljes në nivelin më të lartë dhe e mban `generation_config` të fokusuar te sjellja e modelit (si p.sh. temperatura, top\_p dhe arsyetimi).

### Ndryshimet kryesore

- **API-ja heq `response_mime_type`.** Tani specifikon llojin e MIME-s për hyrjen e formatit brenda `response_format`.
- **`response_format` është tani një objekt (ose matricë) polimorfik.** Çdo hyrje ka një diskriminues `type` (`text`, `audio`, `image`) dhe fusha specifike për llojin. Për të kërkuar modalitete të shumëfishta të rezultateve, kalo një varg hyrjesh të formatit.
- **`image_config` zhvendoset nga `generation_config` në `response_format`.**
  Tani mund të specifikosh cilësimet e nxjerrjes së imazhit si p.sh. `aspect_ratio` dhe `image_size`
  në një hyrje të `response_format` me `"type": "image"`.

### Dalja e strukturuar (JSON)

Skema e re heq fushën `response_mime_type`. Në vend të kësaj, specifikoni
Lloji MIME dhe skema JSON brenda një objekti `response_format` me
`"type": "text"`.

#### Para (trashëgimia)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
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

### PUSHIM

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
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

#### Pas (skema e re)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
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

### PUSHIM

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
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

### Konfigurimi i imazhit

Skema e re heq `image_config` nga `generation_config`. Tani mund të specifikosh
cilësimet e nxjerrjes së imazheve në një hyrje të `response_format` me `"type": "image"`.

#### Para (versioni i vjetër)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
    input: 'Generate an image of a sunset over the ocean.',
    generation_config: {
        image_config: {
            aspect_ratio: '1:1',
            image_size: '1K'
        }
    },
});
```

### PUSHIM

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### Pas (skema e re)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
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
    "model": "gemini-3.8-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

### Konfigurimi i audios

Skema e re zëvendëson `response_modalities: ["audio"]` me një hyrje të `response_format` të `"type": "audio"`.

#### Para (versioni i vjetër)

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

### PUSHIM

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

#### Pas (skema e re)

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

Për të kërkuar modalitete të shumta të daljes (për shembull, tekst dhe audio së bashku),
transmeto një grup hyrjesh formati te `response_format` në vend të një objekti të vetëm.

## Si të migrosh te skema e re

### Përdoruesit e SDK-së

Përmirëso në versionin më të fundit të SDK-së (Python ≥2.0.0, JavaScript ≥2.0.0). SDK-ja të regjistron automatikisht në skemën e re - nuk nevojiten ndryshime të kodit përveç përditësimit të mënyrës se si i lexon përgjigjet (shiko shembujt më sipër). Ki parasysh se vetëm skema e re mbështetet në këto versione të SDK-së. Versionet më të vjetra të SDK-së (Python 1.x.x, JavaScript 1.x.x) do të vazhdojnë të funksionojnë derisa skema e trashëguar të hiqet më **8 qershor 2026**.

### Përdoruesit e REST API

Shto titullin `Api-Revision: 2026-05-20` në kërkesat e tua për t'u regjistruar në
skemën e re tani. Pas datës **26 maj**, skema e re bëhet e parazgjedhura për të gjitha kërkesat. Mund të tërhiqesh përkohësisht me `Api-Revision: 2026-05-07`
deri më **8 qershor**, kur API-ja do të heqë përgjithmonë skemën e vjetër.

### Kronologjia

| Data | Faza | Përdoruesit e SDK-së | Përdoruesit e REST API |
| --- | --- | --- | --- |
| **7 maj** | Prano | Ofrohet version i ri i SDK-së (Python ≥2.0.0, JS ≥2.0.0). Përmirësoje për të marrë automatikisht skemën e re. | Shto titullin `Api-Revision: 2026-05-20` për t'u regjistruar. Parazgjedhja mbetet e trashëguar. |
| **26 maj** | Përmbysja e parazgjedhur | Nuk nevojitet asnjë veprim nëse është përmirësuar tashmë. SDK-të më të vjetra (Python 1.x.x, JS 1.x.x) funksionojnë ende, por kthejnë përgjigje të vjetra. | Skema e re tani është e parazgjedhura. Dërgo titullin "`Api-Revision: 2026-05-07`" për t'u tërhequr. |
| **8 qershor** | Perëndimi i diellit | Versionet e SDK-së në Python 1.x.x dhe JS 1.x.x do të prishen për thirrjet e API-së së "Ndërveprimeve". | Skema e vjetër u hoq për Interactions API. Titulli "`Api-Revision`" u shpërfill. |

## Lista e kontrollit për migrimin

### Skema e hapave (`steps`)

- Përditëso kodin për të lexuar përmbajtjen e përgjigjes nga matrica `steps` në vend të `outputs`.
  [Shiko shembujt](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq#basic-unary).
- Verifiko që kodi yt të trajtojë të dyja llojet e hapave `user_input` dhe `model_output`.
  [Shiko shembujt](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq#basic-unary).
- (Thirrja e funksionit) Përditëso kodin për të gjetur `function_call` hapa në vargun `steps`.
  [Shiko shembujt](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq#function-calling).
- (Veglat në anën e serverit) Përditëso kodin për të administruar hapat specifikë të veglave (p.sh. `google_search_call`, `google_search_result`).
  [Shiko shembujt](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq#server-side-tools).
- (Stateless History) Update history management to pass the `steps` array in the `input` field of the next request.
  [Shiko detajet](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq#stateless-history).
- (Vetëm transmetimi) Përditëso klientin për të dëgjuar për llojet e reja të ngjarjeve SSE (`interaction.created`, `step.delta` etj.).
  [Shiko shembujt](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq#streaming).

### Konfigurimi i formatit të daljes (`response_format`)

- Zëvendëso `response_mime_type` me një fushë `mime_type` brenda `response_format`.
  [Shiko shembujt](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq#structured-output).
- Mbështill skemën ekzistuese JSON të `response_format` brenda një objekti të `{"type": "text", "schema": ...}`.
  [Shiko shembujt](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq#structured-output).
- (Gjenerimi i imazheve) Zhvendos `image_config` nga `generation_config` te një hyrje `{"type": "image", ...}` në `response_format`.
  [Shiko shembujt](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq#image-config).
- (Gjenerimi i të folurit) Zëvendëso `response_modalities=["audio"]` me një hyrje `{"type": "audio"}` në `response_format`.
  [Shiko shembujt](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=sq#audio-config).
- (Multimodal) Konverto `response_format` nga një objekt i vetëm në një grup kur kërkon modalitete të shumëfishta të daljes.

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-15 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-15 UTC."],[],[]]
