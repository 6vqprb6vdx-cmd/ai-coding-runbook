---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=hi
fetched_at: 2026-06-29T05:36:48.487895+00:00
title: "Interactions API \u092a\u0930 \u092e\u093e\u0907\u0917\u094d\u0930\u0947\u091f \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Interactions API पर माइग्रेट करना

इस गाइड से, आपको `generateContent` API से Interactions API पर माइग्रेट करने में मदद मिलती है.

Interactions API, Gemini के साथ इंटिग्रेट करने के लिए स्टैंडर्ड इंटरफ़ेस है. इसे एजेंटिक वर्कफ़्लो, सर्वर-साइड स्टेट मैनेजमेंट, और जटिल मल्टी-मोडल, मल्टी-टर्न बातचीत के लिए ऑप्टिमाइज़ किया गया है. साथ ही, यह बिना स्टेट वाले सिंगल-टर्न के सामान्य अनुरोधों को पूरी तरह से सपोर्ट करता है. `generateContent` को पूरी तरह से सपोर्ट किया जाता है. हालांकि, हमारा सुझाव है कि नए डेवलपमेंट के लिए, Interactions API का इस्तेमाल करें.

### माइग्रेट क्यों करें?

Interactions API, Gemini के साथ इंटिग्रेट करने का ज़्यादा स्ट्रक्चर्ड और बेहतर तरीका है:

- **सर्वर-साइड इतिहास मैनेजमेंट**: `previous_interaction_id` की मदद से, मल्टी-टर्न फ़्लो को आसान बनाया गया है. सर्वर, डिफ़ॉल्ट रूप से स्टेट को चालू करता है (`store=true`). हालांकि, `store=false` सेट करके, बिना स्टेट वाले व्यवहार को चुना जा सकता है.
- **ऑब्ज़र्वेबल एक्ज़ीक्यूशन स्टेप**: टाइप किए गए स्टेप की मदद से, जटिल फ़्लो को डीबग करना और इंटरमीडिएट इवेंट (जैसे, थॉट या सर्च विजेट) के लिए यूज़र इंटरफ़ेस (यूआई) रेंडर करना आसान हो जाता है.
- **एजेंटिक वर्कफ़्लो के लिए बनाया गया है**: टाइप किए गए एक्ज़ीक्यूशन स्टेप की मदद से, मल्टी-स्टेप टूल के इस्तेमाल, ऑर्केस्ट्रेशन, और जटिल रीज़निंग फ़्लो के लिए नेटिव सपोर्ट.
- **लंबे समय तक चलने वाले और बैकग्राउंड टास्क**: Deep Think और Deep Research जैसी समय लेने वाली कार्रवाइयों को बैकग्राउंड प्रोसेस में ऑफ़लोड करने की सुविधा. `background=true`

## सामान्य इनपुट/आउटपुट

इस सेक्शन में, टेक्स्ट जनरेट करने के सामान्य अनुरोध को माइग्रेट करने का तरीका बताया गया है.

### `generateContent` का इस्तेमाल करने से पहले

`generateContent` API, बिना स्टेट वाला है और सीधे जवाब देता है. जवाब का स्ट्रक्चर, आउटपुट को `candidates` की सूची में रैप करता है. हर कैंडिडेट में, पार्स करने के लिए `parts` की सूची के साथ `content` होता है.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Tell me a joke."
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-2.5-flash",
  contents: "Tell me a joke.",
});
console.log(response.text);
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Tell me a joke."
        }]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Why did the chicken cross the road? To get to the other side!"
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 4,
    "candidatesTokenCount": 12,
    "totalTokenCount": 16
  }
}
```

Interactions API, `steps` टाइमलाइन के साथ, सेव किया गया इंटरैक्शन रिसॉर्स दिखाता है. इंटरमीडिएट इवेंट ढूंढने के लिए, `steps` ऐरे की जांच मैन्युअल तरीके से की जा सकती है. हालांकि, Google GenAI SDK टूल, फ़ाइनल आउटपुट को ऐक्सेस करने के लिए, दिखाए गए `Interaction` ऑब्जेक्ट पर सीधे तौर पर सुविधाजनक प्रॉपर्टी उपलब्ध कराते हैं.

सबसे आम सुविधाजनक प्रॉपर्टी **`.output_text`** (स्ट्रिंग) है. यह मॉडल के जवाब के आखिर में, लगातार `TextContent` ब्लॉक को अपने-आप एक्सट्रैक्ट और जॉइन करती है. यह सामान्य जवाबों के लिए पूरी तरह से काम करती है. हालांकि, इसमें टेक्स्ट के पहले वाले ब्लॉक शामिल नहीं होते. ये ब्लॉक, नॉन-टेक्स्ट कॉन्टेंट (जैसे, थॉट, इमेज, ऑडियो या टूल कॉल) से अलग किए जाते हैं. जटिल या इंटरलीव्ड मल्टीमोडल जवाबों के लिए, आपको इसके बजाय `steps` पर मैन्युअल तरीके से इटरेट करना होगा.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

console.log(interaction.output_text);
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a joke."
}'

# Response
{
  "id": "int_123",
  "status": "completed",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Tell me a joke."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

## मल्टी-टर्न बातचीत

Interactions API, डिफ़ॉल्ट रूप से इंटरैक्शन सेव करता है. इससे, मल्टी-टर्न बातचीत के लिए सर्वर-साइड स्टेट मैनेजमेंट की सुविधा मिलती है.

### `generateContent` का इस्तेमाल करने से पहले

`generateContent` में, आपको `contents` ऐरे या क्लाइंट-साइड चैट हेल्पर का इस्तेमाल करके, बातचीत के इतिहास को मैन्युअल तरीके से मैनेज करना होगा.

### Python

**चैट हेल्पर का इस्तेमाल करना (इसका सुझाव दिया जाता है)**

```
from google import genai

client = genai.Client()

chat = client.chats.create(model="gemini-2.5-flash")
response1 = chat.send_message("Hi, my name is Phil.")
print(response1.text)

response2 = chat.send_message("What is my name?")
print(response2.text)
```

**इतिहास को मैन्युअल तरीके से मैनेज करना**

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Content(
            role="user", parts=[types.Part.from_text("Hi, my name is Phil.")]
        ),
        types.Content(
            role="model",
            parts=[types.Part.from_text("Hi Phil, how can I help you?")],
        ),
        types.Content(
            role="user", parts=[types.Part.from_text("What is my name?")]
        ),
    ],
)
print(response.text)
```

### JavaScript

**चैट हेल्पर का इस्तेमाल करना (इसका सुझाव दिया जाता है)**

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const chat = client.chats.create({ model: 'gemini-2.5-flash' });
let response = await chat.sendMessage({ message: 'Hi, my name is Phil.' });
console.log(response.text);

response = await chat.sendMessage({ message: 'What is my name?' });
console.log(response.text);
```

**इतिहास को मैन्युअल तरीके से मैनेज करना**

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: [
        { role: 'user', parts: [{ text: 'Hi, my name is Phil.' }] },
        { role: 'model', parts: [{ text: 'Hi Phil, how can I help you?' }] },
        { role: 'user', parts: [{ text: 'What is my name?' }] }
    ]
});
console.log(response.text);
```

### REST

```
# Request (the second turn requires sending the entire history)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [
        {"role": "user", "parts": [{"text": "Hi, my name is Phil."}]},
        {"role": "model", "parts": [{"text": "Hi Phil, how can I help you?"}]},
        {"role": "user", "parts": [{"text": "What is my name?"}]}
    ]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Your name is Phil."
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ]
}
```

### Interactions API का इस्तेमाल करने के बाद

Interactions API, सर्वर पर स्टेट को मैनेज करता है. `previous_interaction_id` का रेफ़रंस देकर, बातचीत जारी रखी जा सकती है.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.5-flash", input="Hi, my name is Phil."
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    previous_interaction_id=interaction1.id,
    input="What is my name?",
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Hi, my name is Phil.'
});
console.log("Response 1:", interaction.output_text);

interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    previous_interaction_id: interaction.id,
    input: 'What is my name?'
});
console.log("Response 2:", interaction.output_text);
```

### REST

```
# First Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": "Hi, my name is Phil."
}'

# Second Request (using ID from first response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "previous_interaction_id": "int_123",
    "input": "What is my name?"
}'

# Response to Second Request
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Hi, my name is Phil." }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [{ "type": "text", "text": "Hello Phil! How can I help you today?" }]
    },
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "What is my name?" }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [{ "type": "text", "text": "Your name is Phil." }]
    }
  ]
}
```

## मल्टीमोडल इनपुट

दोनों एपीआई, मल्टीमोडल इनपुट (टेक्स्ट, इमेज, वीडियो वगैरह) को सपोर्ट करते हैं.

### `generateContent` का इस्तेमाल करने से पहले

`generateContent` में, `contents` ऐरे में `parts` की सूची पास की जाती है. जवाब, पहले कैंडिडेट के `parts` में आउटपुट दिखाता है.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open("sample.jpg", "rb") as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
        "Describe this image.",
    ],
)
print(response.text)
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [
            {
                "inlineData": {
                    "mimeType": "image/jpeg",
                    "data": "..."
                }
            },
            {
                "text": "Describe this image."
            }
        ]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "This is a picture of a beautiful sunset."
          }
        ],
        "role": "model"
      }
    }
  ]
}
```

### Interactions API का इस्तेमाल करने के बाद

Interactions API में, `input` फ़ील्ड में एक ऐरे पास किया जाता है. टाइमलाइन में `model_output` स्टेप ढूंढकर, आउटपुट कॉन्टेंट वापस पाया जा सकता है.

### Python

```
from google import genai

client = genai.Client()

with open("sample.jpg", "rb") as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_bytes,
        },
        {"type": "text", "text": "Describe this image."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const imageBytes = fs.readFileSync('sample.jpg').toString('base64');

const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: [
        {
            type: 'image',
            mime_type: 'image/jpeg',
            data: imageBytes
        },
        {
            type: 'text',
            text: 'Describe this image.'
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": [
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": "..."
        },
        {
            "type": "text",
            "text": "Describe this image."
        }
    ]
}'

# Response
{
  "id": "int_multimodal",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        {
          "type": "image",
          "mime_type": "image/jpeg",
          "data": "..."
        },
        {
          "type": "text",
          "text": "Describe this image."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "This is a picture of a beautiful sunset over the mountains."
        }
      ]
    }
  ]
}
```

## स्ट्रक्चर्ड आउटपुट

मॉडल से किसी खास स्कीमा से मेल खाने वाला JSON पाने के लिए, जवाब का फ़ॉर्मैट कॉन्फ़िगर करें.

### `generateContent` का इस्तेमाल करने से पहले

`generateContent` में, `generationConfig` ऑब्जेक्ट में नेस्ट किए गए `response_format` फ़ील्ड का इस्तेमाल करके, आउटपुट फ़ॉर्मैट कॉन्फ़िगर किया जाता है.

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel

client = genai.Client()

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Give me a recipe for chocolate chip cookies.",
    config=types.GenerateContentConfig(
        response_format=[
            {
                "type": "text",
                "mime_type": "application/json",
                "schema": Recipe,
            }
        ]
    ),
)
print(response.text)
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Give me a recipe for chocolate chip cookies."
        }]
    }],
    "generationConfig": {
        "responseFormat": [
            {
                "type": "text",
                "mimeType": "application/json",
                "schema": {
                    "type": "OBJECT",
                    "properties": {
                        "recipe_name": { "type": "STRING" },
                        "ingredients": {
                            "type": "ARRAY",
                            "items": { "type": "STRING" }
                        }
                    },
                    "required": ["recipe_name", "ingredients"]
                }
            }
        ]
    }
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"
          }
        ],
        "role": "model"
      }
    }
  ]
}
```

### Interactions API का इस्तेमाल करने के बाद

Interactions API में, आउटपुट फ़ॉर्मैट कंट्रोल, टॉप-लेवल `response_format` ऐरे में चले जाते हैं.

### Python

```
from google import genai
from pydantic import BaseModel

client = genai.Client()

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Give me a recipe for chocolate chip cookies.",
    response_format=[
        {
            "type": "text",
            "mime_type": "application/json",
            "schema": Recipe,
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Give me a recipe for chocolate chip cookies.',
    response_format: [
        {
            type: 'text',
            mime_type: 'application/json',
            schema: {
                type: 'object',
                properties: {
                    recipe_name: { type: 'string' },
                    ingredients: {
                        type: 'array',
                        items: { type: 'string' }
                    }
                },
                required: ['recipe_name', 'ingredients']
            }
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": "Give me a recipe for chocolate chip cookies.",
    "response_format": [
        {
            "type": "text",
            "mime_type": "application/json",
            "schema": {
                "type": "OBJECT",
                "properties": {
                    "recipe_name": { "type": "STRING" },
                    "ingredients": {
                        "type": "ARRAY",
                        "items": { "type": "STRING" }
                    }
                },
                "required": ["recipe_name", "ingredients"]
            }
        }
    ]
}'

# Response
{
  "id": "int_structured",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Give me a recipe for chocolate chip cookies." }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"
        }
      ]
    }
  ]
}
```

## मल्टीमोडल जनरेशन

टेक्स्ट के अलावा अन्य फ़ॉर्मैट (जैसे, इमेज या ऑडियो) में कॉन्टेंट जनरेट करते समय, मुख्य अंतर यह होता है कि जवाब, जनरेट किए गए मीडिया को कैसे स्ट्रक्चर करता है.

### `generateContent` का इस्तेमाल करने से पहले

`generateContent` में, जवाब, जनरेट किए गए मीडिया को सीधे कैंडिडेट के `parts` में दिखाता है. आम तौर पर, यह `inlineData` में base64 डेटा के तौर पर दिखता है.

```
# Response structure concept
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Here is your generated image:"
          },
          {
            "inlineData": {
              "mimeType": "image/jpeg",
              "data": "...base64..."
            }
          }
        ]
      }
    }
  ]
}
```

### Interactions API का इस्तेमाल करने के बाद

Interactions API में, जनरेट किया गया मीडिया, टाइमलाइन में `model_output` स्टेप के `content` ऐरे में अलग-अलग आइटम के तौर पर दिखता है. इससे, इंटरैक्शन का क्रम बना रहता है.

```
# Response structure concept
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Here is your generated image:"
        },
        {
          "type": "image",
          "mime_type": "image/jpeg",
          "data": "...base64..." // Or a reference URL in future
        }
      ]
    }
  ]
}
```

इससे, जवाब को पार्स करने का तरीका, इनपुट और टेक्स्ट आउटपुट को हैंडल करने के तरीके के मुताबिक बना रहता है. टाइमलाइन में हर चीज़ एक स्टेप होती है.

## सर्वर-साइड टूल

Gemini, Google Search grounding जैसे बिल्ट-इन सर्वर-साइड टूल को सपोर्ट करता है. मुख्य अंतर यह है कि जवाब, टूल के एक्ज़ीक्यूशन को कैसे दिखाता है.

### `generateContent` का इस्तेमाल करने से पहले

`generateContent` में, सर्वर-साइड टूल ज़्यादातर ओपेक होते हैं. टूल को चालू करने पर, आपको `groundingMetadata` ऑब्जेक्ट के साथ फ़ाइनल जवाब मिलता है. अहम बात यह है कि साइटेशन इनलाइन नहीं होते. `groundingSupports`, `groundingChunks` में टेक्स्ट सेगमेंट को वेब सोर्स पर वापस मैप करने के लिए, वर्ण इंडेक्स का इस्तेमाल करते हैं.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Who won Euro 2024?",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}]
    ),
)

metadata = response.candidates[0].grounding_metadata
if metadata.search_entry_point:
    print(f"Search Entry Point: {metadata.search_entry_point.rendered_content}")

for support in metadata.grounding_supports:
    print(f"Citation: {support.segment.text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: 'Who won Euro 2024?',
    config: {
        tools: [{ google_search: {} }]
    }
});

const metadata = response.candidates[0].groundingMetadata;
if (metadata.searchEntryPoint) {
    console.log(`Search Entry Point: ${metadata.searchEntryPoint.renderedContent}`);
}
for (const support of metadata.groundingSupports) {
    console.log(`Citation: ${support.segment.text}`);
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Who won Euro 2024?"
        }]
    }],
    "tools": [{
        "googleSearchRetrieval": {}
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

### Interactions API का इस्तेमाल करने के बाद

Interactions API में, सर्वर-साइड टूल, पूरी टाइमलाइन की पारदर्शिता उपलब्ध कराते हैं. एपीआई, कॉल और नतीजे को अलग-अलग एक्ज़ीक्यूशन `steps` (`google_search_call` और `google_search_result`) के तौर पर रिकॉर्ड करता है. इससे यह पता चलता है कि मॉडल ने कौनसा डेटा वापस पाया है.

इसके अलावा, एपीआई, साइटेशन **इनलाइन** दिखाता है. मेटाडेटा के किसी अलग ऑब्जेक्ट से इंडेक्स को मैप करने के बजाय, `model_output` स्टेप में मौजूद टेक्स्ट आइटम में अपना `annotations` ऐरे होता है. यह ऐरे, सीधे सोर्स से लिंक होता है.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Who won Euro 2024?",
    tools=[{"type": "google_search"}],
)

for step in interaction.steps:
    if step.type == "google_search_result":
        print(f"Search Suggestions: {step.search_suggestions}")
    elif step.type == "model_output":
        print(f"Answer: {step.content[0].text}")
        if step.content[0].annotations:
            for anno in step.content[0].annotations:
                print(f"Citation: {anno.title} ({anno.uri})")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Who won Euro 2024?',
    tools: [{ type: 'google_search' }]
});

for (const step of interaction.steps) {
    if (step.type === 'google_search_result') {
        console.log(`Search Suggestions: ${step.search_suggestions}`);
    } else if (step.type === 'model_output') {
        console.log(`Answer: ${step.content[0].text}`);
        if (step.content[0].annotations) {
            for (const anno of step.content[0].annotations) {
                console.log(`Citation: ${anno.title} (${anno.uri})`);
            }
        }
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": "Who won Euro 2024?",
    "tools": [{"type": "google_search"}]
}'

# Response (showing grounding)
{
  "id": "int_grounded",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Who won Euro 2024?" }]
    },
    {
      "type": "google_search_call",
      "status": "done",
      "content": [{ "type": "text", "text": "UEFA Euro 2024 winner" }]
    },
    {
      "type": "google_search_result",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024..." 
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1.",
          "annotations": [
            {
              "start_index": 0,
              "end_index": 42,
              "uri": "https://vertexaisearch...",
              "title": "aljazeera.com"
            }
          ]
        }
      ]
    }
  ]
}
```

## फ़ंक्शन कॉल

फ़ंक्शन कॉल और नतीजों का स्ट्रक्चर भी, Steps स्कीमा के हिसाब से बदल गया है.

### `generateContent` का इस्तेमाल करने से पहले

`generateContent` में, जवाब, कैंडिडेट में फ़ंक्शन कॉल दिखाता है.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What's the weather in Boston?",
    config=types.GenerateContentConfig(tools=[weather_tool]),
)

function_call = response.candidates[0].content.parts[0].function_call
print(f"Requested tool: {function_call.name}")

result = "52°F and rain"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="What's the weather in Boston?")
            ],
        ),
        response.candidates[0].content,
        types.Content(
            role="user",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"result": result},
                )
            ],
        ),
    ],
    config=types.GenerateContentConfig(tools=[weather_tool]),
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let response = await client.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: "What's the weather in Boston?",
    config: { tools: [weatherTool] }
});

const functionCall = response.candidates[0].content.parts[0].functionCall;
console.log(`Requested tool: ${functionCall.name}`);

const result = "52°F and rain";

response = await client.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: [
        { role: 'user', parts: [{ text: "What's the weather in Boston?" }] },
        response.candidates[0].content,
        {
            role: 'user',
            parts: [{
                functionResponse: {
                    name: functionCall.name,
                    response: { result: result }
                }
            }]
        }
    ],
    config: { tools: [weatherTool] }
});
console.log(response.text);
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "What is the weather like in Boston, MA?"
        }]
    }],
    "tools": [{
        "functionDeclarations": [{
            "name": "get_weather",
            "description": "Get the current weather",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "location": {"type": "STRING"}
                },
                "required": ["location"]
            }
        }]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "functionCall": {
              "name": "get_weather",
              "args": { "location": "Boston, MA" }
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ]
}
```

### Interactions API का इस्तेमाल करने के बाद

टूल कॉल और नतीजे अब टाइमलाइन में अलग-अलग स्टेप हैं.

### Python

```
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets weather",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string"}
        },
    },
}

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's the weather in Boston?",
    tools=[weather_tool],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Executing {step.name} for {step.arguments}")

        result = "52°F and rain"

        interaction = client.interactions.create(
            model="gemini-3.5-flash",
            previous_interaction_id=interaction.id,
            input=[
                {
                    "type": "function_result",
                    "call_id": step.id,
                    "name": step.name,
                    "result": [{"type": "text", "text": result}],
                }
            ],
        )
        print(next_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: "function",
    name: "get_weather",
    description: "Get weather for a location",
    parameters: {
        type: "object",
        properties: {
            location: { type: "string" }
        },
        required: ["location"]
    }
};

const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: "What's the weather in Boston?",
    tools: [weatherTool]
});

for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Executing ${step.name} for ${JSON.stringify(step.arguments)}`);

        const result = "52°F and rain";

        const nextInteraction = await client.interactions.create({
            model: 'gemini-3.5-flash',
            previous_interaction_id: interaction.id,
            input: [
                {
                    type: 'function_result',
                    call_id: step.id,
                    name: step.name,
                    result: [{ type: 'text', text: result }]
                }
            ]
        });

        console.log(nextInteraction.output_text);
    }
}
```

### REST

```
# Initial Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": "What's the weather in Boston?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Get weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": { "type": "string" }
            },
            "required": ["location"]
        }
    }]
}'

# Response (requires action)
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        { "type": "text", "text": "What's the weather in Boston?" }
      ]
    },
    {
      "type": "function_call",
      "status": "waiting",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}

# Submit Tool Result Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "previous_interaction_id": "int_001",
    "input": {
        "type": "function_result",
        "call_id": "fc_1",
        "name": "get_weather",
        "result": [
            { "type": "text", "text": "52°F with rain" }
        ]
    }
}'

# Final Response
{
  "id": "int_002",
  "status": "completed",
  "steps": [
    {
      "type": "function_result",
      "call_id": "fc_1",
      "name": "get_weather",
      "result": [
        { "type": "text", "text": "52°F with rain" }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        { "type": "text", "text": "It's 52°F with rain in Boston." }
      ]
    }
  ]
}
```

## स्ट्रीमिंग

स्ट्रीमिंग में मुख्य अंतर यह है कि Interactions API, अनुरोध के मुख्य हिस्से में `"stream": true` के साथ एक ही एंडपॉइंट का इस्तेमाल करता है. वहीं, `generateContent` API के लिए, किसी खास एंडपॉइंट (`:streamGenerateContent`) को कॉल करना ज़रूरी था.

इसके अलावा, स्ट्रीमिंग इवेंट अब इंटरैक्शन लाइफ़साइकल की निगरानी करने और टाइमलाइन के साथ-साथ एक्ज़ीक्यूशन स्टेप को ट्रैक करने के लिए, खास टाइप का इस्तेमाल करते हैं.

### `generateContentStream` का इस्तेमाल करने से पहले

`generateContent` की मदद से, जवाब के चंक की स्ट्रीम का इस्तेमाल किया जाता है.

### Python

```
response = client.models.generate_content_stream(
    model="gemini-2.5-flash", contents="Tell me a story"
)
for chunk in response:
    print(chunk.text, end="")
```

### JavaScript

```
const responseStream = await client.models.generateContentStream({
    model: 'gemini-2.5-flash',
    contents: 'Tell me a story',
});
for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:streamGenerateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Tell me a story"
        }]
    }]
}'

# Response stream
event: content.start
data: {"event_type": "content.start", "index": 0, "content": {"type": "thought"}}
event: content.delta
data: {"event_type": "content.delta", "index": 0, "delta": {"type": "thought_summary", "text": "User wants an explanation."}}
event: content.stop
data: {"event_type": "content.stop", "index": 0}
event: content.start
data: {"event_type": "content.start", "index": 1, "content": {"type": "text"}}
event: content.delta
data: {"event_type": "content.delta", "index": 1, "delta": {"type": "text", "text": "Hello"}}
event: content.stop
data: {"event_type": "content.stop", "index": 1}
```

### Interactions API का इस्तेमाल करने के बाद

Interactions API में, स्ट्रीमिंग, Server-Sent Events (एसएसई) और खास डेल्टा टाइप का इस्तेमाल करती है, ताकि एक्ज़ीक्यूशन स्टेप को दिखाया जा सके.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Tell me a story",
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
    elif event.event_type == "interaction.completed":
        print(f"\n\n--- Stream Finished ---")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a story',
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.delta') {
        if (event.delta.type === 'text' && 'text' in event.delta) {
            process.stdout.write(event.delta.text);
        }
    } else if (event.event_type === 'interaction.completed') {
        console.log('\n\n--- Stream Finished ---');
    }
}
```

### REST

# एसएसई स्ट्रीम आउटपुट का उदाहरण
**event: interaction.created
data: {"type": "interaction.created", "interaction": {"id": "int\_xyz", "status": "created"}}
event: interaction.in\_progress
data: {"type": "interaction.in\_progress", "interaction": {"id": "int\_xyz", "status": "in\_progress"}}
event: step.start
data: {"type": "step.start", "index": 0, "step": {"type": "thought"}}
event: step.delta
data: {"type": "step.delta", "index": 0, "delta": {"type": "thought", "text": "User wants an explanation."}}
event: step.stop
data: {"type": "step.stop", "index": 0, "status": "done"}}
event: step.start
data: {"type": "step.start", "index": 1, "step": {"type": "model\_output"}}
event: step.delta
data: {"type": "step.delta", "index": 1, "delta": {"type": "text", "text": "Hello"}}
event: step.stop
data: {"type": "step.stop", "index": 1, "status": "done"}}
event: interaction.completed
data: {"type": "interaction.completed", "interaction": {"id": "int\_xyz", "status": "completed", "usage": {"prompt\_tokens": 10, "completion\_tokens": 5, "total\_tokens": 15}}}**
```

### स्ट्रीमिंग टूल और फ़ंक्शन कॉल

`generateContent` से `Interactions API` पर माइग्रेट करने के बाद, स्ट्रीम में टूल के काम करने के तरीके में काफ़ी बदलाव आया है. इससे, ज़्यादा बेहतर कंट्रोल और विज़िबिलिटी मिलती है.

#### `generateContent` का इस्तेमाल करने से पहले

`generateContent` की मदद से, स्ट्रीमिंग फ़ंक्शन कॉल एक ही चंक में पूरी तरह से आ जाते थे. आपको रीयल-टाइम में आर्ग्युमेंट जनरेट होते नहीं दिखते थे. इसलिए, हैंडलर सिर्फ़ `functionCall` ऑब्जेक्ट के पूरा होने की जांच करता था.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

stream = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents="What's the weather in Boston?",
    config=types.GenerateContentConfig(tools=[weather_tool]),
)

for chunk in stream:
    # Function calls arrived complete — no partial arguments
    if chunk.candidates[0].content.parts[0].function_call:
        fc = chunk.candidates[0].content.parts[0].function_call
        print(f"Call: {fc.name}({fc.args})")
    elif chunk.text:
        print(chunk.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.models.generateContentStream({
    model: 'gemini-2.5-flash',
    contents: "What's the weather in Boston?",
    config: { tools: [weatherTool] }
});

for await (const chunk of stream) {
    const part = chunk.candidates[0].content.parts[0];
    if (part.functionCall) {
        console.log(`Call: ${part.functionCall.name}(${JSON.stringify(part.functionCall.args)})`);
    } else if (part.text) {
        process.stdout.write(part.text);
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:streamGenerateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{"parts": [{"text": "What'\''s the weather in Boston?"}]}],
    "tools": [{"functionDeclarations": [{"name": "get_weather", "parameters": {"type": "OBJECT", "properties": {"location": {"type": "STRING"}}}}]}]
}'

# Response stream — function call arrives complete in one chunk
{"candidates": [{"content": {"parts": [{"functionCall": {"name": "get_weather", "args": {"location": "Boston, MA"}}}]}}]}
```

#### Interactions API का इस्तेमाल करने के बाद

Interactions API, `arguments` इवेंट के तौर पर, फ़ंक्शन कॉल आर्ग्युमेंट को एक-एक वर्ण करके स्ट्रीम करता है. टूल का पूरा लाइफ़साइकल — थॉट, कॉल, नतीजा, और आउटपुट — अलग-अलग स्टेप की सीरीज़ के तौर पर दिखता है.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's the weather in Boston?",
    tools=[get_weather_tool],
    stream=True,
)

for event in stream:
    if event.event_type == "step.start":
        if event.step.type == "function_call":
            print(f"Calling: {event.step.name}")
    elif event.event_type == "step.delta":
        if event.delta.type == "arguments":
            print(f"  args: {event.delta.partial_arguments}")
        elif event.delta.type == "text":
            print(event.delta.text, end="")
    elif event.event_type == "interaction.completed":
        print("\n--- Done ---")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: "What's the weather in Boston?",
    tools: [getWeatherTool],
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.start') {
        if (event.step.type === 'function_call') {
            console.log(`Calling: ${event.step.name}`);
        }
    } else if (event.event_type === 'step.delta') {
        if (event.delta.type === 'arguments') {
            console.log(`  args: ${event.delta.partial_arguments}`);
        } else if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    } else if (event.event_type === 'interaction.completed') {
        console.log('\n--- Done ---');
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": "What'\''s the weather in Boston?",
    "tools": [{"type": "function", "name": "get_weather", "parameters": {"type": "object", "properties": {"location": {"type": "string"}}}}],
    "stream": true
}'

# Response stream
// Interaction created
event: interaction.created
data: {"type": "interaction.created", "interaction": {"id": "int_xyz", "status": "created"}}

event: interaction.in_progress
data: {"type": "interaction.in_progress", "interaction": {"id": "int_xyz", "status": "in_progress"}}

// ── Step 0: Thought ──────────────────────────────────
event: step.start
data: {"type": "step.start", "index": 0, "step": {"type": "thought"}}

event: step.delta
data: {"type": "step.delta", "index": 0, "delta": {"type": "thought", "text": "The user wants weather data for Boston. I'll call the get_weather tool."}}

event: step.stop
data: {"type": "step.stop", "index": 0, "status": "done"}

// ── Step 1: Function Call (arguments streamed) ───────
event: step.start
data: {"type": "step.start", "index": 1, "step": {"type": "function_call", "id": "fc_1", "name": "get_weather"}}

event: step.delta
data: {"type": "step.delta", "index": 1, "delta": {"type": "arguments", "partial_arguments": "{\"location\": \"Boston, MA\"}"}}

event: step.stop
data: {"type": "step.stop", "index": 1, "status": "waiting"}

// The interaction pauses — the model needs the tool result before continuing.
event: interaction.requires_action
data: {"type": "interaction.requires_action", "interaction": {"id": "int_xyz", "status": "requires_action"}}

// ── (Client submits the tool result) ──────────────────
// The client calls interactions.create with the function_result as input
// and the previous interaction's ID, then resumes consuming the stream.

event: interaction.in_progress
data: {"type": "interaction.in_progress", "interaction": {"id": "int_xyz", "status": "in_progress"}}

// ── Step 2: Function Result (echoed back, no deltas) ─
event: step.start
data: {"type": "step.start", "index": 2, "step": {"type": "function_result", "call_id": "fc_1", "name": "get_weather", "result": [{"type": "text", "text": "52°F, rain"}]}}

event: step.stop
data: {"type": "step.stop", "index": 2, "status": "done"}

// ── Step 3: Thought ──────────────────────────────────
event: step.start
data: {"type": "step.start", "index": 3, "step": {"type": "thought"}}

event: step.delta
data: {"type": "step.delta", "index": 3, "delta": {"type": "thought", "text": "Got weather data. Composing the final response."}}

event: step.stop
data: {"type": "step.stop", "index": 3, "status": "done"}

// ── Step 4: Model Output (text streamed) ─────────────
event: step.start
data: {"type": "step.start", "index": 4, "step": {"type": "model_output"}}

event: step.delta
data: {"type": "step.delta", "index": 4, "delta": {"type": "text", "text": "It's currently 52°F and rainy in Boston."}}

event: step.stop
data: {"type": "step.stop", "index": 4, "status": "done"}

// ── Interaction complete ─────────────────────────────
event: interaction.completed
data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 256, "completion_tokens": 128, "total_tokens": 384}}}
```

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया."],[],[]]
