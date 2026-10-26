---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=hi
fetched_at: 2026-10-26T05:53:31.216996+00:00
title: "\u0938\u094d\u091f\u094d\u0930\u0915\u094d\u091a\u0930\u094d\u0921 \u0906\u0909\u091f\u092a\u0941\u091f \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# स्ट्रक्चर्ड आउटपुट

Gemini मॉडल को इस तरह कॉन्फ़िगर किया जा सकता है कि वे दिए गए JSON स्कीमा के मुताबिक जवाब जनरेट करें. इससे अनुमानित और टाइप-सेफ़ नतीजे मिलते हैं. साथ ही, अनस्ट्रक्चर्ड टेक्स्ट से स्ट्रक्चर्ड डेटा निकालना आसान हो जाता है.

स्ट्रक्चर्ड आउटपुट का इस्तेमाल करना इनके लिए सबसे सही है:

- **डेटा निकालने की सुविधा:** टेक्स्ट से नाम और तारीख जैसी खास जानकारी निकालें.
- **स्ट्रक्चर्ड क्लासिफ़िकेशन:** टेक्स्ट को पहले से तय की गई कैटगरी में बांटें.
- **एजेंटिक वर्कफ़्लो:** टूल या एपीआई के लिए स्ट्रक्चर्ड इनपुट जनरेट करना.

REST API में JSON स्कीमा के साथ-साथ, Google GenAI SDK टूल, [Pydantic](https://docs.pydantic.dev/latest/) (Python) और [Zod](https://zod.dev/) (JavaScript) का इस्तेमाल करके स्कीमा तय करना आसान बनाते हैं.

## स्ट्रक्चर्ड आउटपुट के उदाहरण

### Recipe Extractor

इस उदाहरण में, `object`, `array`, `string`, और `integer` जैसे बुनियादी JSON स्कीमा टाइप का इस्तेमाल करके, टेक्स्ट से स्ट्रक्चर्ड डेटा निकालने का तरीका बताया गया है.

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
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Recipe.model_json_schema(),
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
  model: "gemini-3.8-flash",
  contents: prompt,
  config: {
    responseMimeType: "application/json",
    responseJsonSchema: zodToJsonSchema(recipeSchema),
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
        "gemini-3.8-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### आराम का समय

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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
            "mimeType": "APPLICATION_JSON",
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

इस उदाहरण में, शर्त के साथ स्कीमा के लिए `anyOf` और क्लासिफ़िकेशन के लिए `enum` का इस्तेमाल किया गया है. इससे आउटपुट का स्ट्रक्चर, कॉन्टेंट के हिसाब से अलग-अलग हो सकता है.

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
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": ModerationResult.model_json_schema(),
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
  model: "gemini-3.8-flash",
  contents: prompt,
  config: {
    responseMimeType: "application/json",
    responseJsonSchema: zodToJsonSchema(moderationResultSchema),
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
        "gemini-3.8-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### आराम का समय

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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
            "mimeType": "APPLICATION_JSON",
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

इस उदाहरण में, संगठन के चार्ट जैसे रिकर्सिव स्कीमा को तय करने का तरीका बताया गया है.

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
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Employee.model_json_schema(),
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
  model: "gemini-3.8-flash",
  contents: prompt,
  config: {
    responseMimeType: "application/json",
    responseJsonSchema: zodToJsonSchema(employeeSchema),
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
        "gemini-3.8-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### आराम का समय

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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
            "mimeType": "APPLICATION_JSON",
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

स्ट्रक्चर्ड आउटपुट को स्ट्रीम किया जा सकता है. इससे आपको आउटपुट जनरेट होने के साथ ही, उसे प्रोसेस करने की सुविधा मिलती है. इसके लिए, आपको पूरा आउटपुट जनरेट होने का इंतज़ार नहीं करना पड़ता. इससे आपके ऐप्लिकेशन की परफ़ॉर्मेंस बेहतर हो सकती है.

स्ट्रीम किए गए चंक, मान्य पार्शियल JSON स्ट्रिंग होंगे. इन्हें जोड़कर, फ़ाइनल और पूरा JSON ऑब्जेक्ट बनाया जा सकता है.

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
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Feedback.model_json_schema(),
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
  model: "gemini-3.8-flash",
  contents: prompt,
  config: {
    responseMimeType: "application/json",
    responseJsonSchema: zodToJsonSchema(feedbackSchema),
  },
});

for await (const chunk of stream) {
  console.log(chunk.candidates[0].content.parts[0].text)
}
```

## टूल की मदद से स्ट्रक्चर्ड आउटपुट जनरेट करना

Gemini 3 में, स्ट्रक्चर्ड आउटपुट को पहले से मौजूद टूल के साथ इस्तेमाल किया जा सकता है. इनमें ये टूल शामिल हैं:
[Google Search से सटीक जानकारी पाने की सुविधा](https://ai.google.dev/gemini-api/docs/google-search?hl=hi),
[यूआरएल कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi),
[कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi),
[फ़ाइल सर्च](https://ai.google.dev/gemini-api/docs/file-search?hl=hi#structured-output), और
[फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi).

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
    model="gemini-4-argon",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_mime_type": "application/json",
        "response_json_schema": MatchResult.model_json_schema(),
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
    model: "gemini-4-argon",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseMimeType: "application/json",
      responseJsonSchema: zodToJsonSchema(matchSchema),
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### आराम का समय

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
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
          "mimeType": "APPLICATION_JSON",
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
            },
            "required": ["winner", "final_match_score", "scorers"]
          }
        }
      }
    }
  }'
```

## JSON स्कीमा की सुविधा

JSON ऑब्जेक्ट जनरेट करने के लिए, जनरेशन कॉन्फ़िगरेशन में `response_json_schema` (या REST में `responseFormat.text.schema`) सेट करें. स्कीमा, एक मान्य [JSON स्कीमा](https://json-schema.org/) होना चाहिए, जो आउटपुट के लिए आपके पसंदीदा फ़ॉर्मैट के बारे में बताता हो.

इसके बाद, मॉडल एक ऐसा जवाब जनरेट करेगा जो सिंटैक्स के हिसाब से मान्य JSON स्ट्रिंग होगा और दिए गए स्कीमा से मैच करेगा. स्ट्रक्चर्ड आउटपुट का इस्तेमाल करने पर, मॉडल स्कीमा में मौजूद कुंजियों के क्रम में ही आउटपुट जनरेट करेगा.

Gemini का स्ट्रक्चर्ड आउटपुट मोड, [JSON स्कीमा](https://json-schema.org) की खास जानकारी के सबसेट के साथ काम करता है.

`type` के लिए, इन वैल्यू का इस्तेमाल किया जा सकता है:

- **`string`**: टेक्स्ट के लिए.
- **`number`**: फ़्लोटिंग-पॉइंट नंबर के लिए.
- **`integer`**: पूरी संख्याओं के लिए.
- **`boolean`**: सही/गलत वैल्यू के लिए.
- **`object`**: की-वैल्यू पेयर वाले स्ट्रक्चर्ड डेटा के लिए.
- **`array`**: आइटम की सूचियों के लिए.
- **`null`**: किसी प्रॉपर्टी को शून्य पर सेट करने के लिए, टाइप कलेक्शन में `"null"` को शामिल करें. उदाहरण के लिए, `{"type": ["string", "null"]}`.

जानकारी देने वाली ये प्रॉपर्टी, मॉडल को गाइड करने में मदद करती हैं:

- **`title`**: प्रॉपर्टी के बारे में कम शब्दों में जानकारी.
- **`description`**: किसी प्रॉपर्टी के बारे में ज़्यादा जानकारी.

### टाइप के हिसाब से प्रॉपर्टी

**`object` वैल्यू के लिए:**

- **`properties`**: यह एक ऐसा ऑब्जेक्ट है जिसमें हर कुंजी, प्रॉपर्टी का नाम होती है और हर वैल्यू, उस प्रॉपर्टी का स्कीमा होती है.
- **`required`**: स्ट्रिंग का एक कलेक्शन, जिसमें ज़रूरी प्रॉपर्टी की सूची होती है.
- **`additionalProperties`**: इससे यह कंट्रोल किया जाता है कि `properties` में शामिल नहीं की गई प्रॉपर्टी को अनुमति दी जाए या नहीं. यह बूलियन या स्कीमा हो सकता है.

**`string` वैल्यू के लिए:**

- **`enum`**: इससे क्लासिफ़िकेशन टास्क के लिए, संभावित स्ट्रिंग का एक खास सेट दिखता है.
- **`format`**: इससे स्ट्रिंग के लिए सिंटैक्स तय होता है. जैसे, `date-time`, `date`, `time`.

**`number` और `integer` वैल्यू के लिए:**

- **`enum`**: इसमें संभावित न्यूमेरिक वैल्यू का एक खास सेट शामिल होता है.
- **`minimum`**: कम से कम वैल्यू.
- **`maximum`**: ज़्यादा से ज़्यादा वैल्यू.

**`array` वैल्यू के लिए:**

- **`items`**: इससे कलेक्शन में मौजूद सभी आइटम के लिए स्कीमा तय होता है.
- **`prefixItems`**: यह पहले N आइटम के लिए स्कीमा की सूची तय करता है. इससे ट्यूपल जैसे स्ट्रक्चर बनाए जा सकते हैं.
- **`minItems`**: कलेक्शन में मौजूद आइटम की कम से कम संख्या.
- **`maxItems`**: कलेक्शन में मौजूद आइटम की ज़्यादा से ज़्यादा संख्या.

## मॉडल से जुड़ी सहायता

ये मॉडल, स्ट्रक्चर्ड आउटपुट के साथ काम करते हैं:

| मॉडल | स्ट्रक्चर्ड आउटपुट |
| --- | --- |
| Gemini 4 Argon | ✔️ |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Pro Preview | ✔️ |
| Gemini 3.1 Flash-Lite Preview | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

*\* ध्यान दें कि Gemini 2.0 को JSON इनपुट में साफ़ तौर पर `propertyOrdering` सूची की ज़रूरत होती है, ताकि पसंदीदा स्ट्रक्चर को तय किया जा सके. इसका उदाहरण इस [कुकबुक](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynb) में देखा जा सकता है.*

## स्ट्रक्चर्ड आउटपुट बनाम फ़ंक्शन कॉलिंग

स्ट्रक्चर्ड आउटपुट और फ़ंक्शन कॉलिंग, दोनों में JSON स्कीमा का इस्तेमाल किया जाता है. हालांकि, दोनों का मकसद अलग-अलग होता है:

| सुविधा | इस्तेमाल का मुख्य उदाहरण |
| --- | --- |
| **स्ट्रक्चर्ड आउटपुट** | **उपयोगकर्ता को दिए जाने वाले आखिरी जवाब को फ़ॉर्मैट करना.** इसका इस्तेमाल तब करें, जब आपको मॉडल का *जवाब* किसी खास फ़ॉर्मैट में चाहिए. उदाहरण के लिए, किसी दस्तावेज़ से डेटा निकालकर उसे डेटाबेस में सेव करना. |
| **फ़ंक्शन कॉलिंग** | **बातचीत के दौरान कार्रवाई करना.** इसका इस्तेमाल तब करें, जब मॉडल को फ़ाइनल जवाब देने से पहले, आपको कोई टास्क पूरा करने के लिए *कहना* पड़े. जैसे, "मौसम की मौजूदा जानकारी पाएं". |

## सबसे सही तरीके

- **साफ़ तौर पर ब्यौरा देना:** अपने स्कीमा में `description` फ़ील्ड का इस्तेमाल करें, ताकि मॉडल को साफ़ तौर पर निर्देश दिए जा सकें कि हर प्रॉपर्टी क्या दिखाती है. मॉडल के आउटपुट को गाइड करने के लिए यह ज़रूरी है.
- **स्ट्रॉन्ग टाइपिंग:** जब भी संभव हो, खास टाइप (`integer`, `string`, `enum`) का इस्तेमाल करें. अगर किसी पैरामीटर में मान्य वैल्यू का सीमित सेट है, तो `enum` का इस्तेमाल करें.
- **प्रॉम्प्ट इंजीनियरिंग:** अपने प्रॉम्प्ट में साफ़ तौर पर बताएं कि आपको मॉडल से क्या करवाना है. उदाहरण के लिए, "टेक्स्ट से यह जानकारी निकालें..." या "दिए गए स्कीमा के मुताबिक इस सुझाव/राय/शिकायत को कैटगरी में बांटें...".
- **पुष्टि करना:** स्ट्रक्चर्ड आउटपुट से यह गारंटी मिलती है कि JSON का सिंटैक्स सही है. हालांकि, इससे यह गारंटी नहीं मिलती कि वैल्यू का सिमैंटिक सही है. अपने ऐप्लिकेशन कोड में फ़ाइनल आउटपुट का इस्तेमाल करने से पहले, उसकी पुष्टि ज़रूर करें.
- **गड़बड़ी ठीक करना:** अपने ऐप्लिकेशन में गड़बड़ी ठीक करने की बेहतर सुविधा लागू करें. इससे उन मामलों को आसानी से मैनेज किया जा सकेगा जिनमें मॉडल का आउटपुट, स्कीमा के मुताबिक होने के बावजूद, आपके कारोबारी नियम की ज़रूरी शर्तों को पूरा नहीं करता.

## सीमाएं

- **स्कीमा सबसेट:** JSON स्कीमा की सभी सुविधाएं काम नहीं करतीं. मॉडल, काम न करने वाली प्रॉपर्टी को अनदेखा कर देता है.
- **स्कीमा की जटिलता:** एपीआई, बहुत बड़े या गहराई से नेस्ट किए गए स्कीमा को अस्वीकार कर सकता है. अगर आपको गड़बड़ियां मिलती हैं, तो स्कीमा को आसान बनाने की कोशिश करें. इसके लिए, प्रॉपर्टी के नाम छोटे करें, नेस्टिंग कम करें या पाबंदियों की संख्या सीमित करें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-19 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-19 (UTC) को अपडेट किया गया."],[],[]]
