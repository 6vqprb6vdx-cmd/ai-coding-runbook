---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=pt-BR
fetched_at: 2026-06-15T06:20:05.553091+00:00
title: "API Interactions: guia de migra\u00e7\u00e3o de mudan\u00e7as interruptivas (maio de 2026) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# API Interactions: guia de migração de mudanças interruptivas (maio de 2026)

A API Interactions `v1beta` está introduzindo mudanças interruptivas que reestruturam o formato da API para oferecer suporte a recursos futuros, como direcionamento em tempo real e chamadas de ferramentas assíncronas. Esta página explica o que está mudando e fornece exemplos de código antes e depois para ajudar na migração. Há duas categorias de mudanças:

1. [**Esquema de etapas**](#steps-schema): uma nova matriz `steps` substitui a matriz
   `outputs`, fornecendo uma linha do tempo estruturada de cada interação.
2. [**Configuração do formato de saída**](#output-format-config): um novo polimórfico
   `response_format` consolida todos os controles de formato de saída e remove
   `response_mime_type`.

Siga as etapas em [Como migrar para o novo esquema](#how-to-migrate) para
atualizar sua integração.

## Mudança principal: `outputs` para `steps`

O novo esquema substitui a matriz `outputs` por uma matriz `steps`.

- **Legado**: as respostas retornavam uma matriz `outputs` simples que continha apenas o conteúdo gerado do modelo.
- **Novo esquema**: as respostas retornam uma matriz `steps` que contém etapas estruturadas com discriminadores de tipo.

`POST /interactions` retorna apenas etapas de saída. `GET /interactions/{id}`
retorna a linha do tempo completa das etapas, incluindo a etapa `user_input` inicial.

### Entrada/saída básica (unária)

#### Antes (legado)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a joke."
  }'
```

```
// Response
{
  "id": "int_123",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "Why did the chicken cross the road?"
    }
  ]
}
```

#### Depois (novo esquema)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

// Response access (Recommended sugar)
console.log(interaction.output_text);
```

[sdk-convenience]: /gemini-api/docs/interactions#convenience-properties

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a joke."
  }'
```

```
// POST Response
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}

// GET /v1beta/interactions/int_123 (returns full timeline including input)
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "content": [
        { "type": "text", "text": "Tell me a joke." }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

### Chamadas de função

A estrutura da solicitação permanece inalterada, mas a resposta substitui o conteúdo `outputs` simples por etapas estruturadas.

#### Antes (legado)

### Python

```
# Accessing function call in legacy schema
for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Calling {output.name} with {output.arguments}")
```

### JavaScript

```
// Accessing function call in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Calling {output.name} with {JSON.stringify(output.arguments)}`);
    }
}
```

### REST

```
// Response
{
  "id": "int_001",
  "role": "model",
  "status": "requires_action",
  "outputs": [
    {
      "type": "thought",
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

#### Depois (novo esquema)

### Python

```
# Accessing function call in new steps schema
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Calling {step.name} with {step.arguments}")
```

### JavaScript

```
// Accessing function call in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Calling {step.name} with {JSON.stringify(step.arguments)}`);
    }
}
```

### REST

```
// POST Response
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "thought",
      "summary": [{
        "type": "text",
        "text": "I need to check the weather in Boston..."
      }],
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

### Ferramentas do lado do servidor

As ferramentas do lado do servidor (como a Pesquisa Google ou a execução de código) agora geram tipos de etapas específicos na matriz `steps`. Embora o esquema legado tenha retornado essas operações como tipos de conteúdo específicos na matriz `outputs`, o novo esquema as move para a matriz `steps`. Os exemplos a seguir usam a Pesquisa Google.

#### Antes (legado)

### Python

```
# Accessing search results in legacy schema
for output in interaction.outputs:
    if output.type == "google_search_call":
        print(f"Searched for: {output.arguments.queries}")
    elif output.type == "google_search_result":
        print(f"Found results: {output.result.rendered_content}")
```

### JavaScript

```
// Accessing search results in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'google_search_call') {
        console.log(`Searched for: {output.arguments.queries}`);
    } else if (output.type === 'google_search_result') {
        console.log(`Found results: {output.result.renderedContent}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// Response
{
  "id": "int_456",
  "outputs": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] }
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "rendered_content": "<div>...</div>",
        "url": "https://www.nfl.com/super-bowl"
      }
    },
    {
      "type": "text",
      "text": "The Kansas City Chiefs won the last Super Bowl.",
      "annotations": [
        {
          "start_index": 4,
          "end_index": 22,
          "source": "https://www.nfl.com/super-bowl"
        }
      ]
    }
  ],
  "status": "completed"
}
```

#### Depois (novo esquema)

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result.search_suggestions}")
```

### JavaScript

```
// Accessing search results in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'google_search_call') {
        console.log(`Searched for: {step.arguments.queries}`);
    } else if (step.type === 'google_search_result') {
        console.log(`Found results: {step.result.searchSuggestions}`);
    }
}
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// POST Response
{
  "id": "int_456",
  "steps": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] },
      "signature": "abc123..."
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "search_suggestions": "<div>...</div>"
      },
      "signature": "abc123..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The Kansas City Chiefs won the last Super Bowl.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.nfl.com/super-bowl",
              "title": "NFL.com",
              "start_index": 4,
              "end_index": 22
            }
          ]
        }
      ]
    }
  ],
  "status": "completed"
}
```

### Streaming

O streaming expõe novos tipos de eventos:

#### Novos tipos de evento

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### Tipos de evento descontinuados

Os seguintes tipos de eventos legados são substituídos pelos novos eventos listados acima:

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → substituído por `interaction.in_progress`, `interaction.requires_action` etc.

**Chamadas de função de streaming**: quando você usa o streaming com a chamada de função,
o evento `step.start` entrega o nome da função, e os eventos `step.delta` transmitem
os argumentos como strings JSON parciais (usando `arguments_delta`). É
necessário acumular esses deltas para receber os argumentos completos. Isso é diferente das chamadas unárias, em que você recebe o objeto de chamada de função completo de uma só vez.

#### Exemplos

##### Antes (legado)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain quantum entanglement in simple terms.",
    stream=True,
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
```

### JavaScript

```
// Legacy streaming used content.delta
const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Explain quantum entanglement in simple terms.',
    stream: true,
});

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text') {
            process.stdout.write(chunk.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain quantum entanglement in simple terms.",
    "stream": true
  }'
```

```
// Response (SSE Lines)
// event: interaction.start
// data: {"id": "int_123", "status": "in_progress"}
//
// event: content.start
// data: {"index": 0, "type": "text"}
//
// event: content.delta
// data: {"delta": {"type": "text", "text": "Quantum entanglement is..."}}
//
// event: content.stop
// data: {"index": 0}
//
// event: interaction.complete
// data: {"id": "int_123", "status": "done", "usage": {"total_tokens": 42}}
```

##### Depois (novo esquema)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.5-flash",
    input="Tell me a story.",
    stream=True,
):
    if event.type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a story.',
    stream: true,
});

for await (const event of stream) {
    if (event.type === 'step.delta') {  // CHANGED: step.delta instead of content.delta
        if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
 # Opt-in needed before May 26th
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "Accept: text/event-stream" \
   -H "Api-Revision: 2026-05-20" \
   -d '{
     "model": "gemini-3.5-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.5-flash"}, "event_type": "interaction.created"}
 //
 // event: interaction.in_progress
 // data: {"interaction_id": "int_xyz", "event_type": "interaction.in_progress"}
 //
 // event: step.start
 // data: {"index": 0, "step": {"type": "thought", "signature": "abc123..."}, "event_type": "step.start"}
 //
 // event: step.stop
 // data: {"index": 0, "event_type": "step.stop"}
 //
 // event: step.start
 // data: {"index": 1, "step": {"content": [{"text": "Once upon", "type": "text"}], "type": "model_output"}, "event_type": "step.start"}
 //
 // event: step.delta
 // data: {"index": 1, "delta": {"text": " a time...", "type": "text"}, "event_type": "step.delta"}
 //
 // event: step.stop
 // data: {"type": "step.stop", "index": 1, "status": "done"}
 //
 // event: interaction.completed
 // data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}} // NEW: Dedicated completion event
```

### Histórico de conversas sem estado

Se você gerenciar o histórico de conversas manualmente no lado do cliente (caso de uso sem estado), será necessário atualizar a forma como você encadeia as conversas anteriores.

- **Legado**: os desenvolvedores geralmente coletavam a matriz `outputs` das respostas e as enviavam de volta no campo `input` na próxima conversa.
- **Novo esquema**: agora é necessário coletar a matriz `steps` da resposta e transmiti-la no campo `input` da próxima solicitação, anexando a nova conversa do usuário como uma etapa `user_input`.

## Configuração do formato de saída: mudanças em `response_format`

A API atualizada consolida todos os controles de formato de saída em um campo `response_format` unificado e polimórfico. Isso centraliza a configuração de saída no nível superior e mantém `generation_config` focado no comportamento do modelo (como temperatura, top\_p e pensamento).

### Mudanças importantes

- **A API remove `response_mime_type`.** Agora você especifica o tipo MIME por entrada de formato dentro de `response_format`.
- **`response_format` agora é um objeto polimórfico (ou matriz).** Cada entrada tem um discriminador de `type` (`text`, `audio`, `image`) e campos específicos do tipo. Para solicitar várias modalidades de saída, transmita uma matriz de entradas de formato.
- **`image_config` é movido de `generation_config` para `response_format`.**
  Agora você especifica as configurações de saída de imagem, como `aspect_ratio` e `image_size`
  em uma entrada `response_format` com `"type": "image"`.

### Saída estruturada (JSON)

O novo esquema remove o campo `response_mime_type`. Em vez disso, especifique o
tipo MIME e o esquema JSON dentro de um `response_format` objeto com
`"type": "text"`.

#### Antes (legado)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Summarize this article.",
    response_mime_type="application/json",
    response_format={
        "type": "object",
        "properties": {
            "summary": {"type": "string"}
        }
    },
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Summarize this article.',
    response_mime_type: 'application/json',
    response_format: {
        type: 'object',
        properties: {
            summary: { type: 'string' }
        }
    },
});

console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Summarize this article.",
    "response_mime_type": "application/json",
    "response_format": {
      "type": "object",
      "properties": {
        "summary": { "type": "string" }
      }
    }
  }'
```

#### Depois (novo esquema)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Summarize this article.",
    # response_mime_type is removed — specify mime_type inside response_format
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string"}
            }
        }
    },
)

# Print response
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Summarize this article.',
    // response_mime_type is removed — specify mime_type inside response_format
    response_format: {
        type: 'text',
        mime_type: 'application/json',
        schema: {
            type: 'object',
            properties: {
                summary: { type: 'string' }
            }
        }
    },
});

// Print response
console.log(interaction.output_text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Summarize this article.",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "summary": { "type": "string" }
        }
      }
    }
  }'
```

### Configuração de imagem

O novo esquema remove `image_config` de `generation_config`. Agora você especifica
as configurações de saída de imagem em uma entrada `response_format` com `"type": "image"`.

#### Antes (legado)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Generate an image of a sunset over the ocean.",
    generation_config={
        "image_config": {
            "aspect_ratio": "1:1",
            "image_size": "1K"
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Generate an image of a sunset over the ocean.',
    generation_config: {
        image_config: {
            aspect_ratio: '1:1',
            image_size: '1K'
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### Depois (novo esquema)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Generate an image of a sunset over the ocean.",
    # image_config is removed from generation_config — use response_format
    response_format={
        "type": "image",
        "mime_type": "image/jpeg",
        "aspect_ratio": "1:1",
        "image_size": "1K"
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Generate an image of a sunset over the ocean.',
    // image_config is removed from generation_config — use response_format
    response_format: {
        type: 'image',
        mime_type: 'image/jpeg',
        aspect_ratio: '1:1',
        image_size: '1K'
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

Para solicitar várias modalidades de saída (por exemplo, texto e áudio juntos), transmita uma matriz de entradas de formato para `response_format` em vez de um único objeto.

## Como migrar para o novo esquema

### Usuários do SDK

Faça upgrade para a versão mais recente do SDK (Python 2.0.0 e versões posteriores, JavaScript 2.0.0 e versões posteriores). O SDK ativa automaticamente o novo esquema. Não é necessário mudar o código além de atualizar a forma como você lê as respostas (consulte os exemplos acima). Somente o novo esquema é compatível com essas versões do SDK. As versões mais antigas do SDK (Python 1.x.x, JavaScript 1.x.x) vão continuar funcionando até que o esquema legado seja removido em **8 de junho de 2026**.

### Usuários da API REST

Adicione o cabeçalho `Api-Revision: 2026-05-20` às suas solicitações para ativar o novo esquema agora. Após **26 de maio**, o novo esquema se torna o padrão para todas as
solicitações. Você pode desativar temporariamente com `Api-Revision: 2026-05-07`
até **8 de junho**, quando a API remover permanentemente o esquema legado.

### Cronograma

| Data | Fase | Usuários do SDK | Usuários da API REST |
| --- | --- | --- | --- |
| **7 de maio** | Ativar | Nova versão do SDK disponível (Python 2.0.0 e versões posteriores, JS 2.0.0 e versões posteriores). Faça upgrade para receber o novo esquema automaticamente. | Adicione o cabeçalho `Api-Revision: 2026-05-20` para ativar. O padrão permanece legado. |
| **26 de maio** | Inversão padrão | Nenhuma ação necessária se já tiver feito upgrade. Os SDKs mais antigos (Python 1.x.x, JS 1.x.x) ainda funcionam, mas retornam respostas legadas. | O novo esquema agora é o padrão. Envie o cabeçalho `Api-Revision: 2026-05-07` para desativar. |
| **8 de junho** | Pôr do sol | As versões do SDK Python 1.x.x e JS 1.x.x vão falhar nas chamadas da API Interactions. | Esquema legado removido para a API Interactions. Cabeçalho `Api-Revision` ignorado. |

## Lista de verificação de migração

### Esquema de etapas (`steps`)

- Atualize o código para ler o conteúdo da resposta da matriz `steps` em vez de `outputs`. [Confira exemplos](#basic-unary).
- Verifique se o código processa os tipos de etapa `user_input` e `model_output`. [Confira exemplos](#basic-unary).
- (Chamada de função) Atualize o código para encontrar etapas `function_call` na matriz `steps`. [Confira exemplos](#function-calling).
- (Ferramentas do lado do servidor) Atualize o código para processar etapas específicas da ferramenta (por exemplo, `google_search_call`, `google_search_result`). [Confira exemplos](#server-side-tools).
- (Histórico sem estado) Atualize o gerenciamento do histórico para transmitir a matriz `steps` no campo `input` da próxima solicitação. [Confira os detalhes](#stateless-history).
- (Somente streaming) Atualize o cliente para detectar novos tipos de eventos SSE (`interaction.created`, `step.delta` etc.). [Confira exemplos](#streaming).

### Configuração do formato de saída (`response_format`)

- Substitua `response_mime_type` por um campo `mime_type` dentro de `response_format`. [Confira exemplos](#structured-output).
- Inclua o esquema JSON `response_format` atual em um objeto `{"type": "text", "schema": ...}`. [Confira exemplos](#structured-output).
- (Geração de imagens) Mova `image_config` de `generation_config` para uma entrada `{"type": "image", ...}` em `response_format`. [Confira exemplos](#image-config).
- (Multimodal) Converta `response_format` de um único objeto para uma matriz ao solicitar várias modalidades de saída.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-01 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-01 UTC."],[],[]]
