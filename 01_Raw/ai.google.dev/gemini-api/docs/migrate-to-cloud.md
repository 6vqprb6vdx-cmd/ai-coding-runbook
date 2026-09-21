---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=it
fetched_at: 2026-09-21T05:50:19.681745+00:00
title: "API Gemini Developer e piattaforma agentica Gemini Enterprise \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# API Gemini Developer e piattaforma agentica Gemini Enterprise

Quando sviluppi soluzioni di AI generativa con Gemini, Google offre due prodotti API:
l'[API Gemini Developer](https://ai.google.dev/gemini-api/docs?hl=it) e l'[API Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=it).

L'API Gemini Developer offre il percorso più rapido per creare, mettere in produzione e scalare le applicazioni basate su Gemini. La maggior parte degli sviluppatori dovrebbe utilizzare l'API Gemini Developer, a meno che non sia necessario utilizzare controlli aziendali specifici.

Gemini Enterprise Agent Platform offre un ecosistema completo di funzionalità e servizi pronti per l'uso aziendale per la creazione e il deployment di applicazioni di AI generativa basate su Google Cloud.

Di recente abbiamo semplificato la migrazione tra questi servizi. Sia l'API Gemini
Developer sia l'API Gemini Enterprise Agent Platform sono ora accessibili tramite l'SDK Google Gen AI unificato
.

## Confronto del codice

Questa pagina contiene confronti di codice affiancati tra le guide rapide dell'API Gemini Developer e di Gemini Enterprise Agent Platform per la generazione di testo.

### Python

Puoi accedere sia all'API Gemini Developer sia ai servizi di Gemini Enterprise Agent Platform tramite la libreria `google-genai`. Per istruzioni su come installare `google-genai`, consulta la pagina delle [librerie](https://ai.google.dev/gemini-api/docs/libraries?hl=it).

### API Gemini Developer

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### API Gemini Enterprise Agent Platform

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.6-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript e TypeScript

Puoi accedere sia all'API Gemini Developer sia ai servizi di Gemini Enterprise Agent Platform tramite la libreria `@google/genai`. Per istruzioni su come
installare `@google/genai`, consulta la pagina delle [librerie](https://ai.google.dev/gemini-api/docs/libraries?hl=it).

### API Gemini Developer

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### API Gemini Enterprise Agent Platform

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Vai

Puoi accedere sia all'API Gemini Developer sia ai servizi di Gemini Enterprise Agent Platform tramite la libreria `google.golang.org/genai`. Per istruzioni su come
installare `google.golang.org/genai`, consulta la pagina delle [librerie](https://ai.google.dev/gemini-api/docs/libraries?hl=it).

### API Gemini Developer

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.6-flash", genai.Text("Tell me about New York?"), nil)

}
```

### API Gemini Enterprise Agent Platform

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.6-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Altri casi d'uso e piattaforme

Per altre piattaforme e altri casi d'uso, consulta le guide specifiche per i casi d'uso nella documentazione dell'API [Gemini Developer](https://ai.google.dev/gemini-api/docs?hl=it)
e nella documentazione di [Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=it).

## Considerazioni sulla migrazione

Durante la migrazione:

- Dovrai utilizzare gli account di servizio Google Cloud per l'autenticazione. Per ulteriori informazioni, consulta la documentazione di [Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=it).
- Puoi utilizzare il progetto Google Cloud esistente
  (lo stesso che hai utilizzato per generare la chiave API) o puoi
  [creare un nuovo progetto Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=it).
- Le regioni supportate potrebbero variare tra l'API Gemini Developer e l'API Gemini Enterprise Agent Platform. Consulta l'elenco delle
  [regioni supportate per l'AI generativa su Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=it).
- Tutti i modelli creati in Google AI Studio devono essere sottoposti a un nuovo addestramento in Gemini Enterprise Agent Platform.

Se non hai più bisogno di utilizzare la chiave API Gemini per l'API Gemini Developer, segui le best practice di sicurezza ed eliminala.

Per eliminare una chiave API:

1. Apri la
   [pagina Credenziali API di Google Cloud](https://console.cloud.google.com/apis/credentials?hl=it).
2. Trova la chiave API che vuoi eliminare e fai clic sull'icona **Azioni**.
3. Seleziona **Elimina chiave API**.
4. Nella finestra modale **Elimina credenziale**, seleziona **Elimina**.

   La propagazione dell'eliminazione di una chiave API richiede alcuni minuti. Al termine della propagazione, tutto il traffico che utilizza la chiave API eliminata viene rifiutato.

## Passaggi successivi

- Per saperne di più sulle soluzioni di AI generativa su Gemini Enterprise Agent Platform, consulta la
  [panoramica sull'AI generativa su Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-12 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-12 UTC."],[],[]]
