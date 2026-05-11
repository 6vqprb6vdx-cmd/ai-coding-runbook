---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-BR
fetched_at: 2026-05-11T12:32:44.940130+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Combinar ferramentas integradas e chamada de função

O Gemini permite a combinação de [ferramentas integradas](https://ai.google.dev/gemini-api/docs/tools?hl=pt-br), como `google_search`, e [chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) (também conhecida como *ferramentas personalizadas*) em uma única geração, preservando e expondo o histórico de contexto das chamadas de ferramenta. As combinações de ferramentas integradas e personalizadas permitem fluxos de trabalho complexos e de agentes em que, por exemplo, o modelo pode se basear em dados da Web em tempo real antes de chamar sua lógica de negócios específica.

Confira um exemplo que permite combinações de ferramentas integradas e personalizadas com `google_search` e uma função personalizada `getWeather`:

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
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

for part in response.candidates[0].content.parts:
    if part.tool_call:
        print(f"Tool call: {part.tool_call.tool_type} (ID: {part.tool_call.id})")
    if part.tool_response:
        print(f"Tool response: {part.tool_response.tool_type} (ID: {part.tool_response.id})")
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")

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
                id=response.candidates[0].content.parts[2].function_call.id # Match the ID from the function_call
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      # This flag needs to be enabled for built-in tool context circulation and tool combination
      include_server_side_tool_invocations=True
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
        model: "gemini-3-flash-preview",
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
        if (part.toolCall) {
            console.log(`Tool call: ${part.toolCall.toolType} (ID: ${part.toolCall.id})`);
        }
        if (part.toolResponse) {
            console.log(`Tool response: ${part.toolResponse.toolType} (ID: ${part.toolResponse.id})`);
        }
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

    model := client.GenerativeModel("gemini-3-flash-preview")
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
        case genai.ToolCallPart:
            fmt.Printf("Tool call: %s (ID: %s)\n", p.ToolType, p.ID)
        case genai.ToolResponsePart:
            fmt.Printf("Tool response: %s (ID: %s)\n", p.ToolType, p.ID)
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

## Como funciona

Os modelos Gemini 3 usam a *circulação de contexto de ferramentas* para permitir combinações de ferramentas integradas e personalizadas. A circulação de contexto de ferramentas possibilita preservar e expor o contexto de ferramentas integradas e compartilhá-lo com ferramentas personalizadas na mesma chamada de turno a turno.

### Ativar a combinação de ferramentas

- Defina a flag `include_server_side_tool_invocations` como `true` para ativar a circulação de contexto de ferramentas.
- Inclua os [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br#function-declarations), junto com as
  ferramentas integradas que você quer usar, para acionar o comportamento de combinação.
  - Se você não incluir `function_declarations`, a circulação de contexto de ferramentas ainda vai agir nas ferramentas integradas incluídas, desde que a flag esteja definida.

### A API retorna partes

Em uma única resposta, a API retorna as partes `toolCall` e `toolResponse` para a chamada de ferramenta integrada. Para a chamada de função (ferramenta personalizada), a API retorna a parte de chamada `functionCall`, à qual o usuário fornece a parte `functionResponse` no próximo turno.

- `toolCall` e `toolResponse`: a API retorna essas partes para preservar o contexto de quais ferramentas são executadas no lado do servidor e o resultado da execução delas para o próximo turno.
- `functionCall` e `functionResponse`: a API envia a chamada de função para
  o usuário preencher, e o usuário envia o resultado de volta na
  resposta da função. Essas partes são padrão para todas as [chamadas de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) na API Gemini, não exclusivas do
  recurso de combinação de ferramentas.
- ([Somente ferramenta de](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br)execução de código)
  `executableCode` e `codeExecutionResult`:
  ao usar a ferramenta de execução de código, em vez de `functionCall` e
  `functionResponse`, a API retorna `executableCode` (o código gerado
  pelo modelo que deve ser executado) e `codeExecutionResult` (o
  resultado do código executável).

É necessário retornar todas as partes, incluindo todos os [campos](#critical-fields) que elas
contêm, ao modelo em cada turno para manter o contexto e ativar combinações de ferramentas.

### Campos críticos em partes retornadas

Algumas [partes retornadas pela API](#api-returns-parts) incluem os campos `id`,
`tool_type` e `thought_signature`. Esses campos são essenciais para manter o contexto da ferramenta (e, portanto, para combinações de ferramentas). É necessário retornar todas as partes *conforme fornecidas na resposta* nas solicitações subsequentes.

- `id`: um identificador exclusivo que mapeia uma chamada para a resposta. `id` é **definido em
  todas as respostas de chamada de função**, independentemente da circulação de contexto de ferramentas.
  Você *precisa* fornecer o mesmo `id` na resposta da função que a API fornece na chamada de função. As ferramentas integradas compartilham automaticamente o `id` entre a chamada e a resposta da ferramenta.
  - Encontrado em todas as partes relacionadas à ferramenta: `toolCall`, `toolResponse`, `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: identifica a ferramenta específica que está sendo usada, a ferramenta integrada literal ou (por exemplo, `URL_CONTEXT`) ou o nome da função (por exemplo, `getWeather`).
  - Encontrado nas partes `toolCall` e `toolResponse`.
- `thought_signature`: o contexto criptografado real incorporado em **cada parte retornada pela API**. O contexto não pode ser reconstruído sem assinaturas de pensamento. Se você não retornar as assinaturas de pensamento para todas as partes em cada turno, o modelo vai gerar um erro.
  - Encontrado em *todas* as partes.

### Dados específicos da ferramenta

Algumas ferramentas integradas retornam argumentos de dados visíveis ao usuário específicos do tipo de ferramenta.

| Ferramenta | Argumentos de chamada de ferramenta visíveis ao usuário (se houver) | Resposta da ferramenta visível ao usuário (se houver) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` URLs a serem navegados | `urls_metadata` `retrieved_url`: URLs navegados `url_retrieval_status`: status de navegação |
| **FILE\_SEARCH** | Nenhum | Nenhum |

## Exemplo de estrutura de solicitação de combinação de ferramentas

A estrutura de solicitação a seguir mostra a estrutura da solicitação: "Qual é a cidade mais ao norte dos Estados Unidos? Como está o clima lá hoje?". Ela combina três ferramentas: as ferramentas integradas do Gemini `google_search` e `code_execution`, e uma função personalizada `get_weather`.

```
{
  "model": "models/gemini-3-flash-preview",
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

## Tokens e preços

Observe que as partes `toolCall` e `toolResponse` nas solicitações são contadas para `prompt_token_count`. Como essas etapas intermediárias da ferramenta agora estão visíveis e são retornadas a você, elas fazem parte do histórico de conversas. Isso só acontece com o
caso para *solicitações*, não *respostas*.

A ferramenta Pesquisa Google é uma exceção a essa regra. A Pesquisa Google já
aplica o próprio modelo de preços no nível da consulta, então os tokens não são
cobrados duas vezes (consulte a página de [Preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br)).

Leia a página de [tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) para mais informações.

## Limitações

- O modo `VALIDATED` é o padrão (o modo `AUTO` não é compatível) quando a flag `include_server_side_tool_invocations` está ativada.
- As ferramentas integradas, como `google_search`, dependem de informações de localização e hora atual. Portanto, se a `system_instruction` ou `function_declaration.description` tiver informações de localização e hora conflitantes, o recurso de combinação de ferramentas poderá não funcionar bem.

## Ferramentas compatíveis

A circulação de contexto de ferramentas padrão se aplica a ferramentas do lado do servidor (integradas).
A execução de código também é uma ferramenta do lado do servidor, mas tem a própria solução integrada para a circulação de contexto. O uso do computador e a chamada de função são ferramentas do lado do cliente e também têm soluções integradas para a circulação de contexto.

| Ferramenta | Lado de execução | Suporte à circulação de contexto |
| --- | --- | --- |
| [Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br) | do lado do servidor | Compatível |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br) | do lado do servidor | Compatível |
| [Contexto do URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br) | do lado do servidor | Compatível |
| [Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br) | do lado do servidor | Compatível |
| [Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br) | do lado do servidor | Compatível (integrado, usa as partes `executableCode` e `codeExecutionResult`) |
| [Uso do computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br) | Lado do cliente | Compatível (integrado, usa as partes `functionCall` e `functionResponse`) |
| [Funções personalizadas](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) | Lado do cliente | Compatível (integrado, usa as partes `functionCall` e `functionResponse`) |

## A seguir

- Saiba mais sobre [a chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) na API Gemini.
- Conheça as ferramentas compatíveis:
  - [Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br)
  - [Contexto do URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br)
  - [Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br)

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-07 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-07 UTC."],[],[]]
