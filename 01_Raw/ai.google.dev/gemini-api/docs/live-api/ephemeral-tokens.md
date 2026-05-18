---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=it
fetched_at: 2026-05-18T13:03:10.247398+00:00
title: "Ephemeral tokens \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Ephemeral tokens

I token effimeri sono token di autenticazione di breve durata per accedere all'API Gemini tramite [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Sono progettate per migliorare la sicurezza quando
ti connetti direttamente dal dispositivo di un utente all'API (un'implementazione
[da client a server](https://ai.google.dev/gemini-api/docs/live?hl=it#implementation-approach)). Come le chiavi API standard, i token effimeri possono essere estratti da
applicazioni lato client come browser web o app mobile. Tuttavia, poiché i token effimeri scadono rapidamente e possono essere limitati, riducono significativamente i rischi per la sicurezza in un ambiente di produzione. Devi utilizzarle quando
accedi all'API Live direttamente dalle applicazioni lato client per migliorare la sicurezza della chiave API.

## Come funzionano i token effimeri

Ecco come funzionano i token temporanei a livello generale:

1. Il client (ad es. l'app web) esegue l'autenticazione con il backend.
2. Il backend richiede un token effimero dal servizio di provisioning dell'API Gemini.
3. L'API Gemini rilascia un token di breve durata.
4. Il backend invia il token al client per le connessioni WebSocket all'API Live. Puoi farlo sostituendo la chiave API con un token effimero.
5. Il client utilizza quindi il token come se fosse una chiave API.

![Panoramica dei token temporanei](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=it)

In questo modo la sicurezza viene migliorata perché, anche se estratto, il token ha una durata breve,
a differenza di una chiave API di lunga durata di cui è stato eseguito il deployment lato client. Poiché il client invia i dati
direttamente a Gemini, ciò migliora anche la latenza ed evita che i backend debbano
fare da proxy per i dati in tempo reale.

## Creare un token temporaneo

Ecco un esempio semplificato di come ottenere un token effimero da Gemini.
Per impostazione predefinita, avrai 1 minuto per avviare nuove sessioni dell'API Live utilizzando il token
di questa richiesta (`newSessionExpireTime`) e 30 minuti per inviare messaggi tramite
questa connessione (`expireTime`).

### Python

```
import datetime

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
    'http_options': {'api_version': 'v1alpha'},
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

  const token: AuthToken = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
      httpOptions: {apiVersion: 'v1alpha'},
    },
  });
```

Per i vincoli, i valori predefiniti e altre specifiche dei campi `expireTime`, consulta il
[Riferimento API](https://ai.google.dev/api/live?hl=it#ephemeral-auth-tokens).
Entro il periodo di tempo `expireTime`, dovrai
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=it#session-resumption) per
riconnettere la chiamata ogni 10 minuti (questa operazione può essere eseguita con lo stesso token anche
se `uses: 1`).

È anche possibile bloccare un token temporaneo per un insieme di configurazioni. Questo
potrebbe essere utile per migliorare ulteriormente la sicurezza della tua applicazione e mantenere le istruzioni di sistema sul lato server.

### Python

```
client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'temperature':0.7,
            'response_modalities':['AUDIO']
        }
    },
    'http_options': {'api_version': 'v1alpha'},
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.1-flash-live-preview',
            config: {
                sessionResumption: {},
                temperature: 0.7,
                responseModalities: ['AUDIO']
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

Puoi anche bloccare un sottoinsieme di campi. Per saperne di più, consulta la [documentazione dell'SDK](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields).

## Connettersi all'API Live con un token effimero

Una volta ottenuto un token effimero, lo utilizzi come se fosse una chiave API (ma
ricorda che funziona solo con l'API live e solo con la versione `v1alpha`
dell'API).

L'utilizzo di token temporanei aggiunge valore solo quando vengono implementate applicazioni
che seguono l'approccio di [implementazione da client a server](https://ai.google.dev/gemini-api/docs/live?hl=it#implementation-approach).

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

Per altri esempi, consulta [Inizia a utilizzare l'API Live](https://ai.google.dev/gemini-api/docs/live?hl=it).

## Best practice

- Imposta una breve durata di scadenza utilizzando il parametro `expire_time`.
- I token scadono, pertanto è necessario riavviare il processo di provisioning.
- Verifica l'autenticazione sicura per il tuo backend. I token effimeri saranno
  sicuri quanto il tuo metodo di autenticazione backend.
- In genere, evita di utilizzare token temporanei per le connessioni backend-Gemini,
  in quanto questo percorso è in genere considerato sicuro.

## Limitazioni

Al momento, i token effimeri sono compatibili solo con l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=it).

## Passaggi successivi

- Per saperne di più, consulta il [riferimento](https://ai.google.dev/api/live?hl=it#ephemeral-auth-tokens)
  dell'API Live sui token effimeri.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-13 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-13 UTC."],[],[]]
