---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tool-combination?hl=th
fetched_at: 2026-09-07T05:38:34.645003+00:00
title: "\u0e23\u0e27\u0e21\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e21\u0e37\u0e2d\u0e43\u0e19\u0e15\u0e31\u0e27\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e40\u0e23\u0e35\u0e22\u0e01\u0e43\u0e0a\u0e49\u0e1f\u0e31\u0e07\u0e01\u0e4c\u0e0a\u0e31\u0e19 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# รวมเครื่องมือในตัวและการเรียกใช้ฟังก์ชัน

Gemini อนุญาตให้รวม[เครื่องมือในตัว](https://ai.google.dev/gemini-api/docs/tools?hl=th) เช่น `google_search` และ[การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th) (หรือที่เรียกว่า *เครื่องมือที่กำหนดเอง*) ไว้ในการสร้างครั้งเดียวโดยการเก็บรักษาและแสดงประวัติบริบทของการเรียกเครื่องมือ การรวมเครื่องมือในตัวและเครื่องมือที่กำหนดเองช่วยให้เวิร์กโฟลว์ที่ซับซ้อนและเป็นแบบ Agentic เป็นไปได้ เช่น โมเดลสามารถอ้างอิงข้อมูลเว็บแบบเรียลไทม์ก่อนที่จะเรียกใช้ตรรกะทางธุรกิจที่เฉพาะเจาะจงของคุณ

ตัวอย่างต่อไปนี้แสดงการรวมเครื่องมือในตัวและเครื่องมือที่กำหนดเองด้วย `google_search` และฟังก์ชันที่กำหนดเอง `getWeather`

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

# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather],  # Custom tool
            ),
        ],
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)
function_call_id = None
for part in response.candidates[0].content.parts:
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")
        function_call_id = part.function_call.id

# Turn 2: Manually build history to circulate both tool and function context
history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    # Response from Turn 1 includes tool_call, tool_response, and thought_signatures
    response.candidates[0].content,
    # Return the function_response
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=function_call_id # Match the ID from the function_call
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
                google_search=types.GoogleSearch(),
                function_declarations=[getWeather]
            ),
        ],
        # This flag needs to be enabled for built-in tool context circulation and tool combination
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)

for part in response_2.candidates[0].content.parts:
    if part.text:
        print(part.text)
```

### Javascript

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
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const response1 = await client.models.generateContent({
        model: "gemini-3.7-flash",
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    for (const part of response1.candidates[0].content.parts) {
        if (part.functionCall) {
            console.log(`Function call: ${part.functionCall.name} (ID: ${part.functionCall.id})`);
        }
    }

   const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    // Turn 2: Manually build history to circulate both tool and function context
    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        // Response from Turn 1 includes tool_call, tool_response, and thought_signatures
        response1.candidates[0].content,
        // Return the function_response
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId // Match the ID from the function_call
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

    for (const part of response2.candidates[0].content.parts) {
        if (part.text) {
            console.log(part.text);
        }
    }
}

run();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/generative-ai-go/genai"
    "google.golang.org/api/option"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("GEMINI_API_KEY")))
    if err != nil {
        log.Exit(err)
    }
    defer client.Close()

    getWeather := &genai.FunctionDeclaration{
        Name:        "getWeather",
        Description: "Get the weather in a given location",
        Parameters: &genai.Schema{
            Type: genai.Object,
            Properties: map[string]*genai.Schema{
                "location": {
                    Type:        genai.String,
                    Description: "The city and state, e.g. San Francisco, CA",
                },
            },
            Required: []string{"location"},
        },
    }

    model := client.GenerativeModel("gemini-3.7-flash")
    model.Tools = []*genai.Tool{
        {GoogleSearch: &genai.GoogleSearch{}}, // Built-in tool
        {FunctionDeclarations: []*genai.FunctionDeclaration{getWeather}}, // Custom tool
    }
    ist := true
    model.ToolConfig = &genai.ToolConfig{
        IncludeServerSideToolInvocations: &ist, // This flag needs to be enabled for built-in tool context circulation and tool combination
    }

    chat := model.StartChat()

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    prompt := genai.Text("What is the northernmost city in the United States? What's the weather like there today?")
    resp1, err := chat.SendMessage(ctx, prompt)
    if err != nil {
        log.Exitf("SendMessage failed: %v", err)
    }

    if resp1 == nil || len(resp1.Candidates) == 0 || resp1.Candidates[0].Content == nil {
        log.Exit("empty response from model")
    }

    var functionCallID string
    for _, part := range resp1.Candidates[0].Content.Parts {
        switch p := part.(type) {
        case genai.FunctionCall:
            fmt.Printf("Function call: %s (ID: %s)\n", p.Name, p.ID)
            if p.Name == "getWeather" {
                functionCallID = p.ID
            }
        }
    }

    if functionCallID == "" {
        log.Exit("no getWeather function call in response")
    }

    // Turn 2: Provide function result back to model.
    // Chat history automatically includes tool_call, tool_response, and thought_signatures from Turn 1.
    fr := genai.FunctionResponse{
        Name: "getWeather",
        ID:   functionCallID,
        Response: map[string]any{
            "response": "Very cold. 22 degrees Fahrenheit.",
        },
    }

    resp2, err := chat.SendMessage(ctx, fr)
    if err != nil {
        log.Exitf("SendMessage for turn 2 failed: %v", err)
    }

    if resp2 == nil || len(resp2.Candidates) == 0 || resp2.Candidates[0].Content == nil {
        log.Exit("empty response from model in turn 2")
    }

    for _, part := range resp2.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Println(string(txt))
        }
    }
}
```

### REST

```
# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.7-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What is the northernmost city in the United States? What'\''s the weather like there today?"
    }]
  }],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'

# Turn 2: Manually build history to circulate both tool and function context
# The following request assumes you have captured candidates[0].content from Turn 1 response,
# and extracted function_call.id for getWeather.
# Replace FUNCTION_CALL_ID and insert candidate content from turn 1.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.7-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "What is the northernmost city in the United States? What'\''s the weather like there today?"}]
    },
    YOUR_CANDIDATE_CONTENT_FROM_TURN_1_RESPONSE,
    {
      "role": "user",
      "parts": [{
        "functionResponse": {
          "name": "getWeather",
          "id": "FUNCTION_CALL_ID",
          "response": {"response": "Very cold. 22 degrees Fahrenheit."}
        }
      }]
    }
  ],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'
```

## วิธีการทำงาน

โมเดล Gemini 3 ใช้ *การหมุนเวียนบริบทของเครื่องมือ* เพื่อเปิดใช้การรวมเครื่องมือในตัวและเครื่องมือที่กำหนดเอง การหมุนเวียนบริบทของเครื่องมือช่วยให้เก็บรักษาและแสดงบริบทของเครื่องมือในตัว รวมถึงแชร์บริบทดังกล่าวกับเครื่องมือที่กำหนดเองในการเรียกใช้เดียวกันได้

### เปิดใช้การรวมเครื่องมือ

- คุณต้องตั้งค่าแฟล็ก `include_server_side_tool_invocations` เป็น `true` เพื่อเปิดใช้การหมุนเวียนบริบทของเครื่องมือ
- รวม [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=th#function-declarations) พร้อมกับ
  เครื่องมือในตัวที่ต้องการใช้เพื่อทริกเกอร์ลักษณะการทำงานของการรวม
  - หากไม่รวม `function_declarations` การหมุนเวียนบริบทของเครื่องมือจะยังคงทำงานกับเครื่องมือในตัวที่รวมไว้ ตราบใดที่ตั้งค่าแฟล็กไว้

### API จะแสดงผลเป็นส่วนๆ

ในการตอบกลับครั้งเดียว API จะแสดงผลส่วน `toolCall` และ `toolResponse` สำหรับการเรียกเครื่องมือในตัว สำหรับการเรียกฟังก์ชัน (เครื่องมือที่กำหนดเอง) API จะแสดงผลส่วนการเรียก `functionCall` ซึ่งผู้ใช้จะระบุส่วน `functionResponse` ในเทิร์นถัดไป

- `toolCall` และ `toolResponse`: API จะแสดงผลส่วนเหล่านี้เพื่อเก็บรักษาบริบทของเครื่องมือที่ทำงานฝั่งเซิร์ฟเวอร์และผลลัพธ์ของการดำเนินการสำหรับเทิร์นถัดไป
- `functionCall` และ `functionResponse`: API จะส่งการเรียกฟังก์ชันให้
  ผู้ใช้กรอกข้อมูล และผู้ใช้จะส่งผลลัพธ์กลับมาในการตอบกลับ
  ฟังก์ชัน (ส่วนเหล่านี้เป็นส่วนมาตรฐานของการ[เรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)ทั้งหมดใน Gemini API ไม่ได้มีเฉพาะฟีเจอร์การรวม
  เครื่องมือ)
- ([เครื่องมือการรันโค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)เท่านั้น)
  `executableCode` และ `codeExecutionResult`:
  เมื่อใช้เครื่องมือการรันโค้ด API จะแสดงผล `executableCode` (โค้ดที่โมเดลสร้างขึ้นเพื่อรัน) และ `codeExecutionResult` (ผลลัพธ์ของโค้ดที่รันได้) แทน `functionCall` และ
  `functionResponse`

คุณต้องส่งคืนทุกส่วน รวมถึงทุก[ช่อง](#critical-fields)ที่ส่วนนั้นๆ
มี กลับไปยังโมเดลในแต่ละเทิร์นเพื่อรักษาบริบทและเปิดใช้การรวมเครื่องมือ

### ช่องที่สำคัญในส่วนที่แสดงผล

[บางส่วนที่ API แสดงผลจะมีช่อง `id`,
`tool_type`, และ `thought_signature`](#api-returns-parts) ช่องเหล่านี้มีความสำคัญต่อการรักษาบริบทของเครื่องมือ (และจึงมีความสำคัญต่อการรวมเครื่องมือ) คุณต้องส่งคืนทุกส่วน *ตามที่ระบุไว้ในการตอบกลับ* ในคำขอที่ตามมา

- `id`: ตัวระบุที่ไม่ซ้ำกันซึ่งจับคู่การเรียกกับการตอบกลับ `id` จะ**ตั้งค่าในการ
  ตอบกลับการเรียกฟังก์ชันทั้งหมด** ไม่ว่าการหมุนเวียนบริบทของเครื่องมือจะเปิดอยู่หรือไม่ก็ตาม
  คุณ *ต้อง* ระบุ `id` เดียวกันในการตอบกลับฟังก์ชันที่ API ระบุในการเรียกฟังก์ชัน เครื่องมือในตัวจะแชร์ `id` ระหว่างการเรียกเครื่องมือและการตอบกลับเครื่องมือโดยอัตโนมัติ
  - พบในทุกส่วนที่เกี่ยวข้องกับเครื่องมือ ได้แก่ `toolCall`, `toolResponse`, `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: ระบุเครื่องมือที่เฉพาะเจาะจงที่ใช้ ซึ่งอาจเป็นชื่อเครื่องมือในตัว (เช่น `URL_CONTEXT`) หรือชื่อฟังก์ชัน (เช่น `getWeather`)
  - พบในส่วน `toolCall` และ `toolResponse`
- `thought_signature`: บริบทที่เข้ารหัสจริงซึ่งฝังอยู่ใน**แต่ละส่วนที่ API แสดงผล** คุณจะสร้างบริบทขึ้นใหม่ไม่ได้หากไม่มีลายเซ็นความคิด หากไม่ส่งคืนลายเซ็นความคิดของทุกส่วนในทุกเทิร์น โมเดลจะแสดงข้อผิดพลาด
  - พบใน *ทุก* ส่วน

### ข้อมูลเฉพาะของเครื่องมือ

เครื่องมือในตัวบางรายการจะแสดงผลอาร์กิวเมนต์ข้อมูลที่ผู้ใช้มองเห็นได้ซึ่งเฉพาะเจาะจงกับประเภทเครื่องมือ

| เครื่องมือ | อาร์กิวเมนต์การเรียกเครื่องมือที่ผู้ใช้มองเห็นได้ (หากมี) | การตอบกลับเครื่องมือที่ผู้ใช้มองเห็นได้ (หากมี) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` URL ที่จะเรียกดู | `urls_metadata` `retrieved_url`: URL ที่เรียกดู `url_retrieval_status`: สถานะการเรียกดู |
| **FILE\_SEARCH** | ไม่มี | ไม่มี |

## โครงสร้างคำขอการรวมเครื่องมือตัวอย่าง

โครงสร้างคำขอต่อไปนี้แสดงโครงสร้างคำขอของข้อความแจ้ง "เมืองที่อยู่เหนือสุดในสหรัฐอเมริกาคือเมืองใด วันนี้สภาพอากาศที่นั่นเป็นอย่างไร" โดยจะรวมเครื่องมือ 3 รายการ ได้แก่ เครื่องมือในตัวของ Gemini `google_search` และ `code_execution` รวมถึงฟังก์ชันที่กำหนดเอง `get_weather`

```
{
  "model": "models/gemini-3.7-flash",
  "contents": [{
    "parts": [{
      "text": "What is the northernmost city in the United States? What's the weather like there today?"
    }],
    "role": "user"
  }, {
    "parts": [{
      "thoughtSignature": "...",
      "toolCall": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "args": {
          "queries": ["northernmost city in the United States"]
        },
        "id": "a7b3k9p2"
      }
    }, {
      "thoughtSignature": "...",
      "toolResponse": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "response": {
          "search_suggestions": "..."
        },
        "id": "a7b3k9p2"
      }
    }, {
      "functionCall": {
        "name": "getWeather",
        "args": {
          "city": "Utqiaġvik, Alaska"
        },
        "id": "m4q8z1v6"
      },
      "thoughtSignature": "..."
    }],
    "role": "model"
  }, {
    "parts": [{
      "functionResponse": {
        "name": "getWeather",
        "response": {
          "response": "Very cold. 22 degrees Fahrenheit."
        },
        "id": "m4q8z1v6"
      }
    }],
    "role": "user"
  }],
  "tools": [{
    "functionDeclarations": [{
      "name": "getWeather"
    }]
  }, {
    "googleSearch": {
    }
  }, {
    "codeExecution": {
    }
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}
```

## โทเค็นและราคา

โปรดทราบว่าระบบจะนับส่วน `toolCall` และ `toolResponse` ในคำขอรวมกับ `prompt_token_count` เนื่องจากขั้นตอนเครื่องมือระดับกลางเหล่านี้สามารถมองเห็นได้และระบบจะแสดงผลกลับมาให้คุณ ขั้นตอนเหล่านี้จึงเป็นส่วนหนึ่งของประวัติการสนทนา ซึ่งจะเป็นเช่นนี้เฉพาะกับ
กรณีของ *คำขอ* ไม่ใช่ *การตอบกลับ*

เครื่องมือ Google Search เป็นข้อยกเว้นของกฎนี้ Google Search ใช้โมเดลราคาของตัวเองอยู่แล้วในระดับคําค้นหา ดังนั้นระบบจะไม่คิดค่าบริการโทเค็นซ้ำ (ดูหน้า[การกำหนดราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th))

อ่านข้อมูลเพิ่มเติมได้ที่หน้า[โทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th)

## ข้อจำกัด

- ค่าเริ่มต้นเป็นโหมด `VALIDATED` (`AUTO` ไม่รองรับ) เมื่อเปิดใช้แฟล็ก `include_server_side_tool_invocations`
- เครื่องมือในตัว เช่น `google_search` อาศัยข้อมูลตำแหน่งและเวลาปัจจุบัน ดังนั้นหาก `system_instruction` หรือ `function_declaration.description` มีข้อมูลตำแหน่งและเวลาที่ไม่สอดคล้องกัน ฟีเจอร์การรวมเครื่องมืออาจทำงานได้ไม่ดี

## เครื่องมือที่รองรับ

การหมุนเวียนบริบทของเครื่องมือมาตรฐานใช้ได้กับเครื่องมือฝั่งเซิร์ฟเวอร์ (ในตัว)
การรันโค้ดก็เป็นเครื่องมือฝั่งเซิร์ฟเวอร์เช่นกัน แต่มีโซลูชันในตัวสำหรับการหมุนเวียนบริบท การใช้คอมพิวเตอร์และการเรียกฟังก์ชันเป็นเครื่องมือฝั่งไคลเอ็นต์ และมีโซลูชันในตัวสำหรับการหมุนเวียนบริบทด้วย

| เครื่องมือ | ฝั่งการดำเนินการ | การรองรับการหมุนเวียนบริบท |
| --- | --- | --- |
| [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ |
| [บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ |
| [การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ |
| [การรันโค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ (ในตัว ใช้ส่วน `executableCode` และ `codeExecutionResult`) |
| [การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th) | ฝั่งไคลเอ็นต์ | รองรับ (ในตัว ใช้ส่วน `functionCall` และ `functionResponse`) |
| [ฟังก์ชันที่กำหนดเอง](https://ai.google.dev/gemini-api/docs/function-calling?hl=th) | ฝั่งไคลเอ็นต์ | รองรับ (ในตัว ใช้ส่วน `functionCall` และ `functionResponse`) |

## ขั้นตอนถัดไป

- ดูข้อมูลเพิ่มเติมเกี่ยวกับ[การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)ใน Gemini API
- สำรวจเครื่องมือที่รองรับ
  - [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)
  - [บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th)
  - [การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-08-26 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-08-26 UTC"],[],[]]
