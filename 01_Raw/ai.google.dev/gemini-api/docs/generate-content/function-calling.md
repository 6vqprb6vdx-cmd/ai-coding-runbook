---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=zh-CN
fetched_at: 2026-09-07T05:31:49.991828+00:00
title: "\u4f7f\u7528 Gemini API \u8fdb\u884c\u51fd\u6570\u8c03\u7528 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 Gemini API 进行函数调用

借助函数调用，您可以将模型连接到外部工具和 API。
模型会确定何时调用特定函数，并提供执行实际操作所需的参数，而不是生成文本回答。这使得模型能够充当自然语言与实际操作和数据之间的桥梁。函数调用有 3 个主要应用场景：

- [**执行操作**：](#meeting)使用 API 与外部系统互动，例如安排预约、创建账单、发送电子邮件或控制智能家居设备。
- [**扩充知识**：](#weather)从数据库、API 和知识库等外部来源获取信息。
- [**扩展功能**：](#chart)使用外部工具执行计算，并扩展模型的功能限制，例如使用计算器或创建图表。

您可以浏览以下示例，了解这些使用情形：

### 安排会议

此示例展示了如何定义一个函数，用于在特定时间安排与参会者的会议，从而使模型能够解析用户请求并返回结构化实参，以触发外部系统中的操作。

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
    model="gemini-3.7-flash",
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
  model: 'gemini-3.7-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.7-flash:generateContent" \
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

### 获取天气信息

此示例展示了如何定义一个用于检索某个位置的温度数据的函数，从而使模型能够调用外部 API 来回答需要实时信息或外部信息的查询。

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
    model="gemini-3.7-flash",
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
  model: 'gemini-3.7-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.7-flash:generateContent" \
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

### 创建图表

此示例展示了如何定义一个可根据结构化数据生成条形图的函数，演示了模型如何使用外部工具执行计算或创建视觉资源：

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
    model="gemini-3.7-flash",
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
  model: 'gemini-3.7-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.7-flash:generateContent" \
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

## 函数调用的工作原理

![函数调用概览](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=zh-cn)

函数调用涉及应用、模型和外部函数之间的结构化互动。下面详细介绍了这个流程：

1. **定义函数声明**：在应用代码中定义函数声明。函数声明向模型描述函数的名称、参数和用途。
2. **使用函数声明调用 API**：将用户提示与函数声明一起发送给模型。它会分析请求，并确定函数调用是否有帮助。如果需要，它会返回一个结构化 JSON 对象，其中包含函数名称、实参和一个唯一的 `id`（对于 Gemini 3 模型，API 现在始终会返回此 `id`\*）。
3. **执行函数代码（您的责任）**：模型*不会*执行函数本身。应用负责处理响应并检查是否存在函数调用。如果
   - **是**：提取函数的名称、实参和 `id`，并在应用中执行相应的函数。
   - **否**：模型已直接针对提示提供文本回答（此流程在示例中不太突出，但也是可能的结果）。
4. **创建用户友好的回答**：如果执行了函数，请捕获结果并将其发送回模型，确保在后续对话轮次中包含匹配的 `id`。它将使用该结果生成最终的、用户友好的响应，其中包含函数调用的信息。

此过程可以重复多次，从而实现复杂的互动和工作流程。该模型还支持在单个对话轮次中调用多个函数（[并行函数调用](#parallel_function_calling)）、按顺序调用多个函数（[组合式函数调用](#compositional_function_calling)）以及使用内置 Gemini 工具（[多工具使用](#native-tools)）。

\* **始终映射函数 ID**：Gemini 3 现在始终会为每个 `functionCall` 返回唯一的 `id`。在 `functionResponse` 中包含此确切的 `id`，以便模型能够准确地将结果映射回原始请求。

### 第 1 步：定义函数声明

在应用代码中定义一个函数及其声明，以便用户设置光照值并发出 API 请求。此函数可以调用外部服务或 API。

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

### 第 2 步：使用函数声明调用模型

定义函数声明后，您可以提示模型使用这些声明。它会分析提示和函数声明，并决定是直接回答还是调用函数。如果调用了函数，响应对象将包含函数调用建议。

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
    model="gemini-3.7-flash",
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
  model: 'gemini-3.7-flash',
  contents: contents,
  config: config
});

console.log(response.functionCalls[0]);
```

然后，模型会返回一个 `functionCall` 对象，该对象采用与 OpenAPI 兼容的架构，用于指定如何调用一个或多个已声明的函数，以便回答用户的问题。

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

### 第 3 步：执行 set\_light\_values 函数代码

从模型的回答中提取函数调用详细信息，解析实参，然后执行 `set_light_values` 函数。

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

### 第 4 步：根据函数结果创建用户友好的回答，然后再次调用模型

最后，将函数执行结果发送回模型，以便模型将此信息纳入其对用户的最终回答中。

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
    model="gemini-3.7-flash",
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
  model: 'gemini-3.7-flash',
  contents: contents,
  config: config
});

console.log(final_response.text);
```

至此，函数调用流程已完成。模型成功使用 `set_light_values` 函数执行了用户的请求操作。

## 函数声明

在提示中实现函数调用时，您需要创建一个 `tools` 对象，其中包含一个或多个 `function declarations`。您可以使用 JSON（具体来说是 [OpenAPI 架构](https://spec.openapis.org/oas/v3.0.3#schemaw)格式的[选定子集](https://ai.google.dev/api/caching?hl=zh-cn#Schema)）来定义函数。单个函数声明可以包含以下参数：

- `name`（字符串）：函数的唯一名称（`get_weather_forecast`、`send_email`）。请使用不含空格或特殊字符的描述性名称（使用下划线或驼峰式命名法）。
- `description`（字符串）：对函数用途和功能的清晰而详细的说明。这对于模型了解何时使用函数至关重要。请具体说明，并在必要时提供示例（“根据位置查找影院，还可以选择查找目前正在影院上映的电影。”）。
- `parameters`（对象）：定义函数预期的输入参数。
  - `type`（字符串）：指定总体数据类型，例如 `object`。
  - `properties`（对象）：列出各个参数，每个参数都具有以下属性：
    - `type`（字符串）：参数的数据类型，例如 `string`、`integer`、`boolean, array`。
    - `description`（字符串）：对参数的用途和格式的说明。提供示例和限制条件（“城市和州，例如‘加利福尼亚州旧金山’或邮政编码，例如‘95616’。”）。
    - `enum`（数组，可选）：如果参数值来自固定集，请使用“enum”列出允许的值，而不是仅在说明中描述这些值。这有助于提高准确性（“枚举”：["daylight", "cool", "warm"]）。
  - `required`（数组）：一个字符串数组，列出了函数运行所必需的参数名称。

您还可以使用 `types.FunctionDeclaration.from_callable(client=client, callable=your_function)` 直接从 Python 函数构建 `FunctionDeclarations`。

## 使用思考模型进行函数调用

Gemini 3 和 2.5 系列模型使用内部[“思考”](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)过程来推理请求。这可显著提高函数调用性能，使模型能够更好地确定何时调用函数以及使用哪些参数。由于 Gemini API 是无状态的，因此模型会使用[思考特征](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=zh-cn)在多轮对话中保持上下文。

本部分介绍了如何对思维签名进行高级管理，仅在您手动构建 API 请求（例如通过 REST）或操纵对话历史记录时才需要阅读。

**如果您使用的是 [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn)（我们的官方库），则无需管理此流程**。SDK 会自动处理必要的步骤，如之前的[示例](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#step-4)所示。

### 手动管理对话历史记录

如果您手动修改对话历史记录，而不是发送[完整的上一个回答](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#step-4)，则必须正确处理模型回答中包含的 `thought_signature`。

请遵循以下规则以确保保留模型的上下文：

- 始终将 `thought_signature` 在其原始 [`Part`](https://ai.google.dev/api?hl=zh-cn#request-body-structure) 内发送回模型。
- **请务必在 `function_response` 中包含 `function_call` 中的确切 `id`，以便 API 将结果映射到正确的请求。**
- 不要将包含签名的 `Part` 与不包含签名的部分合并。这会破坏思考的位置上下文。
- 不要组合两个都包含签名的 `Parts`，因为签名字符串无法合并。

#### Gemini 3 思维签名

在 Gemini 3 中，模型回答的任何 [`Part`](https://ai.google.dev/api?hl=zh-cn#request-body-structure) 都可能包含思维签名。虽然我们通常建议从所有 `Part` 类型返回签名，但对于函数调用，必须返回思考签名。除非您手动操作对话历史记录，否则 Google GenAI SDK 会自动处理思考签名。

如果您要手动处理对话记录，请参阅[思考签名](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=zh-cn)页面，详细了解如何处理 Gemini 3 的思考签名。

##### 检查思维签名

虽然不是必需的，但您可以检查响应，以查看 `thought_signature`，用于调试或学习。

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

如需详细了解思路签名的限制和使用情况，以及一般的思考模型，请参阅[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn#signatures)页面。

## 并行函数调用

除了单轮函数调用之外，您还可以一次调用多个函数。并行函数调用可让您同时执行多个函数，适用于函数之间没有依赖关系的情况。这在以下场景中非常有用：从多个独立来源收集数据，例如从不同数据库检索客户详细信息、检查各个仓库的库存水平，或执行多项操作，例如将公寓改造成迪斯科舞厅。

当模型在单个对话轮次中发起多次函数调用时，您无需按接收 `function_call` 对象的顺序返回 `function_result` 对象。Gemini API 会使用模型输出中的 `id` 将每个结果映射回其对应的调用。这样，您就可以异步执行函数，并在函数完成时将结果附加到列表中。

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

配置函数调用模式，以允许使用所有指定的工具。
如需了解详情，您可以参阅[配置函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#function_calling_modes)。

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

chat = client.chats.create(model="gemini-3.7-flash", config=config)
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
    model: 'gemini-3.7-flash',
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

每个打印结果都反映了模型请求的单个函数调用。如需返回结果，请按请求顺序包含响应。

Python SDK 支持[自动函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#automatic_function_calling_python_only)，可自动将 Python 函数转换为声明，并为您处理函数调用执行和响应周期。以下是迪斯科用例的示例。

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
    model="gemini-3.7-flash",
    contents="Do everything you need to this place into party!",
    config=config,
)

print("\nExample 2: Automatic function calling")
print(response.text)
# I've turned on the disco ball, started playing loud and energetic music, and dimmed the lights to 50% brightness. Let's get this party started!
```

## 组合式函数调用

组合式或顺序式函数调用可让 Gemini 将多个函数调用链接在一起，以满足复杂的请求。例如，为了回答“获取我当前位置的温度”，Gemini API 可能会先调用 `get_current_location()` 函数，然后再调用以位置为参数的 `get_weather()` 函数。

以下示例演示了如何使用 Python SDK 和自动函数调用来实现组合式函数调用。

### Python

此示例使用 `google-genai` Python SDK 的自动函数调用功能。SDK 会自动将 Python 函数转换为所需的架构，在模型请求时执行函数调用，并将结果发送回模型以完成任务。

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
    model="gemini-3.7-flash",
    contents="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
    config=config,
)

# Print the final, user-facing response
print(response.text)
```

**预期输出**

运行代码时，您会看到 SDK 编排函数调用。模型首先调用 `get_weather_forecast`，接收温度，然后根据提示中的逻辑调用 `set_thermostat_temperature` 并传入正确的值。

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. I've set the thermostat to 20°C.
```

### JavaScript

此示例展示了如何使用 JavaScript/TypeScript SDK 通过手动执行循环进行组合式函数调用。

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
    model: "gemini-3.7-flash",
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

**预期输出**

运行代码时，您会看到 SDK 编排函数调用。模型首先调用 `get_weather_forecast`，接收温度，然后根据提示中的逻辑调用 `set_thermostat_temperature` 并传入正确的值。

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. It's 25°C in London, so I've set the thermostat to 20°C.
```

组合式函数调用是一项原生 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn) 功能。这意味着 Live API 可以像 Python SDK 一样处理函数调用。

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

## 函数调用模式

通过 Gemini API，您可以控制模型使用所提供工具（函数声明）的方式。具体来说，您可以在 .`function_calling_config` 中设置模式。

- `VALIDATED`：工具组合的默认模式（当内置工具或结构化输出也处于启用状态时）。模型会受到限制，只能预测函数调用或自然语言，并确保遵循函数架构。如果未提供 `allowed_function_names`，模型会从所有可用的函数声明中进行选择。如果提供了 `allowed_function_names`，模型会从一组允许的函数中进行选择。与 `AUTO` 模式相比，此模式可减少格式错误的函数调用。
- `AUTO`：仅启用 function\_declarations 工具时的默认模式。
  模型会根据提示和上下文决定是生成自然语言回答还是建议函数调用。
- `ANY`：模型会受到限制，始终预测函数调用，并确保符合函数架构。如果未指定 `allowed_function_names`，模型可以从提供的任何函数声明中进行选择。如果 `allowed_function_names` 以列表形式提供，模型只能从该列表中的函数中进行选择。如果您需要针对每个提示（如果适用）获得函数调用响应，请使用此模式。
- `NONE`：模型*不得*进行函数调用。这相当于发送不含任何函数声明的请求。使用此参数可暂时停用函数调用，而无需移除工具定义。

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

## 自动函数调用（仅限 Python）

使用 Python SDK 时，您可以直接将 Python 函数作为工具提供。
SDK 会将这些函数转换为声明，管理函数调用执行，并为您处理响应周期。使用类型提示和文档字符串定义函数。为获得最佳效果，建议使用 [Google 风格的文档字符串](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)。然后，SDK 将自动执行以下操作：

1. 检测模型返回的函数调用响应。
2. 在代码中调用相应的 Python 函数。
3. 将函数的响应发送回模型。
4. 返回模型的最终文本回答。

SDK 目前不会将实参说明解析为生成的函数声明的属性说明槽。而是将整个文档字符串作为顶级函数说明发送。

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
    model="gemini-3.7-flash",
    contents="What's the temperature in Boston?",
    config=config,
)

print(response.text)  # The SDK handles the function call and returns the final text
```

您可以使用以下方法停用自动函数调用：

### Python

```
config = types.GenerateContentConfig(
    tools=[get_current_temperature],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)
```

### 自动函数架构声明

该 API 能够描述以下任何类型。允许使用 `Pydantic` 类型，前提是这些类型上定义的字段也由允许的类型组成。此处不太支持字典类型（例如 `dict[str: int]`），请勿使用。

### Python

```
AllowedType = (
  int | float | bool | str | list['AllowedType'] | pydantic.BaseModel)
```

如需查看推断架构的实际效果，您可以使用 [`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable) 对其进行转换：

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

## 多工具使用：将内置工具与函数调用相结合

您可以启用多个工具，在同一请求中将内置工具与函数调用相结合。

借助工具上下文循环功能，Gemini 3 模型可以开箱即用地将内置工具与函数调用相结合。如需了解详情，请参阅[结合使用内置工具和函数调用](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)页面。

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
    model="gemini-3.7-flash",
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
    model="gemini-3.7-flash",
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
        type: Type.OBJECT,
        properties: {
            location: {
                type: Type.STRING,
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const response1 = await client.models.generateContent({
        model: "gemini-3.7-flash",
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

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

    const response2 = await client.models.generateContent({
        model: "gemini-3.7-flash",
        contents: history,
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });
}

run();
```

对于 Gemini 3 系列之前的模型，请使用 [Live API](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=zh-cn)。

## 多模态函数响应

对于 Gemini 3 系列模型，您可以在发送给模型的函数响应部分中添加多模态内容。模型可以在下一轮对话中处理此多模态内容，从而生成更明智的回答。
函数响应中的多模态内容支持以下 MIME 类型：

- **图片**：`image/png`、`image/jpeg`、`image/webp`
- **文档**：`application/pdf`、`text/plain`

如需在函数响应中包含多模态数据，请将其作为嵌套在 `functionResponse` 部分内的一个或多个部分。每个多模态部分都必须包含 `inlineData`。如果您在结构化 `response` 字段中引用了多模态部分，则该字段必须包含唯一的 `displayName`。

您还可以使用 JSON 引用格式 `{"$ref": "<displayName>"}` 从 `functionResponse` 部分的结构化 `response` 字段中引用多模态部分。模型在处理响应时，会将引用替换为多模态内容。每个 `displayName` 只能在结构化 `response` 字段中引用一次。

以下示例展示了一条消息，其中包含名为 `get_image` 的函数的 `functionResponse`，以及一个包含图片数据（带有 `displayName: "instrument.jpg"`）的嵌套部分。`functionResponse` 的 `response` 字段引用了此图片部分：

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
  model="gemini-3.7-flash",
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
  model="gemini-3.7-flash",
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
  model: 'gemini-3.7-flash',
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
  model: 'gemini-3.7-flash',
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.7-flash:generateContent" \
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

## 使用结构化输出的函数调用

对于 Gemini 3 系列模型，您可以将函数调用与[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)搭配使用。这样，模型就可以预测符合特定架构的函数调用或输出。这样一来，当模型不生成函数调用时，您收到的回答格式就会保持一致。

## Model Context Protocol (MCP)

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) 是一种开放标准，用于将 AI 应用与外部工具和数据连接起来。
MCP 为模型提供了一种访问上下文（例如函数 [工具]、数据源 [资源] 或预定义提示）的通用协议。

Gemini SDK 内置了对 MCP 的支持，可减少样板代码并为 MCP 工具提供[自动工具调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#automatic_function_calling_python_only)。当模型生成 MCP 工具调用时，Python 和 JavaScript 客户端 SDK 可以自动执行 MCP 工具，并在后续请求中将响应发送回模型，从而继续此循环，直到模型不再进行任何工具调用。

在此处，您可以找到一个示例，了解如何将本地 MCP 服务器与 Gemini 和 `mcp` SDK 搭配使用。

### Python

确保在所选平台上安装了最新版本的 [`mcp` SDK](https://modelcontextprotocol.io/introduction)。

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
                model="gemini-3.7-flash",
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

确保您选择的平台上安装了最新版本的 `mcp` SDK。

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
  model: "gemini-3.7-flash",
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

### 内置 MCP 支持的限制

内置 MCP 支持是我们 SDK 中的一项[实验性](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#preview)功能，具有以下限制：

- 仅支持工具，不支持资源和提示
- 适用于 Python 和 JavaScript/TypeScript SDK。
- 未来版本可能会出现重大变更。

如果这些限制影响了您构建的内容，您可以随时选择手动集成 MCP 服务器。

## 支持的模型

本部分列出了模型及其函数调用功能。不包括实验性模型。您可以在[模型概览](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)页面上找到全面的功能概览。

| 模型 | 函数调用 | 并行函数调用 | 组合式函数调用 |
| --- | --- | --- | --- |
| [Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=zh-cn) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-cn) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-cn) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-cn) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-cn) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-cn) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-cn) | ✔️ | ✔️ | ✔️ |

## 最佳做法

- **函数和参数说明**：说明应非常清晰具体。模型会根据这些信息选择正确的函数并提供适当的实参。
- **命名**：使用描述性函数名称（不含空格、英文句点或英文短划线）。
- **强类型**：为参数使用特定类型（整数、字符串、枚举）以减少错误。如果某个形参的有效值集有限，请使用枚举。
- **工具选择**：虽然模型可以使用任意数量的工具，但提供的工具过多可能会增加选择错误或次优工具的风险。为获得最佳效果，请尽量仅提供与上下文或任务相关的工具，最好将有效集保持在 10-20 个以内。如果您有大量工具，请考虑根据对话上下文动态选择工具。
- **提示工程**：
  - 提供背景信息：告知模型其角色（例如，“你是一位乐于助人的天气助理。”）。
  - 提供指令：指定如何以及何时使用函数（例如，“不要猜测日期；始终使用未来日期进行预测。”）。
  - 鼓励澄清：指示模型在需要时提出澄清性问题。
  - 如需了解有关设计这些提示的更多策略，请参阅[智能体工作流](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-cn#agentic-workflows)。以下是经过测试的[系统指令](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-cn#agentic-si-template)示例。
- **温度**：使用较低的温度（例如 0）可获得更具确定性和可靠性的函数调用。
- **验证**：如果函数调用会产生重大后果（例如下单），请在执行之前先向用户验证该调用。
- **检查完成原因**：始终检查模型回答中的 [`finishReason`](https://ai.google.dev/api/generate-content?hl=zh-cn#FinishReason)，以处理模型未能生成有效函数调用的情况。
- **错误处理**：在函数中实现稳健的错误处理机制，以妥善处理意外输入或 API 故障。返回信息丰富的错误消息，供模型用来生成对用户的实用回答。
- **安全性**：调用外部 API 时，请注意安全性。使用适当的身份验证和授权机制。避免在函数调用中公开敏感数据。
- **令牌限制**：函数说明和参数会计入输入令牌限制。如果您遇到 token 限制，请考虑限制函数数量或说明长度，将复杂的任务分解为更小、更集中的函数集。
- **混合使用 Bash 和自定义工具** 对于混合使用 Bash 和自定义工具的开发者，Gemini 3.1 Pro 预览版提供了一个单独的端点，可通过 API 调用 [`gemini-3.1-pro-preview-customtools`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn#gemini-31-pro-preview-customtools) 来使用。

## 针对工具前文本要求的解决方法

**问题**：如果您的提示要求模型输出结构化文本（XML、YAML、JSON 等），（例如 `<UPDATE>...</UPDATE>`）紧邻工具调用之前，工具调用有时可能会失败并显示 `Malformed_Function_Call`。

**解决方案**：以下解决方法可解决此问题：

- **首选**：指示模型将工具前注释放在专用的 `update()` 函数调用中，而不是放在原始文本中（详见下文）。
- 指示模型以 Markdown 标题（`# UPDATE`、`## PLAN`）而非结构化文本的形式撰写笔记。
- 不要求模型在工具调用之前输出文本。

### 首选解决方法：将工作笔记封装在专用函数调用中

原说明：

```
Before calling a tool, in every response you MUST first output a single `<UPDATE>` part as specified, don't skip this part or any of required sub-tags within `<UPDATE>`.
```

请使用以下更新后的说明：

```
Before calling any other tool, in every response you MUST first call `update` with all required parameters (previous_step, plan, next_step, external).
```

并更新客户请求中对旧 `<UPDATE>` XML 格式的所有引用。然后，为更新函数添加相应的函数声明：

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
        "type": "STRING",
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

然后，模型将在同一步骤中进行两次调用：替换结构化 XML 的 `update()` 调用，以及它想要进行的实际函数调用。

## 注释和限制

- 函数调用部分的定位：当[将自定义函数声明与内置工具](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)（例如 Google 搜索）搭配使用时，模型可能会在单个对话轮次中返回 `functionCall`、`toolCall` 和 `toolResponse` 部分的混合结果。因此，请勿假定 `functionCall` 始终是 parts 数组中的最后一项。如果您要手动解析 JSON 响应，请务必遍历 parts 数组，而不是依赖于位置。
- 仅支持 [OpenAPI 架构的一部分](https://ai.google.dev/api/caching?hl=zh-cn#FunctionDeclaration)。
- 对于 `ANY` 模式，API 可能会拒绝非常大或嵌套很深的架构。如果您遇到错误，请尝试通过缩短属性名称、减少嵌套或限制函数声明的数量来简化函数参数和响应架构。
- Python 中支持的形参类型有限。
- 自动函数调用仅为 Python SDK 功能。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-08-26。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-08-26。"],[],[]]
