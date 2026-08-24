---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/code-execution?hl=it
fetched_at: 2026-08-24T02:32:30.241565+00:00
title: "Eseguire il codice \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Eseguire il codice

L'API Gemini fornisce uno strumento di esecuzione del codice che consente al modello di generare ed eseguire codice Python. Il modello può quindi apprendere in modo iterativo dai risultati dell'esecuzione del codice fino a raggiungere un output finale. Puoi utilizzare l'esecuzione del codice per creare applicazioni che sfruttano il ragionamento basato sul codice. Ad esempio, puoi utilizzare l'esecuzione del codice per risolvere equazioni o elaborare testo. Puoi
anche utilizzare le [librerie](#supported-libraries) incluse nell'ambiente di esecuzione del codice
per eseguire attività più specializzate.

Gemini è in grado di eseguire codice solo in Python. Puoi comunque chiedere a Gemini di generare codice in un'altra lingua, ma il modello non può utilizzare lo strumento di esecuzione del codice per eseguirlo.

## Abilitare l'esecuzione del codice

Per abilitare l'esecuzione del codice, configura lo strumento di esecuzione del codice sul modello. In questo modo, il modello può generare ed eseguire codice.

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

### Vai

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

L'output potrebbe essere simile al seguente, formattato per una maggiore leggibilità:

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

Questo output combina diverse parti di contenuti restituite dal modello quando si utilizza l'esecuzione del codice:

- `text`: testo in linea generato dal modello
- `executableCode`: codice generato dal modello che deve essere eseguito
- `codeExecutionResult`: risultato del codice eseguibile

Le convenzioni di denominazione per queste parti variano a seconda del linguaggio di programmazione.

## Esecuzione del codice con immagini (Gemini 3)

Il modello Gemini 3 Flash ora può scrivere ed eseguire codice Python per manipolare e ispezionare attivamente le immagini.

**Casi d'uso**

- **Zoom e ispezione**: il modello rileva implicitamente quando i dettagli sono troppo piccoli (ad es. la lettura di un misuratore distante) e scrive codice per ritagliare e riesaminare l'area a una risoluzione più elevata.
- **Matematica visiva**: il modello può eseguire calcoli in più passaggi utilizzando il codice (ad es.
  la somma delle voci di riga in una ricevuta).
- **Annotazione delle immagini**: il modello può annotare le immagini per rispondere alle domande, ad esempio disegnando frecce per mostrare le relazioni.

### Abilitare l'esecuzione del codice con le immagini

L'esecuzione del codice con le immagini è ufficialmente supportata in Gemini 3 Flash. Puoi attivare questo comportamento abilitando sia l'esecuzione del codice come strumento sia il ragionamento.

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

### Vai

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

## Utilizzare l'esecuzione del codice nella chat

Puoi anche utilizzare l'esecuzione del codice come parte di una chat.

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

### Vai

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

## Input/output (I/O)

L'esecuzione del codice supporta l'input di file e l'output di grafici. Utilizzando queste funzionalità di input e
output, puoi caricare file CSV e di testo, porre domande sui
file e generare grafici [Matplotlib](https://matplotlib.org/) come parte
della risposta. I file di output vengono restituiti come immagini in linea nella risposta.

### Prezzi di I/O

Quando utilizzi l'I/O di esecuzione del codice, ti vengono addebitati i token di input e i token di output:

**Token di input:**

- Prompt dell'utente

**Token di output:**

- Codice generato dal modello
- Output di esecuzione del codice nell'ambiente di codice
- Token di ragionamento
- Riepilogo generato dal modello

### Dettagli di I/O

Quando lavori con l'I/O di esecuzione del codice, tieni presente i seguenti dettagli tecnici:

- Il runtime massimo dell'ambiente di codice è di 30 secondi.
- Se l'ambiente di codice genera un errore, il modello potrebbe decidere di rigenerare l'output del codice. Questa operazione può essere eseguita fino a 5 volte.
- La dimensione massima del file di input è limitata dalla finestra dei token del modello. In AI Studio, la dimensione massima del file di input è di 1 milione di token (circa 2 MB per i file di testo dei tipi di input supportati). Se carichi un file troppo grande, AI Studio non ti consentirà di inviarlo.
- L'esecuzione del codice funziona meglio con i file di testo e CSV.
- Il file di input può essere passato in `part.inlineData` o `part.fileData` (caricato
  tramite l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it)) e il file di output viene sempre
  restituito come `part.inlineData`.

## Fatturazione

Non sono previsti costi aggiuntivi per l'abilitazione dell'esecuzione del codice dall'API Gemini.
Ti verrà addebitata la tariffa corrente dei token di input e output in base al modello Gemini che stai utilizzando.

Ecco alcuni altri aspetti da sapere sulla fatturazione per l'esecuzione del codice:

- Ti viene addebitato un solo costo per i token di input che passi al modello e ti vengono addebitati i token di output finali restituiti dal modello.
- I token che rappresentano il codice generato vengono conteggiati come token di output. Il codice generato può includere testo e output multimodale come le immagini.
- Anche i risultati dell'esecuzione del codice vengono conteggiati come token di output.

Il modello di fatturazione è mostrato nel seguente diagramma:

![modello di fatturazione per l'esecuzione del codice](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=it)

- Ti viene addebitata la tariffa corrente dei token di input e output in base al modello Gemini che stai utilizzando.
- Se Gemini utilizza l'esecuzione del codice durante la generazione della risposta, il prompt originale, il codice generato e il risultato del codice eseguito vengono etichettati come *token intermedi* e vengono fatturati come *token di input*.
- Gemini genera quindi un riepilogo e restituisce il codice generato, il risultato del codice eseguito e il riepilogo finale. Questi vengono fatturati come *token di output*.
- L'API Gemini include un conteggio dei token intermedi nella risposta dell'API, in modo da sapere perché ricevi token di input aggiuntivi oltre al prompt iniziale.

## Limitazioni

- Il modello può solo generare ed eseguire codice. Non può restituire altri artefatti come i file multimediali.
- In alcuni casi, l'abilitazione dell'esecuzione del codice può comportare regressioni in altre aree dell'output del modello (ad esempio, la scrittura di una storia).
- Esiste una certa variazione nella capacità dei diversi modelli di utilizzare l'esecuzione del codice con successo.

## Combinazioni di strumenti supportate

Lo strumento di esecuzione del codice può essere combinato con
[il grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it) per
supportare casi d'uso più complessi.

I modelli Gemini 3 supportano la combinazione di strumenti integrati (come l'esecuzione del codice) con strumenti personalizzati (chiamata di funzione). Perché la combinazione di strumenti funzioni, devi restituire i campi `id` e `thought_signature`. Scopri di più nella pagina relativa alle
[combinazioni di strumenti](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it).

## Librerie supportate

L'ambiente di esecuzione del codice include le seguenti librerie:

- attrs
- scacchi
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
- pacchettizzazione
- panda
- cuscino
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
- sei
- striprtf
- sympy
- tabulate
- tensorflow
- toolz
- xlrd

Non puoi installare le tue librerie.

## Passaggi successivi

- Prova il
  [Colab di esecuzione del codice](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Code_Execution.ipynb?hl=it).
- Scopri di più sugli altri strumenti dell'API Gemini:
  - [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)
  - [Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/grounding?hl=it)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
