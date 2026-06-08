---
source_url: https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=it
fetched_at: 2026-06-08T15:01:15.460066+00:00
title: "API Interactions \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# API Interactions

L'**API Interactions** è il nuovo standard consigliato per la creazione con Gemini. È ottimizzato per i workflow agentici, la gestione dello stato lato server e le conversazioni multimodali e multi-turno complesse. L'API [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=it) originale rimane completamente supportata.

## Perché utilizzare l'API Interactions?

- **Gestione della cronologia lato server**: flussi multi-turn semplificati tramite `previous_interaction_id`. Il server abilita lo stato per impostazione predefinita (`store=true`), ma puoi attivare il comportamento senza stato impostando `store=false`.
- **Passaggi di esecuzione osservabili**: i passaggi digitati semplificano il debug di flussi complessi e il rendering dell'interfaccia utente per eventi intermedi (come pensieri o widget di ricerca).
- **Creato per i workflow agentici**: supporto nativo per l'utilizzo di strumenti in più passaggi, l'orchestrazione e i flussi di ragionamento complessi tramite passaggi di esecuzione digitati.
- **Attività in background e a lunga esecuzione**: supporta l'offload di operazioni che richiedono molto tempo, come [Deep Think](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=it) e [Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=it), a processi in background utilizzando `background=true`.
- **Accesso a nuovi modelli e capacità**: in futuro, i nuovi modelli al di fuori della famiglia principale, insieme a nuovi strumenti e capacità agentiche, verranno lanciati esclusivamente sull'API Interactions.

**Utilizza l'API Interactions** se stai iniziando un nuovo progetto, creando applicazioni con agenti o hai bisogno della gestione delle conversazioni lato server. **Utilizza [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=it)** se hai un'integrazione esistente che soddisfa le tue esigenze o se hai bisogno di una funzionalità [non ancora disponibile](#limitations) nell'API Interactions, come l'API Batch o la memorizzazione esplicita nella cache.

## Inizia

- **Configura l'agente di programmazione**: connettiti all'**MCP di Gemini Docs** e installa
  l'`gemini-interactions-api` skill per dare all'assistente l'accesso diretto
  alla documentazione per gli sviluppatori e alle best practice più recenti.
  [Configura l'agente di programmazione →](https://ai.google.dev/gemini-api/docs/coding-agents?hl=it)
- **Esegui la migrazione da `generateContent`**: se hai un'integrazione esistente,
  segui la [guida alla migrazione](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=it) per
  eseguire la transizione all'API Interactions.
- **Prova la guida rapida**: inizia con un esempio di funzionamento minimo nella
  [guida rapida all'API Interactions](https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=it).

### Guide alle funzionalità

Esplora le funzionalità specifiche dell'API Interactions tramite queste guide. Puoi utilizzare il pulsante di attivazione/disattivazione in queste pagine per passare dall'API generateContent all'API Interactions:

- [Generazione di testo](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=it)
- [Generazione di immagini](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=it)
- [Comprensione delle immagini](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=it)
- [Comprensione dell'audio](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=it)
- [Comprensione dei video](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=it)
- [Elaborazione dei documenti](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=it)
- [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=it)
- [Output strutturato](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=it)
- [Agente Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=it)
- [Inferenza flessibile](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=it)
- [Inferenza prioritaria](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=it)
- [Streaming](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=it)

## Come funziona l'API Interactions

L'API Interactions è incentrata su una risorsa principale: [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=it#Resource:Interaction). Un `Interaction` rappresenta un turno completo in una conversazione o un'attività. Funge da record di sessione, contenente l'intera cronologia di un'interazione come sequenza cronologica di **passaggi di esecuzione**. Questi passaggi includono i pensieri del modello, le chiamate e i risultati degli strumenti lato server o lato client (come `function_call` e `function_result`) e l'`model_output` finale. La risorsa archiviata (recuperata tramite `interactions.get`) include anche i passaggi `user_input` per il contesto completo, anche se la risposta `interactions.create` restituisce solo i passaggi generati dal modello.

Quando effettui una chiamata a
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=it#CreateInteraction), stai
creando una nuova risorsa `Interaction`.

### Accedere agli output con le proprietà di convenienza dell'SDK

Mentre l'API Interactions restituisce una sequenza temporale strutturata dei passaggi di esecuzione
(come pensieri, query di ricerca e chiamate di funzione), non è necessario
attraversare manualmente i passaggi per ottenere la risposta finale del modello.

Gli SDK Google GenAI forniscono proprietà di convenienza direttamente
sull'oggetto `Interaction` restituito per accedere agli output per diverse
modalità:

| Proprietà di convenienza dell'SDK | Tipo restituito | Descrizione |
| --- | --- | --- |
| **`interaction.output_text`** | Stringa | Restituisce gli ultimi blocchi di testo nella risposta del modello. Se la risposta è suddivisa in più blocchi `TextContent` consecutivi, questi vengono uniti automaticamente. Non include i blocchi di testo precedenti separati da contenuti non testuali (come pensieri, immagini, audio o chiamate di strumenti). Per risposte multimodali complesse o intercalate, devi eseguire l'iterazione manualmente su `steps`. |
| **`interaction.output_image`** | ImageContent o `None` | Restituisce l'ultimo blocco di immagini generato dal modello nella richiesta corrente. |
| **`interaction.output_audio`** | AudioContent o `None` | Restituisce l'ultimo blocco audio generato dal modello nella richiesta corrente. |

Per casi d'uso avanzati, come il rendering di processi di pensiero intermedi,
l'ispezione di chiamate di strumenti passo passo o il debug, puoi comunque ispezionare e
attraversare manualmente la sequenza temporale `interaction.steps` non elaborata.

### Gestione dello stato lato server

Puoi utilizzare `id` di un'interazione completata in una chiamata successiva utilizzando il parametro
`previous_interaction_id` per continuare la conversazione. Il server
utilizza questo ID per recuperare la cronologia della conversazione, evitando di dover
inviare nuovamente l'intera cronologia chat.

Il parametro `previous_interaction_id` conserva solo la cronologia della conversazione (input e output)
utilizzando `previous_interaction_id`. Gli altri parametri sono **ambito interazione**
e si applicano solo all'interazione specifica che stai generando:

- `tools`
- `system_instruction`
- `generation_config` (inclusi `thinking_level`, `temperature` e così via)

Ciò significa che devi specificare nuovamente questi parametri in ogni nuova interazione se vuoi che vengano applicati. La gestione dello stato lato server è facoltativa. Puoi anche
operare in modalità stateless inviando la cronologia completa della conversazione in ogni
richiesta.

### Archiviazione e conservazione dei dati

Per impostazione predefinita, l'API memorizza tutti gli oggetti Interaction (`store=true`) per semplificare l'utilizzo delle funzionalità di gestione dello stato lato server (con `previous_interaction_id`), l'esecuzione in background (utilizzando `background=true`) e per scopi di osservabilità.

- **Livello a pagamento**: il sistema conserva le interazioni per **55 giorni**.
- **Livello senza costi**: il sistema conserva le interazioni per **1 giorno**.

Se non vuoi, puoi
impostare `store=false` nella tua richiesta. Questo controllo è separato dalla gestione
dello stato; puoi disattivare l'archiviazione per qualsiasi interazione. Tieni presente, tuttavia, che
`store=false` è incompatibile con `background=true` e impedisce l'utilizzo di
`previous_interaction_id` per i turni successivi.

Puoi eliminare le interazioni memorizzate in qualsiasi momento utilizzando il metodo di eliminazione disponibile nella [guida di riferimento API](https://ai.google.dev/api/interactions-api?hl=it). Puoi eliminare le interazioni solo se
conosci l'ID interazione.

Al termine del periodo di conservazione, i dati verranno eliminati automaticamente.

Il sistema elabora gli oggetti Interaction in base ai [termini](https://ai.google.dev/gemini-api/terms?hl=it).

## Best practice

- **Percentuale di successi della cache**: l'utilizzo di `previous_interaction_id` per continuare le conversazioni consente al sistema di utilizzare più facilmente la memorizzazione nella cache implicita per la cronologia delle conversazioni, il che migliora le prestazioni e riduce i costi.
- **Interazioni miste**: hai la flessibilità di combinare le interazioni dell'agente e del modello all'interno di una conversazione. Ad esempio, puoi utilizzare un agente specializzato, come l'agente Deep Research, per la raccolta iniziale dei dati e poi utilizzare un modello Gemini standard per le attività di follow-up, come il riepilogo o la riformattazione, collegando questi passaggi con `previous_interaction_id`.

## Modelli e agenti supportati

| Nome modello | Tipo | ID modello |
| --- | --- | --- |
| Gemini 3.5 Flash | Modello | `gemini-3.5-flash` |
| Gemini 3.1 Flash-Lite | Modello | `gemini-3.1-flash-lite` |
| Gemini 3.1 Pro (anteprima) | Modello | `gemini-3.1-pro-preview` |
| Gemini 3 Flash (anteprima) | Modello | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Modello | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Modello | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | Modello | `gemini-2.5-flash-lite` |
| Anteprima clip di Lyria 3 | Modello | `lyria-3-clip-preview` |
| Anteprima di Lyria 3 Pro | Modello | `lyria-3-pro-preview` |
| Anteprima di Deep Research | Agente | `deep-research-pro-preview-12-2025` |
| Anteprima di Deep Research | Agente | `deep-research-preview-04-2026` |
| Anteprima di Deep Research | Agente | `deep-research-max-preview-04-2026` |

## SDK

Puoi utilizzare l'ultima versione degli SDK Google GenAI per accedere
all'API Interactions.

- In Python, questo è il pacchetto `google-genai` dalla versione `1.55.0` in poi.
- In JavaScript, questo è il pacchetto `@google/genai` dalla versione `1.33.0` in poi.

Puoi scoprire di più su come installare gli SDK nella pagina
[Librerie](https://ai.google.dev/gemini-api/docs/libraries?hl=it).

## Limitazioni

- **Stato beta**: l'API Interactions è in versione beta/anteprima. Funzionalità e
  schemi possono cambiare.
- **MCP remoto**: Gemini 3 non supporta l'MCP remoto, ma sarà disponibile a breve.

Le seguenti funzionalità sono supportate dall'API
[`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=it), ma **non sono ancora
disponibili** nell'API Interactions:

- **[Metadati video](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=it)**: il campo `video_metadata`, utilizzato per impostare gli intervalli di ritaglio e i frame rate personalizzati per la comprensione dei video.
- **[API batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it)**
- **[Chiamata di funzione automatica (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=it#automatic_function_calling_python_only)**
- **[Memorizzazione nella cache esplicita](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=it)**: tieni presente che la memorizzazione nella cache implicita lato server è disponibile nell'API Interactions tramite `previous_interaction_id`.

## Modifiche che provocano un errore

L'API Interactions è attualmente in una fase beta iniziale. Stiamo sviluppando e perfezionando attivamente le funzionalità dell'API, gli schemi delle risorse e le interfacce SDK in base all'utilizzo reale e al feedback degli sviluppatori. Di conseguenza, **potrebbero verificarsi modifiche che causano interruzioni**.

Modifiche che provocano errori esistenti:

- **Schema dei passaggi**: un nuovo array di passaggi sostituisce l'array di output, fornendo una sequenza temporale strutturata di ogni turno di interazione.

Per informazioni sulla modifica che provoca errori più recente e su come eseguire la migrazione, consulta la [guida alla migrazione delle modifiche che provocano errori (maggio 2026)](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it).

Altri potenziali aggiornamenti possono includere modifiche a schemi per input e output, firme di metodi e strutture di oggetti SDK, comportamenti di funzionalità specifici.

Per i workload di produzione, devi continuare a utilizzare l'API [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=it) standard. Continua a essere il
percorso consigliato per le implementazioni stabili e continueremo a svilupparlo e gestirlo attivamente.

## Feedback

Il tuo feedback è fondamentale per lo sviluppo dell'API Interactions.
Condividi le tue opinioni, segnala bug o richiedi funzionalità nel nostro
[forum della community di Google AI Developer](https://discuss.ai.google.dev/c/gemini-api/4?hl=it).

## Passaggi successivi

- Prova il [notebook di avvio rapido dell'API Interactions](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=it).
- Scopri di più sulle [interazioni di streaming](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=it) per la gestione delle risposte in tempo reale.
- Scopri di più sull'[agente Gemini Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-04 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-04 UTC."],[],[]]
