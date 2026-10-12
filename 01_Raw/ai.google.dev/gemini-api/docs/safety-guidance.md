---
source_url: https://ai.google.dev/gemini-api/docs/safety-guidance?hl=it
fetched_at: 2026-10-12T06:58:52.087285+00:00
title: "Linee guida su sicurezza e accuratezza \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Linee guida su sicurezza e accuratezza

I modelli di intelligenza artificiale generativa sono strumenti potenti, ma non sono privi di limitazioni. La loro versatilità e applicabilità a volte possono portare a output imprevisti, ad esempio output imprecisi, con bias o offensivi. La post-elaborazione e una rigorosa valutazione manuale sono essenziali per limitare il rischio di danni derivanti da questi output.

I modelli forniti dall'API Gemini possono essere utilizzati per un'ampia varietà di applicazioni di AI generativa ed elaborazione del linguaggio naturale (NLP). L'utilizzo di queste
funzioni è disponibile solo tramite l'API Gemini o l'app web
Google AI Studio. L'utilizzo dell'API Gemini è soggetto anche alle [Norme relative all'uso vietato dell'AI generativa
Policy](https://policies.google.com/terms/generative-ai/use-policy?hl=it) e ai
[Termini di servizio dell'API Gemini](https://ai.google.dev/terms?hl=it).

Parte di ciò che rende i modelli linguistici di grandi dimensioni (LLM) così utili è che sono strumenti creativi in grado di gestire molte attività linguistiche diverse. Purtroppo, questo significa anche che i modelli linguistici di grandi dimensioni possono generare output imprevisti, inclusi testi offensivi, insensibili o oggettivamente scorretti.
Inoltre, l'incredibile versatilità di questi modelli è anche ciò che rende difficile prevedere esattamente i tipi di output indesiderati che potrebbero produrre. Sebbene l'
API Gemini sia stata progettata tenendo conto dei [principi di AI
di Google](https://ai.google/principles/?hl=it), è responsabilità degli sviluppatori
applicare questi modelli in modo responsabile. Per aiutare gli sviluppatori a creare applicazioni sicure e responsabili, l'API Gemini include alcuni filtri dei contenuti integrati, nonché impostazioni di sicurezza regolabili su 4 dimensioni di danno. Per saperne di più, consulta la
[guida alle impostazioni di sicurezza](https://ai.google.dev/gemini-api/docs/safety-settings?hl=it). Offre anche la funzionalità Grounding con la Ricerca Google abilitata per migliorare l'accuratezza dei fatti, anche se questa funzionalità può essere disattivata per gli sviluppatori i cui casi d'uso sono più creativi e non orientati alla ricerca di informazioni.

Questo documento ha lo scopo di presentarti alcuni rischi per la sicurezza che possono sorgere quando utilizzi i modelli LLM e di consigliarti le nuove raccomandazioni per la progettazione e lo sviluppo della sicurezza. (Tieni presente che anche le leggi e le normative possono imporre restrizioni, ma queste considerazioni esulano dall'ambito di questa guida.)

Quando crei applicazioni con modelli LLM, ti consigliamo di seguire questi passaggi:

- Comprendere i rischi per la sicurezza della tua applicazione
- Valutare le modifiche per mitigare i rischi per la sicurezza
- Eseguire test di sicurezza appropriati per il tuo caso d'uso
- Richiedere feedback agli utenti e monitorare l'utilizzo

Le fasi di regolazione e test devono essere iterative fino a raggiungere un rendimento appropriato per la tua applicazione.

![Ciclo di implementazione del modello](https://ai.google.dev/static/gemini-api/docs/images/safety_diagram.png?hl=it)

## Comprendere i rischi per la sicurezza della tua applicazione

In questo contesto, la sicurezza è definita come la capacità di un modello LLM di evitare di causare danni ai suoi utenti, ad esempio generando un linguaggio tossico o contenuti che promuovono stereotipi. I modelli disponibili tramite l'API Gemini sono stati progettati tenendo conto dei [principi dell'AI di Google](https://ai.google/principles/?hl=it) e il loro utilizzo è soggetto alle [Norme relative all'uso vietato dell'IA generativa](https://policies.google.com/terms/generative-ai/use-policy?hl=it). L'API fornisce filtri di sicurezza integrati per risolvere alcuni problemi comuni dei modelli linguistici, come il linguaggio tossico e i discorsi di incitamento all'odio, e si impegna a garantire l'inclusività e a evitare gli stereotipi. Tuttavia, ogni applicazione può comportare una serie diversa di rischi per i suoi utenti. Pertanto, in qualità di proprietario dell'applicazione, hai la responsabilità di conoscere i tuoi utenti e i potenziali danni che la tua applicazione potrebbe causare, nonché di assicurarti che la tua applicazione utilizzi i modelli LLM in modo sicuro e responsabile.

Nell'ambito di questa valutazione, devi considerare la probabilità che si verifichino danni, determinarne la gravità e i passaggi di mitigazione. Ad esempio, un'app che genera saggi basati su eventi reali dovrà prestare maggiore attenzione a evitare la disinformazione rispetto a un'app che genera storie di fantasia per l'intrattenimento. Un buon modo per iniziare a esplorare i potenziali rischi per la sicurezza è quello di fare ricerche sugli utenti finali e su altre persone che potrebbero essere interessate dai risultati della tua applicazione. Questa operazione può assumere molte forme, tra cui la ricerca di studi all'avanguardia nel dominio della tua app, l'osservazione di come le persone utilizzano app simili o l'esecuzione di uno studio utente, un sondaggio o interviste informali con potenziali utenti.

### Suggerimenti avanzati

- Parla con un mix diversificato di potenziali utenti all'interno della tua popolazione target della tua applicazione e del suo scopo previsto per ottenere una prospettiva più ampia sui potenziali rischi e per modificare i criteri di diversità, se necessario.
- Il [framework di gestione del rischio AI](https://www.nist.gov/itl/ai-risk-management-framework)
  pubblicato dal
  National Institute of Standards and Technology (NIST) del governo statunitense fornisce indicazioni più
  dettagliate e risorse di apprendimento aggiuntive per la gestione del rischio AI.
- La pubblicazione di DeepMind sui
  [rischi etici e sociali di danni derivanti dai modelli linguistici](https://arxiv.org/abs/2112.04359)
  descrive in dettaglio i modi in cui le applicazioni dei modelli linguistici
  possono causare danni.

## Valutare le modifiche per mitigare i rischi per la sicurezza e l'accuratezza dei fatti

Ora che hai compreso i rischi, puoi decidere come mitigarli. Determinare a quali rischi dare la priorità e quanto dovresti fare per cercare di prevenirli è una decisione fondamentale, simile alla gestione delle priorità dei bug in un progetto software. Una volta determinate le priorità, puoi iniziare a pensare ai tipi di mitigazioni più appropriati. Spesso, semplici modifiche possono fare la differenza e ridurre i rischi.

Ad esempio, quando progetti un'applicazione, considera:

- **Ottimizzare l'output del modello** per riflettere meglio ciò che è accettabile nel contesto dell'applicazione. L'ottimizzazione può rendere l'output del modello più prevedibile e coerente e, di conseguenza, può contribuire a mitigare alcuni rischi.
- **Fornire un metodo di input che faciliti gli output più sicuri.** L'input esatto che fornisci a un modello LLM può fare la differenza nella qualità dell'output.
  Vale la pena sperimentare con i prompt di input per trovare quelli che funzionano in modo più sicuro nel tuo caso d'uso, in modo da poter fornire un'esperienza utente che lo faciliti. Ad esempio, potresti limitare gli utenti a scegliere solo da un elenco a discesa di prompt di input oppure offrire suggerimenti popup con frasi descrittive che hai scoperto essere sicure nel contesto dell'applicazione.
- **Bloccare gli input non sicuri e filtrare l'output prima che venga mostrato all'utente.** In situazioni semplici, le liste bloccate possono essere utili per identificare e bloccare parole o frasi non sicure nei prompt o nelle risposte oppure richiedere ai revisori umani di modificare o bloccare manualmente questi contenuti.
- **Utilizzare classificatori addestrati per etichettare ogni prompt con potenziali danni o segnali contraddittori.** È poi possibile applicare varie strategie per gestire la richiesta in base al tipo di danno rilevato, ad esempio, se l'input è apertamente contraddittorio o di natura illecita, potrebbe essere bloccato e fornire una risposta preimpostata.
  **Suggerimento avanzato:** se i segnali determinano che l'output è dannoso, l'applicazione può utilizzare le seguenti opzioni:

  - Mostrare un messaggio di errore o generare un output preimpostato.
  - Riprovare con il prompt, nel caso in cui venga generato un output alternativo sicuro, poiché a volte lo stesso prompt genera output diversi.
- **Implementare misure di salvaguardia contro l'uso improprio intenzionale** , ad esempio assegnando a ogni utente un ID univoco e imponendo un limite al volume di query utente che possono essere inviate in un determinato periodo. Un'altra misura di salvaguardia consiste nel cercare di proteggersi da possibili prompt injection. Il prompt injection, proprio come l'SQL injection, è un modo per gli utenti malintenzionati di progettare un prompt di input che manipola l'output del modello, ad esempio inviando un prompt di input che indica al modello di ignorare eventuali esempi precedenti. Per i dettagli sull'uso improprio intenzionale, consulta le
  [Norme relative all'uso vietato dell'AI generativa](https://policies.google.com/terms/generative-ai/use-policy?hl=it).
- **Modificare la funzionalità in modo che sia intrinsecamente a rischio inferiore.**
  Le attività con un ambito più ristretto (ad es. l'estrazione di parole chiave da passaggi di testo) o che prevedono una maggiore supervisione umana (ad es. la generazione di contenuti di breve durata che verranno esaminati da una persona) spesso comportano un rischio inferiore. Ad esempio, anziché creare un'applicazione per scrivere una risposta email da zero, potresti limitarla all'espansione di una bozza o al suggerimento di formulazioni alternative.
- **Modificare le impostazioni di sicurezza dei contenuti dannosi per ridurre la probabilità di ricevere risposte potenzialmente dannose.** L'API Gemini fornisce impostazioni di sicurezza che puoi modificare durante la fase di prototipazione per determinare se la tua applicazione richiede una configurazione di sicurezza più o meno restrittiva. Puoi modificare queste impostazioni in cinque categorie di filtri per limitare o consentire determinati tipi di contenuti. Per scoprire di più sulle impostazioni di sicurezza regolabili disponibili tramite l'API Gemini, consulta la [guida alle impostazioni di sicurezza](https://ai.google.dev/gemini-api/docs/safety-settings?hl=it).
- **Ridurre le potenziali imprecisioni o allucinazioni fattuali attivando la funzionalità Grounding con la Ricerca Google**. Tieni presente che molti modelli di AI sono sperimentali e potrebbero presentare informazioni oggettivamente imprecise, allucinare o produrre output problematici. La funzionalità Grounding con la Ricerca Google collega il modello Gemini ai contenuti web in tempo reale e funziona con tutte le lingue disponibili. In questo modo, Gemini può fornire risposte più accurate e citare fonti verificabili aggiornate rispetto al knowledge cutoff dei modelli.

## Eseguire test di sicurezza appropriati per il tuo caso d'uso

I test sono una parte fondamentale della creazione di applicazioni robuste e sicure, ma l'estensione, l'ambito e le strategie di test variano. Ad esempio, un generatore di haiku per divertimento è probabile che comporti rischi meno gravi rispetto, ad esempio, a un'applicazione progettata per essere utilizzata da studi legali per riassumere documenti legali e aiutare a redigere contratti. Tuttavia, il generatore di haiku potrebbe essere utilizzato da una gamma più ampia di utenti, il che significa che il potenziale di tentativi contraddittori o persino di input dannosi non intenzionali può essere maggiore. Anche il contesto di implementazione è importante. Ad esempio, un'applicazione con output esaminati da esperti umani prima di intraprendere qualsiasi azione potrebbe essere considerata meno probabile di produrre output dannosi rispetto all'applicazione identica senza questa supervisione.

Non è raro dover apportare diverse modifiche ed eseguire diversi test prima di sentirsi sicuri di essere pronti per il lancio, anche per le applicazioni a rischio relativamente basso. Due tipi di test sono particolarmente utili per le applicazioni di AI:

- Il **benchmarking della sicurezza** prevede la progettazione di metriche di sicurezza che riflettano i modi in cui la tua applicazione potrebbe essere non sicura nel contesto del suo probabile utilizzo, quindi il test del rendimento dell'applicazione in base alle metriche utilizzando set di dati di valutazione. È buona norma pensare ai livelli minimi accettabili delle metriche di sicurezza prima di eseguire i test, in modo da 1) poter valutare i risultati dei test in base a queste aspettative e 2) poter raccogliere il set di dati di valutazione in base ai test che valutano le metriche a cui tieni di più.

  **Suggerimenti avanzati:**

  - Fai attenzione a non fare troppo affidamento sugli approcci "pronti all'uso", perché è probabile che dovrai creare i tuoi set di dati di test utilizzando valutatori umani per adattarli completamente al contesto della tua applicazione.
  - Se hai più di una metrica, dovrai decidere come scambiarle se una modifica comporta miglioramenti per una metrica a scapito di un'altra. Come per altre tecniche di ottimizzazione del rendimento, potresti voler concentrarti sul rendimento nel caso peggiore nel set di valutazione anziché sul rendimento medio.
- I **test contraddittori** prevedono di provare in modo proattivo a interrompere l'applicazione. L'obiettivo è identificare i punti deboli in modo da poter adottare le misure necessarie per risolverli. I test contraddittori possono richiedere molto tempo/impegno da parte dei valutatori esperti nella tua applicazione, ma più ne esegui, maggiori sono le probabilità di individuare i problemi, soprattutto quelli che si verificano raramente o solo dopo esecuzioni ripetute dell'applicazione.

  - I test contraddittori sono un metodo di valutazione sistematica di un modello di ML con l'intento di apprendere come si comporta quando gli viene fornito un input dannoso, inavvertitamente o intenzionalmente:
    - Un input può essere intenzionalmente dannoso quando è chiaramente progettato per produrre un output non sicuro o pericoloso, ad esempio chiedendo a un modello di generazione di testo di generare un discorso di incitamento all'odio nei confronti di una particolare religione.
    - Un input è inavvertitamente dannoso quando produce un output pericoloso pur essendo di per sé innocuo, ad esempio chiedendo a un modello di generazione di testo di descrivere una persona di un particolare gruppo etnico e ricevendo un output razzista.
  - Ciò che distingue un test contraddittorio da una valutazione standard è la composizione dei dati utilizzati per i test. Per i test contraddittori, seleziona
    i dati di test che hanno maggiori probabilità di generare output problematici da
    l modello. Ciò significa analizzare il comportamento del modello per tutti i tipi di danni possibili, inclusi esempi rari o insoliti e casi limite pertinenti alle norme di sicurezza. Deve inoltre includere la diversità nelle diverse dimensioni di una frase, come struttura, significato e lunghezza. Per ulteriori dettagli su cosa considerare quando crei un set di dati di test, consulta le pratiche di AI responsabile di [Google's Responsible AI
    in
    materia di](https://ai.google/responsibilities/responsible-ai-practices/?category=fairness&hl=it)
    equità.
    **Suggerimenti avanzati:**
  - Utilizza i [test automatici](https://www.deepmind.com/blog/red-teaming-language-models-with-language-models?hl=it)
    anziché il metodo tradizionale di coinvolgere persone in 'red
    team' per cercare di interrompere l'applicazione. Nei test automatici, il "red team" è un altro modello linguistico che trova il testo di input che genera output dannosi dal modello in fase di test.

## Monitorare i problemi

Indipendentemente dalla quantità di test e mitigazioni, non puoi mai garantire la perfezione, quindi pianifica in anticipo come individuare e risolvere i problemi che si presentano. Gli approcci comuni includono la configurazione di un canale monitorato in cui gli utenti possono condividere feedback (ad es. valutazione con pollice in su/in giù) e l'esecuzione di uno studio utente per richiedere in modo proattivo feedback da un mix diversificato di utenti, soprattutto se i pattern di utilizzo sono diversi dalle aspettative.

### Suggerimenti avanzati

- Quando gli utenti forniscono feedback sui prodotti di AI, nel tempo possono migliorare notevolmente il rendimento dell'AI e l'esperienza utente, ad esempio aiutandoti a scegliere esempi migliori per l'ottimizzazione dei prompt. Il
  [capitolo Feedback e controllo](https://pair.withgoogle.com/chapter/feedback-controls/)
  della [guida Persone e AI di Google](https://pair.withgoogle.com/guidebook/chapters)
  evidenzia le considerazioni chiave da tenere presenti durante la progettazione dei
  meccanismi di feedback.

## Passaggi successivi

- Per scoprire di più sulle impostazioni di sicurezza regolabili disponibili tramite l'API Gemini, consulta la
  [guida alle impostazioni di sicurezza](https://ai.google.dev/gemini-api/docs/safety-settings?hl=it).
- Per iniziare a scrivere i tuoi primi prompt, consulta l'[introduzione ai prompt](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=it) per iniziare.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-05 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-05 UTC."],[],[]]
