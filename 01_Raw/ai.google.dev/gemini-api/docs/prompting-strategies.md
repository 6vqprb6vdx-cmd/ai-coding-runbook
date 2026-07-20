---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pt-BR
fetched_at: 2026-07-20T04:41:03.506766+00:00
title: "Estrat\u00e9gias de design de comandos \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Estratégias de design de comandos

*Design de comando* é o processo de criação de comandos ou solicitações em linguagem natural
que extraem respostas precisas e de alta qualidade de um modelo de linguagem.

Nesta página, apresentamos conceitos básicos, estratégias e práticas recomendadas para você começar a criar comandos e aproveitar ao máximo os modelos de IA do Gemini.

## Guias de comandos específicos para temas

Quer estratégias de comandos mais específicas? Confira nossos outros guias
em:

- [Comandos com arquivos de mídia](https://ai.google.dev/gemini-api/docs/files?hl=pt-br#prompt-guide)
- Comandos para geração de imagens com a [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=pt-br#imagen-prompt-guide) e a [Geração de imagens nativa do Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br#prompt-guide)
- [Comandos para geração de vídeo](https://ai.google.dev/gemini-api/docs/video?hl=pt-br#prompt-guide)

Você pode encontrar outros exemplos de comandos na [galeria de comandos](https://ai.google.dev/gemini-api/prompts?hl=pt-br), que mostra de forma interativa muitos dos conceitos compartilhados neste guia.

## Instruções claras e específicas

Uma maneira eficaz e eficiente de personalizar o comportamento do modelo é fornecer instruções claras e específicas. As instruções podem ser uma pergunta,
tarefas detalhadas ou tão complexas quanto mapear a experiência e a mentalidade de um usuário.

### Entrada

A entrada é o texto obrigatório no comando para o qual você quer que o modelo forneça uma resposta. As entradas podem ser uma pergunta que o modelo responde (entrada de pergunta), uma tarefa que o modelo realiza (entrada de tarefa), uma entidade em que o modelo opera (entrada de entidade) ou entrada parcial que o modelo conclui ou continue (entrada concluída).

| **Tipo de entrada** | **Comando** | **Saída gerada** |
| --- | --- | --- |
| Pergunta | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| Tarefa | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| Entidade | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### Conclusão parcial de entrada

Os modelos de linguagem generativa funcionam como uma ferramenta avançada de preenchimento automático. Quando você fornece conteúdo parcial, o modelo pode fornecer o restante do conteúdo ou o que considera ser uma continuação desse conteúdo, como uma resposta. Ao fazer isso, se você incluir exemplos ou contexto, o modelo poderá levar esses exemplos ou contexto em consideração.

O exemplo a seguir fornece um prompt com uma instrução e uma entrada de entidade:

|  |
| --- |
| **Comando**:    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **Resposta:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

Embora o modelo tenha feito o que foi solicitado, escrever as instruções em linguagem natural às vezes pode ser desafiador e deixar muito para a interpretação do modelo.
Por exemplo, o cardápio de um restaurante pode conter muitos itens. Para reduzir o tamanho da resposta JSON, omita os itens que não foram ordenados. Nesse caso, é possível fornecer um exemplo e um prefixo de resposta e deixar o modelo
concluí-lo:

|  |
| --- |
| **Comando**:    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **Resposta:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

Observe como "cheeseburger" foi excluído da saída porque não fazia parte do pedido.

Embora seja possível especificar o formato de objetos de resposta JSON simples usando comandos,
recomendamos usar o recurso de
[saída estruturada](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br) da API Gemini ao especificar
um esquema JSON mais complexo para a resposta.

### Restrições

Especifique as restrições à leitura do comando ou à geração de uma resposta. Você pode
dizer ao modelo o que fazer e o que não fazer. Por exemplo, é possível especificar uma restrição
no comando sobre a duração de um resumo:

|  |
| --- |
| **Comando**:     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **Resposta**:     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### Formato da resposta

Você pode dar instruções que especifiquem o formato da resposta. Por exemplo, você pode pedir que a resposta seja formatada como tabela, lista com marcadores, argumento rápido de venda, palavras-chave, frase ou parágrafo. A instrução do sistema a seguir informa ao modelo para ser mais conversacional na resposta:

|  |
| --- |
| **Instrução do sistema**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **Comando**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **Resposta:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### Formatar respostas com a estratégia de conclusão

A [estratégia de conclusão](#completion) também pode ajudar a formatar a resposta.
O exemplo a seguir solicita que o modelo crie um esboço de redação:

|  |
| --- |
| **Comando**:    ``` Create an outline for an essay about hummingbirds. ```  **Resposta:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

O comando não especificou o formato da estrutura de tópicos, e o modelo escolheu um formato para você. Para que o modelo retorne uma estrutura de tópicos em um formato específico, adicione texto que represente o início dela e deixe que o modelo a conclua com base no padrão iniciado.

|  |
| --- |
| **Comando**:    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **Resposta:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## Tomada zero ou poucas fotos

Você pode incluir exemplos no prompt que mostram ao modelo como fazer isso da forma certa. O modelo tenta identificar padrões e relações nos exemplos e os aplica ao gerar uma resposta. As solicitações que contêm alguns exemplos são chamadas de *solicitações curtas*, enquanto as que não fornecem exemplos são chamadas de *solicitações de zero disparo*. Muitas vezes, as solicitações de imagem são usadas para regular a formatação, a frase, o escopo ou o padrão geral das respostas do modelo. Use exemplos específicos e variados para ajudar o modelo a restringir o foco e gerar resultados mais precisos.

Recomendamos sempre incluir exemplos few-shot nos comandos. As instruções sem exemplos de poucos disparos provavelmente serão menos eficazes. Na verdade, é possível remover
instruções do comando se os exemplos forem claros o suficiente para mostrar a
tarefa em questão.

O prompt de imagem zero pede ao modelo para escolher a melhor explicação.

|  |
| --- |
| **Comando**:    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Resposta:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

Se o caso de uso exigir que o modelo produza respostas concisas, inclua exemplos no comando para dar preferência a respostas concisas.

O prompt a seguir fornece dois exemplos que mostram preferência pelas explicações mais curtas. Na resposta, é possível ver que os exemplos guiaram o modelo para escolher a explicação mais curta (`Explanation2`), em vez da explicação mais longa (`Explanation1`) como fazia anteriormente.

|  |
| --- |
| **Comando**:    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Resposta:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### Número ideal de exemplos

Modelos como o Gemini geralmente podem identificar padrões usando alguns exemplos. No entanto, talvez seja necessário testar quantos exemplos fornecer no comando para ter os melhores resultados. Ao mesmo tempo, se você incluir muitos exemplos, o modelo poderá começar a [sobrepor](https://developers.google.com/machine-learning/glossary?hl=pt-br#overfitting) a resposta aos exemplos.

### Consistência no formato

Confira se a estrutura e a formatação dos exemplos few-shot são iguais para evitar respostas com formatos indesejados. Um dos principais objetivos de adicionar exemplos few-shot nos comandos é mostrar ao modelo o formato da resposta. Portanto, é essencial garantir um formato consistente em todos os exemplos, especialmente prestando atenção às tags XML, espaços em branco, novas linhas e divisores de exemplo.

## Adicionar contexto

É possível incluir nas instruções e informações do comando que o modelo precisa para resolver um problema, em vez de presumir que o modelo tem todas as informações necessárias. Essas informações contextuais ajudam o modelo a entender as restrições e os detalhes do que você está pedindo que ele faça.

O exemplo a seguir pede ao modelo que forneça orientação para solução de problemas de um roteador:

|  |
| --- |
| **Comando**:    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **Resposta:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

A resposta se parece com informações genéricas de solução de problemas que não são específicas
do roteador ou do status das luzes indicadoras de LED.

Para personalizar a resposta do roteador específico, é possível adicionar ao prompt o guia de solução de problemas dele como contexto para consulta ao fornecer uma resposta.

|  |
| --- |
| **Comando**:    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **Resposta:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## Dividir comandos em componentes

Para casos de uso que exigem solicitações complexas, é possível ajudar o modelo a gerenciar essa complexidade dividindo os itens em componentes mais simples.

1. **Divida as instruções**:em vez de ter várias instruções em um só comando, crie um por instrução. Você pode escolher qual solicitação processar com base na entrada do usuário.
2. **Encadeie comandos**:para tarefas complexas que envolvem várias etapas sequenciais, transforme cada etapa em um comando e encadeie os comandos em uma sequência. Nessa cadeia sequencial, a saída de um comando na sequência se torna a entrada do próximo comando. A saída do último comando na sequência
   é a saída final.
3. **Agregar respostas**:a agregação é quando você quer executar diferentes tarefas paralelas em diferentes partes dos dados e agregar os resultados para produzir a saída final. Por exemplo, é possível dizer ao modelo para executar uma operação na primeira parte dos dados, executar outra operação no restante dos dados e agregar os resultados.

## Testar parâmetros do modelo

Cada chamada que você envia a um modelo inclui valores de parâmetros que controlam como o modelo gera uma resposta. O modelo pode gerar diferentes resultados para diferentes valores de parâmetros. Teste diferentes valores de parâmetros para conseguir os melhores valores para a tarefa. Os parâmetros disponíveis para modelos diferentes podem ser diferentes. Os parâmetros mais comuns são:

1. **Máximo de tokens de saída**:especifica o número máximo de tokens que podem ser gerados na resposta. Um token tem cerca de quatro caracteres. 100 tokens correspondem a cerca de 60 a 80 palavras.
2. **Temperatura**:controla o grau de aleatoriedade na seleção de tokens. A temperatura é usada para amostragem durante a geração de respostas,
   que ocorre quando `topP` e `topK` são aplicados. Temperaturas mais baixas são boas para comandos que exigem uma resposta mais determinista ou menos aberta, enquanto temperaturas mais altas podem levar a resultados mais diversos ou criativos. Uma temperatura 0 é determinista, o que significa que a resposta de maior probabilidade é sempre selecionada.
3. **`topK`**:o parâmetro `topK` muda a forma como o modelo seleciona tokens para saída. Um `topK` de 1 significa que o token selecionado é o mais provável entre todos os tokens no vocabulário do modelo (também chamado de decodificação gananciosa), enquanto um `topK` de 3 significa que o próximo token é selecionado entre os três mais prováveis usando a temperatura. Em cada etapa de seleção de token, são escolhidos os tokens `topK` com as maiores probabilidades. Em seguida, os tokens são filtrados com base no `topP`, com o token final selecionado usando a amostragem de temperatura.
4. **`topP`**:o parâmetro `topP` muda a forma como o modelo seleciona tokens para saída. Os tokens são selecionados do mais ao menos provável até que a soma das probabilidades seja igual ao valor `topP`. Por exemplo, se os tokens A, B e C tiverem uma probabilidade de 0,3, 0,2 e 0,1 e o valor de `topP` for 0,5, o modelo vai selecionar A ou B como token seguinte usando a temperatura e excluir C como candidato. O valor padrão de `topP` é 0,95.
5. **`stop_sequences`**:defina uma sequência de parada para
   instruir o modelo a parar de gerar conteúdo. Uma sequência de parada pode ser qualquer
   sequência de caracteres. Evite usar uma sequência de caracteres que possa aparecer no conteúdo gerado.

## Estratégias de iteração de prompt

Às vezes, o design de comandos exige algumas iterações até que você receba a resposta desejada de forma consistente. Esta seção fornece orientações sobre algumas coisas que você pode tentar ao iterar nas suas solicitações:

1. **Use frases diferentes**:usar palavras ou frases diferentes nos comandos costuma gerar respostas diferentes do modelo, mesmo que todas tenham o mesmo significado. Se você não estiver recebendo os resultados esperados, tente reformular o comando.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **Mude para uma tarefa análoga**:se você não conseguir que o modelo siga suas instruções para uma tarefa, tente dar a ele instruções para uma tarefa análoga que consiga o mesmo resultado.

   Esse comando instrui o modelo a categorizar um livro usando categorias predefinidas:

   |  |
   | --- |
   | **Comando**:    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **Resposta:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   A resposta está correta, mas o modelo não permaneceu dentro dos limites das opções. Você também precisa modelar para responder apenas com uma das opções, em vez de em uma frase completa. Nesse caso, é possível reformular as instruções como uma pergunta de múltipla escolha e solicitar que o modelo escolha uma opção.

   |  |
   | --- |
   | **Comando**:    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **Resposta:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **Mude a ordem do conteúdo do comando**:às vezes, a ordem do conteúdo no comando afeta a resposta. Tente mudar a ordem do conteúdo e veja
     como isso afeta a resposta.

     ```
     Version 1:
     [examples]
     [context]
     [input]

     Version 2:
     [input]
     [examples]
     [context]

     Version 3:
     [examples]
     [input]
     [context]
     ```

## Respostas substitutas

Uma resposta substituta é retornada pelo modelo quando a solicitação ou a resposta acionam um filtro de segurança. Um exemplo de resposta substituta é "Não posso ajudar com isso, porque sou apenas um modelo de linguagem".

Se o modelo responder com uma resposta substituta, tente aumentar a temperatura.

## Embasamento e execução de código

O Gemini pode usar ferramentas para evitar alucinações em cenários em que poderia produzir respostas incorretas.

O [embasamento com a Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br) conecta o modelo do Gemini ao conteúdo da Web em tempo real e precisa ser ativado sempre que o modelo precisar saber fatos obscuros ou recentes.

A [ferramenta de execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br) do Gemini permite que o modelo gere e execute código Python. Ela deve ser ativada sempre que o modelo precisar realizar qualquer tipo de aritmética, contagem ou cálculo.

## Gemini 3

Os [modelos do Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=pt-br#gemini-3) foram criados para raciocínio avançado e seguimento de instruções.
Elas respondem melhor a comandos diretos, bem estruturados e que definem claramente a tarefa e as restrições. As seguintes práticas são recomendadas para resultados ideais com o Gemini 3:

### Princípios básicos de criação de comandos

- **Seja preciso e direto**:defina seu objetivo de maneira clara e concisa. Evite linguagem desnecessária ou excessivamente persuasiva.
- **Use uma estrutura consistente**:use delimitadores claros para separar diferentes partes do comando. Tags no estilo XML (por exemplo, `<context>`, `<task>`) ou cabeçalhos em Markdown são eficazes. Escolha um formato e use-o de maneira consistente em um único comando.
- **Defina parâmetros**:explique explicitamente termos ou parâmetros ambíguos.
- **Controlar o nível de detalhes da resposta**:por padrão, os modelos do Gemini 3 fornecem respostas diretas e eficientes. Se você precisar de uma resposta mais detalhada ou em formato de conversa, peça isso explicitamente nas instruções.
- **Trate as entradas multimodais de maneira coerente**:ao usar texto, imagens, áudio ou vídeo, trate-os como entradas de mesma classe. Verifique se as instruções referenciam claramente cada modalidade, conforme necessário.
- **Priorize instruções críticas**:coloque restrições comportamentais essenciais, definições de função (persona) e requisitos de formato de saída na instrução do sistema ou no início do comando do usuário.
- **Estrutura para contextos longos**:ao fornecer grandes quantidades de contexto (por exemplo, documentos, código), forneça todo o contexto primeiro. Coloque suas instruções ou perguntas específicas no *final* do comando.
- **Contexto de ancoragem**:depois de um grande bloco de dados, use uma frase de transição clara para conectar o contexto e sua consulta, como "Com base nas informações acima..."

### Estratégias do Gemini 3 Flash

- **Precisão do dia atual**:adicione a seguinte cláusula às instruções do sistema para ajudar o modelo a prestar atenção ao dia atual em 2026:

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **Acurácia do limite de conhecimento**:adicione a seguinte cláusula às instruções do sistema para que o modelo saiba sobre o limite de conhecimento:

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **Performance de embasamento**:adicione a seguinte cláusula às instruções do sistema (com edições quando apropriado) para melhorar a capacidade do modelo de embasar as respostas no contexto fornecido:

  ```
  You are a strictly grounded assistant limited to the information provided in
  the User Context. In your answers, rely **only** on the facts that are
  directly mentioned in that context. You must **not** access or utilize your
  own knowledge or common sense to answer. Do not assume or infer from the
  provided facts; simply report them exactly as they appear. Your answer must
  be factual and fully truthful to the provided text, leaving absolutely no
  room for speculation or interpretation. Treat the provided context as the
  absolute limit of truth; any facts or details that are not directly
  mentioned in the context must be considered **completely untruthful** and
  **completely unsupported**. If the exact answer is not explicitly written in
  the context, you must state that the information is not available.
  ```

### Melhorar o raciocínio e o planejamento

Os modelos das séries Gemini 2.5 e 3 geram automaticamente um texto interno de "pensamento" para melhorar o desempenho do raciocínio. Por isso, geralmente não é necessário que o modelo descreva, planeje ou detalhe as etapas de raciocínio na resposta retornada. Para problemas que exigem muito raciocínio, solicitações simples como "Pense muito antes de responder" podem melhorar o desempenho, mas ao custo de tokens de pensamento extras.

Consulte a documentação sobre o [raciocínio do Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br) para mais detalhes.

### Exemplos de comandos estruturados

Usar tags ou Markdown ajuda o modelo a distinguir entre instruções, contexto e tarefas.

**Exemplo de XML:**

```
<role>
You are a helpful assistant.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Insert User Input Here - The model knows this is data, not instructions]
</context>

<task>
[Insert the specific user request here]
</task>
```

**Exemplo de Markdown:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### Exemplo de modelo que combina práticas recomendadas

Este modelo captura os princípios básicos para comandos com o Gemini 3. Sempre itere e modifique para seu caso de uso específico.

**Instrução do sistema**:

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan.
2. **Execute**: Carry out the plan.
3. **Validate**: Review your output against the user's task.
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Specify Low/Medium/High]
- Tone: [Specify Formal/Casual/Technical]
</constraints>

<output_format>
Structure your response as follows:
1. **Executive Summary**: [Short overview]
2. **Detailed Response**: [The main content]
</output_format>
```

**Comando do usuário:**

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

## Fluxos de trabalho com agentes

Para fluxos de trabalho de agentes complexos, geralmente são necessárias instruções específicas para controlar como o modelo raciocina, planeja e executa tarefas. Embora o Gemini ofereça um desempenho geral excelente, os agentes complexos geralmente exigem que você configure a compensação entre custo computacional (latência e tokens) e precisão da tarefa.

Ao criar comandos para agentes, considere as seguintes dimensões de comportamento que podem ser direcionadas no agente:

### Raciocínio e estratégia

Configuração de como o modelo pensa e planeja antes de agir.

- **Decomposição lógica**:define a profundidade com que o modelo precisa analisar restrições, pré-requisitos e a ordem das operações.
- **Diagnóstico de problemas**: controla a profundidade da análise ao identificar causas e o uso do raciocínio abdutivo pelo modelo. Determina se o modelo deve aceitar a resposta mais óbvia ou explorar explicações complexas e menos prováveis.
- **Exaustividade das informações**:a troca entre analisar todas as políticas e documentos disponíveis e priorizar a eficiência e a velocidade.

### Execução e confiabilidade

Configuração de como o agente opera de forma autônoma e lida com obstáculos.

- **Adaptabilidade**:como o modelo reage a novos dados. Determina se ele deve aderir estritamente ao plano inicial ou mudar imediatamente quando as observações contradizem as proposições.
- **Persistência e recuperação**:o grau em que o modelo tenta corrigir erros por conta própria. A alta persistência aumenta as taxas de sucesso, mas pode gerar custos de token ou loops mais altos.
- **Avaliação de risco**:a lógica para avaliar as consequências. Distingue explicitamente entre ações exploratórias de baixo risco (leituras) e mudanças de estado de alto risco (gravações).

### Interação e saída

Configuração de como o agente se comunica com o usuário e formata os resultados.

- **Ambiguidade e tratamento de permissões**:define quando o modelo pode fazer suposições e quando ele precisa pausar a execução para pedir esclarecimentos ou permissão ao usuário.
- **Nível de detalhe**:controla o volume de texto gerado junto com as chamadas de ferramentas. Isso determina se o modelo explica as ações para o usuário ou permanece em silêncio durante a execução.
- **Precisão e integridade**:a fidelidade necessária da saída. Especifica se o modelo precisa resolver todos os casos extremos e fornecer números exatos ou se estimativas aproximadas são aceitáveis.

### Modelo de instrução do sistema

A instrução do sistema a seguir é um exemplo que foi avaliado por pesquisadores para melhorar a performance em comparativos de agentes em que o modelo precisa obedecer a um conjunto de regras complexo e interagir com um usuário. Ela incentiva o agente a agir como um planejador e raciocinador forte, impõe comportamentos específicos nas dimensões listadas acima e exige que o modelo planeje de forma proativa antes de realizar qualquer ação.

Você pode adaptar esse modelo para atender às restrições do seu caso de uso específico.

```
You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:
    1.1) Policy-based rules, mandatory prerequisites, and constraints.
    1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.
        1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.
    1.3) Other prerequisites (information and/or actions needed).
    1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?
    2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk. **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.
    3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.
    3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.
    3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?
    4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:
    5.1) Using available tools and their capabilities
    5.2) All policies, rules, checklists, and constraints
    5.3) Previous observations and conversation history
    5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.
    6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them. 

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.
    7.1) Resolve conflicts using the order of importance in #1.
    7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.
        7.2.1) To check for whether an option is relevant, reason about all information sources from #5.
        7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.
    7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.
    8.1) Don't be dissuaded by time taken or user frustration.
    8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.
```

## Próximas etapas

- Agora que você tem um entendimento mais profundo sobre o design de comandos, tente escrever seus
  próprios comandos usando o [Google AI Studio](http://aistudio.google.com?hl=pt-br).
- Para saber mais sobre comandos multimodais, consulte
  [Comandos com arquivos de mídia](https://ai.google.dev/gemini-api/docs/files?hl=pt-br#prompt-guide).
- Para saber mais sobre comandos de imagem, consulte os guias de comandos do [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br#prompt-guide) e do [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=pt-br#imagen-prompt-guide).
- Para saber mais sobre comandos de vídeo, consulte o [guia de comandos do Veo](https://ai.google.dev/gemini-api/docs/video?hl=pt-br#prompt-guide).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-10 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-10 UTC."],[],[]]
