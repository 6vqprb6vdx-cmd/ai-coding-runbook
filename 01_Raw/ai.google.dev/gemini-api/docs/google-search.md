---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=it
fetched_at: 2026-08-17T02:23:24.942140+00:00
title: "Grounding con la Ricerca Google \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Grounding con la Ricerca Google

Grounding con la Ricerca Google collega il modello Gemini ai contenuti web in tempo reale e funziona con tutte le lingue disponibili. In questo modo, Gemini può fornire risposte più accurate e citare fonti verificabili aggiornate rispetto al suo knowledge cutoff.

Il grounding ti aiuta a creare applicazioni che possono:

- **Aumentare l'accuratezza fattuale:** ridurre le allucinazioni del modello basando le risposte su informazioni del mondo reale.
- **Accedere a informazioni in tempo reale:** rispondere a domande su eventi e argomenti recenti.
- **Fornire citazioni:** creare fiducia negli utenti mostrando le fonti delle affermazioni del modello.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## Come funziona il grounding con la Ricerca Google

Quando abiliti lo strumento `google_search`, il modello gestisce automaticamente l'intero flusso di lavoro di ricerca, elaborazione e citazione delle informazioni.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=it)

1. **Prompt dell'utente:** la tua applicazione invia un prompt dell'utente all'API Gemini con lo strumento `google_search` abilitato.
2. **Analisi del prompt:** il modello analizza il prompt e determina se una Ricerca Google può migliorare la risposta.
3. **Ricerca Google:** se necessario, il modello genera ed esegue automaticamente una o più query di ricerca.
4. **Elaborazione dei risultati di ricerca:** il modello elabora i risultati di ricerca, sintetizza le informazioni e formula una risposta.
5. **Risposta con grounding:** l'API restituisce una risposta finale e di facile utilizzo basata sui risultati di ricerca. Questa risposta include la risposta di testo del modello con `annotations` in linea contenenti le citazioni, nonché i passaggi `google_search_call` e `google_search_result` con le query di ricerca e i suggerimenti di ricerca.

## Informazioni sulla risposta con grounding

Quando una risposta viene basata correttamente, l'output di testo del modello include `annotations` in linea direttamente nel blocco di contenuti di testo. Queste annotazioni forniscono informazioni sulle citazioni che collegano parti della risposta alle relative fonti.

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

I campi chiave nella risposta:

- `google_search_call` : contiene le `queries` di ricerca eseguite dal modello.
- `google_search_result` : contiene `search_suggestions`, uno snippet HTML per il rendering dei suggerimenti di ricerca nell'interfaccia utente. I requisiti di utilizzo completi sono
  descritti nei [Termini di servizio](https://ai.google.dev/gemini-api/terms?hl=it#grounding-with-google-search).
- `text` con `annotations` : la risposta sintetizzata del modello con citazioni in linea. Ogni annotazione `url_citation` collega un segmento di testo (definito da `start_index` e `end_index`) a un URL di origine. Questo è il modo principale per creare citazioni in linea.

Il grounding con la Ricerca Google può essere utilizzato anche in combinazione con lo strumento di contesto [URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it) per basare le risposte sia sui dati web pubblici sia sugli URL specifici che fornisci.

## Attribuzione delle fonti con citazioni in linea

L'API restituisce annotazioni `url_citation` in linea nel blocco di contenuti di testo, offrendoti il controllo completo sulla modalità di visualizzazione delle fonti nell'interfaccia utente.
Ogni annotazione include `start_index` e `end_index` per identificare la parte di testo che cita. Ecco come estrarli e visualizzarli.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

L'output mostrerà il testo seguito dalle relative citazioni:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## Prezzi

Quando utilizzi il grounding con la Ricerca Google con Gemini 3, al tuo progetto vengono addebitate le query di ricerca che il modello decide di eseguire. Se il modello decide di
eseguire più query di ricerca per rispondere a un singolo prompt (ad esempio,
cercando `"UEFA Euro 2024 winner"` e `"Spain vs England Euro 2024 final
score"` nella stessa chiamata API), questo viene considerato come due utilizzi fatturabili dello strumento
per quella richiesta. Ai fini della fatturazione, ignoriamo le query di ricerca web vuote quando contiamo le query univoche. Questo modello di fatturazione si applica solo ai modelli Gemini 3; quando utilizzi il grounding di ricerca con Gemini 2.5 o modelli precedenti, al tuo progetto viene addebitato un costo per prompt.

Per informazioni dettagliate sui prezzi, consulta la [pagina dei prezzi dell'API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=it).

## Modelli supportati

Puoi trovare le funzionalità complete nella pagina di panoramica del [modello](https://ai.google.dev/gemini-api/docs/models?hl=it).

| Modello | Grounding con la Ricerca Google |
| --- | --- |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash Image Preview | ✔️ |
| Gemini 3.1 Pro (anteprima) | ✔️ |
| Gemini 3 Pro Image Preview | ✔️ |
| Gemini 3 Flash (anteprima) | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Combinazioni di strumenti supportate

Puoi utilizzare il grounding con la Ricerca Google con altri strumenti come
[l'esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it) e
[il contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it) per supportare casi d'uso più complessi.

I modelli Gemini 3 supportano la combinazione di strumenti integrati (come il grounding con la Ricerca Google) con strumenti personalizzati (chiamata di funzione). Scopri di più nella pagina delle
[combinazioni di strumenti](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it).

## Passaggi successivi

- Scopri di più sugli altri strumenti disponibili, come [la chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it).
- Scopri come aumentare i prompt con URL specifici utilizzando lo [strumento di contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
