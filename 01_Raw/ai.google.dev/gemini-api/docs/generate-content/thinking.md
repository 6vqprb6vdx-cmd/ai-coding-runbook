---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ar
fetched_at: 2026-08-24T02:26:55.478245+00:00
title: "\u062a\u0641\u0643\u064a\u0631 Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تفكير Gemini

تستخدم نماذج [Gemini 3 و2.5 سلسلة](https://ai.google.dev/gemini-api/docs/models?hl=ar) "عملية تفكير" داخلية تحسّن بشكل كبير من قدراتها على الاستدلال والتخطيط المتعدد الخطوات، ما يجعلها فعّالة للغاية في المهام المعقّدة، مثل الترميز والرياضيات المتقدّمة وتحليل البيانات.

يوضّح لك هذا الدليل كيفية استخدام إمكانات التفكير في Gemini باستخدام Gemini API.

## إنشاء محتوى باستخدام ميزة "التفكير"

إنشاء طلب باستخدام نموذج تفكير مشابه لأي طلب آخر لإنشاء المحتوى. ويكمن الاختلاف الرئيسي في تحديد أحد الن101}[ماذج التي تتوافق مع ميزة "التفكير"](#supported-models) في حقل `model`، كما هو101}موضّح في مثال [إنشاء النص](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#text-input) التالي:

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### انتقال

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.6-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
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
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## ملخّصات الأفكار

ملخّصات الأفكار هي إصدارات مُلخّصة من الأفكار الأولية للنموذج، وتقدّم إحصاءات حول عملية الاستدلال الداخلية للنموذج. يُرجى العِلم أنّ مستويات التفكير والميزانيات تنطبق على الأفكار الأولية للنموذج وليس على ملخّصات الأفكار.

يمكنك تفعيل ملخّصات الأفكار من خلال ضبط `includeThoughts` على `true` في إعدادات الطلب. بعد ذلك، يمكنك الوصول إلى الملخّص من خلال تكرار عناصر `parts` في المَعلمة `response` والتحقّق من القيمة المنطقية `thought`.

في ما يلي مثال يوضّح كيفية تفعيل ملخّصات الأفكار واستردادها بدون البث، ما يؤدي إلى عرض ملخّص نهائي واحد للأفكار مع الردّ:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### انتقال

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.6-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

في ما يلي مثال على استخدام ميزة "التفكير" مع البث، ما يؤدي إلى عرض ملخّصات متزايدة ومتجدّدة أثناء الإنشاء:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
  }
}

await main();
```

### انتقال

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.6-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## التحكّم في ميزة "التفكير"

تستخدم نماذج Gemini ميزة "التفكير الديناميكي" تلقائيًا، ما يؤدي إلى تعديل مقدار جهد الاستدلال استنادًا إلى مدى تعقيد طلب المستخدم.
مع ذلك، إذا كانت لديك قيود معيّنة على وقت الاستجابة أو كنت تريد أن يستخدم النموذج استدلالاً أعمق من المعتاد، يمكنك اختياريًا استخدام مَعلمات للتحكّم في سلوك ميزة "التفكير".

### مستويات التفكير (Gemini 3)

تتيح لك المَعلمة `thinkingLevel`، التي ننصح باستخدامها مع نماذج Gemini 3 والإصدارات الأحدث، التحكّم في سلوك الاستدلال.

يوضّح الجدول التالي إعدادات `thinkingLevel` لكل نوع من أنواع النماذج:

| مستوى التفكير | ‫Gemini 3.6 و3.5 Flash | Gemini 3.1 Pro | ‫Gemini 3.5 و3.1 Flash-Lite | ‫Gemini 3.1 Flash-Lite Image | Gemini 3 Flash | الوصف |
| --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | متاح | غير متاح | متاح (تلقائي) | متاح (تلقائي) | متاح | يتطابق مع إعداد "بدون تفكير" لمعظم طلبات البحث. يُرجى العِلم أنّ `minimal` لا يضمن إيقاف ميزة "التفكير"، فقد يستخدم النموذج الحد الأدنى من الاستدلال للمهام المعقّدة. |
| **`low`** | متاح | متاح | متاح | غير متاح | متاح | يقلّل وقت الاستجابة والتكلفة إلى الحد الأدنى. |
| **`medium`** | متاح (تلقائي) | متاح | متاح | غير متاح | متاح | تفكير متوازن لمعظم المهام. |
| **`high`** | متاح (ديناميكي) | متاح (تلقائي، ديناميكي) | متاح (ديناميكي) | متاح (ديناميكي) | متاح (تلقائي، ديناميكي) | يزيد من عمق الاستدلال إلى الحد الأقصى. قد يستغرق النموذج وقتًا أطول بكثير للوصول إلى أول رمز مميّز للناتج (بدون تفكير)، ولكن سيكون الناتج أكثر استدلالاً بعناية. |

يوضّح المثال التالي كيفية ضبط مستوى التفكير.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### انتقال

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.6-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
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
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

لا يمكنك إيقاف ميزة "التفكير" في Gemini 3.1 Pro. لا يتيح Gemini 3 Flash وFlash-Lite
أيضًا إيقاف ميزة "التفكير" بالكامل.
إذا لم تحدّد مستوى التفكير، سيستخدم Gemini مستوى التفكير التلقائي لنماذج Gemini 3 (مثلاً، `"high"` لـ Gemini 3.1 Pro و`"medium"` لـ Gemini 3.5 Flash).

لا تتيح نماذج Gemini 2.5 سلسلة `thinkingLevel`، لذا استخدِم `thinkingBudget` بدلاً من ذلك.

### ميزانيات التفكير

توجّه المَعلمة `thinkingBudget`، التي تم طرحها مع سلسلة Gemini 2.5، النموذج بشأن العدد المحدّد من رموز التفكير المميّزة التي يجب استخدامها للاستدلال.

في ما يلي تفاصيل إعدادات `thinkingBudget` لكل نوع من أنواع النماذج.
يمكنك إيقاف ميزة "التفكير" من خلال ضبط `thinkingBudget` على 0.
يؤدي ضبط `thinkingBudget` على -1 إلى تفعيل **التفكير الديناميكي**، ما يعني أنّ النموذج سيعدّل الميزانية استنادًا إلى مدى تعقيد الطلب.

| الطراز | الإعداد التلقائي (لم يتم ضبط ميزانية التفكير) | النطاق | إيقاف ميزة "التفكير" | تفعيل ميزة "التفكير الديناميكي" |
| --- | --- | --- | --- | --- |
| ‫**2.5 Pro** | التفكير الديناميكي | من `128` إلى `32768` | لا ينطبق: لا يمكن إيقاف ميزة "التفكير" | `thinkingBudget = -1` (تلقائي) |
| ‫**2.5 Flash** | التفكير الديناميكي | من `0` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (تلقائي) |
| ‫**2.5 Flash Preview** | التفكير الديناميكي | من `0` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (تلقائي) |
| ‫**2.5 Flash Lite** | لا يفكّر النموذج | من `512` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| ‫**2.5 Flash Lite Preview** | لا يفكّر النموذج | من `512` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| ‫**Robotics-ER 1.6 Preview** | التفكير الديناميكي | من `0` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (تلقائي) |
| ‫**2.5 Flash Live Native Audio Preview (09-2025)** | التفكير الديناميكي | من `0` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (تلقائي) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### انتقال

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

استنادًا إلى الطلب، قد يتجاوز النموذج ميزانية الرموز المميّزة أو يقلّ عنها.

## توقيعات الأفكار

‫Gemini API غير احتفاظي، لذا يتعامل النموذج مع كل طلب بيانات من واجهة برمجة التطبيقات بشكلٍ مستقل ولا يمكنه الوصول إلى سياق الأفكار من الأدوار السابقة في المحادثات المترابطة.

من أجل تفعيل الاحتفاظ بسياق الأفكار في المحادثة المترابطة، يعرض Gemini توقيعات الأفكار، وهي تمثيلات مشفّرة لعملية التفكير الداخلية للنموذج.

- **تعرض نماذج Gemini 2.5** توقيعات الأفكار عند تفعيل ميزة "التفكير" وتضمين الطلب [ميزة "استدعاء الدالة"](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#thinking)، وتحديدًا [إعلانات الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#step-2).
- [**قد تعرض نماذج Gemini 3 توقيعات الأفكار لجميع أنواع الأجزاء.**](https://ai.google.dev/api/caching?hl=ar#Part)
  ننصحك دائمًا بإعادة إرسال جميع التوقيعات كما تم استلامها، ولكن *يجب* ذلك لتوقيعات ميزة "استدعاء الدالة". يمكنك قراءة صفحة
  [توقيعات الأفكار](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ar) لمعرفة المزيد.

تشمل قيود الاستخدام الأخرى التي يجب أخذها في الاعتبار مع ميزة "استدعاء الدالة" ما يلي:

- يتم عرض التوقيعات من النموذج ضمن أجزاء أخرى في الردّ، مثلاً ميزة "استدعاء الدالة" أو أجزاء النص.
  [أعِد إرسال الردّ بالكامل](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#step-4)
  مع جميع الأجزاء إلى النموذج في الأدوار اللاحقة.
- لا تدمِج الأجزاء التي تتضمّن توقيعات معًا.
- لا تدمِج جزءًا يتضمّن توقيعًا مع جزء آخر لا يتضمّن توقيعًا.

## الأسعار

عند تفعيل ميزة "التفكير"، يكون سعر الردّ هو مجموع رموز الإخراج ورموز التفكير. يمكنك الحصول على إجمالي عدد رموز التفكير التي تم إنشاؤها من حقل `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### انتقال

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

تنشئ نماذج التفكير أفكارًا كاملة لتحسين جودة الردّ النهائي
، ثم تعرض [ملخّصات](#summaries) لتقديم إحصاءات حول عملية التفكير. لذا، تستند الأسعار إلى رموز التفكير الكاملة التي يحتاج النموذج إلى إنشائها لإنشاء ملخّص، على الرغم من أنّ واجهة برمجة التطبيقات تعرض الملخّص فقط.

يمكنك التعرّف أكثر على الرموز المميّزة في [دليل عدّ الرموز المميّزة](https://ai.google.dev/gemini-api/docs/tokens?hl=ar).

## أفضل الممارسات

يتضمّن هذا القسم بعض الإرشادات لاستخدام نماذج التفكير بكفاءة.
كما هو الحال دائمًا، سيساعدك اتّباع [إرشادات كتابة الطلبات وأفضل الممارسات](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ar) في الحصول على أفضل النتائج.

### تصحيح الأخطاء والتوجيه

- **مراجعة الاستدلال**: عندما لا تحصل على الردّ المتوقّع من
  نماذج التفكير، قد يساعدك تحليل ملخّصات أفكار Gemini بعناية.
  يمكنك الاطّلاع على كيفية تقسيم النموذج للمهمة والوصول إلى استنتاجه، واستخدام هذه المعلومات لتصحيح النتائج والحصول على النتائج الصحيحة.
- **تقديم إرشادات في الاستدلال**: إذا كنت تأمل في الحصول على ناتج طويل بشكلٍ خاص
  ، قد تحتاج إلى تقديم إرشادات في طلبك لتقييد
  [مقدار التفكير](#set-budget) الذي يستخدمه النموذج. يتيح لك ذلك حجز المزيد من رموز الإخراج لردّك.

### مدى تعقيد المهام

- **المهام السهلة (يمكن إيقاف ميزة "التفكير"):** بالنسبة إلى الطلبات البسيطة التي لا تتطلّب استدلالاً معقّدًا، مثل استرداد الحقائق أو التصنيف، لا تكون ميزة "التفكير" مطلوبة. تشمل الأمثلة ما يلي:
  - "أين تم تأسيس DeepMind؟"
  - "هل يطلب هذا البريد الإلكتروني اجتماعًا أم يقدّم معلومات فقط؟"
- **المهام المتوسطة (تلقائي/بعض التفكير):** تستفيد العديد من الطلبات الشائعة من درجة من المعالجة خطوة بخطوة أو فهم أعمق. يمكن أن يستخدم Gemini بمرونة إمكانية التفكير في مهام مثل:
  - تشبيه عملية التمثيل الضوئي بمرحلة النمو
  - مقارنة السيارات الكهربائية والسيارات الهجينة
- **المهام الصعبة (أقصى إمكانات التفكير):** بالنسبة إلى التحديات المعقّدة حقًا، مثل حلّ المسائل الرياضية المعقّدة أو مهام الترميز، ننصحك بضبط ميزانية تفكير عالية. تتطلّب هذه الأنواع من المهام أن يستخدم النموذج إمكاناته الكاملة في الاستدلال والتخطيط، وغالبًا ما تتضمّن العديد من الخطوات الداخلية قبل تقديم إجابة. تشمل الأمثلة ما يلي:
  - حلّ المسألة 1 في AIME 2025: أوجِد مجموع جميع الأسس الصحيحة b > 9 التي يكون فيها
    ‎17b قاسمًا لـ ‎97b.
  - اكتب رمز Python لتطبيق ويب يعرض بيانات سوق الأسهم في الوقت الفعلي، بما في ذلك مصادقة المستخدم. اجعل الرمز فعّالاً قدر الإمكان.

## النماذج والأدوات والإمكانات المتوافقة

تتوفّر ميزات "التفكير" في جميع نماذج السلسلتَين 3 و2.5.
يمكنك الاطّلاع على جميع إمكانات النموذج في صفحة
[نظرة عامة على النموذج](https://ai.google.dev/gemini-api/docs/models?hl=ar).

تعمل نماذج التفكير مع جميع أدوات Gemini وإمكاناته. يتيح ذلك للنماذج التفاعل مع الأنظمة الخارجية أو تنفيذ الرموز أو الوصول إلى المعلومات في الوقت الفعلي، ودمج النتائج في عملية الاستدلال والردّ النهائي.

يمكنك تجربة أمثلة على استخدام الأدوات مع نماذج التفكير في [كتاب الطبخ الخاص بميزة "التفكير"][Colab].

## ما هي الخطوات التالية؟

- تتوفّر تغطية ميزة "التفكير" في دليل [التوافق مع OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar#thinking).

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
