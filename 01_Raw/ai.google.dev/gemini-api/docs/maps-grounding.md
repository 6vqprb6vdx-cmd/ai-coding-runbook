---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar
fetched_at: 2026-07-06T05:13:48.090449+00:00
title: "\u0627\u0644\u0627\u0633\u062a\u0646\u0627\u062f \u0625\u0644\u0649 \"\u062e\u0631\u0627\u0626\u0637 Google\" \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الاستناد إلى "خرائط Google"

يتيح استخدام "خرائط Google" كمصدر ربط إمكانات Gemini التوليدية بالبيانات الغنية والحقيقية والحديثة المتوفرة في "خرائط Google". تتيح هذه الميزة للمطوّرين دمج وظائف تستند إلى الموقع الجغرافي في تطبيقاتهم بسهولة. عندما يتضمّن طلب بحث المستخدم سياقًا مرتبطًا ببيانات &quot;خرائط Google&quot;، يستفيد نموذج Gemini من &quot;خرائط Google&quot; لتقديم إجابات دقيقة وحديثة وذات صلة بالموقع الجغرافي المحدّد أو المنطقة العامة التي ذكرها المستخدم.

- **ردود دقيقة ومراعية للموقع الجغرافي:** يمكنك الاستفادة من بيانات &quot;خرائط Google&quot; الشاملة والحديثة للاستعلامات الخاصة بمواقع جغرافية معيّنة.
- **التخصيص المحسّن:** تخصيص الاقتراحات والمعلومات استنادًا إلى المواقع الجغرافية التي يقدّمها المستخدم

## البدء

يوضّح هذا المثال كيفية دمج ميزة استخدام "خرائط Google" كمصدر في تطبيقك لتقديم ردود دقيقة ومراعية للموقع الجغرافي على طلبات المستخدمين. يطلب الطلب الحصول على اقتراحات محلية مع تحديد موقع جغرافي اختياري للمستخدم، ما يتيح لنموذج Gemini استخدام بيانات &quot;خرائط Google&quot;.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
    "model": "gemini-3.5-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## طريقة عمل ميزة "استخدام خرائط Google كمصدر"

تدمج ميزة استخدام "خرائط Google" كمصدر واجهة Gemini API مع نظام Google Geo البيئي من خلال استخدام Maps API كمصدر للبيانات الأساسية. عندما يتضمّن طلب المستخدم سياقًا جغرافيًا، يمكن لنموذج Gemini استخدام أداة &quot;الاستناد إلى بيانات واقعية&quot; في &quot;خرائط Google&quot;. يمكن للنموذج بعد ذلك إنشاء ردود استنادًا إلى بيانات &quot;خرائط Google&quot; ذات الصلة بالموقع الجغرافي المقدَّم.

تتضمّن العملية عادةً ما يلي:

1. **طلب بحث المستخدم:** يرسل المستخدم طلب بحث إلى تطبيقك، وقد يتضمّن سياقًا جغرافيًا (مثل "مقاهي بالقرب مني" أو "متاحف في سان فرانسيسكو").
2. **استدعاء الأداة:** يستدعي نموذج Gemini أداة Grounding with Google Maps بعد التعرّف على النية الجغرافية. يمكنك اختياريًا تزويد هذه الأداة `latitude` و`longitude` الخاصين بالمستخدم. الأداة هي أداة بحث نصي وتعمل بشكل مشابه للبحث على &quot;خرائط Google&quot;، إذ إنّ طلبات البحث المحلية (&quot;بالقرب مني&quot;) ستستخدم الإحداثيات، بينما من غير المرجّح أن تتأثر طلبات البحث المحدّدة أو غير المحلية بالموقع الجغرافي الواضح.
3. **استرداد البيانات:** تستعلم خدمة استخدام "خرائط Google" كمصدر من "خرائط Google" عن المعلومات ذات الصلة (مثل الأماكن والمراجعات والصور والعناوين وساعات العمل).
4. **الإنشاء المستند إلى مصادر:** يتم استخدام بيانات &quot;خرائط Google&quot; التي تم استرجاعها لإبلاغ ردّ نموذج Gemini، ما يضمن دقة المعلومات ومدى صلتها بالموضوع.
5. **الردود والتعليقات التوضيحية:** يعرض النموذج ردًا نصيًا مع تعليقات توضيحية مضمّنة تتضمّن روابط تؤدي إلى مصادر &quot;خرائط Google&quot;، ما يتيح للمطوّرين عرض الاقتباسات.

## أسباب استخدام ميزة "استخدام "خرائط Google" كمصدر" وحالات استخدامها

يُعدّ استخدام &quot;خرائط Google&quot; كمصدر مثاليًا للتطبيقات التي تتطلّب معلومات دقيقة وحديثة وخاصة بالموقع الجغرافي. تعمل هذه الميزة على تحسين تجربة المستخدم من خلال توفير محتوى ملائم ومخصّص استنادًا إلى قاعدة بيانات &quot;خرائط Google&quot; الشاملة التي تضم أكثر من 250 مليون مكان حول العالم.

عليك استخدام Grounding with Google Maps عندما يحتاج تطبيقك إلى:

- تقديم إجابات كاملة ودقيقة عن الأسئلة الخاصة بمنطقة جغرافية معيّنة
- إنشاء أدوات تخطيط رحلات ومراجع محلية مستندة إلى المحادثات
- اقتراح نقاط اهتمام استنادًا إلى الموقع الجغرافي وإعدادات المستخدم المفضّلة، مثل المطاعم أو المتاجر
- إنشاء تجارب تستند إلى الموقع الجغرافي للخدمات الاجتماعية أو خدمات البيع بالتجزئة أو توصيل الطعام

يتفوّق استخدام "خرائط Google" كمصدر في حالات الاستخدام التي تكون فيها القرب والبيانات الواقعية الحالية مهمة، مثل العثور على "أفضل مقهى بالقرب مني" أو الحصول على اتجاهات.

## حالات الاستخدام

يتيح استخدام "خرائط Google" كمصدر مجموعة متنوعة من حالات الاستخدام التي تعتمد على الموقع الجغرافي.

### التعامل مع الأسئلة المتعلّقة بمكان معيّن

طرح أسئلة مفصّلة حول مكان معيّن للحصول على إجابات استنادًا إلى مراجعات مستخدمي Google وبيانات &quot;خرائط Google&quot; الأخرى

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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

### توفير ميزة التخصيص المستندة إلى الموقع الجغرافي

الحصول على اقتراحات مخصّصة حسب الإعدادات المفضّلة للمستخدِم ومنطقة جغرافية معيّنة

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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

### المساعدة في التخطيط لبرنامج الرحلة

إنشاء خطط لعدة أيام تتضمّن الاتجاهات ومعلومات حول مواقع جغرافية مختلفة، ما يجعلها مثالية لتطبيقات السفر

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
    "model": "gemini-3.5-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## متطلبات استخدام الخدمة

يوضّح هذا القسم متطلبات استخدام خدمة &quot;التأسيس باستخدام خرائط Google&quot;.

### إبلاغ المستخدم بشأن استخدام مصادر "خرائط Google"

مع كل نتيجة تستند إلى بيانات موثوقة في &quot;خرائط Google&quot;، ستتلقّى تعليقات توضيحية للمصدر على مربّعات المحتوى في الخطوة `model_output` التي تدعم كل ردّ. يتم عرض بيانات التعريف التالية:

- عنوان URL المصدر
- الاسم

عند عرض نتائج من استخدام "خرائط Google" كمصدر، يجب تحديد مصادر "خرائط Google" المرتبطة وإبلاغ المستخدمين بما يلي:

- يجب أن تتبع مصادر &quot;خرائط Google&quot; المحتوى الذي تم إنشاؤه مباشرةً والذي تستند إليه هذه المصادر. يُشار إلى هذا المحتوى الذي يتم إنشاؤه أيضًا باسم "نتيجة مستندة إلى بيانات واقعية" في "خرائط Google".
- يجب أن تكون مصادر "خرائط Google" قابلة للعرض من خلال تفاعل واحد من المستخدم.

### عرض مصادر "خرائط Google" باستخدام روابط "خرائط Google"

بالنسبة إلى كل تعليق توضيحي للمصدر، يجب إنشاء معاينة للرابط وفقًا للمتطلبات التالية:

- يجب الإشارة إلى كل مصدر في &quot;خرائط Google&quot; وفقًا [لإرشادات الإشارة إلى المصدر](#maps-attribution-guidelines) الخاصة بنص &quot;خرائط Google&quot;.
- عرض اسم المصدر المقدَّم في الردّ
- انقر على `url` من التعليق التوضيحي للانتقال إلى المصدر.

### إرشادات تحديد المصدر باستخدام النصوص في "خرائط Google"

عند الإشارة إلى مصادر &quot;خرائط Google&quot; في النص، اتّبِع الإرشادات التالية:

- يجب عدم تعديل النص في "خرائط Google" بأي شكل من الأشكال:
  - لا تغيِّر طريقة كتابة الأحرف الكبيرة والصغيرة في "خرائط Google".
  - لا تلتفّ "خرائط Google" على أسطر متعددة.
  - لا تقم بتوطين "خرائط Google" إلى لغة أخرى.
  - منع المتصفّحات من ترجمة &quot;خرائط Google&quot; باستخدام السمة translate=&quot;no&quot; في HTML

لمزيد من المعلومات حول بعض مزوّدي بيانات "خرائط Google" وبنود الترخيص الخاصة بهم، يُرجى الاطّلاع على [الإشعارات القانونية في "خرائط Google" وGoogle Earth](https://www.google.com/help/legalnotices_maps/?hl=ar).

## أفضل الممارسات

- **توفير الموقع الجغرافي للمستخدم:** للحصول على الردود الأكثر صلة وتخصيصًا، احرص دائمًا على تضمين `latitude` و`longitude` في إعدادات أداة `google_maps` عندما يكون الموقع الجغرافي للمستخدم معروفًا.
- **إعلام المستخدمين النهائيين:** يجب إعلام المستخدمين النهائيين بوضوح بأنّه يتم استخدام بيانات &quot;خرائط Google&quot; للرد على طلباتهم، خاصةً عند تفعيل الأداة.
- **إيقاف الميزة عند عدم الحاجة إليها:** تكون ميزة "التحديد الأرضي" في "خرائط Google" غير مفعّلة تلقائيًا. لا تفعِّلها (`"tools": [{"type": "google_maps"}]`) إلا عندما يكون لطلب البحث سياق جغرافي واضح، وذلك لتحسين الأداء والتكلفة.

## القيود

- لا يتوافق استخدام "خرائط Google" كمصدر حاليًا إلا مع الطلبات والردود باللغة الإنجليزية.
- قد لا تكون الأداة متاحة في بعض المناطق.
- قد تختلف النتائج حسب دقة الموقع الجغرافي وبيانات "خرائط Google" المتاحة.
- **النطاق الجغرافي:** يتوفّر استخدام "خرائط Google" كمصدر على مستوى العالم.
- **الحالة التلقائية:** تكون أداة "استخدام خرائط Google كمصدر" غير مفعّلة تلقائيًا.
  يجب تفعيلها صراحةً في طلبات واجهة برمجة التطبيقات.

## الأسعار وحدود الاستخدام

يختلف سعر استخدام "خرائط Google" كمصدر حسب جيل النموذج:

- **نماذج Gemini 3:** يتم تحصيل رسوم من مشروعك مقابل كل **طلب بحث** يقرّر النموذج تنفيذه. قد يؤدي **طلب بحث** واحد (طلبك من واجهة برمجة التطبيقات إلى النموذج) إلى تنفيذ النموذج لطلبات بحث متعددة للعثور على المعلومات اللازمة. يُحتسب كل طلب بحث من هذه الطلبات كاستخدام خاضع للفوترة للأداة.
- **‫Gemini 2.5 والنماذج الأقدم:** يتم تحصيل رسوم مشروعك لكل **طلب بحث**.
  لا يتم تحصيل رسوم مقابل الطلب إلا إذا عرضت المطالبة نتيجة واحدة على الأقل من نتائج &quot;خرائط Google&quot; المستندة إلى بيانات واقعية، بغض النظر عن عدد طلبات البحث الفردية التي نفّذها النموذج داخليًا للحصول على تلك النتيجة.

للحصول على معلومات مفصّلة عن الأسعار، يُرجى الاطّلاع على [صفحة أسعار Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

## النماذج المتوافقة

تتيح النماذج التالية استخدام "خرائط Google" كمصدر:

| الطراز | استخدام "خرائط Google" كمصدر |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) | ✔️ |
| [إصدار تجريبي من Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [‫Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ✔️ |
| [معاينة Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ |

## مجموعات الأدوات المتوافقة

تتيح نماذج Gemini 3 الجمع بين الأدوات المضمّنة (مثل "تحديد المصدر من خلال خرائط Google") والأدوات المخصّصة (استدعاء الدوال البرمجية). يمكنك الاطّلاع على مزيد من المعلومات في صفحة [مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).

## الخطوات التالية

- [مزيد من المعلومات عن الأدوات الأخرى المتاحة](https://ai.google.dev/gemini-api/docs/tools?hl=ar)
- لمزيد من المعلومات حول أفضل ممارسات الذكاء الاصطناعي المسؤول وفلاتر الأمان في Gemini API، يُرجى الاطّلاع على [دليل إعدادات الأمان](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-24 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-24 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
