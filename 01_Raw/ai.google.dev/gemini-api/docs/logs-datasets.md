---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=it
fetched_at: 2026-06-29T05:34:29.750013+00:00
title: "Log e set di dati \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Log e set di dati

Questa guida contiene tutto il necessario per iniziare ad abilitare la registrazione per le applicazioni API Gemini esistenti. In questa guida imparerai a visualizzare i log di un'applicazione esistente o nuova nella dashboard di Google AI Studio per comprendere meglio il comportamento del modello e il modo in cui gli utenti potrebbero interagire con le tue applicazioni. Utilizza la registrazione per osservare, eseguire il debug e *facoltativamente condividere il feedback sull'utilizzo
con Google per contribuire a migliorare Gemini in tutti i casi d'uso degli sviluppatori*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=it)

Sono supportate tutte le chiamate API `GenerateContent` e `StreamGenerateContent`,
incluse quelle effettuate tramite gli endpoint di compatibilità di [OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=it).

## 1. Abilitare la registrazione in Google AI Studio

Prima di iniziare, assicurati di avere un progetto di tua proprietà con la fatturazione abilitata.

1. Apri la pagina dei log in Google [AI Studio](https://aistudio.google.com/logs?hl=it).
2. Scegli il progetto dal menu a discesa e premi il pulsante di attivazione per abilitare la registrazione per tutte le richieste per impostazione predefinita.

![](https://ai.google.dev/static/gemini-api/docs/images/logs-state.png?hl=it)

Puoi attivare o disattivare la registrazione per tutti i progetti o per progetti specifici e modificare queste preferenze in qualsiasi momento tramite Google AI Studio.

## 2. Visualizzare i log in AI Studio

1. Vai ad [AI Studio](https://aistudio.google.com/logs?hl=it).
2. Seleziona il progetto per cui hai abilitato la registrazione.
3. Dovresti vedere i log visualizzati nella tabella in ordine cronologico inverso.

![](https://storage.googleapis.com/generativeai-downloads/images/nano-banana-logs.gif)

Fai clic su una voce per visualizzare la coppia richiesta-risposta in una visualizzazione di pagina intera. Puoi esaminare il prompt completo, la risposta completa di Gemini e il contesto del turno precedente. Tieni presente che ogni progetto ha un limite di spazio di archiviazione predefinito di un massimo di 1000 log e che i log non salvati nei set di dati scadranno dopo 55 giorni. Se il tuo progetto raggiunge il limite di spazio di archiviazione, ti verrà chiesto di eliminare i log.

## 3. Selezionare e condividere i set di dati

- Nella tabella dei log, individua la barra dei filtri in alto per selezionare una proprietà in base alla quale filtrare.
- Nella visualizzazione filtrata dei log, utilizza le caselle di controllo per selezionare tutti o alcuni log.
- Fai clic sul pulsante "Crea set di dati" visualizzato nella parte superiore dell'elenco.
- Assegna al nuovo set di dati un nome descrittivo e una descrizione facoltativa.
- Verrà visualizzato il set di dati appena creato con il set di log selezionato.
- Esporta il set di dati per ulteriori analisi come file CSV, JSONL o in Fogli Google.

![](https://storage.googleapis.com/generativeai-downloads/images/sales-dataset.gif)

I set di dati possono essere utili per diversi casi d'uso.

- **Selezionare set di sfide:** promuovi miglioramenti futuri che riguardano le aree in cui vuoi che la tua AI migliori.
- **Selezionare set di esempi:** ad esempio, un campione di utilizzo reale per generare risposte da un altro modello o una raccolta di casi limite per i controlli di routine prima del deployment.
- **Set di valutazione:** set rappresentativi dell'utilizzo reale in tutte le funzionalità importanti, per il confronto tra altri modelli o iterazioni delle istruzioni di sistema.

Puoi contribuire a promuovere i progressi nella ricerca sull'AI, nell'API Gemini e in Google AI Studio scegliendo di condividere i tuoi set di dati come esempi dimostrativi. In questo modo possiamo perfezionare i nostri modelli in contesti diversi e creare sistemi di AI che rimangano utili agli sviluppatori in molti campi e applicazioni.

## Passaggi successivi e cosa testare

Ora che hai abilitato la registrazione, ecco alcune cose da provare:

- **Creare prototipi con la cronologia delle sessioni:** utilizza [AI Studio Build](https://aistudio.google.com/apps?hl=it) per creare app di codice e aggiungi la chiave API per abilitare una cronologia dei log utente.
- **Eseguire di nuovo i log con l'API Gemini Batch:** utilizza i set di dati per il campionamento delle risposte
  e la valutazione dei modelli o della logica dell'applicazione eseguendo di nuovo i log tramite l'API
  [Gemini Batch](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

## Compatibilità

Al momento, la registrazione non è supportata per:

- Modelli Imagen e Veo
- Modello di incorporamento Gemini
- Input contenenti video, GIF o PDF

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-01 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-01 UTC."],[],[]]
