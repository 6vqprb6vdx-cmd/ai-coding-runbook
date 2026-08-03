---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ar
fetched_at: 2026-08-03T04:35:57.153325+00:00
title: "\u0627\u0644\u0633\u062c\u0644\u0651\u0627\u062a \u0648\u0645\u062c\u0645\u0648\u0639\u0627\u062a \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# السجلّات ومجموعات البيانات

في هذا الدليل، ستتعرّفون على كيفية عرض السجلات من استخدام Gemini API في لوحة بيانات Google AI Studio لفهم سلوك النموذج بشكل أفضل وكيفية تفاعل المستخدمين مع تطبيقاتكم. يمكنكم استخدام ميزة تسجيل البيانات لمراقبة ملاحظات الاستخدام وتصحيح الأخطاء فيها، و*مشاركتها اختياريًا مع Google للمساعدة في تحسين Gemini في حالات استخدام المطوّرين*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=ar)

تتوفّر إمكانية تسجيل البيانات لجميع طلبات البيانات من واجهة برمجة التطبيقات `GenerateContent` و`BatchGenerateContent` و`StreamGenerateContent` وطلبات البيانات من [Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=ar) API باستثناء
الوكلاء المُدارون. ويشمل ذلك الطلبات التي يتم إجراؤها من خلال
[نقاط نهاية التوافق مع OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar).

## ضبط تسجيل بيانات المشروع

تخزّن واجهة برمجة التطبيقات تلقائيًا جميع عناصر التفاعل (`store=true`) لتسهيل استخدام ميزات إدارة حالة الخادم. في المقابل، لا تخزّن Generate Content API الطلبات تلقائيًا، وتتطلب تفعيل مساحة التخزين لكل طلب أو على مستوى المشروع من AI Studio.

في Google [AI Studio](https://aistudio.google.com/logs?hl=ar)، يمكنكم تفعيل ميزة تسجيل البيانات أو
إيقافها لجميع المشاريع أو لمشاريع معيّنة، وتغيير هذه
الإعدادات المفضّلة في أي وقت من خلال لوحة **الإعدادات** في
[صفحة "السجلات ومجموعات البيانات"](https://aistudio.google.com/logs?hl=ar). يمكن تفعيل ميزة تسجيل البيانات أو إيقافها
بشكل مستقل لواجهة برمجة التطبيقات `generateContent` وواجهة
[التفاعلات](https://ai.google.dev/gemini-api/docs/interactions?hl=ar) API
لتغيير سلوك التخزين التلقائي لمشروع معيّن.

### تسجيل البيانات على مستوى الطلب

يختلف سلوك التخزين وتسجيل البيانات حسب واجهة برمجة التطبيقات:

- **[واجهة Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar):** تخزّن الطلبات تلقائيًا (`store=true`) لتسهيل إدارة حالة جهة الخادم.
- **واجهة Generate Content API (`generateContent`):** لا تخزّن الطلبات تلقائيًا (`store=false`).

إليكم كيفية ضبط السمة `store`:

**واجهة برمجة التطبيقات GenerateContent API**

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents='Explain quantum entanglement in simple terms.',
    config={'store': False} # Set to True to enable logging of this request
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: 'Explain quantum entanglement in simple terms.',
    config: {
        store: false // Set to true to enable logging of this request
    }
});

console.log(response.text);
```

**واجهة Interactions API**

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain quantum entanglement in simple terms.",
    store=True # Set to False to disable logging of this request
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Explain quantum entanglement in simple terms.',
    store: true // Set to false to disable logging of this request
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

## عرض سجلات المشروع في AI Studio

1. انتقِلوا إلى صفحة "السجلات" في [AI Studio](https://aistudio.google.com/logs?hl=ar).
2. اختَاروا مشروعًا من القائمة المنسدلة.
3. ستظهر السجلات في الجدول بترتيب زمني عكسي لواجهة Interactions API، إذا كانت متوفّرة.
4. لمراقبة سجلات المشروع في Generate Content API، فعِّلوا هذه الميزة أولاً في لوحة [الإعدادات](#configure-logging).

انقروا على إدخال لمعاينة الحمولة. يمكنكم الاطّلاع على الطلب والردّ الكاملَين من Gemini، والسياق من المحادثات السابقة. بالنسبة إلى طلبات **واجهة Interactions API**، تتضمّن السجلات أيضًا رابطًا مباشرًا إلى `previous_interaction_id`.

## ضبط فترة الاحتفاظ بمساحة تخزين المشروع

ستنتهي صلاحية السجلات وسيتم وضع علامة عليها للحذف بعد فترة الاحتفاظ التلقائية البالغة
55 يومًا (ما لم يتم [حفظها في مجموعة بيانات](#create) لا تنتهي صلاحيتها).
يمكنكم ضبط فترة الاحتفاظ بسجلات المشروع على 7 أو 14 أو 28 أو 55 يومًا كحد أقصى.

## إنشاء مجموعات البيانات ومشاركتها

يمكنكم حفظ السجلات في مجموعات البيانات لتنظيمها وتصديرها بشكل أكثر فعالية.

- من صفحة ["السجلات"](https://aistudio.google.com/logs?hl=ar)، ابحثوا عن شريط الفلترة
  في أعلى الصفحة لاختيار سمة للفلترة حسبها.
- من العرض الذي تم فلترته، استخدِموا مربّعات الاختيار لاختيار جميع السجلات أو سجلات فردية.
- انقروا على الزر **إنشاء مجموعة بيانات** الذي يظهر في أعلى القائمة.
- أدخِلوا اسمًا لمجموعة البيانات الجديدة ووصفًا اختياريًا لها.
- ستظهر مجموعة البيانات التي أنشأتموها للتو مع مجموعة السجلات المنسّقة.
- يمكنكم تصدير مجموعة البيانات لإجراء تحليل إضافي بتنسيق ملفات CSV أو JSONL أو إلى "جداول بيانات Google".

يمكن أن تكون مجموعات البيانات مفيدة لعدد من حالات الاستخدام المختلفة.

- **تنسيق مجموعات التحديات:** يمكنكم إجراء تحسينات مستقبلية تستهدف المجالات التي تريدون تحسين أداء الذكاء الاصطناعي فيها.
- **تنسيق مجموعات النماذج:** على سبيل المثال، يمكنكم استخدام نموذج من الاستخدام الفعلي لإنشاء ردود من نموذج آخر، أو مجموعة من الحالات القصوى لإجراء عمليات التحقّق الروتينية قبل النشر.
- **مجموعات التقييم:** هي مجموعات تمثّل الاستخدام الفعلي في جميع الإمكانات المهمة، وذلك للمقارنة بين النماذج الأخرى أو تكرارات تعليمات النظام.

يمكنكم المساهمة في أبحاث Gemini وتطويره من خلال اختيار مشاركة مجموعات البيانات مع Google كأمثلة توضيحية.

## القيود

لا تتوفّر حاليًا ميزة تسجيل البيانات لما يلي:

- نماذج Imagen وVeo
- نماذج تضمين Gemini
- نموذج Gemini Robotics
- المدخلات التي تحتوي على فيديوهات أو ملفات GIF أو ملفات PDF
- الوكلاء في المعاينة العلنية في Gemini API

## الخطوات التالية

- **إنشاء نموذج أولي باستخدام سجلّ الجلسة:** يمكنكم استخدام [أداة Build في AI Studio](https://aistudio.google.com/apps?hl=ar) لإنشاء تطبيقات رموز برمجية وإضافة مفتاح واجهة برمجة التطبيقات لتفعيل سجلّ سجلات Gemini API لميزات الذكاء الاصطناعي.
- **إعادة تشغيل السجلات باستخدام Gemini Batch API:** يمكنكم استخدام مجموعات البيانات لأخذ عيّنات من الردود وتقييم النماذج أو منطق التطبيق من خلال إعادة تشغيل السجلات باستخدام [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-22 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-22 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
