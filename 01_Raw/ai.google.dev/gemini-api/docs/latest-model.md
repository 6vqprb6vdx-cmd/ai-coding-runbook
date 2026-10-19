---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=it
fetched_at: 2026-10-19T05:37:46.004118+00:00
title: "Novit\u00e0 di Gemini 4 Argon \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Novità di Gemini 4 Argon

Gemini 4 Argon (`gemini-4-argon`) è il nostro modello più recente e potente. Può ragionare più a lungo su problemi difficili per ottenere risultati migliori in attività complesse di programmazione, agentiche, matematiche e scientifiche. Gemini 4 Argon è disponibile tramite l'API Gemini e in Google AI Studio.

Gemini 4 Argon supporta una finestra contestuale unificata da 1 milione di token, una decodifica lunga fino a 1 milione di token e livelli di ragionamento regolabili (`low`, `medium`, `high`).

[experiment

Prova in AI Studio

Crea app da zero con Gemini 4 Argon e AI Studio.](https://aistudio.google.com/apps?model=gemini-4-argon&hl=it)
[smart\_toy

Galleria delle applicazioni

App Play e Remix, create con Gemini 4 Argon.](https://aistudio.google.com/learn/gemini-4-argon-showcase?hl=it)
[rocket\_launch

Inizia

Inizia a utilizzare Gemini 4 Argon con i prompt iniziali.](https://aistudio.google.com/learn/gemini-4-argon?hl=it)

Questa guida spiega le novità di Gemini 4 Argon, le modifiche all'API, gli esempi di codice e le indicazioni per la migrazione.

## Nuovo modello

| Modello | ID modello | Livello di ragionamento predefinito | Prezzi | Descrizione |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | `gemini-4-argon` | `medium` | Disponibile fino al 30 novembre 2026 al prezzo di lancio di 2 $per milione di token di input e 10 $per milione di token di output (successivamente 4 $ per milione di token di input e 20 $per milione di token di output). Per maggiori dettagli, consulta la pagina dei [prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it). | Il nostro modello più potente, progettato per risolvere i problemi più difficili con profondità e precisione nelle attività di ingegneria del software e di lavoro sulla conoscenza nel mondo reale. |

Per informazioni dettagliate, consulta la [pagina del modello Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=it). Per i dettagli sui prezzi di lancio, consulta la [sezione Prezzi](#pricing) più avanti in questa pagina o la [pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#gemini-4-argon).

## Guida rapida

Utilizza l'esempio seguente per inviare una richiesta a `gemini-4-argon` con il valore predefinito consigliato `thinking_level` (`medium`) e un limite di token di output di 64K:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Write a three.js script that renders a realistic 3D black hole with gravitational lensing."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
});

console.log(interaction.output_text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a three.js script that renders a realistic 3D black hole with gravitational lensing."
  }'
```

## Novità di Gemini 4 Argon

- **Limite unificato di token di input-output di 1 milione**:input, ragionamento e output condividono una finestra di 1.048.576 token.
- **Decodifica lunga**:una singola risposta ora può superare i 64.000 token, fino a 1 milione di token meno l'input. Vedi [Decodifica lunga](https://ai.google.dev/gemini-api/docs/long-decode?hl=it).
- **Comprensione dei video agentica è in disponibilità generale:** la [comprensione dei video agentica](https://ai.google.dev/gemini-api/docs/video-understanding?hl=it#agentic-video-understanding) è ora in disponibilità generale.
- **Supportato in Managed Agents**:l'[agente Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it) in Gemini Managed Agents ora supporta Gemini 4 Argon.

Per le specifiche complete, consulta la [pagina del modello Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=it). Per i dettagli sui prezzi, consulta la [pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#gemini-4-argon).

## Output più grande e decodifica lunga

Gemini 4 Argon può pensare più a lungo su problemi difficili di matematica, scienze e programmazione.

- **Utilizza `thinking_level` per controllare la profondità del ragionamento**:il livello di ragionamento determina la profondità del ragionamento del modello prima di rispondere. `max_output_tokens` è un limite rigido: la risposta si interrompe quando il ragionamento e l'output raggiungono questo limite, quindi impostalo su un valore sufficientemente alto da non interrompere la risposta.
- **Genera fino a 1 milione di token con l'esecuzione in background**:utilizza l'esecuzione in background con `max_output_tokens` maggiore di 65.536 per consentire a una singola risposta di superare i 64.000 token, fino a 1 milione di token. Il modello genera risposte lunghe in hop di massimo 64.000 token e ogni hop continua da dove si è interrotto il precedente. Con l'esecuzione in background, i nostri server eseguono questi hop di continuazione per te. Poiché ogni hop aggiunge un passaggio `model_output` a `interaction.steps`, unisci il testo di tutti i passaggi `model_output` al termine dell'interazione.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Write a complete, rigorous proof of the prime number theorem.",
    background=True,
    generation_config={
        "max_output_tokens": 262144,
        "thinking_level": "high",
    },
)

while interaction.status in ("in_progress", "queued"):
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Each hop adds a model_output step, so join the text of all of them.
text = "".join(
    content.text
    for step in interaction.steps
    if step.type == "model_output"
    for content in step.content
    if content.type == "text"
)
print(text)
print("Status:", interaction.status)
print("Usage:", interaction.usage)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Write a complete, rigorous proof of the prime number theorem.",
  background: true,
  generation_config: {
    max_output_tokens: 262144,
    thinking_level: "high",
  },
});

while (interaction.status === "in_progress" || interaction.status === "queued") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await client.interactions.get(interaction.id);
}

// Each hop adds a model_output step, so join the text of all of them.
const text = interaction.steps
  .filter((step) => step.type === "model_output")
  .flatMap((step) => step.content ?? [])
  .filter((content) => content.type === "text")
  .map((content) => content.text)
  .join("");
console.log(text);
console.log("Status:", interaction.status);
console.log("Usage:", interaction.usage);
```

### REST

```
ID=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a complete, rigorous proof of the prime number theorem.",
    "background": true,
    "generation_config": {
      "max_output_tokens": 262144,
      "thinking_level": "high"
    }
  }' | jq -r '.id')

while true; do
  RESP=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
  STATUS=$(echo "$RESP" | jq -r '.status')
  if [[ "$STATUS" != "in_progress" && "$STATUS" != "queued" ]]; then
    echo "$RESP" | jq -r '[.steps[]? | select(.type == "model_output") | .content[]? | select(.type == "text") | .text] | join("")'
    break
  fi
  sleep 5
done
```

L'esecuzione in background è il modo più semplice per eseguire una decodifica lunga. Esegue il loop di continuazione lato server finché il modello non termina o non raggiunge `max_output_tokens`. Se hai bisogno di un controllo più granulare su nuovi tentativi, backoff e gestione degli errori (o se non vuoi che le tue interazioni vengano archiviate), puoi utilizzare la continuazione lato client nell'[API GenerateContent](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=it). A breve sarà disponibile anche la continuazione lato client per l'API Interactions. Per lo streaming, la riconnessione, il conteggio dei token e quando utilizzare la decodifica lunga, consulta la [guida alla decodifica lunga](https://ai.google.dev/gemini-api/docs/long-decode?hl=it).

### Impostazione dei limiti dei token di output

`max_output_tokens` imposta i token di pensiero e di output totali per una risposta. Impostalo su un valore abbastanza alto da consentire al modello di pensare senza interrompere la risposta e abbastanza basso da limitare la spesa quando un prompt difficile utilizza tutto il budget.

Utilizza questi valori come punto di partenza:

- **Attività standard:** mantieni il valore predefinito di 65.536 o non impostare alcun valore.
- **App esistenti con un limite inferiore a 32.000**:aumenta `max_output_tokens` ad almeno 32.768. Gemini 4 Argon può dedicare più tempo al ragionamento rispetto ai modelli precedenti. Per utilizzare meno token, abbassa il livello di ragionamento.
- **Ragionamento e programmazione complessi**:imposta `background: true` e `max_output_tokens` su 131.072 o 262.144, fino a 1.048.576 meno i token di input.

## Informazioni sui livelli di ragionamento

Il [livello di ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it) è il tuo controllo principale su qualità, latenza e utilizzo dei token in Gemini 4 Argon:

| Livello di pensiero | Utilizzo dei token | Quando utilizzarle |
| --- | --- | --- |
| `low` | Minor numero di token, latenza più bassa | Attività più semplici e lavoro sensibile ai costi. Funziona anche per attività di analisi e scrittura che richiedono un ragionamento semplice. La qualità può diminuire per le attività difficili. |
| `medium` (valore predefinito) | Bilanciato | Consigliato per la maggior parte delle attività, tra cui codice complesso e casi d'uso agentici. |
| `high` | Maggior numero di token, primo token più lento | Ragionamento complesso, matematica e scienze avanzate e le attività di programmazione o degli agenti più difficili. Si abbina bene alla decodifica lunga per output lunghi. |

Esegui le valutazioni a tutti e tre i livelli, quindi scegli il livello più basso che soddisfa i tuoi standard di qualità. Per saperne di più, consulta la [guida al ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    generation_config={
        "thinking_level": "medium"  # Balanced reasoning effort for complex tasks
    }
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  generation_config: {
    thinking_level: "medium", // Balanced reasoning effort for complex tasks
  },
});

console.log(interaction.output_text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-4-argon",
    "input": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    "generation_config": {
      "thinking_level": "medium"
    }
  }'
```

## Gemini 4 Argon in Managed Agents

L'[agente Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it) in Gemini Managed Agents supporta Gemini 4 Argon. Per utilizzarlo, imposta il modello in `agent_config`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input=(
        "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
        "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
        "Check search indexing with Google Search for site:web.dev. "
        "Format the output as a side-by-side scorecard table with prioritized fixes."
    ),
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-4-argon",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  agent: "antigravity-preview-09-2026",
  input:
    "Audit https://web.dev for performance, Core Web Vitals, and SEO. " +
    "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. " +
    "Check search indexing with Google Search for site:web.dev. " +
    "Format the output as a side-by-side scorecard table with prioritized fixes.",
  environment: "remote",
  agent_config: {
    type: "antigravity",
    model: "gemini-4-argon",
  },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google'\''s PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
    "environment": "remote",
    "agent_config": {
      "type": "antigravity",
      "model": "gemini-4-argon"
    }
  }'
```

Per altre opzioni, consulta la sezione sulla [selezione del modello](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it#model-selection) nella guida dell'agente Antigravity.

## Elenco di controllo per la migrazione

```
  `/gemini-api-dev migrate my app to Gemini 4 Argon`
```

### Esegui la migrazione a gemini-4-argon

- **Aggiorna l'ID modello**:modifica la stringa del modello di destinazione in `gemini-4-argon`.
- **Esamina `max_output_tokens`**:se la imposti esplicitamente oggi, valuta la possibilità di aumentarla. Consigliamo almeno 32.768, poiché Gemini 4 Argon può utilizzare una parte maggiore del limite per il ragionamento.
- **Configura il livello di ragionamento:** scegli `low`, `medium` (predefinito) o `high` e testa il tuo workload con tutti e tre.
- **Abbandona la memorizzazione nella cache del contesto esplicita:** la memorizzazione nella cache esplicita (`cachedContents` / `caches.create`) non è supportata su Gemini 4 Argon. Rimuovi dalle richieste le chiamate che creano o fanno riferimento a `cached_content`. La [memorizzazione nella cache implicita](https://ai.google.dev/gemini-api/docs/caching?hl=it) è abilitata per impostazione predefinita per i prompt di almeno 4096 token e sconta del 95% i token di input memorizzati nella cache in caso di successo della cache.
- **Rimuovi i parametri di campionamento**:rimuovi `temperature`, `top_p` e `top_k` dalle richieste. Se vengono forniti, vengono ignorati.
- **Utilizza l'esecuzione in background per output lunghi:** per le attività che richiedono più di 64.000 token, imposta `background` su true e `max_output_tokens` su un valore superiore a 65.536.
- **Aumenta i timeout del client:** i prompt hard possono richiedere diversi minuti. Utilizza l'esecuzione in background o imposta i timeout del client HTTP su almeno 15 minuti.
- **Mantieni lo stato della conversazione sul server**:utilizza `previous_interaction_id` per le conversazioni multi-turno e con chiamate di funzione.

## Prezzi

Gemini 4 Argon è disponibile a un prezzo di lancio fino al 30 novembre 2026:

- **Token di input:** 2,00 $per 1 milione di token (4,00 $ a partire dal 1° dicembre 2026)
  - **Token di input memorizzati nella cache:** la memorizzazione nella cache implicita sconta del 95% l'input memorizzato nella cache, portandolo a 0,10 $per 1 milione di token (0,20 $ a partire dal 1° dicembre 2026).
- **Token di output, inclusi i token di ragionamento:** 10,00 $per 1 milione di token (20,00 $ a partire dal 1° dicembre 2026)

Gemini 4 Argon non è disponibile nel livello senza costi. Per i livelli di prezzo completi, consulta la [pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#gemini-4-argon).

## Altri modelli

- [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=it)
- [Gemini 3.6 Flash e 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=it)
- [Visualizza tutti i modelli](https://ai.google.dev/gemini-api/docs/models?hl=it)

## Passaggi successivi

- Leggi la [guida alla decodifica lunga](https://ai.google.dev/gemini-api/docs/long-decode?hl=it) per lo streaming, la riconnessione e il conteggio dei token.
- Scopri come funzionano i livelli di ragionamento e i riepiloghi dei ragionamenti nella [guida al ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it).
- Scopri di più sui job a lunga esecuzione nella [guida all'esecuzione in background](https://ai.google.dev/gemini-api/docs/background-execution?hl=it).
- Testa e perfeziona i prompt in [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-16 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-16 UTC."],[],[]]
