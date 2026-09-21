---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pt-BR
fetched_at: 2026-09-21T05:56:20.794150+00:00
title: "Registros e conjuntos de dados \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Registros e conjuntos de dados

Neste guia, você vai aprender a visualizar registros do uso da API Gemini no painel do Google AI Studio para entender melhor o comportamento do modelo e como os usuários podem interagir com seus aplicativos. Use a geração de registros para observar, depurar e *compartilhar feedback de uso
com o Google para ajudar a melhorar o Gemini em casos de uso de desenvolvedores*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=pt-br)

Todas as chamadas de API `GenerateContent`, `BatchGenerateContent`, `StreamGenerateContent` e as chamadas da API [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br), exceto os agentes gerenciados, são compatíveis. Isso inclui chamadas feitas por
[endpoints de compatibilidade com a OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br).

## Configurar a geração de registros do projeto

Por padrão, a API armazena todos os objetos de interação (`store=true`) para simplificar o uso de recursos de gerenciamento de estado do lado do servidor. Por outro lado, a API Generate Content não armazena solicitações por padrão e exige que o armazenamento seja ativado por solicitação ou no nível do projeto no AI Studio.

No Google [AI Studio](https://aistudio.google.com/logs?hl=pt-br), é possível ativar ou
desativar a geração de registros para todos os projetos ou para projetos específicos e mudar essas
preferências a qualquer momento no painel **Configurações** na página
[Registros e conjuntos de dados](https://aistudio.google.com/logs?hl=pt-br). A geração de registros pode ser ativada ou desativada
de forma independente para a `generateContent` API e a
[Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br) API
para mudar o comportamento de armazenamento padrão de um projeto.

### Geração de registros no nível da solicitação

O comportamento de armazenamento e geração de registros varia de acordo com a API:

- **[API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br):** armazena solicitações por padrão (`store=true`) para simplificar o gerenciamento de estado do lado do servidor.
- **API Generate Content (`generateContent`)** : não armazena solicitações por padrão (`store=false`).

Veja como definir a propriedade `store`:

**API GenerateContent**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
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
        store: false // Set to true to enable logging of this request
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

// The GenerateContent API does not store requests by default
GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash",
        "Explain quantum entanglement in simple terms.",
        GenerateContentConfig.builder().build());

System.out.println(response.text());
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

## Visualizar registros de projetos no AI Studio

1. Acesse a página "Registros" no [AI Studio](https://aistudio.google.com/logs?hl=pt-br).
2. Selecione um projeto no menu suspenso.
3. Os registros vão aparecer na tabela em ordem cronológica inversa para a API Interactions, se existirem.
4. Para observar os registros de projetos da API Content, primeiro ative essa opção no [painel de configurações](#configure-logging).

Clique em uma entrada para ver uma prévia do payload. É possível inspecionar o comando e a resposta completos do Gemini, além do contexto das conversas anteriores. Para solicitações da **API Interactions**, os registros também incluem um link direto para o `previous_interaction_id`.

## Configurar a retenção de armazenamento do projeto

Os registros vão expirar e serão marcados para exclusão após um período de retenção padrão de
55 dias (a menos que sejam [salvos em um conjunto de dados](#create), que não expira).
É possível configurar o período de retenção dos registros de um projeto para 7, 14, 28 ou 55 dias no máximo.

## Criar e compartilhar conjuntos de dados

É possível salvar registros em conjuntos de dados para organizar e exportá-los com mais eficiência.

- Na página "[Registros](https://aistudio.google.com/logs?hl=pt-br)", localize a barra de filtros
  na parte de cima para selecionar uma propriedade para filtrar.
- Na visualização filtrada, use as caixas de seleção para selecionar todos os registros ou registros individuais.
- Clique no botão **Criar conjunto de dados** que aparece na parte de cima da lista.
- Dê um nome e uma descrição opcional ao novo conjunto de dados.
- Você vai ver o conjunto de dados que acabou de criar com o conjunto de registros selecionado.
- Exporte o conjunto de dados para análise posterior como arquivos CSV, JSONL ou para o Planilhas Google.

Os conjuntos de dados podem ser úteis para vários casos de uso diferentes.

- **Selecionar conjuntos de desafios**:impulsionar melhorias futuras que visam áreas em que você quer que sua IA melhore.
- **Selecionar conjuntos de amostras**:por exemplo, uma amostra de uso real para gerar respostas de outro modelo ou uma coleção de casos extremos para verificações de rotina antes da implantação.
- **Conjuntos de avaliação**:conjuntos que são representativos do uso real em recursos importantes, para comparação entre outros modelos ou iterações de instruções do sistema.

Você pode contribuir para a pesquisa e o desenvolvimento do Gemini compartilhando seus conjuntos de dados com o Google como exemplos de demonstração.

## Limitações

No momento, a geração de registros não é compatível com o seguinte:

- Modelos do Imagen e do Veo
- Modelos de incorporação do Gemini
- Modelo do Gemini Robotics
- Entradas que contêm vídeos, GIFs ou PDFs
- Agentes de prévia pública na API Gemini

## A seguir

- **Criar protótipos com o histórico de sessões**:use o [AI Studio Build](https://aistudio.google.com/apps?hl=pt-br) para criar apps de vibe coding e adicione sua chave de API para ativar um histórico de registros da API Gemini para recursos de IA.
- **Executar registros novamente com a API Gemini Batch:** use conjuntos de dados para amostragem de respostas
  e avaliação de modelos ou lógica de aplicativos executando registros novamente com a
  [API Gemini Batch](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-18 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-18 UTC."],[],[]]
