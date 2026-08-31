---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/structured-output?hl=zh-CN
fetched_at: 2026-08-31T06:36:28.835182+00:00
title: "\u7ed3\u6784\u5316\u8f93\u51fa \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 结构化输出

您可以将 Gemini 模型配置为生成符合所提供 JSON 架构的回答。这可确保获得可预测的类型安全结果，并简化从非结构化文本中提取结构化数据的过程。

使用结构化输出非常适合以下情况：

- **数据提取**：从文本中提取特定信息，例如姓名和日期。
- **结构化分类**：将文本归入预定义的类别。
- **Agentic 工作流**：为工具或 API 生成结构化输入。

除了在 REST API 中支持 JSON 架构之外，Google GenAI SDK 还可让您使用 [Pydantic](https://docs.pydantic.dev/latest/) (Python) 和 [Zod](https://zod.dev/) (JavaScript) 轻松定义架构。

## 结构化输出示例

### 食谱提取器

此示例演示了如何使用 `object`、`array`、`string` 和 `integer` 等基本 JSON 架构类型从文本中提取结构化数据。

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

### Go

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

**示例回答**：

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

### 内容审核

此示例展示了 `anyOf`（用于条件架构）和 `enum`（用于分类），从而使输出结构能够根据内容而变化。

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

### Go

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

### 递归结构

此示例展示了如何定义递归架构，例如组织结构图。

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

### Go

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

**示例回答**：

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

## 流式

您可以流式传输结构化输出，这样一来，您就可以在生成回答的同时开始处理回答，而无需等待整个输出完成。这有助于提升应用的感知性能。

流式传输的块将是有效的部分 JSON 字符串，可以连接起来形成最终的完整 JSON 对象。

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

## 使用工具生成结构化输出

借助 Gemini 3，您可以将结构化输出与内置工具相结合，包括[依托 Google 搜索进行接地](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)、[网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)、[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)、[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn#structured-output)和[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)。

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

## JSON 架构支持

如需生成 JSON 对象，请在生成配置中设置 `response_format`。架构必须是描述所需输出格式的有效 [JSON 架构](https://json-schema.org/)。

然后，模型会生成一个在语法上有效的 JSON 字符串，该字符串与所提供的架构相符。使用结构化输出时，模型将按架构中键的顺序生成输出。

Gemini 的结构化输出模式支持部分 [JSON 架构](https://json-schema.org)规范。

支持以下 `type` 值：

- **`string`**：对于文本。
- **`number`**：适用于浮点数。
- **`integer`**：适用于整数。
- **`boolean`**：对于 true/false 值。
- **`object`**：适用于包含键值对的结构化数据。
- **`array`**：适用于商品列表。
- **`null`**：如需允许属性为 null，请在类型数组中添加 `"null"`（例如 `{"type": ["string", "null"]}`）。

这些描述性属性有助于引导模型：

- **`title`**：属性的简短说明。
- **`description`**：属性的更长、更详细的说明。

### 特定于类型的属性

**对于 `object` 值**：

- **`properties`**：一个对象，其中每个键都是属性名称，每个值都是相应属性的架构。
- **`required`**：一个字符串数组，列出了哪些属性是必需的。
- **`additionalProperties`**：控制是否允许使用未在 `properties` 中列出的属性。可以是布尔值或架构。

**对于 `string` 值**：

- **`enum`**：列出分类任务的一组特定可能字符串。
- **`format`**：指定字符串的语法，例如 `date-time`、`date`、`time`。

**对于 `number` 和 `integer` 值**：

- **`enum`**：列出了一组特定的可能数值。
- **`minimum`**：包含在内的最小值。
- **`maximum`**：最大值（含）。

**对于 `array` 值**：

- **`items`**：定义数组中所有元素的架构。
- **`prefixItems`**：为前 N 个项定义架构列表，从而实现类似元组的结构。
- **`minItems`**：数组中的最小项数。
- **`maxItems`**：数组中的项数上限。

## 模型支持

以下模型支持结构化输出：

| 模型 | 结构化输出 |
| --- | --- |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3 Pro 预览版 | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite 预览版 | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

*\* 请注意，Gemini 2.0 需要在 JSON 输入中明确指定 `propertyOrdering` 列表，以定义首选结构。您可以在此[实战宝典](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynb)中找到示例。*

## 结构化输出与函数调用

结构化输出和函数调用都使用 JSON 架构，但用途不同：

| 功能 | 主要使用场景 |
| --- | --- |
| **结构化输出** | **设置最终用户响应的格式。**如果您希望模型的*回答*采用特定格式（例如，从文档中提取数据以保存到数据库），请使用此参数。 |
| **函数调用** | **在对话期间采取行动。**当模型需要*询问您*才能执行任务（例如“获取当前天气”）时，请使用此值。 |

## 最佳做法

- **清晰的说明**：使用架构中的 `description` 字段向模型清晰说明每个属性的含义。这对于引导模型的输出至关重要。
- **强类型**：尽可能使用特定类型（`integer`、`string`、`enum`）。如果某个形参的有效值数量有限，请使用 `enum`。
- **提示工程**：在提示中明确说明您希望模型执行的操作。例如，“从文本中提取以下信息…”或“根据提供的架构对这条反馈进行分类…”。
- **验证**：虽然结构化输出可保证 JSON 在语法上正确，但无法保证值在语义上正确。请务必先验证应用代码中的最终输出，然后再使用。
- **错误处理**：在应用中实现强大的错误处理机制，以便妥善管理模型输出虽然符合架构要求，但可能不符合业务逻辑要求的情况。

## 限制

- **架构子集**：不支持 JSON 架构规范的所有功能。模型会忽略不受支持的属性。
- **架构复杂性**：API 可能会拒绝非常大或嵌套很深的架构。如果您遇到错误，请尝试缩短属性名称、减少嵌套或限制约束数量，以简化架构。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-30。"],[],[]]
