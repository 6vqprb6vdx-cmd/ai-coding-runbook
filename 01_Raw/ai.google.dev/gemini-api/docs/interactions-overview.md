---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr
fetched_at: 2026-07-06T05:12:13.740673+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Interactions API

Etkileşimler API'si, yeni arayüzümüz ve Gemini modelleri ve aracılarıyla geliştirme yapmanın en basit yoludur. Haziran 2026 itibarıyla genel kullanıma sunulmuştur ve tüm yeni projeler için önerilen arayüzdür.

Artık eski bir API olarak kabul edilse de orijinal [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=tr) API'si tam olarak desteklenmeye devam etmektedir.

## Etkileşimler API'sini neden kullanmalısınız?

- **Kullanıma hazır yeni özellikler**: `previous_interaction_id` kullanılarak isteğe bağlı sunucu tarafında görüşme durumu, hata ayıklama ve kullanıcı arayüzü oluşturma için gözlemlenebilir yürütme adımları ve `background=true` kullanılarak uzun süren görevler için [arka planda yürütme](https://ai.google.dev/gemini-api/docs/background-execution?hl=tr).
- **Daha yüksek önbellek isabet oranlarıyla daha düşük maliyet**: Sunucu tarafında durum yönetimi, dönüşümler arasında daha verimli bağlam önbelleğe alma olanağı sağlayarak çok aşamalı etkileşim sohbetlerinde jeton maliyetlerini azaltır.
- **Yeni nesil modeller ve ajanlar için geliştirilmiştir**: Düşünme modelleri, çok adımlı araç kullanımı ve karmaşık akıl yürütme akışları için özel olarak geliştirilmiştir. Bu sayede, ajan tabanlı uygulamaların oluşturulması, hata ayıklanması ve düzenlenmesi süreci basitleştirilir.
- **Modeller ve temsilciler için tek API**: Deep Research ve özel olarak yönetilen temsilciler gibi Gemini modellerini ve temsilcilerini doğrudan çağırmak için tek bir birleştirilmiş arayüz. Öğrenilecek ayrı uç noktalar veya kalıplar yoktur.
- **Yeni özelliklerin kullanıma sunulduğu yer**: Gelecekte, temel ana hat ailesinin ötesindeki yeni modeller ve özellikler ile yeni temsilci tabanlı özellikler ve araçlar Interactions API'de kullanıma sunulacak.

Varsayılan olarak Interactions API, istekleri depolar. Böylece `previous_interaction_id` kullanarak sunucu tarafı durum yönetimi özelliklerinden yararlanabilirsiniz. `store=false` ayarını yaparak durum bilgisiz davranışı etkinleştirebilirsiniz. Ayrıntılar için [Veri saklama](#data-storage-retention) bölümüne bakın.

## Başlayın

- **Kodlama aracınızı ayarlama**: **Gemini Docs MCP**'ye bağlanın ve `gemini-interactions-api` becerisini yükleyerek asistanınızın en son geliştirici belgelerine ve en iyi uygulamalara doğrudan erişmesini sağlayın.
  [Kodlama temsilcinizi ayarlama →](https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr)
- **`generateContent`**'den geçiş yapma: Mevcut bir entegrasyonunuz varsa Etkileşimler API'sine geçiş yapmak için [Taşıma Kılavuzu](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=tr)'nu inceleyin.
- **Başlayın**: [Interactions API'yi kullanmaya başlama kılavuzundaki](https://ai.google.dev/gemini-api/docs/get-started?hl=tr) adımları uygulayın.

### Özellik rehberleri

Bu kılavuzlar aracılığıyla Interactions API'sinin belirli özelliklerini keşfedin. generateContent ve Interactions API arasında geçiş yapmak için bu sayfalardaki açma/kapatma düğmesini kullanabilirsiniz:

- [Metin üretme](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr)
- [Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)
- [Görüntü anlama](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr)
- [Ses yorumlama](https://ai.google.dev/gemini-api/docs/audio?hl=tr)
- [Video anlama](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr) (Video understanding)
- [Belge işleme](https://ai.google.dev/gemini-api/docs/document-processing?hl=tr)
- [İşlev çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)
- [Yapılandırılmış çıkış](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)
- [Deep Research Agent](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr)
- [Esnek çıkarım](https://ai.google.dev/gemini-api/docs/flex-inference?hl=tr)
- [Öncelik çıkarımı](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr)

## Interactions API'sinin işleyiş şekli

Etkileşimler API'si, temel bir kaynak olan [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=tr#Resource:Interaction) etrafında şekillenir. `Interaction`, bir görüşme veya görevdeki tam bir dönüşü temsil eder. Bir etkileşimin tüm geçmişini **yürütme adımlarının** kronolojik sırası olarak içeren bir oturum kaydı görevi görür. Bu adımlar arasında model düşünceleri, sunucu tarafında veya istemci tarafında araç çağrıları ve sonuçları (ör. `function_call` ve `function_result`) ve nihai `model_output` yer alır. Depolanan kaynak (`interactions.get` aracılığıyla alınan) tam bağlam için `user_input` adımlarını da içerir ancak `interactions.create` yanıtı yalnızca model tarafından oluşturulan adımları döndürür.

[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=tr#CreateInteraction) adresine çağrı yaptığınızda yeni bir `Interaction` kaynağı oluşturursunuz.

### Sunucu tarafı durum yönetimi

Sohbete devam etmek için `previous_interaction_id` parametresini kullanarak sonraki bir çağrıda tamamlanmış bir etkileşimin `id` değerini kullanabilirsiniz. Sunucu, sohbet geçmişini almak için bu kimliği kullanır. Böylece, tüm sohbet geçmişini yeniden göndermeniz gerekmez.

`previous_interaction_id` parametresi yalnızca `previous_interaction_id` kullanılarak yapılan görüşme geçmişini (girişler ve çıkışlar) korur. Diğer parametreler **etkileşim kapsamlıdır**
ve yalnızca şu anda oluşturduğunuz etkileşim için geçerlidir:

- `tools`
- `system_instruction`
- `generation_config` (`thinking_level`, `temperature` vb. dahil)

Bu, geçerli olmasını istediğiniz takdirde bu parametreleri her yeni etkileşimde yeniden belirtmeniz gerektiği anlamına gelir. Bu sunucu tarafı durum yönetimi isteğe bağlıdır. Her isteğe tam görüşme geçmişini göndererek durum bilgisiz modda da çalışabilirsiniz.

### Veri depolama ve saklama

API, varsayılan olarak sunucu tarafı durum yönetimi özelliklerinin (`previous_interaction_id` ile), [arka planda yürütme](https://ai.google.dev/gemini-api/docs/background-execution?hl=tr) (`background=true` kullanılarak) ve gözlemlenebilirlik amaçlarıyla kullanımını basitleştirmek için tüm Interaction nesnelerini (`store=true`) saklar.

- **Ücretli katman**: Sistem, etkileşimleri **55 gün** boyunca saklar.
- **Ücretsiz katman**: Sistem, etkileşimleri **1 gün** boyunca saklar.

Bunu istemiyorsanız isteğinizde `store=false` ayarlayabilirsiniz. Bu kontrol, durum yönetiminden ayrıdır. Herhangi bir etkileşim için depolamayı devre dışı bırakabilirsiniz. Ancak `store=false` öğesinin [arka planda yürütme](https://ai.google.dev/gemini-api/docs/background-execution?hl=tr) ile uyumlu olmadığını ve sonraki dönüşlerde `previous_interaction_id` öğesinin kullanılmasını engellediğini unutmayın.

[API Referansı](https://ai.google.dev/api/interactions-api?hl=tr)'nda bulunan silme yöntemini kullanarak depolanan etkileşimleri istediğiniz zaman silebilirsiniz. Yalnızca etkileşim kimliğini biliyorsanız etkileşimleri silebilirsiniz.

Saklama süresi sona erdikten sonra verileriniz otomatik olarak silinir.

Sistem, Etkileşim nesnelerini [şartlara](https://ai.google.dev/gemini-api/terms?hl=tr) göre işler.

## En iyi uygulamalar

- **Önbellek isabet oranı**: Sohbetlere devam etmek için `previous_interaction_id` kullanıldığında sistem, sohbet geçmişi için örtülü önbelleğe almayı daha kolay kullanabilir. Bu da performansı artırır ve maliyetleri düşürür.
- **Etkileşimleri karıştırma**: Bir görüşmede Agent ve Model etkileşimlerini karıştırıp eşleştirebilirsiniz. Örneğin, ilk veri toplama için Deep Research aracısı gibi özel bir aracı kullanabilir, ardından özetleme veya yeniden biçimlendirme gibi takip görevleri için standart bir Gemini modeli kullanabilirsiniz. Bu adımları `previous_interaction_id` ile bağlayabilirsiniz.

## Desteklenen modeller ve aracı

| Model Adı | Tür | Model Kimliği |
| --- | --- | --- |
| Gemini 3.5 Flash | Model | `gemini-3.5-flash` |
| Gemini 3.1 Pro Önizlemesi | Model | `gemini-3.1-pro-preview` |
| Gemini 3.1 Flash-Lite | Model | `gemini-3.1-flash-lite` |
| Gemini 3 Flash Önizlemesi | Model | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Model | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Model | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | Model | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | Model | `gemini-3-pro-image` |
| Gemini 3.1 Flash Görüntüsü | Model | `gemini-3.1-flash-image` |
| Gemini 3.1 Flash TTS Önizlemesi | Model | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | Model | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | Model | `gemma-4-26b-a4b-it` |
| Lyria 3 Clip Preview | Model | `lyria-3-clip-preview` |
| Lyria 3 Pro Önizlemesi | Model | `lyria-3-pro-preview` |
| Deep Research Önizlemesi | Temsilci | `deep-research-preview-04-2026` |
| Deep Research Önizlemesi | Temsilci | `deep-research-max-preview-04-2026` |
| Antigravity önizlemesi | Temsilci | `antigravity-preview-05-2026` |

## SDK'lar

Etkileşimler API'sine erişmek için Google GenAI SDK'larının en son sürümünü kullanabilirsiniz.

- Python'da bu, `2.3.0` sürümünden itibaren `google-genai` paketidir.
- JavaScript'te bu, `2.3.0` sürümünden itibaren `@google/genai` paketidir.

SDK'ları nasıl yükleyeceğiniz hakkında daha fazla bilgiyi [Kitaplıklar](https://ai.google.dev/gemini-api/docs/libraries?hl=tr) sayfasında bulabilirsiniz.

## Sınırlamalar

- **Uzak MCP**: Gemini 3, uzak MCP'yi desteklemez. Bu özellik yakında kullanıma sunulacaktır.

Aşağıdaki özellikler [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=tr) API tarafından desteklenir ancak Interactions API'de **henüz kullanılamaz**:

- **[Video meta verileri](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr)**: Video anlama için klip aralıklarını ve özel kare hızlarını ayarlamak üzere kullanılan `video_metadata` alanı.
- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr)**
- **[Otomatik işlev çağırma (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=tr#automatic_function_calling_python_only)**
- **[Açık önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr)**: Sunucu tarafında örtülü önbelleğe almanın, `previous_interaction_id` aracılığıyla Interactions API'sinde kullanılabildiğini unutmayın.

## Geri bildirim

Geri bildiriminiz, Etkileşimler API'sinin geliştirilmesi açısından büyük önem taşır.
Düşüncelerinizi paylaşmak, hataları bildirmek veya özellik isteğinde bulunmak için [Google Yapay Zeka Geliştirici Topluluğu Forumu](https://discuss.ai.google.dev/c/gemini-api/4?hl=tr)'nu kullanabilirsiniz.

## Sırada ne var?

- [Interactions API hızlı başlangıç not defterini](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=tr) deneyin.
- [Gemini Deep Research Agent](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) hakkında daha fazla bilgi edinin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-26 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-26 UTC."],[],[]]
