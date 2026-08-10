---
source_url: https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=ar
fetched_at: 2026-08-10T03:12:04.480191+00:00
title: "\u0627\u0644\u0631\u0624\u064a\u0629 \u0627\u0644\u0645\u0633\u062a\u0646\u0650\u062f\u0629 \u0625\u0644\u0649 \u0627\u0644\u0630\u0643\u0627\u0621 \u0627\u0644\u0627\u0635\u0637\u0646\u0627\u0639\u064a \u0627\u0644\u0648\u0643\u064a\u0644 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الرؤية المستنِدة إلى الذكاء الاصطناعي الوكيل

يمكن لنماذج Gemini Robotics ER كتابة رموز Python البرمجية وتنفيذها لمعالجة الصور وتطبيق المنطق قبل تقديم الإجابة. تتضمّن هذه الصفحة أمثلة على تنفيذ الرموز البرمجية، مثل رصد العناصر باستخدام التكبير والقص، وقراءة الأدوات، وقياس السوائل، وقراءة لوحات الدوائر الكهربائية، والتعليق التوضيحي على الصور.

لتكييف هذه الأمثلة مع حالة الاستخدام الخاصة بك، استبدِل نص الطلب وملف الصورة الذي تم تحميله بنصك وملفك. يمكنك أيضًا تعديل مخطط JSON المطلوب في الطلب ليتطابق مع بنية الإخراج التي يحتاجها تطبيقك، أو إضافة `system_instruction` لفرض تنسيق الإخراج ودقته.

للاطّلاع على الرمز الكامل القابل للتنفيذ، راجِع
[كتاب وصفات الروبوتات](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## مستوى التفكير

يمكنك التحكّم في مستوى التفكير للنموذج من أجل تحقيق التوازن بين وقت الاستجابة والدقة. تؤدي المهام المكانية، مثل رصد العناصر، أداءً جيدًا مع مستوى تفكير منخفض. تستفيد المهام المعقّدة، مثل
العد أو تقدير الوزن، من مستوى تفكير أعلى.

يضبط المثال التالي مستوى التفكير على `high` لمهمة عدّ معقّدة:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="scene.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": "Identify and count all objects on the table."}
    ],
    generation_config={
        "thinking_level": "high"  # Use "minimal" or "low" for faster spatial tasks
    }
)

print(interaction.output_text)
```

لمزيد من التفاصيل، يُرجى الاطّلاع على [التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar).

## رصد العناصر (التكبير والاقتصاص)

يستخدم المثال التالي تنفيذ الرمز البرمجي لتكبير صورة واقتصاصها من أجل عرضها بشكل أوضح عند رصد العناصر وعرض المربّعات المحيطة.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="sorting.jpeg")

prompt = """
Return JSON in the format {label: val, y: val, x: val, y2: val, x2: val} for
the compostable objects in this scene. Please Zoom and crop the image for a
clearer view. Return an annotated image of the final result with the bounding
boxes drawn on it to the API caller as a part of your process.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

ستكون مخرجات النموذج مشابهة لاستجابة JSON التالية:

```
[
  {"label": "compostable", "y": 256, "x": 482, "y2": 295, "x2": 546},
  {"label": "compostable", "y": 317, "x": 478, "y2": 350, "x2": 542},
  {"label": "compostable", "y": 586, "x": 556, "y2": 668, "x2": 595},
  {"label": "compostable", "y": 463, "x": 669, "y2": 511, "x2": 718},
  {"label": "compostable", "y": 178, "x": 565, "y2": 250, "x2": 609}
]
```

تعرض الصورة التالية المربّعات التي تم إرجاعها من النموذج.

![مثال يعرض مربّعات الإحاطة للعناصر التي تم العثور عليها](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-bounding-boxes.png?hl=ar)

## قراءة مقياس تناظري وتطبيق المنطق

يوضّح المثال التالي كيفية استخدام النموذج لقراءة مقياس تناظري وإجراء عمليات حسابية متعلقة بالوقت. يستخدم تعليمات النظام لفرض إخراج JSON.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="gauge.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    system_instruction="Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block).",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": """Read the current value from this gauge. Then, calculate how long
        it will take at the current rate for the value to reach maximum.
        Reply in JSON: {"current_value": val, "max_value": val,
        "time_to_max_minutes": val}"""}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

## قياس السائل في وعاء

يوضّح المثال التالي كيفية استخدام تنفيذ الرمز البرمجي لقياس مستوى السائل في حاوية.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="fluid.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    system_instruction="Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block).",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": """Measure the amount of fluid in the container. Reply in JSON:
        {"fluid_level_ml": val, "container_capacity_ml": val,
        "percentage_full": val}"""}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

## قراءة العلامات على لوحة الدوائر

يوضّح المثال التالي كيفية استخدام تنفيذ الرمز البرمجي لقراءة العلامات على لوحة الدوائر.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="circuit_board.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    system_instruction="Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block).",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": """Read all visible component labels and markings on this circuit
        board. Reply in JSON: {"components": [{"label": val,
        "location": [y, x]}]}"""}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

![مثال يعرض علامات على لوحة دوائر كهربائية](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-circuit-board.png?hl=ar)

## التعليق التوضيحي على الصور

يوضّح المثال التالي كيفية استخدام تنفيذ الرمز البرمجي لإضافة تعليق توضيحي إلى صورة (مثل رسم أسهم لتعليمات التخلص من النفايات) وعرض الصورة المعدَّلة.

### Python

```
from google import genai

client = genai.Client()

# Load your image
uploaded_file = client.files.upload(file="sorting.jpeg")

prompt = """
Look at this image and return it as an annotated version using arrows of
different colors to represent which items should go in which bins for
disposal. You must return the final image to the API caller.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

في ما يلي مثال على إدخال صورة.

![مثال يعرض ساعة للقراءة](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-image-annotation.png?hl=ar)

ستكون مخرجات النموذج مشابهة لما يلي:

```
  The annotated image shows the suggested disposal locations for the items on the table:
  - **Green bin (Compost/Organic)**: Green chili, red chili, grapes, and cherries.
  - **Blue bin (Recycling)**: Yellow crushed can and plastic container.
  - **Black bin (Trash)**: Chocolate bar wrapper, Welch's packet, and white tissue.
```

## الخطوات التالية

- [تنظيم المهام](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ar): مهام طويلة الأمد باستخدام واجهات برمجة تطبيقات مخصّصة للروبوتات
- [الروبوتات التي تتضمّن بثًا مباشرًا](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ar): بث مباشر ثنائي الاتجاه في الوقت الفعلي (Gemini Robotics ER 2 فقط)
- [فهم الفيديو](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ar): العثور على اللحظات وتصنيف مستوى التقدّم (الإصدار الثاني من Gemini Robotics فقط)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
