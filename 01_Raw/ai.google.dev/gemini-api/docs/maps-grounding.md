---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr
fetched_at: 2026-10-26T06:02:55.608895+00:00
title: "Google Haritalar ile temellendirme \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Google Haritalar ile temellendirme

Google Haritalar ile Temellendirme, Gemini'ın üretken özelliklerini Google Haritalar'ın zengin, gerçeklere dayalı ve güncel verileriyle birleştirir. Bu özellik, geliştiricilerin uygulamalarına konuma duyarlı işlevleri kolayca eklemelerine olanak tanır. Kullanıcı sorgusunun bağlamı Haritalar verileriyle ilgili olduğunda Gemini modeli, kullanıcının belirttiği konum veya genel alanla alakalı, doğru ve güncel yanıtlar sağlamak için Google Haritalar'dan yararlanır.

- **Doğru ve konuma duyarlı yanıtlar:** Coğrafi konuma özgü sorgular için Google Haritalar'ın kapsamlı ve güncel verilerinden yararlanın.
- **Gelişmiş kişiselleştirme:** Önerileri ve bilgileri, kullanıcı tarafından sağlanan konumlara göre özelleştirin.

## Başlayın

Bu örnekte, kullanıcı sorgularına doğru ve konuma duyarlı yanıtlar sağlamak için Google Haritalar ile Temellendirme'yi uygulamanıza nasıl entegre edeceğiniz gösterilmektedir. İstem, isteğe bağlı bir kullanıcı konumuyla yerel öneriler ister ve Gemini modelinin Google Haritalar verilerini kullanmasına olanak tanır.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "What are the best Italian restaurants within a 15-minute walk from here?"))
        .tools(
            Arrays.asList(
                GoogleMaps.builder().latitude(34.050481).longitude(-118.248526).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Print the model's text response and annotations
if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("What are the best Italian restaurants within a 15-minute walk from here?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(34.050481),
                        Longitude: genai.Ptr(-118.248526),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Print the model's text response and annotations
    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Google Haritalar ile Temellendirme'nin işleyiş şekli

Google Haritalar ile Temellendirme, Haritalar API'yi temellendirme kaynağı olarak kullanarak Gemini API'yi Google Coğrafi ekosistemiyle entegre eder. Kullanıcının sorgusu coğrafi bağlam içerdiğinde Gemini modeli, Google Haritalar ile Temellendirme aracını çağırabilir. Model, sağlanan konumla ilgili Google Haritalar verilerine dayalı yanıtlar üretebilir.

Süreç genellikle şunları içerir:

1. **Kullanıcı sorgusu:** Kullanıcı, uygulamanıza coğrafi bağlam içerebilecek bir sorgu gönderir (ör. "yakınımdaki kafeler", "San Francisco'daki müzeler").
2. **Araç çağırma:** Coğrafi amaçlı sorguyu tanıyan Gemini modeli, Google Haritalar ile Temellendirme aracını çağırır. Bu araç, isteğe bağlı olarak kullanıcının `latitude` ve `longitude` bilgileriyle birlikte kullanılabilir. Bu araç, metin tabanlı bir arama aracıdır ve Haritalar'da arama yapmaya benzer şekilde çalışır. Yerel sorgularda ("yakınımdaki") koordinatlar kullanılırken belirli veya yerel olmayan sorguların açık konumdan etkilenmesi olası değildir.
3. **Veri alma:** Google Haritalar ile Temellendirme hizmeti, Google Haritalar'da alakalı bilgiler (ör. yerler, yorumlar, fotoğraflar, adresler, çalışma saatleri) için sorgu gönderir.
4. **Temellendirilmiş üretim:** Alınan Haritalar verileri, Gemini modelinin yanıtını bilgilendirmek için kullanılır. Böylece gerçeklere dayalı doğruluk ve alaka düzeyi sağlanır.
5. **Yanıt ve ek açıklamalar:** Model, Google Haritalar kaynaklarına bağlantı veren satır içi ek açıklamalar içeren bir metin yanıtı döndürür. Bu sayede geliştiriciler alıntıları gösterebilir.

## Google Haritalar ile Temellendirme neden ve ne zaman kullanılır?

Google Haritalar ile temellendirme, doğru, güncel ve konuma özel bilgiler gerektiren uygulamalar için idealdir. Google Haritalar'ın dünya genelinde 250 milyondan fazla yeri içeren kapsamlı veritabanıyla desteklenen alakalı ve kişiselleştirilmiş içerikler sunarak kullanıcı deneyimini iyileştirir.

Uygulamanızın aşağıdaki durumlarda Google Haritalar ile Temellendirme'yi kullanması gerekir:

- Coğrafi konuma özgü sorulara eksiksiz ve doğru yanıtlar verin.
- Etkileşimli gezi planlayıcılar ve yerel rehberler oluşturun.
- Konuma ve kullanıcı tercihlerine (ör. restoranlar veya mağazalar) göre ilgi çekici yerler önerin.
- Sosyal, perakende veya yemek teslimatı hizmetleri için konum kullanım özellikli deneyimler oluşturun.

Google Haritalar ile temellendirme, "yakınımdaki en iyi kahve dükkanını" bulma veya yol tarifi alma gibi yakınlık ve güncel gerçek verilerin kritik olduğu kullanım alanlarında mükemmeldir.

## Kullanım alanları

Google Haritalar ile Temellendirme, konuma duyarlı çeşitli kullanım alanlarını destekler.

### Yere özel soruları yanıtlama

Belirli bir yer hakkında ayrıntılı sorular sorarak Google kullanıcı yorumlarına ve diğer Haritalar verilerine dayalı yanıtlar alabilirsiniz.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Is there a cafe near the corner of 1st and Main that has outdoor seating?"))
        .tools(
            Arrays.asList(
                GoogleMaps.builder().latitude(34.050481).longitude(-118.248526).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Is there a cafe near the corner of 1st and Main that has outdoor seating?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(34.050481),
                        Longitude: genai.Ptr(-118.248526),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### Konuma dayalı kişiselleştirme sağlama

Kullanıcının tercihlerine ve belirli bir coğrafi bölgeye göre uyarlanmış öneriler alın.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Which family-friendly restaurants near here have the best playground reviews?"))
        .tools(
            Arrays.asList(GoogleMaps.builder().latitude(30.2672).longitude(-97.7431).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Which family-friendly restaurants near here have the best playground reviews?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(30.2672),
                        Longitude: genai.Ptr(-97.7431),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### Seyahat planı oluşturma konusunda yardım

Yol tarifleri ve çeşitli konumlar hakkında bilgiler içeren çok günlük planlar oluşturun. Bu planlar, seyahat uygulamaları için idealdir.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

String prompt =
    "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .tools(
            Arrays.asList(GoogleMaps.builder().latitude(37.78193).longitude(-122.40476).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// ... code to process response
System.out.println(interaction.outputText().orElse(""));
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

    prompt := "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput(prompt),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(37.78193),
                        Longitude: genai.Ptr(-122.40476),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    // ... code to process response
    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## Hizmet kullanım şartları

Bu bölümde, Google Haritalar ile Temellendirme'nin hizmet kullanım koşulları açıklanmaktadır.

### Kullanıcıyı Google Haritalar kaynaklarının kullanımı hakkında bilgilendirme

Her Google Haritalar Grounded sonucunda, her yanıtı destekleyen `model_output` adımının içerik bloklarıyla ilgili kaynak ek açıklamaları alırsınız. Aşağıdaki meta veriler döndürülür:

- kaynak URL
- ad

Google Haritalar ile Temellendirme'den elde edilen sonuçları sunarken ilişkili Google Haritalar kaynaklarını belirtmeniz ve kullanıcılarınızı aşağıdakiler hakkında bilgilendirmeniz gerekir:

- Google Haritalar kaynakları, kaynakların desteklediği oluşturulmuş içeriği hemen takip etmelidir. Bu oluşturulan içerik, Google Haritalar'da Temellendirilmiş Sonuç olarak da adlandırılır.
- Google Haritalar kaynakları, tek bir kullanıcı etkileşimi içinde görüntülenebilmelidir.

### Google Haritalar bağlantılarıyla Google Haritalar kaynaklarını görüntüleme

Her kaynak açıklaması için aşağıdaki koşullara uygun bir bağlantı önizlemesi oluşturulmalıdır:

- Google Haritalar metin [atıf yönergelerine](#maps-attribution-guidelines) uyarak her kaynağı Google Haritalar'a atfedin.
- Yanıtta sağlanan kaynak adını gösterin.
- Ek açıklamada yer alan `url` simgesini kullanarak kaynağa bağlantı verin.

### Google Haritalar metin atıf yönergeleri

Metinlerde Google Haritalar'ı kaynak olarak belirtirken aşağıdaki kurallara uyun:

- Google Haritalar metnini hiçbir şekilde değiştirmeyin:
  - Google Haritalar'ın büyük harf kullanımını değiştirmeyin.
  - Google Haritalar'ı birden fazla satıra sarmayın.
  - Google Haritalar'ı başka bir dile yerelleştirmeyin.
  - HTML özelliğini kullanarak tarayıcıların Google Haritalar'ı çevirmesini engelleyin.

Google Haritalar veri sağlayıcılarımızdan bazıları ve lisans şartları hakkında daha fazla bilgi için [Google Haritalar ve Google Earth yasal uyarıları](https://www.google.com/help/legalnotices_maps/?hl=tr) sayfasını inceleyin.

## En iyi uygulamalar

- **Kullanıcı konumunu sağlama:** En alakalı ve kişiselleştirilmiş yanıtlar için kullanıcının konumu bilindiğinde `google_maps` aracı yapılandırmanıza her zaman `latitude` ve `longitude` değerlerini ekleyin.
- **Son kullanıcıları bilgilendirin:** Son kullanıcılarınızı, özellikle araç etkinleştirildiğinde sorgularını yanıtlamak için Google Haritalar verilerinin kullanıldığı konusunda açıkça bilgilendirin.
- **Gerekmediğinde Kapatma:** Google Haritalar ile temellendirme varsayılan olarak kapalıdır. Performansı ve maliyeti optimize etmek için bu özelliği (`"tools": [{"type": "google_maps"}]`) yalnızca bir sorgunun net bir coğrafi bağlamı olduğunda etkinleştirin.

## Sınırlamalar

- Google Haritalar ile Temellendirme şu anda yalnızca İngilizce istemleri ve yanıtları desteklemektedir.
- Araç bazı bölgelerde kullanılamayabilir.
- Sonuçlar, konum doğruluğuna ve mevcut Haritalar verilerine göre değişiklik gösterebilir.
- **Coğrafi Kapsam:** Google Haritalar ile temellendirme dünya genelinde kullanılabilir.
- **Varsayılan durum:** Google Haritalar ile Temellendirme aracı varsayılan olarak kapalıdır.
  API isteklerinizde bu özelliği açıkça etkinleştirmeniz gerekir.

## Fiyatlandırma ve sıklık sınırları

Google Haritalar ile Temellendirme fiyatlandırması, model nesline göre farklılık gösterir:

- **Gemini 3 ve daha yeni modeller:** Projeniz, modelin yürütmeye karar verdiği her arama sorgusu için faturalandırılır. Tüm Gemini 3 ve daha yeni modellerde ayda 5.000 ücretsiz istek paylaşılır ve ardından **1.000 arama sorgusu başına 14 ABD doları** ücret alınır. Tek bir arama istemi (modele yönelik API isteğiniz), modelin gerekli bilgileri bulmak için birden fazla arama sorgusu yürütmesine neden olabilir. Bu sorguların her biri, aracın faturalandırılabilir kullanımı olarak sayılır.
- **Gemini 2.5 ve eski modeller:** Projeniz,arama istemi başına faturalandırılır
  (1.000 temellendirilmiş istem için 25 ABD doları). Bir istek, yalnızca istem en az bir Google Haritalar temelli sonuç döndürdüğünde faturalandırılır. Modelin bu sonucu elde etmek için dahili olarak kaç tane arama sorgusu gerçekleştirdiği önemli değildir.

Google Haritalar ile Temellendirme kotası genellikle temel Gemini modelinin sıklık sınırlamalarıyla uyumludur. Ayrıntılı fiyatlandırma bilgileri için [Gemini API fiyatlandırma sayfasını](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) inceleyin.

## Desteklenen modeller

Aşağıdaki modellerde Google Haritalar ile Temellendirme özelliği desteklenir:

| Model | Google Haritalar ile temellendirme |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=tr) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=tr) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=tr) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=tr) | ✔️ |
| [Gemini 3.1 Pro Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=tr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=tr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=tr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=tr) | ✔️ |

## Desteklenen araç kombinasyonları

Daha karmaşık kullanım alanlarını desteklemek için Google Haritalar ile Temellendirme'yi, [Google Arama ile Temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) (Gemini 3.5 Flash-Lite ve sonraki modellerde desteklenir) gibi diğer yerleşik araçlarla birlikte kullanabilirsiniz.
Gemini 3 modelleri, bu yerleşik araçların özel araçlarla (işlev çağrısı) birlikte kullanılmasını da destekler. [Araç kombinasyonları](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) sayfasından daha fazla bilgi edinebilirsiniz.

## Sırada ne var?

- Kullanabileceğiniz [diğer araçlar](https://ai.google.dev/gemini-api/docs/tools?hl=tr) hakkında bilgi edinin.
- Sorumlu yapay zekaya dair en iyi uygulamalar ve Gemini API'nin güvenlik filtreleri hakkında daha fazla bilgi edinmek için [Güvenlik ayarları kılavuzuna](https://ai.google.dev/gemini-api/docs/safety-settings?hl=tr) bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-13 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-13 UTC."],[],[]]
