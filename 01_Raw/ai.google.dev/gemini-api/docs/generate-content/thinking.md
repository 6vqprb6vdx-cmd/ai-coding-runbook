---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=tr
fetched_at: 2026-07-27T04:44:23.756659+00:00
title: "Gemini d\u00fc\u015f\u00fcncesi \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini düşüncesi

[Gemini 3 ve 2.5 serisi modeller](https://ai.google.dev/gemini-api/docs/models?hl=tr), akıl yürütme ve çok adımlı planlama yeteneklerini önemli ölçüde geliştiren dahili bir "düşünme süreci" kullanır. Bu sayede kodlama, ileri matematik ve veri analizi gibi karmaşık görevlerde oldukça etkili olurlar.

Bu kılavuzda, Gemini API'yi kullanarak Gemini'ın düşünme özellikleriyle nasıl çalışacağınız gösterilmektedir.

## Düşünerek içerik üretme

Düşünme modeliyle istek başlatmak, diğer tüm içerik oluşturma isteklerine benzer. Aradaki temel fark, aşağıdaki [metin oluşturma](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr#text-input) örneğinde gösterildiği gibi, `model` alanında [düşünme desteği olan modellerden](#supported-models) birinin belirtilmesidir:

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.5-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## Düşünce özetleri

Düşünce özetleri, modelin ham düşüncelerinin özetlenmiş versiyonlarıdır ve modelin dahili akıl yürütme süreci hakkında bilgiler sunar. Düşünce düzeylerinin ve bütçelerin, modelin ham düşünceleri için geçerli olduğunu, düşünce özetleri için geçerli olmadığını unutmayın.

İstek yapılandırmanızda `includeThoughts` değerini `true` olarak ayarlayarak düşünce özetlerini etkinleştirebilirsiniz. Daha sonra, `response` parametresinin `parts` değerlerini yineleyerek ve `thought` boole değerini kontrol ederek özete erişebilirsiniz.

Aşağıda, akış olmadan düşünce özetlerinin nasıl etkinleştirileceğini ve alınacağını gösteren bir örnek verilmiştir. Bu örnek, yanıtla birlikte tek bir nihai düşünce özeti döndürür:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.5-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

Aşağıda, akışla düşünme özelliğinin kullanıldığı ve oluşturma sırasında kademeli özetler döndüren bir örnek verilmiştir:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.5-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
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
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.5-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## Düşünceleri kontrol etme

Gemini modelleri, varsayılan olarak dinamik düşünme özelliğini kullanır ve kullanıcının isteğinin karmaşıklığına göre akıl yürütme çabasını otomatik olarak ayarlar.
Ancak belirli gecikme kısıtlamalarınız varsa veya modelin normalden daha derin bir muhakeme yapmasını istiyorsanız düşünme davranışını kontrol etmek için isteğe bağlı olarak parametreleri kullanabilirsiniz.

### Düşünme düzeyleri (Gemini 3)

Gemini 3 modelleri ve sonraki sürümler için önerilen `thinkingLevel` parametresi, akıl yürütme davranışını kontrol etmenizi sağlar.

Aşağıdaki tabloda her model türü için `thinkingLevel` ayarları ayrıntılı olarak açıklanmaktadır:

| Düşünme Düzeyi | Gemini 3.5 Flash | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3.1 Flash-Lite Görüntüsü | Gemini 3 Flash | Açıklama |
| --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | Destekleniyor | Desteklenmiyor | Destekleniyor (Varsayılan) | Destekleniyor (Varsayılan) | Destekleniyor | Çoğu sorgu için "düşünme yok" ayarıyla eşleşir. `minimal`'nın düşünme özelliğinin devre dışı olduğunu garanti etmediğini unutmayın. Model, karmaşık görevler için çok az gerekçe sunabilir. |
| **`low`** | Destekleniyor | Destekleniyor | Destekleniyor | Desteklenmiyor | Destekleniyor | Gecikmeyi ve maliyeti en aza indirir. |
| **`medium`** | Destekleniyor (Varsayılan) | Destekleniyor | Destekleniyor | Desteklenmiyor | Destekleniyor | Çoğu görev için dengeli düşünme |
| **`high`** | Desteklenir (Dinamik) | Destekleniyor (Varsayılan, Dinamik) | Desteklenir (Dinamik) | Desteklenir (Dinamik) | Destekleniyor (Varsayılan, Dinamik) | Akıl yürütme derinliğini en üst düzeye çıkarır. Modelin ilk (düşünme içermeyen) çıkış jetonuna ulaşması önemli ölçüde daha uzun sürebilir ancak çıkış daha dikkatli bir şekilde gerekçelendirilir. |

Aşağıdaki örnekte, düşünme düzeyinin nasıl ayarlanacağı gösterilmektedir.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Gemini 3.1 Pro'da düşünme özelliğini devre dışı bırakamazsınız. Gemini 3 Flash ve Flash-Lite da tam düşünme özelliğini desteklemez.
Düşünme seviyesi belirtmezseniz Gemini, Gemini 3 modellerinin varsayılan düşünme seviyesini (ör. Gemini 3.1 Pro için `"high"`, Gemini 3.5 Flash için `"medium"`) kullanır.

Gemini 2.5 serisi modeller `thinkingLevel` dosya türünü desteklemez. Bunun yerine `thinkingBudget` dosya türünü kullanın.

### Düşünme bütçeleri

Gemini 2.5 serisiyle kullanıma sunulan `thinkingBudget` parametresi, akıl yürütme için kullanılacak düşünme parçalarının sayısı konusunda modele yol gösterir.

Aşağıda her model türü için `thinkingBudget` yapılandırma ayrıntıları verilmiştir.
`thinkingBudget` değerini 0 olarak ayarlayarak düşünme özelliğini devre dışı bırakabilirsiniz.
`thinkingBudget` değerini -1 olarak ayarlamak **dinamik düşünme** özelliğini etkinleştirir. Bu durumda model, bütçeyi isteğin karmaşıklığına göre ayarlar.

| Model | Varsayılan ayar (Düşünme bütçesi ayarlanmamış) | Aralık | Düşünmeyi devre dışı bırakma | Dinamik düşünmeyi etkinleştirme |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Dinamik düşünme | `128` - `32768` | Geçersiz: Düşünme devre dışı bırakılamaz. | `thinkingBudget = -1` (Varsayılan) |
| **2.5 Flash** | Dinamik düşünme | `0` - `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Varsayılan) |
| **2.5 Flash Önizlemesi** | Dinamik düşünme | `0` - `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Varsayılan) |
| **2.5 Flash Lite** | Model düşünmüyor | `512` - `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite Önizlemesi** | Model düşünmüyor | `512` - `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 Önizlemesi** | Dinamik düşünme | `0` - `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Varsayılan) |
| **2.5 Flash Live Native Audio Preview (09-2025)** | Dinamik düşünme | `0` - `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Varsayılan) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

İstemlere bağlı olarak model, jeton bütçesini aşabilir veya bütçenin altında kalabilir.

## Düşünce imzaları

[düşünce imzalarını manuel olarak yönetmeniz](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr#thought-signatures) gerekir.

Gemini API durum bilgisi içermediğinden model, her API isteğini bağımsız olarak ele alır ve çok adımlı etkileşimlerde önceki adımlardaki düşünce bağlamına erişemez.

Gemini, çok turlu etkileşimlerde düşünce bağlamının korunmasını sağlamak için düşünce imzaları döndürür. Düşünce imzaları, modelin dahili düşünce sürecinin şifrelenmiş temsilleridir.

- **Gemini 2.5 modelleri**, düşünme etkinleştirildiğinde ve istek [işlev çağrısı](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr#thinking), özellikle de [işlev bildirimleri](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr#step-2) içerdiğinde düşünce imzaları döndürür.
- **Gemini 3 modelleri**, her tür [parça](https://ai.google.dev/api/caching?hl=tr#Part) için düşünce imzaları döndürebilir.
  Tüm imzaları her zaman alındığı şekilde geri iletmenizi öneririz ancak işlev çağrısı imzaları için bu *zorunludur*. Daha fazla bilgi için [Thought Signatures](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=tr) (Düşünce İmzaları) sayfasını inceleyin.

İşlev çağrısıyla ilgili dikkate alınması gereken diğer kullanım sınırlamaları şunlardır:

- İmzalar, yanıttaki diğer bölümlerden (ör. işlev çağrısı veya metin bölümleri) döndürülür.
  Sonraki dönüşlerde tüm parçalarıyla birlikte [yanıtın tamamını modele geri gönderin](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr#step-4).
- İmzalı bölümleri birleştirmeyin.
- Bir bölümü imzalı, diğer bölümü imzasız olarak birleştirmeyin.

## Fiyatlandırma

Düşünme etkinleştirildiğinde yanıt fiyatı, çıkış jetonlarının ve düşünme jetonlarının toplamıdır. Oluşturulan düşünme jetonlarının toplam sayısını `thoughtsTokenCount` alanından alabilirsiniz.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

Düşünme modelleri, nihai yanıtın kalitesini artırmak için tam düşünceler üretir ve ardından düşünce süreci hakkında bilgi vermek için [özetler](#summaries) oluşturur. Bu nedenle, API'den yalnızca özet çıktısı alınmasına rağmen fiyatlandırma, modelin özet oluşturmak için üretmesi gereken tam düşünce jetonlarına göre yapılır.

Jetonlar hakkında daha fazla bilgiyi [Jeton sayımı](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) rehberinde bulabilirsiniz.

## En iyi uygulamalar

Bu bölümde, düşünce modellerini verimli bir şekilde kullanmayla ilgili bazı bilgiler yer almaktadır.
Her zaman olduğu gibi, [istem yazma kılavuzumuza ve en iyi uygulamalarımıza](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=tr) uyarak en iyi sonuçları elde edebilirsiniz.

### Hata ayıklama ve yönlendirme

- **Akıl yürütmeyi inceleme**: Düşünce modellerinden beklediğiniz yanıtı alamadığınızda Gemini'ın düşünce özetlerini dikkatlice analiz etmek faydalı olabilir.
  Görevi nasıl parçaladığını ve sonuca nasıl ulaştığını görebilir, bu bilgileri kullanarak doğru sonuçlara ulaşmak için düzeltmeler yapabilirsiniz.
- **Mantıkta Rehberlik Sağlama**: Özellikle uzun bir çıktı almak istiyorsanız isteminizde rehberlik sağlayarak modelin [düşünme miktarını](#set-budget) sınırlayabilirsiniz. Bu sayede, yanıtınız için daha fazla jeton çıktısı ayırabilirsiniz.

### Görevin karmaşıklığı

- **Kolay Görevler (Düşünme devre dışı olabilir):** Bilgi alma veya sınıflandırma gibi karmaşık akıl yürütme gerektirmeyen basit isteklerde düşünme gerekli değildir. Örnekler:
  - "DeepMind nerede kuruldu?"
  - "Bu e-postada toplantı isteğinde mi bulunuluyor yoksa sadece bilgi mi veriliyor?"
- **Orta Görevler (Varsayılan/Biraz Düşünme):** Birçok yaygın istek, adım adım işleme veya daha derin bir anlayıştan yararlanır. Gemini, aşağıdaki gibi görevlerde düşünme yeteneğini esnek bir şekilde kullanabilir:
  - Fotosentez ve büyüme arasında benzerlik kur.
  - Elektrikli arabalar ile hibrit arabaları karşılaştırın ve aralarındaki farkları belirtin.
- **Zor Görevler (Maksimum Düşünme Kapasitesi):** Karmaşık matematik problemlerini çözme veya kodlama görevleri gibi gerçekten zorlu görevler için yüksek bir düşünme bütçesi ayarlamanızı öneririz. Bu tür görevler, modelin tam akıl yürütme ve planlama yeteneklerini kullanmasını gerektirir. Bu görevler genellikle yanıt vermeden önce birçok dahili adım içerir. Örnekler:
  - AIME 2025'teki 1. problemi çözün: 17b'nin 97b'nin bir böleni olduğu tüm b > 9 tam sayı tabanlarının toplamını bulun.
  - Kullanıcı kimlik doğrulaması da dahil olmak üzere gerçek zamanlı borsa verilerini görselleştiren bir web uygulaması için Python kodu yaz. Mümkün olduğunca verimli hale getirin.

## Desteklenen modeller, araçlar ve özellikler

Düşünme özellikleri, tüm 3 ve 2.5 serisi modellerde desteklenir.
Tüm model özelliklerini [modele genel bakış](https://ai.google.dev/gemini-api/docs/models?hl=tr) sayfasında bulabilirsiniz.

Düşünen modeller, Gemini'ın tüm araçları ve özellikleriyle çalışır. Bu sayede modeller, harici sistemlerle etkileşime geçebilir, kod çalıştırabilir veya anlık bilgilere erişebilir. Ayrıca, sonuçları muhakeme ve nihai yanıtlarına dahil edebilir.

[Thinking cookbook][Colab] içinde, araçları düşünme modelleriyle kullanma örneklerini deneyebilirsiniz.

## Sırada ne var?

- Düşünme kapsamı, [OpenAI Uyumluluğu](https://ai.google.dev/gemini-api/docs/openai?hl=tr#thinking) kılavuzumuzda yer almaktadır.

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-07 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-07 UTC."],[],[]]
