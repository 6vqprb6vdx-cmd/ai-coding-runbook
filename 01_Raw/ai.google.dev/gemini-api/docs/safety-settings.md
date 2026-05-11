---
source_url: https://ai.google.dev/gemini-api/docs/safety-settings?hl=ar
fetched_at: 2026-05-11T12:38:46.147144+00:00
title: "\u0625\u0639\u062f\u0627\u062f\u0627\u062a \u0627\u0644\u0623\u0645\u0646 \u0627\u0644\u0634\u062e\u0635\u064a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إعدادات الأمن الشخصي

توفّر Gemini API إعدادات أمان يمكنك تعديلها خلال مرحلة إنشاء النماذج الأولية لتحديد ما إذا كان تطبيقك يتطلّب إعدادات أمان أكثر أو أقل تقييدًا. يمكنك تعديل هذه الإعدادات في أربع فئات من الفلاتر لحظر أنواع معيّنة من المحتوى أو السماح بها.

يتناول هذا الدليل طريقة تعامل Gemini API مع إعدادات السلامة وعمليات الفلترة، وكيفية تغيير إعدادات السلامة في تطبيقك.

## فلاتر السلامة

تغطي فلاتر الأمان القابلة للضبط في Gemini API الفئات التالية:

| الفئة | الوصف |
| --- | --- |
| التحرش | التعليقات السلبية أو المؤذية التي تستهدف الهوية و/أو السمات المحمية |
| الكلام الذي يحضّ على الكراهية | المحتوى الفظ أو غير المحترم أو البذيء |
| محتوى جنسي فاضح | تتضمن السمة إشارات إلى أفعال جنسية أو محتوًى بذيئًا آخر. |
| الفئات الخطيرة | الترويج لأفعال ضارّة أو تسهيل تنفيذها أو التشجيع عليها |

يتم تحديد هذه الفئات في [`HarmCategory`](https://ai.google.dev/api/rest/v1/HarmCategory?hl=ar). يمكنك استخدام هذه الفلاتر لتعديل ما هو مناسب لحالة الاستخدام. على سبيل المثال، إذا كنت تعمل على إنشاء حوارات في ألعاب الفيديو، قد ترى أنّه من المقبول السماح بالمزيد من المحتوى الذي تم تقييمه على أنّه *خطير* بسبب طبيعة اللعبة.

بالإضافة إلى فلاتر الأمان القابلة للتعديل، تتضمّن واجهة برمجة التطبيقات Gemini API إجراءات حماية مدمجة ضد الأضرار الأساسية، مثل المحتوى الذي يعرّض سلامة الأطفال للخطر.
يتم حظر هذه الأنواع من المحتوى الضار دائمًا ولا يمكن تعديلها.

### مستوى فلترة أمان المحتوى

تصنّف Gemini API مستوى احتمال أن يكون المحتوى غير آمن على النحو التالي:
`HIGH` أو `MEDIUM` أو `LOW` أو `NEGLIGIBLE`.

تحظر Gemini API المحتوى استنادًا إلى احتمال أن يكون المحتوى غير آمن، وليس إلى مدى خطورته. من المهم أخذ ذلك في الاعتبار لأنّ بعض المحتوى قد يكون احتمال أن يكون غير آمن منخفضًا، حتى لو كان مستوى الضرر المحتمل مرتفعًا. على سبيل المثال، عند مقارنة الجملتين:

1. لقد لكمني الروبوت.
2. وقد جرحني الروبوت.

قد تؤدي الجملة الأولى إلى زيادة احتمال أن تكون غير آمنة، ولكن قد تعتبر الجملة الثانية أكثر خطورة من حيث العنف.
وبناءً على ذلك، من المهم أن تختبر بعناية وتحدّد مستوى الحظر المناسب الذي تحتاجه لدعم حالات الاستخدام الرئيسية مع تقليل الضرر الذي قد يلحق بالمستخدمين النهائيين.

### فلترة السلامة لكل طلب

يمكنك تعديل إعدادات الأمان لكل طلب ترسله إلى واجهة برمجة التطبيقات. عندما تقدّم طلبًا، يتم تحليل المحتوى وتعيين تقييم أمان له. يتضمّن تقييم الأمان الفئة واحتمالية التصنيف على أنّه محتوى ضار. على سبيل المثال، إذا تم حظر المحتوى بسبب ارتفاع احتمال تصنيفه ضمن فئة المضايقة، سيكون التقييم الخاص بالأمان الذي تم إرجاعه يتضمّن فئة تساوي `HARASSMENT` واحتمال حدوث ضرر تم ضبطه على `HIGH`.

بسبب الأمان المتأصّل في النموذج، تكون الفلاتر الإضافية **غير مفعَّلة** تلقائيًا.
في حال اختيار تفعيلها، يمكنك ضبط النظام لحظر المحتوى استنادًا إلى احتمال أن يكون غير آمن. يغطي السلوك التلقائي للنموذج معظم حالات الاستخدام، لذا يجب عدم تعديل هذه الإعدادات إلا إذا كان التطبيق يتطلب اتساقًا.

يوضّح الجدول التالي إعدادات الحظر التي يمكنك تعديلها لكل فئة. على سبيل المثال، إذا ضبطت إعداد الحظر على **حظر عدد قليل** لفئة **كلام يحض على الكراهية**، سيتم حظر كل المحتوى الذي يُرجّح أن يكون كلامًا يحض على الكراهية. ولكن يُسمح بأي قيمة ذات احتمال أقل.

| الحدّ (Google AI Studio) | الحدّ (واجهة برمجة التطبيقات) | الوصف |
| --- | --- | --- |
| إيقاف | `OFF` | إيقاف فلتر الأمان |
| عدم الحظر | `BLOCK_NONE` | العرض دائمًا بغض النظر عن احتمال ظهور محتوى غير آمن |
| حظر عدد قليل | `BLOCK_ONLY_HIGH` | الحظر عند وجود احتمال كبير بأن يكون المحتوى غير آمن |
| حظر بعض الأرقام | `BLOCK_MEDIUM_AND_ABOVE` | الحظر عند وجود احتمال متوسط أو كبير بأن يكون المحتوى غير آمن |
| حظر معظم الإشعارات | `BLOCK_LOW_AND_ABOVE` | الحظر عند وجود احتمال منخفض أو متوسط أو مرتفع بأن يكون المحتوى غير آمن |
| لا ينطبق | `HARM_BLOCK_THRESHOLD_UNSPECIFIED` | لم يتم تحديد الحدّ، ويتم الحظر باستخدام الحدّ التلقائي |

إذا لم يتم ضبط الحدّ، يكون الحدّ التلقائي للحظر هو **إيقاف** لطُرز Gemini 2.5 و3.

يمكنك ضبط هذه الإعدادات لكل طلب ترسله إلى الخدمة التوليدية.
يمكنك الاطّلاع على مرجع واجهة برمجة التطبيقات [`HarmBlockThreshold`](https://ai.google.dev/api/generate-content?hl=ar#harmblockthreshold) لمعرفة التفاصيل.

### ملاحظات حول الأمان

تعرض الدالة [`generateContent`](https://ai.google.dev/api/generate-content?hl=ar#method:-models.generatecontent)
[`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=ar#generatecontentresponse) التي
تتضمّن ملاحظات حول السلامة.

يتم تضمين الملاحظات حول الطلب في
[`promptFeedback`](https://ai.google.dev/api/generate-content?hl=ar#promptfeedback). إذا تم ضبط
`promptFeedback.blockReason`، يعني ذلك أنّه تم حظر محتوى الطلب.

يتم تضمين الملاحظات حول المرشحين للردود في
[`Candidate.finishReason`](https://ai.google.dev/api/generate-content?hl=ar#candidate) و
[`Candidate.safetyRatings`](https://ai.google.dev/api/generate-content?hl=ar#candidate). إذا تم حظر محتوى الردّ وكان `finishReason` هو `SAFETY`، يمكنك فحص `safetyRatings` للحصول على مزيد من التفاصيل. لا يتم إرجاع المحتوى الذي تم حظره.

## تعديل إعدادات الأمان

يوضّح هذا القسم كيفية تعديل إعدادات الأمان في كلّ من Google AI Studio وفي الرمز البرمجي.

### Google AI Studio

يمكنك تعديل إعدادات الأمان في Google AI Studio.

انقر على **إعدادات الأمان** ضمن **الإعدادات المتقدّمة** في لوحة **إعدادات التنفيذ** لفتح النافذة المنبثقة **إعدادات الأمان**. في النافذة المنبثقة، يمكنك استخدام أشرطة التمرير لضبط مستوى فلترة المحتوى لكل فئة من فئات الأمان:

![](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_ui.png?hl=ar)

عند إرسال طلب (على سبيل المثال، طرح سؤال على النموذج)، ستظهر الرسالة warning
**تم حظر المحتوى** إذا كان محتوى الطلب محظورًا. للاطّلاع على مزيد من التفاصيل، مرِّر المؤشر فوق النص **تم حظر المحتوى** للاطّلاع على الفئة واحتمالية تصنيف المحتوى على أنّه ضار.

### أمثلة على الرموز

يوضّح مقتطف الرمز التالي كيفية ضبط إعدادات الأمان في `GenerateContent` مكالمتك. يؤدي ذلك إلى ضبط الحدّ الأدنى لفئة المحتوى الذي يحض على الكراهية (`HARM_CATEGORY_HATE_SPEECH`). يؤدي ضبط هذه الفئة على `BLOCK_LOW_AND_ABOVE` إلى حظر أي محتوى يتضمّن احتمالاً منخفضًا أو مرتفعًا بأن يكون كلامًا يحض على الكراهية. لفهم إعدادات الحدّ، راجِع [فلترة المحتوى غير الآمن
لكل طلب](#safety-filtering-per-request).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Some potentially unsafe prompt",
    config=types.GenerateContentConfig(
      safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
      ]
    )
)

print(response.text)
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        SafetySettings: []*genai.SafetySetting{
            {
                Category:  "HARM_CATEGORY_HATE_SPEECH",
                Threshold: "BLOCK_LOW_AND_ABOVE",
            },
        },
    }

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Some potentially unsafe prompt."),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const safetySettings = [
  {
    category: "HARM_CATEGORY_HATE_SPEECH",
    threshold: "BLOCK_LOW_AND_ABOVE",
  },
];

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Some potentially unsafe prompt.",
    config: {
      safetySettings: safetySettings,
    },
  });
  console.log(response.text);
}

await main();
```

### جافا

```
SafetySetting hateSpeechSafety = new SafetySetting(HarmCategory.HATE_SPEECH,
    BlockThreshold.LOW_AND_ABOVE);

GenerativeModel gm = new GenerativeModel(
    "gemini-3-flash-preview",
    BuildConfig.apiKey,
    null, // generation config is optional
    Arrays.asList(hateSpeechSafety)
);

GenerativeModelFutures model = GenerativeModelFutures.from(gm);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "safetySettings": [
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_LOW_AND_ABOVE"}
    ],
    "contents": [{
        "parts":[{
            "text": "'\''Some potentially unsafe prompt.'\''"
        }]
    }]
}'
```

## الخطوات التالية

- اطّلِع على [مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api?hl=ar) لمعرفة المزيد عن واجهة برمجة التطبيقات الكاملة.
- راجِع [إرشادات الأمان](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ar) للحصول على نظرة عامة حول اعتبارات الأمان عند التطوير باستخدام نماذج اللغات الكبيرة.
- مزيد من المعلومات حول تقييم الاحتمالية مقابل الخطورة من [فريق Jigsaw](https://developers.perspectiveapi.com/s/about-the-api-score)
- مزيد من المعلومات حول المنتجات التي تساهم في توفير حلول الأمان، مثل
  [Perspective
  API](https://medium.com/jigsaw/reducing-toxicity-in-large-language-models-with-perspective-api-c31c39b7a4d7)
  \* يمكنك استخدام إعدادات الأمان هذه لإنشاء مصنّف
  للمحتوى السام. يمكنك الاطّلاع على [مثال التصنيف](https://ai.google.dev/examples/train_text_classifier_embeddings?hl=ar) للبدء.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
