---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=de
fetched_at: 2026-10-19T05:32:23.033056+00:00
title: "Erl\u00e4uterung der API-Versionen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [API-Referenz](https://ai.google.dev/api?hl=de)

Feedback geben

# Erläuterung der API-Versionen

In diesem Dokument finden Sie einen allgemeinen Überblick über die Unterschiede zwischen den Versionen `v1` und `v1beta` der Gemini API.

- **v1**: Stabile Version der API. Funktionen in der stabilen Version werden während des gesamten Lebenszyklus der Hauptversion vollständig unterstützt. Bei funktionsgefährdenden Änderungen wird eine neue Hauptversion der API erstellt und die vorhandene Version nach einem angemessenen Zeitraum eingestellt.
  Es können abwärtskompatible Änderungen an der API vorgenommen werden, ohne dass sich die Hauptversion ändert. Die **Interactions API** und ihre Kernfunktionen sind in `v1` allgemein verfügbar.
- **v1beta**: Diese Version enthält erste Funktionen, die aktiv entwickelt werden. Funktionen in `v1beta` können sich ändern, da wir sie auf Grundlage von Feedback weiterentwickeln. Sie haben jedoch die Möglichkeit, neue Funktionen auszuprobieren, bevor sie als stabil eingestuft werden.

## Unterstützung von Funktionen und Merkmalen

In der folgenden Tabelle wird die Verfügbarkeit von Funktionen in `v1` (allgemein verfügbar) und `v1beta` (Beta) beschrieben. Die wichtigsten API-Funktionen und ‑Tools gelten sowohl für die Interactions API als auch für `generateContent`, sofern nicht anders angegeben:

| Funktion | v1 | v1beta |
| --- | --- | --- |
| **Wichtige API-Funktionen** |  |  |
| [Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=de) |  |  |
| [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de) |  |  |
| [Strukturierte Ausgabe](https://ai.google.dev/gemini-api/docs/structured-output?hl=de) |  |  |
| [Denken / Argumentation](https://ai.google.dev/gemini-api/docs/thinking?hl=de) |  |  |
| [Systemanweisungen](https://ai.google.dev/gemini-api/docs/system-instructions?hl=de) |  |  |
| [Audioausgabe (Sprachkonfiguration)](https://ai.google.dev/gemini-api/docs/audio?hl=de) |  |  |
| [Service Tier (Priority / Flex)](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de) |  |  |
| **Tools** |  |  |
| [Tool zur Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) |  |  |
| [Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de) |  |  |
| [Google Maps-Fundierung](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de) |  |  |
| [Tool zum URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de) |  |  |
| [Dateisuchtool](https://ai.google.dev/gemini-api/docs/file-search?hl=de) |  |  |
| [Tool zur Computernutzung](https://ai.google.dev/gemini-api/docs/computer-use?hl=de) |  |  |
| [MCP-Server-Tool](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#mcp) |  |  |
| **Echtzeit-APIs** |  |  |
| [Live API (WebSockets)](https://ai.google.dev/gemini-api/docs/live-api?hl=de) |  |  |
| [Live Music API](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=de) |  |  |
| [Einmal-Tokens (Live API)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=de) |  |  |
| **Plattform-APIs** |  |  |
| [Models API](https://ai.google.dev/gemini-api/docs/models?hl=de) |  |  |
| [Files Service Route](https://ai.google.dev/gemini-api/docs/files?hl=de) (Files-Dienstroute) |  |  |
| [Dateisuche speichert Route](https://ai.google.dev/gemini-api/docs/file-search?hl=de) |  |  |
| [Agents API](https://ai.google.dev/gemini-api/docs/agents?hl=de) |  |  |
| [Webhooks API](https://ai.google.dev/gemini-api/docs/webhooks?hl=de) |  |  |
| [Kontext-Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de) |  |  |

- – Unterstützt

## API-Version in einem SDK konfigurieren

Die Gemini API SDKs verwenden standardmäßig `v1beta`. Sie können jedoch Versionen explizit angeben, indem Sie die API-Version festlegen, wie im folgenden Codebeispiel gezeigt:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client = Client.builder()
    .httpOptions(HttpOptions.builder().apiVersion("v1").build())
    .build();

CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.6-flash"))
    .input(InteractionsInput.of("Explain how AI works"))
    .build();
var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        HTTPOptions: genai.HTTPOptions{
            APIVersion: "v1",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.6-flash"),
            Input: interactions.NewInteractionsInput("Explain how AI works"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works",
  }'
```

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-24 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-24 (UTC)."],[],[]]
