---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr
fetched_at: 2026-09-07T05:31:18.308176+00:00
title: "Ba\u015flang\u0131\u00e7 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Başlangıç

Bu kılavuz, eski **generateContent** API'yi kullanmaya başlamanıza yardımcı olacaktır.
Yeni projeler ve uygulamalar için Gemini modelleri ve aracılarıyla geliştirme yapmanın en basit ve en iyi yolu olan yeni **Etkileşimler API'sini** kullanmanızı önemle tavsiye ederiz.

Bu hızlı başlangıç kılavuzunda, [kitaplıklarımızı](https://ai.google.dev/gemini-api/docs/libraries?hl=tr) nasıl yükleyeceğiniz, ilk isteğinizi nasıl yapacağınız, yanıtları nasıl akış şeklinde göstereceğiniz, çok aşamalı etkileşimleri nasıl oluşturacağınız ve standart `generateContent` yöntemini kullanarak araçları nasıl kullanacağınız gösterilmektedir.

## API anahtarı alma

Gemini API'yi kullanmak için isteklerinizin kimliğini doğrulamak, güvenlik sınırlarını zorunlu kılmak ve hesabınızdaki kullanımı izlemek üzere bir API anahtarınızın olması gerekir.

- Google AI Studio, yeni kullanıcılar için otomatik olarak bir proje ve API anahtarı oluşturur.
  Bu anahtarı [API anahtarları sayfasından](https://aistudio.google.com/api-keys?hl=tr) kopyalayabilirsiniz.
- Yeni bir anahtara ihtiyacınız varsa AI Studio'da **API anahtarı oluştur**'u tıklayın ve yeni bir anahtar-proje çifti eklemek için iletişim kutusunu takip edin.

[Gemini API anahtarı oluşturma](https://aistudio.google.com/apikey?hl=tr)

Anahtarınızı ortam değişkeni olarak ayarlayın:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Ücretli katmana yükseltme

Ücretli katmana yükseltme, hız sınırlarınızı artırır ve Cloud Billing'in ayarlanmasını gerektirir.

- AI Studio [API anahtarları](https://aistudio.google.com/api-keys?hl=tr) veya [Projeler](https://aistudio.google.com/projects?hl=tr) sayfalarında **Faturalandırma ayarlarını yap**'ı tıklayın.
- Faturalandırma hesabı oluşturmak veya bağlamak, ödeme yöntemi eklemek ve ücretli kredilerle en az 10 ABD doları (veya eşdeğeri) tutarında ön ödeme yapmak için Cloud Billing iletişim kutusundaki talimatları uygulayın.
- API kullanımınızı [Google AI Studio](https://aistudio.google.com/usage?hl=tr)'da **Kontrol Paneli** > **Kullanım** bölümünde görüntüleyebilirsiniz.

Daha fazla bilgi için [Faturalandırma sayfası](https://ai.google.dev/gemini-api/docs/billing?hl=tr)'na bakın.

## Google GenAI SDK'yı yükleme

### Python

[Python 3.9+](https://www.python.org/downloads/) sürümünü kullanarak aşağıdaki [pip komutunu](https://packaging.python.org/en/latest/tutorials/installing-packages/) kullanarak [`google-genai` paketini](https://pypi.org/project/google-genai/) yükleyin:

```
pip install -q -U google-genai
```

### JavaScript

[Node.js v18+](https://nodejs.org/en/download/package-manager)'ı kullanarak aşağıdaki [npm komutunu](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) kullanarak [TypeScript ve JavaScript için Google Gen AI SDK'sını](https://www.npmjs.com/package/@google/genai) yükleyin:

```
npm install @google/genai
```

## Metin oluşturun

`models.generate_content` yöntemini kullanarak [metin yanıtı oluşturun](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr).

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Yanıtları akış şeklinde göster

Varsayılan olarak, model yalnızca tüm oluşturma işlemi tamamlandıktan sonra yanıt verir. Daha hızlı ve etkileşimli bir deneyim için yanıt parçalarını oluşturuldukça [yayınlayabilirsiniz](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr#stream).

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## Çok aşamalı etkileşimli görüşmeler

SDK'lar, çok turlu sohbetler için durum bilgisi olan bir `chats` yardımcı sağlar. Bu yardımcı, etkileşim geçmişini otomatik olarak yöneten bir [çok turlu sohbet deneyimi](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr#chat) oluşturmaya yardımcı olur.

### Python

```
chat = client.chats.create(model="gemini-3.6-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.6-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## Araçları kullanma

Gerçek zamanlı web içeriğine erişmek için [yanıtları Google Arama ile temellendirerek](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) modelin yeteneklerini genişletin. Model, ne zaman arama yapacağına, sorguları ne zaman yürüteceğine ve yanıtı ne zaman sentezleyeceğine otomatik olarak karar verir.

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

Gemini API, diğer yerleşik araçları da destekler:

- **[Kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr)**:
  Modelin karmaşık matematik problemlerini çözmek için Python kodu yazıp çalıştırmasına olanak tanır.
- **[URL bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr)**: Yanıtları, sağladığınız belirli web sayfası URL'lerine dayandırmanıza olanak tanır.
- **[Dosya arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr)**: Dosyaları yüklemenize ve semantik aramayı kullanarak yanıtları içeriklerinde temellendirmenize olanak tanır.
- **[Google Haritalar](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr)**: Yanıtları konum verileriyle temellendirmenize ve yerleri, yol tariflerini ve haritaları aramanıza olanak tanır.
- **[Bilgisayar kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr)**: Modelin görevleri yerine getirmek için sanal bir bilgisayar ekranı, klavye ve fare ile etkileşime girmesine olanak tanır.

## Özel işlevleri çağırma

Modelleri özel araçlarınıza ve API'lerinize bağlamak için **[işlev çağrısını](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)** kullanın. Model, işlevinizi ne zaman çağıracağını belirler ve uygulamanızın yürütmesi için yanıtta bir `functionCall` döndürür.

Bu örnekte, sahte bir sıcaklık işlevi tanımlanır ve modelin bu işlevi çağırmak isteyip istemediği kontrol edilir.

### Python

```
from google import genai
from google.genai import types

weather_function = {
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.6-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## Sırada ne var?

Gemini API'yi kullanmaya başladığınıza göre, daha gelişmiş uygulamalar oluşturmak için aşağıdaki kılavuzları inceleyin:

- [Metin üretme](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr)
- [Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)
- [Görüntü anlama](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr)
- [Düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) (Thinking)
- [İşlev çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)
- [Google Arama ile temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr)
- [Uzun bağlam](https://ai.google.dev/gemini-api/docs/long-context?hl=tr)
- [Yerleştirmeler](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr)

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
