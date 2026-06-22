---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar
fetched_at: 2026-06-22T06:30:23.282507+00:00
title: "\u0627\u0644\u0627\u0633\u062a\u0646\u062a\u0627\u062c \u0627\u0644\u0645\u0631\u0646 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الاستنتاج المرن

‫Gemini Flex API هو مستوى استنتاج يتيح خفض التكلفة بنسبة% 50 مقارنةً بالأسعار العادية، مقابل وقت استجابة متغيّر وتوفّر بأفضل جهد ممكن. وهي مصمَّمة لأحمال العمل التي يمكنها تحمّل وقت الاستجابة وتتطلّب معالجة متزامنة، ولكنّها لا تحتاج إلى الأداء في الوقت الفعلي الذي توفّره واجهة برمجة التطبيقات العادية.

## كيفية استخدام Flex

لاستخدام المستوى المرن، حدِّد `service_tier` على أنّه `flex` في نص الطلب. تستخدم الطلبات تلقائيًا الفئة العادية إذا تم حذف هذا الحقل.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Analyze this dataset for trends...",
        config={"service_tier": "flex"},
    )
    print(response.text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
    const response = await ai.models.generateContent({
      model: "gemini-3.5-flash",
      contents: "Analyze this dataset for trends...",
      config: { serviceTier: "flex" },
    });
    console.log(response.text);
  } catch (e) {
    console.log(`Flex request failed: ${e}`);
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
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Analyze this dataset for trends..."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        log.Printf("Flex request failed: %v", err)
        return
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Summarize the latest research on quantum computing."}]
  }],
  "service_tier": "flex"
}'
```

## طريقة عمل الاستدلال المرن

تساعد Gemini Flex Inference في سد الفجوة بين واجهة برمجة التطبيقات العادية و[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar) التي تستغرق 24 ساعة. تستفيد هذه الخدمة من سعة الحوسبة "القابلة للتخفيض" في غير أوقات الذروة لتوفير حلّ فعّال من حيث التكلفة للمهام التي تعمل في الخلفية وسير العمل التسلسلي.

| الميزة | التعبير | الأولوية | خطة "الرزمة العادية" | مجمّعة |
| --- | --- | --- | --- | --- |
| **الأسعار** | خصم بنسبة% 50 | أكثر من خطة Standard بنسبة تتراوح بين %75 و%100 | السعر الكامل | خصم بنسبة% 50 |
| **وقت الاستجابة** | دقائق (المدة المستهدَفة من دقيقة واحدة إلى 15 دقيقة) | منخفض (ثوانٍ) | من ثوانٍ إلى دقائق | ما يصل إلى 24 ساعة |
| **الموثوقية** | أفضل جهد (يمكن إيقافه) | عالية (غير قابلة للإزالة) | مرتفع / مرتفع إلى حد ما | عالية (لمعدّل نقل البيانات) |
| **الواجهة** | متزامن | متزامن | متزامن | غير متزامن |

### المزايا الرئيسية

- **فعالية التكلفة**: تحقيق وفورات كبيرة في التكاليف عند إجراء عمليات التقييم غير الإنتاجية، واستخدام البرامج في الخلفية، وإثراء البيانات
- **سهولة الاستخدام**: لا حاجة إلى إدارة عناصر الدفعات أو معرّفات المهام أو الاستقصاء، ما عليك سوى إضافة مَعلمة واحدة إلى طلباتك الحالية.
- **نماذج سير العمل المتزامنة**: هي الأنسب لسلاسل واجهات برمجة التطبيقات المتسلسلة التي يعتمد فيها الطلب التالي على نتيجة الطلب السابق، ما يجعلها أكثر مرونة من "المعالجة المجمّعة" لنماذج سير العمل المستندة إلى الوكيل.

### حالات الاستخدام

- **التقييمات بلا إنترنت**: إجراء اختبارات الانحدار أو قوائم الصدارة باستخدام "نماذج اللغة الكبيرة كحكم"
- **الوكلاء الذين يعملون في الخلفية**: المهام المتسلسلة، مثل تعديلات نظام إدارة علاقات العملاء أو إنشاء الملفات الشخصية أو الإشراف على المحتوى، حيث يكون التأخير لبضع دقائق مقبولاً.
- **البحث المقيّد بالميزانية**: تجارب أكاديمية تتطلّب عددًا كبيرًا من الرموز المميزة بميزانية محدودة.

### حدود معدّل الاستخدام

يتم احتساب عدد الزيارات التي تستخدم ميزة "الاستنتاج المرن" ضمن [حدود المعدّل](https://aistudio.google.com/rate-limit?hl=ar) العامة، ولا توفّر هذه الميزة حدودًا موسّعة للمعدّل مثل [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar).

### السعة القابلة للخفض

يتم التعامل مع الزيارات المرنة بأولوية أقل. في حال حدوث ارتفاع مفاجئ في عدد الزيارات العادية، قد يتم إيقاف طلبات Flex أو إزالتها لضمان توفّر سعة للمستخدمين ذوي الأولوية العالية. إذا كنت تبحث عن استنتاج ذي أولوية عالية، يمكنك الاطّلاع على [الاستنتاج ذو الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar).

### رموز الخطأ

عندما تكون سعة Flex غير متاحة أو يكون النظام مزدحمًا، ستعرض واجهة برمجة التطبيقات رموز الخطأ العادية التالية:

- **‫503 Service Unavailable**: يعمل النظام بكامل طاقته حاليًا.
- **429 Too Many Requests**: تجاوز حدود المعدّل أو استنفاد الموارد

### مسؤولية العميل

- **عدم توفّر خيار احتياطي من جهة الخادم**: لمنع فرض رسوم غير متوقّعة، لن يرقّي النظام تلقائيًا طلب Flex إلى فئة Standard إذا كانت سعة Flex ممتلئة.
- **عمليات إعادة المحاولة**: يجب تنفيذ منطق إعادة المحاولة من جهة العميل باستخدام خوارزمية الرقود الأسي الثنائي.
- **مهلات**: بما أنّ طلبات Flex قد تبقى في صفّ الانتظار، ننصحك بزيادة المهلات من جهة العميل إلى 10 دقائق أو أكثر لتجنُّب إغلاق الاتصال قبل الأوان.

## تعديل فترات المهلة

يمكنك ضبط مهلات لكل طلب في واجهة REST API ومكتبات العميل،
ومهلات عامة فقط عند استخدام مكتبات العميل.

احرص دائمًا على أن يغطي المهلة الزمنية من جهة العميل فترة انتظار الخادم المقصودة (على سبيل المثال، 600 ثانية أو أكثر لقوائم انتظار Flex). تتوقّع حِزم SDK أن تكون قيم المهلة بالملي ثانية.

### مهلات الطلبات

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="why is the sky blue?",
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 900000}
        },
    )
except Exception as e:
    print(f"Flex request failed: {e}")

# Example with streaming
try:
    response = client.models.generate_content_stream(
        model="gemini-3.5-flash",
        contents=["List 5 ideas for a sci-fi movie."],
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 60000}
        }
        # Per-request timeout for the streaming operation
    )
    for chunk in response:
        print(chunk.text, end="")

except Exception as e:
    print(f"An error occurred during streaming: {e}")
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const client = new GoogleGenAI({});

 async function main() {
     try {
         const response = await client.models.generateContent({
             model: "gemini-3.5-flash",
             contents: "why is the sky blue?",
             config: {
               serviceTier: "flex",
               httpOptions: {timeout: 900000}
             },
         });
     } catch (e) {
         console.log(`Flex request failed: ${e}`);
     }

     // Example with streaming
     try {
         const response = await client.models.generateContentStream({
             model: "gemini-3.5-flash",
             contents: ["List 5 ideas for a sci-fi movie."],
             config: {
                 serviceTier: "flex",
                 httpOptions: {timeout: 60000}
             },
         });
         for await (const chunk of response.stream) {
             process.stdout.write(chunk.text());
         }
     } catch (e) {
         console.log(`An error occurred during streaming: ${e}`);
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
    "time"

    "google.golang.org/api/iterator"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    timeoutCtx, cancel := context.WithTimeout(ctx, 900*time.Second)
    defer cancel()

    _, err = client.Models.GenerateContent(
        timeoutCtx,
        "gemini-3.5-flash",
        genai.Text("why is the sky blue?"),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        fmt.Printf("Flex request failed: %v\n", err)
    }

    // Example with streaming
    streamTimeoutCtx, streamCancel := context.WithTimeout(ctx, 60*time.Second)
    defer streamCancel()

    iter := client.Models.GenerateContentStream(
        streamTimeoutCtx,
        "gemini-3.5-flash",
        genai.Text("List 5 ideas for a sci-fi movie."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    for {
        response, err := iter.Next()
        if err == iterator.Done {
            break
        }
        if err != nil {
            fmt.Printf("An error occurred during streaming: %v\n", err)
            break
        }
        fmt.Print(response.Candidates[0].Content.Parts[0])
    }
}
```

### REST

عند إجراء طلبات REST، يمكنك التحكّم في المهلات باستخدام مجموعة من عناوين HTTP وخيارات `curl`:

- **`X-Server-Timeout` العنوان (مهلة من جهة الخادم)**: يقترح هذا العنوان مدة مهلة مفضّلة (600 ثانية تلقائيًا) لخادم Gemini API. سيحاول الخادم الالتزام بذلك، ولكن ليس هناك ما يضمن ذلك. يجب أن تكون القيمة بالثواني.
- **`--max-time` في `curl` (مهلة من جهة العميل)**: يضبط الخيار `curl --max-time
  <seconds>` حدًا أقصى لإجمالي الوقت (بالثواني) الذي ستنتظره `curl`
  حتى تكتمل العملية بأكملها. هذا إجراء وقائي من جهة العميل.

```
 # Set a server timeout hint of 120 seconds and a client-side curl timeout of 125 seconds.
 curl --max-time 125 \
   -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "X-Server-Timeout: 120" \
   -d '{
   "contents": [{
     "parts":[{"text": "Summarize the latest research on quantum computing."}]
   }],
   "service_tier": "flex"
 }'
```

### مهلات عالمية

إذا كنت تريد أن تتضمّن جميع طلبات البيانات من واجهة برمجة التطبيقات التي يتم إجراؤها من خلال مثيل `genai.Client` معيّن (مكتبات العميل فقط) مهلة تلقائية، يمكنك ضبط ذلك عند تهيئة العميل باستخدام `http_options` و`genai.types.HttpOptions`.

### Python

```
from google import genai
from google.genai import types

global_timeout_ms = 120000

client_with_global_timeout = genai.Client(
    http_options=types.HttpOptions(timeout=global_timeout_ms)
)

try:
    # Calling generate_content using global timeout...
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.5-flash",
        contents="Summarize the history of AI development since 2000.",
        config={"service_tier": "flex"},
    )
    print(response.text)

    # A per-request timeout will *override* the global timeout for that specific call.
    shorter_timeout = 30000
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.5-flash",
        contents="Provide a very brief definition of machine learning.",
        config={
            "service_tier": "flex",
            "http_options":{"timeout": shorter_timeout}
        }  # Overrides the global timeout
    )

    print(response.text)

except TimeoutError:
    print(
        f"A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
    )
except Exception as e:
    print(f"An error occurred: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const globalTimeoutMs = 120000;

const clientWithGlobalTimeout = new GoogleGenAI({httpOptions: {timeout: globalTimeoutMs}});

async function main() {
    try {
        // Calling generate_content using global timeout...
        const response1 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.5-flash",
            contents: "Summarize the history of AI development since 2000.",
            config: { serviceTier: "flex" },
        });
        console.log(response1.text());

        // A per-request timeout will *override* the global timeout for that specific call.
        const shorterTimeout = 30000;
        const response2 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.5-flash",
            contents: "Provide a very brief definition of machine learning.",
            config: {
                serviceTier: "flex",
                httpOptions: {timeout: shorterTimeout}
            }  // Overrides the global timeout
        });

        console.log(response2.text());

    } catch (e) {
        if (e.name === 'TimeoutError' || e.message?.includes('timeout')) {
            console.log(
                "A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
            );
        } else {
            console.log(`An error occurred: ${e}`);
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
     "time"

     "google.golang.org/genai"
 )

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     model := client.GenerativeModel("gemini-3.5-flash")

     // Go uses context for timeouts, not client options.
     // Set a default timeout for requests.
     globalTimeout := 120 * time.Second
     fmt.Printf("Using default timeout of %v seconds.\n", globalTimeout.Seconds())

     fmt.Println("Calling generate_content (using default timeout)...")
     ctx1, cancel1 := context.WithTimeout(ctx, globalTimeout)
     defer cancel1()
     resp1, err := model.GenerateContent(ctx1, genai.Text("Summarize the history of AI development since 2000."), &genai.GenerateContentConfig{ServiceTier: "flex"})
     if err != nil {
         log.Printf("Request 1 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 1 successful.")
         fmt.Println(resp1.Text())
     }

     // A different timeout can be used for other requests.
     shorterTimeout := 30 * time.Second
     fmt.Printf("\nCalling generate_content with a shorter timeout of %v seconds...\n", shorterTimeout.Seconds())
     ctx2, cancel2 := context.WithTimeout(ctx, shorterTimeout)
     defer cancel2()
     resp2, err := model.GenerateContent(ctx2, genai.Text("Provide a very brief definition of machine learning."), &genai.GenerateContentConfig{
         ServiceTier: "flex",
     })
     if err != nil {
         log.Printf("Request 2 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 2 successful.")
         fmt.Println(resp2.Text())
     }
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
            return client.models.generate_content(
                model="gemini-3.5-flash",
                contents="Analyze this batch statement.",
                config={"service_tier": "flex"},
            )
        except Exception as e:
            # Check for 503 Service Unavailable or 429 Rate Limits
            print(e.code)
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                # Fallback to standard on last strike (Optional)
                print("Flex exhausted, falling back to Standard...")
                return client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents="Analyze this batch statement."
                )

# Usage
response = call_with_retry()
print(response.text)
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const ai = new GoogleGenAI({});

 async function sleep(ms) {
   return new Promise(resolve => setTimeout(resolve, ms));
 }

 async function callWithRetry(maxRetries = 3, baseDelay = 5) {
   for (let attempt = 0; attempt < maxRetries; attempt++) {
     try {
       console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
       const response = await ai.models.generateContent({
         model: "gemini-3.5-flash",
         contents: "Analyze this batch statement.",
         config: { serviceTier: 'flex' },
       });
       return response;
     } catch (e) {
       if (attempt < maxRetries - 1) {
         const delay = baseDelay * (2 ** attempt);
         console.log(`Flex busy, retrying in ${delay}s...`);
         await sleep(delay * 1000);
       } else {
         console.log("Flex exhausted, falling back to Standard...");
         return await ai.models.generateContent({
           model: "gemini-3.5-flash",
           contents: "Analyze this batch statement.",
         });
       }
     }
   }
 }

 async function main() {
     const response = await callWithRetry();
     console.log(response.text);
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
     "math"
     "time"

     "google.golang.org/genai"
 )

 func callWithRetry(ctx context.Context, client *genai.Client, maxRetries int, baseDelay time.Duration) (*genai.GenerateContentResponse, error) {
     modelName := "gemini-3.5-flash"
     content := genai.Text("Analyze this batch statement.")
     flexConfig := &genai.GenerateContentConfig{
         ServiceTier: "flex",
     }

     for attempt := 0; attempt < maxRetries; attempt++ {
         log.Printf("Attempt %d: Calling Flex tier...", attempt+1)
         resp, err := client.Models.GenerateContent(ctx, modelName, content, flexConfig)
         if err == nil {
             return resp, nil
         }

         log.Printf("Attempt %d failed: %v", attempt+1, err)

         if attempt < maxRetries-1 {
             delay := time.Duration(float64(baseDelay) * math.Pow(2, float64(attempt)))
             log.Printf("Flex busy, retrying in %v...", delay)
             time.Sleep(delay)
         } else {
             log.Println("Flex exhausted, falling back to Standard...")
             return client.Models.GenerateContent(ctx, modelName, content)
         }
     }
     return nil, fmt.Errorf("retries exhausted") // Should not be reached
 }

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     resp, err := callWithRetry(ctx, client, 3, 5*time.Second)
     if err != nil {
         log.Fatalf("Failed after retries: %v", err)
     }
     fmt.Println(resp.Text())
 }
```

## الأسعار

يتم تحديد سعر Flex inference بنسبة% 50 من [سعر واجهة برمجة التطبيقات العادية](https://ai.google.dev/gemini-api/docs/pricing?hl=ar)
ويتم تحصيل الرسوم لكل رمز مميز.

## النماذج المتوافقة

تتيح الطُرز التالية استنتاج Flex:

| الطراز | Flex inference |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) | ✔️ |
| [‫Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ✔️ |
| [إصدار تجريبي من Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [معاينة Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |
| [معاينة الصور في Gemini 3 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=ar) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=ar) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ |

## الخطوات التالية

يمكنك الاطّلاع على خيارات [الاستنتاج والتحسين](https://ai.google.dev/gemini-api/docs/optimization?hl=ar) الأخرى في Gemini:

- [استنتاج الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar) لوقت الاستجابة الفائق السرعة
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar) للمعالجة غير المتزامنة في غضون 24 ساعة
- [التخزين المؤقت للسياق](https://ai.google.dev/gemini-api/docs/caching?hl=ar) لتقليل تكاليف الرموز المميزة للإدخال

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-19 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-19 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
