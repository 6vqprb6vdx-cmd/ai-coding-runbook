---
source_url: https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=tr
fetched_at: 2026-05-11T12:31:13.201302+00:00
title: "Google Haritalar ile temellendirme \u00a0|\u00a0 Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Google Haritalar ile temellendirme

Google Haritalar ile temellendirme, Gemini'ın üretken özelliklerini Google Haritalar'ın zengin, doğru ve güncel verileriyle birleştirir. Bu özellik, geliştiricilerin konuma duyarlı işlevleri uygulamalarına kolayca dahil etmelerini sağlar. Kullanıcı sorgusu Haritalar verileriyle ilgili bir bağlama sahip olduğunda Gemini modeli, kullanıcının belirttiği konum veya genel alanla alakalı, olgusal olarak doğru ve güncel yanıtlar sağlamak için Google Haritalar'dan yararlanır.

- **Doğru ve konuma duyarlı yanıtlar:** Coğrafi olarak belirli sorgular için Google Haritalar'ın kapsamlı ve güncel verilerinden yararlanın.
- **Gelişmiş kişiselleştirme:** Kullanıcı tarafından sağlanan konumlara göre önerileri ve bilgileri uyarlayın.
- **Bağlamsal bilgiler ve widget'lar:** Oluşturulan içerikle birlikte etkileşimli Google Haritalar widget'larını oluşturmak için bağlam jetonları.

## Başlayın

Bu örnekte, kullanıcı sorgularına doğru ve konuma duyarlı yanıtlar vermek için Google Haritalar ile Temellendirme'yi uygulamanıza nasıl entegre edeceğiniz gösterilmektedir. İstemde, isteğe bağlı kullanıcı konumuyla birlikte yerel öneriler isteniyor. Bu sayede Gemini modeli, Google Haritalar verilerini kullanabiliyor.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Google Haritalar ile Temellendirme'nin işleyiş şekli

Google Haritalar ile Temellendirme, temellendirme kaynağı olarak Maps API'sini kullanarak Gemini API'yi Google Coğrafi Ekosistemi ile entegre eder. Kullanıcının sorgusu coğrafi bağlam içerdiğinde Gemini modeli, Google Haritalar ile Temellendirme aracını çağırabilir. Model daha sonra, sağlanan konumla alakalı Google Haritalar verilerine dayalı yanıtlar oluşturabilir.

Bu süreç genellikle şunları içerir:

1. **Kullanıcı sorgusu:** Bir kullanıcı, uygulamanıza coğrafi bağlam da içerebilecek bir sorgu gönderir (ör. "yakınımdaki kafeler", "San Francisco'daki müzeler").
2. **Araç çağırma:** Coğrafi amacı algılayan Gemini modeli, Google Haritalar ile Temellendirme aracını çağırır. Bu araç, isteğe bağlı olarak kullanıcının `latitude` ve `longitude` ile birlikte sağlanabilir. Bu araç, metin tabanlı bir arama aracıdır ve Haritalar'da arama yapmaya benzer şekilde çalışır. Yerel sorgularda ("yakınımdaki") koordinatlar kullanılırken belirli veya yerel olmayan sorguların açık konumdan etkilenmesi olası değildir.
3. **Veri alma:** Google Haritalar ile Temellendirme hizmeti, Google Haritalar'da alakalı bilgiler (ör. yerler, yorumlar, fotoğraflar, adresler, çalışma saatleri) için sorgu gönderir.
4. **Temellendirilmiş üretim:** Alınan Haritalar verileri, Gemini modelinin yanıtını bilgilendirmek için kullanılır. Bu sayede, yanıtın olgusal doğruluğu ve alaka düzeyi sağlanır.
5. **Yanıt ve ek açıklamalar:** Model, Google Haritalar kaynaklarına bağlantı veren satır içi ek açıklamalar içeren bir metin yanıtı döndürür. Bu sayede geliştiriciler alıntıları gösterebilir ve isteğe bağlı olarak bağlamsal bir Google Haritalar widget'ı oluşturabilir.

## Google Haritalar ile Temellendirme neden ve ne zaman kullanılmalıdır?

Google Haritalar ile temellendirme, doğru, güncel ve konuma özel bilgiler gerektiren uygulamalar için idealdir. Dünya genelinde 250 milyondan fazla yerin bulunduğu Google Haritalar'ın kapsamlı veritabanı tarafından desteklenen alakalı ve kişiselleştirilmiş içerikler sunarak kullanıcı deneyimini iyileştirir.

Uygulamanızın aşağıdaki durumlarda Google Haritalar ile Temellendirme'yi kullanması gerekir:

- Coğrafi konuma özel sorulara eksiksiz ve doğru yanıtlar verin.
- Sohbete dayalı gezi planlayıcıları ve yerel rehberler oluşturun.
- Konuma ve kullanıcı tercihlerine (ör. restoranlar veya mağazalar) göre ilgi çekici yerler önerin.
- Sosyal medya, perakende veya yemek teslimatı hizmetleri için konuma duyarlı deneyimler oluşturun.

Google Haritalar ile temellendirme, "yakınımdaki en iyi kahve dükkanını" bulma veya yol tarifi alma gibi yakınlık ve güncel gerçek verilerin kritik olduğu kullanım alanlarında mükemmeldir.

## Kullanım alanları

Google Haritalar ile temellendirme, konuma duyarlı çeşitli kullanım alanlarını destekler.

### Yere özgü soruları yanıtlama

Google kullanıcı yorumlarına ve diğer Haritalar verilerine dayalı yanıtlar almak için belirli bir yer hakkında ayrıntılı sorular sorun.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Konuma dayalı kişiselleştirme sağlama

Kullanıcının tercihlerine ve belirli bir coğrafi bölgeye göre uyarlanmış öneriler alın.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Seyahat planı oluşturma konusunda yardım

Yol tarifleri ve çeşitli yerler hakkında bilgiler içeren çok günlük planlar oluşturun. Bu planlar, seyahat uygulamaları için idealdir.

### Python

```
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476,
        "enable_widget": True
    }]
)
# ... code to process response and widget token
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476,
      enable_widget: true
    }]
  });
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476,
      "enable_widget": true
    }]
  }'
```

## Hizmet kullanım şartları

Bu bölümde, Google Haritalar ile Temellendirme için hizmet kullanım şartları açıklanmaktadır.

### Kullanıcıyı Google Haritalar kaynaklarının kullanımı hakkında bilgilendirme

Her Google Haritalar'a dayalı sonuçta, `model_output` adımının her yanıtı destekleyen içerik bloklarında kaynak açıklamaları gösterilir. Aşağıdaki meta veriler döndürülür:

- kaynak URL
- ad

Google Haritalar ile Temellendirme'den elde edilen sonuçları sunarken ilişkili Google Haritalar kaynaklarını belirtmeniz ve kullanıcılarınızı aşağıdakiler hakkında bilgilendirmeniz gerekir:

- Google Haritalar kaynakları, kaynakların desteklediği oluşturulmuş içeriği hemen takip etmelidir. Bu oluşturulan içeriğe Google Haritalar'da Temellendirilmiş Sonuç da denir.
- Google Haritalar kaynakları, tek bir kullanıcı etkileşimi içinde görüntülenebilmelidir.

### Google Haritalar bağlantılarıyla Google Haritalar kaynaklarını görüntüleme

Her kaynak açıklaması için aşağıdaki koşullara uygun bir bağlantı önizlemesi oluşturulmalıdır:

- Google Haritalar metin [atfetme yönergelerine](#maps-attribution-guidelines) uyarak her kaynağı Google Haritalar'a atfedin.
- Yanıtta belirtilen kaynak adını gösterir.
- Açıklamadaki `url` simgesini kullanarak kaynağa bağlantı verin.

### Google Haritalar metin atıfı yönergeleri

Metinde kaynakları Google Haritalar'a atfederken aşağıdaki yönergelere uyun:

- Google Haritalar metnini hiçbir şekilde değiştirmeyin:
  - Google Haritalar'ın büyük harf kullanımını değiştirmeyin.
  - Google Haritalar'ı birden fazla satıra sarmayın.
  - Google Haritalar'ı başka bir dile yerelleştirmeyin.
  - HTML özelliğini translate="no" kullanarak tarayıcıların Google Haritalar'ı çevirmesini engelleyin.

Google Haritalar veri sağlayıcılarımız ve lisans şartları hakkında daha fazla bilgi için [Google Haritalar ve Google Earth yasal bildirimleri](https://www.google.com/help/legalnotices_maps/?hl=tr)'ne bakın.

## En iyi uygulamalar

- **Kullanıcı konumunu sağlama:** En alakalı ve kişiselleştirilmiş yanıtlar için kullanıcının konumu bilindiğinde `google_maps` aracı yapılandırmanıza her zaman `latitude` ve `longitude` değerlerini ekleyin.
- **Google Haritalar bağlamsal widget'ını oluşturun:** Bağlamsal widget, Gemini API yanıtında döndürülen ve Google Haritalar'daki görsel içerikleri oluşturmak için kullanılabilen bağlam jetonu `google_maps_widget_context_token` ile oluşturulur.
- **Son Kullanıcıları Bilgilendirin:** Özellikle araç etkinleştirildiğinde, Google Haritalar verilerinin sorgularını yanıtlamak için kullanıldığını son kullanıcılarınıza net bir şekilde bildirin.
- **Gerekmediğinde Kapatma:** Google Haritalar ile temellendirme özelliği varsayılan olarak kapalıdır. Performansı ve maliyeti optimize etmek için yalnızca sorgunun net bir coğrafi bağlamı olduğunda (`"tools": [{"type": "google_maps"}]`) etkinleştirin.

## Sınırlamalar

- Google Haritalar ile temellendirme şu anda yalnızca İngilizce istemleri ve yanıtları desteklemektedir.
- Bu araç bazı bölgelerde kullanılamayabilir.
- Sonuçlar, konum doğruluğuna ve kullanılabilir Haritalar verilerine göre değişebilir.
- **Coğrafi Kapsam:** Google Haritalar ile Temellendirme özelliği dünya genelinde kullanılabilir.
- **Varsayılan Durum:** Google Haritalar ile Temellendirme aracı varsayılan olarak devre dışıdır.
  Bu özelliği API isteklerinizde açıkça etkinleştirmeniz gerekir.

## Fiyatlandırma ve sıklık sınırları

Google Haritalar ile temellendirme fiyatlandırması sorgulara göre belirlenir. Geçerli ücret **25 ABD doları / 1.000 temellendirilmiş istem**'dir. Ücretsiz katmanda günde 500 istek kullanılabilir. Bir istek yalnızca istem başarıyla en az bir Google Haritalar temelli sonuç (ör. en az bir Google Haritalar kaynağı içeren sonuçlar) döndürdüğünde kotaya dahil edilir. Tek bir istekten Google Haritalar'a birden fazla sorgu gönderilirse bu, hız sınırına göre tek bir istek olarak sayılır.

Ayrıntılı fiyatlandırma bilgileri için [Gemini API fiyatlandırma sayfasına](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) bakın.

## Desteklenen modeller

Aşağıdaki modellerde Google Haritalar ile Temellendirme özelliği desteklenir:

| Model | Google Haritalar ile Temellendirme |
| --- | --- |
| [Gemini 3.1 Pro Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr) | ✔️ |
| [Gemini 3.1 Flash-Lite Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=tr) | ✔️ |
| [Gemini 3 Flash Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=tr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=tr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=tr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=tr) | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=tr) | ✔️ |

## Desteklenen araç kombinasyonları

Gemini 3 modelleri, yerleşik araçların (ör. Google Haritalar ile temellendirme) özel araçlarla (işlev çağrısı) birleştirilmesini destekler. [Araç kombinasyonları](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=tr) sayfasından daha fazla bilgi edinin.

## Sırada ne var?

- Diğer [kullanılabilir araçlar](https://ai.google.dev/gemini-api/docs/tools?hl=tr) hakkında bilgi edinin.
- Sorumlu yapay zekaya dair en iyi uygulamalar ve Gemini API'nin güvenlik filtreleri hakkında daha fazla bilgi edinmek için [Güvenlik ayarları kılavuzuna](https://ai.google.dev/gemini-api/docs/safety-settings?hl=tr) bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-09 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-09 UTC."],[],[]]
