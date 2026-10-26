---
source_url: https://ai.google.dev/gemini-api/docs/robotics-overview?hl=tr
fetched_at: 2026-10-26T05:55:15.706535+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini Robotics ER

Gemini Robotics ER (somutlaştırılmış akıl yürütme) modelleri, robotların fiziksel dünyayı algılamasını ve bu dünyayla etkileşim kurmasını sağlayan görsel dil modelleridir (VLM'ler). Görsel verileri yorumlar, uzamsal ve zamansal akıl yürütme yapar, çok adımlı görevleri planlar, robotları ve araçları yönetirler.

## Modeller

Gemini Robotics ER 2 modeli, Gemini Robotics'in en yeni modelidir.
Bu model, robotların çevrelerini tam olarak anlamasını sağlayan güncellenmiş akıl yürütme modelimizdir. Robotların temsilci tabanlı orkestrasyonu (ör. VLA'lar kullanarak), ilerleme durumu ve başarı tespiti dahil olmak üzere robot video anlama, cihaz okuma, işaret etme ve uzamsal akıl yürütme gibi somutlaştırılmış akıl yürütme yeteneklerinde uzmanlaşmıştır.

Gemini Robotics ER 2 modeli, iki model uç noktası sunar:

- **`gemini-robotics-er-2-preview`**: Standart ER 2 modeli. Gemini 3.5 Flash'ın üzerine inşa edilen bu model; gelişmiş uzamsal akıl yürütme, videoda an bulma, video ilerleme sınıflandırması, çoklu robot koordinasyonu ve çok adımlı araç kullanımı özelliklerine sahiptir.
- **`gemini-robotics-er-2-streaming-preview`**: [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=tr) kullanılarak anlık akış için optimize edilmiştir. Sürekli ses ve video girişini işleyen düşük gecikmeli robot aracılar için bu modeli kullanın.

Gemini Robotics ER 1.6, [31 Ağustos 2026'da kullanımdan kaldırıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr#robotics-models).
Hâlâ Gemini Robotics ER 1.6'yı kullanıyorsanız API çağrılarınızda `model="gemini-robotics-er-1.6-preview"` yerine `model="gemini-robotics-er-2-preview"` veya `model="gemini-robotics-er-2-streaming-preview"` kullanarak Gemini Robotics ER 2'ye geçin.

[Google AI Studio'da Gemini Robotics ER 2'yi deneme](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=tr)

## Robotik özellikleri

Gemini Robotics ER, çeşitli somutlaştırılmış akıl yürütme özelliklerini destekler.
Daha fazla bilgi edinmek için bir özellik seçin:

| Kapasite | Açıklama | Kılavuz |
| --- | --- | --- |
| Uzamsal akıl yürütme | Nesneleri işaretleme, videoda takip etme, sınırlayıcı kutularla algılama, yörünge planlama. | [Uzamsal akıl yürütme](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=tr) |
| Ajan tabanlı vizyon | Resim işleme araçlarından yararlanarak diğer özellikleri geliştirmek için kod yürütme özelliğini kullanın. | [Temsilci vizyonu](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=tr) |
| Görev düzenleme | Uzun vadeli görevleri tamamlamak için uzamsal akıl yürütmeyi özel robot API'leriyle birleştirme | [Görev düzenleme](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=tr) |
| Akış (yalnızca Gemini Robotics ER 2 Akış uç noktası) | Düşük gecikmeli işlev çağrısı ile gerçek zamanlı robot temsilciler için çift yönlü akış. | [Robotik için akış](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=tr) |
| Video ilerleme durumu (yalnızca Gemini Robotics ER 2) | Sürekli video akışlarından an bulma ve ilerleme sınıflandırması. | [Video anlama](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=tr) |

## Başlamadan önce

Gemini Robotics ER modellerine **Gemini Developer API** üzerinden erişilebilir. Başlamak için [Google AI Studio](https://aistudio.google.com/apikey?hl=tr) veya [Google Cloud Console](https://ai.google.dev/gemini-api/docs/api-key?hl=tr#cloud-console)'dan bir [Gemini API anahtarı](https://ai.google.dev/gemini-api/docs/api-key?hl=tr) oluşturun ve [ortamınızı ayarlayın](https://ai.google.dev/gemini-api/docs/api-key?hl=tr#setup-environment).

Anahtar türleri, güvenlik ve anahtarınızı Python, JavaScript ve diğer dillerde nasıl yapılandıracağınız hakkında ayrıntılı bilgi için [Gemini API anahtarlarını kullanma](https://ai.google.dev/gemini-api/docs/api-key?hl=tr) başlıklı makaleyi inceleyin.

## Başlarken

Aşağıdaki örnekte, bir resimdeki nesneler bulunur ve bunların normalleştirilmiş 2D koordinatları ile etiketleri döndürülür. Bu çıkışı doğrudan bir robotik API'sine veya VLA modeline ileterek robot eylemleri oluşturabilirsiniz.

### Python

```
from google import genai

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

image_response = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": PROMPT}
    ],
    generation_config={"thinking_level": "high"},
)

print(image_response.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const PROMPT = `
  Point to no more than 10 items in the image. The label returned
  should be an identifying name for the object detected.
  The answer should follow the json format: [{"point": <point>,
  "label": <label1>}, ...]. The points are in [y, x] format
  normalized to 0-1000.
`;
const client = new GoogleGenAI();

const uploadedFile = await client.files.upload({ file: "my-image.png" });

const imageResponse = await client.interactions.create({
  model: "gemini-robotics-er-2-preview",
  input: [
    {
      type: "image",
      uri: uploadedFile.uri,
      mime_type: uploadedFile.mimeType,
    },
    { type: "text", text: PROMPT },
  ],
  generation_config: { thinking_level: "high" },
});

console.log(imageResponse.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.List;

Client client = new Client();

String prompt =
    "Point to no more than 10 items in the image. The label returned "
        + "should be an identifying name for the object detected. "
        + "The answer should follow the json format: [{\"point\": <point>, "
        + "\"label\": <label1>}, ...]. The points are in [y, x] format "
        + "normalized to 0-1000.";

File uploadedFile =
    client.files.upload(
        new java.io.File("my-image.png"),
        UploadFileConfig.builder().mimeType("image/png").build());

Content imageContent =
    ImageContent.builder()
        .uri(uploadedFile.uri().orElse(""))
        .mimeType(ImageContentMimeType.of(uploadedFile.mimeType().orElse("image/png")))
        .build();
Content textContent = TextContent.builder().text(prompt).build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-robotics-er-2-preview"))
        .input(InteractionsInput.ofContent(List.of(imageContent, textContent)))
        .generationConfig(
            GenerationConfig.builder().thinkingLevel(ThinkingLevel.HIGH).build())
        .build();

Interaction imageResponse =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(imageResponse.outputText().orElse(""));
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

    prompt := `Point to no more than 10 items in the image. The label returned
should be an identifying name for the object detected.
The answer should follow the json format: [{"point": <point>,
"label": <label1>}, ...]. The points are in [y, x] format
normalized to 0-1000.`

    uploadedFile, err := client.Files.UploadFromPath(ctx, "my-image.png", &genai.UploadFileConfig{
        MIMEType: "image/png",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-robotics-er-2-preview"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    URI:      genai.Ptr(uploadedFile.URI),
                    MimeType: genai.Ptr(interactions.ImageMimeTypeImagePng),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelHigh.ToPointer(),
            },
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
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-robotics-er-2-preview",
    "input": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "image/png",
            "data": "'"${IMAGE_BASE64}"'"
          }
        },
        {
          "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
        }
      ]
    },
    "generation_config": {
      "thinking_config": {
        "thinking_level": "high"
      }
    }
  }'
```

Çıkış, her biri bir `point` (normalleştirilmiş `[y, x]` koordinatları) ve nesneyi tanımlayan bir `label` içeren nesnelerden oluşan bir JSON dizisi olur.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

Aşağıdaki resimde, bu noktaların nasıl gösterilebileceğine dair bir örnek verilmiştir:

![Resimdeki nesnelerin noktalarını gösteren bir örnek](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=tr)

## İşleyiş şekli

Gemini Robotics ER, doğal dildeki istemlerle birlikte resim, video veya ses girişi alır. Nesneleri tanımlar, sahne bağlamı ve uzamsal ilişkiler hakkında akıl yürütür ve koordinatlar veya sınırlayıcı kutular gibi yapılandırılmış çıktılar döndürür.

Gemini Robotics ER, temsilci olarak da çalışır: Karmaşık görevleri alt görevlere ayırır ve robot işlevlerinizi çağırarak veya oluşturulan kodu çalıştırarak bu görevleri yürütür. Örneğin, "elmayı kaseye koy" komutu; bulma, kavrama ve yerleştirme adımlarından oluşan bir diziye dönüşür.

Gemini'ın araç çağrılarını nasıl yürüttüğüyle ilgili ayrıntılar için [İşlev çağrısı](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=tr#how-it-works) bölümüne bakın.

## Güvenlik

Gemini Robotics ER, güvenlik göz önünde bulundurularak tasarlanmış olsa da robotun çevresinde güvenli bir ortam sağlamak sizin sorumluluğunuzdadır. Üretken yapay zeka modelleri hata yapabilir ve fiziksel robotlar hasara neden olabilir. Daha fazla bilgi için [Gemini Robotics güvenlik sayfasını](https://deepmind.google/models/gemini-robotics/safety?hl=tr) ziyaret edin.

## En iyi uygulamalar

1. Sade ve doğal dil kullanın. Robotun ne yapmasını istediğinizi bir insana anlatır gibi açıklayın. Bir terim işe yaramıyorsa yaygın olarak kullanılan bir eş anlamlısını deneyin.
2. Görsel girişi optimize edin. Resmi göndermeden önce küçük veya net olmayan nesneleri kırpın ya da yakınlaştırın. Işık ve düşük renk kontrastı algılamayı etkileyebilir.
3. Karmaşık görevleri adımlara bölün. Modelin odaklanmasını sağlamak ve doğruluğu artırmak için her adımı ayrı bir istem olarak gönderin.
4. Yüksek hassasiyet gerektiren görevler için birden fazla kez sorgu gönderip sonuçların ortalamasını alın. Bu fikir birliği yaklaşımı, konumsal çıkışlardaki varyansı azaltır.

## Sınırlamalar

Gemini Robotics ER ile geliştirme yaparken aşağıdaki sınırlamaları göz önünde bulundurun:

- **API anahtarı kısıtlamaları:** Gemini API, kısıtlanmamış API anahtarlarından gelen istekleri kabul etmez ve `403 Forbidden` hatası döndürür. [AI Studio](https://aistudio.google.com/api-keys?hl=tr)'da kısıtlamalar ekleyerek API anahtarınızın güvenliğini sağlayın.
  Ayrıntılar için [Kısıtlanmamış API anahtarlarının güvenliğini sağlama](https://ai.google.dev/gemini-api/docs/api-key?hl=tr#secure-unrestricted-keys) başlıklı makaleyi inceleyin.
- **Gecikme ve performans:** Karmaşık sorgular, yüksek çözünürlüklü girişler veya yüksek düşünme seviyeleri, işlem sürelerinin uzamasına neden olabilir. Düşünme seviyesi için
  gecikme ile performans arasında iyi bir denge kurmak istiyorsanız orta seviyeyi kullanın.
- **Halüsinasyonlar:** Tüm büyük dil modelleri gibi Gemini Robotics ER modelleri de özellikle belirsiz istemler veya dağıtım dışı girişler için zaman zaman "halüsinasyon" görebilir ya da yanlış bilgiler verebilir.
- **İstem kalitesine bağlılık:** Çıktı kalitesi, giriş isteminin netliğine bağlıdır. Spesifik ve iyi yapılandırılmış istemler kullanın.
- **İşlem maliyeti:** Modeli çalıştırmak, özellikle video girişleri veya yüksek `thinking_budget` ile işlem kaynaklarını tüketir ve maliyetlere neden olur.
  Daha fazla bilgi için [Düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) sayfasına bakın.
- **Giriş türleri:** Her modun sınırlamalarıyla ilgili ayrıntılar için aşağıdaki konulara bakın.
  - [Resim girişleri](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr#technical-details-image)
  - [Video girişleri](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr#supported-formats)
  - [Ses girişleri](https://ai.google.dev/gemini-api/docs/audio?hl=tr#supported-formats)

## Gizlilik Uyarısı

Bu belgede atıfta bulunulan modellerin ("Robotik Modeller"), donanımınızı talimatlarınıza uygun şekilde çalıştırmak ve hareket ettirmek için video ve ses verilerini kullandığını kabul edersiniz. Bu nedenle, Robotik Modeller'i, kimliği belirlenebilen kişilerin verileri (ör. ses, görüntü ve benzerlik verileri ("Kişisel Veriler")) Robotik Modeller tarafından toplanacak şekilde çalıştırabilirsiniz. Robotik Modelleri, kişisel verileri toplayacak şekilde kullanmayı tercih ederseniz kimliği belirlenebilen kişilerin, kişisel verilerinin [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=tr) adresinde bulunan Gemini API Ek Hizmet Şartları'nda ("Şartlar") belirtildiği şekilde Google'a sağlanabileceği ve Google tarafından kullanılabileceği ("Google Verilerinizi Nasıl Kullanır?" başlıklı bölüm de dahil) konusunda yeterli düzeyde bilgilendirilip onay vermediği sürece Robotik Modeller ile etkileşime girmesine veya Robotik Modeller'in bulunduğu alanda bulunmasına izin vermeyeceğinizi kabul edersiniz. Bu bildirimin, Kişisel Veriler'in Şartlar'da belirtilen şekilde toplanmasına ve kullanılmasına izin vermesini sağlayacaksınız. Ayrıca, yüz bulanıklaştırma gibi teknikleri kullanarak ve Robotik Modeller'i mümkün olduğunca kimliği belirlenebilen kişilerin bulunmadığı alanlarda çalıştırarak Kişisel Veriler'in toplanmasını ve dağıtılmasını en aza indirmek için ticari olarak makul çabayı göstereceksiniz.

## Fiyatlandırma

Fiyatlandırma ve kullanılabilir bölgeler hakkında ayrıntılı bilgi için [fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) sayfasını inceleyin.

## Model uç noktaları

### Gemini Robotics ER 2 Preview

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | `gemini-robotics-er-2-preview` |
| saveDesteklenen veri türleri | **Girişler**  Metin, resim, video, ses  **Çıkış**  Metin |
| token\_autoToken sınırları[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) | **Giriş jetonu sınırı**  131.072  **Çıkış parçası sınırı**  65.536 |
| handymanÖzellikler | **[Ses üretme](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr)**  Desteklenmiyor  **[Önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr)**  Destekleniyor  **[Kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr)**  Destekleniyor  **[Bilgisayar kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr)**  Destekleniyor  **[Dosya arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr)**  Destekleniyor  **[İşlev çağrısı](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)**  Destekleniyor  **[Google Haritalar ile Temellendirme](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr)**  Destekleniyor  **[Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)**  Desteklenmiyor  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=tr)**  Desteklenmiyor  **[Arama temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr)**  Destekleniyor  **[Yapılandırılmış çıkışlar](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)**  Destekleniyor  **[Düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr)**  Destekleniyor  **[URL bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr)**  Destekleniyor |
| speedTüketim seçenekleri | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr)**  Destekleniyor  **[Flex çıkarımı](https://ai.google.dev/gemini-api/docs/flex-inference?hl=tr)**  Desteklenmiyor  **[Öncelik çıkarımı](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr)**  Desteklenmiyor |
| 123Sürümler | Daha fazla bilgi için [model sürümü kalıplarını](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#model-versions) okuyun.  - Önizleme: `gemini-robotics-er-2-preview` |
| calendar\_monthSon güncelleme | Temmuz 2026 |
| id\_cardModel kartı | [Model kartı](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=tr) |

### Gemini Robotics ER 2 Streaming Preview

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | `gemini-robotics-er-2-streaming-preview` |
| saveDesteklenen veri türleri | **Girişler**  Metin, resim, video, ses  **Çıkış**  Metin |
| token\_autoToken sınırları[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) | **Giriş jetonu sınırı**  131.072  **Çıkış parçası sınırı**  65.536 |
| handymanÖzellikler | **[Ses üretme](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr)**  Desteklenmiyor  **[Önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr)**  Desteklenmiyor  **[Kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr)**  Desteklenmiyor  **[Bilgisayar kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr)**  Desteklenmiyor  **[Dosya arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr)**  Desteklenmiyor  **[İşlev çağrısı](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)**  Destekleniyor  **[Google Haritalar ile Temellendirme](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr)**  Desteklenmiyor  **[Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)**  Desteklenmiyor  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=tr)**  Destekleniyor  **[Arama temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr)**  Destekleniyor  **[Yapılandırılmış çıkışlar](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)**  Desteklenmiyor  **[Düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr)**  Destekleniyor  **[URL bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr)**  Desteklenmiyor |
| speedTüketim seçenekleri | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr)**  Desteklenmiyor  **[Flex çıkarımı](https://ai.google.dev/gemini-api/docs/flex-inference?hl=tr)**  Desteklenmiyor  **[Öncelik çıkarımı](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr)**  Desteklenmiyor |
| 123Sürümler | Daha fazla bilgi için [model sürümü kalıplarını](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#model-versions) okuyun.  - Önizleme: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthSon güncelleme | Temmuz 2026 |
| id\_cardModel kartı | [Model kartı](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=tr) |

### Gemini Robotics ER 1.6 Preview

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | `gemini-robotics-er-1.6-preview` |
| saveDesteklenen veri türleri | **Girişler**  Metin, resim, video, ses  **Çıkış**  Metin |
| token\_autoToken sınırları[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) | **Giriş jetonu sınırı**  131.072  **Çıkış parçası sınırı**  65.536 |
| handymanÖzellikler | **[Ses üretme](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr)**  Desteklenmiyor  **[Önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr)**  Destekleniyor  **[Kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr)**  Destekleniyor  **[Bilgisayar kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr)**  Destekleniyor  **[Dosya arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr)**  Destekleniyor  **[İşlev çağrısı](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)**  Destekleniyor  **[Google Haritalar ile Temellendirme](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr)**  Destekleniyor  **[Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)**  Desteklenmiyor  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=tr)**  Desteklenmiyor  **[Arama temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr)**  Destekleniyor  **[Yapılandırılmış çıkışlar](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)**  Destekleniyor  **[Düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr)**  Destekleniyor  **[URL bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr)**  Destekleniyor |
| speedTüketim seçenekleri | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr)**  Destekleniyor  **[Flex çıkarımı](https://ai.google.dev/gemini-api/docs/flex-inference?hl=tr)**  Desteklenmiyor  **[Öncelik çıkarımı](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr)**  Desteklenmiyor |
| 123Sürümler | Daha fazla bilgi için [model sürümü kalıplarını](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#model-versions) okuyun.  - Kapat: `gemini-robotics-er-1.6-preview` |
| calendar\_monthSon güncelleme | Aralık 2025 |
| cognition\_2Son güncel bilgi tarihi | Ocak 2025 |

## Sırada ne var?

- [Uzamsal akıl yürütme](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=tr): İşaret etme, izleme, sınırlayıcı kutular, yörüngeler.
- [Ajan tabanlı yetenekler](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=tr): Kod yürütme, cihaz okuma, görüntü ek açıklaması.
- [Görev düzenleme](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=tr): Özel robot API'leri ile uzun vadeli görevler.
- [Akışlı robotik](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=tr): Gerçek zamanlı çift yönlü akış (yalnızca Gemini Robotics ER 2).
- [Video anlama](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=tr): An bulma ve ilerleme sınıflandırması (yalnızca Gemini Robotics ER 2).
- [Gemini Robotics güvenliği](https://deepmind.google/models/gemini-robotics/safety?hl=tr): Model ailesinin temelindeki güvenlik araştırması.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-21 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-21 UTC."],[],[]]
