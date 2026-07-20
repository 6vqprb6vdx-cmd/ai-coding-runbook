---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=it
fetched_at: 2026-07-20T04:34:50.812267+00:00
title: "Utilizzo delle chiavi API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Utilizzo delle chiavi API Gemini

Per utilizzare l'API Gemini, devi autenticare le richieste. Puoi eseguire l'autenticazione utilizzando una chiave API standard o di autorizzazione.

[Creare o visualizzare una chiave API Gemini](https://aistudio.google.com/apikey?hl=it)

## Tipi di chiavi API: standard e di autorizzazione

Le chiavi API forniscono l'accesso all'API Gemini, ma le loro caratteristiche di sicurezza sono diverse. Per migliorare la sicurezza, l'API Gemini sta passando dalle chiavi API standard alle chiavi di autorizzazione:

- **Chiavi API standard**: associano le richieste a un progetto Google Cloud per
  la fatturazione e la quota. Le chiavi standard non identificano un chiamante, il che limita la granularità delle autorizzazioni e del controllo dell'accesso che possono supportare.
- **Chiavi di autorizzazione**: sono associate direttamente a un service account Google Cloud. Quando utilizzi una chiave di autorizzazione, le tue richieste vengono elaborate con l'identità del service account associato, consentendo un controllo dell'accesso granulare. Per impostazione predefinita, le chiavi di autorizzazione sono limitate all'API Generative Language (API Gemini) e forniscono un'applicazione rapida delle chiavi trapelate che interrompe rapidamente l'utilizzo delle chiavi trapelate rilevate dai nostri sistemi.

Per garantire un utilizzo sicuro, l'API Gemini passerà dalle chiavi standard alle chiavi di autorizzazione:

- **Chiavi di autorizzazione predefinite**: tutte le nuove chiavi API create in Google AI Studio
  vengono create automaticamente come chiavi di autorizzazione.
- **Chiavi senza limitazioni rifiutate**: l'API Gemini rifiuta le richieste
  provenienti da **chiavi standard senza limitazioni**. Le chiavi API standard a cui sono state applicate limitazioni esplicite continuano a funzionare. Questa limitazione impedisce l'utilizzo non autorizzato di chiavi che potrebbero essere condivise pubblicamente o collegate ad altri servizi.
- **A settembre 2026**: l'API Gemini rifiuterà le richieste provenienti da **chiavi
  standard**. Devi [eseguire la migrazione alle chiavi di autorizzazione](#migrate-to-auth-key)
  prima di questa data per evitare interruzioni del servizio. Assicurati di eseguire la migrazione alle chiavi di autorizzazione prima di settembre 2026.

## Gestire le chiavi API in Google AI Studio

Puoi gestire i progetti e le chiavi direttamente in [Google AI Studio](https://aistudio.google.com/apikey?hl=it).

### Progetti Google Cloud

Ogni chiave API Gemini è associata a un [progetto Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=it).
I progetti Google Cloud gestiscono la fatturazione, i collaboratori e le autorizzazioni. Google AI Studio fornisce un'interfaccia leggera per accedere a questi progetti.

- **Progetto predefinito**: se sei un nuovo utente, Google AI Studio crea automaticamente
  un progetto Google Cloud e una chiave API predefiniti dopo che hai accettato i
  Termini di servizio. Puoi rinominare questo progetto andando alla visualizzazione **Progetti** nella dashboard.
- **Progetti esistenti**: se hai già un account Google Cloud, AI
  Studio non crea un progetto predefinito. Devi invece importare i progetti esistenti.

### Importare progetti

Per impostazione predefinita, Google AI Studio non mostra tutti i tuoi progetti Google Cloud. Devi importare i progetti che vuoi utilizzare:

1. Vai a [Google AI Studio](https://aistudio.google.com?hl=it).
2. Apri la **dashboard** dal riquadro a sinistra e seleziona **Progetti**.
3. Fai clic sul pulsante **Importa progetti**.
4. Cerca e seleziona il progetto Google Cloud che vuoi importare, poi fai clic su **Importa**.
5. Una volta importato, vai alla pagina **Chiavi API** nella dashboard per creare una chiave nel progetto.

### Risolvere i problemi relativi alle autorizzazioni di creazione delle chiavi

Se il pulsante **Crea chiave API** non è disponibile e viene visualizzato il messaggio:
*"Non hai l'autorizzazione per creare una chiave in questo progetto"*, non disponi delle
autorizzazioni IAM richieste.

Chiedi all'amministratore del progetto cloud o dell'organizzazione Google Cloud di concederti un ruolo contenente le seguenti autorizzazioni (ad esempio Editor progetto):

- `resourcemanager.projects.get`: consente ad AI Studio di verificare il progetto.
- `apikeys.keys.create`: consente la generazione delle chiavi.
- `serviceusage.services.enable`: garantisce che l'API Generative Language sia abilitata.
- `iam.serviceAccounts.create`: necessaria per creare il service account collegato.
- `iam.serviceAccountApiKeyBindings.create`: associa il service account alla chiave API.

Se non riesci a ottenere l'accesso amministrativo, puoi creare un nuovo progetto Google Cloud non associato a un'organizzazione per generare le chiavi.

## Configurazione dell'ambiente

Una volta ottenuta una chiave, configura l'ambiente per utilizzarla in modo sicuro nelle tue applicazioni.

### Opzione 1: utilizzare le variabili di ambiente (consigliata)

Imposta la variabile di ambiente `GEMINI_API_KEY` o `GOOGLE_API_KEY`. Le librerie client dell'API Gemini rilevano e utilizzano automaticamente queste variabili. Se vengono impostate entrambe, `GOOGLE_API_KEY` ha la precedenza.

Seleziona il tuo sistema operativo per impostare la variabile:

### Linux/macOS - Bash

Verifica se hai un file di configurazione bash:

```
~/.bashrc
```

In caso contrario, creane uno e aprilo:

```
touch ~/.bashrc && open ~/.bashrc
```

Aggiungi il comando di esportazione alla fine del file:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Salva il file, poi applica le modifiche:

```
source ~/.bashrc
```

### macOS - Zsh

Verifica se hai un file di configurazione zsh:

```
~/.zshrc
```

In caso contrario, creane uno e aprilo:

```
touch ~/.zshrc && open ~/.zshrc
```

Aggiungi il comando di esportazione:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Salva il file, poi applica le modifiche:

```
source ~/.zshrc
```

### Windows

1. Cerca "Variabili di ambiente" nella barra di ricerca di Windows.
2. Fai clic su **Variabili di ambiente** nella finestra di dialogo Proprietà del sistema.
3. In **Variabili utente** o **Variabili di sistema**, fai clic su **Nuova…**.
4. Imposta il nome della variabile su `GEMINI_API_KEY` e il valore sulla tua chiave API.
5. Fai clic su **OK** per salvare. Apri una nuova sessione del terminale per caricare la variabile.

### Opzione 2: fornire la chiave API in modo esplicito nel codice

Puoi passare la chiave API in modo esplicito durante l'inizializzazione del client. Esegui questa operazione solo se non puoi utilizzare le variabili di ambiente.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
}

main();
```

### Vai

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
    "google.golang.org/genai/interactions"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction, err := client.Interactions.NewModel(ctx, interactions.NewModelParams{
        Model: "gemini-3.5-flash",
        Input: interactions.Input{
            String: "Explain how AI works in a few words",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range interaction.Steps {
        if step.ModelOutput != nil {
            for _, content := range step.ModelOutput.Content {
                if content.Text != nil {
                    fmt.Println(content.Text.Text)
                }
            }
        }
    }
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.interactions.models.interactions.CreateModelInteractionParams;
import com.google.genai.interactions.models.interactions.Interaction;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    CreateModelInteractionParams params =
        CreateModelInteractionParams.builder()
            .input("Explain how AI works in a few words")
            .model("gemini-3.5-flash")
            .build();

    Interaction interaction = client.interactions.create(params);

    interaction.steps().forEach(step -> {
      if (step.isModelOutput()) {
        step.asModelOutput().content().ifPresent(contents -> {
          contents.forEach(content -> {
            content.text().ifPresent(text -> System.out.println(text.text()));
          });
        });
      }
    });
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Sicurezza e gestione dei secret

Tratta la chiave API Gemini come una password. Se viene compromessa, altri utenti possono consumare la quota del tuo progetto, generare addebiti di fatturazione imprevisti e accedere a risorse private.

### Regole di sicurezza critiche

- **Mantieni riservate le chiavi**: non eseguire mai il check-in delle chiavi API nei sistemi di controllo del codice sorgente
  come Git.
- **Non esporre mai le chiavi lato client in produzione**: non codificare le chiavi API
  direttamente nelle app web o mobile. Gli utenti possono estrarre le chiavi compilate nel codice lato client. Per proteggere le app lato client, esegui un server proxy di backend per effettuare le chiamate API effettive.

### Best practice per la gestione dei secret

- **Variabili di ambiente**: leggi le chiavi dalle variabili di ambiente anziché dai file di
  configurazione.
- **Secret Manager**: per la produzione, archivia le chiavi in un archivio di secret sicuro
  come [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=it).
- **Avvisi di fatturazione**: configura gli avvisi di fatturazione nella console Google Cloud per ricevere una notifica in caso di picchi di utilizzo o costi.

### Elenco di controllo per la risposta alle perdite

Se sospetti che la tua chiave API sia stata compromessa:

1. **Genera una nuova chiave**: crea una chiave di sostituzione in Google AI Studio o in
   Cloud Console.
2. **Aggiorna l'applicazione**: esegui il deployment del codice utilizzando la nuova chiave.
3. **Disabilita o elimina la chiave compromessa**: disabilita la chiave compromessa in
   Cloud Console dopo aver verificato la nuova chiave. Non eliminare la vecchia chiave finché la nuova non è completamente attiva per evitare tempi di inattività dell'applicazione.
4. **Controlla l'utilizzo**: controlla i log di fatturazione e l'utilizzo delle API in Google Cloud
   Console per identificare attività non autorizzate.

## Limitare e proteggere le chiavi

L'aggiunta di limitazioni alle chiavi API riduce al minimo i potenziali danni in caso di compromissione di una chiave.

### Applicare limitazioni all'origine delle richieste

Le limitazioni di origine limitano gli indirizzi IP, i siti web o le applicazioni che possono utilizzare la chiave.

1. Vai alla pagina [Credenziali di Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=it).
2. Seleziona il progetto e fai clic sul nome della chiave API che vuoi limitare.
3. In **Limitazioni delle applicazioni**, seleziona **Indirizzi IP** (o il
   tipo di limitazione appropriato per il tuo ambiente).
4. Specifica gli indirizzi IP o gli intervalli consentiti, poi fai clic su **Salva**.

### Proteggere le chiavi API standard senza limitazioni

Per continuare a utilizzare l'API Gemini, devi proteggere tutte le chiavi senza limitazioni.

#### Metodo A: limitare la chiave solo all'API Gemini (AI Studio)

Se utilizzi la chiave solo per l'API Gemini, proteggila direttamente in AI Studio:

1. Nella pagina **Chiavi API** di [Google AI Studio](https://aistudio.google.com/api-keys?hl=it), individua le chiavi contrassegnate con l'etichetta
   **Senza limitazioni**.
2. Passa il mouse sopra l'etichetta e fai clic su **Aggiungi limitazioni** nella finestra di dialogo.
3. Seleziona **Limita solo all'API Gemini**.
4. Fai clic su **Limita chiave** per confermare.

#### Metodo B: limitare la chiave per altri servizi (console Google Cloud)

Se la chiave è condivisa con altre API di Google (opzione sconsigliata), limitala in console Cloud. **Nota: le richieste dell'API Gemini che utilizzano questa chiave non andranno a buon fine dopo l'applicazione di queste limitazioni.**

1. Vai alla pagina [Credenziali della console Google Cloud](https://console.cloud.google.com/apis/credentials?hl=it).
2. Seleziona il progetto e la chiave API.
3. In **Limitazioni delle API**, utilizza il menu a discesa **Seleziona limitazioni delle API** per
   selezionare le API a cui vuoi che questa chiave acceda. Non selezionare l'**API Generative Language**.
4. Fai clic su **Salva**. Crea una chiave limitata separata in AI Studio per continuare a utilizzare l'API Gemini.

### Chiavi inattive bloccate

A partire dal 7 maggio 2026, l'API Gemini bloccherà le chiavi API senza limitazioni che sono inattive da un periodo di tempo prolungato. Queste chiavi mostrano un tag **Bloccata** in AI Studio. Per continuare, devi generare una nuova chiave o utilizzare una chiave limitata esistente.

## Eseguire la migrazione a una chiave di autorizzazione

Segui questi passaggi per creare una nuova chiave API di autorizzazione e aggiornare le tue applicazioni:

1. Vai alla pagina [Chiavi API di AI Studio](https://aistudio.google.com/api-keys?hl=it).
2. Controlla la colonna **Tipo di chiave** per identificare le chiavi elencate come **Standard**.
3. Fai clic su **Crea chiave API** per generare una nuova chiave. Tutte le nuove chiavi create in AI Studio vengono create automaticamente come chiavi di autorizzazione.
4. Copia la nuova chiave API di autorizzazione.
5. Aggiorna il codice dell'applicazione, le variabili di ambiente e le configurazioni di deployment per utilizzare la nuova chiave API di autorizzazione.
6. Testa l'applicazione per verificare che funzioni correttamente con la nuova chiave.
7. Una volta verificata, elimina o revoca la vecchia chiave di traffico per evitare un utilizzo improprio.

## Limitazioni

Google AI Studio impone le seguenti limitazioni di gestione di progetti e chiavi:

- Puoi creare un massimo di 10 progetti alla volta dalla pagina **Progetti** di Google AI Studio.
- Le pagine **Chiavi API** e **Progetti** mostrano un massimo di 100 chiavi e 50 progetti.
- Vengono visualizzate solo le chiavi API senza limitazioni o limitate specificamente all'API Generative Language (API Gemini).

Per la gestione avanzata dei progetti o per modificare le chiavi con altre limitazioni, utilizza
la pagina [Credenziali della console Google Cloud](https://console.cloud.google.com/apis/credentials?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-16 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-16 UTC."],[],[]]
