---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=de
fetched_at: 2026-11-02T07:10:06.555459+00:00
title: "Tokens verstehen und z\u00e4hlen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=de).

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

## Tokens

Tokens können einzelne Zeichen wie `z` oder ganze Wörter wie `cat` sein. Lange Wörter werden in mehrere Tokens aufgeteilt. Die Menge aller vom Modell verwendeten Tokens wird als Vokabular bezeichnet. Der Vorgang, Text in Tokens aufzuteilen, wird als *Tokenisierung* bezeichnet.

Wenn die Abrechnung aktiviert ist, werden die [Kosten eines Aufrufs der Gemini API](https://ai.google.dev/pricing?hl=de) teilweise durch die Anzahl der Eingabe- und Ausgabetokens bestimmt. Daher kann es hilfreich sein, zu wissen, wie Tokens gezählt werden.

## Tokens zählen

Alle Eingaben und Ausgaben der Gemini API werden tokenisiert, einschließlich Text, Bilddateien und anderer nicht textbasierter Modalitäten.

Sie können Tokens auf folgende Weise zählen:

- **Rufen Sie `count_tokens` mit der Eingabe der Anfrage auf.** Gibt die Gesamtzahl der Tokens *nur in der Eingabe* zurück. Führen Sie diesen Aufruf aus, bevor Sie die Eingabe senden, um die Größe Ihrer Anfragen zu prüfen.
- **Verwenden Sie die `usage` in der Antwort auf die Interaktion.** Gibt die Tokenanzahl für Eingabe (`total_input_tokens`), Ausgabe (`total_output_tokens`), Überlegung (`total_thought_tokens`), Cache-Inhalte (`total_cached_tokens`), Toolnutzung (`total_tool_use_tokens`) und insgesamt (`total_tokens`) zurück.

### Texttokens zählen

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.CountTokensResponse;

Client client = new Client();
String prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
CountTokensResponse countResponse =
    client.models.countTokens("gemini-3.8-flash", prompt, null);
System.out.println("total_tokens: " + countResponse.totalTokens().orElse(0));

// Get usage from interaction
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.usage().orElse(null));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    modelInfo, err := client.Models.Get(ctx, "gemini-3.8-flash", nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Input token limit: %d\n", modelInfo.InputTokenLimit)
    fmt.Printf("Output token limit: %d\n", modelInfo.OutputTokenLimit)
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### Tokens für mehrere Unterhaltungen zählen

Zählen Sie Tokens im Unterhaltungsverlauf mit `previous_interaction_id`:

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Usage;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// First interaction
CreateModelInteraction params1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Hi, my name is Bob"))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();

// Second interaction continues the conversation
CreateModelInteraction params2 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What's my name?"))
        .previousInteractionId(interaction1.id().orElse(""))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();

// Usage includes tokens from both turns
if (interaction2.usage().isPresent()) {
  Usage usage = interaction2.usage().get();
  System.out.println("Input tokens: " + usage.totalInputTokens().orElse(0));
  System.out.println("Output tokens: " + usage.totalOutputTokens().orElse(0));
  System.out.println("Total tokens: " + usage.totalTokens().orElse(0));
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := "The quick brown fox jumps over the lazy dog."

    // Count input tokens before sending
    totalTokens, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", genai.Text(prompt), nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("total_tokens: %d\n", totalTokens.TotalTokens)

    // Create the interaction and inspect the returned usage metadata
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(prompt),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
    if interaction.Usage != nil {
        if interaction.Usage.TotalInputTokens != nil {
            fmt.Printf("Input tokens: %d\n", *interaction.Usage.TotalInputTokens)
        }
        if interaction.Usage.TotalOutputTokens != nil {
            fmt.Printf("Output tokens: %d\n", *interaction.Usage.TotalOutputTokens)
        }
        if interaction.Usage.TotalThoughtTokens != nil {
            fmt.Printf("Thought tokens: %d\n", *interaction.Usage.TotalThoughtTokens)
        }
        if interaction.Usage.TotalTokens != nil {
            fmt.Printf("Total tokens: %d\n", *interaction.Usage.TotalTokens)
        }
    }
}
```

### Multimodale Tokens zählen

Alle Eingaben für die Gemini API werden tokenisiert, einschließlich Bilder, Videos und Audio.
Wichtige Punkte zur Tokenisierung:

- **Bilder**: Bilder mit ≤ 384 Pixeln in beiden Dimensionen werden als 258 Tokens gezählt. Größere Bilder werden in 768 × 768 Pixel große Kacheln unterteilt, die jeweils als 258 Tokens gezählt werden.
- **Video**: 263 Tokens pro Sekunde (gilt für die statische Verarbeitung). Bei der agentischen Verarbeitung variiert die Tokennutzung. Weitere Informationen finden Sie unter
  [Tokennutzung für Videos nach Verarbeitungsmodus](#video-token-usage).
- **Audio**: 32 Tokens pro Sekunde

#### Bildtokens

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.Content;
import com.google.genai.types.CountTokensResponse;
import com.google.genai.types.File;
import com.google.genai.types.Part;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;

Client client = new Client();

File uploadedFile =
    client.files.upload(
        new java.io.File("path/to/image.jpg"),
        UploadFileConfig.builder().mimeType("image/jpeg").build());

// Count tokens for image + text
CountTokensResponse countResponse =
    client.models.countTokens(
        "gemini-3.8-flash",
        Arrays.asList(
            Content.fromParts(
                Part.fromText("Tell me about this image"),
                Part.fromUri(
                    uploadedFile.uri().orElse(""), uploadedFile.mimeType().orElse("image/jpeg")))),
        null);
System.out.println("Total tokens: " + countResponse.totalTokens().orElse(0));

// Generate with image
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text("Tell me about this image").build(),
                    ImageContent.builder()
                        .uri(uploadedFile.uri().orElse(""))
                        .mimeType(
                            ImageContentMimeType.of(uploadedFile.mimeType().orElse("image/jpeg")))
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.usage().orElse(null));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:  interactions.Model("gemini-3.8-flash"),
            Input:  interactions.NewInteractionsInput("Explain the history of the internet in 3 paragraphs."),
            Stream: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        }
        if completed := event.GetDataInteractionCompleted(); completed != nil {
            usage := completed.Interaction.Usage
            if usage != nil && usage.TotalTokens != nil {
                fmt.Printf("\nTotal tokens: %d\n", *usage.TotalTokens)
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

**Beispiel für Inline-Daten** :

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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

#### Video tokens

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 100 * 60 = 6,000 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### Tokennutzung für Videos nach Verarbeitungsmodus

Die Tokennutzung für Videos hängt vom Verarbeitungsmodus ab:

| **Verarbeitungsmodus** | **Tokenberechnung** | **Typische Nutzung** |
| --- | --- | --- |
| **Statisch** (Standard) | Standardmäßig ~100 Tokens/Sekunde (niedrige Auflösung) oder ~300 Tokens/Sekunde (hohe Auflösung). Alle Frames werden mit 1 FPS gesampelt. | Vorhersehbar, proportional zur Videodauer. |
| **Agentisch** | Variiert je nach Komplexität der Inhalte. Das Modell lädt nur das Transkript und/oder die Frames und/oder das Audio, die zum Beantworten des Prompts erforderlich sind. | Bis zu 88% weniger Tokens für Inhalte im Langformat. |

Bei der agentischen Verarbeitung kann eine einstündige Vorlesung, für die im statischen Modus ~1,08 Mio. Tokens verwendet würden, je nach Prompt und Inhalt ~108.000 Tokens verwenden.

Die tatsächliche Tokennutzung für eine Anfrage finden Sie unter `interaction.usage`. Agentische Videotokens werden in den folgenden Feldern gemeldet:

- **Ausgangsprompt** (Videoreferenz + Nutzerprompt): `total_input_tokens`
- **Überlegung zur Navigation**: `total_thought_tokens`
- **Transkript, Frames und Audio werden bei Bedarf geladen**: `total_tool_use_tokens`
- **Endgültige Antwort**: `total_output_tokens`

#### Audio tokens

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model="gemini-3.8-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### Tooltokens zählen

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
    model="gemini-3.8-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## Kontextfenster

Jedes Gemini-Modell hat eine maximale Anzahl von Tokens, die es verarbeiten kann.

- **Gemini 4-Modelle (`gemini-4-argon`):** Verwenden ein gemeinsames Kontextfenster mit 1 Mio. Tokens (`1,048,576` Tokens) für Eingabe-, Überlegungs- und Ausgabetokens. Standardmäßig sind synchrone Antworten (`background=False`, Streaming oder Nicht-Streaming) auf `65,536` Ausgabetokens begrenzt. Mit der [langen Decodierung](https://ai.google.dev/gemini-api/docs/long-decode?hl=de) können Sie bis zu `1,048,576` Tokens generieren. Wenn Ihre Eingabetokens plus `max_output_tokens` 1.048.576 Tokens überschreiten, begrenzt die API das Ausgabelimit automatisch auf den verbleibenden Platz im Kontextfenster (`1,048,576` minus Ihre Eingabetokens).
- **Gemini 3- und 2.5-Modelle:** Verwenden separate Budgets für Eingabe (`1,048,576` Tokens) und Ausgabe (`65,536` Tokens).

### Größe des Kontextfensters programmatisch abrufen

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.8-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.8-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Model;

Client client = new Client();

Model modelInfo = client.models.get("gemini-3.8-flash", null);
System.out.println("Input token limit: " + modelInfo.inputTokenLimit().orElse(0));
System.out.println("Output token limit: " + modelInfo.outputTokenLimit().orElse(0));
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Tell me about this instrument"
    imageBytes, err := os.ReadFile("/path/to/organ.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    // Count tokens before creating the interaction
    parts := []*genai.Part{
        genai.NewPartFromText(prompt),
        genai.NewPartFromBytes(imageBytes, "image/jpeg"),
    }
    totalTokens, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Estimated input tokens: %d\n", totalTokens.TotalTokens)

    // Create the multimodal interaction and inspect the usage metadata
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Image),
                    MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
    if interaction.Usage != nil && interaction.Usage.TotalTokens != nil {
        fmt.Printf("Total tokens billed: %d\n", *interaction.Usage.TotalTokens)
    }
}
```

Die Größen der Kontextfenster finden Sie auf der Seite „[Modelle](https://ai.google.dev/gemini-api/docs/models?hl=de)“.

## Nächste Schritte

- [Textgenerierung](https://ai.google.dev/gemini-api/docs/text-generation?hl=de): Grundlagen der Generierung
- [Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de): Kosten mit Caching senken
- [Preise](https://ai.google.dev/gemini-api/docs/pricing?hl=de): Kosten verstehen

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-10-13 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-10-13 (UTC)."],[],[]]
