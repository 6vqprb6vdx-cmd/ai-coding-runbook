---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=it
fetched_at: 2026-10-19T05:48:20.352155+00:00
title: "Configurazione dell'agente di programmazione e risorse per sviluppatori \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Configurazione dell'agente di programmazione e risorse per sviluppatori

Gli agenti di programmazione AI si basano su dati di addestramento che terminano in una data prestabilita. Per questo motivo, gli agenti spesso suggeriscono modelli deprecati (`gemini-1.5`), SDK precedenti (`google-generativeai`) o pattern di codice obsoleti.

Il collegamento dell'agente alle risorse ufficiali per sviluppatori Gemini consente di scrivere
codice accurato utilizzando i modelli attuali, l'SDK `google-genai` e l'[API
Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it).

Puoi concedere al tuo agente di codifica l'accesso alla documentazione e alle regole di Gemini in quattro
modi:

## Riepilogo delle risorse dell'agente

| Risorsa | Cosa fornisce | Disponibilità |
| --- | --- | --- |
| **[Competenze di Gemini Agent](https://ai.google.dev/gemini-api/docs/coding-agents?hl=it#available-skills)** | Regole passo passo, pattern SDK e script helper per funzionalità specifiche (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`). | Preinstallato in [AI Studio Build](https://ai.studio/build); installalo con `skills.sh`, Context7 o Managed Agents. |
| **[Server MCP di Gemini Docs](https://ai.google.dev/gemini-api/docs/coding-agents?hl=it#mcp-setup)** | Ricerca live (`gemini_search_docs`) e lettura a schermo intero (`gemini_get_doc`) in tutta la documentazione. | Supportato in Claude Code, Cursor, OpenAI Codex e VS Code. |
| **[Plugin API Gemini](https://ai.google.dev/gemini-api/docs/coding-agents?hl=it#gemini-api-plugin)** | Pacchetto in bundle con le competenze ufficiali di Gemini, il server MCP di Docs e gli strumenti per le chiavi API. | Antigravity. |
| **[Documenti leggibili automaticamente](https://ai.google.dev/gemini-api/docs/coding-agents?hl=it#machine-readable-docs)** | Pulisci le pagine Markdown e gli indici `llms.txt`. | Tutte le pagine della documentazione su `ai.google.dev/gemini-api/docs`. |

## Installare le skill dell'agente Gemini

Le competenze dell'agente forniscono all'agente di programmazione regole procedurali, nomi di modelli attuali e
pattern di codice SDK. Anziché aggiungere istruzioni lunghe al prompt, l'agente carica ogni skill solo quando necessario. In questo modo, l'agente evita SDK ritirati
e utilizza pattern Gemini moderni.

Le skill funzionano insieme al server MCP di Gemini Docs. Se l'agente non ha installato il server MCP, la skill torna a
[`llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=it). Per scoprire di più
su come funzionano le skill, leggi la [Guida alle skill dell'API Gemini](https://aistudio.google.com/learn/gemini-api-skills?hl=it).

### Installazione con la CLI (`skills.sh` o Context7)

Installa le skill utilizzando [skills.sh](https://skills.sh) (opzione consigliata) o
[Context7](https://context7.com):

```
# List all available skills in the repository
npx skills add google-gemini/gemini-skills --list

# Install a specific skill globally with skills.sh
npx skills add google-gemini/gemini-skills --skill <skill-name> --global

# Or install with Context7
npx ctx7 skills install /google-gemini/gemini-skills <skill-name>
```

### Skill disponibili

#### `gemini-api-dev`

Competenza nella creazione di applicazioni con l'[API
Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) e gli SDK ufficiali dell'API Gemini
(`google-genai` per Python e `@google/genai` per TypeScript). Questa competenza
copre:

- Generazione di testo, chat a più turni, streaming, output strutturati e chiamata di funzione
- Generazione di immagini, sintesi vocale (TTS) e input multimodali
- Gestione dello stato della conversazione lato server, esecuzione in background, ricerca
  approfondita e agenti gestiti
- Nomi dei modelli attuali e migrazione del codice legacy `generateContent` o
  `google-generativeai`

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### `gemini-live-api-dev`

Competenza per la creazione di applicazioni di streaming audio e video in tempo reale con l'[API Gemini Live](https://ai.google.dev/gemini-api/docs/live-api?hl=it). Questa skill tratta i seguenti argomenti:

- Gestione delle sessioni WebSocket, token client effimeri e ripresa della sessione
- Streaming di audio, video e testo con rilevamento di attività vocale (VAD) e
  supporto dell'interruzione
- Ragionamento in background (pensiero esteso), chiamate asincrone non bloccanti
  di strumenti, trascrizione e traduzione vocale in tempo reale

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### `gemini-omni-flash-api`

Skill per generare e modificare video con Gemini Omni Flash utilizzando l'API Interactions. Include script di assistenza (`upload_file.py`,
`generate_video.py`, `prep_video.py`, `inspect_video.py`) e copre:

- Generazione di video da testo e creazione di prompt
- Transizioni del primo e dell'ultimo fotogramma e generazione di video guidata dai riferimenti
- Estensioni video e flussi di lavoro di preelaborazione dei contenuti multimediali

```
npx skills add google-gemini/gemini-skills --skill gemini-omni-flash-api --global
```

### Montare le skill in Managed Agents

Quando esegui agenti gestiti da remoto con l'API Interactions, puoi montare il repository
`google-gemini/gemini-skills` nello spazio di lavoro dell'agente. Per maggiori dettagli, consulta la
[guida alle competenze dell'API Gemini](https://aistudio.google.com/learn/gemini-api-skills?hl=it):

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Build a script that generates a 5-second video of a neon cityscape.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/google-gemini/gemini-skills",
                "target": ".agents",
            }
        ],
    },
)
```

## Connetti il server MCP di Gemini Docs

Il **server MCP di Gemini Docs** pubblico (`https://gemini-api-docs-mcp.dev`) consente
all'agente di accedere in tempo reale all'intero sito di documentazione. Il tuo agente può cercare
e leggere le pagine della documentazione per controllare gli schemi delle richieste, i limiti del modello e le nuove
funzionalità:

- `gemini_search_docs`: esegue ricerche nella documentazione dell'API Gemini per argomento o query.
- `gemini_get_doc`: legge l'intero contenuto Markdown di una pagina di documentazione specifica.

### Configurazione rapida

Esegui questo comando nel terminale o nella radice del progetto per configurare automaticamente gli agenti di codifica rilevati:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

### Configurazione per ambiente

### Claude Code

Esegui nel terminale:

```
$ claude mcp add --transport http geminiDocs https://gemini-api-docs-mcp.dev
```

### Cursore

Aggiungi a `~/.cursor/mcp.json` (globale) o `.cursor/mcp.json` (progetto):

```
{
  "mcpServers": {
    "geminiDocs": {
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

### Codex di OpenAI

Esegui nel terminale:

```
$ codex mcp add geminiDocs --url https://gemini-api-docs-mcp.dev
```

Oppure aggiungi a `~/.codex/config.toml`:

```
[mcp_servers.geminiDocs]
url = "https://gemini-api-docs-mcp.dev"
```

### VS Code (Copilot)

Aggiungi a `.vscode/mcp.json` nel tuo workspace:

```
{
  "servers": {
    "geminiDocs": {
      "type": "http",
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

## Plugin API Gemini

Se utilizzi **Antigravity**, il **plug-in API Gemini** è il modo più rapido per configurare il tuo workspace. Include il server MCP di Gemini Docs, tutte le skill ufficiali di Gemini (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`) e gli strumenti per le chiavi API in un unico download.

- **Installazione in Antigravity (UI):** vai a **Impostazioni > Personalizzazioni > Crea
  con i plug-in Google** e scarica **API Gemini**.
- **Installa con la CLI:**
  `bash
  agy plugin install https://github.com/google-gemini/gemini-skills`

## Documentazione leggibile da macchina

Le pagine web standard includono tag HTML, barre di navigazione e script che occupano
spazio nella finestra contestuale. `ai.google.dev` fornisce endpoint leggibili dalla macchina in modo che
agenti e script possano recuperare direttamente Markdown pulito:

- **Indice `llms.txt`**
  ([`https://ai.google.dev/gemini-api/docs/llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=it)):
  Elenca tutte le pagine della documentazione dell'API Gemini con link a ciascuna pagina.
- **URL Markdown diretti (`.md.txt`)**: aggiungi `.md.txt` a qualsiasi URL di documentazione su `ai.google.dev` (ad esempio, [`https://ai.google.dev/gemini-api/docs/coding-agents.md.txt`](https://ai.google.dev/gemini-api/docs/coding-agents.md.txt?hl=it)) per ottenere un'origine Markdown pulita per prompt salvati, regole `AGENTS.md` o script automatizzati.

## Regole del progetto consigliate (`AGENTS.md`)

Un file di regole del progetto (`AGENTS.md`, `.cursorrules` o `CLAUDE.md`) imposta le regole di base che vengono caricate all'inizio di ogni sessione dell'agente. Aggiungi queste linee guida alla radice del progetto in modo che gli agenti di codifica utilizzino per impostazione predefinita i modelli e gli SDK attuali:

```
# Gemini API Guidelines

- Before writing Gemini API code, consult the `geminiDocs` MCP server (`gemini_search_docs` / `gemini_get_doc`) or `https://ai.google.dev/gemini-api/docs/llms.txt`.
- Always use the current Gemini API SDK (`google-genai` for Python, `@google/genai` for TypeScript/JavaScript). Never use legacy SDKs (`google-generativeai` or `@google/generative-ai`).
- Use the Interactions API (`client.interactions.create`) for new applications unless a specific feature requires `generateContent`.
- Use current recommended models (see https://ai.google.dev/gemini-api/docs/models) and avoid deprecated models.
```

## Verifica e risolvi i problemi

### Verificare la configurazione

Per testare la configurazione, chiedi all'agente di programmazione:

```
Look up the request schema for the Gemini Interactions API in the documentation.
```

Un agente configurato utilizzerà `gemini_search_docs` sul server MCP `geminiDocs` e scriverà codice utilizzando `client.interactions.create` con l'SDK `google-genai` o `@google/genai`.

### Comandi di stato

| Ambiente | Verifica MCP | Verifica delle competenze |
| --- | --- | --- |
| **Claude Code** | Esegui `/mcp` | Esegui `/skills` |
| **Cursore** | Apri **Impostazioni > Funzionalità > MCP** | Apri **Impostazioni > Regole** |
| **OpenAI Codex** | Esegui `codex mcp list` | Controlla `.codex/skills/` o `~/.codex/skills/` |
| **Antigravity** | Apri **Personalizzazioni > Connessioni**. | Apri **Personalizzazioni > Regole** o esegui `/skills list`. |
| **VS Code (Copilot)** | Apri **Estensioni > MCP** o il riquadro Output | Fai clic su **Seleziona strumenti** in Copilot Chat. |

### Risoluzione dei problemi

- **Skill o server MCP non rilevati:** riavvia l'editor (Cursor o VS Code)
  o la sessione del terminale (Claude Code o Codex). La maggior parte degli agenti carica i server MCP e
  le skill solo all'avvio.
- **Conflitto di skill globale:** se l'agente ignora una skill installata a livello globale,
  installa la skill nella radice del progetto senza `--global`:
  `bash
  npx skills add google-gemini/gemini-skills --skill gemini-api-dev`
- **Regole ignorate**:assicurati che il file `AGENTS.md`, `.cursorrules` o `CLAUDE.md`
  si trovi nella directory principale del progetto.

## Passaggi successivi

- [Guida alle competenze dell'API Gemini](https://aistudio.google.com/learn/gemini-api-skills?hl=it)
- [Competenze dell'API Gemini su GitHub](https://github.com/google-gemini/gemini-skills)
- [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it)
- [Modelli disponibili](https://ai.google.dev/gemini-api/docs/models?hl=it)
- [Librerie e SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=it)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-06 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-06 UTC."],[],[]]
