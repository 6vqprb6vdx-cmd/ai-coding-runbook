---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=pt-BR
fetched_at: 2026-09-14T05:34:46.819815+00:00
title: "Vis\u00e3o geral dos agentes \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Visão geral dos agentes

Os agentes gerenciados na API Gemini oferecem um harness de agente configurável. Uma única chamada de API provisiona um sandbox do Linux em que o agente raciocina, executa código, gerencia arquivos e navega na Web de forma autônoma.

[rocket\_launch

Guia de início rápido

Faça sua primeira chamada de agente, transmita respostas e crie um agente personalizado.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pt-br)
[smart\_toy

Agente do Antigravity

Recursos, ferramentas, entrada multimodal e preços do agente padrão.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br)
[experiment

Agentes no AI Studio

Playground visual para criar protótipos de agentes sem escrever código.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=pt-br)

## Agentes gerenciados disponíveis

- **[Agente do Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br)**: agente gerenciado de uso geral com a tecnologia do Gemini 3.8 Flash. Executa código, gerencia arquivos e pesquisa na Web em um sandbox seguro do Linux hospedado pelo Google. É possível
  configurar o modelo subjacente (como o Gemini 3.7 Flash, o Gemini 3.6 Flash ou o Gemini 3.5 Flash)
  usando `agent_config` e estendê-lo com suas próprias instruções, habilidades e dados para
  [criar um agente personalizado](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pt-br).
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br)**: agente de pesquisa autônomo que planeja, executa e sintetiza tarefas de pesquisa de várias etapas para casos de uso como análise de mercado, auditoria e revisões de literatura.

## Segurança e práticas recomendadas

Cada agente é executado em um ambiente de sandbox isolado no nível do SO.
O sandbox tem acesso de rede de saída irrestrito por padrão. É possível restringir ou desativar o acesso à rede usando uma lista de permissões.

### Acesso à rede

Por padrão, os ambientes têm acesso de rede de saída irrestrito. Use uma lista de permissões `network` para restringir o tráfego de saída a domínios específicos ou padrões curinga. Para detalhes de configuração, consulte
[Lista de permissões de rede](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=pt-br#network_allow_list) (AI
Studio) ou [Regras de rede](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pt-br#with_network_rules)
(API).

### APIs e ferramentas externas

É possível conectar APIs e ferramentas externas para estender o agente. Use apenas ferramentas de fontes confiáveis e permissões de escopo para o mínimo necessário. As credenciais podem ser injetadas com segurança por transformações de cabeçalho de proxy de saída e nunca são expostas no sandbox. O agente pode usar qualquer credencial a que tiver acesso. Portanto, forneça apenas credenciais cujo escopo completo você esteja disposto a conceder.

- Use contas de serviço com privilégios mínimos ou chaves de API.
- Prefira tokens de curta duração em vez de chaves de longa duração.
- Forneça apenas credenciais cujo escopo completo você esteja disposto a conceder.
- Alterne as credenciais regularmente.

Para detalhes sobre como configurar transformações de cabeçalho, consulte
[Credenciais](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br#credentials).

### Supervisão humana

Sempre verifique as saídas (código gerado, transformações de dados, mudanças de configuração) antes de implantá-las, principalmente para tarefas que modificam dados ou interagem com sistemas externos.

## Preços

Os agentes gerenciados usam um modelo de [pagamento por uso](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#pricing-for-agents) com base em tokens de modelo do Gemini e uso de ferramentas. Uma única interação pode acionar vários loops de raciocínio, normalmente consumindo de 100 mil a 3 milhões de tokens. A computação do ambiente **não é faturada** durante o pré-lançamento. Consulte os [custos estimados](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br#availability-and-pricing)
para detalhamentos por tarefa. Os agentes gerenciados também estão disponíveis no nível sem custo financeiro com um limite de taxa e uma cota de uso sem custo financeiro.

## Limites

| Limite | Descrição |
| --- | --- |
| **Ciclo de vida do ambiente** | Os ambientes são excluídos permanentemente após sete dias de inatividade. |
| **Desativação da VM** | As VMs são desativadas após um breve período de inatividade para conservar recursos. A próxima solicitação restaura o estado (com uma inicialização a frio). |
| **Software pré-instalado** | Ambiente baseado no Ubuntu com Python 3.12 e Node.js 22. Para mais informações sobre a imagem de base do ambiente, consulte [Software pré-instalado](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br#pre-installed-software). |
| **Número máximo de agentes** | É possível ter até 1.000 agentes gerenciados. |

## Frameworks de agentes

Também é possível criar agentes com o Gemini usando estes frameworks e SDKs:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=pt-br): crie
  fluxos de aplicativos com estado e complexos e sistemas multiagente usando estruturas de grafo.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=pt-br): conecte agentes do Gemini aos seus dados particulares para fluxos de trabalho aprimorados por RAG.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=pt-br): orquestre agentes de IA autônomos e colaborativos de interpretação de papéis.
- [**SDK de IA do Vercel**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=pt-br): crie
  interfaces e agentes de usuário com tecnologia de IA em JavaScript/TypeScript.
- [**\*\*ADK do Google\*\***](https://google.github.io/adk-docs/get-started/python/): um
  framework de código aberto para criar e orquestrar agentes de IA
  interoperáveis.
- [**SDK do Antigravity**](https://antigravity.google/product/antigravity-sdk?hl=pt-br): crie
  agentes de IA autônomos usando as mesmas ferramentas, loop de agente e gerenciamento de contexto
  que alimentam o Google Antigravity, programável em Python.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-10 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-10 UTC."],[],[]]
