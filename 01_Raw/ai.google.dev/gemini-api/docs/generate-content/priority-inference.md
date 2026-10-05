---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=es-419
fetched_at: 2026-10-05T06:37:58.869443+00:00
title: "Inferencia de prioridad \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=es-419)

Enviar comentarios

# Inferencia de prioridad

Descripción: Obtén información para optimizar la latencia con el nivel de
inferencia Priority

La API de Gemini Priority es un nivel de inferencia premium diseñado para cargas de trabajo fundamentales para el negocio que requieren una latencia más baja y la mayor confiabilidad a un precio premium. El tráfico del nivel Priority tiene prioridad sobre el tráfico de la API estándar y el nivel Flexible.

La inferencia Priority está disponible para los usuarios de [los niveles 2 y 3](https://ai.google.dev/gemini-api/docs/billing?hl=es-419#about-billing) en los extremos de la API de GenerateContent
y la API de Interactions.

## Cómo usar Priority

Para usar el nivel Priority, establece el campo `service_tier` en el cuerpo de la solicitud en `priority`. El nivel predeterminado es estándar si se omite el campo.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.6-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
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
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## Cómo funciona la inferencia Priority

La inferencia Priority enruta las solicitudes a colas de procesamiento de alta criticidad, lo que ofrece un rendimiento predecible y rápido para las aplicaciones orientadas al usuario. Su mecanismo principal es una degradación correcta del servidor al procesamiento estándar para el tráfico que excede los límites dinámicos, lo que garantiza la estabilidad de la aplicación en lugar de fallar la solicitud.

| Función | Priority | Estándar | Flexible | Lote |
| --- | --- | --- | --- | --- |
| **Precios** | Entre un 75% y un 100% más que el nivel Estándar | Precio completo | 50% de descuento | 50% de descuento |
| **Latencia** | Segundos | De segundos a minutos | Minutos (objetivo de 1 a 15 min) | Hasta 24 horas |
| **Confiabilidad** | Alta (no se puede descartar) | Alta / media alta | Mejor esfuerzo (se puede descartar) | Alta (para la capacidad de procesamiento) |
| **Interface** | Síncrona | Síncrona | Síncrona | Asíncrona |

### Ventajas clave

- **Latencia baja**: Diseñada para tiempos de respuesta de segundos para herramientas de IA interactivas,
  orientadas al usuario.
- **Alta confiabilidad**: El tráfico se trata con la mayor criticidad y es
  estrictamente no descartable.
- **Degradación elegante**: Los aumentos repentinos de tráfico que exceden los límites dinámicos se degradan automáticamente al nivel Estándar para el procesamiento en lugar de fallar, lo que evita las interrupciones del servicio.
- **Baja fricción**: Usa el mismo método `generateContent` síncrono que los niveles
  Estándar y Flexible.

### Casos de uso

El procesamiento Priority es ideal para flujos de trabajo fundamentales para el negocio en los que el rendimiento y la confiabilidad son primordiales.

- **Aplicaciones de IA interactivas**: Chatbots y copilotos de atención al cliente en los que
  los usuarios pagan un precio premium y esperan respuestas rápidas y coherentes.
- **Motores de decisión en tiempo real**: Sistemas que requieren resultados altamente confiables y de baja latencia
  como la clasificación de tickets en vivo o la detección de fraudes.
- **Funciones premium para clientes**: Desarrolladores que necesitan garantizar objetivos de nivel de servicio (SLO) más altos para los clientes que pagan.

### Límites de frecuencia

El consumo de Priority tiene sus propios límites de frecuencia, aunque el consumo se
cuenta para los [límites de frecuencia generales del tráfico interactivo](https://aistudio.google.com/rate-limit?hl=es-419). Los límites de frecuencia predeterminados para la inferencia Priority son **0.3 veces el límite de frecuencia estándar para el modelo o el nivel**.

### Lógica de degradación correcta

Si se exceden los límites de Priority debido a la congestión, las solicitudes de desbordamiento se degradan **automática y correctamente** al procesamiento Estándar en lugar de fallar con un error 503 o 429. Las solicitudes degradadas se facturan a la tarifa estándar, no a la tarifa premium de Priority.

### Responsabilidad del cliente

- **Supervisión de respuestas**: Los desarrolladores deben supervisar el `x-gemini-service-tier`
  encabezado en la respuesta de la API para detectar si las solicitudes se degradan con frecuencia a
  `standard`.
- **Reintentos**: Los clientes deben implementar la lógica de reintento o la retirada exponencial para los
  errores estándar, como `DEADLINE_EXCEEDED`.

## Precios

La inferencia Priority tiene un precio entre un 75% y un 100% más que la [API estándar](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419) y se factura por token.

## Modelos compatibles

Los siguientes modelos admiten la inferencia Priority:

| Modelo | Inferencia Priority |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=es-419) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=es-419) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=es-419) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=es-419) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=es-419) | ✔️ |

## ¿Qué sigue?

Obtén información sobre las otras opciones de [inferencia y optimización](https://ai.google.dev/gemini-api/docs/optimization?hl=es-419) de Gemini:

- [Inferencia Flexible](https://ai.google.dev/gemini-api/docs/flex-inference?hl=es-419) para una reducción de costos del 50%.
- [API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419) para el procesamiento asíncrono en un plazo de 24 horas.
- [Almacenamiento en caché de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=es-419) para reducir los costos de tokens de entrada.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-12 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-12 (UTC)"],[],[]]
