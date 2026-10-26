---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=it
fetched_at: 2026-10-26T05:48:22.846940+00:00
title: "Combinare strumenti integrati e chiamata di funzione \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Combinare strumenti integrati e chiamata di funzione

Gemini consente la combinazione di [strumenti integrati](https://ai.google.dev/gemini-api/docs/tools?hl=it), come
`google_search`, e [chiamate di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)
(note anche come *strumenti personalizzati*) in una singola interazione, mantenendo ed esponendo
la cronologia del contesto delle chiamate allo strumento. Le combinazioni di strumenti integrati e personalizzati consentono Agentic Workflows complessi in cui, ad esempio, il modello può fare il grounding sui dati web in tempo reale prima di chiamare la logica di business specifica.

Ecco un esempio che abilita le combinazioni di strumenti integrati e personalizzati con `google_search` e una funzione personalizzata `getWeather`:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");

Function customFunc =
    Function.builder()
        .name("get_user_location")
        .description("Retrieves user current location.")
        .parameters(parameters)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the weather like where I am right now?"))
        .tools(Arrays.asList(customFunc, new GoogleSearch()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Vai

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    customFunc := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_user_location"),
        Description: genai.Ptr("Retrieves user current location."),
        Parameters: map[string]any{
            "type": "object",
        },
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("What is the weather like where I am right now?"),
            Tools: []interactions.Tool{
                customFunc,
                interactions.NewTool(interactions.GoogleSearch{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.8-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## Come funziona

I modelli Gemini 3 utilizzano la *circolazione del contesto dello strumento* per abilitare le combinazioni di strumenti integrati e personalizzati. La circolazione del contesto dello strumento consente di mantenere ed esporre il contesto degli strumenti integrati e di condividerlo con gli strumenti personalizzati nella stessa interazione.

### Abilitare la combinazione di strumenti

- Includi [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#function-declarations), insieme
  agli strumenti integrati che vuoi utilizzare, per attivare il comportamento di combinazione.

### Passaggi restituiti dall'API

In una risposta di interazione, l'API restituisce passaggi separati per le chiamate allo strumento integrato e le chiamate di funzione (strumento personalizzato):

- **Passaggi dello strumento integrato**: l'API li gestisce automaticamente, mantenendo il
  contesto tra i turni.
- **Passaggi della chiamata di funzione**: l'API restituisce i passaggi `function_call` per le funzioni
  personalizzate. Esegui la funzione e fornisci il risultato.

### Campi critici nei passaggi restituiti

Alcuni campi nei passaggi restituiti sono fondamentali per mantenere il contesto dello strumento e abilitare le combinazioni di strumenti:

- **`id`**: si trova nei passaggi `function_call` e `function_response`. Un identificatore univoco che mappa una chiamata alla relativa risposta.
- **`signature`**: si trova nei passaggi `thought`, nonché in tutti i passaggi di chiamata allo strumento (ad es. `function_call`) e di risultato (ad es. `function_response`) per i modelli Gemini 3+. Questo contesto criptato consente la **circolazione del contesto dello strumento** tra le interazioni.

**Gestione di questi campi:**

- **Modalità con stato (consigliata)**: quando utilizzi `previous_interaction_id`, il server gestisce automaticamente i campi `id` e `signature`.
- **Modalità stateless**: quando gestisci manualmente la cronologia delle conversazioni, devi assicurarti di passare al modello sia il campo `id` sia il campo `signature` nelle richieste successive per convalidare l'autenticità e mantenere il contesto. Gli SDK ufficiali gestiscono automaticamente questa operazione se restituisci l'oggetto di risposta completo alla cronologia.

### Dati specifici dello strumento

Alcuni strumenti integrati restituiscono argomenti di dati visibili all'utente specifici per il tipo di strumento.

| Strumento | Argomenti della chiamata allo strumento visibili all'utente (se presenti) | Risposta dello strumento visibile all'utente (se presente) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` URL da sfogliare | `status`: stato di navigazione `retrieved_url`: URL sfogliati |
| **file\_search** | Nessuno | Nessuno |

## Token e prezzi

Tieni presente che le parti della chiamata allo strumento integrato nelle richieste vengono conteggiate nel valore `prompt_token_count`. Poiché questi passaggi intermedi dello strumento sono ora visibili e ti vengono restituiti, fanno parte della cronologia delle conversazioni. Questo vale solo per il
caso per *richieste*, non per *risposte*.

Lo strumento Ricerca Google è un'eccezione a questa regola. La Ricerca Google applica già
il proprio modello di prezzi a livello di query, quindi i token non sono
addebitati due volte (vedi la pagina [Prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it)).

Per ulteriori informazioni, consulta la pagina [Token](https://ai.google.dev/gemini-api/docs/tokens?hl=it).

## Limitazioni

- Quando la circolazione del contesto dello strumento è abilitata, la modalità predefinita è `validated` (la modalità `auto` non è supportata).
- Gli strumenti integrati come `google_search` si basano sulle informazioni relative alla posizione e all'ora corrente, quindi se `system_instruction` o `function_declaration.description` contengono informazioni su posizione e ora in conflitto, la funzionalità di combinazione degli strumenti potrebbe non funzionare correttamente.

## Strumenti supportati

La circolazione del contesto dello strumento standard si applica agli strumenti lato server (integrati).
L'esecuzione di codice è anche uno strumento lato server, ma ha una propria soluzione integrata per la circolazione del contesto. L'utilizzo del computer e le chiamate di funzione sono strumenti lato client e hanno anche soluzioni integrate per la circolazione del contesto.

| Strumento | Lato di esecuzione | Supporto per la circolazione del contesto |
| --- | --- | --- |
| [Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it) | Lato server | Supportato |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it) | Lato server | Supportato |
| [Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it) | Lato server | Supportato |
| [Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it) | Lato server | Supportato |
| [Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it) | Lato server | Supportato (integrato, utilizza i passaggi `code_execution` e `code_execution_result`) |
| [Utilizzo del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it) | Lato client | Supportato (integrato, utilizza i passaggi `function_call` e `function_response`) |
| [Funzioni personalizzate](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) | Lato client | Supportato (integrato, utilizza i passaggi `function_call` e `function_response`) |

## Passaggi successivi

- Scopri di più sulle [chiamate di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) nell'API Gemini.
- Esplora gli strumenti supportati:
  - [Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)
  - [Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)
  - [Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-13 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-13 UTC."],[],[]]
