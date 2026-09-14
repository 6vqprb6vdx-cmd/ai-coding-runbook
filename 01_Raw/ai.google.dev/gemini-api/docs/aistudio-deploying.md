---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=tr
fetched_at: 2026-09-14T05:50:56.858499+00:00
title: "Google AI Studio'dan da\u011f\u0131tma \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Google AI Studio'dan dağıtma

Google AI Studio, full-stack uygulamalarınızı doğrudan Oluşturma Modu'ndan dağıtmanıza olanak tanır. Bu sayede prototipten yönetilen ve ölçeklenebilir bir üretim ortamına hızlı bir şekilde geçebilirsiniz.

## Dağıtım seçenekleri

Uygulamanızı AI Studio'nun Oluşturma Modu'ndan dağıtmak için kullandığınız katmana bağlı olarak aşağıdaki şartları karşılamanız gerekir:

- [**Google Cloud Başlangıç Katmanı**](https://docs.cloud.google.com/docs/starter-tier?hl=tr):
  Google Cloud projesi veya faturalandırma hesabı oluşturmadan 2 tam yığın uygulaması yayınlamanıza olanak tanır.
- **Standart dağıtım**: AI Studio hesabınıza bağlı bir Google Cloud projesi ve bu projede faturalandırmanın etkinleştirilmesi gerekir.

## Başlangıç Seviyesi hakkında

Google Cloud Başlangıç Katmanı, tam bir Google Cloud ortamı veya faturalandırma hesabı oluşturmadan uygulamaları doğrudan Google AI Studio'dan Google Cloud'a dağıtmak için kolay bir yol sunar.

Her Google AI Studio dağıtımı, Cloud Run'da karşılık gelen bir hizmet oluşturur. Başlangıç Katmanı ile Google AI Studio'da dağıtılan hizmetler için aşağıdaki sınırlamalar geçerlidir:

- En fazla iki hizmet dağıtabilirsiniz.
- Hizmetleriniz [tek bir Cloud Run bölgesinde](https://docs.cloud.google.com/run/docs/locations?hl=tr) dağıtılmış olmalıdır.

## Başlangıç Seviyesi dağıtım adımları

Uygulamanızı Oluşturma modunda tasarladıktan sonra Başlangıç Katmanı ile dağıtın:

1. Sağ üst köşedeki **Yayınla** düğmesini tıklayın.
2. **Get Started**'ı (Başlayın) tıklayın.
3. **Uygulamayı Yayınla**'yı tıklayın.

Dağıtım tamamlandıktan sonra AI Studio, canlı uygulamanıza erişebileceğiniz bir Cloud Run URL'si sağlar.

## AI Studio için özel URL'ler

Google AI Studio'dan bir uygulama yayınlarken `ai.studio` altında özel ve akılda kalıcı bir alt alan adı ayarlayabilirsiniz (örneğin, `https://your-app-name.ai.studio`).

Google AI Studio, alt alan adlarının tüm projelerde genel olarak benzersiz olmasını gerektirir ve bunları ilk gelene ilk hizmet esasına göre atar. Başka bir proje zaten bir ad kullanıyorsa AI Studio, farklı bir ad seçmenizi ister. Bir uygulamayı yayından kaldırırsanız veya silerseniz özel URL'si serbest bırakılır ve diğer kullanıcılar tarafından talep edilebilir.

### Özel URL ayarlama

Uygulamanız için özel URL ayarlamak veya güncellemek üzere:

1. Google AI Studio'da uygulamanızı **Build** (Oluştur) modunda açın.
2. Sağ üst köşedeki **Yayınla**'yı tıklayın.
3. Dağıtım yapılandırmasında, tercih ettiğiniz alt alan adını **Özel URL** alanına girin veya önerilen URL'yi kabul edin.
4. **Uygulamayı Yayınla**'yı tıklayın.

Mevcut bir özel URL'yi farklı bir uygulamaya aktarmak için önce bu özel URL'nin atandığı uygulamayı yayından kaldırmanız veya silmeniz, ardından seçilen alt alan adını kullanarak yeni uygulamanızı yayınlamanız gerekir.

### Ticari marka veya telif hakkı sorunlarını bildirme

Özel alt alan adları, [Google Hizmet Şartları](https://policies.google.com/terms?hl=tr)'na uygun olmalıdır. Ticari markayı ihlal eden veya telif hakkıyla korunan bir adı izinsiz kullanan özel URL'leri [Google Yasal Sorun Giderici](https://support.google.com/legal/troubleshooter/1114905?hl=tr)'yi kullanarak bildirebilirsiniz.

## Standart dağıtım

Uygulamalarınız geliştikçe Başlangıç Katmanı'nın ötesinde özelliklere (ör. daha yüksek kotalar, daha fazla işlem kaynağı veya Başlangıç Katmanı'nda bulunmayan diğer Google Cloud ürünleri) ihtiyacınız olabilir. Bu özelliklerden yararlanmak için tamamen yönetilen Başlangıç Katmanı projenizi standart bir Google Cloud projesine dönüştürebilirsiniz.

Bu sayede, ilerlemenizi kaybetmeden sorunsuz bir şekilde ölçeklendirme yapabilirsiniz. [Cloud Billing hesabı oluşturma](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=tr#create-new-billing-account), standart Google Cloud Hizmet Şartları'nı resmen kabul etme ve [standart Google Cloud projesine yükseltme](https://docs.cloud.google.com/docs/starter-tier?hl=tr#upgradee) adımlarını uygulayın.
Daha fazla bilgi için [Ücretli hesaplar için kurulum](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=tr#paid-setup) başlıklı makaleyi inceleyin.

Faturalandırma katmanları hakkında daha fazla bilgi edinmek için [Faturalandırma](https://ai.google.dev/gemini-api/docs/billing?hl=tr) başlıklı makaleyi inceleyin.

## Başvurunuzu silme

Uygulamanıza artık ihtiyacınız yoksa aşağıdaki talimatları uygulayarak Google AI Studio'da silebilirsiniz:

1. Google AI Studio'da [Uygulamalar sayfanıza](https://aistudio.google.com/app/apps?hl=tr) gidin.
2. Sol menüden **Uygulamalar**'ı seçin.
3. İşaretçiyi silmek istediğiniz uygulamanın üzerine getirin.
4. Uygulamayı silmek için satırın sağ tarafındaki çöp kutusu simgesini tıklayın.

## Sırada ne var?

- [Google Cloud Başlangıç Katmanı](https://docs.cloud.google.com/docs/starter-tier?hl=tr) hakkında daha fazla bilgi edinin.
- Gemini API'de [Faturalandırma](https://ai.google.dev/gemini-api/docs/billing?hl=tr) hakkında bilgi edinin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-10 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-10 UTC."],[],[]]
