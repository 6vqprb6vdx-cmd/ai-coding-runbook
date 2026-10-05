---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=es-419
fetched_at: 2026-10-05T06:26:28.199253+00:00
title: "Novedades de Gemini 3.8 Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Novedades de Gemini 3.8 Flash

[Ver todos los modelos](https://ai.google.dev/gemini-api/docs/models?hl=es-419)

Gemini 3.8 Flash (`gemini-3.8-flash`) tiene disponibilidad general (DG) y está listo para su uso en producción. Es nuestro modelo Flash más inteligente, diseñado para ingeniería de software a largo plazo, agentes autónomos y flujos de trabajo empresariales complejos.

En esta guía, se explican las novedades de Gemini 3.8 Flash, los cambios en la API, los ejemplos de código y la orientación para la migración.

## Modelo nuevo

| Modelo | ID de modelo | Nivel de pensamiento predeterminado | Precios | Descripción |
| --- | --- | --- | --- | --- |
| Gemini 3.8 Flash | `gemini-3.8-flash` | `medium` | 3.8 Flash está disponible hasta fin de año a un precio de introducción de USD 0.75 por 1 M de tokens de entrada y USD 3.75 por 1 M de tokens de salida. Consulta los [precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419) para obtener más detalles. | Nuestro modelo Flash más inteligente, diseñado para ingeniería de software a largo plazo, agentes autónomos y flujos de trabajo empresariales complejos. |

Gemini 3.8 Flash admite una ventana de contexto de 1 millón de tokens, un máximo de 64, 000 tokens de salida, niveles de pensamiento ajustables (`low`, `medium`, `high`) y el mismo conjunto integral de herramientas integradas.

Para conocer las especificaciones completas, consulta la [página del modelo Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=es-419). Para obtener detalles sobre los precios de introducción, consulta la [sección de precios](#pricing) a continuación o la [página de precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#gemini-3.8-flash).

## Guía de inicio rápido

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write a three.js script that renders a realistic 3D black hole."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Write a three.js script that renders a realistic 3D black hole.",
});

console.log(interaction.output_text);
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

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Write a three.js script that renders a realistic 3D black hole."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Write a three.js script that renders a realistic 3D black hole."),
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
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Write a three.js script that renders a realistic 3D black hole."
  }'
```

## Novedades de Gemini 3.8 Flash

- **Ingeniería de software a largo plazo:** Ofrece resultados sólidos en comparativas de programación del mundo real, refactorización compleja de varios archivos y ejecución determinística de herramientas. Consulta la [metodología de evaluación](https://deepmind.google/models/evals-methodology/gemini-3-8-flash/?hl=es-419) para obtener más detalles.
- **Agentes autónomos:** Te permite crear flujos de trabajo de planificación y organización de herramientas de varios pasos resilientes, lo que reduce considerablemente los bucles y errores fallidos.
- **Flujos de trabajo empresariales complejos:** Ofrece una precisión superior, un razonamiento profundo y un alto rigor fáctico en tareas de dominio exigentes y canalizaciones de datos a gran escala.
- **Modelo predeterminado para los agentes administrados:** El agente predeterminado para los agentes administrados, el [agente de Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419), ahora usa Gemini 3.8 Flash. El [SDK de Antigravity](https://antigravity.google/docs/sdk/overview/?hl=es-419) también usa Gemini 3.8 Flash de forma predeterminada.
- **Precios de lanzamiento:** Gemini 3.8 Flash está disponible a una tarifa de lanzamiento de USD 0.75 por 1 M de tokens de entrada y USD 3.75 por 1 M de tokens de salida hasta el 31 de diciembre de 2026. Los precios estándar de USD 1.50 por 1 M de tokens de entrada y USD 7.50 por 1 M de tokens de salida entrarán en vigencia el 1 de enero de 2027.

Por diseño, Gemini 3.8 Flash puede usar más tokens en tareas complejas y de mayor duración. Para ofrecer resultados de mayor calidad en objetivos difíciles de varios pasos, el modelo realiza pasos de razonamiento más pequeños, llama a las herramientas de forma iterativa y verifica su trabajo a lo largo del proceso. No todos los flujos de trabajo necesitan este nivel de verificación. Para las tareas diarias, puedes reducir el esfuerzo de [razonamiento](#understanding-reasoning-levels) para disminuir el consumo de tokens. Como alternativa, Gemini 3.7 Flash sigue siendo totalmente compatible.

## Cómo comprender los niveles de razonamiento

Gemini 3.8 Flash te brinda un control flexible sobre la latencia y la inteligencia, ya que te permite ajustar el nivel de razonamiento del modelo:

- **Bajo esfuerzo de razonamiento**: Reduce el tiempo de respuesta para tareas críticas de latencia, como canalizaciones de respuesta ante incidentes, chat en tiempo real, redacción de borradores y análisis de datos rápidos.
- **Mediana (predeterminada):** Es la mejor calidad para la mayoría de las tareas. Se recomienda para casos de uso complejos de código y agentes, ya que proporciona una mayor precisión en la primera pasada.
- **Alto esfuerzo de pensamiento**: Maximiza las capacidades de razonamiento y organización de herramientas del modelo. Ideal para razonamiento profundo, matemáticas y tareas difíciles de varios pasos.

En el siguiente ejemplo, se configura `thinking_level` como `medium` para una solicitud de análisis de código compleja:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    generation_config={
        "thinking_level": "medium"  # Balanced reasoning effort for complex tasks
    }
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  generation_config: {
    thinking_level: "medium"
  }
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

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely."))
        .generationConfig(
            GenerationConfig.builder()
                .thinkingLevel(ThinkingLevel.MEDIUM) // Balanced reasoning effort for complex tasks
                .build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely."),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelMedium.ToPointer(), // Balanced reasoning effort for complex tasks
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
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    "generation_config": {
      "thinking_level": "medium"
    }
  }'
```

## Se actualizó el agente de Antigravity

Debido a su rendimiento y razonamiento mejorados, el [agente de Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419) de los Agentes administrados por Gemini ahora se compila de forma predeterminada con la tecnología de Gemini 3.8 Flash.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input=(
        "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
        "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
        "Check search indexing with Google Search for site:web.dev. "
        "Format the output as a side-by-side scorecard table with prioritized fixes."
    ),
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  agent: "antigravity-preview-09-2026",
  input: "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
  environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent(AgentOption.of("antigravity-preview-09-2026"))
        .input(
            InteractionsInput.of(
                "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
                    + "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
                    + "Check search indexing with Google Search for site:web.dev. "
                    + "Format the output as a side-by-side scorecard table with prioritized fixes."))
        .environment(CreateAgentInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

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
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput(
                "Audit https://web.dev for performance, Core Web Vitals, and SEO. " +
                    "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. " +
                    "Check search indexing with Google Search for site:web.dev. " +
                    "Format the output as a side-by-side scorecard table with prioritized fixes.",
            ),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
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
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google'\''s PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
    "environment": "remote"
}'
```

El modelo subyacente de Gemini [se puede configurar](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419#model-selection) con `agent_config`.

## Lista de tareas para la migración

```
  `/gemini-api-dev migrate my app to Gemini 3.8 Flash`
```

### Migra a gemini-3.8-flash

- **Actualiza el ID del modelo:** Cambia la cadena del modelo objetivo a `gemini-3.8-flash`.
- **Se quitaron los parámetros de muestreo obsoletos:**
  - Se quitaron `temperature`, `top_p` y `top_k` de las configuraciones de generación.
  - Reemplaza `thinking_budget` por la cadena de enumeración `thinking_level`. Ten en cuenta que `minimal` no es compatible con Flash 3.8.
  - Se quitó `candidate_count` (no compatible con Gemini 3 y versiones posteriores).
- **Aplica reglas de validación de turnos:**
  - Estandariza las conversaciones de varios turnos en `previous_interaction_id` del servidor.
  - Quita los turnos del modelo completados previamente.
- **Audita las llamadas a función:**
  - Coloca los recursos multimodales dentro de la carga útil de la respuesta.
  - Da formato a las instrucciones intercaladas con `\n\n`.
  - Si ves errores `Malformed_Function_Call` vinculados al texto previo a la herramienta, consulta [Soluciones alternativas para los requisitos de texto previo a la herramienta](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#workarounds-for-pre-tool-text-requirements).
  - Solo si se usa la API de generateContent: Asegúrate de que todos los objetos `FunctionResponse` incluyan `call_id` y `name`.
- **Requisitos básicos de Gemini 3:** Para las actualizaciones del SDK y la conservación de la firma de pensamiento, consulta la [Lista de tareas para la migración a Gemini 3.5](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=es-419#migration).

## Precios

Aprovecha los precios de introducción en Google AI Studio y Gemini Enterprise Agent Platform hasta el 31 de diciembre de 2026 para Gemini 3.8 Flash, Gemini 3.7 Flash y Gemini 3.6 Flash. Los precios estándar entrarán en vigencia el 1 de enero de 2027. Para conocer los precios completos, consulta la [página de precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#gemini-3.8-flash).

## Próximos pasos

- Revisa las especificaciones de la API en la [Descripción general de los modelos](https://ai.google.dev/gemini-api/docs/models?hl=es-419).
- Explora la organización de varios agentes en la [Descripción general de la API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419).
- Probar y definir instrucciones en [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-24 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-24 (UTC)"],[],[]]
