---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419
fetched_at: 2026-09-28T06:10:56.103279+00:00
title: "API de Interactions \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# API de Interactions

La API de Interactions es la mejor manera de crear soluciones con modelos y agentes de Gemini. A partir de junio de 2026, estará disponible de forma general y se recomienda para todos los proyectos nuevos. Si bien ahora se considera heredada, la API original de [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=es-419) sigue siendo totalmente compatible.

## ¿Por qué usar la API de Interactions?

- **Interfaz universal para todas las aplicaciones**: Se diseñó como la interfaz estándar para cada caso de uso, incluida la generación de texto de un solo turno, la comprensión multimodal, las salidas estructuradas, la orquestación de herramientas y los flujos de trabajo basados en agentes.
- **Una sola API para modelos y agentes**: Un extremo y un patrón unificados para llamar a los modelos estándar de Gemini y a los agentes especializados directamente (como Deep Research y los agentes administrados personalizados).
- **Nuevas capacidades listas para usar**: Funciones como el estado de conversación opcional del servidor con `previous_interaction_id`, pasos de ejecución observables para la depuración y la renderización de la IU, y [ejecución en segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=es-419) para tareas de larga duración con `background=true`.
- **Menor costo con mayores tasas de aciertos de caché**: Cuando se usan conversaciones de varios turnos, la administración de estado opcional del servidor permite un almacenamiento en caché del contexto más eficiente en los turnos, lo que reduce los costos de tokens.
- **Dónde se lanzarán las funciones nuevas**: En el futuro, todos los modelos nuevos, las capacidades multimodales, las herramientas y las funciones basadas en agentes se lanzarán en la API de Interactions.

De forma predeterminada, la API de Interactions almacena solicitudes para que puedas aprovechar las funciones de administración de estado del servidor con `previous_interaction_id`. Puedes habilitar el comportamiento sin estado configurando `store=false`. Consulta la sección sobre la [retención de datos](#data-storage-retention) para obtener más información.

## Comenzar

- **Configura tu agente de programación**: Conéctate al **MCP de Gemini Docs** y, luego, instala la habilidad `gemini-api-dev` para darle a tu asistente acceso directo a la documentación para desarrolladores y las prácticas recomendadas más recientes. Para conocer los pasos detallados, consulta la [guía para configurar tu agente de programación](https://ai.google.dev/gemini-api/docs/coding-agents?hl=es-419).
- **Migra desde `generateContent`**: Si tienes una integración existente, sigue la [guía de migración](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=es-419) para realizar la transición a la API de Interactions.
- **Comienza**: Sigue los pasos de la [guía de inicio de la API de Interactions](https://ai.google.dev/gemini-api/docs/get-started?hl=es-419).

### Guías de funciones

Explora las capacidades específicas de la API de Interactions a través de estas guías. Puedes usar el botón de activación de estas páginas para cambiar entre la API de generateContent y la de Interactions:

- [Generación de texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419)
- [Generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419)
- [Comprensión de imágenes](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419)
- [Comprensión de audio](https://ai.google.dev/gemini-api/docs/audio?hl=es-419)
- [Comprensión de videos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=es-419)
- [Procesamiento de documentos](https://ai.google.dev/gemini-api/docs/document-processing?hl=es-419)
- [Llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)
- [Salidas estructuradas](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419)
- [Agente de Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419)
- [Inferencia flexible](https://ai.google.dev/gemini-api/docs/flex-inference?hl=es-419)
- [Inferencia de prioridad](https://ai.google.dev/gemini-api/docs/priority-inference?hl=es-419)

## Cómo funciona la API de Interactions

La API de Interactions se centra en un recurso principal: [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=es-419#Resource:Interaction). Un `Interaction` representa un turno completo en una conversación o tarea. Actúa como un registro de sesión, que contiene todo el historial de una interacción como una secuencia cronológica de **pasos de ejecución**. Estos pasos incluyen las reflexiones del modelo, las llamadas a herramientas y los resultados del servidor o del cliente (como `function_call` y `function_result`), y el `model_output` final. El recurso almacenado (recuperado a través de `interactions.get`) también incluye pasos de `user_input` para el contexto completo, aunque la respuesta de `interactions.create` solo devuelve los pasos generados por el modelo.

Cuando llamas a [`interactions.create`](https://ai.google.dev/api/interactions-api?hl=es-419#CreateInteraction), creas un nuevo recurso `Interaction`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a short story about a time-traveling lighthouse."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Tell me a short story about a time-traveling lighthouse.",
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
        .input(InteractionsInput.of("Tell me a short story about a time-traveling lighthouse."))
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
            Input: interactions.NewInteractionsInput("Tell me a short story about a time-traveling lighthouse."),
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
    "model": "gemini-3.8-flash",
    "input": "Tell me a short story about a time-traveling lighthouse."
  }'
```

### Administración del estado del servidor

Puedes usar el `id` de una interacción completada en una llamada posterior con el parámetro `previous_interaction_id` para continuar la conversación. El servidor usa este ID para recuperar el historial de conversación, lo que te evita tener que volver a enviar todo el historial de chat:

### Python

```
from google import genai

client = genai.Client()

# 1. First turn
turn1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Phil."
)

# 2. Second turn (chained using previous_interaction_id)
turn2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is my name?",
    previous_interaction_id=turn1.id
)

print(turn2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

// 1. First turn
const turn1 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Hi, my name is Phil.",
});

// 2. Second turn (chained using previous_interaction_id)
const turn2 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "What is my name?",
  previous_interaction_id: turn1.id,
});

console.log(turn2.output_text);
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

// 1. First turn
Interaction turn1 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("Hi, my name is Phil."))
                    .build()))
        .interaction()
        .get();

// 2. Second turn (chained using previousInteractionId)
Interaction turn2 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("What is my name?"))
                    .previousInteractionId(turn1.id().get())
                    .build()))
        .interaction()
        .get();

System.out.println(turn2.outputText().orElse(""));
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

    // 1. First turn
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Hi, my name is Phil."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // 2. Second turn (chained using PreviousInteractionID)
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            Input:                 interactions.NewInteractionsInput("What is my name?"),
            PreviousInteractionID: turn1.Interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

### REST

```
# Replace PREVIOUS_INTERACTION_ID with the id returned from the first turn
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is my name?",
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID"
  }'
```

El parámetro `previous_interaction_id` solo conserva el historial de conversaciones (entradas y salidas) con `previous_interaction_id`. Los demás parámetros son de **alcance de la interacción** y se aplican solo a la interacción específica que estás generando:

- `tools`
- `system_instruction`
- `generation_config` (incluidos `thinking_level`, `temperature`, etcétera)

Esto significa que debes volver a especificar estos parámetros en cada interacción nueva si quieres que se apliquen. Esta administración de estado del servidor es opcional. También puedes operar en modo sin estado enviando el historial de conversación completo en cada solicitud.

### Almacenamiento y retención de datos

De forma predeterminada, la API almacena todos los objetos Interaction (`store=true`) para simplificar el uso de las funciones de administración de estados del servidor (con `previous_interaction_id`), la [ejecución en segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=es-419) (con `background=true`) y los fines de observabilidad.

- **Nivel pagado**: El sistema conserva las interacciones durante **55 días**.
- **Nivel gratuito**: El sistema retiene las interacciones durante **1 día**.

Si no quieres esto, puedes establecer `store=false` en tu solicitud. Este control es independiente de la administración del estado. Puedes inhabilitar el almacenamiento para cualquier interacción. Sin embargo, ten en cuenta que `store=false` no es compatible con la [ejecución en segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=es-419) y evita el uso de `previous_interaction_id` en turnos posteriores.

En el caso de los proyectos del nivel pagado, puedes configurar el período de retención en [AI Studio](https://aistudio.google.com/logs?hl=es-419) para marcar automáticamente los registros para su eliminación del almacenamiento del proyecto después de 7, 14, 28 o 55 días. Una retención más corta puede afectar la recuperación de conversaciones anteriores.

Puedes borrar las interacciones almacenadas en cualquier momento con el método [`delete`](https://ai.google.dev/api/interactions-api?hl=es-419#deleteInteraction) de forma programática, lo que requiere el ID de interacción. También puedes ver y administrar los registros de interacciones almacenados, incluida la eliminación del almacenamiento del proyecto, en [AI Studio](https://aistudio.google.com/logs?hl=es-419).

Una vez que venza el período de retención, tus datos se borrarán automáticamente.

Los objetos de interacciones se procesan según las [condiciones](https://ai.google.dev/gemini-api/terms?hl=es-419).

### Cómo ver las interacciones en AI Studio

La API almacena las solicitudes de la API de Interactions ejecutadas con `store=true` para los proyectos del nivel pagado. Puedes verlos directamente en la [página Logs de Google AI Studio](https://ai.google.dev/gemini-api/docs/www.aistudio.google.com/logs?hl=es-419). Para obtener más información, consulta la [guía de registros](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=es-419).

## Prácticas recomendadas

- **Tasa de aciertos de caché**: El almacenamiento en caché implícito se admite en los modos con y sin estado (consulta la [guía de inicio rápido](https://ai.google.dev/gemini-api/docs/get-started?hl=es-419#4_multi-turn_conversations)). El uso de `previous_interaction_id` (con estado) para continuar las conversaciones permite que el sistema utilice más fácilmente el almacenamiento en caché implícito para el historial de conversaciones, lo que mejora el rendimiento y reduce los costos.
- **Combinación de interacciones**: Tienes la flexibilidad de combinar interacciones del agente y del modelo en una conversación. Por ejemplo, puedes usar un agente especializado, como el agente de Deep Research, para la recopilación inicial de datos y, luego, usar un modelo estándar de Gemini para tareas de seguimiento, como resumir o reformatear, y vincular estos pasos con `previous_interaction_id`.

## Modelos y agentes compatibles

| Nombre del modelo | Tipo | ID de modelo |
| --- | --- | --- |
| Gemini 3.8 Flash | Modelo | `gemini-3.8-flash` |
| Gemini 3.7 Flash | Modelo | `gemini-3.7-flash` |
| Gemini 3.6 Flash | Modelo | `gemini-3.6-flash` |
| Gemini 3.5 Flash | Modelo | `gemini-3.5-flash` |
| Versión preliminar de Gemini 3.1 Pro | Modelo | `gemini-3.1-pro-preview` |
| Gemini 3.5 Flash-Lite | Modelo | `gemini-3.5-flash-lite` |
| Gemini 3.1 Flash-Lite | Modelo | `gemini-3.1-flash-lite` |
| Versión preliminar de Gemini 3 Flash | Modelo | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Modelo | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Modelo | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | Modelo | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | Modelo | `gemini-3-pro-image` |
| Gemini 3.1 Flash Image | Modelo | `gemini-3.1-flash-image` |
| Versión preliminar de TTS de Gemini 3.1 Flash | Modelo | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | Modelo | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | Modelo | `gemma-4-26b-a4b-it` |
| Lyria 3.5 | Modelo | `lyria-3.5` |
| Vista previa de clip de Lyria 3 | Modelo | `lyria-3-clip-preview` |
| Versión preliminar de Lyria 3 Pro | Modelo | `lyria-3-pro-preview` |
| Versión preliminar de Deep Research | Agente | `deep-research-preview-04-2026` |
| Versión preliminar de Deep Research | Agente | `deep-research-max-preview-04-2026` |
| Vista previa de Antigravity | Agente | `antigravity-preview-09-2026` |

## SDK

Puedes usar la versión más reciente de los SDKs de IA generativa de Google para acceder a la API de Interactions.

- En Python, este es el paquete `google-genai` a partir de la versión `2.3.0`.
- En JavaScript, este es el paquete `@google/genai` a partir de la versión `2.3.0`.
- En Go, este es el paquete `google.golang.org/genai`.
- En Java, este es el paquete `com.google.genai:google-genai`.

Puedes obtener más información para instalar los SDKs en la página [Libraries](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419).

## Limitaciones

- **MCP remoto**: Gemini 3 no admite MCP remoto. Esta función estará disponible pronto.
- **Compatibilidad del modelo de varios turnos**: Cuando se combinan diferentes modelos en una conversación (con estado o sin estado), los modelos posteriores deben admitir las modalidades de salida de los modelos anteriores como entrada. Por ejemplo, si generas una imagen con `gemini-3.1-flash-image`, no puedes continuar esa conversación con un modelo que no acepte entradas de imágenes (como un modelo solo de texto o un modelo de generación de música como Lyria).

La API de [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=es-419) admite las siguientes funciones, pero **aún no están disponibles** en la API de Interactions:

- **[API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419)**
- **[Llamada a función automática (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=es-419#automatic_function_calling_python_only)**
- **[Almacenamiento en caché explícito](https://ai.google.dev/gemini-api/docs/caching?hl=es-419)**: Ten en cuenta que el almacenamiento en caché implícito del servidor está disponible en la API de Interactions a través de `previous_interaction_id`.
- **[Configuración de seguridad](https://ai.google.dev/gemini-api/docs/safety-settings?hl=es-419)**: La API de Interactions no admite la configuración de seguridad personalizada.

## Comentarios

Tus comentarios son fundamentales para el desarrollo de la API de Interactions.
Comparte tus opiniones, informa errores o solicita funciones en nuestro [foro de la comunidad de desarrolladores de IA de Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=es-419).

## ¿Qué sigue?

- Prueba el [notebook de inicio rápido de la API de Interactions](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=es-419).
- Obtén más información sobre el [agente de Deep Research de Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-24 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-24 (UTC)"],[],[]]
