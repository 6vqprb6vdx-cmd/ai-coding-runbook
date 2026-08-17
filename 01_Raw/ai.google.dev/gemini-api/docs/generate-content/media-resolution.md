---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=it
fetched_at: 2026-08-17T02:26:12.868004+00:00
title: "Risoluzione dei contenuti multimediali \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Risoluzione dei contenuti multimediali

Il parametro `media_resolution` controlla il modo in cui l'API Gemini elabora gli input multimediali come immagini, video e documenti PDF determinando il **numero massimo di token** allocati per gli input multimediali, consentendoti di bilanciare la qualità della risposta rispetto alla latenza e al costo. Per le diverse impostazioni, i valori predefiniti e la loro corrispondenza con i token, consulta la sezione [Conteggi dei token](#token-counts).

Puoi configurare la risoluzione dei contenuti multimediali in due modi:

- [Per parte](https://ai.google.dev/gemini-api/docs/media-resolution?hl=it#per-part-media-resolution) (solo Gemini 3)
- [A livello globale](https://ai.google.dev/gemini-api/docs/media-resolution?hl=it#global-media-resolution) per un'intera richiesta `generateContent` (tutti i modelli multimodali)

## Risoluzione dei contenuti multimediali per parte (solo Gemini 3)

Gemini 3 ti consente di impostare la risoluzione dei contenuti multimediali per singoli oggetti multimediali all'interno della richiesta, offrendo un'ottimizzazione granulare dell'utilizzo dei token. Puoi combinare i livelli di risoluzione in una singola richiesta. Ad esempio, puoi utilizzare l'alta risoluzione per un diagramma complesso e la bassa risoluzione per un'immagine contestuale semplice. Questa impostazione sostituisce qualsiasi configurazione globale per una parte specifica. Per le impostazioni predefinite, consulta la sezione [Conteggi dei token](https://ai.google.dev/gemini-api/docs/media-resolution?hl=it#token-counts).

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is available in the v1beta API version.
client = genai.Client(
  http_options={
      'api_version': 'v1beta',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1beta' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## Risoluzione globale dei contenuti multimediali

Puoi impostare una risoluzione predefinita per tutte le parti multimediali di una richiesta utilizzando `GenerationConfig`. Questa funzionalità è supportata da tutti i modelli multimodali. Se una richiesta
include sia impostazioni globali sia [per parte](https://ai.google.dev/gemini-api/docs/media-resolution?hl=it#per-part-media-resolution), l'impostazione per parte ha la precedenza per l'elemento specifico.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3.6-flash',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## Valori di risoluzione disponibili

L'API Gemini definisce i seguenti livelli per la risoluzione dei contenuti multimediali:

- `MEDIA_RESOLUTION_UNSPECIFIED`: l'impostazione predefinita. Il conteggio dei token per questo livello varia in modo significativo tra Gemini 3 e i modelli Gemini precedenti.
- `MEDIA_RESOLUTION_LOW`: conteggio dei token inferiore, con conseguente elaborazione più rapida e costi inferiori, ma con meno dettagli.
- `MEDIA_RESOLUTION_MEDIUM`: un equilibrio tra dettagli, costi e latenza.
- `MEDIA_RESOLUTION_HIGH`: conteggio dei token più elevato, che fornisce più dettagli al modello, a scapito di una maggiore latenza e di costi più elevati.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (solo per parte): conteggio dei token più elevato, necessario per casi d'uso specifici come l'[utilizzo del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it).

Tieni presente che `MEDIA_RESOLUTION_HIGH` offre prestazioni ottimali per la maggior parte dei casi d'uso.

Il numero esatto di token generati per ciascuno di questi livelli dipende sia dal **tipo di contenuti multimediali** (immagine, video, PDF) sia dalla **versione del modello**.

## Conteggi dei token

Le tabelle seguenti riepilogano i conteggi approssimativi dei token per ogni valore `media_resolution` e tipo di contenuti multimediali per famiglia di modelli.

**Modelli Gemini 3**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **Image** | **Video** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (valore predefinito) | 1120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 280 + testo nativo |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 560 + testo nativo |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 1120 + testo nativo |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | N/D | N/D |

**Modelli Gemini 2.5**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **Image** | **Video** | **PDF (scansionato)** | **PDF (nativo)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (valore predefinito) | 256 + panoramica e scansione (~2048) | 256 | 256 + OCR | 256 + testo nativo |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 64 + OCR | 64 + testo nativo |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 256 + OCR | 256 + testo nativo |
| `MEDIA_RESOLUTION_HIGH` | 256 + panoramica e scansione | 256 | 256 + OCR | 256 + testo nativo |

## Scegliere la risoluzione giusta

- **Valore predefinito (`UNSPECIFIED`):** inizia con il valore predefinito. È ottimizzato per un buon equilibrio tra qualità, latenza e costi per i casi d'uso più comuni.
- **`LOW`:** utilizza questa impostazione per gli scenari in cui i costi e la latenza sono fondamentali e i dettagli granulari sono meno importanti.
- **`MEDIUM` / `HIGH`:** aumenta la risoluzione quando l'attività richiede la comprensione di dettagli complessi all'interno dei contenuti multimediali. Questo è spesso necessario per l'analisi visiva complessa, la lettura di grafici o la comprensione di documenti densi.
- **`ULTRA HIGH`** : disponibile solo per l'impostazione per parte. Consigliato per casi d'uso specifici come l'utilizzo del computer o quando i test mostrano un miglioramento netto rispetto a `HIGH`.
- **Controllo per parte (Gemini 3):** ottimizza l'utilizzo dei token. Ad esempio, in un prompt con più immagini, utilizza `HIGH` per un diagramma complesso e `LOW` o `MEDIUM` per immagini contestuali più semplici.

**Impostazioni consigliate**

Di seguito sono elencate le impostazioni di risoluzione dei contenuti multimediali consigliate per ogni tipo di contenuti multimediali supportato.

|  |  |  |  |
| --- | --- | --- | --- |
| **Tipo di contenuti multimediali** | **Impostazione consigliata** | **Token massimi** | **Indicazioni sull'utilizzo** |
| **Google Immagini** | `MEDIA_RESOLUTION_HIGH` | 1120 | Consigliato per la maggior parte delle attività di analisi delle immagini per garantire la massima qualità. |
| **PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | Ottimale per la comprensione dei documenti; la qualità in genere satura a `medium`. L'aumento a `high` raramente migliora i risultati dell'OCR per i documenti standard. |
| **Video** (generale) | `MEDIA_RESOLUTION_LOW` (o `MEDIA_RESOLUTION_MEDIUM`) | 70 (per frame) | **Nota:** per i video, le impostazioni `low` e `medium` vengono trattate in modo identico (70 token) per ottimizzare l'utilizzo del contesto. Questo è sufficiente per la maggior parte delle attività di riconoscimento e descrizione delle azioni. |
| **Video** (con molti testi) | `MEDIA_RESOLUTION_HIGH` | 280 (per frame) | Obbligatorio solo quando il caso d'uso prevede la lettura di testi densi (OCR) o piccoli dettagli all'interno dei frame video. |

Esegui sempre test e valuta l'impatto delle diverse impostazioni di risoluzione sulla tua applicazione specifica per trovare il miglior compromesso tra qualità, latenza e costi.

## Riepilogo della compatibilità delle versioni

- L'enumerazione `MediaResolution` è disponibile per tutti i modelli che supportano l'input multimediale.
- I conteggi dei token associati a ogni livello di enumerazione **differiscono** tra i modelli Gemini 3 e le versioni precedenti di Gemini.
- L'impostazione di `media_resolution` su singoli oggetti `Part` è **esclusiva dei modelli Gemini 3**.

## Passaggi successivi

- Scopri di più sulle funzionalità multimodali dell'API Gemini nelle
  [guide alla comprensione delle immagini](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=it), alla [comprensione dei video](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=it) e alla
  [comprensione dei documenti](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
