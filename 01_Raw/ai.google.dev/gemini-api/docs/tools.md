---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=tr
fetched_at: 2026-06-08T15:08:10.744258+00:00
title: "Gemini API ile Ara\u00e7lar\u0131 Kullanma \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini API ile Araçları Kullanma

Araçlar, Gemini modellerinin yeteneklerini genişleterek dünyada işlem yapmalarını, anlık bilgilere erişmelerini ve karmaşık hesaplama görevlerini gerçekleştirmelerini sağlar. Modeller, hem standart istek-yanıt etkileşimlerinde hem de [Live API](https://ai.google.dev/gemini-api/docs/live-tools?hl=tr) kullanılarak yapılan gerçek zamanlı akış oturumlarında araçları kullanabilir.

Araçlar, bir modelin sorgulara yanıt vermek için kullanabileceği belirli özelliklerdir (ör. Google Arama veya Kod Yürütme). Gemini API, tümüyle yönetilen bir dizi yerleşik araç sunar. Dilerseniz [Function Calling](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)'i kullanarak özel araçlar da tanımlayabilirsiniz.

Çok adımlı, hedefe yönelik sistemler oluşturmak için [Agents
Overview](https://ai.google.dev/gemini-api/docs/agents?hl=tr) (Temsilcilere Genel Bakış) başlıklı makaleyi inceleyin.

## Kullanılabilir yerleşik araçlar

| Araç | Açıklama | Kullanım Alanları |
| --- | --- | --- |
| [Google Arama](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) | Halüsinasyonları azaltmak için yanıtları web'deki güncel olaylara ve bilgilere dayandırın. | \- Son olaylarla ilgili soruları yanıtlama   - Çeşitli kaynaklardan alınan bilgilerle gerçekleri doğrulama |
| [Google Haritalar](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr) | Yerleri bulabilen, yol tarifi alabilen ve zengin yerel bağlam bilgileri sağlayabilen konuma duyarlı asistanlar oluşturun. | \- Birden fazla durak içeren seyahat planları yapma   - Kullanıcı ölçütlerine göre yerel işletmeleri bulma |
| [Kod Yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) | Modelin matematik problemlerini çözmek veya verileri doğru şekilde işlemek için Python kodu yazmasına ve çalıştırmasına izin verin. | \- Karmaşık matematik denklemlerini çözme   - Metin verilerini hassas bir şekilde işleme ve analiz etme |
| [URL Bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) | Modele, belirli web sayfalarındaki veya belgelerdeki içerikleri okuyup analiz etmesini söyleyin. | \- Belirli URL'lere veya dokümanlara göre soruları yanıtlama   - Farklı web sayfalarındaki bilgileri alma |
| [Bilgisayar Kullanımı (Önizleme)](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr) | Gemini'ın ekranı görüntülemesine ve web tarayıcısı kullanıcı arayüzleriyle etkileşim kurmak için işlemler oluşturmasına izin verin (istemci tarafında yürütme). | \- Tekrarlayan web tabanlı iş akışlarını otomatikleştirme   - Web uygulaması kullanıcı arayüzlerini test etme |
| [Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr) | Veriyle Artırılmış Üretim'i (RAG) etkinleştirmek için kendi dokümanlarınızı dizine ekleyin ve arayın. | - Teknik kılavuzlarda arama yapma   - Tescilli verilerle ilgili soruları yanıtlama |

Belirli araçlarla ilişkili maliyetler hakkında ayrıntılı bilgi için [Fiyatlandırma sayfasına](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#pricing_for_tools) bakın.

## Araç yürütme nasıl çalışır?

Araçlar, modelin sohbet sırasında işlem isteğinde bulunmasına olanak tanır. Akış, aracın yerleşik (Google tarafından yönetilen) veya özel (sizin tarafınızdan yönetilen) olmasına bağlı olarak değişir.

### Yerleşik araç akışı

Yerleşik araçlar (Google Arama, Google Haritalar, URL Bağlamı, Dosya Arama, Kod Yürütme) için tüm süreç tek bir API çağrısı içinde gerçekleşir:

1. **Siz** bir istem gönderiyorsunuz: "GOOG'un en son hisse senedi fiyatının karekökü nedir?"
2. **Gemini**, araçlara ihtiyaç duyduğuna karar verir ve bunları Google'ın sunucularında çalıştırır (ör. hisse senedi fiyatını arar, ardından karekökü hesaplamak için Python kodu çalıştırır).
3. **Gemini**, araç sonuçlarına dayalı nihai yanıtı geri gönderir.

### Özel araç akışı (işlev çağırma)

Özel araçlar ve bilgisayar kullanımı için yürütme işlemini uygulamanız gerçekleştirir:

1. İşlev (araç) bildirimleriyle birlikte **istem** gönderiyorsunuz.
2. **Gemini**, belirli bir işlevi (ör. `{"name": "get_order_status", "args": {"order_id": "123"}}`) çağırmak için her zaman benzersiz bir `id` ile birlikte yapılandırılmış JSON gönderebilir.
3. İşlevi uygulamanızda veya ortamınızda **siz** yürütürsünüz.
4. İşlev çağrısıyla aynı `id` ile işlev sonuçlarını **siz** Gemini'a geri gönderirsiniz.
5. **Gemini**, sonuçları kullanarak nihai bir yanıt veya başka bir araç çağrısı oluşturur.

Daha fazla bilgi için [İşlev çağrısı kılavuzunu](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) inceleyin.

### Yerleşik ve özel araçları birleştirme akışı

Yerleşik araçları ve özel araçları (işlev çağrıları) birleştiren isteklerde model, farklı ortamlarda yürütmeyi koordine etmek için [araç bağlamı dolaşımını](https://ai.google.dev/gemini-api/docs/toold-combination?hl=tr) kullanır:

1. **Siz** bir istem gönderip etkinleştirmek istediğiniz yerleşik araçları ve özel işlevleri tanımlayarak kombinasyon desteğini etkinleştirmek için bir işaret ayarlarsınız.
2. **Gemini**, yerleşik araçları çalıştırır ve herhangi bir istemci tarafı işlev çağrısı oluşturulursa kullanıcıya yanıt verir (önce hangisinin çalıştırılacağı, isteme ve modelin kararına bağlıdır). Aşağıdaki bilgileri içeren bir yanıt gönderir:
   - Araç çağrısının onayı
   - Araç yanıtının sonuçları (model iki paralel işlev çağrısı oluşturduysa bu, JSON'dan sonra gelebilir)
   - İşlevinizi çağırmak için yapılandırılmış JSON
   - Bağlamı korumak için şifrelenmiş düşünce imzaları
3. İşlevi uygulamanızda veya ortamınızda **siz** yürütürsünüz.
4. Gemini'ın yanıtının tüm bölümlerini ve işlev çağrısı sonuçlarınızı **siz** döndürürsünüz.
5. **Gemini**, birleştirilmiş tüm bağlamı kullanarak son yanıtı oluşturur.

Yerleşik ve özel araç kombinasyonu desteğini etkinleştirme ve bağlam dolaşımı örnekleri hakkında bilgi edinmek için [Araç kombinasyonu kılavuzunu](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) okuyun.

## Yapılandırılmış çıkışlar ve işlev çağırma

Gemini, yapılandırılmış çıktılar oluşturmak için iki yöntem sunar. Modelin kendi araçlarınıza veya veri sistemlerinize bağlanarak ara adım atması gerektiğinde [fonksiyon çağrısı](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) özelliğini kullanın. Modelin nihai yanıtının belirli bir şemaya kesinlikle uyması gerektiğinde (ör. özel bir kullanıcı arayüzü oluşturmak için) [Yapılandırılmış Çıkışlar](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)'ı kullanın.

## Araçlarla yapılandırılmış çıkışlar

[Yapılandırılmış Çıkışlar](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)'ı yerleşik araçlarla birleştirerek harici verilere veya hesaplamalara dayalı model yanıtlarının katı bir şemaya uymaya devam etmesini sağlayabilirsiniz.

Kod örnekleri için [Araçlarla yapılandırılmış çıkışlar](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=tr#structured_outputs_with_tools) başlıklı makaleye bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-04-29 UTC."],[],[]]
