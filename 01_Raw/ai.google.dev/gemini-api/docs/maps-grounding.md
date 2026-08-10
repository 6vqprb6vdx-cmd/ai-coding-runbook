---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar
fetched_at: 2026-08-10T03:11:28.878786+00:00
title: "\u0627\u0644\u0627\u0633\u062a\u0646\u0627\u062f \u0625\u0644\u0649 \"\u062e\u0631\u0627\u0626\u0637 Google\" \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الاستناد إلى "خرائط Google"

يتيح استخدام "خرائط Google" كمصدر ربط الإمكانات الإنشائية في Gemini بالبيانات الغنية والحقيقية والحديثة في "خرائط Google". تتيح هذه الميزة للمطوّرين دمج وظائف تستند إلى الموقع الجغرافي بسهولة في تطبيقاتهم. عندما يتضمّن طلب المستخدم سياقًا مرتبطًا ببيانات "خرائط Google"، يستفيد نموذج Gemini من "خرائط Google" لتقديم إجابات دقيقة ومحدّثة تستند إلى الحقائق وذات صلة بالموقع الجغرافي أو المنطقة العامة التي حدّدها المستخدم.

- **ردود دقيقة تستند إلى الموقع الجغرافي:** يمكنك الاستفادة من بيانات "خرائط Google" الشاملة والحديثة للردّ على طلبات البحث الجغرافية.
- **تخصيص محسَّن:** يمكنك تخصيص الاقتراحات والمعلومات استنادًا إلى المواقع الجغرافية التي يقدّمها المستخدمون.

## البدء

يوضِّح هذا المثال كيفية دمج ميزة استخدام "خرائط Google" كمصدر في تطبيقك لتقديم ردود دقيقة تستند إلى الموقع الجغرافي لطلبات المستخدمين. يطلب الطلب اقتراحات محلية مع موقع جغرافي اختياري للمستخدم، ما يتيح لنموذج Gemini استخدام بيانات "خرائط Google".

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## آلية عمل ميزة "تحديد المصدر من خلال خرائط Google"

تدمج ميزة "استخدام خرائط Google كمصدر" واجهة Gemini API مع نظام Google Geo المتكامل باستخدام Maps API كمصدر لتحديد المصدر. عندما يتضمّن طلب المستخدم سياقًا جغرافيًا، يمكن لنموذج Gemini استدعاء أداة "تحديد المصدر من خلال خرائط Google". بعد ذلك، يمكن للنموذج إنشاء ردود تستند إلى بيانات "خرائط Google" ذات الصلة بالموقع الجغرافي المقدَّم.

تتضمّن العملية عادةً ما يلي:

1. **طلب المستخدم:** يرسل المستخدم طلبًا إلى تطبيقك، وقد يتضمّن سياقًا جغرافيًا (مثل "مقاهي بالقرب مني" أو "متاحف في سان فرانسيسكو").
2. **استدعاء الأداة:** يستدعي نموذج Gemini أداة "استخدام "خرائط Google" كمصدر" بعد التعرّف على الغرض الجغرافي من الطلب. يمكن تزويد هذه الأداة اختياريًا بـ
   الخاص بالمستخدم `latitude` و`longitude`. الأداة هي أداة بحث نصي وتعمل بطريقة مشابهة للبحث على "خرائط Google"، حيث ستستخدم طلبات البحث المحلية ("بالقرب مني") الإحداثيات، بينما من غير المرجّح أن تتأثر طلبات البحث المحدّدة أو غير المحلية بالموقع الجغرافي الصريح.
3. **استرجاع البيانات:** تطلب خدمة "استخدام "خرائط Google" كمصدر" معلومات ذات صلة من "خرائط Google" (مثل الأماكن والمراجعات والصور والعناوين وساعات العمل).
4. **الإنشاء المستند إلى المصدر:** يتم استخدام بيانات "خرائط Google" التي تم استرجاعها لإعلام ردّ نموذج Gemini، ما يضمن الدقة والحصول على معلومات ذات صلة.
5. **الردّ والتعليقات التوضيحية:** يعرض النموذج ردًا نصيًا يتضمّن تعليقات توضيحية مضمّنة ترتبط بمصادر "خرائط Google"، ما يتيح للمطوّرين عرض الاقتباسات.

## أسباب استخدام ميزة "استخدام "خرائط Google" كمصدر" والحالات التي يجب استخدامها فيها

يُعدّ استخدام "خرائط Google" كمصدر مثاليًا للتطبيقات التي تتطلّب معلومات دقيقة وحديثة ومحدّدة حسب الموقع الجغرافي. وهي تحسّن تجربة المستخدم من خلال تقديم محتوى ذي صلة ومخصّص يستند إلى قاعدة بيانات "خرائط Google" الشاملة التي تضم أكثر من 250 مليون مكان في جميع أنحاء العالم.

عليك استخدام ميزة "استخدام "خرائط Google" كمصدر" عندما يحتاج تطبيقك إلى:

- تقديم ردود كاملة ودقيقة على الأسئلة الجغرافية المحدّدة
- إنشاء أدوات تخطيط رحلات ومُرشدين محليين في المحادثات
- اقتراح نقاط اهتمام استنادًا إلى الموقع الجغرافي والإعدادات المفضّلة للمستخدم، مثل المطاعم أو المتاجر.
- إنشاء تجارب تستند إلى الموقع الجغرافي للخدمات الاجتماعية أو خدمات البيع بالتجزئة أو خدمات توصيل الطعام

يتميّز استخدام "خرائط Google" كمصدر في حالات الاستخدام التي تكون فيها القرب والبيانات الواقعية الحالية مهمة، مثل العثور على "أفضل مقهى بالقرب مني" أو الحصول على الاتجاهات.

## حالات الاستخدام

يتيح استخدام "خرائط Google" كمصدر مجموعة متنوعة من حالات الاستخدام التي تستند إلى الموقع الجغرافي.

### التعامل مع الأسئلة الخاصة بمكان معيّن

يمكنك طرح أسئلة مفصّلة حول مكان معيّن للحصول على إجابات استنادًا إلى مراجعات مستخدمي Google وبيانات "خرائط Google" الأخرى.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### تقديم تجربة مخصّصة تستند إلى الموقع الجغرافي

يمكنك الحصول على اقتراحات مخصّصة حسب الإعدادات المفضّلة للمستخدم ومنطقة جغرافية معيّنة.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### المساعدة في تخطيط برنامج الرحلة

يمكنك إنشاء خطط لعدة أيام تتضمّن الاتجاهات والمعلومات حول مواقع جغرافية مختلفة، ما يجعلها مثالية لتطبيقات السفر.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## متطلبات استخدام الخدمة

يصف هذا القسم متطلبات استخدام خدمة "تحديد المصدر من خلال خرائط Google".

### إعلام المستخدم بشأن استخدام مصادر "خرائط Google"

مع كل نتيجة تستند إلى "خرائط Google"، ستتلقّى تعليقات توضيحية للمصدر على فقرات المحتوى في خطوة `model_output` التي تتوافق مع كل ردّ. يتم عرض البيانات الوصفية التالية:

- عنوان URL للمصدر
- الاسم

عند عرض نتائج ميزة "استخدام "خرائط Google" كمصدر"، عليك تحديد مصادر "خرائط Google" المرتبطة بها وإعلام المستخدمين بما يلي:

- يجب أن تظهر مصادر "خرائط Google" مباشرةً بعد المحتوى الذي تم إنشاؤه والذي تستنده إليه المصادر. يُشار أيضًا إلى هذا المحتوى الذي تم إنشاؤه باسم "نتيجة تستند إلى خرائط Google".
- يجب أن تكون مصادر "خرائط Google" قابلة للعرض خلال تفاعل واحد مع المستخدم.

### عرض مصادر "خرائط Google" مع روابط "خرائط Google"

بالنسبة إلى كل تعليق توضيحي للمصدر، يجب إنشاء معاينة للرابط وفقًا للمتطلبات التالية:

- يجب تحديد مصدر كل تعليق توضيحي على أنّه "خرائط Google" وفقًا لإرشادات تحديد المصدر النصي في "خرائط Google"
  .
- يجب عرض اسم المصدر المقدَّم في الردّ.
- يجب الربط بالمصدر باستخدام الـ `url` من التعليق التوضيحي.

### إرشادات تحديد المصدر النصي في "خرائط Google"

عند تحديد مصادر "خرائط Google" في النص، اتّبِع الإرشادات التالية:

- لا تعدِّل النص "خرائط Google" بأي شكل من الأشكال:
  - لا تغيِّر حالة الأحرف في "خرائط Google".
  - لا تنقل النص "خرائط Google" إلى أسطر متعددة.
  - لا تترجِم النص "خرائط Google" إلى لغة أخرى.
  - امنع المتصفّحات من ترجمة النص "خرائط Google" باستخدام سمة HTML‏ translate="no".

لمزيد من المعلومات عن بعض مزوّدي بيانات "خرائط Google" وبنود الترخيص الخاصة بهم
، اطّلِع على [الإشعارات القانونية في "خرائط Google" وGoogle Earth](https://www.google.com/help/legalnotices_maps/?hl=ar).

## أفضل الممارسات

- **تحديد موقع المستخدم:** للحصول على الردود الأكثر صلة وتخصيصًا،
  عليك دائمًا تضمين `latitude` و`longitude` في إعدادات أداة `google_maps` عندما يكون موقع المستخدم معروفًا.
- **إعلام المستخدمين النهائيين:** عليك إعلام المستخدمين النهائيين بوضوح بأنّه يتم استخدام بيانات "خرائط Google" للإجابة عن طلباتهم، خاصةً عند تفعيل الأداة.
- **إيقاف الأداة عند عدم الحاجة إليها:** تكون ميزة استخدام "خرائط Google" كمصدر غير مفعّلة تلقائيًا. عليك تفعيلها فقط (`"tools": [{"type": "google_maps"}]`) عندما يتضمّن الطلب سياقًا جغرافيًا واضحًا، وذلك لتحسين الأداء والتكلفة.

## القيود

- لا تتيح ميزة استخدام "خرائط Google" كمصدر حاليًا استخدام الطلبات والردود إلا باللغة الإنجليزية.
- قد لا تكون الأداة متاحة في جميع المناطق.
- قد تختلف النتائج استنادًا إلى دقة الموقع الجغرافي وبيانات "خرائط Google" المتاحة.
- **النطاق الجغرافي:** تتوفّر ميزة استخدام "خرائط Google" كمصدر على مستوى العالم.
- **الحالة التلقائية:** تكون أداة "استخدام "خرائط Google" كمصدر" غير مفعّلة تلقائيًا.
  عليك تفعيلها صراحةً في طلبات واجهة برمجة التطبيقات.

## التسعير والحدود القصوى للطلبات

يختلف تسعير ميزة "استخدام "خرائط Google" كمصدر" حسب إنشاء النموذج:

- **نماذج Gemini 3:** يتم تحصيل رسوم من مشروعك مقابل كل **طلب بحث** يقرّر النموذج تنفيذه. قد يؤدي **طلب بحث** واحد (طلب بيانات من واجهة برمجة التطبيقات الذي ترسله إلى النموذج) إلى تنفيذ النموذج لطلبات بحث متعددة للعثور على المعلومات اللازمة. ويُحتسب كل طلب من هذه الطلبات كاستخدام خاضع للفوترة للأداة.
- **نماذج Gemini 2.5 والإصدارات الأقدم:** يتم تحصيل رسوم من مشروعك مقابل كل **طلب بحث**.
  لا يتم تحصيل رسوم من الطلب إلا إذا عرض الطلب بنجاح نتيجة واحدة على الأقل تستند إلى "خرائط Google"، بغض النظر عن عدد طلبات البحث الفردية التي نفّذها النموذج داخليًا للحصول على هذه النتيجة.

للحصول على معلومات مفصّلة عن الأسعار، اطّلِع على [صفحة تسعير Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

## النماذج المتوافقة

تتيح النماذج التالية ميزة "استخدام "خرائط Google" كمصدر":

| الطراز | استخدام "خرائط Google" كمصدر |
| --- | --- |
| [‫Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ar) | ✔️ |
| [‫Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ar) | ✔️ |
| [‫Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) | ✔️ |
| [‫Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [‫Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ✔️ |
| [‫Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |
| [‫Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ |
| [‫Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ✔️ |
| [‫Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ |

## مجموعات الأدوات المتوافقة

تتيح نماذج Gemini 3 الجمع بين الأدوات المضمّنة (مثل "تحديد المصدر من خلال خرائط Google") والأدوات المخصّصة (استدعاء الدوال). يمكنك الاطّلاع على مزيد من المعلومات في صفحة
[مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).

## الخطوات التالية

- تعرَّف على الأدوات الأخرى [المتاحة](https://ai.google.dev/gemini-api/docs/tools?hl=ar).
- لمزيد من المعلومات عن أفضل ممارسات الذكاء الاصطناعي المسؤول وفلاتر الأمان في Gemini API
  ، اطّلِع على [دليل إعدادات الأمان](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
