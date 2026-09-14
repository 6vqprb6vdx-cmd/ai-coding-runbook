---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=de
fetched_at: 2026-09-14T05:35:17.139679+00:00
title: "Gemini-Denken \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini-Denken

Die Modelle der [Gemini 3- und 2.5-Serie](https://ai.google.dev/gemini-api/docs/models?hl=de) verwenden einen
„Denkprozess“, der ihre Fähigkeiten zum logischen Schlussfolgern und zur mehrstufigen
Planung erheblich verbessert. Dadurch sind sie sehr effektiv für komplexe Aufgaben wie
Programmieren, fortgeschrittene Mathematik und Datenanalyse.

Wenn Sie ein Thinking Model verwenden, führt Gemini intern einen Denkprozess durch, bevor es antwortet. Die Interactions API stellt diesen Denkprozess über `thought`-Schritte dar. Das sind spezielle Schritte, die chronologisch neben Funktionsaufrufen, Nutzereingaben oder Modellausgaben im `steps`-Array angezeigt werden.

Jeder Denkprozessschritt enthält zwei Felder:

| Feld | Erforderlich? | Beschreibung |
| --- | --- | --- |
| `signature` | ✅ Ja | Eine verschlüsselte Darstellung des internen Denkzustands des Modells. Immer vorhanden, auch wenn das Modell nur minimal logisch schlussfolgert. |
| `summary` | ❌ Nein | Ein Array mit Inhalten (Text und/oder Bilder), in dem der Denkprozess zusammengefasst wird. Je nach [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=de)-Konfiguration, ob das Modell ausreichend logisch schlussgefolgert hat oder nicht, oder je nach Inhaltstyp kann es leer sein. Bei latenten Bildern gibt es beispielsweise möglicherweise keine Textzusammenfassungen. |

## Interaktionen mit Thinking

Das Initiieren einer Interaktion mit einem Thinking Model ähnelt jeder anderen Interaktionsanfrage. Geben Sie im `model` Feld eines der [Modelle mit Thinking-Unterstützung](#thinking-levels) an:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## Zusammenfassungen der Gedanken

Zusammenfassungen der Gedanken geben Einblicke in den internen Denkprozess des Modells.
Standardmäßig wird nur die endgültige Ausgabe zurückgegeben. Sie können Zusammenfassungen der Gedanken mit `thinking_summaries` aktivieren:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

Ein Denkprozessblock kann in den folgenden Fällen **nur eine Signatur ohne Zusammenfassung** enthalten:

- Einfache Anfragen, bei denen das Modell nicht ausreichend logisch schlussgefolgert hat, um eine Zusammenfassung zu erstellen
- `thinking_summaries: "none"`, wobei Zusammenfassungen explizit deaktiviert sind
- Bestimmte Arten von Denkprozessinhalten, z. B. Bilder, haben möglicherweise keine Textzusammenfassungen

Ihr Code sollte immer Denkprozessblöcke verarbeiten, bei denen `summary` leer oder nicht vorhanden ist.

## Streaming mit Thinking

Verwenden Sie Streaming, um während der Generierung schrittweise Zusammenfassungen der Gedanken zu erhalten.
Denkprozessblöcke werden mit Server-Sent Events (SSE) mit zwei verschiedenen Delta-Typen bereitgestellt:

| Delta-Typ | Enthält | Wann gesendet |
| --- | --- | --- |
| `thought_summary` | Text- oder Bildzusammenfassung | Ein oder mehrere Deltas mit schrittweiser Zusammenfassung |
| `thought_signature` | Die kryptografische Signatur | Das letzte Delta vor `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

Die Streaming-Antwort verwendet Server-Sent Events (SSE) und besteht aus Schritten und Ereignissen, z. B.:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.6-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Thinking steuern

Gemini-Modelle führen standardmäßig dynamische Denkprozesse durch und passen den Aufwand für das logische Schlussfolgern automatisch an die Komplexität der Anfrage an. Sie können dieses Verhalten mit dem Parameter `thinking_level` steuern.

| Modell | Standard-Thinking | Unterstützte Stufen |
| --- | --- | --- |
| gemini-3.6-flash | An (Medium) | minimal, niedrig, mittel, hoch |
| gemini-3.5-flash-lite | An (minimal) | minimal, niedrig, mittel, hoch |
| gemini-3.1-pro-preview | An (hoch) | niedrig, mittel, hoch |
| gemini-3.1-flash-lite-image | An (minimal) | minimal, hoch |
| gemini-3-flash-preview | An (hoch) | minimal, niedrig, mittel, hoch |
| gemini-3-pro-preview | An (hoch) | niedrig, hoch |
| gemini-3.5-flash | An (Medium) | minimal, niedrig, mittel, hoch |
| gemini-2.5-pro | An | niedrig, mittel, hoch |
| gemini-2.5-flash | An | niedrig, mittel, hoch |
| gemini-2.5-flash-lite | Aus | niedrig, mittel, hoch |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Gedankensignaturen

Gedankensignaturen sind verschlüsselte Darstellungen des internen Denkprozesses des Modells. Sie sind erforderlich, um die Kontinuität des Denkprozesses bei Mehrfachdialogen aufrechtzuerhalten.

Mit der Interactions API ist die Verarbeitung von Gedankensignaturen viel einfacher als mit der `generateContent` API.

### Zustandsorientierter Modus (empfohlen)

Wenn Sie die Interactions API standardmäßig im zustandsorientierten Modus verwenden (indem Sie `store: true` festlegen und die `previous_interaction_id` in nachfolgenden Schritten übergeben), verwaltet der Server automatisch den Unterhaltungsstatus, einschließlich aller Denkprozessblöcke und Signaturen. In diesem Modus müssen Sie nichts in Bezug auf Signaturen tun. Sie werden vollständig serverseitig verarbeitet.

### Zustandsloser Modus

Wenn Sie den Unterhaltungsstatus selbst verwalten (zustandsloser Modus) und die vollständige Historie der Eingaben und Ausgaben in jeder Anfrage übergeben:

- Sie **MÜSSEN** immer alle `thought`-Blöcke genau so noch einmal senden, wie sie vom Modell empfangen wurden.
- Sie sollten **Denkprozessblöcke nicht aus dem Verlauf entfernen oder ändern, da sie die Signaturen enthalten, die das Modell benötigt, um den Denkprozess fortzusetzen.**
- Wenn Sie innerhalb einer Sitzung das Modell wechseln, sollten Sie trotzdem die Denkprozessblöcke des vorherigen Modells noch einmal senden. Das Back-End verwaltet die Kompatibilität.

## Preise

Wenn Thinking aktiviert ist, setzt sich der Preis für die Antwort aus den Ausgabe-Tokens und den Thinking-Tokens zusammen. Die Gesamtzahl der generierten Thinking-Tokens finden Sie im Feld `total_thought_tokens`.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

Thinking Models generieren vollständige Denkprozesse, um die Qualität der endgültigen
Antwort zu verbessern, und geben dann [Zusammenfassungen](#summaries) aus, um Einblicke in den
Denkprozess zu geben. Die Preise basieren auf den vollständigen Denkprozess-Tokens, die das Modell generieren muss, obwohl nur die Zusammenfassung von der API ausgegeben wird.

Weitere Informationen zu Tokens finden Sie im [Leitfaden zum Zählen von Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=de).

## Best Practices

Beachten Sie diese Richtlinien, um Thinking Models effizient zu verwenden.

- **Denkprozess überprüfen**: Analysieren Sie Zusammenfassungen der Gedanken, um Fehler zu verstehen und Prompts zu verbessern.
- **Thinking-Budget steuern**: Fordern Sie das Modell auf, bei längeren Ausgaben weniger zu denken, um Tokens zu sparen.
- **Einfache Aufgaben**: Verwenden Sie minimales oder niedriges Thinking für die Faktenabfrage oder Klassifizierung (z.B. „Wo wurde DeepMind gegründet?“).
- **Mittelkomplexe Aufgaben**: Verwenden Sie das Standard-Thinking, um Konzepte zu vergleichen oder kreativ zu denken (z.B. „Vergleichen Sie Elektro- und Hybridautos“).
- **Komplexe Aufgaben**: Verwenden Sie das maximale Thinking für fortgeschrittenes Programmieren, Mathematik oder mehrstufige Planung (z.B. „Lösen Sie AIME-Mathematikaufgaben“).

## Nächste Schritte

- [Textgenerierung](https://ai.google.dev/gemini-api/docs/text-generation?hl=de): Einfache Textantworten
- [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de): Verbindung zu Tools herstellen
- [Gemini 3-Leitfaden](https://ai.google.dev/gemini-api/docs/gemini-3?hl=de): Modellspezifische Funktionen

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-12 (UTC)."],[],[]]
