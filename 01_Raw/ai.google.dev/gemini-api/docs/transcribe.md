---
source_url: https://ai.google.dev/gemini-api/docs/transcribe?hl=tr
fetched_at: 2026-10-12T06:56:46.145396+00:00
title: "Ses transkripti \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Ses transkripti

Gemini API, Gemini 3.5 Transcribe modelini (`gemini-3.5-transcribe`) kullanarak ses dosyalarındaki konuşmaları metne dönüştürür. Gemini'ın ses anlama özelliklerine dayalı olarak otomatik dil tanımlama, konuşmacı diarizasyonu, kelime düzeyinde zaman damgaları ve özel kelime bilgisi ipuçlarıyla doğru transkripsiyon sağlar. Ayrıca, akıcılığı bozan ifadeleri kaldırma ve akıllı biçimlendirme özelliklerine sahip bir [akıllı metne dönüştürme](#transcription-modes) modu da sunar.

Ses dosyasını metne dönüştürmek için sesi yükleyip `gemini-3.5-transcribe`'a iletin:

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const audioFile = await client.files.upload({
  file: "path/to/sample.mp3",
  config: { mime_type: "audio/mp3" },
});

const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
});

console.log(interaction.output_text);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

## Genel Bakış

Gemini 3.5 Transcribe, sesle yazma görevleri için optimize edilmiştir. Farklı aksanları, arka plan gürültüsünü ve çok dilli sohbetleri destekler.

Temel özellikler:

- **Otomatik konuşma tanıma (ASR):** [85'ten fazla yerel ayarda](#supported-languages) dilleri otomatik olarak algılar. Cümle içi ve cümleler arası dil değişimini manuel yapılandırma olmadan işler.
- **Özel kelime dağarcığı:** 1.000'e kadar ifade ileterek tanımayı alana özgü terimler, kısaltmalar ve özel adlar yönünde önyargılı hale getirir.
- **Konuşmacı diarizasyonu:** Birden fazla konuşmacı arasında ayrım yapar ve konuşulan segmentleri farklı etiketlere atfeder.
- **Kelime düzeyinde zaman damgaları:** Tanınan her kelime için tam başlangıç ve bitiş zamanı farkları oluşturur.
- **Akıllı metne dönüştürme:** Akıcılık sorunlarını, dolgu kelimelerini ve tekrarları temizler, yapılandırılmış biçimlendirme uygular.
- **Biçimlendirme ve normalleştirme:** Büyük harf kullanımı, noktalama ve ters metin normalleştirme (ör. "yirmi altı milyon dolar"ı "26 milyon TL"ye dönüştürme) uygular.

Ses içeriğiyle ilgili genel sesli akıl yürütme veya soru yanıtlama için [Ses anlama](https://ai.google.dev/gemini-api/docs/audio?hl=tr)'yı kullanın. Metin okuma ses sentezi için [Metin okuma](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr)'yı kullanın.

## Dil algılama ve ipuçları

Model, varsayılan olarak konuşma dilini otomatik olarak algılar. Konuşmacılar dil değiştirirken diller arasında dinamik olarak geçiş yapar.

Otomatik algılamayı kullanmak için `language_codes` öğesini atlayın veya boş bir liste sağlayın:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "language_codes": [],
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      language_codes: [],
    },
  },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    LanguageCodes: []string{},
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "language_codes": []
      }
    }
  }'
```

Dili önceden biliyorsanız transkripsiyon doğruluğunu artırmak için `language_codes` içinde BCP-47 dil kodlarını belirtin (bkz. [Desteklenen diller](#supported-languages)):

### Python

```
generation_config = {
    "transcription_config": {
        "language_codes": ["es-ES"],
    }
}
```

### JavaScript

```
const generationConfig = {
  transcription_config: {
    language_codes: ["es-ES"],
  },
};
```

### Go

```
package main

import (
    "google.golang.org/genai/interactions/models/interactions"
)

func main() {
    generationConfig := &interactions.GenerationConfig{
        TranscriptionConfig: &interactions.TranscriptionConfig{
            LanguageCodes: []string{"es-ES"},
        },
    }
    _ = generationConfig
}
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "language_codes": ["es-ES"]
    }
  }
}
```

## Özel kelime dağarcığı

Konuşma modelini, yaygın olmayan kelimelere, teknik jargonlara, marka adlarına veya özel isimlere yönlendirebilirsiniz. `custom_vocabulary` dizisinde en fazla 1.000 terim sağlayın (en iyi sonuçlar genellikle 100 terime kadar olan terimlerle elde edilir):

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"],
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      custom_vocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    CustomVocabulary: []string{"Gemini", "Kubernetes", "BigQuery"},
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## Konuşmacı ayırma

Konuşmacı diarizasyonu, kayıttaki farklı sesleri tanımlar ve her segmenti `spk_1` veya `spk_2` gibi bir konuşmacı tanımlayıcısıyla etiketler. En fazla 8 konuşmacı desteklenir (3 veya daha fazla konuşmacı için ilişkilendirme deneyseldir).

`diarization_mode` içinde `mode` yapılandırarak ayırmayı etkinleştirin:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "diarization_mode": "speaker",
            },
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        diarization_mode: "speaker",
      },
    },
  },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.NewTranscriptionMode(interactions.VerbatimTranscriptionMode{
                        DiarizationMode: genai.Ptr("speaker"),
                    }))),
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "diarization_mode": "speaker"
        }
      }
    }
  }'
```

## Kelime düzeyinde zaman damgaları

Kelime düzeyindeki zaman damgaları, ses akışında tanınan her kelime için tam başlangıç ve bitiş zamanlarını sağlar.

`mode` içinde `timestamp_granularities` seçeneğini yapılandırarak zaman damgalarını etkinleştirin:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "timestamp_granularities": ["word"],
            },
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        timestamp_granularities: ["word"],
      },
    },
  },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.NewTranscriptionMode(interactions.VerbatimTranscriptionMode{
                        TimestampGranularities: []string{"word"},
                    }))),
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "timestamp_granularities": ["word"]
        }
      }
    }
  }'
```

Hem konuşmacı etiketlerini hem de kelime zaman damgalarını almak için `diarization_mode` ve `timestamp_granularities` seçeneklerini `mode` bölümünde birleştirebilirsiniz:

### Python

```
generation_config = {
    "transcription_config": {
        "mode": {
            "type": "verbatim",
            "diarization_mode": "speaker",
            "timestamp_granularities": ["word"],
        },
    }
}
```

### JavaScript

```
const generationConfig = {
  transcription_config: {
    mode: {
      type: "verbatim",
      diarization_mode: "speaker",
      timestamp_granularities: ["word"],
    },
  },
};
```

### Go

```
package main

import (
    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
)

func main() {
    generationConfig := &interactions.GenerationConfig{
        TranscriptionConfig: &interactions.TranscriptionConfig{
            Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.NewTranscriptionMode(interactions.VerbatimTranscriptionMode{
                DiarizationMode:        genai.Ptr("speaker"),
                TimestampGranularities: []string{"word"},
            }))),
        },
    }
    _ = generationConfig
}
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "mode": {
        "type": "verbatim",
        "diarization_mode": "speaker",
        "timestamp_granularities": ["word"]
      }
    }
  }
}
```

## Metne dönüştürme modları

Gemini 3.5 Transcribe, `mode` parametresi aracılığıyla iki transkripsiyon modunu destekler:

- **`verbatim` (varsayılan)**: Konuşulan her şeyin kelimesi kelimesine tam transkriptini döndürür. Bu transkriptte, ham dolgu kelimeleri ("ııı", "şey", "gibi", "biliyorsunuz"), tekrarlar, duraklamalar ve yanlış başlangıçlar korunur. Zaman damgaları ve konuşmacı ayırma bu modda yapılandırılır (`{"type": "verbatim", ...}`).
- **`smart` (Akıllı transkript)**: Akıllı son işlem uygulayarak transkripti okunacak şekilde optimize eder:
  - **Akıcılık bozukluklarını giderme**: Görüşmelerdeki dolgu kelimelerini, takılmaları ve yanlış başlangıçları kaldırır.
  - **Satır içi otomatik düzeltmeler**: Konuşma sırasında yapılan düzeltmeleri doğrudan çözer (örneğin, *"Salı günü buluşalım, aslında hayır, Çarşamba günü saat ikide"* ifadesi *"Çarşamba günü saat 14:00'te buluşalım"* olarak değiştirilir).
  - **Otomatik yapılandırılmış biçimlendirme**: Konuşma sırasında söylenen düşünceleri otomatik olarak paragraflara, numaralı listelere, madde işaretlerine, biçimlendirilmiş tarihlere, para birimlerine ve sayılara dönüştürür.
  - **Dil bilgisi temizliği**: Doğal noktalama, cümlelerde büyük harf kullanımı ve akıcılık sağlar.

| Seslendirilmiş içerik | `verbatim` çıkış | `smart` (Akıllı transkript) çıkışı |
| --- | --- | --- |
| "Şey, toplantıya Ayşe'yi davet etmeliyiz. Hayır, pardon, Ali'yi ve Can'ı davet etmeliyiz." | "Toplantıya Ayşe'yi davet etmeliyiz. Hayır, Ali'yi ve Can'ı davet etmeliyiz." | "Toplantıya Bob ve Carol'ı davet etmemiz gerektiğini düşünüyorum." |
| "İlk öğe bütçesini incele, ikinci öğe zaman çizelgesini tamamla, üçüncü öğe özeti gönder" | "first item review budget second item finalize timeline third item send recap" (ilk öğe bütçesini incele, ikinci öğe zaman çizelgesini sonlandır, üçüncü öğe özeti gönder) | "1. Bütçeyi inceleyin 2. Zaman çizelgesine son şeklini verin 3. Özeti gönder" |

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": "smart",
        }
    },
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: "smart",
    },
  },
});
console.log(interaction.output_text);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.TranscriptionConfigModeEnumSmart)),
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": "smart"
      }
    }
  }'
```

## Metne dönüştürme çıktısını ayrıştırma

Transkript metninin tamamı `interaction.output_text` içinde döndürülür.

`timestamp_granularities` veya `diarization_mode` etkinleştirildiğinde API, etkileşim içeriğine eklenmiş ayrıntılı kelime düzeyinde ek açıklamalar da döndürür.

Kelime zaman damgalarını ve konuşmacı dönüşlerini ayıklayıp yinelemek için aşağıdaki adımları uygulayın:

### Python

```
def extract_word_annotations(interaction):
    words = []
    for step in getattr(interaction, "steps", []) or []:
        for content in getattr(step, "content", []) or []:
            for annotation in getattr(content, "annotations", []) or []:
                if getattr(annotation, "type", None) == "word_info":
                    words.append(annotation)
    return words

words = extract_word_annotations(interaction)

for w in words:
    speaker = f"[{w.speaker}] " if getattr(w, "speaker", None) else ""
    start = getattr(w, "start_offset", "")
    end = getattr(w, "end_offset", "")
    timing = f"({start} -> {end}) " if start and end else ""
    print(f"{speaker}{timing}{w.text}")
```

### JavaScript

```
function extractWordAnnotations(interaction) {
  const words = [];
  for (const step of interaction.steps ?? []) {
    for (const content of step.content ?? []) {
      for (const annotation of content.annotations ?? []) {
        if (annotation.type === "word_info") {
          words.push(annotation);
        }
      }
    }
  }
  return words;
}

const words = extractWordAnnotations(interaction);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.start_offset && w.end_offset) ? `(${w.start_offset} -> ${w.end_offset}) ` : "";
  console.log(`${speaker}${timing}${w.text}`);
}
```

### Go

```
package main

import (
    "fmt"

    "google.golang.org/genai/interactions/models/interactions"
)

func extractWordAnnotations(interaction *interactions.Interaction) []*interactions.WordInfo {
    var words []*interactions.WordInfo
    if interaction == nil {
        return words
    }
    for _, step := range interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    for _, annotation := range content.TextContent.Annotations {
                        if annotation.WordInfo != nil {
                            words = append(words, annotation.WordInfo)
                        }
                    }
                }
            }
        }
    }
    return words
}

func main() {
    var interaction *interactions.Interaction
    words := extractWordAnnotations(interaction)

    for _, w := range words {
        speaker := ""
        if w.Speaker != nil && *w.Speaker != "" {
            speaker = fmt.Sprintf("[%s] ", *w.Speaker)
        }
        timing := ""
        if w.StartOffset != nil && w.EndOffset != nil {
            timing = fmt.Sprintf("(%s -> %s) ", *w.StartOffset, *w.EndOffset)
        }
        fmt.Printf("%s%s%s\n", speaker, timing, w.GetText())
    }
}
```

### REST

```
{
  "id": "interactions/abc123xyz",
  "status": "completed",
  "steps": [
    {
      "id": "step_001",
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Hello world",
          "annotations": [
            {
              "type": "word_info",
              "text": "Hello",
              "speaker": "spk_1",
              "start_offset": "0.100s",
              "end_offset": "0.450s"
            },
            {
              "type": "word_info",
              "text": "world",
              "speaker": "spk_1",
              "start_offset": "0.500s",
              "end_offset": "0.850s"
            }
          ]
        }
      ]
    }
  ]
}
```

## Desteklenen diller

Gemini 3.5 Transcribe'da aşağıdaki diller ve BCP-47 dil kodları desteklenir:

| Dil | BCP-47 kodu | Dil | BCP-47 kodu |
| --- | --- | --- | --- |
| Afrikaanca | `af-ZA` | Japonca | `ja-JP` |
| Amharca | `am-ET` | Cava dili | `jv-ID` |
| Arapça (Mısır) | `ar-EG` | Kabuverdianu | `kea-CV` |
| Ermenice | `hy-AM` | Kannada | `kn-IN` |
| Assamca | `as-IN` | Kazakça | `kk-KZ` |
| Azerice | `az-AZ` | Korece | `ko-KR` |
| Belarus dili | `be-BY` | Kırgızca | `ky-KG` |
| Bengalce (Bangladeş) | `bn-BD` | Letonca | `lv-LV` |
| Bengalce (Hindistan) | `bn-IN` | Lingala | `ln-CD` |
| Boşnakça | `bs-BA` | Litvanca | `lt-LT` |
| Bulgarca | `bg-BG` | Makedonca | `mk-MK` |
| Bulgarca (Aromanca) | `rup-BG` | Malayca | `ms-MY` |
| Burmaca | `my-MM` | Malayalamca | `ml-IN` |
| Kantonca (Geleneksel) | `yue-Hant-HK` | Maltaca | `mt-MT` |
| Katalanca | `ca-ES` | Mandarin Çincesi (Basitleştirilmiş) | `cmn-Hans-CN` |
| Sabuanca | `ceb` | Marathi | `mr-IN` |
| Orta Khmer | `km-KH` | Moğolca | `mn-MN` |
| Hırvatça | `hr-HR` | Nepalce | `ne-NP` |
| Çekya | `cs-CZ` | Norveççe | `nb-NO` |
| Danca | `da-DK` | Oriya dili | `or-IN` |
| Felemenkçe | `nl-NL` | Lehçe | `pl-PL` |
| İngilizce (İngiltere) | `en-GB` | Portekizce (Brezilya) | `pt-BR` |
| İngilizce (Hindistan) | `en-IN` | Portekizce (Portekiz) | `pt-PT` |
| İngilizce (ABD) | `en-US` | Pencapça | `pa-IN` |
| Estonca | `et-EE` | Pencapça (Gurmukhi alfabesi) | `pa-Guru-IN` |
| Farsça | `fa-IR` | Rumence | `ro-RO` |
| Filipince | `fil-PH` | Rusça | `ru-RU` |
| Fince | `fi-FI` | Sırpça | `sr-RS` |
| Fransızca | `fr-FR` | Sindce (Arapça alfabesi) | `sd-Arab-IN` |
| Galiçyaca | `gl-ES` | Slovakça | `sk-SK` |
| Gürcüce | `ka-GE` | Slovence | `sl-SI` |
| Almanca | `de-DE` | İspanyolca (Latin Amerika) | `es-419` |
| Greek | `el-GR` | İspanyolca (Amerika Birleşik Devletleri) | `es-US` |
| Güceratça | `gu-IN` | Swahili (Kenya) | `sw-KE` |
| Hausaca | `ha-NG` | İsveççe | `sv-SE` |
| İbranice | `he-IL` | Tacikçe | `tg-TJ` |
| Hintçe | `hi-IN` | Telugu dili | `te-IN` |
| Macarca | `hu-HU` | Tayca | `th-TH` |
| İzlandaca | `is-IS` | Türkçe | `tr-TR` |
| Indian English | `en-IN` | Ukraynaca | `uk-UA` |
| Endonezce | `id-ID` | Özbekçe | `uz-UZ` |
| İtalyanca | `it-IT` | Vietnamca | `vi-VN` |

## Desteklenen ses biçimleri

Gemini 3.5 Transcribe aşağıdaki ses biçimi MIME türlerini destekler:

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG - `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 - `audio/l16`
- Opus - `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM - `audio/webm`

Desteklenen MIME türlerinin ve parametre şemalarının tam listesi için [Interactions API referansına](https://ai.google.dev/api/interactions-api?hl=tr#Resource:Content) bakın.

## Parametre referansı

`generation_config` içindeki `transcription_config` nesnesinde alanları ayarlayarak metne dönüştürmeyi yapılandırın:

| Alan | Tür | Açıklama |
| --- | --- | --- |
| `language_codes` | Dize dizisi | BCP-47 dil kodları (ör. `["en-US"]`). Atlanırsa veya boş bırakılırsa (`[]`) model, dili otomatik olarak algılar ve kod değiştirmeyi yönetir. |
| `custom_vocabulary` | Dize dizisi | Konuşma tanımayı etkilemek için 1.000'e kadar özel terim, kısaltma veya özel isim. Konuşmacı ayırma ve kelime düzeyinde zaman damgalarıyla uyumlu değildir. |
| `mode` | Nesne veya Dize | Metne dönüştürme modu yapılandırması. `"smart"` veya bire bir mod nesnesi (`{"type": "verbatim", ...}`) kabul eder. Varsayılan olarak bire bir transkripsiyon kullanılır. |
| `mode.type` | Dize | *(Yalnızca Ayrıntılı mod)* Mod tanımlayıcısı. Her zaman `"verbatim"` olarak ayarlanır. |
| `mode.timestamp_granularities` | Dize dizisi | *(Yalnızca ayrıntılı mod)* Döndürülecek zaman damgalarının ayrıntı düzeyi. Kelime başlangıcı ve bitişi için ofsetleri etkinleştirmek üzere `["word"]` iletin. Özel kelime dağarcığıyla uyumlu değildir. |
| `mode.diarization_mode` | Dize | *(Yalnızca Ayrıntılı mod)* Konuşmacı ayrımı modu. Farklı konuşmacıları tanımlamak ve etiketlemek için `"speaker"` iletin. Özel kelime dağarcığıyla uyumlu değildir. |

## En iyi uygulamalar

- **Temiz ses sağlayın:** Ses kayıtlarında net bir ses ayrımı olduğundan emin olun ve ciddi kırpmalardan kaçının.
- **Bilinen durumlarda dil ipuçları verin:** Sesin dilini önceden biliyorsanız doğruluğu en üst düzeye çıkarmak için `language_codes` belirtin.
- **Özel kelime dağarcığını hedefleme:** `custom_vocabulary` içine günlük hayatta sık kullanılan kelimeler yerine yalnızca farklı alan terimleri, marka adları veya özel isimler ekleyin.
- **Büyük kayıtlar için Files API'yi kullanın:** Birkaç saniyeden uzun dosyalar için dosyayı `client.files.upload` kullanarak yükleyin ve döndürülen dosya URI'sini modele iletin.

## Sınırlamalar

- **Ses süresi:** Standart tekli istekler, 1 saate kadar olan ses dosyalarını destekler. Konuşmacı ayrımı veya kelime düzeyinde zaman damgaları gibi özellikler etkinleştirildiğinde ses işleme 30 dakika ile sınırlıdır.
- **Kelime düzeyinde zaman damgaları:** Kelime düzeyinde zaman damgalarının etkinleştirilmesi, genel transkripsiyon doğruluğunu düşürebilir.
- **Konuşmacı ayırma:** Konuşmacı ayırma özelliği en fazla 8 konuşmacıyı destekler. 3 veya daha fazla hoparlör için konuşmacı ilişkilendirme özelliği deneyseldir.
- **Özel kelime dağarcığı:** `custom_vocabulary` içinde 1.000'e kadar terim sağlayabilirsiniz ancak en iyi sonuçlar genellikle 100 terimle elde edilir. `custom_vocabulary` özelliğini konuşmacı diarizasyonu veya kelime düzeyinde zaman damgalarıyla birlikte kullanamazsınız. API, bu özelliklerden biriyle birlikte `custom_vocabulary` belirtilen istekleri reddeder.
- **Mod uyumluluğu:** Akıllı transkripsiyon (`"smart"`), `timestamp_granularities` veya `diarization_mode` ile birlikte kullanılamaz.

## Sırada ne var?

- Live API'yi kullanarak [Canlı transkripsiyon kılavuzu](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=tr) ile anlık ses akışı yapın.
- Ses içeriklerini analiz etmek, özetlemek veya sorgulamak için [Ses yorumlama](https://ai.google.dev/gemini-api/docs/audio?hl=tr)'yı keşfedin.
- [Metin okuma](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr) özelliğini kullanarak metinden ses sentezlemeyi öğrenin.
- Model fiyatlandırması ve jeton sınırları için [fiyatlandırma sayfasına](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#gemini-3.5-transcribe) bakın.
- Medya dosyalarını yükleme ve yönetmeyle ilgili ayrıntılar için [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr) kılavuzuna göz atın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-24 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-24 UTC."],[],[]]
