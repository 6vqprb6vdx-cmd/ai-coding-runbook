---
source_url: https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar
fetched_at: 2026-05-11T12:36:38.684895+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# استدعاء الدوال باستخدام Gemini API

تتيح لكم ميزة استدعاء الدوال ربط النماذج بالأدوات وواجهات برمجة التطبيقات الخارجية.
بدلاً من إنشاء ردود نصية، يحدّد النموذج متى يجب استدعاء دوال معيّنة ويقدّم المَعلمات اللازمة لتنفيذ الإجراءات في العالم الحقيقي.
ويسمح ذلك للنموذج بأن يكون بمثابة جسر بين اللغة الطبيعية والإجراءات والبيانات في العالم الحقيقي. تتوفّر 3 حالات استخدام أساسية لميزة استدعاء الدوال:

- **تعزيز المعرفة:** يمكنكم الوصول إلى المعلومات من مصادر خارجية، مثل قواعد البيانات وواجهات برمجة التطبيقات وقواعد المعلومات.
- **توسيع الإمكانات:** يمكنكم استخدام الأدوات الخارجية لإجراء العمليات الحسابية وتوسيع نطاق قيود النموذج، مثل استخدام آلة حاسبة أو إنشاء رسوم بيانية.
- **اتخاذ الإجراءات:** يمكنكم التفاعل مع الأنظمة الخارجية باستخدام واجهات برمجة التطبيقات، مثل تحديد المواعيد أو إنشاء الفواتير أو إرسال الرسائل الإلكترونية أو التحكّم في أجهزة المنزل الذكي.

Get Weather
Schedule Meeting
Create Chart

### Python

```
from google import genai

schedule_meeting_function = {
    "type": "function",
    "name": "schedule_meeting",
    "description": "Schedules a meeting with specified attendees at a given time and date.",
    "parameters": {
        "type": "object",
        "properties": {
            "attendees": {"type": "array", "items": {"type": "string"}},
            "date": {"type": "string", "description": "Date (e.g., '2024-07-29')"},
            "time": {"type": "string", "description": "Time (e.g., '15:00')"},
            "topic": {"type": "string", "description": "The meeting topic."},
        },
        "required": ["attendees", "date", "time", "topic"],
    },
}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Schedule a meeting with Bob and Alice for 03/14/2025 at 10:00 AM about Q3 planning.",
    tools=[{"type": "function", **schedule_meeting_function}],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function to call: {step.name}")
        print(f"Arguments: {step.arguments}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const scheduleMeetingFunction = {
  type: 'function',
  name: 'schedule_meeting',
  description: 'Schedules a meeting with specified attendees at a given time and date.',
  parameters: {
    type: 'object',
    properties: {
      attendees: { type: 'array', items: { type: 'string' } },
      date: { type: 'string', description: 'Date (e.g., "2024-07-29")' },
      time: { type: 'string', description: 'Time (e.g., "15:00")' },
      topic: { type: 'string', description: 'The meeting topic.' },
    },
    required: ['attendees', 'date', 'time', 'topic'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: 'Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about Q3 planning.',
  tools: [scheduleMeetingFunction],
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`Function to call: ${step.name}`);
    console.log(`Arguments: ${JSON.stringify(step.arguments)}`);
  }
}
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about Q3 planning.",
    "tools": [{
        "type": "function",
        "name": "schedule_meeting",
        "description": "Schedules a meeting with specified attendees at a given time and date.",
        "parameters": {
          "type": "object",
          "properties": {
            "attendees": {"type": "array", "items": {"type": "string"}},
            "date": {"type": "string"},
            "time": {"type": "string"},
            "topic": {"type": "string"}
          },
          "required": ["attendees", "date", "time", "topic"]
        }
    }]
  }'
```

## آلية عمل ميزة استدعاء الدوال

![نظرة عامة على ميزة &quot;استدعاء الدالة&quot;](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=ar)

تتضمّن ميزة استدعاء الدوال تفاعلاً منظَّمًا بين تطبيقكم والنموذج والدوال الخارجية:

1. **تحديد بيان الدالة:** يمكنكم تحديد اسم الدالة ومَعلماتها والغرض منها للنموذج.
2. **استدعاء النموذج اللغوي الكبير باستخدام بيانات الدوال:** يمكنكم إرسال طلب المستخدم إلى النموذج مع بيانات الدوال.
3. **تنفيذ رمز الدالة (مسؤوليتكم):** لاينفّذ النموذج الدالة بنفسه. يمكنكم استخراج الاسم والوسيطات وتنفيذها في تطبيقكم.
4. **إنشاء ردّ سهل الاستخدام:** يمكنكم إرسال النتيجة إلى النموذج للحصول على ردّ نهائي سهل الاستخدام.

يمكن تكرار هذه العملية عدة مرات. يتيح النموذج استدعاء
دوال متعددة في دورة واحدة ([استدعاء الدوال بالتوازي](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar#parallel_function_calling)) وفي
تسلسل ([استدعاء الدوال التركيبي](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar#compositional_function_calling)).

### الخطوة 1: تحديد بيان دالة

### Python

```
set_light_values_declaration = {
    "type": "function",
    "name": "set_light_values",
    "description": "Sets the brightness and color temperature of a light.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "integer",
                "description": "Light level from 0 to 100",
            },
            "color_temp": {
                "type": "string",
                "enum": ["daylight", "cool", "warm"],
                "description": "Color temperature",
            },
        },
        "required": ["brightness", "color_temp"],
    },
}

def set_light_values(brightness: int, color_temp: str) -> dict:
    """Set the brightness and color temperature of a room light."""
    return {"brightness": brightness, "colorTemperature": color_temp}
```

### JavaScript

```
const setLightValuesTool = {
  type: 'function',
  name: 'set_light_values',
  description: 'Sets the brightness and color temperature of a light.',
  parameters: {
    type: 'object',
    properties: {
      brightness: { type: 'number', description: 'Light level from 0 to 100' },
      color_temp: { type: 'string', enum: ['daylight', 'cool', 'warm'] },
    },
    required: ['brightness', 'color_temp'],
  },
};

function setLightValues(brightness, color_temp) {
  return { brightness: brightness, colorTemperature: color_temp };
}
```

### الخطوة 2: استدعاء النموذج باستخدام بيانات الدوال

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Turn the lights down to a romantic level",
    tools=[set_light_values_declaration],
)

# Find the function call step
fc_step = next(s for s in interaction.steps if s.type == "function_call")
print(fc_step)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: 'Turn the lights down to a romantic level',
  tools: [setLightValuesTool],
});

// Find the function call step
const fcStep = interaction.steps.find(s => s.type === 'function_call');
console.log(fcStep);
```

يعرض النموذج خطوة `function_call` تتضمّن `type` و`name` و`arguments`:

```
type='function_call'
name='set_light_values'
arguments={'color_temp': 'warm', 'brightness': 25}
```

### الخطوة 3: تنفيذ الدالة

### Python

```
fc_step = next(s for s in interaction.steps if s.type == "function_call")

if fc_step.name == "set_light_values":
    result = set_light_values(**fc_step.arguments)
    print(f"Function execution result: {result}")
```

### JavaScript

```
const fcStep = interaction.steps.find(s => s.type === 'function_call');

let result;
if (fcStep.name === 'set_light_values') {
  result = setLightValues(fcStep.arguments.brightness, fcStep.arguments.color_temp);
  console.log(`Function execution result: ${JSON.stringify(result)}`);
}
```

### الخطوة 4: إرسال النتيجة إلى النموذج

### Python

```
final_interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {
            "type": "function_result",
            "name": fc_step.name,
            "call_id": fc_step.id,
            "result": [{"type": "text", "text": json.dumps(result)}],
        }
    ],
    tools=[set_light_values_declaration],
    previous_interaction_id=interaction.id,
)

print(final_interaction.steps[-1].content[0].text)
```

### JavaScript

```
const finalInteraction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: [{
    type: 'function_result',
    name: fcStep.name,
    call_id: fcStep.id,
    result: [{ type: 'text', text: JSON.stringify(result) }]
  }],
  tools: [setLightValuesTool],
  previous_interaction_id: interaction.id,
});

console.log(finalInteraction.steps.at(-1).content[0].text);
```

## بيانات الدوال

يتم تمرير بيان الدالة كأداة ويتضمّن ما يلي:

- `type` (سلسلة): يجب أن يكون `"function"` للدوال المخصّصة.
- `name` (سلسلة): اسم دالة فريد (يجب استخدام الشرطات السفلية أو التنسيق camelCase).
- `description` (سلسلة): شرح واضح للغرض من الدالة.
- `parameters` (كائن): مَعلمات الإدخال التي تتوقّعها الدالة.
  - `type` (سلسلة): نوع البيانات العام، مثل `object`.
  - `properties` (كائن): مَعلمات فردية تتضمّن النوع والوصف.
  - `required` (صفيف): أسماء المَعلمات الإلزامية.

## استدعاء الدوال باستخدام النماذج المفكّرة

تستخدم نماذج Gemini 3 و2.5 سلسلة عملية ["تفكير"](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=ar) داخلية تعمل على تحسين ميزة استدعاء الدوال.
تتعامل حِزم تطوير البرامج (SDK) تلقائيًا مع [توقيعات الأفكار](https://ai.google.dev/gemini-api/docs/interactions/thought-signatures?hl=ar) نيابةً عنكم.

## استدعاء الدوال بالتوازي

يمكنكم استدعاء دوال متعددة في الوقت نفسه عندما تكون مستقلة:

### Python

```
power_disco_ball = {"type": "function", "name": "power_disco_ball", "description": "Powers the disco ball.",
    "parameters": {"type": "object", "properties": {"power": {"type": "boolean"}}, "required": ["power"]}}
start_music = {"type": "function", "name": "start_music", "description": "Play music.",
    "parameters": {"type": "object", "properties": {"energetic": {"type": "boolean"}, "loud": {"type": "boolean"}}, "required": ["energetic", "loud"]}}
dim_lights = {"type": "function", "name": "dim_lights", "description": "Dim the lights.",
    "parameters": {"type": "object", "properties": {"brightness": {"type": "number"}}, "required": ["brightness"]}}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Turn this place into a party!",
    tools=[power_disco_ball, start_music, dim_lights],
    generation_config={"tool_choice": "any"},
)

for step in interaction.steps:
    if step.type == "function_call":
        args = ", ".join(f"{key}={val}" for key, val in step.arguments.items())
        print(f"{step.name}({args})")
```

### JavaScript

```
const powerDiscoBall = { type: 'function', name: 'power_disco_ball', description: 'Powers the disco ball.',
  parameters: { type: 'object', properties: { power: { type: 'boolean' } }, required: ['power'] } };
const startMusic = { type: 'function', name: 'start_music', description: 'Play music.',
  parameters: { type: 'object', properties: { energetic: { type: 'boolean' }, loud: { type: 'boolean' } }, required: ['energetic', 'loud'] } };
const dimLights = { type: 'function', name: 'dim_lights', description: 'Dim the lights.',
  parameters: { type: 'object', properties: { brightness: { type: 'number' } }, required: ['brightness'] } };

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: 'Turn this place into a party!',
  tools: [powerDiscoBall, startMusic, dimLights],
  generation_config: { tool_choice: 'any' },
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`${step.name}(${JSON.stringify(step.arguments)})`);
  }
}
```

## استدعاء الدوال التركيبي

يمكنكم ربط عمليات استدعاء دوال متعددة معًا للطلبات المعقّدة (مثل الحصول على الموقع الجغرافي أولاً، ثم الحصول على حالة الطقس لهذا الموقع الجغرافي).

### Python

```
get_weather_forecast_declaration = {
    "type": "function",
    "name": "get_weather_forecast",
    "description": "Gets the current weather temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The location"},
        },
        "required": ["location"],
    },
}

set_thermostat_temperature_declaration = {
    "type": "function",
    "name": "set_thermostat_temperature",
    "description": "Sets the thermostat to a desired temperature.",
    "parameters": {
        "type": "object",
        "properties": {
            "temperature": {
                "type": "integer",
                "description": "The temperature in Celsius",
            },
        },
        "required": ["temperature"],
    },
}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise 18°C.",
    tools=[
        get_weather_forecast_declaration,
        set_thermostat_temperature_declaration,
    ],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function to call: {step.name}")
        print(f"Arguments: {step.arguments}")
    elif hasattr(step, "content") and step.content:
         for part in step.content:
             if hasattr(part, "text"):
                 print(part.text)
```

## أوضاع استدعاء الدوال

يمكنكم التحكّم في كيفية استخدام النموذج للأدوات باستخدام `tool_choice` في `generation_config`:

- `auto` (الإعداد التلقائي): يقرّر النموذج ما إذا كان سيستدعي دالة أو سيردّ مباشرةً.
- `any`: يقتصر النموذج على توقُّع استدعاء دالة دائمًا.
- `none`: `لا شيء`: يُمنع النموذج من إجراء عمليات استدعاء الدوال.
- `validated` (معاينة): يضمن النموذج الالتزام بمخطط الدالة.

### Python

```
generation_config = {
    "tool_choice": {
        "allowed_tools": {
            "mode": "any",
            "tools": ["get_current_temperature"]
        }
    }
}
```

### JavaScript

```
const generation_config = {
  tool_choice: {
    allowed_tools: {
      mode: 'any',
      tools: ['get_current_temperature']
    }
  }
};
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the temperature in Boston?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string"}
        },
        "required": ["location"]
      }
    }],
    "generation_config": {
      "tool_choice": {
        "allowed_tools": {
          "mode": "any",
          "tools": ["get_current_temperature"]
        }
      }
    }
  }'
```

## استخدام أدوات متعددة

يمكنكم تفعيل أدوات متعددة، والجمع بين الأدوات المضمّنة واستدعاء الدوال في الطلب نفسه. يمكن لنماذج Gemini 3 الجمع بين الأدوات المضمّنة واستدعاء الدوال خارج نطاق التفاعل في Interactions. يؤدي تمرير `previous_interaction_id` إلى تداول سياق الأداة المضمّنة تلقائيًا.

### Python

```
from google import genai
import json

client = genai.Client()

get_weather = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

tools = [
    {"type": "google_search"},  # Built-in tool
    get_weather                 # Custom tool
]

# Turn 1: Initial request with both tools enabled
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=tools
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} (ID: {step.id})")
        # Execute your custom function locally
        result = {"response": "Very cold. 22 degrees Fahrenheit."}
        # Turn 2: Provide the function result back to the model.
        # Passing `previous_interaction_id` automatically circulates the
        # built-in Google Search context from Turn 1
        interaction_2 = client.interactions.create(
            model="gemini-3-flash-preview",
            previous_interaction_id=interaction.id,
            tools=tools,
            input=[{
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}]
            }]
        )

        print(interaction_2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: 'function',
    name: 'get_weather',
    description: 'Gets the weather for a given location.',
    parameters: {
        type: 'object',
        properties: {
            location: { type: 'string', description: 'The city and state, e.g. San Francisco, CA' }
        },
        required: ['location']
    }
};

const tools = [
    {type: 'google_search'}, // Built-in tool
    weatherTool              // Custom tool
];

// Turn 1: Initial request with both tools enabled
let interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: tools
});

for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Function call: ${step.name} (ID: ${step.id})`);
        // Execute your custom function locally
        const result = {response: "Very cold. 22 degrees Fahrenheit."};
        // Turn 2: Provide the function result back to the model.
        const interaction_2 = await client.interactions.create({
            model: 'gemini-3-flash-preview',
            previous_interaction_id: interaction.id,
            tools: tools,
            input: [{
                type: 'function_result',
                name: step.name,
                call_id: step.id,
                result: [{ type: 'text', text: JSON.stringify(result) }]
            }]
        });

        console.log(interaction_2.steps.at(-1).content[0].text);
    }
}
```

## ردود الدوال المتعددة الوسائط

بالنسبة إلى نماذج Gemini 3 سلسلة، يمكنكم تضمين محتوى متعدد الوسائط في أجزاء ردّ الدالة التي ترسلونها إلى النموذج. يمكن للنموذج معالجة هذا المحتوى المتعدد الوسائط في دورته التالية لإنتاج ردّ أكثر استنارة.

لتضمين بيانات متعددة الوسائط في ردّ دالة، يمكنكم تضمينها ككتلة محتوى واحدة أو أكثر في حقل `result` لخطوة `function_result`. يجب أن تحدّد كل كتلة محتوى `type` (مثل `"text"` أو `"image"`).

يوضّح المثال التالي كيفية إرسال ردّ دالة يحتوي على بيانات صورة إلى النموذج في تفاعل:

### Python

```
import base64
from google import genai
import requests

client = genai.Client()

# Find the function call step
tool_call = next(s for s in interaction.steps if s.type == "function_call")

# Execute your tool to get image bytes
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content

base64_image_data = base64.b64encode(image_bytes).decode("utf-8")

final_interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction.id,
    input=[
        {
            "type": "function_result",
            "name": tool_call.name,
            "call_id": tool_call.id,
            "result": [
                {"type": "text", "text": "instrument.jpg"},
                {
                    "type": "image",
                    "mime_type": "image/jpeg",
                    "data": base64_image_data,
                },
            ],
        }
    ],
)

print(final_interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Find the function call step
const toolCall = interaction.steps.find(s => s.type === 'function_call');

// Execute your tool to get image bytes and convert to base64
// (Implementation depends on your environment)
const base64ImageData = "BASE64_IMAGE_DATA";

const finalInteraction = await ai.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction.id,
    input: [{
        type: 'function_result',
        name: toolCall.name,
        call_id: toolCall.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }]
});

console.log(finalInteraction.steps.at(-1).content[0].text);
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [
      {
        "type": "function_result",
        "name": "get_image",
        "call_id": "call_123",
        "result": [
          {"type": "text", "text": "instrument.jpg"},
          {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": "BASE64_IMAGE_DATA"
          }
        ]
      }
    ]
  }'
```

## استدعاء الدوال باستخدام الناتج المنظَّم

بالنسبة إلى نماذج Gemini 3 سلسلة، يمكنكم الجمع بين استدعاء الدوال و
[الناتج المنظَّم](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=ar) للحصول على
ردود منسّقة باستمرار.

## بروتوكول سياق النموذج (MCP) عن بُعد

تتيح واجهة برمجة التطبيقات Interactions API الاتصال بخوادم MCP عن بُعد لمنح النموذج إمكانية الوصول إلى الأدوات والخدمات الخارجية. يمكنكم تقديم `name` و`url` للخادم في إعداد الأدوات.

عند استخدام بروتوكول MCP عن بُعد، يُرجى مراعاة القيود التالية:

- **أنواع الخوادم**: لا يعمل بروتوكول MCP عن بُعد إلا مع خوادم HTTP القابلة للبث. لا تتوافق هذه الميزة مع خوادم SSE (أحداث Server-Sent Events).
- **دعم النموذج**: لا يعمل بروتوكول MCP عن بُعد مع نماذج Gemini 3 في الوقت الحالي. سيتوفّر دعم نماذج Gemini 3 قريبًا.
- **التسمية**: يجب ألا تتضمّن أسماء خوادم MCP الرمز `-`. يُرجى استخدام أسماء خوادم `snake_case` بدلاً من ذلك.

| الحقل | النوع | مطلوب | الوصف |
| --- | --- | --- | --- |
| `type` | `string` | نعم | يجب أن يكون `"mcp_server"`. |
| `name` | `string` | لا | اسم العرض لخادم MCP |
| `url` | `string` | لا | عنوان URL الكامل لنقطة نهاية خادم MCP |
| `headers` | `object` | لا | أزواج المفتاح والقيمة التي يتم إرسالها كعناوين HTTP مع كل طلب إلى الخادم (مثل رموز المصادقة) |
| `allowed_tools` | `array` | لا | يمكنكم تقييد الأدوات التي يمكن للوكيل استدعاؤها من الخادم. |

### مثال

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-2.5-flash",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ]
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-2.5-flash',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ]
});
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-2.5-flash",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ]
}'
```

## بث عمليات استدعاء الأدوات

عند استخدام الأدوات مع البث، ينشئ النموذج عمليات استدعاء الدوال كسلسلة من أحداث `step.delta` على البث. يمكن بث وسيطات الأداة كوسيطات جزئية باستخدام `arguments`. يجب تجميع هذه التغييرات الجزئية لإعادة إنشاء عمليات استدعاء الأدوات الكاملة قبل تنفيذها.

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The city and state"}
        },
        "required": ["location"]
    }
}

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the weather in Paris?",
    tools=[weather_tool],
    stream=True
)

current_calls = {}
tool_calls = []

for event in stream:
    if event.event_type == "step.start":
        if event.step.type == "function_call":
            current_calls[event.index] = {
                "id": event.step.id,
                "name": event.step.name,
                "arguments": ""
            }
            # Handle arguments provided in step.start
            if hasattr(event.step, "arguments") and event.step.arguments:
                if isinstance(event.step.arguments, dict):
                    current_calls[event.index]["arguments"] = json.dumps(event.step.arguments)
                else:
                    current_calls[event.index]["arguments"] = event.step.arguments
    elif event.event_type == "step.delta":
        if event.delta.type == "arguments":
            if event.index in current_calls:
                current_calls[event.index]["arguments"] += event.delta.partial_arguments
        elif event.delta.type == "text":
            print(event.delta.text, end="", flush=True)

    elif event.event_type == "interaction.completed":
        for index, call in current_calls.items():
            args = call["arguments"]
            if args:
                args = json.loads(args)
            else:
                args = {}

            tool_calls.append({
                "type": "function_call",
                "id": call["id"],
                "name": call["name"],
                "arguments": args
            })

        print(f"\nFinal tool calls ready to execute:")
        print(json.dumps(tool_calls, indent=2))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: 'function',
    name: 'get_weather',
    description: 'Gets the weather for a given location.',
    parameters: {
        type: 'object',
        properties: {
            location: { type: 'string', description: 'The city and state' }
        },
        required: ['location']
    }
};

const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'What is the weather in Paris?',
    tools: [weatherTool],
    stream: true,
});

const currentCalls = new Map();
let toolCalls = [];

for await (const event of stream) {
    const evType = event.event_type;
    if (evType === 'step.start') {
        if (event.step.type === 'function_call') {
            currentCalls.set(event.index, {
                id: event.step.id,
                name: event.step.name,
                arguments: ''
            });
            // Handle arguments provided in step.start
            if (event.step.arguments) {
                if (typeof event.step.arguments === 'object') {
                    currentCalls.get(event.index).arguments = JSON.stringify(event.step.arguments);
                } else {
                    currentCalls.get(event.index).arguments = event.step.arguments;
                }
            }
        }
    } else if (evType === 'step.delta') {
        if (event.delta.type === 'arguments') {
            if (currentCalls.has(event.index)) {
                currentCalls.get(event.index).arguments += event.delta.partial_arguments;
            }
        } else if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    } else if (evType === 'interaction.completed' || evType === 'interaction.complete') {
        toolCalls = Array.from(currentCalls.values()).map(call => ({
            type: 'function_call',
            id: call.id,
            name: call.name,
            arguments: call.arguments ? JSON.parse(call.arguments) : {}
        }));
        console.log('\nFinal tool calls ready to execute:');
        console.log(JSON.stringify(toolCalls, null, 2));
    }
}
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the weather in Paris?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state"}
            },
            "required": ["location"]
        }
    }],
    "stream": true
}'
```

## أفضل الممارسات

- **أوصاف الدوال والمَعلمات:** يجب أن تكون واضحة ومحدَّدة.
- **التسمية:** يجب استخدام أسماء وصفية بدون مسافات أو رموز خاصة.
- **الكتابة القوية:** يجب استخدام أنواع محدَّدة (عدد صحيح أو سلسلة أو تعداد).
- **اختيار الأدوات:** يجب أن يكون الحد الأقصى للأدوات النشطة من 10 إلى 20 أداة.
- **هندسة الطلبات:** يجب تقديم السياق والتعليمات.
- **التحقّق:** يجب التحقّق من عمليات استدعاء الدوال قبل تنفيذها.
- **معالجة الأخطاء:** يجب اتخاذ إجراءات فعالة لمعالجة الأخطاء.
- **الأمان:** يجب استخدام طريقة مصادقة مناسبة لواجهات برمجة التطبيقات الخارجية.

## الملاحظات والقيود

- [لا تتوافق هذه الميزة إلا مع مجموعة فرعية من مخطط OpenAPI.](https://ai.google.dev/api/rest/v1beta/cachedContents?hl=ar#FunctionDeclaration)
- بالنسبة إلى الوضع `any`، قد ترفض واجهة برمجة التطبيقات المخططات الكبيرة جدًا أو المتداخلة بعمق.
- تقتصر أنواع المَعلمات المتوافقة في Python.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-09 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-09 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
