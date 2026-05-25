---
source_url: https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=hi
fetched_at: 2026-05-25T13:01:13.895209+00:00
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

# स्ट्रीमिंग इंटरैक्शन

इंटरैक्शन बनाते समय, `stream: true` सेट किया जा सकता है. इससे, [सर्वर-सेंट इवेंट](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) (एसएसई) का इस्तेमाल करके, जवाब को धीरे-धीरे स्ट्रीम किया जा सकता है.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Count to from 1 to 25.",
    stream=True,
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Count to from 1 to 25.",
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Count to from 1 to 25.",
    "stream": true
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"1, 2, 3, 4, 5, 6, ","type":"text"},"event_type":"step.delta"}

event: step.delta
data: {"index":1,"delta":{"text":"7, 8, 9, 10, 11, 12, 13,","type":"text"},"event_type":"step.delta"}

...

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_...","status":"completed","usage":{"total_tokens":346,"total_input_tokens":11,"input_tokens_by_modality":[{"modality":"text","tokens":11}],"total_cached_tokens":0,"total_output_tokens":90,"total_tool_use_tokens":0,"total_thought_tokens":245},"created":"2026-05-12T18:44:51Z","updated":"2026-05-12T18:44:51Z","service_tier":"standard","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## इवेंट किस तरह के हैं

सर्वर-सेंट हर इवेंट में, `event_type` नाम और उससे जुड़ा JSON डेटा शामिल होता है. Interactions API, सिमेट्रिक स्ट्रीमिंग मॉडल का इस्तेमाल करता है. इसमें, सभी कॉन्टेंट—टेक्स्ट, टूल कॉल, थिंकिंग—**चरण-आधारित** एक जैसे इवेंट के ज़रिए फ़्लो होता है.

हर स्ट्रीम, इस इवेंट फ़्लो को फ़ॉलो करती है:

1. `interaction.created`: इंटरैक्शन बनाया जाता है. इसमें मेटाडेटा (आईडी, मॉडल, स्टेटस) शामिल होता है.
2. **चरणों** की सीरीज़. हर चरण में ये चीज़ें शामिल होती हैं:
   - `step.start` इवेंट. यह इवेंट के टाइप (जैसे, `model_output`, `thought`, `function_call`) की जानकारी देता है.
   - `step.delta` एक या उससे ज़्यादा इवेंट. इनमें उस चरण के लिए, धीरे-धीरे मिलने वाला डेटा शामिल होता है.
   - `step.stop` इवेंट. यह इवेंट, चरण के पूरा होने की जानकारी देता है.
3. `interaction.completed` इवेंट. इसमें `usage` के फ़ाइनल आंकड़े शामिल होते हैं.

`stream: false` सेट करने पर, एपीआई `steps` कलेक्शन के साथ एक `interaction` ऑब्जेक्ट दिखाता है. `steps` में मौजूद हर एलिमेंट, `step.start` → `step.delta`(s) → `step.stop` साइकल का पूरी तरह से असेंबल किया गया वर्शन होता है.

### `interaction.created`

यह इवेंट तब भेजा जाता है, जब इंटरैक्शन पहली बार बनाया जाता है. इसमें इंटरैक्शन आईडी, मॉडल, और शुरुआती स्टेटस शामिल होता है.

```
event: interaction.created
data: {"interaction": {"id": "...", "model": "gemini-3-flash-preview", "status": "in_progress", "object": "interaction"}, "event_type": "interaction.created"}
```

### `interaction.status_update`

यह इवेंट, इंटरैक्शन-लेवल के स्टेटस में बदलाव का सिग्नल देता है. यह इवेंट, चरणों के बीच दिख सकता है.

```
event: interaction.status_update
data: {"interaction_id": "...", "status": "in_progress", "event_type": "interaction.status_update"}
```

### `step.start`

यह इवेंट, नए चरण की शुरुआत की जानकारी देता है. इसमें चरण का `type` और `index` शामिल होता है. चरण का टाइप तय करता है कि किस तरह के डेल्टा टाइप की उम्मीद की जानी चाहिए और स्ट्रीमिंग के बिना जवाब में चरण कैसे दिखता है:

| चरण का टाइप | डेल्टा के संभावित टाइप | ब्यौरा |
| --- | --- | --- |
| `model_output` | `text`, `image`, `audio` | मॉडल के फ़ाइनल जवाब का कॉन्टेंट. |
| `thought` | `thought_signature`, `thought_summary` | चेन-ऑफ़-थॉट रीज़निंग. `summary` सिर्फ़ तब मौजूद होता है, जब `thinking_summaries` की सुविधा चालू हो. |
| `function_call` | `arguments_delta` | क्लाइंट से किसी फ़ंक्शन को चलाने का अनुरोध. इंटरैक्शन का स्टेटस `requires_action` पर सेट करता है. |
| सर्वर-साइड टूल | टूल के हिसाब से अलग-अलग होता है | एपीआई से चलाए जाने वाले टूल. जैसे, `google_search_call`, `google_search_result`, `code_execution_call`, `code_execution_result`. |

पूरी सूची देखने के लिए, [Interactions API का रेफ़रंस](https://ai.google.dev/api/interactions?hl=hi) देखें.

```
event: step.start
data: {"index": 0, "step": {"type": "model_output"}, "event_type": "step.start"}
```

फ़ंक्शन कॉल के लिए, चरण में फ़ंक्शन का नाम, आईडी, और खाली आर्ग्युमेंट `{}` शामिल होते हैं

```
event: step.start
data: {"index": 0, "step": {"type": "function_call", "id":"un6k8t18", "name": "get_weather", "arguments":{}}, "event_type": "step.start"}
```

### `step.delta`

मौजूदा चरण के लिए, धीरे-धीरे मिलने वाला डेटा. `delta` ऑब्जेक्ट में एक `type` फ़ील्ड होता है. इससे, इसके आकार का पता चलता है.

**उदाहरण:**

**`text`:** `model_output` चरण से मिलने वाला, धीरे-धीरे टेक्स्ट टोकन:

```
event: step.delta
data: {"index": 0, "delta": {"type": "text", "text": "Hello, my name is Phil"}, "event_type": "step.delta"}

event: step.delta
data: {"index": 0, "delta": {"type": "text", "text": ", and I live in Germany." }, "event_type": "step.delta"}
```

**`image`:** `model_output` चरण से मिलने वाला, Base64 में एनकोड किया गया इमेज डेटा:

```
event: step.delta
data: {"index": 0, "delta": {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAoHBwgHBgoICAgLCg..."}, "event_type": "step.delta"}
```

**`thought_summary`:** `thought` चरण से मिलने वाला, थिंकिंग की खास जानकारी का कॉन्टेंट:

```
event: step.delta
data: {"index": 0, "delta": {"type": "thought_summary", "content": {"type": "text", "text": "I need to find the GCD..."}}, "event_type": "step.delta"}
```

**`arguments_delta`:** फ़ंक्शन कॉल के आर्ग्युमेंट के लिए (आंशिक) JSON स्ट्रिंग. इसे डेल्टा में इकट्ठा करना ज़रूरी है:

```
event: step.delta
data: {"index": 0, "delta": {"type": "arguments_delta", "arguments": "{\"location\": \"San Francisco, CA\"}"}, "event_type": "step.delta"}
```

ये डेल्टा के कुछ सबसे सामान्य टाइप हैं. डेल्टा के सभी टाइप की पूरी सूची देखने के लिए, [Interactions API का रेफ़रंस देखें](https://ai.google.dev/api/interactions?hl=hi).

### `step.stop`

यह इवेंट, चरण के खत्म होने की जानकारी देता है. इसमें चरण का `index` शामिल होता है.

```
event: step.stop
data: {"index": 0, "event_type": "step.stop"}
```

### `interaction.completed`

यह इवेंट तब भेजा जाता है, जब इंटरैक्शन पूरा हो जाता है. इसमें `usage` के आंकड़ों के साथ, फ़ाइनल इंटरैक्शन ऑब्जेक्ट शामिल होता है. स्ट्रीमिंग के बिना वाले मोड में, यह टॉप-लेवल का रिस्पॉन्स ऑब्जेक्ट होता है. जवाब में `steps` शामिल नहीं होते.

```
event: interaction.completed
data: {"interaction": {"id": "v1_abc123", "status": "completed", "usage": {"total_input_tokens": 7, "total_output_tokens": 12, "total_tokens": 19}}, "event_type": "interaction.completed"}
```

### `error`

यह इवेंट तब भेजा जाता है, जब इंटरैक्शन के दौरान कोई गड़बड़ी होती है. इसमें मैसेज और कोड के साथ, गड़बड़ी का ऑब्जेक्ट शामिल होता है.

```
event: error
data: {"error":{"message":"Deadline expired before operation could complete.","code":"gateway_timeout"},"event_type":"error"}
```

## टूल की मदद से स्ट्रीमिंग

Interactions API, एक ही अनुरोध में क्लाइंट-साइड टूल (फ़ंक्शन कॉलिंग) और सर्वर-साइड टूल (Google Search, कोड एक्ज़ीक्यूशन वगैरह), दोनों की मदद से स्ट्रीमिंग की सुविधा देता है. स्ट्रीमिंग के दौरान, टूल के इनवोकेशन, इवेंट स्ट्रीम में टाइप किए गए चरणों के तौर पर दिखते हैं. फ़ंक्शन कॉल के लिए, `step.start` इवेंट, फ़ंक्शन का नाम डिलीवर करता है. वहीं, `step.delta` इवेंट, आर्ग्युमेंट को JSON स्ट्रिंग (`arguments_delta`) के तौर पर स्ट्रीम करते हैं. पूरे आर्ग्युमेंट पाने के लिए, आपको इन डेल्टा को इकट्ठा करना होगा.
Google Search जैसे सर्वर-साइड टूल, एपीआई से अपने-आप चलते हैं. इससे, `google_search_call` और `google_search_result` चरण जनरेट होते हैं.

### फ़ंक्शन कॉलिंग की मदद से स्ट्रीमिंग

स्ट्रीमिंग के साथ फ़ंक्शन कॉलिंग करने के लिए, क्लाइंट को मल्टी-टर्न बातचीत को मैनेज करना होगा:

1. **पहला टर्न (फ़ंक्शन का अनुरोध):** `stream: true` और आपके तय किए गए `tools` के साथ, `interactions.create` को कॉल करें. एपीआई, `function_call` चरण को स्ट्रीम करेगा. `step.delta` इवेंट से, आर्ग्युमेंट की JSON स्ट्रिंग (`arguments_delta`) को तब तक इकट्ठा करें, जब तक इंटरैक्शन, `requires_action` स्टेटस के साथ पूरा न हो जाए.
2. **दूसरा टर्न (नतीजा भेजना):** `interactions.create` को फिर से कॉल करें. इसमें `previous_interaction_id` (पहले इंटरैक्शन के आईडी से मैच करने वाला) पास करें. साथ ही, `input` कलेक्शन में `function_result` ब्लॉक भेजें. इससे स्ट्रीम फिर से शुरू हो जाती है. इससे मॉडल को अपना फ़ाइनल जवाब जनरेट करने में मदद मिलती है.

### Python

```
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
            }
        },
        "required": ["location"]
    }
}

# Turn 1: Request function call
stream = client.interactions.create(
    model="gemini-3-flash-preview",
    tools=[weather_tool],
    input="What is the weather in Paris right now?",
    stream=True,
)

first_interaction_id = None
func_call_id = None
func_call_name = None
func_args_accumulated = ""

for event in stream:
    if event.event_type == "interaction.created":
        first_interaction_id = event.interaction.id
    elif event.event_type == "step.start":
        step = event.step
        if step.type == "function_call":
            func_call_id = step.id
            func_call_name = step.name
    elif event.event_type == "step.delta":
        if event.delta.type == "arguments_delta":
            func_args_accumulated += event.delta.arguments

# Turn 2: Execute tool and send the result back to resume stream
if func_call_id:
    # Execute weather_tool using accumulated arguments
    # args = json.loads(func_args_accumulated)
    dummy_result = {
        "content": [{"type": "text", "text": '{"weather": "Sunny and 22°C"}'}]
    }

    stream2 = client.interactions.create(
        model="gemini-3-flash-preview",
        previous_interaction_id=first_interaction_id,
        input=[{
            "type": "function_result",
            "name": func_call_name,
            "call_id": func_call_id,
            "result": dummy_result
        }],
        stream=True,
    )

    for event in stream2:
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const weatherTool = {
    type: "function",
    name: "get_weather",
    description: "Get the current weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// Turn 1: Request function call
const stream = await client.interactions.create({
    model: "gemini-3-flash-preview",
    tools: [weatherTool],
    input: "What is the weather in Paris right now?",
    stream: true,
});

let firstInteractionId = null;
let funcCallId = null;
let funcCallName = null;
let funcArgsAccumulated = "";

for await (const event of stream) {
    if (event.event_type === "interaction.created") {
        firstInteractionId = event.interaction.id;
    } else if (event.event_type === "step.start") {
        const step = event.step;
        if (step.type === "function_call") {
            funcCallId = step.id;
            funcCallName = step.name;
        }
    } else if (event.event_type === "step.delta") {
        if (event.delta.type === "arguments_delta") {
            funcArgsAccumulated += event.delta.arguments;
        }
    }
}

// Turn 2: Execute tool and send the result back to resume stream
if (funcCallId && firstInteractionId && funcCallName) {
    // const args = JSON.parse(funcArgsAccumulated);
    const dummyResult = {
        content: [{ type: "text", text: '{"weather": "Sunny and 22°C"}' }]
    };

    const stream2 = await client.interactions.create({
        model: "gemini-3-flash-preview",
        previous_interaction_id: firstInteractionId,
        input: [{
            type: "function_result",
            name: funcCallName,
            call_id: funcCallId,
            result: dummyResult
        }],
        stream: true,
    });

    for await (const event of stream2) {
        if (event.event_type === "step.delta") {
            if (event.delta.type === "text") {
                process.stdout.write(event.delta.text);
            }
        }
    }
}
```

### REST

**पहला टर्न:** फ़ंक्शन कॉल का अनुरोध करें

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the weather in Paris right now?",
    "stream": true,
    "tools": [
      {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            }
          },
          "required": ["location"]
        }
      }
    ]
  }'
```

**दूसरा टर्न:** पहले टर्न से मिले `previous_interaction_id` और `call_id` का इस्तेमाल करके, फ़ंक्शन का नतीजा भेजें

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "v1_ChdGUVFJYXBXVUdLVEF4TjhQ...",
    "stream": true,
    "input": [
      {
        "type": "function_result",
        "name": "get_weather",
        "call_id": "CALL_ID",
        "result": {
          "content": [
            {
              "type": "text",
              "text": "{\"weather\": \"Sunny and 22°C\"}"
            }
          ]
        }
      }
    ]
  }'
```

### एक से ज़्यादा टूल की मदद से स्ट्रीमिंग

यहां दिए गए उदाहरण में, एक ही अनुरोध में `function` टूल और `google_search`, दोनों का इस्तेमाल किया गया है:

### Python

```
from google import genai

client = genai.Client()

tools = [
    {"type": "google_search"},
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA"
                }
            },
            "required": ["location"]
        }
    }
]

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    tools=tools,
    input="Search what it the largest mountain in Europe and what the weather is there right now?",
    stream=True,
)
for event in stream:
    if event.event_type == "step.start":
        step = event.step
        print(f"\n--- Step {event.index}: {step.type} ---")
        # Show details for tool steps
        if step.type == "google_search_call":
            print(f"  Search ID: {step.id}")
        elif step.type == "google_search_result":
            print(f"  Result for: {step.call_id}")
        elif step.type == "function_call":
            print(f"  Function: {step.name}({step.arguments})")
    elif event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
        elif event.delta.type == "google_search_call":
            print(f"  Queries: {event.delta.arguments}")
        elif event.delta.type == "arguments_delta":
            print(f"  Args chunk: {event.delta.arguments}", end="", flush=True)
    elif event.event_type == "interaction.completed":
        print(f"\n\nStatus: {event.interaction.status}")
        if event.interaction.status == "requires_action":
            print("Action required: provide function call results to continue.")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const tools = [
    { type: "google_search" },
    {
        type: "function",
        name: "get_weather",
        description: "Get the current weather in a given location",
        parameters: {
            type: "object",
            properties: {
                location: {
                    type: "string",
                    description: "The city and state, e.g. San Francisco, CA"
                }
            },
            required: ["location"]
        }
    }
];

const stream = await client.interactions.create({
    model: "gemini-3-flash-preview",
    tools: tools,
    input: "Search what it the largest mountain in Europe and what the weather is there right now?",
    stream: true,
});
for await (const event of stream) {
    if (event.event_type === "step.start") {
        const step = event.step;
        console.log(`\n--- Step ${event.index}: ${step.type} ---`);
        // Show details for tool steps
        if (step.type === "google_search_call") {
            console.log(`  Search ID: ${step.id}`);
        } else if (step.type === "google_search_result") {
            console.log(`  Result for: ${step.call_id}`);
        } else if (step.type === "function_call") {
            console.log(`  Function: ${step.name}(${JSON.stringify(step.arguments)})`);
        }
    } else if (event.event_type === "step.delta") {
        if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        } else if (event.delta.type === "google_search_call") {
            console.log(`  Queries: ${JSON.stringify(event.delta.arguments?.queries)}`);
        } else if (event.step.type === "google_search_result") {
            console.log(`  Result for: ${event.step.call_id}`);
        } else if (event.delta.type === "arguments_delta") {
            process.stdout.write(`  Args chunk: ${event.delta.arguments}`);
        }
    } else if (event.event_type === "interaction.completed") {
        console.log(`\n\nStatus: ${event.interaction.status}`);
        if (event.interaction.status === "requires_action") {
            console.log("Action required: provide function call results to continue.");
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Search what it the largest mountain in Europe and what the weather is there right now?",
    "stream": true,
    "tools": [
      { "type": "google_search" },
      {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            }
          },
          "required": ["location"]
        }
      }
    ]
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"id":"mkutnkgn","signature":"","type":"google_search_call"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"...","type":"google_search_call","arguments":{"queries":["largest mountain in Europe"]}},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"call_id":"mkutnkgn","signature":"","type":"google_search_result"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"signature":"...","type":"google_search_result","is_error":false},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: step.start
data: {"index":2,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":2,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":2,"event_type":"step.stop"}

event: step.start
data: {"index":3,"step":{"id":"ktr5aysg","type":"function_call","name":"get_weather","arguments":{}},"event_type":"step.start"}

event: step.delta
data: {"index":3,"delta":{"arguments":"{\"location\":\"Mount Elbrus, Russia\"}","type":"arguments_delta"},"event_type":"step.delta"}

event: step.stop
data: {"index":3,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_...","status":"requires_action","usage":{"total_tokens":299,"total_input_tokens":138,"input_tokens_by_modality":[{"modality":"text","tokens":138}],"total_cached_tokens":0,"total_output_tokens":20,"total_tool_use_tokens":0,"total_thought_tokens":141},"created":"2026-05-12T17:24:26Z","updated":"2026-05-12T17:24:26Z","service_tier":"standard","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## थिंकिंग की मदद से स्ट्रीमिंग

जब मॉडल, थिंकिंग का इस्तेमाल करता है, तो आपको `thought` चरण मिलेंगे. इनमें डेल्टा के दो अलग-अलग टाइप होंगे: `thought_summary` (धीरे-धीरे मिलने वाला टेक्स्ट या इमेज की खास जानकारी का कॉन्टेंट) और `thought_signature` (मॉडल की इंटरनल रीज़निंग का एनक्रिप्ट किया गया वर्शन. यह `step.stop` से पहले, आखिरी डेल्टा के तौर पर भेजा जाता है). अगर `thinking_summaries` की सुविधा चालू है, तो `thought_summary` डेल्टा, मॉडल की रीज़निंग की खास जानकारी स्ट्रीम करते हैं. थिंकिंग के बारे में ज़्यादा जानने के लिए, [थिंकिंग गाइड](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=hi) देखें.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the greatest common divisor of 1071 and 462?",
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True,
)
for event in stream:
    if event.event_type == "step.start":
        print(f"\n--- Step: {event.step.type} ---")
    elif event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if event.delta.content.type == "text":
                print(event.delta.content.text, end="", flush=True)
        elif event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What is the greatest common divisor of 1071 and 462?",
    generation_config: {
        thinking_summaries: "auto",
    },
    stream: true,
});
for await (const event of stream) {
    if (event.event_type === "step.start") {
        console.log(`\n--- Step: ${event.step.type} ---`);
    } else if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (event.delta.content.type === "text") {
                process.stdout.write(event.delta.content.text);
            }
        } else if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the greatest common divisor of 1071 and 462?",
    "stream": true,
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"content":{"text":"**Implementing Euclidean Algorithm**\n\nI've just worked through a detailed example applying the Euclidean algorithm to find the GCD of 1071 and 462, confirming its step-by-step nature. The calculations went smoothly, tracking the remainders until zero. My focus is now solidifying the implementation logic, ensuring accuracy and considering potential edge cases. I'll translate this example into code.\n\n\n","type":"text"},"type":"thought_summary"},"event_type":"step.delta"}

event: step.delta
data: {"index":0,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

...
```

## एजेंट की मदद से स्ट्रीमिंग

Interactions API, Deep Research जैसे एजेंट के साथ काम करता है. एजेंट, `background=True` का इस्तेमाल करते हैं और नतीजे एसिंक्रोनस तरीके से देते हैं. हालांकि, एजेंट इंटरैक्शन को स्ट्रीम भी किया जा सकता है. इससे, प्रोग्रेस अपडेट और इंटरमीडिएट चरण मिलते हैं. ज़्यादा जानकारी के लिए, [Deep Research गाइड](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=hi) देखें.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the latest advances in quantum computing.",
    stream=True,
    background=True,
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
)
for event in stream:
    if event.event_type == "step.start":
        print(f"\n--- Step: {event.step.type} ---")
    elif event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
        elif event.delta.type == "thought_summary":
            if event.delta.content.type == "text":
                print(event.delta.content.text, end="", flush=True)
    elif event.event_type == "interaction.completed":
        print(f"\n\nTotal Tokens: {event.interaction.usage.total_tokens}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "deep-research-preview-04-2026",
    input: "Research the latest advances in quantum computing.",
    stream: true,
    background: true,
    agent_config: {
        type: "deep-research",
        thinking_summaries: "auto"
    }
});
for await (const event of stream) {
    if (event.event_type === "step.start") {
        console.log(`\n--- Step: ${event.step.type} ---`);
    } else if (event.event_type === "step.delta") {
        if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        } else if (event.delta.type === "thought_summary") {
            if (event.delta.content.type === "text") {
                process.stdout.write(event.delta.content.text);
            }
        }
    } else if (event.event_type === "interaction.completed") {
        console.log(`\n\nTotal Tokens: ${event.interaction.usage.total_tokens}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Research the latest advances in quantum computing.",
    "stream": true,
    "background": true,
    "agent_config": {
      "type": "deep-research",
      "thinking_summaries": "auto"
    }
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","agent":"deep-research-preview-04-2026"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"content":{"text":"***Generating research plan***\n\nTo best answer your request, I'm starting by constructing a comprehensive research plan. This will outline the key areas I need to investigate and the strategy I'll use to connect them."},"type":"thought_summary"},"event_type":"step.delta"}

... (additional thought steps) ...

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"# The Quantum Inflection Point: Exhaustive Analysis of Hardware, Algorithms, and Market Dynamics in 2026\n\n## Executive Summary\n\n..."},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_...","status":"completed","usage":{"total_tokens":1117031,"total_input_tokens":428865,"total_output_tokens":22294,"total_thought_tokens":26213},"created":"2026-05-12T17:24:27Z","updated":"2026-05-12T17:24:27Z","object":"interaction","agent":"deep-research-preview-04-2026"},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## इमेज जनरेट करने की प्रोसेस की मदद से इमेज जनरेट करने के लिए ऑटोमेशन

Interactions API, एक साथ कई आउटपुट मोडैलिटी को स्ट्रीम करने की सुविधा देता है. `response_format` में `text` और `image`, दोनों का अनुरोध करके, एक ही स्ट्रीम में इंटरलीव किए गए टेक्स्ट और जनरेट की गई इमेज पाई जा सकती हैं.

यहां दिए गए उदाहरण में, जानकारी खोजने और इंटरलीव किए गए इलस्ट्रेशन वाली कहानी जनरेट करने के लिए, `gemini-3.1-flash-image-preview` (Nano Banana 2) का इस्तेमाल किया गया है.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.1-flash-image-preview",
    tools=[{"type": "google_search", "search_types": ["web_search", "image_search"]}],
    input="Search for the history of the Colosseum and write a short illustrated story about a gladiator named Marcus. Interleave text and generated images.",
    response_format=[
        {"type": "text"},
        {"type": "image"}
    ],
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
        elif event.delta.type == "image":
            print(f"\n[Image chunk: {len(event.delta.data)} bytes]", end="", flush=True)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: "gemini-3.1-flash-image-preview",
    tools: [{ type: "google_search", search_types: ["web_search", "image_search"] }],
    input: "Search for the history of the Colosseum and write a short illustrated story about a gladiator named Marcus. Interleave text and generated images.",
    response_format: [
        { type: "text" },
        { type: "image" }
    ],
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        } else if (event.delta.type === "image") {
            console.log(`\n[Image chunk: ${event.delta.data.length} bytes]`);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3.1-flash-image-preview",
    "input": "Search for the history of the Colosseum and write a short illustrated story about a gladiator named Marcus. Interleave text and generated images.",
    "stream": true,
    "tools": [
      { "type": "google_search",
        "search_types": ["web_search", "image_search"]
      }
    ],
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "response_format": [
      { "type": "text" }, { "type": "image"}
    ]
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","model":"gemini-3.1-flash-image-preview"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"text":"Here is a short illustrated story about the Colosseum...\n\n### Part 1: The New Flavian Amphitheater\n\n...","type":"text"},"event_type":"step.delta"}

...

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: step.start
data: {"index":2,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":2,"delta":{"mime_type":"image/jpeg","data":"/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAoHBwgHBgoICAgLCg...","type":"image"},"event_type":"step.delta"}

event: step.delta
data: {"index":2,"delta":{"text":"### Part 2: The Hypogeum and the Wait\n\n...","type":"text"},"event_type":"step.delta"}

...

event: step.stop
data: {"index":2,"event_type":"step.stop"}

event: step.start
data: {"index":3,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":3,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":3,"event_type":"step.stop"}

event: step.start
data: {"index":4,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":4,"delta":{"mime_type":"image/jpeg","data":"/9j/4AAQSkZJRgABAQAAAQABAAD/...","type":"image"},"event_type":"step.delta"}

event: step.delta
data: {"index":4,"delta":{"text":"### Part 3: The Moment of Spectacle\n\n...","type":"text"},"event_type":"step.delta"}

...

event: step.stop
data: {"index":4,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_...","status":"completed","usage":{"total_tokens":6128,"total_input_tokens":29,"total_output_tokens":6099,"output_tokens_by_modality":[{"modality":"image","tokens":4480}]}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## अनजान इवेंट को मैनेज करना

एपीआई की वर्शनिंग नीति के मुताबिक, समय के साथ-साथ इवेंट के नए टाइप और डेल्टा के नए टाइप जोड़े जा सकते हैं. आपके कोड को, इवेंट के अनजान टाइप को आसानी से मैनेज करना चाहिए. साथ ही, जिन इवेंट की पहचान नहीं हो पाती उन्हें लॉग करें और स्किप करें. इसके बजाय, गड़बड़ी न दिखाएं.

## आगे क्या करना है

- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=hi) के बारे में ज़्यादा जानें.
- टूल की मदद से [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=hi) के बारे में जानें.
- बेहतर रीज़निंग के लिए, [थिंकिंग](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=hi) के बारे में जानें.
- लंबे समय तक चलने वाले टास्क के लिए, [Deep Research एजेंट](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=hi) आज़माएं.
- इवेंट के सभी टाइप और डेल्टा के सभी टाइप देखने के लिए, [Interactions API का रेफ़रंस](https://ai.google.dev/api/interactions?hl=hi) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-21 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-21 (UTC) को अपडेट किया गया."],[],[]]
