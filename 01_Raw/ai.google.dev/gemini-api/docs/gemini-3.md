---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=es-419
fetched_at: 2026-09-28T06:15:48.403971+00:00
title: "Gu\u00eda para desarrolladores de Gemini 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)

Enviar comentarios

# Guía para desarrolladores de Gemini 3

Gemini 3 es nuestra familia de modelos más inteligente hasta la fecha, creada sobre una base de razonamiento de vanguardia. Está diseñado para hacer realidad cualquier idea a través del dominio de flujos de trabajo de agentes, la programación autónoma y las tareas multimodales complejas.
En esta guía, se explican las funciones clave de la familia de modelos Gemini 3 y cómo aprovecharlas al máximo.

Explora nuestra [colección de apps de Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=es-419) para ver cómo el modelo maneja el razonamiento avanzado, la programación autónoma y las tareas multimodales complejas.

Comienza con algunas líneas de código:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(
            InteractionsInput.of(
                "Find the race condition in this multi-threaded C++ snippet: [code here]"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.1-pro-preview"),
            Input: interactions.NewInteractionsInput("Find the race condition in this multi-threaded C++ snippet: [code here]"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Conoce la serie Gemini 3

Gemini 3.1 Pro es el mejor modelo para tareas complejas que requieren un amplio conocimiento del mundo y un razonamiento avanzado en todas las modalidades.

Gemini 3 Flash es nuestro modelo más reciente de la serie 3, con inteligencia de nivel Pro a la velocidad y el precio de Flash.

Nano Banana Pro (también conocido como Gemini 3 Pro Image) es nuestro modelo de generación de imágenes de mayor calidad, y Nano Banana 2 (también conocido como Gemini 3.1 Flash Image) es el equivalente de alto volumen, alta eficiencia y menor precio.

Gemini 3.1 Flash-Lite es nuestro modelo de trabajo diseñado para ser rentable y realizar tareas de gran volumen.

Actualmente, todos los modelos de Gemini 3 están en versión preliminar.

| ID de modelo | Ventana de contexto (dentro / fuera) | Fecha límite de conocimiento | Precios (entrada y salida)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1 millón / 64,000 | Enero de 2025 | USD 0.25 (texto, imagen, video), USD 0.50 (audio) / USD 1.50 |
| **gemini-3.1-flash-image-preview** | 128 k / 32 k | Enero de 2025 | USD 0.25 (entrada de texto) / USD 0.067 (salida de imagen)\*\* |
| **gemini-3.1-pro-preview** | 1 millón / 64,000 | Enero de 2025 | USD 2 / USD 12 (menos de 200,000 tokens)   USD 4 / USD 18 (más de 200,000 tokens) |
| **gemini-3-flash-preview** | 1 millón / 64,000 | Enero de 2025 | USD 0.50 / USD 3 |
| **gemini-3-pro-image-preview** | 65,000 / 32,000 | Enero de 2025 | USD 2 (entrada de texto) / USD 0.134 (salida de imagen)\*\* |

*\* Los precios son por 1 millón de tokens, a menos que se indique lo contrario.*
*\*\* Los precios de las imágenes varían según la resolución. Consulta la [página de precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419) para obtener más detalles.*

Para obtener información detallada sobre los límites, los precios y otros datos, consulta la [página de modelos](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419).

## Nuevas funciones de la API en Gemini 3

Gemini 3 introduce nuevos parámetros diseñados para brindarles a los desarrolladores más control sobre la latencia, el costo y la fidelidad multimodal.

### Nivel de pensamiento

Los modelos de la serie Gemini 3 usan el pensamiento dinámico de forma predeterminada para razonar las instrucciones. Puedes usar el parámetro `thinking_level`, que controla la profundidad **máxima** del proceso de razonamiento interno del modelo antes de que produzca una respuesta. Gemini 3 trata estos niveles como asignaciones relativas para el razonamiento en lugar de garantías estrictas de tokens.

Si no se especifica `thinking_level`, Gemini 3 usará `high` de forma predeterminada. Para obtener respuestas más rápidas y con menor latencia cuando no se requiere un razonamiento complejo, puedes restringir el nivel de pensamiento del modelo a `low`.

| Nivel de razonamiento | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Descripción |
| --- | --- | --- | --- | --- |
| **`minimal`** | No compatible | Admitido (predeterminado) | Admitido | Coincide con el parámetro de configuración "sin pensar" para la mayoría de las búsquedas. El modelo puede pensar de forma muy mínima para tareas de programación complejas. Minimiza la latencia para aplicaciones de chat o de alta capacidad de procesamiento. Ten en cuenta que `minimal` no garantiza que el pensamiento esté desactivado. |
| **`low`** | Admitido | Admitido | Admitido | Minimiza la latencia y el costo. Es ideal para seguir instrucciones simples, chatear o usar aplicaciones de alta capacidad de procesamiento. |
| **`medium`** | Admitido | Admitido | Admitido | Pensamiento equilibrado para la mayoría de las tareas. |
| **`high`** | Admitido (predeterminado, dinámico) | Admitido (dinámico) | Admitido (predeterminado, dinámico) | Maximiza la profundidad del razonamiento. El modelo puede tardar mucho más en alcanzar un primer token de salida (sin pensar), pero la salida se razonará con más cuidado. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(InteractionsInput.of("How does AI work?"))
        .generationConfig(
            GenerationConfig.builder()
                .thinkingLevel(ThinkingLevel.LOW)
                .build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.1-pro-preview"),
            Input: interactions.NewInteractionsInput("How does AI work?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelLow.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### Temperatura

Para todos los modelos de Gemini 3, te recomendamos que mantengas el parámetro de temperatura en su valor predeterminado de `1.0`.

Si bien los modelos anteriores a menudo se beneficiaban de ajustar la temperatura para controlar la creatividad en comparación con el determinismo, las capacidades de razonamiento de Gemini 3 están optimizadas para el parámetro de configuración predeterminado. Cambiar la temperatura (establecerla por debajo de 1.0) puede generar un comportamiento inesperado, como bucles o un rendimiento degradado, en especial en tareas complejas de razonamiento o matemáticas.

### Firmas de razonamiento

Los modelos de Gemini 3 usan firmas de pensamiento para mantener el contexto de razonamiento en las llamadas a la API. Estas firmas son representaciones encriptadas del proceso de pensamiento interno del modelo.

- **Modo con estado (recomendado)**: Cuando se usa la API de Interactions en modo con estado (proporcionando `previous_interaction_id`), el servidor administra automáticamente el historial de conversaciones y las firmas de pensamiento.
- **Modo sin estado**: Si administras el historial de conversación de forma manual, debes incluir bloques de pensamiento con sus firmas en las solicitudes posteriores para validar la autenticidad.

Para obtener información detallada, consulta la página [Firmas de pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419).

### Resultados estructurados con herramientas

Los modelos de Gemini 3 te permiten combinar [salidas estructuradas](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419) con herramientas integradas, como la [Fundamentación con la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419), el [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419), la [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) y las [Llamadas a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.interactions.URLContext;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();
properties.put("winner", Map.of("type", "string", "description", "The name of the winner."));
properties.put(
    "final_match_score", Map.of("type", "string", "description", "The final match score."));
properties.put(
    "scorers",
    Map.of(
        "type", "array",
        "items", Map.of("type", "string"),
        "description", "The name of the scorer."));

Map<String, Object> schema = new HashMap<>();
schema.put("type", "object");
schema.put("properties", properties);
schema.put("required", Arrays.asList("winner", "final_match_score", "scorers"));

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-pro-preview"))
        .input(InteractionsInput.of("Search for all details for the latest Euro."))
        .tools(Arrays.asList(GoogleSearch.builder().build(), URLContext.builder().build()))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(
                    TextResponseFormat.builder()
                        .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                        .schema(schema)
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

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

    schema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "winner": map[string]any{
                "type":        "string",
                "description": "The name of the winner.",
            },
            "final_match_score": map[string]any{
                "type":        "string",
                "description": "The final match score.",
            },
            "scorers": map[string]any{
                "type":        "array",
                "items":       map[string]any{"type": "string"},
                "description": "The name of the scorer.",
            },
        },
        "required": []string{"winner", "final_match_score", "scorers"},
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.1-pro-preview"),
            Input: interactions.NewInteractionsInput("Search for all details for the latest Euro."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
                interactions.NewTool(interactions.URLContext{}),
            },
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.TextResponseFormat{
                    MimeType: interactions.TextResponseFormatMimeType("application/json").ToPointer(),
                    Schema:   schema,
                }),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Generación de imágenes

Gemini 3.1 Flash Image y Gemini 3 Pro Image te permiten generar y editar imágenes a partir de instrucciones de texto. Utiliza el razonamiento para "pensar" en una instrucción y puede recuperar datos en tiempo real, como pronósticos del clima o gráficos de acciones, antes de usar la fundamentación de la [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419) para generar imágenes de alta fidelidad.

**Capacidades nuevas y mejoradas:**

- **Renderización de texto y 4K:** Genera texto y diagramas nítidos y legibles con resoluciones de hasta 2K y 4K.
- **Generación fundamentada:** Usa la herramienta `google_search` para verificar hechos y generar imágenes basadas en información del mundo real. La fundamentación con la Búsqueda de *Imágenes* de Google está disponible para Gemini 3.1 Flash Image.
- **Edición conversacional:** Edición de imágenes de varios turnos con solo pedir cambios (p.ej., "Haz que el fondo sea un atardecer"). Este flujo de trabajo se basa en las **firmas de pensamiento** para conservar el contexto visual entre turnos.

Para obtener detalles completos sobre las relaciones de aspecto, los flujos de trabajo de edición y las opciones de configuración, consulta la [guía de generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419).

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageResponseFormat;
import com.google.genai.gaos.models.interactions.ImageResponseFormatAspectRatio;
import com.google.genai.gaos.models.interactions.ImageResponseFormatImageSize;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.Optional;

Client client = new Client();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-pro-image-preview"))
        .input(InteractionsInput.of("Generate an infographic of the current weather in Tokyo."))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(
                    ImageResponseFormat.builder()
                        .aspectRatio(ImageResponseFormatAspectRatio.ONE_HUNDRED_AND_SIXTY_NINE)
                        .imageSize(ImageResponseFormatImageSize.FOUR_K)
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

Optional<ImageContent> generatedImage = interaction.outputImage();
if (generatedImage.isPresent() && generatedImage.get().data().isPresent()) {
  byte[] imageBytes = Base64.getDecoder().decode(generatedImage.get().data().get());
  Files.write(Paths.get("weather_tokyo.png"), imageBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3-pro-image-preview"),
            Input: interactions.NewInteractionsInput("Generate an infographic of the current weather in Tokyo."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.ImageResponseFormat{
                    AspectRatio: interactions.ImageResponseFormatAspectRatioOneHundredAndSixtyNine.ToPointer(),
                    ImageSize:   interactions.ImageResponseFormatImageSize("4K").ToPointer(),
                }),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if generatedImage := res.Interaction.GetOutputImage(); generatedImage != nil && generatedImage.Data != nil {
        imageBytes, err := base64.StdEncoding.DecodeString(*generatedImage.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("weather_tokyo.png", imageBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**Ejemplo de respuesta**

![Clima en Tokio](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=es-419)

### Ejecución de código con imágenes

Gemini 3 Flash puede tratar la visión como una investigación activa, no solo como una mirada estática. Al combinar el razonamiento con la [ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419), el modelo formula un plan y, luego, escribe y ejecuta código de Python para acercar, recortar, anotar o manipular imágenes de otra manera paso a paso para fundamentar visualmente sus respuestas.

**Casos de uso:**

- **Acercar y revisar:** El modelo detecta de forma implícita cuando los detalles son demasiado pequeños (p.ej., leer un medidor o un número de serie distantes) y escribe código para recortar y volver a examinar el área con una resolución más alta.
- **Cálculos y gráficos visuales:** El modelo puede ejecutar cálculos de varios pasos con código (p.ej., sumar los artículos de una factura o generar un gráfico de Matplotlib a partir de datos extraídos).
- **Anotación de imágenes:** El modelo puede dibujar flechas, cuadros delimitadores o cualquier otra anotación directamente en las imágenes para responder preguntas espaciales como "¿Dónde debería ir este elemento?".

Para habilitar el pensamiento visual, configura [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) como herramienta. El modelo usará código automáticamente para manipular imágenes cuando sea necesario.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CodeExecutionCallStep;
import com.google.genai.gaos.models.interactions.CodeExecutionResultStep;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.io.InputStream;
import java.net.URL;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;

Client client = new Client();

URL url = new URL("https://goo.gle/instrument-img");
byte[] imageBytes;
try (InputStream is = url.openStream()) {
  imageBytes = is.readAllBytes();
}
String base64ImageData = Base64.getEncoder().encodeToString(imageBytes);

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    ImageContent.builder()
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .data(base64ImageData)
                        .build(),
                    TextContent.builder()
                        .text("Zoom into the expression pedals and tell me how many pedals are there?")
                        .build())))
        .tools(Arrays.asList(CodeExecution.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep) {
    ModelOutputStep modelOutput = (ModelOutputStep) step;
    for (Content contentBlock : modelOutput.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent) {
        System.out.println("Text: " + ((TextContent) contentBlock).text().orElse(""));
      }
    }
  } else if (step instanceof CodeExecutionCallStep) {
    CodeExecutionCallStep callStep = (CodeExecutionCallStep) step;
    callStep.arguments().flatMap(args -> args.code()).ifPresent(code -> System.out.println("Code: " + code));
  } else if (step instanceof CodeExecutionResultStep) {
    CodeExecutionResultStep resultStep = (CodeExecutionResultStep) step;
    System.out.println("Output: " + resultStep.result().orElse(""));
  }
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "io"
    "log"
    "net/http"

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

    httpRes, err := http.Get("https://goo.gle/instrument-img")
    if err != nil {
        log.Fatal(err)
    }
    defer httpRes.Body.Close()
    imageBytes, err := io.ReadAll(httpRes.Body)
    if err != nil {
        log.Fatal(err)
    }
    base64ImageData := base64.StdEncoding.EncodeToString(imageBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3-flash-preview"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    MimeType: interactions.ImageContentMimeType("image/jpeg").ToPointer(),
                    Data:     genai.Ptr(base64ImageData),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: "Zoom into the expression pedals and tell me how many pedals are there?",
                }),
            }),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if modelOutput := step.ModelOutputStep; modelOutput != nil {
            for _, contentBlock := range modelOutput.Content {
                if textContent := contentBlock.TextContent; textContent != nil {
                    fmt.Println("Text:", textContent.Text)
                }
            }
        } else if callStep := step.CodeExecutionCallStep; callStep != nil {
            if callStep.Arguments.Code != nil {
                fmt.Println("Code:", *callStep.Arguments.Code)
            }
        } else if resultStep := step.CodeExecutionResultStep; resultStep != nil {
            fmt.Println("Output:", resultStep.Result)
        }
    }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

Para obtener más detalles sobre la ejecución de código con imágenes, consulta [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419#images).

### Respuestas de funciones multimodales

La [llamada a función multimodal](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#multimodal) permite que los usuarios obtengan respuestas de funciones que contienen objetos multimodales, lo que mejora el uso de las capacidades de llamada a función del modelo. Las llamadas a funciones estándar solo admiten respuestas de funciones basadas en texto:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.FunctionResultSubcontent;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.io.InputStream;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

Client client = new Client();

Map<String, Object> itemProp = new HashMap<>();
itemProp.put("type", "string");
itemProp.put("description", "The name or description of the item ordered (e.g., 'instrument').");

Map<String, Object> properties = new HashMap<>();
properties.put("item_name", itemProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("item_name"));

Function getImageTool =
    Function.builder()
        .name("get_image")
        .description("Retrieves the image file reference for a specific order item.")
        .parameters(parameters)
        .build();

CreateModelInteraction req1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.of(
                "Use the get_image tool to show me the instrument I ordered last month."))
        .tools(Arrays.asList(getImageTool))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(req1)).interaction().get();

FunctionCallStep fcStep = null;
for (Step step : interaction1.steps().orElse(Collections.emptyList())) {
  if (step instanceof FunctionCallStep) {
    fcStep = (FunctionCallStep) step;
    break;
  }
}

if (fcStep != null) {
  System.out.println("Tool Call: " + fcStep.name().orElse(""));

  URL url = new URL("https://goo.gle/instrument-img");
  byte[] imageBytes;
  try (InputStream is = url.openStream()) {
    imageBytes = is.readAllBytes();
  }
  String base64ImageData = Base64.getEncoder().encodeToString(imageBytes);

  List<FunctionResultSubcontent> subcontents = new ArrayList<>();
  subcontents.add(TextContent.builder().text("instrument.jpg").build());
  subcontents.add(
      ImageContent.builder()
          .mimeType(ImageContentMimeType.IMAGE_JPEG)
          .data(base64ImageData)
          .build());

  FunctionResultStep funcResult =
      FunctionResultStep.builder()
          .name(fcStep.name().orElse(""))
          .callId(fcStep.id().orElse(""))
          .result(FunctionResultStepResultUnion.of(subcontents))
          .build();

  CreateModelInteraction req2 =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3-flash-preview"))
          .input(InteractionsInput.ofStep(Arrays.asList(funcResult)))
          .tools(Arrays.asList(getImageTool))
          .previousInteractionId(interaction1.id().orElse(""))
          .build();

  Interaction interaction2 =
      client.interactions.create(CreateInteractionRequestBody.of(req2)).interaction().get();
  System.out.println("Final model response: " + interaction2.outputText().orElse(""));
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "io"
    "log"
    "net/http"

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

    getImageTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_image"),
        Description: genai.Ptr("Retrieves the image file reference for a specific order item."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "item_name": map[string]any{
                    "type":        "string",
                    "description": "The name or description of the item ordered (e.g., 'instrument').",
                },
            },
            "required": []string{"item_name"},
        },
    })

    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3-flash-preview"),
            Input: interactions.NewInteractionsInput("Use the get_image tool to show me the instrument I ordered last month."),
            Tools: []interactions.Tool{getImageTool},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res1.Interaction.Steps {
        if fcStep := step.FunctionCallStep; fcStep != nil {
            fmt.Println("Tool Call:", fcStep.Name)

            httpRes, err := http.Get("https://goo.gle/instrument-img")
            if err != nil {
                log.Fatal(err)
            }
            defer httpRes.Body.Close()
            imageBytes, err := io.ReadAll(httpRes.Body)
            if err != nil {
                log.Fatal(err)
            }
            base64ImageData := base64.StdEncoding.EncodeToString(imageBytes)

            funcResult := interactions.NewStep(interactions.FunctionResultStep{
                Name:   genai.Ptr(fcStep.Name),
                CallID: fcStep.ID,
                Result: interactions.NewFunctionResultStepResultUnion([]interactions.FunctionResultSubcontent{
                    interactions.NewFunctionResultSubcontent(interactions.TextContent{
                        Text: "instrument.jpg",
                    }),
                    interactions.NewFunctionResultSubcontent(interactions.ImageContent{
                        MimeType: interactions.ImageContentMimeType("image/jpeg").ToPointer(),
                        Data:     genai.Ptr(base64ImageData),
                    }),
                }),
            })

            res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model:                 interactions.Model("gemini-3-flash-preview"),
                    PreviousInteractionID: res1.Interaction.ID,
                    Tools:                 []interactions.Tool{getImageTool},
                    Input:                 interactions.NewInteractionsInput([]interactions.Step{funcResult}),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            if res2.Interaction.OutputText != nil {
                fmt.Println("Final model response:", *res2.Interaction.OutputText)
            }
            break
        }
    }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### Combina herramientas integradas y llamadas a funciones

Gemini 3 permite el uso de herramientas integradas (como la Búsqueda de Google, el contexto de URL y [más](https://ai.google.dev/gemini-api/docs/tools?hl=es-419)) y herramientas personalizadas de [llamada a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) en la misma llamada a la API, lo que permite flujos de trabajo más complejos.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> cityProp = new HashMap<>();
cityProp.put("type", "string");
cityProp.put("description", "The city and state, e.g. Utqiaġvik, Alaska");

Map<String, Object> properties = new HashMap<>();
properties.put("city", cityProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("city"));

Function getWeather =
    Function.builder()
        .name("getWeather")
        .description("Gets the weather for a requested city.")
        .parameters(parameters)
        .build();

CreateModelInteraction request =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3-flash-preview"))
        .input(
            InteractionsInput.of(
                "What is the northernmost city in the United States? What's the weather like there today?"))
        .tools(Arrays.asList(GoogleSearch.builder().build(), getWeather))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(request)).interaction().get();

FunctionCallStep fcStep = null;
for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof FunctionCallStep) {
    fcStep = (FunctionCallStep) step;
    break;
  }
}

if (fcStep != null) {
  FunctionResultStep funcResult =
      FunctionResultStep.builder()
          .name(fcStep.name().orElse(""))
          .callId(fcStep.id().orElse(""))
          .result(
              FunctionResultStepResultUnion.of(
                  "{\"response\": \"Very cold. 22 degrees Fahrenheit.\"}"))
          .build();

  CreateModelInteraction finalRequest =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3-flash-preview"))
          .input(InteractionsInput.ofStep(Arrays.asList(funcResult)))
          .tools(Arrays.asList(GoogleSearch.builder().build(), getWeather))
          .previousInteractionId(interaction.id().orElse(""))
          .build();

  Interaction finalInteraction =
      client.interactions.create(CreateInteractionRequestBody.of(finalRequest)).interaction().get();
  System.out.println(finalInteraction.outputText().orElse(""));
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

    getWeather := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("getWeather"),
        Description: genai.Ptr("Gets the weather for a requested city."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "city": map[string]any{
                    "type":        "string",
                    "description": "The city and state, e.g. Utqiaġvik, Alaska",
                },
            },
            "required": []string{"city"},
        },
    })

    tools := []interactions.Tool{
        interactions.NewTool(interactions.GoogleSearch{}),
        getWeather,
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3-flash-preview"),
            Input: interactions.NewInteractionsInput("What is the northernmost city in the United States? What's the weather like there today?"),
            Tools: tools,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if fcStep := step.FunctionCallStep; fcStep != nil {
            funcResult := interactions.NewStep(interactions.FunctionResultStep{
                Name:   genai.Ptr(fcStep.Name),
                CallID: fcStep.ID,
                Result: interactions.NewFunctionResultStepResultUnion(`{"response": "Very cold. 22 degrees Fahrenheit."}`),
            })

            finalRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model:                 interactions.Model("gemini-3-flash-preview"),
                    PreviousInteractionID: res.Interaction.ID,
                    Tools:                 tools,
                    Input:                 interactions.NewInteractionsInput([]interactions.Step{funcResult}),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            if finalRes.Interaction.OutputText != nil {
                fmt.Println(*finalRes.Interaction.OutputText)
            }
            break
        }
    }
}
```

## Migración desde Gemini 2.5

Gemini 3 es nuestra familia de modelos más potente hasta la fecha y ofrece una mejora gradual con respecto a Gemini 2.5. Cuando realices la migración, ten en cuenta lo siguiente:

- **Pensar:** Si antes usabas ingeniería de instrucciones compleja (como la cadena de pensamiento) para obligar a Gemini 2.5 a razonar, prueba Gemini 3 con `thinking_level: "high"` y con instrucciones simplificadas.
- **Configuración de temperatura:** Si tu código existente establece explícitamente la temperatura (en especial, en valores bajos para obtener resultados determinísticos), te recomendamos que quites este parámetro y uses el valor predeterminado de Gemini 3, que es 1.0, para evitar posibles problemas de bucles o degradación del rendimiento en tareas complejas.
- **Comprensión de documentos y PDFs:**
  Si dependías de un comportamiento específico para el análisis de documentos densos, prueba el nuevo parámetro de configuración de `media_resolution_high` para garantizar la precisión continua.
- **Consumo de tokens:** La migración a los valores predeterminados de Gemini 3 puede **aumentar** el uso de tokens para los archivos PDF, pero **disminuir** el uso de tokens para los videos. Si las solicitudes ahora superan la ventana de contexto debido a resoluciones predeterminadas más altas, te recomendamos que reduzcas explícitamente la resolución de los medios.
- **Segmentación de imágenes:** Las capacidades de segmentación de imágenes (que devuelven máscaras a nivel de píxel para los objetos) no son compatibles con Gemini 3 Pro ni Gemini 3 Flash. Para las cargas de trabajo que requieren segmentación de imágenes integrada, recomendamos seguir usando Gemini 2.5 Flash con el modo de pensamiento desactivado.
- **Uso de la computadora:** Gemini 3 Pro y Gemini 3 Flash admiten el [uso de la computadora](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419). A diferencia de la serie 2.5, no necesitas usar un modelo independiente para acceder a la herramienta Uso de la computadora.
- **Compatibilidad con herramientas**: Ahora se admite la [combinación de herramientas integradas con llamadas a funciones](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419) para los modelos de Gemini 3. También se admite el [anclaje a tierra de Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419) para los modelos de Gemini 3.

## Compatibilidad con OpenAI

Para los usuarios que utilizan la [capa de compatibilidad con OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=es-419), los parámetros estándar (`reasoning_effort` de OpenAI) se asignan automáticamente a los equivalentes de Gemini (`thinking_level`).

## Prácticas recomendadas para escribir instrucciones

Gemini 3 es un modelo de razonamiento, lo que cambia la forma en que debes darle instrucciones.

- **Instrucciones precisas:** Sé conciso en tus instrucciones. Gemini 3 responde mejor a las instrucciones directas y claras. Es posible que analice en exceso las técnicas de ingeniería de instrucciones detalladas o demasiado complejas que se usaban para los modelos anteriores.
- **Detalle de la respuesta:** De forma predeterminada, Gemini 3 es menos detallado y prefiere proporcionar respuestas directas y eficientes. Si tu caso de uso requiere un asistente más conversacional o "parlanchín", debes dirigir explícitamente el modelo en la instrucción (p.ej., "Explica esto como un asistente amigable y parlanchín").
- **Administración del contexto:** Cuando trabajes con conjuntos de datos grandes (p.ej., libros completos, bases de código o videos largos), coloca tus instrucciones o preguntas específicas al final de la instrucción, después del contexto de los datos. Ancla el razonamiento del modelo a los datos proporcionados comenzando tu pregunta con una frase como "Según la información anterior…".

Obtén más información sobre las estrategias de diseño de instrucciones en la [guía de ingeniería de instrucciones](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=es-419).

## Preguntas frecuentes

1. **¿Cuál es la fecha límite de conocimiento de Gemini 3?** Los modelos de Gemini 3 tienen una fecha límite de conocimiento de enero de 2025. Para obtener información más reciente, usa la herramienta [Search Grounding](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419).
2. **¿Cuáles son los límites de la ventana de contexto?** Los modelos de Gemini 3 admiten una ventana de contexto de entrada de 1 millón de tokens y hasta 64,000 tokens de salida.
3. **¿Existe un nivel gratuito para Gemini 3?** Gemini 3 Flash`gemini-3-flash-preview` tiene un nivel gratuito en la API de Gemini. Puedes probar Gemini 3.1 Pro y 3 Flash sin costo en Google AI Studio, pero no hay un nivel gratuito disponible para `gemini-3.1-pro-preview` en la API de Gemini.
4. **¿Mi código `thinking_budget` anterior seguirá funcionando?** Sí, `thinking_budget` sigue siendo compatible con versiones anteriores, pero recomendamos migrar a `thinking_level` para obtener un rendimiento más predecible. No uses ambos en la misma solicitud.
5. **¿Gemini 3 admite la API de Batch?** Sí, Gemini 3 admite la [API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419).
6. **¿Se admite el almacenamiento en caché de contexto?** Sí, [Context Caching](https://ai.google.dev/gemini-api/docs/caching?hl=es-419) es compatible con Gemini 3.
7. **¿Qué herramientas son compatibles con Gemini 3?** Gemini 3 admite [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419), [Fundamentación con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419), [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419), [Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) y [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419). También admite la [Llamada a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419) estándar para tus propias herramientas personalizadas y en [combinación con herramientas integradas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419).
8. **¿Qué es `gemini-3.1-pro-preview-customtools`?** Si usas `gemini-3.1-pro-preview` y el modelo ignora tus herramientas personalizadas en favor de los comandos de bash, prueba el modelo `gemini-3.1-pro-preview-customtools`.
   Obtén más información [aquí][customtools-model].

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-24 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-24 (UTC)"],[],[]]
