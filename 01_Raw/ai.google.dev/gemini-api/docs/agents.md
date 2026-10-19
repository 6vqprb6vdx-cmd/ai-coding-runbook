---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=tr
fetched_at: 2026-10-19T05:49:07.329008+00:00
title: "Arac\u0131lara genel bak\u0131\u015f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Aracılara genel bakış

Gemini API'deki yönetilen ajanlar, yapılandırılabilir bir ajan koşumu sağlar. Tek bir API çağrısı, aracının akıl yürüttüğü, kod yürüttüğü, dosyaları yönettiği ve web'de bağımsız olarak gezindiği bir Linux sanal alanı sağlar.

[rocket\_launch

Hızlı başlangıç kılavuzu

İlk ajan görüşmenizi yapın, yanıtları yayınlayın ve özel bir ajan oluşturun.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr)
[smart\_toy

Antigravity Agent

Varsayılan aracının özellikleri, araçları, çok formatlı girişi ve fiyatlandırması.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr)
[experiment

AI Studio'daki temsilciler

Kod yazmadan ajan prototipi oluşturmak için görsel deneme alanı.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=tr)

## Kullanılabilir yönetilen aracıları

- **[Antigravity agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr)**: Gemini 3.8 Flash ile oluşturulmuş genel amaçlı yönetilen ajan. Google tarafından barındırılan güvenli bir Linux sanal alanında kod çalıştırır, dosyaları yönetir ve web'de arama yapar. `agent_config` simgesini kullanarak temel modeli (ör. Gemini 3.6 Flash veya Gemini 3.5 Flash-Lite) yapılandırabilir ve [özel bir aracı oluşturmak](https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr) için kendi talimatlarınız, becerileriniz ve verilerinizle genişletebilirsiniz.
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr)**: Pazar analizi, durum tespiti ve literatür incelemeleri gibi kullanım alanları için çok adımlı araştırma görevlerini planlayan, yürüten ve sentezleyen bağımsız araştırma ajanı.

## Güvenlik ve en iyi uygulamalar

Her aracı, işletim sistemi düzeyinde yalıtılmış bir korumalı alan ortamında çalışır.
Korumalı alan, varsayılan olarak sınırsız giden ağ erişimine sahiptir. İzin verilenler listesi kullanarak ağ erişimini kısıtlayabilir veya devre dışı bırakabilirsiniz.

### Ağ erişimi

Varsayılan olarak, ortamların sınırsız giden ağ erişimi vardır. Giden trafiği belirli alanlarla veya joker karakter kalıplarıyla kısıtlamak için `network` izin verilenler listesini kullanın. Yapılandırma ayrıntıları için [Ağ İzin Verilenler Listesi](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=tr#network_allow_list) (AI Studio) veya [Ağ kuralları](https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr#with_network_rules) (API) başlıklı makaleleri inceleyin.

### Harici araçlar ve API'ler

Ajanı genişletmek için harici araçlar ve API'ler bağlayabilirsiniz. Yalnızca güvenilir kaynaklardan gelen araçları kullanın ve izinleri gereken minimum düzeyde tutun. Gizli dizileri yönetilen kimlik bilgileri olarak saklayın ve kimliklerine göre referans verin. Böylece çıkış proxy'si bunları istek sırasında ekler ve bunlar hiçbir zaman sanal alan içinde açığa çıkmaz. Aracı, erişebildiği tüm kimlik bilgilerini kullanabilir. Bu nedenle, yalnızca tam kapsamlı erişim izni vermeye hazır olduğunuz kimlik bilgilerini sağlayın.

- En az ayrıcalıklı hizmet hesaplarını veya API anahtarlarını kullanın.
- Uzun ömürlü anahtarlar yerine kısa ömürlü jetonları tercih edin.
- Yalnızca tam kapsamını vermeye istekli olduğunuz kimlik bilgilerini sağlayın.
- Kimlik bilgilerini düzenli aralıklarla değiştirin.

Kimlik bilgisi türleri ve yönetim işlemleri için [Kimlik bilgileri](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=tr) başlıklı makaleyi inceleyin. Ayrıca, izin verilenler listesi kuralında satır içi olarak başlıklar da ayarlayabilirsiniz. [Ağ yapılandırması](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr#network-configuration) bölümüne bakın.

### İnsan denetimi

Çıktıları (oluşturulan kod, veri dönüşümleri, yapılandırma değişiklikleri) dağıtmadan önce her zaman doğrulayın. Bu, özellikle verileri değiştiren veya harici sistemlerle etkileşimde bulunan görevler için önemlidir.

## Fiyatlandırma

Yönetilen ajanlar, Gemini model jetonlarına ve araç kullanımına dayalı bir [kullandıkça öde modelini](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#pricing-for-agents) kullanır. Tek bir etkileşim, genellikle 100.000 ila 3.000.000 jeton tüketen birden fazla muhakeme döngüsünü tetikleyebilir. Önizleme sırasında ortam işlem ücreti **alınmaz**. Görev başına dökümler için [tahmini maliyetlere](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr#availability-and-pricing) bakın. Yönetilen aracılar, ücretsiz katmanda ücretsiz sıklık sınırlaması ve kullanım kotasıyla da kullanılabilir.

## Sınırlar

| Sınır | Açıklama |
| --- | --- |
| **Ortamın kullanım ömrü** | Ortamlar, 7 gün boyunca işlem yapılmadığında kalıcı olarak silinir. |
| **VM Spin-down** | Sanal makineler, kaynakları korumak için kısa bir süre işlem yapılmadığında kapatılır. Bir sonraki istek durumu (baştan başlatma ile) geri yükler. |
| **Önceden Yüklenmiş Yazılım** | Python 3.12 ve Node.js 22'nin bulunduğu Ubuntu tabanlı ortam. Ortamın temel görüntüsü hakkında daha fazla bilgi için [Önceden yüklenmiş yazılım](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr#pre-installed-software) başlıklı makaleyi inceleyin. |
| **Maksimum ajan sayısı** | En fazla 1.000 yönetilen ajana sahip olabilirsiniz. |

## Ajan çerçeveleri

Ayrıca aşağıdaki çerçeveleri ve SDK'ları kullanarak Gemini ile ajanlar oluşturabilirsiniz:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=tr): Grafik yapılarını kullanarak durum bilgisi olan, karmaşık uygulama akışları ve çoklu ajan sistemleri oluşturun.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=tr): RAG ile geliştirilmiş iş akışları için Gemini ajanlarını özel verilerinize bağlayın.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=tr): İşbirlikçi, rol oynayan otonom yapay zeka ajanlarını yönetin.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=tr): JavaScript/TypeScript'te yapay zeka destekli kullanıcı arayüzleri ve temsilciler oluşturun.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): Birlikte çalışabilen yapay zeka temsilcileri oluşturmak ve düzenlemek için kullanılan açık kaynaklı bir çerçeve.
- [**Antigravity SDK'sı**](https://antigravity.google/product/antigravity-sdk?hl=tr): Google Antigravity'yi destekleyen aynı araçları, aracı döngüsünü ve bağlam yönetimini kullanarak Python'da programlanabilen otonom yapay zeka aracıları oluşturun.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-09 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-09 UTC."],[],[]]
