---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=es-419
fetched_at: 2026-08-31T06:35:53.629973+00:00
title: "Ejecuci\u00f3n en segundo plano \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Ejecución en segundo plano

Para tareas de larga duración, como la investigación exhaustiva, el razonamiento complejo o las ejecuciones de agentes de varios pasos, los tiempos de espera de conexión pueden interrumpir las solicitudes HTTP estándar (que suelen cerrarse después de 60 segundos). La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) proporciona la **ejecución en segundo plano** para ejecutar estas tareas de forma asíncrona.

Para permitir que la interacción se ejecute hasta que complete la tarea en el servidor, establece `"background": true` cuando crees la interacción. La API muestra de inmediato un ID de interacción, que las aplicaciones cliente pueden usar para sondear el estado, transmitir el progreso o volver a conectarse a una transmisión desconectada.

La ejecución en segundo plano es compatible con los modelos estándar de Gemini (como `gemini-3.6-flash` y `gemini-3.1-pro-preview`) y los agentes administrados (como `antigravity-preview-05-2026`).

## Crea una interacción en segundo plano

Para iniciar una interacción en segundo plano, establece el parámetro `background` en `true` cuando crees el recurso.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a guide on space exploration.",
    background=True,
)
print(f"Created background interaction ID: {interaction.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Write a guide on space exploration.",
    background: true,
});
console.log(`Created background interaction ID: ${interaction.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Write a guide on space exploration.",
    "background": true
  }'
```

## Cómo funciona la ejecución en segundo plano

Cuando creas una interacción en segundo plano, la tarea se ejecuta de forma asíncrona en el servidor. La interacción pasa por varios estados de ejecución:

- `in_progress`: El servidor está ejecutando la interacción de forma activa (como ejecutar código o investigar).
- `requires_action`: La interacción se pausó y está esperando la entrada del cliente (como confirmar la ejecución de una herramienta o responder una pregunta).
- `completed`: La interacción finalizó correctamente y el resultado está disponible.
- `failed`: Se produjo un error durante la ejecución (como una falla de la herramienta o límites de frecuencia).
- `cancelled`: Una solicitud del cliente detuvo la ejecución.

### Casos de uso

Usa la ejecución en segundo plano para lo siguiente:

- **Ejecuciones de agentes:** Tareas que requieren ejecución de código, navegación web o coordinación de agentes secundarios (como `antigravity-preview-05-2026`).
- **Investigación exhaustiva:** Ejecuciones con `deep-research-preview-04-2026` o `deep-research-max-preview-04-2026` que tardan varios minutos.
- **Razonamiento extenso:** Tareas en las que los pasos de pensamiento del modelo superan los límites de conexión HTTP estándar.

## Recupera resultados

Obtén resultados de la interacción en segundo plano con **sondeo** o **transmisión**.

### Patrón de sondeo (sin bloqueo)

El sondeo verifica el estado de la interacción de forma periódica con solicitudes GET sin bloqueo hasta que alcanza un estado terminal.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.get(id="YOUR_INTERACTION_ID")

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.get("YOUR_INTERACTION_ID");

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

if (interaction.status === "completed") {
    console.log(interaction.output_text);
} else {
    console.log(`Finished with status: ${interaction.status}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### Patrón de transmisión

Si una interrupción de la red desconecta una transmisión, esta puede reanudarse desde el último evento recibido. Cada delta contiene un `event_id` único en su carga útil. Si pasas este ID como `last_event_id`, se reanuda la transmisión desde ese evento.

### Python

```
import time
from google import genai

client = genai.Client()
interaction_id = "YOUR_INTERACTION_ID"

def stream_with_reconnect(interaction_id: str):
    last_event_id = None
    while True:
        try:
            # Retrieve the stream. If resuming, pass last_event_id
            stream = client.interactions.get(
                id=interaction_id,
                stream=True,
                last_event_id=last_event_id
            )

            for event in stream:
                # Log event updates and capture event_id if present
                if event.event_id:
                    last_event_id = event.event_id

                if event.event_type == "step.delta" and event.delta.type == "text":
                    print(event.delta.text, end="", flush=True)

                if event.event_type == "interaction.completed":
                    return

        except Exception as e:
            print(f"\n[Connection lost: {e}. Reconnecting in 3s...]")
            time.sleep(3)

stream_with_reconnect(interaction_id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const interactionId = "YOUR_INTERACTION_ID";

async function streamWithReconnect(id) {
    let lastEventId = undefined;
    while (true) {
        try {
            // Retrieve the stream. If resuming, pass last_event_id in options
            const stream = await client.interactions.get(id, {
                stream: true,
                last_event_id: lastEventId
            });

            for await (const event of stream) {
                // Capture event_id if present
                const idVal = event.event_id || event.id;
                if (idVal) {
                    lastEventId = idVal;
                }

                if (event.event_type === "step.delta" && event.delta?.type === "text") {
                    process.stdout.write(event.delta.text);
                }

                if (event.event_type === "interaction.completed") {
                    return;
                }
            }
        } catch (error) {
            console.log(`\n[Connection lost: ${error.message}. Reconnecting in 3s...]`);
            await new Promise(resolve => setTimeout(resolve, 3000));
        }
    }
}

await streamWithReconnect(interactionId);
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## Conversaciones de varios turnos

Las interacciones posteriores se pueden encadenar a una conversación en segundo plano con `previous_interaction_id`, sujeto a estas restricciones:

1. **Se bloquean las ejecuciones activas:** Si se encadena una interacción posterior a una con el estado `in_progress`, se muestra un error `400 Bad Request`. Espera a que la interacción alcance el estado `completed` antes de iniciar la siguiente.
2. **Parámetro de entorno para agentes administrados:** Cuando se encadenan interacciones para agentes administrados (como `antigravity-preview-05-2026`), las solicitudes deben incluir `previous_interaction_id` y `environment`.

En los siguientes ejemplos, se muestra cómo encadenar interacciones:

### Python

```
import time
from google import genai

client = genai.Client()
agent_model = "antigravity-preview-05-2026"

# First interaction: Provision sandbox environment and execute first instruction
interaction1 = client.interactions.create(
    model=agent_model,
    input="Create a folder named project/ and write hello.py inside.",
    environment="remote",
    background=True
)

# Wait for completion
while True:
    check = client.interactions.get(id=interaction1.id)
    if check.status != "in_progress":
        break
    time.sleep(2)

# Second interaction: Chain using previous_interaction_id and environment
interaction2 = client.interactions.create(
    model=agent_model,
    input="List all files in the project/ directory.",
    previous_interaction_id=interaction1.id,
    environment="remote",
    background=True
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const agentModel = "antigravity-preview-05-2026";

// First interaction: Provision sandbox environment and execute first instruction
const interaction1 = await client.interactions.create({
    model: agentModel,
    input: "Create a folder named project/ and write hello.py inside.",
    environment: "remote",
    background: true
});

// Wait for completion
while (true) {
    const check = await client.interactions.get(interaction1.id);
    if (check.status !== "in_progress") {
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// Second interaction: Chain using previous_interaction_id and environment
const interaction2 = await client.interactions.create({
    model: agentModel,
    input: "List all files in the project/ directory.",
    previous_interaction_id: interaction1.id,
    environment: "remote",
    background: true
});
```

### REST

```
# Chain second interaction (Make sure FIRST_INTERACTION_ID has status 'completed')
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "antigravity-preview-05-2026",
    "input": "List all files in the project/ directory.",
    "previous_interaction_id": "FIRST_INTERACTION_ID",
    "environment": "remote",
    "background": true
  }'
```

## Cancelación y eliminación

Controla las ejecuciones en curso y administra el almacenamiento con solicitudes de cancelación y eliminación:

- **Cancelar (`POST /interactions/{id}/cancel`):** Detiene la tarea en ejecución. El estado pasa a `cancelled`. Las acciones de limpieza en el servidor pueden causar una pequeña demora antes de que se actualice el estado en las solicitudes GET.
- **Borrar (`DELETE /interactions/{id}`):** Quita los registros de interacción del servidor. Las solicitudes GET posteriores muestran un error `404 Not Found`.

### Python

```
from google import genai

client = genai.Client()

# Cancel a running interaction
client.interactions.cancel(id="YOUR_INTERACTION_ID")

# Delete the interaction record entirely
client.interactions.delete(id="YOUR_INTERACTION_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Cancel a running interaction
await client.interactions.cancel("YOUR_INTERACTION_ID");

// Delete the interaction record entirely
await client.interactions.delete("YOUR_INTERACTION_ID");
```

### REST

```
# Cancel the interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID/cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"

# Delete the interaction
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## Próximos pasos

- Lee la [descripción general de la API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) para comprender la administración de sesiones y estados.
- Consulta la guía de [interacciones de transmisión](https://ai.google.dev/gemini-api/docs/streaming?hl=es-419) para obtener detalles sobre las actualizaciones de eventos en tiempo real.
- Explora el [inicio rápido de agentes administrados](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=es-419) para compilar agentes de varios turnos con estado.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-30 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-30 (UTC)"],[],[]]
