---
source_url: https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-TW
fetched_at: 2026-10-26T05:44:58.280484+00:00
title: "\u7d50\u69cb\u5316\u8f38\u51fa\u5167\u5bb9 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 結構化輸出內容

您可以設定 Gemini 模型，依據提供的 JSON 結構定義生成回覆。這可確保結果可預測且類型安全，並簡化從非結構化文字中擷取結構化資料的程序。

結構化輸出內容最適合用於：

- **資料擷取：**從文字中擷取特定資訊，例如姓名和日期。
- **結構化分類：**將文字分類至預先定義的類別。
- **Agentic Workflows：**為工具或 API 生成結構化輸入內容。

除了在 REST API 中支援 JSON 結構定義外，Google GenAI SDK 也允許使用 [Pydantic](https://docs.pydantic.dev/latest/) (Python) 和 [Zod](https://zod.dev/) (JavaScript) 定義結構定義。

## 結構化輸出內容範例

### 食譜擷取器

這個範例說明如何使用 `object`、`array`、`string` 和 `integer` 等基本 JSON 結構定義類型，從文字中擷取結構化資料。

### Python

```
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
    model="gemini-3.8-flash",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.output_text)
print(recipe)
```

### JavaScript

```
// Note: Ensure zod is installed (npm install zod)
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
  model: "gemini-3.8-flash",
  input: prompt,
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: recipeJsonSchema
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.output_text));
console.log(recipe);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> ingredientProps = new HashMap<>();
Map<String, Object> nameProp = new HashMap<>();
nameProp.put("type", "string");
nameProp.put("description", "Name of the ingredient.");
ingredientProps.put("name", nameProp);

Map<String, Object> quantityProp = new HashMap<>();
quantityProp.put("type", "string");
quantityProp.put("description", "Quantity of the ingredient, including units.");
ingredientProps.put("quantity", quantityProp);

Map<String, Object> ingredientItemSchema = new HashMap<>();
ingredientItemSchema.put("type", "object");
ingredientItemSchema.put("properties", ingredientProps);
ingredientItemSchema.put("required", Arrays.asList("name", "quantity"));

Map<String, Object> properties = new HashMap<>();

Map<String, Object> recipeNameProp = new HashMap<>();
recipeNameProp.put("type", "string");
recipeNameProp.put("description", "The name of the recipe.");
properties.put("recipe_name", recipeNameProp);

Map<String, Object> prepTimeProp = new HashMap<>();
prepTimeProp.put("type", "integer");
prepTimeProp.put("description", "Optional time in minutes to prepare the recipe.");
properties.put("prep_time_minutes", prepTimeProp);

Map<String, Object> ingredientsProp = new HashMap<>();
ingredientsProp.put("type", "array");
ingredientsProp.put("items", ingredientItemSchema);
properties.put("ingredients", ingredientsProp);

Map<String, Object> instructionsProp = new HashMap<>();
instructionsProp.put("type", "array");
Map<String, Object> stringItem = new HashMap<>();
stringItem.put("type", "string");
instructionsProp.put("items", stringItem);
properties.put("instructions", instructionsProp);

Map<String, Object> recipeJsonSchema = new HashMap<>();
recipeJsonSchema.put("type", "object");
recipeJsonSchema.put("properties", properties);
recipeJsonSchema.put("required", Arrays.asList("recipe_name", "ingredients", "instructions"));

String prompt =
    "Please extract the recipe from the following text.\n"
        + "The user wants to make delicious chocolate chip cookies.\n"
        + "They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,\n"
        + "1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,\n"
        + "3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.\n"
        + "For the best part, they'll need 2 cups of semisweet chocolate chips.\n"
        + "First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,\n"
        + "baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar\n"
        + "until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry\n"
        + "ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons\n"
        + "onto ungreased baking sheets and bake for 9 to 11 minutes.";

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(recipeJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .responseFormat(format)
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

    recipeJsonSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "recipe_name": map[string]any{
                "type":        "string",
                "description": "The name of the recipe.",
            },
            "prep_time_minutes": map[string]any{
                "type":        "integer",
                "description": "Optional time in minutes to prepare the recipe.",
            },
            "ingredients": map[string]any{
                "type": "array",
                "items": map[string]any{
                    "type": "object",
                    "properties": map[string]any{
                        "name": map[string]any{
                            "type":        "string",
                            "description": "Name of the ingredient.",
                        },
                        "quantity": map[string]any{
                            "type":        "string",
                            "description": "Quantity of the ingredient, including units.",
                        },
                    },
                    "required": []string{"name", "quantity"},
                },
            },
            "instructions": map[string]any{
                "type": "array",
                "items": map[string]any{
                    "type": "string",
                },
            },
        },
        "required": []string{"recipe_name", "ingredients", "instructions"},
    }

    prompt := `Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.`

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   recipeJsonSchema,
        }),
    )

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model:          interactions.Model("gemini-3.8-flash"),
                Input:          interactions.NewInteractionsInput(prompt),
                ResponseFormat: &format,
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
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

**回應範例：**

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

### 內容審核

這個範例展示了用於條件式結構定義的 `anyOf`，以及用於分類的 `enum`，可讓輸出結構依據內容而有所不同。

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import Union, Literal

class SpamDetails(BaseModel):
    reason: str = Field(description="The reason why the content is considered spam.")
    spam_type: Literal["phishing", "scam", "unsolicited promotion", "other"] = Field(description="The type of spam.")

class NotSpamDetails(BaseModel):
    summary: str = Field(description="A brief summary of the content.")
    is_safe: bool = Field(description="Whether the content is safe for all audiences.")

class ModerationResult(BaseModel):
    decision: Union[SpamDetails, NotSpamDetails]

client = genai.Client()

prompt = """
Please moderate the following content and provide a decision.
Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
"""

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": ModerationResult.model_json_schema()
    },
)

result = ModerationResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
// Note: Ensure zod is installed (npm install zod)
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const moderationResultJsonSchema = {
  type: "object",
  properties: {
    decision: {
      anyOf: [
        {
          type: "object",
          title: "SpamDetails",
          description: "Details for content classified as spam.",
          properties: {
            reason: { type: "string", description: "The reason why the content is considered spam." },
            spam_type: { type: "string", enum: ["phishing", "scam", "unsolicited promotion", "other"], description: "The type of spam." }
          },
          required: ["reason", "spam_type"]
        },
        {
          type: "object",
          title: "NotSpamDetails",
          description: "Details for content classified as not spam.",
          properties: {
            summary: { type: "string", description: "A brief summary of the content." },
            is_safe: { type: "boolean", description: "Whether the content is safe for all audiences." }
          },
          required: ["summary", "is_safe"]
        }
      ]
    }
  },
  required: ["decision"]
};

const moderationResultSchema = z.fromJSONSchema(moderationResultJsonSchema);

const client = new GoogleGenAI({});

const prompt = `
Please moderate the following content and provide a decision.
Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
`;

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: prompt,
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: moderationResultJsonSchema
  },
});

const result = moderationResultSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> spamProps = new HashMap<>();
Map<String, Object> reasonProp = new HashMap<>();
reasonProp.put("type", "string");
reasonProp.put("description", "The reason why the content is considered spam.");
spamProps.put("reason", reasonProp);

Map<String, Object> spamTypeProp = new HashMap<>();
spamTypeProp.put("type", "string");
spamTypeProp.put("enum", Arrays.asList("phishing", "scam", "unsolicited promotion", "other"));
spamTypeProp.put("description", "The type of spam.");
spamProps.put("spam_type", spamTypeProp);

Map<String, Object> spamDetailsSchema = new HashMap<>();
spamDetailsSchema.put("type", "object");
spamDetailsSchema.put("title", "SpamDetails");
spamDetailsSchema.put("properties", spamProps);
spamDetailsSchema.put("required", Arrays.asList("reason", "spam_type"));

Map<String, Object> notSpamProps = new HashMap<>();
Map<String, Object> summaryProp = new HashMap<>();
summaryProp.put("type", "string");
summaryProp.put("description", "A brief summary of the content.");
notSpamProps.put("summary", summaryProp);

Map<String, Object> isSafeProp = new HashMap<>();
isSafeProp.put("type", "boolean");
isSafeProp.put("description", "Whether the content is safe for all audiences.");
notSpamProps.put("is_safe", isSafeProp);

Map<String, Object> notSpamDetailsSchema = new HashMap<>();
notSpamDetailsSchema.put("type", "object");
notSpamDetailsSchema.put("title", "NotSpamDetails");
notSpamDetailsSchema.put("properties", notSpamProps);
notSpamDetailsSchema.put("required", Arrays.asList("summary", "is_safe"));

Map<String, Object> decisionProp = new HashMap<>();
decisionProp.put("anyOf", Arrays.asList(spamDetailsSchema, notSpamDetailsSchema));

Map<String, Object> properties = new HashMap<>();
properties.put("decision", decisionProp);

Map<String, Object> moderationResultJsonSchema = new HashMap<>();
moderationResultJsonSchema.put("type", "object");
moderationResultJsonSchema.put("properties", properties);
moderationResultJsonSchema.put("required", Arrays.asList("decision"));

String prompt =
    "Please moderate the following content and provide a decision.\n"
        + "Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'";

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(moderationResultJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .responseFormat(format)
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

    spamDetailsSchema := map[string]any{
        "type":  "object",
        "title": "SpamDetails",
        "properties": map[string]any{
            "reason": map[string]any{
                "type":        "string",
                "description": "The reason why the content is considered spam.",
            },
            "spam_type": map[string]any{
                "type":        "string",
                "enum":        []string{"phishing", "scam", "unsolicited promotion", "other"},
                "description": "The type of spam.",
            },
        },
        "required": []string{"reason", "spam_type"},
    }

    notSpamDetailsSchema := map[string]any{
        "type":  "object",
        "title": "NotSpamDetails",
        "properties": map[string]any{
            "summary": map[string]any{
                "type":        "string",
                "description": "A brief summary of the content.",
            },
            "is_safe": map[string]any{
                "type":        "boolean",
                "description": "Whether the content is safe for all audiences.",
            },
        },
        "required": []string{"summary", "is_safe"},
    }

    moderationResultJsonSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "decision": map[string]any{
                "anyOf": []any{spamDetailsSchema, notSpamDetailsSchema},
            },
        },
        "required": []string{"decision"},
    }

    prompt := "Please moderate the following content and provide a decision.\n" +
        "Content: 'Congratulations! You've won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'"

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   moderationResultJsonSchema,
        }),
    )

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model:          interactions.Model("gemini-3.8-flash"),
                Input:          interactions.NewInteractionsInput(prompt),
                ResponseFormat: &format,
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": "Please moderate the following content and provide a decision.\nContent: '\''Congratulations! You have won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'\''",
      "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
          "type": "object",
          "properties": {
            "decision": {
              "anyOf": [
                {
                  "type": "object",
                  "title": "SpamDetails",
                  "description": "Details for content classified as spam.",
                  "properties": {
                    "reason": { "type": "string", "description": "The reason why the content is considered spam." },
                    "spam_type": { "type": "string", "enum": ["phishing", "scam", "unsolicited promotion", "other"], "description": "The type of spam." }
                  },
                  "required": ["reason", "spam_type"]
                },
                {
                  "type": "object",
                  "title": "NotSpamDetails",
                  "description": "Details for content classified as not spam.",
                  "properties": {
                    "summary": { "type": "string", "description": "A brief summary of the content." },
                    "is_safe": { "type": "boolean", "description": "Whether the content is safe for all audiences." }
                  },
                  "required": ["summary", "is_safe"]
                }
              ]
            }
          },
          "required": ["decision"]
        }
      }
      }
    }'
```

**回應範例：**

```
{
  "decision": {
    "reason": "The content is an unsolicited prize notification attempting to trick the user into clicking a suspicious link.",
    "spam_type": "scam"
  }
}
```

### 遞迴結構

這個範例說明如何定義遞迴結構定義，例如組織圖。

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class Employee(BaseModel):
    """Represents an employee in an organization."""
    name: str
    employee_id: int
    reports: List["Employee"] = Field(
        default_factory=list,
        description="A list of employees reporting to this employee."
    )

client = genai.Client()

prompt = """
Generate an organization chart for a small team.
The manager is Alice, who manages Bob and Charlie. Bob manages David.
"""

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Employee.model_json_schema()
    },
)

employee = Employee.model_validate_json(interaction.output_text)
print(employee)
```

### JavaScript

```
// Note: Ensure zod is installed (npm install zod)
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const employeeJsonSchema = {
  type: "object",
  properties: {
    name: { type: "string" },
    employee_id: { type: "integer" },
    reports: {
      type: "array",
      description: "A list of employees reporting to this employee.",
      items: {
        "$ref": "#"
      }
    }
  },
  required: ["name", "employee_id", "reports"]
};

const employeeSchema = z.fromJSONSchema(employeeJsonSchema);

const client = new GoogleGenAI({});

const prompt = `
Generate an organization chart for a small team.
The manager is Alice, who manages Bob and Charlie. Bob manages David.
`;

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: prompt,
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: employeeJsonSchema
  },
});

const employee = employeeSchema.parse(JSON.parse(interaction.output_text));
console.log(employee);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();

Map<String, Object> nameProp = new HashMap<>();
nameProp.put("type", "string");
properties.put("name", nameProp);

Map<String, Object> idProp = new HashMap<>();
idProp.put("type", "integer");
properties.put("employee_id", idProp);

Map<String, Object> reportsProp = new HashMap<>();
reportsProp.put("type", "array");
reportsProp.put("description", "A list of employees reporting to this employee.");
reportsProp.put("items", Collections.singletonMap("$ref", "#"));
properties.put("reports", reportsProp);

Map<String, Object> employeeJsonSchema = new HashMap<>();
employeeJsonSchema.put("type", "object");
employeeJsonSchema.put("properties", properties);
employeeJsonSchema.put("required", Arrays.asList("name", "employee_id", "reports"));

String prompt =
    "Generate an organization chart for a small team.\n"
        + "The manager is Alice, who manages Bob and Charlie. Bob manages David.";

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(employeeJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .responseFormat(format)
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

    employeeJsonSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "name": map[string]any{
                "type": "string",
            },
            "employee_id": map[string]any{
                "type": "integer",
            },
            "reports": map[string]any{
                "type":        "array",
                "description": "A list of employees reporting to this employee.",
                "items": map[string]any{
                    "$ref": "#",
                },
            },
        },
        "required": []string{"name", "employee_id", "reports"},
    }

    prompt := "Generate an organization chart for a small team.\n" +
        "The manager is Alice, who manages Bob and Charlie. Bob manages David."

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   employeeJsonSchema,
        }),
    )

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model:          interactions.Model("gemini-3.8-flash"),
                Input:          interactions.NewInteractionsInput(prompt),
                ResponseFormat: &format,
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": "Generate an organization chart for a small team.\nThe manager is Alice, who manages Bob and Charlie. Bob manages David.",
      "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "employee_id": { "type": "integer" },
            "reports": {
              "type": "array",
              "description": "A list of employees reporting to this employee.",
              "items": {
                "$ref": "#"
              }
            }
          },
          "required": ["name", "employee_id", "reports"]
        }
      }
      }
    }'
```

**回應範例：**

```
{
  "name": "Alice",
  "employee_id": 101,
  "reports": [
    {
      "name": "Bob",
      "employee_id": 102,
      "reports": [
        {
          "name": "David",
          "employee_id": 104,
          "reports": []
        }
      ]
    },
    {
      "name": "Charlie",
      "employee_id": 103,
      "reports": []
    }
  ]
}
```

## 串流結果

您可以串流輸出結構化內容，在生成回覆時就開始處理。串流區塊是有效的 JSON 字串片段，可串連成最終的 JSON 物件。

### Python

```
from google import genai
from pydantic import BaseModel
from typing import Literal

class Feedback(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    summary: str

client = genai.Client()
prompt = "The new UI is incredibly intuitive. Add a very long summary to test streaming!"

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Feedback.model_json_schema()
    },
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text" and getattr(event.delta, "text", None):
            print(event.delta.text, end="", flush=True)
```

### JavaScript

```
// Note: Ensure zod is installed (npm install zod)
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
  model: "gemini-3.8-flash",
  input: "The new UI is incredibly intuitive. Add a very long summary!",
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: feedbackJsonSchema
  },
  stream: true,
});

for await (const event of stream) {
  if (event.event_type === "step.delta") {
    if (event.delta.type === "text") {
      process.stdout.write(event.delta.text);
    }
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.StepDeltaData;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.utils.EventStream;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();

Map<String, Object> sentimentProp = new HashMap<>();
sentimentProp.put("type", "string");
sentimentProp.put("enum", Arrays.asList("positive", "neutral", "negative"));
properties.put("sentiment", sentimentProp);

Map<String, Object> summaryProp = new HashMap<>();
summaryProp.put("type", "string");
properties.put("summary", summaryProp);

Map<String, Object> feedbackJsonSchema = new HashMap<>();
feedbackJsonSchema.put("type", "object");
feedbackJsonSchema.put("properties", properties);
feedbackJsonSchema.put("required", Arrays.asList("sentiment", "summary"));

String prompt = "The new UI is incredibly intuitive. Add a very long summary to test streaming!";

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(feedbackJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .responseFormat(format)
        .stream(true)
        .build();

CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));

try (EventStream<InteractionSSEStreamEvent> events = response.events()) {
  for (InteractionSSEStreamEvent streamEvent : events) {
    InteractionSSEEvent event = streamEvent.data().orElse(null);
    if (event instanceof StepDelta) {
      StepDeltaData data = ((StepDelta) event).delta().orElse(null);
      if (data instanceof TextDelta) {
        ((TextDelta) data).text().ifPresent(System.out::print);
      }
    }
  }
}
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

    feedbackJsonSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "sentiment": map[string]any{
                "type": "string",
                "enum": []string{"positive", "neutral", "negative"},
            },
            "summary": map[string]any{
                "type": "string",
            },
        },
        "required": []string{"sentiment", "summary"},
    }

    prompt := "The new UI is incredibly intuitive. Add a very long summary to test streaming!"

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   feedbackJsonSchema,
        }),
    )

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model:          interactions.Model("gemini-3.8-flash"),
                Input:          interactions.NewInteractionsInput(prompt),
                ResponseFormat: &format,
                Stream:         genai.Ptr(true),
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }
    defer resp.InteractionSSEStreamEvent.Close()

    for resp.InteractionSSEStreamEvent.Next() {
        event := resp.InteractionSSEStreamEvent.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        }
    }
}
```

### REST

```
curl -N -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": "The new UI is incredibly intuitive. Add a very long summary!",
      "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
          "type": "object",
          "properties": {
            "sentiment": { "type": "string", "enum": ["positive", "neutral", "negative"] },
            "summary": { "type": "string" }
          },
          "required": ["sentiment", "summary"]
        }
      },
      "stream": true
    }'
```

## 使用工具產生結構化輸出內容

Gemini 3 可讓您將結構化輸出內容與內建工具結合，包括[以 Google 搜尋強化事實基礎](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)、[網址背景資訊](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)、[執行程式碼](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)、[檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw#structured-output)和[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)。

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Search for all details for the latest Euro.",
    tools=[{"type": "google_search"}, {"type": "url_context"}],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
// Note: Ensure zod is installed (npm install zod)
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
  model: "gemini-4-argon",
  input: "Search for all details for the latest Euro.",
  tools: [{type: "google_search"}, {type: "url_context"}],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: matchJsonSchema
  },
});

const match = matchSchema.parse(JSON.parse(interaction.output_text));
console.log(match);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.interactions.URLContext;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();

Map<String, Object> winnerProp = new HashMap<>();
winnerProp.put("type", "string");
winnerProp.put("description", "The name of the winner.");
properties.put("winner", winnerProp);

Map<String, Object> scoreProp = new HashMap<>();
scoreProp.put("type", "string");
scoreProp.put("description", "The final match score.");
properties.put("final_match_score", scoreProp);

Map<String, Object> scorersProp = new HashMap<>();
scorersProp.put("type", "array");
scorersProp.put("description", "The name of the scorer.");
scorersProp.put("items", Collections.singletonMap("type", "string"));
properties.put("scorers", scorersProp);

Map<String, Object> matchJsonSchema = new HashMap<>();
matchJsonSchema.put("type", "object");
matchJsonSchema.put("properties", properties);
matchJsonSchema.put("required", Arrays.asList("winner", "final_match_score", "scorers"));

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(matchJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-4-argon"))
        .input(InteractionsInput.of("Search for all details for the latest Euro."))
        .tools(Arrays.asList(GoogleSearch.builder().build(), URLContext.builder().build()))
        .responseFormat(format)
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

    matchJsonSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "winner": map[string]any{
                "type":        "string",
                "description": "The name of the winner.",
            },
            "final_match_score": map[string]any{
                "type":        "string",
                "description": "The final match score.",
            },
            "scorers": map[string]any{
                "type":        "array",
                "description": "The name of the scorer.",
                "items": map[string]any{
                    "type": "string",
                },
            },
        },
        "required": []string{"winner", "final_match_score", "scorers"},
    }

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   matchJsonSchema,
        }),
    )

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-4-argon"),
                Input: interactions.NewInteractionsInput("Search for all details for the latest Euro."),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleSearch{}),
                    interactions.NewTool(interactions.URLContext{}),
                },
                ResponseFormat: &format,
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-4-argon",
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

## 支援 JSON 結構定義

如要生成 JSON 物件，請使用 `text` 類型的物件 (或包含物件的陣列) 設定 `response_format`，並將 `mime_type` 設為 `application/json`。請在 `schema` 欄位中提供結構定義。

Gemini 的結構化輸出模式支援 [JSON 結構定義](https://json-schema.org/)規格的部分內容。

支援下列 `type` 值：

- **`string`**：文字。
- **`number`**：用於浮點數。
- **`integer`**：用於整數。
- **`boolean`**：用於 true 或 false 值。
- **`object`**：適用於含有鍵/值組合的結構化資料。
- **`array`**：用於項目清單。
- **`null`**：如要允許屬性為空值，請在類型陣列中加入 `"null"` (例如 `{"type": ["string", "null"]}`)。

這些描述性屬性有助於引導模型：

- **`title`**：屬性的簡短說明。
- **`description`**：更長、更詳細的屬性說明。

### 類型專屬屬性

**`object` 值：**

- **`properties`**：物件，其中每個鍵都是屬性名稱，每個值都是該屬性的結構定義。
- **`required`**：字串陣列，列出必要屬性。
- **`additionalProperties`**：控制是否允許 `properties` 中未列出的屬性。可以是布林值或結構定義。
- **不支援的計數限制**：在限制解碼期間，系統不會強制執行 `minProperties` 和 `maxProperties`，伺服器會忽略這些限制。視需要驗證應用程式程式碼中的屬性數量。

**`string` 值：**

- **`enum`**：列出分類任務可能出現的一組特定字串。
- **`format`**：指定字串的語法，例如 `date-time`、`date`、`time`。
- **不支援的長度限制**：`minLength` 和 `maxLength` 在限制解碼期間不會強制執行，且會由伺服器忽略。如有需要，請在應用程式程式碼中驗證字串長度。

**`number` 和 `integer` 值：**

- **`enum`**：列出一組特定的可能數值。
- **`minimum`**：最小值 (含)。
- **`maximum`**：最大值 (含)。

**`array` 值：**

- **`items`**：定義陣列中所有項目的結構定義。
- **`prefixItems`**：定義前 N 個項目的結構定義清單，允許類似元組的結構。
- **`minItems`**：陣列中的項目數量下限。
- **`maxItems`**：陣列中的項目數量上限。
- **不支援的陣列限制**：`uniqueItems`、`contains`、`minContains` 和 `maxContains` 在限制解碼期間不會強制執行，且會由伺服器忽略。如有需要，請在應用程式程式碼中簡化項目或檢查陣列內容。

## 結構化輸出與函式呼叫

| 功能 | 主要用途 |
| --- | --- |
| **結構化輸出** | **設定最終回覆的格式。**當您希望模型以特定格式*回答*時，可以使用這個方法。 |
| **呼叫函式** | **在對話期間採取行動。**如果模型需要*請你*執行工作，才能提供最終答案，請使用這個選項。 |

## 最佳做法

- **清楚說明：**使用 `description` 欄位引導模型。
- **強型別：**使用特定類型 (`integer`、`string`、`enum`)。
- **提示工程：**清楚說明您希望模型執行的工作。
- **驗證：**雖然輸出內容是語法正確的 JSON，但請務必在應用程式中驗證值。
- **錯誤處理：**針對符合結構定義但語意不正確的輸出內容，導入完善的錯誤處理機制。

## 限制

- **結構定義子集：**不支援部分 JSON 結構定義功能。
- **結構定義複雜度：**如果結構定義過大或巢狀結構過深，可能會遭到拒絕，並顯示 `400 INVALID_ARGUMENT` 錯誤，指出結構定義產生的限制狀態過多，或分支過多，無法提供服務。常見原因包括 `maxItems` 限制過大 (尤其是巢狀陣列)、屬性或列舉名稱過長、列舉值過多、選用屬性過長、`anyOf` 有許多替代方案，以及數值 `minimum`/`maximum` 邊界。如要修正這個問題，請降低或移除巢狀陣列限制、縮短名稱，或在選用屬性之間穿插必要屬性。
- **未強制執行的限制：** `minLength`、`maxLength`、`minProperties`、`maxProperties`、`uniqueItems`、`contains`、`minContains` 和 `maxContains` (及其蛇形命名法變體) 不會由受限解碼文法引擎強制執行。如果結構定義中含有這些關鍵字 (例如由 Pydantic 的 `Field(min_length=...)` 或 Zod 的 `.min()` 自動發出)，API 會在要求正規化期間自動移除並忽略這些關鍵字，而不會傳回錯誤。強制執行 `minItems` 和 `maxItems`。如要強制執行其他限制，請在用戶端驗證剖析後的輸出內容 (例如使用 Pydantic `model_validate_json()` 或 Zod `.parse()`)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-21 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-21 (世界標準時間)。"],[],[]]
