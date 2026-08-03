---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=de
fetched_at: 2026-08-03T04:33:06.153599+00:00
title: "Tokens verstehen und z\u00e4hlen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Tokens verstehen und zählen

Gemini und andere generative KI-Modelle verarbeiten Eingaben und Ausgaben mit einer Granularität, die als *Token* bezeichnet wird.

**Bei Gemini-Modellen entspricht ein Token etwa 4 Zeichen.
100 Tokens entsprechen etwa 60–80 englischen Wörtern.**

## Informationen zu Tokens

Tokens können einzelne Zeichen wie `z` oder ganze Wörter wie `cat` sein. Lange Wörter werden in mehrere Tokens aufgeteilt. Die Menge aller vom Modell verwendeten Tokens wird als Vokabular bezeichnet und der Vorgang, Text in Tokens aufzuteilen, als *Tokenisierung*.

Wenn die Abrechnung aktiviert ist, werden die [Kosten eines Aufrufs der Gemini API](https://ai.google.dev/pricing?hl=de) teilweise durch die Anzahl der Eingabe- und Ausgabetokens bestimmt. Daher kann es hilfreich sein, zu wissen, wie Tokens gezählt werden.

## Tokens zählen

Alle Eingaben und Ausgaben der Gemini API werden tokenisiert, einschließlich Text, Bilddateien und anderer nicht textbasierter Modalitäten.

Sie können Tokens auf folgende Arten zählen:

- **Rufen Sie `count_tokens` mit der Eingabe der Anfrage auf.** Gibt die Gesamtzahl der Tokens *nur in der Eingabe* zurück. Führen Sie diesen Aufruf aus, bevor Sie Eingaben senden, um die Größe Ihrer Anfragen zu prüfen.
- **Verwenden Sie die `usage` in der Antwort auf die Interaktion.** Gibt die Anzahl der Tokens für Eingabe (`total_input_tokens`), Ausgabe (`total_output_tokens`), Überlegung (`total_thought_tokens`), Cache-Inhalte (`total_cached_tokens`), Toolnutzung (`total_tool_use_tokens`) und insgesamt (`total_tokens`) zurück.

### Text-Tokens zählen

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
const countResponse = await client.models.countTokens({
    model: "gemini-3.6-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### Tokens für Mehrfachdialoge zählen

Zählen Sie Tokens im Unterhaltungsverlauf mit `previous_interaction_id`:

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    input="What's my name?",
    previous_interaction_id=interaction1.id
)

# Usage includes tokens from both turns
print(f"Input tokens: {interaction2.usage.total_input_tokens}")
print(f"Output tokens: {interaction2.usage.total_output_tokens}")
print(f"Total tokens: {interaction2.usage.total_tokens}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// First interaction
const interaction1 = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### Multimodale Tokens zählen

Alle Eingaben für die Gemini API werden tokenisiert, einschließlich Bilder, Videos und Audio.
Wichtige Informationen zur Tokenisierung:

- **Bilder**: Bilder mit ≤ 384 Pixeln in beiden Dimensionen werden als 258 Tokens gezählt. Größere Bilder werden in 768 × 768 Pixel große Kacheln unterteilt, die jeweils als 258 Tokens gezählt werden.
- **Video**: 263 Tokens pro Sekunde
- **Audio**: 32 Tokens pro Sekunde

#### Bild-Tokens

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Tell me about this image"},
        {"type": "image", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type}
    ]
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const uploadedFile = await client.files.upload({
    file: "path/to/image.jpg",
    config: { mimeType: "image/jpeg" }
});

// Count tokens
const countResponse = await client.models.countTokens({
    model: "gemini-3.6-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

**Beispiel für Inline-Daten** :

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Describe this image"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.usage)
```

#### Video-Tokens

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 263 * 60 = 15,780 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### Audio-Tokens

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### Tokens für Systemanweisungen zählen

Systemanweisungen werden als Teil der Eingabetokens gezählt:

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### Tool-Tokens zählen

Tools (Funktionen, Code-Ausführung, Google Suche) werden ebenfalls gezählt:

### Python

```
# This will only work for SDK newer than 2.0.0
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## Kontextfenster

Jedes Gemini-Modell hat eine maximale Anzahl von Tokens, die es verarbeiten kann. Das Kontextfenster definiert das kombinierte Limit für Eingabe- und Ausgabetokens.

### Größe des Kontextfensters programmatisch abrufen

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.6-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.6-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

Die Größen der Kontextfenster finden Sie auf der Seite „[Modelle](https://ai.google.dev/gemini-api/docs/models?hl=de)“.

## Nächste Schritte

- [Textgenerierung](https://ai.google.dev/gemini-api/docs/text-generation?hl=de): Grundlagen der Generierung
- [Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de): Kosten mit Caching senken
- [Preise](https://ai.google.dev/gemini-api/docs/pricing?hl=de): Kosten verstehen

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
