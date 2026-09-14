---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=it
fetched_at: 2026-09-14T05:49:20.238858+00:00
title: "Note di rilascio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Note di rilascio

Questa pagina documenta gli aggiornamenti dell'API Gemini.

## 21 luglio 2026

- **Disponibilità generale (GA) di Gemini 3.6 Flash e Gemini 3.5 Flash-Lite**:
  Sono state rilasciate versioni stabili e pronte per la produzione dei nostri modelli Flash 3.x più recenti:

  - **Gemini 3.6 Flash** (`gemini-3.6-flash`): offre una migliore efficienza dei token e funzionalità di pianificazione di codice/agenti a un prezzo inferiore rispetto a 3.5 Flash, risolvendo i feedback degli sviluppatori relativi alla verbosità dell'output.
  - **Gemini 3.5 Flash-Lite** (`gemini-3.5-flash-lite`): offre un'opzione di subagente a bassa latenza e altamente conveniente progettata per l'automazione di volumi elevati.

  Per saperne di più, consulta la guida [Ultimo modello Gemini](https://ai.google.dev/gemini-api/docs/latest-model?hl=it).
- **Parametri obsoleti**: i parametri di campionamento `temperature`, `top_p`
  e `top_k` sono ora obsoleti. Per maggiori dettagli, consulta la sezione
  [Ultimo modello Gemini](https://ai.google.dev/gemini-api/docs/latest-model?hl=it#sampling-parameter-deprecation).

## 6 luglio 2026

- Supporto dei [log degli sviluppatori](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=it) per l'API Interactions: i log per le chiamate API Interactions supportate sono ora visualizzabili nella [dashboard di AI Studio](https://aistudio.google.com/logs?hl=it).

## 30 giugno 2026

- **Gemini Omni Flash in anteprima pubblica**: rilasciato il giorno `gemini-omni-flash-preview`,
  un modello multimodale ad alte prestazioni progettato per la generazione di video ad alta velocità
  e l'editing di video conversazionali. Utilizzando l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it),
  puoi generare video di 3-10 secondi a 720p da descrizioni di testo o animare immagini statiche,
  quindi modificare e perfezionare gli output in modo conversazionale. Per iniziare, consulta la guida a
  [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=it) e la
  scheda del modello [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=it).
- Rilasciato `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite) per la disponibilità generale, il nostro modello multimodale integrato ottimizzato per una latenza e una generazione e modifica delle immagini a costi contenuti. Consulta la scheda del modello [Gemini 3.1
  Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=it) e la guida alla [generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it).

## 24 giugno 2026

- **Uso del computer**: è stata lanciata l'anteprima pubblica del supporto per lo strumento
  [Uso del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it) in Gemini 3.5 Flash. Questa
  release include azioni semplificate con intent, supporto integrato per
  ambienti browser, mobile e desktop, policy di sicurezza configurabili e
  rilevamento avanzato dell'iniezione di prompt.

## 17 giugno 2026

- **Supporto dello streaming per la generazione vocale**: lo streaming tramite `streamGenerateContent`
  (e `stream: true` nell'API Interactions) è ora supportato per il
  modello `gemini-3.1-flash-tts-preview`. Per saperne di più, consulta la guida
  [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it#streaming).

## 15 giugno 2026

- **Annuncio del ritiro**: i seguenti modelli di generazione di immagini
  verranno ritirati e [disattivati](https://ai.google.dev/gemini-api/docs/deprecations?hl=it) il **17 agosto 2026**:

  - **Modelli Imagen 4 e Gemini 3 Image**:

    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

    Per eseguire la migrazione del codice a endpoint di anteprima o stabili più recenti, consulta la pagina
    [Ritiri di Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=it#imagen-models).
- **Annuncio del ritiro**: i seguenti modelli di generazione video verranno ritirati e [arrestati](https://ai.google.dev/gemini-api/docs/deprecations?hl=it) il **30 giugno 2026**:

  - **Modelli Veo**:

    - `veo-2.0-generate-001`
    - `veo-3.0-generate-001`
    - `veo-3.0-fast-generate-001`

    Aggiorna l'integrazione in modo da utilizzare gli ID modello di anteprima di Veo 3.1
    (`veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`) o i
    modelli 3.1 GA disponibili tramite
    [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=it)
    per evitare interruzioni del servizio.
- **Annuncio del ritiro**: lo strumento sperimentale GMP Contextual View (un'interfaccia fissa per Grounding con Google Maps) verrà [chiuso](https://ai.google.dev/gemini-api/docs/deprecations?hl=it) il **15 giugno 2026**:

## 1° giugno 2026

- I seguenti modelli Gemini 2.0 sono ora [disattivati](https://ai.google.dev/gemini-api/docs/deprecations?hl=it):

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  Utilizza [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=it) o
  [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=it)
  in alternativa.

## 28 maggio 2026

- Sono state rilasciate `gemini-3.1-flash-image` (Nano Banana 2) e `gemini-3-pro-image`
  (Nano Banana Pro), le versioni disponibili a livello generale (GA) dei nostri modelli
  visivi nativi, [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=it)
  e [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=it).
- **Supporto della generazione di immagini da video**: ora puoi passare un file video (tramite caricamento diretto o come URL pubblico di YouTube) come contesto multimodale insieme a un prompt testuale per generare miniature di alta qualità, locandine cinematografiche o infografiche riassuntive. Questa funzionalità è supportata esclusivamente sul modello
  `gemini-3.1-flash-image`. Per saperne di più, consulta la guida
  [Generazione di immagini da video](https://ai.google.dev/gemini-api/docs/image-generation?hl=it#video-to-image).
- Annuncio di ritiro: i modelli `gemini-3.1-flash-image-preview` e
  `gemini-3-pro-image-preview` sono deprecati
  e verranno [disattivati](https://ai.google.dev/gemini-api/docs/deprecations?hl=it) il 25 giugno 2026.

## 25 maggio 2026

- Il modello `gemini-3.1-flash-lite-preview` è stato
  [arrestato](https://ai.google.dev/gemini-api/docs/deprecations?hl=it). Utilizza
  [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=it).

## 19 maggio 2026

- Rilasciata il giorno `gemini-3.5-flash`, la versione in disponibilità generale (GA) di
  [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=it),
  il nostro modello più intelligente per prestazioni all'avanguardia sostenute in
  attività agentiche e di programmazione. Ora questo è il modello alla base di `gemini-flash-latest`.
- Lanciati gli **agenti gestiti nell'API Gemini** in anteprima pubblica. In questo modo, gli sviluppatori possono creare e implementare agent autonomi e stateful che vengono eseguiti in ambienti sandbox Linux sicuri, isolati e ospitati da Google. Per saperne di più,
  consulta la pagina [Panoramica degli agenti](https://ai.google.dev/gemini-api/docs/agents?hl=it) e la
  [guida rapida](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=it).
- È stato rilasciato l'agente gestito **Antigravity Agent** per uso generico,
  [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=it), in anteprima pubblica.
  L'agente Antigravity può pianificare, ragionare, scrivere ed eseguire codice autonomamente,
  gestire file e navigare sul web all'interno del suo container sandbox. Per esempi di codice e specifiche, consulta la guida
  [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it).

## 7 maggio 2026

- Rilasciata il giorno `gemini-3.1-flash-lite`, la versione di disponibilità generale (GA) di
  [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=it),
  ottimizzata per velocità, scalabilità ed efficienza in termini di costi.
- Annuncio di ritiro: il modello `gemini-3.1-flash-lite-preview` verrà ritirato l'11/05/26 e [disattivato](https://ai.google.dev/gemini-api/docs/deprecations?hl=it) il 25 maggio 2026.

## 6 maggio 2026

- **Modifica che causa interruzione imminente**: lo schema di richiesta e risposta (`outputs` → `steps`) e la configurazione del formato di output (`response_format`) dell'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) stanno cambiando. Il nuovo schema diventerà
  quello predefinito il **26 maggio** e lo schema legacy verrà rimosso l'**8 giugno**.
  Per maggiori dettagli, consulta la
  [guida alla migrazione](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=it).

## 5 maggio 2026

- Aggiornamento della **Ricerca file** per supportare la ricerca multimodale. Ora puoi incorporare e cercare immagini in modo nativo utilizzando il modello `gemini-embedding-2`.
  I metadati di base ora includono `media_id` per le citazioni visive e
  `page_numbers` che indicano dove si trovano le informazioni. Per saperne
  di più, consulta la guida alla [ricerca di file](https://ai.google.dev/gemini-api/docs/file-search?hl=it).

## 4 maggio 2026

- È stato lanciato il supporto dei [webhook](https://ai.google.dev/gemini-api/docs/webhooks?hl=it) basati su eventi nell'API Gemini per sostituire i flussi di lavoro di polling per l'API Batch e le operazioni a lunga esecuzione.

## 30 aprile 2026

- Il modello `gemini-robotics-er-1.5-preview` è stato
  [arrestato](https://ai.google.dev/gemini-api/docs/deprecations?hl=it). Utilizza
  [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=it).

## 22 aprile 2026

- Rilasciato `gemini-embedding-2` come disponibile pubblicamente
  (GA). Per saperne di più, consulta la pagina [Incorporamenti](https://ai.google.dev/gemini-api/docs/embeddings?hl=it).

## 21 aprile 2026

- Sono state rilasciate nuove versioni dell'agente [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it)
  con pianificazione collaborativa, supporto della visualizzazione, integrazione
  del server MCP e ricerca di file:

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=it): progettato per
    velocità ed efficienza, ideale per essere trasmesso in streaming a un'interfaccia utente client.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=it): massima
    completezza per la raccolta e la sintesi automatica del contesto.

## 15 aprile 2026

- È stata lanciata l'[anteprima di Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=it), il nostro modello di sintesi vocale economico, espressivo e controllabile. Per saperne di più, leggi la documentazione su
  [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it).

## 14 aprile 2026

- È stato rilasciato `gemini-robotics-er-1.6-preview`, il nostro modello di robotica aggiornato.
  Ora ha nuove funzionalità come la lettura degli strumenti e capacità di ragionamento spaziale e fisico migliorate. Per scoprire di più, consulta la pagina [Gemini Robotics-ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=it) e il [blog](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=it).
- Annuncio di ritiro: il modello `gemini-robotics-er-1.5-preview` verrà [arrestato](https://ai.google.dev/gemini-api/docs/deprecations?hl=it) il 30 aprile 2026 alle 9:00 PST.

## 2 aprile 2026

- Rilasciati il giorno `gemma-4-26b-a4b-it` e il giorno `gemma-4-31b-it`, disponibili su
  [AI Studio](https://aistudio.google.com?hl=it) e tramite l'API Gemini,
  nell'ambito del lancio di [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=it).

## 1° aprile 2026

- Sono stati introdotti i nuovi livelli di inferenza [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=it) e [Priorità](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it), che offrono più opzioni
  per ottimizzare i costi o la latenza.

## 31 marzo 2026

- È stata lanciata l'anteprima di Veo 3.1 Lite, [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=it), il nostro modello di [generazione di video](https://ai.google.dev/gemini-api/docs/video?hl=it) più conveniente, progettato per l'iterazione rapida e la creazione di applicazioni ad alto volume.
- Il modello `gemini-2.5-flash-lite-preview-09-2025` è stato arrestato. Utilizza
  [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=it).

## 26 marzo 2026

- Rilasciato il [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=it), l'ultimo modello
  audio-to-audio (A2A) progettato per dialoghi in tempo reale e applicazioni
  AI vocali. Leggi la documentazione dell'[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=it) per iniziare.

## 25 marzo 2026

- Sono stati lanciati i modelli di generazione di musica [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=it): [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=it)
  (clip di 30 secondi) e [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=it)
  (brani integrali). Entrambi i modelli accettano input di testo e immagini e generano
  audio stereo di alta qualità a 48 kHz. Per dettagli ed esempi di codice, consulta la guida alla [generazione di musica](https://ai.google.dev/gemini-api/docs/music-generation?hl=it).

## 23 marzo 2026

- Sono stati implementati i [piani di fatturazione con pagamento anticipato e posticipato](https://ai.google.dev/gemini-api/docs/billing?hl=it) in
  AI Studio. Gli account esistenti potrebbero essere interessati. Per saperne di più, leggi la documentazione sulla [fatturazione](https://ai.google.dev/gemini-api/docs/billing?hl=it).

## 18 marzo 2026

- È stata rilasciata la nuova funzionalità [Combinazione di strumenti integrati e chiamate di funzione](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it), che consente
  di utilizzare gli strumenti integrati di Gemini insieme a strumenti di chiamata di funzione personalizzati
  in un'unica chiamata API.
- [Grounding con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it#supported_models)
  è ora supportato per i modelli Gemini 3.

## 16 marzo 2026

- Sono stati introdotti [livelli di utilizzo](https://ai.google.dev/gemini-api/docs/billing?hl=it#about-billing)
  e [limiti di spesa per l'account di fatturazione](https://ai.google.dev/gemini-api/docs/billing?hl=it#tier-spend-caps)
  migliorati per un'esperienza di fatturazione utente migliore.

## 12 marzo 2026

- Sono stati introdotti i [limiti di spesa a livello di progetto](https://ai.google.dev/gemini-api/docs/billing?hl=it#project-spend-caps) nella fatturazione di AI Studio.

## 10 marzo 2026

- È stato rilasciato `gemini-embedding-2-preview`, il nostro primo modello di embedding multimodale.
  Supporta input di testo, immagini, video, audio e PDF,
  mappa tutte le modalità in uno spazio di embedding unificato. Per saperne di più, consulta
  [Incorporamenti](https://ai.google.dev/gemini-api/docs/embeddings?hl=it).
- Annuncio di ritiro: il modello `gemini-2.5-flash-lite-preview-09-2025` verrà [arrestato](https://ai.google.dev/gemini-api/docs/deprecations?hl=it) il 31 marzo 2026.

## 9 marzo 2026

- Il modello Gemini 3 Pro Preview è stato [arrestato](https://ai.google.dev/gemini-api/docs/deprecations?hl=it). Ora `gemini-3-pro-preview` rimanda a
  [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=it).

## 3 marzo 2026

- È stata lanciata l'anteprima di Gemini 3.1 Flash-Lite, il primo modello Flash-Lite della
  serie Gemini 3. Consulta la [pagina del modello](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=it) per specifiche, aggiornamenti specifici e indicazioni per gli sviluppatori.

## 26 febbraio 2026

- È stato lanciato Nano Banana 2, [Gemini 3.1 Flash Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview?hl=it), un modello ad alta efficienza
  ottimizzato per la velocità e i casi d'uso ad alto volume.
- Annuncio del ritiro: l'anteprima di Gemini 3 Pro (`gemini-3-pro-preview`)
  verrà [chiusa](https://ai.google.dev/gemini-api/docs/deprecations?hl=it) il 9 marzo 2026.

## 19 febbraio 2026

- È stata rilasciata l'[anteprima di Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=it), la nostra ultima iterazione della nuova famiglia di modelli Gemini 3.
- È stato lanciato un endpoint separato `gemini-3.1-pro-preview-customtools`, che è
  più efficace nel dare la priorità agli strumenti personalizzati, per gli utenti che creano con un mix di bash
  e strumenti.

## 18 febbraio 2026

- Annuncio relativo al ritiro: i seguenti modelli verranno
  [disattivati](https://ai.google.dev/gemini-api/docs/deprecations?hl=it) il 1° giugno 2026:

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## 17 febbraio 2026

- I seguenti modelli sono [in fase di arresto](https://ai.google.dev/gemini-api/docs/deprecations?hl=it):

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## 29 gennaio 2026

- È stato lanciato il supporto per lo strumento Utilizzo del computer in `gemini-3-pro-preview` e
  `gemini-3-flash-preview`.

## 21 gennaio 2026

- Modificati gli alias di `latest`:

  - `gemini-pro-latest` è passato a `gemini-3-pro-preview`
  - `gemini-flash-latest` è passato a `gemini-3-flash-preview`

## 15 gennaio 2026

- Annuncio di ritiro: i seguenti modelli verranno
  [arrestati](https://ai.google.dev/gemini-api/docs/deprecations?hl=it) il 17 febbraio 2026:

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- Il modello `gemini-2.5-flash-image-preview` è stato arrestato.

## 14 gennaio 2026

- Il modello `text-embedding-004` è stato [arrestato](https://ai.google.dev/gemini-api/docs/deprecations?hl=it).

## 13 Gennaio 2026

- Sono state aggiunte risoluzioni di output 4K per [Veo](https://ai.google.dev/gemini-api/docs/video?hl=it) e un maggiore
  supporto per i video verticali in tutte le risoluzioni.

## 12 gennaio 2026

- È stata lanciata la funzionalità del ciclo di vita del modello. Alcuni modelli ora specificano la fase del ciclo di vita e la cronologia di ritiro. Per ulteriori informazioni, consulta la seguente documentazione:

  - [Fasi del modello](https://ai.google.dev/api/generate-content?hl=it#ModelStatus)

## 8 gennaio 2026

- È stato lanciato il supporto per i bucket Cloud Storage e per qualsiasi URL pre-firmato di database pubblico e privato come sorgente di ingresso dei dati per l'API Gemini. Il limite di dimensione del file
  è stato aumentato da 20 MB a 100 MB. Per maggiori dettagli, consulta la [guida ai metodi di input dei file](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=it).

## 19 dicembre 2025

- È stata introdotta una modifica che causa interruzioni all'API Interactions nella versione v1 beta. Il campo `total_reasoning_tokens` è stato rinominato in
  `total_thought_tokens` per allinearsi meglio al concetto di "pensieri" nei
  modelli di pensiero.

## 17 dicembre 2025

- È stata lanciata l'anteprima di Gemini 3 Flash, `gemini-3-flash-preview`, che offre prestazioni veloci
  di livello avanzato che competono con modelli più grandi a una frazione del
  costo. Con ragionamento visivo e spaziale migliorato e funzionalità di programmazione agentica. Leggi la documentazione su alcune nuove funzionalità, tra cui:

  - [Risposte di funzioni multimodali](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#multimodal)
  - [Esecuzione di codice con immagini](https://ai.google.dev/gemini-api/docs/code-execution?hl=it#images)

## 12 dicembre 2025

- Rilasciato il giorno `gemini-2.5-flash-native-audio-preview-12-2025`,
  un nuovo modello audio nativo per l'API Live. Questo aggiornamento migliora la capacità del modello
  di gestire workflow complessi. Per saperne di più, consulta la
  [guida all'API Live](https://ai.google.dev/gemini-api/docs/live-guide?hl=it) e
  [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-live?hl=it).

## 11 dicembre 2025

- È stata lanciata l'API Interactions. Questa API fornisce un'interfaccia unificata
  per interagire con i modelli e gli agenti Gemini. Per saperne di più, consulta la guida all'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it).
- È stato lanciato l'agente Gemini Deep Research in anteprima. Può pianificare, eseguire e sintetizzare autonomamente i risultati per attività di ricerca in più passaggi. Per
  maggiori dettagli, consulta la guida [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it).

## 10 dicembre 2025

- Sono stati lanciati miglioramenti ai nostri [modelli di sintesi vocale](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it), all'anteprima di Gemini 2.5 Flash TTS (ottimizzata per la bassa latenza) e all'anteprima di Gemini 2.5 Pro TTS (ottimizzata per la qualità), tra cui espressività migliorata, ritmo preciso e dialoghi fluidi.

## 9 dicembre 2025

- I seguenti modelli API Gemini Live non sono più disponibili:
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 5 dicembre 2025

- La fatturazione di Gemini 3 per il [grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it) inizierà il 5 gennaio 2026.

## 4 dicembre 2025

- Annuncio di ritiro: il modello `gemini-2.5-flash-image-preview` verrà
  disattivato il 15 gennaio 2026.

## 3 dicembre 2025

- Annuncio di ritiro: il modello `text-embedding-004` verrà disattivato il 14 gennaio 2026.

## 20 novembre 2025

- È stata rilasciata l'anteprima delle immagini di Gemini 3 Pro, `gemini-3-pro-image-preview`, la
  prossima iterazione del modello Nano Banana. Per ulteriori dettagli, consulta la pagina [Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it).

## 18 novembre 2025

- È stato lanciato il primo modello della serie Gemini 3, `gemini-3-pro-preview`, il nostro
  modello allo stato dell'arte per il ragionamento e la comprensione multimodale con potenti
  funzionalità agentiche e di programmazione.

  Oltre ai miglioramenti in termini di intelligenza e prestazioni,
  l'anteprima di Gemini 3 Pro introduce nuovi comportamenti relativi a:

  - [Risoluzione dei contenuti multimediali](https://ai.google.dev/gemini-api/docs/media-resolution?hl=it)
  - [Firme del pensiero](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=it)
  - [Livelli di pensiero](https://ai.google.dev/gemini-api/docs/thinking?hl=it#thinking-levels)

  Leggi la [Guida per gli sviluppatori di Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=it) per
  migrazione, nuove funzionalità e specifiche.

## 11 novembre 2025

- Annuncio del ritiro: i seguenti modelli verranno chiusi:

  - 12 novembre:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - 14 novembre:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## 10 novembre 2025

- Il seguente modello è stato arrestato:

  - `imagen-3.0-generate-002`

  Usa [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=it#imagen-4). Per ulteriori dettagli, consulta la
  [tabella dei ritiri di Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=it).

## 6 novembre 2025

- È stata lanciata l'API File Search in anteprima pubblica, consentendo agli sviluppatori di
  basare le risposte sui propri dati. Per saperne di più, consulta la nuova pagina [Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it).

## November 4, 2025

- Per [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=it), il conteggio dei token di input per le immagini è stato ridotto da 1290 a 258, diminuendo il costo della modifica delle immagini.
- Annuncio del ritiro: i seguenti modelli verranno chiusi:

  - 18 novembre:

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - 2 dicembre:

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - 9 dicembre:

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## 29 ottobre 2025

- È stato lanciato il nuovo strumento [logging e set di dati](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=it)
  per l'API Gemini.

## 20 ottobre 2025

- I seguenti modelli API Gemini Live sono ora arrestati:

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  Puoi utilizzare `gemini-2.5-flash-native-audio-preview-09-2025`.
- Annuncio di ritiro: chiusura di `gemini-2.0-flash-live-001` e
  `gemini-live-2.5-flash-preview` a partire dal 9 dicembre 2025.

## 17 ottobre 2025

- **Grounding con Google Maps** è ora
  disponibile a livello generale. Per saperne di più, consulta la documentazione relativa a
  [Grounding con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it).

## 15 ottobre 2025

- Sono stati rilasciati i modelli [Veo 3.1 e 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=it#veo-3.1) in anteprima pubblica, con nuove funzionalità, tra cui:

  - Estensione dei video creati con Veo.
  - Fare riferimento a un massimo di tre immagini per generare un video.
  - Fornire immagini del primo e dell'ultimo fotogramma per generare video.

  Questo lancio ha aggiunto anche altre opzioni per le durate dei video di output di Veo 3: 4, 6 e 8 secondi.
- Annuncio di ritiro: chiusura di `veo-3.0-generate-preview` e
  `veo-3.0-fast-generate-preview` a partire dal 12 novembre 2025.

## 7 ottobre 2025

- È stata lanciata l'[anteprima dell'utilizzo di Gemini 2.5 su computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it)

## 2 ottobre 2025

- Lancio della disponibilità generale di Gemini 2.5 Flash Image: [Generazione di immagini con Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it)

## 29 settembre 2025

- I seguenti modelli Gemini 1.5 sono stati disattivati:
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 25 settembre 2025

- È stato rilasciato il modello Gemini Robotics-ER 1.5 in anteprima. Consulta la
  [panoramica della robotica](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=it)
  per scoprire come utilizzare il modello per la tua applicazione di robotica.
- Sono stati lanciati i seguenti modelli di anteprima:

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  Per maggiori dettagli, consulta la pagina [Modelli](https://ai.google.dev/gemini-api/docs/models?hl=it).

## 23 settembre 2025

- Rilasciato `gemini-2.5-flash-native-audio-preview-09-2025`, un nuovo modello audio nativo per l'API Live con gestione migliorata delle chiamate di funzioni e dell'interruzione del parlato. Per saperne di più, consulta la
  [guida all'API Live](https://ai.google.dev/gemini-api/docs/live-guide?hl=it) e
  [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.5-flash-native-audio).

## 16 settembre 2025

- Annuncio di ritiro: i seguenti modelli verranno arrestati a ottobre 2025:

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  Per informazioni dettagliate sull'ultimo modello di embedding, consulta la pagina [Embedding](https://ai.google.dev/gemini-api/docs/embeddings?hl=it).

## 10 settembre 2025

- È stato rilasciato il supporto per il
  [modello Embeddings nell'API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it#batch-embedding)
  ed è stata aggiunta l'API Batch alla
  [libreria di compatibilità con OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=it#batch) per
  semplificare ulteriormente l'inizio delle query batch.

## 9 settembre 2025

- Lancio di Veo 3 e Veo 3 Fast GA, con prezzi più bassi e nuove opzioni per
  proporzioni, risoluzione e seeding. Per saperne di più, leggi la
  [documentazione di Veo](https://ai.google.dev/gemini-api/docs/video?hl=it#model-features).

## 26 agosto 2025

- È stato lanciato [Gemini 2.5 Image Preview](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.5-flash-image-preview),
  il nostro modello di generazione di immagini nativo più recente.

## 18 agosto 2025

- È stato rilasciato lo [strumento di contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it) per la disponibilità generale (GA), uno strumento per fornire URL come contesto aggiuntivo ai prompt. Il supporto per l'utilizzo del contesto URL con il modello `gemini-2.0-flash`
  (disponibile durante la release sperimentale) verrà interrotto tra una settimana.

## 14 agosto 2025

- Sono stati rilasciati i modelli Imagen 4 Ultra, Standard e Fast come disponibili a livello generale
  (GA). Per saperne di più, consulta la pagina [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=it).

## 7 agosto 2025

- L'impostazione `allow_adult` nella generazione Da immagine a video è ora disponibile nelle regioni con limitazioni. Per informazioni dettagliate, visita la pagina
  [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=it#veo-model-parameters).

## 31 luglio 2025

- È stata lanciata la generazione di video da immagini per il modello Veo 3 Preview.
- È stato rilasciato il modello di anteprima di Veo 3 Fast.
- Per scoprire di più su Veo 3, visita la pagina [Veo](https://ai.google.dev/gemini-api/docs/video?hl=it).

## 22 luglio 2025

- Rilasciato il giorno `gemini-2.5-flash-lite`, il nostro modello Gemini 2.5 veloce, economico e ad alte prestazioni. Per saperne di più, consulta [Gemini 2.5 Flash Lite](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.5-flash-lite).

## Luglio 17, 2025

- È stato lanciato `veo-3.0-generate-preview`, l'ultimo aggiornamento di Veo che introduce la generazione di video con audio. Per scoprire di più su Veo 3, visita la pagina [Veo](https://ai.google.dev/gemini-api/docs/video?hl=it).
- Limiti di frequenza aumentati per Imagen 4 Standard e Ultra. Per ulteriori dettagli, visita la pagina [Limiti di frequenza](https://ai.google.dev/gemini-api/docs/rate-limits?hl=it).

## 14 luglio 2025

- È stata rilasciata `gemini-embedding-001`, la versione stabile del nostro
  modello di text embedding. Per saperne di più, consulta
  [Incorporamenti](https://ai.google.dev/gemini-api/docs/embeddings?hl=it). Il modello `gemini-embedding-exp-03-07` verrà ritirato il 14 agosto 2025.

## 7 luglio 2025

- È stata lanciata la modalità batch dell'API Gemini. Raggruppa le richieste e inviale per l'elaborazione
  in modo asincrono. Per saperne di più, vedi [Modalità batch](https://ai.google.dev/gemini-api/docs/batch-mode?hl=it).

## 26 giugno 2025

- I modelli in anteprima `gemini-2.5-pro-preview-05-06` e
  `gemini-2.5-pro-preview-03-25` ora reindirizzano alla
  versione stabile più recente `gemini-2.5-pro`.
- `gemini-2.5-pro-exp-03-25` è stato chiuso.

## 24 giugno 2025

- Sono stati rilasciati i modelli di anteprima Imagen 4 Ultra e Standard. Per saperne di più, consulta la pagina
  [Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it).

## 17 giugno 2025

- È stato rilasciato `gemini-2.5-pro`, la versione stabile del nostro modello più potente, ora con il pensiero adattivo. Per saperne di più, vedi
  [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.5-pro)
  e [Pensiero](https://ai.google.dev/gemini-api/docs/thinking?hl=it). `gemini-2.5-pro-preview-05-06`
  verrà reindirizzato a `gemini-2.5-pro` il 26 giugno 2025.
- È stato rilasciato `gemini-2.5-flash`, il nostro primo modello 2.5 Flash stabile. Per saperne di più, consulta [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.5-flash).
  `gemini-2.5-flash-preview-04-17` verrà ritirato il 15 luglio 2025.
- Rilasciato il giorno `gemini-2.5-flash-lite-preview-06-17`, un modello Gemini 2.5 a basso costo e ad alte prestazioni. Per saperne di più, consulta [Gemini 2.5 Flash Lite (anteprima)](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.5-flash-lite).

## 5 giugno 2025

- È stato rilasciato `gemini-2.5-pro-preview-06-05`, una nuova versione del nostro modello più potente, ora con il pensiero adattivo. Per saperne di più, consulta
  [Anteprima di Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.5-pro-preview-06-05)
  e [Pensiero](https://ai.google.dev/gemini-api/docs/thinking?hl=it).
  `gemini-2.5-pro-preview-05-06` verrà reindirizzato a `gemini-2.5-pro` il
  26 giugno 2025.

## 27 maggio 2025

- L'ultimo modello di ottimizzazione disponibile, Gemini 1.5 Flash 001, è stato arrestato.
  L'ottimizzazione non è più supportata su nessun modello.
  Consulta [Ottimizzazione con l'API Gemini](https://ai.google.dev/gemini-api/docs/model-tuning?hl=it).

## 20 maggio 2025

**Aggiornamenti dell'API:**

- È stato lanciato il supporto per la
  [pre-elaborazione video personalizzata](https://ai.google.dev/gemini-api/docs/video-understanding?hl=it#customize-video-processing)
  utilizzando intervalli di ritaglio e campionamento della frequenza fotogrammi configurabile.
- È stato lanciato l'utilizzo di più strumenti, che supporta la configurazione
  dell'[esecuzione del codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it) e del
  [Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/grounding?hl=it) nella stessa
  richiesta `generateContent`.
- È stato lanciato il supporto per le
  [chiamate di funzioni asincrone](https://ai.google.dev/gemini-api/docs/live-tools?hl=it#async-function-calling)
  nell'API Live.
- È stato lanciato uno
  [strumento di contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)
  sperimentale per fornire URL come contesto aggiuntivo per i prompt.

**Aggiornamenti del modello:**

- È stato rilasciato `gemini-2.5-flash-preview-05-20`, un modello Gemini
  [in anteprima](https://ai.google.dev/gemini-api/docs/models?hl=it#model-versions) ottimizzato per
  il rapporto prezzo/prestazioni e il pensiero adattivo. Per saperne di più, consulta
  [Anteprima di Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.5-flash-preview)
  e [Pensiero](https://ai.google.dev/gemini-api/docs/thinking?hl=it).
- Sono stati rilasciati i modelli
  [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.5-pro-preview-tts)
  e
  [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.5-flash-preview-tts), in grado di
  [generare discorsi](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it) con uno o due
  oratori.
- È stato rilasciato il modello `lyria-realtime-exp`, che
  [genera musica](https://ai.google.dev/gemini-api/docs/music-generation?hl=it) in tempo reale.
- Sono stati rilasciati `gemini-2.5-flash-preview-native-audio-dialog` e
  `gemini-2.5-flash-exp-native-audio-thinking-dialog`,
  nuovi modelli Gemini per l'API Live con funzionalità di output audio native. Per
  scoprire di più, consulta la
  [guida all'API Live](https://ai.google.dev/gemini-api/docs/live-guide?hl=it#native-audio-output) e
  [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.5-flash-native-audio).
- Rilasciata l'anteprima di `gemma-3n-e4b-it`, disponibile su
  [AI Studio](https://aistudio.google.com?hl=it) e tramite l'API Gemini,
  nell'ambito del lancio di [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=it).

## 7 maggio 2025

- È stato rilasciato `gemini-2.0-flash-preview-image-generation`, un modello di anteprima per
  generare e modificare immagini. Per saperne di più, consulta [Generazione
  di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it) e
  [Generazione di immagini di anteprima di Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.0-flash-preview-image-generation).

## 6 maggio 2025

- È stato rilasciato `gemini-2.5-pro-preview-05-06`, una nuova versione del nostro modello più potente, con miglioramenti al codice e alle chiamate di funzione. `gemini-2.5-pro-preview-03-25`
  punterà automaticamente alla nuova versione del modello.

## 17 aprile 2025

- È stato rilasciato `gemini-2.5-flash-preview-04-17`, un modello Gemini
  [in anteprima](https://ai.google.dev/gemini-api/docs/models?hl=it#model-versions) ottimizzato per
  il rapporto prezzo/prestazioni e il pensiero adattivo. Per saperne di più, consulta
  [Anteprima di Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.5-flash-preview)
  e [Pensiero](https://ai.google.dev/gemini-api/docs/thinking?hl=it).

## 16 Aprile 2025

- È stata lanciata la memorizzazione nella cache del contesto per
  [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.0-flash).

## 9 aprile 2025

**Aggiornamenti del modello:**

- È stato rilasciato `veo-2.0-generate-001`, un modello di generazione video da testo e immagini disponibile a livello generale (GA) in grado di generare video dettagliati e artisticamente sfumati. Per saperne di più, consulta la [documentazione di Veo](https://ai.google.dev/gemini-api/docs/video?hl=it).
- È stata rilasciata il giorno `gemini-2.0-flash-live-001` una versione di anteprima pubblica del modello
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=it) con la fatturazione abilitata.

  - **Gestione e affidabilità delle sessioni migliorate**

    - **Ripresa della sessione**:mantieni attive le sessioni in caso di interruzioni temporanee della rete. L'API ora supporta l'archiviazione dello stato della sessione lato server (fino a 24 ore) e fornisce handle (session\_resumption) per riconnettersi e riprendere da dove avevi interrotto.
    - **Sessioni più lunghe tramite la compressione del contesto:** consente interazioni più lunghe rispetto ai limiti di tempo precedenti. Configura la compressione della finestra contestuale con un meccanismo a finestra scorrevole per gestire automaticamente la lunghezza del contesto, evitando interruzioni improvvise dovute ai limiti del contesto.
    - **Notifica di disconnessione controllata**:ricevi un messaggio del server `GoAway` che indica quando una connessione sta per chiudersi, consentendo una gestione controllata prima della chiusura.
  - **Maggiore controllo sulle dinamiche di interazione**
  - **Rilevamento dell'attività vocale (VAD) configurabile**: scegli i livelli di sensibilità o disattiva completamente il VAD automatico e utilizza i nuovi eventi client (`activityStart`, `activityEnd`) per il controllo manuale del turno.
  - **Gestione configurabile delle interruzioni:** decidi se l'input dell'utente
    deve interrompere la risposta del modello.
  - **Copertura della rotazione configurabile**:scegli se l'API elabora continuamente tutti gli input audio e video o li acquisisce solo quando viene rilevato che l'utente finale sta parlando.
  - **Risoluzione dei contenuti multimediali configurabile:** ottimizza la qualità o l'utilizzo dei token
    selezionando la risoluzione per i contenuti multimediali di input.
  - **Output e funzionalità più ricchi**
  - **Opzioni di voce e lingua ampliate:** scegli tra due nuove voci e
    30 nuove lingue per l'uscita audio. La lingua di output è ora
    configurabile in `speechConfig`.
  - **Streaming di testo**:ricevi risposte di testo in modo incrementale man mano che vengono generate, consentendo una visualizzazione più rapida per l'utente.
  - **Report sull'utilizzo dei token:** ottieni approfondimenti sull'utilizzo con conteggi dettagliati dei token forniti nel campo `usageMetadata` dei messaggi del server, suddivisi per modalità e fasi di prompt o risposta.

## 4 aprile 2025

- Rilasciata il giorno `gemini-2.5-pro-preview-03-25`, una versione di Gemini 2.5 Pro in anteprima pubblica
  con la fatturazione abilitata. Puoi continuare a utilizzare `gemini-2.5-pro-exp-03-25`
  nel livello senza costi.

## 25 marzo 2025

- Rilasciato `gemini-2.5-pro-exp-03-25`, un modello Gemini sperimentale pubblico
  con la modalità di ragionamento sempre attiva per impostazione predefinita.
  Per saperne di più, consulta [Gemini 2.5 Pro Experimental](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-2.5-pro-preview-03-25).

## 12 marzo 2025

**Aggiornamenti del modello:**

- È stato lanciato un modello sperimentale [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=it#gemini)
  in grado di generare e modificare immagini.
- Rilasciato il giorno `gemma-3-27b-it`, disponibile su
  [AI Studio](https://aistudio.google.com?hl=it) e tramite l'API Gemini,
  nell'ambito del lancio di [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=it).

**Aggiornamenti dell'API:**

- È stato aggiunto il supporto per gli [URL di YouTube](https://ai.google.dev/gemini-api/docs/vision?hl=it#youtube) come origine media.
- È stato aggiunto il supporto per l'inclusione di un
  [video incorporato](https://ai.google.dev/gemini-api/docs/vision?hl=it#inline-video) di dimensioni inferiori a 20 MB.

## 11 marzo 2025

**Aggiornamenti dell'SDK:**

- È stata rilasciata l'[SDK Google Gen AI per TypeScript e JavaScript](https://googleapis.github.io/js-genai) in anteprima pubblica.

## 7 marzo 2025

**Aggiornamenti del modello:**

- Rilasciato il giorno `gemini-embedding-exp-03-07`, un
  [modello di incorporamento sperimentale](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=it)
  basato su Gemini in anteprima pubblica.

## 28 febbraio 2025

**Aggiornamenti dell'API:**

- Supporto della funzionalità [Ricerca come strumento](https://ai.google.dev/gemini-api/docs/grounding?hl=it)
  aggiunta a `gemini-2.0-pro-exp-02-05`, un modello sperimentale basato su
  Gemini 2.0 Pro.

## 25 febbraio 2025

**Aggiornamenti del modello:**

- È stata rilasciata il giorno `gemini-2.0-flash-lite` una versione disponibile a livello generale (GA) di
  [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#gemini-2.0-flash-lite),
  ottimizzata per velocità, scalabilità ed efficienza in termini di costi.

## 19 febbraio 2025

**Aggiornamenti di AI Studio:**

- Supporto per
  [regioni aggiuntive](https://ai.google.dev/gemini-api/docs/available-regions?hl=it)
  (Kosovo, Groenlandia e Isole Fær Øer).

**Aggiornamenti dell'API:**

- Supporto per
  [regioni aggiuntive](https://ai.google.dev/gemini-api/docs/available-regions?hl=it)
  (Kosovo, Groenlandia e Isole Fær Øer).

## 18 febbraio 2025

**Aggiornamenti del modello:**

- Gemini 1.0 Pro non è più supportato. Per l'elenco dei modelli supportati, consulta
  [Modelli Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it).

## 11 febbraio 2025

**Aggiornamenti dell'API:**

- Aggiornamenti sulla
  [compatibilità delle librerie OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=it).

## 6 febbraio 2025

**Aggiornamenti del modello:**

- È stata rilasciata il giorno `imagen-3.0-generate-002` una versione disponibile a livello generale (GA) di
  [Imagen 3 nell'API Gemini](https://ai.google.dev/gemini-api/docs/imagen?hl=it).

**Aggiornamenti dell'SDK:**

- È stato rilasciato l'[SDK Google Gen AI per Java](https://github.com/googleapis/java-genai)
  per l'anteprima pubblica.

## 5 febbraio 2025

**Aggiornamenti del modello:**

- Rilasciata il giorno `gemini-2.0-flash-001` una versione con disponibilità generale (GA) di
  [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#gemini-2.0-flash) che
  supporta l'output di solo testo.
- Rilasciata il giorno `gemini-2.0-pro-exp-02-05`,
  una versione di anteprima
  pubblica [sperimentale](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=it) di Gemini 2.0 Pro.
- È stato rilasciato `gemini-2.0-flash-lite-preview-02-05`, un [modello](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#gemini-2.0-flash-lite) sperimentale in anteprima pubblica ottimizzato per l'efficienza dei costi.

**Aggiornamenti dell'API:**

- È stato aggiunto il supporto
  [dell'input di file e dell'output di grafici](https://ai.google.dev/gemini-api/docs/code-execution?hl=it#input-output)
  all'esecuzione del codice.

**Aggiornamenti dell'SDK:**

- È stata rilasciata la
  [SDK Google Gen AI per Python](https://googleapis.github.io/python-genai/)
  in disponibilità generale (GA).

## 21 gennaio 2025

**Aggiornamenti del modello:**

- Rilasciata il giorno `gemini-2.0-flash-thinking-exp-01-21`, l'ultima versione di anteprima del modello alla base del [modello Gemini 2.0 Flash Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=it).

## 19 dicembre 2024

**Aggiornamenti del modello:**

- È stata rilasciata la modalità Gemini 2.0 Flash Thinking per l'anteprima pubblica. La modalità di pensiero è
  un modello di calcolo in fase di test che ti consente di vedere il processo di pensiero del modello
  mentre genera una risposta e produce risposte con capacità di ragionamento
  più solide.

  Scopri di più sulla modalità Flash Thinking di Gemini 2.0 nella nostra [pagina di panoramica](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=it).

## 11 dicembre 2024

**Aggiornamenti del modello:**

- È stato rilasciato [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#gemini-2.0-flash)
  per l'anteprima pubblica. L'elenco parziale delle funzionalità di Gemini 2.0 Flash Experimental include:
  - Due volte più veloce di Gemini 1.5 Pro
  - Streaming bidirezionale con la nostra API Live
  - Generazione di risposte multimodali sotto forma di testo, immagini e voce
  - Utilizzo di strumenti integrati con il ragionamento multi-turn per utilizzare funzionalità come l'esecuzione di codice, la ricerca, la chiamata di funzione e altro ancora

Scopri di più su Gemini 2.0 Flash nella nostra [pagina
di panoramica](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=it).

## 21 novembre 2024

**Aggiornamenti del modello:**

- È stato rilasciato `gemini-exp-1121`, un modello sperimentale dell'API Gemini ancora più potente.

**Aggiornamenti del modello:**

- Aggiornati gli alias dei modelli `gemini-1.5-flash-latest` e `gemini-1.5-flash`
  per utilizzare `gemini-1.5-flash-002`.
  - Modifica del parametro `top_k`: il modello `gemini-1.5-flash-002`
    supporta valori `top_k` compresi tra 1 e 41 (esclusi).
    I valori superiori a 40 verranno modificati in 40.

## 14 novembre 2024

**Aggiornamenti del modello:**

- È stato rilasciato `gemini-exp-1114`, un potente modello sperimentale dell'API Gemini.

## 8 novembre 2024

**Aggiornamenti dell'API:**

- Aggiunto il [supporto di Gemini](https://ai.google.dev/gemini-api/docs/openai?hl=it) nelle librerie OpenAI / API REST.

## 31 ottobre 2024

**Aggiornamenti dell'API:**

- È stato aggiunto il [supporto per il grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/grounding?hl=it).

## 3 ottobre 2024

**Aggiornamenti del modello:**

- Rilasciata il giorno `gemini-1.5-flash-8b-001`, una versione stabile del nostro modello di API Gemini più piccolo.

## 24 settembre 2024

**Aggiornamenti del modello:**

- Sono state rilasciate `gemini-1.5-pro-002` e `gemini-1.5-flash-002`, due nuove versioni stabili
  di Gemini 1.5 Pro e 1.5 Flash, per la disponibilità generale.
- È stato aggiornato il codice del modello `gemini-1.5-pro-latest` per utilizzare `gemini-1.5-pro-002`
  e il codice del modello `gemini-1.5-flash-latest` per utilizzare `gemini-1.5-flash-002`.
- Rilasciato `gemini-1.5-flash-8b-exp-0924` per sostituire `gemini-1.5-flash-8b-exp-0827`.
- È stato rilasciato il [filtro di sicurezza per l'integrità civica](https://ai.google.dev/gemini-api/docs/safety-settings?hl=it#safety-filters)
  per l'API Gemini e AI Studio.
- È stato rilasciato il supporto per due nuovi parametri per Gemini 1.5 Pro e 1.5 Flash in
  Python e NodeJS:
  [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=it#FIELDS.frequency_penalty) e
  [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=it#FIELDS.presence_penalty).

## 19 settembre 2024

**Aggiornamenti di AI Studio:**

- Sono stati aggiunti i pulsanti Mi piace e Non mi piace alle risposte del modello per consentire agli utenti di
  fornire un feedback sulla qualità di una risposta.

**Aggiornamenti dell'API:**

- È stato aggiunto il supporto per i crediti Google Cloud, che ora possono essere utilizzati per
  l'utilizzo dell'API Gemini.

## 17 settembre 2024

**Aggiornamenti di AI Studio:**

- È stato aggiunto un pulsante **Apri in Colab** che esporta un prompt e il codice per eseguirlo in un notebook Colab. La funzionalità non supporta ancora
  i prompt con strumenti (modalità JSON, chiamata di funzione o esecuzione del codice).

## 13 settembre 2024

**Aggiornamenti di AI Studio:**

- È stato aggiunto il supporto della modalità di confronto, che consente di confrontare le risposte di modelli e prompt per trovare la soluzione migliore per il tuo caso d'uso.

## 30 agosto 2024

**Aggiornamenti del modello:**

- Gemini 1.5 Flash supporta
  [la fornitura di schemi JSON tramite la configurazione del modello](https://ai.google.dev/gemini-api/docs/json-mode?hl=it#supply-schema-in-config).

## 27 agosto 2024

**Aggiornamenti del modello:**

- Sono stati rilasciati i seguenti
  [modelli sperimentali](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=it):
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## 9 agosto 2024

**Aggiornamenti dell'API:**

- È stato aggiunto il supporto per l'[elaborazione dei PDF](https://ai.google.dev/gemini-api/docs/document-processing?hl=it).

## 5 agosto 2024

**Aggiornamenti del modello:**

- È stato rilasciato il supporto per il fine-tuning per Gemini 1.5 Flash.

## 1° agosto 2024

**Aggiornamenti del modello:**

- È stata rilasciata `gemini-1.5-pro-exp-0801`, una nuova versione sperimentale di
  [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#gemini-1.5-pro).

## 12 luglio 2024

**Aggiornamenti del modello:**

- Supporto per Gemini 1.0 Pro Vision rimosso dai servizi e dagli strumenti di Google AI.

## 27 giugno 2024

**Aggiornamenti del modello:**

- Rilascio della disponibilità generale della finestra contestuale da 2 milioni di token di Gemini 1.5 Pro.

**Aggiornamenti dell'API:**

- È stato aggiunto il supporto per l'[esecuzione del codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it).

## 18 giugno 2024

**Aggiornamenti dell'API:**

- È stato aggiunto il supporto per la [memorizzazione nella cache del contesto](https://ai.google.dev/gemini-api/docs/caching?hl=it).

## 12 giugno 2024

**Aggiornamenti del modello:**

- Gemini 1.0 Pro Vision è stato ritirato.

## 23 maggio 2024

**Aggiornamenti del modello:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#gemini-1.5-pro)
  (`gemini-1.5-pro-001`) è disponibile a livello generale (GA).
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#gemini-1.5-flash)
  (`gemini-1.5-flash-001`) è disponibile pubblicamente (GA).

## 14 maggio 2024

**Aggiornamenti dell'API:**

- È stata introdotta una finestra contestuale di 2 milioni di token per Gemini 1.5 Pro (lista di attesa).
- È stata introdotta la [fatturazione](https://ai.google.dev/gemini-api/docs/billing?hl=it) con pagamento a consumo per Gemini 1.0 Pro, mentre la fatturazione per Gemini 1.5 Pro e Gemini 1.5 Flash sarà disponibile a breve.
- Sono stati introdotti limiti di frequenza più elevati per il futuro livello a pagamento di Gemini 1.5
  Pro.
- Aggiunto il supporto video integrato all'[API File](https://ai.google.dev/api/rest/v1beta/files?hl=it).
- Aggiunto il supporto del testo normale all'[API File](https://ai.google.dev/api/rest/v1beta/files?hl=it).
- È stato aggiunto il supporto per la chiamata di funzioni parallela, che restituisce più di una
  chiamata alla volta.

## 10 maggio 2024

**Aggiornamenti del modello:**

- È stato rilasciato [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#gemini-1.5-flash)
  (`gemini-1.5-flash-latest`) in anteprima.

## 9 aprile 2024

**Aggiornamenti del modello:**

- È stato rilasciato [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#gemini-1.5-pro)
  (`gemini-1.5-pro-latest`) in anteprima.
- È stato rilasciato un nuovo modello di text embedding, `text-embeddings-004`, che supporta
  [l'embedding elastico](https://ai.google.dev/gemini-api/docs/embeddings?hl=it#elastic-embedding)
  con dimensioni inferiori a 768.

**Aggiornamenti dell'API:**

- È stata rilasciata l'[API File](https://ai.google.dev/api/rest/v1beta/files?hl=it) per l'archiviazione temporanea
  di file multimediali da utilizzare nei prompt.
- È stato aggiunto il supporto per i prompt con dati di testo, immagini e audio, noti anche come prompt *multimodali*. Per scoprire di più, consulta
  [Prompt con contenuti multimediali](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=it).
- Sono state rilasciate le [istruzioni di sistema](https://ai.google.dev/gemini-api/docs/system-instructions?hl=it) in
  versione beta.
- È stata aggiunta la
  [modalità di chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#function_calling_mode),
  che definisce il comportamento di esecuzione per la chiamata di funzione.
- È stato aggiunto il supporto per l'opzione di configurazione `response_mime_type`, che consente di richiedere risposte in [formato JSON](https://ai.google.dev/gemini-api/docs/api-overview?hl=it#json).

## 19 marzo 2024

**Aggiornamenti del modello:**

- Aggiunto il supporto per
  [l'ottimizzazione di Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/)
  in Google AI Studio o con l'API Gemini.

## 13 dicembre 2023

**Aggiornamenti del modello:**

- gemini-pro: nuovo modello di testo per un'ampia gamma di attività. Equilibra capacità ed efficienza.
- gemini-pro-vision: nuovo modello multimodale per un'ampia gamma di attività.
  Equilibra capacità ed efficienza.
- embedding-001: Nuovo modello di embedding.
- aqa: Un nuovo modello appositamente ottimizzato e addestrato per rispondere alle domande
  utilizzando passaggi di testo per basare le risposte generate.

Per ulteriori dettagli, consulta la sezione [Modelli Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it).

**Aggiornamenti della versione dell'API:**

- v1: Il canale API stabile.
- v1beta: canale beta. Questo canale ha funzionalità che potrebbero essere in fase di
  sviluppo.

Per ulteriori dettagli, consulta l'[argomento sulle versioni dell'API](https://ai.google.dev/gemini-api/docs/api-versions?hl=it).

**Aggiornamenti dell'API:**

- `GenerateContent` è un unico endpoint unificato per chat e messaggi.
- Streaming disponibile tramite il metodo `StreamGenerateContent`.
- Funzionalità multimodale: l'immagine è una nuova modalità supportata
- Nuove funzionalità beta:
  - [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)
  - [Semantic Retriever](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=it)
  - Question Answering con attribuzione (AQA)
- Conteggio dei candidati aggiornato: i modelli Gemini restituiscono un solo candidato.
- Diverse impostazioni di sicurezza e categorie di classificazione di sicurezza. Per maggiori dettagli, consulta le
  [impostazioni di sicurezza](https://ai.google.dev/gemini-api/docs/safety-settings?hl=it).
- L'ottimizzazione dei modelli non è ancora supportata per i modelli Gemini (in corso).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-12 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-12 UTC."],[],[]]
