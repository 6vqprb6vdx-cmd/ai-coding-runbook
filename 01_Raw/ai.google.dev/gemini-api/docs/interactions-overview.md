---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-BR
fetched_at: 2026-07-20T04:42:19.802742+00:00
title: "API Interactions \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# API Interactions

A API Interactions é a melhor maneira de criar com modelos e agentes do Gemini. Desde junho de 2026, ele está disponível para todos e é recomendado para todos os novos projetos. Embora agora seja considerada legada, a API
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=pt-br) original
continua sendo totalmente compatível.

## Por que usar a API Interactions?

- **Interface universal para todos os aplicativos**: projetada como a interface padrão para todos os casos de uso, incluindo geração de texto de turno único, compreensão multimodal, saídas estruturadas, orquestração de ferramentas e fluxos de trabalho de agentes.
- **API única para modelos e agentes**: um endpoint e um padrão unificados para chamar modelos padrão do Gemini e agentes especializados diretamente (como Deep Research e agentes gerenciados personalizados).
- **Novas funcionalidades prontas para uso**: recursos como estado de conversa opcional do lado do servidor usando `previous_interaction_id`, etapas de execução observáveis para depuração e renderização da interface, além de [execução em segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-br) para tarefas de longa duração usando `background=true`.
- **Custo menor com taxas de ocorrência em cache mais altas**: ao usar conversas multiturno, o gerenciamento de estado opcional do lado do servidor permite um cache de contexto mais eficiente entre as rodadas, reduzindo os custos de token.
- **Onde os novos recursos são lançados**: daqui em diante, todos os novos modelos, recursos multimodais, ferramentas e recursos de agente serão lançados na API Interactions.

Por padrão, a API Interactions armazena solicitações para que você possa aproveitar
os recursos de gerenciamento de estado do lado do servidor usando
`previous_interaction_id`. É possível ativar o comportamento sem estado definindo
`store=false`. Consulte a seção [retenção de dados](#data-storage-retention) para mais detalhes.

## Primeiros passos

- **Configure seu agente de programação**: conecte-se ao **MCP dos Documentos do Gemini** e instale
  a habilidade `gemini-interactions-api` para dar ao seu assistente acesso direto aos
  documentos mais recentes para desenvolvedores e às práticas recomendadas. Para conferir as etapas detalhadas, consulte o
  [guia de configuração do seu agente de programação](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pt-br).
- **Migrar de `generateContent`**: se você tiver uma integração, siga o [guia de migração](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=pt-br) para fazer a transição para a API Interactions.
- **Começar**: siga as etapas no [guia de início rápido da API Interactions](https://ai.google.dev/gemini-api/docs/get-started?hl=pt-br).

### Guias de recursos

Confira estes guias para conhecer os recursos específicos da API Interactions. Use a chave nessas páginas para alternar entre a API generateContent e a API Interactions:

- [Geração de texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br)
- [Geração de imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br)
- [Compreensão de imagens](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pt-br)
- [Compreensão de áudio](https://ai.google.dev/gemini-api/docs/audio?hl=pt-br)
- [Compreensão do vídeo](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pt-br)
- [Processamento de documentos](https://ai.google.dev/gemini-api/docs/document-processing?hl=pt-br)
- [Chamadas de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)
- [Saída estruturada](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br)
- [Agente Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br)
- [Inferência flexível](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pt-br)
- [Inferência de prioridade](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pt-br)

## Como a API Interactions funciona

A API Interactions se concentra em um recurso principal: o [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=pt-br#Resource:Interaction). Um `Interaction` representa uma rodada completa em uma conversa ou tarefa. Ele funciona como um registro de sessão, contendo todo o histórico de uma interação como uma sequência cronológica de **etapas de execução**. Essas etapas incluem reflexões do modelo, chamadas de ferramentas e resultados do lado do servidor ou do lado do cliente (como `function_call` e `function_result`) e o `model_output` final. O recurso armazenado (recuperado via `interactions.get`) também inclui etapas `user_input` para contexto completo, embora a resposta `interactions.create` retorne apenas etapas geradas pelo modelo.

Ao fazer uma chamada para
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=pt-br#CreateInteraction), você está
criando um novo recurso `Interaction`.

### Gerenciamento de estado do lado do servidor

Você pode usar o `id` de uma interação concluída em uma chamada subsequente usando o parâmetro `previous_interaction_id` para continuar a conversa. O servidor usa esse ID para recuperar o histórico da conversa, evitando que você precise reenviar todo o histórico do chat.

O parâmetro `previous_interaction_id` preserva apenas o histórico de conversas (entradas e saídas) usando `previous_interaction_id`. Os outros parâmetros são **no escopo da interação** e se aplicam apenas à interação específica que você está gerando:

- `tools`
- `system_instruction`
- `generation_config` (incluindo `thinking_level`, `temperature` etc.)

Isso significa que você precisa especificar esses parâmetros novamente em cada nova interação se quiser que eles sejam aplicados. O gerenciamento de estado do lado do servidor é opcional. Você também pode operar no modo sem estado enviando o histórico completo da conversa em cada solicitação.

### Armazenamento e retenção de dados

Por padrão, a API armazena todos os objetos de interação (`store=true`) para simplificar o uso de recursos de gerenciamento de estado do lado do servidor (com `previous_interaction_id`), [execução em segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-br) (usando `background=true`) e fins de observabilidade.

- **Nível pago**: o sistema retém as interações por **55 dias**.
- **Nível sem custo financeiro**: o sistema retém as interações por **1 dia**.

Se não quiser isso, defina `store=false` na sua solicitação. Esse controle é separado do gerenciamento de estado. Você pode desativar o armazenamento para qualquer interação. No entanto, `store=false` é incompatível com a [execução em segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-br) e impede o uso de `previous_interaction_id` em turnos subsequentes.

Para projetos do nível pago, é possível configurar a janela de retenção no [AI Studio](https://aistudio.google.com/logs?hl=pt-br) para marcar automaticamente os registros para exclusão do armazenamento do projeto após 7, 14, 28 ou 55 dias. Um período de retenção mais curto pode afetar a recuperação de conversas anteriores.

É possível excluir interações armazenadas a qualquer momento usando o método [`delete`](https://ai.google.dev/api/interactions-api?hl=pt-br#deleteInteraction) de forma programática, que
requer o ID da interação. Também é possível conferir e gerenciar os registros de interações armazenadas, incluindo a exclusão do armazenamento do projeto, no [AI Studio](https://aistudio.google.com/logs?hl=pt-br).

Após o período de armazenamento expirar, seus dados serão excluídos automaticamente.

Os objetos de interação são processados de acordo com os [termos](https://ai.google.dev/gemini-api/terms?hl=pt-br).

### Ver interações no AI Studio

A API armazena solicitações da API Interactions executadas com `store=true` para projetos no nível pago. Você pode conferir essas informações diretamente na
[página "Registros" do Google AI Studio](https://ai.google.dev/gemini-api/docs/www.aistudio.google.com/logs?hl=pt-br). Consulte o
[guia de registros](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pt-br) para mais informações.

## Práticas recomendadas

- **Taxa de ocorrência em cache**: o armazenamento em cache implícito é compatível com os modos com e sem estado. Consulte o [guia de início rápido](https://ai.google.dev/gemini-api/docs/get-started?hl=pt-br#4_multi-turn_conversations). Usar `previous_interaction_id` (com estado) para continuar conversas permite que o sistema utilize mais facilmente o cache implícito para o histórico de conversas, o que melhora o desempenho e reduz os custos.
- **Interações combinadas**: você pode combinar interações de agente e modelo em uma conversa. Por exemplo, você pode usar um agente especializado, como o Deep Research, para a coleta inicial de dados e, em seguida, usar um modelo padrão do Gemini para tarefas de acompanhamento, como resumir ou reformatar, vinculando essas etapas ao `previous_interaction_id`.

## Modelos e agentes compatíveis

| Nome do modelo | Tipo | ID do modelo |
| --- | --- | --- |
| Gemini 3.5 Flash | Modelo | `gemini-3.5-flash` |
| Pré-lançamento do Gemini 3.1 Pro | Modelo | `gemini-3.1-pro-preview` |
| Gemini 3.1 Flash-Lite | Modelo | `gemini-3.1-flash-lite` |
| Pré-lançamento do Gemini 3 Flash | Modelo | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Modelo | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Modelo | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | Modelo | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | Modelo | `gemini-3-pro-image` |
| Imagem do Gemini 3.1 Flash | Modelo | `gemini-3.1-flash-image` |
| Pré-lançamento do Gemini 3.1 Flash TTS | Modelo | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | Modelo | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | Modelo | `gemma-4-26b-a4b-it` |
| Prévia de clipes do Lyria 3 | Modelo | `lyria-3-clip-preview` |
| Pré-lançamento do Lyria 3 Pro | Modelo | `lyria-3-pro-preview` |
| Prévia do Deep Research | Agente | `deep-research-preview-04-2026` |
| Prévia do Deep Research | Agente | `deep-research-max-preview-04-2026` |
| Prévia do Antigravity | Agente | `antigravity-preview-05-2026` |

## SDKs

Use a versão mais recente dos SDKs da IA generativa do Google para acessar a API Interactions.

- Em Python, esse é o pacote `google-genai` da versão `2.3.0` em diante.
- Em JavaScript, esse é o pacote `@google/genai` da versão `2.3.0`
  em diante.

Saiba mais sobre como instalar os SDKs na página [Bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br).

## Limitações

- **MCP remoto**: o Gemini 3 não é compatível com MCP remoto, mas isso vai estar disponível em breve.
- **Compatibilidade de modelos com várias interações**: ao misturar modelos diferentes em uma
  conversa (com ou sem estado), os modelos subsequentes precisam aceitar
  as modalidades de saída dos modelos anteriores como entrada. Por exemplo, se você gerar uma imagem usando o `gemini-3.1-flash-image`, não poderá continuar essa conversa com um modelo que não aceita entradas de imagem, como um modelo somente de texto ou um modelo de geração de música como o Lyria.

Os seguintes recursos são compatíveis com a API
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=pt-br), mas **ainda não estão
disponíveis** na API Interactions:

- **[Metadados de vídeo](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pt-br)**: o campo `video_metadata`, usado para definir intervalos de corte
  e taxas de frames personalizadas para o entendimento de vídeo.
- **[API em lote](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br)**
- **[Chamada automática de função (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=pt-br#automatic_function_calling_python_only)**
- **[Criação de cache explícita](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br)**: observe que a criação de cache implícita do lado do servidor está disponível na API Interactions
  via `previous_interaction_id`.
- **[Configurações de segurança](https://ai.google.dev/gemini-api/docs/safety-settings?hl=pt-br)**: as configurações de segurança personalizadas não são compatíveis com a API Interactions.

## Feedback

Seu feedback é fundamental para o desenvolvimento da API Interactions.
Compartilhe suas ideias, informe bugs ou solicite recursos no [fórum da comunidade de desenvolvedores da IA do Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=pt-br).

## A seguir

- Teste o [notebook de início rápido da API Interactions](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=pt-br).
- Saiba mais sobre o [agente do Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-16 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-16 UTC."],[],[]]
