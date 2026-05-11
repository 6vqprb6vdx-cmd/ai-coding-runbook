---
source_url: https://ai.google.dev/gemini-api/docs/interactions/gemini-3?hl=ar
fetched_at: 2026-05-11T12:39:12.901685+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# دليل المطوّرين في Gemini 3

‫Gemini 3 هو أذكى مجموعة نماذج لدينا حتى الآن، وقد تم إنشاؤه بالاستناد إلى أساس من الاستدلال المتقدّم. وهو مصمّم لتحويل أي فكرة إلى واقع من خلال إتقان مهام سير العمل المستندة إلى الوكلاء والترميز المستقل والمهام المعقّدة المتعددة الوسائط.
يغطّي هذا الدليل الميزات الرئيسية لمجموعة نماذج Gemini 3 وكيفية الاستفادة منها إلى أقصى حد.

يمكنك استكشاف [مجموعتنا من تطبيقات Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=ar) للاطّلاع على كيفية تعامل النموذج مع الاستدلال المتقدّم والترميز المستقل والمهام المعقّدة
المتعددة الوسائط.

إليك بعض أسطر الرموز البرمجية للبدء:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.steps.at(-1).content[0].text);
}

run();
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## التعرّف على سلسلة Gemini 3

‫Gemini 3.1 Pro هو الأفضل للمهام المعقّدة التي تتطلّب معرفة واسعة بالعالم واستدلالاً متقدّمًا على مستوى الوسائط المتعددة.

‫Gemini 3 Flash هو أحدث نموذج لدينا من السلسلة 3، ويتميّز بذكاء على مستوى Pro وبسرعة وأسعار Flash.

‫Nano Banana Pro (المعروف أيضًا باسم Gemini 3 Pro Image) هو نموذج إنشاء الصور الأعلى جودة لدينا، وNano Banana 2 (المعروف أيضًا باسم Gemini 3.1 Flash Image) هو النموذج المكافئ الذي يتميّز بالإنتاج الكبير والكفاءة العالية والسعر المنخفض.

‫Gemini 3.1 Flash-Lite هو نموذجنا الأساسي المصمّم لتحقيق فعالية التكلفة والتعامل مع المهام الكبيرة.

جميع نماذج Gemini 3 هي حاليًا في مرحلة المعاينة.

| رقم تعريف الطراز | قدرة الاستيعاب (الإدخال / الإخراج) | تاريخ آخر تحديث للبيانات | الأسعار (الإدخال / الإخراج)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite-preview** | مليون / 64 ألف | يناير 2025 | ‫0.25 دولار أمريكي (نص، صورة، فيديو)، 0.50 دولار أمريكي (صوت) / 1.50 دولار أمريكي |
| **gemini-3.1-flash-image-preview** | 128 ألف / 32 ألف | يناير 2025 | ‫0.25 دولار أمريكي (إدخال نصي) / 0.067 دولار أمريكي (إخراج صورة)\*\* |
| **gemini-3.1-pro-preview** | مليون / 64 ألف | يناير 2025 | ‫2 دولار أمريكي / 12 دولار أمريكي (<200 ألف رمز مميّز)   4 دولارات أمريكية / 18 دولار أمريكي (>200 ألف رمز مميّز) |
| **gemini-3-flash-preview** | مليون / 64 ألف | يناير 2025 | ‫0.50 دولار أمريكي / 3 دولارات أمريكية |
| **gemini-3-pro-image-preview** | 65 ألف / 32 ألف | يناير 2025 | ‫2 دولار أمريكي (إدخال نصي) / 0.134 دولار أمريكي (إخراج صورة)\*\* |

*\* يتم تحديد الأسعار لكل مليون رمز مميّز ما لم تتم الإشارة إلى خلاف ذلك.*
*\*\* تختلف أسعار الصور حسب درجة الدقة. يمكنك الاطّلاع على [صفحة الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar) للحصول على التفاصيل.*

للاطّلاع على الحدود والأسعار والمعلومات الإضافية بالتفصيل، يُرجى الانتقال إلى صفحة
[النماذج](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar).

## ميزات واجهة برمجة التطبيقات الجديدة في Gemini 3

يقدّم Gemini 3 معلّمات جديدة مصمّمة لمنح المطوّرين مزيدًا من التحكّم في وقت الاستجابة والتكلفة ودقة الوسائط المتعددة.

### مستوى التفكير

تستخدم نماذج سلسلة Gemini 3 التفكير الديناميكي تلقائيًا للاستنتاج من خلال الطلبات. يمكنك استخدام المَعلمة `thinking_level` التي تتحكّم في **الحد الأقصى** لعمق عملية الاستنتاج الداخلية للنموذج قبل أن يُنشئ ردًا. يعامل Gemini 3 هذه المستويات على أنّها مخصّصات نسبية للتفكير بدلاً من ضمانات صارمة للرموز المميّزة.

إذا لم يتم تحديد `thinking_level`، سيستخدم Gemini 3 القيمة التلقائية `high`. للحصول على ردود أسرع وأقل وقت استجابة عندما لا يكون الاستنتاج المعقّد مطلوبًا، يمكنك حصر مستوى التفكير في النموذج على `low`.

| مستوى التفكير | Gemini 3.1 Pro | ‎3.1 Flash-Lite | Gemini 3 Flash | الوصف |
| --- | --- | --- | --- | --- |
| **`minimal`** | غير متاح | متاح (تلقائي) | متاح | يطابق الإعداد "بدون تفكير" لمعظم طلبات البحث. قد يفكّر النموذج بشكل بسيط جدًا لمهام الترميز المعقّدة. يقلّل وقت الاستجابة لتطبيقات المحادثة أو التطبيقات التي تعالج البيانات بمعدّل أعلى لنقل البيانات. ملاحظة: لا يضمن `minimal` إيقاف التفكير. |
| **`low`** | متاح | متاح | متاح | يقلّل وقت الاستجابة والتكلفة. الأفضل لاتّباع التعليمات البسيطة أو المحادثة أو التطبيقات التي تعالج البيانات بسرعة كبيرة. |
| **`medium`** | متاح | متاح | متاح | تفكير متوازن لمعظم المهام. |
| **`high`** | متاح (تلقائي، ديناميكي) | متاح (ديناميكي) | متاح (تلقائي، ديناميكي) | يزيد عمق الاستنتاج إلى أقصى حد. قد يستغرق النموذج وقتًا أطول بكثير للوصول إلى أول رمز مميّز للناتج (غير التفكير)، ولكن سيكون الناتج أكثر استنتاجًا بعناية. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.steps.at(-1).content[0].text);
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### درجة الحرارة

بالنسبة إلى جميع نماذج Gemini 3، ننصحك بشدة بإبقاء مَعلمة درجة العشوائية على قيمتها التلقائية `1.0`.

في حين أنّ النماذج السابقة كانت تستفيد غالبًا من ضبط درجة العشوائية للتحكّم في الإبداع مقابل الحتمية، تم تحسين إمكانات الاستدلال في Gemini 3 للإعداد التلقائي. قد يؤدي تغيير درجة العشوائية (ضبطها على قيمة أقل من 1.0) إلى سلوك غير متوقّع، مثل التكرار أو تدهور الأداء، خاصةً في المهام الرياضية أو الاستدلالية المعقّدة.

### توقيعات الأفكار

تستخدم نماذج Gemini 3 توقيعات الأفكار للحفاظ على سياق الاستنتاج في جميع طلبات البيانات من واجهة برمجة التطبيقات. هذه التوقيعات هي تمثيلات مشفّرة لعملية التفكير الداخلية للنموذج.

- **الوضع المستند إلى الحالة (ننصح به)**: عند استخدام Interactions API في الوضع المستند إلى الحالة (توفير `previous_interaction_id`)، يدير الخادم تلقائيًا سجلّ المحادثات وتوقيعات الأفكار.
- **الوضع غير المستند إلى الحالة**: إذا كنت تدير سجلّ المحادثات يدويًا، عليك تضمين كتل الأفكار مع توقيعاتها في الطلبات اللاحقة للتحقّق من صحتها.

للحصول على معلومات مفصّلة، يُرجى الاطّلاع على صفحة [توقيعات الأفكار](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=ar).

### مُخرجات منظَّمة باستخدام الأدوات

تتيح لك نماذج Gemini 3 الجمع بين [المُخرجات المنظَّمة](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=ar) والأدوات المضمّنة، بما في ذلك [تحديد المصدر من خلال "بحث Search"](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=ar) وسياق عنوان URL وتنفيذ الرموز البرمجية واستدعاء الدوال.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.steps[-1].content[0].text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
  console.log(match);
}

run();
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### إنشاء الصور

يتيح لك Gemini 3.1 Flash Image وGemini 3 Pro Image إنشاء الصور وتعديلها من الطلبات النصية. يستخدم النموذج الاستدلال "للتفكير" في الطلب ويمكنه استرداد البيانات في الوقت الفعلي، مثل التنبؤات الجوية أو الرسوم البيانية للأسهم، قبل استخدام [بحث Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=ar) لتحديد المصدر قبل إنشاء صور عالية الدقة.

**الإمكانات الجديدة والمحسّنة:**

- **درجة دقة 4K وعرض النصوص:** يمكنك إنشاء نصوص ورسوم بيانية واضحة وسهلة القراءة بدرجات دقة تصل إلى 2K و4K.
- **الإنشاء المستند إلى Grounding:** يمكنك استخدام أداة `google_search` للتحقّق من الحقائق وإنشاء الصور استنادًا إلى معلومات العالم الواقعي. تتوفّر ميزة Grounding with Google *Image* Search لنموذج Gemini 3.1 Flash Image.
- **التعديل الحواري:** يمكنك تعديل الصور في محادثة متعددة الجولات من خلال طلب إجراء تغييرات (على سبيل المثال، "اجعل الخلفية غروب الشمس"). تعتمد سير العمل هذا على **توقيعات الأفكار** للحفاظ على السياق المرئي بين الجولات.

للاطّلاع على التفاصيل الكاملة حول نسب العرض إلى الارتفاع وسير عمل التعديل وخيارات الإعداد
، يُرجى الانتقال إلى [دليل إنشاء الصور](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=ar).

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

image_blocks = [content_block for content_block in interaction.steps[-1].content if content_block.type == "image"]
if image_blocks:
    image_data = base64.b64decode(image_blocks[0].data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  for (const contentBlock of interaction.steps.at(-1).content) {
    if (contentBlock.type === "image") {
      const buffer = Buffer.from(contentBlock.data, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**مثال على الرد**

![الطقس في طوكيو](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=ar)

### تنفيذ الرموز البرمجية باستخدام الصور

يمكن أن يعامل Gemini 3 Flash الرؤية على أنّها تحقيق نشط، وليس مجرد نظرة ثابتة. من خلال الجمع بين الاستنتاج وتنفيذ [الرموز البرمجية](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=ar)، يضع النموذج خطة، ثم يكتب وينفّذ
رموز Python البرمجية لتكبير الصور أو اقتصاصها أو إضافة تعليقات توضيحية إليها أو معالجتها بطريقة أخرى
خطوةً بخطوة لتثبيت إجاباته بصريًا.

**حالات الاستخدام:**

- **التكبير والتفحّص:** يرصد النموذج ضمنيًا عندما تكون التفاصيل صغيرة جدًا (على سبيل المثال، قراءة مقياس أو رقم تسلسلي بعيدَين) ويكتب رموزًا برمجية لاقتصاص المنطقة وإعادة فحصها بدقة أعلى.
- **الرياضيات والرسم البياني المرئيان:** يمكن للنموذج إجراء عمليات حسابية متعددة الخطوات باستخدام الرموز البرمجية (على سبيل المثال، جمع بنود في إيصال أو إنشاء رسم بياني باستخدام Matplotlib من البيانات المستخرَجة).
- **التعليقات التوضيحية على الصور:** يمكن للنموذج رسم أسهم أو مربعات إحاطة أو تعليقات توضيحية أخرى مباشرةً على الصور للإجابة عن الأسئلة المكانية مثل "أين يجب وضع هذا العنصر؟".

لتفعيل التفكير المرئي، يمكنك إعداد [تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=ar) كأداة. سيستخدم النموذج تلقائيًا الرموز البرمجية لمعالجة الصور عند الحاجة.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### راحة

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

لمزيد من التفاصيل حول تنفيذ الرموز البرمجية باستخدام الصور، يُرجى الاطّلاع على [تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=ar#images).

### ردود الدوال المتعددة الوسائط

[تتيح ميزة استدعاء الدوال المتعددة الوسائط](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar#multimodal)
للمستخدمين الحصول على ردود دوال تحتوي على
عناصر متعددة الوسائط، ما يسمح بتحسين استخدام إمكانات استدعاء الدوال
في النموذج. لا يتيح استدعاء الدوال العادي سوى ردود الدوال النصية:

### Python

```
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

model_output_step = next(s for s in interaction_2.steps if s.type == "model_output")
print(f"\nFinal model response: {model_output_step.content[0].text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

// 1. Define the tool
const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

// 2. Send the request with tools
const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

// 3. Find the function call step
const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

// Execute tool (fetch image)
const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

// 4. Send multimodal function result back
const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.steps.at(-1).content[0].text}`);
```

### راحة

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

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### الجمع بين الأدوات المضمّنة واستدعاء الدوال

[يتيح Gemini 3 استخدام الأدوات المضمّنة (مثل بحث Google وسياق عنوان URL
والمزيد](https://ai.google.dev/gemini-api/docs/tools?hl=ar)) وأدوات استدعاء الدوال المخصّصة[في طلب بيانات من واجهة برمجة التطبيقات نفسه، ما يسمح بإنشاء مهام سير عمل أكثر تعقيدًا
.](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar)

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

# Find the function call step
fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    # Simulate a function result
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

// Find the function call step
const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.steps.at(-1).content[0].text);
}
```

## نقل البيانات من Gemini 2.5

‫Gemini 3 هو أقدر مجموعة نماذج لدينا حتى الآن، ويقدّم تحسينًا تدريجيًا مقارنةً بـ Gemini 2.5. عند نقل البيانات، يُرجى مراعاة ما يلي:

- **التفكير:** إذا كنت تستخدم سابقًا هندسة الطلبات المعقّدة (مثل
  سلسلة الأفكار) لإجبار Gemini 2.5 على الاستنتاج، جرِّب Gemini 3 مع
  `thinking_level: "high"` والطلبات البسيطة.
- **إعدادات درجة العشوائية:** إذا كان الرمز البرمجي الحالي يضبط درجة العشوائية بشكل صريح (خاصةً على قيم منخفضة للنتائج الخوارزمية الحتمية)، ننصحك بإزالة هذه المَعلمة واستخدام القيمة التلقائية لـ Gemini 3 وهي 1.0 لتجنُّب المشاكل المحتملة في التكرار أو تدهور الأداء في المهام المعقّدة.
- **فهم ملفات PDF والمستندات:** إذا كنت تعتمد على سلوك معيّن لتحليل المستندات الكثيفة، اختبِر الإعداد الجديد `media_resolution_high` لضمان استمرار الدقة.
- **استهلاك الرموز المميّزة:** قد يؤدي نقل البيانات إلى الإعدادات التلقائية في Gemini 3 إلى **زيادة** استخدام الرموز المميّزة لملفات PDF، ولكن **تقليل** استخدام الرموز المميّزة للفيديوهات. إذا كانت الطلبات تتجاوز الآن قدرة الاستيعاب بسبب درجات الدقة التلقائية الأعلى، ننصحك بتقليل درجة دقة الوسائط بشكل صريح.
- **تقسيم الصور:** لا تتوفّر إمكانات تقسيم الصور (عرض أقنعة على مستوى البكسل للكائنات) في Gemini 3 Pro أو Gemini 3 Flash. بالنسبة إلى
  أحمال العمل التي تتطلّب تقسيم الصور المضمّن، ننصحك بمتابعة
  استخدام Gemini 2.5 Flash مع إيقاف التفكير أو [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ar).
- **استخدام الكمبيوتر:** يتيح Gemini 3 Pro وGemini 3 Flash استخدام [الكمبيوتر
  الكمبيوتر](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=ar). على عكس السلسلة 2.5، لست بحاجة إلى استخدام نموذج منفصل للوصول إلى أداة استخدام الكمبيوتر.
- **توافق الأدوات**: [أصبح الجمع بين الأدوات المضمّنة واستدعاء الدوال](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=ar) متاحًا الآن لنماذج Gemini 3. [أصبحت ميزة Grounding with Google Maps
  متاحة أيضًا الآن لنماذج Gemini 3
  .](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=ar)

## التوافق مع OpenAI

بالنسبة إلى المستخدمين الذين يستخدِمون [طبقة التوافق مع OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar)، يتم تلقائيًا ربط
المَعلمات العادية (مَعلمة `reasoning_effort` من OpenAI) بالمَعلمات المكافئة في
Gemini (`thinking_level`).

## أفضل الممارسات المتعلّقة بالطلبات

‫Gemini 3 هو نموذج استدلال، ما يغيّر طريقة إنشاء الطلبات.

- **تعليمات دقيقة:** يجب أن تكون طلبات الإدخال موجزة. يستجيب Gemini 3 بشكل أفضل للتعليمات المباشرة والواضحة. قد يفرط في تحليل تقنيات هندسة الطلبات المطوّلة أو المعقّدة جدًا التي كانت تُستخدم للنماذج القديمة.
- **الإسهاب في الناتج:** يكون Gemini 3 أقل إسهابًا تلقائيًا ويفضّل تقديم إجابات مباشرة وفعّالة. إذا كانت حالة الاستخدام تتطلّب شخصية أكثر حوارية أو "ثرثرة"، عليك توجيه النموذج بشكل صريح في الطلب (على سبيل المثال، "اشرح هذا الأمر كمساعد ودود وثَرثار").
- **إدارة السياق:** عند العمل مع مجموعات بيانات كبيرة (على سبيل المثال، كتب كاملة أو
  قواعد رموز أو فيديوهات طويلة)، ضَع التعليمات أو الأسئلة المحدّدة في
  نهاية الطلب، بعد سياق البيانات. يمكنك تثبيت استنتاج النموذج على البيانات المقدَّمة من خلال بدء سؤالك بعبارة مثل "استنادًا إلى المعلومات السابقة...".

مزيد من المعلومات حول استراتيجيات تصميم الطلبات في الـ [دليل هندسة الطلبات](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ar).

## الأسئلة الشائعة

1. **ما هو تاريخ آخر تحديث للبيانات في Gemini 3؟** تاريخ آخر تحديث للبيانات في نماذج Gemini 3 هو يناير 2025. للحصول على معلومات أحدث، استخدِم أداة
   [Grounding with Google Search](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=ar).
2. **ما هي حدود قدرة الاستيعاب؟** تتيح نماذج Gemini 3 قدرة استيعاب للإدخال تصل إلى مليون رمز مميّز وقدرة استيعاب للإخراج تصل إلى 64 ألف رمز مميّز.
3. **هل تتوفّر فئة مجانية لـ Gemini 3؟** يتوفّر في Gemini API فئة مجانية لنموذج Gemini 3 Flash `gemini-3-flash-preview`. يمكنك تجربة Gemini 3.1 Pro و3 Flash مجانًا في Google AI Studio، ولكن لا تتوفّر فئة مجانية لنموذج `gemini-3.1-pro-preview` في Gemini API.
4. **هل سيظل الرمز البرمجي القديم `thinking_budget` يعمل؟** نعم، لا يزال `thinking_budget` متاحًا للتوافق مع الإصدارات السابقة، ولكن ننصحك بنقل البيانات إلى `thinking_level` للحصول على أداء أكثر قابلية للتوقّع. يُرجى عدم استخدام كليهما في الطلب نفسه.
5. **هل يتيح Gemini 3 استخدام Batch API؟** نعم، يتيح Gemini 3 استخدام
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar).
6. **هل تتوفّر ميزة Context Caching؟** نعم، تتوفّر ميزة [Context Caching](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=ar) لـ Gemini 3.
7. **ما هي الأدوات المتاحة في Gemini 3؟** يتيح Gemini 3 استخدام
   [بحث Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=ar) و
   [استخدام "خرائط Google" كمصدر](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=ar) والبحث عن الملفات
   [File Search](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=ar) وتنفيذ الرموز البرمجية
   [Code Execution](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=ar) وسياق عنوان URL
   [URL Context](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=ar). ويتيح أيضًا
   استدعاء الدوال[العادي](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar) لأدواتك المخصّصة، وبالاشتراك مع
   [الأدوات المضمّنة](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=ar).
8. **ما هو `gemini-3.1-pro-preview-customtools`؟** إذا كنت تستخدم
   `gemini-3.1-pro-preview` ويتجاهل النموذج أدواتك المخصّصة لصالح
   أوامر bash، جرِّب نموذج `gemini-3.1-pro-preview-customtools` بدلاً من ذلك.
   مزيد من المعلومات [هنا][customtools-model].

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-11 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-11 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
