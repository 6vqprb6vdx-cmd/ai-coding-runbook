---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/image-generation?hl=tr
fetched_at: 2026-09-21T05:55:16.316309+00:00
title: "Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)

Geri bildirim gönderin

# Nano Banana ile görüntü üretme

Tam işlevli, kullanıcı arayüzü tamamlanmış uygulamaların prototipini oluşturmak için istem girin ve Nano Banana 2'nin gerçek dünya araçları, verileri ve Gemini ekosistemiyle entegre edildiğini görün. Tüm bunları tek bir kod satırı yazmadan yapabilirsiniz.

- [Nano Banana 2 uygulamasını deneyin](https://aistudio.google.com/apps/bundled/pet_passport?hl=tr)
- Dilerseniz istemleri kullanarak kendi uygulamanızı oluşturabilirsiniz:

- ![dergi](https://storage.googleapis.com/generativeai-downloads/images/magazine-2.jpg)
  ![londra](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/05-output.jpg)
  ![restore](https://storage.googleapis.com/generativeai-downloads/images/quetzal.png)
  ![muz](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/06-output.jpg)
  ![kafe](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/02-a-photo-of-an-everyday-scene-at-a-busy-cafe-servin.jpg)
  ![makale](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/10-use-search-to-find-how-the-gemini-3-flash-launch-h.jpg)
  ![köpek](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/01-an-icon-representing-a-cute-dog-the-background-is-.jpg)
  ![izometrik](https://storage.googleapis.com/generativeai-downloads/images/isometric-pool.jpg)
- ![dergi](https://storage.googleapis.com/generativeai-downloads/images/magazine-2.jpg)

  Nano Banana 2 tarafından üretildi

  **İstem:** "Parlak bir dergi kapağının fotoğrafı. Minimalist mavi kapakta büyük ve kalın Nano Banana yazıyor. Metin, serif yazı tipinde ve görünümü dolduruyor. Başka metin yok. Metnin önünde, şık ve minimalist bir elbise giymiş bir kişinin portresi var. Odak noktası olan 2 rakamını eğlenceli bir şekilde tutuyor.
    
  Köşeye, barkodun yanı sıra sayı numarasını ve "Şubat 2026" tarihini ekleyin. Dergi, tasarımcı mağazasında turuncu sıvalı bir duvarın önündeki rafta duruyor."

  [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2&hl=tr)'da [profesyonel ürün çekimleri](#4_product_mockups_commercial_photography) oluşturma
- ![londra](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/05-output.jpg)

  Nano Banana Pro ile üretildi

  **İstem:** "Londra'nın en ikonik simge yapılarını ve mimari unsurlarını içeren, 45 derecelik yukarıdan bakış açılı net bir izometrik minyatür 3D çizgi film sahnesi oluştur. Gerçekçi PBR malzemeleri ve yumuşak, gerçekçi ışıklandırma ve gölgelerle yumuşak ve zarif dokular kullanın. Etkileyici bir atmosfer oluşturmak için mevcut hava koşullarını doğrudan şehir ortamına entegre edin. Yumuşak ve tek renkli bir arka planla temiz ve minimalist bir kompozisyon kullanın. En üstte ortada, büyük ve kalın harflerle "Londra" başlığını, altında belirgin bir hava durumu simgesini, ardından tarihi (küçük metin) ve sıcaklığı (orta metin) yerleştirin. Tüm metinler, tutarlı bir boşlukla ortalanmalı ve binaların üst kısımlarıyla hafifçe çakışabilir."

  [Arama temellendirmesi](#use-with-grounding) hakkında daha fazla bilgi edinin ve [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2%2Csearch_grounding&hl=tr)'da deneyin.
- ![quetzal](https://storage.googleapis.com/generativeai-downloads/images/quetzal.png)

  Nano Banana 2 tarafından üretildi

  **İstem:** "Görsel arama özelliğini kullanarak parlak bir ketsal kuşunun doğru resimlerini bul. Bu kuşun, yukarıdan aşağıya doğal bir renk geçişi ve minimal bir kompozisyonla 3:2 oranında güzel bir duvar kağıdını oluştur."

  Nano Banana 2 ile Google [Görsel Arama](#image-search)'yı kullanın. [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2%2Csearch_grounding&hl=tr)'da deneyin.
- ![muz](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/06.jpg)

  Nano Banana Pro ile üretildi

  **İstem:** "Bu logoyu muz kokulu bir parfümün üst düzey reklamına yerleştir. Logo, şişeye mükemmel şekilde entegre edilmiş."

  [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2&hl=tr)'da Nano Banana'nın [yüksek kaliteli ayrıntı koruma](#5_high-fidelity_detail_preservation) özelliğini deneyin.
- ![kafe](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/02-a-photo-of-an-everyday-scene-at-a-busy-cafe-servin.jpg)

  Nano Banana Pro ile üretildi

  **İstem:** "Kahvaltı servisi yapan kalabalık bir kafedeki günlük bir sahnenin fotoğrafı. Ön planda mavi saçlı bir anime karakteri var. Kişilerden biri kalemle çizilmiş, diğeri ise kil animasyon karakteri.

  [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2&hl=tr)'da Nano Banana ile farklı [sanatsal stilleri](#3_style_transfer) deneyin.
- ![makale](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/10-use-search-to-find-how-the-gemini-3-flash-launch-h.jpg)

  Nano Banana Pro ile üretildi

  **İstem:** "Gemini 3 Flash'in kullanıma sunulmasının nasıl karşılandığını bulmak için aramayı kullan. Bu bilgileri kullanarak konuyla ilgili kısa bir makale (başlıklarla birlikte) yaz. Makalenin, tasarıma odaklanan parlak bir dergide göründüğü şeklinin fotoğrafını döndür. Bu resimde, Gemini 3 Flash ile ilgili makalenin yer aldığı, katlanmış tek bir sayfa gösteriliyor. Bir lokomotif fotoğraf. Serif yazı tipinde başlık."

  [Arama](#use-with-grounding) sonuçlarından [doğru metinler](#3_accurate_text_in_images) oluşturun. [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2%2Csearch_grounding&hl=tr)'da Nano Banana'yı deneyin
- ![köpek](https://storage.googleapis.com/generativeai-downloads/images/Nano%20Banana%20Pro%20outputs%20for%20docs/01-an-icon-representing-a-cute-dog-the-background-is-.jpg)

  Nano Banana Pro ile üretildi

  **İstem:** "Sevimli bir köpeği temsil eden simge. Arka plan beyaz olmalı. Simgeleri renkli ve dokunma hissi uyandıran 3D tarzında oluştur. Metin yok."

  [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2%2Csearch_grounding&hl=tr)'da Nano Banana ile [simgeler, çıkartmalar ve öğeler](#2_stylized_illustrations_stickers) oluşturma
- ![izometrik](https://storage.googleapis.com/generativeai-downloads/images/isometric-pool.jpg)

  Nano Banana 2 tarafından üretildi

  **İstem:** "Tamamen izometrik bir fotoğraf oluştur. Bu, minyatür değil, yalnızca mükemmel bir şekilde izometrik olan bir fotoğraftır. Bu, güzel bir modern bahçenin fotoğrafı. 2 şeklinde büyük bir havuz ve "Nano Banana 2" yazısı var."

  [AI Studio](https://aistudio.google.com/apps?features=nano_banana_2&hl=tr)'da [gerçekçi görüntü üretme](#1_photorealistic_scenes) özelliğini deneyin

**Nano Banana**, Gemini'ın yerel görüntü üretme özelliklerinin adıdır.
Gemini, metin, resim, video veya bunların kombinasyonuyla etkileşimli olarak resim oluşturabilir ve işleyebilir. Bu sayede, görselleri benzeri görülmemiş bir kontrolle oluşturabilir, düzenleyebilir ve yineleyebilirsiniz.

Nano Banana, Gemini API'de bulunan dört farklı modeli ifade eder:

- **Nano Banana 2 Lite ([Gemini 3.1 Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=tr))
  (`gemini-3.1-flash-lite-image`):** Hız ve maliyetin temel operasyonel kısıtlamalar olduğu durumlarda hız ve ölçek için tasarlanmış, en hızlı ve en uygun fiyatlı Gemini görüntü modelimiz. Birden fazla referans girişi veya çok aşamalı etkileşimli sıralı düzenleme için optimize edilmemiştir.
- **Nano Banana 2 ([Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=tr))
  (`gemini-3.1-flash-image`):** En çok yönlü modeldir ve tüm görevler için genel amaçlı bir model olarak kullanılır. Hız ile son teknoloji 4K görüntü üretimi, dünya bilgisi ve güvenilir metin oluşturma arasında denge kurar. Birden fazla referans görselin işlenmesi ve tutarlılık konusunda mükemmel sonuçlar verir.
- **Nano Banana Pro ([Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=tr))
  (`gemini-3-pro-image`):** En karmaşık görsel görevler için premium seçenek. Dünya bilgisi, gelişmiş yerelleştirme, marka tutarlılığı ve hassas yaratıcı kontrol konusunda en üst düzeyde performans sunar.
- **Nano Banana ([Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=tr))
  (`gemini-2.5-flash-image`):** Nano Banana serisinin öncüsü.
  Güvenilir bir araç olsa da müşterilerin gelişmiş kalite, daha hızlı oluşturma hızları ve daha düşük API fiyatlandırması için Nano Banana 2 Lite'a geçmelerini önemle tavsiye ederiz.

Üretilen tüm görüntülerde [SynthID filigranı](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=tr) bulunur.

## Görüntü üretme (metinden görüntü oluşturma)

### Python

```
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

prompt = ("Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme")
response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[prompt],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const prompt =
    "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme";

  const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: prompt,
  });
  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("gemini-native-image.png", buffer);
      console.log("Image saved as gemini-native-image.png");
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.1-flash-image",
      genai.Text("Create a picture of a nano banana dish in a " +
                 " fancy restaurant with a Gemini theme"),
  )

  for _, part := range result.Candidates[0].Content.Parts {
      if part.Text != "" {
          fmt.Println(part.Text)
      } else if part.InlineData != nil {
          imageBytes := part.InlineData.Data
          outputFilename := "gemini_generated_image.png"
          _ = os.WriteFile(outputFilename, imageBytes, 0644)
      }
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class TextToImage {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("TEXT", "IMAGE")
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image",
          "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme",
          config);

      for (Part part : response.parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("_01_generated_image.png"), blob.data().get());
          }
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class TextToImage {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme" }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("generated_image.png", imageBytes);
                Console.WriteLine("Image saved as generated_image.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"}
      ]
    }]
  }'
```

## Görüntü düzenleme (metin ve görüntüden görüntüye)

**Hatırlatma**: Yüklediğiniz tüm resimlerle ilgili gerekli haklara sahip olduğunuzdan emin olun.
Başkalarının haklarını ihlal eden içerikler (ör. yanıltıcı, taciz edici veya zarar verici videolar ya da görüntüler) üretmeyin. Bu üretken yapay zeka hizmetinin kullanımı [Yasaklanan Kullanım Politikamıza](https://policies.google.com/terms/generative-ai/use-policy?hl=tr) tabidir.

Resim sağlayın ve metin istemlerini kullanarak öğe ekleyin, kaldırın veya değiştirin, stili değiştirin ya da renk derecelendirmesini ayarlayın.

Aşağıdaki örnekte, `base64` kodlu resimlerin nasıl yükleneceği gösterilmektedir.
Birden fazla resim, daha büyük yükler ve desteklenen MIME türleri için [Resim anlama](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr) sayfasını inceleyin.

### Python

```
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

prompt = (
    "Create a picture of my cat eating a nano-banana in a "
    "fancy restaurant under the Gemini constellation",
)

image = Image.open("/path/to/cat_image.png")

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[prompt, image],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const imagePath = "path/to/cat_image.png";
  const imageData = fs.readFileSync(imagePath);
  const base64Image = imageData.toString("base64");

  const prompt = [
    { text: "Create a picture of my cat eating a nano-banana in a" +
            "fancy restaurant under the Gemini constellation" },
    {
      inlineData: {
        mimeType: "image/png",
        data: base64Image,
      },
    },
  ];

  const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: prompt,
  });
  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("gemini-native-image.png", buffer);
      console.log("Image saved as gemini-native-image.png");
    }
  }
}

main();
```

### Go

```
package main

import (
 "context"
 "fmt"
 "log"
 "os"
 "google.golang.org/genai"
)

func main() {

 ctx := context.Background()
 client, err := genai.NewClient(ctx, nil)
 if err != nil {
     log.Fatal(err)
 }

 imagePath := "/path/to/cat_image.png"
 imgData, _ := os.ReadFile(imagePath)

 parts := []*genai.Part{
   genai.NewPartFromText("Create a picture of my cat eating a nano-banana in a fancy restaurant under the Gemini constellation"),
   &genai.Part{
     InlineData: &genai.Blob{
       MIMEType: "image/png",
       Data:     imgData,
     },
   },
 }

 contents := []*genai.Content{
   genai.NewContentFromParts(parts, genai.RoleUser),
 }

 result, _ := client.Models.GenerateContent(
     ctx,
     "gemini-3.1-flash-image",
     contents,
 )

 for _, part := range result.Candidates[0].Content.Parts {
     if part.Text != "" {
         fmt.Println(part.Text)
     } else if part.InlineData != nil {
         imageBytes := part.InlineData.Data
         outputFilename := "gemini_generated_image.png"
         _ = os.WriteFile(outputFilename, imageBytes, 0644)
     }
 }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class TextAndImageToImage {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("TEXT", "IMAGE")
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image",
          Content.fromParts(
              Part.fromText("""
                  Create a picture of my cat eating a nano-banana in
                  a fancy restaurant under the Gemini constellation
                  """),
              Part.fromBytes(
                  Files.readAllBytes(
                      Path.of("src/main/resources/cat.jpg")),
                  "image/jpeg")),
          config);

      for (Part part : response.parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("gemini_generated_image.png"), blob.data().get());
          }
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class TextAndImageToImage {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "Create a picture of my cat eating a nano-banana in a fancy restaurant under the Gemini constellation" },
            new Part
            {
                FileData = new FileData { FileUri = "file:///path/to/cat_image.png" }
            }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("gemini_generated_image.png", imageBytes);
                Console.WriteLine("Image saved as gemini_generated_image.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d "{
      \"contents\": [{
        \"parts\":[
            {\"text\": \"'Create a picture of my cat eating a nano-banana in a fancy restaurant under the Gemini constellation\"},
            {
              \"inline_data\": {
                \"mime_type\":\"image/jpeg\",
                \"data\": \"<BASE64_IMAGE_DATA>\"
              }
            }
        ]
      }]
    }"
```

### Çok aşamalı etkileşimli görüntü düzenleme

Görsel oluşturmaya ve düzenlemeye sohbet ederek devam edin. Resimler üzerinde yineleme yapmak için sohbet veya çok turlu görüşme önerilir. Aşağıdaki örnekte, fotosentez hakkında infografik oluşturma istemi gösterilmektedir.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.1-flash-image",
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        tools=[{"google_search": {}}]
    )
)

message = "Create a vibrant infographic that explains photosynthesis as if it were a recipe for a plant's favorite food. Show the \"ingredients\" (sunlight, water, CO2) and the \"finished dish\" (sugar/energy). The style should be like a page from a colorful kids' cookbook, suitable for a 4th grader."

response = chat.send_message(message)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif image:= part.as_image():
        image.save("photosynthesis.png")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const chat = ai.chats.create({
    model: "gemini-3.1-flash-image",
    config: {
      responseModalities: ['TEXT', 'IMAGE'],
      tools: [{googleSearch: {}}],
    },
  });
}

await main();

const message = "Create a vibrant infographic that explains photosynthesis as if it were a recipe for a plant's favorite food. Show the \"ingredients\" (sunlight, water, CO2) and the \"finished dish\" (sugar/energy). The style should be like a page from a colorful kids' cookbook, suitable for a 4th grader."

let response = await chat.sendMessage({message});

for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("photosynthesis.png", buffer);
      console.log("Image saved as photosynthesis.png");
    }
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    model := client.GenerativeModel("gemini-3.1-flash-image")
    model.GenerationConfig = &pb.GenerationConfig{
        ResponseModalities: []pb.ResponseModality{genai.Text, genai.Image},
    }
    chat := model.StartChat()

    message := "Create a vibrant infographic that explains photosynthesis as if it were a recipe for a plant's favorite food. Show the \"ingredients\" (sunlight, water, CO2) and the \"finished dish\" (sugar/energy). The style should be like a page from a colorful kids' cookbook, suitable for a 4th grader."

    resp, err := chat.SendMessage(ctx, genai.Text(message))
    if err != nil {
        log.Fatal(err)
    }

    for _, part := range resp.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Printf("%s", string(txt))
        } else if img, ok := part.(genai.ImageData); ok {
            err := os.WriteFile("photosynthesis.png", img.Data, 0644)
            if err != nil {
                log.Fatal(err)
            }
        }
    }
}
```

### Java

```
import com.google.genai.Chat;
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.GoogleSearch;
import com.google.genai.types.ImageConfig;
import com.google.genai.types.Part;
import com.google.genai.types.RetrievalConfig;
import com.google.genai.types.Tool;
import com.google.genai.types.ToolConfig;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class MultiturnImageEditing {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {

      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("TEXT", "IMAGE")
          .tools(Tool.builder()
              .googleSearch(GoogleSearch.builder().build())
              .build())
          .build();

      Chat chat = client.chats.create("gemini-3.1-flash-image", config);

      GenerateContentResponse response = chat.sendMessage("""
          Create a vibrant infographic that explains photosynthesis
          as if it were a recipe for a plant's favorite food.
          Show the "ingredients" (sunlight, water, CO2)
          and the "finished dish" (sugar/energy).
          The style should be like a page from a colorful
          kids' cookbook, suitable for a 4th grader.
          """);

      for (Part part : response.parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("photosynthesis.png"), blob.data().get());
          }
        }
      }
      // ...
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class MultiturnImageEditing {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "Create a vibrant infographic that explains photosynthesis as if it were a recipe for a plant's favorite food. Show the \"ingredients\" (sunlight, water, CO2) and the \"finished dish\" (sugar/energy). The style should be like a page from a colorful kids' cookbook, suitable for a 4th grader." }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "TEXT", "IMAGE" },
            Tools = new List<Tool> { new Tool { GoogleSearch = new GoogleSearch() } }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("photosynthesis.png", imageBytes);
                Console.WriteLine("Image saved as photosynthesis.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [
        {"text": "Create a vibrant infographic that explains photosynthesis as if it were a recipe for a plants favorite food. Show the \"ingredients\" (sunlight, water, CO2) and the \"finished dish\" (sugar/energy). The style should be like a page from a colorful kids cookbook, suitable for a 4th grader."}
      ]
    }],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"]
    }
  }'
```

![Fotosentez hakkında yapay zekayla üretilmiş infografik](https://ai.google.dev/static/gemini-api/docs/images/infographic-eng.png?hl=tr)

Fotosentez hakkında yapay zekayla üretilmiş infografik

Ardından, grafikteki dili İspanyolca olarak değiştirmek için aynı sohbeti kullanabilirsiniz.

### Python

```
message = "Update this infographic to be in Spanish. Do not change any other elements of the image."
aspect_ratio = "16:9" # "1:1","1:4","1:8","2:3","3:2","3:4","4:1","4:3","4:5","5:4","8:1","9:16","16:9","21:9"
resolution = "2K" # "512", "1K", "2K", "4K"

response = chat.send_message(message,
    config=types.GenerateContentConfig(
        response_format={"image": {aspect_ratio: aspect_ratio,                 image_size: resolution}},
    ))

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif image:= part.as_image():
        image.save("photosynthesis_spanish.png")
```

### JavaScript

```
const message = 'Update this infographic to be in Spanish. Do not change any other elements of the image.';
const aspectRatio = '16:9';
const resolution = '2K';

let response = await chat.sendMessage({
  message,
  config: {
    responseModalities: ['TEXT', 'IMAGE'],
    responseFormat: {
    image: {
      aspectRatio: aspectRatio,
      imageSize: resolution,
    }
  },
    tools: [{googleSearch: {}}],
  },
});

for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("photosynthesis2.png", buffer);
      console.log("Image saved as photosynthesis2.png");
    }
}
```

### Go

```
message = "Update this infographic to be in Spanish. Do not change any other elements of the image."
aspect_ratio = "16:9" // "1:1","1:4","1:8","2:3","3:2","3:4","4:1","4:3","4:5","5:4","8:1","9:16","16:9","21:9"
resolution = "2K"     // "512", "1K", "2K", "4K"

model.GenerationConfig.ImageConfig = &pb.ImageConfig{
    AspectRatio: aspect_ratio,
    ImageSize:   resolution,
}

resp, err = chat.SendMessage(ctx, genai.Text(message))
if err != nil {
    log.Fatal(err)
}

for _, part := range resp.Candidates[0].Content.Parts {
    if txt, ok := part.(genai.Text); ok {
        fmt.Printf("%s", string(txt))
    } else if img, ok := part.(genai.ImageData); ok {
        err := os.WriteFile("photosynthesis_spanish.png", img.Data, 0644)
        if err != nil {
            log.Fatal(err)
        }
    }
}
```

### Java

```
String aspectRatio = "16:9"; // "1:1","1:4","1:8","2:3","3:2","3:4","4:1","4:3","4:5","5:4","8:1","9:16","16:9","21:9"
String resolution = "2K"; // "512", "1K", "2K", "4K"

config = GenerateContentConfig.builder()
    .responseModalities("TEXT", "IMAGE")
    .imageConfig(ImageConfig.builder()
        .aspectRatio(aspectRatio)
        .imageSize(resolution)
        .build())
    .build();

response = chat.sendMessage(
    "Update this infographic to be in Spanish. " +
    "Do not change any other elements of the image.",
    config);

for (Part part : response.parts()) {
  if (part.text().isPresent()) {
    System.out.println(part.text().get());
  } else if (part.inlineData().isPresent()) {
    var blob = part.inlineData().get();
    if (blob.data().isPresent()) {
      Files.write(Paths.get("photosynthesis_spanish.png"), blob.data().get());
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class MultiturnImageEditingSpanish {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "Update this infographic to be in Spanish. Do not change any other elements of the image." }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "TEXT", "IMAGE" },
            ImageConfig = new ImageConfig
            {
                AspectRatio = "16:9",
                ImageSize = "2K"
            }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("photosynthesis_spanish.png", imageBytes);
                Console.WriteLine("Image saved as photosynthesis_spanish.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "Create a vibrant infographic that explains photosynthesis..."}]
      },
      {
        "role": "model",
        "parts": [{"inline_data": {"mime_type": "image/png", "data": "<PREVIOUS_IMAGE_DATA>"}}]
      },
      {
        "role": "user",
        "parts": [{"text": "Update this infographic to be in Spanish. Do not change any other elements of the image."}]
      }
    ],
    "tools": [{"google_search": {}}],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"],
      "responseFormat": {
    "image": {
        "aspectRatio": "16:9",
        "imageSize": "2K"
      }
  }
    }
  }'
```

![İspanyolca fotosentez infografiği (yapay zekayla üretilmiş)](https://ai.google.dev/static/gemini-api/docs/images/infographic-spanish.png?hl=tr)

İspanyolca fotosentez infografiği (yapay zekayla üretilmiş)

## Gemini 3 görüntü modelleriyle gelen yenilikler

Gemini 3, son teknoloji görüntü üretme ve düzenleme modelleri sunar. Gemini 3.1
Flash Image, hız ve yüksek hacimli kullanım alanları için, Gemini 3
Pro Image ise profesyonel öğe üretimi için optimize edilmiştir.
Gelişmiş akıl yürütme yoluyla en zorlu iş akışlarının üstesinden gelmek için tasarlanan bu modeller, karmaşık ve çok aşamalı etkileşim içerik oluşturma ve değiştirme görevlerinde üstün performans gösterir.

- **Yüksek çözünürlüklü çıktı**: 1K, 2K ve 4K görseller için yerleşik üretim özellikleri.
  - **Gemini 3.1 Flash Image**, daha küçük olan 512 (0,5K) çözünürlüğünü ekler.
  - **Gemini 3.1 Flash Lite Image** yalnızca 1K çözünürlüğü destekler.
- **Gelişmiş metin oluşturma**: İnfografikler, menüler, diyagramlar ve pazarlama öğeleri için okunaklı ve stilize edilmiş metinler oluşturabilir.
- **Google Arama ile temellendirme**: Model, Google Arama'yı bir araç olarak kullanarak gerçekleri doğrulayabilir ve gerçek zamanlı verilere (ör. güncel hava durumu haritaları, borsa grafikleri, son olaylar) dayalı görüntüler oluşturabilir.
  - **Gemini 3.1 Flash Lite Image modeli tarafından desteklenmez.**
  - **Gemini 3.1 Flash Image**, Web Araması'nın yanı sıra Görüntüler için Google Arama ile Temellendirme entegrasyonunu ekler.
- **Düşünme modu**: Model, karmaşık istemleri değerlendirmek için "düşünme" sürecini kullanır. Son yüksek kaliteli çıktıyı üretmeden önce kompozisyonu iyileştirmek için geçici "düşünce resimleri" oluşturur (arka uçta görünür ancak ücretlendirilmez).
- **En fazla 14 referans görsel**: Artık nihai resmi oluşturmak için en fazla 14 referans görseli karıştırabilirsiniz.
- **Yeni en-boy oranları**: Gemini 3.1 Flash Lite Image, `1:1`, `3:2`,
  `2:3`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` [en-boy oranlarını](#aspect_ratios_and_image_size) ekler.

### En fazla 14 referans görsel kullanın

Gemini 3 görüntü modelleri, 14 adede kadar referans görseli karıştırmanıza olanak tanır. Bu 14 resim aşağıdakileri içerebilir:

| Gemini 3.1 Flash Lite Image | Gemini 3.1 Flash Görüntüsü | Gemini 3 Pro Image |
| --- | --- | --- |
| Son resme eklenecek, yüksek çözünürlüklü en fazla 14 nesne resmi | Son resme eklenecek, yüksek çözünürlüklü en fazla 10 nesne resmi | Son resme eklenecek, yüksek çözünürlüklü en fazla 6 nesne resmi |
| Yok | Karakter tutarlılığını korumak için en fazla 4 karakter resmi | Karakter tutarlılığını korumak için en fazla 5 karakter resmi |
| Yok | Yok | Stil referansı olarak kullanılacak en fazla 3 resim |

### Python

```
from google import genai
from google.genai import types
from PIL import Image

prompt = "An office group photo of these people, they are making funny faces."
aspect_ratio = "5:4" # "1:1","1:4","1:8","2:3","3:2","3:4","4:1","4:3","4:5","5:4","8:1","9:16","16:9","21:9"
resolution = "2K" # "512", "1K", "2K", "4K"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[
        prompt,
        Image.open('person1.png'),
        Image.open('person2.png'),
        Image.open('person3.png'),
        Image.open('person4.png'),
        Image.open('person5.png'),
    ],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        response_format={"image": {aspect_ratio: aspect_ratio,                 image_size: resolution}},
    )
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif image:= part.as_image():
        image.save("office.png")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const prompt =
      'An office group photo of these people, they are making funny faces.';
  const aspectRatio = '5:4';
  const resolution = '2K';

const contents = [
  { text: prompt },
  {
    inlineData: {
      mimeType: "image/jpeg",
      data: base64ImageFile1,
    },
  },
  {
    inlineData: {
      mimeType: "image/jpeg",
      data: base64ImageFile2,
    },
  },
  {
    inlineData: {
      mimeType: "image/jpeg",
      data: base64ImageFile3,
    },
  },
  {
    inlineData: {
      mimeType: "image/jpeg",
      data: base64ImageFile4,
    },
  },
  {
    inlineData: {
      mimeType: "image/jpeg",
      data: base64ImageFile5,
    },
  }
];

const response = await ai.models.generateContent({
    model: 'gemini-3.1-flash-image',
    contents: contents,
    config: {
      responseModalities: ['TEXT', 'IMAGE'],
      responseFormat: {
    image: {
        aspectRatio: aspectRatio,
        imageSize: resolution,
      }
  },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("image.png", buffer);
      console.log("Image saved as image.png");
    }
  }

}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    model := client.GenerativeModel("gemini-3.1-flash-image")
    model.GenerationConfig = &pb.GenerationConfig{
        ResponseModalities: []pb.ResponseModality{genai.Text, genai.Image},
        ImageConfig: &pb.ImageConfig{
            AspectRatio: "5:4",
            ImageSize:   "2K",
        },
    }

    img1, err := os.ReadFile("person1.png")
    if err != nil { log.Fatal(err) }
    img2, err := os.ReadFile("person2.png")
    if err != nil { log.Fatal(err) }
    img3, err := os.ReadFile("person3.png")
    if err != nil { log.Fatal(err) }
    img4, err := os.ReadFile("person4.png")
    if err != nil { log.Fatal(err) }
    img5, err := os.ReadFile("person5.png")
    if err != nil { log.Fatal(err) }

    parts := []genai.Part{
        genai.Text("An office group photo of these people, they are making funny faces."),
        genai.ImageData{MIMEType: "image/png", Data: img1},
        genai.ImageData{MIMEType: "image/png", Data: img2},
        genai.ImageData{MIMEType: "image/png", Data: img3},
        genai.ImageData{MIMEType: "image/png", Data: img4},
        genai.ImageData{MIMEType: "image/png", Data: img5},
    }

    resp, err := model.GenerateContent(ctx, parts...)
    if err != nil {
        log.Fatal(err)
    }

    for _, part := range resp.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Printf("%s", string(txt))
        } else if img, ok := part.(genai.ImageData); ok {
            err := os.WriteFile("office.png", img.Data, 0644)
            if err != nil {
                log.Fatal(err)
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.ImageConfig;
import com.google.genai.types.Part;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class GroupPhoto {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("TEXT", "IMAGE")
          .imageConfig(ImageConfig.builder()
              .aspectRatio("5:4")
              .imageSize("2K")
              .build())
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image",
          Content.fromParts(
              Part.fromText("An office group photo of these people, they are making funny faces."),
              Part.fromBytes(Files.readAllBytes(Path.of("person1.png")), "image/png"),
              Part.fromBytes(Files.readAllBytes(Path.of("person2.png")), "image/png"),
              Part.fromBytes(Files.readAllBytes(Path.of("person3.png")), "image/png"),
              Part.fromBytes(Files.readAllBytes(Path.of("person4.png")), "image/png"),
              Part.fromBytes(Files.readAllBytes(Path.of("person5.png")), "image/png")
          ), config);

      for (Part part : response.parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("office.png"), blob.data().get());
          }
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class GroupPhoto {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "An office group photo of these people, they are making funny faces." },
            new Part { FileData = new FileData { FileUri = "file:///person1.png" } },
            new Part { FileData = new FileData { FileUri = "file:///person2.png" } },
            new Part { FileData = new FileData { FileUri = "file:///person3.png" } },
            new Part { FileData = new FileData { FileUri = "file:///person4.png" } },
            new Part { FileData = new FileData { FileUri = "file:///person5.png" } }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "TEXT", "IMAGE" },
            ImageConfig = new ImageConfig
            {
                AspectRatio = "5:4",
                ImageSize = "2K"
            }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("office.png", imageBytes);
                Console.WriteLine("Image saved as office.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d "{
      \"contents\": [{
        \"parts\":[
            {\"text\": \"An office group photo of these people, they are making funny faces.\"},
            {\"inline_data\": {\"mime_type\":\"image/png\", \"data\": \"<BASE64_DATA_IMG_1>\"}},
            {\"inline_data\": {\"mime_type\":\"image/png\", \"data\": \"<BASE64_DATA_IMG_2>\"}},
            {\"inline_data\": {\"mime_type\":\"image/png\", \"data\": \"<BASE64_DATA_IMG_3>\"}},
            {\"inline_data\": {\"mime_type\":\"image/png\", \"data\": \"<BASE64_DATA_IMG_4>\"}},
            {\"inline_data\": {\"mime_type\":\"image/png\", \"data\": \"<BASE64_DATA_IMG_5>\"}}
        ]
      }],
      \"generationConfig\": {
        \"responseModalities\": [\"TEXT\", \"IMAGE\"],
        \"responseFormat\": {
        \"image\": {
          \"aspectRatio\": \"5:4\",
          \"imageSize\": \"2K\"
        }
      }
      }
    }"
```

![Yapay zekayla üretilmiş ofis grubu fotoğrafı](https://ai.google.dev/static/gemini-api/docs/images/office-group-photo.jpeg?hl=tr)

Yapay zekayla üretilmiş ofis grubu fotoğrafı

### Google Arama ile Temellendirme

Hava durumu tahminleri, borsa grafikleri veya son olaylar gibi anlık bilgilere dayalı görüntüler oluşturmak için [Google Arama aracını](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) kullanın.

Google Arama ile temellendirme, görüntü oluşturma ile birlikte kullanılırken görüntü tabanlı arama sonuçlarının oluşturma modeline aktarılmadığını ve yanıttan çıkarıldığını unutmayın (bkz. [Görüntüler için Google Arama ile temellendirme](#image-search)).

### Python

```
from google import genai
prompt = "Visualize the current weather forecast for the next 5 days in San Francisco as a clean, modern weather chart. Add a visual on what I should wear each day"
aspect_ratio = "16:9" # "1:1","1:4","1:8","2:3","3:2","3:4","4:1","4:3","4:5","5:4","8:1","9:16","16:9","21:9"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=['Text', 'Image'],
        response_format={"image": {aspect_ratio: aspect_ratio,}},
        tools=[{"google_search": {}}]
    )
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif image:= part.as_image():
        image.save("weather.png")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const prompt = 'Visualize the current weather forecast for the next 5 days in San Francisco as a clean, modern weather chart. Add a visual on what I should wear each day';
  const aspectRatio = '16:9';
  const resolution = '2K';

const response = await ai.models.generateContent({
    model: 'gemini-3.1-flash-image',
    contents: prompt,
    config: {
      responseModalities: ['TEXT', 'IMAGE'],
      responseFormat: {
    image: {
        aspectRatio: aspectRatio,
        imageSize: resolution,
      }
  },
    tools: [{ googleSearch: {} }]
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("image.png", buffer);
      console.log("Image saved as image.png");
    }
  }

}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.GoogleSearch;
import com.google.genai.types.ImageConfig;
import com.google.genai.types.Part;
import com.google.genai.types.Tool;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class SearchGrounding {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("TEXT", "IMAGE")
          .imageConfig(ImageConfig.builder()
              .aspectRatio("16:9")
              .build())
          .tools(Tool.builder()
              .googleSearch(GoogleSearch.builder().build())
              .build())
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image", """
              Visualize the current weather forecast for the next 5 days
              in San Francisco as a clean, modern weather chart.
              Add a visual on what I should wear each day
              """,
          config);

      for (Part part : response.parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("weather.png"), blob.data().get());
          }
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class SearchGrounding {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "Visualize the current weather forecast for the next 5 days in San Francisco as a clean, modern weather chart. Add a visual on what I should wear each day" }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "TEXT", "IMAGE" },
            ImageConfig = new ImageConfig
            {
                AspectRatio = "16:9"
            },
            Tools = new List<Tool> { new Tool { GoogleSearch = new GoogleSearch() } }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("weather.png", imageBytes);
                Console.WriteLine("Image saved as weather.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "Visualize the current weather forecast for the next 5 days in San Francisco as a clean, modern weather chart. Add a visual on what I should wear each day"}]}],
    "tools": [{"google_search": {}}],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"],
      "responseFormat": {
    "image": {"aspectRatio": "16:9"}
  }
    }
  }'
```

![San Francisco için yapay zekayla üretilmiş beş günlük hava durumu grafiği](https://ai.google.dev/static/gemini-api/docs/images/weather-forecast.png?hl=tr)

San Francisco için yapay zekayla üretilmiş beş günlük hava durumu grafiği

Yanıtta, aşağıdaki zorunlu alanları içeren `groundingMetadata` yer alıyor:

- **`searchEntryPoint`**: Gerekli arama önerilerini oluşturmak için HTML ve CSS'yi içerir.
- **`groundingChunks`**: Oluşturulan görüntüyü temellendirmek için kullanılan en iyi 3 web kaynağını döndürür.

### Görseller için Google Arama ile temellendirme (3.1 Flash)

Görseller için Google Arama ile temellendirme, modellerin Google Arama aracılığıyla alınan web görsellerini görüntü oluşturma için görsel bağlam olarak kullanmasına olanak tanır. Görsel Arama, mevcut Google Arama ile Temellendirme aracındaki yeni bir arama türüdür ve standart [Web Arama](#use-with-grounding) ile birlikte çalışır.

Görsel Arama'yı etkinleştirmek için API isteğinizde `googleSearch` aracını yapılandırın
ve `searchTypes` nesnesinde `imageSearch` değerini belirtin. Görsel Arama bağımsız olarak veya Web Arama ile birlikte kullanılabilir.

Resimler için Google Arama ile Temellendirme özelliğinin, insan aramak için kullanılamayacağını unutmayın.

### Python

```
from google import genai
prompt = "A detailed painting of a Timareta butterfly resting on a flower"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        tools=[
            types.Tool(google_search=types.GoogleSearch(
                search_types=types.SearchTypes(
                    web_search=types.WebSearch(),
                    image_search=types.ImageSearch()
                )
            ))
        ]
    )
)

# Display grounding sources if available
if response.candidates and response.candidates[0].grounding_metadata and response.candidates[0].grounding_metadata.search_entry_point:
    display(HTML(response.candidates[0].grounding_metadata.search_entry_point.rendered_content))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {

  const ai = new GoogleGenAI({});

  const prompt = "A detailed painting of a Timareta butterfly resting on a flower";

  const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: prompt,
    config: {
      responseModalities: ["IMAGE"],
      tools: [
        {
          googleSearch: {
            searchTypes: {
              webSearch: {},
              imageSearch: {}
            }
          }
        }
      ]
    }
  });

  // Display grounding sources if available
  if (response.candidates && response.candidates[0].groundingMetadata && response.candidates[0].groundingMetadata.searchEntryPoint) {
      console.log(response.candidates[0].groundingMetadata.searchEntryPoint.renderedContent);
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"

  "google.golang.org/genai"
  pb "google.golang.org/genai/schema"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
    log.Fatal(err)
  }
  defer client.Close()

  model := client.GenerativeModel("gemini-3.1-flash-image")
  model.Tools = []*pb.Tool{
    {
      GoogleSearch: &pb.GoogleSearch{
        SearchTypes: &pb.SearchTypes{
          WebSearch:   &pb.WebSearch{},
          ImageSearch: &pb.ImageSearch{},
        },
      },
    },
  }
  model.GenerationConfig = &pb.GenerationConfig{
    ResponseModalities: []pb.ResponseModality{genai.Image},
  }

  prompt := "A detailed painting of a Timareta butterfly resting on a flower"
  resp, err := model.GenerateContent(ctx, genai.Text(prompt))
  if err != nil {
    log.Fatal(err)
  }

  if resp.Candidates[0].GroundingMetadata != nil && resp.Candidates[0].GroundingMetadata.SearchEntryPoint != nil {
    fmt.Println(resp.Candidates[0].GroundingMetadata.SearchEntryPoint.RenderedContent)
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.GoogleSearch;
import com.google.genai.types.ImageSearch;
import com.google.genai.types.SearchTypes;
import com.google.genai.types.Tool;
import com.google.genai.types.WebSearch;

import java.io.IOException;

public class ImageSearchGrounding {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("IMAGE")
          .tools(Tool.builder()
              .googleSearch(GoogleSearch.builder()
                  .searchTypes(SearchTypes.builder()
                      .webSearch(WebSearch.builder().build())
                      .imageSearch(ImageSearch.builder().build())
                      .build())
                  .build())
              .build())
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image",
          "A detailed painting of a Timareta butterfly resting on a flower",
          config);

      if (response.candidates().isPresent() && !response.candidates().get().isEmpty()) {
        var candidate = response.candidates().get().get(0);
        if (candidate.groundingMetadata().isPresent() && candidate.groundingMetadata().get().searchEntryPoint().isPresent()) {
          System.out.println(candidate.groundingMetadata().get().searchEntryPoint().get().renderedContent().orElse(""));
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public class ImageSearchGrounding {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "A detailed painting of a Timareta butterfly resting on a flower" }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "IMAGE" },
            Tools = new List<Tool>
            {
                new Tool
                {
                    GoogleSearch = new GoogleSearch
                    {
                        SearchTypes = new SearchTypes
                        {
                            WebSearch = new WebSearch(),
                            ImageSearch = new ImageSearch()
                        }
                    }
                }
            }
        }
    );

    foreach (var candidate in response.Candidates) {
        if (candidate.GroundingMetadata != null && candidate.GroundingMetadata.SearchEntryPoint != null) {
            Console.WriteLine(candidate.GroundingMetadata.SearchEntryPoint.RenderedContent);
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "A detailed painting of a Timareta butterfly resting on a flower"}]}],
    "tools": [{"google_search": {"searchTypes": {"webSearch": {}, "imageSearch": {}}}}],
    "generationConfig": {
      "responseModalities": ["IMAGE"]
    }
  }'
```

**Görüntüleme koşulları**

Google Arama ile Temellendirme'de Görsel Arama'yı kullanırken aşağıdaki koşullara uymanız gerekir:

- **Kaynak atfı**: Kaynak resmi içeren web sayfasına (resim dosyası değil,"içeren sayfa") kullanıcı tarafından bağlantı olarak tanınacak şekilde bir bağlantı sağlamanız gerekir.
- **Doğrudan gezinme**: Kaynak resimleri de göstermeyi seçerseniz kaynak resimlerden bunları içeren kaynak web sayfasına doğrudan, tek tıklamayla erişilebilen bir yol sağlamanız gerekir. Son kullanıcının kaynak web sayfasına erişimini geciktiren veya soyutlayan diğer tüm uygulamalara (ör. çok tıklamalı yol veya ara resim görüntüleyici kullanımı) izin verilmez.

**Yanıt**

API, görsel arama kullanılarak kaynağa dayalı yanıtlarda, çıktısını doğrulanmış kaynaklara bağlamak için net atıf ve meta veri sağlar. `groundingMetadata` nesnesindeki temel alanlar şunlardır:

- **`imageSearchQueries`**: Modelin görsel bağlam (görsel arama) için kullandığı belirli sorgular.
- **`groundingChunks`**: Alınan sonuçlarla ilgili kaynak bilgilerini içerir.
  Resim kaynakları için bunlar, yeni bir resim parçası türü kullanılarak yönlendirme URL'leri olarak döndürülür. Bu parça şunları içerir:

  - **`uri`**: İlişkilendirme için kullanılan web sayfası URL'si (açılış sayfası).
  - **`image_uri`**: Doğrudan resim URL'si.
- **`groundingSupports`**: Oluşturulan içeriği parçalardaki ilgili alıntı kaynağına bağlayan belirli eşlemeler sağlar.
- **`searchEntryPoint`**: Arama Önerileri'ni oluşturmak için uyumlu HTML ve CSS içeren "Google Arama" çipini içerir.

### Video-görüntü üretimi (3.1 Flash ve 3.1 Flash Lite)

Video-görsel üretimi, çok formatlı bir referans olarak videonun bağlamını kullanarak yeni görseller oluşturmanıza olanak tanır. Bu özellik; yüksek kaliteli video küçük resimleri, sinematik posterler, özet infografikleri veya bir video sahnesinden ilham alan yeni sanat eserleri oluşturmak için kullanışlıdır.

Oluşturma sırasında model, görsel temaları ve önemli etkinlikleri ayıklamak için video karelerini bağlam içinde (modelin giriş jetonu sınırı olan 131.072 jetona kadar) analiz eder. Ardından, çıkış resmini sentezlemek için bunları metin isteminizle birlikte kullanır.

Herkese açık [YouTube URL'lerini](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr#youtube) doğrudan API isteğinize iletebilir veya [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr)'yi kullanarak yerel video dosyalarını yükleyebilirsiniz.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Pass a public YouTube video URL as part of the contents
response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[
        types.Part(
          file_data=types.FileData(file_uri="https://www.youtube.com/watch?v=UTdfxFyOQTI"),
          video_metadata=types.VideoMetadata(fps=0.5)
        ),
        "Generate a poster image that captures the key themes of this video."
    ],
    config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"]
    )
)

# Save the generated image part
for part in response.parts:
    if part.inline_data is not None:
        image = part.as_image()
        image.save("video_poster.png")
        print("Image saved as video_poster.png")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
  const ai = new GoogleGenAI({});

  const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: [
      {
        fileData: {
          fileUri: "https://www.youtube.com/watch?v=UTdfxFyOQTI",
        },
        videoMetadata: {
          fps: 0.5
        }
      },
      { text: "Generate a poster image that captures the key themes of this video." }
    ],
    config: {
      responseModalities: ["TEXT", "IMAGE"]
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("video_poster.png", buffer);
      console.log("Image saved as video_poster.png");
    }
  }
}

main();
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    videoPart := genai.NewPartFromURI("https://www.youtube.com/watch?v=UTdfxFyOQTI", "video/mp4")
    videoPart.VideoMetadata = &genai.VideoMetadata{FPS: genai.Ptr(0.5)}

    parts := []*genai.Part{
        videoPart,
        genai.NewPartFromText("Generate a poster image that captures the key themes of this video."),
    }

    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.1-flash-image",
        contents,
        &genai.GenerateContentConfig{
            ResponseModalities: []string{"TEXT", "IMAGE"},
        },
    )
    if err != nil {
        log.Fatal(err)
    }

    for _, part := range result.Candidates[0].Content.Parts {
        if part.InlineData != nil {
            imageBytes := part.InlineData.Data
            _ = os.WriteFile("video_poster.png", imageBytes, 0644)
            log.Println("Image saved as video_poster.png")
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.FileData;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import com.google.genai.types.VideoMetadata;
import com.google.common.collect.ImmutableList;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class VideoToImage {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      Part videoPart = Part.builder()
          .fileData(FileData.builder()
              .fileUri("https://www.youtube.com/watch?v=UTdfxFyOQTI")
              .build())
          .videoMetadata(VideoMetadata.builder()
              .fps(0.5)
              .build())
          .build();

      Part textPart = Part.builder()
          .text("Generate a poster image that captures the key themes of this video.")
          .build();

      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("TEXT", "IMAGE")
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image",
          Content.builder()
              .role("user")
              .parts(ImmutableList.of(videoPart, textPart))
              .build(),
          config);

      for (Part part : response.parts()) {
        if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("video_poster.png"), blob.data().get());
            System.out.println("Image saved as video_poster.png");
          }
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using Google.GenAI.Types;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class VideoToImage {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part
            {
                FileData = new FileData { FileUri = "https://www.youtube.com/watch?v=UTdfxFyOQTI" },
                VideoMetadata = new VideoMetadata { Fps = 0.5 }
            },
            new Part { Text = "Generate a poster image that captures the key themes of this video." }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "TEXT", "IMAGE" }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("video_poster.png", imageBytes);
                Console.WriteLine("Image saved as video_poster.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "https://www.youtube.com/watch?v=UTdfxFyOQTI"
          },
          "video_metadata": {
            "fps": 0.5
          }
        },
        {"text": "Generate a poster image that captures the key themes of this video."}
      ]
    }],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"]
    }
  }'
```

![YouTube videosundan yapay zekayla üretilen infografik](https://ai.google.dev/static/gemini-api/docs/images/youtube_infographics.png?hl=tr)

YouTube videosundan yapay zekayla üretilmiş bilgi grafiği

### 4K çözünürlüğe kadar resim oluşturma

Gemini 3 görüntü modelleri varsayılan olarak 1.000 görüntü oluşturur ancak 2.000, 4.000 ve 512 (0, 5K) görüntü de üretebilir (yalnızca Gemini 3.1 Flash Image). Daha yüksek çözünürlüklü öğeler oluşturmak için `generation_config` içinde `image_size` değerini belirtin.

Büyük harf "K" kullanmanız gerekir (ör. 1K, 2K, 4K). `512` değerinde "K" soneki kullanılmıyor. Küçük harfli parametreler (ör. 1k) reddedilir.

### Python

```
from google import genai
from google.genai import types

prompt = "Da Vinci style anatomical sketch of a dissected Monarch butterfly. Detailed drawings of the head, wings, and legs on textured parchment with notes in English."
aspect_ratio = "1:1" # "1:1","1:4","1:8","2:3","3:2","3:4","4:1","4:3","4:5","5:4","8:1","9:16","16:9","21:9"
resolution = "1K" # "512", "1K", "2K", "4K"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        response_format={"image": {aspect_ratio: aspect_ratio,                 image_size: resolution}},
    )
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif image:= part.as_image():
        image.save("butterfly.png")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const prompt =
      'Da Vinci style anatomical sketch of a dissected Monarch butterfly. Detailed drawings of the head, wings, and legs on textured parchment with notes in English.';
  const aspectRatio = '1:1';
  const resolution = '1K';

  const response = await ai.models.generateContent({
    model: 'gemini-3.1-flash-image',
    contents: prompt,
    config: {
      responseModalities: ['TEXT', 'IMAGE'],
      responseFormat: {
    image: {
        aspectRatio: aspectRatio,
        imageSize: resolution,
      }
  },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("image.png", buffer);
      console.log("Image saved as image.png");
    }
  }

}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    model := client.GenerativeModel("gemini-3.1-flash-image")
    model.GenerationConfig = &pb.GenerationConfig{
        ResponseModalities: []pb.ResponseModality{genai.Text, genai.Image},
        ImageConfig: &pb.ImageConfig{
            AspectRatio: "1:1",
            ImageSize:   "1K",
        },
    }

    prompt := "Da Vinci style anatomical sketch of a dissected Monarch butterfly. Detailed drawings of the head, wings, and legs on textured parchment with notes in English."
    resp, err := model.GenerateContent(ctx, genai.Text(prompt))
    if err != nil {
        log.Fatal(err)
    }

    for _, part := range resp.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Printf("%s", string(txt))
        } else if img, ok := part.(genai.ImageData); ok {
            err := os.WriteFile("butterfly.png", img.Data, 0644)
            if err != nil {
                log.Fatal(err)
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.GoogleSearch;
import com.google.genai.types.ImageConfig;
import com.google.genai.types.Part;
import com.google.genai.types.Tool;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class HiRes {
    public static void main(String[] args) throws IOException {

      try (Client client = new Client()) {
        GenerateContentConfig config = GenerateContentConfig.builder()
            .responseModalities("TEXT", "IMAGE")
            .imageConfig(ImageConfig.builder()
                .aspectRatio("16:9")
                .imageSize("4K")
                .build())
            .build();

        GenerateContentResponse response = client.models.generateContent(
            "gemini-3.1-flash-image", """
              Da Vinci style anatomical sketch of a dissected Monarch butterfly.
              Detailed drawings of the head, wings, and legs on textured
              parchment with notes in English.
              """,
            config);

        for (Part part : response.parts()) {
          if (part.text().isPresent()) {
            System.out.println(part.text().get());
          } else if (part.inlineData().isPresent()) {
            var blob = part.inlineData().get();
            if (blob.data().isPresent()) {
              Files.write(Paths.get("butterfly.png"), blob.data().get());
            }
          }
        }
      }
    }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class HiRes {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "Da Vinci style anatomical sketch of a dissected Monarch butterfly. Detailed drawings of the head, wings, and legs on textured parchment with notes in English." }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "TEXT", "IMAGE" },
            ImageConfig = new ImageConfig
            {
                AspectRatio = "1:1",
                ImageSize = "1K"
            }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("butterfly.png", imageBytes);
                Console.WriteLine("Image saved as butterfly.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "Da Vinci style anatomical sketch of a dissected Monarch butterfly. Detailed drawings of the head, wings, and legs on textured parchment with notes in English."}]}],
    "tools": [{"google_search": {}}],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"],
      "responseFormat": {
    "image": {"aspectRatio": "1:1", "imageSize": "1K"}
  }
    }
  }'
```

Aşağıda, bu istemden oluşturulan örnek bir resim verilmiştir:

![Yapay zeka tarafından üretilmiş, Da Vinci tarzında, parçalanmış bir kral kelebeğinin anatomik çizimi.](https://ai.google.dev/static/gemini-api/docs/images/gemini3-4k-image.png?hl=tr)

Kral kelebeğinin diseksiyonu yapılmış halinin, Da Vinci tarzında yapay zekayla üretilmiş anatomik çizimi.

### Düşünme süreci

Gemini 3 görüntü modelleri, karmaşık istemler için akıl yürütme süreci ("Düşünme") kullanan düşünen modellerdir. Bu özellik varsayılan olarak etkindir ve API'de devre dışı bırakılamaz. Düşünme süreci hakkında daha fazla bilgi edinmek için [Gemini Düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) rehberine bakın.

Model, kompozisyonu ve mantığı test etmek için en fazla iki ara görüntü oluşturur. Düşünme aşamasındaki son resim, oluşturulan son resimdir.

Son görüntünün üretilmesine yol açan düşünceleri kontrol edebilirsiniz.

### Python

```
for part in response.parts:
    if part.thought:
        if part.text:
            print(part.text)
        elif image:= part.as_image():
            image.show()
```

### JavaScript

```
for (const part of response.candidates[0].content.parts) {
  if (part.thought) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, 'base64');
      fs.writeFileSync('image.png', buffer);
      console.log('Image saved as image.png');
    }
  }
}
```

### Java

```
for (Part part : response.parts()) {
  if (part.thought().orElse(false)) {
    if (part.text().isPresent()) {
      System.out.println(part.text().get());
    } else if (part.inlineData().isPresent()) {
      var blob = part.inlineData().get();
      if (blob.data().isPresent()) {
        Files.write(Paths.get("image.png"), blob.data().get());
        System.out.println("Image saved as image.png");
      }
    }
  }
}
```

### C#

```
foreach (var candidate in response.Candidates) {
    foreach (var part in candidate.Content.Parts) {
        if (part.Thought) {
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("image.png", imageBytes);
                Console.WriteLine("Image saved as image.png");
            }
        }
    }
}
```

#### Düşünme düzeylerini kontrol etme

Gemini 3.1 Flash Image ve Gemini 3.1 Flash Lite Image ile modelin kalite ve gecikme süresini dengelemek için kullandığı düşünme miktarını kontrol edebilirsiniz. Varsayılan `thinkingLevel` değeri `minimal`'dir ve desteklenen düzeyler `minimal` ile `high`'dir. `thinkingLevel` değerini `minimal` olarak ayarladığınızda en düşük gecikmeli yanıtlar elde edilir. Minimal düşünme, modelin hiç düşünmediği anlamına gelmez.

Modelin oluşturduğu düşüncelerin yanıtta döndürülüp döndürülmeyeceğini veya gizli kalıp kalmayacağını belirlemek için `includeThoughts` Boole değerini ekleyebilirsiniz.

### Python

```
from google import genai

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents="A futuristic city built inside a giant glass bottle floating in space",
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        thinking_config=types.ThinkingConfig(
            thinking_level="High",
            include_thoughts=True
        ),
    )
)

for part in response.parts:
    if part.thought: # Skip outputting thoughts
      continue
    if part.text:
      display(Markdown(part.text))
    elif image:= part.as_image():
      image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: "A futuristic city built inside a giant glass bottle floating in space",
    config: {
      responseModalities: ["IMAGE"],
      thinkingConfig: {
        thinkingLevel: "High",
        includeThoughts: true
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.thought) { // Skip outputting thoughts
      continue;
    }
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("image.png", buffer);
      console.log("Image saved as image.png");
    }
  }
}
main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    pb "google.golang.org/genai/schema"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    model := client.GenerativeModel("gemini-3.1-flash-image")
    model.GenerationConfig = &pb.GenerationConfig{
        ResponseModalities: []pb.ResponseModality{genai.Image},
        ThinkingConfig: &pb.ThinkingConfig{
            ThinkingLevel:   "High",
            IncludeThoughts: true,
        },
    }

    prompt := "A futuristic city built inside a giant glass bottle floating in space"
    resp, err := model.GenerateContent(ctx, genai.Text(prompt))
    if err != nil {
        log.Fatal(err)
    }

    for _, part := range resp.Candidates[0].Content.Parts {
        if part.Thought { // Skip outputting thoughts
            continue
        }
        if txt, ok := part.(genai.Text); ok {
            fmt.Printf("%s", string(txt))
        } else if img, ok := part.(genai.ImageData); ok {
            err := os.WriteFile("image.png", img.Data, 0644)
            if err != nil {
                log.Fatal(err)
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;
import com.google.genai.types.ThinkingConfig;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class ThinkingLevels {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentConfig config = GenerateContentConfig.builder()
          .responseModalities("IMAGE")
          .thinkingConfig(ThinkingConfig.builder()
              .thinkingLevel("High")
              .includeThoughts(true)
              .build())
          .build();

      GenerateContentResponse response = client.models.generateContent(
          "gemini-3.1-flash-image",
          "A futuristic city built inside a giant glass bottle floating in space",
          config);

      for (Part part : response.parts()) {
        if (part.thought().orElse(false)) {
          // Skip outputting thoughts
          continue;
        }
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("image.png"), blob.data().get());
            System.out.println("Image saved as image.png");
          }
        }
      }
    }
  }
}
```

### C#

```
using Google.GenAI;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

public class ThinkingLevels {
  public static async Task Main(string[] args) {
    var client = new Client();

    var response = await client.Models.GenerateContentAsync(
        model: "gemini-3.1-flash-image",
        contents: new List<Part>
        {
            new Part { Text = "A futuristic city built inside a giant glass bottle floating in space" }
        },
        config: new GenerateContentConfig
        {
            ResponseModalities = new List<string> { "IMAGE" },
            ThinkingConfig = new ThinkingConfig
            {
                ThinkingLevel = "High",
                IncludeThoughts = true
            }
        }
    );

    foreach (var candidate in response.Candidates) {
        foreach (var part in candidate.Content.Parts) {
            if (part.Thought) {
                // Skip outputting thoughts
                continue;
            }
            if (part.Text != null) {
                Console.WriteLine(part.Text);
            } else if (part.InlineData != null) {
                var imageBytes = Convert.FromBase64String(part.InlineData.Data);
                await File.WriteAllBytesAsync("image.png", imageBytes);
                Console.WriteLine("Image saved as image.png");
            }
        }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "A futuristic city built inside a giant glass bottle floating in space"}]}],
    "generationConfig": {
      "responseModalities": ["IMAGE"],
      "thinkingConfig": {
        "thinkingLevel": "High",
        "includeThoughts": true
      }
    }
  }'
```

`includeThoughts`, `true` veya `false` olarak ayarlanmış olsun ya da olmasın, düşünme jetonlarının faturalandırıldığını unutmayın. Çünkü [düşünme süreci](#thinking-process), süreci görüntüleyip görüntülemediğinizden bağımsız olarak her zaman varsayılan olarak gerçekleşir.

#### Düşünce imzaları

Düşünce imzaları, modelin dahili düşünce sürecinin şifrelenmiş temsilleridir ve çok aşamalı etkileşimlerde akıl yürütme bağlamını korumak için kullanılır. Tüm yanıtlarda `thought_signature` alanı bulunur. Genel bir kural olarak, bir model yanıtında düşünce imzası alırsanız bir sonraki turda görüşme geçmişini gönderirken bunu aynen aldığınız şekilde geri iletmeniz gerekir. Düşünce imzalarının dolaştırılamaması yanıtın başarısız olmasına neden olabilir. İmzalarla ilgili daha fazla açıklama için [düşünce imzası](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=tr)
dokümanını inceleyin.

Düşünce imzaları şu şekilde çalışır:

- Yanıtta yer alan, resim `mimetype` içeren tüm `inline_data` bölümlerinde imza bulunmalıdır.
- Düşüncelerin hemen ardından (herhangi bir resimden önce) metin bölümleri varsa ilk metin bölümünde de imza bulunmalıdır.
- `inline_data` Resim içeren `mimetype` bölümler düşüncelerin bir parçasıysa imza içermez.

Aşağıdaki kodda, düşünce imzalarının nerede yer aldığına dair bir örnek gösterilmektedir:

```
[
  {
    "inline_data": {
      "data": "<base64_image_data_0>",
      "mime_type": "image/png"
    },
    "thought": true // Thoughts don't have signatures
  },
  {
    "inline_data": {
      "data": "<base64_image_data_1>",
      "mime_type": "image/png"
    },
    "thought": true // Thoughts don't have signatures
  },
  {
    "inline_data": {
      "data": "<base64_image_data_2>",
      "mime_type": "image/png"
    },
    "thought": true // Thoughts don't have signatures
  },
  {
    "text": "Here is a step-by-step guide to baking macarons, presented in three separate images.\n\n### Step 1: Piping the Batter\n\nThe first step after making your macaron batter is to pipe it onto a baking sheet. This requires a steady hand to create uniform circles.\n\n",
    "thought_signature": "<Signature_A>" // The first non-thought part always has a signature
  },
  {
    "inline_data": {
      "data": "<base64_image_data_3>",
      "mime_type": "image/png"
    },
    "thought_signature": "<Signature_B>" // All image parts have a signatures
  },
  {
    "text": "\n\n### Step 2: Baking and Developing Feet\n\nOnce piped, the macarons are baked in the oven. A key sign of a successful bake is the development of \"feet\"—the ruffled edge at the base of each macaron shell.\n\n"
    // Follow-up text parts don't have signatures
  },
  {
    "inline_data": {
      "data": "<base64_image_data_4>",
      "mime_type": "image/png"
    },
    "thought_signature": "<Signature_C>" // All image parts have a signatures
  },
  {
    "text": "\n\n### Step 3: Assembling the Macaron\n\nThe final step is to pair the cooled macaron shells by size and sandwich them together with your desired filling, creating the classic macaron dessert.\n\n"
  },
  {
    "inline_data": {
      "data": "<base64_image_data_5>",
      "mime_type": "image/png"
    },
    "thought_signature": "<Signature_D>" // All image parts have a signatures
  }
]
```

## Diğer görüntü üretme modları

Gemini, istem yapısına ve bağlama dayalı olarak diğer görüntü etkileşimi modlarını da destekler. Örneğin:

- **Metinden resimlere ve metne (araya eklenmiş):** İlgili metinlerle birlikte resimler oluşturur.
  - Örnek istem: "Paella için resimli bir tarif oluştur."
- **Resimler ve metinden resimlere ve metne (dönüşümlü)**: İlgili yeni resimler ve metinler oluşturmak için giriş resimlerini ve metinlerini kullanır.
  - Örnek istem: (Mobilyalı bir odanın resmiyle) "Mekanıma hangi renklerde kanepeler yakışır? Resmi güncelleyebilir misin?"

## Toplu olarak resim oluşturma

Çok sayıda resim oluşturmanız gerekiyorsa [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr)'yi kullanabilirsiniz. 24 saate kadar yanıt süresi karşılığında daha yüksek [hız sınırları](https://ai.google.dev/gemini-api/docs/rate-limits?hl=tr) elde edersiniz.

Toplu API görüntü örnekleri ve kodu için [Toplu API görüntü üretme belgelerini](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr#image-generation) ve [çözüm kitabını](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb?hl=tr) inceleyin.

## İstem yazma kılavuzu ve stratejileri

Görüntü oluşturmada ustalaşmak için temel bir ilkeyi anlamanız gerekir:

> **Anahtar kelimeleri listelemekle yetinmeyin, sahneyi açıklayın.**
> Modelin temel gücü, dili derinlemesine anlamasıdır. Bir anlatı, açıklayıcı bir paragraf neredeyse her zaman bağlantısız kelimelerden oluşan bir listeden daha iyi ve tutarlı bir resim oluşturur.

### Görüntü üretme istemleri

Aşağıdaki stratejiler, tam olarak aradığınız resimleri oluşturmak için etkili istemler oluşturmanıza yardımcı olacaktır.

#### Fotoğrafçılık

Gerçekçi görüntüler için fotoğrafçılık terimlerini kullanın. Modeli gerçekçi bir sonuca yönlendirmek için kamera açılarını, lens türlerini, ışıklandırmayı ve ince ayrıntıları belirtin.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| Güneşten etkilenmiş derin kırışıklıkları ve sıcak, bilgili bir gülümsemesi olan yaşlı bir Japon seramik sanatçısının yakın çekim portre fotoğrafı. Yeni sırlanmış bir çay kasesini dikkatlice inceliyor. Arka planda, güneş ışığıyla dolu rustik atölyesi var. Sahne, pencereden süzülen yumuşak, altın saat ışığıyla aydınlatılıyor ve kilden yapılmış ürünün ince dokusu vurgulanıyor. 85 mm portre lensiyle çekilmiş, yumuşak ve bulanık bir arka plan (bokeh) oluşturulmuş. Genel atmosfer sakin ve ustaca olmalı. Dikey portre yönü. | Yaşlı Japon seramik sanatçısı |

#### Stilize edilmiş resimler ve çıkartmalar

Çıkartma, simge veya öğe oluşturmak için stil hakkında net olun ve beyaz arka plan isteyin.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| Küçük bir bambu şapka takan mutlu bir kırmızı pandanın kawaii tarzı çıkartması. Yeşil bir bambu yaprağını yiyor. Tasarımda belirgin ve temiz ana hatlar, basit selüloit gölgeleme ve canlı bir renk paleti kullanılıyor. Arka plan beyaz olmalıdır. | Kawaii kızıl panda çıkartması |

#### Resimlerdeki metinlerin doğruluğu

Gemini, metin oluşturma konusunda üstündür. Metin, yazı tipi stili (açıklayıcı bir şekilde) ve genel tasarım hakkında net olun. Profesyonel öğe üretimi için Gemini 3 Pro Image'i kullanın.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| "The Daily Grind" adlı bir kafe için modern ve minimalist bir logo oluştur. Metin, sade, kalın ve sans-serif yazı tipinde olmalıdır. Renk şeması siyah beyazdır. Logoyu daire içine alın. Kahve çekirdeklerini akıllıca kullanın. | Kafe logosu |

#### Ürün maketleri ve ticari fotoğrafçılık

E-ticaret, reklam veya markalama için net ve profesyonel ürün fotoğrafları oluşturmak üzere idealdir.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| Parlak beton yüzey üzerinde sunulan, mat siyah renkte minimalist seramik kahve kupasının yüksek çözünürlüklü, stüdyo ışıklı ürün fotoğrafı. Işıklandırma, yumuşak ve dağınık parlak alanlar oluşturmak ve sert gölgeleri ortadan kaldırmak için tasarlanmış üç noktalı bir softbox kurulumudur. Temiz çizgilerini göstermek için kamera açısı biraz yükseltilmiş 45 derecelik bir çekimdir. Kahveden yükselen buhara keskin bir şekilde odaklanılmış, ultra gerçekçi bir görüntü. Kare resim. | Seramik kahve kupası ürün fotoğrafı |

#### Minimalist ve öğeler arasındaki boşluk tasarımı

Metnin yerleştirileceği web siteleri, sunumlar veya pazarlama materyalleri için arka plan oluşturmak üzere mükemmeldir.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| Kadrajın sağ alt kısmında yer alan tek bir narin kırmızı akçaağaç yaprağının yer aldığı minimalist bir kompozisyon. Arka plan, metin için önemli bir boş alan oluşturan geniş ve boş bir kirli beyaz tuvaldir. Sol üstten gelen yumuşak ve eşit dağılmış ışıklandırma. Kare resim. | Kırmızı akçaağaç yaprağı içeren minimalist tasarım |

#### Sıralı sanat (çizgi roman paneli / resimli taslak)

Görsel hikaye anlatımı için paneller oluşturmak üzere karakter tutarlılığı ve sahne açıklaması üzerine kuruludur. Metin doğruluğu ve hikaye anlatma becerisi için bu istemler en iyi sonucu Gemini 3.1 Pro ve Gemini 3.1 Flash Image ile verir.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| **Giriş resmi:**  Beyaz gözlüklü adam   Giriş resmi   **İstem:** Yüksek kontrastlı siyah beyaz mürekkeplerle, sert ve karanlık bir sanat tarzında 3 panelli bir çizgi roman oluştur. Karakteri komik bir sahneye yerleştir. | Sert ve gerçekçi kara film tarzında çizgi roman paneli |

#### Google Arama ile Temellendirme

Google Arama'yı kullanarak güncel veya gerçek zamanlı bilgilere dayalı görseller oluşturun.
Bu özellik; haberler, hava durumu ve zamana duyarlı diğer konular için kullanışlıdır.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| Dün geceki Şampiyonlar Ligi Arsenal maçının basit ama şık bir grafiğini oluştur. | Arsenal futbol maçının skor grafiği |

### Resimleri düzenleme istemleri

Bu örneklerde, düzenleme, kompozisyon ve stil aktarımı için metin istemlerinizle birlikte nasıl resim sağlayacağınız gösterilmektedir.

#### Öğe ekleme ve kaldırma

Bir resim sağlayın ve değişikliğinizi açıklayın. Model, orijinal resmin stili, ışıklandırması ve perspektifiyle eşleşir.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| **Giriş resmi:**  Kabarık tüylü, kızıl bir kedinin fotogerçekçi resmi...   Giriş resmi   **İstem:** Kedimin sağlanan resmini kullanarak lütfen başına küçük, örülmüş bir büyücü şapkası ekleyin. Koltukta rahatça oturuyormuş gibi görünmesini ve fotoğraftaki yumuşak ışıkla uyumlu olmasını sağlayın. | Sihirbaz şapkalı kedi |

#### İç boyama (semantik maskeleme)

Resmin geri kalanına dokunmadan belirli bir bölümünü düzenlemek için "maske"yi sohbet ederek tanımlayın.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| **Giriş resmi:**  Modern ve iyi aydınlatılmış bir oturma odasının geniş çekimi...   Giriş resmi   **İstem:** Sağlanan oturma odası resmini kullanarak yalnızca mavi kanepenin yerine eski tarz, kahverengi deri bir Chesterfield kanepe koy. Odanın geri kalanını (ör. koltuktaki yastıklar ve aydınlatma) değiştirmeyin. | Kahverengi deri kanepeli oturma odası |

#### Stil aktarımı

Bir resim sağlayın ve modelden içeriğini farklı bir sanatsal tarzda yeniden oluşturmasını isteyin.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| **Giriş resmi:**  Kalabalık bir şehir caddesinin fotogerçekçi ve yüksek çözünürlüklü fotoğrafı...   Giriş resmi   **İstem:** Gece çekilmiş modern bir şehir caddesinin fotoğrafını, Vincent van Gogh'un "Yıldızlı Gece" adlı eserinin sanatsal tarzına dönüştür. Binaların ve arabaların orijinal kompozisyonunu koruyun ancak tüm öğeleri, girdaplı, impasto fırça darbeleri ve koyu maviler ile parlak sarılardan oluşan dramatik bir paletle oluşturun. | Yıldızlı Gece tarzında şehir caddesi |

#### Gelişmiş kompozisyon: Birden fazla görüntüyü birleştirme

Yeni bir kompozit sahne oluşturmak için bağlam olarak birden fazla resim sağlayın. Bu özellik, ürün maketleri veya yaratıcı kolajlar için idealdir.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| **Giriş resimleri:**  Mavi çiçekli bir yazlık elbisenin profesyonelce çekilmiş fotoğrafı...   Giriş 1: Elbise   Saçları topuz yapılmış bir kadının tam boy fotoğrafı...   Giriş 2: Model   **İstem:** Profesyonel bir e-ticaret moda fotoğrafı oluştur. İlk resimdeki mavi çiçekli elbiseyi alıp ikinci resimdeki kadına giydir. Elbiseyi giyen kadının, dış ortamla uyumlu olacak şekilde ışık ve gölgeler ayarlanmış, gerçekçi ve tam vücut fotoğrafını oluştur. | Moda e-ticaret çekimi |

#### Yüksek doğruluk oranıyla ayrıntı koruma

Düzenleme sırasında önemli ayrıntıların (ör. yüz veya logo) korunmasını sağlamak için düzenleme isteğinizle birlikte bu ayrıntıları ayrıntılı bir şekilde açıklayın.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| **Giriş resimleri:**  Kahverengi saçlı ve mavi gözlü bir kadının profesyonel portre fotoğrafı...   Giriş 1: Kadın   &quot;G&quot; ve &quot;A&quot; harflerinin yer aldığı sade ve modern bir logo...   Giriş 2: Logo   **İstem:** Kahverengi saçlı, mavi gözlü ve ifadesiz kadının ilk resmini al. İkinci resimdeki logoyu kadının siyah tişörtüne ekle. Kadının yüzünün ve özelliklerinin tamamen değişmeden kalmasını sağla. Logo, gömleğin kıvrımlarını takip ederek kumaşa doğal bir şekilde basılmış gibi görünmelidir. | Tişörtünde logo olan kadın |

#### Bir şeyi hayata geçirmek

Kaba bir taslak veya çizim yükleyip modelden bunu tamamlanmış bir resme dönüştürmesini isteyin.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| **Giriş resmi:**  Araba eskizi   Arabanın kaba taslağı   **İstem:** Fütüristik bir arabanın bu taslak halindeki kurşun kalem çizimini, galerideki bitmiş konsept arabanın cilalı bir fotoğrafına dönüştür. Eskizdeki şık çizgileri ve alçak profili koruyun ancak metalik mavi boya ve neon jant ışığı ekleyin. | Konsept arabanın rötuşlanmış fotoğrafı |

#### Karakter tutarlılığı: 360 görünüm

Farklı açılar için yinelemeli istemler girerek bir karakterin 360 derece görünümlerini oluşturabilirsiniz. En iyi sonuçlar için tutarlılığı korumak amacıyla daha önce oluşturulan resimleri sonraki istemlere ekleyin. Karmaşık pozlar için istenen pozun referans görselini ekleyin.

| **İstem** | **Oluşturulan çıkış** |
| --- | --- |
| **Giriş resmi:**  Beyaz gözlüklü bir adamın orijinal girişi   Orijinal resim   **İstem:** Bu adamın beyaz arka plan üzerinde, sağa doğru bakan profil fotoğrafı | Sağa bakan beyaz gözlüklü bir adamın çıktısı   Beyaz gözlüklü adam sağa bakıyor   Beyaz gözlüklü bir adamın ileriye doğru baktığı görsel   Beyaz gözlüklü adam öne bakıyor |

### En iyi uygulamalar

Sonuçlarınızı iyi seviyeden mükemmel seviyeye taşımak için bu profesyonel stratejileri iş akışınıza dahil edin.

- **Çok ayrıntılı olun:** Ne kadar çok ayrıntı verirseniz o kadar fazla kontrol sahibi olursunuz. "Fantezi zırh" yerine "gümüş yaprak desenleriyle işlenmiş, yüksek yakalı ve şahin kanatları şeklinde omuzlukları olan, süslü elf zırhı" gibi bir açıklama yapın.
- **Bağlam ve amaç sağlama:** Resmin *amacını* açıklayın. Modelin bağlamı anlaması, nihai çıktıyı etkiler. Örneğin, "Üst düzey, minimalist bir cilt bakımı markası için logo oluştur" istemi, yalnızca "Logo oluştur" istemine kıyasla daha iyi sonuçlar verir.
- **Tekrar edin ve iyileştirin:** İlk denemede mükemmel bir resim elde etmeyi beklemeyin. Küçük değişiklikler yapmak için modelin etkileşimli yapısından yararlanın. "Bu harika, ancak ışığı biraz daha sıcak yapabilir misin?" veya "Her şeyi aynı tut ama karakterin ifadesini daha ciddi olacak şekilde değiştir" gibi istemlerle devam edin.
- **Adım adım talimatlar kullanın:** Çok sayıda öğe içeren karmaşık sahneler için isteminizi adımlara ayırın. "Öncelikle şafakta sakin ve sisli bir orman arka planı oluştur. Ardından, ön plana yosun kaplı eski bir taş sunak ekleyin.
  Son olarak, sunakın üzerine tek bir parlayan kılıç yerleştirin."
- **"Anlamsal olumsuz istemler" kullanın:** "Araba yok" demek yerine istediğiniz sahneyi olumlu bir şekilde tanımlayın: "Trafik işareti olmayan boş ve ıssız bir sokak."
- **Kamerayı kontrol etme:** Kompozisyonu kontrol etmek için fotoğraf ve sinema dilini kullanın. `wide-angle shot`, `macro shot`, `low-angle
  perspective` gibi terimler.

## Sınırlamalar

- En iyi performans için şu dilleri kullanın: EN, ar-EG, de-DE, es-MX,
  fr-FR, hi-IN, id-ID, it-IT, ja-JP, ko-KR, pt-BR, ru-RU, ua-UA, vi-VN, zh-CN.
- Görüntü üretme, ses girişlerini desteklemez. Video girişleri yalnızca Gemini 3.1 Flash Image ve Gemini 3.1 Flash Lite Image için desteklenir.
- Model, kullanıcının açıkça istediği resim çıkışlarının sayısını her zaman tam olarak karşılamaz.
- `gemini-2.5-flash-image`, giriş olarak en fazla 3 resimle en iyi şekilde çalışır. `gemini-3-pro-image` ise yüksek doğrulukta 5 resmi ve toplamda 14 resmi destekler. `gemini-3.1-flash-image`, tek bir iş akışında en fazla 4 karakter benzerliğini ve 10 nesnenin doğruluğunu destekler.
- Gemini, bir görüntü için metin oluştururken önce metni oluşturup ardından metni içeren bir görüntü istemeniz durumunda en iyi sonucu verir.
- `gemini-3.1-flash-image` Google Arama ile Temellendirme, şu anda web aramasından elde edilen gerçek hayattaki insan fotoğraflarının kullanılmasını desteklemiyor.
- Üretilen tüm görüntülerde [SynthID filigranı](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=tr) bulunur.

## İsteğe bağlı yapılandırmalar

İsteğe bağlı olarak, `generate_content` çağrılarının `config` alanında modelin çıkışının yanıt biçimlerini ve en-boy oranını yapılandırabilirsiniz.

### Çıkış türleri

Model, varsayılan olarak metin ve resim yanıtları (ör. `response_modalities=['Text', 'Image']`) döndürür.
`response_modalities=['Image']` kullanarak yanıtı yalnızca metin içermeyen resimler döndürecek şekilde yapılandırabilirsiniz.

### Python

```
response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[prompt],
    config=types.GenerateContentConfig(
        response_modalities=['Image']
    )
)
```

### JavaScript

```
const response = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: prompt,
    config: {
        responseModalities: ['Image']
    }
  });
```

### Go

```
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.1-flash-image",
    genai.Text("Create a picture of a nano banana dish in a " +
                " fancy restaurant with a Gemini theme"),
    &genai.GenerateContentConfig{
        ResponseModalities: "Image",
    },
  )
```

### Java

```
response = client.models.generateContent(
    "gemini-3.1-flash-image",
    prompt,
    GenerateContentConfig.builder()
        .responseModalities("IMAGE")
        .build());
```

### C#

```
var response = await client.Models.GenerateContentAsync(
    model: "gemini-3.1-flash-image",
    contents: new List<Part> { new Part { Text = prompt } },
    config: new GenerateContentConfig
    {
        ResponseModalities = new List<string> { "IMAGE" }
    }
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"}
      ]
    }],
    "generationConfig": {
      "responseModalities": ["Image"]
    }
  }'
```

### En boy oranları ve resim boyutu

Model, varsayılan olarak çıkış resminin boyutunu giriş resminizin boyutuyla eşleştirir veya 1:1 kareler oluşturur.
Yanıt isteğindeki `aspect_ratio` alanını kullanarak çıkış resminin en boy oranını kontrol edebilirsiniz. Bu alan, yanıt isteğinde `response_format` altında gösterilir:

### Python

```
# For gemini-2.5-flash-image
response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
    config=types.GenerateContentConfig(
        response_format={"image": {aspect_ratio: "16:9",}}
    )
)

# For gemini-3.1-flash-image and gemini-3-pro-image
response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[prompt],
    config=types.GenerateContentConfig(
        response_format={"image": {aspect_ratio: "16:9",                 image_size: "2K",}}
    )
)
```

### JavaScript

```
// For gemini-2.5-flash-image
const response = await ai.models.generateContent({
    model: "gemini-2.5-flash-image",
    contents: prompt,
    config: {
      responseFormat: {
    image: {
        aspectRatio: "16:9",
      }
  },
    }
  });

// For gemini-3.1-flash-image and gemini-3-pro-image
const response_gemini3 = await ai.models.generateContent({
    model: "gemini-3.1-flash-image",
    contents: prompt,
    config: {
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "2K",
      }
  },
    }
  });
```

### Go

```
// For gemini-2.5-flash-image
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-2.5-flash-image",
    genai.Text("Create a picture of a nano banana dish in a " +
                " fancy restaurant with a Gemini theme"),
    &genai.GenerateContentConfig{
        ImageConfig: &genai.ImageConfig{
          AspectRatio: "16:9",
        },
    }
  )

// For gemini-3.1-flash-image and gemini-3-pro-image
result_gemini3, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.1-flash-image",
    genai.Text("Create a picture of a nano banana dish in a " +
                " fancy restaurant with a Gemini theme"),
    &genai.GenerateContentConfig{
        ImageConfig: &genai.ImageConfig{
          AspectRatio: "16:9",
          ImageSize: "2K",
        },
    }
  )
```

### Java

```
// For gemini-2.5-flash-image
response = client.models.generateContent(
    "gemini-2.5-flash-image",
    prompt,
    GenerateContentConfig.builder()
        .imageConfig(ImageConfig.builder()
            .aspectRatio("16:9")
            .build())
        .build());

// For gemini-3.1-flash-image and gemini-3-pro-image
response_gemini3 = client.models.generateContent(
    "gemini-3.1-flash-image",
    prompt,
    GenerateContentConfig.builder()
        .imageConfig(ImageConfig.builder()
            .aspectRatio("16:9")
            .imageSize("2K")
            .build())
        .build());
```

### C#

```
// For gemini-2.5-flash-image
var response = await client.Models.GenerateContentAsync(
    model: "gemini-2.5-flash-image",
    contents: new List<Part> { new Part { Text = prompt } },
    config: new GenerateContentConfig
    {
        ImageConfig = new ImageConfig
        {
            AspectRatio = "16:9"
        }
    }
);

// For gemini-3.1-flash-image and gemini-3-pro-image
var response_gemini3 = await client.Models.GenerateContentAsync(
    model: "gemini-3.1-flash-image",
    contents: new List<Part> { new Part { Text = prompt } },
    config: new GenerateContentConfig
    {
        ImageConfig = new ImageConfig
        {
            AspectRatio = "16:9",
            ImageSize = "2K"
        }
    }
);
```

### REST

```
# For gemini-2.5-flash-image
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"}
      ]
    }],
    "generationConfig": {
      "responseFormat": {
    "image": {
        "aspectRatio": "16:9"
      }
  }
    }
  }'

# For gemini-3-pro-image
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"}
      ]
    }],
    "generationConfig": {
      "responseFormat": {
    "image": {
        "aspectRatio": "16:9",
        "imageSize": "2K"
      }
  }
    }
  }'
```

Kullanılabilen farklı oranlar ve oluşturulan resmin boyutu aşağıdaki tablolarda listelenmiştir:

### 3.1 Flash Image

| En boy oranı | 512 çözünürlük | 500 jeton | 1K çözünürlük | 1.000 jeton | 2K çözünürlük | 2 bin parça | 4K çözünürlük | 4 bin parça |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **1:1** | 512x512 | 747 | 1024x1024 | 1120 | 2048x2048 | 1680 | 4096x4096 | 2520 |
| **1:4** | 256x1024 | 747 | 512x2048 | 1120 | 1024x4096 | 1680 | 2048x8192 | 2520 |
| **1:8** | 192x1536 | 747 | 384x3072 | 1120 | 768x6144 | 1680 | 1536x12288 | 2520 |
| **2:3** | 424x632 | 747 | 848x1264 | 1120 | 1696x2528 | 1680 | 3392x5056 | 2520 |
| **3:2** | 632x424 | 747 | 1264x848 | 1120 | 2528x1696 | 1680 | 5056x3392 | 2520 |
| **3:4** | 448x600 | 747 | 896x1200 | 1120 | 1792x2400 | 1680 | 3584x4800 | 2520 |
| **4:1** | 1024x256 | 747 | 2048x512 | 1120 | 4096x1024 | 1680 | 8192x2048 | 2520 |
| **4:3** | 600x448 | 747 | 1200x896 | 1120 | 2400x1792 | 1680 | 4800x3584 | 2520 |
| **4:5** | 464x576 | 747 | 928x1152 | 1120 | 1856x2304 | 1680 | 3712x4608 | 2520 |
| **5:4** | 576x464 | 747 | 1152x928 | 1120 | 2304x1856 | 1680 | 4608x3712 | 2520 |
| **8:1** | 1536x192 | 747 | 3072x384 | 1120 | 6144x768 | 1680 | 12288x1536 | 2520 |
| **9:16** | 384x688 | 747 | 768x1376 | 1120 | 1536x2752 | 1680 | 3072x5504 | 2520 |
| **16:9** | 688x384 | 747 | 1376x768 | 1120 | 2752x1536 | 1680 | 5504x3072 | 2520 |
| **21:9** | 792x168 | 747 | 1584x672 | 1120 | 3168x1344 | 1680 | 6336x2688 | 2520 |

### 3.1 Flash Lite Image

| En boy oranı | 512 çözünürlük | 500 jeton | 1K çözünürlük | 1.000 jeton |
| --- | --- | --- | --- | --- |
| **1:1** | 512x512 | 747 | 1024x1024 | 1120 |
| **1:4** | 256x1024 | 747 | 512x2048 | 1120 |
| **1:8** | 192x1536 | 747 | 384x3072 | 1120 |
| **2:3** | 424x632 | 747 | 848x1264 | 1120 |
| **3:2** | 632x424 | 747 | 1264x848 | 1120 |
| **3:4** | 448x600 | 747 | 896x1200 | 1120 |
| **4:1** | 1024x256 | 747 | 2048x512 | 1120 |
| **4:3** | 600x448 | 747 | 1200x896 | 1120 |
| **4:5** | 464x576 | 747 | 928x1152 | 1120 |
| **5:4** | 576x464 | 747 | 1152x928 | 1120 |
| **8:1** | 1536x192 | 747 | 3072x384 | 1120 |
| **9:16** | 384x688 | 747 | 768x1376 | 1120 |
| **16:9** | 688x384 | 747 | 1376x768 | 1120 |
| **21:9** | 792x168 | 747 | 1584x672 | 1120 |

### 3.1 Pro Image

| En boy oranı | 1K çözünürlük | 1.000 jeton | 2K çözünürlük | 2 bin parça | 4K çözünürlük | 4 bin parça |
| --- | --- | --- | --- | --- | --- | --- |
| **1:1** | 1024x1024 | 1120 | 2048x2048 | 1120 | 4096x4096 | 2000 |
| **2:3** | 848x1264 | 1120 | 1696x2528 | 1120 | 3392x5056 | 2000 |
| **3:2** | 1264x848 | 1120 | 2528x1696 | 1120 | 5056x3392 | 2000 |
| **3:4** | 896x1200 | 1120 | 1792x2400 | 1120 | 3584x4800 | 2000 |
| **4:3** | 1200x896 | 1120 | 2400x1792 | 1120 | 4800x3584 | 2000 |
| **4:5** | 928x1152 | 1120 | 1856x2304 | 1120 | 3712x4608 | 2000 |
| **5:4** | 1152x928 | 1120 | 2304x1856 | 1120 | 4608x3712 | 2000 |
| **9:16** | 768x1376 | 1120 | 1536x2752 | 1120 | 3072x5504 | 2000 |
| **16:9** | 1376x768 | 1120 | 2752x1536 | 1120 | 5504x3072 | 2000 |
| **21:9** | 1584x672 | 1120 | 3168x1344 | 1120 | 6336x2688 | 2000 |

### Gemini 2.5 Flash Image

| En boy oranı | Çözünürlük | Token'lar |
| --- | --- | --- |
| 1:1 | 1024x1024 | 1290 |
| 2:3 | 832x1248 | 1290 |
| 3:2 | 1248x832 | 1290 |
| 3:4 | 864x1184 | 1290 |
| 4:3 | 1184x864 | 1290 |
| 4:5 | 896x1152 | 1290 |
| 5:4 | 1152x896 | 1290 |
| 9:16 | 768x1344 | 1290 |
| 16:9 | 1344x768 | 1290 |
| 21:9 | 1536x672 | 1290 |

## Model seçimi

Belirli kullanım alanınıza en uygun modeli seçin.

- **Gemini 3.1 Flash Image (Nano Banana 2)**, maliyet ve gecikme dengesi açısından en iyi genel performansı ve zekayı sunduğu için tercih etmeniz gereken görüntü üretme modelidir. Daha fazla bilgi için model [fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#gemini-3.1-flash-image) ve [özellikler](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=tr) sayfasına göz atın.
- **Gemini 3.1 Flash Lite Image (Nano Banana 2 Lite)**, görüntü üretme ailesinin verimlilik uzmanı olarak tasarlanmıştır. Ultra düşük gecikme süresi ve uygun maliyetli görüntü üretme ve düzenleme özellikleri sunar.
  Daha fazla bilgi için model [fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#gemini-3.1-flash-lite-image) ve [özellikler](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=tr) sayfasına göz atın.
- **Gemini 3 Pro Image (Nano Banana Pro)**, profesyonel öğe üretimi ve karmaşık talimatlar için tasarlanmıştır. Bu modelde, Google Arama kullanılarak gerçek dünyayla bağlantı kurulur, oluşturma işleminden önce kompozisyonu iyileştiren varsayılan bir "Düşünme" süreci uygulanır ve 4K çözünürlüğe kadar görüntüler oluşturulabilir. Daha fazla bilgi için model [fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#gemini-3-pro-image) ve [özellikler](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=tr) sayfasına göz atın.
- **Gemini 2.5 Flash Image (Nano Banana)**, hız ve verimlilik için tasarlanmıştır. Bu model, yüksek hacimli ve düşük gecikmeli görevler için optimize edilmiştir ve 1.024 piksel çözünürlükte görüntüler oluşturur. Daha fazla bilgi için model [fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#gemini-2.5-flash-image) ve [özellikler](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=tr) sayfasına göz atın.

### Imagen ne zaman kullanılır?

Gemini'ın yerleşik görüntü üretme özelliklerini kullanmanın yanı sıra Gemini API aracılığıyla özel görüntü üretme modelimiz [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=tr)'e de erişebilirsiniz. Kapatma tarihinden önce taşımayı planlayın.

## Sırada ne var?

- Daha fazla örnek ve kod örneğini [cookbook rehberinde](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_Started_Nano_Banana.ipynb?hl=tr) bulabilirsiniz.
- Gemini API ile nasıl video oluşturacağınızı öğrenmek için [Veo kılavuzuna](https://ai.google.dev/gemini-api/docs/video?hl=tr) göz atın.
- Gemini modelleri hakkında daha fazla bilgi edinmek için [Gemini modelleri](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr) başlıklı makaleyi inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-08 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-08 UTC."],[],[]]
