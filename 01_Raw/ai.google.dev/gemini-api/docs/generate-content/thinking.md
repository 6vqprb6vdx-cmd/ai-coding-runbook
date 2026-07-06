---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=de
fetched_at: 2026-07-06T05:17:20.285195+00:00
title: "Gemini-Denken \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini-Denken

Die Modelle der [Gemini 3- und 2.5-Serie](https://ai.google.dev/gemini-api/docs/models?hl=de) verwenden einen internen
„Denkprozess“, der ihre Fähigkeiten zur Schlussfolgerung und mehrstufigen
Planung erheblich verbessert. Dadurch sind sie sehr effektiv für komplexe Aufgaben wie
Programmieren, fortgeschrittene Mathematik und Datenanalyse.

In diesem Leitfaden erfahren Sie, wie Sie die Denkfunktionen von Gemini mit der Gemini API verwenden.

## Inhalte mit Thinking-Modus generieren

Das Initiieren einer Anfrage mit einem Thinking-Modell ähnelt jeder anderen Anfrage zur Inhaltserstellung. Der Hauptunterschied besteht darin, eines der
[Modelle mit Thinking-Unterstützung](#supported-models) im `model` Feld anzugeben, wie
im folgenden [Beispiel zur Textgenerierung](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#text-input) gezeigt:

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Ok

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.5-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## Zusammenfassungen der Gedanken

Zusammenfassungen der Gedanken sind zusammengefasste Versionen der Rohgedanken des Modells und bieten Einblicke in den internen Denkprozess des Modells. Die Denkaufwände und -budgets gelten für die Rohgedanken des Modells und nicht für Zusammenfassungen der Gedanken.

Sie können Zusammenfassungen der Gedanken aktivieren, indem Sie `includeThoughts` in der Anfragekonfiguration auf `true` setzen. Anschließend können Sie auf die Zusammenfassung zugreifen, indem Sie die `parts` des Parameters `response` durchlaufen und den booleschen Wert `thought` prüfen.

Hier ein Beispiel, wie Sie Zusammenfassungen der Gedanken ohne Streaming aktivieren und abrufen. In diesem Fall wird mit der Antwort eine einzelne, endgültige Zusammenfassung der Gedanken zurückgegeben:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.5-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Ok

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

Und hier ein Beispiel für die Verwendung von Thinking-Modus mit Streaming, bei dem während der Generierung fortlaufende, inkrementelle Zusammenfassungen zurückgegeben werden:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.5-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
  }
}

await main();
```

### Ok

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.5-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## Thinking-Modus steuern

Gemini-Modelle verwenden standardmäßig dynamisches Denken und passen den Aufwand für die Schlussfolgerung automatisch an die Komplexität der Anfrage des Nutzers an.
Wenn Sie jedoch bestimmte Latenzbeschränkungen haben oder das Modell eine tiefere Schlussfolgerung als üblich durchführen soll, können Sie optional Parameter verwenden, um das Thinking-Verhalten zu steuern.

### Denkaufwände (Gemini 3)

Mit dem Parameter `thinkingLevel`, der für Gemini 3-Modelle und höher empfohlen wird, können Sie das Verhalten bei der Schlussfolgerung steuern.

In der folgenden Tabelle sind die Einstellungen für `thinkingLevel` für jeden Modelltyp aufgeführt:

| Denkaufwand | Gemini 3.5 Flash | Gemini 3.1 Pro | Gemini 3.1 Flash Lite | Gemini 3.1 Flash Lite Image | Gemini 3 Flash | Beschreibung |
| --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | Unterstützt | Nicht unterstützt | Unterstützt (Standardeinstellung) | Unterstützt (Standardeinstellung) | Unterstützt | Entspricht für die meisten Anfragen der Einstellung „Kein Thinking-Modus“. Beachten Sie, dass `minimal` nicht garantiert, dass der Thinking-Modus deaktiviert ist. Das Modell kann für komplexe Aufgaben sehr wenig Schlussfolgerungen ziehen. |
| **`low`** | Unterstützt | Unterstützt | Unterstützt | Nicht unterstützt | Unterstützt | Minimiert Latenz und Kosten. |
| **`medium`** | Unterstützt (Standardeinstellung) | Unterstützt | Unterstützt | Nicht unterstützt | Unterstützt | Ausgewogener Denkaufwand für die meisten Aufgaben. |
| **`high`** | Unterstützt (dynamisch) | Unterstützt (Standardeinstellung, dynamisch) | Unterstützt (dynamisch) | Unterstützt (dynamisch) | Unterstützt (Standardeinstellung, dynamisch) | Maximiert die Tiefe der Schlussfolgerung. Es kann deutlich länger dauern, bis das Modell ein erstes Ausgabetoken (ohne Thinking-Modus) erreicht, aber die Ausgabe ist sorgfältiger durchdacht. |

Das folgende Beispiel zeigt, wie Sie den Denkaufwand festlegen.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Ok

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Der Thinking-Modus kann für Gemini 3.1 Pro nicht deaktiviert werden. Gemini 3 Flash und Flash Lite
unterstützen ebenfalls keine vollständige Deaktivierung des Thinking-Modus.
Wenn Sie keinen Denkaufwand angeben, verwendet Gemini den Standard-Denkaufwand der Gemini 3-Modelle (z.B. `"high"` für Gemini 3.1 Pro und `"medium"` für Gemini 3.5 Flash).

Modelle der Gemini 2.5-Serie unterstützen `thinkingLevel` nicht. Verwenden Sie stattdessen `thinkingBudget`.

### Thinking-Budgets

Der Parameter `thinkingBudget`, der mit der Gemini 2.5-Serie eingeführt wurde, gibt dem Modell die spezifische Anzahl von Thinking-Tokens vor, die für die Schlussfolgerung verwendet werden sollen.

Im Folgenden finden Sie Details zur Konfiguration von `thinkingBudget` für jeden Modelltyp.
Sie können den Thinking-Modus deaktivieren, indem Sie `thinkingBudget` auf 0 setzen.
Wenn Sie `thinkingBudget` auf -1 setzen, wird der **dynamische Thinking-Modus** aktiviert. Das Modell passt das Budget dann an die Komnessität der Anfrage an.

| Modell | Standardeinstellung (Thinking-Budget ist nicht festgelegt) | Bereich | Thinking-Modus deaktivieren | Dynamischen Thinking-Modus aktivieren |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Dynamischer Thinking-Modus | `128` bis `32768` | Nicht zutreffend: Der Thinking-Modus kann nicht deaktiviert werden | `thinkingBudget = -1` (Standardeinstellung) |
| **2.5 Flash** | Dynamischer Thinking-Modus | `0` bis `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Standardeinstellung) |
| **2.5 Flash (Vorabversion)** | Dynamischer Thinking-Modus | `0` bis `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Standardeinstellung) |
| **2.5 Flash Lite** | Modell denkt nicht | `512` bis `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite (Vorabversion)** | Modell denkt nicht | `512` bis `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 (Vorabversion)** | Dynamischer Thinking-Modus | `0` bis `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Standardeinstellung) |
| **2.5 Flash Live Native Audio (Vorabversion, 09/2025)** | Dynamischer Thinking-Modus | `0` bis `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Standardeinstellung) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Ok

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

Je nach Prompt kann das Modell das Token-Budget über- oder unterschreiten.

## Gedankensignaturen

Die Gemini API ist zustandslos. Das Modell behandelt jede API-Anfrage unabhängig und hat keinen Zugriff auf den Denkkontext aus früheren Runden in Multi-Turn-Interaktionen.

Um den Denkkontext über mehrere Runden hinweg beizubehalten, gibt Gemini Gedankensignaturen zurück. Das sind verschlüsselte Darstellungen des internen Denkprozesses des Modells.

- **Gemini 2.5-Modelle** geben Gedankensignaturen zurück, wenn der Thinking-Modus aktiviert ist und
  die Anfrage [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#thinking) enthält,
  insbesondere [Funktionsdeklarationen](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#step-2).
- **Gemini 3-Modelle** können Gedankensignaturen für alle Arten von [Teilen](https://ai.google.dev/api/caching?hl=de#Part) zurückgeben.
  Wir empfehlen, alle Signaturen so zurückzugeben, wie sie empfangen wurden. Für Funktionsaufrufsignaturen ist dies *erforderlich*. Weitere Informationen finden Sie auf der
  [Seite Gedankensignaturen](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=de).

Weitere Nutzungsbeschränkungen, die bei Funktionsaufrufen zu beachten sind:

- Signaturen werden vom Modell innerhalb anderer Teile in der Antwort zurückgegeben, z. B. Funktionsaufrufe oder Textteile.
  [Geben Sie die gesamte Antwort](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#step-4)
  mit allen Teilen in nachfolgenden Runden an das Modell zurück.
- Verketten Sie keine Teile mit Signaturen.
- Führen Sie keinen Teil mit einer Signatur mit einem anderen Teil ohne Signatur zusammen.

## Preise

Wenn der Thinking-Modus aktiviert ist, setzt sich der Preis für die Antwort aus den Ausgabetokens und den Thinking-Tokens zusammen. Die Gesamtzahl der generierten Thinking-Tokens finden Sie im Feld `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Ok

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

Thinking-Modelle generieren vollständige Gedanken, um die Qualität der endgültigen
Antwort zu verbessern, und geben dann [Zusammenfassungen](#summaries) aus, um Einblicke in den
Denkprozess zu geben. Die Preise basieren also auf den vollständigen Thinking-Tokens, die das Modell zum Erstellen einer Zusammenfassung benötigt, obwohl nur die Zusammenfassung von der API ausgegeben wird.

Weitere Informationen zu Tokens finden Sie im [Leitfaden zum Zählen von Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=de).

## Best Practices

Dieser Abschnitt enthält einige Hinweise zur effizienten Verwendung von Thinking-Modellen.
Wie immer erzielen Sie die besten Ergebnisse, wenn Sie unsere [Prompt-Anleitung und Best Practices](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=de) befolgen.

### Debugging und Steuerung

- **Schlussfolgerung überprüfen**: Wenn Sie nicht die erwartete Antwort von den
  Thinking-Modellen erhalten, kann es hilfreich sein, die Zusammenfassungen der Gedanken von Gemini sorgfältig zu analysieren.
  Sie können sehen, wie die Aufgabe aufgeschlüsselt und die Schlussfolgerung erreicht wurde, und diese Informationen verwenden, um die Ergebnisse zu korrigieren.
- **Anleitung zur Schlussfolgerung geben**: Wenn Sie eine besonders lange
  Ausgabe wünschen, können Sie in Ihrem Prompt eine Anleitung geben, um den
  [Denkaufwand](#set-budget) des Modells zu begrenzen. So können Sie mehr Ausgabetokens für Ihre Antwort reservieren.

### Aufgabenkomplexität

- **Einfache Aufgaben (Thinking-Modus kann deaktiviert werden)** : Für einfache Anfragen, bei denen keine komplexe Schlussfolgerung erforderlich ist, z. B. das Abrufen von Fakten oder die Klassifizierung, ist der Thinking-Modus nicht erforderlich. Beispiele:
  - „Wo wurde DeepMind gegründet?“
  - „Wird in dieser E‑Mail um ein Meeting gebeten oder werden nur Informationen bereitgestellt?“
- **Mittelschwere Aufgaben (Standard/etwas Thinking-Modus)** : Viele häufige Anfragen profitieren von einer schrittweisen Verarbeitung oder einem tieferen Verständnis. Gemini kann die Thinking-Funktion flexibel für Aufgaben wie die folgenden verwenden:
  - Analogie zwischen Photosynthese und Erwachsenwerden
  - Vergleich und Gegenüberstellung von Elektroautos und Hybridautos
- **Schwierige Aufgaben (maximale Thinking-Funktion)** : Für wirklich komplexe Aufgaben wie das Lösen komplexer mathematischer Probleme oder Programmieraufgaben empfehlen wir, ein hohes Thinking-Budget festzulegen. Bei diesen Aufgaben muss das Modell seine gesamten Schlussfolgerungs- und Planungsfunktionen nutzen. Oft sind viele interne Schritte erforderlich, bevor eine Antwort gegeben wird. Beispiele:
  - Lösen Sie Aufgabe 1 in AIME 2025: Finden Sie die Summe aller ganzzahligen Basen b > 9 für
    die 17b ein Teiler von 97b ist.
  - Schreiben Sie Python-Code für eine Webanwendung, die Echtzeit-Börsendaten visualisiert, einschließlich der Nutzerauthentifizierung. Machen Sie sie so effizient wie möglich.

## Unterstützte Modelle, Tools und Funktionen

Thinking-Funktionen werden für alle Modelle der 3- und 2.5-Serie unterstützt.
Alle Modellfunktionen finden Sie auf der
[Seite Modellübersicht](https://ai.google.dev/gemini-api/docs/models?hl=de).

Thinking-Modelle funktionieren mit allen Tools und Funktionen von Gemini. So können die Modelle mit externen Systemen interagieren, Code ausführen oder auf Echtzeitinformationen zugreifen und die Ergebnisse in ihre Schlussfolgerungen und die endgültige Antwort einbeziehen.

Beispiele für die Verwendung von Tools mit Thinking-Modellen finden Sie im [Thinking-Kochbuch][Colab].

## Nächste Schritte

- Informationen zur Thinking-Abdeckung finden Sie in unserem [Leitfaden zur OpenAI-Kompatibilität](https://ai.google.dev/gemini-api/docs/openai?hl=de#thinking).

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-30 (UTC)."],[],[]]
