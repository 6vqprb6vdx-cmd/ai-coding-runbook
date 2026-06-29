---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=tr
fetched_at: 2026-06-29T05:31:19.780628+00:00
title: "Medya \u00e7\u00f6z\u00fcn\u00fcrl\u00fc\u011f\u00fc \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Medya çözünürlüğü

`media_resolution` parametresi, medya girişleri için ayrılan **maksimum jeton sayısını** belirleyerek Gemini API'nin resim, video ve PDF belgeleri gibi medya girişlerini nasıl işleyeceğini kontrol eder. Bu sayede yanıt kalitesini gecikme ve maliyetle dengelemenizi sağlar. Farklı ayarlar, varsayılan değerler ve bunların jetonlarla nasıl eşleştiği hakkında bilgi edinmek için [Jeton sayıları](#token-counts) bölümüne bakın.

İsteğinizdeki (yalnızca Gemini 3) bağımsız medya nesneleri (içerik öğeleri) için medya çözünürlüğünü yapılandırabilirsiniz.

## İçerik öğesi başına medya çözünürlüğü (yalnızca Gemini 3)

Gemini 3, isteğinizdeki her bir medya nesnesi için medya çözünürlüğünü ayarlamanıza olanak tanır ve jeton kullanımında ayrıntılı optimizasyon sunar. Tek bir istekte çözünürlük düzeylerini karıştırabilirsiniz. Örneğin, karmaşık bir şema için yüksek çözünürlük, basit bir bağlamsal resim için düşük çözünürlük kullanabilirsiniz.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Kullanılabilir çözünürlük değerleri

Gemini API, medya çözünürlüğü için aşağıdaki düzeyleri tanımlar:

- `unspecified`: Varsayılan ayardır. Bu seviyenin jeton sayısı, Gemini 3 ile önceki Gemini modelleri arasında önemli ölçüde farklılık gösterir.
- `low`: Daha düşük jeton sayısı, daha hızlı işlem ve daha düşük maliyetle sonuçlanır ancak daha az ayrıntı içerir.
- `medium`: Ayrıntı, maliyet ve gecikme arasında bir denge.
- `high`: Gecikme ve maliyet artışı karşılığında, modelin çalışması için daha fazla ayrıntı sağlayan daha yüksek jeton sayısı.
- `ultra_high` (Yalnızca içerik öğesi başına): En yüksek jeton sayısıdır. [Bilgisayar kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr) gibi belirli kullanım alanları için gereklidir.

`high` seçeneğinin çoğu kullanım alanında optimum performans sağladığını unutmayın.

Bu seviyelerin her biri için oluşturulan jetonların tam sayısı hem **medya türüne** (resim, video, PDF) hem de **model sürümüne** bağlıdır.

## Jeton sayıları

Aşağıdaki tablolarda, her model ailesi için her `media_resolution` değeri ve medya türüne ait yaklaşık jeton sayıları özetlenmektedir.

**Gemini 3 modelleri**

| MediaResolution | Resim | Video | PDF |
| --- | --- | --- | --- |
| `unspecified` (Varsayılan) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + Doğal Metin |
| `medium` | 560 | 70 | 560 + Doğal Metin |
| `high` | 1120 | 280 | 1.120 + Yerel Metin |
| `ultra_high` | 2240 | Yok | Yok |

## Doğru çözünürlüğü seçme

- **Varsayılan (`unspecified`):** Varsayılanla başlayın. En yaygın kullanım alanlarında kalite, gecikme ve maliyet arasında iyi bir denge sağlamak için ayarlanmıştır.
- **`low`:** Maliyet ve gecikmenin öncelikli olduğu, ayrıntılı bilgilerin daha az önemli olduğu senaryolarda kullanılır.
- **`medium` / `high`:** Görev, medyada karmaşık ayrıntıların anlaşılmasını gerektirdiğinde çözünürlüğü artırın. Bu özellik genellikle karmaşık görsel analiz, grafik okuma veya yoğun belge anlama için gereklidir.
- **`ultra_high`**: Yalnızca içerik öğesi başına ayar için kullanılabilir. Bilgisayar kullanımı gibi belirli kullanım alanları veya testlerin `high` üzerinde net bir iyileşme gösterdiği durumlarda önerilir.
- **İçerik öğesi başına kontrol (Gemini 3):** Jeton kullanımını optimize eder. Örneğin, birden fazla resim içeren bir istemde karmaşık bir diyagram için `high`, daha basit bağlamsal resimler için `low` veya `medium` kullanın.

**Önerilen ayarlar**

Aşağıda, desteklenen her medya türü için önerilen medya çözünürlüğü ayarları listelenmiştir.

| Medya Türü | Önerilen Ayar | Maksimum jeton sayısı | Kullanım Yönergeleri |
| --- | --- | --- | --- |
| **Resimler** | `high` | 1120 | Maksimum kaliteyi sağlamak için çoğu görüntü analizi görevinde önerilir. |
| **PDF'ler** | `medium` | 560 | Belge anlamak için idealdir. Kalite genellikle `medium`'da doygunluğa ulaşır. `high`'ya yükseltmek, standart dokümanlar için OCR sonuçlarını nadiren iyileştirir. |
| **Video** (Genel) | `low` (veya `medium`) | 70 (kare başına) | **Not:** Video için `low` ve `medium` ayarları, bağlam kullanımını optimize etmek amacıyla aynı şekilde (70 jeton) değerlendirilir. Bu, çoğu eylem tanıma ve açıklama görevi için yeterlidir. |
| **Video** (Metin ağırlıklı) | `high` | 280 (kare başına) | Yalnızca kullanım alanında yoğun metin okuma (OCR) veya video karelerindeki küçük ayrıntılar yer aldığında gereklidir. |

Kalite, gecikme ve maliyet arasında en iyi dengeyi bulmak için farklı çözünürlük ayarlarının uygulamanız üzerindeki etkisini her zaman test edin ve değerlendirin.

## Sürüm uyumluluğu özeti

- `resolution` ayarını tek tek içerik öğelerinde belirleme **yalnızca Gemini 3 modellerinde kullanılabilir**.

## Sonraki adımlar

- Gemini API'nin çok formatlı özellikleriyle ilgili daha fazla bilgiyi [Görüntü Anlama](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr), [Video Anlama](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr) ve [Doküman Anlama](https://ai.google.dev/gemini-api/docs/document-processing?hl=tr) kılavuzlarında bulabilirsiniz.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-22 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-22 UTC."],[],[]]
