---
source_url: https://ai.google.dev/gemini-api/docs/function-calling?hl=th
fetched_at: 2026-08-17T02:18:36.946882+00:00
title: "\u0e01\u0e32\u0e23\u0e40\u0e23\u0e35\u0e22\u0e01\u0e43\u0e0a\u0e49\u0e1f\u0e31\u0e07\u0e01\u0e4c\u0e0a\u0e31\u0e19\u0e14\u0e49\u0e27\u0e22 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การเรียกใช้ฟังก์ชันด้วย Gemini API

การเรียกใช้ฟังก์ชันช่วยให้คุณเชื่อมต่อโมเดลกับเครื่องมือและ API ภายนอกได้
แทนที่จะสร้างการตอบกลับเป็นข้อความ โมเดลจะกำหนดเวลาที่จะเรียกใช้ฟังก์ชันที่เฉพาะเจาะจงและระบุพารามิเตอร์ที่จำเป็นเพื่อดำเนินการต่างๆ ในโลกแห่งความเป็นจริง
ซึ่งช่วยให้โมเดลทำหน้าที่เป็นสะพานเชื่อมระหว่างภาษาธรรมชาติกับข้อมูลและการดำเนินการต่างๆ ในโลกแห่งความเป็นจริง การเรียกใช้ฟังก์ชันมีกรณีการใช้งานหลัก 3 กรณีดังนี้

- [**ดำเนินการ:**](#meeting) โต้ตอบกับระบบภายนอกโดยใช้ API เช่น
  การกำหนดเวลาการนัดหมาย การสร้างใบแจ้งหนี้ การส่งอีเมล หรือการควบคุม
  อุปกรณ์สมาร์ทโฮม
- [**เพิ่มพูนความรู้:**](#weather) เข้าถึงข้อมูลจากแหล่งที่มาภายนอก เช่น
  ฐานข้อมูล API และฐานความรู้
- [**ขยายขีดความสามารถ:**](#chart) ใช้เครื่องมือภายนอกเพื่อทำการคำนวณและ
  ขยายข้อจำกัดของโมเดล เช่น การใช้เครื่องคิดเลขหรือการสร้าง
  แผนภูมิ

คุณสามารถดูตัวอย่างกรณีการใช้งานเหล่านี้ได้ด้านล่าง

### กำหนดเวลาการประชุม

ตัวอย่างนี้แสดงวิธีกำหนดฟังก์ชันที่กำหนดเวลาการประชุมกับผู้เข้าร่วมในเวลาที่เฉพาะเจาะจง ซึ่งช่วยให้โมเดลแยกวิเคราะห์คำขอของผู้ใช้และแสดงอาร์กิวเมนต์ที่มีโครงสร้างเพื่อทริกเกอร์การดำเนินการในระบบภายนอกได้

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
    model="gemini-3.6-flash",
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
  model: 'gemini-3.6-flash',
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about Q3 planning.",
    "tools": [{
        "type": "function",
        "name": "schedule_meeting",
        "description": "Schedules a meeting with specified attendees at a given time and date.",
        "parameters": {
          "type": "object",
          "properties": {
            "attendees": {"type": "array", "items": {"type&quot;: "string"}},
            "date": {"type": "string"},
            "time": {"type": "string"},
            "topic": {"type": "string"}
          },
          "required": ["attendees", "date", "time", "topic"]
        }
    }]
  }'
```

### รับสภาพอากาศ

ตัวอย่างนี้แสดงวิธีกำหนดฟังก์ชันที่ดึงข้อมูลอุณหภูมิของสถานที่หนึ่งๆ ซึ่งช่วยให้โมเดลเรียกใช้ API ภายนอกเพื่อตอบคำถามที่ต้องใช้ข้อมูลแบบเรียลไทม์หรือข้อมูลภายนอกได้

### Python

```
from google import genai

weather_function = {
    "type": "function",
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

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What's the temperature in London?",
    tools=[weather_function],
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

const weatherFunctionDeclaration = {
  type: 'function',
  name: 'get_current_temperature',
  description: 'Gets the current temperature for a given location.',
  parameters: {
    type: 'object',
    properties: {
      location: {
        type: 'string',
        description: 'The city name, e.g. San Francisco',
      },
    },
    required: ['location'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: "What's the temperature in London?",
  tools: [weatherFunctionDeclaration],
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What'\''s the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type";: "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

### สร้างแผนภูมิ

ตัวอย่างนี้แสดงวิธีกำหนดฟังก์ชันที่สร้างแผนภูมิแท่งจากข้อมูลที่มีโครงสร้าง ซึ่งแสดงให้เห็นว่าโมเดลใช้เครื่องมือภายนอกเพื่อทำการคำนวณหรือสร้างชิ้นงานแบบภาพได้อย่างไร

### Python

```
from google import genai

create_chart_function = {
    "type": "function",
    "name": "create_bar_chart",
    "description": "Creates a bar chart given a title, labels, and values.",
    "parameters": {
        "type": "object",
        "properties": {
            "title": {"type": "string", "description": "The title for the chart."},
            "labels": {"type": "array", "items": {"type": "string"}},
            "values": {"type": "array", "items": {"type": "number"}},
        },
        "required": ["title", "labels", "values"],
    },
}

client = genai.Client()

interaction = client.interactions.create(
    model=";gemini-3.6-flash",
    input="Create a bar chart titled 'Quarterly Sales' with Q1: 50000, Q2: 75000, Q3: 60000.",
    tools=[create_chart_function],
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

const createChartFunctionDeclaration = {
  type: 'function',
  name: 'create_bar_chart',
  description: 'Creates a bar chart given a title, labels, and values.',
  parameters: {
    type: 'object',
    properties: {
      title: { type: 'string', description: 'The title for the chart.' },
      labels: { type: 'array', items: { type: 'string' } },
      values: { type: 'array', items: { type: 'number' } },
    },
    required: ['title', 'labels', 'values'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: "Create a bar chart titled 'Quarterly Sales' with Q1: 50000, Q2: 75000, Q3: 60000.",
  tools: [createChartFunctionDeclaration],
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`${step.name}(${JSON.stringify(step.arguments)})`);
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Create a bar chart titled '\''Quarterly Sales'\'' with Q1: 50000, Q2: 75000, Q3: 60000.",
    "tools": [{
        "type": "function",
        "name": "create_bar_chart",
        "description": "Creates a bar chart given a title, labels, and values.",
        "parameters": {
          "type": "object",
          "properties": {
            "title": {"type": "string"},
            "labels": {"type": "array", "items": {"type": "string"}},
            "values": {"type": "array", "items": {"type": "number"}}
          },
          "required": ["title", "labels", "values"]
        }
    }]
  }'
```

## วิธีการทำงานของการเรียกใช้ฟังก์ชัน

![ภาพรวมการเรียกใช้ฟังก์ชัน](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=th)

การเรียกใช้ฟังก์ชันเกี่ยวข้องกับการโต้ตอบที่มีโครงสร้างระหว่างแอปพลิเคชัน โมเดล และฟังก์ชันภายนอก ดังนี้

1. **กำหนดการประกาศฟังก์ชัน:** กำหนดชื่อ พารามิเตอร์ และวัตถุประสงค์ของฟังก์ชันให้กับโมเดล
2. **เรียกใช้ LLM ด้วยการประกาศฟังก์ชัน:** ส่งพรอมต์ของผู้ใช้พร้อมกับการประกาศฟังก์ชันไปยังโมเดล
3. **เรียกใช้โค้ดฟังก์ชัน (ความรับผิดชอบของคุณ):** โมเดล *ไม่*
   เรียกใช้ฟังก์ชันด้วยตัวเอง แยกชื่อและอาร์กิวเมนต์ แล้วเรียกใช้ในแอปพลิเคชัน
4. **สร้างการตอบกลับที่เข้าใจง่าย:** ส่งผลลัพธ์กลับไปยังโมเดลเพื่อรับการตอบกลับสุดท้ายที่เข้าใจง่าย

คุณสามารถทำกระบวนการนี้ซ้ำได้หลายครั้ง โมเดลรองรับการเรียกใช้ฟังก์ชันหลายรายการในครั้งเดียว ([การเรียกใช้ฟังก์ชันแบบขนาน](#parallel_function_calling)) และตามลำดับ ([การเรียกใช้ฟังก์ชันแบบผสม](#compositional_function_calling))

### ขั้นตอนที่ 1: กำหนดการประกาศฟังก์ชัน

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
                "enum": ["daylight", "cool&>quot;, "warm"],
                "description": "Color temperature",
            },
        },
        "required": ["brightness", "color_temp"],
    },
}

def set_light_values(brightness: int, color_temp: str) - dict:
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

### ขั้นตอนที่ 2: เรียกใช้โมเดลด้วยการประกาศฟังก์ชัน

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Turn the lights down to a romantic level",
    tools=[set_light_values_declaration],
)

fc_step = next(s for s in interaction.steps if s.type == "function_call")
print(fc_step)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: 'Turn the lights down to a romantic level',
  tools: [setLightValuesTool],
});

const fcStep = in>teraction.steps.find(s = s.type === 'function_call');
console.log(fcStep);
```

โมเดลจะแสดงผลขั้นตอน `function_call` พร้อม `type`, `name` และ `arguments` ดังนี้

```
type='function_call'
name='set_light_values'
arguments={'color_temp': &#39;warm', 'brightness': 25}
```

### ขั้นตอนที่ 3: เรียกใช้ฟังก์ชัน

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

### ขั้นตอนที่ 4: ส่งผลลัพธ์กลับไปยังโมเดล

### Python

```
final_interaction = client.interactions.create(
    model="gemini-3.6-flash",
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

print(final_interaction.output_text)
```

### JavaScript

```
const finalInteraction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: [{
    type: 'function_result',
    name: fcStep.name,
    call_id: fcStep.id,
    result: [{ type: 'text', text: JSON.stringify(result) }]
  }],
  tools: [setLightValuesTool],
  previous_interaction_id: interaction.id,
});

console.log(finalInteraction.output_text);
```

### การเรียกใช้ฟังก์ชันแบบ Stateless

นอกจากนี้ คุณยังใช้การเรียกใช้ฟังก์ชันในโหมด Stateless ได้ด้วยการจัดการประวัติการสนทนาในฝั่งไคลเอ็นต์และตั้งค่า `store=false`

ในโหมด Stateless คุณต้องส่งประวัติการสนทนาทั้งหมดในช่อง `input` ของคำขอที่ตามมาแต่ละรายการ ประวัติการสนทนานี้ต้องมีข้อมูลต่อไปนี้ 1. ขั้นตอน `user_input` เริ่มต้น
2. ขั้นตอนทั้งหมดที่โมเดลสร้างขึ้นและแสดงผลใน Turn 1 (รวมถึงขั้นตอน `thought` และ `function_call`) ตรงตามที่ได้รับ
3. ขั้นตอน `function_result` ที่มีเอาต์พุตของฟังก์ชันที่เรียกใช้

### Python

```
from google import genai
import json

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "Turn the lights down to a romantic level"}]
    }
]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history,
    tools=[set_light_values_declaration],
)

for step in interaction.steps:
    history.append(step.model_dump())

fc_step = next(s for s in interaction.steps if s.type == "function_call")
if fc_step.name == "set_light_values":
    result = set_light_values(**fc_step.arguments)

history.append({
    "type": "function_result",
    "name": fc_step.name,
    "call_id": fc_step.id,
    "result": [{"type": "text", "text": json.dumps(result)}],
})

final_interaction = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history,
    tools=[set_light_values_declaration],
)

print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const history = [
    {
      type: "user_input",
      content: [{ type: "text", text: "Turn the lights down to a romantic level" }]
    }
  ];

  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    store: false,
    input: history,
    tools: [setLightValuesTool],
  });

  history.push(...interaction.st>eps);

  const fcStep = interaction.steps.find(s = s.type === 'function_call');
  let result;
  if (fcStep.name === 'set_light_values') {
    result = setLightValues(fcStep.arguments.brightness, fcStep.arguments.color_temp);
  }

  history.push({
    type: 'function_result',
    name: fcStep.name,
    call_id: fcStep.id,
    result: [{ type: 'text', text: JSON.stringify(result) }]
  });

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    store: false,
    input: history,
    tools: [setLightValuesTool],
  });

  console.log(finalInteraction.output_text);
}

await main();
```

### REST

```
# Turn 1: Send request with tools and store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "Turn the lights down to a romantic level"
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
  --argjson first_input '[{"type": "user_input", "content": "Turn the lights down to a romantic level"}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.6-flash\",
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

## การประกาศฟังก์ชัน

ระบบจะส่งการประกาศฟังก์ชันเป็นเครื่องมือและมีข้อมูลต่อไปนี้

- `type` (สตริง): ต้องเป็น `"function"` สำหรับฟังก์ชันที่กำหนดเอง
- `name` (สตริง): ชื่อฟังก์ชันที่ไม่ซ้ำกัน (ใช้ขีดล่างหรือ camelCase)
- `description` (สตริง): คำอธิบายที่ชัดเจนเกี่ยวกับวัตถุประสงค์ของฟังก์ชัน
- `parameters` (ออบเจ็กต์): พารามิเตอร์อินพุตที่ฟังก์ชันคาดหวัง
  - `type` (สตริง): ประเภทข้อมูลโดยรวม เช่น `object`
  - `properties` (ออบเจ็กต์): พารามิเตอร์แต่ละรายการที่มีประเภทและคำอธิบาย
  - `required` (อาร์เรย์): ชื่อพารามิเตอร์ที่ต้องระบุ

## การเรียกใช้ฟังก์ชันด้วยโมเดลการคิด

โมเดล Gemini 3 Series ใช้กระบวนการ ["คิด"](https://ai.google.dev/gemini-api/docs/thinking?hl=th) ภายในที่ช่วยปรับปรุงการเรียกใช้ฟังก์ชัน SDK จะจัดการ[ลายเซ็นการคิด](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=th)ให้คุณโดยอัตโนมัติ

## การเรียกใช้ฟังก์ชันแบบขนาน

เรียกใช้ฟังก์ชันหลายรายการพร้อมกันเมื่อฟังก์ชันเหล่านั้นเป็นอิสระจากกัน

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
    model="gemini-3.6-flash",
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
  model: 'gemini-3.6-flash',
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Turn this place into a party!",
    "tools": [
      {
        "type": "function",
        "name": "power_disco_ball",
        "description": "Powers the disco ball.",
        "parameters": {
          "type": "object",
          "properties": {
            "power": {"type": "boolean"}
          },
          "required": ["power"]
        }
      },
      {
        "type": "function",
        "name": "start_music",
        "description": "Play music.",
        "parameters": {
          "type": "object",
          "properties": {
            "energetic": {"type": "boolean"},
            "loud": {"type": "boolean&quot;}
          },
          "required": ["energetic", "loud"]
        }
      },
      {
        "type": "function",
        "name": "dim_lights",
        "description": "Dim the lights.",
        "parameters": {
          "type": "object",
          "properties": {
            "brightness": {"type": "number"}
          },
          "required": ["brightness"]
        }
      }
    ]
  }'
```

## การเรียกใช้ฟังก์ชันแบบผสม

เชื่อมโยงการเรียกใช้ฟังก์ชันหลายรายการเข้าด้วยกันสำหรับคำขอที่ซับซ้อน (เช่น รับสถานที่ก่อน แล้วรับสภาพอากาศของสถานที่นั้น)

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
    model="gemini-3.6-flash",
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

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherForecastTool = {
  type: 'function',
  name: 'get_weather_forecast',
  description: 'Gets the current weather temperature for a given location.',
  parameters: {
    type: 'object',
    properties: {
      location: { type: 'string', description: 'The location' },
    },
    required: ['location'],
  },
};

const setThermostatTemperatureTool = {
  type: 'function',
  name: 'set_thermostat_temperature',
  description: 'Sets the thermostat to a desired temperature.',
  parameters: {
    type: 'object',
    properties: {
      temperature: {
        type: 'integer',
        description: 'The temperature in Celsius',
      },
    },
    required: ['temperature'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: "If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise 18°C.",
  tools: [
    getWeatherForecastTool,
    setThermostatTemperatureTool,
  ],
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`Function to call: ${step.name}`);
    console.log(`Arguments: ${JSON.stringify(step.arguments)}`);
  } else if (step.content) {
    for (const part of step.content) {
      if (part.text) {
        console.log(part.text);
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "If it'\''s warmer than 20°C in London, set the thermostat to 20°C, otherwise 18°C.",
    "tools": [
      {
        "type": "function",
        "name": "get_weather_forecast",
        "description": "Gets the current weather temperature for a given location.",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {"type": "string"}
          },
          "required": ["location"]
        }
      },
      {
        "type": "function",
        "name": "set_thermostat_temperature&quot;,
        "description": "Sets the thermostat to a desired temperature.",
        "parameters": {
          "type": "object",
          "properties": {
            "temperature": {"type": "integer"}
          },
          "required": ["temperature"]
        }
      }
    ]
  }'
```

## โหมดการเรียกใช้ฟังก์ชัน

ควบคุมวิธีที่โมเดลใช้เครื่องมือโดยใช้ `tool_choice` ใน `generation_config`

- `auto` (ค่าเริ่มต้น): โมเดลจะตัดสินใจว่าจะเรียกใช้ฟังก์ชันหรือตอบกลับโดยตรง
- `any`: โมเดลจะถูกจำกัดให้คาดการณ์การเรียกใช้ฟังก์ชันเสมอ
- `none`: โมเดลจะถูกห้ามไม่ให้ทำการเรียกใช้ฟังก์ชัน
- `validated`: โมเดลจะตรวจสอบว่าฟังก์ชันเป็นไปตามสคีมา

### Python

```
generation_config = {
    "tool_choice": {
        "allowed_tools": {
            "mode": "any",
            "tools&quot;: ["get_current_temperature"]
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
      tools: ['get_current_temperature';]
    }
  }
};
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
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

## การใช้เครื่องมือหลายรายการ

คุณสามารถเปิดใช้เครื่องมือหลายรายการได้โดยรวมเครื่องมือในตัวกับการเรียกใช้ฟังก์ชันในคำขอเดียวกัน โมเดล Gemini 3 สามารถรวมเครื่องมือในตัวกับการเรียกใช้ฟังก์ชันได้ทันทีใน Interactions การส่ง `previous_interaction_id` จะหมุนเวียนบริบทของเครื่องมือในตัวโดยอัตโนมัติ

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
    {"type": "google_search"},
    get_weather               
]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=tools
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} (ID: {step.id})")
        result = {"response": "Very cold. 22 degrees Fahrenheit."}
        interaction_2 = client.interactions.create(
            model="gemini-3.6-flash",
            previous_interaction_id=interaction.id,
            tools=tools,
            input=[{
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}]
            }]
        )

        print(interaction_2.output_text)
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
    weatherTool            
];

let interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: tools
});

for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Function call: ${step.name} (ID: ${step.id})`);
        const result = {response: "Very cold. 22 degrees Fahrenheit."};
        const interaction_2 = await client.interactions.create({
            model: 'gemini-3.6-flash',
            previous_interaction_id: interaction.id,
            tools: tools,
            input: [{
                type: 'function_result',
                name: step.name,
                call_id: step.id,
                result: [{ type: 'text', text: JSON.stringify(result) }]
            }]
        });

        console.log(interaction_2.output_text);
    }
}
```

### REST

```
# Turn 1: Send request with built-in google_search tool and custom weather tool
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
    "tools": [
      {"type": "google_search"},
      {
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
          },
          "required": ["location"]
        }
      }
    ]
  }'

# Turn 2: Provide function result and pass previous_interaction_id
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "previous_interaction_id": "INTERACTION_ID",
    "tools": [
      {"type": "google_search"},
      {
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
          &quot;type": "object",
          "properties": {
            "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
          },
          "required": ["location"]
        }
      }
    ],
    "input": [
      {
        "type": "function_result",
        "name": "get_weather",
        "call_id": "call_123",
        "result": [{"type": "text", "text": "{\"response\": \"Very cold. 22 degrees Fahrenheit.\"}"}]
      }
    ]
  }'
```

## การตอบกลับของฟังก์ชันแบบมัลติโมดัล

สำหรับโมเดล Gemini 3 Series คุณสามารถรวมเนื้อหาแบบมัลติโมดัลในส่วนการตอบกลับของฟังก์ชันที่คุณส่งไปยังโมเดลได้ โมเดลสามารถประมวลผลเนื้อหาแบบมัลติโมดัลนี้ใน Turn ถัดไปเพื่อสร้างการตอบกลับที่มีข้อมูลมากขึ้น

หากต้องการรวมข้อมูลแบบมัลติโมดัลในการตอบกลับของฟังก์ชัน ให้รวมข้อมูลดังกล่าวเป็นบล็อกเนื้อหาอย่างน้อย 1 รายการในช่อง `result` ของขั้นตอน `function_result` บล็อกเนื้อหาแต่ละรายการต้องระบุ `type` (เช่น `"text"`, `"image"`)

ตัวอย่างต่อไปนี้แสดงวิธีส่งการตอบกลับของฟังก์ชันที่มีข้อมูลรูปภาพกลับไปยังโมเดลในการโต้ตอบ

### Python

```
import base64
from google import genai
import requests

client = genai.Client()

tool_call = next(s for s in interaction.steps if s.type == "function_call")

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content

base64_image_data = base64.b64encode(image_bytes).decode("utf-8")

final_interaction = client.interactions.create(
    model="gemini-3.6-flash",
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

print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const toolCall = interaction.step>s.find(s = s.type === 'function_call');

const base64ImageData = "BASE64_IMAGE_DATA";

const finalInteraction = await client.interactions.create({
    model: 'gemini-3.6-flash',
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

console.log(finalInteraction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
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

## การเรียกใช้ฟังก์ชันพร้อมเอาต์พุตที่มีโครงสร้าง

สำหรับโมเดล Gemini 3 Series ให้รวมการเรียกใช้ฟังก์ชันกับ
[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th) เพื่อ
รับการตอบกลับที่มีรูปแบบสอดคล้องกัน

## MCP (Model Context Protocol) ระยะไกล

Interactions API รองรับการเชื่อมต่อกับเซิร์ฟเวอร์ MCP ระยะไกลเพื่อให้โมเดลเข้าถึงเครื่องมือและบริการภายนอกได้ คุณระบุ `name` และ `url` ของเซิร์ฟเวอร์ในการกำหนดค่าเครื่องมือ

เมื่อใช้ MCP ระยะไกล โปรดคำนึงถึงข้อจำกัดต่อไปนี้

- **ประเภทเซิร์ฟเวอร์**: MCP ระยะไกลใช้ได้กับเซิร์ฟเวอร์ HTTP ที่สตรีมได้เท่านั้น ไม่รองรับเซิร์ฟเวอร์ SSE (Server-Sent Events)
- **การตั้งชื่อ**: ชื่อเซิร์ฟเวอร์ MCP ไม่ควรมีอักขระ `-` ให้ใช้ชื่อเซิร์ฟเวอร์ `snake_case` แทน

| ช่อง | ประเภท | ต้องระบุ | คำอธิบาย |
| --- | --- | --- | --- |
| `type` | `string` | ใช่ | ต้องเป็น `"mcp_server"` |
| `name` | `string` | ไม่ | ชื่อที่แสดงสำหรับเซิร์ฟเวอร์ MCP |
| `url` | `string` | ไม่ | URL แบบเต็มสำหรับอุปกรณ์ปลายทางของเซิร์ฟเวอร์ MCP |
| `headers` | `object` | ไม่ | คู่คีย์-ค่าที่ส่งเป็นส่วนหัว HTTP พร้อมกับคำขอแต่ละรายการที่ส่งไปยังเซิร์ฟเวอร์ (เช่น โทเค็นการตรวจสอบสิทธิ์) |
| `allowed_tools` | `array` | ไม่ | จำกัดเครื่องมือจากเซิร์ฟเวอร์ที่ Agent อาจเรียกใช้ |

### ตัวอย่าง

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Check the weather in San Francisco.",
    tools=[
        {
            "type": "mcp_server",
            "name": "weather",
            "url";: "https://gemini-api-demos.uc.r.appspot.com/mcp",
        }
    ]
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Check the weather in San Francisco.',
    tools: [
        {
            type: 'mcp_server',
            name: 'weather',
            url: 'https://gemini-api-demos.uc.r.appspot.com/mcp'
        }
    ]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.6-flash",
    "input": "Check the weather in San Francisco.",
    "tools": [
        {
            "type": "mcp_server",
            &quot;name": "weather",
            "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
        }
    ]
}'
```

## สตรีมการเรียกใช้เครื่องมือ

เมื่อใช้เครื่องมือกับการสตรีม โมเดลจะสร้างการเรียกใช้ฟังก์ชันเป็นลำดับเหตุการณ์ `step.delta` ในสตรีม คุณสามารถสตรีมอาร์กิวเมนต์ของเครื่องมือเป็นอาร์กิวเมนต์บางส่วนได้โดยใช้ `arguments` คุณต้องรวม Delta เหล่านี้เพื่อสร้างการเรียกใช้เครื่องมือที่สมบูรณ์ก่อนที่จะเรียกใช้

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
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
    } else if (evT>ype === 'interaction.completed' || evType === 'interaction.complete') {
        toolCalls = Array.from(currentCalls.values()).map(call = ({
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.6-flash",
    "input": "What is the weather in Paris?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
            "type": "object",
            "properties&quot;: {
                "location": {"type": "string", "description": "The city and state"}
            },
            "required": ["location"]
        }
    }],
    "stream": true
}'
```

## แนวทางปฏิบัติแนะนำ

- **คำอธิบายฟังก์ชันและพารามิเตอร์:** ชัดเจนและเฉพาะเจาะจง
- **การตั้งชื่อ:** ใช้ชื่อที่สื่อความหมายโดยไม่มีการเว้นวรรคหรือสัญลักษณ์พิเศษ
- **การพิมพ์ที่เข้มงวด:** ใช้ประเภทที่เฉพาะเจาะจง (จำนวนเต็ม สตริง Enum)
- **การเลือกเครื่องมือ:** ตั้งค่าเครื่องมือที่ใช้งานอยู่ไม่เกิน 10-20 รายการ
- **การเขียนพรอมต์:** ระบุบริบทและวิธีการ
- **การตรวจสอบ:** ตรวจสอบการเรียกใช้ฟังก์ชันก่อนที่จะเรียกใช้
- **การจัดการข้อผิดพลาด:** ใช้การจัดการข้อผิดพลาดที่มีประสิทธิภาพ
- **ความปลอดภัย:** ใช้การตรวจสอบสิทธิ์ที่เหมาะสมสำหรับ API ภายนอก

## วิธีแก้ปัญหาสำหรับข้อกำหนดเกี่ยวกับข้อความก่อนใช้เครื่องมือ

**ปัญหา:** หากพรอมต์กำหนดให้โมเดลแสดงผลข้อความที่มีโครงสร้าง (XML, YAML, JSON ฯลฯ) (เช่น `<UPDATE>...</UPDATE>`) ทันทีก่อนที่จะทำการเรียกใช้เครื่องมือ การเรียกใช้เครื่องมืออาจล้มเหลวเป็นครั้งคราวโดยมีข้อความแสดงข้อผิดพลาด `Malformed_Function_Call`

**วิธีแก้ปัญหา:** วิธีแก้ปัญหาต่อไปนี้จะช่วยแก้ปัญหานี้ได้

- **แนะนำ:** สั่งให้โมเดลใส่หมายเหตุที่เขียนไว้ก่อนใช้เครื่องมือไว้ในการเรียกใช้ฟังก์ชัน `update()` ที่เฉพาะเจาะจงแทนที่จะเป็นข้อความธรรมดา (ดูรายละเอียดด้านล่าง)
- สั่งให้โมเดลเขียนหมายเหตุเป็นส่วนหัวมาร์กดาวน์ (`# UPDATE`, `## PLAN`) แทนที่จะเป็นข้อความที่มีโครงสร้าง
- ไม่ต้องกำหนดให้โมเดลแสดงผลข้อความก่อนการเรียกใช้เครื่องมือ

### วิธีแก้ปัญหาที่แนะนำ: ใส่หมายเหตุที่เขียนไว้ก่อนใช้เครื่องมือไว้ในการเรียกใช้ฟังก์ชันที่เฉพาะเจาะจง

แทนที่จะใช้คำสั่งเดิม

```
Before calling a tool, in every response you MUST first output a single `<UPDATE>` part as specified, don't skip this part or any of required sub-tags with<in `UP>DATE`.
```

ให้ใช้คำสั่งที่อัปเดตแล้วนี้

```
Before calling any other tool, in every response you MUST first call `update` with all required parameters (previous_step, plan, next_step, external).
```

และอัปเดตการอ้างอิงทั้งหมดไปยังรูปแบบ XML `<UPDATE>` เดิมในคำขอของลูกค้า จากนั้นเพิ่มการประกาศฟังก์ชันที่เกี่ยวข้องสำหรับฟังก์ชันอัปเดต

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

จากนั้นโมเดลจะทำการเรียกใช้ 2 ครั้งในขั้นตอนเดียวกัน ได้แก่ การเรียกใช้ `update()` ที่แทนที่ XML ที่มีโครงสร้าง และการเรียกใช้ฟังก์ชันจริงที่ต้องการ

## หมายเหตุและข้อจำกัด

- รองรับเฉพาะ[ชุดย่อยของสคีมา OpenAPI](https://ai.google.dev/api/rest/v1beta/cachedContents?hl=th#FunctionDeclaration) เท่านั้น
- สำหรับโหมด `any` API อาจปฏิเสธสคีมาที่มีขนาดใหญ่มากหรือมีการซ้อนกันลึก
- ประเภทพารามิเตอร์ที่รองรับใน Python มีจำนวนจำกัด

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
