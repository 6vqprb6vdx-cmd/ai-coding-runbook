---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=tr
fetched_at: 2026-08-24T02:23:54.997765+00:00
title: "Veri g\u00fcnl\u00fck kayd\u0131 ve payla\u015f\u0131m\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Veri günlük kaydı ve paylaşımı

Bu sayfada, faturalandırmanın etkinleştirildiği projeler için desteklenen Gemini API çağrılarından elde edilen ve geliştiricilere ait API verileri olan [Gemini API günlüklerinin](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=tr) depolanması ve yönetilmesi açıklanmaktadır. Günlükler, kullanıcının isteğinden modelin yanıtına kadar olan tüm süreci kapsar.
Google Cloud projenize özel olan bu günlükler, yalnızca [kötüye kullanımı izleme](https://ai.google.dev/gemini-api/docs/usage-policies?hl=tr) amacıyla tutulan günlüklerden ayrıdır.

## Paylaşılabilecek veriler

Proje sahibi olarak, kendi kullanımınız için veya modellerimizi sürekli olarak iyileştirmemize yardımcı olmak üzere Google ile geri bildirim ve paylaşım amacıyla Gemini API çağrılarının günlüğe kaydedilmesini etkinleştirebilirsiniz.

Günlük kaydı etkinleştirildiğinde, ürün iyileştirmeleri ve model eğitimi için aşağıdaki verileri göndermeyi seçerek çeşitli alanlardaki ve kullanım alanlarındaki geliştiriciler için değerli olmaya devam eden yapay zeka sistemleri oluşturmamıza yardımcı olabilirsiniz:

- **Veri kümeleri:** Desteklenen Gemini API çağrılarından ilgilendiğiniz günlükleri (istekler, yanıtlar, meta veriler vb.) seçmek için Google AI Studio'nun Günlükler ve Veri Kümeleri arayüzünü kullanın. Veri kümelerine dahil edilerek katkıda bulunulur. Veri kümesi oluşturma sırasında bu özelliği devre dışı bırakabilirsiniz.
- **Geri bildirim:** Günlükleri incelerken geri bildirimde bulunabilirsiniz. Beğenme ve beğenmeme puanları ile yazdığınız yorumlar bu kapsamdadır.

Google ile bir veri kümesi paylaştığınızda, istekler ve yanıtlar dahil olmak üzere bu veri kümesindeki günlükleriniz, "[Ücretsiz Hizmetler](https://ai.google.dev/gemini-api/terms?hl=tr#data-use-unpaid)" ile ilgili [Şartlarımız](https://developers.google.com/terms?hl=tr) uyarınca işlenir. Bu, veri kümesinin modellerimizi iyileştirmek ve eğitmek de dahil olmak üzere Google ürünlerini, hizmetlerini ve makine öğrenimi teknolojilerini geliştirmek ve iyileştirmek için kullanılabileceği anlamına gelir. **Kişisel, hassas veya gizli bilgiler eklemeyin.**

## Verilerinizi nasıl kullanırız?

Günlükler varsayılan olarak en fazla 55 gün boyunca saklanır. Bu sürenin ardından günlükler otomatik olarak silinmek üzere işaretlenir. Bir projenin saklama süresi penceresi, 7, 14, 28 veya 55 gün sonra günlükleri silinmek üzere otomatik olarak işaretlemek için AI Studio'da güncellenebilir.

Aşağı akış kullanım alanları için belirlenen saklama süresinin ötesinde ilgi çekici günlükleri saklamak ve model iyileştirmelerine isteğe bağlı olarak katkıda bulunmak amacıyla [veri kümeleri](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=tr) oluşturulabilir. Veri kümelerinde depolanan günlüklerin saklama süreleri ayarlanmaz.

Varsayılan olarak, günlük kaydı yalnızca faturalandırmanın etkinleştirildiği projelerde kullanılabilir. Bu nedenle, günlüklerdeki istemler ve yanıtlar, veri kullanımına ilişkin [Şartlarımız](https://developers.google.com/terms?hl=tr) uyarınca ürün iyileştirme veya geliştirme için kullanılmaz.

Günlüklerinizin veri kümelerini Google ile paylaşmayı seçerseniz bu veri kümeleri, yapay zeka sistemlerinin ve uygulamalarının kullanıldığı alanların ve bağlamların çeşitliliğini daha iyi anlamak için gerçek dünya gösterim verileri olarak kullanılır. Bu veriler, model kalitesini artırmak ve gelecekteki modellerin ve hizmetlerin eğitim ve değerlendirme süreçlerine bilgi sağlamak için kullanılabilir. Bu veriler, [Ücretsiz Hizmetler](https://ai.google.dev/gemini-api/terms?hl=tr#data-use-unpaid) için veri kullanım şartlarımıza uygun olarak işlenir.

Bu nedenle, inceleme uzmanları paylaştığınız API girişlerini ve çıkışlarını okuyabilir, işleyebilir ve bunlara açıklama ekleyebilir. Veriler model geliştirmede kullanılmadan önce Google, bu süreç kapsamında kullanıcı gizliliğini korumak için gerekli önlemleri alır. Örneğin, inceleme uzmanları görmeden veya açıklama eklemeden önce bu verilerin Google Hesabınız, API anahtarınız ve Cloud projenizle bağlantısını kaldırırız.

## Veri izinleri

API verilerine katkıda bulunmayı etkinleştirerek Google'ın verileri bu dokümanda açıklandığı şekilde işlemesi ve kullanması için gerekli izinlere sahip olduğunuzu onaylarsınız. **Lütfen ücretli hizmet aracılığıyla elde edilen hassas, gizli veya özel bilgileri içeren günlükler göndermeyin**.
API Şartları'ndaki "[İçerik Gönderme](https://developers.google.com/terms?hl=tr#b_submission_of_content)" bölümü uyarınca Google'a verdiğiniz lisans, Hizmetler'e gönderdiğiniz tüm içerikler (ör.ilişkili sistem talimatları da dahil olmak üzere istemler, önbelleğe alınmış içerikler ve resim, video ya da doküman gibi dosyalar) ve oluşturulan tüm yanıtlar için de geçerlidir. Bu geçerlilik, kullanımımız için geçerli yasalar uyarınca gerekli olduğu ölçüde geçerlidir.

## Veri paylaşımı ve geri bildirim

Verilerinizi örnek olarak paylaşmayı kabul ederek yapay zeka araştırmalarının, Gemini API'nin ve Google AI Studio'nun sınırlarını genişletmemize yardımcı olabilirsiniz. Bu sayede, modellerimizi çeşitli bağlamlarda sürekli olarak iyileştirebilir ve farklı alanlardaki ve kullanım alanlarındaki geliştiriciler için değerli olmaya devam edecek yapay zeka sistemleri oluşturabiliriz.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-08-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-08-19 UTC."],[],[]]
