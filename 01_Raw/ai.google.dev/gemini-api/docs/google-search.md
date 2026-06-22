---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=tr
fetched_at: 2026-06-22T06:31:27.188529+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) is now available in preview with collaborative planning, visualization, MCP support, and more.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Google Arama ile Temellendirme

Google Arama ile Temellendirme, Gemini modelini güncel web içeriğine bağlar ve tüm dillerde kullanılabilir. Bu sayede Gemini, son güncel bilgi tarihinin ötesinde doğrulanabilir kaynaklardan alıntı yaparak daha doğru yanıtlar verebilir.

Temellendirme, aşağıdaki işlemleri yapabilen uygulamalar oluşturmanıza yardımcı olur:

- **Doğruluğu artırma:** Yanıtları gerçek dünyadaki bilgilere dayandırarak model halüsinasyonlarını azaltın.
- **Anlık bilgilere erişme:** Son olaylar ve konularla ilgili soruları yanıtlama
- **Alıntı ekleyin:** Modelin iddialarının kaynaklarını göstererek kullanıcıların güvenini kazanın.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

[Arama aracı not defterini](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=tr) deneyerek daha fazla bilgi edinebilirsiniz.

## Google Arama ile temellendirme nasıl çalışır?

`google_search` aracını etkinleştirdiğinizde model, arama, işleme ve bilgi alıntılamayla ilgili tüm iş akışını otomatik olarak yönetir.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=tr)

1. **Kullanıcı istemi:** Uygulamanız, kullanıcının istemini `google_search` aracı etkinleştirilmiş şekilde Gemini API'ye gönderiyor.
2. **İstem Analizi:** Model, istemi analiz eder ve Google Arama'nın yanıtı iyileştirip iyileştiremeyeceğini belirler.
3. **Google Arama:** Gerekirse model, bir veya daha fazla arama sorgusunu otomatik olarak oluşturup yürütür.
4. **Arama sonuçlarını işleme:** Model, arama sonuçlarını işler, bilgileri sentezler ve bir yanıt oluşturur.
5. **Temellendirilmiş Yanıt:** API, arama sonuçlarına dayalı, son ve kullanıcı dostu bir yanıt döndürür. Bu yanıtta, modelin metin yanıtı ve arama sorguları, web sonuçları ve alıntılarla birlikte `groundingMetadata` yer alır.

## Temellendirme yanıtını anlama

Bir yanıt başarıyla temellendirildiğinde yanıtta `groundingMetadata` alanı bulunur. Bu yapılandırılmış veriler, hak taleplerini doğrulamak ve uygulamanızda zengin bir alıntı deneyimi oluşturmak için gereklidir.

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

Gemini API, `groundingMetadata` ile birlikte aşağıdaki bilgileri döndürür:

- `webSearchQueries` : Kullanılan arama sorgularının dizisi. Bu, hata ayıklama ve modelin muhakeme sürecini anlamak için yararlıdır.
- `searchEntryPoint` : Gerekli arama önerilerini oluşturmak için HTML ve CSS'yi içerir. Kullanımla ilgili tüm şartlar [Hizmet Şartları](https://ai.google.dev/gemini-api/terms?hl=tr#grounding-with-google-search)'nda ayrıntılı olarak açıklanmıştır.
- `groundingChunks` : Web kaynaklarını (`uri` ve `title`) içeren nesne dizisi.
- `groundingSupports` : Model yanıtı `text` ile `groundingChunks` içindeki kaynakları bağlamak için kullanılan parçalar dizisi. Her parça, bir metni `segment` (`startIndex` ve `endIndex` ile tanımlanır) bir veya daha fazla `groundingChunkIndices` ile bağlar. Bu, metin içi alıntılar oluşturmanın anahtarıdır.

Google Arama ile temellendirme, yanıtları hem herkese açık web verileri hem de sağladığınız belirli URL'lerle temellendirmek için [URL bağlam aracı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) ile birlikte de kullanılabilir.

## Satır içi alıntılarla kaynakları atfetme

API, yapılandırılmış alıntı verileri döndürerek kaynakları kullanıcı arayüzünüzde nasıl göstereceğiniz konusunda tam kontrol sahibi olmanızı sağlar. Modelin ifadelerini doğrudan kaynaklarına bağlamak için `groundingSupports` ve `groundingChunks` alanlarını kullanabilirsiniz. Meta verileri işleyerek satır içi, tıklanabilir alıntılar içeren bir yanıt oluşturmak için kullanılan yaygın bir kalıbı aşağıda bulabilirsiniz.

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

Satır içi alıntıların yer aldığı yeni yanıt şu şekilde görünür:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## Fiyatlandırma

Gemini 3 ile Google Arama'yı Temellendirme özelliğini kullandığınızda projeniz, modelin yürütmeye karar verdiği her arama sorgusu için faturalandırılır. Model, tek bir isteme yanıt vermek için birden fazla arama sorgusu yürütmeye karar verirse (örneğin, aynı API çağrısında `"UEFA Euro 2024 winner"` ve `"Spain vs England Euro 2024 final
score"` için arama yaparsa) bu, söz konusu istek için aracın iki faturalandırılabilir kullanımı olarak sayılır. Faturalandırma amacıyla, benzersiz sorguları sayarken boş web arama sorgularını yoksayarız. Bu faturalandırma modeli yalnızca Gemini 3 modelleri için geçerlidir. Gemini 2.5 veya daha eski modellerle arama temellendirmeyi kullandığınızda projeniz istem başına faturalandırılır.

Ayrıntılı fiyatlandırma bilgileri için [Gemini API fiyatlandırma sayfasını](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) inceleyin.

## Desteklenen modeller

Tüm özellikleri [modele
genel bakış](https://ai.google.dev/gemini-api/docs/models?hl=tr) sayfasında bulabilirsiniz.

| Model | Google Arama ile Temellendirme |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Flash Image Önizlemesi | ✔️ |
| Gemini 3.1 Pro Önizlemesi | ✔️ |
| Gemini 3 Pro Görüntü Önizlemesi | ✔️ |
| Gemini 3 Flash Önizlemesi | ✔️ |
| Gemini 3.1 Flash-Lite Önizlemesi | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Desteklenen araç kombinasyonları

Daha karmaşık kullanım alanlarını desteklemek için Google Arama ile Temellendirme'yi [kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) ve [URL bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) gibi diğer araçlarla birlikte kullanabilirsiniz.

Gemini 3 modelleri, yerleşik araçların (ör. Google Arama ile temellendirme) özel araçlarla (işlev çağrısı) birlikte kullanılmasını destekler. [Araç kombinasyonları](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) sayfasından daha fazla bilgi edinin.

## Sırada ne var?

- [Gemini API çözüm kitabında Google Arama ile Temellendirme](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=tr)'yi deneyin.
- [İşlev Çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) gibi diğer araçlar hakkında bilgi edinin.
- [URL bağlamı aracını](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) kullanarak istemleri belirli URL'lerle nasıl zenginleştireceğinizi öğrenin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-19 UTC."],[],[]]
