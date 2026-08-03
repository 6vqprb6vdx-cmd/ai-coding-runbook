---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=it
fetched_at: 2026-08-03T04:28:25.549602+00:00
title: "Errori API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Errori API

Questa pagina fornisce un riferimento per i codici di errore del backend restituiti dall'API `GenerateContent`, descrive il formato della risposta di errore gRPC e fornisce i passaggi per la risoluzione dei problemi.

## Codici di errore HTTP

La seguente tabella elenca i codici di errore del backend comuni, le spiegazioni delle cause e le soluzioni consigliate:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Codice HTTP** | **Stato** | **Descrizione** | **Esempio** | **Soluzione** |
| 400 | INVALID\_ARGUMENT | Il corpo della richiesta non è in un formato corretto. | Nella richiesta è presente un errore di battitura o manca un campo obbligatorio. | Consulta il [riferimento API](https://ai.google.dev/api?hl=it) per il formato della richiesta, gli esempi e le versioni supportate. L'utilizzo di funzionalità di una versione API più recente con un endpoint precedente può causare errori. |
| 400 | FAILED\_PRECONDITION | Il livello senza costi dell'API Gemini non è disponibile nel tuo paese. Attiva la fatturazione per il tuo progetto in Google AI Studio. | Stai effettuando una richiesta in una regione in cui il livello senza costi non è supportato e non hai attivato la fatturazione per il tuo progetto in Google AI Studio. | Per utilizzare l'API Gemini, devi configurare un piano a pagamento utilizzando [Google AI Studio](https://aistudio.google.com/apikey?hl=it). |
| 403 | PERMISSION\_DENIED | La tua chiave API non dispone delle autorizzazioni richieste. | Stai utilizzando la chiave API errata; stai tentando di utilizzare un modello ottimizzato senza eseguire [l'autenticazione corretta](https://ai.google.dev/gemini-api/docs/model-tuning?hl=it). | Verifica che la chiave API sia impostata e disponga dell'accesso corretto. Assicurati di eseguire l'autenticazione corretta per utilizzare i modelli ottimizzati. |
| 404 | NOT\_FOUND | La risorsa richiesta non è stata trovata. | Non è stato trovato un file immagine, audio o video a cui viene fatto riferimento nella richiesta. | Verifica che tutti i parametri della richiesta siano validi per la tua versione API. |
| 429 | RESOURCE\_EXHAUSTED | Hai superato uno dei limiti di frequenza dell'API (RPM, TPM, RPD, spesa e così via). | Stai inviando troppe richieste, utilizzando troppi token o superando i limiti basati sulla spesa per la cronologia della fatturazione e il livello del tuo account. | Verifica di rispettare i [limiti di frequenza](https://ai.google.dev/gemini-api/docs/rate-limits?hl=it) del modello. Attendi e riprova dopo un breve periodo. Riduci la frequenza o le dimensioni delle richieste. [Se necessario, richiedi un aumento del limite di frequenza](https://ai.google.dev/gemini-api/docs/rate-limits?hl=it#request-rate-limit-increase). |
| 499 | CANCELLED | L'operazione è stata annullata, in genere dal chiamante. | Il client ha chiuso la connessione prima che l'API potesse terminare la risposta. | Verifica se la tua infrastruttura di rete o client chiude prematuramente la connessione (ad es. a causa di un timeout lato client). |
| 500 | INTERNAL | Si è verificato un errore imprevisto da parte di Google. | Il contesto di input è troppo lungo. | Controlla la [pagina di stato dell'API Gemini](https://aistudio.google.com/status?hl=it) per eventuali incidenti in corso. Riduci il contesto di input o passa temporaneamente a un altro modello (ad es. da Gemini 2.5 Pro a Gemini 2.5 Flash) e verifica se funziona. In alternativa, attendi un po' e riprova a inviare la richiesta. Se il problema persiste dopo aver riprovato, segnalalo utilizzando il pulsante **Invia feedback** in Google AI Studio. |
| 503 | UNAVAILABLE | Il servizio potrebbe essere temporaneamente sovraccarico o non disponibile. | Il servizio sta temporaneamente esaurendo la capacità. | Controlla la [pagina di stato dell'API Gemini](https://aistudio.google.com/status?hl=it) per eventuali incidenti in corso. Passa temporaneamente a un altro modello (ad es. da Gemini 2.5 Pro a Gemini 2.5 Flash) e verifica se funziona. In alternativa, attendi un po' e riprova a inviare la richiesta. Se il problema persiste dopo aver riprovato, segnalalo utilizzando il pulsante **Invia feedback** in Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Il servizio non è in grado di completare l'elaborazione entro la scadenza. | Il prompt (o il contesto) è troppo grande per essere elaborato in tempo. | Imposta un "timeout" più lungo nella richiesta del client per evitare questo errore. |

## Formato della risposta di errore

Quando una richiesta `GenerateContent` non va a buon fine, l'API imposta il codice di stato HTTP (ad es. `400 Bad Request`, `403 Forbidden` o `429 Too Many Requests`) e restituisce un corpo della risposta JSON contenente i dettagli dello stato gRPC:

```
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "API_KEY_INVALID",
        "domain": "googleapis.com",
        "metadata": {
          "service": "generativelanguage.googleapis.com"
        }
      },
      {
        "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
        "locale": "en-US",
        "message": "API key not valid. Please pass a valid API key."
      }
    ]
  }
}
```

| Campo | Tipo | Descrizione |
| --- | --- | --- |
| `code` | integer | Il codice di stato HTTP. |
| `message` | stringa | Una descrizione dell'errore leggibile da una persona. |
| `status` | stringa | Il codice di stato gRPC in `SCREAMING_CASE`. |
| `details` | matrice | Contesto di errore aggiuntivo, ad esempio `ErrorInfo` o `LocalizedMessage`. |

## Passaggi successivi

- [Risoluzione dei problemi dell'API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=it): risolvi problemi comuni e scenari di errore.
- [Limiti di frequenza](https://ai.google.dev/gemini-api/docs/rate-limits?hl=it): scopri di più sui limiti di richiesta e sulla gestione delle quote.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
