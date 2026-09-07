---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=pt-BR
fetched_at: 2026-09-07T05:34:39.453602+00:00
title: "Pensamento do Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Pensamento do Gemini

Os modelos das séries [Gemini 3 e 2.5](https://ai.google.dev/gemini-api/docs/models?hl=pt-br) usam um
"processo de raciocínio" interno que melhora significativamente as habilidades de raciocínio e planejamento de várias etapas, tornando-os altamente eficazes para tarefas complexas, como
programação, matemática avançada e análise de dados.

Este guia mostra como trabalhar com os recursos de raciocínio do Gemini usando a API Gemini.

## Gerar conteúdo com raciocínio

Iniciar uma solicitação com um modelo de raciocínio é semelhante a qualquer outra solicitação de geração de conteúdo. A principal diferença está em especificar um dos
[modelos com suporte de raciocínio](#supported-models) no campo `model`, conforme
demonstrado no exemplo de [geração de texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br#text-input) a seguir:

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.8-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## Resumos de raciocínio

Os resumos de raciocínio são versões resumidas dos pensamentos brutos do modelo e oferecem insights sobre o processo de raciocínio interno do modelo. Os níveis e orçamentos de raciocínio se aplicam aos pensamentos brutos do modelo e não aos resumos de raciocínio.

É possível ativar os resumos de raciocínio definindo `includeThoughts` como `true` na configuração da solicitação. Em seguida, acesse o resumo iterando pelas `parts` do parâmetro `response` e verificando o booleano `thought`.

Confira um exemplo que demonstra como ativar e recuperar resumos de raciocínio sem streaming, que retorna um único resumo de raciocínio final com a resposta:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.8-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

Confira um exemplo de uso do raciocínio com streaming, que retorna resumos incrementais durante a geração:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.8-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.8-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
  }
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.8-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## Controlar o raciocínio

Os modelos do Gemini se envolvem no raciocínio dinâmico por padrão, ajustando automaticamente a quantidade de esforço de raciocínio com base na complexidade da solicitação do usuário.
No entanto, se você tiver restrições de latência específicas ou exigir que o modelo se envolva em um raciocínio mais profundo do que o normal, use parâmetros para controlar o comportamento de raciocínio.

### Níveis de raciocínio (Gemini 3)

O parâmetro `thinkingLevel`, recomendado para modelos do Gemini 3 e versões mais recentes, permite controlar o comportamento de raciocínio.

A tabela a seguir detalha as configurações de `thinkingLevel` para cada tipo de modelo:

| Nível de raciocínio | Gemini 3.8 e 3.7 Flash | Gemini 3.6 e 3.5 Flash | Gemini 3.1 Pro | Gemini 3.5 e 3.1 Flash-Lite | Imagem do Gemini 3.1 Flash-Lite | Gemini 3 Flash | Descrição |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | Indisponível (erro) | Compatível | Indisponível | Compatível (padrão) | Compatível (padrão) | Compatível | Corresponde à configuração "sem raciocínio" para a maioria das consultas. Observação: `minimal` não garante que o raciocínio esteja desativado. O modelo pode raciocinar de forma muito mínima para tarefas complexas. |
| **`low`** | Compatível | Compatível | Compatível | Compatível | Não compatível | Compatível | Minimiza a latência e o custo. |
| **`medium`** | Compatível (padrão) | Compatível (padrão) | Compatível | Compatível | Indisponível | Compatível | Raciocínio equilibrado para a maioria das tarefas. |
| **`high`** | Compatível (dinâmico) | Compatível (dinâmico) | Compatível (padrão, dinâmico) | Compatível (dinâmico) | Compatível (dinâmico) | Compatível (padrão, dinâmico) | Maximiza a profundidade do raciocínio. O modelo pode levar muito mais tempo para alcançar um primeiro token de saída (sem raciocínio), mas a saída será mais cuidadosamente raciocinada. |

O exemplo a seguir mostra como definir o nível de raciocínio.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Não é possível desativar o raciocínio do Gemini 3.1 Pro. O Gemini 3 Flash e o Flash-Lite
também não oferecem suporte ao raciocínio completo.
Se você não especificar um nível de raciocínio, o Gemini vai usar o nível de raciocínio padrão dos modelos do Gemini 3 (por exemplo, `"high"` para o Gemini 3.1 Pro e `"medium"` para o Gemini 3.5 Flash).

Os modelos da série Gemini 2.5 não oferecem suporte a `thinkingLevel`. Use `thinkingBudget`.

### Orçamentos de raciocínio

O parâmetro `thinkingBudget`, introduzido com a série Gemini 2.5, orienta o modelo sobre o número específico de tokens de raciocínio a serem usados para o raciocínio.

A seguir, confira os detalhes de configuração de `thinkingBudget` para cada tipo de modelo.
É possível desativar o raciocínio definindo `thinkingBudget` como 0.
Definir o `thinkingBudget` como -1 ativa o
**raciocínio dinâmico**, o que significa que o modelo vai ajustar o orçamento com base na
complexidade da solicitação.

| Modelo | Configuração padrão (o orçamento de raciocínio não está definido) | Intervalo | Desativar raciocínio | Ativar raciocínio dinâmico |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Raciocínio dinâmico | `128` a `32768` | N/A: não é possível desativar o raciocínio | `thinkingBudget = -1` (padrão) |
| **2.5 Flash** | Raciocínio dinâmico | `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (padrão) |
| **2.5 Flash Preview** | Raciocínio dinâmico | `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (padrão) |
| **2.5 Flash Lite** | O modelo não pensa | `512` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite Preview** | O modelo não pensa | `512` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 Preview** | Raciocínio dinâmico | `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (padrão) |
| **2.5 Flash Live Native Audio Preview (09-2025)** | Raciocínio dinâmico | `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (padrão) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

Dependendo do prompt, o modelo pode exceder ou ficar abaixo do orçamento de tokens.

## Assinaturas de raciocínio

A API Gemini não tem estado, então o modelo trata cada solicitação de API de forma independente e não tem acesso ao contexto de raciocínio de turnos anteriores em interações multiturno.

Para manter o contexto de raciocínio em interações multiturno, o Gemini retorna assinaturas de raciocínio, que são representações criptografadas do processo de raciocínio interno do modelo.

- **Os modelos do Gemini 2.5** retornam assinaturas de raciocínio quando o raciocínio está ativado e
  a solicitação inclui [chamadas de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br#thinking),
  especificamente [declarações de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br#step-2).
- Os **modelos do Gemini 3** podem retornar assinaturas de raciocínio para todos os tipos de [partes](https://ai.google.dev/api/caching?hl=pt-br#Part).
  Recomendamos que você sempre transmita todas as assinaturas de volta conforme recebidas, mas isso é *necessário* para assinaturas de chamadas de função. Leia a
  [página Assinaturas de raciocínio](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=pt-br) para
  saber mais.

Outras limitações de uso a serem consideradas com a chamada de função incluem:

- As assinaturas são retornadas do modelo em outras partes da resposta, por exemplo, chamadas de função ou partes de texto.
  [Retorne a resposta inteira](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br#step-4)
  com todas as partes para o modelo em turnos subsequentes.
- Não concatene partes com assinaturas.
- Não mescle uma parte com uma assinatura com outra parte sem uma assinatura.

## Preços

Quando o raciocínio está ativado, o preço da resposta é a soma dos tokens de saída e dos tokens de raciocínio. É possível acessar o número total de tokens de raciocínio gerados no campo `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

Os modelos de raciocínio geram pensamentos completos para melhorar a qualidade da resposta final
e, em seguida, resumos de saída para fornecer insights sobre o processo de raciocínio. Portanto, o preço é baseado nos tokens de pensamento completos que o modelo precisa gerar para criar um resumo, embora apenas o resumo seja gerado pela API.

Saiba mais sobre tokens no [guia Contagem de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br).

## Práticas recomendadas

Esta seção inclui algumas orientações para usar modelos de raciocínio de forma eficiente.
Como sempre, seguir nossas [orientações e práticas recomendadas de prompt](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pt-br) vai gerar os melhores resultados.

### Depuração e direção

- **Analisar o raciocínio**: quando você não recebe a resposta esperada dos
  modelos de raciocínio, pode ser útil analisar cuidadosamente os resumos de raciocínio do Gemini.
  É possível conferir como ele dividiu a tarefa e chegou à conclusão, e usar essas informações para corrigir os resultados certos.
- **Fornecer orientação no raciocínio**: se você espera uma saída particularmente longa, forneça orientação no prompt para restringir a
  [quantidade de raciocínio](#set-budget) que o modelo usa. Isso permite reservar mais da saída de token para sua resposta.

### Complexidade da tarefa

- **Tarefas fáceis (o raciocínio pode estar DESATIVADO)** : para solicitações simples em que o raciocínio complexo não é necessário, como recuperação ou classificação de fatos, o raciocínio não é necessário. Exemplos:
  - "Onde a DeepMind foi fundada?"
  - "Este e-mail está pedindo uma reunião ou apenas fornecendo informações?"
- **Tarefas médias (padrão/algum raciocínio)** : muitas solicitações comuns se beneficiam de um grau de processamento passo a passo ou de um entendimento mais profundo. O Gemini pode usar a capacidade de raciocínio de forma flexível para tarefas como:
  - Analogizar a fotossíntese e o crescimento.
  - Comparar e contrastar carros elétricos e híbridos.
- **Tarefas difíceis (capacidade máxima de raciocínio)** : para desafios realmente complexos, como resolver problemas de matemática complexos ou tarefas de programação, recomendamos definir um orçamento de raciocínio alto. Esses tipos de tarefas exigem que o modelo envolva todos os recursos de raciocínio e planejamento, geralmente envolvendo muitas etapas internas antes de fornecer uma resposta. Exemplos:
  - Resolva o problema 1 no AIME 2025: encontre a soma de todas as bases inteiras b > 9 para
    as quais 17b é um divisor de 97b.
  - Escreva um código Python para um aplicativo da Web que visualize dados do mercado de ações em tempo real, incluindo a autenticação do usuário. Deixe-o o mais eficiente possível.

## Modelos, ferramentas e recursos compatíveis

Os recursos de raciocínio são compatíveis com todos os modelos das séries 3 e 2.5.
Você pode encontrar todos os recursos do modelo na
[página de visão geral do modelo](https://ai.google.dev/gemini-api/docs/models?hl=pt-br).

Os modelos de raciocínio funcionam com todas as ferramentas e recursos do Gemini. Isso permite que os modelos interajam com sistemas externos, executem códigos ou acessem informações em tempo real, incorporando os resultados ao raciocínio e à resposta final.

Você pode conferir exemplos de uso de ferramentas com modelos de raciocínio no [cookbook de raciocínio][Colab].

## A seguir

- A cobertura de raciocínio está disponível no nosso guia de [compatibilidade com a OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br#thinking).

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-04 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-04 UTC."],[],[]]
