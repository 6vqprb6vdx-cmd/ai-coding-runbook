---
source_url: https://ai.google.dev/gemini-api/docs/interactions/api-key?hl=it
fetched_at: 2026-05-18T13:05:40.667016+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Utilizzo delle chiavi API Gemini

Per utilizzare l'API Gemini, devi avere una chiave API. Questa pagina descrive come creare e
gestire le chiavi in Google AI Studio, nonché come configurare l'ambiente
per utilizzarle nel codice.

[Creare o visualizzare una chiave API Gemini](https://aistudio.google.com/app/apikey?hl=it)

## Chiavi API

Puoi creare e gestire tutte le tue chiavi API Gemini dalla pagina
[Chiavi API di **Google AI Studio**](https://aistudio.google.com/app/apikey?hl=it).

Una volta ottenuta una chiave API, hai le seguenti opzioni per connetterti all'API Gemini:

- [Impostare la chiave API come variabile di ambiente](#set-api-env-var)
- [Fornire la chiave API in modo esplicito](#provide-api-key-explicitly)

Per il test iniziale, puoi codificare una chiave API, ma questa operazione deve essere
temporanea perché non è sicura. Puoi trovare esempi di codifica hardcoded della chiave API nella sezione [Fornire la chiave API in modo esplicito](#provide-api-key-explicitly).

## Progetti Google Cloud

I [progetti Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=it)
sono fondamentali per utilizzare i servizi Google Cloud (come l'API Gemini),
gestire la fatturazione e controllare collaboratori e autorizzazioni. Google AI
Studio fornisce un'interfaccia leggera per i tuoi progetti Google Cloud.

Se non hai ancora creato progetti, devi crearne uno nuovo o importarne uno da Google Cloud in Google AI Studio. La pagina **Progetti** di Google AI
Studio mostrerà tutte le chiavi che dispongono dell'autorizzazione sufficiente per utilizzare l'API
Gemini. Per istruzioni, consulta la sezione [Importare progetti](#import-projects).

### Progetto predefinito

Per i nuovi utenti, dopo aver accettato i Termini di servizio, Google AI Studio crea un progetto Google Cloud e una chiave API predefiniti per facilitarne l'utilizzo. Puoi rinominare questo
progetto in Google AI Studio andando alla visualizzazione **Progetti** nella
**Dashboard**, facendo clic sul pulsante delle impostazioni con tre puntini accanto a un progetto e
scegliendo **Rinomina progetto**. Per gli utenti esistenti o per quelli che hanno già account Google Cloud non verrà creato un progetto predefinito.

## Importare progetti

Ogni chiave API Gemini è associata a un progetto cloud Google. Per impostazione predefinita,
Google AI Studio non mostra tutti i tuoi progetti cloud. Devi importare i
progetti che vuoi cercando il nome o l'ID progetto nella
finestra di dialogo **Importa progetti**. Per visualizzare un elenco completo dei progetti a cui hai accesso, visita Cloud Console.

Se non hai ancora importato progetti cloud, segui questi passaggi per importare un progetto Google Cloud e creare una chiave:

1. Vai a [Google AI Studio](https://aistudio.google.com?hl=it).
2. Apri la **dashboard** dal riquadro laterale a sinistra.
3. Seleziona **Progetti**.
4. Seleziona il pulsante **Importa progetti** nella pagina **Progetti**.
5. Cerca e seleziona il progetto Google Cloud che vuoi importare e fai clic sul pulsante
   **Importa**.

Una volta importato un progetto, vai alla pagina **Chiavi API** dal menu **Dashboard** e crea una chiave API nel progetto appena importato.

## Limitazioni

Di seguito sono riportate le limitazioni della gestione delle chiavi API e dei progetti Google Cloud in
Google AI Studio.

- Puoi creare un massimo di 10 progetti alla volta dalla pagina **Progetti** di Google AI Studio.
- Puoi assegnare un nome e rinominare progetti e chiavi.
- Le pagine **Chiavi API** e **Progetti** mostrano un massimo di 100 chiavi e
  50 progetti.
- Vengono visualizzate solo le chiavi API senza limitazioni o limitate all'API Generative
  Language.

Per un accesso di gestione aggiuntivo ai tuoi progetti, inclusa la modifica e la limitazione delle chiavi API, visita la
[pagina delle credenziali di console Google Cloud](https://console.cloud.google.com/apis/credentials?hl=it).
Nella console Cloud, puoi selezionare il tuo progetto, fare clic su una chiave API esistente e poi limitarla all'**API Generative Language**.

## Impostazione della chiave API come variabile di ambiente

Se imposti la variabile di ambiente `GEMINI_API_KEY` o `GOOGLE_API_KEY`, la chiave API verrà rilevata automaticamente dal client quando utilizzi una delle [librerie API Gemini](https://ai.google.dev/gemini-api/docs/libraries?hl=it). Ti consigliamo di impostare solo una di queste variabili, ma se vengono impostate entrambe, `GOOGLE_API_KEY` ha la precedenza.

Se utilizzi l'API REST o JavaScript sul browser, devi fornire la chiave API in modo esplicito.

Ecco come puoi impostare la chiave API localmente come variabile di ambiente
`GEMINI_API_KEY` con diversi sistemi operativi.

### Linux/macOS - Bash

Bash è una configurazione comune del terminale Linux e macOS. Puoi verificare se
hai un file di configurazione eseguendo il seguente comando:

```
~/.bashrc
```

Se la risposta è "No such file or directory", devi creare questo
file e aprirlo eseguendo i seguenti comandi o utilizzare `zsh`:

```
touch ~/.bashrc
open ~/.bashrc
```

Successivamente, devi impostare la chiave API aggiungendo il seguente comando di esportazione:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Dopo aver salvato il file, applica le modifiche eseguendo:

```
source ~/.bashrc
```

### macOS - Zsh

Zsh è una configurazione comune del terminale Linux e macOS. Puoi verificare se
hai un file di configurazione eseguendo il seguente comando:

```
~/.zshrc
```

Se la risposta è "No such file or directory", devi creare questo
file e aprirlo eseguendo i seguenti comandi o utilizzare `bash`:

```
touch ~/.zshrc
open ~/.zshrc
```

Successivamente, devi impostare la chiave API aggiungendo il seguente comando di esportazione:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Dopo aver salvato il file, applica le modifiche eseguendo:

```
source ~/.zshrc
```

### Windows

1. Cerca "Variabili di ambiente" nella barra di ricerca.
2. Scegli di modificare le **impostazioni di sistema**. Potresti dover confermare di voler
   procedere.
3. Nella finestra di dialogo delle impostazioni di sistema, fai clic sul pulsante **Variabili
   di ambiente**.
4. In **Variabili utente** (per l'utente corrente) o **Variabili
   di sistema** (si applica a tutti gli utenti che utilizzano la macchina), fai clic su **Nuova…**
5. Specifica il nome della variabile come `GEMINI_API_KEY`. Specifica la chiave API Gemini
   come valore della variabile.
6. Fai clic su **Ok** per applicare le modifiche.
7. Apri una nuova sessione del terminale (cmd o Powershell) per ottenere la nuova variabile.

## Fornire la chiave API in modo esplicito

In alcuni casi, potresti voler fornire esplicitamente una chiave API. Ad esempio:

- Stai effettuando una semplice chiamata API e preferisci codificare la chiave API.
- Vuoi un controllo esplicito senza dover fare affidamento sul rilevamento automatico delle
  variabili di ambiente da parte delle librerie dell'API Gemini
- Stai utilizzando un ambiente in cui le variabili di ambiente non sono supportate
  (ad es.web) o stai effettuando chiamate REST.

Di seguito sono riportati esempi di come fornire una chiave API in modo esplicito utilizzando l'API Interactions:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3-flash-preview", 
    input="Explain how AI works in a few words"
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -X POST \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain how AI works in a few words"
  }'
```

## Proteggere la chiave API

Tratta la chiave API Gemini come una password. Se viene compromesso, altri possono utilizzare la quota del tuo progetto, sostenere addebiti (se la fatturazione è abilitata) e accedere ai tuoi dati privati, come i file.

### Regole di sicurezza critiche

- **Mantieni riservate le chiavi**: le chiavi API per Gemini potrebbero accedere a dati sensibili da cui dipende la tua applicazione.

  - **Non eseguire mai il commit delle chiavi API nel controllo del codice sorgente.** Non archiviare la chiave API in sistemi di controllo della versione come Git.
  - **Non esporre mai le chiavi API lato client.** Non utilizzare la chiave API direttamente
    nelle app web o mobile in produzione. Le chiavi nel codice lato client
    (incluse le nostre librerie JavaScript/TypeScript e le chiamate REST) possono essere
    estratte.
- **Limita l'accesso**: limita l'utilizzo della chiave API a indirizzi IP, referrer HTTP o app per Android/iOS specifici, ove possibile.
- **Limita l'utilizzo**: abilita solo le API necessarie per ogni chiave.
- **Esegui controlli regolari**: controlla regolarmente le chiavi API e ruotale periodicamente.

### Best practice

- **Utilizza chiamate lato server con chiavi API** Il modo più sicuro per utilizzare la chiave API è chiamare l'API Gemini da un'applicazione lato server in cui la chiave può essere mantenuta riservata.
- **Utilizza token effimeri per l'accesso lato client (solo API Live):** per l'accesso diretto lato client all'API Live, puoi utilizzare token effimeri. Presentano
  rischi per la sicurezza inferiori e possono essere adatti all'uso in produzione. Per saperne di più, consulta la guida sui
  [token effimeri](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=it).
- **Valuta la possibilità di aggiungere limitazioni alla chiave**:puoi limitare le autorizzazioni di una chiave
  aggiungendo [limitazioni relative alle chiavi API](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=it#add-api-restrictions).
  Ciò riduce al minimo i potenziali danni in caso di perdita della chiave.

Per alcune best practice generali, puoi anche consultare questo
[articolo del Centro assistenza](https://support.google.com/googleapi/answer/6310037?hl=it).

## Risoluzione dei problemi relativi alla creazione della chiave API

In Google AI Studio, il pulsante **Crea chiave API** potrebbe non essere disponibile e potrebbe essere visualizzato il messaggio: "*Non hai l'autorizzazione per creare una chiave in questo progetto*".

Ciò si verifica quando non disponi delle autorizzazioni necessarie all'interno del progetto per generare una nuova chiave:

- **`resourcemanager.projects.get`**: consente ad AI Studio di verificare l'esistenza del progetto.
- **`apikeys.keys.create`**: consente la generazione della chiave API.
- **`serviceusage.services.enable`**: necessario per garantire che l'API Gemini sia
  attiva nel progetto.

Per correggere le autorizzazioni, chiedi all'amministratore del progetto o all'amministratore della tua organizzazione, se il progetto appartiene a un'[organizzazione](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=it), di concederti un ruolo con le autorizzazioni elencate sopra (ad esempio Editor progetto o un ruolo personalizzato).

Se non disponi dell'accesso amministrativo a un progetto, puoi creare
un nuovo progetto non associato a un'organizzazione per generare le chiavi.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-12 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-12 UTC."],[],[]]
