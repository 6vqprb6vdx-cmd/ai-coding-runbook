---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=pt-BR
fetched_at: 2026-10-12T06:54:23.344258+00:00
title: "Pensamento do Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Pensamento do Gemini

Os [modelos da série Gemini 3 e 2.5](https://ai.google.dev/gemini-api/docs/models?hl=pt-br) usam um "processo de pensamento" que melhora significativamente as habilidades de raciocínio e planejamento de várias etapas, tornando-os altamente eficazes para tarefas complexas, como programação, matemática avançada e análise de dados.

Quando você usa um modelo de pensamento, o Gemini raciocina internamente antes de responder. A API Interactions mostra esse raciocínio usando etapas `thought`, que aparecem em ordem cronológica junto com chamadas de função, entradas do usuário ou saídas do modelo na matriz `steps`.

Cada etapa de pensamento contém dois campos:

| Campo | Obrigatório | Descrição |
| --- | --- | --- |
| `signature` | ✅ Sim | Uma representação criptografada do estado de raciocínio interno do modelo. Sempre presente, mesmo quando o modelo realiza um raciocínio mínimo. |
| `summary` | ❌ Não | Uma matriz de conteúdo (texto e/ou imagens) que resume o raciocínio. Pode estar vazio dependendo da configuração [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=pt-br), se o modelo fez raciocínio suficiente ou do tipo de conteúdo. Por exemplo, latentes de imagem podem não ter resumos de texto. |

## Interações com o pensamento

Iniciar uma interação com um modelo de pensamento é semelhante a qualquer outra solicitação de interação. Especifique um dos [modelos com suporte de pensamento](#thinking-levels) no campo `model`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Explain the concept of Occam's Razor and provide a simple, everyday example."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("Explain the concept of Occam's Razor and provide a simple, everyday example."),
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## Resumos de raciocínio

Os resumos de pensamento fornecem insights sobre o processo de raciocínio interno do modelo.
Por padrão, apenas a saída final é retornada. É possível ativar os resumos de ideias
com `thinking_summaries`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtStep;
import com.google.genai.gaos.models.interactions.ThoughtSummaryContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Collections;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the sum of the first 50 prime numbers?"))
        .generationConfig(
            GenerationConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ThoughtStep thoughtStep) {
    System.out.println("Thought summary:");
    for (ThoughtSummaryContent contentBlock : thoughtStep.summary().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent) {
        System.out.println(textContent.text().orElse(""));
      }
    }
    System.out.println();
  } else if (step instanceof ModelOutputStep outputStep) {
    for (Content contentBlock : outputStep.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent) {
        System.out.println("Answer:");
        System.out.println(textContent.text().orElse(""));
        System.out.println();
      }
    }
  }
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Provide a list of 3 famous physicists and their key contributions"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelLow.ToPointer(),
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

Um bloco de pensamento pode conter **apenas uma assinatura sem resumo** nestes casos:

- Solicitações simples, em que o modelo não raciocinou o suficiente para gerar um resumo
- `thinking_summaries: "none"`, em que os resumos estão explicitamente desativados
- Alguns tipos de conteúdo de pensamento, como imagens, podem não ter resumos de texto

Seu código sempre precisa processar blocos de pensamento em que `summary` está vazio ou ausente.

## Streaming com raciocínio

Use o streaming para receber resumos incrementais de ideias durante a geração.
Os blocos de pensamento são entregues usando eventos enviados pelo servidor (SSE) com dois tipos
de delta distintos:

| Tipo de delta | Contém | Quando enviado |
| --- | --- | --- |
| `thought_summary` | Conteúdo de resumo de texto ou imagem | Um ou mais deltas com resumo incremental |
| `thought_signature` | A assinatura criptográfica | o último delta antes de `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.StepDeltaData;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtSummaryDelta;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();

String prompt =
    "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.\n"
        + "Alice does not live in the red house.\n"
        + "Bob does not live in the green house.\n"
        + "Carol does not live in the red or green house.\n"
        + "Which house does each person live in?";

StringBuilder thoughts = new StringBuilder();
StringBuilder answer = new StringBuilder();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .generationConfig(
            GenerationConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .stream(true)
        .build();

CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));

try (EventStream<InteractionSSEStreamEvent> stream = response.events()) {
  for (InteractionSSEStreamEvent streamEvent : stream) {
    InteractionSSEEvent event = streamEvent.data().orElse(null);
    if (event instanceof StepDelta stepDelta) {
      StepDeltaData delta = stepDelta.delta().orElse(null);
      if (delta instanceof ThoughtSummaryDelta thoughtDelta) {
        Content content = thoughtDelta.content().orElse(null);
        if (content instanceof TextContent textContent) {
          if (thoughts.length() == 0) {
            System.out.println("Thinking...");
          }
          String summaryText = textContent.text().orElse("");
          System.out.print("[Thought] " + summaryText);
          thoughts.append(summaryText);
        }
      } else if (delta instanceof TextDelta textDelta) {
        String text = textDelta.text().orElse("");
        if (!text.isEmpty()) {
          if (answer.length() == 0) {
            System.out.println("\nAnswer:");
          }
          System.out.print(text);
          answer.append(text);
        }
      }
    }
  }
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("What is the sum of the first 50 prime numbers?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel:     interactions.ThinkingLevelHigh.ToPointer(),
                ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if thought := step.ThoughtStep; thought != nil {
            for _, part := range thought.Summary {
                if part.TextContent != nil {
                    fmt.Printf("Thought summary:\n%s\n\n", part.TextContent.Text)
                }
            }
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Printf("Answer:\n%s\n", *res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

A resposta de streaming usa eventos enviados pelo servidor (SSE) e é composta de etapas
e eventos, por exemplo:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.8-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Controle do pensamento

Os modelos do Gemini usam o pensamento dinâmico por padrão, ajustando automaticamente a quantidade de esforço de raciocínio com base na complexidade da solicitação. É possível controlar esse comportamento usando o parâmetro `thinking_level`.

| Modelo | Raciocínio padrão | Níveis compatíveis |
| --- | --- | --- |
| gemini-3.8-flash | Ativada (média) | baixa, média, alta |
| gemini-3.6-flash | Ativada (média) | mínima, baixa, média, alta |
| gemini-3.5-flash-lite | Ativado (mínimo) | mínima, baixa, média, alta |
| gemini-3.1-pro-preview | Ligado (alto) | baixa, média, alta |
| gemini-3.1-flash-lite-image | Ativado (mínimo) | mínima, alta |
| gemini-3-flash-preview | Ligado (alto) | mínima, baixa, média, alta |
| gemini-3-pro-preview | Ligado (alto) | baixo, alto |
| gemini-2.5-pro | Ativado | baixa, média, alta |
| gemini-2.5-flash | Ativado | baixa, média, alta |
| gemini-2.5-flash-lite | Desativada | baixa, média, alta |
| gemini-robotics-er-2-preview | Ligado (alto) | mínima, baixa, média, alta |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Provide a list of 3 famous physicists and their key contributions"))
        .generationConfig(GenerationConfig.builder().thinkingLevel(ThinkingLevel.LOW).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("What is the sum of the first 50 prime numbers?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel:     interactions.ThinkingLevelHigh.ToPointer(),
                ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
            },
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
            if thoughtDelta := stepDelta.GetDeltaThoughtSummary(); thoughtDelta != nil {
                if textContent := thoughtDelta.GetContentText(); textContent != nil {
                    fmt.Printf("[Thought Summary] %s\n", textContent.Text)
                }
            }
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### Limites de tokens e `max_output_tokens`

O parâmetro de geração [`max_output_tokens`](https://ai.google.dev/api/interactions-api?hl=pt-br#request-body) define o número máximo de tokens que uma resposta pode gerar, incluindo tokens de pensamento.

Quando definido, esse parâmetro atua como um corte rígido imposto pela infraestrutura sem mudar a forma como o modelo aloca o orçamento de pensamento (`thinking_level`).

Se o modelo atingir esse limite durante o raciocínio, ele vai parar de gerar com o status
`"incomplete"` e retornar uma saída truncada ou vazia (mas ainda cobrando por
todos os tokens de raciocínio gerados). Para reduzir o custo ou a latência sem truncar as respostas, diminua `thinking_level` (`low` ou `medium`) em vez de definir um `max_output_tokens` pequeno.

## Assinaturas de raciocínio

As assinaturas de pensamento são representações criptografadas do raciocínio interno do modelo. Elas precisam manter a continuidade do raciocínio em interações de várias etapas.

A API Interactions simplifica muito mais o processamento de assinaturas de pensamento do que a API `generateContent`.

### Modo com estado (recomendado)

Por padrão, quando você usa a API Interactions no modo com estado (definindo `store: true` e transmitindo `previous_interaction_id` em turnos subsequentes), o servidor gerencia automaticamente o estado da conversa, incluindo todos os blocos de pensamento e assinaturas. Nesse modo, você não precisa fazer nada em relação às assinaturas. Eles são processados totalmente no lado do servidor.

### Modo sem estado

Se você estiver gerenciando o estado da conversa (modo sem estado) e transmitindo o histórico completo de entradas e saídas em cada solicitação:

- Você **PRECISA** sempre reenviar todos os blocos `thought` exatamente como foram recebidos do modelo.
- **NÃO** remova nem modifique os blocos de pensamento do histórico, porque eles contêm as assinaturas obrigatórias para que o modelo continue raciocinando.
- Ao trocar de modelo em uma sessão, ainda é necessário reenviar os blocos de pensamento do modelo anterior. O back-end gerencia a compatibilidade.

## Preços

Quando o raciocínio está ativado, o preço da resposta é a soma dos tokens de saída e de raciocínio. É possível conferir o número total de tokens de pensamento gerados no campo `total_thought_tokens`.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
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

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain the concept of Occam's Razor."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.usage().isPresent()) {
  Usage usage = interaction.usage().get();
  System.out.println("Thoughts tokens: " + usage.totalThoughtTokens().orElse(0));
  System.out.println("Output tokens: " + usage.totalOutputTokens().orElse(0));
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

    // Turn 1: Execute a reasoning + tool use interaction
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("Compare the GDP growth of Japan and Germany in 2025."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelHigh.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Turn 2: Pass PreviousInteractionID so thought signatures are automatically preserved
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-pro"),
            PreviousInteractionID: turn1.Interaction.ID,
            Input:                 interactions.NewInteractionsInput("Now summarize that comparison in a 3-row markdown table."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

Os modelos de pensamento geram ideias completas para melhorar a qualidade da resposta final e, em seguida, produzem [resumos](#summaries) para fornecer insights sobre o processo de pensamento. O preço se baseia nos tokens de pensamento completos que o modelo precisa gerar, embora apenas o resumo seja gerado pela API.

Saiba mais sobre tokens no guia [Contagem de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br).

## Práticas recomendadas

Siga estas diretrizes para usar modelos de pensamento de forma eficiente.

- **Revisar o raciocínio**: analise os resumos de pensamento para entender as falhas e melhorar os comandos.
- **Controle o orçamento de pensamento**: peça ao modelo para pensar menos em saídas longas e economizar tokens.
- **Tarefas simples**: use o mínimo de raciocínio para recuperação ou classificação de fatos (por exemplo, "Onde a DeepMind foi fundada?").
- **Tarefas moderadas**: use o pensamento padrão para comparar conceitos ou raciocínio criativo (por exemplo, "Compare carros elétricos e híbridos").
- **Tarefas complexas**: use o pensamento máximo para programação avançada, matemática ou planejamento em várias etapas (por exemplo, resolver problemas de matemática da AIME).

## A seguir

- [Geração de texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br): respostas de texto básicas
- [Chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br): conexão com ferramentas
- [Guia do Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=pt-br): recursos específicos do modelo

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-09 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-09 UTC."],[],[]]
