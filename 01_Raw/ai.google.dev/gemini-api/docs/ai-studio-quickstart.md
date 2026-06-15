---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=pt-BR
fetched_at: 2026-06-15T06:22:21.807058+00:00
title: "Guia de in\u00edcio r\u00e1pido do Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Guia de início rápido do Google AI Studio

[O Google AI Studio](https://aistudio.google.com/?hl=pt-br) permite que você teste rapidamente
modelos e experimente diferentes comandos. Quando estiver tudo pronto, você
pode selecionar "Gerar código" e a linguagem de programação de sua preferência para
usar a [API Gemini](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br).

## Comandos e configurações

O Google AI Studio oferece várias interfaces para comandos projetados para diferentes casos de uso. Este guia aborda os **comandos de chat**, usados para criar
experiências conversacionais. Essa técnica de comando permite várias entradas
e respostas para gerar a saída. Saiba mais com o nosso
[exemplo de comando de chat abaixo](#chat_example).
Outras opções incluem **transmissão em tempo real**, **geração de vídeo** e
muito mais.

O AI Studio também oferece o painel **Configurações de execução**, em que é possível fazer
ajustes nos [parâmetros do modelo](https://ai.google.dev/docs/prompting-strategies?hl=pt-br#model-parameters),
[configurações de segurança](https://ai.google.dev/gemini-api/docs/safety-settings?hl=pt-br) e ativar ferramentas como
[saída estruturada](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br), [chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br), [execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br) e [embasamento](https://ai.google.dev/gemini-api/docs/grounding?hl=pt-br).

## Exemplo de comando de chat: criar um aplicativo de chat personalizado

Se você já usou um chatbot de uso geral, como o
[Gemini](https://gemini.google.com/?hl=pt-br), já sabe como os modelos de IA
generativa podem ser poderosos para diálogos abertos. Embora esses chatbots de uso geral sejam úteis, muitas vezes eles precisam ser personalizados para casos de uso específicos.

Por exemplo, talvez você queira criar um chatbot de atendimento ao cliente que só ofereça suporte a conversas sobre o produto de uma empresa. Ou um chatbot que fale com um tom ou estilo específico: um bot que faça muitas piadas, rime como um poeta ou use muitos emojis nas respostas.

Este exemplo mostra como usar o Google AI Studio para criar um chatbot amigável que se comunica como se fosse um alienígena vivendo em uma das luas de Júpiter, Europa.

### Etapa 1: criar um comando de chat

Para criar um chatbot, você precisa fornecer exemplos de interações entre um usuário e o chatbot para orientar o modelo a fornecer as respostas que você procura.

Para criar um comando de chat:

1. Abra o [Google AI Studio](https://aistudio.google.com/?hl=pt-br). O **Playground** será aberto por padrão com um novo comando de chat.
2. Clique em **Configurações de execução** tune no canto superior direito
   para expandir o painel e localize o
   [**Instruções do sistema**](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br#system-instructions)
   campo de entrada. Cole o seguinte no campo de entrada de texto:

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

Depois de adicionar as instruções do sistema, comece a testar o aplicativo conversando com o modelo:

1. Na caixa de entrada de texto com o rótulo **Digite algo...**, digite uma pergunta ou
   observação que um usuário possa fazer. Por exemplo:

   **Usuário:**

   ```
   What's the weather like?
   ```
2. Clique no botão **Executar** para receber uma resposta do chatbot. Essa resposta pode ser algo como:

   **Modelo:**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### Etapa 2: ensinar o bot a conversar melhor

Ao fornecer uma única instrução, você conseguiu criar um chatbot alienígena básico da Europa. No entanto, uma única instrução pode não ser suficiente para garantir a consistência e a qualidade das respostas do modelo. Sem instruções mais específicas, a resposta do modelo a uma pergunta sobre o clima tende a ser muito longa e pode ter uma mente própria.

Personalize o tom do chatbot adicionando às instruções do sistema:

1. Inicie um novo comando de chat ou use o mesmo. As instruções do sistema podem ser modificadas após o início da sessão de chat.
2. Na seção **Instruções do sistema**, mude as instruções que você já tem para o seguinte:

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. Digite novamente sua pergunta (`What's the weather like?`) e clique no botão **Executar**. Se você não iniciou um novo chat, sua resposta pode ser parecida com esta:

   **Modelo:**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

Você pode usar essa abordagem para adicionar mais profundidade ao chatbot. Faça mais perguntas, edite as respostas e melhore a qualidade do chatbot. Continue adicionando ou modificando as instruções e teste como elas mudam o comportamento do chatbot.

### Etapa 3: próximas etapas

Assim como os outros tipos de comando, depois de criar o protótipo do comando, você pode usar o botão **Gerar código** para começar a programar ou salvar o comando para trabalhar nele mais tarde e compartilhar com outras pessoas.

## Leitura adicional

- Se você já pode passar para o código, consulte os [guias de início rápido
  da API](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br).
- Para saber como criar comandos melhores, confira as [diretrizes de design de comandos](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-12 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-12 UTC."],[],[]]
