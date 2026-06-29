---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=hi
fetched_at: 2026-06-29T05:36:04.081313+00:00
title: "\u0938\u094d\u091f\u094d\u0930\u0915\u094d\u091a\u0930\u094d\u0921 \u0906\u0909\u091f\u092a\u0941\u091f \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# स्ट्रक्चर्ड आउटपुट

Gemini मॉडल को कॉन्फ़िगर करके, दिए गए JSON स्कीमा के मुताबिक जवाब जनरेट किए जा सकते हैं. इससे टाइप-सेफ़ नतीजे मिलते हैं और बिना स्ट्रक्चर वाले टेक्स्ट से स्ट्रक्चर्ड डेटा को आसानी से निकाला जा सकता है.

स्ट्रक्चर्ड आउटपुट का इस्तेमाल इन कामों के लिए सबसे सही है:

- **डेटा निकालना:** टेक्स्ट से नाम और तारीख जैसी जानकारी निकालना.
- **स्ट्रक्चर्ड क्लासिफ़िकेशन:** टेक्स्ट को पहले से तय की गई कैटगरी में बांटना.
- **एजेंटिक वर्कफ़्लो:** टूल या एपीआई के लिए स्ट्रक्चर्ड इनपुट जनरेट करना.

REST API में JSON स्कीमा के साथ-साथ, Google के GenAI SDK टूल भी काम करते हैं. इनकी मदद से, [Pydantic](https://docs.pydantic.dev/latest/) (Python) और [Zod](https://zod.dev/) (JavaScript) का इस्तेमाल करके स्कीमा को आसानी से तय किया जा सकता है.

## स्ट्रक्चर्ड आउटपुट के उदाहरण

### रेसिपी एक्सट्रैक्टर

इस उदाहरण में, `object`, `array`, `string`, और `integer` जैसे बुनियादी JSON स्कीमा टाइप का इस्तेमाल करके, टेक्स्ट से स्ट्रक्चर्ड डेटा निकालने का तरीका दिखाया गया है.

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

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Recipe.model_json_schema()}},
    },
)

recipe = Recipe.model_validate_json(response.text)
print(recipe)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ingredientSchema = z.object({
  name: z.string().describe("Name of the ingredient."),
  quantity: z.string().describe("Quantity of the ingredient, including units."),
});

const recipeSchema = z.object({
  recipe_name: z.string().describe("The name of the recipe."),
  prep_time_minutes: z.number().optional().describe("Optional time in minutes to prepare the recipe."),
  ingredients: z.array(ingredientSchema),
  instructions: z.array(z.string()),
});

const ai = new GoogleGenAI({});

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

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(recipeSchema) } },
  },
});

const recipe = recipeSchema.parse(JSON.parse(response.text));
console.log(recipe);
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `
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
  `
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
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
                    "type":  "array",
                    "items": map[string]any{"type": "string"},
                },
            },
            "required": []string{"recipe_name", "ingredients", "instructions"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          { "text": "Please extract the recipe from the following text.\nThe user wants to make delicious chocolate chip cookies.\nThey need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,\n1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,\n3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.\nFor the best part, they will need 2 cups of semisweet chocolate chips.\nFirst, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,\nbaking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar\nuntil light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry\ningredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons\nonto ungreased baking sheets and bake for 9 to 11 minutes." }
        ]
      }],
      "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
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
          }
        }
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
    }'
```

**जवाब का उदाहरण:**

```
{
  "recipe_name": "Delicious Chocolate Chip Cookies",
  "ingredients": [
    {
      "name": "all-purpose flour",
      "quantity": "2 and 1/4 cups"
    },
    {
      "name": "baking soda",
      "quantity": "1 teaspoon"
    },
    {
      "name": "salt",
      "quantity": "1 teaspoon"
    },
    {
      "name": "unsalted butter (softened)",
      "quantity": "1 cup"
    },
    {
      "name": "granulated sugar",
      "quantity": "3/4 cup"
    },
    {
      "name": "packed brown sugar",
      "quantity": "3/4 cup"
    },
    {
      "name": "vanilla extract",
      "quantity": "1 teaspoon"
    },
    {
      "name": "large eggs",
      "quantity": "2"
    },
    {
      "name": "semisweet chocolate chips",
      "quantity": "2 cups"
    }
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

### कॉन्टेंट मॉडरेट करना

इस उदाहरण में, शर्त के साथ स्कीमा लागू करने के लिए `anyOf` और क्लासिफ़िकेशन के लिए `enum` का इस्तेमाल किया गया है. इससे कॉन्टेंट के आधार पर आउटपुट स्ट्रक्चर में बदलाव किया जा सकता है.

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

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": ModerationResult.model_json_schema()}},
    },
)

result = ModerationResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const spamDetailsSchema = z.object({
  reason: z.string().describe("The reason why the content is considered spam."),
  spam_type: z.enum(["phishing", "scam", "unsolicited promotion", "other"]).describe("The type of spam."),
});

const notSpamDetailsSchema = z.object({
  summary: z.string().describe("A brief summary of the content."),
  is_safe: z.boolean().describe("Whether the content is safe for all audiences."),
});

const moderationResultSchema = z.object({
  decision: z.union([spamDetailsSchema, notSpamDetailsSchema]),
});

const ai = new GoogleGenAI({});

const prompt = `
Please moderate the following content and provide a decision.
Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
`;

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(moderationResultSchema) } },
  },
});

const result = moderationResultSchema.parse(JSON.parse(response.text));
console.log(result);
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `
  Please moderate the following content and provide a decision.
  Content: 'Congratulations! You''ve won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com'
  `
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "decision": map[string]any{
                    "anyOf": []map[string]any{
                        {
                            "type":        "object",
                            "title":       "SpamDetails",
                            "description": "Details for content classified as spam.",
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
                        },
                        {
                            "type":        "object",
                            "title":       "NotSpamDetails",
                            "description": "Details for content classified as not spam.",
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
                        },
                    },
                },
            },
            "required": []string{"decision"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          { "text": "Please moderate the following content and provide a decision.\nContent: ''Congratulations! You have won a free cruise to the Bahamas. Click here to claim your prize: www.definitely-not-a-scam.com''" }
        ]
      }],
      "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
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
          }
        }
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
     }'
 ```

**Example Response:**

```json
{
"decision": {
 "reason": "The content is an unsolicited prize notification attempting to trick the user into clicking a suspicious link.",
 "spam_type": "scam"
}
}
```

### रिकर्सिव स्ट्रक्चर

इस उदाहरण में, किसी रिकर्सिव स्कीमा को तय करने का तरीका बताया गया है. जैसे, संगठन का चार्ट.

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

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Employee.model_json_schema()}},
    },
)

employee = Employee.model_validate_json(response.text)
print(employee)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const employeeSchema = z.object({
  name: z.string(),
  employee_id: z.number().int(),
  reports: z.lazy(() => z.array(employeeSchema)).describe("A list of employees reporting to this employee."),
});

const ai = new GoogleGenAI({});

const prompt = `
Generate an organization chart for a small team.
The manager is Alice, who manages Bob and Charlie. Bob manages David.
`;

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(employeeSchema) } },
  },
});

const employee = employeeSchema.parse(JSON.parse(response.text));
console.log(employee);
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `
  Generate an organization chart for a small team.
  The manager is Alice, who manages Bob and Charlie. Bob manages David.
  `
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "name":        map[string]any{"type": "string"},
                "employee_id": map[string]any{"type": "integer"},
                "reports": map[string]any{
                    "type":        "array",
                    "description": "A list of employees reporting to this employee.",
                    "items": map[string]any{
                        "$ref": "#",
                    },
                },
            },
            "required": []string{"name", "employee_id", "reports"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          { "text": "Generate an organization chart for a small team.\nThe manager is Alice, who manages Bob and Charlie. Bob manages David." }
        ]
      }],
      "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
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
        }
      }
          },
          "required": ["name", "employee_id", "reports"]
        }
      }
    }'
```

**जवाब का उदाहरण:**

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

## स्ट्रीमिंग

स्ट्रक्चर्ड आउटपुट को स्ट्रीम किया जा सकता है. इससे, पूरे आउटपुट के जनरेट होने का इंतज़ार किए बिना, जवाब को प्रोसेस करना शुरू किया जा सकता है. इससे आपके ऐप्लिकेशन की परफ़ॉर्मेंस बेहतर हो सकती है.

स्ट्रीम किए गए चंक, मान्य आंशिक JSON स्ट्रिंग होंगे. इन्हें जोड़कर, फ़ाइनल और पूरा JSON ऑब्जेक्ट बनाया जा सकता है.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import Literal

class Feedback(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    summary: str

client = genai.Client()
prompt = "The new UI is incredibly intuitive and visually appealing. Great job. Add a very long summary to test streaming!"

response_stream = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Feedback.model_json_schema()}},
    },
)

for chunk in response_stream:
    print(chunk.candidates[0].content.parts[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});
const prompt = "The new UI is incredibly intuitive and visually appealing. Great job! Add a very long summary to test streaming!";

const feedbackSchema = z.object({
  sentiment: z.enum(["positive", "neutral", "negative"]),
  summary: z.string(),
});

const stream = await ai.models.generateContentStream({
  model: "gemini-3.5-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(feedbackSchema) } },
  },
});

for await (const chunk of stream) {
  console.log(chunk.candidates[0].content.parts[0].text)
}
```

## टूल की मदद से स्ट्रक्चर्ड आउटपुट जनरेट करना

Gemini 3 की मदद से, स्ट्रक्चर्ड आउटपुट को पहले से मौजूद टूल के साथ जोड़ा जा सकता है. इनमें ये टूल शामिल हैं:
[Google Search से मिली जानकारी का इस्तेमाल करना](https://ai.google.dev/gemini-api/docs/google-search?hl=hi),
[यूआरएल का कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi),
[कोड एक्ज़ीक्यूट करना](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi),
[फ़ाइल खोजना](https://ai.google.dev/gemini-api/docs/file-search?hl=hi#structured-output), और
[फ़ंक्शन कॉल करना](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi).

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

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
          }
        }
      },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

## JSON स्कीमा के साथ काम करता है

JSON ऑब्जेक्ट जनरेट करने के लिए, जनरेशन कॉन्फ़िगरेशन में `response_format` को सेट करें. स्कीमा, मान्य [JSON स्कीमा](https://json-schema.org/) होना चाहिए. इसमें, आउटपुट के फ़ॉर्मैट के बारे में बताया गया हो.

इसके बाद, मॉडल एक ऐसा जवाब जनरेट करेगा जो सिंटैक्टिक तौर पर मान्य JSON स्ट्रिंग हो और दिए गए स्कीमा से मेल खाती हो. स्ट्रक्चर्ड आउटपुट का इस्तेमाल करते समय, मॉडल आउटपुट को उसी क्रम में जनरेट करेगा जिस क्रम में स्कीमा में कुंजियां मौजूद हैं.

Gemini के स्ट्रक्चर्ड आउटपुट मोड में, [JSON स्कीमा](https://json-schema.org) के कुछ स्पेसिफ़िकेशन काम करते हैं.

`type` एट्रिब्यूट के लिए, इन वैल्यू का इस्तेमाल किया जा सकता है:

- **`string`**: टेक्स्ट के लिए.
- **`number`**: फ़्लोटिंग-पॉइंट नंबर के लिए.
- **`integer`**: पूर्णांकों के लिए.
- **`boolean`**: सही/गलत वैल्यू के लिए.
- **`object`**: यह स्ट्रक्चर्ड डेटा के लिए होता है, जिसमें कुंजी-वैल्यू पेयर होते हैं.
- **`array`**: आइटम की सूचियों के लिए.
- **`null`**: किसी प्रॉपर्टी को शून्य के तौर पर सेट करने के लिए, टाइप कलेक्शन में `"null"` शामिल करें. उदाहरण के लिए, `{"type": ["string", "null"]}`.

ब्यौरे वाली इन प्रॉपर्टी से, मॉडल को सही जानकारी देने में मदद मिलती है:

- **`title`**: किसी प्रॉपर्टी के बारे में कम शब्दों में जानकारी.
- **`description`**: किसी प्रॉपर्टी के बारे में ज़्यादा जानकारी.

### टाइप के हिसाब से प्रॉपर्टी

**`object` वैल्यू के लिए:**

- **`properties`**: यह एक ऐसा ऑब्जेक्ट है जिसमें हर कुंजी, प्रॉपर्टी का नाम होती है और हर वैल्यू, उस प्रॉपर्टी का स्कीमा होती है.
- **`required`**: यह स्ट्रिंग का एक कलेक्शन है. इसमें उन प्रॉपर्टी की सूची दी गई है जिन्हें सेट करना ज़रूरी है.
- **`additionalProperties`**: इससे यह तय होता है कि `properties` में शामिल नहीं की गई प्रॉपर्टी को अनुमति दी जाए या नहीं. यह बूलियन या स्कीमा हो सकता है.

**`string` वैल्यू के लिए:**

- **`enum`**: इसमें क्लासिफ़िकेशन के कामों के लिए, संभावित स्ट्रिंग का एक खास सेट दिया गया है.
- **`format`**: यह स्ट्रिंग के लिए सिंटैक्स तय करता है. जैसे, `date-time`, `date`, `time`.

**`number` और `integer` वैल्यू के लिए:**

- **`enum`**: यह फ़ंक्शन, संख्या वाली संभावित वैल्यू का कोई खास सेट दिखाता है.
- **`minimum`**: कम से कम वैल्यू.
- **`maximum`**: ज़्यादा से ज़्यादा वैल्यू.

**`array` वैल्यू के लिए:**

- **`items`**: यह कलेक्शन में मौजूद सभी आइटम के लिए स्कीमा तय करता है.
- **`prefixItems`**: यह पहले N आइटम के लिए स्कीमा की सूची तय करता है. इससे टपल जैसे स्ट्रक्चर बनाए जा सकते हैं.
- **`minItems`**: कलेक्शन में मौजूद आइटम की कम से कम संख्या.
- **`maxItems`**: कलेक्शन में मौजूद आइटम की ज़्यादा से ज़्यादा संख्या.

## मॉडल से जुड़ी सहायता

ये मॉडल, स्ट्रक्चर्ड आउटपुट जनरेट करने की सुविधा के साथ काम करते हैं:

| मॉडल | स्ट्रक्चर्ड आउटपुट |
| --- | --- |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Pro की झलक | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite की झलक | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

*\* ध्यान दें कि Gemini 2.0 को JSON इनपुट में, `propertyOrdering` की साफ़ तौर पर दी गई सूची की ज़रूरत होती है, ताकि पसंदीदा स्ट्रक्चर तय किया जा सके. आपको इस [कुकबुक](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynb) में इसका उदाहरण मिल सकता है.*

## स्ट्रक्चर्ड आउटपुट बनाम फ़ंक्शन कॉलिंग

स्ट्रक्चर्ड आउटपुट और फ़ंक्शन कॉलिंग, दोनों में JSON स्कीमा का इस्तेमाल किया जाता है. हालांकि, इनके मकसद अलग-अलग होते हैं:

| सुविधा | इस्तेमाल का मुख्य उदाहरण |
| --- | --- |
| **स्ट्रक्चर्ड आउटपुट** | **उपयोगकर्ता को जवाब देने के लिए, फ़ॉर्मैट किया जा रहा है.** इसका इस्तेमाल तब करें, जब आपको मॉडल से किसी खास फ़ॉर्मैट में *जवाब* चाहिए हो. उदाहरण के लिए, किसी दस्तावेज़ से डेटा निकालकर डेटाबेस में सेव करना. |
| **फ़ंक्शन कॉलिंग** | **बातचीत के दौरान कार्रवाई करना.** इसका इस्तेमाल तब करें, जब मॉडल को फ़ाइनल जवाब देने से पहले, *आपसे* कोई टास्क (जैसे, "मौसम की मौजूदा जानकारी पाना") पूरा करने के लिए कहना हो. |

## सबसे सही तरीके

- **साफ़ तौर पर ब्यौरा देना:** अपने स्कीमा में `description` फ़ील्ड का इस्तेमाल करें. इससे मॉडल को साफ़ तौर पर यह निर्देश दिया जा सकेगा कि हर प्रॉपर्टी क्या दिखाती है. मॉडल के आउटपुट को गाइड करने के लिए यह ज़रूरी है.
- **स्ट्रॉन्ग टाइपिंग:** जब भी हो सके, खास टाइप (`integer`, `string`, `enum`) का इस्तेमाल करें. अगर किसी पैरामीटर के लिए मान्य वैल्यू का सेट सीमित है, तो `enum` का इस्तेमाल करें.
- **प्रॉम्प्ट इंजीनियरिंग:** अपने प्रॉम्प्ट में साफ़ तौर पर बताएं कि आपको मॉडल से क्या काम करवाना है. उदाहरण के लिए, "टेक्स्ट से यह जानकारी निकालो..." या "इस सुझाव/राय/शिकायत को दिए गए स्कीमा के हिसाब से कैटगरी में बांटो...".
- **पुष्टि करना:** स्ट्रक्चर्ड आउटपुट से, सिंटैक्टिक तौर पर सही JSON की गारंटी मिलती है. हालांकि, इससे यह गारंटी नहीं मिलती कि वैल्यू सिमैंटिक तौर पर सही हैं. अपने ऐप्लिकेशन कोड में, फ़ाइनल आउटपुट का इस्तेमाल करने से पहले, हमेशा उसकी पुष्टि करें.
- **गड़बड़ी ठीक करना:** अपने ऐप्लिकेशन में गड़बड़ी ठीक करने की बेहतर सुविधा लागू करें. इससे उन मामलों को आसानी से मैनेज किया जा सकेगा जहां मॉडल का आउटपुट, स्कीमा के मुताबिक होने के बावजूद आपके कारोबारी नियम से जुड़ी ज़रूरी शर्तों को पूरा नहीं करता है.

## सीमाएं

- **स्कीमा का सबसेट:** JSON स्कीमा स्पेसिफ़िकेशन की सभी सुविधाएँ काम नहीं करती हैं. मॉडल, इस्तेमाल नहीं की जा सकने वाली प्रॉपर्टी को अनदेखा करता है.
- **स्कीमा की जटिलता:** एपीआई, बहुत बड़े या डीपली नेस्ट किए गए स्कीमा को अस्वीकार कर सकता है. अगर आपको गड़बड़ियां मिलती हैं, तो प्रॉपर्टी के नाम छोटे करके, नेस्टिंग कम करके या शर्तों की संख्या सीमित करके, अपने स्कीमा को आसान बनाने की कोशिश करें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-23 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-23 (UTC) को अपडेट किया गया."],[],[]]
