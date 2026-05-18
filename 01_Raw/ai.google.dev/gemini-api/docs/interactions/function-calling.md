---
source_url: https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=hi
fetched_at: 2026-05-18T13:11:04.881806+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini API के साथ फ़ंक्शन कॉल करने की सुविधा

फ़ंक्शन कॉल करने की सुविधा की मदद से, मॉडल को बाहरी टूल और एपीआई से कनेक्ट किया जा सकता है.
मॉडल, टेक्स्ट में जवाब जनरेट करने के बजाय, यह तय करता है कि किन फ़ंक्शन को कॉल करना है. साथ ही, असल दुनिया में होने वाली कार्रवाइयों को पूरा करने के लिए ज़रूरी पैरामीटर उपलब्ध कराता है.
इससे मॉडल, नैचुरल लैंग्वेज और असल दुनिया में होने वाली कार्रवाइयों और डेटा के बीच पुल की तरह काम करता है. फ़ंक्शन कॉल करने की सुविधा को तीन मुख्य तरीकों से इस्तेमाल किया जा सकता है:

- **जानकारी बढ़ाना:** डेटाबेस, एपीआई, और नॉलेज बेस जैसे बाहरी सोर्स से जानकारी ऐक्सेस करना.
- **क्षमताएं बढ़ाना:** कैलकुलेशन करने के लिए, बाहरी टूल का इस्तेमाल करना. साथ ही, मॉडल की सीमाओं को बढ़ाना. जैसे, कैलकुलेटर का इस्तेमाल करना या चार्ट बनाना.
- **कार्रवाई करना:** एपीआई का इस्तेमाल करके, बाहरी सिस्टम से इंटरैक्ट करना. जैसे, अपॉइंटमेंट शेड्यूल करना, इनवॉइस बनाना, ईमेल भेजना या स्मार्ट होम डिवाइसों को कंट्रोल करना.

मौसम की जानकारी पाना
मीटिंग शेड्यूल करना
चार्ट बनाना

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
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

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
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

फ़ंक्शन कॉल करने की सुविधा के इंटरैक्शन को स्ट्रीम किया जा सकता है, ताकि टूल कॉल के चरण, धीरे-धीरे मिलते रहें. टूल के साथ स्ट्रीमिंग के बारे में ज़्यादा जानने के लिए, [स्ट्रीमिंग इंटरैक्शन](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=hi#streaming-with-tools) की गाइड देखें. इसमें `arguments` डेल्टा को इकट्ठा करने और `function_call` चरणों को मैनेज करने का तरीका भी शामिल है.

## फ़ंक्शन कॉल करने की सुविधा कैसे काम करती है

![फ़ंक्शन कॉल करने की सुविधा के बारे में खास जानकारी](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=hi)

फ़ंक्शन कॉल करने की सुविधा में, आपके ऐप्लिकेशन, मॉडल, और बाहरी फ़ंक्शन के बीच स्ट्रक्चर्ड इंटरैक्शन शामिल होता है:

1. **फ़ंक्शन के एलान की जानकारी देना:** मॉडल को फ़ंक्शन का नाम, पैरामीटर, और मकसद बताना.
2. **फ़ंक्शन के एलान की जानकारी के साथ एलएलएम को कॉल करना:** मॉडल को, उपयोगकर्ता का प्रॉम्प्ट और फ़ंक्शन के एलान की जानकारी भेजना.
3. **फ़ंक्शन का कोड एक्ज़ीक्यूट करना (यह आपकी ज़िम्मेदारी है):** मॉडल, फ़ंक्शन को *खुद*
   एक्ज़ीक्यूट नहीं करता. नाम और आर्ग्युमेंट एक्सट्रैक्ट करें और अपने ऐप्लिकेशन में एक्ज़ीक्यूट करें.
4. **उपयोगकर्ता के लिए आसान जवाब बनाना:** मॉडल को, नतीजा वापस भेजें, ताकि वह उपयोगकर्ता के लिए आसान जवाब दे सके.

इस प्रोसेस को कई बार दोहराया जा सकता है. मॉडल, एक ही बार में कई फ़ंक्शन को कॉल कर सकता है. इसे [पैरलल फ़ंक्शन कॉल करना](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=hi#parallel_function_calling) कहते हैं. साथ ही, मॉडल एक के बाद एक फ़ंक्शन को भी कॉल कर सकता है. इसे [कंपोज़िशनल फ़ंक्शन कॉल करना](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=hi#compositional_function_calling) कहते हैं.

### पहला चरण: फ़ंक्शन के एलान की जानकारी देना

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
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

### दूसरा चरण: फ़ंक्शन के एलान की जानकारी के साथ मॉडल को कॉल करना

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
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

मॉडल, `type`, `name`, और `arguments` के साथ `function_call` चरण दिखाता है:

```
type='function_call'
name='set_light_values'
arguments={'color_temp': 'warm', 'brightness': 25}
```

### तीसरा चरण: फ़ंक्शन को एक्ज़ीक्यूट करना

### Python

```
# This will only work for SDK newer than 2.0.0
fc_step = next(s for s in interaction.steps if s.type == "function_call")

if fc_step.name == "set_light_values":
    result = set_light_values(**fc_step.arguments)
    print(f"Function execution result: {result}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const fcStep = interaction.steps.find(s => s.type === 'function_call');

let result;
if (fcStep.name === 'set_light_values') {
  result = setLightValues(fcStep.arguments.brightness, fcStep.arguments.color_temp);
  console.log(`Function execution result: ${JSON.stringify(result)}`);
}
```

### चौथा चरण: मॉडल को नतीजा वापस भेजना

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
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

### स्टेटलेस फ़ंक्शन कॉल करना

क्लाइंट साइड पर बातचीत के इतिहास को मैनेज करके और `store=false` सेट करके, स्टेटलेस मोड में भी फ़ंक्शन कॉल करने की सुविधा का इस्तेमाल किया जा सकता है.

स्टेटलेस मोड में, आपको हर अगले अनुरोध के `input` फ़ील्ड में बातचीत का पूरा इतिहास पास करना होगा. इस इतिहास में ये चीज़ें शामिल होनी चाहिए: 1. `user_input` का शुरुआती चरण.
2. पहले राउंड में मॉडल से जनरेट किए गए सभी चरण. इनमें `thought` और `function_call` चरण शामिल हैं. ये चरण, ठीक उसी तरह शामिल होने चाहिए जैसे मिले थे.
3. `function_result` चरण. इसमें, आपके एक्ज़ीक्यूट किए गए फ़ंक्शन का आउटपुट शामिल होता है.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import json

client = genai.Client()

# Initialize history with Turn 1 input
history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "Turn the lights down to a romantic level"}]
    }
]

# Turn 1: Call model with tools and store=False
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    store=False,
    input=history,
    tools=[set_light_values_declaration],
)

# Append all model-generated steps (including thoughts and function_calls)
for step in interaction.steps:
    history.append(step.model_dump())

# Find the function call step to execute it
fc_step = next(s for s in interaction.steps if s.type == "function_call")
if fc_step.name == "set_light_values":
    result = set_light_values(**fc_step.arguments)

# Append the function result as a step
history.append({
    "type": "function_result",
    "name": fc_step.name,
    "call_id": fc_step.id,
    "result": [{"type": "text", "text": json.dumps(result)}],
})

# Turn 2: Send the full history to get the final response
final_interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    store=False,
    input=history,
    tools=[set_light_values_declaration],
)

print(final_interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  // Initialize history with Turn 1 input
  const history = [
    {
      type: "user_input",
      content: [{ type: "text", text: "Turn the lights down to a romantic level" }]
    }
  ];

  // Turn 1: Call model with tools and store: false
  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    store: false,
    input: history,
    tools: [setLightValuesTool],
  });

  // Append all model-generated steps
  history.push(...interaction.steps);

  // Find and execute function
  const fcStep = interaction.steps.find(s => s.type === 'function_call');
  let result;
  if (fcStep.name === 'set_light_values') {
    result = setLightValues(fcStep.arguments.brightness, fcStep.arguments.color_temp);
  }

  // Append function result step
  history.push({
    type: 'function_result',
    name: fcStep.name,
    call_id: fcStep.id,
    result: [{ type: 'text', text: JSON.stringify(result) }]
  });

  // Turn 2: Send full history
  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    store: false,
    input: history,
    tools: [setLightValuesTool],
  });

  console.log(finalInteraction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# Turn 1: Send request with tools and store: false
# Specifies the API revision to avoid breaking changes when they become default
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": [{"type": "text", "text": "Turn the lights down to a romantic level"}]
      }
    ],
    "tools": [{
      "type": "function",
      "name": "set_light_values",
      "description": "Sets the brightness and color temperature of a light.",
      "parameters": {
        "type": "object",
        "properties": {
          "brightness": {"type": "integer", "description": "Light level from 0 to 100"},
          "color_temp": {"type": "string", "enum": ["daylight", "cool", "warm"]}
        },
        "required": ["brightness", "color_temp"]
      }
    }]
  }')

# Extract model steps (thought, function_call)
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Extract function call details to execute
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')

# Assume local execution returns: {"brightness": 25, "colorTemperature": "warm"}
RESULT="{\"brightness\": 25, \"colorTemperature\": \"warm\"}"

# Reconstruct history for Turn 2
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": [{"type": "text", "text": "Turn the lights down to a romantic level"}]}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d "{
    \"model\": \"gemini-3-flash-preview\",
    \"store\": false,
    \"input\": $HISTORY,
    \"tools\": [{
      \"type\": \"function\",
      \"name\": \"set_light_values\",
      \"description\": \"Sets the brightness and color temperature of a light.\",
      \"parameters\": {
        \"type\": \"object\",
        \"properties\": {
          \"brightness\": {\"type\": \"integer\"},
          \"color_temp\": {\"type\": \"string\"}
        },
        \"required\": [\"brightness\", \"color_temp\"]
      }
    }]
  }"
```

## फ़ंक्शन के एलान की जानकारी

फ़ंक्शन के एलान की जानकारी, टूल के तौर पर पास की जाती है. इसमें ये चीज़ें शामिल होती हैं:

- `type` (स्ट्रिंग): कस्टम फ़ंक्शन के लिए, इसकी वैल्यू `"function"` होनी चाहिए.
- `name` (स्ट्रिंग): फ़ंक्शन का यूनीक नाम. इसके लिए, अंडरस्कोर या कैमल केस का इस्तेमाल करें.
- `description` (स्ट्रिंग): फ़ंक्शन के मकसद की साफ़ तौर पर जानकारी.
- `parameters` (ऑब्जेक्ट): इनपुट पैरामीटर जिनकी ज़रूरत फ़ंक्शन को होती है.
  - `type` (स्ट्रिंग): डेटा का सामान्य टाइप. जैसे, `object`.
  - `properties` (ऑब्जेक्ट): टाइप और ब्यौरे के साथ अलग-अलग पैरामीटर.
  - `required` (ऐरे): ज़रूरी पैरामीटर के नाम.

## थिंकिंग मॉडल के साथ फ़ंक्शन कॉल करने की सुविधा

Gemini 3 और 2.5 सीरीज़ के मॉडल, इंटरनल ["थिंकिंग"](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=hi) प्रोसेस का इस्तेमाल करते हैं. इससे फ़ंक्शन कॉल करने की सुविधा बेहतर होती है.
एसडीके, [थॉट सिग्नेचर](https://ai.google.dev/gemini-api/docs/interactions/thought-signatures?hl=hi) को अपने-आप मैनेज करते हैं.

## पैरलल फ़ंक्शन कॉल करना

एक साथ कई फ़ंक्शन कॉल करें, जब वे एक-दूसरे पर निर्भर न हों:

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
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

## कंपोज़िशनल फ़ंक्शन कॉल करना

मुश्किल अनुरोधों के लिए, एक के बाद एक कई फ़ंक्शन कॉल करें. जैसे, पहले जगह की जानकारी पाएं, फिर उस जगह के मौसम की जानकारी पाएं.

### Python

```
# This will only work for SDK newer than 2.0.0
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

## फ़ंक्शन कॉल करने के मोड

`generation_config` में `tool_choice` का इस्तेमाल करके, कंट्रोल करें कि मॉडल, टूल का इस्तेमाल कैसे करता है:

- `auto` (डिफ़ॉल्ट): मॉडल तय करता है कि किसी फ़ंक्शन को कॉल करना है या सीधे जवाब देना है.
- `any`: मॉडल को हमेशा फ़ंक्शन कॉल का अनुमान लगाने के लिए मजबूर किया जाता है.
- `none`: मॉडल को फ़ंक्शन कॉल करने से रोका जाता है.
- `validated` (झलक): मॉडल, फ़ंक्शन स्कीमा के पालन को पक्का करता है.

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
const generation_config = {
  tool_choice: {
    allowed_tools: {
      mode: 'any',
      tools: ['get_current_temperature']
    }
  }
};
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
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

## एक से ज़्यादा टूल का इस्तेमाल करना

एक ही अनुरोध में, एक से ज़्यादा टूल चालू किए जा सकते हैं. इसके लिए, बिल्ट-इन टूल को फ़ंक्शन कॉल करने की सुविधा के साथ जोड़ा जा सकता है. Gemini 3 मॉडल, Interactions में बिल्ट-इन टूल को फ़ंक्शन कॉल करने की सुविधा के साथ जोड़ सकते हैं. `previous_interaction_id` पास करने पर, बिल्ट-इन टूल का कॉन्टेक्स्ट अपने-आप सर्कुलेट हो जाता है.

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
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

## मल्टीमॉडल फ़ंक्शन के जवाब

Gemini 3 सीरीज़ के मॉडल के लिए, फ़ंक्शन के जवाब के उन हिस्सों में मल्टीमॉडल कॉन्टेंट शामिल किया जा सकता है जिन्हें मॉडल को भेजा जाता है. मॉडल, अगले राउंड में इस मल्टीमॉडल कॉन्टेंट को प्रोसेस करके, ज़्यादा जानकारी वाला जवाब दे सकता है.

फ़ंक्शन के जवाब में मल्टीमॉडल डेटा शामिल करने के लिए, इसे `result` फ़ील्ड के `function_result` चरण में एक या उससे ज़्यादा कॉन्टेंट ब्लॉक के तौर पर शामिल करें. हर कॉन्टेंट ब्लॉक में, उसका `type` तय करना ज़रूरी है. जैसे, `"text"`, `"image"`.

यहां दिए गए उदाहरण में दिखाया गया है कि किसी इंटरैक्शन में, इमेज डेटा वाला फ़ंक्शन का जवाब मॉडल को कैसे भेजा जाता है:

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
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

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
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

## स्ट्रक्चर्ड आउटपुट के साथ फ़ंक्शन कॉल करने की सुविधा

Gemini 3 सीरीज़ के मॉडल के लिए, फ़ंक्शन कॉल करने की सुविधा को
[स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=hi) के साथ जोड़ें, ताकि
फ़ॉर्मैट किए गए जवाब मिल सकें.

## रिमोट एमसीपी (मॉडल कॉन्टेक्स्ट प्रोटोकॉल)

Interactions API, रिमोट एमसीपी सर्वर से कनेक्ट करने की सुविधा देता है, ताकि मॉडल को बाहरी टूल और सेवाओं का ऐक्सेस मिल सके. टूल के कॉन्फ़िगरेशन में, सर्वर का `name` और `url` डालें.

रिमोट एमसीपी का इस्तेमाल करते समय, इन बातों का ध्यान रखें:

- **सर्वर के टाइप**: रिमोट एमसीपी, सिर्फ़ स्ट्रीम किए जा सकने वाले एचटीटीपी सर्वर के साथ काम करता है. एसएसई (सर्वर-सेंट इवेंट) सर्वर काम नहीं करते.
- **मॉडल के साथ काम करने की सुविधा**: फ़िलहाल, रिमोट एमसीपी, Gemini 3 मॉडल के साथ काम नहीं करता. यह सुविधा, Gemini 3 के लिए जल्द ही उपलब्ध होगी.
- **नामकरण**: एमसीपी सर्वर के नामों में `-` वर्ण शामिल नहीं होना चाहिए. इसके बजाय, `snake_case` सर्वर के नामों का इस्तेमाल करें.

| फ़ील्ड | टाइप | ज़रूरी है | ब्यौरा |
| --- | --- | --- | --- |
| `type` | `string` | हां | इसकी वैल्यू `"mcp_server"` होनी चाहिए. |
| `name` | `string` | नहीं | एमसीपी सर्वर का डिसप्ले नेम. |
| `url` | `string` | नहीं | एमसीपी सर्वर के एंडपॉइंट का पूरा यूआरएल. |
| `headers` | `object` | नहीं | कुंजी-वैल्यू पेयर, जो सर्वर को हर अनुरोध के साथ एचटीटीपी हेडर के तौर पर भेजे जाते हैं. उदाहरण के लिए, पुष्टि करने वाले टोकन. |
| `allowed_tools` | `array` | नहीं | यह तय करें कि एजेंट, सर्वर के किन टूल को कॉल कर सकता है. |

### उदाहरण

### Python

```
# This will only work for SDK newer than 2.0.0
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
// This will only work for SDK newer than 2.0.0
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

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
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

## सबसे सही तरीके

- **फ़ंक्शन और पैरामीटर के ब्यौरे:** साफ़ और सटीक जानकारी दें.
- **नामकरण:** ऐसे नाम इस्तेमाल करें जिनसे फ़ंक्शन के बारे में पता चलता हो. साथ ही, उनमें स्पेस या खास वर्ण शामिल न करें.
- **टाइप तय करना:** खास टाइप (इंटीजर, स्ट्रिंग, एनम) का इस्तेमाल करें.
- **टूल चुनना:** ज़्यादा से ज़्यादा 10 से 20 टूल चालू रखें.
- **प्रॉम्प्ट इंजीनियरिंग:** कॉन्टेक्स्ट और निर्देश दें.
- **पुष्टि करना:** फ़ंक्शन कॉल को एक्ज़ीक्यूट करने से पहले, उनकी पुष्टि करें.
- **गड़बड़ी ठीक करना:** गड़बड़ी ठीक करने की मज़बूत सुविधा लागू करें.
- **सुरक्षा:** बाहरी एपीआई के लिए, पुष्टि करने का सही तरीका इस्तेमाल करें.

## ध्यान देने वाली बातें और सीमाएं

- OpenAPI स्कीमा का सिर्फ़ [सबसेट](https://ai.google.dev/api/rest/v1beta/cachedContents?hl=hi#FunctionDeclaration) काम करता है.
- `any` मोड के लिए, एपीआई बहुत बड़े या डीपली नेस्टेड स्कीमा को अस्वीकार कर सकता है.
- Python में, पैरामीटर के सीमित टाइप काम करते हैं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-16 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-16 (UTC) को अपडेट किया गया."],[],[]]
