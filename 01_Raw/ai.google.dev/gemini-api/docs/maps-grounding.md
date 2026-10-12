---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fr
fetched_at: 2026-10-12T06:51:16.902631+00:00
title: "Ancrage avec Google\u00a0Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Ancrage avec Google Maps

L'ancrage avec Google Maps permet d'associer les capacités génératives de Gemini aux données riches, factuelles et à jour de Google Maps. Cette fonctionnalité permet aux développeurs d'intégrer facilement des fonctionnalités de localisation dans leurs applications. Lorsqu'une requête utilisateur comporte un contexte lié aux données Maps, le modèle Gemini s'appuie sur Google Maps pour fournir des réponses factuelles et récentes qui sont pertinentes pour la zone géographique spécifiée par l'utilisateur ou la zone géographique générale.

- **Des réponses précises et géolocalisées** : exploitez les données actuelles et exhaustives de Google Maps pour les requêtes géographiques spécifiques.
- **Personnalisation améliorée** : personnalisez les recommandations et les informations en fonction des lieux fournis par les utilisateurs.

## Commencer

Cet exemple montre comment intégrer l'ancrage avec Google Maps à votre application pour fournir des réponses précises et géolocalisées aux requêtes des utilisateurs. La requête demande des recommandations locales avec une position de l'utilisateur facultative, ce qui permet au modèle Gemini d'utiliser les données Google Maps.

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

## Fonctionnement de l'ancrage avec Google Maps

L'ancrage avec Google Maps intègre l'API Gemini à l'écosystème Google Geo en utilisant l'API Google Maps comme source d'ancrage. Lorsque la requête d'un utilisateur contient un contexte géographique, le modèle Gemini peut appeler l'outil d'ancrage avec Google Maps. Le modèle peut ensuite générer des réponses ancrées dans les données Google Maps pertinentes pour le lieu fourni.

Ce processus implique généralement les étapes suivantes :

1. **Requête utilisateur** : un utilisateur envoie une requête à votre application, qui peut inclure un contexte géographique (par exemple, "cafés à proximité", "musées à San Francisco").
2. **Invocation de l'outil** : le modèle Gemini, qui reconnaît l'intention géographique, invoque l'outil d'ancrage avec Google Maps. Cet outil peut éventuellement être fourni avec les `latitude` et `longitude` de l'utilisateur. Cet outil de recherche textuelle fonctionne de la même manière que la recherche dans Maps. Les requêtes locales ("près de moi") utilisent les coordonnées, tandis que les requêtes spécifiques ou non locales sont peu susceptibles d'être influencées par la position explicite.
3. **Récupération des données** : le service d'ancrage avec Google Maps interroge Google Maps pour obtenir des informations pertinentes (par exemple, des lieux, des avis, des photos, des adresses ou des horaires d'ouverture).
4. **Génération ancrée** : les données Maps récupérées sont utilisées pour étayer la réponse du modèle Gemini, ce qui garantit l'exactitude et la pertinence des faits.
5. **Réponse et annotations** : le modèle renvoie une réponse textuelle avec des annotations intégrées renvoyant aux sources Google Maps, ce qui permet aux développeurs d'afficher des citations.

## Pourquoi et quand utiliser l'ancrage avec Google Maps

L'ancrage avec Google Maps est idéal pour les applications qui nécessitent des informations précises, à jour et spécifiques à un lieu. Elle améliore l'expérience utilisateur en fournissant des contenus pertinents et personnalisés, basés sur la vaste base de données de Google Maps qui compte plus de 250 millions de lieux dans le monde.

Vous devez utiliser l'ancrage avec Google Maps lorsque votre application doit :

- Fournissez des réponses complètes et précises aux questions spécifiques à une zone géographique.
- Créez des planificateurs de voyage et des guides locaux conversationnels.
- Recommander des points d'intérêt en fonction de la position et des préférences de l'utilisateur (restaurants ou magasins, par exemple).
- Créez des expériences basées sur la localisation pour les services sociaux, de vente au détail ou de livraison de repas.

L'ancrage avec Google Maps excelle dans les cas d'utilisation où la proximité et les données factuelles actuelles sont essentielles, comme pour trouver le "meilleur café à proximité" ou obtenir un itinéraire.

## Cas d'utilisation

L'ancrage avec Google Maps est compatible avec différents cas d'utilisation basés sur la localisation.

### Gérer les questions spécifiques à un lieu

Posez des questions détaillées sur un lieu spécifique pour obtenir des réponses basées sur les avis des utilisateurs Google et d'autres données Maps.

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

### Fournir une personnalisation basée sur la position

Obtenez des recommandations adaptées aux préférences d'un utilisateur et à une zone géographique spécifique.

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

### Aide à la planification d'itinéraires

Générez des plans sur plusieurs jours avec des itinéraires et des informations sur différents lieux, parfaits pour les applications de voyage.

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

## Conditions d'utilisation des services

Cette section décrit les exigences d'utilisation du service pour l'ancrage avec Google Maps.

### Informer l'utilisateur de l'utilisation des sources Google Maps

Pour chaque résultat Google Maps ancré, vous recevrez des annotations de source sur les blocs de contenu de l'étape `model_output` qui soutiennent chaque réponse. Les métadonnées suivantes sont renvoyées :

- URL source
- nom

Lorsque vous présentez des résultats issus de l'ancrage avec Google Maps, vous devez spécifier les sources Google Maps associées et informer vos utilisateurs des points suivants :

- Les sources Google Maps doivent suivre immédiatement le contenu généré qu'elles prennent en charge. Ce contenu généré est également appelé "résultat ancré Google Maps".
- Les sources Google Maps doivent être visibles en une seule interaction de l'utilisateur.

### Afficher les sources Google Maps avec des liens Google Maps

Pour chaque annotation source, un aperçu du lien doit être généré en respectant les exigences suivantes :

- Attribuez chaque source à Google Maps en suivant les [Consignes d'attribution](#maps-attribution-guidelines) du texte Google Maps.
- Affichez le nom de la source fourni dans la réponse.
- Associez la source à l'aide de `url` à partir de l'annotation.

### Consignes concernant l'attribution de texte Google Maps

Lorsque vous attribuez des sources à Google Maps dans un texte, suivez ces consignes :

- Ne modifiez en aucun cas le texte "Google Maps" :
  - Ne modifiez pas la typographie de Google Maps.
  - N'insérez pas Google Maps sur plusieurs lignes.
  - Ne localisez pas Google Maps dans une autre langue.
  - Empêchez les navigateurs de traduire Google Maps en utilisant l'attribut HTML translate="no".

Pour en savoir plus sur certains de nos fournisseurs de données Google Maps et sur les conditions de licence qu'ils appliquent, consultez les [mentions légales de Google Maps et Google Earth](https://www.google.com/help/legalnotices_maps/?hl=fr).

## Bonnes pratiques

- **Indiquez la position de l'utilisateur** : pour obtenir les réponses les plus pertinentes et personnalisées, incluez toujours `latitude` et `longitude` dans la configuration de votre outil `google_maps` lorsque la position de l'utilisateur est connue.
- **Informez les utilisateurs finaux** : indiquez clairement à vos utilisateurs finaux que les données Google Maps sont utilisées pour répondre à leurs requêtes, en particulier lorsque l'outil est activé.
- **Désactivez l'ancrage avec Google Maps lorsque vous n'en avez pas besoin** : il est désactivé par défaut. Ne l'activez (`"tools": [{"type": "google_maps"}]`) que lorsqu'une requête présente un contexte géographique clair, afin d'optimiser les performances et les coûts.

## Limites

- L'ancrage avec Google Maps n'accepte actuellement que les requêtes et les réponses en anglais.
- Il est possible que l'outil ne soit pas disponible dans toutes les régions.
- Les résultats peuvent varier en fonction de la précision de la localisation et des données Maps disponibles.
- **Couverture géographique** : l'ancrage avec Google Maps est disponible dans le monde entier.
- **État par défaut** : l'outil d'ancrage avec Google Maps est désactivé par défaut.
  Vous devez l'activer explicitement dans vos requêtes d'API.

## Tarifs et limites de débit

Les tarifs de l'ancrage avec Google Maps varient selon la génération du modèle :

- **Gemini 3 et modèles ultérieurs** : votre projet est facturé pour chaque requête de recherche que le modèle décide d'exécuter, avec 5 000 requêtes sans frais par mois partagées entre tous les modèles Gemini 3 et ultérieurs, puis **14 $ pour 1 000 requêtes de recherche**. Une seule requête de recherche (votre requête d'API au modèle) peut entraîner l'exécution de plusieurs requêtes de recherche par le modèle pour trouver les informations nécessaires. Chacune de ces requêtes est considérée comme une utilisation facturable de l'outil.
- **Gemini 2.5 et modèles plus anciens** : votre projet est facturé par requête de recherche (25 $ pour 1 000 requêtes ancrées). Une requête n'est facturée que si la requête renvoie au moins un résultat ancré Google Maps, quel que soit le nombre de requêtes de recherche individuelles effectuées en interne par le modèle pour obtenir ce résultat.

Le quota d'ancrage avec Google Maps correspond généralement aux limites de débit du modèle Gemini sous-jacent. Pour en savoir plus sur les tarifs, consultez la [page des tarifs de l'API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=fr).

## Modèles compatibles

Les modèles suivants sont compatibles avec l'ancrage avec Google Maps :

| Modèle | Ancrage avec Google Maps |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=fr) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=fr) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=fr) | ✔️ |
| [Preview Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fr) | ✔️ |
| [Preview Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=fr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=fr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=fr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=fr) | ✔️ |

## Combinaisons d'outils compatibles

Vous pouvez utiliser l'ancrage avec Google Maps avec d'autres outils intégrés, comme l'[ancrage avec la recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr) (pris en charge sur les modèles Gemini 3.5 Flash-Lite et versions ultérieures), pour des cas d'utilisation plus complexes.
Les modèles Gemini 3 prennent également en charge la combinaison de ces outils intégrés avec des outils personnalisés (appel de fonction). Pour en savoir plus, consultez la page sur les [combinaisons d'outils](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr).

## Étape suivante

- En savoir plus sur les autres [outils disponibles](https://ai.google.dev/gemini-api/docs/tools?hl=fr)
- Pour en savoir plus sur les bonnes pratiques d'IA responsable et les filtres de sécurité de l'API Gemini, consultez le [guide sur les paramètres de sécurité](https://ai.google.dev/gemini-api/docs/safety-settings?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/10/09 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/10/09 (UTC)."],[],[]]
