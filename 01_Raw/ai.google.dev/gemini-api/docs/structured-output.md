---
source_url: https://ai.google.dev/gemini-api/docs/structured-output?hl=th
fetched_at: 2026-08-24T02:21:49.096371+00:00
title: "\u0e40\u0e2d\u0e32\u0e15\u0e4c\u0e1e\u0e38\u0e15\u0e17\u0e35\u0e48\u0e21\u0e35\u0e42\u0e04\u0e23\u0e07\u0e2a\u0e23\u0e49\u0e32\u0e07 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# เอาต์พุตที่มีโครงสร้าง

คุณสามารถกำหนดค่าโมเดล Gemini ให้สร้างคำตอบที่เป็นไปตาม JSON Schema ที่ระบุได้ ซึ่งจะช่วยให้ได้ผลลัพธ์ที่คาดการณ์ได้และมีความปลอดภัยในการกำหนดประเภท รวมถึงลดความซับซ้อนในการดึง Structured Data จากข้อความที่ไม่มีโครงสร้าง

การใช้เอาต์พุตที่มีโครงสร้างเหมาะสำหรับกรณีต่อไปนี้

- **การดึงข้อมูล:** ดึงข้อมูลที่เฉพาะเจาะจง เช่น ชื่อและวันที่ จากข้อความ
- **การจัดประเภทที่มีโครงสร้าง:** จัดประเภทข้อความเป็นหมวดหมู่ที่กำหนดไว้ล่วงหน้า
- **เวิร์กโฟลว์แบบ Agent:** สร้างอินพุตที่มีโครงสร้างสำหรับเครื่องมือหรือ API

นอกจากจะรองรับ JSON Schema ใน REST API แล้ว Google GenAI SDK ยังช่วยให้คุณกำหนดสคีมาโดยใช้
[Pydantic](https://docs.pydantic.dev/latest/) (Python) และ
[Zod](https://zod.dev/) (JavaScript) ได้ด้วย

## ตัวอย่างเอาต์พุตที่มีโครงสร้าง

### ตัวดึงข้อมูลสูตรอาหาร

ตัวอย่างนี้แสดงวิธีดึง Structured Data จากข้อความโดยใช้ประเภท JSON Schema พื้นฐาน เช่น `object`, `array`, `string` และ `integer`

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
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
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

**ตัวอย่างการตอบสนอง:**

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

### การกลั่นกรองเนื้อหา

ตัวอย่างนี้แสดง `anyOf` สำหรับสคีมาแบบมีเงื่อนไขและ `enum` สำหรับการจัดประเภท ซึ่งช่วยให้โครงสร้างเอาต์พุตแตกต่างกันไปตามเนื้อหาได้

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
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
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

**ตัวอย่างการตอบสนอง:**

```
{
  "decision": {
    "reason": "The content is an unsolicited prize notification attempting to trick the user into clicking a suspicious link.",
    "spam_type": "scam"
  }
}
```

### โครงสร้างแบบวนซ้ำ

ตัวอย่างนี้แสดงวิธีกำหนดสคีมาแบบวนซ้ำ เช่น แผนผังองค์กร

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
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
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

**ตัวอย่างการตอบสนอง:**

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

## การสตรีมผลลัพธ์

คุณสามารถสตรีมเอาต์พุตที่มีโครงสร้าง ซึ่งช่วยให้คุณเริ่มประมวลผลการตอบสนองได้ทันทีที่ระบบสร้างการตอบสนอง ก้อนข้อมูลที่สตรีมเป็นสตริง JSON บางส่วนที่ถูกต้อง ซึ่งสามารถนำมารวมกันเพื่อสร้างออบเจ็กต์ JSON สุดท้ายได้

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
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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

### REST

```
curl -N -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
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

## เอาต์พุตที่มีโครงสร้างพร้อมเครื่องมือ

Gemini 3 ช่วยให้คุณรวมเอาต์พุตที่มีโครงสร้างกับเครื่องมือในตัวได้ ซึ่งรวมถึง
[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th),
[บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th),
[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th),
[การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th#structured-output) และ
[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)

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

## การรองรับ JSON Schema

หากต้องการสร้างออบเจ็กต์ JSON ให้กำหนดค่า `response_format` ด้วยออบเจ็กต์ (หรืออาร์เรย์ที่มีออบเจ็กต์) ประเภท `text` และตั้งค่า `mime_type` เป็น `application/json` โดยคุณควรระบุสคีมาในช่อง `schema`

โหมดเอาต์พุตที่มีโครงสร้างของ Gemini รองรับข้อมูลจำเพาะของ
[JSON Schema](https://json-schema.org/) บางส่วน

ระบบรองรับค่า `type` ต่อไปนี้

- **`string`**: สำหรับข้อความ
- **`number`**: สำหรับเลขจุดลอยตัว
- **`integer`**: สำหรับจำนวนเต็ม
- **`boolean`**: สำหรับค่าจริงหรือเท็จ
- **`object`**: สำหรับ Structured Data พร้อมคู่คีย์-ค่า
- **`array`**: สำหรับรายการไอเทม
- **`null`**: หากต้องการอนุญาตให้พร็อพเพอร์ตี้เป็น null ให้ใส่ `"null"` ในอาร์เรย์ประเภท (เช่น `{"type": ["string", "null"]}`)

พร็อพเพอร์ตี้เชิงอธิบายเหล่านี้ช่วยแนะนำโมเดล

- **`title`**: คำอธิบายสั้นๆ ของพร็อพเพอร์ตี้
- **`description`**: คำอธิบายที่ยาวและละเอียดมากขึ้นของพร็อพเพอร์ตี้

### พร็อพเพอร์ตี้เฉพาะประเภท

**สำหรับค่า `object`**

- **`properties`**: ออบเจ็กต์ที่แต่ละคีย์เป็นชื่อพร็อพเพอร์ตี้ และแต่ละค่าเป็นสคีมาสำหรับพร็อพเพอร์ตี้นั้น
- **`required`**: อาร์เรย์ของสตริงที่แสดงรายการพร็อพเพอร์ตี้ที่ต้องระบุ
- **`additionalProperties`**: ควบคุมว่าจะอนุญาตพร็อพเพอร์ตี้ที่ไม่ได้ระบุไว้ใน `properties` หรือไม่ โดยอาจเป็นบูลีนหรือสคีมา

**สำหรับค่า `string`**

- **`enum`**: แสดงรายการชุดสตริงที่เป็นไปได้ที่เฉพาะเจาะจงสำหรับงานการจัดประเภท
- **`format`**: ระบุไวยากรณ์สำหรับสตริง เช่น `date-time`, `date`, `time`

**สำหรับค่า `number` และ `integer`**

- **`enum`**: แสดงรายการชุดค่าตัวเลขที่เป็นไปได้ที่เฉพาะเจาะจง
- **`minimum`**: ค่าต่ำสุดแบบรวม
- **`maximum`**: ค่าสูงสุดแบบรวม

**สำหรับค่า `array`**

- **`items`**: กำหนดสคีมาสำหรับไอเทมทั้งหมดในอาร์เรย์
- **`prefixItems`**: กำหนดรายการสคีมาสำหรับไอเทม N รายการแรก ซึ่งช่วยให้มีโครงสร้างคล้ายกับ Tuple
- **`minItems`**: จำนวนไอเทมขั้นต่ำในอาร์เรย์
- **`maxItems`**: จำนวนไอเทมสูงสุดในอาร์เรย์

## เอาต์พุตที่มีโครงสร้างเทียบกับการเรียกใช้ฟังก์ชัน

| ฟีเจอร์ | กรณีการใช้งานหลัก |
| --- | --- |
| **เอาต์พุตที่มีโครงสร้าง** | **การจัดรูปแบบการตอบสนองสุดท้าย** ใช้เมื่อต้องการให้ *คำตอบ* ของโมเดลอยู่ในรูปแบบที่เฉพาะเจาะจง |
| **การเรียกใช้ฟังก์ชัน** | **การดำเนินการระหว่างการสนทนา** ใช้เมื่อโมเดลต้อง *ขอให้คุณ* ทำงานบางอย่างก่อนที่จะให้คำตอบสุดท้าย |

## แนวทางปฏิบัติแนะนำ

- **คำอธิบายที่ชัดเจน:** ใช้ช่อง `description` เพื่อแนะนำโมเดล
- **การพิมพ์ที่เข้มงวด:** ใช้ประเภทที่เฉพาะเจาะจง (`integer`, `string`, `enum`)
- **วิศวกรรมพรอมต์ (Prompt Engineering):** ระบุสิ่งที่คุณต้องการให้โมเดลทำอย่างชัดเจน
- **การตรวจสอบ:** แม้ว่าเอาต์พุตจะเป็น JSON ที่มีไวยากรณ์ถูกต้อง แต่ให้ตรวจสอบค่าในแอปพลิเคชันเสมอ
- **การจัดการข้อผิดพลาด:** ใช้การจัดการข้อผิดพลาดที่มีประสิทธิภาพสำหรับเอาต์พุตที่เป็นไปตามสคีมาแต่มีความหมายไม่ถูกต้อง

## ข้อจำกัด

- **สคีมาบางส่วน:** ระบบไม่รองรับฟีเจอร์ทั้งหมดของ JSON Schema
- **ความซับซ้อนของสคีมา:** ระบบอาจปฏิเสธสคีมาที่มีขนาดใหญ่มากหรือมีการซ้อนกันหลายชั้น

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
