---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=pt-BR
fetched_at: 2026-06-22T06:29:00.224710+00:00
title: "Vis\u00e3o geral da API Gemini Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Visão geral da API Gemini Live

A API Live permite interações de voz e visão em tempo real e com baixa latência com o Gemini. Ela processa fluxos contínuos de áudio, imagens e texto para fornecer respostas faladas imediatas e semelhantes às humanas, criando uma experiência de conversa natural para os usuários.

![Visão geral da API Live](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=pt-br)

[Testar a API Live no Google AI Studiomic](https://aistudio.google.com/live?hl=pt-br)
[Exemplo de apps clonados do GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Usar habilidades do agente de codificaçãoterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pt-br)

## Casos de uso

A API Live pode ser usada para criar agentes de voz em tempo real para vários setores, incluindo:

- **E-commerce e varejo**:assistentes de compras que oferecem recomendações personalizadas e representantes de suporte ao cliente que resolvem problemas dos clientes.
- **Jogos**:personagens não jogáveis (NPCs) interativos, assistentes de ajuda no jogo e tradução em tempo real do conteúdo do jogo.
- **Interfaces de última geração**:experiências ativadas por voz e vídeo em robótica, óculos inteligentes e veículos.
- **Saúde**:acompanhantes de saúde para suporte e educação de pacientes.
- **Serviços financeiros**:consultores de IA para gestão de patrimônio e orientação de investimentos.
- **Educação**:mentores de IA e acompanhantes de aprendizado que oferecem instrução e feedback personalizados.
- **Tradução e localização**:tradução em tempo real e com baixa latência de conversas faladas, permitindo uma comunicação multilíngue perfeita.

## Principais recursos

A API Live oferece um conjunto abrangente de recursos para criar agentes de voz robustos:

- [**Suporte multilíngue**](https://ai.google.dev/gemini-api/docs/live-guide?hl=pt-br#supported-languages):
  Converse em 70 idiomas compatíveis.
- [**Interrupção**](https://ai.google.dev/gemini-api/docs/live-guide?hl=pt-br#interruptions):
  os usuários podem interromper o modelo a qualquer momento para interações responsivas.
- [**Uso de ferramentas**](https://ai.google.dev/gemini-api/docs/live-tools?hl=pt-br):
  integra ferramentas como chamadas de função e a Pesquisa Google para interações dinâmicas.
- [**Transcrições de áudio**](https://ai.google.dev/gemini-api/docs/live-guide?hl=pt-br#audio-transcription):
  fornece transcrições de texto da entrada do usuário e da saída do modelo.
- [**Áudio proativo**](https://ai.google.dev/gemini-api/docs/live-guide?hl=pt-br#proactive-audio):
  Permite controlar quando o modelo responde e em quais contextos.
- [**Diálogo afetivo**](https://ai.google.dev/gemini-api/docs/live-guide?hl=pt-br#affective-dialog):
  adapta o estilo e o tom da resposta para corresponder à expressão de entrada do usuário.
- [**\*\*Tradução instantânea\*\***](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=pt-br):
  tradução de voz para voz em tempo real em mais de 70 idiomas.

## Especificações técnicas

A tabela a seguir descreve as especificações técnicas da API Live:

| Categoria | Detalhes |
| --- | --- |
| Modalidades de entrada | Áudio (áudio PCM bruto de 16 bits, 16 kHz, little-endian), imagens (JPEG <= 1 FPS), texto |
| Modalidades de saída | Áudio (áudio PCM bruto de 16 bits, 24 kHz, little-endian) |
| Protocolo | Conexão WebSocket com estado (WSS) |

## Escolher uma abordagem de implementação

Ao fazer a integração com a API Live, você precisa escolher uma das seguintes abordagens de implementação:

- **Servidor para servidor**: seu back-end se conecta à API Live usando
  [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Normalmente, o cliente envia dados de stream (áudio, vídeo, texto) para o servidor, que os encaminha para a API Live.
- **Cliente para servidor**: o código de front-end se conecta diretamente à API Live
  usando [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) para transmitir dados, ignorando o back-end.

## Primeiros passos

Selecione o guia que corresponde ao seu ambiente de desenvolvimento:

Servidor para servidor

### [Tutorial do SDK GenAI](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=pt-br)

Conecte-se à API Gemini Live usando o SDK GenAI para criar um aplicativo multimodal em tempo real com um back-end Python.

Cliente para servidor

### [Tutorial do WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=pt-br)

Conecte-se à API Gemini Live usando WebSockets para criar um aplicativo multimodal em tempo real com um front-end JavaScript e tokens temporários.

Kit de desenvolvimento de agente

### [Tutorial do ADK](https://google.github.io/adk-docs/streaming/)

Crie um agente e use o Kit de Desenvolvimento de Agente (ADK) Streaming para ativar a comunicação de voz e vídeo.

## Integrações com parceiros

Para simplificar o desenvolvimento de apps de áudio e vídeo em tempo real, você pode usar
uma integração de terceiros que ofereça suporte à API Gemini Live
pelo WebRTC ou WebSockets.

[LiveKit

Use a API Gemini Live com os agentes do LiveKit.](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat by Daily

Crie um chatbot de IA em tempo real usando o Gemini Live e o Pipecat.](https://docs.pipecat.ai/guides/features/gemini-live)
[Fishjam by Software Mansion

Crie aplicativos de streaming de vídeo e áudio ao vivo com o Fishjam.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Vision Agents by Stream

Crie aplicativos de IA de voz e vídeo em tempo real com os Vision Agents.](https://visionagents.ai/integrations/gemini)
[Voximplant

Conecte chamadas recebidas e efetuadas à API Live com o Voximplant.](https://voximplant.com/products/gemini-client)
[Agora

Crie aplicativos de IA conversacional em tempo real com o Agora.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[SDK de IA do Firebase

Comece a usar a API Gemini Live com o Firebase AI Logic.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=pt-br)

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-12 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-12 UTC."],[],[]]
