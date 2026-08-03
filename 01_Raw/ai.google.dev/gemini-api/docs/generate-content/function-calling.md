---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=hi
fetched_at: 2026-08-03T04:33:33.634677+00:00
title: "Gemini API \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u092b\u093c\u0902\u0915\u094d\u0936\u0928 \u0915\u0949\u0932 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini API की मदद से फ़ंक्शन कॉल करना

फ़ंक्शन कॉलिंग की सुविधा की मदद से, मॉडल को बाहरी टूल और एपीआई से कनेक्ट किया जा सकता है.
टेक्स्ट वाले जवाब जनरेट करने के बजाय, मॉडल यह तय करता है कि कब किसी फ़ंक्शन को कॉल करना है. साथ ही, असल दुनिया में होने वाली कार्रवाइयों को पूरा करने के लिए ज़रूरी पैरामीटर उपलब्ध कराता है.
इससे मॉडल, नैचुरल लैंग्वेज और असल दुनिया की कार्रवाइयों और डेटा के बीच एक पुल की तरह काम कर पाता है. फ़ंक्शन कॉलिंग का इस्तेमाल इन तीन मुख्य कामों के लिए किया जाता है:

- [**कार्रवाइयां करना:**](#meeting) एपीआई का इस्तेमाल करके बाहरी सिस्टम के साथ इंटरैक्ट करना. जैसे, अपॉइंटमेंट शेड्यूल करना, इनवॉइस बनाना, ईमेल भेजना या स्मार्ट होम डिवाइसों को कंट्रोल करना.
- [**जानकारी को बेहतर बनाना:**](#weather) डेटाबेस, एपीआई, और नॉलेज बेस जैसे बाहरी सोर्स से जानकारी ऐक्सेस करना.
- [**ज़्यादा सुविधाएं:**](#chart) कैलकुलेशन करने और मॉडल की सीमाओं को बढ़ाने के लिए, बाहरी टूल का इस्तेमाल करें. जैसे, कैलकुलेटर का इस्तेमाल करना या चार्ट बनाना.

इस्तेमाल के इन उदाहरणों को यहां देखा जा सकता है:

### मीटिंग शेड्यूल करें

इस उदाहरण में, एक ऐसा फ़ंक्शन बनाने का तरीका दिखाया गया है जो किसी खास समय पर मीटिंग शेड्यूल करता है. इससे मॉडल को उपयोगकर्ता के अनुरोधों को पार्स करने और बाहरी सिस्टम में कार्रवाइयां ट्रिगर करने के लिए, स्ट्रक्चर्ड आर्ग्युमेंट वापस भेजने की अनुमति मिलती है.

### Python

```
from google import genai
from google.genai import types

# Define the function declaration for the model
schedule_meeting_function = {
    "name": "schedule_meeting",
    "description": "Schedules a meeting with specified attendees at a given time and date.",
    "parameters": {
        "type": "object",
        "properties": {
            "attendees": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of people attending the meeting.",
            },
            "date": {
                "type": "string",
                "description": "Date of the meeting (e.g., '2024-07-29')",
            },
            "time": {
                "type": "string",
                "description": "Time of the meeting (e.g., '15:00')",
            },
            "topic": {
                "type": "string",
                "description": "The subject or topic of the meeting.",
            },
        },
        "required": ["attendees", "date", "time", "topic"],
    },
}

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[schedule_meeting_function])
config = types.GenerateContentConfig(tools=[tools])

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Schedule a meeting with Bob and Alice for 03/14/2025 at 10:00 AM about the Q3 planning.",
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"ID: {function_call.id}")
    print(f"Arguments: {function_call.args}")
    #  In a real app, you would call your function here:
    #  result = schedule_meeting(**function_call.args)
else:
    print("No function call found in the response.")
    print(response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

// Configure the client
const ai = new GoogleGenAI({});

// Define the function declaration for the model
const scheduleMeetingFunctionDeclaration = {
  name: 'schedule_meeting',
  description: 'Schedules a meeting with specified attendees at a given time and date.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      attendees: {
        type: Type.ARRAY,
        items: { type: Type.STRING },
        description: 'List of people attending the meeting.',
      },
      date: {
        type: Type.STRING,
        description: 'Date of the meeting (e.g., "2024-07-29")',
      },
      time: {
        type: Type.STRING,
        description: 'Time of the meeting (e.g., "15:00")',
      },
      topic: {
        type: Type.STRING,
        description: 'The subject or topic of the meeting.',
      },
    },
    required: ['attendees', 'date', 'time', 'topic'],
  },
};

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3.6-flash',
  contents: 'Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning.',
  config: {
    tools: [{
      functionDeclarations: [scheduleMeetingFunctionDeclaration]
    }],
  },
});

// Check for function calls in the response
if (response.functionCalls && response.functionCalls.length > 0) {
  const functionCall = response.functionCalls[0]; // Assuming one function call
  console.log(`Function to call: ${functionCall.name}`);
  console.log(`ID: ${functionCall.id}`);
  console.log(`Arguments: ${JSON.stringify(functionCall.args)}`);
  // In a real app, you would call your actual function here:
  // const result = await scheduleMeeting(functionCall.args);
} else {
  console.log("No function call found in the response.");
  console.log(response.text);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning."
          }
        ]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "schedule_meeting",
            "description": "Schedules a meeting with specified attendees at a given time and date.",
            "parameters": {
              "type": "object",
              "properties": {
                "attendees": {
                  "type": "array",
                  "items": {"type": "string"},
                  "description": "List of people attending the meeting."
                },
                "date": {
                  "type": "string",
                  "description": "Date of the meeting (e.g., '2024-07-29')"
                },
                "time": {
                  "type": "string",
                  "description": "Time of the meeting (e.g., '15:00')"
                },
                "topic": {
                  "type": "string",
                  "description": "The subject or topic of the meeting."
                }
              },
              "required": ["attendees", "date", "time", "topic"]
            }
          }
        ]
      }
    ]
  }'
```

### मौसम की जानकारी

इस उदाहरण में, किसी जगह के तापमान का डेटा पाने वाले फ़ंक्शन को तय करने का तरीका बताया गया है. इससे मॉडल, उन सवालों के जवाब देने के लिए बाहरी एपीआई को कॉल कर सकता है जिनके लिए रीयल-टाइम या बाहरी जानकारी की ज़रूरत होती है.

### Python

```
from google import genai
from google.genai import types

# Define the function declaration for the model
weather_function = {
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What's the temperature in London?",
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"ID: {function_call.id}")
    print(f"Arguments: {function_call.args}")
    #  In a real app, you would call your function here:
    #  result = get_current_temperature(**function_call.args)
else:
    print("No function call found in the response.")
    print(response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

// Configure the client
const ai = new GoogleGenAI({});

// Define the function declaration for the model
const weatherFunctionDeclaration = {
  name: 'get_current_temperature',
  description: 'Gets the current temperature for a given location.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      location: {
        type: Type.STRING,
        description: 'The city name, e.g. San Francisco',
      },
    },
    required: ['location'],
  },
};

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3.6-flash',
  contents: "What's the temperature in London?",
  config: {
    tools: [{
      functionDeclarations: [weatherFunctionDeclaration]
    }],
  },
});

// Check for function calls in the response
if (response.functionCalls && response.functionCalls.length > 0) {
  const functionCall = response.functionCalls[0]; // Assuming one function call
  console.log(`Function to call: ${functionCall.name}`);
  console.log(`ID: ${functionCall.id}`);
  console.log(`Arguments: ${JSON.stringify(functionCall.args)}`);
  // In a real app, you would call your actual function here:
  // const result = await getCurrentTemperature(functionCall.args);
} else {
  console.log("No function call found in the response.");
  console.log(response.text);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "What'\''s the temperature in London?"
          }
        ]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

### चार्ट बनाएं

इस उदाहरण में, स्ट्रक्चर्ड डेटा से बार चार्ट जनरेट करने वाले फ़ंक्शन को तय करने का तरीका बताया गया है. इससे पता चलता है कि मॉडल, कैलकुलेशन करने या विज़ुअल ऐसेट बनाने के लिए बाहरी टूल का इस्तेमाल कैसे कर सकता है:

### Python

```
import os
from google import genai
from google.genai import types

# Define the function declaration for the model
create_chart_function = {
    "name": "create_bar_chart",
    "description": "Creates a bar chart given a title, labels, and corresponding values.",
    "parameters": {
        "type": "object",
        "properties": {
            "title": {
                "type": "string",
                "description": "The title for the chart.",
            },
            "labels": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of labels for the data points (e.g., ['Q1', 'Q2', 'Q3']).",
            },
            "values": {
                "type": "array",
                "items": {"type": "number"},
                "description": "List of numerical values corresponding to the labels (e.g., [50000, 75000, 60000]).",
            },
        },
        "required": ["title", "labels", "values"],
    },
}

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[create_chart_function])
config = types.GenerateContentConfig(tools=[tools])

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Create a bar chart titled 'Quarterly Sales' with data: Q1: 50000, Q2: 75000, Q3: 60000.",
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"ID: {function_call.id}")
    print(f"Arguments: {function_call.args}")
    #  In a real app, you would call your function here using a charting library:
    #  result = create_bar_chart(**function_call.args)
else:
    print("No function call found in the response.")
    print(response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

// Configure the client
const ai = new GoogleGenAI({});

// Define the function declaration for the model
const createChartFunctionDeclaration = {
  name: 'create_bar_chart',
  description: 'Creates a bar chart given a title, labels, and corresponding values.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      title: {
        type: Type.STRING,
        description: 'The title for the chart.',
      },
      labels: {
        type: Type.ARRAY,
        items: { type: Type.STRING },
        description: 'List of labels for the data points (e.g., ["Q1", "Q2", "Q3"]).',
      },
      values: {
        type: Type.ARRAY,
        items: { type: Type.NUMBER },
        description: 'List of numerical values corresponding to the labels (e.g., [50000, 75000, 60000]).',
      },
    },
    required: ['title', 'labels', 'values'],
  },
};

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3.6-flash',
  contents: "Create a bar chart titled 'Quarterly Sales' with data: Q1: 50000, Q2: 75000, Q3: 60000.",
  config: {
    tools: [{
      functionDeclarations: [createChartFunctionDeclaration]
    }],
  },
});

// Check for function calls in the response
if (response.functionCalls && response.functionCalls.length > 0) {
  const functionCall = response.functionCalls[0]; // Assuming one function call
  console.log(`Function to call: ${functionCall.name}`);
  console.log(`ID: ${functionCall.id}`);
  console.log(`Arguments: ${JSON.stringify(functionCall.args)}`);
  // In a real app, you would call your actual function here:
  // const result = await createBarChart(functionCall.args);
} else {
  console.log("No function call found in the response.");
  console.log(response.text);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Create a bar chart titled ''Quarterly Sales'' with data: Q1: 50000, Q2: 75000, Q3: 60000."
          }
        ]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "create_bar_chart",
            "description": "Creates a bar chart given a title, labels, and corresponding values.",
            "parameters": {
              "type": "object",
              "properties": {
                "title": {
                  "type": "string",
                  "description": "The title for the chart."
                },
                "labels": {
                  "type": "array",
                  "items": {"type": "string"},
                  "description": "List of labels for the data points (e.g., [''Q1'', ''Q2'', ''Q3''])."
                },
                "values": {
                  "type": "array",
                  "items": {"type": "number"},
                  "description": "List of numerical values corresponding to the labels (e.g., [50000, 75000, 60000])."
                }
              },
              "required": ["title", "labels", "values"]
            }
          }
        ]
      }
    ]
  }'
```

## फ़ंक्शन कॉलिंग की सुविधा कैसे काम करती है

![फ़ंक्शन कॉलिंग के बारे में खास जानकारी](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=hi)

फ़ंक्शन कॉलिंग में, आपके ऐप्लिकेशन, मॉडल, और बाहरी फ़ंक्शन के बीच स्ट्रक्चर्ड इंटरैक्शन शामिल होता है. इस प्रोसेस के बारे में यहां बताया गया है:

1. **फ़ंक्शन डिक्लेरेशन तय करें:** अपने ऐप्लिकेशन कोड में फ़ंक्शन डिक्लेरेशन तय करें. फ़ंक्शन के बारे में जानकारी देने वाले स्टेटमेंट में, मॉडल को फ़ंक्शन के नाम, पैरामीटर, और मकसद के बारे में बताया जाता है.
2. **फ़ंक्शन के एलान के साथ एपीआई को कॉल करें:** मॉडल को, फ़ंक्शन के एलान के साथ-साथ उपयोगकर्ता का प्रॉम्प्ट भेजें. यह अनुरोध का विश्लेषण करता है और यह तय करता है कि फ़ंक्शन कॉल करना मददगार होगा या नहीं. अगर ऐसा है, तो यह फ़ंक्शन के नाम, आर्ग्युमेंट, और यूनीक `id` (Gemini 3 मॉडल के लिए, एपीआई अब हमेशा `id` दिखाता है\*) के साथ स्ट्रक्चर्ड JSON ऑब्जेक्ट के तौर पर जवाब देता है.
3. **फ़ंक्शन कोड को लागू करना (आपकी ज़िम्मेदारी):** मॉडल, फ़ंक्शन को *लागू नहीं करता*. जवाब को प्रोसेस करने और फ़ंक्शन कॉल की जांच करने की ज़िम्मेदारी आपके ऐप्लिकेशन की है. अगर
   - **हां**: फ़ंक्शन का नाम, आर्ग्युमेंट, और `id` निकालें. इसके बाद, अपने ऐप्लिकेशन में इससे जुड़ा फ़ंक्शन लागू करें.
   - **नहीं:** मॉडल ने प्रॉम्प्ट का सीधा जवाब टेक्स्ट के तौर पर दिया है
     (उदाहरण में इस फ़्लो पर कम ज़ोर दिया गया है, लेकिन यह एक संभावित नतीजा है).
4. **उपयोगकर्ता के लिए आसान जवाब तैयार करना:** अगर कोई फ़ंक्शन पूरा हो गया है, तो उसके नतीजे को कैप्चर करें और उसे मॉडल को वापस भेजें. साथ ही, यह पक्का करें कि बातचीत के अगले चरण में, आपने मैच करने वाला `id` शामिल किया हो. यह नतीजे का इस्तेमाल करके, उपयोगकर्ता के लिए एक ऐसा जवाब जनरेट करेगा जिसमें फ़ंक्शन कॉल से मिली जानकारी शामिल होगी.

इस प्रोसेस को कई बार दोहराया जा सकता है. इससे मुश्किल इंटरैक्शन और वर्कफ़्लो को पूरा किया जा सकता है. यह मॉडल, एक ही बार में कई फ़ंक्शन कॉल करने ([पैरलल फ़ंक्शन कॉलिंग](#parallel_function_calling)), क्रम से फ़ंक्शन कॉल करने ([कंपोज़िशनल फ़ंक्शन कॉलिंग](#compositional_function_calling)), और Gemini के बिल्ट-इन टूल ([एक से ज़्यादा टूल का इस्तेमाल करना](#native-tools)) के साथ भी काम करता है.

\* **फ़ंक्शन आईडी हमेशा मैप करें:** Gemini 3 अब हर `functionCall` के साथ हमेशा एक यूनीक `id` दिखाता है. अपने `functionResponse` में यह `id` शामिल करें, ताकि मॉडल आपके नतीजे को ओरिजनल अनुरोध से सटीक तरीके से मैप कर सके.

### पहला चरण: फ़ंक्शन के बारे में जानकारी देना

अपने ऐप्लिकेशन कोड में एक फ़ंक्शन और उसके एलान को तय करें. इससे उपयोगकर्ता, रोशनी की वैल्यू सेट कर पाएंगे और एपीआई अनुरोध कर पाएंगे. यह फ़ंक्शन, बाहरी सेवाओं या एपीआई को कॉल कर सकता है.

### Python

```
# Define a function that the model can call to control smart lights
set_light_values_declaration = {
    "name": "set_light_values",
    "description": "Sets the brightness and color temperature of a light.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "integer",
                "description": "Light level from 0 to 100. Zero is off and 100 is full brightness",
            },
            "color_temp": {
                "type": "string",
                "enum": ["daylight", "cool", "warm"],
                "description": "Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.",
            },
        },
        "required": ["brightness", "color_temp"],
    },
}

# This is the actual function that would be called based on the model's suggestion
def set_light_values(brightness: int, color_temp: str) -> dict[str, int | str]:
    """Set the brightness and color temperature of a room light. (mock API).

    Args:
        brightness: Light level from 0 to 100. Zero is off and 100 is full brightness
        color_temp: Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.

    Returns:
        A dictionary containing the set brightness and color temperature.
    """
    return {"brightness": brightness, "colorTemperature": color_temp}
```

### JavaScript

```
import { Type } from '@google/genai';

// Define a function that the model can call to control smart lights
const setLightValuesFunctionDeclaration = {
  name: 'set_light_values',
  description: 'Sets the brightness and color temperature of a light.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      brightness: {
        type: Type.NUMBER,
        description: 'Light level from 0 to 100. Zero is off and 100 is full brightness',
      },
      color_temp: {
        type: Type.STRING,
        enum: ['daylight', 'cool', 'warm'],
        description: 'Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.',
      },
    },
    required: ['brightness', 'color_temp'],
  },
};

/**

*   Set the brightness and color temperature of a room light. (mock API)
*   @param {number} brightness - Light level from 0 to 100. Zero is off and 100 is full brightness
*   @param {string} color_temp - Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.
*   @return {Object} A dictionary containing the set brightness and color temperature.
*/
function setLightValues(brightness, color_temp) {
  return {
    brightness: brightness,
    colorTemperature: color_temp
  };
}
```

### दूसरा चरण: फ़ंक्शन के बारे में जानकारी देकर मॉडल को कॉल करना

फ़ंक्शन के एलान तय करने के बाद, मॉडल को उनका इस्तेमाल करने के लिए कहा जा सकता है. यह प्रॉम्प्ट और फ़ंक्शन के एलान का विश्लेषण करता है. इसके बाद, यह तय करता है कि सीधे जवाब देना है या किसी फ़ंक्शन को कॉल करना है. अगर किसी फ़ंक्शन को कॉल किया जाता है, तो जवाब ऑब्जेक्ट में फ़ंक्शन कॉल का सुझाव शामिल होगा.

### Python

```
from google.genai import types

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[set_light_values_declaration])
config = types.GenerateContentConfig(tools=[tools])

# Define user prompt
contents = [
    types.Content(
        role="user", parts=[types.Part(text="Turn the lights down to a romantic level")]
    )
]

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=contents,
    config=config,
)

print(response.candidates[0].content.parts[0].function_call)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

// Generation config with function declaration
const config = {
  tools: [{
    functionDeclarations: [setLightValuesFunctionDeclaration]
  }]
};

// Configure the client
const ai = new GoogleGenAI({});

// Define user prompt
const contents = [
  {
    role: 'user',
    parts: [{ text: 'Turn the lights down to a romantic level' }]
  }
];

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3.6-flash',
  contents: contents,
  config: config
});

console.log(response.functionCalls[0]);
```

इसके बाद, मॉडल OpenAPI के साथ काम करने वाले स्कीमा में `functionCall` ऑब्जेक्ट दिखाता है. इसमें यह बताया जाता है कि उपयोगकर्ता के सवाल का जवाब देने के लिए, एलान किए गए एक या उससे ज़्यादा फ़ंक्शन को कैसे कॉल किया जाए.

### Python

```
id='8f2b1a3c' args={'color_temp': 'warm', 'brightness': 25} name='set_light_values'
```

### JavaScript

```
{
  id: '8f2b1a3c',
  name: 'set_light_values',
  args: { brightness: 25, color_temp: 'warm' }
}
```

### तीसरा चरण: set\_light\_values फ़ंक्शन कोड को लागू करना

मॉडल के जवाब से फ़ंक्शन कॉल की जानकारी निकालें, आर्ग्युमेंट पार्स करें, और `set_light_values` फ़ंक्शन को लागू करें.

### Python

```
# Extract tool call details, it may not be in the first part.
tool_call = response.candidates[0].content.parts[0].function_call

if tool_call.name == "set_light_values":
    result = set_light_values(**tool_call.args)
    print(f"Function execution result: {result}")
```

### JavaScript

```
// Extract tool call details
const tool_call = response.functionCalls[0]

let result;
if (tool_call.name === 'set_light_values') {
  result = setLightValues(tool_call.args.brightness, tool_call.args.color_temp);
  console.log(`Function execution result: ${JSON.stringify(result)}`);
}
```

### चौथा चरण: फ़ंक्शन के नतीजे के साथ उपयोगकर्ता के लिए आसान जवाब जनरेट करना और मॉडल को फिर से कॉल करना

आखिर में, फ़ंक्शन के नतीजे को वापस मॉडल को भेजें, ताकि वह इस जानकारी को उपयोगकर्ता को दिए जाने वाले अपने फ़ाइनल जवाब में शामिल कर सके.

### Python

```
from google import genai
from google.genai import types

# Create a function response part
function_response_part = types.Part.from_function_response(
    name=tool_call.name,
    response={"result": result},
    id=tool_call.id,
)

# Append function call and result of the function execution to contents
contents.append(response.candidates[0].content) # Append the content from the model's response.
contents.append(types.Content(role="user", parts=[function_response_part])) # Append the function response

client = genai.Client()
final_response = client.models.generate_content(
    model="gemini-3.6-flash",
    config=config,
    contents=contents,
)

print(final_response.text)
```

### JavaScript

```
// Create a function response part
const function_response_part = {
  name: tool_call.name,
  response: { result },
  id: tool_call.id
}

// Append function call and result of the function execution to contents
contents.push(response.candidates[0].content);
contents.push({ role: 'user', parts: [{ functionResponse: function_response_part }] });

// Get the final response from the model
const final_response = await ai.models.generateContent({
  model: 'gemini-3.6-flash',
  contents: contents,
  config: config
});

console.log(final_response.text);
```

इससे फ़ंक्शन कॉलिंग की प्रोसेस पूरी हो जाती है. मॉडल ने उपयोगकर्ता के अनुरोध को पूरा करने के लिए, `set_light_values` फ़ंक्शन का इस्तेमाल किया.

## फ़ंक्शन के एलान

किसी प्रॉम्प्ट में फ़ंक्शन कॉलिंग लागू करने पर, आपको एक `tools` ऑब्जेक्ट बनाना होता है. इसमें एक या उससे ज़्यादा `function declarations` होते हैं. JSON का इस्तेमाल करके फ़ंक्शन तय किए जाते हैं. खास तौर पर, [OpenAPI स्कीमा](https://spec.openapis.org/oas/v3.0.3#schemaw) फ़ॉर्मैट के [चुनिंदा सबसेट](https://ai.google.dev/api/caching?hl=hi#Schema) का इस्तेमाल करके. किसी फ़ंक्शन के एक ही एलान में ये पैरामीटर शामिल किए जा सकते हैं:

- `name` (string): फ़ंक्शन के लिए यूनीक नाम (`get_weather_forecast`,
  `send_email`). ऐसे नाम इस्तेमाल करें जिनमें खाली जगह या खास वर्ण न हों. साथ ही, वे नाम जानकारी देने वाले हों (अंडरस्कोर या कैमल केस का इस्तेमाल करें).
- `description` (string): फ़ंक्शन के मकसद और क्षमताओं के बारे में साफ़ तौर पर और पूरी जानकारी. इससे मॉडल को यह समझने में मदद मिलती है कि फ़ंक्शन का इस्तेमाल कब करना है. जवाब में सटीक जानकारी दें. अगर ज़रूरी हो, तो उदाहरण भी दें ("जगह के हिसाब से थिएटर ढूंढता है. साथ ही, अगर चाहें, तो फ़िल्म के टाइटल के हिसाब से भी थिएटर ढूंढता है. यह फ़िलहाल थिएटर में चल रही फ़िल्मों के बारे में जानकारी देता है.").
- `parameters` (object): यह फ़ंक्शन के लिए ज़रूरी इनपुट पैरामीटर तय करता है.
  - `type` (string): यह पूरे डेटा टाइप के बारे में बताता है. जैसे, `object`.
  - `properties` (ऑब्जेक्ट): इसमें अलग-अलग पैरामीटर की सूची होती है. हर पैरामीटर में यह जानकारी होती है:
    - `type` (string): पैरामीटर का डेटा टाइप, जैसे कि `string`,
      `integer`, `boolean, array`.
    - `description` (string): पैरामीटर के मकसद और फ़ॉर्मैट की जानकारी. उदाहरण और पाबंदियां दें ("शहर और राज्य, उदाहरण के लिए, 'सैन फ़्रांसिस्को, कैलिफ़ोर्निया' या ज़िप कोड, उदाहरण के लिए, '95616'.").
    - `enum` (ऐरे, ज़रूरी नहीं): अगर पैरामीटर की वैल्यू एक तय सेट से ली गई हैं, तो "enum" का इस्तेमाल करके, अनुमति वाली वैल्यू की सूची बनाएं. इसके बजाय, सिर्फ़ ब्यौरे में उनका वर्णन न करें. इससे सटीक जानकारी मिलती है ("enum":
      ["daylight", "cool", "warm"]).
  - `required` (ऐरे): स्ट्रिंग का एक ऐरे, जिसमें उन पैरामीटर के नाम दिए गए हैं जो फ़ंक्शन के काम करने के लिए ज़रूरी हैं.

`types.FunctionDeclaration.from_callable(client=client, callable=your_function)` का इस्तेमाल करके, Python फ़ंक्शन से सीधे तौर पर `FunctionDeclarations` भी बनाया जा सकता है.

## सूझ-बूझ वाले मॉडल के साथ फ़ंक्शन कॉलिंग की सुविधा

Gemini 3 और 2.5 सीरीज़ के मॉडल, अनुरोधों के जवाब देने के लिए इंटरनल ["सोचने"](https://ai.google.dev/gemini-api/docs/thinking?hl=hi) की प्रोसेस का इस्तेमाल करते हैं. इससे फ़ंक्शन कॉलिंग की परफ़ॉर्मेंस में काफ़ी सुधार होता है. साथ ही, मॉडल यह बेहतर तरीके से तय कर पाता है कि किसी फ़ंक्शन को कब कॉल करना है और किन पैरामीटर का इस्तेमाल करना है. Gemini API, स्टेटलेस होता है. इसलिए, मॉडल सिलसिलेवार बातचीत में कॉन्टेक्स्ट बनाए रखने के लिए, [थॉट सिग्नेचर](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=hi) का इस्तेमाल करते हैं.

इस सेक्शन में, थॉट सिग्नेचर को बेहतर तरीके से मैनेज करने के बारे में बताया गया है. इसकी ज़रूरत सिर्फ़ तब होती है, जब आपको एपीआई के अनुरोधों को मैन्युअल तरीके से बनाना हो (जैसे, REST के ज़रिए) या बातचीत के इतिहास में बदलाव करना हो.

**अगर [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=hi) (हमारी आधिकारिक लाइब्रेरी) का इस्तेमाल किया जा रहा है, तो आपको इस प्रोसेस को मैनेज करने की ज़रूरत नहीं है**. एसडीके, ज़रूरी चरणों को अपने-आप पूरा करते हैं. जैसा कि पहले [उदाहरण](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#step-4) में दिखाया गया है.

### बातचीत के इतिहास को मैन्युअल तरीके से मैनेज करना

अगर आपको बातचीत के इतिहास में मैन्युअल तरीके से बदलाव करना है, तो [पिछले जवाब की पूरी जानकारी](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#step-4) भेजने के बजाय, आपको मॉडल के टर्न में शामिल `thought_signature` को सही तरीके से मैनेज करना होगा.

यह पक्का करने के लिए कि मॉडल का कॉन्टेक्स्ट बना रहे, इन नियमों का पालन करें:

- `thought_signature` को हमेशा उसके ओरिजनल [`Part`](https://ai.google.dev/api?hl=hi#request-body-structure) के अंदर मॉडल में वापस भेजें.
- **अपने `function_response` में हमेशा `function_call` से मिला `id` शामिल करें, ताकि एपीआई नतीजे को सही अनुरोध से मैप कर सके.**
- सिग्नेचर वाले `Part` को ऐसे `Part` के साथ न मिलाएं जिसमें सिग्नेचर न हो. इससे, विचार के क्रम से जुड़े कॉन्टेक्स्ट में रुकावट आती है.
- दो ऐसे `Parts` को न मिलाएं जिनमें हस्ताक्षर शामिल हों, क्योंकि हस्ताक्षर वाली स्ट्रिंग को मर्ज नहीं किया जा सकता.

#### Gemini 3 के जवाबों में शामिल किए गए विचार

Gemini 3 में, मॉडल के जवाब के किसी भी [`Part`](https://ai.google.dev/api?hl=hi#request-body-structure) में थॉट सिग्नेचर हो सकता है.
आम तौर पर, हम सभी तरह के `Part` से सिग्नेचर वापस भेजने का सुझाव देते हैं. हालांकि, फ़ंक्शन कॉलिंग के लिए थॉट सिग्नेचर वापस भेजना ज़रूरी है. अगर बातचीत के इतिहास में मैन्युअल तरीके से बदलाव नहीं किया जा रहा है, तो Google GenAI SDK, थॉट सिग्नेचर को अपने-आप मैनेज करेगा.

अगर बातचीत के इतिहास को मैन्युअल तरीके से बदला जा रहा है, तो Gemini 3 के लिए थॉट सिग्नेचर मैनेज करने के बारे में पूरी जानकारी और दिशा-निर्देश पाने के लिए, [थॉट सिग्नेचर](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=hi) पेज पर जाएं.

##### सोच के सिग्नेचर की जांच करना

इसे लागू करना ज़रूरी नहीं है. हालांकि, डीबग करने या शिक्षा के मकसद से, `thought_signature` देखने के लिए रिस्पॉन्स की जांच की जा सकती है.

### Python

```
import base64
# After receiving a response from a model with thinking enabled
# response = client.models.generate_content(...)

# The signature is attached to the response part containing the function call
part = response.candidates[0].content.parts[0]
if part.thought_signature:
  print(base64.b64encode(part.thought_signature).decode("utf-8"))
```

### JavaScript

```
// After receiving a response from a model with thinking enabled
// const response = await ai.models.generateContent(...)

// The signature is attached to the response part containing the function call
const part = response.candidates[0].content.parts[0];
if (part.thoughtSignature) {
  console.log(part.thoughtSignature);
}
```

[सोचने की प्रक्रिया](https://ai.google.dev/gemini-api/docs/thinking?hl=hi#signatures) वाले पेज पर, थॉट सिग्नेचर के इस्तेमाल और इससे जुड़ी सीमाओं के बारे में ज़्यादा जानें. साथ ही, सोचने के मॉडल के बारे में सामान्य जानकारी पाएं.

## पैरलल फ़ंक्शन कॉलिंग

एक बार में एक फ़ंक्शन कॉल करने के साथ-साथ, एक साथ कई फ़ंक्शन भी कॉल किए जा सकते हैं. पैरलल फ़ंक्शन कॉलिंग की मदद से, एक साथ कई फ़ंक्शन लागू किए जा सकते हैं. इसका इस्तेमाल तब किया जाता है, जब फ़ंक्शन एक-दूसरे पर निर्भर न हों. यह कई स्थितियों में काम आता है. जैसे, अलग-अलग सोर्स से डेटा इकट्ठा करना. जैसे, अलग-अलग डेटाबेस से ग्राहक की जानकारी पाना या अलग-अलग वेयरहाउस में इन्वेंट्री के लेवल की जांच करना. इसके अलावा, कई कार्रवाइयां करना. जैसे, अपने अपार्टमेंट को डिस्को में बदलना.

जब मॉडल एक ही बार में कई फ़ंक्शन कॉल शुरू करता है, तो आपको `function_result` ऑब्जेक्ट को उसी क्रम में वापस करने की ज़रूरत नहीं होती जिस क्रम में `function_call` ऑब्जेक्ट मिले थे. Gemini API, हर नतीजे को वापस उसकी कॉल पर मैप करता है. इसके लिए, मॉडल के आउटपुट से मिले `id` का इस्तेमाल किया जाता है. इससे, फ़ंक्शन को एसिंक्रोनस तरीके से लागू किया जा सकता है. साथ ही, नतीजे पूरे होने पर उन्हें अपनी सूची में जोड़ा जा सकता है.

### Python

```
power_disco_ball = {
    "name": "power_disco_ball",
    "description": "Powers the spinning disco ball.",
    "parameters": {
        "type": "object",
        "properties": {
            "power": {
                "type": "boolean",
                "description": "Whether to turn the disco ball on or off.",
            }
        },
        "required": ["power"],
    },
}

start_music = {
    "name": "start_music",
    "description": "Play some music matching the specified parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "energetic": {
                "type": "boolean",
                "description": "Whether the music is energetic or not.",
            },
            "loud": {
                "type": "boolean",
                "description": "Whether the music is loud or not.",
            },
        },
        "required": ["energetic", "loud"],
    },
}

dim_lights = {
    "name": "dim_lights",
    "description": "Dim the lights.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "number",
                "description": "The brightness of the lights, 0.0 is off, 1.0 is full.",
            }
        },
        "required": ["brightness"],
    },
}
```

### JavaScript

```
import { Type } from '@google/genai';

const powerDiscoBall = {
  name: 'power_disco_ball',
  description: 'Powers the spinning disco ball.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      power: {
        type: Type.BOOLEAN,
        description: 'Whether to turn the disco ball on or off.'
      }
    },
    required: ['power']
  }
};

const startMusic = {
  name: 'start_music',
  description: 'Play some music matching the specified parameters.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      energetic: {
        type: Type.BOOLEAN,
        description: 'Whether the music is energetic or not.'
      },
      loud: {
        type: Type.BOOLEAN,
        description: 'Whether the music is loud or not.'
      }
    },
    required: ['energetic', 'loud']
  }
};

const dimLights = {
  name: 'dim_lights',
  description: 'Dim the lights.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      brightness: {
        type: Type.NUMBER,
        description: 'The brightness of the lights, 0.0 is off, 1.0 is full.'
      }
    },
    required: ['brightness']
  }
};
```

फ़ंक्शन कॉलिंग मोड को कॉन्फ़िगर करें, ताकि बताए गए सभी टूल का इस्तेमाल किया जा सके.
ज़्यादा जानने के लिए, [फ़ंक्शन कॉलिंग को कॉन्फ़िगर करने](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#function_calling_modes) के बारे में पढ़ें.

### Python

```
from google import genai
from google.genai import types

# Configure the client and tools
client = genai.Client()
house_tools = [
    types.Tool(function_declarations=[power_disco_ball, start_music, dim_lights])
]
config = types.GenerateContentConfig(
    tools=house_tools,
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
        disable=True
    ),
    # Force the model to call 'any' function, instead of chatting.
    tool_config=types.ToolConfig(
        function_calling_config=types.FunctionCallingConfig(mode='ANY')
    ),
)

chat = client.chats.create(model="gemini-3.6-flash", config=config)
response = chat.send_message("Turn this place into a party!")

# Print out each of the function calls requested from this single call
print("Example 1: Forced function calling")
for fn in response.function_calls:
    args = ", ".join(f"{key}={val}" for key, val in fn.args.items())
    print(f"{fn.name}({args}) - ID: {fn.id}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

// Set up function declarations
const houseFns = [powerDiscoBall, startMusic, dimLights];

const config = {
    tools: [{
        functionDeclarations: houseFns
    }],
    // Force the model to call 'any' function, instead of chatting.
    toolConfig: {
        functionCallingConfig: {
            mode: 'any'
        }
    }
};

// Configure the client
const ai = new GoogleGenAI({});

// Create a chat session
const chat = ai.chats.create({
    model: 'gemini-3.6-flash',
    config: config
});
const response = await chat.sendMessage({message: 'Turn this place into a party!'});

// Print out each of the function calls requested from this single call
console.log("Example 1: Forced function calling");
for (const fn of response.functionCalls) {
    const args = Object.entries(fn.args)
        .map(([key, val]) => `${key}=${val}`)
        .join(', ');
    console.log(`${fn.name}(${args}) - ID: ${fn.id}`);
}
```

प्रिंट किए गए हर नतीजे में, फ़ंक्शन कॉल का एक ऐसा अनुरोध दिखता है जो मॉडल ने किया है. नतीजे वापस भेजने के लिए, जवाबों को उसी क्रम में शामिल करें जिस क्रम में अनुरोध किए गए थे.

Python SDK में [फ़ंक्शन को अपने-आप कॉल करने की सुविधा](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#automatic_function_calling_python_only) उपलब्ध है. यह सुविधा, Python फ़ंक्शन को अपने-आप डिक्लेरेशन में बदल देती है. साथ ही, फ़ंक्शन कॉल को एक्ज़ीक्यूट करने और जवाब देने के साइकल को मैनेज करती है. डिस्को के इस्तेमाल का उदाहरण यहां दिया गया है.

### Python

```
from google import genai
from google.genai import types

# Actual function implementations
def power_disco_ball_impl(power: bool) -> dict:
    """Powers the spinning disco ball.

    Args:
        power: Whether to turn the disco ball on or off.

    Returns:
        A status dictionary indicating the current state.
    """
    return {"status": f"Disco ball powered {'on' if power else 'off'}"}

def start_music_impl(energetic: bool, loud: bool) -> dict:
    """Play some music matching the specified parameters.

    Args:
        energetic: Whether the music is energetic or not.
        loud: Whether the music is loud or not.

    Returns:
        A dictionary containing the music settings.
    """
    music_type = "energetic" if energetic else "chill"
    volume = "loud" if loud else "quiet"
    return {"music_type": music_type, "volume": volume}

def dim_lights_impl(brightness: float) -> dict:
    """Dim the lights.

    Args:
        brightness: The brightness of the lights, 0.0 is off, 1.0 is full.

    Returns:
        A dictionary containing the new brightness setting.
    """
    return {"brightness": brightness}

# Configure the client
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[power_disco_ball_impl, start_music_impl, dim_lights_impl]
)

# Make the request
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Do everything you need to this place into party!",
    config=config,
)

print("\nExample 2: Automatic function calling")
print(response.text)
# I've turned on the disco ball, started playing loud and energetic music, and dimmed the lights to 50% brightness. Let's get this party started!
```

## कॉम्पोज़िशनल फ़ंक्शन कॉलिंग

कंपोज़िशनल या सीक्वेंशियल फ़ंक्शन कॉलिंग की मदद से, Gemini एक मुश्किल अनुरोध को पूरा करने के लिए, एक साथ कई फ़ंक्शन कॉल कर सकता है. उदाहरण के लिए, "मेरी मौजूदा जगह का तापमान बताओ" सवाल का जवाब देने के लिए, Gemini API पहले `get_current_location()` फ़ंक्शन को कॉल कर सकता है. इसके बाद, वह `get_weather()` फ़ंक्शन को कॉल कर सकता है, जो जगह की जानकारी को पैरामीटर के तौर पर लेता है.

यहां दिए गए उदाहरण में, Python SDK और अपने-आप फ़ंक्शन कॉल करने की सुविधा का इस्तेमाल करके, कंपोज़िशनल फ़ंक्शन कॉल करने की सुविधा को लागू करने का तरीका बताया गया है.

### Python

इस उदाहरण में, `google-genai` Python SDK की अपने-आप फ़ंक्शन कॉल करने की सुविधा का इस्तेमाल किया गया है. एसडीके, Python फ़ंक्शन को ज़रूरी स्कीमा में अपने-आप बदल देता है. साथ ही, मॉडल के अनुरोध करने पर फ़ंक्शन कॉल को लागू करता है और टास्क पूरा करने के लिए, नतीजे वापस मॉडल को भेजता है.

```
import os
from google import genai
from google.genai import types

# Example Functions
def get_weather_forecast(location: str) -> dict:
    """Gets the current weather temperature for a given location."""
    print(f"Tool Call: get_weather_forecast(location={location})")
    # TODO: Make API call
    print("Tool Response: {'temperature': 25, 'unit': 'celsius'}")
    return {"temperature": 25, "unit": "celsius"}  # Dummy response

def set_thermostat_temperature(temperature: int) -> dict:
    """Sets the thermostat to a desired temperature."""
    print(f"Tool Call: set_thermostat_temperature(temperature={temperature})")
    # TODO: Interact with a thermostat API
    print("Tool Response: {'status': 'success'}")
    return {"status": "success"}

# Configure the client and model
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[get_weather_forecast, set_thermostat_temperature]
)

# Make the request
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
    config=config,
)

# Print the final, user-facing response
print(response.text)
```

**अनुमानित आउटपुट**

कोड चलाने पर, आपको दिखेगा कि SDK फ़ंक्शन कॉल को व्यवस्थित कर रहा है. मॉडल पहले `get_weather_forecast` को कॉल करता है, तापमान की जानकारी पाता है, और फिर प्रॉम्प्ट में दिए गए लॉजिक के आधार पर सही वैल्यू के साथ `set_thermostat_temperature` को कॉल करता है.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. I've set the thermostat to 20°C.
```

### JavaScript

इस उदाहरण में, मैन्युअल एक्ज़ीक्यूशन लूप का इस्तेमाल करके, कंपोज़िशनल फ़ंक्शन कॉलिंग करने के लिए JavaScript/TypeScript SDK का इस्तेमाल करने का तरीका दिखाया गया है.

```
import { GoogleGenAI, Type } from "@google/genai";

// Configure the client
const ai = new GoogleGenAI({});

// Example Functions
function get_weather_forecast({ location }) {
  console.log(`Tool Call: get_weather_forecast(location=${location})`);
  // TODO: Make API call
  console.log("Tool Response: {'temperature': 25, 'unit': 'celsius'}");
  return { temperature: 25, unit: "celsius" };
}

function set_thermostat_temperature({ temperature }) {
  console.log(
    `Tool Call: set_thermostat_temperature(temperature=${temperature})`,
  );
  // TODO: Make API call
  console.log("Tool Response: {'status': 'success'}");
  return { status: "success" };
}

const toolFunctions = {
  get_weather_forecast,
  set_thermostat_temperature,
};

const tools = [
  {
    functionDeclarations: [
      {
        name: "get_weather_forecast",
        description:
          "Gets the current weather temperature for a given location.",
        parameters: {
          type: Type.OBJECT,
          properties: {
            location: {
              type: Type.STRING,
            },
          },
          required: ["location"],
        },
      },
      {
        name: "set_thermostat_temperature",
        description: "Sets the thermostat to a desired temperature.",
        parameters: {
          type: Type.OBJECT,
          properties: {
            temperature: {
              type: Type.NUMBER,
            },
          },
          required: ["temperature"],
        },
      },
    ],
  },
];

// Prompt for the model
let contents = [
  {
    role: "user",
    parts: [
      {
        text: "If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
      },
    ],
  },
];

// Loop until the model has no more function calls to make
while (true) {
  const result = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents,
    config: { tools },
  });

  if (result.functionCalls && result.functionCalls.length > 0) {
    const functionCall = result.functionCalls[0];

    const { name, args } = functionCall;

    if (!toolFunctions[name]) {
      throw new Error(`Unknown function call: ${name}`);
    }

    // Call the function and get the response.
    const toolResponse = toolFunctions[name](args);

    const functionResponsePart = {
      name: functionCall.name,
      response: {
        result: toolResponse,
      },
      id: functionCall.id,
    };

    // Send the function response back to the model.
    contents.push({
      role: "model",
      parts: [
        {
          functionCall: functionCall,
        },
      ],
    });
    contents.push({
      role: "user",
      parts: [
        {
          functionResponse: functionResponsePart,
        },
      ],
    });
  } else {
    // No more function calls, break the loop.
    console.log(result.text);
    break;
  }
}
```

**अनुमानित आउटपुट**

कोड चलाने पर, आपको दिखेगा कि SDK फ़ंक्शन कॉल को व्यवस्थित कर रहा है. मॉडल पहले `get_weather_forecast` को कॉल करता है, तापमान की जानकारी पाता है, और फिर प्रॉम्प्ट में दिए गए लॉजिक के आधार पर सही वैल्यू के साथ `set_thermostat_temperature` को कॉल करता है.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. It's 25°C in London, so I've set the thermostat to 20°C.
```

फ़ंक्शन कॉलिंग की सुविधा, [Live
API](https://ai.google.dev/gemini-api/docs/live?hl=hi) की एक नेटिव सुविधा है. इसका मतलब है कि Live API, Python SDK की तरह फ़ंक्शन कॉल को हैंडल कर सकता है.

### Python

```
# Light control schemas
turn_on_the_lights_schema = {'name': 'turn_on_the_lights'}
turn_off_the_lights_schema = {'name': 'turn_off_the_lights'}

prompt = """
  Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
  """

tools = [
    {'code_execution': {}},
    {'function_declarations': [turn_on_the_lights_schema, turn_off_the_lights_schema]}
]

await run(prompt, tools=tools, modality="AUDIO")
```

### JavaScript

```
// Light control schemas
const turnOnTheLightsSchema = { name: 'turn_on_the_lights' };
const turnOffTheLightsSchema = { name: 'turn_off_the_lights' };

const prompt = `
  Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
`;

const tools = [
  { codeExecution: {} },
  { functionDeclarations: [turnOnTheLightsSchema, turnOffTheLightsSchema] }
];

await run(prompt, tools=tools, modality="AUDIO")
```

## फ़ंक्शन कॉलिंग मोड

Gemini API की मदद से, यह कंट्रोल किया जा सकता है कि मॉडल, उपलब्ध कराए गए टूल (फ़ंक्शन के बारे में जानकारी) का इस्तेमाल कैसे करे. खास तौर पर, `function_calling_config` में जाकर मोड सेट किया जा सकता है.

- `VALIDATED`: टूल कॉम्बिनेशन के लिए डिफ़ॉल्ट मोड (जब पहले से मौजूद टूल या स्ट्रक्चर्ड आउटपुट भी चालू हों). मॉडल को फ़ंक्शन कॉल या नेचुरल लैंग्वेज का अनुमान लगाने के लिए सीमित किया गया है. साथ ही, यह पक्का किया गया है कि फ़ंक्शन स्कीमा का पालन किया गया हो. अगर `allowed_function_names` नहीं दिया जाता है, तो मॉडल, फ़ंक्शन के उपलब्ध सभी एलान में से किसी एक को चुनता है. अगर `allowed_function_names` दिया जाता है, तो मॉडल, अनुमति वाले फ़ंक्शन के सेट में से कोई फ़ंक्शन चुनता है. यह मोड, `AUTO` मोड की तुलना में, गलत तरीके से किए गए फ़ंक्शन कॉल की संख्या को कम करता है.
- `AUTO`: सिर्फ़ function\_declarations टूल चालू होने पर डिफ़ॉल्ट मोड.
  मॉडल, प्रॉम्प्ट और कॉन्टेक्स्ट के आधार पर यह तय करता है कि नैचुरल लैंग्वेज में जवाब जनरेट करना है या फ़ंक्शन कॉल का सुझाव देना है.
- `ANY`: मॉडल को हमेशा फ़ंक्शन कॉल का अनुमान लगाने के लिए बाध्य किया जाता है. साथ ही, यह फ़ंक्शन स्कीमा के मुताबिक काम करता है. अगर `allowed_function_names` तय नहीं किया गया है, तो मॉडल, दिए गए किसी भी फ़ंक्शन के एलान में से किसी एक को चुन सकता है.
  अगर `allowed_function_names` को सूची के तौर पर दिया जाता है, तो मॉडल सिर्फ़ उस सूची में मौजूद फ़ंक्शन चुन सकता है. इस मोड का इस्तेमाल तब करें, जब आपको हर प्रॉम्प्ट के लिए फ़ंक्शन कॉल के जवाब की ज़रूरत हो (अगर लागू हो).
- `NONE`: मॉडल को फ़ंक्शन कॉल करने की *अनुमति नहीं है*. यह किसी फ़ंक्शन के बारे में जानकारी दिए बिना अनुरोध भेजने के बराबर है. इसका इस्तेमाल, टूल के डेफ़िनिशन को हटाए बिना, फ़ंक्शन कॉलिंग को कुछ समय के लिए बंद करने के लिए करें.

### Python

```
from google.genai import types

# Configure function calling mode
tool_config = types.ToolConfig(
    function_calling_config=types.FunctionCallingConfig(
        mode="ANY", allowed_function_names=["get_current_temperature"]
    )
)

# Create the generation config
config = types.GenerateContentConfig(
    tools=[tools],  # not defined here.
    tool_config=tool_config,
)
```

### JavaScript

```
import { FunctionCallingConfigMode } from '@google/genai';

// Configure function calling mode
const toolConfig = {
  functionCallingConfig: {
    mode: FunctionCallingConfigMode.ANY,
    allowedFunctionNames: ['get_current_temperature']
  }
};

// Create the generation config
const config = {
  tools: tools, // not defined here.
  toolConfig: toolConfig,
};
```

## फ़ंक्शन को अपने-आप कॉल करने की सुविधा (सिर्फ़ Python के लिए)

Python SDK का इस्तेमाल करते समय, Python फ़ंक्शन को सीधे तौर पर टूल के तौर पर इस्तेमाल किया जा सकता है.
एसडीके इन फ़ंक्शन को डिक्लेरेशन में बदलता है. साथ ही, फ़ंक्शन कॉल के एक्ज़ीक्यूशन को मैनेज करता है और आपके लिए रिस्पॉन्स साइकल को हैंडल करता है. टाइप हिंट और डॉकस्ट्रिंग के साथ अपने फ़ंक्शन को तय करें. बेहतर नतीजों के लिए, हमारा सुझाव है कि आप [Google-स्टाइल वाली डॉकस्ट्रिंग](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods) का इस्तेमाल करें.
इसके बाद, SDK अपने-आप ये काम करेगा:

1. मॉडल से मिले फ़ंक्शन कॉल के जवाबों का पता लगाना.
2. अपने कोड में, उससे जुड़ा Python फ़ंक्शन कॉल करें.
3. फ़ंक्शन के जवाब को मॉडल को वापस भेजें.
4. मॉडल से मिले टेक्स्ट वाले जवाब को दिखाता है.

फ़िलहाल, एसडीके जनरेट किए गए फ़ंक्शन के एलान की प्रॉपर्टी के ब्यौरे वाले स्लॉट में, आर्ग्युमेंट के ब्यौरे को पार्स नहीं करता है. इसके बजाय, यह पूरी डॉकस्ट्रिंग को टॉप-लेवल फ़ंक्शन के ब्यौरे के तौर पर भेजता है.

### Python

```
from google import genai
from google.genai import types

# Define the function with type hints and docstring
def get_current_temperature(location: str) -> dict:
    """Gets the current temperature for a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA

    Returns:
        A dictionary containing the temperature and unit.
    """
    # ... (implementation) ...
    return {"temperature": 25, "unit": "Celsius"}

# Configure the client
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[get_current_temperature]
)  # Pass the function itself

# Make the request
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What's the temperature in Boston?",
    config=config,
)

print(response.text)  # The SDK handles the function call and returns the final text
```

इन तरीकों से, फ़ंक्शन को अपने-आप कॉल करने की सुविधा बंद की जा सकती है:

### Python

```
config = types.GenerateContentConfig(
    tools=[get_current_temperature],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)
```

### फ़ंक्शन के स्कीमा का अपने-आप एलान होना

यह एपीआई, इनमें से किसी भी टाइप के बारे में जानकारी दे सकता है. `Pydantic` टाइप इस्तेमाल किए जा सकते हैं. हालांकि, यह ज़रूरी है कि उनमें तय किए गए फ़ील्ड भी इस्तेमाल किए जा सकने वाले टाइप के हों. यहां डिक्शनरी टाइप (जैसे कि `dict[str: int]`) का इस्तेमाल नहीं किया जा सकता. इसलिए, इनका इस्तेमाल न करें.

### Python

```
AllowedType = (
  int | float | bool | str | list['AllowedType'] | pydantic.BaseModel)
```

अनुमानित स्कीमा देखने के लिए, इसे [`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable) का इस्तेमाल करके बदला जा सकता है:

### Python

```
from google import genai
from google.genai import types

def multiply(a: float, b: float):
    """Returns a * b."""
    return a * b

client = genai.Client()
fn_decl = types.FunctionDeclaration.from_callable(callable=multiply, client=client)

# to_json_dict() provides a clean JSON representation.
print(fn_decl.to_json_dict())
```

## एक से ज़्यादा टूल का इस्तेमाल करना: बिल्ट-इन टूल को फ़ंक्शन कॉलिंग के साथ जोड़ना

एक ही अनुरोध में, फ़ंक्शन कॉलिंग के साथ-साथ पहले से मौजूद कई टूल को चालू किया जा सकता है.

Gemini 3 मॉडल, टूल कॉन्टेक्स्ट सर्कुलेशन की सुविधा की वजह से, बिल्ट-इन टूल को फ़ंक्शन कॉलिंग की सुविधा के साथ जोड़ सकते हैं. ज़्यादा जानने के लिए, [बिल्ट-इन टूल और फ़ंक्शन कॉलिंग को एक साथ इस्तेमाल करना](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) लेख पढ़ें.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
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

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3.6-flash",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

Gemini 3 सीरीज़ से पहले के मॉडल के लिए, [Live API](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=hi) का इस्तेमाल करें.

## टेक्स्ट, इमेज, और वीडियो वगैरह का इस्तेमाल करके की गई क्वेरी के जवाब

Gemini 3 सीरीज़ के मॉडल के लिए, फ़ंक्शन के जवाब वाले उन हिस्सों में मल्टीमॉडल कॉन्टेंट शामिल किया जा सकता है जिन्हें मॉडल को भेजा जाता है. मॉडल, इस मल्टीमॉडल कॉन्टेंट को अपने अगले टर्न में प्रोसेस कर सकता है, ताकि ज़्यादा जानकारी वाला जवाब दिया जा सके.
फ़ंक्शन के जवाबों में मल्टीमॉडल कॉन्टेंट के लिए, इन MIME टाइप का इस्तेमाल किया जा सकता है:

- **इमेज**: `image/png`, `image/jpeg`, `image/webp`
- **दस्तावेज़**: `application/pdf`, `text/plain`

किसी फ़ंक्शन के जवाब में मल्टीमॉडल डेटा शामिल करने के लिए, उसे `functionResponse` पार्ट में नेस्ट किए गए एक या उससे ज़्यादा पार्ट के तौर पर शामिल करें. मल्टीमॉडल वाले हर हिस्से में `inlineData` होना चाहिए. अगर स्ट्रक्चर्ड `response` फ़ील्ड में मल्टीमॉडल पार्ट का रेफ़रंस दिया गया है, तो उसमें एक यूनीक `displayName` होना चाहिए.

JSON रेफ़रंस फ़ॉर्मैट `{"$ref": "<displayName>"}` का इस्तेमाल करके, स्ट्रक्चर्ड `response` फ़ील्ड में मौजूद `functionResponse` पार्ट से मल्टीमॉडल पार्ट को भी रेफ़रंस किया जा सकता है. जवाब को प्रोसेस करते समय, मॉडल रेफ़रंस की जगह मल्टीमॉडल कॉन्टेंट का इस्तेमाल करता है. हर `displayName` को स्ट्रक्चर्ड `response` फ़ील्ड में सिर्फ़ एक बार रेफ़रंस किया जा सकता है.

इस उदाहरण में, `get_image` नाम के फ़ंक्शन के लिए `functionResponse` वाला मैसेज दिखाया गया है. साथ ही, इसमें `displayName: "instrument.jpg"` के साथ इमेज डेटा वाला नेस्ट किया गया हिस्सा भी दिखाया गया है. `functionResponse` के `response` फ़ील्ड में, इमेज के इस हिस्से का रेफ़रंस दिया गया है:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          id=function_call.id,
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3.6-flash',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'user',
    parts: [
      {
        functionResponse: {
          id: functionCall.id,
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData]
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3.6-flash',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "id": "UNIQUE_CALL_ID_HERE",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

## स्ट्रक्चर्ड आउटपुट के साथ फ़ंक्शन कॉलिंग

Gemini 3 सीरीज़ के मॉडल के लिए, [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) के साथ फ़ंक्शन कॉलिंग का इस्तेमाल किया जा सकता है. इससे मॉडल, किसी खास स्कीमा के मुताबिक फ़ंक्शन कॉल या आउटपुट का अनुमान लगा पाता है. इस वजह से, जब मॉडल फ़ंक्शन कॉल जनरेट नहीं करता है, तो आपको एक जैसे फ़ॉर्मैट में जवाब मिलते हैं.

## मॉडल कॉन्टेक्स्ट प्रोटोकॉल (एमसीपी)

[मॉडल कॉन्टेक्स्ट प्रोटोकॉल (एमसीपी)](https://modelcontextprotocol.io/introduction), एआई ऐप्लिकेशन को बाहरी टूल और डेटा से कनेक्ट करने के लिए एक ओपन स्टैंडर्ड है.
एमसीपी, मॉडल को कॉन्टेक्स्ट ऐक्सेस करने के लिए एक सामान्य प्रोटोकॉल उपलब्ध कराता है. जैसे, फ़ंक्शन (टूल), डेटा सोर्स (संसाधन) या पहले से तय किए गए प्रॉम्प्ट.

Gemini SDK में, MCP के लिए पहले से ही सहायता उपलब्ध है. इससे बॉयलरप्लेट कोड कम हो जाता है. साथ ही, MCP टूल के लिए [टूल को अपने-आप कॉल करने की सुविधा](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#automatic_function_calling_python_only) मिलती है. जब मॉडल, एमसीपी टूल कॉल जनरेट करता है, तो Python और JavaScript क्लाइंट एसडीके, एमसीपी टूल को अपने-आप लागू कर सकता है. साथ ही, जवाब को मॉडल को वापस भेज सकता है. यह प्रोसेस तब तक चलती रहती है, जब तक मॉडल कोई और टूल कॉल नहीं करता.

यहां Gemini और `mcp` एसडीके के साथ लोकल एमसीपी सर्वर इस्तेमाल करने का एक उदाहरण दिया गया है.

### Python

पक्का करें कि आपके चुने हुए प्लैटफ़ॉर्म पर, [`mcp` SDK](https://modelcontextprotocol.io/introduction) का नया वर्शन इंस्टॉल हो.

```
pip install mcp
```

```
import os
import asyncio
from datetime import datetime
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from google import genai

client = genai.Client()

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="npx",  # Executable
    args=["-y", "@philschmid/weather-mcp"],  # MCP Server
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Prompt to get the weather for the current day in London.
            prompt = f"What is the weather in London in {datetime.now().strftime('%Y-%m-%d')}?"

            # Initialize the connection between client and server
            await session.initialize()

            # Send request to the model with MCP function declarations
            response = await client.aio.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt,
                config=genai.types.GenerateContentConfig(
                    temperature=0,
                    tools=[session],  # uses the session, will automatically call the tool
                    # Uncomment if you **don't** want the SDK to automatically call the tool
                    # automatic_function_calling=genai.types.AutomaticFunctionCallingConfig(
                    #     disable=True
                    # ),
                ),
            )
            print(response.text)

# Start the asyncio event loop and run the main function
asyncio.run(run())
```

### JavaScript

पक्का करें कि आपके चुने हुए प्लैटफ़ॉर्म पर `mcp` SDK का नया वर्शन इंस्टॉल हो.

```
npm install @modelcontextprotocol/sdk
```

 दें.

```
import { GoogleGenAI, FunctionCallingConfigMode , mcpToTool} from '@google/genai';
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

// Create server parameters for stdio connection
const serverParams = new StdioClientTransport({
  command: "npx", // Executable
  args: ["-y", "@philschmid/weather-mcp"] // MCP Server
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

// Configure the client
const ai = new GoogleGenAI({});

// Initialize the connection between client and server
await client.connect(serverParams);

// Send request to the model with MCP tools
const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: `What is the weather in London in ${new Date().toLocaleDateString()}?`,
  config: {
    tools: [mcpToTool(client)],  // uses the session, will automatically call the tool
    // Uncomment if you **don't** want the sdk to automatically call the tool
    // automaticFunctionCalling: {
    //   disable: true,
    // },
  },
});
console.log(response.text)

// Close the connection
await client.close();
```

### एमसीपी की सुविधा के साथ काम करने की सीमाएं

हमारे एसडीके में, एमसीपी की सुविधा पहले से मौजूद होती है. यह [एक्सपेरिमेंट के तौर पर](https://ai.google.dev/gemini-api/docs/models?hl=hi#preview) उपलब्ध है. इसकी कुछ सीमाएं हैं:

- सिर्फ़ टूल इस्तेमाल किए जा सकते हैं. संसाधन या प्रॉम्प्ट नहीं
- यह Python और JavaScript/TypeScript SDK के लिए उपलब्ध है.
- आने वाली रिलीज़ में, बड़े बदलाव हो सकते हैं.

अगर ये सर्वर, आपकी ज़रूरत के हिसाब से काम नहीं करते हैं, तो एमसीपी सर्वर को मैन्युअल तरीके से इंटिग्रेट किया जा सकता है.

## इन मॉडल के साथ काम करता है

इस सेक्शन में, मॉडल और उनके फ़ंक्शन कॉल करने की क्षमताओं के बारे में बताया गया है. इसमें एक्सपेरिमेंट के तौर पर उपलब्ध मॉडल शामिल नहीं हैं. [मॉडल की खास जानकारी](https://ai.google.dev/gemini-api/docs/models?hl=hi) पेज पर जाकर, Gemini Pro 1.5 की सभी क्षमताओं के बारे में जानकारी पाई जा सकती है.

| मॉडल | फ़ंक्शन कॉलिंग | पैरलल फ़ंक्शन कॉलिंग | कॉम्पोज़िशनल फ़ंक्शन कॉलिंग |
| --- | --- | --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=hi) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=hi) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Pro की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=hi) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=hi) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ | ✔️ | ✔️ |

## सबसे सही तरीके

- **फ़ंक्शन और पैरामीटर के बारे में जानकारी:** इनके बारे में जानकारी देते समय, साफ़ तौर पर और सटीक तरीके से बताएं. मॉडल, सही फ़ंक्शन चुनने और सही आर्ग्युमेंट देने के लिए इन पर निर्भर करता है.
- **नाम:** फ़ंक्शन के ऐसे नाम इस्तेमाल करें जिनसे उनके काम के बारे में पता चलता हो. इन नामों में स्पेस, अवधि या डैश नहीं होने चाहिए.
- **स्ट्रॉन्ग टाइपिंग:** गड़बड़ियों को कम करने के लिए, पैरामीटर के लिए खास टाइप (पूर्णांक, स्ट्रिंग, enum) का इस्तेमाल करें. अगर किसी पैरामीटर के लिए मान्य वैल्यू का सेट सीमित है, तो enum का इस्तेमाल करें.
- **टूल चुनना:** मॉडल, किसी भी संख्या में टूल का इस्तेमाल कर सकता है. हालांकि, बहुत ज़्यादा टूल उपलब्ध कराने से, गलत या ज़रूरत के हिसाब से सही न होने वाले टूल को चुनने का जोखिम बढ़ सकता है. सबसे अच्छे नतीजे पाने के लिए, कॉन्टेक्स्ट या टास्क के हिसाब से सिर्फ़ काम के टूल उपलब्ध कराएं. हमारा सुझाव है कि एक्टिव सेट में ज़्यादा से ज़्यादा 10 से 20 टूल रखें. अगर आपके पास कई टूल हैं, तो बातचीत के कॉन्टेक्स्ट के आधार पर डाइनैमिक टूल चुनने की सुविधा का इस्तेमाल करें.
- **प्रॉम्प्ट इंजीनियरिंग:**
  - संदर्भ दें: मॉडल को उसकी भूमिका के बारे में बताएं. उदाहरण के लिए, "तुम मौसम की जानकारी देने वाले एक मददगार असिस्टेंट हो.").
  - निर्देश दें: यह बताएं कि फ़ंक्शन का इस्तेमाल कब और कैसे करना है. उदाहरण के लिए, "तारीखों का अनुमान न लगाएं; पूर्वानुमान के लिए हमेशा आने वाली तारीख का इस्तेमाल करें.").
  - ज़्यादा जानकारी के लिए सवाल पूछने को बढ़ावा देना: मॉडल को निर्देश दें कि अगर ज़रूरत हो, तो वह ज़्यादा जानकारी के लिए सवाल पूछे.
  - इन प्रॉम्प्ट को डिज़ाइन करने की अन्य रणनीतियों के लिए, [एजेंटिक वर्कफ़्लो](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=hi#agentic-workflows) देखें. यहां, जांच किए गए [सिस्टम के निर्देश](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=hi#agentic-si-template) का एक उदाहरण दिया गया है.
- **तापमान:** फ़ंक्शन कॉल को ज़्यादा भरोसेमंद और सटीक बनाने के लिए, कम तापमान (जैसे, 0) का इस्तेमाल करें.
- **पुष्टि करना:** अगर फ़ंक्शन कॉल के गंभीर नतीजे होते हैं (जैसे, ऑर्डर देना), तो उसे पूरा करने से पहले उपयोगकर्ता से पुष्टि करें.
- **जवाब जनरेट न होने की वजह देखें:** मॉडल के जवाब में मौजूद [`finishReason`](https://ai.google.dev/api/generate-content?hl=hi#FinishReason) को हमेशा देखें. इससे उन मामलों को हैंडल करने में मदद मिलती है जिनमें मॉडल, फ़ंक्शन कॉल जनरेट नहीं कर सका.
- **गड़बड़ी ठीक करना**: अपने फ़ंक्शन में गड़बड़ी ठीक करने की बेहतर सुविधा लागू करें, ताकि अचानक मिलने वाले इनपुट या एपीआई के काम न करने की समस्या को आसानी से ठीक किया जा सके. ऐसे सूचना देने वाले गड़बड़ी के मैसेज दिखाएं जिनका इस्तेमाल मॉडल, उपयोगकर्ता को काम के जवाब देने के लिए कर सके.
- **सुरक्षा:** बाहरी एपीआई को कॉल करते समय, सुरक्षा का ध्यान रखें. पुष्टि करने और अनुमति देने के सही तरीकों का इस्तेमाल करें. फ़ंक्शन कॉल में संवेदनशील डेटा को ज़ाहिर न करें.
- **टोकन की सीमाएं:** फ़ंक्शन की जानकारी और पैरामीटर, इनपुट टोकन की सीमा में गिने जाते हैं. अगर टोकन की सीमाएं पूरी हो रही हैं, तो फ़ंक्शन की संख्या या जानकारी की लंबाई को सीमित करें. साथ ही, मुश्किल टास्क को छोटे-छोटे, ज़्यादा फ़ोकस वाले फ़ंक्शन सेट में बांटें.
- **बैश और कस्टम टूल का मिक्सचर** बैश और कस्टम टूल का मिक्सचर इस्तेमाल करने वाले लोगों के लिए, Gemini 3.1 Pro Preview में एक अलग एंडपॉइंट उपलब्ध है. इसे एपीआई के ज़रिए ऐक्सेस किया जा सकता है. इसे [`gemini-3.1-pro-preview-customtools`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi#gemini-31-pro-preview-customtools) कहा जाता है.

## टूल से पहले टेक्स्ट की ज़रूरी शर्तों को पूरा करने के तरीके

**समस्या:** अगर आपके प्रॉम्प्ट में मॉडल को स्ट्रक्चर्ड टेक्स्ट (एक्सएमएल, YAML, JSON वगैरह) आउटपुट करने के लिए कहा गया है (जैसे, `<UPDATE>...</UPDATE>`) टूल कॉल करने से ठीक पहले, टूल कॉल कभी-कभी `Malformed_Function_Call` के साथ फ़ेल हो सकता है.

**समाधान:** इस समस्या को हल करने के लिए, यहां दिए गए तरीके अपनाएं:

- **सुझाया गया तरीका:** मॉडल को निर्देश दें कि वह टूल से पहले के नोट, रॉ टेक्स्ट के बजाय `update()` फ़ंक्शन कॉल के अंदर रखे. इसके बारे में यहां ज़्यादा जानकारी दी गई है.
- मॉडल को निर्देश दें कि वह स्ट्रक्चर्ड टेक्स्ट के बजाय, Markdown हेडर (`# UPDATE`, `## PLAN`) के तौर पर नोट लिखे.
- मॉडल को टूल कॉल से पहले टेक्स्ट आउटपुट करने की ज़रूरत नहीं है.

### सुझाया गया तरीका: वर्किंग नोट को किसी फ़ंक्शन कॉल में रैप करें

मूल निर्देश के बजाय:

```
Before calling a tool, in every response you MUST first output a single `<UPDATE>` part as specified, don't skip this part or any of required sub-tags with<in `UP>DATE`.
```

अपडेट किए गए इस निर्देश का इस्तेमाल करें:

```
Before calling any other tool, in every response you MUST first call `update` with all required parameters (previous_step, plan, next_step, external).
```

साथ ही, ग्राहक के अनुरोध में `<UPDATE>` XML फ़ॉर्मैट के सभी रेफ़रंस अपडेट करें. इसके बाद, अपडेट फ़ंक्शन के लिए फ़ंक्शन का एलान जोड़ें:

```
{
  "name": "update",
  "description": "Update working notes (previous step analysis, plan, next step, external note).",
  "parameters": {
    "type": "OBJECT",
    "properties": {
      "previous_step": {
        "type": "STRING",
        "description": "Key findings and outcomes since the previous step."
      },
      "plan": {
        "type": "STRING",
        "description": "The current status of the plan."
      },
      "next_step": {
        "type": "STRING",
        "description": "Brief explanation of the immediate next action according to the plan."
      },
      "external": {
        ";type": "STRING",
        "description": "A short, plain-language note shown to the User about what you are ABOUT TO DO next."
      }
    },
    "required": [
      "previous_step",
      "plan",
      "next_step",
      "external"
    ]
  }
}
```

इसके बाद, मॉडल एक ही चरण में दो कॉल करेगा: पहला, `update()` कॉल, जो स्ट्रक्चर्ड एक्सएमएल को बदलता है. दूसरा, वह फ़ंक्शन कॉल जिसे मॉडल को करना है.

## अहम जानकारी और सीमाएं

- फ़ंक्शन कॉल के हिस्सों की पोज़िशन: कस्टम फ़ंक्शन के एलान [के साथ-साथ, बिल्ट-इन टूल](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) (जैसे कि Google Search) का इस्तेमाल करने पर, मॉडल एक ही टर्न में `functionCall`, `toolCall`, और `toolResponse` के हिस्सों को मिलाकर जवाब दे सकता है. इस वजह से, यह न मान लें कि `functionCall` हमेशा पार्ट्स ऐरे में आखिरी आइटम होगा. अगर JSON रिस्पॉन्स को मैन्युअल तरीके से पार्स किया जा रहा है, तो पोज़िशन पर भरोसा करने के बजाय हमेशा parts ऐरे के हर हिस्से पर बारी-बारी से काम करें.
- सिर्फ़ [OpenAPI स्कीमा के सबसेट](https://ai.google.dev/api/caching?hl=hi#FunctionDeclaration) का इस्तेमाल किया जा सकता है.
- `ANY` मोड के लिए, एपीआई बहुत बड़े या डीपली नेस्ट किए गए स्कीमा को अस्वीकार कर सकता है. अगर आपको गड़बड़ियां मिलती हैं, तो फ़ंक्शन पैरामीटर और जवाब के स्कीमा को आसान बनाएं. इसके लिए, प्रॉपर्टी के नाम छोटे करें, नेस्टिंग कम करें या फ़ंक्शन के एलान की संख्या सीमित करें.
- Python में, इस्तेमाल किए जा सकने वाले पैरामीटर टाइप सीमित हैं.
- फ़ंक्शन को अपने-आप कॉल करने की सुविधा, सिर्फ़ Python SDK में उपलब्ध है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
