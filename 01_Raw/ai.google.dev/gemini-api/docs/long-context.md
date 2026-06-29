---
source_url: https://ai.google.dev/gemini-api/docs/long-context?hl=tr
fetched_at: 2026-06-29T05:27:40.746201+00:00
title: "Uzun ba\u011flam \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Uzun bağlam

Birçok Gemini modelinde 1 milyon veya daha fazla parçalık büyük bağlam pencereleri bulunur.
Geçmişte büyük dil modelleri (LLM'ler), modele aynı anda iletilebilecek metin (veya jeton) miktarıyla ilgili önemli sınırlamalara sahipti.
Gemini'ın uzun bağlam penceresi, birçok yeni kullanım alanının ve geliştirici paradigmasının kilidini açıyor.

[Metin oluşturma](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr) veya [çok formatlı girişler](https://ai.google.dev/gemini-api/docs/vision?hl=tr) gibi durumlar için kullandığınız kod, uzun bağlamla birlikte herhangi bir değişiklik yapmadan çalışır.

Bu belgede, 1 milyon ve daha fazla parçalık bağlam pencerelerine sahip modelleri kullanarak neler yapabileceğiniz hakkında genel bir bakış sunulmaktadır. Bu sayfada, bağlam penceresiyle ilgili kısa bir genel bakış sunulmakta ve geliştiricilerin uzun bağlam, uzun bağlamın çeşitli gerçek dünya kullanım alanları ve uzun bağlam kullanımını optimize etme yöntemleri hakkında nasıl düşünmesi gerektiği ele alınmaktadır.

Belirli modellerin bağlam penceresi boyutları için [Modeller](https://ai.google.dev/gemini-api/docs/models?hl=tr) sayfasına bakın.

## Bağlam penceresi nedir?

Gemini modellerini kullanmanın temel yolu, modele bilgi (bağlam) iletmektir. Model daha sonra bir yanıt oluşturur. Bağlam penceresi, kısa süreli belleğe benzetilebilir. Kullanıcıların kısa süreli hafızasında sınırlı miktarda bilgi depolanabilir. Bu durum, üretken modeller için de geçerlidir.

Modellerin nasıl çalıştığı hakkında daha fazla bilgiyi [üretken modeller kılavuzumuzda](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=tr#under-the-hood) bulabilirsiniz.

## Uzun bağlamı kullanmaya başlama

Üretken modellerin önceki sürümleri,tek seferde yalnızca 8.000 jeton işleyebiliyordu. Daha yeni modeller, 32.000 hatta 128.000 jeton kabul ederek bu sınırı daha da ileriye taşıdı. Gemini, 1 milyon jeton kabul edebilen ilk modeldir.

Pratikte 1 milyon jeton şöyle görünür:

- 50.000 satır kod (satır başına standart 80 karakterle)
- Son 5 yılda gönderdiğiniz tüm kısa mesajlar
- 8 ortalama uzunlukta İngilizce roman
- Ortalama uzunlukta 200'den fazla podcast bölümünün transkripti

Diğer birçok modelde yaygın olan daha sınırlı bağlam pencereleri genellikle jeton tasarrufu için eski mesajları rastgele bırakma, içeriği özetleme, vektör veritabanlarıyla RAG kullanma veya istemleri filtreleme gibi stratejiler gerektirir.

Bu teknikler belirli senaryolarda değerli olmaya devam etse de Gemini'ın geniş bağlam penceresi daha doğrudan bir yaklaşımı mümkün kılar: tüm ilgili bilgileri en baştan sağlamak. Gemini modelleri, büyük bağlam yetenekleriyle özel olarak geliştirildiğinden bağlam içi öğrenme konusunda güçlü bir performans gösterir. Örneğin, yalnızca bağlam içi eğitici materyaller (500 sayfalık bir referans dil bilgisi, bir sözlük ve yaklaşık 400 paralel cümle) kullanılarak Gemini, aynı materyalleri kullanan bir insan öğrenenle benzer kalitede, 200'den az konuşanı olan bir Papua dili olan Kalamang'dan İngilizceye [çeviri yapmayı öğrendi](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf). Bu, Gemini'ın uzun bağlam özelliği sayesinde mümkün olan paradigma değişikliğini gösterir. Bu özellik, bağlam içi güçlü öğrenme yoluyla yeni olanaklar sunar.

## Uzun bağlam kullanım alanları

Çoğu üretken modelin standart kullanım alanı hâlâ metin girişi olsa da Gemini model ailesi, çok formatlı kullanım alanlarında yeni bir paradigma sunuyor. Bu modeller metin, video, ses ve görüntüleri doğal olarak anlayabilir. Bu modeller, [çok formatlı dosya türlerini kabul eden Gemini API](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=tr) ile birlikte sunulur.

### Uzun metin

Metin, LLM'lerle ilgili gelişmelerin temelini oluşturan zeka katmanı olduğunu kanıtlamıştır. Daha önce de belirtildiği gibi, LLM'lerin pratik sınırlamalarının çoğu, belirli görevleri yerine getirmek için yeterince büyük bir bağlam penceresine sahip olmamalarından kaynaklanıyordu. Bu durum, almayla artırılmış üretim (RAG) ve modele dinamik olarak alakalı bağlamsal bilgiler sağlayan diğer tekniklerin hızla benimsenmesine yol açtı. Artık daha büyük bağlam pencereleriyle birlikte yeni kullanım alanları sunan yeni teknikler kullanıma sunuluyor.

Metin tabanlı uzun bağlam için bazı yeni ve standart kullanım alanları şunlardır:

- Büyük metin derlemelerini özetleme
  - Daha küçük bağlam modelleriyle önceki özetleme seçenekleri, yeni jetonlar modele aktarılırken önceki bölümlerin durumunu korumak için kayan bir pencere veya başka bir teknik gerektiriyordu.
- Soru sorma ve yanıtlama
  - Geçmişte, bağlamın sınırlı miktarı ve modellerin olgusal hatırlama oranının düşük olması nedeniyle bu yalnızca RAG ile mümkündü.
- Temsilci tabanlı iş akışları
  - Metin, aracıların yaptıkları ve yapmaları gereken işlemlerin durumunu korumasının temelini oluşturur. Dünya ve aracının hedefi hakkında yeterli bilgiye sahip olmamak, aracıların güvenilirliğini sınırlar.

[Çok örnekli bağlam içi öğrenme](https://arxiv.org/pdf/2404.11018), uzun bağlam modellerinin sunduğu en benzersiz özelliklerden biridir. Araştırmalar, modele bir görevin bir veya birkaç örneğinin sunulduğu ve bunun yüzlerce, binlerce hatta yüz binlerce örneğe çıkarıldığı yaygın "tek görevli" veya "çok görevli" örnek paradigmanın, modelin yeni yetenekler kazanmasına yol açabileceğini göstermiştir. Bu çok görevli yaklaşımın, belirli bir görev için ince ayar yapılmış modellerle benzer performans gösterdiği de kanıtlanmıştır. Gemini modelinin performansının henüz üretime geçiş için yeterli olmadığı kullanım alanlarında çok görevli yaklaşımı deneyebilirsiniz. Uzun bağlam optimizasyonu bölümünde daha sonra inceleyeceğiniz gibi, bağlam önbelleğe alma bu tür yüksek giriş parçası iş yükünü çok daha ekonomik hale getirir ve bazı durumlarda gecikmeyi daha da azaltır.

### Uzun video

Video içeriğinin faydası, uzun süredir ortamın erişilebilirliğinin olmaması nedeniyle kısıtlanıyordu. İçeriği hızlı göz atma zordu, transkriptler genellikle videonun nüansını yakalayamıyordu ve çoğu araç resim, metin ve sesi birlikte işlemiyordu. Gemini ile uzun bağlamlı metin özellikleri, çok formatlı girişlerle ilgili soruları akıl yürüterek yanıtlamaya ve bu sırada performansı korumaya olanak tanır.

Uzun video bağlamıyla ilgili bazı yeni ve standart kullanım alanları şunlardır:

- Video soruları ve yanıtları
- [Google'ın Project Astra](https://deepmind.google/technologies/gemini/project-astra/?hl=tr) ile gösterildiği gibi video belleği
- Video altyazı ekleme
- Mevcut meta verileri yeni çok formatlı anlayışla zenginleştirerek video öneri sistemleri
- Veri kümesi ve ilişkili video meta verilerine bakıp izleyiciyle alakalı olmayan video bölümlerini kaldırarak videoları özelleştirme
- Video içeriği denetimi
- Gerçek zamanlı video işleme

Videolarla çalışırken [videoların jetonlara nasıl işlendiğini](https://ai.google.dev/gemini-api/docs/tokens?hl=tr#media-token) göz önünde bulundurmak önemlidir. Bu durum, faturalandırma ve kullanım sınırlarını etkiler. Video dosyalarıyla istem oluşturma hakkında daha fazla bilgiyi [İstem oluşturma kılavuzunda](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=tr#prompting-with-videos) bulabilirsiniz.

### Uzun ses içerikleri

Gemini modelleri, sesi anlayabilen ilk doğal olarak çok formatlı büyük dil modelleriydi. Geçmişte, tipik geliştirici iş akışında sesi işlemek için konuşmayı metne dönüştürme modeli ve metni metne dönüştürme modeli gibi alana özgü birden fazla modelin bir araya getirilmesi gerekiyordu. Bu durum, birden fazla gidiş-dönüş isteği gerçekleştirilmesinden kaynaklanan ek gecikmeye ve genellikle birden fazla model kurulumunun bağlantısı kesilmiş mimarilerine atfedilen performans düşüşüne yol açtı.

Ses bağlamı için bazı yeni ve standart kullanım alanları şunlardır:

- Anlık metne dönüştürme ve çeviri
- Podcast / video soru-cevap
- Toplantıyı metne dönüştürme ve özetleme
- Sesli asistanlar

Ses dosyalarıyla istem oluşturma hakkında daha fazla bilgiyi [İstem oluşturma kılavuzu](https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python&hl=tr#prompting-with-videos)'nda bulabilirsiniz.

## Uzun bağlam optimizasyonları

Uzun bağlam ve Gemini modelleriyle çalışırken birincil optimizasyon, [bağlam önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr) özelliğini kullanmaktır. Tek bir istekte çok sayıda jetonun işlenmesinin daha önce mümkün olmamasının yanı sıra, diğer temel kısıtlama maliyetti. Kullanıcının 10 PDF, bir video ve bazı iş belgeleri yüklediği bir "verilerinizle sohbet edin" uygulamanız varsa bu istekleri işlemek için geçmişte daha karmaşık bir alma artırılmış oluşturma (RAG) aracı/çerçevesiyle çalışmanız ve bağlam penceresine taşınan jetonlar için önemli bir miktar ödeme yapmanız gerekirdi. Artık kullanıcının yüklediği dosyaları önbelleğe alabilir ve bunları saatlik olarak depolamak için ödeme yapabilirsiniz. Örneğin, Gemini Flash ile istek başına giriş / çıkış maliyeti, standart giriş / çıkış maliyetinden yaklaşık 4 kat daha azdır. Bu nedenle, kullanıcı verileriyle yeterince sohbet ederse bu, geliştirici olarak sizin için büyük bir maliyet tasarrufu sağlar.

## Uzun bağlam sınırlamaları

Bu kılavuzun çeşitli bölümlerinde, Gemini modellerinin çeşitli iğne-samanlıkta-iğne-arama değerlendirmelerinde nasıl yüksek performans elde ettiğinden bahsettik. Bu testlerde, aradığınız tek bir iğnenin olduğu en temel kurulum dikkate alınır. Birden fazla "iğne" veya aradığınız belirli bilgi parçaları olduğunda model aynı doğrulukla çalışmaz. Performans, bağlama bağlı olarak büyük ölçüde değişebilir. Doğru bilgilerin alınması ile maliyet arasında doğal bir denge olduğundan bu durumu göz önünde bulundurmanız önemlidir. Tek bir sorguda yaklaşık% 99 doğruluk elde edebilirsiniz ancak bu sorguyu her gönderdiğinizde giriş jetonu maliyetini ödemeniz gerekir. Bu nedenle, 100 bilgi parçasının alınması için% 99 performans gerekiyorsa muhtemelen 100 istek göndermeniz gerekir. Bu, bağlam önbelleğe almanın, performansı yüksek tutarken Gemini modellerini kullanmayla ilişkili maliyeti önemli ölçüde azaltabileceği iyi bir örnektir.

## SSS

### Sorgumu bağlam penceresinde nereye yerleştirmeliyim?

Çoğu durumda, özellikle de bağlamın tamamı uzunsa sorgunuzu / sorunuzu istemin sonuna (diğer tüm bağlamlardan sonra) yerleştirdiğinizde modelin performansı daha iyi olur.

### Bir sorguya daha fazla jeton eklediğimde model performansı düşer mi?

Genel olarak, jetonların modele iletilmesi gerekmiyorsa iletilmemesi en iyisidir. Ancak, bazı bilgileri içeren büyük bir jeton yığınınız varsa ve bu bilgiler hakkında soru sormak istiyorsanız model, bu bilgileri ayıklama konusunda oldukça başarılıdır (birçok durumda% 99'a varan doğruluk).

### Uzun bağlamlı sorgularla maliyetimi nasıl düşürebilirim?

Çok kez yeniden kullanmak istediğiniz benzer bir jeton / bağlam kümeniz varsa [bağlam önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr), bu bilgilerle ilgili soru sormayla ilişkili maliyetleri azaltmanıza yardımcı olabilir.

### Bağlam uzunluğu, model gecikmesini etkiler mi?

Boyutundan bağımsız olarak, her istekte belirli bir gecikme süresi vardır ancak genellikle daha uzun sorgularda gecikme süresi (ilk jetona kadar geçen süre) daha yüksek olur.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-22 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-22 UTC."],[],[]]
