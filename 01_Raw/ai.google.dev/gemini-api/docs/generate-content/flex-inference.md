---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/flex-inference?hl=tr
fetched_at: 2026-06-29T05:32:23.407342+00:00
title: "Flex \u00e7\u0131kar\u0131m\u0131 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Flex çıkarımı

Açıklama: Esnek çıkarım katmanıyla maliyetleri nasıl optimize edeceğinizi öğrenin

Gemini Flex API, değişken gecikme süresi ve en iyi çaba ile kullanılabilirlik karşılığında standart ücretlere kıyasla% 50 maliyet düşüşü sunan bir çıkarım katmanıdır. Bu API, eşzamanlı işleme gerektiren ancak standart API'nin gerçek zamanlı performansına ihtiyaç duymayan, gecikmeye toleranslı iş yükleri için tasarlanmıştır.

## Flex nasıl kullanılır?

Esnek katmanı kullanmak için istek gövdesinde `service_tier` değerini `flex` olarak belirtin. Bu alan atlanırsa istekler varsayılan olarak standart katmanı kullanır.

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

## Flex çıkarımının işleyiş şekli

Gemini Flex çıkarımı, standart API ile [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr)'nin 24 saatlik yanıt süresi arasındaki boşluğu kapatır. Arka plan görevleri ve sıralı iş akışları için uygun maliyetli bir çözüm sunmak üzere yoğun olmayan zamanlardaki, "kullanılmayan" bilgi işlem kapasitesinden yararlanır.

| Özellik | Yaratıcılığınızı | Öncelik | Standart | Toplu |
| --- | --- | --- | --- | --- |
| **Fiyatlandırma** | %50 indirim | Standart'tan% 75-100 daha fazla | Tam fiyat | %50 indirim |
| **Gecikme** | Dakikalar (1-15 dakika hedef) | Düşük (saniye) | Saniyeden dakikaya | En fazla 24 saat |
| **Güvenilirlik** | En iyi sonuç (Sheddable) | Yüksek (tüy dökmeyen) | Yüksek / Biraz yüksek | Yüksek (aktarım hızı için) |
| **Arayüz** | Eşzamanlı | Eşzamanlı | Eşzamanlı | Eşzamansız |

### Temel avantajlar

- **Maliyet verimliliği**: Üretim dışı değerlendirmeler, arka plan aracıları ve veri zenginleştirme için önemli ölçüde tasarruf sağlar.
- **Kolay**: Toplu nesneleri, iş kimliklerini veya yoklamayı yönetmeniz gerekmez. Mevcut isteklerinize tek bir parametre eklemeniz yeterlidir.
- **Eşzamanlı iş akışları**: Bir sonraki isteğin bir öncekinin çıkışına bağlı olduğu sıralı API zincirleri için idealdir. Bu nedenle, aracı iş akışları için toplu işlerden daha esnektir.

### Kullanım alanları

- **Çevrimdışı değerlendirmeler**: "LLM-as-a-judge" regresyon testleri veya skor tabloları çalıştırma.
- **Arka plan aracıları**: CRM güncellemeleri, profil oluşturma veya içerik denetleme gibi sıralı görevler. Bu görevlerde birkaç dakikalık gecikme kabul edilebilir.
- **Bütçe kısıtlamalı araştırma**: Sınırlı bir bütçeyle yüksek jeton hacmi gerektiren akademik deneyler.

### Hız sınırları

Esnek çıkarım trafiği, genel [hız sınırlarınıza](https://aistudio.google.com/rate-limit?hl=tr) dahil edilir. [Toplu İşlem API'si](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr) gibi genişletilmiş hız sınırları sunmaz.

### Sökülebilir kapasite

Esnek trafik daha düşük öncelikli olarak değerlendirilir. Standart trafikte ani bir artış olursa yüksek öncelikli kullanıcılar için kapasite sağlamak amacıyla esnek istekler öncelikli olarak işlenebilir veya çıkarılabilir. Yüksek öncelikli çıkarım arıyorsanız [Öncelikli çıkarım](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr) bölümüne bakın.

### Hata kodları

Esnek kapasite kullanılamadığında veya sistemde yoğunluk olduğunda API, standart hata kodlarını döndürür:

- **503 Hizmet Kullanılamıyor**: Sistem şu anda tam kapasiteyle çalışıyor.
- **429 Çok Fazla İstek Var**: Sıklık sınırları veya kaynak tükenmesi.

### Müşterinin sorumluluğu

- **Sunucu tarafında yedekleme yok**: Beklenmedik ücretleri önlemek için Flex kapasitesi doluysa sistem, Flex isteğini otomatik olarak Standart katmana yükseltmez.
- **Yeniden denemeler**: Eksponansiyel geri yükleme ile kendi istemci tarafı yeniden deneme mantığınızı uygulamanız gerekir.
- **Zaman aşımları**: Esnek istekler bir kuyrukta bekleyebileceğinden, bağlantının erken kapanmasını önlemek için istemci tarafı zaman aşımlarını 10 dakika veya daha uzun bir süreye çıkarmanızı öneririz.

## Zaman aşımı aralıklarını ayarlama

REST API ve istemci kitaplıkları için istek başına zaman aşımlarını, istemci kitaplıklarını kullanırken ise yalnızca genel zaman aşımlarını yapılandırabilirsiniz.

İstemci tarafı zaman aşımınızın her zaman amaçlanan sunucu bekleme süresini (ör. Flex bekleme sıraları için 600 saniye ve üzeri) kapsadığından emin olun. SDK'lar zaman aşımı değerlerini milisaniye cinsinden bekler.

### İstek başına zaman aşımı

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

REST çağrıları yaparken HTTP üstbilgileri ve `curl` seçeneklerinin bir kombinasyonunu kullanarak zaman aşımlarını kontrol edebilirsiniz:

- **`X-Server-Timeout` üstbilgi (sunucu tarafı zaman aşımı)**: Bu üstbilgi, Gemini API sunucusu için tercih edilen bir zaman aşımı süresi (varsayılan 600 saniye) önerir. Sunucu bu isteğe uymaya çalışır ancak bu garanti edilmez. Değer saniye cinsinden olmalıdır.
- **`curl` içinde `--max-time` (İstemci Tarafı Zaman Aşımı)**: `curl --max-time
  <seconds>` seçeneği, `curl`'nin tüm işlemin tamamlanmasını bekleyeceği toplam süreye (saniye cinsinden) kesin bir sınır koyar. Bu, istemci tarafı bir güvenlik önlemidir.

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

### Global zaman aşımları

Belirli bir `genai.Client` örneği (yalnızca istemci kitaplıkları) üzerinden yapılan tüm API çağrılarının varsayılan bir zaman aşımı olmasını istiyorsanız istemciyi `http_options` ve `genai.types.HttpOptions` kullanarak başlatırken bunu yapılandırabilirsiniz.

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

## Yeniden denemeleri uygulama

Flex, 503 hatalarıyla başarısız olabilen bir katman olduğundan başarısız isteklerle devam etmek için isteğe bağlı olarak yeniden deneme mantığını uygulamanın bir örneğini aşağıda bulabilirsiniz:

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

## Fiyatlandırma

Esnek çıkarım, [standart API](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) fiyatının% 50'si üzerinden fiyatlandırılır ve jeton başına faturalandırılır.

## Desteklenen modeller

Aşağıdaki modellerde Flex çıkarımı desteklenir:

| Model | Esnek çıkarım |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=tr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr) | ✔️ |
| [Gemini 3.1 Pro Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr) | ✔️ |
| [Gemini 3 Flash Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=tr) | ✔️ |
| [Gemini 3 Pro ile Görüntü Önizleme](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=tr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=tr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=tr) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=tr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=tr) | ✔️ |

## Sırada ne var?

Gemini'ın diğer [çıkarım ve optimizasyon](https://ai.google.dev/gemini-api/docs/optimization?hl=tr) seçenekleri hakkında bilgi edinin:

- Ultra düşük gecikme için [öncelikli çıkarım](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr).
- 24 saat içinde eşzamansız işleme için [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr).
- Giriş jetonu maliyetlerini azaltmak için [bağlam önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr).

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-23 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-23 UTC."],[],[]]
