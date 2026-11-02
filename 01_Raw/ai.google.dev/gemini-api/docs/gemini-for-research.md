---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=ar
fetched_at: 2026-11-02T07:27:35.381897+00:00
title: "\u062a\u0633\u0631\u064a\u0639 \u0639\u0645\u0644\u064a\u0629 \u0627\u0644\u0627\u0643\u062a\u0634\u0627\u0641 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Gemini \u0644\u0623\u063a\u0631\u0627\u0636 \u0627\u0644\u0628\u062d\u062b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)

# تسريع عملية الاكتشاف باستخدام Gemini لأغراض البحث

[الحصول على مفتاح واجهة Gemini API](https://aistudio.google.com/apikey?hl=ar)

يمكن استخدام نماذج Gemini لتطوير الأبحاث الأساسية في مختلف المجالات.
إليك بعض الطرق التي يمكنك من خلالها استكشاف Gemini لإجراء بحثك:

- **تحليل نواتج النموذج والتحكّم فيها**: لإجراء المزيد من التحليلات، يمكنك فحص الردود المقترَحة التي أنشأها النموذج باستخدام أدوات مثل `CitationMetadata`. يمكنك أيضًا ضبط خيارات لإنشاء النماذج والمخرجات، مثل `responseSchema` و`topP` و`topK`. [مزيد من المعلومات](https://ai.google.dev/api/generate-content?hl=ar)
- **مدخلات متعدّدة الوسائط**: يمكن لـ Gemini معالجة الصور والمقاطع الصوتية والفيديوهات، ما يتيح مجموعة كبيرة من مجالات البحث المثيرة. [مزيد من المعلومات](https://ai.google.dev/gemini-api/docs/vision?hl=ar)
- **قدرات استيعاب المعلومات الكثيرة**: يتضمّن كل من Gemini 3.0 Flash وPro قدرة استيعاب تصل إلى مليون رمز مميّز. [مزيد من المعلومات](https://ai.google.dev/gemini-api/docs/long-context?hl=ar)
- **Grow with Google**: يمكنك الوصول بسرعة إلى نماذج Gemini من خلال واجهة برمجة التطبيقات وGoogle AI Studio لحالات الاستخدام في الإنتاج. إذا كنت تبحث عن منصة مستندة إلى Google Cloud، يمكن أن توفّر لك Gemini Enterprise Agent Platform بنية أساسية إضافية داعمة.

لدعم الأبحاث الأكاديمية وتعزيز الأبحاث المتطوّرة، تتيح Google للعلماء والباحثين الأكاديميين إمكانية الوصول إلى أرصدة Gemini API من خلال [برنامج Gemini الأكاديمي](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=ar#gemini-academic-program).

## بدء استخدام Gemini

تساعدك واجهة Gemini API وGoogle AI Studio في بدء العمل باستخدام أحدث نماذج Google وتحويل أفكارك إلى تطبيقات قابلة للتوسّع.

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;

Client client = new Client();
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("How large is the universe?"))
    .build();
var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("How large is the universe?"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## الأكاديميون المميزون

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=ar)

"يبحث فريقنا في Gemini كنموذج لغة مرئية (VLM) وسلوكياته التي تحاكي سلوك الإنسان في بيئات متنوعة من منظورَي المتانة والأمان. حتى الآن، قيّمنا مدى فعالية Gemini في التعامل مع عوامل التشتيت، مثل النوافذ المنبثقة، عندما تنفّذ وكالات VLM مهام على الكمبيوتر، واستفدنا من Gemini في تحليل التفاعل الاجتماعي والأحداث المؤقتة وعوامل الخطر استنادًا إلى إدخال الفيديو".

[الموقع الإلكتروني الخاص بـ "ديي يانغ"](https://cs.stanford.edu/~diyiy/)

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=ar)

"لقد ساعدنا Gemini Pro وFlash، بفضل قدرتهما على استيعاب معلومات كثيرة، في مشروعنا OK-Robot، وهو مشروع مفتوح المفردات للتحكّم في الأجهزة الجوّالة. يتيح Gemini تنفيذ طلبات وأوامر معقّدة باللغة الطبيعية استنادًا إلى "ذاكرة" الروبوت، أي الملاحظات السابقة التي سجّلها الروبوت خلال مدة تشغيل طويلة. أنا و"ماهي شافي الله" نستخدم Gemini أيضًا لتقسيم المهام إلى تعليمات برمجية يمكن للروبوت تنفيذها في العالم الحقيقي".

[الموقع الإلكتروني الخاص بـ "ليريل بينتو"](https://www.lerrelpinto.com/)

## برنامج Gemini الأكاديمي

يمكن للباحثين الأكاديميين المؤهّلين (مثل أعضاء هيئة التدريس والموظفين وطلاب الدكتوراه) في [البلدان
المتاحة](https://ai.google.dev/gemini-api/docs/available-regions?hl=ar) تقديم طلب للحصول على رصيد في Gemini API وسقف استخدام أعلى لمشاريعهم البحثية. يتيح هذا الدعم إنتاجية أعلى للتجارب العلمية ويساهم في تطوير الأبحاث.

نحن مهتمون بشكل خاص بمجالات البحث الواردة في القسم التالي،
ولكن نرحّب بطلبات التقديم من مختلف التخصصات العلمية:

- **التقييمات والمقاييس**: طُرق تقييم يوافق عليها المنتدى ويمكن أن تقدّم إشارة أداء قوية في مجالات مثل الدقة الواقعية والأمان واتّباع التعليمات والاستدلال والتخطيط.
- **تسريع الاكتشافات العلمية بما يعود بالنفع على البشرية**: التطبيقات المحتملة للذكاء الاصطناعي في الأبحاث العلمية المتعددة التخصصات، بما في ذلك مجالات مثل الأمراض النادرة والمهملة، وعلم الأحياء التجريبي، وعلم المواد، والاستدامة
- **التجسيد والتفاعلات**: استخدام النماذج اللغوية الكبيرة لاستكشاف تفاعلات جديدة في مجالات الذكاء الاصطناعي المجسَّد والتفاعلات المحيطة والروبوتات والتفاعل بين الإنسان والحاسوب
- **الإمكانات الناشئة**: استكشاف إمكانات بالذكاء الاصطناعي الوكيل جديدة مطلوبة لتحسين الاستدلال والتخطيط، وكيفية توسيع نطاق الإمكانات أثناء الاستنتاج (مثل استخدام Gemini Flash).
- **التفاعل مع المحتوى المتعدّد الوسائط وفهمه**: تحديد الثغرات والفرص في النماذج الأساسية المتعدّدة الوسائط من أجل التحليل والاستدلال والتخطيط لمجموعة متنوعة من المهام

الأهلية: يمكن فقط للأفراد (أعضاء هيئة التدريس أو الباحثين أو ما يعادلهم) التابعين لمؤسسة أكاديمية صالحة أو مؤسسة بحثية أكاديمية تقديم طلب. يُرجى العِلم أنّه سيتم منح إذن الوصول إلى واجهة برمجة التطبيقات والائتمانات وإزالتها وفقًا لتقدير Google. نراجع الطلبات شهريًا.

### بدء البحث باستخدام Gemini API

[تقديم طلب الآن](https://forms.gle/HMviQstU8PxC5iCt5)

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-24 (حسب التوقيت العالمي المتفَّق عليه)

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-24 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
