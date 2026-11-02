---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=tr
fetched_at: 2026-11-02T07:06:05.443244+00:00
title: "Ba\u011flam\u0131 \u00f6nbelle\u011fe alma \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Bağlamı önbelleğe alma

Tipik bir yapay zeka iş akışında, aynı giriş jetonlarını bir modele tekrar tekrar iletebilirsiniz. Gemini API, performansı ve maliyetleri optimize etmek için örtük önbelleğe alma özelliği sunar.

## Örtülü önbelleğe alma

Dolaylı önbelleğe alma, tüm Gemini 2.5 ve daha yeni modellerde varsayılan olarak etkindir. Hem [durum bilgisi olan](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr#multi-turn-conversations) (`previous_interaction_id` kullanarak) hem de [durum bilgisi olmayan](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr#stateless-conversations) sohbet modları için desteklenir.
İsteğiniz önbelleklere ulaşırsa maliyet tasarruflarını otomatik olarak aktarırız. Özelliği etkinleştirmek için herhangi bir yapılandırma yapmanız gerekmez. Aşağıdaki tabloda her model için minimum giriş birimi sayısı listelenmiştir:

| Model | Minimum jeton sınırı |
| --- | --- |
| Gemini 4 Argon | 4.096 |
| Gemini 3.8 Flash | 4.096 |
| Gemini 3.6 Flash | 4.096 |
| Gemini 3.1 Pro Preview | 4.096 |
| Gemini 2.5 Flash | 2.048 |
| Gemini 2.5 Pro | 2.048 |

Dolaylı önbellek isabeti olasılığını artırmak için:

- Büyük ve yaygın içerikleri isteminizin başına koymayı deneyin.
- Benzer ön eke sahip istekleri kısa bir süre içinde göndermeyi deneyin.

Önbellek isabeti olan jetonların sayısını yanıt nesnesinin `usage.total_cached_tokens` (Python ve JavaScript) alanında görebilirsiniz.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-23 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-23 UTC."],[],[]]
