---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pt-BR
fetched_at: 2026-07-27T04:40:16.636343+00:00
title: "Registros e conjuntos de dados \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Registros e conjuntos de dados

Neste guia, você vai aprender a
ver registros do uso da API Gemini no painel do Google AI Studio
para entender melhor o comportamento do modelo e como os usuários interagem com seus
aplicativos. Use o registro em registros para observar, depurar e *compartilhar feedback de uso com o Google para ajudar a melhorar o Gemini em casos de uso de desenvolvedores*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=pt-br)

Todas as chamadas de API `GenerateContent`, `BatchGenerateContent`, `StreamGenerateContent` e [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br), exceto as de agentes gerenciados, são compatíveis. Isso inclui chamadas feitas pelos endpoints de
[compatibilidade com a OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br).

## Configurar o registro do projeto

Por padrão, a API armazena todos os objetos de interação (`store=true`) para simplificar o uso dos recursos de gerenciamento de estado do lado do servidor. Por outro lado, a API Generate Content não armazena solicitações por padrão e exige que o armazenamento seja ativado por solicitação ou no nível do projeto no AI Studio.

No [AI Studio](https://aistudio.google.com/logs?hl=pt-br) do Google, é possível ativar ou desativar o registro em todos os projetos ou em projetos específicos e mudar essas preferências a qualquer momento no painel **Configurações** da página [Registros e conjuntos de dados](https://aistudio.google.com/logs?hl=pt-br). É possível ativar ou desativar o registro em log
de forma independente para a API `generateContent` e a API
[Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br)
para mudar o comportamento de armazenamento padrão de um projeto.

### Geração de registros no nível da solicitação

O comportamento de armazenamento e geração de registros varia de acordo com a API:

- **[API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br)**:armazena solicitações por padrão (`store=true`) para simplificar o gerenciamento de estado do lado do servidor.
- **API Generate Content (`generateContent`)**: não armazena solicitações por padrão (`store=false`).

Veja como definir a propriedade `store`:

**API GenerateContent**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.6-flash',
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
    model: 'gemini-3.6-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

**API Interactions**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

## Ver registros do projeto no AI Studio

1. Acesse a página "Registros" no [AI Studio](https://aistudio.google.com/logs?hl=pt-br).
2. Selecione um projeto no menu suspenso.
3. Os registros vão aparecer na tabela em ordem cronológica inversa para a API Interactions, se existirem.
4. Para observar os registros do projeto da API Content, primeiro ative essa opção no [painel de configurações](#configure-logging).

Clique em uma entrada para ver uma prévia do payload. Você pode inspecionar o comando e a resposta completos do Gemini, além do contexto das trocas anteriores. Para solicitações da **API Interactions**, os registros também incluem um link direto para o `previous_interaction_id`.

## Configurar a retenção de armazenamento do projeto

Os registros expiram e são marcados para exclusão após um período de retenção padrão de 55 dias, a menos que sejam [salvos em um conjunto de dados](#create), que não expira.
É possível configurar a janela de retenção dos registros de um projeto para, no máximo, 7, 14, 28 ou 55 dias.

## Criar e compartilhar conjuntos de dados

É possível salvar registros em conjuntos de dados para organizar e exportar com mais eficiência.

- Na [página "Registros"](https://aistudio.google.com/logs?hl=pt-br), localize a barra de filtro
  na parte de cima para selecionar uma propriedade de filtragem.
- Na visualização filtrada, use as caixas de seleção para selecionar todos os registros ou apenas alguns.
- Clique no botão **Criar conjunto de dados** que aparece na parte de cima da lista.
- Dê um nome e uma descrição opcional ao novo conjunto de dados.
- Você vai encontrar o conjunto de dados que acabou de criar com o conjunto selecionado de registros.
- Exporte seu conjunto de dados para análise posterior como arquivos CSV, JSONL ou para o Google Planilhas.

Os conjuntos de dados podem ser úteis para vários casos de uso diferentes.

- **Organize conjuntos de desafios**:impulsione melhorias futuras que visam áreas em que você quer que a IA melhore.
- **Organizar conjuntos de amostras**:por exemplo, uma amostra de uso real para gerar respostas de outro modelo ou uma coleção de casos extremos para verificações de rotina antes da implantação.
- **Conjuntos de avaliação**:conjuntos representativos do uso real em recursos importantes, para comparação entre outros modelos ou iterações de instruções do sistema.

Você pode contribuir para a pesquisa e o desenvolvimento do Gemini compartilhando seus conjuntos de dados com o Google como exemplos de demonstração.

## Limitações

No momento, o registro em log não é compatível com o seguinte:

- Modelos do Imagen e do Veo
- Modelos de incorporação do Gemini
- Modelo do Gemini Robotics
- Entradas com vídeos, GIFs ou PDFs
- Agentes de pré-lançamento público na API Gemini

## A seguir

- **Crie protótipos com o histórico da sessão**:use o [AI Studio Build](https://aistudio.google.com/apps?hl=pt-br) para programar apps com vibe coding e adicione sua chave de API para ativar um histórico de registros da API Gemini para recursos de IA.
- **Executar novamente os registros com a API Gemini Batch**:use conjuntos de dados para amostragem de respostas e avaliação de modelos ou lógica de aplicativos executando novamente os registros com a [API Gemini Batch](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-22 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-22 UTC."],[],[]]
