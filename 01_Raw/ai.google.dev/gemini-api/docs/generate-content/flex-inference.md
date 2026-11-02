---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/flex-inference?hl=fa
fetched_at: 2026-11-02T07:13:31.705549+00:00
title: "\u0627\u0633\u062a\u0646\u062a\u0627\u062c \u0627\u0646\u0639\u0637\u0627\u0641\u200c\u067e\u0630\u06cc\u0631 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs/generate-content?hl=fa)

ارسال بازخورد

# استنتاج انعطاف‌پذیر

شرح: با نحوه بهینه‌سازی هزینه‌ها با سطح استنباط «انعطاف‌پذیر» آشنا شوید

‫Gemini Flex API یک سطح استنتاج است که درمقایسه با نرخ‌های استاندارد، ۵۰٪ کاهش هزینه ارائه می‌دهد و درعوض، تأخیر متغیر و دردسترس بودن با حداکثر تلاش را ارائه می‌دهد. این API برای حجم‌های کاری با تحمل تأخیر طراحی شده است که به پردازش هم‌زمان نیاز دارند اما به عملکرد هم‌زمان API استاندارد نیاز ندارند.

## نحوه استفاده از Flex

برای استفاده از سطح Flex،‏ `service_tier` را به‌عنوان `flex` در
بدنه درخواست مشخص کنید. به‌طور پیش‌فرض، اگر این فیلد حذف شود، درخواست‌ها از سطح استاندارد استفاده می‌کنند.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
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
      model: "gemini-3.8-flash",
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

### رفتن

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
        "gemini-3.8-flash",
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

### استراحت

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Summarize the latest research on quantum computing."}]
  }],
  "service_tier": "flex"
}'
```

## نحوه عملکرد «استنتاج انعطاف‌پذیر»

استنتاج Gemini Flex فاصله بین میانای برنامه‌سازی کاربردی استاندارد و زمان پاسخ ۲۴ ساعته [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=fa) را پر می‌کند. این سرویس از ظرفیت محاسباتی «قابل‌کاهش» در ساعات کم‌مصرف استفاده می‌کند تا راه‌حلی مقرون‌به‌صرفه برای کارهای پس‌زمینه و گردش‌های کاری متوالی ارائه دهد.

| ویژگی | به‌رخ کشیدن | اولویت | استاندارد | دسته |
| --- | --- | --- | --- | --- |
| **قیمت‌گذاری** | ‫٪۵۰ تخفیف | ‫۷۵ تا ۱۰۰٪ بیشتر از «استاندارد» | قیمت کامل | ‫٪۵۰ تخفیف |
| **تأخیر** | دقیقه (هدف ۱ تا ۱۵ دقیقه) | کم (ثانیه) | ثانیه به دقیقه | حداکثر ۲۴ ساعت |
| **قابلیت اطمینان** | نهایت تلاش (قابل‌حذف) | زیاد (غیرقابل ریزش) | زیاد / متوسط روبه‌بالا | بالا (برای توان گذرداد) |
| **میانا** | هم‌زمان | همگام | همگام | غیرهمگام |

### مزایای کلیدی

- **بهینگی هزینه**: صرفه‌جویی قابل‌توجه برای ارزیابی‌های غیرتولیدی، عامل‌های پس‌زمینه، و غنی‌سازی داده‌ها.
- **اصطکاک کم**: نیازی به مدیریت کردن اشیای دسته‌ای، شناسه‌های کار، یا نظرسنجی نیست؛ کافی است یک پارامتر به درخواست‌های موجودتان اضافه کنید.
- **گردش کارهای همگام**: ایده‌آل برای زنجیره‌های متوالی میانای برنامه‌سازی کاربردی که در آن درخواست بعدی به خروجی درخواست قبلی بستگی دارد، که آن را برای گردش کارهای عامل‌گرا انعطاف‌پذیرتر از Batch می‌کند.

### موارد استفاده

- **ارزیابی‌های آفلاین**: اجرای آزمایش‌های رگرسیون «مدل زبانی بزرگ به‌عنوان داور» یا تابلوهای پیشتازان.
- **عامل‌های پس‌زمینه**: تکالیف ترتیبی مثل به‌روزرسانی‌های CRM، ساختن نمایه‌های شخصی، یا مدیریت محتوا که در آن‌ها چند دقیقه تأخیر قابل‌قبول است.
- **پژوهش با بودجه محدود**: آزمایش‌های دانشگاهی که به حجم بالای ژتون با بودجه محدود نیاز دارند.

### محدودیت‌های نرخ

ترافیک استنتاج انعطاف‌پذیر جزو [حدود نرخ](https://aistudio.google.com/rate-limit?hl=fa) عمومی شما محسوب می‌شود؛
این ترافیک حدود نرخ گسترده‌ای مانند [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=fa) ارائه نمی‌دهد.

### ظرفیت قابل‌کاهش

ترافیک Flex با اولویت پایین‌تری درنظر گرفته می‌شود. اگر ترافیک استاندارد افزایش ناگهانی داشته باشد، ممکن است درخواست‌های Flex برای اطمینان از وجود ظرفیت برای کاربران با اولویت بالا، پیش‌دستی یا تخلیه شوند. اگر به‌دنبال استنتاج با اولویت بالا هستید،
[استنتاج با اولویت](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fa) را بررسی کنید

### کدهای خطا

وقتی ظرفیت Flex دردسترس نباشد یا سیستم شلوغ باشد، میانای برنامه‌سازی کاربردی
کدهای خطای استاندارد را برمی‌گرداند:

- **‫۵۰۳ سرویس دردسترس نیست**: درحال‌حاضر، سیستم به حداکثر ظرفیت رسیده است.
- **‫429 درخواست‌های بیش‌ازحد**: محدودیت‌های نرخ یا اتمام منابع.

### مسئولیت کارخواه

- **بدون بازگشت به سمت سرور**: برای جلوگیری از هزینه‌های غیرمنتظره، اگر ظرفیت Flex پر باشد، سیستم به‌طور خودکار درخواست Flex را به سطح Standard ارتقا نمی‌دهد.
- **تلاش‌های مجدد**: باید منطق تلاش مجدد سمت کارخواه خودتان را با
  عقب‌نشینی نمایی پیاده‌سازی کنید.
- **زمان‌های استراحت**: چون درخواست‌های Flex ممکن است در صف قرار بگیرند، توصیه می‌کنیم
  زمان‌های استراحت سمت کارخواه را به ۱۰ دقیقه یا بیشتر افزایش دهید تا از بسته شدن زودرس
  اتصال جلوگیری شود.

## تنظیم پنجره‌های زمان استراحت

می‌توانید زمان‌های اتمام درخواست را برای REST API و کتابخانه‌های کارخواه پیکربندی کنید،
و زمان‌های اتمام سراسری را فقط هنگام استفاده از کتابخانه‌های کارخواه پیکربندی کنید.

همیشه مطمئن شوید که مهلت زمانی سمت مشتری شما پنجره صبر سرور موردنظر را پوشش می‌دهد (برای نمونه، ۶۰۰ ثانیه و بیشتر برای صف‌های انتظار Flex). کیت‌های توسعه نرم‌افزار انتظار دارند مقادیر زمان اتمام برحسب میلی‌ثانیه باشد.

### زمان‌های اتمام درخواست

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
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
        model="gemini-3.8-flash",
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
             model: "gemini-3.8-flash",
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
             model: "gemini-3.8-flash",
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

### رفتن

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
        "gemini-3.8-flash",
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
        "gemini-3.8-flash",
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

هنگام برقراری تماس‌های REST، می‌توانید زمان‌های اتمام را بااستفاده از ترکیبی از سرصفحه‌های HTTP و گزینه‌های `curl` کنترل کنید:

- **سرصفحه `X-Server-Timeout` (مهلت زمانی سمت سرور)**: این سرصفحه مدت‌زمان مهلت زمانی ترجیحی (به‌طور پیش‌فرض ۶۰۰ ثانیه) را به سرور Gemini API پیشنهاد می‌دهد. سرور
  تلاش می‌کند این را رعایت کند، اما تضمینی وجود ندارد. مقدار باید برحسب ثانیه باشد.
- **`--max-time` در `curl` (مهلت سمت کارخواه)**: گزینه `curl --max-time
  <seconds>` محدودیت سختی را برای کل زمان (به ثانیه) که `curl`
  منتظر می‌ماند تا کل عملیات تکمیل شود تعیین می‌کند. این یک اقدام حفاظتی سمت کارخواه است.

```
 # Set a server timeout hint of 120 seconds and a client-side curl timeout of 125 seconds.
 curl --max-time 125 \
   -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "X-Server-Timeout: 120" \
   -d '{
   "contents": [{
     "parts":[{"text": "Summarize the latest research on quantum computing."}]
   }],
   "service_tier": "flex"
 }'
```

### درنگ‌های سراسری

اگر می‌خواهید همه تماس‌های «میانای برنامه‌سازی کاربردی» که ازطریق نمونه `genai.Client` خاصی (فقط کتابخانه‌های کارخواه) برقرار می‌شوند زمان اتمام پیش‌فرض داشته باشند، می‌توانید این را هنگام مقداردهی اولیه کارخواه بااستفاده از `http_options` و `genai.types.HttpOptions` پیکربندی کنید.

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
        model="gemini-3.8-flash",
        contents="Summarize the history of AI development since 2000.",
        config={"service_tier": "flex"},
    )
    print(response.text)

    # A per-request timeout will *override* the global timeout for that specific call.
    shorter_timeout = 30000
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.8-flash",
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
            model: "gemini-3.8-flash",
            contents: "Summarize the history of AI development since 2000.",
            config: { serviceTier: "flex" },
        });
        console.log(response1.text());

        // A per-request timeout will *override* the global timeout for that specific call.
        const shorterTimeout = 30000;
        const response2 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.8-flash",
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

### رفتن

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

     model := client.GenerativeModel("gemini-3.8-flash")

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

## پیاده‌سازی تلاش‌های مجدد

چون Flex قابل‌حذف است و با خطاهای ۵۰۳ ناموفق می‌شود، در اینجا نمونه‌ای از
پیاده‌سازی اختیاری منطق تکرار مجدد برای ادامه دادن با درخواست‌های ناموفق ارائه شده است:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model="gemini-3.8-flash",
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
                    model="gemini-3.8-flash",
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
         model: "gemini-3.8-flash",
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
           model: "gemini-3.8-flash",
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

### رفتن

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
     modelName := "gemini-3.8-flash"
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

## قیمت‌گذاری

قیمت استنتاج انعطاف‌پذیر ۵۰٪ قیمت [میانای برنامه‌سازی کاربردی استاندارد](https://ai.google.dev/gemini-api/docs/pricing?hl=fa) است و براساس هر نمانه صورت‌حساب می‌شود.

## مدل‌های پشتیبانی‌شده

مدل‌های زیر از استنتاج انعطاف‌پذیر پشتیبانی می‌کنند:

| مدل | استنتاج انعطاف‌پذیر |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=fa) | ✔️ |
| [‫Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=fa) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=fa) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=fa) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fa) | ✔️ |
| [پیش‌نمایش Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fa) | ✔️ |
| [پیش‌نمایش Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=fa) | ✔️ |
| [پیش‌دید تصویر Gemini 3 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=fa) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=fa) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=fa) | ✔️ |
| [تصویر Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=fa) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=fa) | ✔️ |

## قدم بعدی چیست

درباره سایر گزینه‌های [استنباط و بهینه‌سازی](https://ai.google.dev/gemini-api/docs/optimization?hl=fa) Gemini بخوانید:

- [استنتاج اولویت](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fa) برای تأخیر بسیار کم.
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=fa) برای پردازش ناهمزمان در عرض ۲۴ ساعت.
- [ذخیره‌سازی بافت در حافظه نهان](https://ai.google.dev/gemini-api/docs/caching?hl=fa) برای کاهش هزینه توکن ورودی.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-13 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-13 به‌وقت ساعت هماهنگ جهانی."],[],[]]
