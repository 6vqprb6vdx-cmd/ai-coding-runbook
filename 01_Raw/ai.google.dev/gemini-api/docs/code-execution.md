---
source_url: https://ai.google.dev/gemini-api/docs/code-execution?hl=ar
fetched_at: 2026-08-24T02:30:51.401345+00:00
title: "\u062a\u0646\u0641\u064a\u0630 \u0627\u0644\u0631\u0645\u0632 \u0627\u0644\u0628\u0631\u0645\u062c\u064a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تنفيذ الرمز البرمجي

توفّر Gemini API أداة لتنفيذ الرموز البرمجية تتيح للنموذج إنشاء رموز Python البرمجية وتشغيلها. يمكن للنموذج بعد ذلك التعلّم بشكل متكرّر من نتائج تنفيذ الرموز البرمجية إلى أن يصل إلى ناتج نهائي. يمكنك استخدام أداة تنفيذ الرموز البرمجية لإنشاء تطبيقات تستفيد من إمكانات الاستنتاج المستندة إلى الرموز البرمجية. على سبيل المثال، يمكنك استخدام أداة تنفيذ الرموز البرمجية لحلّ المعادلات أو معالجة النصوص. يمكنك
أيضًا استخدام [المكتبات](#supported-libraries) المضمّنة في بيئة تنفيذ الرموز البرمجية
لإجراء مهام أكثر تخصّصًا.

لا يمكن لـ Gemini تنفيذ الرموز البرمجية إلا بلغة Python. يمكنك مع ذلك أن تطلب من Gemini إنشاء رموز برمجية بلغة أخرى، ولكن لا يمكن للنموذج استخدام أداة تنفيذ الرموز البرمجية لتشغيلها.

## تفعيل أداة تنفيذ الرموز البرمجية

لتفعيل أداة تنفيذ الرموز البرمجية، عليك ضبطها على النموذج. يسمح ذلك للنموذج بإنشاء الرموز البرمجية وتشغيلها.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the sum of the first 50 prime numbers? "
          "Generate and run code for the calculation, and make sure you get all 50.",
    tools=[{"type": "code_execution"}]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
    elif step.type == "code_execution_call":
        print(step.arguments.code)
    elif step.type == "code_execution_result":
        print(step.result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What is the sum of the first 50 prime numbers? " +
           "Generate and run code for the calculation, and make sure you get all 50.",
    tools: [{ type: "code_execution" }]
});

for (const step of interaction.steps) {
    if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log(contentBlock.text);
            }
        }
    } else if (step.type === "code_execution_call") {
        console.log(step.arguments.code);
    } else if (step.type === "code_execution_result") {
        console.log(step.result);
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
    "input": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50.",
    "tools": [{"type": "code_execution"}]
}'
```

قد تبدو النتيجة على النحو التالي، وقد تم تنسيقها لتسهيل قراءتها:

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

تجمع هذه النتيجة عدة أجزاء من المحتوى يعرضها النموذج عند استخدام أداة تنفيذ الرموز البرمجية:

- `text`: نص مضمّن ينشئه النموذج
- `code_execution_call`: رمز ينشئه النموذج ويكون الهدف منه تنفيذه
- `code_execution_result`: نتيجة الرمز القابل للتنفيذ

## تنفيذ الرموز البرمجية باستخدام الصور (Gemini 3)

يمكن الآن لنموذج Gemini 3 Flash كتابة رموز Python البرمجية وتنفيذها لمعالجة الصور وفحصها بشكل نشط.

**حالات الاستخدام**

- **التكبير والفحص**: يرصد النموذج ضمنيًا ما إذا كانت التفاصيل صغيرة جدًا
  (مثل قراءة مقياس بعيد)، ويكتب رمزًا لقصّ المنطقة وإعادة فحصها
  بدقة أعلى.
- **الرياضيات المرئية**: يمكن للنموذج إجراء عمليات حسابية متعددة الخطوات باستخدام الرموز البرمجية (مثل
  جمع بنود في فاتورة).
- **إضافة تعليقات توضيحية إلى الصور**: يمكن للنموذج إضافة تعليقات توضيحية إلى الصور للإجابة عن الأسئلة، مثل
  رسم أسهم لإظهار العلاقات.

## تفعيل أداة تنفيذ الرموز البرمجية باستخدام الصور

تتوفّر أداة تنفيذ الرموز البرمجية باستخدام الصور رسميًا في Gemini 3 Flash. يمكنك تفعيل هذا السلوك من خلال تفعيل كل من "الاستخدام كأداة تنفيذ رموز برمجية" و"التفكير".

### Python

```
from google import genai
import requests
import base64
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "image", "data": base64.b64encode(image_bytes).decode('utf-8'), "mime_type": "image/jpeg"},
        {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
    ],
    tools=[{"type": "code_execution"}]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                img = Image.open(io.BytesIO(base64.b64decode(content_block.data)))
                img.show()  # or: img.save("output_image.jpg")
    elif step.type == "code_execution_call":
        print(step.arguments.code)
    elif step.type == "code_execution_result":
        print(step.result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {
  const client = new GoogleGenAI({});

  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
      {
        type: "image",
        data: base64ImageData,
        mime_type: "image/jpeg"
      },
      { type: "text", text: "Zoom into the expression pedals and tell me how many pedals are there?" }
    ],
    tools: [{ type: "code_execution" }]
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log(`\nGenerated Code:\n`, step.arguments.code);
    } else if (step.type === "code_execution_result") {
      console.log(`\nExecution Output:\n`, step.result);
    }
  }
}

main();
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

# Use jq to create the JSON payload to avoid "Argument list too long" error with large base64 strings
echo -n "$IMAGE_B64" > image_b64.txt
jq -n \
  --rawfile b64 image_b64.txt \
  --arg mime "$MIME_TYPE" \
  '{
    model: "gemini-3.6-flash",
    input: [
      {type: "image", data: $b64, mime_type: $mime},
      {type: "text", text: "Zoom into the expression pedals and tell me how many pedals are there?"}
    ],
    tools: [{type: "code_execution"}]
  }' > payload.json

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d @payload.json
```

## استخدام أداة تنفيذ الرموز البرمجية في التفاعلات المتعددة الأدوار

يمكنك أيضًا استخدام أداة تطبيق الرموز البرمجية كجزء من محادثة مترابطة باستخدام `previous_interaction_id`.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="I have a math question for you.",
    tools=[{"type": "code_execution"}]
)
print(interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    previous_interaction_id=interaction1.id,
    input="What is the sum of the first 50 prime numbers? "
          "Generate and run code for the calculation, and make sure you get all 50.",
    tools=[{"type": "code_execution"}]
)

for step in interaction2.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
    elif step.type == "code_execution_call":
        print(step.arguments.code)
    elif step.type == "code_execution_result":
        print(step.result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction1 = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "I have a math question for you.",
    tools: [{ type: "code_execution" }]
});
console.log(interaction1.output_text);

const interaction2 = await client.interactions.create({
    model: "gemini-3.6-flash",
    previous_interaction_id: interaction1.id,
    input: "What is the sum of the first 50 prime numbers? " +
           "Generate and run code for the calculation, and make sure you get all 50.",
    tools: [{ type: "code_execution" }]
});

for (const step of interaction2.steps) {
    if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log(contentBlock.text);
            }
        }
    } else if (step.type === "code_execution_call") {
        console.log(step.arguments.code);
    } else if (step.type === "code_execution_result") {
        console.log(step.result);
    }
}
```

### REST

```
# First turn
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
    "model": "gemini-3.6-flash",
    "input": "I have a math question for you.",
    "tools": [{"type": "code_execution"}]
}')

INTERACTION_ID=$(echo $RESPONSE1 | jq -r '.id')

# Second turn with previous_interaction_id
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
    "model": "gemini-3.6-flash",
    "previous_interaction_id": "'"$INTERACTION_ID"'",
    "input": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50.",
    "tools": [{"type": "code_execution"}]
}'
```

## الإدخال/الإخراج

في نماذج Gemini الحالية، مثل
[Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#gemini-3.6-flash)، تتيح أداة تنفيذ الرموز البرمجية إدخال الملفات وإخراج الرسومات البيانية. باستخدام إمكانات الإدخال والإخراج هذه
، يمكنك تحميل ملفات CSV وملفات نصية وطرح أسئلة حول
الملفات، وإنشاء رسومات بيانية باستخدام [Matplotlib](https://matplotlib.org/) كجزء
من الردّ. يتم عرض ملفات الإخراج كصور مضمّنة في الردّ.

### أسعار الإدخال/الإخراج

عند استخدام إمكانات الإدخال/الإخراج لأداة تنفيذ الرموز البرمجية، يتم تحصيل رسوم منك مقابل الرموز المميّزة المدخَلة والرموز المميّزة الناتجة:

**الرموز المميّزة المدخَلة:**

- طلب المستخدم

**الرموز المميّزة الناتجة:**

- الرمز الذي ينشئه النموذج
- ناتج تطبيق الرموز البرمجية في بيئة الرمز
- رموز التفكير المميّزة
- الملخّص الذي ينشئه النموذج

### تفاصيل الإدخال/الإخراج

عند استخدام إمكانات الإدخال/الإخراج لأداة تنفيذ الرموز البرمجية، يُرجى العِلم بالتفاصيل الفنية التالية:

- الحدّ الأقصى لوقت تشغيل بيئة الرمز هو 30 ثانية.
- إذا أدت بيئة الرمز إلى حدوث خطأ، قد يقرّر النموذج إعادة إنشاء ناتج الرمز. يمكن أن يحدث ذلك ما يصل إلى 5 مرات.
- يتم تحديد الحدّ الأقصى لحجم ملف الإدخال من خلال نافذة الرموز المميّزة للنموذج. إذا حمّلت ملفًا يتجاوز الحدّ الأقصى لنافذة السياق للنموذج، ستعرض واجهة برمجة التطبيقات خطأً.
- تعمل أداة تنفيذ الرموز البرمجية بشكل أفضل مع الملفات النصية وملفات CSV.
- يمكن تمرير ملف الإدخال كبيانات مضمّنة أو تحميله باستخدام الـ
  [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar)،
  ويتم دائمًا عرض ملف الإخراج كبيانات مضمّنة.

## الفوترة

لا يتم تحصيل أي رسوم إضافية مقابل تفعيل أداة تنفيذ الرموز البرمجية من Gemini API.
سيتم تحصيل رسوم منك بالسعر الحالي للرموز المميّزة المدخَلة والرموز المميّزة الناتجة استنادًا إلى نموذج Gemini الذي تستخدمه.

في ما يلي بعض المعلومات الأخرى التي يجب معرفتها حول الفوترة المتعلقة بأداة تنفيذ الرموز البرمجية:

- يتم تحصيل رسوم منك مرة واحدة فقط مقابل الرموز المميّزة المدخَلة التي تمرّرها إلى النموذج، ويتم تحصيل رسوم منك مقابل الرموز المميّزة الناتجة النهائية التي يعرضها لك النموذج.
- يتم احتساب الرموز المميّزة التي تمثّل الرمز الذي تم إنشاؤه كرموز مميّزة ناتجة. يمكن أن يشمل الرمز الذي تم إنشاؤه نصًا ونتائج متعددة الوسائط، مثل الصور.
- يتم أيضًا احتساب نتائج تنفيذ الرموز البرمجية كرموز مميّزة ناتجة.

يظهر نموذج الفوترة في الرسم البياني التالي:

![نموذج الفوترة لتنفيذ الرموز البرمجية](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=ar)

- يتم تحصيل رسوم منك بالسعر الحالي للرموز المميّزة المدخَلة والرموز المميّزة الناتجة استنادًا إلى نموذج Gemini الذي تستخدمه.
- إذا استخدم Gemini أداة تنفيذ الرموز البرمجية عند إنشاء ردّك، يتم تصنيف الطلب الأصلي والرمز الذي تم إنشاؤه ونتيجة الرمز الذي تم تنفيذه على أنّها *رموز مميّزة وسيطة* ويتم تحصيل رسوم منك مقابلها كـ *رموز مميّزة مدخَلة*.
- بعد ذلك، ينشئ Gemini ملخّصًا ويعرض الرمز الذي تم إنشاؤه ونتيجة الرمز الذي تم تنفيذه والملخّص النهائي. ويتم تحصيل رسوم منك مقابل هذه العناصر كـ *رموز مميّزة ناتجة*.
- يتضمّن Gemini API عدد الرموز المميّزة الوسيطة في الردّ من واجهة برمجة التطبيقات، ما يتيح لك معرفة سبب حصولك على رموز مميّزة مدخَلة إضافية بخلاف طلبك الأولي.

## القيود

- لا يمكن للنموذج سوى إنشاء الرموز البرمجية وتنفيذها. لا يمكنه عرض عناصر أخرى، مثل ملفات الوسائط.
- في بعض الحالات، يمكن أن يؤدي تفعيل أداة تنفيذ الرموز البرمجية إلى حدوث تراجع في جوانب أخرى من مخرجات النموذج (على سبيل المثال، كتابة قصة).
- هناك بعض الاختلاف في قدرة النماذج المختلفة على استخدام أداة تنفيذ الرموز البرمجية بنجاح.

## مجموعات الأدوات المتوافقة

يمكن الجمع بين أداة تنفيذ الرموز البرمجية و
[أداة تحديد المصدر من خلال "بحث Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) لـ
تقديم حالات استخدام أكثر تعقيدًا.

تتيح نماذج Gemini 3 الجمع بين الأدوات المضمّنة (مثل أداة تنفيذ الرموز البرمجية) والأدوات المخصّصة (استدعاء الدوال).

## المكتبات المتوافقة

تتضمّن بيئة تنفيذ الرموز البرمجية المكتبات التالية:

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
- مكتبة نامبي
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
- tabulate
- tensorflow
- toolz
- xlrd

لا يمكنك تثبيت مكتباتك الخاصة.

## الخطوات التالية

- جرِّب [دليل التشغيل السريع لواجهة برمجة التطبيقات Interactions API](https://ai.google.dev/gemini-api/docs/quickstart?hl=ar).
- تعرَّف على أدوات Gemini API الأخرى:
  - [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)
  - [تحديد المصدر من خلال "بحث Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
