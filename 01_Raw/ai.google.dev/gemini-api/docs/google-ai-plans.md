---
source_url: https://ai.google.dev/gemini-api/docs/google-ai-plans?hl=tr
fetched_at: 2026-09-14T05:39:15.725633+00:00
title: "Google AI planlar\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)

Geri bildirim gönderin

# Google AI planları

AI Studio'da Google AI abonelik planınızı kullanın.

Google AI Pro ve Ultra abonelik planları, ücretsiz katmana kıyasla AI Studio'da prototip oluşturma ve geliştirme için daha fazla model erişimi ve daha yüksek sıklık sınırları sunar.

Google AI planına kaydolmak için Google AI Studio'da sol gezinme menüsündeki **Yükselt** düğmesini tıklayarak doğrudan yükseltme yapabilirsiniz. Alternatif olarak, [Google AI Planları sayfasını](https://one.google.com/about/google-ai-plans/?hl=tr) ziyaret ederek de kaydolabilirsiniz.

## Genel Bakış

Google AI Pro ve Ultra abonelikleri, geliştiricilerin Google AI Studio Playground'da ücretli modellerin ve daha yüksek sıklık sınırlarının kilidini açmasına olanak tanır. Ayrıca, [Build mode](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=tr)'da (Oluşturma modu) Code Assistant (Kod Asistanı) gibi özellikleri kullanarak sezgisel kodlama yapabilirler. Aboneler, [Playground](https://aistudio.google.com/prompts/new_chat?hl=tr) ve [Build](https://aistudio.google.com/apps?hl=tr) arayüzlerinde kullanmak üzere ücretsiz katmandan daha yüksek bir günlük kota hakkı elde eder. Günlük sınırlar, Cloud Faturalandırma ile üretime yönelik ölçekte geliştirmeye geçmeden önce sorunsuz bir geliştirme deneyimi sağlamak için kayan zaman aralıkları yerine sıfırlamalar kullanılarak uygulanır.

| Plan | AI Studio kullanımı | Model erişimi ve avantajlar |
| --- | --- | --- |
| **Ücretsiz** | Az kota | Daha fazla erişim için yükseltme seçeneğiyle birlikte temel sınırlar ve erişim. |
| **AI Pro** | Daha yüksek kota | Gemini Pro, Nano Banana ve Lyria gibi premium modellere erişim |
| **AI Ultra** | En yüksek kota | Prototip oluşturma, geliştirme ve gelişmiş öncü modeller için en yüksek kullanım sınırları. |

## Gemini API kullanımı

AI Studio'da günlük temel abonelik kotaları tükendiğinde, iş akışlarınıza doğrudan Gemini API'nin istek başına ödeme kullanımına yönelik olarak Cloud Faturalandırma'nın etkinleştirildiği bir Gemini API anahtarıyla devam edebilirsiniz.
Projeler ve API anahtarları için Gemini API kullanımı [AI Studio kontrol panelinde](https://aistudio.google.com/projects?hl=tr) gözlemlenebilir.

Google Cloud Platform (GCP) projeleri ve Cloud Billing'i etkinleştirmiş aboneler, Gemini API dahil olmak üzere Cloud hizmetleri için [Google Developer Program](https://developers.google.com/program?hl=tr)'dan aylık Cloud kredisi almaya uygundur. Ön ödemeli ve sonradan ödemeli kullanım ve faturalandırma değişmez. Ön ödemeli faturalandırmayı kullanan kullanıcıların promosyon kredilerini etkinleştirmek için AI Studio'da 0 ABD dolarından fazla ödenmiş bakiyeye sahip olması gerekir. Varsa uygun Google Cloud kredileri öncelikle uygulanır.
[Daha fazla bilgi edinin](https://ai.google.dev/gemini-api/docs/billing?hl=tr#billing-plans).

Google Yapay Zeka aboneliği entegrasyonu, gelişmiş deneme ve geliştirme için giriş eşiğini düşürür. Ancak büyük ölçekli üretim dağıtımları için Google Cloud projeleri, [Google Cloud Başlangıç Katmanı](https://cloud.google.com/blog/topics/developers-practitioners/the-starter-tier-for-google-ai-studio-explained?hl=tr) ve Gemini API anahtarları önerilen yöntemdir.

## Sınırlamalar ve uyumluluk

- **Yalnızca AI Studio kullanıcı arayüzü:** Geliştirici kullanımına yönelik Google AI planı avantajları yalnızca Google AI Studio web arayüzünde geçerlidir. Gemini API'nin doğrudan kullanımı (ör. API anahtarlarının veya harici uygulamaların kullanılması) ayrı olarak faturalandırılır ve yönetilir. Ancak aboneliğinizi diğer Google ürünlerinde kullanabilirsiniz ([Google AI Planları](https://one.google.com/about/google-ai-plans/?hl=tr)'na bakın).
- **API faturalandırmasından farklıdır:** AI Studio için Google AI planları, geliştirme ve üretim API kullanımını kapsayan [Gemini API kullanım katmanlarından](https://ai.google.dev/gemini-api/docs/billing?hl=tr) ayrıdır.
- **Google One kredileri:** [Google One yapay zeka kredileri](https://support.google.com/googleone/answer/16287445?hl=tr), AI Studio'da desteklenmeyen ve Google Cloud kredileriyle çakışmayan ayrı bir kredi sistemidir.
- **Aracı erişimi:** AI Studio'daki aracılara (Deep Research ve Antigravity Preview) erişim, Google AI planlarına dahil değildir ve [ücretli bir API anahtarı](https://ai.google.dev/gemini-api/docs/billing?hl=tr#setup-billing) gerektirir.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-08-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-08-19 UTC."],[],[]]
