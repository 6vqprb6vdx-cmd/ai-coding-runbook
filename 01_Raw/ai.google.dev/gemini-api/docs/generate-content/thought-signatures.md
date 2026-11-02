---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=sq
fetched_at: 2026-11-02T07:27:54.954766+00:00
title: "N\u00ebnshkrimet e mendimeve \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs/generate-content?hl=sq)

Dërgo komente

# Nënshkrimet e mendimeve

Nënshkrimet e mendimeve janë përfaqësime të enkriptuara të procesit të mendimit të brendshëm të modelit dhe përdoren për të ruajtur kontekstin e arsyetimit nëpër ndërveprimet me shumë hapa.
Kur përdor modele arsyetuese (si p.sh. seritë Gemini 4, 3 dhe 2.5), API-ja mund të
kthejë një fushë `thoughtSignature` brenda [pjesëve të përmbajtjes](https://ai.google.dev/api/caching?hl=sq#Part)
të përgjigjes (p.sh. pjesët `text` ose `functionCall`).

Si rregull i përgjithshëm, nëse merr një nënshkrim arsyetimi në një përgjigje të modelit,
duhet ta dërgosh mbrapsht saktësisht siç është marrë kur dërgon historikun e bisedës
në radhën tjetër.
**Kur përdor modelet Gemini 4 dhe Gemini 3, duhet të kalosh përsëri nënshkrimet e mendimeve gjatë thirrjes së funksionit, në rast të kundërt do të marrësh një gabim validimi** (kod statusi 4xx).
Kjo përfshin kur përdor cilësimin e `minimal`
[nivelit të arsyetimit](https://ai.google.dev/gemini-api/docs/thinking?hl=sq#thinking-levels) për Gemini 3
Flash.

## Si funksionon

Grafiku më poshtë vizualizon kuptimin e "radhës" dhe "hapit" në lidhje me
[thirrjen e funksionit](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq) në Gemini API. Një "radhë"
është një shkëmbim i vetëm dhe i plotë në një bisedë mes një përdoruesi dhe një modeli. Një
"hap" është një veprim ose operacion më i detajuar i kryer nga modeli, shpesh si
pjesë e një procesi më të madh për të përfunduar një radhë.

![Diagrami i hapave dhe radhës së thirrjes së funksionit](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=sq)

*Ky dokument fokusohet në trajtimin e thirrjes së funksionit për modelet Gemini 4 dhe Gemini 3. Referoju
seksionit të [sjelljes së modelit](#model-behavior) për mospërputhjet me 2.5.*

Gemini 4 dhe Gemini 3 kthejnë nënshkrimet e mendimit për të gjitha përgjigjet e modelit (përgjigjet nga API-ja) me një thirrje funksioni. Nënshkrimet e mendimit shfaqen në rastet e mëposhtme:

- Kur ka thirrje të [funksionit paralel](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq#parallel_function_calling), pjesa e parë e thirrjes së funksionit e kthyer nga përgjigjja e modelit do të ketë një nënshkrim të mendimit.
- Kur ka thirrje vijuese të funksionit (me shumë hapa), çdo thirrje e funksionit do të ketë një nënshkrim dhe duhet t'i transmetosh mbrapsht të gjitha nënshkrimet.
- Përgjigjet e modelit pa një thirrje funksioni do të kthejnë një nënshkrim mendimi brenda pjesës së fundit të kthyer nga modeli.

Tabela e mëposhtme ofron një pamje për thirrjet e funksioneve me shumë hapa,
duke kombinuar përkufizimet e radhëve dhe hapave me konceptin e nënshkrimeve
të prezantuara më sipër:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Kthesu** | **Hapi** | **Kërkesa e përdoruesit** | **Përgjigjja e modelit** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | Asnjë |

## Nënshkrimet në pjesët e thirrjes së funksionit

Kur Gemini gjeneron një `functionCall`, ai mbështetet te `thought_signature`
për të përpunuar si duhet rezultatin e veglës në radhën tjetër.

- **Sjellja**:
  - **Thirrje e vetme funksioni**: Pjesa `functionCall` do të përmbajë një `thought_signature`.
  - **Thirrjet paralele të funksionit**: Nëse modeli gjeneron thirrje paralele të funksionit në një përgjigje, `thought_signature` i bashkëngjitet **vetëm pjesës së parë**
    `functionCall`. Pjesët vijuese të `functionCall` në të njëjtën përgjigje
    **nuk** do të përmbajnë një nënshkrim.
- **Kërkesa**: Ti **duhet** ta kthesh këtë nënshkrim në pjesën e saktë ku është marrë kur dërgon përsëri historikun e bisedës.
- **Validation**: Strict validation is enforced for all function calls within
  the current turn . (Kërkohet vetëm radha aktuale; ne nuk kryejmë verifikim në
  radhët e mëparshme)
  - API-ja kthehet prapa në historik (nga më i riu te më i vjetri) për të gjetur mesazhin më të fundit të **Përdoruesit** që përmban përmbajtje standarde (p.sh. `text`) ( që do të ishte fillimi i radhës aktuale). Kjo nuk do të **be** një `functionResponse`.
  - **Të gjitha** kthesat e modelit `functionCall` që ndodhin pas atij mesazhi specifik të përdorimit
    konsiderohen pjesë e kthesës.
  - Pjesa **e parë** `functionCall` në **çdo hap** të radhës aktuale **duhet** të përfshijë `thought_signature`.
  - Nëse heq një `thought_signature` për pjesën e parë `functionCall` në çdo hap të radhës aktuale, kërkesa do të dështojë me një gabim 400.
- **Nëse nuk kthehen nënshkrimet e duhura, ja se si do të shfaqet gabimi**
  - Modelet e Gemini 3: Mosparaqitja e nënshkrimeve do të rezultojë në një gabim 400. Teksti do të jetë në formën:
    - Thirrjes së funksionit `<Function Call>` në bllokun e përmbajtjes `<index of contents array>` i mungon një `thought_signature`. Për shembull, *Thirrja e funksionit
      `FC1` në bllokun e përmbajtjes `1.` i mungon një `thought_signature`.*

### Shembulli i thirrjes vijuese të funksionit

Ky seksion tregon një shembull të thirrjeve të shumëfishta të funksioneve ku përdoruesi bën një pyetje komplekse që kërkon shumë detyra.

Le të shikojmë një shembull të thirrjes së funksionit me disa raunde ku përdoruesi bën një pyetje komplekse që kërkon disa detyra: `"Check flight status for AA100 and
book a taxi if delayed"`.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Kthesu** | **Hapi** | **Kërkesa e përdoruesit** | **Përgjigjja e modelit** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Kodi i mëposhtëm ilustron sekuencën në tabelën e mësipërme.

**Raundi 1, hapi 1 (kërkesa e përdoruesit)**

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

**Raundi 1, hapi 1 (përgjigjja e modelit)**

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

**Rradha 1, Hapi 2 (Përgjigjja e përdoruesit - Daljet e veglës së dërgimit)** Duke qenë se kjo radhë e përdoruesit përfshin vetëm një `functionResponse` (pa tekst të ri), ne jemi përsëri në radhën 1. Ne
duhet të ruajmë `<Signature_A>`.

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

**Radha 1, hapi 2 (Modeli)** Modeli tani vendos të rezervojë një taksi bazuar në rezultatin e mëparshëm të veglës.

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

**Raundi 1, hapi 3 (Përdoruesi - Dërgimi i rezultatit të veglës)** Për të dërguar konfirmimin e rezervimit të taksisë, duhet të përfshijmë nënshkrimet për **TË GJITHA** thirrjet e funksionit në këtë cikël (`<Signature A>` + `<Signature B>`).

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

### Shembulli i thirrjes së funksionit paralel

Le të shohim një shembull të thirrjes së funksionit paralel ku përdoruesi i kërkon
`"Check weather in Paris and London"` të shikojë se ku modeli kryen verifikimin.

| **Kthesu** | **Hapi** | **Kërkesa e përdoruesit** | **Përgjigjja e modelit** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ("Paris") + nënshkrimi  FC2 ("London") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (nuk ka FC) | Asnjë |

Kodi i mëposhtëm ilustron sekuencën në tabelën e mësipërme.

**Raundi 1, hapi 1 (kërkesa e përdoruesit)**

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

**Raundi 1, hapi 1 (përgjigjja e modelit)**

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

**Kthehu 1, Hapi 2 (Përgjigjja e përdoruesit - Daljet e veglës së dërgimit)** Ne duhet të ruajmë
`<Signature_A>` në pjesën e parë pikërisht siç është marrë.

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

## Nënshkrimet në pjesët jo `functionCall`

Gemini mund të kthejë gjithashtu `thought_signatures` në pjesën përfundimtare të përgjigjes
në pjesët jo të thirrjes së funksionit.

- **Sjellja**: Pjesa përfundimtare e përmbajtjes (`text, inlineData…`) e kthyer nga modeli mund të përfshijë një `thought_signature`.
- **Rekomandim**: Kthimi i këtyre nënshkrimeve **rekomandohet** për të siguruar që modeli të mbajë arsyetimin me cilësi të lartë, sidomos për ndjekjen e udhëzimeve komplekse ose flukset e punës të agjentëve të simuluar.
- **Verifikimi**: API-ja **nuk** e zbaton në mënyrë strikte verifikimin. Nuk do të marrësh një gabim bllokimi nëse i heq ato, megjithëse performanca mund të ulet.

### Arsyetimi me tekst/në kontekst (pa verifikim)

**Raundi 1, hapi 1 (përgjigjja e modelit)**

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

**Radha 2, hapi 1 (përdoruesi)**

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

## Nënshkrimet për përputhshmërinë me OpenAI

Shembujt e mëposhtëm tregojnë se si të menaxhosh nënshkrimet e mendimeve për një API të plotësimit të bisedës duke përdorur [përputhshmërinë me OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=sq).

### Shembulli i thirrjes vijuese të funksionit

Ky është një shembull i thirrjes së shumë funksioneve ku përdoruesi bën një pyetje komplekse që kërkon shumë detyra.

Le të shikojmë një shembull të thirrjes së funksionit me disa kthesa ku përdoruesi pyet
`Check flight status for AA100 and book a taxi if delayed` dhe mund të shikosh se çfarë
ndodh kur përdoruesi bën një pyetje komplekse që kërkon disa detyra.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Kthesu** | **Hapi** | **Kërkesa e përdoruesit** | **Përgjigjja e modelit** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Kodi i mëposhtëm kalon nëpër sekuencën e dhënë.

**Radha 1, Hapi 1 (Kërkesa e përdoruesit)**

```
{
  "model": "google/gemini-4-argon",
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

**Raundi 1, hapi 1 (përgjigjja e modelit)**

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

**Raundi 1, hapi 2 (përgjigjja e përdoruesit - dërgimi i rezultateve të veglës)**

Duke qenë se ky hap i përdoruesit përfshin vetëm një `functionResponse` (pa tekst të ri), ne jemi
ende në hapin 1 dhe duhet të ruajmë `<Signature_A>`.

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

**Kthehu 1, Hapi 2 (Model)**

Modeli tani vendos të rezervojë një taksi bazuar në rezultatin e mëparshëm të veglës.

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

**Radha 1, hapi 3 (Përdoruesi - Dërgimi i rezultatit të veglës)**

Për të dërguar konfirmimin e rezervimit të taksisë, ne duhet të përfshijmë nënshkrimet për TË GJITHA thirrjet e funksioneve në këtë cikël (`<Signature A>` + `<Signature B>`).

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

### Shembulli i thirrjes së funksionit paralel

Le të shikojmë një shembull të thirrjes paralele të funksionit ku përdoruesi pyet
`"Check weather in Paris and London"` dhe mund të shikosh se ku kryen modeli
verifikimin.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Kthehu** | **Hapi** | **Kërkesa e përdoruesit** | **Përgjigjja e modelit** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

Ja kodi për të kaluar nëpër sekuencën e dhënë.

**Raundi 1, hapi 1 (kërkesa e përdoruesit)**

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

**Raundi 1, hapi 1 (përgjigjja e modelit)**

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

**Rradha 1, Hapi 2 (Përgjigjja e përdoruesit - Dërgimi i daljeve të veglës)**

Duhet të ruash `<Signature_A>` në pjesën e parë saktësisht siç është marrë.

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

## Pyetjet më të shpeshta

1. **Si mund ta transferoj historikun nga një model tjetër te Gemini 4 ose Gemini 3 me një pjesë të thirrjes së funksionit në radhën dhe hapin aktual? Duhet të jap pjesët e thirrjes së funksionit që nuk janë gjeneruar nga API-ja dhe që për këtë arsye nuk kanë një nënshkrim të lidhur të mendimit?**

   Megjithëse injektimi i blloqeve të personalizuara të thirrjeve të funksioneve në kërkesë është shumë i
   këshillueshëm, në rastet kur nuk mund të shmanget, p.sh. për t'i dhënë modelit informacione
   për thirrjet e funksioneve dhe përgjigjet që janë ekzekutuar në mënyrë
   deterministike nga klienti ose për të transferuar një gjurmë nga një model tjetër
   që nuk përfshin nënshkrime të mendimeve, mund të caktosh nënshkrimet e mëposhtme
   fiktive të `"context_engineering_is_the_way_to_go"` ose
   `"skip_thought_signature_validator"` në fushën e nënshkrimit të mendimit për të kapërcyer
   verifikimin.
2. **Po dërgoj mbrapsht thirrje dhe përgjigje paralele të ndërthurura të funksionit dhe API-ja po kthen një kod 400. Pse?**

   Kur API-ja kthen thirrje paralele të funksionit "FC1 + nënshkrimi, FC2", përgjigjja e pritshme e përdoruesit është "FC1+ nënshkrimi, FC2, FR1, FR2". Nëse i ke ato
   të ndërthurura si "FC1 + nënshkrimi, FR1, FC2, FR2", API-ja do të kthejë një gabim
   400.
3. **Kur transmeton dhe modeli nuk kthen një thirrje funksioni, nuk mund të gjej
   nënshkrimin e mendimit**

   Gjatë një përgjigjeje të modelit që nuk përfshin një FC me një kërkesë transmetimi, modeli mund të kthejë nënshkrimin e mendimit në një pjesë me një pjesë përmbajtjeje me tekst bosh. Këshillohet të analizosh të gjithë kërkesën derisa të kthehet `finish_reason`
   nga modeli.

## Nënshkrimet e mendimeve për modele të ndryshme

Modelet [Gemini 4](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=sq), [Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=sq#gemini-3) dhe Gemini 2.5
sillen ndryshe me nënshkrimet e mendimeve në thirrjet e funksioneve:

- Nëse ka thirrje funksionesh në një përgjigje,
  - Gemini 4 dhe Gemini 3 do të kenë gjithmonë nënshkrimin në pjesën e parë të thirrjes së funksionit.
    Është **e detyrueshme** që ta kthesh atë pjesë.
  - Gemini 2.5 do të ketë nënshkrimin në pjesën e parë (pavarësisht nga lloji). Është **opsionale** që ta kthesh atë pjesë.
- Nëse nuk ka thirrje funksionesh në një përgjigje,
  - Gemini 4 dhe Gemini 3 do të kenë nënshkrimin në pjesën e fundit nëse modeli gjeneron një mendim.
  - Gemini 2.5 nuk do të ketë një nënshkrim në asnjë pjesë.

Referoju faqes [Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=sq#signatures) për më shumë detaje krahasimi.
Për modelet e imazheve të Gemini 3, shiko seksionin e procesit të të menduarit të udhëzuesit për [Gjenerimin e imazheve](https://ai.google.dev/gemini-api/docs/image-generation?hl=sq#thinking-process).

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-13 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-13 UTC."],[],[]]
