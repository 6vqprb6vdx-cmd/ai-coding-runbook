---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=it
fetched_at: 2026-10-26T05:46:28.723921+00:00
title: "Novit\u00e0 di Gemini 4 Argon \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs/generate-content?hl=it)

Invia feedback

# Novità di Gemini 4 Argon

Gemini 4 Argon (`gemini-4-argon`) è il nostro modello più recente e potente. Può ragionare più a lungo su problemi difficili per ottenere risultati migliori in attività complesse di programmazione, agentiche, matematiche e scientifiche. Gemini 4 Argon è disponibile tramite l'API Gemini e in Google AI Studio.

Gemini 4 Argon supporta un limite unificato di 1 milione di token di input-output, una decodifica lunga fino a 1 milione di token e livelli di ragionamento regolabili (`low`, `medium`, `high`).

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
| Gemini 4 Argon | `gemini-4-argon` | `medium` | Disponibile fino al 30 novembre 2026 al prezzo di lancio di 2 $per milione di token di input e 10 $per milione di token di output (successivamente 4 $ per milione di token di input e 20 $per milione di token di output). Per i dettagli, consulta la sezione [Prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it). | Il nostro modello più potente, progettato per risolvere i problemi più difficili con profondità e precisione nelle attività di ingegneria del software e di lavoro sulla conoscenza nel mondo reale. |

## Guida rapida

Utilizza l'esempio seguente per inviare una richiesta a `gemini-4-argon` con il valore predefinito consigliato `thinking_level` (`medium`) e un limite di token di output di 64K:

### Python

```
pip install -U "google-genai>=2.30.1"
```

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
    config=types.GenerateContentConfig(
        max_output_tokens=65536,
        thinking_config=types.ThinkingConfig(thinking_level="medium"),
    ),
)

print(response.text)
```

### JavaScript

```
npm install "@google/genai@>=2.29.1"
```

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-4-argon",
  contents: "Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
  config: {
    maxOutputTokens: 65536,
    thinkingConfig: {
      thinkingLevel: "medium",
    },
  },
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders a realistic 3D black hole with gravitational lensing."}]
    }],
    "generationConfig": {
      "maxOutputTokens": 65536,
      "thinkingConfig": {
        "thinkingLevel": "medium"
      }
    }
  }'
```

## Novità di Gemini 4 Argon

- **Limite unificato di 1 milione di token di input-output:** i token di input, pensiero e output condividono un'unica finestra da 1 milione di token, con un limite di 32.000 per richiesta per le chiamate non in streaming e di 64.000 per stream per le chiamate in streaming.
- **Decodifica lunga fino a 1 milione di token**:il modello può generare oltre il limite per richiesta, fino a 1 milione di token meno l'input. Gli SDK Google GenAI più recenti continuano a essere disponibili per impostazione predefinita.
- **Comprensione dei video agentica (GA):** la [comprensione dei video agentica](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=it#agentic-video-understanding) è ora in disponibilità generale.
- **Supportato in Managed Agents**:l'[agente Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it) in Gemini Managed Agents ora supporta Gemini 4 Argon.

Per maggiori dettagli, consulta la [pagina del modello Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=it). Per i dettagli sui prezzi, consulta la [pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#gemini-4-argon).

## Output più grande e decodifica lunga

Quando un'attività richiede un ragionamento approfondito, Gemini 4 Argon può pensare più a lungo e lavorare di più per risolvere problemi complessi di matematica, scienze e programmazione in un'unica generazione.

- **Limite unificato di 1 milione di token di input-output**:Argon può utilizzare fino a 1 milione di token, meno i token di input, per il ragionamento e l'output combinati.
- **I token di ragionamento vengono conteggiati ai fini di `max_output_tokens`**:per le attività difficili, il modello utilizza una parte maggiore del tuo budget di `max_output_tokens` per fornire una risposta migliore. Utilizza `thinking_level` per controllare l'utilizzo dei token.
- **Limiti per richiesta (64.000 in modalità flusso di dati / 32.000 in modalità non flusso di dati)**: una richiesta in modalità flusso di dati restituisce fino a 65.536 token. Una richiesta non in streaming restituisce fino a 32.768 token, rispetto ai 65.536 di Gemini 3.x. Per le chiamate REST, questi limiti sono anche i valori predefiniti.

Gli SDK di Google GenAI più recenti eseguono la decodifica lunga per impostazione predefinita. Utilizza Python `google-genai` 2.30.1 o versioni successive oppure JavaScript `@google/genai` 2.29.1 o versioni successive.

In queste versioni, `automatic_continuation` è `True` per impostazione predefinita, quindi non è necessario impostarlo. Quando imposti `max_output_tokens` su un valore superiore al limite per richiesta, `generate_content` e `generate_content_stream` continuano automaticamente tra le richieste finché il modello non termina o non raggiunge `max_output_tokens`, restituendo una risposta combinata.

```
response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Write a complete, rigorous proof of the prime number theorem.",
    config=types.GenerateContentConfig(
        max_output_tokens=262144,
        thinking_config=types.ThinkingConfig(thinking_level="high"),
        automatic_continuation=True,  # Default.
    ),
)
```

Per eseguire il loop autonomamente, imposta `automatic_continuation=False`. Se chiami REST o utilizzi un SDK precedente, le richieste si interrompono al limite per richiesta. Per i loop REST, i framework di terze parti, il conteggio dei token e quando utilizzare la decodifica lunga, consulta la [guida alla decodifica lunga](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=it).

### Impostazione dei limiti dei token di output

`max_output_tokens` imposta i token di ragionamento e di output totali per una generazione, incluse tutte le richieste di continuazione. Impostalo su un valore sufficientemente alto in modo che il ragionamento non interrompa la risposta. Impostalo su un valore sufficientemente basso da limitare la spesa quando un prompt difficile lo utilizza tutto.

Utilizza le seguenti indicazioni come punto di partenza:

- **Attività standard**:mantieni l'impostazione predefinita.
- **App esistenti con un limite inferiore a 32.000**:aumenta `max_output_tokens` a 32.768. Per utilizzare meno token, riduci `thinking_level`.
- **Attività che in precedenza utilizzavano più di 32.000 token:** imposta `max_output_tokens` su 65.536.
- **Ragionamento e programmazione complessi**:imposta `max_output_tokens` su 131.072 o 262.144, fino a 1.048.576 meno i token di input.

Se una richiesta utilizza tutto il valore `max_output_tokens`, restituisce `finish_reason: "MAX_TOKENS"` e include un `continuation_token`. Puoi riprendere o ricominciare.

- **Riprendi dal checkpoint:** invia la richiesta originale con l'ultimo `continuation_token` e un `max_output_tokens` più alto. Se non generi `max_output_tokens`, la richiesta restituisce `400 INVALID_ARGUMENT`.
- **Ricomincia**:invia la richiesta originale con un valore `max_output_tokens` più alto e senza `continuation_token`.

### Informazioni sui livelli di ragionamento

Il [livello di ragionamento](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=it) è il tuo controllo principale su qualità, latenza e utilizzo dei token in Gemini 4 Argon:

| Livello di pensiero | Utilizzo dei token | Quando utilizzarle |
| --- | --- | --- |
| `low` | Minor numero di token, latenza più bassa | Attività più semplici e lavoro sensibile ai costi. Funziona anche per attività di analisi e scrittura che richiedono un ragionamento semplice. La qualità può diminuire per le attività difficili. |
| `medium` (valore predefinito) | Bilanciato | Consigliato per la maggior parte delle attività, tra cui codice complesso e casi d'uso agentici. |
| `high` | Maggior numero di token, primo token più lento | Ragionamento complesso, matematica e scienze avanzate e le attività di programmazione o degli agenti più difficili. Si abbina bene alla decodifica lunga per output lunghi. |

Esegui le valutazioni a tutti e tre i livelli con un valore `max_output_tokens` elevato, in modo che il limite non interrompa le risposte. Quindi scegli il valore più basso di `thinking_level` che soddisfa i tuoi standard di qualità.

## Elenco di controllo per la migrazione

```
  `/gemini-api-dev migrate my app to Gemini 4 Argon`
```

### Esegui la migrazione a gemini-4-argon

- **Aggiorna l'ID modello**:modifica la stringa del modello in `gemini-4-argon`.
- **Imposta `max_output_tokens` in modo esplicito:** il valore predefinito è 64K per le chiamate SDK e di streaming e 32K per le chiamate REST non di streaming.
- **Aumenta i limiti inferiori a 32K**:aumenta qualsiasi limite inferiore a 32K ad almeno 32.768. Utilizza `thinking_level` per ridurre la spesa per i token.
- **Pianifica una decodifica lunga:** per le attività che superano il limite per richiesta, utilizza l'SDK più recente o aggiungi un loop `continuation_token`.
- **Sostituisci `thinking_budget` con `thinking_level`:** `thinking_budget` funziona ancora e viene mappato al `thinking_level` più vicino, ma restituisce un avviso. Testa il tuo workload a `low`, `medium` e `high`.
- **Disattiva la memorizzazione nella cache del contesto esplicita**:la memorizzazione nella cache esplicita (`cachedContents`/`caches.create`) non è supportata su Gemini 4 Argon e restituisce un errore.
  Rimuovi le chiamate che creano o trasmettono `cached_content` in `GenerateContentConfig`.
  La [memorizzazione nella cache implicita](https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=it) è abilitata per impostazione predefinita per i prompt di almeno 4096 token e sconta del 95% i token di input memorizzati nella cache in caso di successo della cache.
- **Rimuovi i parametri ritirati:** rimuovi `temperature`, `top_p`, `top_k` e `candidate_count` dalle richieste. Se forniti, i parametri di campionamento vengono ignorati.
- **Aumenta i timeout del client:** imposta i timeout del client HTTP su almeno 20 minuti per chiamata.
- **Conserva le firme di pensiero**:passa la cronologia completa della conversazione, incluse le [firme di pensiero](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=it#signatures), nelle richieste multi-turn e di chiamata di funzione.

## Prezzi

Gemini 4 Argon è disponibile a un prezzo di lancio fino al 30 novembre 2026:

- **Token di input:** 2,00 $per 1 milione di token (4,00 $ a partire dal 1° dicembre 2026)
  - **Token di input memorizzati nella cache:** la memorizzazione nella cache implicita sconta del 95% l'input memorizzato nella cache, portandolo a 0,10 $per 1 milione di token (0,20 $ a partire dal 1° dicembre 2026).
- **Token di output, inclusi i token di ragionamento:** 10,00 $per 1 milione di token (20,00 $ a partire dal 1° dicembre 2026)

Gemini 4 Argon non è disponibile nel livello senza costi. Per i livelli di prezzo completi, consulta la [pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#gemini-4-argon).

## Altri modelli

- [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8?hl=it)
- [Gemini 3.6 Flash e 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6?hl=it)
- [Visualizza tutti i modelli](https://ai.google.dev/gemini-api/docs/models?hl=it)

## Passaggi successivi

- Leggi la [guida per gli sviluppatori sulla decodifica lunga](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=it) per i pattern completi di streaming, riconnessione e conteggio dei token.
- Scopri come funzionano i livelli di ragionamento e i riepiloghi dei ragionamenti nella [guida al ragionamento](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=it).
- Testa Gemini 4 Argon in [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-16 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-16 UTC."],[],[]]
