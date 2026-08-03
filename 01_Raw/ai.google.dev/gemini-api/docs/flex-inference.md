---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=de
fetched_at: 2026-08-03T04:27:13.971630+00:00
title: "Flex-Inferenz \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Flex-Inferenz

Die Gemini Flex API ist eine Inferenzebene, die im Vergleich zu Standardpreisen eine Kostenreduzierung von 50% bietet. Im Gegenzug sind Latenz und Verfügbarkeit variabel und werden nach dem Best-Effort-Prinzip bereitgestellt. Sie wurde für latenzunempfindliche Arbeitslasten entwickelt, die eine synchrone Verarbeitung erfordern, aber nicht die Echtzeitleistung der Standard-API benötigen.

## Flex verwenden

Wenn Sie die Flex-Ebene verwenden möchten, geben Sie in Ihrer Anfrage `service_tier` als `flex` an. Standardmäßig wird die Standardebene für Anfragen verwendet, wenn dieses Feld nicht angegeben wird.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.6-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## So funktioniert die Flex-Inferenz

Die Gemini Flex-Inferenz schließt die Lücke zwischen der Standard-API und der 24-stündigen
Bearbeitungszeit der [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de). Sie nutzt Rechenkapazität außerhalb der Spitzenzeiten, um eine kostengünstige Lösung für Hintergrundaufgaben und sequenzielle Workflows zu bieten.

| Funktion | Flex | Priorität | Standard | Batch |
| --- | --- | --- | --- | --- |
| **Preise** | 50% Rabatt | 75–100% mehr als Standard | Standardpreis | 50% Rabatt |
| **Latenz** | Minuten (Ziel: 1–15 Minuten) | Niedrig (Sekunden) | Sekunden bis Minuten | Bis zu 24 Stunden |
| **Zuverlässigkeit** | Best-Effort-Ansatz | Hoch | Hoch / Mittel bis hoch | Hoch (für Durchsatz) |
| **Schnittstelle** | Synchron | Synchron | Synchron | Asynchron |

### Hauptvorteile

- **Kosteneffizienz**: Erhebliche Einsparungen bei nicht produktiven Evaluierungen, Hintergrund-Agents und Datenanreicherung.
- **Geringer Aufwand**: Fügen Sie Ihren bestehenden Anfragen einfach einen einzelnen Parameter hinzu.
- **Synchrone Workflows**: Ideal für sequenzielle API-Ketten, bei denen die nächste Anfrage von der Ausgabe der vorherigen abhängt. Dadurch ist sie flexibler als Batch für agentenbasierte Workflows.

### Anwendungsfälle

- **Offline-Evaluierungen**: Ausführen von Regressions- oder Leaderboard-Tests mit LLM-as-a-Judge.
- **Hintergrund-Agents**: Sequenzielle Aufgaben wie CRM-Aktualisierungen, Profilerstellung oder Inhaltsmoderation, bei denen Verzögerungen von einigen Minuten akzeptabel sind.
- **Budgetbeschränkte Forschung**: Akademische Experimente, die ein hohes Tokenvolumen bei einem begrenzten Budget erfordern.

### Ratenlimits

Der Flex-Inferenz-Traffic wird auf Ihre allgemeinen [Ratenlimits](https://aistudio.google.com/rate-limit?hl=de) angerechnet. Es gibt keine
erweiterten Ratenlimits wie bei der [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de).

### Kapazität

Flex-Traffic wird mit niedrigerer Priorität behandelt. Bei einem Anstieg des Standard-Traffics können Flex-Anfragen vorzeitig beendet oder entfernt werden, um Kapazität für Nutzer mit hoher Priorität zu gewährleisten. Wenn Sie eine Inferenz mit hoher Priorität benötigen, lesen Sie den Abschnitt
[Inferenz mit Priorität](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de).

### Fehlercodes

Wenn die Flex-Kapazität nicht verfügbar ist oder das System überlastet ist, gibt die API Standardfehlercodes zurück:

- **503 Dienst nicht verfügbar**: Das System ist derzeit ausgelastet.
- **429 Zu viele Anfragen**: Ratenlimits oder Ressourcenerschöpfung.

### Verantwortung des Clients

- **Kein serverseitiges Fallback**: Um unerwartete Kosten zu vermeiden, wird eine Flex-Anfrage nicht
  automatisch auf die Standardebene aktualisiert, wenn die Flex-Kapazität
  voll ist.
- **Wiederholungen**: Sie müssen Ihre eigene clientseitige Wiederholungslogik mit
  exponentiellem Backoff implementieren.
- **Zeitlimits**: Da Flex-Anfragen in einer Warteschlange stehen können, empfehlen wir,
  die clientseitigen Zeitlimits auf mindestens 10 Minuten zu erhöhen, um ein vorzeitiges
  Schließen der Verbindung zu vermeiden.

## Zeitlimits anpassen

Sie können Zeitlimits pro Anfrage für die REST API und Clientbibliotheken konfigurieren.
Achten Sie immer darauf, dass das clientseitige Zeitlimit das beabsichtigte serverseitige Zeitlimit abdeckt (z.B. 600 Sekunden oder mehr für Flex-Warteschlangen). Die SDKs erwarten Zeitlimitwerte in Millisekunden.

### Zeitlimits pro Anfrage

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.6-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

## Wiederholungen implementieren

Da Flex-Anfragen vorzeitig beendet werden können und mit 503-Fehlern fehlschlagen, finden Sie hier ein Beispiel für die optionale Implementierung einer Wiederholungslogik, um mit fehlgeschlagenen Anfragen fortzufahren:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.6-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.6-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.6-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## Preise

Die Flex-Inferenz kostet 50% der [Standard-API](https://ai.google.dev/gemini-api/docs/pricing?hl=de)
und wird pro Token abgerechnet.

## Unterstützte Modelle

Die folgenden Modelle unterstützen die Flex-Inferenz:

| Modell | Flex-Inferenz |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=de) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=de) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=de) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de) | ✔️ |
| [Gemini 3.1 Pro (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de) | ✔️ |
| [Gemini 3 Flash (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=de) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=de) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=de) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=de) | ✔️ |

## Nächste Schritte

- [Inferenz mit Priorität](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de) für extrem niedrige Latenz.
- [Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=de): Informationen zu Tokens.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
