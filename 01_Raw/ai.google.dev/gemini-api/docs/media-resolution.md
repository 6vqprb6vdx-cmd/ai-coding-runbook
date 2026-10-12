---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=de
fetched_at: 2026-10-12T06:59:12.407071+00:00
title: "Medienaufl\u00f6sung \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Medienauflösung

Mit dem Parameter `media_resolution` wird gesteuert, wie die Gemini API Media-Eingaben wie Bilder, Videos, Audio und PDF-Dokumente verarbeitet. Dazu wird die **maximale Anzahl von Tokens** für Media-Eingaben festgelegt. So können Sie die Antwortqualität mit Latenz und Kosten in Einklang bringen. Bei visuellen und Dokument-Eingaben wird die Tokenzuweisung basierend auf der Auflösungseinstellung skaliert. Audioeingaben werden dagegen bei allen Auflösungsstufen mit einer festen Rate pro Sekunde tokenisiert. Informationen zu den verschiedenen Einstellungen, Standardwerten und wie sie mit Tokens zusammenhängen, finden Sie im Abschnitt [Tokenanzahl](#token-counts).

Sie können die Media-Auflösung für einzelne Media-Objekte (Inhaltselemente) in Ihrer Anfrage konfigurieren (nur Gemini 3).

## Auflösung von Medien pro Inhaltselement (nur Gemini 3)

Mit Gemini 3 können Sie die Media-Auflösung für einzelne Media-Objekte in Ihrer Anfrage festlegen und so die Token-Nutzung detailliert optimieren. Sie können Auflösungsstufen in einer einzelnen Anfrage kombinieren. So können Sie beispielsweise für ein komplexes Diagramm eine hohe Auflösung und für ein einfaches Kontextbild eine niedrige Auflösung verwenden.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Describe the details in this high-resolution image.").build();
Content imageContent =
    ImageContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/image/scones.jpg")
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/image.jpg", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe the details in this high-resolution image.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:        genai.Ptr(uploadedFile.URI),
                    MimeType:   interactions.ImageContentMimeType(uploadedFile.MIMEType).ToPointer(),
                    Resolution: interactions.MediaResolutionHigh.ToPointer(),
                }),
            }),
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
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Verfügbare Auflösungswerte

Die Gemini API definiert die folgenden Stufen für die Media-Auflösung:

- `unspecified`: Die Standardeinstellung. Die Anzahl der Tokens für diese Stufe variiert erheblich zwischen Gemini 3 und früheren Gemini-Modellen.
- `low`: Geringere Anzahl von Tokens, was zu einer schnelleren Verarbeitung und niedrigeren Kosten führt, aber weniger Details liefert.
- `medium`: Ein ausgewogenes Verhältnis zwischen Detailgrad, Kosten und Latenz.
- `high`: Höhere Anzahl von Tokens, die dem Modell mehr Details zur Verfügung stellen, was jedoch zu einer höheren Latenz und höheren Kosten führt.
- `ultra_high` (nur pro Inhaltselement): Höchste Anzahl an Tokens, die für bestimmte Anwendungsfälle wie die [Computernutzung](https://ai.google.dev/gemini-api/docs/computer-use?hl=de) erforderlich ist.

`high` bietet für die meisten Anwendungsfälle die optimale Leistung.

Die genaue Anzahl der Tokens, die für jede dieser Ebenen generiert werden, hängt sowohl vom **Medientyp** (Bild, Video, Audio, PDF) als auch von der **Modellversion** ab.

## Tokenanzahl

In den folgenden Tabellen sind die ungefähren Tokenzahlen für jeden `media_resolution`-Wert und Medientyp pro Modellfamilie zusammengefasst.

**Gemini 3-Modelle**

| MediaResolution | Bild | Video | Audio | PDF |
| --- | --- | --- | --- | --- |
| `unspecified` (Standard) | 1.120 | 70 | 25 (pro Sekunde) | 560 |
| `low` | 280 | 70 | 25 (pro Sekunde) | 280 + nativer Text |
| `medium` | 560 | 70 | 25 (pro Sekunde) | 560 + nativer Text |
| `high` | 1.120 | 280 | 25 (pro Sekunde) | 1120 + nativer Text |
| `ultra_high` | 2240 | – | – | – |

## Die richtige Auflösung auswählen

- **Standard (`unspecified`)**: Beginnen Sie mit der Standardeinstellung. Es ist für die meisten gängigen Anwendungsfälle auf ein gutes Gleichgewicht zwischen Qualität, Latenz und Kosten abgestimmt.
- **`low`**:Für Szenarien, in denen Kosten und Latenz im Vordergrund stehen und detaillierte Informationen weniger wichtig sind.
- **`medium` / `high`**:Erhöhen Sie die Auflösung, wenn die Aufgabe das Erfassen komplexer Details in den Media erfordert. Das ist oft für komplexe visuelle Analysen, das Lesen von Diagrammen oder das Erfassen von dichten Dokumenten erforderlich.
- **`ultra_high`**: Nur für die Einstellung pro Inhaltselement verfügbar. Empfohlen für bestimmte Anwendungsfälle wie die Verwendung auf einem Computer oder wenn Tests eine deutliche Verbesserung gegenüber `high` zeigen.
- **Steuerung pro Inhaltselement (Gemini 3)**: Optimiert die Tokennutzung. Verwenden Sie beispielsweise in einem Prompt mit mehreren Bildern `high` für ein komplexes Diagramm und `low` oder `medium` für einfachere Kontextbilder.

**Empfohlene Einstellungen**

In den folgenden Listen sind die empfohlenen Einstellungen für die Media-Auflösung für jeden unterstützten Medientyp aufgeführt.

| Medientyp | Empfohlene Einstellung | Maximale Anzahl der Tokens | Usage Guidance |
| --- | --- | --- | --- |
| **Bilder** | `high` | 1.120 | Für die meisten Bildanalyseaufgaben empfohlen, um maximale Qualität zu gewährleisten. |
| **PDFs** | `medium` | 560 | Optimal für das Verständnis von Dokumenten; die Qualität erreicht in der Regel bei `medium` ein Sättigungsniveau. Eine Erhöhung auf `high` führt bei Standarddokumenten selten zu besseren OCR-Ergebnissen. |
| **Video** (Allgemein) | `low` oder `medium` | 70 (pro Frame) | **Hinweis**:Bei Video werden die Einstellungen für `low` und `medium` identisch behandelt (70 Tokens), um die Kontextnutzung zu optimieren. Das ist für die meisten Aufgaben zur Aktionserkennung und ‑beschreibung ausreichend. |
| **Video** (textlastig) | `high` | 280 (pro Frame) | Nur erforderlich, wenn der Anwendungsfall das Lesen von dichtem Text (OCR) oder kleinen Details in Videoframes umfasst. |
| **Audio** | `unspecified` (Standard) | 25 (pro Sekunde) | Audio wird mit einer festen Rate von 25 Tokens pro Sekunde für alle unterstützten Auflösungseinstellungen (`unspecified`, `low`, `medium` und `high`) tokenisiert. |

Testen und bewerten Sie immer die Auswirkungen verschiedener Auflösungseinstellungen auf Ihre Anwendung, um das beste Verhältnis zwischen Qualität, Latenz und Kosten zu finden.

## Beziehung zu Videoverarbeitungsmodi

Mit den `media_resolution`- und Verarbeitungsparametern werden verschiedene Aspekte der Videoeingabe gesteuert:

- Mit `media_resolution` wird die **Auflösung** jedes Frames gesteuert (Anzahl der Tokens pro Frame).
- Mit den Steuerelementen `processing` / `media_processing` wird festgelegt, **welche Inhalte aus dem Video** in den Kontext geladen werden.

Du kannst beides für denselben Videoeingang festlegen. Sie können beispielsweise die Verarbeitung durch KI-Agenten mit niedriger Media-Auflösung verwenden, um die Gesamtzahl der Tokens für ein langes Video zu minimieren.

Weitere Informationen zu den Videoverarbeitungsmodi finden Sie im Leitfaden [Agentic Video Understanding](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de#agentic-video-understanding).

## Zusammenfassung der Versionskompatibilität

- Das Festlegen von `resolution` für einzelne Inhalte ist **nur bei Gemini 3-Modellen möglich**.

## Nächste Schritte

- Weitere Informationen zu den multimodalen Funktionen der Gemini API finden Sie in den Anleitungen zu [Bildverständnis](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de), [Videoverständnis](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de), [Audioverständnis](https://ai.google.dev/gemini-api/docs/audio?hl=de) und [Dokumentverständnis](https://ai.google.dev/gemini-api/docs/document-processing?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-24 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-24 (UTC)."],[],[]]
