---
source_url: https://ai.google.dev/gemini-api/docs/code-execution?hl=th
fetched_at: 2026-06-22T06:26:26.059219+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) is now available in preview with collaborative planning, visualization, MCP support, and more.

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การเรียกใช้โค้ด

Gemini API มีเครื่องมือเรียกใช้โค้ดที่ช่วยให้โมเดลสร้างและรันโค้ด Python ได้ จากนั้นโมเดลจะเรียนรู้ซ้ำๆ จากผลการเรียกใช้โค้ดจนกว่าจะได้เอาต์พุตสุดท้าย คุณสามารถใช้การดำเนินการโค้ดเพื่อสร้างแอปพลิเคชันที่ได้รับประโยชน์จากการให้เหตุผลตามโค้ด เช่น คุณสามารถใช้การเรียกใช้โค้ดเพื่อแก้สมการหรือประมวลผลข้อความ นอกจากนี้ คุณยังใช้ [ไลบรารี](#supported-libraries)ที่รวมอยู่ในสภาพแวดล้อมการเรียกใช้โค้ดเพื่อทำงานที่เฉพาะเจาะจงมากขึ้นได้ด้วย

Gemini สามารถเรียกใช้โค้ดใน Python ได้เท่านั้น คุณยังคงขอความช่วยเหลือจาก Gemini ให้สร้างโค้ดในภาษาอื่นได้ แต่โมเดลจะใช้เครื่องมือเรียกใช้โค้ดเพื่อดำเนินการไม่ได้

## เปิดใช้การเรียกใช้โค้ด

หากต้องการเปิดใช้การเรียกใช้โค้ด ให้กำหนดค่าเครื่องมือเรียกใช้โค้ดในโมเดล ซึ่งจะช่วยให้โมเดลสร้างและรันโค้ดได้

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is the sum of the first 50 prime numbers? "
    "Generate and run code for the calculation, and make sure you get all 50.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: [
    "What is the sum of the first 50 prime numbers? " +
      "Generate and run code for the calculation, and make sure you get all 50.",
  ],
  config: {
    tools: [{ codeExecution: {} }],
  },
});

const parts = response?.candidates?.[0]?.content?.parts || [];
parts.forEach((part) => {
  if (part.text) {
    console.log(part.text);
  }

  if (part.executableCode && part.executableCode.code) {
    console.log(part.executableCode.code);
  }

  if (part.codeExecutionResult && part.codeExecutionResult.output) {
    console.log(part.codeExecutionResult.output);
  }
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("What is the sum of the first 50 prime numbers? " +
                  "Generate and run code for the calculation, and make sure you get all 50."),
        config,
    )

    fmt.Println(result.Text())
    fmt.Println(result.ExecutableCode())
    fmt.Println(result.CodeExecutionResult())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d ' {"tools": [{"code_execution": {}}],
    "contents": {
      "parts":
        {
            "text": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."
        }
    },
}'
```

เอาต์พุตอาจมีลักษณะดังต่อไปนี้ ซึ่งจัดรูปแบบให้อ่านง่าย

```
Okay, I need to calculate the sum of the first 50 prime numbers. Here's how I'll
approach this:

1.  **Generate Prime Numbers:** I'll use an iterative method to find prime
    numbers. I'll start with 2 and check if each subsequent number is divisible
    by any number between 2 and its square root. If not, it's a prime.
2.  **Store Primes:** I'll store the prime numbers in a list until I have 50 of
    them.
3.  **Calculate the Sum:**  Finally, I'll sum the prime numbers in the list.

Here's the Python code to do this:

def is_prime(n):
  """Efficiently checks if a number is prime."""
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

primes = []
num = 2
while len(primes) < 50:
  if is_prime(num):
    primes.append(num)
  num += 1

sum_of_primes = sum(primes)
print(f'{primes=}')
print(f'{sum_of_primes=}')

primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
sum_of_primes=5117

The sum of the first 50 prime numbers is 5117.
```

เอาต์พุตนี้รวมส่วนเนื้อหาหลายส่วนที่โมเดลส่งคืนเมื่อใช้การเรียกใช้โค้ด

- `text`: ข้อความแบบอินไลน์ที่โมเดลสร้างขึ้น
- `executableCode`: โค้ดที่โมเดลสร้างขึ้นเพื่อเรียกใช้
- `codeExecutionResult`: ผลลัพธ์ของโค้ดที่เรียกใช้ได้

รูปแบบการตั้งชื่อสำหรับส่วนเหล่านี้จะแตกต่างกันไปตามภาษาโปรแกรม

## การเรียกใช้โค้ดกับรูปภาพ (Gemini 3)

ตอนนี้โมเดล Gemini 3 Flash สามารถเขียนและเรียกใช้โค้ด Python เพื่อจัดการและตรวจสอบรูปภาพได้อย่างมีประสิทธิภาพ

**กรณีการใช้งาน**

- **ซูมและตรวจสอบ**: โมเดลจะตรวจหาโดยนัยเมื่อรายละเอียดมีขนาดเล็กเกินไป
  (เช่น การอ่านมาตรวัดที่อยู่ไกลออกไป) และเขียนโค้ดเพื่อครอบตัดและตรวจสอบพื้นที่อีกครั้ง
  ด้วยความละเอียดที่สูงขึ้น
- **คณิตศาสตร์เชิงภาพ**: โมเดลสามารถทำการคำนวณหลายขั้นตอนโดยใช้โค้ด (เช่น
  การรวมรายการในใบเสร็จ)
- **การใส่คำอธิบายประกอบในรูปภาพ**: โมเดลสามารถใส่คำอธิบายประกอบในรูปภาพเพื่อตอบคำถาม เช่น
  การวาดลูกศรเพื่อแสดงความสัมพันธ์

### เปิดใช้การเรียกใช้โค้ดกับรูปภาพ

ระบบรองรับการเรียกใช้โค้ดกับรูปภาพอย่างเป็นทางการใน Gemini 3 Flash คุณสามารถเปิดใช้งานลักษณะการทำงานนี้ได้โดยเปิดใช้ทั้งการเรียกใช้โค้ดเป็นเครื่องมือและการคิด

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

# Ensure you have your API key set
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[image, "Zoom into the expression pedals and tell me how many pedals are there?"],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        # display() is a standard function in Jupyter/Colab notebooks
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
async function main() {
  const ai = new GoogleGenAI({ });

  // 1. Prepare Image Data
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  // 2. Call the API with Code Execution enabled
  const result = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
      {
        inlineData: {
          mimeType: 'image/jpeg',
          data: base64ImageData,
        },
      },
      { text: "Zoom into the expression pedals and tell me how many pedals are there?" }
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  // 3. Process the response (Text, Code, and Execution Results)
  const candidates = result.candidates;
  if (candidates && candidates[0].content.parts) {
    for (const part of candidates[0].content.parts) {
      if (part.text) {
        console.log("Text:", part.text);
      }
      if (part.executableCode) {
        console.log(`\nGenerated Code (${part.executableCode.language}):\n`, part.executableCode.code);
      }
      if (part.codeExecutionResult) {
        console.log(`\nExecution Output (${part.codeExecutionResult.outcome}):\n`, part.codeExecutionResult.output);
      }
    }
  }
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "io"
    "log"
    "net/http"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // Initialize Client (Reads GEMINI_API_KEY from env)
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // 1. Download the image
    imageResp, err := http.Get("https://goo.gle/instrument-img")
    if err != nil {
        log.Fatal(err)
    }
    defer imageResp.Body.Close()

    imageBytes, err := io.ReadAll(imageResp.Body)
    if err != nil {
        log.Fatal(err)
    }

    // 2. Configure Code Execution Tool
    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    // 3. Generate Content
    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        []*genai.Content{
            {
                Parts: []*genai.Part{
                    {InlineData: &genai.Blob{MIMEType: "image/jpeg", Data: imageBytes}},
                    {Text: "Zoom into the expression pedals and tell me how many pedals are there?"},
                },
                Role: "user",
            },
        },
        config,
    )
    if err != nil {
        log.Fatal(err)
    }

    // 4. Parse Response (Text, Code, Output)
    for _, cand := range result.Candidates {
        for _, part := range cand.Content.Parts {
            if part.Text != "" {
                fmt.Println("Text:", part.Text)
            }
            if part.ExecutableCode != nil {
                fmt.Printf("\nGenerated Code (%s):\n%s\n", 
                    part.ExecutableCode.Language, 
                    part.ExecutableCode.Code)
            }
            if part.CodeExecutionResult != nil {
                fmt.Printf("\nExecution Output (%s):\n%s\n", 
                    part.CodeExecutionResult.Outcome, 
                    part.CodeExecutionResult.Output)
            }
        }
    }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3.5-flash"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [
        {
          "code_execution": {}
        }
      ]
    }'
```

## ใช้การเรียกใช้โค้ดในการแชท

คุณยังใช้การเรียกใช้โค้ดเป็นส่วนหนึ่งของการแชทได้ด้วย

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

response = chat.send_message("I have a math question for you.")
print(response.text)

response = chat.send_message(
    "What is the sum of the first 50 prime numbers? "
    "Generate and run code for the calculation, and make sure you get all 50."
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
```

### JavaScript

```
import {GoogleGenAI} from "@google/genai";

const ai = new GoogleGenAI({});

const chat = ai.chats.create({
  model: "gemini-3.5-flash",
  history: [
    {
      role: "user",
      parts: [{ text: "I have a math question for you:" }],
    },
    {
      role: "model",
      parts: [{ text: "Great! I'm ready for your math question. Please ask away." }],
    },
  ],
  config: {
    tools: [{codeExecution:{}}],
  }
});

const response = await chat.sendMessage({
  message: "What is the sum of the first 50 prime numbers? " +
            "Generate and run code for the calculation, and make sure you get all 50."
});
console.log("Chat response:", response.text);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    chat, _ := client.Chats.Create(
        ctx,
        "gemini-3.5-flash",
        config,
        nil,
    )

    result, _ := chat.SendMessage(
                    ctx,
                    genai.Part{Text: "What is the sum of the first 50 prime numbers? " +
                                          "Generate and run code for the calculation, and " +
                                          "make sure you get all 50.",
                              },
                )

    fmt.Println(result.Text())
    fmt.Println(result.ExecutableCode())
    fmt.Println(result.CodeExecutionResult())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"tools": [{"code_execution": {}}],
    "contents": [
        {
            "role": "user",
            "parts": [{
                "text": "Write code to print \"Hello world!\" and execute it"
            }]
        },{
            "role": "model",
            "parts": [
              {
                "executable_code": {
                  "id": "a1b2c3d4",
                  "language": "PYTHON",
                  "code": "\nprint(\"hello world!\")\n"
                }
                "thought_signature": "..."
              },
              {
                "code_execution_result": {
                  "id": "a1b2c3d4",
                  "outcome": "OUTCOME_OK",
                  "output": "hello world!\n"
                }
              },
              {
                "text": "I have printed \"hello world!\" using the provided python code block. \n",
                "thought_signature": "..."
              }
            ],
        },{
            "role": "user",
            "parts": [{
                "text": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."
            }]
        }
    ]
}'
```

## อินพุต/เอาต์พุต (I/O)

การเรียกใช้โค้ดรองรับอินพุตไฟล์และเอาต์พุตกราฟ คุณสามารถอัปโหลดไฟล์ CSV และไฟล์ข้อความ ถามคำถามเกี่ยวกับ
ไฟล์ และสร้างกราฟ [Matplotlib](https://matplotlib.org/) เป็นส่วนหนึ่ง
ของการตอบกลับได้โดยใช้ความสามารถด้านอินพุตและ
เอาต์พุตเหล่านี้ ระบบจะแสดงไฟล์เอาต์พุตเป็นรูปภาพแบบอินไลน์ในการตอบกลับ

### การกำหนดราคา I/O

เมื่อใช้ I/O ของการเรียกใช้โค้ด ระบบจะเรียกเก็บเงินจากคุณสำหรับโทเค็นอินพุตและโทเค็นเอาต์พุต

**โทเค็นอินพุต:**

- พรอมต์ของผู้ใช้

**โทเค็นเอาต์พุต:**

- โค้ดที่โมเดลสร้างขึ้น
- เอาต์พุตการเรียกใช้โค้ดในสภาพแวดล้อมโค้ด
- โทเค็นการคิด
- ข้อมูลสรุปที่โมเดลสร้างขึ้น

### รายละเอียด I/O

เมื่อทำงานกับ I/O ของการเรียกใช้โค้ด โปรดทราบรายละเอียดทางเทคนิคต่อไปนี้

- รันไทม์สูงสุดของสภาพแวดล้อมโค้ดคือ 30 วินาที
- หากสภาพแวดล้อมโค้ดสร้างข้อผิดพลาด โมเดลอาจตัดสินใจสร้างเอาต์พุตโค้ดใหม่ ซึ่งอาจเกิดขึ้นได้สูงสุด 5 ครั้ง
- ขนาดอินพุตไฟล์สูงสุดจะจำกัดตามหน้าต่างโทเค็นของโมเดล ใน AI Studio ขนาดไฟล์อินพุตสูงสุดคือ 1 ล้านโทเค็น (ประมาณ 2 MB สำหรับไฟล์ข้อความของประเภทอินพุตที่รองรับ) หากคุณอัปโหลดไฟล์ที่มีขนาดใหญ่เกินไป AI Studio จะไม่อนุญาตให้คุณส่งไฟล์ดังกล่าว
- การเรียกใช้โค้ดทำงานได้ดีที่สุดกับไฟล์ข้อความและไฟล์ CSV
- คุณส่งไฟล์อินพุตใน `part.inlineData` หรือ `part.fileData` (อัปโหลด
  ผ่าน [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th)) ได้ และระบบจะส่งคืนไฟล์เอาต์พุตเป็น `part.inlineData` เสมอ

## การเรียกเก็บเงิน

การเปิดใช้การเรียกใช้โค้ดจาก Gemini API จะไม่มีค่าใช้จ่ายเพิ่มเติม
ระบบจะเรียกเก็บเงินจากคุณตามอัตราปัจจุบันของโทเค็นอินพุตและเอาต์พุตโดยอิงตามโมเดล Gemini ที่คุณใช้

สิ่งอื่นๆ ที่ควรทราบเกี่ยวกับการเรียกเก็บเงินสำหรับการเรียกใช้โค้ดมีดังนี้

- ระบบจะเรียกเก็บเงินจากคุณเพียงครั้งเดียวสำหรับโทเค็นอินพุตที่คุณส่งไปยังโมเดล และจะเรียกเก็บเงินสำหรับโทเค็นเอาต์พุตสุดท้ายที่โมเดลส่งคืนให้คุณ
- ระบบจะนับโทเค็นที่แสดงโค้ดที่สร้างขึ้นเป็นโทเค็นเอาต์พุต โค้ดที่สร้างขึ้นอาจมีข้อความและเอาต์พุตหลายรูปแบบ เช่น รูปภาพ
- ระบบจะนับผลการเรียกใช้โค้ดเป็นโทเค็นเอาต์พุตด้วย

โมเดลการเรียกเก็บเงินแสดงอยู่ในแผนภาพต่อไปนี้

![โมเดลการเรียกเก็บเงินสำหรับการรันโค้ด](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=th)

- ระบบจะเรียกเก็บเงินจากคุณตามอัตราปัจจุบันของโทเค็นอินพุตและเอาต์พุตโดยอิงตามโมเดล Gemini ที่คุณใช้
- หาก Gemini ใช้การเรียกใช้โค้ดเมื่อสร้างการตอบกลับ พรอมต์เดิม โค้ดที่สร้างขึ้น และผลลัพธ์ของโค้ดที่เรียกใช้จะติดป้ายกำกับเป็น *โทเค็นระดับกลาง* และระบบจะเรียกเก็บเงินเป็น *โทเค็นอินพุต*
- จากนั้น Gemini จะสร้างข้อมูลสรุปและส่งคืนโค้ดที่สร้างขึ้น ผลลัพธ์ของโค้ดที่เรียกใช้ และข้อมูลสรุปสุดท้าย ระบบจะเรียกเก็บเงินสำหรับรายการเหล่านี้เป็น *โทเค็นเอาต์พุต*
- Gemini API จะรวมจำนวนโทเค็นระดับกลางไว้ในการตอบกลับจาก API เพื่อให้คุณทราบว่าเหตุใดคุณจึงได้รับโทเค็นอินพุตเพิ่มเติมนอกเหนือจากพรอมต์เริ่มต้น

## ข้อจำกัด

- โมเดลสามารถสร้างและเรียกใช้โค้ดได้เท่านั้น โดยไม่สามารถส่งคืนอาร์ติแฟกต์อื่นๆ เช่น ไฟล์สื่อ
- ในบางกรณี การเปิดใช้การเรียกใช้โค้ดอาจทำให้เกิดการถดถอยในส่วนอื่นๆ ของเอาต์พุตโมเดล (เช่น การเขียนเรื่องราว)
- โมเดลต่างๆ มีความสามารถในการใช้การเรียกใช้โค้ดให้สำเร็จแตกต่างกัน

## ชุดค่าผสมของเครื่องมือที่รองรับ

คุณสามารถรวมเครื่องมือเรียกใช้โค้ดกับ
[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th) เพื่อ
รองรับกรณีการใช้งานที่ซับซ้อนมากขึ้น

โมเดล Gemini 3 รองรับการรวมเครื่องมือในตัว (เช่น การเรียกใช้โค้ด) กับเครื่องมือที่กำหนดเอง (การเรียกฟังก์ชัน) คุณต้องส่งฟิลด์ `id` และ `thought_signature` กลับมาเพื่อให้การรวมเครื่องมือทำงานได้ ดูข้อมูลเพิ่มเติมได้ในหน้า
[ชุดค่าผสมของเครื่องมือ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=th)

## ไลบรารีที่รองรับ

สภาพแวดล้อมการเรียกใช้โค้ดมีไลบรารีต่อไปนี้

- attrs
- chess
- contourpy
- fpdf
- geopandas
- imageio
- jinja2
- joblib
- jsonschema
- jsonschema-specifications
- lxml
- matplotlib
- mpmath
- numpy
- opencv-python
- openpyxl
- packaging
- pandas
- pillow
- protobuf
- pylatex
- pyparsing
- PyPDF2
- python-dateutil
- python-docx
- python-pptx
- reportlab
- scikit-learn
- scipy
- seaborn
- six
- striprtf
- sympy
- tabulate
- tensorflow
- toolz
- xlrd

คุณจะติดตั้งไลบรารีของคุณเองไม่ได้

## ขั้นตอนถัดไป

- ลองใช้
  [Colab ของการเรียกใช้โค้ด](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Code_Execution.ipynb?hl=th)
- ดูข้อมูลเกี่ยวกับเครื่องมืออื่นๆ ของ Gemini API ได้แก่
  - [การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
  - [การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/grounding?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-19 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-19 UTC"],[],[]]
