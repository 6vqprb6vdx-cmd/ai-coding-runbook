---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=de
fetched_at: 2026-10-12T06:50:42.996730+00:00
title: "Neu in Gemini\u00a03.8 Flash \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs/generate-content?hl=de)

Feedback geben

# Neu in Gemini 3.8 Flash

[3.6 Flash und 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6?hl=de)
[Andere Modelle](#other-models)

Gemini 3.8 Flash (`gemini-3.8-flash`) ist allgemein verfügbar und kann in der Produktion eingesetzt werden. Es ist unser intelligentestes Flash-Modell, das für langfristige Softwareentwicklung, autonome KI-Agenten und komplexe Unternehmensworkflows entwickelt wurde.

In diesem Leitfaden werden die Neuerungen in Gemini 3.8 Flash, API-Änderungen, Codebeispiele und Migrationsanleitungen beschrieben.

## Neues Modell

| Modell | Modell-ID | Standardmäßiger Denkaufwand | Preise | Beschreibung |
| --- | --- | --- | --- | --- |
| Gemini 3.8 Flash | `gemini-3.8-flash` | `medium` | 3.8 Flash ist bis zum Jahresende zum Einführungspreis von 0,75 $ pro 1 Million Eingabetokens und 3,75 $ pro 1 Million Ausgabetokens verfügbar. Weitere Informationen finden Sie unter [Preise](https://ai.google.dev/gemini-api/docs/pricing?hl=de). | Unser intelligentestes Flash-Modell, das für langfristige Softwareentwicklung, autonome KI-Agenten und komplexe Unternehmensworkflows entwickelt wurde. |

Gemini 3.8 Flash unterstützt ein Kontextfenster von 1 Million Tokens, maximal 64.000 Ausgabetokens, anpassbare Denkebenen (`low`, `medium`, `high`) und dieselben integrierten Tools.

Die vollständigen Spezifikationen finden Sie auf der [Modellseite für Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=de). Details zu Einführungspreisen finden Sie unten im [Abschnitt zu Preisen](#pricing) oder auf der [Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de#gemini-3.8-flash).

## Kurzanleitung

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Write a three.js script that renders a realistic 3D black hole."
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Write a three.js script that renders a realistic 3D black hole.",
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders a realistic 3D black hole."}]
    }]
  }'
```

## Neues bei Gemini 3.8 Flash

- **Softwareentwicklung mit langem Horizont**:Liefert gute Ergebnisse bei realen Coding-Benchmarks, komplexem Refactoring mehrerer Dateien und deterministischer Toolausführung. Weitere Informationen finden Sie in der [Bewertungsmethodik](https://deepmind.google/models/evals-methodology/gemini-3-8-flash/?hl=de).
- **Autonome Agents**:Damit können Sie robuste mehrstufige Planungs- und Tool-Orchestrierungs-Workflows erstellen und so die Anzahl fehlgeschlagener Schleifen und Fehler erheblich reduzieren.
- **Komplexe Unternehmensworkflows**:Bietet überlegene Genauigkeit, fundierte Argumentation und hohe faktische Strenge bei anspruchsvollen Aufgaben und umfangreichen Datenpipelines.
- **Standardmodell für verwaltete KI-Agenten**: Der Standard-KI-Agent für verwaltete KI-Agenten, der [Antigravity-KI-Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=de), verwendet jetzt Gemini 3.8 Flash. Das [Antigravity SDK](https://antigravity.google/docs/sdk/overview/?hl=de) verwendet standardmäßig auch Gemini 3.8 Flash.
- **Einführungspreise**:Gemini 3.8 Flash ist bis zum 31. Dezember 2026 zum Einführungspreis von 0,75 $ pro 1 Million Eingabetokens und 3,75 $ pro 1 Million Ausgabetokens verfügbar. Die Standardpreise von 1,50 $ pro 1 Million Eingabetokens und 7,50 $ pro 1 Million Ausgabetokens treten am 1. Januar 2027 in Kraft.

Gemini 3.8 Flash kann bei längeren und komplexen Aufgaben mehr Tokens verwenden. Um bei schwierigen, mehrstufigen Zielen Ergebnisse von höherer Qualität zu liefern, führt das Modell kleinere Denkschritte aus, ruft Tools iterativ auf und überprüft seine Arbeit im Laufe des Prozesses. Nicht für jeden Workflow ist diese Art der Bestätigung erforderlich. Bei alltäglichen Aufgaben können Sie den [Aufwand für das Reasoning](#understanding-reasoning-levels) verringern, um den Tokenverbrauch zu reduzieren. Alternativ wird Gemini 3.6 Flash weiterhin unterstützt.

## Schlussfolgerungsniveaus

Mit Gemini 3.8 Flash haben Sie die Möglichkeit, die Latenz und Intelligenz flexibel zu steuern, indem Sie den Denkaufwand des Modells anpassen:

- **Geringer Analyseaufwand**: Verkürzt die Zeit bis zur Antwort bei latenzkritischen Tasks wie Incident Response Pipelines, Echtzeit-Chats, dem Verfassen von Entwürfen und der schnellen Datenanalyse.
- **Mittel (Standard):** Beste Qualität für die meisten Aufgaben. Empfohlen für komplexe Code- und KI-Agent-Anwendungsfälle, da die Genauigkeit beim ersten Durchlauf höher ist.
- **Hoher Denkaufwand**: Maximiert die Fähigkeiten des Modells in Bezug auf Schlussfolgerungen und Tool-Orchestrierung. Optimal für tiefgründige Problemlösung, Mathematik und schwierige mehrstufige Aufgaben.

Im folgenden Beispiel wird für `thinking_level` der Wert `medium` für eine komplexe Codeanalyseanfrage festgelegt:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="medium"  # Balanced reasoning effort for complex tasks
        ),
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  config: {
    thinkingConfig: {
      thinkingLevel: "medium", // Balanced reasoning effort for complex tasks
    },
  },
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely."}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "medium"
      }
    }
  }'
```

## Aktualisierter Antigravity-Agent

## Checkliste für die Migration

```
  `/gemini-api-dev migrate my app to Gemini 3.8 Flash`
```

### Zu gemini-3.8-flash migrieren

- **Modell-ID aktualisieren**:Ändern Sie den Zielmodellstring in `gemini-3.8-flash`.
- **Denkaufwand konfigurieren**:Ersetzen Sie `thinking_budget` durch die String-Enumeration `thinking_level`. Hinweis: `minimal` wird in Gemini 3.8 Flash nicht unterstützt. Wählen Sie `low`, `medium` (Standard) oder `high` aus.
- **Gemini 3-API-Parameteränderungen anwenden**:Entfernen Sie die verworfenen Sampling-Parameter (`temperature`, `top_p`, `top_k`), `candidate_count` (wird in Gemini 3 und höher nicht unterstützt) und vorab ausgefüllte Modell-Turns. [Änderungen an der Gemini 3.6 API und Parameteraktualisierungen](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6?hl=de#api-changes-and-parameter-updates)
- **Regeln für die Validierung von Zügen erzwingen**:Entfernen Sie vorab ausgefüllte Modellzüge und sorgen Sie dafür, dass der letzte Nutzerzug nicht leer ist.
- **Funktionsaufrufe prüfen**:
  - Platzieren Sie multimodale Assets in der Antwortnutzlast.
  - Inline-Anweisungen mit `\n\n` formatieren.
  - Wenn `Malformed_Function_Call`-Fehler im Zusammenhang mit Text vor dem Tool angezeigt werden, lesen Sie den Abschnitt [Workarounds for pre-tool text requirements](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=de#workarounds-for-pre-tool-text-requirements) (Problemumgehungen für Anforderungen an Text vor dem Tool).
  - Nur bei Verwendung der generateContent API: Achten Sie darauf, dass alle `FunctionResponse`-Objekte `call_id` und `name` enthalten.
- **Gemini 3-Mindestanforderungen**:Informationen zu SDK-Updates und zur Beibehaltung von Gedanken-Signaturen finden Sie unter [Gedanken-Signaturen](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=de).

## Preise

Bis zum 31. Dezember 2026 können Sie die Einführungspreise für Gemini 3.8 Flash und Gemini 3.6 Flash in Google AI Studio und der Gemini Enterprise Agent Platform nutzen. Die Standardpreise treten am 1. Januar 2027 in Kraft. Eine vollständige Übersicht der Preisstufen finden Sie auf der [Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de#gemini-3.8-flash).

## Andere Modelle

- [Gemini 3.6 Flash und 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6?hl=de)
- [Alle Modelle ansehen](https://ai.google.dev/gemini-api/docs/models?hl=de)

## Nächste Schritte

- API-Spezifikationen finden Sie in der [Modellübersicht](https://ai.google.dev/gemini-api/docs/models?hl=de).
- Weitere Informationen zur Orchestrierung mehrerer Agenten finden Sie in der [Übersicht über die Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de).
- Prompts in [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de) testen und optimieren

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-10-09 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-10-09 (UTC)."],[],[]]
