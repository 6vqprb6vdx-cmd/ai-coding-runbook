---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419
fetched_at: 2026-06-22T06:27:26.158227+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Combina herramientas integradas y llamadas a funciones

Gemini permite combinar [herramientas integradas](https://ai.google.dev/gemini-api/docs/tools?hl=es-419), como `google_search`, y [llamadas a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) (también conocidas como *herramientas personalizadas*) en una sola generación, ya que conserva y expone el historial de contexto de las llamadas a herramientas. Las combinaciones de herramientas integradas y personalizadas permiten flujos de trabajo complejos y basados en agentes en los que, por ejemplo, el modelo puede fundamentarse en datos web en tiempo real antes de llamar a tu lógica empresarial específica.

Este es un ejemplo que habilita combinaciones de herramientas integradas y personalizadas con `google_search` y una función personalizada `getWeather`:

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
    model="gemini-3.5-flash",
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
    model="gemini-3.5-flash",
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
        model: "gemini-3.5-flash",
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

    model := client.GenerativeModel("gemini-3.5-flash")
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

## Cómo funciona

Los modelos de Gemini 3 usan la *circulación de contexto de herramientas* para habilitar combinaciones de herramientas integradas y personalizadas. La circulación del contexto de la herramienta permite conservar y exponer el contexto de las herramientas integradas, y compartirlo con las herramientas personalizadas en la misma llamada de un turno a otro.

### Habilita la combinación de herramientas

- Debes establecer la marca `include_server_side_tool_invocations` en `true` para habilitar la circulación del contexto de la herramienta.
- Incluye el [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#function-declarations), junto con las herramientas integradas que quieras usar, para activar el comportamiento de combinación.
  - Si no incluyes `function_declarations`, la circulación del contexto de la herramienta seguirá actuando sobre las herramientas integradas incluidas, siempre y cuando se establezca la marca.

### La API devuelve partes

En una sola respuesta, la API devuelve las partes `toolCall` y `toolResponse` para la llamada a la herramienta integrada. Para la llamada a la función (herramienta personalizada), la API devuelve la parte de la llamada `functionCall`, a la que el usuario proporciona la parte `functionResponse` en el siguiente turno.

- `toolCall` y `toolResponse`: La API devuelve estas partes para conservar el contexto de qué herramientas se ejecutan en el servidor y el resultado de su ejecución para el siguiente turno.
- `functionCall` y `functionResponse`: La API envía la llamada a la función para que el usuario la complete, y el usuario devuelve el resultado en la respuesta de la función (estas partes son estándar para todas las [llamadas a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) en la API de Gemini, no son exclusivas de la función de combinación de herramientas).
- (Solo para la herramienta [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419)) `executableCode` y `codeExecutionResult`:
  Cuando se usa la herramienta Ejecución de código, en lugar de `functionCall` y `functionResponse`, la API devuelve `executableCode` (el código generado por el modelo que se debe ejecutar) y `codeExecutionResult` (el resultado del código ejecutable).

Debes devolver todas las partes, incluidos todos los [campos](#critical-fields) que contienen, al modelo en cada turno para mantener el contexto y habilitar las combinaciones de herramientas.

### Campos críticos en las piezas devueltas

Algunas [partes que devuelve la API](#api-returns-parts) incluirán los campos `id`, `tool_type` y `thought_signature`. Estos campos son fundamentales para mantener el contexto de la herramienta (y, por lo tanto, para las combinaciones de herramientas). Debes devolver todas las partes *tal como se indican en la respuesta* en tus solicitudes posteriores.

- `id`: Es un identificador único que asigna una llamada a su respuesta. `id` se **establece en todas las respuestas de llamadas a funciones**, independientemente de la circulación del contexto de la herramienta.
  *Debes* proporcionar el mismo `id` en la respuesta de la función que la API proporciona en la llamada a función. Las herramientas integradas comparten automáticamente el `id` entre la llamada a la herramienta y la respuesta de la herramienta.
  - Se encuentra en todas las partes relacionadas con herramientas: `toolCall`, `toolResponse`, `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: Identifica la herramienta específica que se usa; el nombre literal de la herramienta integrada (p.ej., `URL_CONTEXT`) o de la función (p.ej., `getWeather`).
  - Se encuentra en las partes `toolCall` y `toolResponse`.
- `thought_signature`: Es el contexto encriptado real incorporado en **cada parte que devuelve la API**. El contexto no se puede reconstruir sin firmas de pensamiento. Si no devuelves las firmas de pensamiento de todas las partes en cada turno, el modelo mostrará un error.
  - Se encuentra en *todas* las partes.

### Datos específicos de la herramienta

Algunas herramientas integradas devuelven argumentos de datos visibles para el usuario que son específicos del tipo de herramienta.

| Herramienta | Argumentos de la llamada a la herramienta visibles para el usuario (si hay alguno) | Respuesta de la herramienta visible para el usuario (si corresponde) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` URLs que se explorarán | `urls_metadata` `retrieved_url`: URLs navegadas `url_retrieval_status`: Estado de navegación |
| **FILE\_SEARCH** | Ninguno | Ninguno |

## Ejemplo de estructura de solicitud de combinación de herramientas

La siguiente estructura de solicitud muestra la estructura de la instrucción: "¿Cuál es la ciudad más septentrional de Estados Unidos? ¿Cómo está el clima hoy?". Combina tres herramientas: las herramientas integradas de Gemini `google_search`
y `code_execution`, y una función personalizada `get_weather`.

```
{
  "model": "models/gemini-3.5-flash",
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

## Tokens y precios

Ten en cuenta que las partes `toolCall` y `toolResponse` de las solicitudes se incluyen en el recuento de `prompt_token_count`. Dado que estos pasos intermedios de la herramienta ahora son visibles y se te devuelven, forman parte del historial de conversación. Esto solo se aplica a las *solicitudes*, no a las *respuestas*.

La herramienta de la Búsqueda de Google es una excepción a esta regla. La Búsqueda de Google ya aplica su propio modelo de precios a nivel de la búsqueda, por lo que no se cobra doble por los tokens (consulta la página [Precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419)).

Lee la página [Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) para obtener más información.

## Limitaciones

- Se establece el modo `VALIDATED` de forma predeterminada (el modo `AUTO` no admitido) cuando la marca `include_server_side_tool_invocations` está habilitada.
- Las herramientas integradas, como `google_search`, dependen de la información de la ubicación y la hora actual, por lo que, si tu `system_instruction` o `function_declaration.description` tienen información de ubicación y hora contradictoria, es posible que la función de combinación de herramientas no funcione bien.

## Herramientas compatibles

La circulación estándar del contexto de la herramienta se aplica a las herramientas del servidor (integradas).
Code Execution también es una herramienta del servidor, pero tiene su propia solución integrada para la circulación del contexto. El uso de la computadora y la llamada a funciones son herramientas del cliente y también tienen soluciones integradas para la circulación del contexto.

| Herramienta | Lado de ejecución | Asistencia para la circulación de contexto |
| --- | --- | --- |
| [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419) | Del lado del servidor | Compatible |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419) | Del lado del servidor | Compatible |
| [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419) | Del lado del servidor | Compatible |
| [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419) | Del lado del servidor | Compatible |
| [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) | Del lado del servidor | Compatible (integrado, usa piezas `executableCode` y `codeExecutionResult`) |
| [Uso de la computadora](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419) | Del lado del cliente | Compatible (integrado, usa piezas `functionCall` y `functionResponse`) |
| [Funciones personalizadas](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) | Del lado del cliente | Compatible (integrado, usa piezas `functionCall` y `functionResponse`) |

## ¿Qué sigue?

- Obtén más información sobre la [llamada a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) en la API de Gemini.
- Explora las herramientas compatibles:
  - [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419)
  - [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419)
  - [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-19 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-19 (UTC)"],[],[]]
