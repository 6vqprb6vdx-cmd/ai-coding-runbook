---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=tr
fetched_at: 2026-06-15T06:17:56.347630+00:00
title: "Google AI Studio'da uygulama geli\u015ftirme \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Google AI Studio'da uygulama geliştirme

Bu sayfada, Google AI Studio'yu kullanarak Gemini'ın [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) ve [Live API](https://ai.google.dev/gemini-api/docs/live?hl=tr) gibi en yeni özelliklerini test eden uygulamaları hızlıca oluşturma (veya "vibe code") ve dağıtma açıklanmaktadır. Google AI Studio, doğal dil istemiyle tam yığın çalışma zamanlarına sahip **web uygulamaları** ve Kotlin ile Jetpack Compose kullanılarak oluşturulan **yerel Android uygulamaları** geliştirmeyi destekler.

## Başlayın

Google AI Studio'nun [Build mode](https://aistudio.google.com/apps?hl=tr)'unda (Geliştirme modu) sezgisel kodlamaya başlayın. İnşa etmeye başlamanın birkaç yolu vardır:

- **İstemle başlayın**: Oluşturma modunda, giriş kutusunu kullanarak oluşturmak istediğiniz öğenin açıklamasını girin. İsteminize görüntü üretme veya Google Haritalar verileri gibi belirli özellikleri eklemek için Yapay Zeka Çipleri'ni seçin. Hatta sesle yazma düğmesini kullanarak ne istediğinizi söyleyebilirsiniz.
- **"Kendimi Şanslı Hissediyorum" düğmesi**: Yaratıcı bir başlangıca ihtiyacınız varsa "Kendimi Şanslı Hissediyorum" düğmesini kullanın. Gemini, başlamanıza yardımcı olacak bir proje fikri içeren istem oluşturur.
- **Galerideki bir projeyi remiksleme**: [Uygulama Galerisi](https://aistudio.google.com/apps?source=showcase&hl=tr)'nden bir proje açın ve **Uygulamayı Kopyala**'yı seçin.

İstemi çalıştırdıktan sonra gerekli kod ve dosyaların oluşturulduğunu görürsünüz. Uygulamanızın canlı önizlemesi sağ tarafta gösterilir.

## Ne oluşturulur?

İsteminizi çalıştırdığınızda AI Studio, eksiksiz bir uygulama oluşturur. Platform seçiciyi kullanarak **web uygulaması** veya **yerel Android uygulaması** oluşturmayı seçebilirsiniz.

**Web uygulamaları** (varsayılan) için AI Studio, aşağıdakileri içeren tam yığınlı bir ortam oluşturur:

- **İstemci tarafı**: Bir web ön ucu (varsayılan olarak React kullanılır).
- **Sunucu tarafı**: Güvenli API çağrılarına, veritabanı bağlantılarına ve npm paketi kullanımına olanak tanıyan bir Node.js çalışma zamanı.

AI Studio, **Android uygulamaları** için tarayıcı tabanlı bir emülatörde önizleyebileceğiniz, fiziksel bir cihaza yükleyebileceğiniz ve test için Play Store'da yayınlayabileceğiniz bir Kotlin ve Jetpack Compose projesi oluşturur. [Android uygulamaları oluşturma hakkında daha fazla bilgi edinin](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=tr).

Sağdaki önizleme bölmesinde **Kod** sekmesini seçerek oluşturulan kodu görüntüleyebilirsiniz. **Antigravity Agent**, yığınınızdaki birden fazla dosyayı akıllıca yöneterek değişikliklerin doğru şekilde yayılmasını sağlar.

### The Antigravity Agent

**Antigravity Agent**, [Google Antigravity](https://antigravity.google?hl=tr)'deki temel yapay zeka işlevidir. Artık agent harness'ın temel bileşenleri, Google AI Studio'daki Build modu deneyimine güç veriyor. Tüm projenizin bağlamını koruyarak, birden fazla dosyayı yöneterek ve karmaşık talimatları anlayarak basit kod oluşturmanın ötesine geçer. Böylece sağlam ve tam yığın uygulamalar oluşturabilirsiniz.

Temel özellikler:

- **Bağlam farkındalığı**: Önceki istemlerin ve dosya durumlarının bağlamını korur.
- **Çoklu dosya yönetimi**: Birden fazla dosya arasındaki bağımlılıkları yönetir.
- **Doğrulanmış yürütme**: Halüsinasyonları azaltmak için kod güncellemelerini doğrular.

## Yazılım çapında özellikler

Google AI Studio, modern web ekosisteminin gücünden yararlanmanızı sağlayarak yalnızca istemci tarafı prototipler oluşturmanıza olanak tanır.

- **Sunucu tarafı çalışma zamanı ve npm**: npm paketlerinin geniş kitaplığından yararlanın. Aracı, uygulamanız için gereken paketleri (ör. veri görselleştirme veya API istemcileri için belirli kitaplıklar) otomatik olarak tanımlayıp yükler. İsterseniz belirli paketleri de isteyebilirsiniz.
- **Gizli anahtar yönetimi**: API anahtarlarını ve gizli anahtarları **Ayarlar** menüsünde güvenli bir şekilde saklayın. Bunlara sunucu tarafı kodunuzdan erişilebilir ve istemci tarafı maruziyetten korunur.
- **Çok oyunculu**: Doğrudan AI Studio'da gerçek zamanlı ortak çalışma deneyimleri oluşturun. Sunucu tarafı çalışma zamanı, kullanıcıların birlikte etkileşimde bulunması için gereken durumu ve bağlantıları yönetir.
- **Firebase Firestore ve Authentication**: Firestore veritabanı (kalıcı veri depolama) ve Firebase Authentication ("Google ile oturum açma" özelinde oturum açma akışları) dahil olmak üzere Firebase'i otomatik olarak sağlama ve ayarlama.
  Aracı, tüm kurulum sürecini yönetir ve hatta bu hizmetler için uygulamanızdaki kodu yazar.
- **Google Workspace entegrasyonları**: Uygulamanızı Gmail, E-Tablolar, Dokümanlar, Drive ve Takvim gibi Google Workspace API'lerine bağlayın. AI Studio, tüm OAuth yapılandırmasını otomatik olarak gerçekleştirir.

[Tam yığın uygulamalar geliştirme hakkında daha fazla bilgi edinin](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=tr).

### Android uygulamaları

Ayrıca Kotlin ve Jetpack Compose kullanarak yerel Android uygulamaları da oluşturabilirsiniz.
Uygulamanızı tarayıcı tabanlı bir Android emülatöründe önizleyin, tarayıcıda ADB kullanarak fiziksel bir cihaza yükleyin ve dahili test için Play Store'da yayınlayın.

[Android uygulamaları oluşturma hakkında daha fazla bilgi edinin](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=tr).

## Geliştirmeye devam etme

Google AI Studio, uygulamanız için ilk kodu oluşturduktan sonra kodu iyileştirmeye devam edebilirsiniz:

### Google AI Studio'da geliştirme

- **Gemini ile yineleme yapma**: Gemini'a değişiklik yapmasını, yeni özellikler eklemesini veya stili değiştirmesini istemek için **Oluşturma modundaki** sohbet panelini kullanın.
- **Kodu doğrudan düzenleme**: Canlı düzenlemeler yapmak için önizleme panelinde **Kod sekmesini** açın.

### Harici olarak geliştirme

Daha gelişmiş iş akışları için kodu dışa aktarabilir ve tercih ettiğiniz ortamda çalışabilirsiniz:

- **İndirin ve yerel olarak geliştirin**: Oluşturulan kodu **ZIP dosyası** olarak dışa aktarın ve kod düzenleyicinize aktarın.
- **GitHub'a gönderme**: Kodu bir **GitHub deposuna** göndererek mevcut geliştirme ve dağıtım süreçlerinize entegre edin.

## Temel özellikler

Google AI Studio, geliştirme sürecini sezgisel ve görsel hale getirmek için çeşitli özellikler içerir:

- **Tam yığın uygulamalar oluşturma ve üzerinde yineleme yapma**: Yalnızca bir istemle tam yığın uygulamalar oluşturun ve sohbet ya da **not ekleme modu** aracılığıyla yineleme yapın. Not ekleme modu, uygulamanızın kullanıcı arayüzünün herhangi bir bölümünü vurgulamanıza ve istediğiniz değişikliği açıklamanıza olanak tanır.
- **Uygulamanızı paylaşma ve dağıtma**: Oluşturduğunuz içerikleri başkalarıyla paylaşarak ortak çalışabilir veya çalışmalarınızı sergileyebilirsiniz. Paylaşım sırasında API çağrıları, kullanım sınırlarınıza dahil edilir. Ücretli modelleri kullanırsanız maliyetler söz konusu olabilir. Ardından, uygulamanız hazır olduğunda Cloud Run'a dağıtın.
- **Uygulama galerisi**: Uygulama Galerisi, proje fikirlerinin görsel kitaplığını sunar.
  Gemini ile neler yapabileceğinizi keşfedebilir, uygulamaların önizlemesini anında görebilir ve bunları kendi tarzınıza göre yeniden düzenleyebilirsiniz.

## Uygulamanızı dağıtma veya arşivleme

Uygulamanız hazır olduğunda dağıtabilirsiniz:

- **Cloud Run**: Uygulamanızı ölçeklenebilir bir hizmet olarak dağıtın.
  [Google Cloud Run](https://cloud.google.com/run?hl=tr) fiyatlandırması, kullanıma bağlı olarak geçerli olabilir. Dağıtım hakkında daha fazla bilgi edinmek için [Google AI Studio'dan dağıtma](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=tr) başlıklı makaleyi inceleyin.
- **GitHub**: Projenizi bir GitHub deposuna aktarın.

## Sınırlamalar

Bu bölümde, Google AI Studio'daki derleme modunun mevcut sınırlamaları listelenmektedir.

### API anahtarı yönetimi

Gemini API'yi kullanan yeni bir uygulama oluşturduğunuzda AI Studio, Gemini API anahtarınızı uygulamanın sunucu tarafı ortamında otomatik olarak gizli olarak yapılandırır.
Bu anahtarı **Sırlar** panelinde görüntüleyip yönetebilirsiniz.

- **Otomatik kurulum**: `GEMINI_API_KEY` sizin için kurulur. Oluşturmaya başlamak için manuel yapılandırma gerekmez.
- **Yalnızca sunucu tarafı**: API anahtarları sunucu tarafı çalışma zamanına yerleştirilir ve hiçbir zaman istemci tarafı koduna dahil edilmez.
- **Mevcut uygulamalar**: 14 Mayıs 2026'dan önce oluşturulan uygulamalarda, uygulamadaki Gemini özelliklerini bir sonraki değiştirişinizde aracı, Gemini API entegrasyonunuzu otomatik olarak önerilen sunucu tarafı yaklaşımına yükseltir.

### Google AI Studio dışında dağıtım

- **Cloud Run**: AI Studio'dan Cloud Run'a dağıtım yaptığınızda API anahtarınız sunucu tarafı ortamına güvenli bir şekilde dahil edilir. Dağıtılan uygulama, tüm kullanıcıların Gemini API çağrıları için API anahtarınızı kullanır.
- **ZIP olarak indirme**: Uygulamanızı başka bir yerde çalıştırmak için ZIP dosyası olarak indirirseniz barındırma ortamınızda `GEMINI_API_KEY` ortam değişkenini
  ayarlamanız gerekir. Uygulamanızın Gemini API çağrıları sunucu tarafı kodundan yapıldığından anahtar, son kullanıcılara gösterilmez.

### Uygulamalar paylaşılırken hata oluşuyor

Uygulamanızı paylaştığınızda son kullanıcınız paylaşılan URL'yi kullanırken **403 Erişim Kısıtlandı** hatasıyla karşılaşıyorsa bunun nedeni aşağıdakilerden biri olabilir:

- **Tarayıcı uzantıları**: Privacy Badger gibi gizlilik uzantıları uygulamayı engelliyor olabilir. Hatayı önlemek için uzantıyı devre dışı bırakın.
- **Derleme sorunları**: Mevcut kodla ilgili sorunlar olabilir. Aracıdan "mevcut kodla ilgili derleme sorunlarını düzeltmesini" isteyin ve ardından URL'yi yeniden paylaşın.

## SSS

### AI Studio'da Build nedir?

AI Studio Build, Gemini'ı kullanarak basit bir istemden üretime hazır, yapay zeka destekli bir uygulamaya geçmenizi sağlamak için tasarlanmış bir platformdur. Ne oluşturmak istediğinizi bir istemle açıklayın. Gemini sizin için bir uygulama oluşturur. Ayrıca, Gemini API ile neler yapabileceğinizi görmek için galerimize göz atabilir ve uygulamaları remiksleyerek kendinize göre düzenleyebilirsiniz.

### Build, Gemini API anahtarımı nasıl işler?

Gemini API'yi kullanan bir uygulama oluşturduğunuzda AI Studio, Gemini API anahtarınızı otomatik olarak sunucu tarafı gizli anahtarı olarak ayarlar. Uygulamanızın Gemini API çağrıları, bu anahtar kullanılarak sunucu tarafı kodundan yapıldığından tarayıcıda hiçbir zaman gösterilmez. API anahtarınızı Ayarlar'daki **Gizli Anahtarlar** panelinde görüntüleyebilirsiniz.

### Uygulamaları paylaşırken API anahtarım açığa çıkar mı?

Hayır. API anahtarınız sunucu tarafında gizli olarak saklanır ve hiçbir zaman istemci tarafı koduna dahil edilmez. Uygulamanızı paylaştığınızda diğer kullanıcılar uygulamayı kullanabilir ancak API anahtarınızı göremez.

Uygulamalarınızı başkalarıyla paylaşırken API çağrıları, kullanım sınırlarınıza dahil edilir.
Ücretli modelleri kullanırsanız maliyetler söz konusu olabilir. AI Studio, kurulum sırasında ve paylaşmadan önce uygulamanızın maliyet oluşturup oluşturmayacağı konusunda sizi uyarır.

### Uygulamalarımı kimler görebilir?

Uygulamanız varsayılan olarak özeldir. Uygulamanızı diğer kullanıcılarla paylaşarak kullanmalarını sağlayabilirsiniz. Uygulamanızı paylaştığınız kullanıcılar, uygulamanın kodunu görebilir ve kendi amaçları için kodu çatallayabilir. Uygulamanızı düzenleme izniyle paylaşırsanız diğer kullanıcılar uygulamanızın kodunu düzenleyebilir.

### Uygulamaları Yapay Zeka Stüdyosu dışında çalıştırabilir miyim?

Evet. Uygulamanızı AI Studio'dan [Cloud Run](https://cloud.google.com/run?hl=tr)'a dağıtabilirsiniz. Bu sayede uygulamanız, sunucu tarafı ortamında API anahtarınız güvenli bir şekilde yapılandırılmış olarak herkese açık bir URL'ye sahip olur. Uygulamanızı ZIP dosyası olarak indirip başka bir yerde de barındırabilirsiniz. Bu durumda, barındırma ortamınızda `GEMINI_API_KEY` ortam değişkenini ayarlamanız gerekir. Gemini API çağrıları sunucu tarafı kodundan yapıldığından anahtarınız güvende kalır.

Dağıtım seçenekleri hakkında daha fazla bilgi edinmek için [Google AI Studio'dan dağıtma](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=tr) başlıklı makaleyi inceleyin.

### Uygulamaları kendi araçlarımla yerel olarak geliştirip burada paylaşabilir miyim?

Bu işlev henüz kullanılamıyor. Gelecekte uygulamalar için daha fazla kullanım alanını desteklemeyi heyecanla bekliyoruz. Aklınızda belirli bir şey varsa lütfen geri bildirimde bulunun.

### Uygulamalarımda veritabanı veya başka bir depolama alanı nasıl kullanabilirim?

AI Studio uygulamaları, Cloud Run container'ında çalışan standart uygulamalardır. Dinamik IP aralığından erişimi engelleyen bir güvenlik duvarı olmadığı sürece, ağ üzerinden bağlanabileceğiniz herhangi bir depolama çözümünü kullanabilirsiniz.

Gelecekte depolama için doğrudan destek eklemek üzere çalışıyoruz. Bu desteği doğrudan AI Studio'da yapılandırabileceksiniz.

### Mikrofona, web kamerasına ve diğer Navigator API'lerine nasıl erişebilirim?

İzleyicilerin, bir uygulamanın web kamerasını veya diğer cihazlarını kullanımından haberdar olmasını sağlamak için uygulama bu [Navigator API'lerine](https://developer.mozilla.org/en-US/docs/Web/API/Navigator) erişmeden önce ek bir onay vermesini zorunlu tutarız.
Uygulama geliştiriciler, bu izin isteklerini uygulamalarının `metadata.json` dosyasına ekleyebilir. Örneğin:

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

`requestFramePermissions` için desteklenen değerler, standart [politika kontrollü özelliklerin](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md) bir alt kümesidir.

### GitHub'ı uygulamalarımla nasıl kullanabilirim?

AI Studio'nun GitHub entegrasyonu, çalışmalarınız için bir depo oluşturmanıza ve en son değişikliklerinizi kaydetmenize olanak tanır. Uzak değişikliklerin çekilmesi şu anda desteklenmemektedir.

### Diğer kullanıcılara uygulamamda düzenleme erişimi verebilir miyim?

Bu özellik henüz desteklenmemektedir ancak yakında desteklenecektir.

### Uygulamam neden politika ihlali nedeniyle işaretlendi?

Uygulamaların politikalarımıza uygunluğunu sağlamak için otomatik olarak inceleyen sistemlerimiz vardır. Bir uygulamanın politikalarımızı ihlal ettiğini tespit edersek uygulama AI Studio'dan kaldırılır. Politika ihlalleri aşağıdakileri kapsar ancak bunlarla sınırlı değildir:

- Kötü amaçlı yazılım, kimlik avı veya kimliğe bürünme içeren uygulamalar
- Çocukların cinsel istismarı nitelikli görsel politikasını ihlal eden içerikler gösteren veya dağıtan uygulamalar
- Taciz politikasını ihlal eden içerikler gösteren veya dağıtan uygulamalar
- Nefret söylemi politikasını ihlal eden içerikler gösteren veya dağıtan uygulamalar
- İnsan ticareti politikasını ihlal eden içerikleri gösteren veya dağıtan uygulamalar
- Müstehcen içerik politikası'nı ihlal eden içerikleri gösteren veya dağıtan uygulamalar
- Şiddet ve kan politikalarını ihlal eden içerikleri gösteren veya dağıtan uygulamalar
- Zararlı veya tehlikeli içerik politikalarını ihlal eden içerik gösteren ya da dağıtan uygulamalar

Uygulamanız politika ihlali nedeniyle işaretlendiyse ve bunun hatalı olduğunu düşünüyorsanız itirazda bulunabilirsiniz. Politikalarımızın tekrarlı şekilde ihlal edilmesi, AI Studio'ya erişiminizin sonlandırılmasına neden olabilir.

### Uygulama geliştirici olarak sorumluluklarım nelerdir?

Uygulamanızın sahibi olarak, uygulamanızın davranışından ve işlediği tüm verilerden sorumlu olduğunuzu hatırlatırız. Bunlardan bazıları:

- **Yasal Uygunluk ve Üçüncü Taraf Hakları:** Uygulamanızın geçerli tüm yasalara ve düzenlemelere uygun olmasını ve fikri mülkiyet ile gizlilik hakları da dahil olmak üzere başkalarının haklarını ihlal etmemesini sağlama.
- **İçerik İzleme:** Uygulamanızın kullandığı diğer hizmetler için ek şartlara uyulması gerekebilir. Örneğin, Firestore için geçerli olan [Google Cloud Hizmet Şartları](https://cloud.google.com/terms?hl=tr), üçüncü taraf içeriği barındıran müşterilerin hangi içeriğin yasaklandığını (ör. yasa dışı içerik) tanımlayan politikalar yayınlamasını ve bu yasa dışı içeriğin varlığını izlemesini zorunlu kılar.
- **Güvenli uygulama:** Uygulamanızın kötüye kullanılmasını önlemek için gerekli güvenlik önlemlerini ve moderasyon araçlarını uygulama.

Hizmet Şartları'ndaki [kullanım kısıtlamalarına](https://ai.google.dev/gemini-api/terms?hl=tr#use-restrictions) dikkat edin.

### AI Studio'daki uygulama galerisinde yer alan uygulamalar için hangi şartlar geçerlidir?

Aksi belirtilmediği sürece, AI Studio'daki uygulama galerisinde yer alan uygulamaların kullanımında [Gemini API Ek Hizmet Şartları](https://ai.google.dev/gemini-api/terms?hl=tr) geçerlidir.

## Sırada ne var?

- [Tam Yığın Uygulamaları Geliştirme](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=tr) (web)
- [Android Uygulamaları Geliştirme](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=tr)
- [Uygulama Galerisi](https://aistudio.google.com/apps?source=showcase&hl=tr)'ndeki örneklere bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-19 UTC."],[],[]]
