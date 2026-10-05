---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=pt-BR
fetched_at: 2026-10-05T06:28:40.155204+00:00
title: "Resolu\u00e7\u00e3o da m\u00eddia \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Resolução da mídia

O parâmetro `media_resolution` controla como a API Gemini processa entradas de mídia, como imagens, vídeos, áudio e documentos PDF, determinando o **número máximo de tokens** alocados para entradas de mídia. Isso permite equilibrar a qualidade da resposta com a latência e o custo. Enquanto as entradas visuais e de documentos dimensionam a alocação de tokens com base na configuração de resolução, as entradas de áudio são tokenizadas a uma taxa fixa por segundo em todos os níveis de resolução. Para
conferir diferentes configurações, valores padrão e como eles correspondem a tokens, consulte a seção
[Contagem de tokens](#token-counts).

É possível configurar a resolução de mídia para objetos de mídia individuais (itens de conteúdo) na sua solicitação (somente Gemini 3).

## Resolução de mídia por item de conteúdo (somente Gemini 3)

Com o Gemini 3, é possível definir a resolução de mídia para objetos individuais na sua solicitação, oferecendo uma otimização refinada do uso de tokens. É possível misturar níveis de resolução em uma única solicitação. Por exemplo, use alta resolução para um diagrama complexo e baixa resolução para uma imagem contextual simples.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Describe the details in this high-resolution image.").build();
Content imageContent =
    ImageContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/image/scones.jpg")
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
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

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/image.jpg", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe the details in this high-resolution image.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:        genai.Ptr(uploadedFile.URI),
                    MimeType:   interactions.ImageContentMimeType(uploadedFile.MIMEType).ToPointer(),
                    Resolution: interactions.MediaResolutionHigh.ToPointer(),
                }),
            }),
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
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Valores de resolução disponíveis

A API Gemini define os seguintes níveis de resolução de mídia:

- `unspecified`: a configuração padrão. A contagem de tokens para esse nível varia muito entre o Gemini 3 e os modelos anteriores.
- `low`: contagem de tokens menor, resultando em processamento mais rápido e custo menor, mas com menos detalhes.
- `medium`: um equilíbrio entre detalhes, custo e latência.
- `high`: contagem de tokens mais alta, fornecendo mais detalhes para o modelo trabalhar, mas com aumento da latência e do custo.
- `ultra_high` (apenas por item de conteúdo): contagem máxima de tokens, necessária para casos de uso específicos, como [uso de computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br).

O `high` oferece a performance ideal para a maioria dos casos de uso.

O número exato de tokens gerados para cada um desses níveis depende do **tipo de mídia** (imagem, vídeo, áudio, PDF) e da **versão do modelo**.

## Contagem de tokens

As tabelas abaixo resumem as contagens aproximadas de tokens para cada valor de `media_resolution` e tipo de mídia por família de modelos.

**Modelos do Gemini 3**

| MediaResolution | Imagem | Vídeo | Áudio | PDF |
| --- | --- | --- | --- | --- |
| `unspecified` (padrão) | 1120 | 70 | 25 (por segundo) | 560 |
| `low` | 280 | 70 | 25 (por segundo) | 280 + texto nativo |
| `medium` | 560 | 70 | 25 (por segundo) | 560 + texto nativo |
| `high` | 1120 | 280 | 25 (por segundo) | 1120 + texto nativo |
| `ultra_high` | 2240 | N/A | N/A | N/A |

## Como escolher a resolução certa

- **Padrão (`unspecified`)**: comece com o padrão. Ele é ajustado para um bom equilíbrio entre qualidade, latência e custo nos casos de uso mais comuns.
- **`low`**:use em cenários em que o custo e a latência são fundamentais, e o detalhe refinado é menos importante.
- **`medium` / `high`**:aumente a resolução quando a tarefa exigir a compreensão de detalhes complexos na mídia. Isso geralmente é necessário para análises visuais complexas, leitura de gráficos ou compreensão de documentos densos.
- **`ultra_high`**: disponível apenas para a configuração por item de conteúdo. Recomendado para casos de uso específicos, como uso de computador ou quando o teste mostra uma melhoria clara em relação a `high`.
- **Controle por item de conteúdo (Gemini 3)**: otimiza o uso de tokens. Por exemplo, em um comando com várias imagens, use `high` para um diagrama complexo e `low` ou `medium` para imagens contextuais mais simples.

**Configurações recomendadas**

Confira abaixo as configurações de resolução de mídia recomendadas para cada tipo de mídia compatível.

| Tipo de mídia | Configuração recomendada | Máximo de tokens | Orientação de uso |
| --- | --- | --- | --- |
| **Imagens** | `high` | 1120 | Recomendado para a maioria das tarefas de análise de imagens para garantir a qualidade máxima. |
| **PDFs** | `medium` | 560 | Ideal para compreensão de documentos. A qualidade geralmente satura em `medium`. Aumentar para `high` raramente melhora os resultados do OCR em documentos padrão. |
| **Vídeo** (Geral) | `low` (ou `medium`) | 70 (por frame) | **Observação**:para vídeo, as configurações `low` e `medium` são tratadas de forma idêntica (70 tokens) para otimizar o uso do contexto. Isso é suficiente para a maioria das tarefas de reconhecimento e descrição de ações. |
| **Vídeo** (com muito texto) | `high` | 280 (por frame) | Obrigatório apenas quando o caso de uso envolve a leitura de texto denso (OCR) ou pequenos detalhes em frames de vídeo. |
| **Áudio** | `unspecified` (padrão) | 25 (por segundo) | O áudio é tokenizado a uma taxa fixa de 25 tokens por segundo em todas as configurações de resolução compatíveis (`unspecified`, `low`, `medium` e `high`). |

Sempre teste e avalie o impacto de diferentes configurações de resolução no seu aplicativo para encontrar o melhor equilíbrio entre qualidade, latência e custo.

## Relação com os modos de processamento de vídeo

Os parâmetros `media_resolution` e de processamento controlam diferentes aspectos da entrada de vídeo:

- `media_resolution` controla a **resolução** de cada frame (número de tokens por frame).
- `processing` / `media_processing` controla **qual conteúdo do vídeo** é carregado no contexto.

É possível definir os dois na mesma entrada de vídeo. Por exemplo, você pode usar o processamento com agentes com baixa resolução de mídia para minimizar o uso total de tokens em um vídeo longo.

Para detalhes sobre os modos de processamento de vídeo, consulte o guia [Entendimento de vídeo com agente](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pt-br#agentic-video-understanding).

## Resumo da compatibilidade de versões

- A definição do `resolution` em itens de conteúdo individuais é **exclusiva dos modelos do Gemini 3**.

## Próximas etapas

- Saiba mais sobre os recursos multimodais da API Gemini nos guias de [compreensão de imagens](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pt-br), [entendimento de vídeo](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pt-br), [compreensão de áudio](https://ai.google.dev/gemini-api/docs/audio?hl=pt-br) e [compreensão de documentos](https://ai.google.dev/gemini-api/docs/document-processing?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-24 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-24 UTC."],[],[]]
