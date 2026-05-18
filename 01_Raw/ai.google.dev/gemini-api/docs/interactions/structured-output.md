---
source_url: https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=pt-BR
fetched_at: 2026-05-18T13:02:27.921364+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Respostas estruturadas

É possível configurar os modelos do Gemini para gerar respostas que sigam um esquema JSON fornecido. Isso garante resultados previsíveis e seguros de tipo e simplifica
a extração de dados estruturados de texto não estruturado.

Usar respostas estruturadas é ideal para:

- **Extração de dados**:extrai informações específicas, como nomes e datas, de um texto.
- **Classificação estruturada**:classifique textos em categorias predefinidas.
- **Fluxos de trabalho agênticos**:geram entradas estruturadas para ferramentas ou APIs.

Além de oferecer suporte ao esquema JSON na API REST, os SDKs da IA generativa do Google permitem definir esquemas usando [Pydantic](https://docs.pydantic.dev/latest/) (Python) e [Zod](https://zod.dev/) (JavaScript).

Extrator de receitas
Moderação de conteúdo
Estruturas recursivas

Este exemplo demonstra como extrair dados estruturados de texto usando tipos básicos de esquema JSON, como `object`, `array`, `string` e `integer`.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")

class Recipe(BaseModel):
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    ingredients: List[Ingredient]
    instructions: List[str]

client = genai.Client()

prompt = """
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.
"""

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.steps[-1].content[0].text)
print(recipe)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const recipeJsonSchema = {
  type: "object",
  properties: {
    recipe_name: {
      type: "string",
      description: "The name of the recipe."
    },
    prep_time_minutes: {
        type: "integer",
        description: "Optional time in minutes to prepare the recipe."
    },
    ingredients: {
      type: "array",
      items: {
        type: "object",
        properties: {
          name: { type: "string", description: "Name of the ingredient."},
          quantity: { type: "string", description: "Quantity of the ingredient, including units."}
        },
        required: ["name", "quantity"]
      }
    },
    instructions: {
      type: "array",
      items: { type: "string" }
    }
  },
  required: ["recipe_name", "ingredients", "instructions"]
};

const recipeSchema = z.fromJSONSchema(recipeJsonSchema);

const client = new GoogleGenAI({});

const prompt = `
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.
`;

const interaction = await client.interactions.create({
  model: "gemini-3-flash-preview",
  input: prompt,
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: recipeJsonSchema
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
console.log(recipe);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": "Please extract the recipe from the following text.\nThe user wants to make delicious chocolate chip cookies.\nThey need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,\n1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,\n3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.\nFor the best part, they will need 2 cups of semisweet chocolate chips.\nFirst, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,\nbaking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar\nuntil light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry\ningredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons\nonto ungreased baking sheets and bake for 9 to 11 minutes.",
      "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
          "type": "object",
          "properties": {
            "recipe_name": {
              "type": "string",
              "description": "The name of the recipe."
            },
            "prep_time_minutes": {
                "type": "integer",
                "description": "Optional time in minutes to prepare the recipe."
            },
            "ingredients": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": { "type": "string", "description": "Name of the ingredient."},
                  "quantity": { "type": "string", "description": "Quantity of the ingredient, including units."}
                },
                "required": ["name", "quantity"]
              }
            },
            "instructions": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["recipe_name", "ingredients", "instructions"]
        }
      }
      }
    }'
```

**Exemplo de resposta:**

```
{
  "recipe_name": "Delicious Chocolate Chip Cookies",
  "ingredients": [
    { "name": "all-purpose flour", "quantity": "2 and 1/4 cups" },
    { "name": "baking soda", "quantity": "1 teaspoon" },
    { "name": "salt", "quantity": "1 teaspoon" },
    { "name": "unsalted butter (softened)", "quantity": "1 cup" },
    { "name": "granulated sugar", "quantity": "3/4 cup" },
    { "name": "packed brown sugar", "quantity": "3/4 cup" },
    { "name": "vanilla extract", "quantity": "1 teaspoon" },
    { "name": "large eggs", "quantity": "2" },
    { "name": "semisweet chocolate chips", "quantity": "2 cups" }
  ],
  "instructions": [
    "Preheat the oven to 375°F (190°C).",
    "In a small bowl, whisk together the flour, baking soda, and salt.",
    "In a large bowl, cream together the butter, granulated sugar, and brown sugar until light and fluffy.",
    "Beat in the vanilla and eggs, one at a time.",
    "Gradually beat in the dry ingredients until just combined.",
    "Stir in the chocolate chips.",
    "Drop by rounded tablespoons onto ungreased baking sheets and bake for 9 to 11 minutes."
  ]
}
```

## Resultados de streaming

É possível transmitir saídas estruturadas, permitindo que você comece a processar a
resposta enquanto ela está sendo gerada. Os blocos transmitidos são strings JSON parciais válidas que podem ser concatenadas para formar o objeto JSON final.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
from pydantic import BaseModel
from typing import Literal

class Feedback(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    summary: str

client = genai.Client()
prompt = "The new UI is incredibly intuitive. Add a very long summary to test streaming!"

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Feedback.model_json_schema()
    },
    stream=True
)
for event in stream:
    if event.event_type == "step.delta" and event.delta.text:
        print(event.delta.text, end="")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const feedbackJsonSchema = {
  type: "object",
  properties: {
    sentiment: { type: "string", enum: ["positive", "neutral", "negative"] },
    summary: { type: "string" }
  },
  required: ["sentiment", "summary"]
};

const feedbackSchema = z.fromJSONSchema(feedbackJsonSchema);

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
  model: "gemini-3-flash-preview",
  input: "The new UI is incredibly intuitive. Add a very long summary!",
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: feedbackJsonSchema
  },
  stream: true,
});

for await (const event of stream) {
  if (event.type === "step.delta" && event.delta?.text) {
    process.stdout.write(event.delta.text);
  }
}
```

## Saídas estruturadas com ferramentas

Com o Gemini 3, você pode combinar saídas estruturadas com ferramentas integradas, incluindo
[Embasamento com a Pesquisa Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pt-br),
[Contexto de URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=pt-br),
[Execução de código](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pt-br), [Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=pt-br#structured-output) e
[Chamada de função](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pt-br).

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[{"type": "google_search"}, {"type": "url_context"}],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.steps[-1].content[0].text)
print(result)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string" },
    final_match_score: { type: "string" },
    scorers: { type: "array", items: { type: "string" } }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.1-pro-preview",
  input: "Search for all details for the latest Euro.",
  tools: [{type: "google_search"}, {type: "url_context"}],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: matchJsonSchema
  },
});

const match = matchSchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
console.log(match);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [{"type": "google_search"}, {"type": "url_context"}],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
            "winner": {"type": "string"},
            "final_match_score": {"type": "string"},
            "scorers": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["winner", "final_match_score", "scorers"]
      }
    }
  }'
```

## Suporte a esquemas JSON

Para gerar um objeto JSON, configure `response_format` com um objeto (ou uma matriz que contenha um objeto) do tipo `text` e defina `mime_type` como `application/json`. O esquema precisa ser fornecido no campo `schema`.

O modo de saída estruturada do Gemini é compatível com um subconjunto da especificação [JSON Schema](https://json-schema.org/).

Os seguintes valores de `type` são aceitos:

- **`string`**: para texto.
- **`number`**: para usar pontos flutuantes.
- **`integer`**: para números inteiros.
- **`boolean`**: para valores verdadeiro ou falso.
- **`object`**: para dados estruturados com pares de chave-valor.
- **`array`**: para listas de itens.
- **`null`**: para permitir que uma propriedade seja nula, inclua `"null"` na matriz de tipo (por exemplo, `{"type": ["string", "null"]}`).

Essas propriedades descritivas ajudam a orientar o modelo:

- **`title`**: uma breve descrição de uma propriedade.
- **`description`**: uma descrição mais longa e detalhada de uma propriedade.

### Propriedades específicas do tipo

**Para valores de `object`:**

- **`properties`**: um objeto em que cada chave é um nome de propriedade e cada valor é um esquema para essa propriedade.
- **`required`**: uma matriz de strings que lista quais propriedades são obrigatórias.
- **`additionalProperties`**: controla se as propriedades não listadas em `properties` são permitidas. Pode ser um booleano ou um esquema.

**Para valores de `string`:**

- **`enum`**: lista um conjunto específico de strings possíveis para tarefas de classificação.
- **`format`**: especifica uma sintaxe para a string, como `date-time`, `date` e `time`.

**Para valores `number` e `integer`:**

- **`enum`**: lista um conjunto específico de valores numéricos possíveis.
- **`minimum`**: o valor mínimo inclusivo.
- **`maximum`**: o valor máximo inclusivo.

**Para valores de `array`:**

- **`items`**: define o esquema de todos os itens na matriz.
- **`prefixItems`**: define uma lista de esquemas para os primeiros N itens, permitindo estruturas semelhantes a tuplas.
- **`minItems`**: o número mínimo de itens na matriz.
- **`maxItems`**: o número máximo de itens na matriz.

## Saídas estruturadas x chamada de função

| Recurso | Caso de uso principal |
| --- | --- |
| **Saídas estruturadas** | **Formatando a resposta final.** Use quando quiser que a *resposta* do modelo esteja em um formato específico. |
| **Chamada de função** | **Realizar ações durante a conversa** Use quando o modelo precisar *pedir que você* realize uma tarefa antes de dar uma resposta final. |

## Práticas recomendadas

- **Descrições claras**:use o campo `description` para orientar o modelo.
- **Tipagem forte**:use tipos específicos (`integer`, `string`, `enum`).
- **Engenharia de comando**:indique claramente o que você quer que o modelo faça.
- **Validação**:embora a saída seja um JSON sintaticamente correto, sempre valide os valores na sua aplicação.
- **Tratamento de erros**:implemente um tratamento de erros robusto para saídas compatíveis com o esquema, mas semanticamente incorretas.

## Limitações

- **Subconjunto de esquema**:nem todos os recursos do esquema JSON são compatíveis.
- **Complexidade do esquema**:esquemas muito grandes ou aninhados podem ser rejeitados.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-12 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-12 UTC."],[],[]]
