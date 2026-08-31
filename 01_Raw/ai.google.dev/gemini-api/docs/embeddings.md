---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=it
fetched_at: 2026-08-31T06:37:53.985561+00:00
title: "Embedding \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Embedding

L'API Gemini offre modelli di incorporamento per generare incorporamenti per testo, immagini,
video e altri contenuti. Questi embedding risultanti possono essere utilizzati per attività
come la ricerca semantica, la classificazione e il clustering, fornendo risultati più accurati
e sensibili al contesto rispetto agli approcci basati su parole chiave.

L'ultimo modello, `gemini-embedding-2`, è il primo modello di embedding multimodale nell'API Gemini. Mappa testo, immagini,
video, audio e documenti in uno spazio di incorporamento unificato, consentendo la ricerca,
la classificazione e il clustering cross-modali in oltre 100 lingue. Per saperne di più, consulta la
[sezione sugli incorporamenti multimodali](#multimodal). Per i casi d'uso
solo testo, `gemini-embedding-001` rimane disponibile.

La creazione di sistemi di Retrieval Augmented Generation (RAG) è un caso d'uso comune per
i prodotti AI. Gli incorporamenti svolgono un ruolo chiave nel migliorare significativamente gli output del modello
con una maggiore accuratezza, coerenza e ricchezza contestuale. Se preferisci
utilizzare una soluzione RAG gestita, abbiamo creato lo strumento [Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)
che rende la RAG più facile da gestire e più conveniente.

## Generazione degli incorporamenti in corso…

Utilizza il metodo `embedContent` per generare incorporamenti di testo:

### Python

```
from google import genai

client = genai.Client()

result = client.models.embed_content(
        model="gemini-embedding-2",
        contents="What is the meaning of life?"
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {

    const ai = new GoogleGenAI({});

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: 'What is the meaning of life?',
    });

    console.log(response.embeddings);
}

main();
```

### Go

```
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    contents := []*genai.Content{
        genai.NewContentFromText("What is the meaning of life?", genai.RoleUser),
    }
    result, err := client.Models.EmbedContent(ctx,
        "gemini-embedding-2",
        contents,
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }

    embeddings, err := json.MarshalIndent(result.Embeddings, "", "  ")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(string(embeddings))
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "model": "models/gemini-embedding-2",
        "content": {
        "parts": [{
            "text": "What is the meaning of life?"
        }]
        }
    }'
```

## Specifica il tipo di attività per migliorare il rendimento

Puoi utilizzare gli incorporamenti per un'ampia gamma di attività, dalla classificazione alla ricerca di documenti. Specificare il tipo di attività corretto consente di ottimizzare gli incorporamenti per le
relazioni previste, massimizzando l'accuratezza e l'efficienza.

### Tipi di attività con Embeddings 2

Per le attività solo di testo con `gemini-embedding-2`, ti consigliamo vivamente di
aggiungere le istruzioni dell'attività nel prompt. A questo scopo, formatta la query e il documento con il prefisso dell'attività corretto.

Le tabelle seguenti mostrano esempi di formattazione di query e documenti per casi d'uso simmetrici e asimmetrici utilizzando il modello `gemini-embedding-2`.

**Casi d'uso per il recupero (formato asimmetrico)**

Nei casi d'uso asimmetrici, aggiungi il prefisso dell'attività alla query e applica
la struttura del documento per i contenuti che vuoi incorporare e recuperare.

| Caso d'uso | Struttura della query | Struttura del documento |
| --- | --- | --- |
| Query di ricerca | `task: search result | query: {content}` | `title: {title} | text: {content}` Se non è presente un titolo, utilizza `title: none`. |
| Question answering | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| Fact checking | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| Recupero del codice | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**Esempio di utilizzo**

### Python

```
# Generate embedding for a task's query. Use your correct task here:
def prepare_query(query):
    # return f"task: question answering | query: {query}"
    # return f"task: fact checking | query: {query}"
    # return f"task: code retrieval | query: {query}"
    return f"task: search result | query: {query}"

# Generate embedding for document of an asymmetric retrieval task:
def prepare_document(content, title=None):
    if title is None:
        title = "none"
    return f"title: {title} | text: {content}"
```

**Casi d'uso con un solo input (formato simmetrico)**

Nei casi d'uso simmetrici, per la stessa attività, utilizza la stessa formattazione
per la query e il documento.

| Caso d'uso | Struttura dell'input |
| --- | --- |
| Classificazione | `task: classification | query: {content}` |
| Clustering | `task: clustering | query: {content}` |
| Similarità semantica | `task: sentence similarity | query: {content}` Non utilizzare questo campo per la ricerca o il recupero. È destinato alla similarità semantica del testo. |

**Esempio di utilizzo**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

È importante che l'attività venga utilizzata in modo coerente. Ad esempio, se i documenti sono
incorporati con `f'task: classification | query: {content}'`, anche la query deve
essere incorporata seguendo il formato di questa attività.

### Tipi di attività con incorporamenti 1

Per `gemini-embedding-001`, puoi specificare `task_type` nel metodo `embedContent`. Per un elenco completo dei tipi di attività supportati, consulta la tabella [Tipi di attività supportati](#supported-task-types).

Il seguente esempio mostra come utilizzare `SEMANTIC_SIMILARITY` per verificare il grado di somiglianza del significato di stringhe di testo.

### Python

```
from google import genai
from google.genai import types
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

client = genai.Client()

texts = [
    "What is the meaning of life?",
    "What is the purpose of existence?",
    "How do I bake a cake?",
]

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts,
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)

# Create a 3x3 table to show the similarity matrix
df = pd.DataFrame(
    cosine_similarity([e.values for e in result.embeddings]),
    index=texts,
    columns=texts,
)

print(df)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
// npm i compute-cosine-similarity
import * as cosineSimilarity from "compute-cosine-similarity";

async function main() {
    const ai = new GoogleGenAI({});

    const texts = [
        "What is the meaning of life?",
        "What is the purpose of existence?",
        "How do I bake a cake?",
    ];

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-001',
        contents: texts,
        config: { taskType: 'SEMANTIC_SIMILARITY' },
    });

    const embeddings = response.embeddings.map(e => e.values);

    for (let i = 0; i < texts.length; i++) {
        for (let j = i + 1; j < texts.length; j++) {
            const text1 = texts[i];
            const text2 = texts[j];
            const similarity = cosineSimilarity(embeddings[i], embeddings[j]);
            console.log(`Similarity between '${text1}' and '${text2}': ${similarity.toFixed(4)}`);
        }
    }
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "math"

    "google.golang.org/genai"
)

// cosineSimilarity calculates the similarity between two vectors.
func cosineSimilarity(a, b []float32) (float64, error) {
    if len(a) != len(b) {
        return 0, fmt.Errorf("vectors must have the same length")
    }

    var dotProduct, aMagnitude, bMagnitude float64
    for i := 0; i < len(a); i++ {
        dotProduct += float64(a[i] * b[i])
        aMagnitude += float64(a[i] * a[i])
        bMagnitude += float64(b[i] * b[i])
    }

    if aMagnitude == 0 || bMagnitude == 0 {
        return 0, nil
    }

    return dotProduct / (math.Sqrt(aMagnitude) * math.Sqrt(bMagnitude)), nil
}

func main() {
    ctx := context.Background()
    client, _ := genai.NewClient(ctx, nil)
    defer client.Close()

    texts := []string{
        "What is the meaning of life?",
        "What is the purpose of existence?",
        "How do I bake a cake?",
    }

    var contents []*genai.Content
    for _, text := range texts {
        contents = append(contents, genai.NewContentFromText(text, genai.RoleUser))
    }

    result, _ := client.Models.EmbedContent(ctx,
        "gemini-embedding-001",
        contents,
        &genai.EmbedContentRequest{TaskType: genai.TaskTypeSemanticSimilarity},
    )

    embeddings := result.Embeddings

    for i := 0; i < len(texts); i++ {
        for j := i + 1; j < len(texts); j++ {
            similarity, _ := cosineSimilarity(embeddings[i].Values, embeddings[j].Values)
            fmt.Printf("Similarity between '%s' and '%s': %.4f\n", texts[i], texts[j], similarity)
        }
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -d '{
    "taskType": "SEMANTIC_SIMILARITY",
    "content": {
        "parts": [
        {
            "text": "What is the meaning of life?"
        },
        {
            "text": "How much wood would a woodchuck chuck?"
        },
        {
            "text": "How does the brain work?"
        }
        ]
    }
    }'
```

Gli snippet di codice mostreranno il grado di somiglianza tra i diversi blocchi di testo quando vengono eseguiti.

#### Tipi di attività supportati

Tipi di attività supportati per `gemini-embedding-001`:

| Tipo di attività | Descrizione | Esempi |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | Incorporamenti ottimizzati per valutare la somiglianza del testo. | Sistemi di suggerimenti, rilevamento dei duplicati |
| **CLASSIFICAZIONE** | Incorporamenti ottimizzati per classificare i testi in base a etichette preimpostate. | Analisi del sentiment, rilevamento dello spam |
| **CLUSTERING** | Incorporamenti ottimizzati per raggruppare i testi in base alle loro somiglianze. | Organizzazione dei documenti, ricerca di mercato, rilevamento anomalie |
| **RETRIEVAL\_DOCUMENT** | Incorporamenti ottimizzati per la ricerca di documenti. | Indicizzazione di articoli, libri o pagine web per la ricerca. |
| **RETRIEVAL\_QUERY** | Incorporamenti ottimizzati per le query di ricerca generali. Utilizza `RETRIEVAL_QUERY` per le query e `RETRIEVAL_DOCUMENT` per i documenti da recuperare. | Ricerca personalizzata |
| **CODE\_RETRIEVAL\_QUERY** | Incorporamenti ottimizzati per il recupero di blocchi di codice in base a query in linguaggio naturale. Utilizza `CODE_RETRIEVAL_QUERY` per le query e `RETRIEVAL_DOCUMENT` per i blocchi di codice da recuperare. | Suggerimenti di codice e ricerca |
| **QUESTION\_ANSWERING** | Incorporamenti per le domande in un sistema di risposta alle domande, ottimizzati per trovare documenti che rispondono alla domanda. Utilizza `QUESTION_ANSWERING` per le domande e `RETRIEVAL_DOCUMENT` per i documenti da recuperare. | Chatbox |
| **FACT\_VERIFICATION** | Incorporamenti per le affermazioni che devono essere verificate, ottimizzati per il recupero di documenti che contengono prove a sostegno o confutazione dell'affermazione. Utilizza `FACT_VERIFICATION` per il testo di destinazione; `RETRIEVAL_DOCUMENT` per i documenti da recuperare | Sistemi di verifica dei fatti automatizzati |

## Controllare le dimensioni dell'incorporamento

Sia `gemini-embedding-001` che `gemini-embedding-2` vengono addestrati utilizzando la tecnica di apprendimento della rappresentazione Matrioska (MRL), che insegna a un modello a imparare incorporamenti di grandi dimensioni con segmenti iniziali (o prefissi) che sono anche versioni più semplici e utili degli stessi dati.

Utilizza il parametro `output_dimensionality` per controllare le dimensioni
del vettore di incorporamento di output. La selezione di una dimensionalità di output più piccola può consentire di risparmiare
spazio di archiviazione e aumentare l'efficienza di calcolo per le applicazioni downstream,
sacrificando poco in termini di qualità. Per impostazione predefinita, entrambi i modelli restituiscono un embedding
a 3072 dimensioni, ma puoi troncarlo a una dimensione più piccola senza
perdere qualità per risparmiare spazio di archiviazione. Ti consigliamo di utilizzare dimensioni di output pari a 768, 1536 o 3072.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents="What is the meaning of life?",
    config=types.EmbedContentConfig(output_dimensionality=768)
)

[embedding_obj] = result.embeddings
embedding_length = len(embedding_obj.values)

print(f"Length of embedding: {embedding_length}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {
    const ai = new GoogleGenAI({});

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: 'What is the meaning of life?',
        config: { outputDimensionality: 768 },
    });

    const embeddingLength = response.embeddings[0].values.length;
    console.log(`Length of embedding: ${embeddingLength}`);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // The client uses Application Default Credentials.
    // Authenticate with 'gcloud auth application-default login'.
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    contents := []*genai.Content{
        genai.NewContentFromText("What is the meaning of life?", genai.RoleUser),
    }

    result, err := client.Models.EmbedContent(ctx,
        "gemini-embedding-2",
        contents,
        &genai.EmbedContentRequest{OutputDimensionality: 768},
    )
    if err != nil {
        log.Fatal(err)
    }

    embedding := result.Embeddings[0]
    embeddingLength := len(embedding.Values)
    fmt.Printf("Length of embedding: %d\n", embeddingLength)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H 'Content-Type: application/json' \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -d '{
        "content": {"parts":[{ "text": "What is the meaning of life?"}]},
        "output_dimensionality": 768
    }'
```

Output di esempio dello snippet di codice:

```
Length of embedding: 768
```

## Garantire la qualità per le dimensioni più piccole

Mentre gli incorporamenti predefiniti a 3072 dimensioni sono sempre normalizzati, Gemini
Embedding 2 normalizza automaticamente anche le dimensioni troncate (ad es. 768, 1536). In questo modo, la similarità semantica viene calcolata tramite la direzione del vettore anziché la magnitudo, fornendo risultati più accurati fin da subito.

**Modelli precedenti**: se utilizzi `gemini-embedding-001`, devi normalizzare manualmente
le dimensioni non 3072 nel seguente modo:

### Python

```
import numpy as np
from numpy.linalg import norm

# Only for embeddings from `gemini-embedding-001`
embedding_values_np = np.array(embedding_obj.values)
normed_embedding = embedding_values_np / np.linalg.norm(embedding_values_np)

print(f"Normed embedding length: {len(normed_embedding)}")
print(f"Norm of normed embedding: {np.linalg.norm(normed_embedding):.6f}") # Should be very close to 1
```

Output di esempio di questo snippet di codice:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

La tabella seguente mostra i punteggi MTEB, un benchmark di uso comune per
gli incorporamenti, per diverse dimensioni. In particolare, il risultato mostra che il rendimento
non è strettamente legato alle dimensioni della dimensione di incorporamento, con dimensioni
inferiori che ottengono punteggi paragonabili a quelli delle dimensioni superiori.

| Dimensione MRL | Punteggio MTEB (Gemini Embedding 001) |
| --- | --- |
| 2048 | 68.16 |
| 1536 | 68.17 |
| 768 | 67,99 |
| 512 | 67,55 |
| 256 | 66,19 |
| 128 | 63,31 |

## Embedding multimodali

Il modello `gemini-embedding-2` supporta l'input multimodale, consentendoti
di incorporare contenuti di immagini, video, audio e documenti insieme al testo. Tutte le modalità
vengono mappate nello stesso spazio di incorporamento, consentendo la ricerca e
il confronto cross-modale.

### Modalità supportate e limiti

Il limite massimo complessivo di token di input è di 8192 token.

| Modalità | Specifiche e limiti |
| --- | --- |
| **Testo** | Supporta fino a 8192 token. |
| **Image** | Massimo 6 immagini per richiesta. Formati supportati: PNG, JPEG. |
| **Audio** | Durata massima di 180 secondi. Formati supportati: MP3, WAV. |
| **Video** | Durata massima di 120 secondi. Formati supportati: MP4, MOV. Codec supportati: H264, H265, AV1, VP9.  Il sistema elabora un massimo di 32 fotogrammi per video: i video brevi (≤ 32 secondi) vengono campionati a 1 fps, mentre i video più lunghi vengono campionati in modo uniforme a 32 fotogrammi. Le tracce audio non vengono elaborate nei file video. |
| **Documenti (PDF)** | Massimo un file per richiesta, fino a 6 pagine. |

### Incorporare immagini

L'esempio seguente mostra come incorporare un'immagine utilizzando
`gemini-embedding-2`.

Le immagini possono essere fornite come dati in linea o come file caricati
tramite l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it).

### Python

```
from google import genai
from google.genai import types

with open('example.png', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("example.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'image/png',
                data: imgBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### REST

```
IMG_PATH="/path/to/your/image.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "image/png",
                    "data": "'"${IMG_BASE64}"'"
                }
            }]
        }
    }'
```

### Aggregazione dell'incorporamento

Quando lavori con contenuti multimodali, la struttura dell'input influisce sull'output
dell'incorporamento:

- **Più parti (aggregate)**: l'aggiunta di più input direttamente al
  parametro `contents` produce un incorporamento aggregato per tutti gli input.
- **Più oggetti `Content` (separati)**: il wrapping di ogni input in un oggetto `Content` e il passaggio nel parametro `contents` restituiscono incorporamenti separati per ogni voce.
- **Rappresentazione a livello di post:** per oggetti complessi come i post sui social media
  con più elementi multimediali, ti consigliamo di aggregare incorporamenti separati
  (ad esempio, calcolando la media) per creare una rappresentazione coerente a livello di post.

L'esempio seguente mostra come creare un incorporamento aggregato per l'input di testo e
immagine. Basta aggiungere più input al parametro `contents`:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('dog.png', 'rb') as f:
    image_bytes = f.read()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        "An image of a dog",
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
    ]
)

# This produces one embedding
for embedding in result.embeddings:
    print(embedding.values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("dog.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [
            'An image of a dog',
            {
                inlineData: {
                    mimeType: 'image/png',
                    data: imgBase64,
                },
            },
        ],
    });

    // This produces one embedding
    for (const embedding of response.embeddings) {
        console.log(embedding.values);
    }
}

main();
```

### REST

```
IMG_PATH="/path/to/your/dog.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [
                {"text": "An image of a dog"},
                {
                    "inline_data": {
                        "mime_type": "image/png",
                        "data": "'"${IMG_BASE64}"'"
                    }
                }
            ]
        }
    }'
```

D'altra parte, se utilizzi oggetti `Content` all'interno del parametro `contents`,
restituisce incorporamenti separati. Questo esempio crea più incorporamenti in una
chiamata di incorporamento:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('dog.png', 'rb') as f:
    image_bytes = f.read()

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents=[
        types.Content(parts=[types.Part.from_text(text="An image of a dog")]),
        types.Content(
            parts=[
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/png",
                ),
            ]
        ),
    ],
)

# This produces two embeddings
for embedding in result.embeddings:
    print(embedding.values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("dog.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [
            { parts: [{ text: 'An image of a dog' }] },
            {
                parts: [{
                    inlineData: {
                        mimeType: 'image/png',
                        data: imgBase64,
                    },
                }],
            },
        ],
    });

    // This produces two embeddings
    for (const embedding of response.embeddings) {
        console.log(embedding.values);
    }
}

main();
```

### REST

```
IMG_PATH="/path/to/your/dog.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:batchEmbedContents" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "requests": [
            {
                "model": "models/gemini-embedding-2",
                "content": {"parts": [{"text": "An image of a dog"}]}
            },
            {
                "model": "models/gemini-embedding-2",
                "content": {"parts": [{"inline_data": {"mime_type": "image/png", "data": "'"${IMG_BASE64}"'"}}]}
            }
        ]
    }'
```

### Incorporare l'audio

L'esempio seguente mostra come incorporare un file audio utilizzando
`gemini-embedding-2`.

I file audio possono essere forniti come dati incorporati o come file caricati
tramite l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it).

### Python

```
from google import genai
from google.genai import types

with open('example.mp3', 'rb') as f:
    audio_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=audio_bytes,
            mime_type='audio/mpeg',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const audioBase64 = fs.readFileSync("example.mp3", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'audio/mpeg',
                data: audioBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### REST

```
AUDIO_PATH="/path/to/your/example.mp3"
AUDIO_BASE64=$(base64 -w0 "${AUDIO_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "audio/mpeg",
                    "data": "'"${AUDIO_BASE64}"'"
                }
            }]
        }
    }'
```

### Incorporamento di video

L'esempio seguente mostra come incorporare un video utilizzando
`gemini-embedding-2`.

I video possono essere forniti come dati in linea o come file caricati
tramite l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('example.mp4', 'rb') as f:
    video_bytes = f.read()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=video_bytes,
            mime_type='video/mp4',
        ),
    ]
)

print(result.embeddings[0].values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const videoBase64 = fs.readFileSync("example.mp4", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'video/mp4',
                data: videoBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### REST

```
VIDEO_PATH="/path/to/your/video.mp4"
VIDEO_BASE64=$(base64 -w0 "${VIDEO_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "video/mp4",
                    "data": "'"${VIDEO_BASE64}"'"
                }
            }]
        }
    }'
```

Se devi incorporare video di durata superiore a 120 secondi, puoi suddividerli in segmenti sovrapposti e incorporarli singolarmente.

### Incorporare documenti

I documenti in formato PDF possono essere incorporati direttamente. Il modello elabora i contenuti
visivi e di testo di ogni pagina.

I PDF possono essere forniti come dati incorporati o come file caricati
tramite l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it).

#### Come il modello elabora i PDF

Quando incorpori un PDF, il modello elabora il documento utilizzando sia le funzionalità visive che quelle di testo:

- **Rappresentazione visiva**:il modello esegue il rendering di ogni pagina come immagine, che consuma **258 token** per pagina.
- **Estrazione del testo**:il modello estrae il testo dal documento. Per i **PDF nativi** (che contengono testo digitale), il modello estrae il testo direttamente. Per i **PDF scansionati** (che contengono immagini di testo), il modello esegue automaticamente il riconoscimento ottico dei caratteri (OCR) per estrarre il testo.

Per calcolare il numero totale di token per un PDF, somma i token visivi (258 per pagina) ai token di testo. Gli input devono rientrare nel **limite di 8192 token** del modello (condiviso tra tutte le modalità). Il sistema tronca automaticamente gli input che superano questo limite.

#### Limiti dei PDF

- **File per richiesta**:puoi inviare un massimo di un file PDF.
- **Limite di pagine**:puoi inviare un massimo di 6 pagine per file. Per una qualità ottimale, ti consigliamo vivamente di utilizzare una pagina per PDF.

L'esempio seguente mostra come incorporare un PDF utilizzando `gemini-embedding-2`:

### Python

```
from google import genai
from google.genai import types

with open('example.pdf', 'rb') as f:
    pdf_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=pdf_bytes,
            mime_type='application/pdf',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const pdfBase64 = fs.readFileSync("example.pdf", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'application/pdf',
                data: pdfBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### REST

```
PDF_PATH="/path/to/your/example.pdf"
PDF_BASE64=$(base64 -w0 "${PDF_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "application/pdf",
                    "data": "'"${PDF_BASE64}"'"
                }
            }]
        }
    }'
```

## Casi d'uso

Gli incorporamenti di testo sono fondamentali per una serie di casi d'uso comuni dell'AI, ad esempio:

- **Retrieval-Augmented Generation (RAG)**: gli incorporamenti migliorano la qualità
  del testo generato recuperando e incorporando informazioni pertinenti nel
  contesto di un modello.
- **Recupero delle informazioni**:cerca il testo o i documenti semanticamente più simili dato un testo di input.

  [Tutorial sulla ricerca di documentitask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **Riorganizzazione della ricerca**: dai la priorità agli elementi più pertinenti assegnando un punteggio semantico ai risultati iniziali in base alla query.

  [Tutorial sul ranking delle ricerchetask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **Rilevamento di anomalie:** il confronto di gruppi di incorporamenti può aiutare a identificare
  tendenze nascoste o valori anomali.

  [Tutorial sul rilevamento di anomaliebubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **Classificazione**:categorizza automaticamente il testo in base ai suoi contenuti, ad esempio
  l'analisi del sentiment o il rilevamento dello spam

  [Tutorial sulla classificazionetoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **Clustering**:comprendi in modo efficace le relazioni complesse creando cluster e visualizzazioni degli incorporamenti.

  [Tutorial sulla visualizzazione del clusteringbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## Memorizzazione degli incorporamenti

Quando porti gli incorporamenti in produzione, è comune utilizzare **database vettoriali** per archiviare, indicizzare e recuperare in modo efficiente gli incorporamenti ad alta dimensionalità. Google Cloud offre servizi di dati gestiti che
possono essere utilizzati a questo scopo, tra cui
[Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/BUILD/vector-search-2?hl=it),
[BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=it), [AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=it) e
[Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=it).

I seguenti tutorial mostrano come utilizzare altri database vettoriali di terze parti
con Gemini Embedding.

- [Tutorial di ChromaDBbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [Tutorial di QDrantbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Tutorial di Weaviatebolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Tutorial di Pineconebolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## Versioni modello

### Embedding Gemini 2

| Proprietà | Descrizione |
| --- | --- |
| Codice modello id\_card | **API Gemini**  `gemini-embedding-2` |
| saveTipi di dati supportati | **Ingresso**  Testo, immagine, video, audio, PDF  **Output**  Text embedding |
| token\_autoLimiti dei token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=it) | **Limite di token di input**  8192  **Dimensioni della dimensione di output**  Flessibile, supporta: 128 - 3072, consigliato: 768, 1536, 3072 |
| Versioni 123 | Per ulteriori dettagli, leggi i [pattern delle versioni del modello](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#model-versions).  - Stabile: `gemini-embedding-2` |
| calendar\_monthUltimo aggiornamento | Aprile 2026 |

### Incorporamento di Gemini

| Proprietà | Descrizione |
| --- | --- |
| Codice modello id\_card | **API Gemini**  `gemini-embedding-001` |
| saveTipi di dati supportati | **Ingresso**  Testo  **Output**  Text embedding |
| token\_autoLimiti dei token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=it) | **Limite di token di input**  2048  **Dimensioni della dimensione di output**  Flessibile, supporta: 128 - 3072, consigliato: 768, 1536, 3072 |
| Versioni 123 | Per ulteriori dettagli, leggi i [pattern delle versioni del modello](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#model-versions).  - Stabile: `gemini-embedding-001` |
| calendar\_monthUltimo aggiornamento | Giugno 2025 |

Per i modelli di incorporamento ritirati, visita la pagina [Ritiri](https://ai.google.dev/gemini-api/docs/deprecations?hl=it).

## Migrazione da gemini-embedding-001

Gli spazi di incorporamento tra `gemini-embedding-001` e
`gemini-embedding-2` sono **incompatibili**. Ciò significa che non puoi
confrontare direttamente gli incorporamenti generati da un modello con quelli generati
dall'altro. Se esegui l'upgrade a `gemini-embedding-2`, devi incorporare nuovamente tutti i dati esistenti.

Oltre all'incompatibilità, esistono diverse altre differenze notevoli tra
i due modelli:

- **Specifica del tipo di attività**:con `gemini-embedding-001`, specifichi il tipo di attività utilizzando il parametro `task_type` (ad es. `SEMANTIC_SIMILARITY`, `RETRIEVAL_DOCUMENT`). Con `gemini-embedding-2`, il parametro `task_type` non è supportato. Devi invece includere le istruzioni per l'attività
  direttamente nel prompt per le attività solo di testo. Per informazioni dettagliate su come formattare i prompt per diversi casi d'uso, consulta la sezione [Tipi di attività con Embeddings 2](#task-types-embeddings-2).
- **Aggregazione di incorporamenti**:`gemini-embedding-001` genera incorporamenti
  individuali per ogni stringa in un elenco di input. Al contrario,
  `gemini-embedding-2` produce un unico embedding aggregato quando più
  input (come testo e immagini) vengono forniti direttamente in una richiesta. Per
  generare incorporamenti separati per i singoli input, racchiudi ogni input in un
  oggetto `Content` o utilizza l'[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it#batch-embedding). Per saperne di più, consulta [Incorporamento dell'aggregazione](#embedding-aggregation).
- **Normalizzazione**:se utilizzi `output_dimensionality` per richiedere incorporamenti
  con meno di 3072 dimensioni, `gemini-embedding-2` normalizza automaticamente
  questi incorporamenti troncati. Con `gemini-embedding-001`, devi eseguire la normalizzazione manuale per le dimensioni diverse da 3072. Per i dettagli, vedi
  [Garantire la qualità per le dimensioni più piccole](#quality-for-smaller-dimensions).

## Incorporamenti batch

Se la latenza non è un problema, prova a utilizzare i modelli Gemini Embeddings con l'[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it#batch-embedding). Ciò
consente un throughput molto più elevato al 50% del prezzo di Embedding predefinito.
Trova esempi su come iniziare nella [raccolta di ricette dell'API Batch](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb).

## Avviso sull'utilizzo responsabile

A differenza dei modelli di AI generativa che creano nuovi contenuti, il modello Gemini Embedding
è destinato solo a trasformare il formato dei dati di input in una rappresentazione
numerica. Sebbene Google sia responsabile di fornire un modello di incorporamento
che trasforma il formato dei dati di input nel formato numerico richiesto,
gli utenti mantengono la piena responsabilità dei dati inseriti e degli incorporamenti
risultanti. Utilizzando il modello Gemini Embedding, confermi di detenere i
diritti necessari per i contenuti caricati. Non generare contenuti che
violano la proprietà intellettuale o i diritti di privacy altrui. L'utilizzo di questo
servizio è soggetto alle nostre [Norme relative all'uso
vietato](https://policies.google.com/terms/generative-ai/use-policy?hl=it) e ai
[Termini di servizio di Google](https://ai.google.dev/gemini-api/terms?hl=it).

## Inizia a creare con gli incorporamenti

Consulta il [notebook della guida rapida
sugli incorporamenti](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb)
per esplorare le funzionalità del modello e scoprire come personalizzare e visualizzare gli
incorporamenti.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-22 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-22 UTC."],[],[]]
