---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tool-combination?hl=sq
fetched_at: 2026-10-19T05:30:39.979867+00:00
title: "Kombino veglat e integruara dhe telefonatat e funksioneve \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs/generate-content?hl=sq)

Dërgo komente

# Kombino veglat e integruara dhe telefonatat e funksioneve

Gemini lejon kombinimin e [veglave të integruara](https://ai.google.dev/gemini-api/docs/tools?hl=sq), si p.sh. `google_search`, dhe [thirrjes së funksionit](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq) (e njohur gjithashtu si *veglat e personalizuara*) në një gjenerim të vetëm duke ruajtur dhe ekspozuar historikun e kontekstit të thirrjeve të veglave. Kombinimet e integruara dhe të personalizuara të veglave lejojnë flukse pune komplekse dhe të drejtuara nga agjentët ku, për shembull, modeli mund të bazohet në të dhënat e uebit në kohë reale para se të thërrasë logjikën tënde specifike të biznesit.

Këtu është një shembull që aktivizon kombinimet e veglave të integruara dhe të personalizuara me
`google_search` dhe një funksion të personalizuar `getWeather`:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
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

# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather],  # Custom tool
            ),
        ],
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)
function_call_id = None
for part in response.candidates[0].content.parts:
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")
        function_call_id = part.function_call.id

# Turn 2: Manually build history to circulate both tool and function context
history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    # Response from Turn 1 includes tool_call, tool_response, and thought_signatures
    response.candidates[0].content,
    # Return the function_response
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=function_call_id # Match the ID from the function_call
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=history,
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),
                function_declarations=[getWeather]
            ),
        ],
        # This flag needs to be enabled for built-in tool context circulation and tool combination
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)

for part in response_2.candidates[0].content.parts:
    if part.text:
        print(part.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const response1 = await client.models.generateContent({
        model: "gemini-3.8-flash",
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    for (const part of response1.candidates[0].content.parts) {
        if (part.functionCall) {
            console.log(`Function call: ${part.functionCall.name} (ID: ${part.functionCall.id})`);
        }
    }

   const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    // Turn 2: Manually build history to circulate both tool and function context
    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        // Response from Turn 1 includes tool_call, tool_response, and thought_signatures
        response1.candidates[0].content,
        // Return the function_response
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId // Match the ID from the function_call
                }
            }]
        }
    ];

    const response2 = await client.models.generateContent({
        model: "gemini-3.8-flash",
        contents: history,
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    for (const part of response2.candidates[0].content.parts) {
        if (part.text) {
            console.log(part.text);
        }
    }
}

run();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/generative-ai-go/genai"
    "google.golang.org/api/option"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("GEMINI_API_KEY")))
    if err != nil {
        log.Exit(err)
    }
    defer client.Close()

    getWeather := &genai.FunctionDeclaration{
        Name:        "getWeather",
        Description: "Get the weather in a given location",
        Parameters: &genai.Schema{
            Type: genai.Object,
            Properties: map[string]*genai.Schema{
                "location": {
                    Type:        genai.String,
                    Description: "The city and state, e.g. San Francisco, CA",
                },
            },
            Required: []string{"location"},
        },
    }

    model := client.GenerativeModel("gemini-3.8-flash")
    model.Tools = []*genai.Tool{
        {GoogleSearch: &genai.GoogleSearch{}}, // Built-in tool
        {FunctionDeclarations: []*genai.FunctionDeclaration{getWeather}}, // Custom tool
    }
    ist := true
    model.ToolConfig = &genai.ToolConfig{
        IncludeServerSideToolInvocations: &ist, // This flag needs to be enabled for built-in tool context circulation and tool combination
    }

    chat := model.StartChat()

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    prompt := genai.Text("What is the northernmost city in the United States? What's the weather like there today?")
    resp1, err := chat.SendMessage(ctx, prompt)
    if err != nil {
        log.Exitf("SendMessage failed: %v", err)
    }

    if resp1 == nil || len(resp1.Candidates) == 0 || resp1.Candidates[0].Content == nil {
        log.Exit("empty response from model")
    }

    var functionCallID string
    for _, part := range resp1.Candidates[0].Content.Parts {
        switch p := part.(type) {
        case genai.FunctionCall:
            fmt.Printf("Function call: %s (ID: %s)\n", p.Name, p.ID)
            if p.Name == "getWeather" {
                functionCallID = p.ID
            }
        }
    }

    if functionCallID == "" {
        log.Exit("no getWeather function call in response")
    }

    // Turn 2: Provide function result back to model.
    // Chat history automatically includes tool_call, tool_response, and thought_signatures from Turn 1.
    fr := genai.FunctionResponse{
        Name: "getWeather",
        ID:   functionCallID,
        Response: map[string]any{
            "response": "Very cold. 22 degrees Fahrenheit.",
        },
    }

    resp2, err := chat.SendMessage(ctx, fr)
    if err != nil {
        log.Exitf("SendMessage for turn 2 failed: %v", err)
    }

    if resp2 == nil || len(resp2.Candidates) == 0 || resp2.Candidates[0].Content == nil {
        log.Exit("empty response from model in turn 2")
    }

    for _, part := range resp2.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Println(string(txt))
        }
    }
}
```

### REST

```
# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What is the northernmost city in the United States? What'\''s the weather like there today?"
    }]
  }],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'

# Turn 2: Manually build history to circulate both tool and function context
# The following request assumes you have captured candidates[0].content from Turn 1 response,
# and extracted function_call.id for getWeather.
# Replace FUNCTION_CALL_ID and insert candidate content from turn 1.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "What is the northernmost city in the United States? What'\''s the weather like there today?"}]
    },
    YOUR_CANDIDATE_CONTENT_FROM_TURN_1_RESPONSE,
    {
      "role": "user",
      "parts": [{
        "functionResponse": {
          "name": "getWeather",
          "id": "FUNCTION_CALL_ID",
          "response": {"response": "Very cold. 22 degrees Fahrenheit."}
        }
      }]
    }
  ],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'
```

## Si funksionon

Modelet e Gemini 3 përdorin *qarkullimin e kontekstit të veglave* për të mundësuar kombinime të veglave të personalizuara dhe të integruara. Qarkullimi i kontekstit të veglës bën të mundur ruajtjen dhe ekspozimin e kontekstit të veglave të integruara dhe ndarjen e tij me veglat e personalizuara në të njëjtin telefonatë nga një raund në tjetrin.

### Aktivizo kombinimin e veglave

- Duhet të caktosh flamurin `include_server_side_tool_invocations` në `true` për të aktivizuar qarkullimin e kontekstit të veglës.
- Përfshi [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq#function-declarations), si dhe veglat e integruara që dëshiron të përdorësh, për të aktivizuar sjelljen e kombinimit.
  - Nëse nuk përfshin `function_declarations`, qarkullimi i kontekstit të veglës do të veprojë përsëri në veglat e integruara të përfshira, për aq kohë sa është caktuar flamuri.

### API-ja kthen pjesë

Në një përgjigje të vetme, API-ja kthen pjesët `toolCall` dhe `toolResponse` për thirrjen e veglës së integruar. Për thirrjen e funksionit (vegla e personalizuar), API-ja kthen pjesën e thirrjes `functionCall`, për të cilën përdoruesi jep pjesën `functionResponse` në radhën tjetër.

- `toolCall` dhe `toolResponse`: API-ja i kthen këto pjesë për të ruajtur kontekstin se cilat vegla ekzekutohen në anën e serverit dhe rezultatin e ekzekutimit të tyre për radhën tjetër.
- `functionCall` dhe `functionResponse`: API-ja i dërgon thirrjen e funksionit përdoruesit për ta plotësuar dhe përdoruesi dërgon mbrapsht rezultatin në përgjigjen e funksionit (këto pjesë janë standarde për të gjitha [thirrjet e funksioneve](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq) në Gemini API, jo unike për veçorinë e kombinimit të veglave).
- (Vetëm veglat e [ekzekutimit të kodit](https://ai.google.dev/gemini-api/docs/code-execution?hl=sq))
  `executableCode` dhe `codeExecutionResult`:
  Kur përdor veglën e ekzekutimit të kodit, në vend të `functionCall` dhe
  `functionResponse`, API-ja kthen `executableCode` (kodi i gjeneruar
  nga modeli që synohet të ekzekutohet) dhe `codeExecutionResult` (rezultati i
  kodit të ekzekutueshëm).

Duhet t'i kthesh të gjitha pjesët, duke përfshirë të gjitha [fushat](#critical-fields) që ato përmbajnë, përsëri te modeli në çdo radhë për të ruajtur kontekstin dhe për të aktivizuar kombinimet e veglave.

### Fushat kritike në pjesët e kthyera

[Pjesë të caktuara të kthyera nga API](#api-returns-parts) do të përfshijnë fushat `id`,
`tool_type` dhe `thought_signature`. Këto fusha janë kritike për
mbajtjen e kontekstit të veglës (dhe prandaj kritike për kombinimet e veglave); duhet të kthesh të gjitha pjesët *siç jepen në përgjigje* në kërkesat e tua vijuese.

- `id`: Një identifikues unik që lidh një telefonatë me përgjigjen e saj. `id` është **caktuar në
  të gjitha përgjigjet e thirrjeve të funksioneve**, pavarësisht nga qarkullimi i kontekstit të veglës.
  *Duhet* të japësh të njëjtën `id` në përgjigjen e funksionit
  që ofron API-ja në thirrjen e funksionit. Veglat e integruara ndajnë automatikisht `id` mes thirrjes së veglës dhe përgjigjes së veglës.
  - Gjenden në të gjitha pjesët në lidhje me veglat: `toolCall`, `toolResponse`,
    `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: Identifikon veglën specifike që po përdoret; vegla e integruar fjalë për fjalë ose (p.sh. `URL_CONTEXT`) ose emri i funksionit (p.sh. `getWeather`).
  - U gjet në `toolCall` dhe `toolResponse` pjesë.
- `thought_signature`: Konteksti aktual i enkriptuar i integruar në **secilën
  pjesë të kthyer nga API-ja**. Context can't be
  reconstructed without thought signatures; if you don't return the thought
  signatures for all parts in every turn, the model will error out.
  - Gjendet në *të gjitha* pjesët.

### Të dhënat specifike për veglën

Disa vegla të integruara kthejnë argumente të të dhënave të dukshme për përdoruesin që janë specifike për llojin e veglës.

| Vegla | Argumentet e thirrjes së veglës të dukshme për përdoruesin (nëse ka) | Përgjigjja e veglës e dukshme për përdoruesin (nëse ka) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` URL-të që do të shfletohen | `url_metadata` `retrieved_url`: URL-të e shfletuara `url_retrieval_status`: Statusi i shfletimit |
| **FILE\_SEARCH** | Asnjë | Asnjë |

## Shembull i strukturës së kërkesës për kombinimin e veglave

Struktura e mëposhtme e kërkesës tregon strukturën e kërkesës së kërkesës: "Cili është qyteti më verior në Shtetet e Bashkuara? Si është moti atje sot?". Ajo kombinon tre vegla: veglat e integruara të Gemini `google_search`
dhe `code_execution`, si dhe një funksion të personalizuar `get_weather`.

```
{
  "model": "models/gemini-3.8-flash",
  "contents": [{
    "parts": [{
      "text": "What is the northernmost city in the United States? What's the weather like there today?"
    }],
    "role": "user"
  }, {
    "parts": [{
      "thoughtSignature": "...",
      "toolCall": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "args": {
          "queries": ["northernmost city in the United States"]
        },
        "id": "a7b3k9p2"
      }
    }, {
      "thoughtSignature": "...",
      "toolResponse": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "response": {
          "search_suggestions": "..."
        },
        "id": "a7b3k9p2"
      }
    }, {
      "functionCall": {
        "name": "getWeather",
        "args": {
          "city": "Utqiaġvik, Alaska"
        },
        "id": "m4q8z1v6"
      },
      "thoughtSignature": "..."
    }],
    "role": "model"
  }, {
    "parts": [{
      "functionResponse": {
        "name": "getWeather",
        "response": {
          "response": "Very cold. 22 degrees Fahrenheit."
        },
        "id": "m4q8z1v6"
      }
    }],
    "role": "user"
  }],
  "tools": [{
    "functionDeclarations": [{
      "name": "getWeather"
    }]
  }, {
    "googleSearch": {
    }
  }, {
    "codeExecution": {
    }
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}
```

## Tokenët dhe çmimet

Ki parasysh se pjesët `toolCall` dhe `toolResponse` në kërkesa llogariten për `prompt_token_count`. Duke qenë se këta hapa të ndërmjetëm të veglës tani janë të dukshëm dhe të kthehen ty, ata janë pjesë e historikut të bisedës. Kjo vlen vetëm për *kërkesat*, jo për *përgjigjet*.

Vegla e "Kërko në Google" është një përjashtim nga ky rregull. "Kërko në Google" e zbaton tashmë modelin e vet të çmimeve në nivel kërkese, kështu që tokenat nuk tarifohen dy herë (shiko faqen [Çmimet](https://ai.google.dev/gemini-api/docs/pricing?hl=sq)).

Lexo faqen [Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=sq) për më shumë informacion.

## Kufizimet

- Parazgjidhet modaliteti `VALIDATED` (modaliteti `AUTO` nuk mbështetet) kur
  aktivizohet flamuri `include_server_side_tool_invocations`
- Veglat e integruara si `google_search` mbështeten te informacionet e vendndodhjes dhe orës aktuale, kështu që nëse `system_instruction` ose `function_declaration.description` kanë informacione të papërputhshme të vendndodhjes dhe orës, veçoria e kombinimit të veglave mund të mos funksionojë mirë.

## Veglat e mbështetura

Qarkullimi standard i kontekstit të veglës zbatohet për veglat në anën e serverit (të integruara).
"Ekzekutimi i kodit" është gjithashtu një vegël nga ana e serverit, por ka zgjidhjen e vet të integruar për qarkullimin e kontekstit. "Përdorimi i kompjuterit" dhe thirrja e funksionit janë vegla në anën e klientit,
si dhe kanë zgjidhje të integruara për qarkullimin e kontekstit.

| Vegla | Ana e ekzekutimit | Context Circulation Support |
| --- | --- | --- |
| [Kërko në Google](https://ai.google.dev/gemini-api/docs/google-search?hl=sq) | Në anën e serverit | Mbështetet |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=sq) | Nga ana e serverit | Mbështetet |
| [Konteksti i URL-së](https://ai.google.dev/gemini-api/docs/url-context?hl=sq) | Nga ana e serverit | Mbështetet |
| [Kërkimi i skedarëve](https://ai.google.dev/gemini-api/docs/file-search?hl=sq) | Në anën e serverit | Mbështetet |
| [Ekzekutimi i kodit](https://ai.google.dev/gemini-api/docs/code-execution?hl=sq) | Në anën e serverit | Mbështetur (i integruar, përdor pjesë të `executableCode` dhe `codeExecutionResult`) |
| [Përdorimi i kompjuterit](https://ai.google.dev/gemini-api/docs/computer-use?hl=sq) | Në anën e klientit | Mbështetur (i integruar, përdor pjesë të `functionCall` dhe `functionResponse`) |
| [Funksionet e personalizuara](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq) | Nga ana e klientit | Mbështetur (i integruar, përdor pjesë të `functionCall` dhe `functionResponse`) |

## Çfarë ka më pas

- Mëso më shumë rreth [Thirrjes së funksionit](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq) në Gemini API.
- Eksploro veglat e mbështetura:
  - [Kërko në Google](https://ai.google.dev/gemini-api/docs/google-search?hl=sq)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=sq)
  - [Konteksti me URL](https://ai.google.dev/gemini-api/docs/url-context?hl=sq)
  - [Kërkimi i skedarëve](https://ai.google.dev/gemini-api/docs/file-search?hl=sq)

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-13 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-13 UTC."],[],[]]
