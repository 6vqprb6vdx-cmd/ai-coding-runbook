---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar
fetched_at: 2026-10-26T06:07:18.515104+00:00
title: "\u0627\u0644\u0627\u0633\u062a\u0646\u062a\u0627\u062c \u0627\u0644\u0645\u0631\u0646 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الاستنتاج المرن

‫Gemini Flex API هو مستوى استنتاج يتيح خفض التكلفة بنسبة% 50 مقارنةً بالأسعار العادية، مقابل سرعة متغيرة ومدى توفّر بأفضل جهد. تم تصميمها لأحمال العمل التي تتحمّل وقت الاستجابة وتتطلّب معالجة متزامنة ولكنّها لا تحتاج إلى الأداء في الوقت الفعلي الذي توفّره واجهة برمجة التطبيقات العادية.

## كيفية استخدام Flex

لاستخدام فئة Flex، حدِّد `service_tier` على أنّها `flex` في طلبك. تستخدم الطلبات تلقائيًا الفئة العادية في حال حذف هذا الحقل.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.8-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Analyze this dataset for trends..."))
        .serviceTier(ServiceTier.FLEX)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

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
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("Analyze this dataset for trends..."),
            ServiceTier: interactions.ServiceTierFlex.ToPointer(),
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## طريقة عمل الاستنتاج المرن

تعمل ميزة الاستنتاج المرن في Gemini Flex كجسر بين واجهة برمجة التطبيقات العادية و[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar) التي تتيح معالجة البيانات خلال 24 ساعة. وتستخدم هذه الفئة سعة الحوسبة "القابلة للتعديل" في غير أوقات الذروة لتوفير حلّ منخفض التكلفة للمهام التي يتم تنفيذها في الخلفية وسير العمل المتسلسل.

| الميزة | التعبير | الأولوية | خطة "الرزمة العادية" | مجمّعة |
| --- | --- | --- | --- | --- |
| **الأسعار** | خصم بنسبة% 50 | أكثر من خطة Standard بنسبة تتراوح بين %75 و%100 | السعر الكامل | خصم بنسبة% 50 |
| **وقت الاستجابة** | الدقائق (الهدف: من دقيقة إلى 15 دقيقة) | منخفض (بالثواني) | ثوانٍ إلى دقائق | ما يصل إلى 24 ساعة |
| **الموثوقية** | أفضل جودة ممكنة (يمكن التضحية بها) | عالية (غير قابلة للتخفيض) | مرتفع / مرتفع إلى حد ما | عالية (لمعدّل نقل البيانات) |
| **الواجهة** | متزامن | متزامن | متزامن | غير متزامن |

### المزايا الرئيسية

- **الكفاءة من حيث التكلفة**: توفير كبير في تكاليف التقييمات غير الإنتاجية والوكلاء في الخلفية وتحسين البيانات
- **سهولة الاستخدام**: ما عليك سوى إضافة مَعلمة واحدة إلى طلباتك الحالية.
- **سير العمل المتزامن**: خيار مثالي لسلاسل واجهات برمجة التطبيقات المتسلسلة التي يعتمد فيها الطلب التالي على ناتج الطلب السابق، ما يجعله أكثر مرونة من "المعالجة المجمّعة" لسير العمل بالذكاء الاصطناعي الوكيل.

### حالات الاستخدام

- **التقييمات غير المتصلة بالإنترنت**: إجراء اختبارات الانحدار أو قوائم الصدارة باستخدام "نماذج اللغة الكبيرة كحكم"
- **الوكلاء الذين يعملون في الخلفية**: المهام المتسلسلة، مثل تعديلات نظام إدارة علاقات العملاء أو إنشاء الملفات الشخصية أو الإشراف على المحتوى، حيث يمكن قبول تأخيرات لمدة دقائق
- **الأبحاث ذات الميزانية المحدودة**: التجارب الأكاديمية التي تتطلّب حجمًا كبيرًا من الرموز المميّزة بميزانية محدودة.

### الحدود القصوى لمعدّل الاستخدام

يتم احتساب عدد طلبات الاستنتاج المرن ضمن [الحدود القصوى لمعدّل الاستخدام](https://aistudio.google.com/rate-limit?hl=ar) العامة، ولا يوفّر حدودًا قصوى موسّعة لمعدّل الاستخدام مثل [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar).

### السعة القابلة للتخفيض

يتم التعامل مع حركة المرور المرنة بأولوية أقل. في حال حدوث ارتفاع مفاجئ في عدد الزيارات العادية، قد يتم إيقاف طلبات Flex أو إزالتها لضمان توفّر السعة للمستخدمين ذوي الأولوية العالية. إذا كنت تبحث عن استنتاج ذي أولوية عالية، اطّلِع على [الاستنتاج ذو الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar).

### رموز الخطأ

عندما تكون سعة Flex غير متاحة أو يكون النظام مزدحمًا، ستعرض واجهة برمجة التطبيقات رموز الخطأ العادية التالية:

- **‫503 الخدمة غير متاحة**: يتلقّى النظام عدد طلبات كبيرًا جدًا في الوقت الحالي.
- **‫429 Too Many Requests**: تجاوز حدود المعدّل أو استنفاد الموارد

### مسؤولية العميل

- **عدم توفّر خيار احتياطي من جهة الخادم**: لمنع فرض رسوم غير متوقّعة، لن يُجري النظام ترقية تلقائية لطلب Flex إلى المستوى "العادي" إذا كانت سعة Flex ممتلئة.
- **عمليات إعادة المحاولة**: عليك تنفيذ منطق إعادة المحاولة من جهة العميل باستخدام خوارزمية الرقود الأسي الثنائي.
- **مهلات**: بما أنّ طلبات Flex قد تبقى في قائمة الانتظار، ننصحك بزيادة المهلات من جهة العميل إلى 10 دقائق أو أكثر لتجنُّب إغلاق الاتصال قبل الأوان.

## تعديل فترات المهلة

يمكنك ضبط مهلة لكل طلب في REST API ومكتبات العملاء.
احرص دائمًا على أن يغطي المهلة الزمنية من جهة العميل فترة انتظار الخادم المقصودة (على سبيل المثال، 600 ثانية أو أكثر في قوائم انتظار Flex). تتوقّع حِزم SDK قيم المهلة بالملّي ثانية.

### مهلات الطلب

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client =
    Client.builder()
        .httpOptions(HttpOptions.builder().timeout(900000).build())
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("why is the sky blue?"))
        .serviceTier(ServiceTier.FLEX)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"
    "time"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        HTTPOptions: genai.HTTPOptions{
            Timeout: genai.Ptr(15 * time.Minute),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("why is the sky blue?"),
            ServiceTier: interactions.ServiceTierFlex.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

## تنفيذ عمليات إعادة المحاولة

بما أنّ Flex يمكن إيقافه مؤقتًا ويتعذّر تنفيذه بسبب أخطاء 503، إليك مثال على التنفيذ الاختياري لمنطق إعادة المحاولة لمواصلة الطلبات التي تعذّر تنفيذها:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.8-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.8-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.8-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.8-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

int maxRetries = 3;
int baseDelay = 5;
Interaction interaction = null;

for (int attempt = 0; attempt < maxRetries; attempt++) {
  try {
    CreateModelInteraction flexParams =
        CreateModelInteraction.builder()
            .model(Model.of("gemini-3.8-flash"))
            .input(InteractionsInput.of("Analyze this batch statement."))
            .serviceTier(ServiceTier.FLEX)
            .build();
    interaction =
        client.interactions.create(CreateInteractionRequestBody.of(flexParams)).interaction().get();
    break;
  } catch (Exception e) {
    if (attempt < maxRetries - 1) {
      int delay = baseDelay * (1 << attempt); // Exponential Backoff
      System.out.println("Flex busy, retrying in " + delay + "s...");
      Thread.sleep(delay * 1000L);
    } else {
      System.out.println("Flex exhausted, falling back to Standard...");
      CreateModelInteraction standardParams =
          CreateModelInteraction.builder()
              .model(Model.of("gemini-3.8-flash"))
              .input(InteractionsInput.of("Analyze this batch statement."))
              .build();
      interaction =
          client
              .interactions
              .create(CreateInteractionRequestBody.of(standardParams))
              .interaction()
              .get();
    }
  }
}

if (interaction != null) {
  System.out.println(interaction.outputText().orElse(""));
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

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

    maxRetries := 3
    baseDelay := 5
    var interaction *interactions.Interaction

    for attempt := 0; attempt < maxRetries; attempt++ {
        res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model:       interactions.Model("gemini-3.8-flash"),
                Input:       interactions.NewInteractionsInput("Analyze this batch statement."),
                ServiceTier: interactions.ServiceTierFlex.ToPointer(),
            }),
        })
        if err == nil {
            interaction = res.Interaction
            break
        }

        if attempt < maxRetries-1 {
            delay := baseDelay * (1 << attempt) // Exponential Backoff
            fmt.Printf("Flex busy, retrying in %ds...\n", delay)
            time.Sleep(time.Duration(delay) * time.Second)
        } else {
            fmt.Println("Flex exhausted, falling back to Standard...")
            stdRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model: interactions.Model("gemini-3.8-flash"),
                    Input: interactions.NewInteractionsInput("Analyze this batch statement."),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            interaction = stdRes.Interaction
        }
    }

    if interaction != nil && interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
}
```

## الأسعار

يتم تحديد سعر الاستنتاج المرن بنسبة% 50 من [سعر واجهة برمجة التطبيقات العادية](https://ai.google.dev/gemini-api/docs/pricing?hl=ar)
ويتم تحصيل الرسوم لكل رمز مميز.

## النماذج المتوافقة

تتيح النماذج التالية الاستنتاج المرن:

| الطراز | الاستنتاج المرن |
| --- | --- |
| [‫Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=ar) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=ar) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ar) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ar) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ✔️ |
| [‫Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [معاينة Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ |

## الخطوات التالية

- [استنتاج الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar) لوقت الاستجابة الفائق السرعة
- [الرموز المميّزة](https://ai.google.dev/gemini-api/docs/tokens?hl=ar): فهم الرموز المميّزة

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-10-13 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-10-13 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
