---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=it
fetched_at: 2026-09-21T05:49:07.212195+00:00
title: "Firme del pensiero \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs/generate-content?hl=it)

Invia feedback

# Firme del pensiero

Le firme di ragionamento sono rappresentazioni criptate del processo di ragionamento interno del modello e vengono utilizzate per preservare il contesto di ragionamento nelle interazioni multi-step.
Quando utilizzi i modelli di ragionamento (come le serie Gemini 3 e 2.5), l'API può
restituire un campo `thoughtSignature` all'interno delle [parti di contenuti](https://ai.google.dev/api/caching?hl=it#Part)
della risposta (ad es. parti `text` o `functionCall`).

In generale, se ricevi una firma di ragionamento in una risposta del modello, devi restituirla esattamente come l'hai ricevuta quando invii la cronologia della conversazione nel turno successivo.
**Quando utilizzi i modelli Gemini 3, devi restituire le firme di ragionamento durante la chiamata di funzione, altrimenti riceverai un errore di convalida** (codice di stato 4xx).
Ciò include l'utilizzo dell'impostazione del `minimal`
[livello di ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it#thinking-levels) per Gemini 3
Flash.

## Come funziona

Il grafico riportato di seguito visualizza il significato di "turno" e "step" in relazione alla
[chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) nell'API Gemini. Un "turno" è un singolo scambio completo in una conversazione tra un utente e un modello. Uno "step" è un'azione o un'operazione più granulare eseguita dal modello, spesso come parte di un processo più ampio per completare un turno.

![Diagramma dei turni e dei passaggi della chiamata di funzione](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=it)

*Questo documento si concentra sulla gestione della chiamata di funzione per i modelli Gemini 3. Per le discrepanze con la versione 2.5, consulta la sezione relativa al [comportamento del modello](#model-behavior).*

Gemini 3 restituisce le firme di ragionamento per tutte le risposte del modello (risposte dell'API) con una chiamata di funzione. Le firme di ragionamento vengono visualizzate nei seguenti casi:

- Quando sono presenti [chiamate di funzione parallele](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#parallel_function_calling), la prima parte della chiamata di funzione restituita dalla risposta del modello avrà una
  firma di ragionamento.
- Quando sono presenti chiamate di funzione sequenziali (multi-step), ogni chiamata di funzione avrà una firma e devi restituire tutte le firme.
- Le risposte del modello senza una chiamata di funzione restituiranno una firma di ragionamento all'interno dell'ultima parte restituita dal modello.

La tabella seguente fornisce una visualizzazione delle chiamate di funzione multi-step, combinando le definizioni di turni e step con il concetto di firme introdotto sopra:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Turno** | **Step** | **Richiesta utente** | **Risposta del modello** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | Nessuno |

## Firme nelle parti di chiamata di funzione

Quando Gemini genera un `functionCall`, si basa su `thought_signature` per elaborare correttamente l'output dello strumento nel turno successivo.

- **Comportamento**:
  - **Chiamata di funzione singola**: la parte `functionCall` conterrà un `thought_signature`.
  - **Chiamate di funzione parallele**: se il modello genera chiamate di funzione parallele
    in una risposta, `thought_signature` viene allegato **solo alla prima**
    `functionCall` parte. Le parti `functionCall` successive nella stessa risposta **non** conterranno una firma.
- **Requisito**: **devi** restituire questa firma nella parte esatta in cui l'hai ricevuta quando invii la cronologia della conversazione.
- **Convalida**: viene applicata una convalida rigorosa per tutte le chiamate di funzione all'interno
  del turno corrente . (È richiesto solo il turno corrente; non eseguiamo la convalida nei turni precedenti)
  - L'API torna indietro nella cronologia (dal più recente al più vecchio) per trovare il messaggio **Utente** più recente che contiene contenuti standard (ad es. `text`) ( che sarebbe l'inizio del turno corrente). Non **be** un `functionResponse`.
  - **Tutti** i turni `functionCall` del modello che si verificano dopo questo messaggio di utilizzo specifico
    sono considerati parte del turno.
  - La **prima** parte `functionCall` in **ogni step** del turno corrente **deve** includere il relativo `thought_signature`.
  - Se ometti un `thought_signature` per la prima parte `functionCall` in qualsiasi step del turno corrente, la richiesta non andrà a buon fine e verrà restituito un errore 400.
- **Se non vengono restituite le firme corrette, ecco come si verificherà l'errore**
  - Modelli Gemini 3: se non includi le firme, verrà restituito un errore 400. La formulazione sarà del tipo:
    - Nella chiamata di funzione `<Function Call>` nel `<index of contents array>`
      blocco di contenuti manca un `thought_signature`. Ad esempio, *nella chiamata di funzione `FC1` nel blocco di contenuti `1.` manca un `thought_signature`.*

### Esempio di chiamata di funzione sequenziale

Questa sezione mostra un esempio di più chiamate di funzione in cui l'utente pone una domanda complessa che richiede più attività.

Esaminiamo un esempio di chiamata di funzione multi-turno in cui l'utente pone
una domanda complessa che richiede più attività: `"Check flight status for AA100 and
book a taxi if delayed"`.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Turno** | **Step** | **Richiesta utente** | **Risposta del modello** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Il seguente codice illustra la sequenza nella tabella riportata sopra.

**Turno 1, Step 1 (richiesta utente)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "check_flight",
          "description": "Gets the current status of a flight",
          "parameters": {
            "type": "object",
            "properties": {
              "flight": {
                "type": "string",
                "description": "The flight number to check"
              }
            },
            "required": [
              "flight"
            ]
          }
        },
        {
          "name": "book_taxi",
          "description": "Book a taxi",
          "parameters": {
            "type": "object",
            "properties": {
              "time": {
                "type": "string",
                "description": "time to book the taxi"
              }
            },
            "required": [
              "time"
            ]
          }
        }
      ]
    }
  ]
}
```

**Turno 1, Step 1 (risposta del modello)**

```
{
"content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>"
          }
        ]
  }
}
```

**Turno 1, Step 2 (risposta dell'utente - invio degli output dello strumento)** Poiché questo turno dell'utente contiene solo un `functionResponse` (nessun testo nuovo), siamo ancora nel Turno 1. Dobbiamo
conservare `<Signature_A>`.

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
                }
              }
            }
        ]
}
```

**Turno 1, Step 2 (modello)** Il modello ora decide di prenotare un taxi in base all'output dello strumento precedente.

```
{
      "content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>"
          }
        ]
      }
}
```

**Turno 1, Step 3 (utente - invio dell'output dello strumento)** Per inviare la conferma della prenotazione del taxi, dobbiamo includere le firme per **TUTTE** le chiamate di funzione in questo loop
(`<Signature A>` + `<Signature B>`).

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
              }
              }
            }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "book_taxi",
              "response": {
                "booking_status": "success"
              }
              }
            }
        ]
    }
}
```

### Esempio di chiamata di funzione parallela

Esaminiamo un esempio di chiamata di funzione parallela in cui l'utente chiede
`"Check weather in Paris and London"` per vedere dove il modello esegue la convalida.

| **Turno** | **Step** | **Richiesta utente** | **Risposta del modello** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ("Paris") + signature  FC2 ("London") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (no FCs) | None |

Il seguente codice illustra la sequenza nella tabella riportata sopra.

**Turno 1, Step 1 (richiesta utente)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "get_current_temperature",
          "description": "Gets the current temperature for a given location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco"
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**Turno 1, Step 1 (risposta del modello)**

```
{
  "content": {
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "Paris"
          }
        },
        "thoughtSignature": "<Signature_A>"// INCLUDED on First FC
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "London"
          }// NO signature on subsequent parallel FCs
        }
      }
    ]
  }
}
```

**Turno 1, Step 2 (risposta dell'utente - invio degli output dello strumento)** Dobbiamo conservare
`<Signature_A>` nella prima parte esattamente come l'abbiamo ricevuta.

```
[
  {
    "role": "user",
    "parts": [
      {
        "text": "Check the weather in Paris and London."
      }
    ]
  },
  {
    "role": "model",
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "Paris"
          }
        },
        "thought_signature": "<Signature_A>" // MUST BE INCLUDED
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "London"
          }
        }
      } // NO SIGNATURE FIELD
    ]
  },
  {
    "role": "user",
    "parts": [
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "15C"
          }
        }
      },
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "12C"
          }
        }
      }
    ]
  }
]
```

## Firme nelle parti non `functionCall`

Gemini può anche restituire `thought_signatures` nella parte finale della risposta nelle parti non relative alla chiamata di funzione.

- **Comportamento**: la parte di contenuti finale (`text, inlineData…`) restituita dal
  modello può contenere un `thought_signature`.
- **Consigli**: la restituzione di queste firme è **consigliata** per garantire
  che il modello mantenga un ragionamento di alta qualità, soprattutto per le istruzioni complesse
  o i workflow agentici simulati.
- **Convalida**: l'API **non** applica rigorosamente la convalida. Se le ometti, non riceverai un errore di blocco, anche se il rendimento potrebbe peggiorare.

### Ragionamento di testo/nel contesto (nessuna convalida)

**Turno 1, Step 1 (risposta del modello)**

```
{
  "role": "model",
  "parts": [
    {
      "text": "I need to calculate the risk. Let me think step-by-step...",
      "thought_signature": "<Signature_C>" // OPTIONAL (Recommended)
    }
  ]
}
```

**Turno 2, Step 1 (utente)**

```
[
  { "role": "user", "parts": [{ "text": "What is the risk?" }] },
  {
    "role": "model", 
    "parts": [
      {
        "text": "I need to calculate the risk. Let me think step-by-step...",
        // If you omit <Signature_C> here, no error will occur.
      }
    ]
  },
  { "role": "user", "parts": [{ "text": "Summarize it." }] }
]
```

## Firme per la compatibilità con OpenAI

I seguenti esempi mostrano come gestire le firme di ragionamento per un'API di completamento della chat
utilizzando [la compatibilità con OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=it).

### Esempio di chiamata di funzione sequenziale

Questo è un esempio di più chiamate di funzione in cui l'utente pone una domanda complessa che richiede più attività.

Esaminiamo un esempio di chiamata di funzione multi-turno in cui l'utente chiede `Check flight status for AA100 and book a taxi if delayed` e puoi vedere cosa succede quando l'utente pone una domanda complessa che richiede più attività.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Turno** | **Step** | **Richiesta utente** | **Risposta del modello** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Il seguente codice illustra la sequenza indicata.

**Turno 1, Step 1 (richiesta utente)**

```
{
  "model": "google/gemini-3.1-pro-preview",
  "messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "check_flight",
        "description": "Gets the current status of a flight",
        "parameters": {
          "type": "object",
          "properties": {
            "flight": {
              "type": "string",
              "description": "The flight number to check."
            }
          },
          "required": [
            "flight"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "book_taxi",
        "description": "Book a taxi",
        "parameters": {
          "type": "object",
          "properties": {
            "time": {
              "type": "string",
              "description": "time to book the taxi"
            }
          },
          "required": [
            "time"
          ]
        }
      }
    }
  ]
}
```

**Turno 1, Step 1 (risposta del modello)**

```
{
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>"
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    }
```

**Turno 1, Step 2 (risposta dell'utente - invio degli output dello strumento)**

Poiché questo turno dell'utente contiene solo un `functionResponse` (nessun testo nuovo), siamo
ancora nel Turno 1 e dobbiamo conservare `<Signature_A>`.

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    }
  ]
```

**Turno 1, Step 2 (modello)**

Il modello ora decide di prenotare un taxi in base all'output dello strumento precedente.

```
{
"role": "model",
"tool_calls": [
{
"extra_content": {
"google": {
"thought_signature": "<Signature B>"
}
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-2",
            "type": "function"
          }
       ]
}
```

**Turno 1, Step 3 (utente - invio dell'output dello strumento)**

Per inviare la conferma della prenotazione del taxi, dobbiamo includere le firme per TUTTE
le chiamate di funzione in questo loop (`<Signature A>` + `<Signature B>`).

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature B>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "book_taxi",
      "tool_call_id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
      "content": "{\"booking_status\":\"success\"}"
    }
  ]
```

### Esempio di chiamata di funzione parallela

Esaminiamo un esempio di chiamata di funzione parallela in cui l'utente chiede
`"Check weather in Paris and London"` e puoi vedere dove il modello esegue la
convalida.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Turno** | **Step** | **Richiesta utente** | **Risposta del modello** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

Ecco il codice per esaminare la sequenza indicata.

**Turno 1, Step 1 (richiesta utente)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "get_current_temperature",
          "description": "Gets the current temperature for a given location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco"
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**Turno 1, Step 1 (risposta del modello)**

```
{
"role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Signature returned
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": {
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function" // No signature on Parallel FC
          }
        ]
}
```

**Turno 1, Step 2 (risposta dell'utente - invio degli output dello strumento)**

Devi conservare `<Signature_A>` nella prima parte esattamente come l'hai ricevuta.

```
"messages": [
    {
      "role": "user",
      "content": "Check the weather in Paris and London."
    },
    {
      "role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": { //No Signature
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function"
          }
        ]
    },
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
      "content": "{\"temp\":\"15C\"}"
    },    
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
      "content": "{\"temp\":\"12C\"}"
    }
  ]
```

## Domande frequenti

1. **Come faccio a trasferire la cronologia da un modello diverso a Gemini 3 con una parte di chiamata di funzione nel turno e nello step correnti? Devo fornire parti di chiamata di funzione
   che non sono state generate dall'API e quindi non hanno una firma di ragionamento associata
   ?**

   Sebbene l'inserimento di blocchi di chiamate di funzione personalizzati nella richiesta sia fortemente
   sconsigliato, nei casi in cui non è possibile evitarlo, ad es. fornire informazioni
   al modello sulle chiamate di funzione e sulle risposte eseguite
   in modo deterministico dal client o trasferire una traccia da un modello diverso
   che non include firme di ragionamento, puoi impostare le seguenti
   firme fittizie di `"context_engineering_is_the_way_to_go"` o
   `"skip_thought_signature_validator"` nel campo della firma di ragionamento per saltare la
   convalida.
2. **Sto inviando chiamate di funzione e risposte parallele intercalate e l'API restituisce un errore 400. Perché?**

   Quando l'API restituisce chiamate di funzione parallele "FC1 + signature, FC2", la risposta dell'utente prevista è "FC1+ signature, FC2, FR1, FR2". Se le hai intercalate come "FC1 + signature, FR1, FC2, FR2", l'API restituirà un errore 400.
3. **Durante lo streaming e il modello non restituisce una chiamata di funzione, non riesco a trovare
   la firma di ragionamento**

   Durante una risposta del modello che non contiene una chiamata di funzione con una richiesta di streaming, il modello può restituire la firma di ragionamento in una parte con una parte di contenuti di testo vuota. È consigliabile analizzare l'intera richiesta finché il modello non restituisce `finish_reason`.

## Firme di ragionamento per modelli diversi

[I modelli Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-3) e i modelli Gemini 2.5
si comportano in modo diverso con le firme di ragionamento nelle chiamate di funzione:

- Se in una risposta sono presenti chiamate di funzione,
  - Gemini 3 avrà sempre la firma nella prima parte della chiamata di funzione.
    È **obbligatorio** restituire questa parte.
  - Gemini 2.5 avrà la firma nella prima parte (indipendentemente dal tipo). La restituzione di questa parte è **facoltativa**.
- Se in una risposta non sono presenti chiamate di funzione,
  - Gemini 3 avrà la firma nell'ultima parte se il modello genera un ragionamento.
  - Gemini 2.5 non avrà una firma in nessuna parte.

Per maggiori dettagli sul confronto, consulta la pagina [Ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it#signatures) per maggiori
dettagli sul confronto.
Per i modelli di immagini Gemini 3, consulta la sezione relativa al processo di ragionamento della
[guida alla generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it#thinking-process).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-08 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-08 UTC."],[],[]]
