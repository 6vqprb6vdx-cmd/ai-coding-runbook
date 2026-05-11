---
source_url: https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=it
fetched_at: 2026-05-11T12:40:06.387287+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Inferenza con priorità

L'API Gemini Priority è un livello di inferenza premium progettato per workload mission critical che richiedono una latenza inferiore e la massima affidabilità a un prezzo premium. Il traffico del livello Priority ha la priorità rispetto al traffico dell'API standard e del livello Flex.

L'inferenza con priorità è disponibile in tutti gli endpoint dell'API Interactions.

## Come utilizzare la priorità

Per utilizzare il livello Priority, imposta il campo `service_tier` della richiesta su `priority`. Se il campo viene omesso, il livello predefinito è standard.

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input="Triage this critical customer support ticket immediately.",
        service_tier='priority'
    )

    # Validate for graceful downgrade
    # Note: Checking headers might vary by SDK implementation, this is illustrative
    # if interaction.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
    #     print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(interaction.steps[-1].content[0].text)

except Exception as e:
    print(f"Error during API call: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const interaction = await ai.interactions.create({
          model: "gemini-3-flash-preview",
          input: "Triage this critical customer support ticket immediately.",
          service_tier: "priority"
      });

      // Validate for graceful downgrade
      // if (interaction.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
      //     console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      // }

      console.log(interaction.steps.at(-1).content[0].text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Come funziona l'inferenza con priorità

L'inferenza con priorità indirizza le richieste alle code di calcolo ad alta criticità, offrendo prestazioni veloci e prevedibili per le applicazioni rivolte agli utenti. Il suo meccanismo principale è un downgrade controllato lato server all'elaborazione standard per il traffico che supera i limiti dinamici, garantendo la stabilità dell'applicazione anziché la mancata riuscita della richiesta.

| Funzionalità | Priorità | Standard | Flex | Batch |
| --- | --- | --- | --- | --- |
| **Prezzi** | 75-100% in più rispetto a Standard | Intero | Sconto del 50% | Sconto del 50% |
| **Latenza** | Secondi | Da secondi a minuti | Minuti (target 1-15 min) | Fino a 24 ore |
| **Affidabilità** | Elevata (non eliminabile) | Elevata / medio-alta | Best effort (eliminabile) | Elevata (per il throughput) |
| **Interfaccia** | Sincrona | Sincrona | Sincrona | Asincrona |

### Vantaggi principali

- **Bassa latenza**: progettata per tempi di risposta in secondi per gli strumenti di AI interattivi
  rivolti agli utenti.
- **Elevata affidabilità**: il traffico viene trattato con la massima criticità ed è
  strettamente non eliminabile.
- **Riduzione controllata**: i picchi di traffico che superano i limiti dinamici vengono
  automaticamente sottoposti a downgrade al livello Standard per l'elaborazione anziché non riuscire,
  evitando interruzioni del servizio.
- **Basso attrito**: utilizza lo stesso metodo sincrono `create` dei livelli
  Standard e Flex.

### Casi d'uso

L'elaborazione con priorità è ideale per i workflow mission critical in cui le prestazioni e l'affidabilità sono fondamentali.

- **Applicazioni di AI interattive**: chatbot e copiloti dell'assistenza clienti in cui
  gli utenti pagano un premio e si aspettano risposte rapide e coerenti.
- **Motori decisionali in tempo reale**: sistemi che richiedono risultati a bassa latenza e altamente affidabili
  , come il triage dei ticket live o il rilevamento delle frodi.
- **Funzionalità premium per i clienti**: sviluppatori che devono garantire obiettivi di livello
  di servizio (SLO) più elevati per i clienti paganti.

### Limiti di frequenza

Il consumo con priorità ha i propri limiti di frequenza, anche se il consumo viene
conteggiato ai fini dei [limiti di frequenza del traffico interattivo complessivo](https://aistudio.google.com/rate-limit?hl=it). I limiti di frequenza predefiniti per l'inferenza con priorità sono **0,3 volte il limite di frequenza standard per modello / livello**

### Logica di downgrade controllato

Se i limiti di priorità vengono superati a causa della congestione, le richieste di overflow vengono sottoposte a downgrade **automatico e controllato** all'elaborazione standard anziché non riuscire con un errore 503 o 429. Le richieste sottoposte a downgrade vengono fatturate alla tariffa standard, non alla tariffa premium con priorità.

### Responsabilità del cliente

- **Monitoraggio delle risposte**: gli sviluppatori devono monitorare l'`x-gemini-service-tier`
  intestazione nella risposta dell'API per rilevare se le richieste vengono sottoposte a downgrade frequente a
  `standard`.
- **Nuovi tentativi**: i client devono implementare la logica di ripetizione/il backoff esponenziale per gli
  errori standard, ad esempio `DEADLINE_EXCEEDED`.

## Prezzi

L'inferenza con priorità ha un prezzo superiore del 75-100% rispetto all'[API standard](https://ai.google.dev/gemini-api/docs/pricing?hl=it) e viene fatturata per token.

## Modelli supportati

I seguenti modelli supportano l'inferenza con priorità:

| Modello | Inferenza con priorità |
| --- | --- |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=it) | ✔️ |
| [Gemini 3.1 Flash-Lite (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=it) | ✔️ |
| [Gemini 3.1 Pro (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=it) | ✔️ |
| [Gemini 3 Flash (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=it) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=it) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=it) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=it) | ✔️ |

## Passaggi successivi

- [Inferenza Flex](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=it) per la riduzione dei costi.
- [Token](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=it): informazioni sui token.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-09 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-09 UTC."],[],[]]
