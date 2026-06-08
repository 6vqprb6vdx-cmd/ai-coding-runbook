---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=ar
fetched_at: 2026-06-08T15:05:54.013738+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# سياق عنوان URL

تتيح لك أداة "سياق عنوان URL" تقديم سياق إضافي للنماذج في شكل عناوين URL. من خلال تضمين عناوين URL في طلبك، سيتمكّن النموذج من الوصول إلى المحتوى من تلك الصفحات (ما دام نوع عنوان URL غير مدرَج في [قسم القيود](#limitations)) للاستناد إليه وتحسين رده.

تفيد أداة سياق عنوان URL في مهام مثل ما يلي:

- **استخراج البيانات**: استخراج معلومات معيّنة، مثل الأسعار أو الأسماء أو النتائج الرئيسية، من عناوين URL متعددة
- **مقارنة المستندات**: يمكنك تحليل تقارير أو مقالات أو ملفات PDF متعددة لتحديد الاختلافات وتتبُّع المؤشرات.
- **تجميع المحتوى وإنشاؤه**: يمكنك الجمع بين المعلومات من عدة عناوين URL مصدر لإنشاء ملخّصات أو منشورات مدوّنات أو تقارير دقيقة.
- **تحليل الرموز البرمجية والمستندات**: يمكنك الإشارة إلى مستودع GitHub أو مستندات فنية لشرح الرموز البرمجية أو إنشاء تعليمات الإعداد أو الإجابة عن الأسئلة.

يوضّح المثال التالي كيفية مقارنة وصفتَي طعام من موقعَين إلكترونيَين مختلفَين.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3.5-flash"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## آلية العمل

تستخدم أداة "سياق عنوان URL" عملية استرجاع من خطوتَين لتحقيق التوازن بين السرعة والتكلفة والوصول إلى البيانات الحديثة. عند تقديم عنوان URL، تحاول الأداة أولاً جلب المحتوى من ذاكرة تخزين مؤقت للفهرس الداخلي. ويعمل ذلك كذاكرة تخزين مؤقت محسّنة للغاية. إذا لم يكن عنوان URL متاحًا في الفهرس (على سبيل المثال، إذا كانت الصفحة جديدة جدًا)، ستعود الأداة تلقائيًا إلى إجراء عملية جلب مباشرة.
يصل هذا التطبيق مباشرةً إلى عنوان URL لاسترداد محتواه في الوقت الفعلي.

## الدمج مع أدوات أخرى

يمكنك الجمع بين أداة سياق عنوان URL وأدوات أخرى لإنشاء سير عمل أكثر فعالية.

تتيح [نماذج Gemini 3](#supported-models) إمكانية الجمع بين الأدوات المضمّنة (مثل "سياق عنوان URL") والأدوات المخصّصة (استدعاء الدوال). يمكنك الاطّلاع على مزيد من المعلومات في صفحة [مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).

### تحديد المصدر باستخدام "بحث Google"

عند تفعيل كلّ من ميزة &quot;السياق من عنوان URL&quot; و[تحديد المصدر من خلال "بحث Search"](https://ai.google.dev/gemini-api/docs/grounding?hl=ar)، يمكن للنموذج استخدام إمكانات البحث للعثور على معلومات ذات صلة على الإنترنت، ثم استخدام أداة &quot;السياق من عنوان URL&quot; لفهم الصفحات التي يعثر عليها بشكل أكثر تفصيلاً. هذا الأسلوب فعّال مع الطلبات التي تتطلّب بحثًا واسع النطاق وتحليلاً معمّقًا لصفحات معيّنة.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3.5-flash"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## فهم الردّ

عندما يستخدم النموذج أداة سياق عنوان URL، يتضمّن الردّ عنصر `url_context_metadata`. يسرد هذا العنصر عناوين URL التي استردّ منها النموذج المحتوى وحالة كل محاولة استرداد، ما يفيد في التحقّق من صحة النتائج وتصحيح الأخطاء.

في ما يلي مثال على هذا الجزء من الرد
(تم حذف أجزاء من الرد للاختصار):

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

للحصول على تفاصيل كاملة عن هذا العنصر، يُرجى الاطّلاع على
[مرجع واجهة برمجة التطبيقات `UrlContextMetadata`](https://ai.google.dev/api/generate-content?hl=ar#UrlContextMetadata).

### عمليات التحقّق من الأمان

يُجري النظام عملية تدقيق في المحتوى على عنوان URL للتأكّد من استيفائه معايير الأمان. إذا لم يجتَز عنوان URL الذي قدّمته عملية التحقّق هذه، سيظهر لك `url_retrieval_status` من `URL_RETRIEVAL_STATUS_UNSAFE`.

### عدد الرموز المميّزة

يتم احتساب المحتوى الذي يتم استرجاعه من عناوين URL التي تحدّدها في طلبك كجزء من الرموز المميزة للإدخال. يمكنك الاطّلاع على عدد الرموز المميزة لطلبك واستخدام الأدوات في عنصر [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=ar#UsageMetadata) من مخرجات النموذج. في ما يلي مثال على الناتج:

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

يعتمد السعر لكل رمز مميز على النموذج المستخدَم، راجِع صفحة
[الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar) للحصول على التفاصيل.

## النماذج المتوافقة

| الطراز | سياق عنوان URL |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) | ✔️ |
| [إصدار تجريبي من Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [‫Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ✔️ |
| [معاينة Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ |

## أفضل الممارسات

- **تقديم عناوين URL محدّدة**: للحصول على أفضل النتائج، قدِّم عناوين URL مباشرة إلى المحتوى الذي تريد أن يحلّله النموذج. لن يستردّ النموذج المحتوى إلا من عناوين URL التي تقدّمها، وليس من أي محتوى من الروابط المتداخلة.
- **التحقّق من إمكانية الوصول**: تأكَّد من أنّ عناوين URL التي تقدّمها لا تؤدي إلى صفحات تتطلّب تسجيل الدخول أو تقع خلف حاجز دفع.
- **استخدام عنوان URL الكامل**: يجب تقديم عنوان URL الكامل، بما في ذلك البروتوكول (مثلاً، https://www.google.com بدلاً من google.com فقط).

## القيود

- لا تتوفّر حاليًا ميزة "استدعاء الدوال": استخدام الأدوات (سياق عنوان URL، وتحديد المصدر باستخدام "بحث Google"، وما إلى ذلك) مع ميزة "استدعاء الدوال".
- حدّ الطلبات: يمكن للأداة معالجة ما يصل إلى 20 عنوان URL لكل طلب.
- حجم محتوى عنوان URL: الحد الأقصى لحجم المحتوى الذي يتم استرجاعه من عنوان URL واحد هو 34 ميغابايت.
- إمكانية الوصول إلى الجميع: يجب أن تكون عناوين URL متاحة للجميع على الويب.
  لا تتوافق عناوين المضيف المحلي (مثل localhost و127.0.0.1) والشبكات الخاصة وخدمات الأنفاق (مثل ngrok وpinggy).
- ‫Gemini API فقط: لا تتوفّر ميزة "سياق عنوان URL" إلا في Gemini API، وليس من خلال منصة وكيل Gemini Enterprise.

### أنواع المحتوى المتوفّرة وغير المتوفّرة

يمكن للأداة استخراج المحتوى من عناوين URL التي تتضمّن أنواع المحتوى التالية:

- نص (text/html أو application/json أو text/plain أو text/xml أو text/css أو
  text/javascript أو text/csv أو text/rtf)
- صورة (image/png أو image/jpeg أو image/bmp أو image/webp)
- ‫PDF (application/pdf)

**لا تتوافق أنواع المحتوى التالية:**

- المحتوى المحمي بنظام حظر الاشتراك غير المدفوع
- فيديوهات YouTube (راجِع مقالة [فهم الفيديو](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar#youtube) للتعرّف على كيفية معالجة عناوين URL الخاصة بفيديوهات YouTube)
- ملفات Google Workspace، مثل مستندات Google أو جداول البيانات
- ملفات الفيديو والصوت

## الخطوات التالية

- يمكنك الاطّلاع على [كتاب وصفات سياق عنوان URL](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=ar#url-context)
  للحصول على المزيد من الأمثلة.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-01 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-01 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
