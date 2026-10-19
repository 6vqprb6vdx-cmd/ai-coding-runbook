---
source_url: https://ai.google.dev/gemini-api/docs/generate-content?hl=tr
fetched_at: 2026-10-19T05:30:18.493275+00:00
title: "Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)

# Gemini API

Gemini API; Gemini, Veo, Nano Banana ve diğer modellerle istemden üretime geçmenin en hızlı yoludur. Bu sayede, metin ve resim oluşturmak, çok formatlı girişleri analiz etmek ve sohbet aracısı oluşturmak için bu üretken modelleri uygulamalarınıza entegre edebilirsiniz.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-4-argon",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-4-argon",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-4-argon",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-4-argon", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
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

[Oluşturmaya başlayın](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)

---

## Modellerle tanışın

[Tümünü görüntüleyin](https://ai.google.dev/gemini-api/docs/models?hl=tr)

[auto\_awesome
Gemini 4 Argon
Yeni

Paylaşılan 1 milyon parçalık bağlam penceresi ve 1 milyon parçaya kadar uzun kod çözme özelliğine sahip amiral gemisi akıl yürütme modelimiz.](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=tr)
[spark
Gemini 3.6 Flash
Yeni

Temsilci ve çok formatlı görevlerde güçlü performans sunmak için hızı zekayla dengeleyen en yeni modelimiz.](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=tr)
[graphic\_eq
Gemini 3.8 Flash TTS
Yeni

İfade dolu oyunculuk, özel ses tasarımı ve ses kopyalama özelliklerine sahip, stüdyo kalitesinde bir metin okuma modeli.](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=tr)
[spark
Gemini 3.5 Flash-Lite
Yeni

Yüksek hacimli, maliyete duyarlı ve düşük gecikmeli yüksek gönderim hacmine sahip alt aracı görevleri için optimize edilmiş model.](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=tr)
[spark
Gemini 3.1 Flash-Lite

Gemini 3 serisinin performans ve kalitesine sahip, yüksek hacimli ve maliyet açısından hassas model.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr)
[spark
Gemini 3 Flash

Daha büyük modellerle rekabet eden öncü sınıf performansını çok daha düşük maliyetle sunar.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=tr)
[🍌
Nano Banana

Son teknoloji görüntü üretme ve düzenleme modelleri.](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)
[video\_library
Veo 3.1

Doğal ses özelliğine sahip, son teknolojiyle geliştirilen video üretme modelimiz.](https://ai.google.dev/gemini-api/docs/video?hl=tr)
[spark
Gemini Robotics

Gemini'ın ajan özelliklerini robotik alana taşıyan ve fiziksel dünyada gelişmiş akıl yürütme imkanı sunan bir görsel-dil modeli (VLM).](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=tr)

## Özellikleri keşfedin

[imagesmode

Yerel Görüntü Üretme (Nano Banana)

Gemini 2.5 Flash Image ile bağlama uygun görselleri yerel olarak üretip düzenleyin.](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)
[article

Uzun Bağlam

Gemini modellerine milyonlarca jeton girerek yapılandırılmamış resim, video ve dokümanlardan anlam çıkarın.](https://ai.google.dev/gemini-api/docs/long-context?hl=tr)
[code

Yapılandırılmış Çıkışlar

Gemini'ı, otomatik işleme uygun yapılandırılmış bir veri biçimi olan JSON ile yanıt vermeye zorlayın.](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)
[functions

İşlev Çağırma

Gemini'ı harici API'lere ve araçlara bağlayarak temsilci tabanlı iş akışları oluşturun.](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)
[videocam

Veo 3.1 ile video üretimi

Son teknolojiyle geliştirilen modelimizi kullanarak metin veya görüntü istemlerinden yüksek kaliteli video içerikleri oluşturun.](https://ai.google.dev/gemini-api/docs/video?hl=tr)
[android\_recorder

Live API ile Sesli Ajanlar

Live API ile anlık ses uygulamaları ve aracıları oluşturun.](https://ai.google.dev/gemini-api/docs/live-api?hl=tr)
[build

Araçlar

Google Arama, URL Bağlamı, Google Haritalar, kod yürütme ve bilgisayar kullanımı gibi yerleşik araçlar aracılığıyla Gemini'ı dünyaya bağlayın.](https://ai.google.dev/gemini-api/docs/tools?hl=tr)
[stacks

Belge Anlama

Tam çok formatlı anlayışla veya diğer metin tabanlı dosya türleriyle 1.000 sayfaya kadar PDF dosyası işleyin.](https://ai.google.dev/gemini-api/docs/document-processing?hl=tr)
[cognition\_2

Düşünen

Düşünme yeteneklerinin, karmaşık görevler ve ajanlar için akıl yürütmeyi nasıl iyileştirdiğini keşfedin.](https://ai.google.dev/gemini-api/docs/thinking?hl=tr)

[Google AI Studio

İstemleri test edin, API anahtarlarınızı yönetin, kullanımı izleyin ve prototipler oluşturun.](https://aistudio.google.com?hl=tr)
[group

Geliştirici Topluluğu

Diğer geliştiricilere ve Google mühendislerine soru sorup çözümler bulabilirsiniz.](https://discuss.ai.google.dev/c/gemini-api/4?hl=tr)
[menu\_book

API Referansı

Gemini API hakkında ayrıntılı bilgiyi resmi referans belgelerinde bulabilirsiniz.](https://ai.google.dev/api?hl=tr)
[sensors

Durum

Gemini API, Google AI Studio ve model hizmetlerimizin durumunu kontrol edin.](https://aistudio.google.com/status?hl=tr)

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-16 UTC.

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-16 UTC."],[],[]]
