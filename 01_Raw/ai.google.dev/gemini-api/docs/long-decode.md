---
source_url: https://ai.google.dev/gemini-api/docs/long-decode?hl=it
fetched_at: 2026-10-19T05:33:44.566520+00:00
title: "Decodifica lunga \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Decodifica lunga

La decodifica lunga consente a Gemini 4 Argon di generare più di 64.000 token per le attività di ragionamento approfondito, fino alla finestra contestuale unificata di 1 milione di token (1.048.576 token condivisi tra input, ragionamento e output). Nell'API Interactions, puoi attivare la decodifica lunga con l'esecuzione in background in modo che i nostri server generino e combinino automaticamente ogni hop di 64.000 token in una singola interazione.

## Come funziona la decodifica lunga

Una singola chiamata del modello genera fino a 64.000 token. Quando una risposta richiede più di 64.000 token, il server la genera in hop di 64.000 token che continuano dal punto in cui si è interrotto l'hop precedente. Ogni hop aggiunge un passaggio `model_output` a `interaction.steps` con lo stesso ID interazione, quindi unisci questi passaggi per leggere la risposta completa:

1. Crea un'interazione con `background: true` e `max_output_tokens` maggiore di 65.536, fino a 1 milione.
2. Il server genera il primo hop, fino a 64.000 token.
3. Il server avvia l'hop successivo dal punto in cui si è interrotto l'ultimo e ripete l'operazione finché il modello non termina o non utilizza tutti i `max_output_tokens`.
4. Esegui il polling dell'interazione o trasmettila in streaming per ottenere il risultato.

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
# 1. Create the background interaction. It returns an ID right away.
ID=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a complete, rigorous proof of the prime number theorem.",
    "background": true,
    "generation_config": {"max_output_tokens": 262144, "thinking_level": "high"}
  }' | jq -r '.id')

# 2. Poll until the status is no longer in_progress or queued.
#    The REST response has no output_text field, so join the text of every model_output step.
while true; do
  RESP=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
  STATUS=$(echo "$RESP" | jq -r '.status')
  if [[ "$STATUS" != "in_progress" && "$STATUS" != "queued" ]]; then
    echo "$RESP" | jq -r '[.steps[]? | select(.type == "model_output") | .content[]? | select(.type == "text") | .text] | join("")'
    echo "$RESP" | jq '{status, usage}'
    break
  fi
  sleep 5
done
```

## Limiti di output

Le interazioni di streaming e non di streaming hanno un limite di token di output predefinito di 64.000, quindi le risposte fino a 64.000 token non richiedono modifiche al codice. Per generare più di 64.000 token, attiva l'esecuzione in background e aumenta `max_output_tokens`.

| Come creare l'interazione | Limite di output |
| --- | --- |
| `background: false` (streaming o non streaming) | 65.536 token. I valori maggiori di 65.536 restituiscono un errore 400. La decodifica lunga sarà disponibile a breve. |
| `background: true`, `max_output_tokens` non impostato | 65.536 token |
| `background: true`, `max_output_tokens` maggiore di 65.536 | Il valore di `max_output_tokens`, fino a 1.048.576 meno l'input |

## Quando utilizzare la decodifica lunga

La maggior parte delle richieste termina entro 64.000 token. Utilizza la decodifica lunga solo quando una risposta richiede più ragionamento e output.

| Workload | Utilizzare la decodifica lunga? | Perché |
| --- | --- | --- |
| Matematica, scienze, ricerca e dimostrazioni formali difficili | Sì | Il modello può utilizzare più di 64.000 token per esplorare e controllare il suo ragionamento. |
| Le attività di programmazione e agentiche più difficili | Sì | Alcune attività richiedono più di 64.000 token di ragionamento e codice in una risposta. La maggior parte delle attività di programmazione e agentiche termina con meno di 64.000 token. |
| Strumenti di valutazione che si arrestano al limite di output | Sì | La decodifica lunga impedisce di troncare le risposte quando il modello utilizza una risposta completa di 64.000 token per il ragionamento. |
| Chat, domande e risposte, riepilogo, classificazione ed estrazione | No | Queste attività terminano con meno di 32.000 token. |
| Richieste di una lunghezza fissa, ad esempio "scrivi un libro di 700.000 parole" | No | Il modello non segue i target di lunghezza. |
| Agenti che chiamano gli strumenti in molti turni brevi | No | Ogni turno è breve. Gli output di grandi dimensioni in ogni turno riempiono rapidamente la finestra contestuale condivisa. |
| Prompt vicini al limite di input | No | L'output può utilizzare solo 1.048.576 token meno l'input. |
| Richieste sensibili alla latenza | No | La decodifica lunga può essere eseguita per diversi minuti. |

L'impostazione di un valore elevato di `max_output_tokens` consente al modello di ragionare più a lungo su problemi difficili, ma il modello decide comunque quanto scrivere. Per controllare la quantità di ragionamento utilizzata dal modello, imposta [`thinking_level`](https://ai.google.dev/gemini-api/docs/thinking?hl=it).

## Scegliere come eseguire la decodifica lunga

L'esecuzione in background è il modo più semplice per eseguire la decodifica lunga nell'API Interactions. La continuazione lato client, in cui il codice avvia ogni hop, è disponibile con l'API GenerateContent. Sarà disponibile a breve nell'API Interactions come opzione più avanzata per gestire la resilienza.

|  | Esecuzione in background (API Interactions) | Continuazione lato client (API GenerateContent) |
| --- | --- | --- |
| **Chi avvia ogni hop** | I nostri server | L'SDK AI generativa di Google o il tuo codice |
| **Token per richiesta** | Il valore di `max_output_tokens`, in un'interazione | 64.000 per stream, 32.000 per richiesta non di streaming |
| **Tempo di esecuzione** | Fino a 24 ore | 20 minuti |
| **Spazio di archiviazione** | Richiede `store: true` | Nessun elemento archiviato sul server. |
| **Ideale per** | Il modo più semplice per eseguire la decodifica lunga | Controllo più granulare dei nuovi tentativi, in modo da poter creare il tuo backoff, la gestione degli errori e la resilienza |

Per utilizzare la continuazione lato client, consulta la sezione [Decodifica lunga con l'API GenerateContent](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=it).

## Trasmettere in streaming la decodifica lunga

Per trasmettere in streaming gli output e i riepiloghi del ragionamento man mano che arrivano, aggiungi `stream: true` e `thinking_summaries: "auto"`. Gli stream lunghi possono essere interrotti, quindi il client deve riconnettersi. Segui il pattern di riconnessione nella [guida all'esecuzione in background](https://ai.google.dev/gemini-api/docs/background-execution?hl=it). La decodifica lunga aggiunge queste regole:

- **Salva l'ID interazione:** leggilo dall'evento `interaction.created`.
- **Salva ogni `event_id`:** un `event_id` può arrivare negli eventi `interaction.status_update`, non solo nei delta di testo.
- **Riconnettiti con `last_event_id`:** chiama `interactions.get` con `stream: true` e l'ultimo `event_id`. Lo stream continua dopo questo evento.
- **Leggi fino alla fine:** dopo la riconnessione, leggi lo stream fino alla fine prima di controllare lo stato. Il server riproduce gli eventi mancanti, anche dopo il completamento dell'interazione.
- **Imposta timeout lunghi:** imposta i timeout di lettura HTTP su 15-20 minuti per stream.
- **Prevedi l'output in blocchi di 5000 token:** dopo i primi 64.000 token (circa i primi 10 minuti), lo stream invia l'output in blocchi di circa 5000 token. Le pause tra i blocchi sono normali. L'interazione non è bloccata, quindi mantieni aperta la connessione.

## Stato in background

Un'interazione in background può essere eseguita per un massimo di 24 ore. Quando lo stato non è più `in_progress` o `queued`, gestisci lo stato terminale utilizzando questa tabella:

| Stato | Significato | Cosa fare |
| --- | --- | --- |
| `completed` | Il modello ha terminato. | Unisci i passaggi `model_output` in `steps` e leggi `usage`. Per continuare la conversazione, passa il `id` di questa interazione come `previous_interaction_id`. |
| `requires_action` | Il modello ha richiesto una chiamata di strumento. | Esegui lo strumento. Poi invia il risultato con l'`id` di questa interazione. |
| `incomplete` | Il modello ha utilizzato tutti i `max_output_tokens`. Il testo può essere vuoto se il modello stava ancora ragionando. | Invia di nuovo la richiesta con un valore di `max_output_tokens` più alto. |
| `failed` | Il server non è riuscito a completare l'operazione o l'interazione è stata eseguita per più di 24 ore. | Riprova a inviare la richiesta. Se l'operazione non va a buon fine, condividi l'`id` dell'interazione con l'assistenza. |
| `cancelled` | Hai annullato l'interazione. | Leggi `usage` per visualizzare i token fatturati. |

Per interrompere un'interazione in esecuzione, chiama `client.interactions.cancel(id=interaction.id)` in Python, `client.interactions.cancel(interaction.id)` in JavaScript o `POST /v1beta/interactions/{id}/cancel` in REST.

## Impostare `max_output_tokens`

`max_output_tokens` imposta il limite combinato per il ragionamento e l'output nell'interazione. La riduzione non rende il modello più conciso, ma tronca la risposta prima.

| Il tuo workload | `max_output_tokens` consigliato |
| --- | --- |
| App esistenti con un limite inferiore a 32.000 | Aumenta a 32.768. Non è necessaria l'esecuzione in background. |
| Attività di programmazione e agentiche lunghe | Inizia da 65.536 (valore predefinito). Non è necessaria l'esecuzione in background. |
| Ragionamento complesso, matematica, scienze e dimostrazioni difficili | Imposta `background: true` e inizia da 262.144, fino a 1.048.576 meno i token di input. |

Per utilizzare meno token, riduci `thinking_level`. Utilizza `high` per le attività di ragionamento più difficili. Utilizza `medium` (valore predefinito) per la maggior parte del lavoro di programmazione e agentico.

## Contare i token

`interaction.usage` riporta i totali di tutti gli hop. Leggi questi campi: `total_input_tokens`, `total_cached_tokens`, `total_output_tokens`, `total_thought_tokens` e `total_tokens`.

`total_input_tokens` somma i token di input di ogni hop. Ogni hop invia il prompt e tutto ciò che è stato generato finora al modello come input, quindi gli stessi token vengono conteggiati di nuovo in ogni hop successivo. Ad esempio, un prompt di 1000 token che produce 200.000 token di ragionamento e output richiede quattro hop:

| Hop | Input inviato al modello | Token di input |
| --- | --- | --- |
| 1 | Prompt | 1000 |
| 2 | Prompt + hop 1 | 66.536 |
| 3 | Prompt + hop 1 e 2 | 132.072 |
| 4 | Prompt + hop da 1 a 3 | 197.608 |
| **Totale** |  | **397.216** |

`total_input_tokens` riporta circa 397.000 token (con gli input hop ripetuti scontati automaticamente del 95% dalla memorizzazione nella cache implicita), anche se la dimensione effettiva del contesto è di circa 201.000 token: il prompt di 1000 token più 200.000 token di ragionamento e output.

Durante uno stream, gli eventi `step.stop` e `interaction.status_update` includono `usage` (cumulativo per l'interazione). Leggi l'ultimo valore di `usage` anziché sommarli.

## Informazioni sulla fatturazione

Paghi per ogni token in ogni hop, inclusi gli hop che contengono solo il ragionamento.

- **Sconto cache:** la memorizzazione nella cache implicita sconta l'input ripetuto in ogni hop del 95%. L'input memorizzato nella cache costa 0,10 $per 1 milione di token anziché 2,00 $durante il periodo introduttivo.
- **Interazioni annullate e non riuscite:** paghi per tutto il lavoro completato prima della fine dell'interazione.

## Risoluzione dei problemi

| Sintomo | Causa e correzione |
| --- | --- |
| L'output si interrompe a 64.000 | `background` è `false` o `max_output_tokens` non è impostato. Imposta `background: true` e `max_output_tokens` maggiore di 65.536. |
| 400: "max\_output\_tokens maggiore di 65536 non è ancora supportato con background=false." | La decodifica lunga senza esecuzione in background non è ancora disponibile. Imposta `background: true`. |
| 400: "store=true è obbligatorio per le interazioni in background" | L'esecuzione in background richiede `store: true`. |
| Stato `incomplete` con testo vuoto | Il modello ha utilizzato tutti i token per il ragionamento. Aumenta `max_output_tokens` o riduci `thinking_level`. |
| La compattazione del contesto inizia troppo presto | Il framework dell'agente o lo strumento di valutazione legge `total_input_tokens`. Consulta la sezione [Contare i token](#count-tokens). |

## Limitazioni

- **Nessuna decodifica lunga senza esecuzione in background:** le interazioni con `background: false` si interrompono a 65.536 token. Il supporto sarà disponibile a breve.
- **Nessun target di lunghezza:** il modello non segue i target di lunghezza dei token o di conteggio delle parole.

## Passaggi successivi

- [Novità di Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/latest-model?hl=it)
- [Esecuzione in background](https://ai.google.dev/gemini-api/docs/background-execution?hl=it)
- [Ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it)
- [Decodifica lunga con l'API GenerateContent](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=it)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-13 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-13 UTC."],[],[]]
