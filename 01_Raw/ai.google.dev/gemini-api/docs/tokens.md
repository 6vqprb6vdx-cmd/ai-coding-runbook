---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=pt-BR
fetched_at: 2026-10-19T05:39:52.662088+00:00
title: "Entender e contar tokens \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Entender e contar tokens

O Gemini e outros modelos de IA generativa processam a entrada e a saída em uma granularidade chamada *token*.

**Para os modelos do Gemini, um token equivale a cerca de quatro caracteres.
100 tokens equivalem a cerca de 60 a 80 palavras em inglês.**

## Sobre os tokens

Os tokens podem ser caracteres únicos, como `z`, ou palavras inteiras, como `cat`. Palavras longas são divididas em vários tokens. O conjunto de todos os tokens usados pelo modelo é chamado de vocabulário, e o processo de divisão do texto em tokens é chamado de *tokenização*.

Quando o faturamento está ativado, o [custo de uma chamada para a API Gemini](https://ai.google.dev/pricing?hl=pt-br) é
determinado em parte pelo número de tokens de entrada e saída. Portanto, saber como
contar tokens pode ser útil.

## Contar tokens

Toda entrada e saída da API Gemini é tokenizada, incluindo texto, arquivos de imagem e outras modalidades não textuais.

É possível contar tokens das seguintes maneiras:

- **Chame `count_tokens` com a entrada da solicitação.** Retorna o número total de tokens *somente na entrada*. Faça essa chamada antes de enviar a entrada para verificar o tamanho das solicitações.
- **Use o `usage` na resposta de interação.** Retorna contagens de tokens para entrada (`total_input_tokens`), saída (`total_output_tokens`), pensamento (`total_thought_tokens`), conteúdo armazenado em cache (`total_cached_tokens`), uso de ferramentas (`total_tool_use_tokens`) e total (`total_tokens`).

### Contar tokens de texto

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
const countResponse = await client.models.countTokens({
    model: "gemini-3.8-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.CountTokensResponse;

Client client = new Client();
String prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
CountTokensResponse countResponse =
    client.models.countTokens("gemini-3.8-flash", prompt, null);
System.out.println("total_tokens: " + countResponse.totalTokens().orElse(0));

// Get usage from interaction
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.usage().orElse(null));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    modelInfo, err := client.Models.Get(ctx, "gemini-3.8-flash", nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Input token limit: %d\n", modelInfo.InputTokenLimit)
    fmt.Printf("Output token limit: %d\n", modelInfo.OutputTokenLimit)
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### Contar tokens de várias rodadas

Conte os tokens no histórico de conversas usando `previous_interaction_id`:

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's my name?",
    previous_interaction_id=interaction1.id
)

# Usage includes tokens from both turns
print(f"Input tokens: {interaction2.usage.total_input_tokens}")
print(f"Output tokens: {interaction2.usage.total_output_tokens}")
print(f"Total tokens: {interaction2.usage.total_tokens}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// First interaction
const interaction1 = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Usage;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// First interaction
CreateModelInteraction params1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Hi, my name is Bob"))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();

// Second interaction continues the conversation
CreateModelInteraction params2 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What's my name?"))
        .previousInteractionId(interaction1.id().orElse(""))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();

// Usage includes tokens from both turns
if (interaction2.usage().isPresent()) {
  Usage usage = interaction2.usage().get();
  System.out.println("Input tokens: " + usage.totalInputTokens().orElse(0));
  System.out.println("Output tokens: " + usage.totalOutputTokens().orElse(0));
  System.out.println("Total tokens: " + usage.totalTokens().orElse(0));
}
```

### Go

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

    prompt := "The quick brown fox jumps over the lazy dog."

    // Count input tokens before sending
    totalTokens, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", genai.Text(prompt), nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("total_tokens: %d\n", totalTokens.TotalTokens)

    // Create the interaction and inspect the returned usage metadata
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(prompt),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
    if interaction.Usage != nil {
        if interaction.Usage.TotalInputTokens != nil {
            fmt.Printf("Input tokens: %d\n", *interaction.Usage.TotalInputTokens)
        }
        if interaction.Usage.TotalOutputTokens != nil {
            fmt.Printf("Output tokens: %d\n", *interaction.Usage.TotalOutputTokens)
        }
        if interaction.Usage.TotalThoughtTokens != nil {
            fmt.Printf("Thought tokens: %d\n", *interaction.Usage.TotalThoughtTokens)
        }
        if interaction.Usage.TotalTokens != nil {
            fmt.Printf("Total tokens: %d\n", *interaction.Usage.TotalTokens)
        }
    }
}
```

### Contar tokens multimodais

Toda entrada da API Gemini é tokenizada, incluindo imagens, vídeo e áudio.
Principais pontos sobre a tokenização:

- **Imagens**: imagens ≤384 pixels em ambas as dimensões contam como 258 tokens. Imagens maiores são divididas em blocos de 768 x 768 pixels, cada um contando como 258 tokens.
- **Vídeo**: 263 tokens por segundo (aplicável ao processamento estático). Para o processamento de agentes, o uso de tokens varia. Consulte
  [Uso de tokens de vídeo por modo de processamento](#video-token-usage).
- **Áudio**: 32 tokens por segundo

#### Tokens de imagem

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Tell me about this image"},
        {"type": "image", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type}
    ]
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const uploadedFile = await client.files.upload({
    file: "path/to/image.jpg",
    config: { mimeType: "image/jpeg" }
});

// Count tokens
const countResponse = await client.models.countTokens({
    model: "gemini-3.8-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.Content;
import com.google.genai.types.CountTokensResponse;
import com.google.genai.types.File;
import com.google.genai.types.Part;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;

Client client = new Client();

File uploadedFile =
    client.files.upload(
        new java.io.File("path/to/image.jpg"),
        UploadFileConfig.builder().mimeType("image/jpeg").build());

// Count tokens for image + text
CountTokensResponse countResponse =
    client.models.countTokens(
        "gemini-3.8-flash",
        Arrays.asList(
            Content.fromParts(
                Part.fromText("Tell me about this image"),
                Part.fromUri(
                    uploadedFile.uri().orElse(""), uploadedFile.mimeType().orElse("image/jpeg")))),
        null);
System.out.println("Total tokens: " + countResponse.totalTokens().orElse(0));

// Generate with image
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text("Tell me about this image").build(),
                    ImageContent.builder()
                        .uri(uploadedFile.uri().orElse(""))
                        .mimeType(
                            ImageContentMimeType.of(uploadedFile.mimeType().orElse("image/jpeg")))
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.usage().orElse(null));
```

### Go

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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:  interactions.Model("gemini-3.8-flash"),
            Input:  interactions.NewInteractionsInput("Explain the history of the internet in 3 paragraphs."),
            Stream: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        }
        if completed := event.GetDataInteractionCompleted(); completed != nil {
            usage := completed.Interaction.Usage
            if usage != nil && usage.TotalTokens != nil {
                fmt.Printf("\nTotal tokens: %d\n", *usage.TotalTokens)
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

**Exemplo de dados inline:**

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.usage)
```

#### Tokens de vídeo

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 100 * 60 = 6,000 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### Uso de tokens de vídeo por modo de processamento

O uso de tokens para vídeo depende do modo de processamento:

| **Modo de processamento** | **Cálculo de tokens** | **Uso normal** |
| --- | --- | --- |
| **Estático** (padrão) | ~100 tokens/segundo por padrão (baixa resolução) ou ~300 tokens/segundo (alta resolução). Todos os frames são amostrados a 1 FPS. | Previsível, proporcional à duração do vídeo. |
| **De agente** | Varia de acordo com a complexidade do conteúdo. O modelo carrega apenas a transcrição e/ou os frames e/ou o áudio necessários para responder ao comando. | Até 88% menos tokens para conteúdo longo. |

Com o processamento de agentes, uma palestra de 1 hora que usaria ~1,08 milhão de tokens no modo estático pode usar ~108 mil tokens, dependendo do comando e do conteúdo.

Para verificar o uso real de tokens de uma solicitação, inspecione `interaction.usage`. Os tokens de vídeo de agentes são informados nos seguintes campos:

- **Comando inicial** (referência de vídeo + comando do usuário): `total_input_tokens`
- **Pensamento de navegação**: `total_thought_tokens`
- **Transcrição, frames e áudio carregados sob demanda**: `total_tool_use_tokens`
- **Resposta final**: `total_output_tokens`

#### Tokens de áudio

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### Contar tokens de instruções do sistema

As instruções do sistema são contadas como parte dos tokens de entrada:

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### Contar tokens de ferramentas

As ferramentas (funções, execução de código, Pesquisa Google) também são contadas:

### Python

```
# This will only work for SDK newer than 2.0.0
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## Janela de contexto

Cada modelo do Gemini tem um número máximo de tokens que pode processar.

- **Modelos do Gemini 4 (`gemini-4-argon`):** compartilham uma única janela de contexto de 1 milhão de tokens (`1,048,576` tokens) em tokens de entrada, pensamento e saída. Por padrão, as respostas síncronas (`background=False`, streaming ou não streaming) são limitadas a `65,536` tokens de saída, ou você pode gerar até `1,048,576` tokens usando a [decodificação longa](https://ai.google.dev/gemini-api/docs/long-decode?hl=pt-br). Se os tokens de entrada mais `max_output_tokens` excederem 1.048.576 tokens, a API limitará automaticamente a saída ao espaço restante na janela de contexto (`1,048,576` menos os tokens de entrada).
- **Modelos do Gemini 3 e 2.5:** usam orçamentos de entrada (`1,048,576` tokens) e saída (`65,536` tokens) separados.

### Receber o tamanho da janela de contexto de maneira programática

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.8-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.8-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Model;

Client client = new Client();

Model modelInfo = client.models.get("gemini-3.8-flash", null);
System.out.println("Input token limit: " + modelInfo.inputTokenLimit().orElse(0));
System.out.println("Output token limit: " + modelInfo.outputTokenLimit().orElse(0));
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

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

    prompt := "Tell me about this instrument"
    imageBytes, err := os.ReadFile("/path/to/organ.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    // Count tokens before creating the interaction
    parts := []*genai.Part{
        genai.NewPartFromText(prompt),
        genai.NewPartFromBytes(imageBytes, "image/jpeg"),
    }
    totalTokens, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Estimated input tokens: %d\n", totalTokens.TotalTokens)

    // Create the multimodal interaction and inspect the usage metadata
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Image),
                    MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
    if interaction.Usage != nil && interaction.Usage.TotalTokens != nil {
        fmt.Printf("Total tokens billed: %d\n", *interaction.Usage.TotalTokens)
    }
}
```

Encontre os tamanhos da janela de contexto na página de [modelos](https://ai.google.dev/gemini-api/docs/models?hl=pt-br).

## A seguir

- [Geração de texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br): noções básicas de geração
- [Armazenamento em cache](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br): reduzir custos com o armazenamento em cache
- [Preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br): entender os custos

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-13 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-13 UTC."],[],[]]
