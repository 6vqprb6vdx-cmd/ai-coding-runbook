---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/code-execution?hl=ar
fetched_at: 2026-08-03T04:38:03.485732+00:00
title: "\u062a\u0646\u0641\u064a\u0630 \u0627\u0644\u0631\u0645\u0632 \u0627\u0644\u0628\u0631\u0645\u062c\u064a \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تنفيذ الرمز البرمجي

توفّر Gemini API أداة لتنفيذ الرموز البرمجية تتيح للنموذج إنشاء رموز Python البرمجية وتشغيلها. يمكن للنموذج بعد ذلك أن يتعلّم بشكل متكرّر من نتائج تنفيذ الرمز البرمجي إلى أن يصل إلى الناتج النهائي. يمكنك استخدام تنفيذ التعليمات البرمجية لإنشاء تطبيقات تستفيد من الاستدلال المستند إلى التعليمات البرمجية. على سبيل المثال، يمكنك استخدام تطبيق الرموز البرمجية لحل المعادلات أو معالجة النصوص. يمكنك أيضًا استخدام [المكتبات](#supported-libraries) المضمّنة في بيئة تنفيذ الرمز البرمجي لتنفيذ مهام أكثر تخصصًا.

يمكن لـ Gemini تنفيذ الرمز البرمجي بلغة Python فقط. سيظل بإمكانك أن تطلب من Gemini إنشاء رمز بلغة أخرى، ولكن لن يتمكّن النموذج من استخدام أداة تنفيذ الرمز البرمجي لتشغيله.

## تفعيل تنفيذ الرموز البرمجية

لتفعيل تنفيذ الرموز البرمجية، عليك ضبط أداة تنفيذ الرموز البرمجية على النموذج. يتيح ذلك للنموذج إنشاء الرمز وتشغيله.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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
        "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

قد يبدو الناتج على النحو التالي، وقد تم تنسيقه لتسهيل قراءته:

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

يجمع هذا الناتج عدة أجزاء من المحتوى يعرضها النموذج عند استخدام تنفيذ الرمز البرمجي:

- ‫`text`: نص مضمّن تم إنشاؤه بواسطة النموذج
- ‫`executableCode`: رمز تم إنشاؤه بواسطة النموذج ويهدف إلى التنفيذ
- `codeExecutionResult`: نتيجة الرمز القابل للتنفيذ

تختلف اصطلاحات التسمية لهذه الأجزاء حسب لغة البرمجة.

## تنفيذ الرمز البرمجي باستخدام الصور (Gemini 3)

يمكن لنموذج Gemini 3 Flash الآن كتابة رموز Python البرمجية وتنفيذها من أجل التعديل على الصور وفحصها بشكل نشط.

**حالات الاستخدام**

- **التكبير والتدقيق**: يرصد النموذج تلقائيًا عندما تكون التفاصيل صغيرة جدًا (على سبيل المثال، قراءة مقياس بعيد)، ويكتب رمزًا برمجيًا لاقتصاص المنطقة وإعادة فحصها بدقة أعلى.
- **الرياضيات المرئية**: يمكن للنموذج إجراء عمليات حسابية متعددة الخطوات باستخدام الرموز البرمجية (مثل جمع بنود الإيصال).
- **التعليق التوضيحي على الصور**: يمكن للنموذج إضافة تعليقات توضيحية إلى الصور للإجابة عن أسئلة، مثل رسم أسهم لتوضيح العلاقات.

### تفعيل تنفيذ الرموز البرمجية باستخدام الصور

تتوفّر ميزة "تنفيذ التعليمات البرمجية" مع الصور رسميًا في Gemini 3 Flash. يمكنك تفعيل هذا السلوك من خلال تفعيل كلّ من "الاستخدام كأداة تنفيذ رموز برمجية" و"التفكير".

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
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
        "gemini-3.6-flash",
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
MODEL="gemini-3.6-flash"

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

## استخدام ميزة "تنفيذ الرمز البرمجي" في المحادثة

يمكنك أيضًا استخدام تنفيذ التعليمات البرمجية كجزء من محادثة.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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
        "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

## الإدخال/الإخراج (I/O)

يتيح تنفيذ الرموز البرمجية إدخال الملفات وإخراج الرسوم البيانية. باستخدام إمكانات الإدخال والإخراج هذه، يمكنك تحميل ملفات CSV وملفات نصية وطرح أسئلة حول الملفات والحصول على رسومات بيانية من [Matplotlib](https://matplotlib.org/) كجزء من الرد. يتم عرض ملفات الإخراج كصور مضمّنة في الردّ.

### أسعار مؤتمر I/O

عند استخدام تطبيق الرموز البرمجية لوحدات الإدخال والإخراج، يتم تحصيل رسوم منك مقابل الرموز المميزة للإدخال والرموز المميزة للإخراج:

**الرموز المميّزة المدخَلة:**

- طلب المستخدم

**الرموز المميزة الناتجة:**

- الرمز البرمجي الذي أنشأه النموذج
- ناتج تنفيذ الرمز البرمجي في بيئة الرمز البرمجي
- رموز مميّزة للتفكير
- ملخّص من إنشاء النموذج

### تفاصيل مؤتمر I/O

عند العمل على عمليات الإدخال والإخراج لتنفيذ الرمز، يجب الانتباه إلى التفاصيل الفنية التالية:

- الحدّ الأقصى لوقت تشغيل بيئة الرمز هو 30 ثانية.
- إذا أدّى تنفيذ الرمز البرمجي إلى حدوث خطأ، قد يقرّر النموذج إعادة إنشاء مخرجات الرمز البرمجي. يمكن أن يحدث ذلك 5 مرات كحد أقصى.
- يتم تحديد الحد الأقصى لحجم إدخال الملفات من خلال نافذة الرموز المميزة للنموذج. في AI Studio، يبلغ الحد الأقصى لحجم ملف الإدخال مليون رمز مميز (أي حوالي 2 ميغابايت لملفات النصوص من أنواع الإدخال المتوافقة). إذا حمّلت ملفًا كبيرًا جدًا، لن يسمح لك AI Studio بإرساله.
- يعمل تنفيذ الرمز البرمجي بشكل أفضل مع ملفات النصوص وملفات CSV.
- يمكن تمرير ملف الإدخال في `part.inlineData` أو `part.fileData` (يتم تحميله
  عبر [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar))، ويتم دائمًا عرض ملف الإخراج
  بتنسيق `part.inlineData`.

## الفوترة

لن يتم تحصيل أي رسوم إضافية مقابل تفعيل تطبيق الرموز البرمجية من خلال Gemini API.
سيتم تحصيل الرسوم منك وفقًا للمعدّل الحالي لرموز الإدخال والإخراج استنادًا إلى نموذج Gemini الذي تستخدمه.

في ما يلي بعض المعلومات الأخرى التي يجب معرفتها حول الفوترة مقابل تنفيذ الرموز البرمجية:

- يتم تحصيل الرسوم منك مرة واحدة فقط مقابل الرموز المميزة التي يتم إدخالها إلى النموذج، ويتم تحصيل الرسوم منك مقابل الرموز المميزة للناتج النهائي التي يعرضها النموذج.
- يتم احتساب الرموز المميزة التي تمثّل الرمز البرمجي الذي تم إنشاؤه كرموز مميزة ناتجة. يمكن أن يتضمّن الرمز البرمجي الذي تم إنشاؤه نصًا ومخرجات متعددة الوسائط، مثل الصور.
- يتم أيضًا احتساب نتائج تنفيذ الرمز البرمجي كرموز مميّزة ناتجة.

يظهر نموذج الفوترة في الرسم البياني التالي:

![نموذج الفوترة لتنفيذ الرموز البرمجية](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=ar)

- يتم تحصيل الرسوم منك بالسعر الحالي لرموز الإدخال والإخراج استنادًا إلى نموذج Gemini الذي تستخدمه.
- إذا استخدم Gemini تنفيذ الرمز البرمجي عند إنشاء ردّك، سيتم تصنيف الطلب الأصلي والرمز البرمجي الذي تم إنشاؤه ونتيجة الرمز البرمجي المنفَّذ على أنّها *رموز مميزة وسيطة*، وسيتم تحصيل الرسوم منها باعتبارها *رموزًا مميزة للإدخال*.
- بعد ذلك، ينشئ Gemini ملخّصًا ويعرض الرمز البرمجي الذي تم إنشاؤه ونتيجة الرمز البرمجي الذي تم تنفيذه والملخّص النهائي. تتم فوترة هذه الرموز المميزة على أنّها *رموز مميزة ناتجة*.
- يتضمّن Gemini API عدد الرموز المميّزة الوسيط في الردّ من واجهة برمجة التطبيقات، ما يتيح لك معرفة سبب تلقّيك رموزًا مميزة إضافية للإدخال تتجاوز طلبك الأولي.

## القيود

- يمكن للنموذج إنشاء الرمز البرمجي وتنفيذه فقط. ولا يمكنه عرض عناصر أخرى، مثل ملفات الوسائط.
- في بعض الحالات، يمكن أن يؤدي تفعيل تطبيق الرموز البرمجية إلى حدوث تراجع في جوانب أخرى من مخرجات النموذج (على سبيل المثال، كتابة قصة).
- تتفاوت النماذج المختلفة في قدرتها على تنفيذ الرموز البرمجية بنجاح.

## مجموعات الأدوات المتوافقة

يمكن دمج أداة تطبيق الرموز البرمجية مع [تحديد المصدر من خلال "بحث Search"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) لتفعيل المزيد من حالات الاستخدام المعقّدة.

تتيح نماذج Gemini 3 الجمع بين الأدوات المضمّنة (مثل "تنفيذ الرمز البرمجي") والأدوات المخصّصة (استدعاء الدوال). يجب إعادة تمرير الحقلَين `id` و`thought_signature` لكي تعمل ميزة دمج الأدوات. يمكنك الاطّلاع على مزيد من المعلومات في صفحة [مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).

## المكتبات المتوافقة

تتضمّن بيئة تنفيذ الرمز البرمجي المكتبات التالية:

- attrs
- شطرنج
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
- حزمة محتوى التطبيق
- باندا
- وسادة
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
- ستة
- striprtf
- sympy
- جدولة
- tensorflow
- toolz
- xlrd

لا يمكنك تثبيت مكتباتك الخاصة.

## الخطوات التالية

- جرِّب
  [تنفيذ الرمز البرمجي في Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Code_Execution.ipynb?hl=ar).
- مزيد من المعلومات حول أدوات Gemini API الأخرى:
  - [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)
  - [تحديد المصدر من خلال "بحث Google"](https://ai.google.dev/gemini-api/docs/grounding?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
