---
source_url: https://ai.google.dev/gemini-api/docs/agent-credentials?hl=it
fetched_at: 2026-09-21T05:48:54.027216+00:00
title: "Credenziali negli agenti gestiti \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Credenziali negli agenti gestiti

Le credenziali sono secret gestiti dal server che consentono agli agenti di raggiungere servizi di terze parti
senza che il secret entri mai nell'ambiente dell'agente. Archivi una credenziale una sola volta, fai riferimento a essa tramite ID e il proxy di uscita la risolve e la inserisce al momento della richiesta.

I valori dei secret sono di sola scrittura. Una volta memorizzati, non vengono mai restituiti da alcun
endpoint, quindi un agente compromesso non può leggere i token che sta utilizzando.

Il luogo principale in cui utilizzi una credenziale è la lista consentita di rete su
[`environment.network`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it). Memorizza prima il secret:

### Python

```
from google import genai

client = genai.Client()

credential = client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)

print(f"Credential ID: {credential.id}, Status: {credential.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const credential = await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
});

console.log(`Credential ID: ${credential.id}, Status: ${credential.status}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "github-production",
    "type": "bearer_token",
    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}'
```

Quindi, collegalo al dominio che autentica:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Triage the open issues in my-org/my-repo.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {"domain": "api.github.com", "credential": "github-production"},
                {"domain": "*"},
            ]
        },
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Triage the open issues in my-org/my-repo.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                { domain: "api.github.com", credential: "github-production" },
                { domain: "*" },
            ],
        },
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Triage the open issues in my-org/my-repo.",
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                { "domain": "api.github.com", "credential": "github-production" },
                { "domain": "*" }
            ]
        }
    }
}'
```

L'agente ora effettua richieste autenticate a `api.github.com` e il token
non esiste mai all'interno della sandbox.

## Tipi di credenziali

Ogni credenziale ha un `type` che determina quali campi accetta e come
il proxy la applica.

| Tipo | Caso d'uso | Comportamento |
| --- | --- | --- |
| `bearer_token` | Token di accesso personali, token bot, chiavi API statiche | Il proxy inserisce il token come intestazione della richiesta. Nessuna logica di aggiornamento. |
| `oauth2` | App OAuth e flussi con delega utente | Il proxy scambia il token di aggiornamento con i token di accesso e li aggiorna alla scadenza. |
| `environment_variable` | SDK client che leggono i secret dall'ambiente di processo | L'ambiente dell'agente riceve un segnaposto. Il proxy sostituisce il secret reale nelle richieste in uscita. |

## Utilizzare le credenziali nella lista consentita di rete

Aggiungi `credential` a una regola della lista consentita e il proxy autentica ogni
richiesta in uscita a quel dominio. Questo è il modo consigliato per concedere a un agente l'accesso a un'API privata, a un repository privato o a un bucket privato.

Puoi combinare regole autenticate e non autenticate nella stessa lista consentita:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Sync the open Jira issues into the tracking sheet in my repo.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app",
            }
        ],
        "network": {
            "allowlist": [
                {"domain": "github.com", "credential": "github-production"},
                {"domain": "api.atlassian.com", "credential": "jira-oauth"},
                {"domain": "*.googleapis.com"},
            ]
        },
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Sync the open Jira issues into the tracking sheet in my repo.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/your-org/backend",
                target: "/backend-app",
            },
        ],
        network: {
            allowlist: [
                { domain: "github.com", credential: "github-production" },
                { domain: "api.atlassian.com", credential: "jira-oauth" },
                { domain: "*.googleapis.com" },
            ],
        },
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Sync the open Jira issues into the tracking sheet in my repo.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app"
            }
        ],
        "network": {
            "allowlist": [
                { "domain": "github.com", "credential": "github-production" },
                { "domain": "api.atlassian.com", "credential": "jira-oauth" },
                { "domain": "*.googleapis.com" }
            ]
        }
    }
}'
```

Poiché il proxy risolve la credenziale per richiesta, una credenziale `oauth2`
aggiorna il token di accesso in modo trasparente. Un'interazione a lunga esecuzione non
si interrompe alla scadenza del token di accesso.

### Combinazione di `credential` e `transform`

Le regole della lista consentita accettano anche un oggetto
[`transform`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it#private-sources) incorporato che
imposta le intestazioni direttamente nella regola. Entrambi i meccanismi vengono applicati dal proxy
di uscita sul cavo, quindi in entrambi i casi il valore dell'intestazione non esiste mai all'interno
della sandbox. Entrambi i campi possono essere visualizzati nella stessa regola.

| Configurazione della regola | Comportamento |
| --- | --- |
| Solo `credential` | Il proxy risolve le credenziali e inserisce la relativa intestazione in ogni richiesta al dominio. |
| Solo `transform` | Inserimento di intestazione statica. Le intestazioni che scrivi vengono inviate così come sono. |
| Entrambi | La credenziale viene applicata per prima, poi `transform` viene unita sopra. Un'intestazione `transform` esplicita ha la precedenza se entrambe impostano la stessa chiave. |
| Nessuna delle due | Il dominio è consentito e non vengono inserite intestazioni. |

Una credenziale è utile quando vuoi archiviare un secret una sola volta e farvi riferimento da ogni ambiente, agente e trigger del tuo progetto e quando vuoi che l'aggiornamento e la rotazione dei token di accesso vengano gestiti per te. Un `transform` inline è adatto
quando il valore appartiene a una singola chiamata, ad esempio un token che generi
tu stesso subito prima di creare l'interazione.

La combinazione dei due è comune. La credenziale contiene l'intestazione di autenticazione
e `transform` aggiunge tutto ciò che il servizio upstream si aspetta nella stessa
richiesta:

```
{
    "domain": "api.atlassian.com",
    "credential": "jira-oauth",
    "transform": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

Per spostare un secret da un `transform` inline a una credenziale, archivialo
con `POST /credentials`, sostituisci l'intestazione di autenticazione in `transform` con
`"credential": "<id>"` e lascia invariato il resto dell'oggetto `transform`.

## Utilizzare le credenziali con i server MCP

I server MCP remoti accettano lo stesso campo `credential`. Impostalo su uno strumento `mcp_server` e il proxy inserisce l'intestazione di autenticazione in ogni richiesta al server:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Create a new issue in my-org/my-repo",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "github",
        "url": "https://api.githubcopilot.com/mcp",
        "credential": "github-production",
    }],
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Create a new issue in my-org/my-repo",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "github",
        url: "https://api.githubcopilot.com/mcp",
        credential: "github-production",
    }],
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Create a new issue in my-org/my-repo",
    "environment": "remote",
    "tools": [
        {
            "type": "mcp_server",
            "name": "github",
            "url": "https://api.githubcopilot.com/mcp",
            "credential": "github-production"
        }
    ]
}'
```

`credential` e `headers` seguono la stessa regola di precedenza della lista consentita.
La credenziale viene applicata per prima e `headers` viene unita in primo piano, quindi un'intestazione
esplicita ha la precedenza se entrambe impostano la stessa chiave:

```
{
    "type": "mcp_server",
    "name": "jira",
    "url": "https://jira.atlassian.com/mcp",
    "credential": "jira-oauth",
    "headers": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

Per spostare un secret da `headers` in linea a una credenziale, archivialo con
`POST /credentials` e sostituisci la voce di autenticazione in `headers` con `credential`.
Mantieni le altre intestazioni dove si trovano.

## Utilizzare le credenziali come variabili di ambiente

Alcune librerie client leggono i secret dall'ambiente di processo anziché
accettarli come intestazioni delle richieste. I client in modalità socket e long polling sono lo scenario comune.

Associa una credenziale `environment_variable` a un nome di variabile in
`environment.env`:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run the sync script and check notifications.",
    environment={
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "SLACK_BOT_TOKEN": {"credential": "slack-bot-token"},
        },
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run the sync script and check notifications.",
    environment: {
        type: "remote",
        env: {
            NODE_ENV: "production",
            SLACK_BOT_TOKEN: { credential: "slack-bot-token" },
        },
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Run the sync script and check notifications.",
    "environment": {
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "SLACK_BOT_TOKEN": { "credential": "slack-bot-token" }
        }
    }
}'
```

`env` accetta stringhe letterali e riferimenti alle credenziali affiancati. Una stringa letterale viene inserita nel container come una normale variabile di testo normale.

Un riferimento alle credenziali non lo è. La variabile riceve il segnaposto
`__GEMINI_CRED_<credential-id>__` e il proxy sostituisce il segreto reale solo
per le richieste in uscita dirette a un dominio in `trusted_domains` delle credenziali. Una
richiesta a qualsiasi altro dominio viene rifiutata, quindi il secret non lascia mai il
perimetro e il segnaposto non viene inviato al suo posto.

Imposta `trusted_domains` su ogni credenziale `environment_variable`. È il
controllo che definisce l'ambito in cui può essere utilizzato il secret.

## Crea una qualifica

Ogni richiesta di creazione richiede un `type`, oltre ai campi richiesti da quel tipo.

Quando chiami direttamente REST, tutti i nomi dei campi utilizzano snake\_case. L'invio di un campo
camelCase restituisce `400`.

### Token di connessione

Una credenziale con token di autenticazione richiede solo `token`:

### Python

```
credential = client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)
```

### JavaScript

```
const credential = await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "github-production",
    "type": "bearer_token",
    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}'
```

La risposta restituisce solo i metadati, mai il token:

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

Per impostazione predefinita, il proxy invia `Authorization: Bearer <token>`. Esegui l'override di
`header_name` e `prefix` per scegliere come target un servizio che si aspetta qualcos'altro:

### Python

```
credential = client.credentials.create(
    id="my-api-key",
    type="bearer_token",
    token="key_xxxxxxxxxxxx",
    header_name="x-goog-api-key",
    prefix="",
)
```

### JavaScript

```
const credential = await client.credentials.create({
    id: "my-api-key",
    type: "bearer_token",
    token: "key_xxxxxxxxxxxx",
    header_name: "x-goog-api-key",
    prefix: "",
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "my-api-key",
    "type": "bearer_token",
    "token": "key_xxxxxxxxxxxx",
    "header_name": "x-goog-api-key",
    "prefix": ""
}'
```

Questa configurazione produce l'intestazione `x-goog-api-key: key_xxxxxxxxxxxx`.

La seguente tabella mostra come si combinano `header_name` e `prefix`:

| Configurazione | Intestazione inserita |
| --- | --- |
| `{"token": "ghp_xxx"}` | `Authorization: Bearer ghp_xxx` |
| `{"token": "sk_live_xxx"}` | `Authorization: Bearer sk_live_xxx` |
| `{"token": "key_xxx", "header_name": "x-goog-api-key", "prefix": ""}` | `x-goog-api-key: key_xxx` |
| `{"token": "mytoken", "header_name": "X-API-Token", "prefix": ""}` | `X-API-Token: mytoken` |

### OAuth2

Una credenziale OAuth2 richiede `client_id`, `client_secret`, `refresh_token` e `token_url`. Il campo `scopes` è facoltativo:

### Python

```
credential = client.credentials.create(
    id="jira-oauth",
    type="oauth2",
    client_id="my-client-id",
    client_secret="my-client-secret",
    token_url="https://auth.atlassian.com/oauth/token",
    refresh_token="rt_xxxxxxxxxxxxxxxxxxxx",
    scopes=["read:jira-work", "write:jira-work"],
)
```

### JavaScript

```
const credential = await client.credentials.create({
    id: "jira-oauth",
    type: "oauth2",
    client_id: "my-client-id",
    client_secret: "my-client-secret",
    token_url: "https://auth.atlassian.com/oauth/token",
    refresh_token: "rt_xxxxxxxxxxxxxxxxxxxx",
    scopes: ["read:jira-work", "write:jira-work"],
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "jira-oauth",
    "type": "oauth2",
    "client_id": "my-client-id",
    "client_secret": "my-client-secret",
    "token_url": "https://auth.atlassian.com/oauth/token",
    "refresh_token": "rt_xxxxxxxxxxxxxxxxxxxx",
    "scopes": ["read:jira-work", "write:jira-work"]
}'
```

La creazione di una credenziale OAuth2 esegue uno scambio di token in tempo reale con
`token_url` per verificare che la configurazione funzioni. La credenziale viene memorizzata solo se il provider restituisce una risposta di token riuscita contenente un `access_token`. Sono accettate sia le risposte JSON che quelle form-urlencoded.

Ciò significa che al momento della creazione è necessario un token di aggiornamento valido e non scaduto. Se il
fornitore rifiuta lo scambio, l'errore ti viene restituito:

```
{
  "error": {
    "message": "OAuth token validation failed with HTTP 403: {\"error\":\"unauthorized_client\",\"error_description\":\"refresh_token is invalid\"}",
    "code": "invalid_request"
  }
}
```

Una volta memorizzato, il proxy aggiorna i token di accesso alla scadenza. Se il fornitore
ruota i token di aggiornamento e ne restituisce uno nuovo durante un aggiornamento, il nuovo token
sostituisce automaticamente quello memorizzato.

### Variabile di ambiente

Una qualifica `environment_variable` richiede `value` e `injection_location`:

### Python

```
credential = client.credentials.create(
    id="slack-bot-token",
    type="environment_variable",
    value="xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    trusted_domains=["*.slack.com", "slack.com"],
    injection_location="header",
)
```

### JavaScript

```
const credential = await client.credentials.create({
    id: "slack-bot-token",
    type: "environment_variable",
    value: "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    trusted_domains: ["*.slack.com", "slack.com"],
    injection_location: "header",
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "slack-bot-token",
    "type": "environment_variable",
    "value": "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    "trusted_domains": ["*.slack.com", "slack.com"],
    "injection_location": "header"
}'
```

Il campo `injection_location` indica al proxy in quale punto della richiesta in uscita sostituire il secret. Accetta `header`, `query` o `body`, come
singola stringa o come array quando un servizio ne richiede più di una:

```
"injection_location": ["header", "query"]
```

La sostituzione avviene solo nelle località che elenchi. Una richiesta che contiene il
segnaposto in un'altra posizione viene rifiutata anziché inviata.

Per associare la credenziale a un nome di variabile, consulta [Utilizzare le credenziali come variabili di ambiente](#environment-variables).

### ID generati

Il campo `id` è facoltativo. Omettilo e il servizio genera un UUID:

```
{
  "id": "9e545973-4330-49bb-9a44-930cea9fbe3c",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

Fornisci il tuo ID quando vuoi un riferimento stabile e leggibile da utilizzare in tutte le
interazioni. Poiché l'ID viene visualizzato nel percorso della risorsa, preferisci caratteri
alfanumerici minuscoli con trattini o trattini bassi.

## Elenca le credenziali

Elenca le credenziali appartenenti al tuo progetto. Utilizza i parametri di impaginazione per
controllare le dimensioni del batch di risposta.

### Python

```
response = client.credentials.list(page_size=10)
for credential in response.credentials:
    print(f"Credential ID: {credential.id}, Type: {credential.type}")
```

### JavaScript

```
const response = await client.credentials.list({ page_size: 10 });
for (const credential of response.credentials) {
    console.log(`Credential ID: ${credential.id}, Type: ${credential.type}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/credentials?page_size=10" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

La risposta contiene solo metadati:

```
{
  "credentials": [
    {
      "id": "github-production",
      "type": "bearer_token",
      "status": "active",
      "create_time": "2026-07-15T10:00:00.000000000Z",
      "update_time": "2026-07-15T10:00:00.000000000Z"
    },
    {
      "id": "jira-oauth",
      "type": "oauth2",
      "status": "active",
      "create_time": "2026-07-15T10:05:00.000000000Z",
      "update_time": "2026-07-15T10:05:00.000000000Z"
    }
  ],
  "next_page_token": "Cj...5aE="
}
```

Passa `next_page_token` come `page_token` per recuperare la pagina successiva. Il campo viene omesso quando non sono presenti altri risultati.

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| `page_size` | integer | Numero massimo di credenziali per pagina. |
| `page_token` | stringa | Token dal campo `next_page_token` di una risposta precedente. |

## Ottenere una credenziale

Recupera i metadati per una credenziale specifica in base al relativo ID.

### Python

```
credential = client.credentials.get(id="github-production")
print(f"Credential ID: {credential.id}, Status: {credential.status}")
```

### JavaScript

```
const credential = await client.credentials.get("github-production");
console.log(`Credential ID: ${credential.id}, Status: ${credential.status}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

La risposta è simile alla seguente:

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

La richiesta di una credenziale inesistente restituisce `404`:

```
{
  "error": {
    "message": "Result not found.; GetCredential call failed",
    "code": "not_found"
  }
}
```

## Ruotare una credenziale

Sostituisci un secret senza modificare alcuna regola della lista consentita, definizione dello strumento o
variabile di ambiente che lo fa riferimento. La rotazione ha effetto alla successiva
risoluzione del proxy.

La richiesta deve includere `type`, oltre ai campi che vuoi modificare. I campi che
ometti mantengono i valori correnti.

Ruotare un token di connessione:

### Python

```
credential = client.credentials.update(
    id="github-production",
    type="bearer_token",
    token="ghp_new_xxxxxxxxxxxxxxxxxxxx",
)
```

### JavaScript

```
const credential = await client.credentials.update("github-production", {
    type: "bearer_token",
    token: "ghp_new_xxxxxxxxxxxxxxxxxxxx",
});
```

### REST

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "type": "bearer_token",
    "token": "ghp_new_xxxxxxxxxxxxxxxxxxxx"
}'
```

Ruota un token di aggiornamento OAuth2:

### Python

```
credential = client.credentials.update(
    id="jira-oauth",
    type="oauth2",
    refresh_token="rt_new_xxxxxxxxxxxxxxxxxxxx",
)
```

### JavaScript

```
const credential = await client.credentials.update("jira-oauth", {
    type: "oauth2",
    refresh_token: "rt_new_xxxxxxxxxxxxxxxxxxxx",
});
```

### REST

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/credentials/jira-oauth" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "type": "oauth2",
    "refresh_token": "rt_new_xxxxxxxxxxxxxxxxxxxx"
}'
```

La risposta riflette il nuovo `update_time`:

```
{
  "id": "jira-oauth",
  "type": "oauth2",
  "status": "active",
  "create_time": "2026-07-15T10:05:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

Il `type` di una credenziale viene fissato al momento della creazione. Per modificarla, elimina la credenziale
e creane una nuova.

## Eliminare una credenziale

Elimina una credenziale e il relativo secret archiviato quando non sono più necessari.

### Python

```
client.credentials.delete(id="github-production")
```

### JavaScript

```
await client.credentials.delete("github-production");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

Un'eliminazione corretta restituisce un oggetto vuoto:

```
{}
```

Qualsiasi regola di lista consentita, strumento o variabile di ambiente che fa ancora riferimento all'ID non verrà risolto, quindi aggiornali prima.

## Riferimento al campo

Campi comuni a ogni credenziale:

| Campo | Tipo | Obbligatorio | Descrizione |
| --- | --- | --- | --- |
| `id` | stringa | No | Identificatore univoco. Generato come UUID se omesso. |
| `type` | stringa | Sì | Uno dei valori `bearer_token`, `oauth2`, `environment_variable`. |
| `status` | stringa | Sola lettura | Stato attuale della credenziale. |
| `create_time` | stringa | Sola lettura | Timestamp di creazione RFC 3339. |
| `update_time` | stringa | Sola lettura | Timestamp RFC 3339 dell'ultimo aggiornamento. |

Campi per `bearer_token`:

| Campo | Tipo | Obbligatorio | Descrizione |
| --- | --- | --- | --- |
| `token` | stringa | Sì | Solo scrittura. Il valore del token. |
| `header_name` | stringa | No | Intestazione da inserire. Il valore predefinito è `Authorization`. |
| `prefix` | stringa | No | Prefisso valore. Il valore predefinito è `Bearer`. Imposta questo valore su `""` per non specificare un limite. |

Campi per `oauth2`:

| Campo | Tipo | Obbligatorio | Descrizione |
| --- | --- | --- | --- |
| `client_id` | stringa | Sì | ID client OAuth2. |
| `client_secret` | stringa | Sì | Solo scrittura. Client secret OAuth2. |
| `refresh_token` | stringa | Sì | Solo scrittura. Token di aggiornamento utilizzato per ottenere i token di accesso. |
| `token_url` | stringa | Sì | Endpoint token del fornitore. |
| `scopes` | matrice | No | Ambiti OAuth da richiedere. |

Campi per `environment_variable`:

| Campo | Tipo | Obbligatorio | Descrizione |
| --- | --- | --- | --- |
| `value` | stringa | Sì | Solo scrittura. Il valore del secret. |
| `injection_location` | stringa o array | Sì | Dove sostituire il secret. Uno o più dei seguenti valori: `header`, `query`, `body`. |
| `trusted_domains` | matrice | No | Pattern di dominio autorizzati per la sostituzione. |

## Errori

Gli errori restituiscono un oggetto JSON con un `message` e un `code`:

```
{
  "error": {
    "message": "Credential 'github-production' already exists.; CreateCredential call failed",
    "code": "aborted"
  }
}
```

| Stato HTTP | `code` | Causa |
| --- | --- | --- |
| 400 | `invalid_request` | Campo obbligatorio mancante, campo sconosciuto, `type` non supportato o convalida OAuth2 non riuscita. |
| 404 | `not_found` | Nessuna credenziale con questo ID. |
| 409 | `aborted` | Esiste già una credenziale con questo ID. |

I campi sconosciuti vengono rifiutati anziché ignorati e l'errore indica il nome del campo:

```
{
  "error": {
    "message": "Unknown parameter 'headerName'. Did you mean 'header_name'?",
    "code": "invalid_request"
  }
}
```

## Passaggi successivi

- [Ambienti](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it): scopri come gli agenti eseguono il codice e mantengono i file.
- [Panoramica degli agenti](https://ai.google.dev/gemini-api/docs/agents?hl=it): scopri i concetti fondamentali degli agenti gestiti.
- [Creazione di agenti personalizzati](https://ai.google.dev/gemini-api/docs/custom-agents?hl=it): definisci i tuoi agenti utilizzando `AGENTS.md` e `SKILL.md`.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-18 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-18 UTC."],[],[]]
