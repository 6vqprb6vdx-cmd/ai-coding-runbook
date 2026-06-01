---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr
fetched_at: 2026-06-01T19:41:08.756806+00:00
title: "Antigravity Agent \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Antigravity Agent

Antigravity ajanı, Gemini API'de genel amaçlı olarak yönetilen bir ajandır. Tek bir API çağrısı, Google tarafından barındırılan kendi güvenli Linux sanal alanınızda akıl yürüten, kod yürüten, dosyaları yöneten ve web'de gezinmenizi sağlayan bir aracı sunar.

Gemini 3.5 Flash tarafından desteklenir ve Antigravity IDE ile aynı koşum takımını kullanır. [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=tr) ve [Google AI Studio](https://aistudio.google.com?hl=tr) üzerinden kullanılabilir.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Özellikler

Her çağrı, bir Linux sanal alanı sağlayabilir ve araç kullanma döngüsünü başlatabilir. Aracı, görev tamamlanana kadar plan yapar, harekete geçer, sonuçları gözlemler ve tekrarlar.

- **Kod yürütme:** Bash, Python ve Node.js komutlarını çalıştırın. Paketleri yükleyin, testleri çalıştırın ve uygulamalar oluşturun.
- **Dosya yönetimi:** Korumalı alandaki dosyaları okuma, yazma, düzenleme, arama ve listeleme. Dosyalar, etkileşimler arasında korunur.
- **Web erişimi:** Veriler için Google Arama ve URL getirme.
- **Bağlam sıkıştırma:** Bağlamı kaybetmeden veya jeton sınırlarına ulaşmadan uzun süren, çok turlu oturumları desteklemek için otomatik bağlam sıkıştırma (~135 bin jetonda tetiklenir).

Çok turlu kullanım ve yayın için [Hızlı Başlangıç](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr) bölümüne bakın.

## Desteklenen araçlar

Varsayılan olarak, temsilci `code_execution`, `google_search` ve `url_context` uygulamalarına erişebilir. `environment` parametresini belirttiğinizde dosya sistemi araçları otomatik olarak etkinleştirilir. Varsayılan grubu özelleştirirken veya kısıtlarken yalnızca `tools` parametresini belirtmeniz gerekir.

| Araç | Değer türü | Açıklama |
| --- | --- | --- |
| Kod Yürütme | `code_execution` | stdout/stderr yakalama ile kabuk komutlarını (bash, Python, Node) çalıştırın. |
| Google Arama | `google_search` | Herkese açık web'de arama yapın. |
| URL Bağlamı | `url_context` | Web sayfalarını getirme ve okuma |
| Dosya sistemi | *(`environment` üzerinden etkinleştirilir)* | Korumalı alanda dosyaları okuma, yazma, düzenleme, arama ve listeleme Ayrı bir araç türü yoktur. `environment` ayarlandığında otomatik olarak etkinleştirilir. |

Aracı belirli araçlarla sınırlamak için yalnızca ihtiyacınız olanları iletin:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## Çok formatlı giriş

Antigravity aracısı, çok formatlı girişleri destekler. Şu anda yalnızca `text` ve `image` girişleri desteklenmektedir. Resimler satır içi Base64 kodlu dizeler (`data`) olarak sağlanmalıdır.

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### REST

```
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## Aracıyı özelleştirme

Antigravity aracısını talimatlarını, araçlarını ve ortamını özelleştirerek genişletebilirsiniz. Aracı, özelleştirme için dosya sistemi tabanlı bir yaklaşımı destekler: Talimatlar ve beceriler için `AGENTS.md` gibi dosyaları doğrudan korumalı alana `.agents/skills/` altında bağlayabilir veya yapılandırmayı etkileşim sırasında satır içi olarak iletebilirsiniz. Yapılandırmanızı satır içi olarak yineleyebilir ve hazır olduğunuzda yönetilen bir aracı olarak kaydedebilirsiniz.

Özel aracıların nasıl oluşturulacağıyla ilgili tüm ayrıntılar için [Yönetilen Aracıları Oluşturma](https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr) başlıklı makaleyi inceleyin.

## Ortam

Her çağrı, bir Linux sanal alanı oluşturur veya yeniden kullanır. `environment` parametresi üç biçimde olabilir:

| Form | Açıklama |
| --- | --- |
| `"remote"` | Varsayılan ayarlarla yeni bir korumalı alan sağlayın. |
| `"env_abc123"` | Tüm dosyaları ve durumu koruyarak mevcut bir ortamı kimliğe göre yeniden kullanın. |
| `{...}` | Özel kaynaklar ve ağ kurallarıyla tam `EnvironmentConfig` |

Kaynaklar (Git, GCS, satır içi), ağ, yaşam döngüsü ve kaynak sınırları hakkında ayrıntılı bilgi için [Ortamlar](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr) başlıklı makaleyi inceleyin.

## Kullanılabilirlik ve fiyatlandırma

Antigravity aracısı, Google AI Studio'daki [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=tr) ve Gemini API üzerinden önizleme olarak kullanılabilir.

Fiyatlandırma, temel Gemini model jetonlarına ve aracının kullandığı araçlara dayalı [kullandıkça öde modeline](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#pricing-for-agents) göre belirlenir. Tek bir çıktı üreten standart bir sohbet isteğinin aksine, Antigravity etkileşimi, aracı tabanlı bir iş akışıdır. Tek bir istek, muhakeme, araç yürütme, kod çalıştırma ve dosya yönetimi gibi işlemleri içeren bağımsız bir döngüyü tetikler.

### Tahmini maliyetler

Maliyetler, görevin karmaşıklığına göre değişir. Aracı, kaç araç çağrısı, kod yürütme ve dosya işlemi gerektiğini bağımsız olarak belirler. Aşağıdaki tahminler, çalıştırmalara dayanmaktadır.

| Görev kategorisi | Giriş jetonları | Çıkış jetonları | Normal maliyet |
| --- | --- | --- | --- |
| **Araştırma ve bilgi sentezi** | 100 bin - 500 bin | 10 bin-40 bin | 0,30-1,00 ABD doları |
| **Doküman ve içerik oluşturma** | 100 bin - 500 bin | 15.000-50.000 | 0,30-1,30 ABD doları |
| **Süreç ve sistem tasarımı** | 100 bin - 400 bin | 10.000-30.000 | 0,25-0,80 ABD doları |
| **Veri işleme ve analiz** | 300.000-3.000.000 | 30 bin - 150 bin | 0,70-3,25 ABD doları |

Giriş jetonlarının% 50-70'i genellikle önbelleğe alınır. Çok sayıda araç çağrısı içeren karmaşık aracı iş akışları, tek bir etkileşimde 3-5 milyon jeton biriktirebilir ve maliyeti yaklaşık 5 ABD dolarına kadar çıkabilir.

Önizleme döneminde **ortam işlem** (CPU, bellek, korumalı alan yürütme) için **ücret alınmaz**.

## Sınırlamalar

- **Önizleme durumu:** Antigravity aracısı ve Etkileşimler API'si önizleme aşamasındadır. Özellikler ve şemalar değişebilir.
- **Desteklenmeyen oluşturma yapılandırması:** Aşağıdaki parametreler desteklenmez ve 400 hatası döndürür: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Yapılandırılmış çıkış:** Antigravity aracısı, yapılandırılmış çıkışları desteklemez.
- **Kullanılamayan araçlar:** `file_search`, `computer_use`, `google_maps`, `function_calling` ve `mcp` henüz desteklenmemektedir.
- **Dosya sistemi aracı:** Şu anda dosya sistemi aracı yok. Bu, `environment`'nın bir parçasıdır.
- **Arka plan:** Temsilci, `background=True` kullanımını desteklemiyor ve `store=True` gerektiriyor.
- **Desteklenmeyen çok formatlı türler.** Ses, video ve doküman girişleri şu anda desteklenmemektedir. Yalnızca metin ve resimlere izin verilir.

## Sırada ne var?

- [Hızlı başlangıç](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr): Çok turlu görüşmeler ve akış.
- [Özel Ajanlar Oluşturma](https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr): Özel talimatlar, beceriler ve ajanları kaydetme.
- [Ortamlar](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr): korumalı alan yapılandırması, kaynaklar, ağ iletişimi.
- [Deep Research Agent](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=tr): Uzun araştırma görevleri.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=tr): Temel API.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-20 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-20 UTC."],[],[]]
