---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tool-combination?hl=de
fetched_at: 2026-08-24T02:21:59.026988+00:00
title: "Integrierte Tools und Funktionsaufrufe kombinieren \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Integrierte Tools und Funktionsaufrufe kombinieren

Mit Gemini können Sie die Kombination von [integrierten Tools](https://ai.google.dev/gemini-api/docs/tools?hl=de) wie `google_search` und [Funktionsaufrufen](https://ai.google.dev/gemini-api/docs/function-calling?hl=de) (auch als *benutzerdefinierte Tools* bezeichnet) in einer einzigen Generierung ermöglichen, indem der Kontextverlauf von Toolaufrufen beibehalten und verfügbar gemacht wird. Kombinationen aus integrierten und benutzerdefinierten Tools ermöglichen komplexe, agentenbasierte Workflows, bei denen sich das Modell beispielsweise auf Echtzeit-Webdaten stützen kann, bevor es Ihre spezifische Geschäftslogik aufruft.

Hier ein Beispiel, das Kombinationen aus integrierten und benutzerdefinierten Tools mit `google_search` und einer benutzerdefinierten Funktion `getWeather` ermöglicht:

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
    model="gemini-3.6-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather]       # Custom tool
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
    model="gemini-3.6-flash",
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
    const model = client.getGenerativeModel({
        model: "gemini-3.6-flash",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;

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

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });

    for (const part of result2.response.candidates[0].content.parts) {
        if (part.text) {
            console.log(part.text);
        }
    }
}

run();
```

### Ok

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

    model := client.GenerativeModel("gemini-3.6-flash")
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

## Funktionsweise

Gemini 3-Modelle verwenden die *Toolkontext-Zirkulation* , um Kombinationen aus integrierten und benutzerdefinierten Tools zu ermöglichen. Durch die Toolkontext-Zirkulation kann der Kontext von integrierten Tools beibehalten und verfügbar gemacht und in demselben Aufruf von Runde zu Runde mit benutzerdefinierten Tools geteilt werden.

### Toolkombination aktivieren

- Sie müssen das Flag `include_server_side_tool_invocations` auf `true` setzen, um die Toolkontext-Zirkulation zu aktivieren.
- Fügen Sie die [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#function-declarations) zusammen mit den
  integrierten Tools ein, die Sie verwenden möchten, um das Kombinationsverhalten auszulösen.
  - Wenn Sie `function_declarations` nicht einfügen, wirkt sich die Toolkontext-Zirkulation trotzdem auf die eingeschlossenen integrierten Tools aus, solange das Flag gesetzt ist.

### API gibt Teile zurück

In einer einzigen Antwort gibt die API die Teile `toolCall` und `toolResponse` für den Aufruf des integrierten Tools zurück. Für den Aufruf der Funktion (benutzerdefiniertes Tool) gibt die API den Aufrufteil `functionCall` zurück, für den der Nutzer in der nächsten Runde den Teil `functionResponse` bereitstellt.

- `toolCall` und `toolResponse`: Die API gibt diese Teile zurück, um den Kontext beizubehalten, welche Tools serverseitig ausgeführt werden, und das Ergebnis ihrer Ausführung für die nächste Runde.
- `functionCall` und `functionResponse`: Die API sendet den Funktionsaufruf an
  den Nutzer, damit er ihn ausfüllt, und der Nutzer sendet das Ergebnis in der
  Funktionsantwort zurück. Diese Teile sind für alle [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de) in der Gemini API Standard und nicht spezifisch für die
  Toolkombinationsfunktion.
- ([Nur Tool zur Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de))
  `executableCode` und `codeExecutionResult`:
  Wenn Sie das Tool zur Codeausführung verwenden, gibt die API anstelle von `functionCall` und
  `functionResponse` die Teile `executableCode` (der vom Modell generierte Code, der ausgeführt werden soll) und `codeExecutionResult` (das
  Ergebnis des ausführbaren Codes) zurück.

Sie müssen alle Teile, einschließlich aller darin enthaltenen [Felder](#critical-fields), in jeder Runde an das Modell zurückgeben, um den Kontext beizubehalten und Tool
kombinationen zu ermöglichen.

### Wichtige Felder in zurückgegebenen Teilen

Bestimmte [von der API zurückgegebene Teile](#api-returns-parts) enthalten die Felder `id`,
`tool_type`, und `thought_signature`. Diese Felder sind entscheidend für die Beibehaltung des Toolkontexts (und daher entscheidend für Toolkombinationen). Sie müssen alle Teile *genau wie in der Antwort angegeben* in Ihren nachfolgenden Anfragen zurückgeben.

- `id`: Eine eindeutige Kennung, die einen Aufruf seiner Antwort zuordnet. `id` wird **in
  allen Funktionsaufrufantworten festgelegt**, unabhängig von der Toolkontext-Zirkulation.
  Sie *müssen* in der Funktionsantwort dieselbe `id` angeben, die die API im Funktionsaufruf bereitstellt. Integrierte Tools teilen die `id` automatisch zwischen dem Toolaufruf und der Toolantwort.
  - In allen toolbezogenen Teilen enthalten: `toolCall`, `toolResponse`, `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: Gibt das verwendete Tool an, entweder das Literal des integrierten Tools (z.B. `URL_CONTEXT`) oder den Funktionsnamen (z.B. `getWeather`).
  - In den Teilen `toolCall` und `toolResponse` enthalten.
- `thought_signature`: Der tatsächliche verschlüsselte Kontext, der in **jedem von der API zurückgegebenen Teil** eingebettet ist. Ohne Thought Signatures kann der Kontext nicht wiederhergestellt werden. Wenn Sie die Thought Signatures für alle Teile nicht in jeder Runde zurückgeben, gibt das Modell einen Fehler aus.
  - In *allen* Teilen enthalten.

### Toolspezifische Daten

Einige integrierte Tools geben für den Nutzer sichtbare Datenargumente zurück, die für den Tooltyp spezifisch sind.

| Tool | Für den Nutzer sichtbare Toolaufrufargumente (falls vorhanden) | Für den Nutzer sichtbare Toolantwort (falls vorhanden) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` Zu durchsuchende URLs | `urls_metadata` `retrieved_url`: Durchsuchte URLs `url_retrieval_status`: Status der Suche |
| **FILE\_SEARCH** | Keine | Keine |

## Beispiel für die Anfragestruktur für Toolkombinationen

Die folgende Anfragestruktur zeigt die Anfragestruktur des Prompts: „Was ist die nördlichste Stadt in den Vereinigten Staaten? Wie ist das Wetter dort heute?“ Dabei werden drei Tools kombiniert: die integrierten Gemini-Tools `google_search` und `code_execution` sowie eine benutzerdefinierte Funktion `get_weather`.

```
{
  "model": "models/gemini-3.6-flash",
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

## Tokens und Preise

Die Teile `toolCall` und `toolResponse` in Anfragen werden auf `prompt_token_count` angerechnet. Da diese Zwischenschritte für Tools jetzt sichtbar sind und an Sie zurückgegeben werden, sind sie Teil des Unterhaltungsverlaufs. Dies gilt nur für den
Fall von *Anfragen*, nicht für *Antworten*.

Das Tool Google Suche ist eine Ausnahme von dieser Regel. Google Suche wendet bereits
ein eigenes Preismodell auf Abfrageebene an, sodass Tokens nicht
doppelt berechnet werden (siehe die [Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de)).

Weitere Informationen finden Sie auf der Seite [Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=de).

## Beschränkungen

- Standardmäßig wird der Modus `VALIDATED` verwendet (`AUTO` wird nicht unterstützt), wenn das Flag `include_server_side_tool_invocations` aktiviert ist.
- Integrierte Tools wie `google_search` verwenden Informationen zum Standort und zur aktuellen Uhrzeit. Wenn Ihre `system_instruction` oder `function_declaration.description` widersprüchliche Standort- und Zeitinformationen enthält, funktioniert die Toolkombinationsfunktion möglicherweise nicht richtig.

## Unterstützte Tools

Die standardmäßige Toolkontext-Zirkulation gilt für serverseitige (integrierte) Tools.
Die Codeausführung ist ebenfalls ein serverseitiges Tool, hat aber eine eigene integrierte Lösung für die Kontext-Zirkulation. Die Computernutzung und Funktionsaufrufe sind clientseitige Tools und haben ebenfalls integrierte Lösungen für die Kontext-Zirkulation.

| Tool | Ausführungsseite | Unterstützung der Kontext-Zirkulation |
| --- | --- | --- |
| [Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de) | Serverseitig | Unterstützt |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de) | Serverseitig | Unterstützt |
| [URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de) | Serverseitig | Unterstützt |
| [Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de) | Serverseitig | Unterstützt |
| [Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) | Serverseitig | Unterstützt (integriert, verwendet die Teile `executableCode` und `codeExecutionResult`) |
| [Computernutzung](https://ai.google.dev/gemini-api/docs/computer-use?hl=de) | Clientseitig | Unterstützt (integriert, verwendet die Teile `functionCall` und `functionResponse`) |
| [Benutzerdefinierte Funktionen](https://ai.google.dev/gemini-api/docs/function-calling?hl=de) | Clientseitig | Unterstützt (integriert, verwendet die Teile `functionCall` und `functionResponse`) |

## Nächste Schritte

- Weitere Informationen zu [Funktionsaufrufen](https://ai.google.dev/gemini-api/docs/function-calling?hl=de) in der Gemini API.
- Unterstützte Tools:
  - [Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de)
  - [URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de)
  - [Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
