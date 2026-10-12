---
source_url: https://ai.google.dev/gemini-api/docs/structured-output?hl=ar
fetched_at: 2026-10-12T07:01:56.370817+00:00
title: "\u0627\u0644\u0646\u062a\u0627\u0626\u062c \u0627\u0644\u0645\u0646\u0638\u064e\u0651\u0645\u0629 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# النتائج المنظَّمة

يمكنك ضبط نماذج Gemini لإنشاء ردود تتوافق مع مخطط JSON مقدَّم. يضمن ذلك الحصول على نتائج متوقّعة وآمنة من حيث النوع، كما يسهّل استخراج البيانات المنظَّمة من النصوص غير المنظَّمة.

يُعدّ استخدام المُخرجات المنظَّمة مثاليًا للحالات التالية:

- **استخراج البيانات:** استخراج معلومات محدّدة، مثل الأسماء والتواريخ، من النص
- **التصنيف المنظَّم:** تصنيف النص ضِمن فئات محدَّدة مسبقًا
- **سير عمل الذكاء الاصطناعي الوكيل:** إنشاء مدخلات منظَّمة للأدوات أو واجهات برمجة التطبيقات

بالإضافة إلى إتاحة JSON Schema في REST API، تتيح حِزم تطوير البرامج (SDK) من Google للذكاء الاصطناعي التوليدي تحديد المخططات باستخدام [Pydantic](https://docs.pydantic.dev/latest/) (لغة Python) و[Zod](https://zod.dev/) (لغة JavaScript).

## أمثلة على الناتج المنظَّم

### أداة استخراج وصفات الطعام

يوضّح هذا المثال كيفية استخراج البيانات المنظَّمة من نص باستخدام أنواع أساسية من مخطط JSON، مثل `object` و`array` و`string` و`integer`.

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

### جافا

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

**مثال على الرد:**

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

### الإشراف على المحتوى

يعرض هذا المثال `anyOf` للمخططات الشرطية و`enum` للتصنيف، ما يسمح بتغيير بنية الإخراج استنادًا إلى المحتوى.

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

### جافا

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

**مثال على الرد:**

```
{
  "decision": {
    "reason": "The content is an unsolicited prize notification attempting to trick the user into clicking a suspicious link.",
    "spam_type": "scam"
  }
}
```

### البُنى التكرارية

يوضّح هذا المثال كيفية تحديد مخطط تكراري، مثل مخطط تنظيمي.

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

### جافا

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

**مثال على الرد:**

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

## نتائج البث

يمكنك بث النتائج المنظَّمة، ما يتيح لك بدء معالجة الرد أثناء إنشائه. الأجزاء التي يتم بثها هي سلاسل JSON جزئية صالحة يمكن ربطها لتكوين عنصر JSON النهائي.

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

### جافا

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

## مُخرجات منظَّمة باستخدام الأدوات

يتيح لك Gemini 3 الجمع بين "النتائج المنظَّمة" والأدوات المضمّنة، بما في ذلك
[تحديد المصدر من خلال "بحث Search"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) و
[سياق عناوين URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) و
[تطبيق الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) و
[البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar#structured-output) و
[استدعاء الدالة](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar).

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
    model="gemini-3.1-pro-preview",
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
  model: "gemini-3.1-pro-preview",
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

### جافا

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
        .model(Model.of("gemini-3.1-pro-preview"))
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
                Model: interactions.Model("gemini-3.1-pro-preview"),
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

## التوافق مع مخطّط JSON

لإنشاء عنصر JSON، اضبط `response_format` باستخدام عنصر (أو مصفوفة تحتوي على عنصر) من النوع `text` واضبط `mime_type` على `application/json`. يجب تقديم المخطط في الحقل `schema`.

يتوافق وضع الإخراج المنظَّم في Gemini مع مجموعة فرعية من مواصفات
[مخطط JSON](https://json-schema.org/).

في ما يلي القيم المسموح بها لـ `type`:

- ‫**`string`**: للنص
- **`number`**: للأرقام ذات الفاصلة العائمة
- ‫**`integer`**: للأعداد الصحيحة
- **`boolean`**: للقيم الصحيحة أو الخاطئة
- **`object`**: للبيانات المنظَّمة التي تتضمّن أزواجًا من المفاتيح والقيم
- ‫**`array`**: لقوائم العناصر
- **`null`**: للسماح بأن تكون قيمة السمة فارغة، أدرِج `"null"` في مصفوفة النوع (مثل `{"type": ["string", "null"]}`).

تساعد هذه الخصائص الوصفية في توجيه النموذج:

- ‫**`title`**: وصف مختصر للمكان المخصّص للاستئجار
- ‫**`description`**: وصف أطول وأكثر تفصيلاً للمكان المخصّص للاستئجار

### السمات الخاصة بأنواع محدّدة

**بالنسبة إلى قيم `object`:**

- ‫**`properties`**: عنصر يكون فيه كل مفتاح اسم خاصية وكل قيمة مخططًا لهذه الخاصية.
- استبدِل **`required`** بمصفوفة من السلاسل التي تسرد السمات الإلزامية.
- **`additionalProperties`**: تتحكّم هذه السمة في ما إذا كان يُسمح بالسمات غير المدرَجة في `properties`. يمكن أن تكون قيمة منطقية أو مخططًا.

**بالنسبة إلى قيم `string`:**

- ‫**`enum`**: تعرض هذه السمة مجموعة محدّدة من السلاسل المحتملة لمهام التصنيف.
- **`format`**: تحدّد هذه السمة بنية السلسلة، مثل `date-time` أو `date` أو `time`.

**بالنسبة إلى القيمتَين `number` و`integer`:**

- **`enum`**: تعرض مجموعة معيّنة من القيم الرقمية المحتملة.
- ‫**`minimum`**: تمثّل الحد الأدنى للقيمة الشاملة.
- ‫**`maximum`**: تمثّل الحد الأقصى للقيمة الشاملة.

**بالنسبة إلى قيم `array`:**

- ‫**`items`**: تحدّد هذه السمة المخطط لجميع العناصر في المصفوفة.
- ‫**`prefixItems`**: تحدّد هذه السمة قائمة بمخططات أول N عناصر، ما يتيح إنشاء بنى شبيهة بالصفوف.
- ‫**`minItems`**: الحد الأدنى لعدد العناصر في المصفوفة
- ‫**`maxItems`**: الحد الأقصى لعدد العناصر في المصفوفة

## المخرجات المنظَّمة مقابل استدعاء الدوال

| الميزة | حالة الاستخدام الأساسية |
| --- | --- |
| **المُخرجات المنظَّمة** | **تنسيق الردّ النهائي** يجب استخدامها عندما تريد أن يكون *ردّ* النموذج بتنسيق معيّن. |
| **استدعاء الدوال** | **اتّخاذ إجراء أثناء المحادثة** يُستخدَم عندما يحتاج النموذج إلى *أن يطلب منك* تنفيذ مهمة قبل تقديم إجابة نهائية. |

## أفضل الممارسات

- **أوصاف واضحة:** استخدِم الحقل `description` لتوجيه النموذج.
- **الكتابة القوية:** استخدِم أنواعًا محدّدة (`integer` و`string` و`enum`).
- **هندسة الطلبات:** حدِّد بوضوح ما تريد أن يفعله النموذج.
- **التحقّق من الصحة:** على الرغم من أنّ الناتج هو JSON صحيح من الناحية النحوية، يجب دائمًا التحقّق من صحة القيم في تطبيقك.
- **معالجة الأخطاء:** اتّخِذ إجراءات فعالة لمعالجة الأخطاء في النتائج التي تتوافق مع المخطط ولكنّها غير صحيحة دلاليًا.

## القيود

- **مجموعة فرعية من المخطط:** لا تتوفّر جميع ميزات JSON Schema.
- **تعقيد المخطط:** قد يتم رفض المخططات الكبيرة جدًا أو المتداخلة بشكل كبير.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-24 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-24 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
