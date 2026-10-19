---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl
fetched_at: 2026-10-19T05:36:09.878797+00:00
title: "Grounding z u\u017cyciem Map Google \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Grounding z użyciem Map Google

Grounding z użyciem Map Google łączy możliwości generatywne Gemini z bogatymi, aktualnymi i opartymi na faktach danymi z Map Google. Ta funkcja umożliwia deweloperom łatwe wprowadzanie w aplikacjach funkcji uwzględniających lokalizację. Gdy zapytanie użytkownika ma kontekst związany z danymi z Map, model Gemini korzysta z Map Google, aby udzielać dokładnych i aktualnych odpowiedzi, które są odpowiednie dla określonej przez użytkownika lokalizacji lub ogólnego obszaru.

- **Dokładne odpowiedzi uwzględniające lokalizację:** korzystaj z obszernych i aktualnych danych z Map Google w przypadku zapytań dotyczących konkretnych lokalizacji.
- **Ulepszona personalizacja:** dostosowuj rekomendacje i informacje na podstawie lokalizacji podanych przez użytkownika.

## Rozpocznij

Ten przykład pokazuje, jak zintegrować powiązanie ze źródłami informacji przy użyciu Map Google z aplikacją, aby udzielać dokładnych odpowiedzi uwzględniających lokalizację na zapytania użytkowników. Prompt prosi o lokalne rekomendacje z opcjonalną lokalizacją użytkownika, co umożliwia modelowi Gemini korzystanie z danych z Map Google.

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

## Jak działa grounding z użyciem Map Google

Powiązanie ze źródłami informacji przy użyciu Map Google integruje interfejs Gemini API z ekosystemem Google Geo, używając interfejsu API Map Google jako źródła informacji. Gdy zapytanie użytkownika zawiera kontekst geograficzny, model Gemini może wywołać narzędzie Grounding z użyciem Map Google. Model może wtedy generować odpowiedzi na podstawie danych z Map Google dotyczących podanej lokalizacji.

Proces ten zwykle obejmuje te etapy:

1. **Zapytanie użytkownika:** użytkownik przesyła zapytanie do Twojej aplikacji, które może zawierać kontekst geograficzny (np. „kawiarnie w pobliżu”, „muzea w San Francisco”).
2. **Wywołanie narzędzia:** model Gemini, rozpoznając intencję geograficzną, wywołuje narzędzie powiązanie ze źródłami informacji przy użyciu Map Google. To narzędzie może opcjonalnie otrzymać współrzędne geograficzne użytkownika (`latitude` i `longitude`). Narzędzie to służy do wyszukiwania tekstowego i działa podobnie do wyszukiwania w Mapach. Zapytania lokalne („w pobliżu”) będą korzystać ze współrzędnych, a zapytania konkretne lub nielokalne raczej nie będą uwzględniać lokalizacji.
3. **Pobieranie danych:** usługa powiązanie ze źródłami informacji przy użyciu Map Google wysyła zapytania do Map Google, aby uzyskać odpowiednie informacje (np. miejsca, opinie, zdjęcia, adresy, godziny otwarcia).
4. **Generowanie oparte na faktach:** Pobrane dane z Map są używane do tworzenia odpowiedzi przez model Gemini, co zapewnia zgodność z prawdą i trafność.
5. **Odpowiedź i adnotacje:** model zwraca odpowiedź tekstową z adnotacjami w tekście, które zawierają linki do źródeł w Mapach Google, co umożliwia deweloperom wyświetlanie cytatów.

## Kiedy i dlaczego warto używać powiązania ze źródłami informacji przy użyciu Map Google

Powiązanie ze źródłami informacji przy użyciu Map Google jest idealne w przypadku aplikacji, które wymagają dokładnych, aktualnych i specyficznych dla lokalizacji informacji. Poprawia komfort użytkowania, udostępniając trafne i spersonalizowane treści oparte na obszernej bazie danych Map Google, która zawiera ponad 250 milionów miejsc na całym świecie.

Powiązanie ze źródłami informacji przy użyciu Map Google warto używać, gdy aplikacja musi:

- udzielać wyczerpujących i dokładnych odpowiedzi na pytania dotyczące lokalizacji;
- tworzyć konwersacyjne kreatory podróży i lokalne przewodniki;
- polecać ciekawe miejsca na podstawie lokalizacji i preferencji użytkownika, np. restauracje lub sklepy;
- tworzyć funkcje uwzględniające lokalizację w usługach społecznościowych, handlowych lub dostawy jedzenia.

Powiązanie ze źródłami informacji przy użyciu Map Google sprawdza się w przypadkach użycia, w których kluczowe są bliskość i aktualne dane zgodne z prawdą, np. podczas wyszukiwania „najlepszej kawiarni w pobliżu” lub wyznaczania trasy.

## Przypadki użycia

Powiązanie ze źródłami informacji przy użyciu Map Google obsługuje różne przypadki użycia uwzględniające lokalizację.

### Obsługa pytań dotyczących konkretnych miejsc

Zadawaj szczegółowe pytania o konkretne miejsce, aby uzyskać odpowiedzi na podstawie opinii użytkowników Google i innych danych z Map.

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

### Udostępnianie personalizacji na podstawie lokalizacji

Uzyskuj rekomendacje dostosowane do preferencji użytkownika i konkretnego obszaru geograficznego.

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

### Pomoc w planowaniu planu podróży

Generuj plany wielodniowe z trasami i informacjami o różnych lokalizacjach, które są idealne w przypadku aplikacji podróżniczych.

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

## Wymagania dotyczące korzystania z usługi

Ta sekcja zawiera opis wymagań dotyczących korzystania z usługi Grounding z użyciem Map Google.

### Informowanie użytkownika o korzystaniu ze źródeł z Map Google

W przypadku każdego wyniku opartego na danych z Map Google otrzymasz adnotacje źródłowe w blokach treści kroku `model_output`, które obsługują każdą odpowiedź. Zwracane są te metadane:

- adres URL źródła
- nazwa

Podczas prezentowania wyników groundingu z użyciem Map Google musisz określić powiązane źródła z Map Google i poinformować użytkowników o tych kwestiach:

- Źródła z Map Google muszą znajdować się bezpośrednio po wygenerowanej treści, którą obsługują. Ta wygenerowana treść jest też nazywana wynikiem opartym na danych z Map Google.
- Źródła z Map Google muszą być widoczne w ramach jednej interakcji użytkownika.

### Wyświetlanie źródeł z Map Google z linkami do Map Google

W przypadku każdej adnotacji źródłowej należy wygenerować podgląd linku zgodnie z tymi wymaganiami:

- Przypisz każde źródło do Map Google zgodnie ze wskazówkami dotyczącymi atrybucji tekstowej w Mapach Google
  .
- Wyświetl nazwę źródła podaną w odpowiedzi.
- Utwórz link do źródła za pomocą `url` z adnotacji.

### Wskazówki dotyczące atrybucji tekstowej w Mapach Google

Gdy przypisujesz źródła do Map Google w tekście, postępuj zgodnie z tymi wskazówkami:

- Nie modyfikuj w żaden sposób tekstu Mapy Google:
  - Nie zmieniaj wielkości liter w nazwie Mapy Google.
  - Nie dziel nazwy Mapy Google na kilka wierszy.
  - Nie tłumacz nazwy Mapy Google na inny język.
  - Uniemożliwiaj przeglądarkom tłumaczenie nazwy Mapy Google, używając atrybutu HTML translate="no".

Więcej informacji o niektórych dostawcach danych do Map Google i ich
warunkach licencji znajdziesz w [informacjach prawnych dotyczących Map Google i Google Earth](https://www.google.com/help/legalnotices_maps/?hl=pl).

## Sprawdzone metody

- **Podaj lokalizację użytkownika:** aby uzyskać najbardziej trafne i spersonalizowane odpowiedzi, zawsze uwzględniaj współrzędne geograficzne (`latitude` i `longitude`) w konfiguracji narzędzia `google_maps`, gdy znana jest lokalizacja użytkownika.
- **Informuj użytkowników:** wyraźnie informuj użytkowników, że do odpowiadania na ich zapytania używane są dane z Map Google, zwłaszcza gdy narzędzie jest włączone.
- **Wyłączaj, gdy nie jest potrzebne:** Powiązanie ze źródłami informacji przy użyciu Map Google jest domyślnie wyłączone. Aby zoptymalizować wydajność i koszty, włączaj go (`"tools": [{"type": "google_maps"}]`) tylko wtedy, gdy zapytanie ma
  wyraźny kontekst geograficzny.

## Ograniczenia

- Powiązanie ze źródłami informacji przy użyciu Map Google obsługuje obecnie tylko prompty i odpowiedzi w języku angielskim.
- Narzędzie może być niedostępne w niektórych regionach.
- Wyniki mogą się różnić w zależności od dokładności lokalizacji i dostępnych danych z Map.
- **Zasięg geograficzny:** Powiązanie ze źródłami informacji przy użyciu Map Google jest dostępne na całym świecie.
- **Stan domyślny:** narzędzie powiązanie ze źródłami informacji przy użyciu Map Google jest domyślnie wyłączone.
  Musisz je wyraźnie włączyć w żądaniach do interfejsu API.

## Ceny i ograniczanie liczby żądań

Ceny powiązania ze źródłami informacji przy użyciu Map Google różnią się w zależności od generowania modelu:

- **Modele Gemini 3 i nowsze:** projekt jest obciążany za każde zapytanie wyszukiwania, które model zdecyduje się wykonać. Miesięcznie masz do dyspozycji 5000 bezpłatnych zapytań, które są wspólne dla wszystkich modeli Gemini 3 i nowszych. Następnie płacisz **14 USD za 1000 zapytań wyszukiwania**. Pojedynczy prompt wyszukiwania (żądanie do interfejsu API wysyłane do modelu) może spowodować, że model wykona wiele zapytań wyszukiwania, aby znaleźć potrzebne informacje. Każde z tych zapytań jest liczone jako płatne użycie narzędzia.
- **Modele Gemini 2.5 i starsze:** projekt jest obciążany za każdy prompt wyszukiwania (25 USD za 1000 promptów opartych na danych podstawowych). Opłata jest naliczana tylko wtedy, gdy prompt zwróci co najmniej 1 wynik oparty na danych z Map Google, niezależnie od tego, ile pojedynczych zapytań wyszukiwania model wykonał wewnętrznie, aby uzyskać ten wynik.

Limit zapytań w przypadku groundingu z użyciem Map Google jest zwykle zgodny z limitami zapytań podstawowego modelu Gemini. Szczegółowe informacje o cenach znajdziesz na stronie z cennikiem interfejsu [Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=pl).

## Obsługiwane modele

Powiązanie ze źródłami informacji przy użyciu Map Google obsługują te modele:

| Model | Powiązanie ze źródłami informacji przy użyciu Map Google |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=pl) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=pl) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=pl) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=pl) | ✔️ |
| [Gemini 3.1 Pro (wersja zapoznawcza)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3 Flash (wersja zapoznawcza)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pl) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ |

## Obsługiwane kombinacje narzędzi

Powiązanie ze źródłami informacji przy użyciu Map Google możesz używać z innymi wbudowanymi narzędziami, takimi jak
[powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl) (obsługiwane w modelach
Gemini 3.5 Flash-Lite i nowszych), aby obsługiwać bardziej złożone przypadki użycia.
Modele Gemini 3 obsługują też łączenie tych wbudowanych narzędzi z narzędziami niestandardowymi (wywoływanie funkcji). Więcej informacji znajdziesz na
[stronie dotyczącej kombinacji narzędzi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl).

## Co dalej?

- Dowiedz się więcej o innych [dostępnych narzędziach](https://ai.google.dev/gemini-api/docs/tools?hl=pl).
- Więcej informacji o sprawdzonych metodach dotyczących odpowiedzialnej AI i filtrach bezpieczeństwa interfejsu Gemini API znajdziesz w [przewodniku po ustawieniach bezpieczeństwa](https://ai.google.dev/gemini-api/docs/safety-settings?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-13 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-13 UTC."],[],[]]
