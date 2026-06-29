---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=tr
fetched_at: 2026-06-29T05:33:26.905379+00:00
title: "Google Arama temeli \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Google Arama temeli

Google Arama ile Temellendirme, Gemini modelini gerçek zamanlı web içeriğine bağlar ve tüm dillerde kullanılabilir. Bu sayede Gemini, son güncel bilgi tarihinin ötesinde daha doğru yanıtlar verebilir ve doğrulanabilir kaynaklardan alıntı yapabilir.

Temellendirme, aşağıdaki işlemleri yapabilen uygulamalar oluşturmanıza yardımcı olur:

- **Doğruluğu artırma:** Yanıtları gerçek dünyadaki bilgilere dayandırarak model halüsinasyonlarını azaltın.
- **Anlık bilgilere erişme:** Yakın zamandaki olaylar ve konularla ilgili soruları yanıtlama
- **Alıntı ekleyin:** Modelin iddialarının kaynaklarını göstererek kullanıcıların güvenini kazanın.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## Google Arama ile temellendirme nasıl çalışır?

`google_search` aracını etkinleştirdiğinizde model, bilgi arama, işleme ve alıntı yapma işlemlerinin tüm iş akışını otomatik olarak gerçekleştirir.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=tr)

1. **Kullanıcı istemi:** Uygulamanız, kullanıcının istemini `google_search` aracı etkinleştirilmiş şekilde Gemini API'ye gönderiyor.
2. **İstem Analizi:** Model, istemi analiz eder ve Google Arama'nın yanıtı iyileştirip iyileştiremeyeceğini belirler.
3. **Google Arama:** Gerekirse model, bir veya daha fazla arama sorgusunu otomatik olarak oluşturup yürütür.
4. **Arama sonuçlarını işleme:** Model, arama sonuçlarını işler, bilgileri sentezler ve bir yanıt oluşturur.
5. **Temellendirilmiş Yanıt:** API, arama sonuçlarına dayalı, son ve kullanıcı dostu bir yanıt döndürür. Bu yanıtta, alıntıları içeren satır içi `annotations` ile modelin metin yanıtı, arama sorgularını ve arama önerilerini içeren `google_search_call` ve `google_search_result` adımları yer alır.

## Temellendirme yanıtını anlama

Yanıt başarıyla temellendirildiğinde modelin metin çıkışı, metin içeriği bloğunda doğrudan satır içi `annotations` içerir. Bu ek açıklamalar, yanıtın bölümlerini kaynaklarına bağlayan alıntı bilgileri sağlar.

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

Yanıtın temel alanları:

- `google_search_call` : Modelin yürüttüğü arama `queries` içerir.
- `google_search_result` : Arama önerilerini kullanıcı arayüzünüzde oluşturmak için kullanılan bir HTML snippet'i olan `search_suggestions` içerir. Kullanımla ilgili tüm şartlar [Hizmet Şartları](https://ai.google.dev/gemini-api/terms?hl=tr#grounding-with-google-search)'nda ayrıntılı olarak açıklanmıştır.
- `text` ile `annotations` : Modelin satır içi alıntılarla sentezlenmiş yanıtı. Her `url_citation` ek açıklaması, bir metin segmentini (`start_index` ve `end_index` ile tanımlanır) bir kaynak URL'ye bağlar. Bu, satır içi alıntı oluşturmanın anahtarıdır.

Google Arama ile temellendirme, yanıtları hem herkese açık web verileri hem de sağladığınız belirli URL'lerle temellendirmek için [URL bağlam aracı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) ile birlikte de kullanılabilir.

## Satır içi alıntılarla kaynakları atfetme

API, metin içerik bloğunda satır içi `url_citation` ek açıklamalar döndürerek kaynakları kullanıcı arayüzünüzde nasıl göstereceğiniz konusunda size tam kontrol sağlar.
Her ek açıklama, metnin hangi bölümüne atıfta bulunduğunu belirlemek için `start_index` ve `end_index` içerir. Bunları nasıl ayıklayıp görüntüleyeceğinizi öğrenin.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

Çıktıda, metin ve alıntıları gösterilir:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## Fiyatlandırma

Gemini 3 ile Google Arama'yı Temellendirme özelliğini kullandığınızda projeniz, modelin yürütmeye karar verdiği her arama sorgusu için faturalandırılır. Model, tek bir isteme yanıt vermek için birden fazla arama sorgusu yürütmeye karar verirse (örneğin, aynı API çağrısında `"UEFA Euro 2024 winner"` ve `"Spain vs England Euro 2024 final
score"` için arama yaparsa) bu, söz konusu istek için aracın iki faturalandırılabilir kullanımı olarak sayılır. Faturalandırma amacıyla, benzersiz sorguları sayarken boş web arama sorgularını dikkate almayız. Bu faturalandırma modeli yalnızca Gemini 3 modelleri için geçerlidir. Gemini 2.5 veya daha eski modellerle arama temellendirmeyi kullandığınızda projeniz istem başına faturalandırılır.

Ayrıntılı fiyatlandırma bilgileri için [Gemini API fiyatlandırma sayfasını](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) inceleyin.

## Desteklenen modeller

Tüm özellikleri [modele genel bakış](https://ai.google.dev/gemini-api/docs/models?hl=tr) sayfasında bulabilirsiniz.

| Model | Google Arama ile Temellendirme |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash Image Önizlemesi | ✔️ |
| Gemini 3.1 Pro Önizlemesi | ✔️ |
| Gemini 3 Pro Görüntü Önizlemesi | ✔️ |
| Gemini 3 Flash Önizlemesi | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Desteklenen araç kombinasyonları

Daha karmaşık kullanım alanlarını desteklemek için Google Arama ile Temellendirme'yi [kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) ve [URL bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) gibi diğer araçlarla birlikte kullanabilirsiniz.

Gemini 3 modelleri, yerleşik araçların (ör. Google Arama ile Temellendirme) özel araçlarla (işlev çağrısı) birlikte kullanılmasını destekler. [Araç kombinasyonları](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) sayfasından daha fazla bilgi edinin.

## Sırada ne var?

- [İşlev Çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) gibi diğer araçlar hakkında bilgi edinin.
- [URL bağlamı aracını](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) kullanarak istemleri belirli URL'lerle nasıl zenginleştireceğinizi öğrenin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-22 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-22 UTC."],[],[]]
