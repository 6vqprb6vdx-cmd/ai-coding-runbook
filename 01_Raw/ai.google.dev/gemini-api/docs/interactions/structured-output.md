---
source_url: https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=hi
fetched_at: 2026-05-11T12:39:52.072246+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# स्ट्रक्चर्ड आउटपुट

Gemini मॉडल को कॉन्फ़िगर करके, दिए गए JSON स्कीमा के मुताबिक जवाब जनरेट किए जा सकते हैं. इससे टाइप-सेफ़ नतीजे मिलते हैं और बिना स्ट्रक्चर वाले टेक्स्ट से स्ट्रक्चर्ड डेटा को आसानी से निकाला जा सकता है.

स्ट्रक्चर्ड आउटपुट का इस्तेमाल इन कामों के लिए सबसे सही है:

- **डेटा निकालना:** टेक्स्ट से नाम और तारीख जैसी जानकारी निकालना.
- **स्ट्रक्चर्ड क्लासिफ़िकेशन:** टेक्स्ट को पहले से तय की गई कैटगरी में बांटना.
- **एजेंटिक वर्कफ़्लो:** टूल या एपीआई के लिए स्ट्रक्चर्ड इनपुट जनरेट करना.

REST API में JSON स्कीमा के साथ-साथ, Google के GenAI SDK टूल में स्कीमा को [Pydantic](https://docs.pydantic.dev/latest/) (Python) और [Zod](https://zod.dev/) (JavaScript) का इस्तेमाल करके भी तय किया जा सकता है.

रेसिपी एक्सट्रैक्टर
कॉन्टेंट मॉडरेशन
रिकर्सिव स्ट्रक्चर

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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
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

**जवाब का उदाहरण:**

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

## स्ट्रीमिंग के नतीजे

स्ट्रक्चर्ड आउटपुट को स्ट्रीम किया जा सकता है. इससे, जवाब जनरेट होने के साथ-साथ उसकी प्रोसेसिंग शुरू की जा सकती है. स्ट्रीम किए गए चंक, मान्य पार्शियल JSON स्ट्रिंग होते हैं. इन्हें जोड़कर, फ़ाइनल JSON ऑब्जेक्ट बनाया जा सकता है.

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

## टूल के साथ स्ट्रक्चर्ड आउटपुट

Gemini 3 की मदद से, स्ट्रक्चर्ड आउटपुट को पहले से मौजूद टूल के साथ जोड़ा जा सकता है. इनमें ये टूल शामिल हैं:
[Google Search से जानकारी पाना](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=hi),
[यूआरएल का कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=hi),
[कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=hi),
[फ़ाइल खोजना](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=hi#structured-output), और
[फ़ंक्शन कॉल करना](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=hi).

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

result = MatchResult.model_validate_json(interaction.steps[-1].content[0].text)
print(result)
```

### JavaScript

```
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

## JSON स्कीमा के साथ काम करता है

JSON ऑब्जेक्ट जनरेट करने के लिए, `response_format` को `text` टाइप के ऑब्जेक्ट (या ऑब्जेक्ट वाला ऐरे) के साथ कॉन्फ़िगर करें. साथ ही, इसके `mime_type` को `application/json` पर सेट करें. स्कीमा, `schema` फ़ील्ड में दिया जाना चाहिए.

Gemini के स्ट्रक्चर्ड आउटपुट मोड में, [JSON स्कीमा](https://json-schema.org/) के कुछ स्पेसिफ़िकेशन काम करते हैं.

`type` एट्रिब्यूट के लिए, इन वैल्यू का इस्तेमाल किया जा सकता है:

- **`string`**: टेक्स्ट के लिए.
- **`number`**: फ़्लोटिंग-पॉइंट नंबर के लिए.
- **`integer`**: पूर्णांकों के लिए.
- **`boolean`**: सही या गलत वैल्यू के लिए.
- **`object`**: यह स्ट्रक्चर्ड डेटा के लिए होता है, जिसमें कुंजी-वैल्यू पेयर होते हैं.
- **`array`**: आइटम की सूचियों के लिए.
- **`null`**: किसी प्रॉपर्टी को शून्य के तौर पर सेट करने के लिए, टाइप कलेक्शन में `"null"` शामिल करें. उदाहरण के लिए, `{"type": ["string", "null"]}`.

ब्यौरे वाली इन प्रॉपर्टी से, मॉडल को गाइड करने में मदद मिलती है:

- **`title`**: किसी प्रॉपर्टी के बारे में कम शब्दों में जानकारी.
- **`description`**: किसी प्रॉपर्टी के बारे में ज़्यादा जानकारी.

### टाइप के हिसाब से प्रॉपर्टी

**`object` वैल्यू के लिए:**

- **`properties`**: यह एक ऐसा ऑब्जेक्ट है जिसमें हर कुंजी, प्रॉपर्टी का नाम होती है और हर वैल्यू, उस प्रॉपर्टी का स्कीमा होती है.
- **`required`**: यह स्ट्रिंग का एक कलेक्शन है. इसमें उन प्रॉपर्टी की सूची दी गई है जिन्हें सेट करना ज़रूरी है.
- **`additionalProperties`**: इससे यह तय होता है कि `properties` में शामिल नहीं की गई प्रॉपर्टी को अनुमति दी जाए या नहीं. यह बूलियन या स्कीमा हो सकता है.

**`string` वैल्यू के लिए:**

- **`enum`**: इसमें क्लासिफ़िकेशन टास्क के लिए, संभावित स्ट्रिंग का एक खास सेट दिया गया है.
- **`format`**: यह स्ट्रिंग के लिए सिंटैक्स तय करता है. जैसे, `date-time`, `date`, `time`.

**`number` और `integer` वैल्यू के लिए:**

- **`enum`**: यह संभावित संख्यात्मक वैल्यू का एक खास सेट दिखाता है.
- **`minimum`**: कम से कम वैल्यू.
- **`maximum`**: ज़्यादा से ज़्यादा वैल्यू.

**`array` वैल्यू के लिए:**

- **`items`**: यह कलेक्शन में मौजूद सभी आइटम के लिए स्कीमा तय करता है.
- **`prefixItems`**: यह पहले N आइटम के लिए स्कीमा की सूची तय करता है. इससे टपल जैसे स्ट्रक्चर बनाए जा सकते हैं.
- **`minItems`**: कलेक्शन में मौजूद आइटम की कम से कम संख्या.
- **`maxItems`**: कलेक्शन में मौजूद आइटम की ज़्यादा से ज़्यादा संख्या.

## मॉडल से जुड़ी सहायता

| मॉडल | स्ट्रक्चर्ड आउटपुट |
| --- | --- |
| Gemini 3.1 Pro की झलक | ✔️ |
| Gemini 3 Flash की झलक | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

*\* Gemini 2.0 के लिए, `propertyOrdering` की साफ़ तौर पर बताई गई सूची ज़रूरी है.*

## स्ट्रक्चर्ड आउटपुट बनाम फ़ंक्शन कॉलिंग

| सुविधा | इस्तेमाल का मुख्य उदाहरण |
| --- | --- |
| **स्ट्रक्चर्ड आउटपुट** | **फ़ाइनल जवाब को फ़ॉर्मैट करना.** इसका इस्तेमाल तब करें, जब आपको मॉडल से किसी खास फ़ॉर्मैट में *जवाब* चाहिए हो. |
| **फ़ंक्शन कॉलिंग** | **बातचीत के दौरान कार्रवाई करना.** इसका इस्तेमाल तब करें, जब मॉडल को फ़ाइनल जवाब देने से पहले, किसी टास्क को पूरा करने के लिए *आपसे पूछना* हो. |

## सबसे सही तरीके

- **साफ़ तौर पर ब्यौरा देना:** मॉडल को सही जानकारी देने के लिए, `description` फ़ील्ड का इस्तेमाल करें.
- **स्ट्रॉन्ग टाइपिंग:** खास टाइप (`integer`, `string`, `enum`) का इस्तेमाल करें.
- **प्रॉम्प्ट इंजीनियरिंग:** साफ़ तौर पर बताएं कि आपको मॉडल से क्या काम कराना है.
- **पुष्टि करना:** आउटपुट, सिंटैक्टिक तौर पर सही JSON है. हालांकि, अपने ऐप्लिकेशन में वैल्यू की पुष्टि हमेशा करें.
- **गड़बड़ी ठीक करना:** स्कीमा के मुताबिक, लेकिन सिमेंटिक रूप से गलत आउटपुट के लिए, गड़बड़ी ठीक करने की मज़बूत सुविधा लागू करें.

## सीमाएं

- **स्कीमा का सबसेट:** JSON स्कीमा की सभी सुविधाएँ काम नहीं करती हैं.
- **स्कीमा की जटिलता:** बहुत बड़े या डीपली नेस्ट किए गए स्कीमा अस्वीकार किए जा सकते हैं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-09 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-09 (UTC) को अपडेट किया गया."],[],[]]
