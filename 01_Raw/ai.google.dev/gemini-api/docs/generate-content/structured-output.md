---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=de
fetched_at: 2026-09-07T05:45:57.634802+00:00
title: "Strukturierte Ausgaben \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Strukturierte Ausgaben

Sie können Gemini-Modelle so konfigurieren, dass sie Antworten generieren, die einem bereitgestellten JSON-Schema entsprechen. So erhalten Sie vorhersagbare, typsichere Ergebnisse und können strukturierte Daten einfacher aus unstrukturiertem Text extrahieren.

Strukturierte Ausgaben sind ideal für folgende Anwendungsfälle:

- **Datenextraktion**:Bestimmte Informationen wie Namen und Datumsangaben aus Text extrahieren.
- **Strukturierte Klassifizierung**:Text in vordefinierte Kategorien einordnen.
- **Agentenbasierte Workflows**:Strukturierte Eingaben für Tools oder APIs generieren.

Die Google GenAI SDKs unterstützen nicht nur JSON-Schemas in der REST API, sondern
ermöglichen auch die einfache Definition von Schemas mit
[Pydantic](https://docs.pydantic.dev/latest/) (Python) und
[Zod](https://zod.dev/) (JavaScript).

## Beispiele für strukturierte Ausgaben

### Rezept-Extraktor

In diesem Beispiel wird gezeigt, wie Sie mit grundlegenden JSON-Schema-Typen wie `object`, `array`, `string` und `integer` strukturierte Daten aus Text extrahieren.

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
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(recipeSchema) } },
  },
});

const recipe = recipeSchema.parse(JSON.parse(response.text));
console.log(recipe);
```

### Ok

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
        "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

**Beispielantwort** :

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

### Inhalte moderieren

In diesem Beispiel werden `anyOf` für bedingte Schemas und `enum` für die Klassifizierung verwendet, sodass die Ausgabestruktur je nach Inhalt variieren kann.

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
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(moderationResultSchema) } },
  },
});

const result = moderationResultSchema.parse(JSON.parse(response.text));
console.log(result);
```

### Ok

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
        "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

### Rekursive Strukturen

In diesem Beispiel wird gezeigt, wie Sie ein rekursives Schema wie ein Organigramm definieren.

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
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(employeeSchema) } },
  },
});

const employee = employeeSchema.parse(JSON.parse(response.text));
console.log(employee);
```

### Ok

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
        "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

**Beispielantwort** :

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

## Streaming

Sie können strukturierte Ausgaben streamen. So können Sie die Antwort verarbeiten, während sie generiert wird, ohne warten zu müssen, bis die gesamte Ausgabe fertig ist. Dadurch kann die wahrgenommene Leistung Ihrer Anwendung verbessert werden.

Die gestreamten Chunks sind gültige partielle JSON-Strings, die zu einem vollständigen JSON-Objekt zusammengefügt werden können.

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
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(feedbackSchema) } },
  },
});

for await (const chunk of stream) {
  console.log(chunk.candidates[0].content.parts[0].text)
}
```

## Strukturierte Ausgaben mit Tools

Mit Gemini 3 können Sie strukturierte Ausgaben mit integrierten Tools kombinieren, darunter
[Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de),
[URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de),
[Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de),
[Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de#structured-output) und
[Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de).

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

## JSON-Schema-Unterstützung

Wenn Sie ein JSON-Objekt generieren möchten, legen Sie das `response_format` in der Generierungskonfiguration fest. Das Schema muss ein gültiges [JSON-Schema](https://json-schema.org/) sein, das das gewünschte Ausgabeformat beschreibt.

Das Modell generiert dann eine Antwort, die ein syntaktisch gültiger JSON-String ist, der dem angegebenen Schema entspricht. Bei Verwendung strukturierter Ausgaben werden die Ausgaben in derselben Reihenfolge wie die Schlüssel im Schema generiert.

Der Modus für strukturierte Ausgaben von Gemini unterstützt eine Teilmenge der [JSON-Schema](https://json-schema.org)-Spezifikation.

Die folgenden Werte von `type` werden unterstützt:

- **`string`**: Für Text.
- **`number`**: Für Gleitkommazahlen.
- **`integer`**: Für ganze Zahlen.
- **`boolean`**: Für „true“/„false“-Werte.
- **`object`**: Für strukturierte Daten mit Schlüssel/Wert-Paaren.
- **`array`**: Für Listen von Elementen.
- **`null`**: Wenn eine Property null sein darf, fügen Sie `"null"` in das Typ-Array ein (z.B. `{"type": ["string", "null"]}`).

Diese beschreibenden Properties helfen, das Modell zu steuern:

- **`title`**: Eine kurze Beschreibung einer Property.
- **`description`**: Eine längere und detailliertere Beschreibung einer Property.

### Typspezifische Properties

**Für `object` Werte:**

- **`properties`**: Ein Objekt, bei dem jeder Schlüssel ein Property-Name und jeder Wert ein Schema für diese Property ist.
- **`required`**: Ein Array von Strings, in dem die obligatorischen Properties aufgeführt sind.
- **`additionalProperties`**: Steuert, ob Properties, die nicht in `properties` aufgeführt sind, zulässig sind. Kann ein boolescher Wert oder ein Schema sein.

**Für `string` Werte:**

- **`enum`**: Listet eine bestimmte Menge möglicher Strings für Klassifizierungsaufgaben auf.
- **`format`**: Gibt eine Syntax für den String an, z. B. `date-time`, `date` oder `time`.

**Für `number` und `integer` Werte:**

- **`enum`**: Listet eine bestimmte Menge möglicher numerischer Werte auf.
- **`minimum`**: Der kleinste inklusive Wert.
- **`maximum`**: Der größte inklusive Wert.

**Für `array` Werte:**

- **`items`**: Definiert das Schema für alle Elemente im Array.
- **`prefixItems`**: Definiert eine Liste von Schemas für die ersten N Elemente und ermöglicht so tupelähnliche Strukturen.
- **`minItems`**: Die Mindestanzahl von Elementen im Array.
- **`maxItems`**: Die Höchstanzahl von Elementen im Array.

## Modellunterstützung

Die folgenden Modelle unterstützen strukturierte Ausgaben:

| Modell | Strukturierte Ausgaben |
| --- | --- |
| Gemini 3.1 Flash Lite | ✔️ |
| Gemini 3.1 Pro (Vorabversion) | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash Lite (Vorabversion) | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash Lite | ✔️\* |

*\* Hinweis: Für Gemini 2.0 ist eine explizite `propertyOrdering` Liste in der JSON-Eingabe erforderlich, um die bevorzugte Struktur zu definieren. Ein Beispiel finden Sie in diesem [Cookbook](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynb).*

## Strukturierte Ausgaben im Vergleich zu Funktionsaufrufen

Sowohl strukturierte Ausgaben als auch Funktionsaufrufe verwenden JSON-Schemas, dienen aber unterschiedlichen Zwecken:

| Funktion | Primärer Anwendungsfall |
| --- | --- |
| **Strukturierte Ausgaben** | **Formatieren der endgültigen Antwort für den Nutzer.** Verwenden Sie diese Option, wenn die *Antwort* des Modells in einem bestimmten Format vorliegen soll (z.B. zum Extrahieren von Daten aus einem Dokument, um sie in einer Datenbank zu speichern). |
| **Funktionsaufrufe** | **Aktionen während der Unterhaltung ausführen.** Verwenden Sie diese Option, wenn das Modell Sie *auffordern* muss, eine Aufgabe auszuführen (z.B. „Aktuelles Wetter abrufen“), bevor es eine endgültige Antwort geben kann. |

## Best Practices

- **Klare Beschreibungen**:Verwenden Sie das Feld `description` in Ihrem Schema, um dem Modell klare Anweisungen zu geben, was jede Property darstellt. Das ist entscheidend, um die Ausgabe des Modells zu steuern.
- **Strenge Typisierung**:Verwenden Sie nach Möglichkeit spezifische Typen (`integer`, `string`, `enum`). Wenn ein Parameter eine begrenzte Anzahl gültiger Werte hat, verwenden Sie `enum`.
- **Prompt-Engineering** : Geben Sie in Ihrem Prompt klar an, was das Modell tun soll. Beispiel: „Extrahieren Sie die folgenden Informationen aus dem Text…“ oder „Klassifizieren Sie dieses Feedback gemäß dem angegebenen Schema…“.
- **Validierung**:Strukturierte Ausgaben garantieren zwar syntaktisch korrektes JSON, aber nicht, dass die Werte semantisch korrekt sind. Validieren Sie die endgültige Ausgabe immer in Ihrem Anwendungscode, bevor Sie sie verwenden.
- **Fehlerbehandlung**:Implementieren Sie eine robuste Fehlerbehandlung in Ihrer Anwendung, um Fälle zu verarbeiten, in denen die Ausgabe des Modells zwar dem Schema entspricht, aber möglicherweise nicht Ihren Geschäftslogikanforderungen genügt.

## Beschränkungen

- **Schema-Teilmenge**:Nicht alle Funktionen der JSON-Schema-Spezifikation werden unterstützt. Das Modell ignoriert nicht unterstützte Properties.
- **Schema-Komplexität**:Die API lehnt möglicherweise sehr große oder tief verschachtelte Schemas ab. Wenn Fehler auftreten, versuchen Sie, Ihr Schema zu vereinfachen, indem Sie Property-Namen kürzen, die Verschachtelung reduzieren oder die Anzahl der Einschränkungen begrenzen.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
