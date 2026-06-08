---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=tr
fetched_at: 2026-06-08T14:55:41.779376+00:00
title: "Gemini Developer API'de veri saklama s\u00fcresi yoktur \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini Developer API'de veri saklama süresi yoktur

Bu sayfada, Gemini Developer API'sinde genellikle "sıfır veri saklama" olarak adlandırılan özellik hakkında ayrıntılı bilgiler verilmektedir.

## Eğitim kısıtlaması

[Gemini API Hizmet Şartları](https://ai.google.dev/gemini-api/terms?hl=tr)'nda belirtildiği gibi, Ücretli Hizmetler'i kullandığınızda Google, ürünlerimizi iyileştirmek için istemlerinizi (ilişkili sistem talimatları, önbelleğe alınmış içerik ve resim, video veya belge gibi dosyalar dahil) ya da yanıtlarınızı kullanmaz. Ücretli Hizmetler [burada](https://ai.google.dev/gemini-api/terms?hl=tr#paid-services) tanımlanmıştır.

## Müşteri verilerini saklama ve sıfır veri saklama hedefine ulaşma

Müşteri verileri genellikle aşağıdaki senaryo ve koşullarda sınırlı süreler boyunca saklanır. Veri saklama süresinin sıfır olması için müşterilerin bu alanların her birinde belirli işlemleri yapması veya belirli özelliklerden kaçınması gerekir:

- **Kötüye kullanım izleme için istem günlüğü**: [Gemini API Ek Hizmet Şartları](https://ai.google.dev/gemini-api/terms?hl=tr)'nda belirtildiği gibi, Ücretli Hizmetler için Google, [Yasaklanan Kullanım Politikası](https://policies.google.com/terms/generative-ai/use-policy?hl=tr)'nın ihlallerini tespit etmek amacıyla istemleri ve yanıtları sınırlı bir süre boyunca kaydeder. Belirli bir proje için ZDR isteğiniz onaylandığında, tüm kullanıcı içeriği (istemler ve yanıtlar) ve tanımlanabilir meta veriler (ör. IP adresleri ve Google Hesabı kimlikleri) günlüğe kaydetmeden önce temizlenir. Elde edilen kayıt, temizlenmiş olarak işaretlenir ve tanımlanabilir kullanıcı verisi içermez. Bu sayede, Gemini Enterprise Agent Platform Zero Data Retention ile eşitlik sağlanır.
- **Google Arama ile temellendirme**: [Gemini API Ek Hizmet Şartları](https://ai.google.dev/gemini-api/terms?hl=tr#grounding-with-google-search)'nda belirtildiği gibi Google, temellendirilmiş sonuçlar ve arama önerileri oluşturmak amacıyla istemleri, bağlamsal bilgileri ve oluşturulan çıkışları otuz (30) gün boyunca saklar.
  Bu depolanmış bilgiler, temellendirmeyi destekleyen sistemlerin hata ayıklaması ve test edilmesi için kullanılabilir. **Google Arama ile Temellendirme'yi kullanıyorsanız bu bilgilerin depolanmasını devre dışı bırakmanın bir yolu yoktur.**
- **Google Haritalar ile temellendirme**: [Gemini API Ek Hizmet Şartları](https://ai.google.dev/gemini-api/terms?hl=tr)'nda belirtildiği gibi Google, temellendirilmiş sonuçlar oluşturmak amacıyla istemleri, bağlamsal bilgileri ve oluşturulan çıkışları otuz (30) gün boyunca saklar. Bu saklanan bilgiler yalnızca güvenilirlik mühendisliği için (ör. hizmet sorunları durumunda hata ayıklama) kullanılabilir.
  **Google Haritalar ile Temellendirme'yi kullanıyorsanız bu bilgilerin depolanmasını devre dışı bırakmanın bir yolu yoktur.**
- **Interactions API**: Interactions API, çok turlu etkileşimleri etkinleştirmek için bir görüşmenin etkin durumunu yönetir. **Etkileşimler API'si, varsayılan olarak durum depolamayı etkinleştirir**. Veri ayak izinin sıfır olmasını sağlamak için varsayılan durum tutma özelliğini devre dışı bırakmak üzere API isteklerinizde `store` parametresini açıkça `false` olarak ayarlamanız gerekir.
- **Live API**: Bu durum bilgisi olan API, görüşme durumunu saklayarak gerçek zamanlı yeniden bağlantıya olanak tanır. Veri saklama süresini sıfıra indirmek için **SessionResumptionConfig'i yapılandırmayın**. Oturum tanıtıcısı oluşturulursa sohbet durumu (metin, ses ve video dahil) 24 saate kadar saklanır.
- **File API Storage**: File API, kullanıcıların büyük öğeler yüklemesine olanak tanır.
  Dosyalar, kullanıcı tarafından silinene veya süreleri dolana kadar hareketsiz olarak saklanır.
  File API'nin kullanımı ZDR günlüğünden bağımsızdır. Kullanıcıların sıfır veri ayak izi sağlamak için dosyaları manuel olarak silmesi gerekir.
- **Açık Bağlam Önbelleğe Alma**: Kullanıcılar, `cached_content` alanını kullanarak büyük veri kümelerini (ör. uzun videolar veya belge kitaplıkları) manuel olarak önbelleğe alabilir. Bu isteklerin günlükleri ZDR bırakma politikalarına uygun olsa da önbelleğe alınan bağlamın kendisi kullanıcı tanımlı bir `ttl` veya `expire_time` ile depolanır. Mutlak sıfır veri ayak izi elde etmek için cached\_content özelliğini kullanmayın.
- **Örtülü Bellek İçi Önbelleğe Alma**: Gemini modelleri, geliştiriciler için gecikmeyi ve maliyeti azaltmak amacıyla verileri varsayılan olarak bellek içinde önbelleğe alır. Bu veriler kesinlikle RAM'de (aktif olmayan durumda değil) bulunur, proje düzeyinde izole edilir ve 24 saatlik bir TTL'ye sahiptir.
  **Bu, sıfır veri saklama politikasını ihlal etmez.**

## Sırada ne var?

- [Üretken Yapay Zeka Yasaklanan Kullanım Politikası](https://policies.google.com/terms/generative-ai/use-policy?hl=tr) hakkında bilgi edinin.
- [Gemini API Ek Hizmet Şartları](https://ai.google.dev/gemini-api/terms?hl=tr)'nı inceleyin.
- Kurumsal düzeyde, self servis ZDR kontrolleri gerekiyorsa [Gemini Enterprise Ajan Platformu
  Sıfır Veri Saklama
  rehberine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=tr) bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-28 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-28 UTC."],[],[]]
