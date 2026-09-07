---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de
fetched_at: 2026-09-07T05:35:51.443207+00:00
title: "Fundierung mit Google Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Fundierung mit Google Maps

Die Fundierung mit Google Maps verbindet die generativen Funktionen von Gemini mit den umfangreichen, faktischen und aktuellen Daten von Google Maps. Mit dieser Funktion können Entwickler standortbezogene Funktionen ganz einfach in ihre Anwendungen einbinden. Wenn eine Nutzeranfrage einen Kontext mit Bezug auf Maps-Daten hat, nutzt das Gemini-Modell Google Maps, um faktisch korrekte und aktuelle Antworten zu geben, die für den angegebenen Standort oder den ungefähren Ort des Nutzers relevant sind.

- **Genaue, standortbezogene Antworten**:Nutzen Sie die umfangreichen und aktuellen Daten von Google Maps für geografisch spezifische Anfragen.
- **Verbesserte Personalisierung**:Passen Sie Empfehlungen und Informationen an die vom Nutzer angegebenen Standorte an.

## Jetzt starten

In diesem Beispiel wird gezeigt, wie Sie die Fundierung mit Google Maps in Ihre Anwendung einbinden, um genaue, standortbezogene Antworten auf Nutzeranfragen zu geben. Der Prompt fragt nach lokalen Empfehlungen mit einem optionalen Nutzerstandort, sodass das Gemini-Modell Google Maps-Daten verwenden kann.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
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
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## So funktioniert die Fundierung mit Google Maps

Bei der Fundierung mit Google Maps wird die Gemini API in das Google Geo-Ökosystem eingebunden, indem die Maps API als Fundierungsquelle verwendet wird. Wenn die Anfrage eines Nutzers einen geografischen Kontext enthält, kann das Gemini-Modell das Tool „Fundierung mit Google Maps“ aufrufen. Das Modell kann dann Antworten generieren, die auf Google Maps-Daten basieren, die für den angegebenen Standort relevant sind.

Der Prozess umfasst in der Regel Folgendes:

1. **Nutzeranfrage**:Ein Nutzer sendet eine Anfrage an Ihre Anwendung, die möglicherweise einen geografischen Kontext enthält (z.B. „Cafés in meiner Nähe“, „Museen in San Francisco“).
2. **Toolaufruf**:Das Gemini-Modell erkennt die geografische Absicht und ruft das Tool „Fundierung mit Google Maps“ auf. Optional können diesem Tool die `latitude` und `longitude` des Nutzers übergeben werden. Das Tool ist ein Textsuchtool und verhält sich ähnlich wie die Suche in Google Maps. Bei lokalen Anfragen („in meiner Nähe“) werden die Koordinaten verwendet, während spezifische oder nicht lokale Anfragen wahrscheinlich nicht vom expliziten Standort beeinflusst werden.
3. **Datenabruf**:Der Dienst „Fundierung mit Google Maps“ fragt Google Maps nach relevanten Informationen ab (z.B. Orte, Rezensionen, Fotos, Adressen, Öffnungszeiten).
4. **Fundierte Generierung**:Die abgerufenen Maps-Daten werden verwendet, um die Antwort des Gemini-Modells zu informieren und so die faktische Richtigkeit und Relevanz zu gewährleisten.
5. **Antwort und Anmerkungen**:Das Modell gibt eine Textantwort mit Inline-Anmerkungen zurück, die auf Google Maps-Quellen verweisen, sodass Entwickler Zitate anzeigen können.

## Gründe und Anwendungsfälle für die Fundierung mit Google Maps

Die Fundierung mit Google Maps ist ideal für Anwendungen, die genaue, aktuelle und standortspezifische Informationen erfordern. Sie verbessert die Nutzererfahrung, indem sie relevante und personalisierte Inhalte bereitstellt, die auf der umfangreichen Google Maps-Datenbank mit über 250 Millionen Orten weltweit basieren.

Sie sollten die Fundierung mit Google Maps verwenden, wenn Ihre Anwendung Folgendes leisten muss:

- Vollständige und genaue Antworten auf geografisch spezifische Fragen geben
- Konversationelle Reiseplaner und lokale Reiseführer erstellen
- Sehenswürdigkeiten basierend auf dem Standort und den Nutzerpräferenzen wie Restaurants oder Geschäfte empfehlen
- Standortbezogene Funktionen für soziale Dienste, Einzelhandelsdienste oder Essenslieferdienste erstellen

Die Fundierung mit Google Maps eignet sich besonders für Anwendungsfälle, in denen Nähe und aktuelle faktische Daten entscheidend sind, z. B. um das „beste Café in meiner Nähe“ zu finden oder eine Wegbeschreibung zu erhalten.

## Anwendungsfälle

Die Fundierung mit Google Maps unterstützt eine Vielzahl von standortbezogenen Anwendungsfällen.

### Ortsbezogene Fragen beantworten

Stellen Sie detaillierte Fragen zu einem bestimmten Ort, um Antworten zu erhalten, die auf Google-Nutzerrezensionen und anderen Maps-Daten basieren.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Standortbezogene Personalisierung bereitstellen

Erhalten Sie Empfehlungen, die auf die Präferenzen eines Nutzers und eine bestimmte geografische Region zugeschnitten sind.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Bei der Reiseplanung helfen

Erstellen Sie mehrtägige Pläne mit Wegbeschreibungen und Informationen zu verschiedenen Orten, die sich perfekt für Reiseanwendungen eignen.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## Anforderungen an die Dienstnutzung

In diesem Abschnitt werden die Anforderungen an die Dienstnutzung für die Fundierung mit Google Maps beschrieben.

### Nutzer über die Verwendung von Google Maps-Quellen informieren

Bei jedem Ergebnis, das auf Google Maps basiert, erhalten Sie Quellenangaben zu den Inhaltsblöcken des Schritts `model_output`, die die jeweilige Antwort unterstützen. Die folgenden Metadaten werden zurückgegeben:

- Quell-URL
- Name

Wenn Sie Ergebnisse aus der Fundierung mit Google Maps präsentieren, müssen Sie die zugehörigen Google Maps-Quellen angeben und Ihre Nutzer über Folgendes informieren:

- Die Google Maps-Quellen müssen direkt auf die generierten Inhalte folgen, die von den Quellen unterstützt werden. Diese generierten Inhalte werden auch als auf Google Maps basierendes Ergebnis bezeichnet.
- Die Google Maps-Quellen müssen innerhalb einer Nutzerinteraktion sichtbar sein.

### Google Maps-Quellen mit Google Maps-Links anzeigen

Für jede Quellenangabe muss eine Linkvorschau generiert werden, die die folgenden Anforderungen erfüllt:

- Geben Sie jede Quelle gemäß den Richtlinien für die Quellenangabe als Text
  [für Google Maps an](#maps-attribution-guidelines).
- Zeigen Sie den in der Antwort angegebenen Quellennamen an.
- Verlinken Sie die Quelle mit der `url` aus der Anmerkung.

### Richtlinien für die Quellenangabe als Text für Google Maps

Wenn Sie Quellen in Texten Google Maps zuordnen, beachten Sie die folgenden Richtlinien:

- Ändern Sie den Text „Google Maps“ in keiner Weise:
  - Ändern Sie die Groß- und Kleinschreibung von „Google Maps“ nicht.
  - Fügen Sie keinen Zeilenumbruch in „Google Maps“ ein.
  - Lokalisieren Sie „Google Maps“ nicht in eine andere Sprache.
  - Verhindern Sie, dass Browser „Google Maps“ übersetzen, indem Sie das HTML-Attribut translate="no" verwenden.

Weitere Informationen zu einigen unserer Google Maps-Datenanbieter und ihren
Lizenzbedingungen finden Sie in den [rechtlichen Hinweisen zu Google Maps und Google Earth](https://www.google.com/help/legalnotices_maps/?hl=de).

## Best Practices

- **Nutzerstandort angeben**:Um die relevantesten und personalisiertesten Antworten zu erhalten, geben Sie in der Toolkonfiguration für `google_maps` immer den Breiten- und Längengrad (`latitude` und `longitude`) an, wenn der Standort des Nutzers bekannt ist.
- **Endnutzer informieren**:Informieren Sie Ihre Endnutzer deutlich darüber, dass Google Maps-Daten verwendet werden, um ihre Anfragen zu beantworten, insbesondere wenn das Tool aktiviert ist.
- **Deaktivieren, wenn nicht erforderlich**:Die Fundierung mit Google Maps ist standardmäßig deaktiviert. Aktivieren Sie sie nur (`"tools": [{"type": "google_maps"}]`), wenn eine Anfrage einen
  klaren geografischen Kontext hat, um Leistung und Kosten zu optimieren.

## Beschränkungen

- Die Fundierung mit Google Maps unterstützt derzeit nur Prompts und Antworten in englischer Sprache.
- Das Tool ist möglicherweise nicht in allen Regionen verfügbar.
- Die Ergebnisse können je nach Standortgenauigkeit und verfügbaren Maps-Daten variieren.
- **Geografischer Umfang**:Die Fundierung mit Google Maps ist weltweit verfügbar.
- **Standardstatus**:Das Tool „Fundierung mit Google Maps“ ist standardmäßig deaktiviert.
  Sie müssen es in Ihren API-Anfragen explizit aktivieren.

## Preise und Ratenlimits

Die Preise für die Fundierung mit Google Maps variieren je nach Modellgeneration:

- **Gemini 3-Modelle**:Ihrem Projekt wird jede **Suchanfrage** in Rechnung gestellt, die das Modell ausführt. Eine einzelne **Suchanfrage** (Ihre API-Anfrage an das Modell) kann dazu führen, dass das Modell mehrere Suchanfragen ausführt, um die erforderlichen Informationen zu finden. Jede dieser Anfragen zählt als kostenpflichtige Nutzung des Tools.
- **Gemini 2.5 und ältere Modelle**:Ihrem Projekt wird jede **Suchanfrage** in Rechnung gestellt.
  Eine Anfrage wird nur dann in Rechnung gestellt, wenn die Anfrage mindestens ein auf Google Maps basierendes Ergebnis zurückgibt, unabhängig davon, wie viele einzelne Suchanfragen das Modell intern ausgeführt hat, um dieses Ergebnis zu erhalten.

Ausführliche Informationen zu den Preisen finden Sie auf der Seite [Gemini API-Preise](https://ai.google.dev/gemini-api/docs/pricing?hl=de).

## Unterstützte Modelle

Die folgenden Modelle unterstützen die Fundierung mit Google Maps:

| Modell | Fundierung mit Google Maps |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=de) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=de) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=de) | ✔️ |
| [Gemini 3.1 Pro (Vorschau)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de) | ✔️ |
| [Gemini 3 Flash (Vorschau)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=de) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=de) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=de) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=de) | ✔️ |

## Unterstützte Toolkombinationen

Gemini 3-Modelle unterstützen die Kombination von integrierten Tools (z. B. Fundierung mit Google Maps) mit benutzerdefinierten Tools (Funktionsaufruf). Weitere Informationen finden Sie auf der
[Seite Toolkombinationen](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de).

## Nächste Schritte

- Weitere Informationen zu anderen [verfügbaren Tools](https://ai.google.dev/gemini-api/docs/tools?hl=de).
- Weitere Informationen zu Best Practices für die verantwortungsbewusste Anwendung von KI und den Sicherheitsfiltern der Gemini API finden Sie unter [Sicherheitseinstellungen](https://ai.google.dev/gemini-api/docs/safety-settings?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
