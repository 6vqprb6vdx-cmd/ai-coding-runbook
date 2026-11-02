---
source_url: https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=tr
fetched_at: 2026-11-02T07:23:18.990627+00:00
title: "Live API'de D\u00fc\u015f\u00fcnme \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Live API'de Düşünme

Gemini Live API, Gemini modelleriyle anlık ve iki yönlü sesli sohbetler yapmanızı sağlar.

Standart ses modelleri, anlık karşılıklı diyaloglar için uygundur. Modelle konuşursunuz ve model hemen sözlü bir yanıt oluşturur. Ancak bir istek planlama, karmaşık analiz veya harici araçlar gerektirdiğinde doğrudan yanıtlar sınırlanır. Model, ya gerekçe sunmadan yanıt vermeli ya da araçların tamamlanmasını beklerken sessizce duraklamalıdır.

Live API'de düşünme (`gemini-3.8-live-extended-thinking`), gerçek zamanlı sesli oturumlara arka plan gerekçelendirmesi ekler. Model, etkileşimi etkin tutmak için doğal sohbet dolguları konuşurken arka planda eşzamansız araçları planlar ve çağırır.

Bu mimari, etkileşimli yaşam döngüsünü iki temel şekilde değiştirir:

- **Sohbet dolguları**: Model, arka planda araçları çalıştırırken ara güncellemeleri (ör. "Uçuş seçenekleri kontrol ediliyor") sesli olarak bildirir.
- **Etkileşim durumu izleme**: Model, tek bir istek sırasında birden fazla kez konuşabildiğinden sunucu, arka plan işleme sırasında `interaction_status: "IN_PROGRESS"`, genel görev tamamlandığında ise `interaction_status: "IDLE"` yayar.

Aşağıdaki şemada, standart Live Voice oturumları ile arka plan gerekçelendirmesiyle düşünme arasındaki etkileşim yaşam döngüleri karşılaştırılmaktadır:

![Live API işlev çağrısı ve durum izleme karşılaştırması](https://ai.google.dev/static/gemini-api/docs/images/thinking-model-comparison.svg?hl=tr)

## Doğru modeli seçme

`gemini-3.8-live` ve `gemini-3.8-live-extended-thinking` arasında seçim yaparken üç temel unsuru göz önünde bulundurun: yanıt gecikmesi, görev karmaşıklığı ve istemci durumu işleme.

### Gemini 3.8 Live'ı ne zaman kullanmalısınız?

Anında sırayla konuşmanın önemli olduğu ve görevlerin doğrudan yapıldığı düşük gecikmeli konuşma sesli aracıları için `gemini-3.8-live` kullanın.

- **Sohbet odaklı sesli asistanlar**: Müşteri hizmetleri triyajı, dil pratiği, sesli arama ve etkileşimli hikaye anlatımı.
- **Hızlı araç yürütme**: Harici araçların milisaniyeler içinde döndüğü iş akışları (ör. sensör değerlerini okuma veya akıllı cihazları kontrol etme).
- **Basit istemci mantığı**: Her kullanıcı dönüşünün tek bir model yanıtı aldığı ve oturum boşta kaldığında `turnComplete: true` güvenilir bir şekilde sinyal veren uygulamalar.

### Genişletilmiş düşünme özellikli Gemini 3.8 Live'ı ne zaman kullanmalısınız?

Ajanınızın karmaşık verileri değerlendirmesi, birden fazla adımı planlaması veya çalışması birkaç saniye süren araçları kullanması gerektiğinde `gemini-3.8-live-extended-thinking` kullanın.

- **Çok adımlı teşhis ve destek**: Teknik destek temsilcileri, birden fazla günlük, hata kodu ve yapılandırma kontrolü genelinde sistem sorunlarını teşhis eder.
- **Koordineli veri alma**: Uçuş arayan, otelleri sorgulayan ve paralel API çağrıları arasında fiyatları karşılaştıran seyahat ve rezervasyon acenteleri.
- **FeTeMM ve kodlama eğitimi**: Formülleri doğrulayan, kodda hata ayıklayan veya açıklamada bulunmadan önce çok adımlı mantıkla çalışan eğitim aracıları.
- **Masking tool latency**: Uzun süren işlevlerin dinleyici için garip bir sessizliğe neden olacağı ses deneyimleri.

### Temel farkların özeti

Aşağıdaki tabloda, iki model arasındaki teknik farklılıklar özetlenmektedir:

| Özellik | Gemini 3.8 Live | Gemini 3.8 Live Extended Thinking |
| --- | --- | --- |
| **Birincil kullanım alanları** | Düşük gecikmeli sesli asistanlar, doğrudan komutlar, hızlı araçlar | Çok adımlı problem çözme, karmaşık planlama, çok araçlı iş akışları |
| **Model uç noktası** | `gemini-3.8-live` | `gemini-3.8-live-extended-thinking` |
| **Muhakeme mimarisi** | Sabit gecikme profiliyle aralıklı muhakeme (`thinking_level` desteklenmez) | Yapılandırılabilir arka plan gerekçelendirmesi (`thinking_level`: `low`, `medium`, `high`; `MINIMAL` desteklenmez) |
| **Sınırları belirleme** | `turnComplete: true`, dönüşü kapatır ve boşta kalma durumuna döner. | `turnComplete: true` bir ifadeyi tamamlar; `interaction_status` oturum yaşam döngüsünü kontrol eder. |
| **Sohbetlerde kullanılan dolgu kelimeler** | Model, konuşmadan önce aracın yürütülmesini bekliyor | Model, işleme sırasında ara sohbet dolguları yayınlar. |
| **Araç yürütme** | Eşzamanlı (`BLOCKING`) ve eşzamansız (`NON_BLOCKING`) araçları destekler. | Asenkron (`NON_BLOCKING`) araç beyanları gerektirir |

## Taşıma ve entegrasyon yolları

Mevcut ses uygulamalarını yükseltmek veya Thinking'i Live API oturumlarınıza entegre etmek için aşağıdaki adımları uygulayın.

### Gemini 3.1 Flash Live'dan yükseltme

`gemini-3.1-flash-live-preview` kullanan mevcut ses uygulamalarında `gemini-3.8-live`'ye yükseltmek için model dizesinin güncellenmesi ve `thinking_level`'nin (veya `thinking_config`) kurulum yapılandırmanızdan çıkarılması gerekir. `thinking_level`, `gemini-3.8-live` için desteklenmez:

```
{
  "setup": {
    "model": "models/gemini-3.8-live"
  }
}
```

Dönüşüm yaşam döngüsü ve `turnComplete` sinyalleri aynı kalır.

### Düşünme Sürecini Benimseme

`gemini-3.8-live-extended-thinking`'yı kullanmak için üç entegrasyon noktasını güncelleyin:

1. **`turnComplete` yerine `interaction_status` izleyin**: Düşünme oturumlarında model, akıl yürütme sırasında ara sohbet dolguları verebilir. Kullanıcı arayüzü durumunu yönetmek için gelen sunucu mesajlarındaki `interaction_status` alanını inceleyin. Yalnızca `interaction_status`, `IDLE` olduğunda boşta kalma moduna dönün.

   ### Python

   ```
   status = getattr(message, "interaction_status", None)
   if status == "IDLE":
       # Ready for user input
       set_ui_state("listening")
   elif status == "IN_PROGRESS":
       # Reasoning or executing tools
       set_ui_state("thinking")
   ```

   ### JavaScript

   ```
   if (message.interactionStatus === 'IDLE') {
     // Ready for user input
     setUiState('listening');
   } else if (message.interactionStatus === 'IN_PROGRESS') {
     // Reasoning or executing tools
     setUiState('thinking');
   }
   ```
2. **Engellemeyen işlevleri tanımlayın**: Tüm işlev tanımlamalarında `"behavior": "NON_BLOCKING"` değerini ayarlayın. Düşünme modelleri, sözlü güncellemeler yayınlarken araçları arka planda eşzamansız olarak çalıştırır. Senkronize engelleme araçları hata döndürüyor.

   ### Python

   ```
   search_flights = types.FunctionDeclaration(
       name="search_flights",
       description="Searches for available flights.",
       behavior="NON_BLOCKING",
       parameters={
           "type": "OBJECT",
           "properties": {
               "destination": {"type": "STRING"},
           },
           "required": ["destination"],
       },
   )
   ```

   ### JavaScript

   ```
   const searchFlights = {
     name: 'search_flights',
     description: 'Searches for available flights.',
     behavior: 'NON_BLOCKING',
     parameters: {
       type: 'OBJECT',
       properties: {
         destination: { type: 'STRING' },
       },
       required: ['destination'],
     },
   };
   ```
3. **Akıl yürütme derinliğini yapılandırma**: Oturum yapılandırmanızda `thinking_config` değerini ayarlayarak akıl yürütme seviyelerini (`low`, `medium` veya `high`; `MINIMAL` desteklenmez) düzenleyin.

   ### Python

   ```
   config = types.LiveConnectConfig(
       response_modalities=["AUDIO"],
       thinking_config=types.ThinkingConfig(
           thinking_level="low",
       ),
       tools=[types.Tool(function_declarations=[search_flights])],
   )
   ```

   ### JavaScript

   ```
   const config = {
     responseModalities: [Modality.AUDIO],
     thinkingConfig: {
       thinkingLevel: 'low',
     },
     tools: [{ functionDeclarations: [searchFlights] }],
   };
   ```

## Protokol yan yana karşılaştırması

Bu bölümde, bir Canlı API oturumunun her aşamasında değiştirilen WebSocket mesajları karşılaştırılır.

### 1. adım: Oturum kurulumu

Her iki model de aynı WebSocket uç noktasına bağlanır:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent?key=$API_KEY
```

- **Aynı**: WebSocket URL'si ve API anahtarı kimlik doğrulaması.
- **Model dizesi**: `gemini-3.8-live` versus
  `gemini-3.8-live-extended-thinking`.
- **Düşünme yapılandırması**: Düşünme, akıl yürütme derinliğini ayarlamak için `thinkingConfig` seçeneğini ekler.
- **Araç davranışı**: Düşünme, işlev bildirimlerinde `"behavior": "NON_BLOCKING"` gerektirir.

### Gemini 3.8 Live

```
{
  "setup": {
    "model": "models/gemini-3.8-live",
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "prebuiltVoiceConfig": {
            "voiceName": "Puck"
          }
        }
      }
    }
  }
}
```

### Gemini 3.8 Live Extended Thinking

```
{
  "setup": {
    "model": "models/gemini-3.8-live-extended-thinking",
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "prebuiltVoiceConfig": {
            "voiceName": "Puck"
          }
        }
      },
      "thinkingConfig": {
        "thinkingLevel": "LOW"
      }
    },
    "tools": [{
      "functionDeclarations": [{
        "name": "searchFlights",
        "description": "Searches for flights between cities.",
        "behavior": "NON_BLOCKING",
        "parameters": {
          "type": "OBJECT",
          "properties": {
            "destination": { "type": "STRING" }
          },
          "required": ["destination"]
        }
      }]
    }]
  }
}
```

Her iki model de bağlantı kurulduğunda aynı sunucu onayını alır:

```
{
  "setupComplete": {}
}
```

### 2. adım: Kullanıcı ses girişi

Ses akışı her iki modelde de aynıdır. Gerçek zamanlı 16 kHz ham PCM ses parçaları `realtimeInput` kullanılarak yayınlanır:

```
{
  "realtimeInput": {
    "audio": {
      "data": "UklGRiQAAABXQVZF...",
      "mimeType": "audio/pcm;rate=16000"
    }
  }
}
```

### 3. adım: Model yanıtı ve durum yaşam döngüsü

Her iki model de `serverContent.modelTurn` içinde 24 kHz PCM ses parçaları yayınlar. Ancak yaşam döngüsü yönetimi farklıdır:

#### Gemini 3.8 Live yanıt akışı

1. Sunucu, sıra için ses parçaları yayınlar.
2. Sunucu, modelin konuşmayı bitirdiğini ve oturumun boşta olduğunu belirten `turnComplete: true` karakterini gönderir.

```
// 1. Audio stream chunks
{
  "serverContent": {
    "modelTurn": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "audio/pcm;rate=24000",
            "data": "..."
          }
        }
      ]
    }
  }
}

// 2. Turn completion -> Signals client to switch UI to Idle/Listening
{
  "serverContent": {
    "turnComplete": true
  }
}
```

#### Gemini 3.8 Live Extended Thinking yanıt akışı

1. **Konuşma sırasında kullanılan dolgu kelimeleri**: Model, `turnComplete: true` ve `interactionStatus: "IN_PROGRESS"` ile ara konuşma (ör. *"Seattle'a uçuşları kontrol ediliyor..."*) yapıyor.
2. **Asenkron araç çağrısı**: Sunucu, araç çağrısını yayınlarken `interactionStatus` `"IN_PROGRESS"` olarak kalır. Bu, sunucunun çok adımlı dönüşü etkin bir şekilde işlediğini ve araç yanıtını beklediğini gösterir.
3. **Araç yanıtı**: İstemci, işlevi yürütür ve çıkışı döndürür.
4. **Son yanıt**: Sunucu, `turnComplete: true` ve `interactionStatus: "IDLE"` ile birlikte yanıtın tamamını sunar.

```
// 1. Spoken verbal filler while background reasoning proceeds
{
  "serverContent": {
    "modelTurn": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "audio/pcm;rate=24000",
            "data": "..."
          }
        }
      ]
    },
    "turnComplete": true,
    "interactionStatus": "IN_PROGRESS"
  }
}

// 2. Asynchronous tool call emitted with IN_PROGRESS status
{
  "toolCall": {
    "functionCalls": [
      {
        "id": "call_123",
        "name": "searchFlights",
        "args": {
          "destination": "Seattle"
        }
      }
    ]
  },
  "interactionStatus": "IN_PROGRESS"
}

// 3. Client executes function and returns result
{
  "toolResponse": {
    "functionResponses": [
      {
        "response": {
          "output": {
            "flight": "DL 145",
            "price": "$145"
          }
        },
        "id": "call_123"
      }
    ]
  }
}

// 4. Final spoken answer delivered -> session transitions to IDLE when done
{
  "serverContent": {
    "modelTurn": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "audio/pcm;rate=24000",
            "data": "..."
          }
        }
      ]
    },
    "interactionStatus": "IDLE",
    "turnComplete": true
  }
}
```

## SDK uygulama örnekleri

Aşağıdaki örneklerde, Google GenAI SDK'sını kullanarak Düşünme'yi nasıl yapılandıracağınız ve `interaction_status`'yı nasıl işleyeceğiniz gösterilmektedir.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live-extended-thinking"

# Define non-blocking function declaration
search_flights = types.FunctionDeclaration(
    name="search_flights",
    description="Searches for available flights to a destination.",
    behavior="NON_BLOCKING",
    parameters={
        "type": "OBJECT",
        "properties": {
            "destination": {"type": "STRING"}
        },
        "required": ["destination"]
    }
)

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    thinking_config=types.ThinkingConfig(
        thinking_level="low"
    ),
    tools=[types.Tool(function_declarations=[search_flights])]
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session connected with Thinking")

        async for message in session.receive():
            # Inspect interaction status for server lifecycle tracking
            status = getattr(message, "interaction_status", None)
            if status:
                print(f"Interaction status: {status}")

            # Handle audio output parts
            if message.server_content and message.server_content.model_turn:
                for part in message.server_content.model_turn.parts:
                    if part.inline_data:
                        # Process 24kHz audio chunk
                        pass

            # Handle asynchronous tool call
            if message.tool_call:
                for call in message.tool_call.function_calls:
                    print(f"Executing tool: {call.name}")
                    # Simulate function execution
                    response = types.FunctionResponse(
                        id=call.id,
                        name=call.name,
                        response={"result": "Flight DL 145 ($145)"}
                    )
                    await session.send_tool_response(
                        function_responses=[response]
                    )

            # Status is IDLE when reasoning and all turns are complete
            if status == "IDLE":
                print("Session is idle and ready for user input.")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live-extended-thinking';

const searchFlights = {
  name: 'search_flights',
  description: 'Searches for available flights to a destination.',
  behavior: 'NON_BLOCKING',
  parameters: {
    type: 'OBJECT',
    properties: {
      destination: { type: 'STRING' }
    },
    required: ['destination']
  }
};

const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low'
  },
  tools: [{ functionDeclarations: [searchFlights] }]
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.log('Session connected'),
      onmessage: async (event) => {
        const message = JSON.parse(event.data);

        if (message.interactionStatus) {
          console.log(`Interaction status: ${message.interactionStatus}`);
        }

        if (message.toolCall) {
          for (const call of message.toolCall.functionCalls) {
            console.log(`Executing tool: ${call.name}`);
            session.sendToolResponse({
              functionResponses: [{
                id: call.id,
                name: call.name,
                response: { result: 'Flight DL 145 ($145)' }
              }]
            });
          }
        }

        if (message.interactionStatus === 'IDLE') {
          console.log('Session is idle and waiting for input.');
        }
      }
    }
  });
}

main();
```

## Sırada ne var?

- [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=tr) ve [Gemini 3.8 Live Extended Thinking](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=tr) model sayfalarını okuyun.
- Tüm Live API modellerindeki ayrıntılı özellik karşılaştırmaları için [Model karşılaştırma](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=tr#model-comparison) tablosuna göz atın.
- [Live API Tool Use](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=tr) (Live API Aracı Kullanımı) kılavuzunda işlev çağırma hakkında daha fazla bilgi edinin.
- Oturumun devam ettirilmesi ve bağlam yaşam döngüsünü yönetmek için [Oturum yönetimi](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=tr)'ni inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-17 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-17 UTC."],[],[]]
