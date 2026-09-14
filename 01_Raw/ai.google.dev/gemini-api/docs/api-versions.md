---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=de
fetched_at: 2026-09-14T05:37:29.463590+00:00
title: "Erl\u00e4uterung der API-Versionen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [API-Referenz](https://ai.google.dev/api?hl=de)

Feedback geben

# Erläuterung der API-Versionen

In diesem Dokument finden Sie einen allgemeinen Überblick über die Unterschiede zwischen den `v1`
und `v1beta` Versionen der Gemini API.

- **v1**: Stabile Version der API. Funktionen in der stabilen Version werden über die gesamte Lebensdauer der Hauptversion vollständig unterstützt. Bei nicht abwärtskompatiblen Änderungen wird die nächste Hauptversion der API erstellt und die vorhandene Version nach einem angemessenen Zeitraum eingestellt.
  Nicht abwärtskompatible Änderungen können an der API vorgenommen werden, ohne die Hauptversion zu ändern. Seit Juni 2026 ist die **Interactions API** allgemein verfügbar und wird in `v1` unterstützt.
- **v1beta**: Diese Version enthält frühe Funktionen und Möglichkeiten, die
  aktiv entwickelt werden. Funktionen in `v1beta` können sich ändern, da wir sie basierend auf Feedback weiterentwickeln. Sie können jedoch neue Funktionen ausprobieren, bevor sie in die stabile Version übernommen werden.

| Funktion | v1 | v1beta |
| --- | --- | --- |
| Interactions API |  |  |
| Inhalte generieren – Nur Texteingabe |  |  |
| Inhalte generieren – Text- und Bildeingabe |  |  |
| Inhalte generieren – Textausgabe |  |  |
| Inhalte generieren – Multi-Turn-Unterhaltungen (Chat) |  |  |
| Inhalte generieren – Funktionsaufrufe |  |  |
| Inhalte generieren – Streaming |  |  |
| Inhalte einbetten – Nur Texteingabe |  |  |
| Antwort generieren |  |  |
| Semantischer Retriever |  |  |

- - Unterstützt
- - Wird nie unterstützt

## API-Version in einem SDK konfigurieren

In den Gemini API SDKs ist standardmäßig `v1beta` festgelegt. Sie können jedoch Versionen explizit angeben, indem Sie die API-Version festlegen, wie im folgenden Codebeispiel gezeigt:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.6-flash',
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
    model: "gemini-3.6-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works"
  }'
```

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-12 (UTC)."],[],[]]
