---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=ar
fetched_at: 2026-10-19T05:31:40.933031+00:00
title: "\u0633\u064a\u0627\u0642 \u0639\u0646\u0648\u0627\u0646 URL \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# سياق عنوان URL

تتيح لك أداة "سياق عنوان URL" تقديم سياق إضافي للنماذج في شكل عناوين URL. من خلال تضمين عناوين URL في طلبك، سيتمكّن النموذج من الوصول إلى المحتوى من تلك الصفحات (ما دام ليس من نوع عناوين URL المدرَجة في [قسم القيود](#limitations)) للاستناد إليه وتحسين رده.

تكون أداة سياق عنوان URL مفيدة في مهام مثل ما يلي:

- **استخراج البيانات**: يمكنك استخراج معلومات محدّدة، مثل الأسعار أو الأسماء أو النتائج الرئيسية، من عناوين URL متعدّدة.
- **مقارنة المستندات**: يمكنك تحليل تقارير أو مقالات أو ملفات PDF متعددة لتحديد الاختلافات وتتبُّع المؤشرات.
- **تجميع المعلومات وإنشاء المحتوى**: يمكنك دمج المعلومات من عدة عناوين URL للمصادر لإنشاء ملخّصات أو منشورات مدوّنة أو تقارير دقيقة.
- **تحليل الرموز البرمجية والمستندات**: يمكنك الإشارة إلى مستودع GitHub أو مستندات فنية لشرح الرموز البرمجية أو إنشاء تعليمات الإعداد أو الإجابة عن الأسئلة.

يوضّح المثال التالي كيفية مقارنة وصفتَي طعام من موقعَين إلكترونيَين مختلفَين.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
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

    url1 := "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
    url2 := "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(
                fmt.Sprintf("Compare the ingredients and cooking times from the recipes at %s and %s", url1, url2),
            ),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.URLContext{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Print the model's text response and its source annotations
    for _, step := range res.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, contentBlock := range step.ModelOutputStep.Content {
                if contentBlock.TextContent != nil {
                    fmt.Println(contentBlock.TextContent.Text)
                    if len(contentBlock.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range contentBlock.TextContent.Annotations {
                            if annotation.URLCitation != nil {
                                fmt.Printf("  - %s: %s\n", annotation.URLCitation.GetTitle(), annotation.URLCitation.GetURL())
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## آلية العمل

تستخدم أداة "سياق عناوين URL" عملية استرجاع من خطوتَين لتحقيق التوازن بين السرعة والتكلفة والوصول إلى البيانات الحديثة. عند تقديم عنوان URL، تحاول الأداة أولاً جلب المحتوى من ذاكرة تخزين مؤقت داخلية للفهرس. ويعمل هذا كذاكرة تخزين
مؤقت محسّنة للغاية. إذا لم يكن عنوان URL متاحًا في الفهرس (على سبيل المثال، إذا كانت الصفحة جديدة جدًا)، ستعود الأداة تلقائيًا إلى إجراء جلب مباشر.
يؤدي ذلك إلى الوصول مباشرةً إلى عنوان URL لاسترداد محتواه في الوقت الفعلي.

## الدمج مع أدوات أخرى

يمكنك دمج أداة سياق عناوين URL مع أدوات أخرى لإنشاء مسارات عمل أكثر فعالية.

تتيح [نماذج Gemini 3](#supported-models) الجمع بين الأدوات المضمّنة
(مثل "سياق عناوين URL") والأدوات المخصّصة (استدعاء الدوال). يمكنك الاطّلاع على مزيد من المعلومات في صفحة [مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).

### تحديد المصدر من خلال "بحث Google"

عند تفعيل كل من سياق عناوين URL و[تحديد المصدر من خلال &quot;بحث Google&quot;](https://ai.google.dev/gemini-api/docs/grounding?hl=ar)، يمكن للنموذج استخدام إمكانات البحث للعثور على المعلومات ذات الصلة على الإنترنت، ثم استخدام أداة سياق عناوين URL للحصول على فهم أكثر تعمقًا للصفحات التي يعثر عليها. هذا الأسلوب فعّال مع الطلبات التي تتطلّب بحثًا واسع النطاق وتحليلاً معمّقًا لصفحات معيّنة.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
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
            Input: interactions.NewInteractionsInput("Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.URLContext{}),
                interactions.NewTool(interactions.GoogleSearch{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, contentBlock := range step.ModelOutputStep.Content {
                if contentBlock.TextContent != nil {
                    fmt.Println(contentBlock.TextContent.Text)
                }
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## فهم الردّ

عندما يستخدم النموذج أداة "سياق عناوين URL"، يتضمّن ردّه النصي تعليقات توضيحية مضمّنة من النوع `url_citation` على مجموعة النصوص. يربط كل تعليق توضيحي جزءًا من نص الردّ (من خلال `start_index` و`end_index`) بعنوان URL المصدر الذي تم استخلاصه منه. هذه هي الطريقة الأساسية لعرض الاقتباسات في تطبيقك، ويمكنك الاطّلاع على [المثال الرئيسي أعلاه](#get-started) لمعرفة كيفية استخراجها.

تتضمّن الإجابة أيضًا خطوة `url_context_result` مع بيانات وصفية حول كل محاولة لاسترداد عنوان URL (الحالة وعنوان URL الذي تم استرداده). وهذا مفيد بشكل أساسي لتصحيح الأخطاء.

### عمليات التحقّق من الأمان

يُجري النظام عملية تحقّق من الإشراف على المحتوى في عناوين URL للتأكّد من أنّها تستوفي معايير الأمان. إذا لم ينجح عنوان URL في هذا الفحص، ستعرض خطوة `url_context_result` المقابلة `status` من `"unsafe"`.

### عدد الرموز المميّزة

يتم احتساب المحتوى الذي يتم استرداده من عناوين URL المحدّدة في طلبك
كجزء من الرموز المميّزة للإدخال. يمكنك الاطّلاع على عدد الرموز المميزة في
الكائن `usage` الخاص بالتفاعل. في ما يلي مثال على ذلك:

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

يعتمد السعر لكل رمز مميّز على النموذج المستخدَم، ويمكنك الاطّلاع على صفحة [الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar) لمزيد من التفاصيل.

## النماذج المتوافقة

| الطراز | سياق عناوين URL |
| --- | --- |
| [‫Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=ar) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=ar) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ar) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ar) | ✔️ |
| [‫Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ✔️ |
| [معاينة Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ |

## أفضل الممارسات

- **تقديم عناوين URL محدّدة**: للحصول على أفضل النتائج، قدِّم عناوين URL مباشرة إلى
  المحتوى الذي تريد أن يحلّله النموذج. سيسترد النموذج المحتوى فقط من عناوين URL التي تقدّمها، وليس أي محتوى من الروابط المضمّنة.
- **التحقّق من إمكانية الوصول**: تأكَّد من أنّ عناوين URL التي تقدّمها لا تؤدي إلى صفحات تتطلّب تسجيل الدخول أو تقع خلف حاجز دفع.
- **استخدام عنوان URL الكامل**: يجب تقديم عنوان URL الكامل، بما في ذلك البروتوكول (مثلاً، https://www.google.com بدلاً من google.com فقط).

## القيود

- حدّ الطلب: يمكن للأداة معالجة ما يصل إلى 20 عنوان URL لكل طلب.
- حجم محتوى عنوان URL: الحد الأقصى لحجم المحتوى الذي يتم استرداده من عنوان URL واحد هو 34 ميغابايت.
- إمكانية الوصول العلني: يجب أن تكون عناوين URL متاحة للجميع على الويب.
  لا تتوافق عناوين المضيف المحلي (مثل localhost و127.0.0.1) والشبكات الخاصة وخدمات الأنفاق (مثل ngrok وpinggy).

### أنواع المحتوى المتوافقة وغير المتوافقة

يمكن للأداة استخراج المحتوى من عناوين URL التي تتضمّن أنواع المحتوى التالية:

- النصوص (text/html وapplication/json وtext/plain وtext/xml وtext/css وtext/javascript وtext/csv وtext/rtf)
- صورة (image/png أو image/jpeg أو image/bmp أو image/webp)
- ملف PDF ‏ (application/pdf)

**لا** تتوافق أنواع المحتوى التالية مع ميزة "استعراض المحتوى":

- المحتوى المحمي بنظام حظر الاشتراك غير المدفوع
- فيديوهات على YouTube (يُرجى الاطّلاع على
  [فهم الفيديو](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar#youtube) لمعرفة
  كيفية معالجة عناوين URL على YouTube)
- ملفات Google Workspace، مثل "مستندات Google" أو جداول البيانات
- ملفات الفيديو والصوت

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-10-13 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-10-13 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
