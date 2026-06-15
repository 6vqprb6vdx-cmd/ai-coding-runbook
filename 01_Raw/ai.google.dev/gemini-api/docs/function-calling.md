---
source_url: https://ai.google.dev/gemini-api/docs/function-calling?hl=de
fetched_at: 2026-06-15T06:21:57.505680+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Funktionsaufrufe mit der Gemini API

Mit Funktionsaufrufen können Sie Modelle mit externen Tools und APIs verbinden.
Anstatt Textantworten zu generieren, bestimmt das Modell, wann bestimmte Funktionen aufgerufen werden sollen, und stellt die erforderlichen Parameter zum Ausführen von Aktionen in der realen Welt bereit.
So kann das Modell als Brücke zwischen natürlicher Sprache und realen Aktionen und Daten fungieren. Funktionsaufrufe haben drei primäre Anwendungsfälle:

- [**Aktionen ausführen**](#meeting):Über APIs mit externen Systemen interagieren, z. B. Termine planen, Rechnungen erstellen, E‑Mails senden oder Smart-Home-Geräte steuern.
- [**Wissen erweitern**](#weather):Zugriff auf Informationen aus externen Quellen wie Datenbanken, APIs und Wissensdatenbanken.
- [**Funktionen erweitern**](#chart):Verwenden Sie externe Tools, um Berechnungen durchzuführen und die Einschränkungen des Modells zu erweitern, z. B. durch die Verwendung eines Taschenrechners oder das Erstellen von Diagrammen.

Unten finden Sie Beispiele für diese Anwendungsfälle:

### Besprechung planen

In diesem Beispiel wird gezeigt, wie Sie eine Funktion definieren, mit der eine Besprechung mit Teilnehmern zu einem bestimmten Zeitpunkt geplant wird. So kann das Modell Nutzeranfragen parsen und strukturierte Argumente zurückgeben, um Aktionen in externen Systemen auszulösen.

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
    model="gemini-3.5-flash",
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
  model: 'gemini-3.5-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

### Wettervorhersage

In diesem Beispiel wird gezeigt, wie Sie eine Funktion definieren, die Temperaturdaten für einen Ort abruft. So kann das Modell externe APIs aufrufen, um Anfragen zu beantworten, für die Echtzeit- oder externe Informationen erforderlich sind.

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
    model="gemini-3.5-flash",
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
  model: 'gemini-3.5-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

### Diagramm erstellen

In diesem Beispiel wird gezeigt, wie Sie eine Funktion definieren, die ein Balkendiagramm aus strukturierten Daten generiert. So wird veranschaulicht, wie das Modell externe Tools verwenden kann, um Berechnungen durchzuführen oder visuelle Elemente zu erstellen:

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
    model="gemini-3.5-flash",
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
  model: 'gemini-3.5-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

## Funktionsweise von Funktionsaufrufen

![Funktionsaufrufe – Übersicht](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=de)

Beim Funktionsaufruf findet eine strukturierte Interaktion zwischen Ihrer Anwendung, dem Modell und externen Funktionen statt. So funktioniert der Prozess:

1. **Funktionsdeklaration definieren**:Definieren Sie die Funktionsdeklaration in Ihrem Anwendungscode. Funktionsdeklarationen beschreiben dem Modell den Namen, die Parameter und den Zweck der Funktion.
2. **API mit Funktionsdeklarationen aufrufen**:Senden Sie den Nutzer-Prompt zusammen mit den Funktionsdeklarationen an das Modell. Sie analysiert die Anfrage und ermittelt, ob ein Funktionsaufruf hilfreich wäre. Wenn ja, antwortet sie mit einem strukturierten JSON-Objekt, das den Funktionsnamen, die Argumente und eine eindeutige `id` enthält (diese `id` wird jetzt immer von der API für Gemini 3-Modelle zurückgegeben\*).
3. **Funktionscode ausführen (Ihre Verantwortung)**: Das Modell *führt die Funktion nicht selbst aus*. Ihre Anwendung ist dafür verantwortlich, die Antwort zu verarbeiten und nach einem Funktionsaufruf zu suchen. Wenn
   - **Ja**: Extrahieren Sie den Namen, die Argumente und `id` der Funktion und führen Sie die entsprechende Funktion in Ihrer Anwendung aus.
   - **Nein**:Das Modell hat eine direkte Textantwort auf den Prompt gegeben. Dieser Ablauf wird im Beispiel weniger betont, ist aber ein mögliches Ergebnis.
4. **Nutzerfreundliche Antwort erstellen**:Wenn eine Funktion ausgeführt wurde, erfassen Sie das Ergebnis und senden Sie es in einer nachfolgenden Unterhaltungsrunde zurück an das Modell. Achten Sie darauf, dass Sie das entsprechende `id` einfügen. Anhand des Ergebnisses wird eine endgültige, nutzerfreundliche Antwort generiert, die die Informationen aus dem Funktionsaufruf enthält.

Dieser Prozess kann über mehrere Runden wiederholt werden, was komplexe Interaktionen und Workflows ermöglicht. Das Modell unterstützt auch das Aufrufen mehrerer Funktionen in einem einzelnen Turn ([parallele Funktionsaufrufe](#parallel_function_calling)), nacheinander ([zusammengesetzte Funktionsaufrufe](#compositional_function_calling)) und mit integrierten Gemini-Tools ([Verwendung mehrerer Tools](#native-tools)).

\* **Funktions-IDs immer zuordnen**:Gemini 3 gibt jetzt immer eine eindeutige `id` mit jedem `functionCall` zurück. Fügen Sie genau diesen `id` in Ihre `functionResponse` ein, damit das Modell Ihr Ergebnis der ursprünglichen Anfrage zuordnen kann.

### Schritt 1: Funktionsdeklaration definieren

Definieren Sie eine Funktion und ihre Deklaration in Ihrem Anwendungscode, mit der Nutzer Lichtwerte festlegen und eine API-Anfrage stellen können. Diese Funktion kann externe Dienste oder APIs aufrufen.

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

### Schritt 2: Modell mit Funktionsdeklarationen aufrufen

Nachdem Sie die Funktionsdeklarationen definiert haben, können Sie das Modell auffordern, sie zu verwenden. Es analysiert den Prompt und die Funktionsdeklarationen und entscheidet, ob es direkt antworten oder eine Funktion aufrufen soll. Wenn eine Funktion aufgerufen wird, enthält das Antwortobjekt einen Vorschlag für einen Funktionsaufruf.

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
    model="gemini-3.5-flash",
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
  model: 'gemini-3.5-flash',
  contents: contents,
  config: config
});

console.log(response.functionCalls[0]);
```

Das Modell gibt dann ein `functionCall`-Objekt in einem OpenAPI-kompatiblen Schema zurück, in dem angegeben wird, wie eine oder mehrere der deklarierten Funktionen aufgerufen werden, um die Frage des Nutzers zu beantworten.

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

### Schritt 3: Code der Funktion „set\_light\_values“ ausführen

Extrahieren Sie die Details zum Funktionsaufruf aus der Antwort des Modells, parsen Sie die Argumente und führen Sie die Funktion `set_light_values` aus.

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

### Schritt 4: Nutzerfreundliche Antwort mit Funktionsergebnis erstellen und das Modell noch einmal aufrufen

Senden Sie das Ergebnis der Funktionsausführung schließlich zurück an das Modell, damit es diese Informationen in seine endgültige Antwort an den Nutzer einbeziehen kann.

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
    model="gemini-3.5-flash",
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
  model: 'gemini-3.5-flash',
  contents: contents,
  config: config
});

console.log(final_response.text);
```

Damit ist der Ablauf für Funktionsaufrufe abgeschlossen. Das Modell hat die Funktion `set_light_values` erfolgreich verwendet, um die angeforderte Aktion des Nutzers auszuführen.

## Funktionsdeklarationen

Wenn Sie Funktionsaufrufe in einem Prompt implementieren, erstellen Sie ein `tools`-Objekt, das ein oder mehrere `function declarations` enthält. Sie definieren Funktionen mit JSON, insbesondere mit einer [ausgewählten Teilmenge](https://ai.google.dev/api/caching?hl=de#Schema) des [OpenAPI-Schemaformats](https://spec.openapis.org/oas/v3.0.3#schemaw). Eine einzelne Funktionsdeklaration kann die folgenden Parameter enthalten:

- `name` (String): Ein eindeutiger Name für die Funktion (`get_weather_forecast`, `send_email`). Verwenden Sie beschreibende Namen ohne Leerzeichen oder Sonderzeichen (verwenden Sie Unterstriche oder CamelCase).
- `description` (string): Eine klare und detaillierte Beschreibung des Zwecks und der Funktionen der Funktion. Das ist wichtig, damit das Modell weiß, wann die Funktion verwendet werden soll. Sei konkret und gib bei Bedarf Beispiele an („Findet Kinos anhand des Standorts und optional des Filmtitels, der derzeit in den Kinos läuft.“).
- `parameters` (Objekt): Definiert die Eingabeparameter, die von der Funktion erwartet werden.
  - `type` (String): Gibt den allgemeinen Datentyp an, z. B. `object`.
  - `properties` (Objekt): Listet einzelne Parameter auf, jeweils mit:
    - `type` (String): Der Datentyp des Parameters, z. B. `string`, `integer` oder `boolean, array`.
    - `description` (String): Eine Beschreibung des Zwecks und des Formats des Parameters. Geben Sie Beispiele und Einschränkungen an („Die Stadt und das Bundesland, z. B. ‚San Francisco, CA‘, oder eine Postleitzahl, z. B. ‚95616‘“).
    - `enum` (Array, optional): Wenn die Parameterwerte aus einem festen Set stammen, verwenden Sie „enum“, um die zulässigen Werte aufzulisten, anstatt sie nur in der Beschreibung zu beschreiben. Das verbessert die Genauigkeit („enum“:[„daylight“, „cool“, „warm“]).
  - `required` (Array): Ein Array von Strings mit den Parameternamen, die für die Funktion erforderlich sind.

Sie können `FunctionDeclarations` auch direkt aus Python-Funktionen mit `types.FunctionDeclaration.from_callable(client=client, callable=your_function)` erstellen.

## Funktionsaufrufe mit Thinking-Modellen

Die Modelle der Gemini 3- und 2.5-Serie verwenden einen internen [Denkprozess](https://ai.google.dev/gemini-api/docs/thinking?hl=de), um Anfragen zu bearbeiten. Dadurch wird die Leistung von Funktionsaufrufen deutlich verbessert. Das Modell kann so besser bestimmen, wann eine Funktion aufgerufen werden soll und welche Parameter verwendet werden müssen. Da die Gemini API zustandslos ist, verwenden Modelle [Gedankensignaturen](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=de), um den Kontext über mehrere Konversationsrunden hinweg beizubehalten.

In diesem Abschnitt wird die erweiterte Verwaltung von Gedanken-Signaturen behandelt. Dies ist nur erforderlich, wenn Sie API-Anfragen manuell erstellen (z. B. über REST) oder den Unterhaltungsverlauf bearbeiten.

**Wenn Sie die [Google GenAI SDKs](https://ai.google.dev/gemini-api/docs/libraries?hl=de) (unsere offiziellen Bibliotheken) verwenden, müssen Sie diesen Prozess nicht verwalten.** Die SDKs führen die erforderlichen Schritte automatisch aus, wie im vorherigen [Beispiel](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#step-4) gezeigt.

### Unterhaltungsverlauf manuell verwalten

Wenn Sie den Unterhaltungsverlauf manuell ändern, müssen Sie anstelle der [vollständigen vorherigen Antwort](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#step-4) die `thought_signature` im Zug des Modells korrekt verarbeiten.

Beachten Sie die folgenden Regeln, damit der Kontext des Modells erhalten bleibt:

- Senden Sie den `thought_signature` immer zurück an das Modell innerhalb des ursprünglichen [`Part`](https://ai.google.dev/api?hl=de#request-body-structure).
- **Fügen Sie in Ihre `function_response` immer die genaue `id` aus der `function_call` ein, damit die API das Ergebnis der richtigen Anfrage zuordnen kann.**
- Führen Sie keine `Part` mit einer Signatur mit einer ohne Signatur zusammen, da dadurch der Positionskontext des Gedankens verloren geht.
- Kombinieren Sie nicht zwei `Parts`, die beide Signaturen enthalten, da die Signaturstrings nicht zusammengeführt werden können.

#### Gedankensignaturen von Gemini 3

In Gemini 3 kann jede [`Part`](https://ai.google.dev/api?hl=de#request-body-structure) einer Modellantwort eine Gedanken-Signatur enthalten.
Wir empfehlen zwar, Signaturen für alle `Part`-Typen zurückzugeben, aber für Funktionsaufrufe ist es obligatorisch, Gedankensignaturen zurückzugeben. Sofern Sie den Unterhaltungsverlauf nicht manuell bearbeiten, werden Gedanken-Signaturen automatisch vom Google GenAI SDK verarbeitet.

Wenn Sie den Chatverlauf manuell bearbeiten, finden Sie auf der Seite [Gedankensignaturen](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=de) eine vollständige Anleitung und Details zum Umgang mit Gedankensignaturen für Gemini 3.

##### Gedankensignaturen prüfen

Die Antwort muss nicht unbedingt geprüft werden, aber Sie können sich die `thought_signature` zu Debugging- oder Lernzwecken ansehen.

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

Weitere Informationen zu Einschränkungen und zur Verwendung von Gedanken-Signaturen sowie zu Denkmodellen im Allgemeinen finden Sie auf der Seite [Denken](https://ai.google.dev/gemini-api/docs/thinking?hl=de#signatures).

## Parallele Funktionsaufrufe

Neben dem Aufrufen von Funktionen in einzelnen Zügen können Sie auch mehrere Funktionen gleichzeitig aufrufen. Mit parallelen Funktionsaufrufen können Sie mehrere Funktionen gleichzeitig ausführen. Das ist nützlich, wenn die Funktionen nicht voneinander abhängig sind. Das ist in Szenarien wie dem Erheben von Daten aus mehreren unabhängigen Quellen nützlich, z. B. beim Abrufen von Kundendetails aus verschiedenen Datenbanken, beim Prüfen von Lagerbeständen in verschiedenen Lagern oder beim Ausführen mehrerer Aktionen wie dem Umwandeln Ihrer Wohnung in eine Disco.

Wenn das Modell mehrere Funktionsaufrufe in einem einzigen Zug initiiert, müssen Sie die `function_result`-Objekte nicht in derselben Reihenfolge zurückgeben, in der die `function_call`-Objekte empfangen wurden. Die Gemini API ordnet jedes Ergebnis mithilfe der `id` aus der Ausgabe des Modells dem entsprechenden Aufruf zu. So können Sie Ihre Funktionen asynchron ausführen und die Ergebnisse nach Abschluss an Ihre Liste anhängen.

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

Konfigurieren Sie den Funktionsaufrufmodus so, dass alle angegebenen Tools verwendet werden können.
[Weitere Informationen zum Konfigurieren von Funktionsaufrufen](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#function_calling_modes)

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

chat = client.chats.create(model="gemini-3.5-flash", config=config)
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
    model: 'gemini-3.5-flash',
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

Jedes der ausgegebenen Ergebnisse spiegelt einen einzelnen Funktionsaufruf wider, den das Modell angefordert hat. Senden Sie die Ergebnisse in derselben Reihenfolge zurück, in der sie angefordert wurden.

Das Python SDK unterstützt den [automatischen Funktionsaufruf](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#automatic_function_calling_python_only), bei dem Python-Funktionen automatisch in Deklarationen umgewandelt werden und der Ausführungs- und Antwortzyklus des Funktionsaufrufs für Sie übernommen wird. Im Folgenden finden Sie ein Beispiel für den Anwendungsfall „Disco“.

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
    model="gemini-3.5-flash",
    contents="Do everything you need to this place into party!",
    config=config,
)

print("\nExample 2: Automatic function calling")
print(response.text)
# I've turned on the disco ball, started playing loud and energetic music, and dimmed the lights to 50% brightness. Let's get this party started!
```

## Zusammengesetzte Funktionsaufrufe

Durch die Komposition oder das sequenzielle Aufrufen von Funktionen kann Gemini mehrere Funktionsaufrufe verketten, um eine komplexe Anfrage zu bearbeiten. Um beispielsweise die Frage „Wie ist die Temperatur an meinem aktuellen Standort?“ zu beantworten, ruft die Gemini API möglicherweise zuerst eine `get_current_location()`-Funktion und dann eine `get_weather()`-Funktion auf, die den Standort als Parameter verwendet.

Das folgende Beispiel zeigt, wie Sie die Komposition von Funktionsaufrufen mit dem Python SDK und automatischen Funktionsaufrufen implementieren.

### Python

In diesem Beispiel wird die automatische Funktion zum Aufrufen von Funktionen des `google-genai` Python SDK verwendet. Das SDK konvertiert die Python-Funktionen automatisch in das erforderliche Schema, führt die Funktionsaufrufe aus, wenn das Modell dies anfordert, und sendet die Ergebnisse zurück an das Modell, um die Aufgabe abzuschließen.

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
    model="gemini-3.5-flash",
    contents="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
    config=config,
)

# Print the final, user-facing response
print(response.text)
```

**Erwartete Ausgabe**

Wenn Sie den Code ausführen, sehen Sie, wie das SDK die Funktionsaufrufe orchestriert. Das Modell ruft zuerst `get_weather_forecast` auf, empfängt die Temperatur und ruft dann `set_thermostat_temperature` mit dem richtigen Wert basierend auf der Logik im Prompt auf.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. I've set the thermostat to 20°C.
```

### JavaScript

In diesem Beispiel wird gezeigt, wie Sie das JavaScript-/TypeScript-SDK für zusammengesetzte Funktionsaufrufe mit einer manuellen Ausführungsschleife verwenden.

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
    model: "gemini-3.5-flash",
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

**Erwartete Ausgabe**

Wenn Sie den Code ausführen, sehen Sie, wie das SDK die Funktionsaufrufe orchestriert. Das Modell ruft zuerst `get_weather_forecast` auf, empfängt die Temperatur und ruft dann `set_thermostat_temperature` mit dem richtigen Wert auf, der auf der Logik im Prompt basiert.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. It's 25°C in London, so I've set the thermostat to 20°C.
```

Kompositionelle Funktionsaufrufe sind eine native [Live API](https://ai.google.dev/gemini-api/docs/live?hl=de)-Funktion. Das bedeutet, dass die Live API den Funktionsaufruf ähnlich wie das Python SDK verarbeiten kann.

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

## Modi für Funktionsaufrufe

Mit der Gemini API können Sie steuern, wie das Modell die bereitgestellten Tools (Funktionsdeklarationen) verwendet. Sie können den Modus in `function_calling_config` festlegen.

- `VALIDATED`: Standardmodus für die Kombination von Tools (wenn auch integrierte Tools oder strukturierte Ausgaben aktiviert sind). Das Modell ist darauf beschränkt, entweder Funktionsaufrufe oder natürliche Sprache vorherzusagen, und sorgt für die Einhaltung des Funktionsschemas. Wenn `allowed_function_names` nicht angegeben ist, wählt das Modell aus allen verfügbaren Funktionsdeklarationen aus. Wenn `allowed_function_names` angegeben wird, wählt das Modell aus den zulässigen Funktionen aus. In diesem Modus werden weniger fehlerhafte Funktionsaufrufe generiert als im Modus `AUTO`.
- `AUTO`: Standardmodus, wenn nur das Tool „function\_declarations“ aktiviert ist.
  Das Modell entscheidet anhand des Prompts und des Kontexts, ob eine Antwort in natürlicher Sprache generiert oder ein Funktionsaufruf vorgeschlagen werden soll.
- `ANY`: Das Modell ist darauf beschränkt, immer einen Funktionsaufruf vorherzusagen, und sorgt für die Einhaltung des Funktionsschemas. Wenn `allowed_function_names` nicht angegeben ist, kann das Modell eine beliebige der bereitgestellten Funktionsdeklarationen auswählen.
  Wenn `allowed_function_names` als Liste angegeben wird, kann das Modell nur aus den Funktionen in dieser Liste auswählen. Verwenden Sie diesen Modus, wenn Sie für jeden Prompt eine Antwort auf einen Funktionsaufruf benötigen (falls zutreffend).
- `NONE`: Das Modell darf *keine* Funktionsaufrufe ausführen. Dies entspricht dem Senden einer Anfrage ohne Funktionsdeklarationen. Damit können Sie Funktionsaufrufe vorübergehend deaktivieren, ohne Ihre Tool-Definitionen zu entfernen.

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

## Automatischer Funktionsaufruf (nur Python)

Wenn Sie das Python SDK verwenden, können Sie Python-Funktionen direkt als Tools bereitstellen.
Das SDK wandelt diese Funktionen in Deklarationen um, verwaltet die Ausführung des Funktionsaufrufs und übernimmt den Antwortzyklus für Sie. Definieren Sie Ihre Funktion mit Type Hints und einem Docstring. Für optimale Ergebnisse wird empfohlen, [Docstrings im Google-Stil](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods) zu verwenden.
Das SDK führt dann automatisch folgende Aktionen aus:

1. Antworten auf Funktionsaufrufe des Modells erkennen.
2. Rufen Sie die entsprechende Python-Funktion in Ihrem Code auf.
3. Senden Sie die Antwort der Funktion zurück an das Modell.
4. Gibt die endgültige Textantwort des Modells zurück.

Das SDK parst derzeit keine Argumentbeschreibungen in die Property-Beschreibungs-Slots der generierten Funktionsdeklaration. Stattdessen wird der gesamte Docstring als Funktionsbeschreibung auf oberster Ebene gesendet.

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
    model="gemini-3.5-flash",
    contents="What's the temperature in Boston?",
    config=config,
)

print(response.text)  # The SDK handles the function call and returns the final text
```

Sie können automatische Funktionsaufrufe mit dem folgenden Befehl deaktivieren:

### Python

```
config = types.GenerateContentConfig(
    tools=[get_current_temperature],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)
```

### Automatische Deklaration des Funktionsschemas

Die API kann die folgenden Typen beschreiben. `Pydantic`-Typen sind zulässig, sofern die darin definierten Felder auch aus zulässigen Typen bestehen. Dict-Typen (z. B. `dict[str: int]`) werden hier nicht gut unterstützt. Verwenden Sie sie nicht.

### Python

```
AllowedType = (
  int | float | bool | str | list['AllowedType'] | pydantic.BaseModel)
```

Wenn Sie sehen möchten, wie das abgeleitete Schema aussieht, können Sie es mit [`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable) konvertieren:

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

## Nutzung mehrerer Tools: Integrierte Tools mit Funktionsaufrufen kombinieren

Sie können mehrere Tools aktivieren und integrierte Tools mit Funktionsaufrufen in derselben Anfrage kombinieren.

Gemini 3-Modelle können integrierte Tools und Funktionsaufrufe dank der Funktion für die Weitergabe des Tool-Kontexts kombinieren. Weitere Informationen finden Sie auf der Seite [Integrierte Tools und Funktionsaufrufe kombinieren](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de).

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
    model="gemini-3.5-flash",
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
    model="gemini-3.5-flash",
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
        model: "gemini-3.5-flash",
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

Für Modelle vor der Gemini 3-Serie verwenden Sie die [Live API](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=de).

## Multimodale Funktionsantworten

Bei Modellen der Gemini 3-Serie können Sie multimodale Inhalte in die Funktionsantwortteile einfügen, die Sie an das Modell senden. Das Modell kann diese multimodalen Inhalte in seinem nächsten Zug verarbeiten, um eine fundiertere Antwort zu generieren.
Die folgenden MIME-Typen werden für multimodale Inhalte in Funktionsantworten unterstützt:

- **Google Bilder**: `image/png`, `image/jpeg`, `image/webp`
- **Dokumente**: `application/pdf`, `text/plain`

Wenn Sie multimodale Daten in eine Funktionsantwort einfügen möchten, müssen Sie sie als einen oder mehrere Teile einfügen, die im `functionResponse`-Teil verschachtelt sind. Jeder multimodale Teil muss `inlineData` enthalten. Wenn Sie von einem strukturierten `response`-Feld aus auf einen multimodalen Teil verweisen, muss dieser eine eindeutige `displayName` enthalten.

Sie können auch von einem strukturierten `response`-Feld des `functionResponse`-Teils aus auf einen multimodalen Teil verweisen. Verwenden Sie dazu das JSON-Referenzformat `{"$ref": "<displayName>"}`. Das Modell ersetzt die Referenz durch den multimodalen Inhalt, wenn es die Antwort verarbeitet. Jeder `displayName` kann im strukturierten Feld `response` nur einmal referenziert werden.

Im folgenden Beispiel wird eine Nachricht mit einem `functionResponse` für eine Funktion mit dem Namen `get_image` und einem verschachtelten Teil mit Bilddaten mit `displayName: "instrument.jpg"` gezeigt. Das Feld `response` von `functionResponse` verweist auf diesen Bildteil:

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
  model="gemini-3.5-flash",
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
  model="gemini-3.5-flash",
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
  model: 'gemini-3.5-flash',
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
  model: 'gemini-3.5-flash',
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

## Funktionsaufrufe mit strukturierter Ausgabe

Bei Modellen der Gemini 3-Serie können Sie Funktionsaufrufe mit [strukturierter Ausgabe](https://ai.google.dev/gemini-api/docs/structured-output?hl=de) verwenden. So kann das Modell Funktionsaufrufe oder Ausgaben vorhersagen, die einem bestimmten Schema entsprechen. So erhalten Sie einheitlich formatierte Antworten, wenn das Modell keine Funktionsaufrufe generiert.

## Model Context Protocol (MCP)

Das [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) ist ein offener Standard zum Verbinden von KI-Anwendungen mit externen Tools und Daten.
MCP bietet ein gemeinsames Protokoll für den Zugriff von Modellen auf Kontext, z. B. Funktionen (Tools), Datenquellen (Ressourcen) oder vordefinierte Prompts.

Die Gemini SDKs bieten integrierte Unterstützung für das MCP, wodurch Boilerplate-Code reduziert wird und [automatische Tool-Aufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#automatic_function_calling_python_only) für MCP-Tools möglich sind. Wenn das Modell einen MCP-Tool-Aufruf generiert, können das Python- und das JavaScript-Client-SDK das MCP-Tool automatisch ausführen und die Antwort in einer nachfolgenden Anfrage an das Modell zurücksenden. Dieser Vorgang wird so lange wiederholt, bis das Modell keine weiteren Tool-Aufrufe mehr ausführt.

Hier finden Sie ein Beispiel für die Verwendung eines lokalen MCP-Servers mit Gemini und dem `mcp` SDK.

### Python

Achten Sie darauf, dass die aktuelle Version des [`mcp` SDK](https://modelcontextprotocol.io/introduction) auf der gewünschten Plattform installiert ist.

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
                model="gemini-3.5-flash",
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

Achten Sie darauf, dass die aktuelle Version des `mcp` SDK auf der von Ihnen gewählten Plattform installiert ist.

```
npm install @modelcontextprotocol/sdk
```

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
  model: "gemini-3.5-flash",
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

### Einschränkungen bei der integrierten MCP-Unterstützung

Die integrierte Unterstützung für MCP ist eine [experimentelle](https://ai.google.dev/gemini-api/docs/models?hl=de#preview) Funktion in unseren SDKs und unterliegt den folgenden Einschränkungen:

- Es werden nur Tools unterstützt, keine Ressourcen oder Prompts.
- Es ist für das Python- und das JavaScript-/TypeScript-SDK verfügbar.
- In zukünftigen Releases kann es zu nicht abwärtskompatiblen Änderungen kommen.

Die manuelle Integration von MCP-Servern ist immer eine Option, wenn diese die Entwicklung einschränken.

## Unterstützte Modelle

In diesem Abschnitt werden Modelle und ihre Funktionsaufruffunktionen aufgeführt. Experimentelle Modelle sind nicht enthalten. Eine umfassende Übersicht über die Funktionen finden Sie auf der Seite [Modellübersicht](https://ai.google.dev/gemini-api/docs/models?hl=de).

| Modell | Funktionsaufrufe | Parallele Funktionsaufrufe | Zusammengesetzte Funktionsaufrufe |
| --- | --- | --- | --- |
| [Gemini 3.1 Pro (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=de) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=de) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=de) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=de) | ✔️ | ✔️ | ✔️ |

## Best Practices

- **Funktions- und Parameterbeschreibungen**:Beschreibungen müssen äußerst klar und präzise sein. Das Modell stützt sich darauf, um die richtige Funktion auszuwählen und passende Argumente bereitzustellen.
- **Benennung**:Verwenden Sie aussagekräftige Funktionsnamen (ohne Leerzeichen, Punkte oder Bindestriche).
- **Starke Typisierung**:Verwenden Sie für Parameter bestimmte Typen (Ganzzahl, String, Enum), um Fehler zu reduzieren. Wenn ein Parameter nur eine begrenzte Anzahl gültiger Werte haben kann, verwenden Sie ein Enum.
- **Tool-Auswahl**:Das Modell kann eine beliebige Anzahl von Tools verwenden. Wenn Sie jedoch zu viele Tools bereitstellen, kann das Risiko steigen, dass ein falsches oder suboptimales Tool ausgewählt wird. Die besten Ergebnisse erzielen Sie, wenn Sie nur die relevanten Tools für den Kontext oder die Aufgabe bereitstellen und die Anzahl der aktiven Tools idealerweise auf maximal 10–20 begrenzen. Wenn Sie eine große Anzahl von Tools haben, sollten Sie die dynamische Tool-Auswahl basierend auf dem Unterhaltungskontext in Betracht ziehen.
- **Prompt Engineering**:
  - Kontext angeben: Weisen Sie dem Modell eine Rolle zu, z. B. „Du bist ein hilfreicher Wetterassistent“.
  - Geben Sie Anweisungen: Geben Sie an, wie und wann Funktionen verwendet werden sollen (z.B. „Raten Sie keine Daten; verwenden Sie für Prognosen immer ein zukünftiges Datum.“).
  - Um Klärung bitten: Weisen Sie das Modell an, bei Bedarf klärende Fragen zu stellen.
  - Weitere Strategien zum Entwerfen dieser Prompts finden Sie unter [Agentic Workflows](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=de#agentic-workflows). Hier ist ein Beispiel für eine getestete [Systemanweisung](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=de#agentic-si-template).
- **Temperatur**:Verwenden Sie eine niedrige Temperatur (z.B. 0) für deterministischere und zuverlässigere Funktionsaufrufe.
- **Validierung**:Wenn ein Funktionsaufruf erhebliche Folgen hat (z.B. eine Bestellung aufgeben), validieren Sie den Aufruf vor der Ausführung mit dem Nutzer.
- **Grund für Abschluss prüfen**:Prüfen Sie immer [`finishReason`](https://ai.google.dev/api/generate-content?hl=de#FinishReason) in der Antwort des Modells, um Fälle zu behandeln, in denen das Modell keinen gültigen Funktionsaufruf generieren konnte.
- **Fehlerbehandlung**: Implementieren Sie eine robuste Fehlerbehandlung in Ihren Funktionen, um unerwartete Eingaben oder API-Fehler ordnungsgemäß zu verarbeiten. Geben Sie informative Fehlermeldungen zurück, die das Modell verwenden kann, um hilfreiche Antworten für den Nutzer zu generieren.
- **Sicherheit**:Achten Sie beim Aufrufen externer APIs auf die Sicherheit. Verwenden Sie geeignete Authentifizierungs- und Autorisierungsmechanismen. Vermeiden Sie die Offenlegung vertraulicher Daten in Funktionsaufrufen.
- **Tokenlimits**:Funktionsbeschreibungen und Parameter werden auf Ihr Eingabetokenlimit angerechnet. Wenn Sie Tokenlimits erreichen, sollten Sie die Anzahl der Funktionen oder die Länge der Beschreibungen begrenzen und komplexe Aufgaben in kleinere, fokussiertere Funktionsgruppen aufteilen.
- **Mischung aus Bash und benutzerdefinierten Tools**: Für Entwickler, die eine Mischung aus Bash und benutzerdefinierten Tools verwenden, ist für Gemini 3.1 Pro Preview ein separater Endpunkt über die API verfügbar, der [`gemini-3.1-pro-preview-customtools`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de#gemini-31-pro-preview-customtools) heißt.

## Hinweise und Einschränkungen

- Positionierung von Teilen des Funktionsaufrufs: Wenn Sie benutzerdefinierte Funktionsdeklarationen [zusammen mit integrierten Tools](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de) (z. B. der Google Suche) verwenden, kann das Modell in einem einzigen Zug eine Mischung aus `functionCall`-, `toolCall`- und `toolResponse`-Teilen zurückgeben. Gehen Sie daher nicht davon aus, dass `functionCall` immer das letzte Element im Array „parts“ ist. Wenn Sie die JSON-Antwort manuell parsen, sollten Sie immer das Array „parts“ durchlaufen, anstatt sich auf die Position zu verlassen.
- Es wird nur eine [Teilmenge des OpenAPI-Schemas](https://ai.google.dev/api/caching?hl=de#FunctionDeclaration) unterstützt.
- Im `ANY`-Modus lehnt die API möglicherweise sehr große oder tief verschachtelte Schemas ab. Wenn Fehler auftreten, versuchen Sie, die Schemas für Funktionsparameter und Antworten zu vereinfachen, indem Sie Eigenschaftsnamen kürzen, die Schachtelung reduzieren oder die Anzahl der Funktionsdeklarationen begrenzen.
- Die unterstützten Parametertypen in Python sind begrenzt.
- Der automatische Funktionsaufruf ist nur eine Funktion des Python SDK.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-10 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-10 (UTC)."],[],[]]
