---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/code-execution?hl=de
fetched_at: 2026-08-17T02:20:43.475039+00:00
title: "Codeausf\u00fchrung \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Codeausführung

Die Gemini API bietet ein Tool zur Code-Ausführung, mit dem das Modell Python-Code generieren und ausführen kann. Das Modell kann dann iterativ aus den Ergebnissen der Codeausführung lernen, bis es eine endgültige Ausgabe erstellt hat. Sie können die Codeausführung verwenden, um Anwendungen zu erstellen, die von codebasierten Schlussfolgerungen profitieren. Beispielsweise können Sie die Codeausführung verwenden, um Gleichungen zu lösen oder Text zu verarbeiten. Sie können
auch die [Bibliotheken](#supported-libraries) verwenden, die in der Code-Ausführungsumgebung
enthalten sind, um speziellere Aufgaben auszuführen.

Gemini kann Code nur in Python ausführen. Sie können Gemini weiterhin bitten, Code in einer anderen Sprache zu generieren, aber das Modell kann das Tool zur Code-Ausführung nicht verwenden, um ihn auszuführen.

## Code-Ausführung aktivieren

Konfigurieren Sie das Tool zur Codeausführung für das Modell, um die Codeausführung zu aktivieren. So kann das Modell Code generieren und ausführen.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What is the sum of the first 50 prime numbers? "
    "Generate and run code for the calculation, and make sure you get all 50.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: [
    "What is the sum of the first 50 prime numbers? " +
      "Generate and run code for the calculation, and make sure you get all 50.",
  ],
  config: {
    tools: [{ codeExecution: {} }],
  },
});

const parts = response?.candidates?.[0]?.content?.parts || [];
parts.forEach((part) => {
  if (part.text) {
    console.log(part.text);
  }

  if (part.executableCode && part.executableCode.code) {
    console.log(part.executableCode.code);
  }

  if (part.codeExecutionResult && part.codeExecutionResult.output) {
    console.log(part.codeExecutionResult.output);
  }
});
```

### Ok

```
package main

import (
    "context"
    "fmt"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        genai.Text("What is the sum of the first 50 prime numbers? " +
                  "Generate and run code for the calculation, and make sure you get all 50."),
        config,
    )

    fmt.Println(result.Text())
    fmt.Println(result.ExecutableCode())
    fmt.Println(result.CodeExecutionResult())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d ' {"tools": [{"code_execution": {}}],
    "contents": {
      "parts":
        {
            "text": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."
        }
    },
}'
```

Die Ausgabe könnte so aussehen. Sie wurde zur besseren Lesbarkeit formatiert:

```
Okay, I need to calculate the sum of the first 50 prime numbers. Here's how I'll
approach this:

1.  **Generate Prime Numbers:** I'll use an iterative method to find prime
    numbers. I'll start with 2 and check if each subsequent number is divisible
    by any number between 2 and its square root. If not, it's a prime.
2.  **Store Primes:** I'll store the prime numbers in a list until I have 50 of
    them.
3.  **Calculate the Sum:**  Finally, I'll sum the prime numbers in the list.

Here's the Python code to do this:

def is_prime(n):
  """Efficiently checks if a number is prime."""
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

primes = []
num = 2
while len(primes) < 50:
  if is_prime(num):
    primes.append(num)
  num += 1

sum_of_primes = sum(primes)
print(f'{primes=}')
print(f'{sum_of_primes=}')

primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
sum_of_primes=5117

The sum of the first 50 prime numbers is 5117.
```

Diese Ausgabe kombiniert mehrere Inhaltsteile, die das Modell bei der Verwendung der Codeausführung zurückgibt:

- `text`: Inline-Text, der vom Modell generiert wurde
- `executableCode`: Code, der vom Modell generiert wurde und ausgeführt werden soll
- `codeExecutionResult`: Ergebnis des ausführbaren Codes

Die Benennungskonventionen für diese Teile variieren je nach Programmiersprache.

## Codeausführung mit Bildern (Gemini 3)

Das Gemini 3 Flash-Modell kann jetzt Python-Code schreiben und ausführen, um Bilder aktiv zu bearbeiten und zu untersuchen.

**Anwendungsbeispiele**

- **Zoomen und untersuchen**: Das Modell erkennt implizit, wenn Details zu klein sind
  (z.B. beim Lesen eines Messgeräts in der Ferne), und schreibt Code, um den Bereich zuzuschneiden und mit höherer Auflösung neu zu untersuchen.
- **Visuelle Mathematik**: Das Modell kann mehrstufige Berechnungen mit Code ausführen (z.B.
  Posten auf einer Rechnung summieren).
- **Bildannotation**: Das Modell kann Bilder annotieren, um Fragen zu beantworten, z. B. Pfeile zeichnen, um Beziehungen darzustellen.

### Codeausführung mit Bildern aktivieren

Die Codeausführung mit Bildern wird in Gemini 3 Flash offiziell unterstützt. Sie können dieses Verhalten aktivieren, indem Sie sowohl die Codeausführung als Tool als auch die Funktion „Thinking“ aktivieren.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

# Ensure you have your API key set
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[image, "Zoom into the expression pedals and tell me how many pedals are there?"],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        # display() is a standard function in Jupyter/Colab notebooks
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
async function main() {
  const ai = new GoogleGenAI({ });

  // 1. Prepare Image Data
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  // 2. Call the API with Code Execution enabled
  const result = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: [
      {
        inlineData: {
          mimeType: 'image/jpeg',
          data: base64ImageData,
        },
      },
      { text: "Zoom into the expression pedals and tell me how many pedals are there?" }
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  // 3. Process the response (Text, Code, and Execution Results)
  const candidates = result.candidates;
  if (candidates && candidates[0].content.parts) {
    for (const part of candidates[0].content.parts) {
      if (part.text) {
        console.log("Text:", part.text);
      }
      if (part.executableCode) {
        console.log(`\nGenerated Code (${part.executableCode.language}):\n`, part.executableCode.code);
      }
      if (part.codeExecutionResult) {
        console.log(`\nExecution Output (${part.codeExecutionResult.outcome}):\n`, part.codeExecutionResult.output);
      }
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
    "io"
    "log"
    "net/http"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // Initialize Client (Reads GEMINI_API_KEY from env)
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // 1. Download the image
    imageResp, err := http.Get("https://goo.gle/instrument-img")
    if err != nil {
        log.Fatal(err)
    }
    defer imageResp.Body.Close()

    imageBytes, err := io.ReadAll(imageResp.Body)
    if err != nil {
        log.Fatal(err)
    }

    // 2. Configure Code Execution Tool
    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    // 3. Generate Content
    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        []*genai.Content{
            {
                Parts: []*genai.Part{
                    {InlineData: &genai.Blob{MIMEType: "image/jpeg", Data: imageBytes}},
                    {Text: "Zoom into the expression pedals and tell me how many pedals are there?"},
                },
                Role: "user",
            },
        },
        config,
    )
    if err != nil {
        log.Fatal(err)
    }

    // 4. Parse Response (Text, Code, Output)
    for _, cand := range result.Candidates {
        for _, part := range cand.Content.Parts {
            if part.Text != "" {
                fmt.Println("Text:", part.Text)
            }
            if part.ExecutableCode != nil {
                fmt.Printf("\nGenerated Code (%s):\n%s\n", 
                    part.ExecutableCode.Language, 
                    part.ExecutableCode.Code)
            }
            if part.CodeExecutionResult != nil {
                fmt.Printf("\nExecution Output (%s):\n%s\n", 
                    part.CodeExecutionResult.Outcome, 
                    part.CodeExecutionResult.Output)
            }
        }
    }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3.6-flash"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [
        {
          "code_execution": {}
        }
      ]
    }'
```

## Code-Ausführung im Chat verwenden

Sie können die Codeausführung auch im Rahmen eines Chats verwenden.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

response = chat.send_message("I have a math question for you.")
print(response.text)

response = chat.send_message(
    "What is the sum of the first 50 prime numbers? "
    "Generate and run code for the calculation, and make sure you get all 50."
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
```

### JavaScript

```
import {GoogleGenAI} from "@google/genai";

const ai = new GoogleGenAI({});

const chat = ai.chats.create({
  model: "gemini-3.6-flash",
  history: [
    {
      role: "user",
      parts: [{ text: "I have a math question for you:" }],
    },
    {
      role: "model",
      parts: [{ text: "Great! I'm ready for your math question. Please ask away." }],
    },
  ],
  config: {
    tools: [{codeExecution:{}}],
  }
});

const response = await chat.sendMessage({
  message: "What is the sum of the first 50 prime numbers? " +
            "Generate and run code for the calculation, and make sure you get all 50."
});
console.log("Chat response:", response.text);
```

### Ok

```
package main

import (
    "context"
    "fmt"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    chat, _ := client.Chats.Create(
        ctx,
        "gemini-3.6-flash",
        config,
        nil,
    )

    result, _ := chat.SendMessage(
                    ctx,
                    genai.Part{Text: "What is the sum of the first 50 prime numbers? " +
                                          "Generate and run code for the calculation, and " +
                                          "make sure you get all 50.",
                              },
                )

    fmt.Println(result.Text())
    fmt.Println(result.ExecutableCode())
    fmt.Println(result.CodeExecutionResult())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"tools": [{"code_execution": {}}],
    "contents": [
        {
            "role": "user",
            "parts": [{
                "text": "Write code to print \"Hello world!\" and execute it"
            }]
        },{
            "role": "model",
            "parts": [
              {
                "executable_code": {
                  "id": "a1b2c3d4",
                  "language": "PYTHON",
                  "code": "\nprint(\"hello world!\")\n"
                }
                "thought_signature": "..."
              },
              {
                "code_execution_result": {
                  "id": "a1b2c3d4",
                  "outcome": "OUTCOME_OK",
                  "output": "hello world!\n"
                }
              },
              {
                "text": "I have printed \"hello world!\" using the provided python code block. \n",
                "thought_signature": "..."
              }
            ],
        },{
            "role": "user",
            "parts": [{
                "text": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."
            }]
        }
    ]
}'
```

## Ein- und Ausgabe (E/A)

Die Codeausführung unterstützt die Dateieingabe und die Grafikausgabe. Mit diesen Ein- und
Ausgabefunktionen können Sie CSV- und Textdateien hochladen, Fragen zu den
Dateien stellen und [Matplotlib](https://matplotlib.org/)Diagramme als Teil
der Antwort generieren lassen. Die Ausgabedateien werden als Inline-Bilder in der Antwort zurückgegeben.

### E/A-Preise

Bei der Verwendung der Codeausführung für die Ein- und Ausgabe werden Ihnen Eingabe- und Ausgabetokens in Rechnung gestellt:

**Eingabetokens**

- Nutzer-Prompt

**Ausgabetokens**

- Code, der vom Modell generiert wurde
- Ausgabe der Codeausführung in der Codeumgebung
- Thinking-Tokens
- Vom Modell generierte Zusammenfassung

### E/A-Details

Beachten Sie bei der Arbeit mit der Codeausführung für die Ein- und Ausgabe die folgenden technischen Details:

- Die maximale Laufzeit der Codeumgebung beträgt 30 Sekunden.
- Wenn die Codeumgebung einen Fehler generiert, kann das Modell die Codeausgabe neu generieren. Das kann bis zu fünf Mal passieren.
- Die maximale Größe der Eingabedatei ist durch das Tokenfenster des Modells begrenzt. In AI Studio beträgt die maximale Größe der Eingabedatei 1 Million Tokens (ungefähr 2 MB für Textdateien der unterstützten Eingabetypen). Wenn Sie eine zu große Datei hochladen, können Sie sie in AI Studio nicht senden.
- Die Codeausführung funktioniert am besten mit Text- und CSV-Dateien.
- Die Eingabedatei kann in `part.inlineData` oder `part.fileData` übergeben werden (über die [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de) hochgeladen). Die Ausgabedatei wird immer als `part.inlineData` zurückgegeben.

## Abrechnung

Für die Aktivierung der Codeausführung über die Gemini API fallen keine zusätzlichen Kosten an.
Die Abrechnung erfolgt zum aktuellen Preis für Eingabe- und Ausgabetokens basierend auf dem verwendeten Gemini-Modell.

Weitere Informationen zur Abrechnung der Codeausführung:

- Sie werden nur einmal für die Eingabetokens in Rechnung gestellt, die Sie an das Modell übergeben. Außerdem werden Ihnen die endgültigen Ausgabetokens in Rechnung gestellt, die Sie vom Modell erhalten.
- Tokens, die generierten Code darstellen, werden als Ausgabetokens gezählt. Generierter Code kann Text und multimodale Ausgaben wie Bilder enthalten.
- Die Ergebnisse der Codeausführung werden ebenfalls als Ausgabetokens gezählt.

Das Abrechnungsmodell ist im folgenden Diagramm dargestellt:

![Abrechnungsmodell für die Codeausführung](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=de)

- Die Abrechnung erfolgt zum aktuellen Preis für Eingabe- und Ausgabetokens basierend auf dem verwendeten Gemini-Modell.
- Wenn Gemini bei der Generierung Ihrer Antwort die Codeausführung verwendet, werden der ursprüngliche Prompt, der generierte Code und das Ergebnis des ausgeführten Codes als *Zwischentokens* bezeichnet und als *Eingabetokens* in Rechnung gestellt.
- Gemini generiert dann eine Zusammenfassung und gibt den generierten Code, das Ergebnis des ausgeführten Codes und die endgültige Zusammenfassung zurück. Diese werden als *Ausgabetokens* in Rechnung gestellt.
- Die Gemini API enthält eine Anzahl der Zwischentokens in der API-Antwort, damit Sie wissen, warum Sie zusätzliche Eingabetokens über Ihren ursprünglichen Prompt hinaus erhalten.

## Beschränkungen

- Das Modell kann nur Code generieren und ausführen. Es kann keine anderen Artefakte wie Mediendateien zurückgeben.
- In einigen Fällen kann die Aktivierung der Codeausführung zu Regressionen in anderen Bereichen der Modellausgabe führen (z. B. beim Schreiben einer Geschichte).
- Die Fähigkeit der verschiedenen Modelle, die Codeausführung erfolgreich zu nutzen, variiert.

## Unterstützte Toolkombinationen

Das Tool zur Codeausführung kann mit
[der Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de) kombiniert werden, um
komplexere Anwendungsfälle zu ermöglichen.

Gemini 3-Modelle unterstützen die Kombination von integrierten Tools (z. B. Codeausführung) mit benutzerdefinierten Tools (Funktionsaufrufe). Sie müssen die Felder `id` und `thought_signature` zurückgeben, damit die Toolkombination funktioniert. Weitere Informationen finden Sie auf der
[Seite Toolkombinationen](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de).

## Unterstützte Bibliotheken

Die Codeausführungsumgebung enthält die folgenden Bibliotheken:

- attrs
- chess
- contourpy
- fpdf
- geopandas
- imageio
- jinja2
- joblib
- jsonschema
- jsonschema-specifications
- lxml
- matplotlib
- mpmath
- numpy
- opencv-python
- openpyxl
- packaging
- pandas
- pillow
- protobuf
- pylatex
- pyparsing
- PyPDF2
- python-dateutil
- python-docx
- python-pptx
- reportlab
- scikit-learn
- scipy
- seaborn
- six
- striprtf
- sympy
- tabulate
- tensorflow
- toolz
- xlrd

Sie können keine eigenen Bibliotheken installieren.

## Nächste Schritte

- Probieren Sie das
  [Colab zur Code-Ausführung aus](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Code_Execution.ipynb?hl=de).
- Weitere Informationen zu anderen Gemini API-Tools:
  - [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)
  - [Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/grounding?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
