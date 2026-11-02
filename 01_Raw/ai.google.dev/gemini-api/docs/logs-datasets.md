---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pt-BR
fetched_at: 2026-11-02T07:28:36.961734+00:00
title: "Registros e conjuntos de dados \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Registros e conjuntos de dados

Neste guia, você vai aprender a
visualizar os registros de uso da API Gemini no painel do Google AI Studio
para entender melhor o comportamento do modelo e como os usuários podem estar interagindo com seus
aplicativos. Use os registros para observar, depurar e *compartilhar feedback de uso com o Google para ajudar a melhorar o Gemini em todos os casos de uso do desenvolvedor*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=pt-br)

Todas as chamadas de API `GenerateContent`, `BatchGenerateContent`, `StreamGenerateContent` e [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br), exceto agentes gerenciados, são compatíveis. Isso inclui chamadas feitas por endpoints de [compatibilidade com a OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br).

## Configurar a geração de registros do projeto

Por padrão, as APIs [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br) e
Generate Content armazenam solicitações (`store=true`). Para a API Interactions,
isso também ativa os recursos de gerenciamento de estado do lado do servidor.

No Google [AI Studio](https://aistudio.google.com/logs?hl=pt-br), é possível ativar ou
desativar o armazenamento para projetos individuais e mudar essas
preferências a qualquer momento no painel **Configurações** do
[Painel de registros da API Gemini](https://aistudio.google.com/logs?hl=pt-br). É possível ativar ou desativar a geração de registros
de forma independente para a API `generateContent` e a API
[Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br)
para mudar o comportamento de armazenamento padrão de um projeto.

### Geração de registros no nível da solicitação

As duas APIs armazenam solicitações por padrão (`store=true`):

- **[API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br)**: armazena solicitações por padrão para simplificar o gerenciamento de estado do lado do servidor.
- **API Content Generate (`generateContent`, `streamGenerateContent` e
  `batchGenerateContent`)**: armazena solicitações por padrão para projetos criados
  a partir de 26 de outubro de 2026. Os projetos criados antes dessa data não armazenam
  solicitações por padrão (`store=false`), a menos que a geração de registros esteja ativada no AI Studio.

A propriedade `store` no nível da solicitação tem precedência sobre a configuração para envolvidos no projeto. A configuração de `store` em solicitações da API Generate Content exige
`google-genai` 2.33.0 ou mais recente para Python, `@google/genai` 2.31.0 ou mais recente
para JavaScript, `google-genai` 1.79.0 ou mais recente para Java e
`google.golang.org/genai` 1.76.0 ou mais recente para Go. Veja como definir
a propriedade `store`:

**API GenerateContent**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': True} # Set to False to disable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: true // Set to false to disable logging of this request
    }
});

console.log(response.text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;

Client client = new Client();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        "Explain quantum entanglement in simple terms.",
        GenerateContentConfig.builder()
            .store(true) // Set to false to disable logging of this request
            .build());

System.out.println(response.text());
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

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain quantum entanglement in simple terms."),
        &genai.GenerateContentConfig{
            Store: genai.Ptr(true), // Set to false to disable logging of this request
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

**API Interactions**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
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
        .input(InteractionsInput.of("Explain quantum entanglement in simple terms."))
        .store(true) // Set to false to disable logging of this request
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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Explain quantum entanglement in simple terms."),
            Store: genai.Ptr(true), // Set to false to disable logging of this request
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

## Ver registros do projeto no AI Studio

1. Acesse a página "Registros" no [AI Studio](https://aistudio.google.com/logs?hl=pt-br).
2. Selecione um projeto no menu suspenso.
3. Os registros vão aparecer na tabela em ordem cronológica inversa, se houver.
4. Para projetos criados antes de 26 de outubro de 2026, primeiro ative a geração de registros da API Content no [painel de configurações](#configure-logging) para observar os registros do projeto para a API Content.

Clique em uma entrada para ver uma prévia do payload. Você pode
inspecionar o comando e a resposta completos do Gemini, além do contexto das
interações anteriores. Para solicitações da **API Interactions**, os registros também incluem um link direto para o `previous_interaction_id`.

## Configurar a retenção de armazenamento do projeto

Os registros vão expirar e serão marcados para exclusão após uma janela de retenção padrão de
55 dias (a menos que sejam [salvos em um conjunto de dados](#create), que não expira).
É possível configurar a janela de retenção dos registros de um projeto para no máximo 7, 14, 28 ou 55
dias.

## Criar e compartilhar conjuntos de dados

É possível salvar registros em conjuntos de dados para organizar e exportar com mais eficiência.

- Na [página Registros](https://aistudio.google.com/logs?hl=pt-br), localize a barra de filtro
  na parte de cima para selecionar uma propriedade para filtrar.
- Na visualização com filtro, use as caixas de seleção para selecionar todos os registros ou registros individuais.
- Clique no botão **Criar conjunto de dados** que aparece na parte de cima da lista.
- Dê um nome e uma descrição opcional ao novo conjunto de dados.
- Você vai ver o conjunto de dados que acabou de criar com o conjunto de registros selecionado.
- Exporte seu conjunto de dados para análise posterior como arquivos CSV, JSONL ou para o Google Planilhas.

Os conjuntos de dados podem ser úteis para vários casos de uso diferentes.

- **Organizar conjuntos de desafios**: promova melhorias futuras que visem as áreas em que você quer que a IA melhore.
- **Selecionar conjuntos de amostras**: por exemplo, uma amostra de uso real para gerar respostas de outro modelo ou uma coleção de casos extremos para verificações de rotina antes da implantação.
- **Conjuntos de avaliação**: conjuntos que representam o uso real em recursos importantes, para comparação com outros modelos ou iterações de instruções do sistema.

Você pode contribuir para a pesquisa e o desenvolvimento do Gemini compartilhando
seus conjuntos de dados com o Google como exemplos de demonstração.

## Limitações

No momento, não há suporte para geração de registros nos seguintes casos:

- Modelos Imagen e Veo
- Modelos de embedding do Gemini
- Modelo do Gemini Robotics
- Entradas com vídeos, GIFs ou PDFs
- Agentes de pré-lançamento público na API Gemini

## A seguir

- **Criar protótipos com histórico de sessão**: use o [AI Studio Build](https://aistudio.google.com/apps?hl=pt-br) para criar apps com vibe coding e adicione sua chave de API para ativar um histórico de registros da API Gemini para recursos de IA.
- **Executar novamente os registros com a API Gemini Batch**: use conjuntos de dados para amostragem de respostas
  e avaliação de modelos ou lógica de aplicativos executando novamente os registros com a
  [API Gemini Batch](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-26 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-26 UTC."],[],[]]
