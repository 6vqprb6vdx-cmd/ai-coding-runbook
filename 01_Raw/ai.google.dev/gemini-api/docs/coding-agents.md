---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr
fetched_at: 2026-10-12T06:59:30.126511+00:00
title: "Kodlama arac\u0131s\u0131 kurulumu ve geli\u015ftirici kaynaklar\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Kodlama aracısı kurulumu ve geliştirici kaynakları

Yapay zeka kodlama aracıları, belirli bir tarihte sona eren eğitim verilerini kullanır. Bu nedenle, ajanlar genellikle desteği sonlandırılmış modeller (`gemini-1.5`), eski SDK'lar (`google-generativeai`) veya güncel olmayan kod kalıpları önerir.

Temsilcinizi resmi Gemini geliştirici kaynaklarına bağlamak, mevcut modelleri, `google-genai` SDK'sını ve [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr)'yi kullanarak doğru kod yazmasına yardımcı olur.

Kodlama temsilcinize dört şekilde Gemini dokümanlarına ve kurallarına erişim izni verebilirsiniz:

## Temsilci kaynaklarının özeti

| Kaynak | Sunduğu bilgiler | Kullanılabilirlik |
| --- | --- | --- |
| **[Gemini Agent Skills](https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr#available-skills)** | Belirli özellikler (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`) için adım adım kurallar, SDK kalıpları ve yardımcı komut dosyaları. | [AI Studio Build](https://ai.studio/build)'da önceden yüklenmiş olarak gelir. `skills.sh`, Context7 veya Yönetilen Ajanlar ile yükleyin. |
| **[Gemini Docs MCP Sunucusu](https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr#mcp-setup)** | Tüm dokümanlarda canlı arama (`gemini_search_docs`) ve tam sayfa okuma (`gemini_get_doc`) | Claude Code, Cursor, OpenAI Codex ve VS Code'da desteklenir. |
| **[Gemini API Eklentisi](https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr#gemini-api-plugin)** | Resmi Gemini becerileri, Dokümanlar MCP sunucusu ve API anahtarı araçlarını içeren toplu paket. | Antigravity |
| **[Makine Tarafından Okunabilir Dokümanlar](https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr#machine-readable-docs)** | Markdown sayfalarını ve `llms.txt` dizinlerini temizleyin. | `ai.google.dev/gemini-api/docs` adresindeki tüm doküman sayfaları. |

## Gemini ajan becerilerini yükleme

Agent skills, kodlama aracınıza prosedür kuralları, mevcut model adları ve SDK kodu kalıpları sağlar. İsteminizde uzun talimatlar eklemek yerine, aracınız her beceriyi yalnızca gerektiğinde yükler. Bu, aracınızın desteği sonlandırılan SDK'ları kullanmasını önler ve modern Gemini kalıplarını kullanmasına yardımcı olur.

Beceri, Gemini Dokümanlar MCP sunucusuyla birlikte çalışır. Aracınızda MCP sunucusu yüklü değilse beceri [`llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=tr)'ye geri döner. Becerilerin işleyiş şekli hakkında daha fazla bilgi edinmek için [Gemini API Becerileri Rehberi](https://aistudio.google.com/learn/gemini-api-skills?hl=tr)'ni okuyun.

### KSA (`skills.sh` veya Context7) ile yükleme

[skills.sh](https://skills.sh) (önerilir) veya [Context7](https://context7.com) kullanarak beceri yükleyin:

```
# List all available skills in the repository
npx skills add google-gemini/gemini-skills --list

# Install a specific skill globally with skills.sh
npx skills add google-gemini/gemini-skills --skill <skill-name> --global

# Or install with Context7
npx ctx7 skills install /google-gemini/gemini-skills <skill-name>
```

### Kullanılabilir beceriler

#### `gemini-api-dev`

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) ve resmi Gemini API SDK'leri (Python için `google-genai` ve TypeScript için `@google/genai`) ile uygulama geliştirme becerisi. Bu beceri şunları kapsar:

- Metin oluşturma, çok aşamalı etkileşim, yayın, yapılandırılmış çıkışlar ve işlev çağrısı
- Görüntü oluşturma, metin okuma (TTS) ve çok formatlı girişler
- Sunucu tarafında görüşme durumu yönetimi, arka planda yürütme, DeepResearch ve yönetilen aracılar
- Mevcut model adları ve eski `generateContent` veya `google-generativeai` kodunu taşıma

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### `gemini-live-api-dev`

[Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=tr) ile gerçek zamanlı ses ve video akışı uygulamaları oluşturma becerisi. Bu beceri şunları kapsar:

- WebSocket oturum yönetimi, kısa ömürlü istemci jetonları ve oturuma devam etme
- Ses etkinliği algılama (VAD) ve araya girme desteğiyle ses, video ve metin akışı
- Arka plan muhakemesi (genişletilmiş düşünme), engellemeyen eşzamansız araç çağrıları, transkripsiyon ve canlı konuşma çevirisi

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### `gemini-omni-flash-api`

Interactions API'yi kullanarak Gemini Omni Flash ile video oluşturma ve düzenleme becerisi. Yardımcı komut dosyaları (`upload_file.py`,
`generate_video.py`, `prep_video.py`, `inspect_video.py`) içerir ve şunları kapsar:

- Metinden video üretme ve istem oluşturma
- İlk ve son kare geçişleri ile referans yönlendirmeli video üretimi
- Video uzantıları ve medya ön işleme iş akışları

```
npx skills add google-gemini/gemini-skills --skill gemini-omni-flash-api --global
```

### Yönetilen Ajanlar'da becerileri kullanma

Etkileşimler API'si ile uzaktan yönetilen aracıları çalıştırdığınızda `google-gemini/gemini-skills` deposunu aracının çalışma alanına bağlayabilirsiniz. Ayrıntılar için [Gemini API Skills Guide](https://aistudio.google.com/learn/gemini-api-skills?hl=tr)'ı (Gemini API Beceri Kılavuzu) inceleyin:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Build a script that generates a 5-second video of a neon cityscape.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/google-gemini/gemini-skills",
                "target": ".agents",
            }
        ],
    },
)
```

## Gemini Dokümanları MCP sunucusunu bağlama

Herkese açık **Gemini Docs MCP sunucusu** (`https://gemini-api-docs-mcp.dev`), aracınıza tüm doküman sitesine canlı erişim sağlar. Ajanınız, istek şemalarını, model sınırlarını ve yeni özellikleri kontrol etmek için doküman sayfalarını arayabilir ve okuyabilir:

- `gemini_search_docs`: Gemini API belgelerinde konuya veya sorguya göre arama yapar.
- `gemini_get_doc`: Belirli bir dokümantasyon sayfasının Markdown içeriğinin tamamını okur.

### Hızlı kurulum

Algılanan kodlama aracılarınızı otomatik olarak yapılandırmak için terminalinizde veya proje kökünüzde şu komutu çalıştırın:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

### Ortama göre yapılandırma

### Claude Code

Terminalinizde şunu çalıştırın:

```
$ claude mcp add --transport http geminiDocs https://gemini-api-docs-mcp.dev
```

### İmleç

`~/.cursor/mcp.json` (global) veya `.cursor/mcp.json` (proje) öğesine ekleme:

```
{
  "mcpServers": {
    "geminiDocs": {
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

### OpenAI Codex

Terminalinizde şunu çalıştırın:

```
$ codex mcp add geminiDocs --url https://gemini-api-docs-mcp.dev
```

Dilerseniz `~/.codex/config.toml` uygulamasına ekleyin:

```
[mcp_servers.geminiDocs]
url = "https://gemini-api-docs-mcp.dev"
```

### VS Code (Copilot)

Çalışma alanınızdaki `.vscode/mcp.json` dosyasına ekleme:

```
{
  "servers": {
    "geminiDocs": {
      "type": "http",
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

## Gemini API eklentisi

**Antigravity**'yi kullanıyorsanız **Gemini API eklentisi**, çalışma alanınızı kurmanın en hızlı yoludur. Gemini Docs MCP sunucusu, tüm resmi Gemini becerileri (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`) ve API anahtarı araçlarını tek bir indirme işleminde bir araya getirir.

- **Antigravity'de (Kullanıcı Arayüzü) yükleme:** **Ayarlar > Özelleştirmeler > Google Eklentileri ile Oluştur**'a gidip **Gemini API**'yi indirin.
- **KSA ile yükleme:**
  `bash
  agy plugin install https://github.com/google-gemini/gemini-skills`

## Makine tarafından okunabilir belgeler

Standart web sayfaları, bağlam penceresi alanını kaplayan HTML etiketleri, gezinme çubukları ve komut dosyaları içerir. `ai.google.dev`, aracıların ve komut dosyalarının doğrudan temiz Markdown getirebilmesi için makine tarafından okunabilir uç noktalar sağlar:

- **`llms.txt` index**
  ([`https://ai.google.dev/gemini-api/docs/llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=tr)):
  Her sayfaya bağlantı içeren tüm Gemini API dokümanları sayfalarını listeler.
- **Doğrudan Markdown URL'leri (`.md.txt`)**: Kaydedilmiş istemler, `AGENTS.md` kuralları veya otomatik komut dosyaları için temiz Markdown kaynağı almak üzere `ai.google.dev`'daki herhangi bir doküman URL'sine `.md.txt` ekleyin (örneğin, [`https://ai.google.dev/gemini-api/docs/coding-agents.md.txt`](https://ai.google.dev/gemini-api/docs/coding-agents.md.txt?hl=tr)).

## Önerilen proje kuralları (`AGENTS.md`)

Proje kuralları dosyası (`AGENTS.md`, `.cursorrules` veya `CLAUDE.md`), her aracı oturumunun başında yüklenen temel kuralları belirler. Kodlama aracılarının varsayılan olarak mevcut modelleri ve SDK'ları kullanması için bu yönergeleri proje kökünüze ekleyin:

```
# Gemini API Guidelines

- Before writing Gemini API code, consult the `geminiDocs` MCP server (`gemini_search_docs` / `gemini_get_doc`) or `https://ai.google.dev/gemini-api/docs/llms.txt`.
- Always use the current Gemini API SDK (`google-genai` for Python, `@google/genai` for TypeScript/JavaScript). Never use legacy SDKs (`google-generativeai` or `@google/generative-ai`).
- Use the Interactions API (`client.interactions.create`) for new applications unless a specific feature requires `generateContent`.
- Use current recommended models (see https://ai.google.dev/gemini-api/docs/models) and avoid deprecated models.
```

## Doğrulama ve sorun giderme

### Kurulumu doğrulama

Ayarlarınızı test etmek için kodlama aracınıza şunu sorun:

```
Look up the request schema for the Gemini Interactions API in the documentation.
```

Yapılandırılmış bir aracı, `geminiDocs` MCP sunucusunda `gemini_search_docs` kullanır ve `google-genai` veya `@google/genai` SDK'sı ile `client.interactions.create` kullanarak kod yazar.

### Durum komutları

| Ortam | MCP doğrulaması | Beceri doğrulama |
| --- | --- | --- |
| **Claude Code** | `/mcp` çalıştırma | `/skills` çalıştırma |
| **İmleç** | **Ayarlar > Özellikler > MCP**'yi açın. | **Ayarlar > Kurallar**'ı açın. |
| **OpenAI Codex** | `codex mcp list` çalıştırma | `.codex/skills/` veya `~/.codex/skills/`'ı kontrol edin. |
| **Antigravity** | **Özelleştirmeler > Bağlantılar**'ı açın. | **Özelleştirmeler > Kurallar**'ı açın veya `/skills list` komutunu çalıştırın. |
| **VS Code (Copilot)** | **Uzantılar > MCP** veya Çıkış paneli'ni açın. | Copilot Chat'te **Araçları Seç**'i tıklayın. |

### Sorun giderme

- **Beceri veya MCP sunucusu algılanmadı:** Düzenleyicinizi (Cursor veya VS Code) ya da terminal oturumunuzu (Claude Code veya Codex) yeniden başlatın. Çoğu aracı, MCP sunucularını ve becerilerini yalnızca başlatıldığında yükler.
- **Global beceri çakışması:** Aracınız, global olarak yüklenmiş bir beceriyi yoksayarsa `--global` olmadan beceriyi proje kökünüze yükleyin:
  `bash
  npx skills add google-gemini/gemini-skills --skill gemini-api-dev`
- **Yoksayılan kurallar:** `AGENTS.md`, `.cursorrules` veya `CLAUDE.md`
  dosyanızın projenizin kök dizininde olduğundan emin olun.

## Sırada ne var?

- [Gemini API Skills kılavuzu](https://aistudio.google.com/learn/gemini-api-skills?hl=tr)
- [GitHub'daki Gemini API becerileri](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr)
- [Kullanılabilir modeller](https://ai.google.dev/gemini-api/docs/models?hl=tr)
- [Kitaplıklar ve SDK'lar](https://ai.google.dev/gemini-api/docs/libraries?hl=tr)

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-06 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-06 UTC."],[],[]]
