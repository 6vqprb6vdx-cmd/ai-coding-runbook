---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=it
fetched_at: 2026-08-17T02:17:07.573214+00:00
title: "Log e set di dati \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Log e set di dati

In questa guida imparerai a
visualizzare i log dell'utilizzo dell'API Gemini nella dashboard di Google AI Studio
per comprendere meglio il comportamento del modello e il modo in cui gli utenti potrebbero interagire con le tue
applicazioni. Utilizza la registrazione per osservare, eseguire il debug e *condividere facoltativamente il feedback sull'utilizzo
con Google per contribuire a migliorare Gemini in vari casi d'uso per gli sviluppatori*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=it)

Sono supportate tutte le chiamate API `GenerateContent`, `BatchGenerateContent`, `StreamGenerateContent` e le chiamate API [Interazioni](https://ai.google.dev/gemini-api/docs/interactions?hl=it), escluse quelle degli agenti gestiti. Sono incluse le chiamate effettuate tramite
endpoint di [compatibilità con OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=it).

## Configurare la registrazione del progetto

Per impostazione predefinita, l'API archivia tutti gli oggetti di interazione (`store=true`) per semplificare l'utilizzo delle funzionalità di gestione dello stato lato server. Al contrario, l'API
Generate Content non archivia le richieste per impostazione predefinita e richiede l'attivazione dell'archiviazione
per richiesta o a livello di progetto da AI Studio.

In Google [AI Studio](https://aistudio.google.com/logs?hl=it) puoi attivare o disattivare la registrazione per tutti i progetti o per progetti specifici e modificare queste preferenze in qualsiasi momento tramite il pannello **Impostazioni** nella pagina [Log e set di dati](https://aistudio.google.com/logs?hl=it). La registrazione può essere attivata o disattivata
in modo indipendente per l'API `generateContent` e l'API
[Interazioni](https://ai.google.dev/gemini-api/docs/interactions?hl=it)
per modificare il comportamento di archiviazione predefinito per un progetto.

### Logging a livello di richiesta

Il comportamento di archiviazione e logging varia a seconda dell'API:

- **[API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=it):** memorizza le richieste per impostazione predefinita (`store=true`) per semplificare la gestione dello stato lato server.
- **Genera API Content (`generateContent`):** per impostazione predefinita non memorizza le richieste (`store=false`).

Ecco come impostare la proprietà `store`:

**API GenerateContent**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

**API Interactions**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

## Visualizzare i log del progetto in AI Studio

1. Vai alla pagina Log in [AI Studio](https://aistudio.google.com/logs?hl=it).
2. Seleziona un progetto dal menu a discesa.
3. Se esistono, i log vengono visualizzati nella tabella in ordine cronologico inverso per l'API Interactions.
4. Per osservare i log del progetto per l'API Content, devi prima abilitarla nel [pannello delle impostazioni](#configure-logging).

Fai clic su una voce per visualizzare un'anteprima del payload. Puoi
esaminare il prompt e la risposta completi di Gemini, nonché il contesto dei
turni precedenti. Per le richieste dell'**API Interactions**, i log includono anche un link diretto
al `previous_interaction_id`.

## Configura la conservazione dello spazio di archiviazione del progetto

I log scadranno e verranno contrassegnati per l'eliminazione dopo un periodo di conservazione predefinito di
55 giorni (a meno che non vengano [salvati in un set di dati](#create), che non scadono).
Puoi configurare la finestra di conservazione dei log di un progetto su un massimo di 7, 14, 28 o 55 giorni.

## Creare e condividere set di dati

Puoi salvare i log nei set di dati per organizzarli ed esportarli in modo più efficace.

- Nella [pagina Log](https://aistudio.google.com/logs?hl=it), individua la barra dei filtri
  in alto per selezionare una proprietà in base alla quale filtrare.
- Dalla visualizzazione filtrata, utilizza le caselle di controllo per selezionare tutti i log o i singoli log.
- Fai clic sul pulsante **Crea set di dati** visualizzato nella parte superiore dell'elenco.
- Assegna un nome e una descrizione facoltativa al nuovo set di dati.
- Vedrai il set di dati appena creato con il set di log selezionato.
- Esporta il set di dati per un'ulteriore analisi come file CSV, JSONL o in Fogli Google.

I set di dati possono essere utili per una serie di casi d'uso diversi.

- **Crea set di sfide**:promuovi miglioramenti futuri che prendano di mira le aree in cui vuoi che la tua AI migliori.
- **Crea set di campioni**:ad esempio, un campione di utilizzo reale per generare risposte da un altro modello o una raccolta di casi limite per i controlli di routine prima del deployment.
- **Set di valutazione**:set rappresentativi dell'utilizzo reale delle funzionalità importanti, per il confronto con altri modelli o iterazioni delle istruzioni di sistema.

Puoi contribuire alla ricerca e allo sviluppo di Gemini scegliendo di condividere
i tuoi set di dati con Google come esempi dimostrativi.

## Limitazioni

La registrazione non è attualmente supportata per quanto segue:

- Modelli Imagen e Veo
- Modelli di embedding Gemini
- Modello Gemini Robotics
- Input contenenti video, GIF o PDF
- Agenti in anteprima pubblica nell'API Gemini

## Passaggi successivi

- **Prototipo con la cronologia della sessione**:utilizza [AI Studio Build](https://aistudio.google.com/apps?hl=it) per creare app di codice e aggiungere la chiave API per attivare una cronologia dei log dell'API Gemini per le funzionalità di AI.
- **Esegui di nuovo i log con l'API Gemini Batch:** utilizza i set di dati per il campionamento delle risposte e la valutazione dei modelli o della logica dell'applicazione eseguendo di nuovo i log con l'[API Gemini Batch](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-22 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-22 UTC."],[],[]]
