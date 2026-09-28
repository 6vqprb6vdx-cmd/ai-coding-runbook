---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=es-419
fetched_at: 2026-09-28T06:19:35.739904+00:00
title: "Pensamiento de Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=es-419)

Enviar comentarios

# Pensamiento de Gemini

Los [modelos de las series Gemini 3 y 2.5](https://ai.google.dev/gemini-api/docs/models?hl=es-419) usan un "proceso de pensamiento" interno que mejora significativamente sus capacidades de razonamiento y planificación de varios pasos, lo que los hace muy eficaces para tareas complejas, como programación, matemáticas avanzadas y análisis de datos.

En esta guía, se muestra cómo trabajar con las capacidades de pensamiento de Gemini usando la API de Gemini.

## Genera contenido con razonamiento

Iniciar una solicitud con un modelo de razonamiento es similar a cualquier otra solicitud de generación de contenido. La diferencia clave radica en especificar uno de los [modelos con asistencia para el pensamiento](#supported-models) en el campo `model`, como se demuestra en el siguiente ejemplo de [generación de texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419#text-input):

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: prompt,
  });

  console.log(response.text);
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

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.8-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## Resúmenes de razonamiento

Los resúmenes de pensamientos son versiones resumidas de los pensamientos sin procesar del modelo y ofrecen estadísticas sobre el proceso de razonamiento interno del modelo. Ten en cuenta que los niveles y los presupuestos de pensamiento se aplican a los pensamientos sin procesar del modelo y no a los resúmenes de pensamiento.

Para habilitar los resúmenes de pensamientos, establece `includeThoughts` en `true` en la configuración de tu solicitud. Luego, puedes acceder al resumen iterando el parámetro `response` de `parts` y verificando el valor booleano `thought`.

Este es un ejemplo que muestra cómo habilitar y recuperar resúmenes de pensamientos sin transmisión, lo que devuelve un solo resumen de pensamientos final con la respuesta:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.8-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
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
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

Y aquí tienes un ejemplo de cómo usar el pensamiento con transmisión, que devuelve resúmenes incrementales y continuos durante la generación:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.8-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.8-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
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
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.8-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## Control del pensamiento

De forma predeterminada, los modelos de Gemini participan en el pensamiento dinámico, ya que ajustan automáticamente la cantidad de esfuerzo de razonamiento en función de la complejidad de la solicitud del usuario.
Sin embargo, si tienes restricciones de latencia específicas o necesitas que el modelo realice un razonamiento más profundo de lo habitual, puedes usar parámetros de forma opcional para controlar el comportamiento de pensamiento.

### Niveles de pensamiento (Gemini 3)

El parámetro `thinkingLevel`, recomendado para los modelos de Gemini 3 y posteriores, te permite controlar el comportamiento del razonamiento.

En la siguiente tabla, se detallan los parámetros de configuración de `thinkingLevel` para cada tipo de modelo:

| Nivel de razonamiento | Gemini 3.8 y 3.7 Flash | Gemini 3.6 y 3.5 Flash | Gemini 3.1 Pro | Gemini 3.5 y 3.1 Flash-Lite | Imagen de Gemini 3.1 Flash-Lite | Gemini 3 Flash | Gemini Robotics ER 2 | Descripción |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | No admitido (error) | Admitido | No compatible | Admitido (predeterminado) | Admitido (predeterminado) | Admitido | Admitido | Coincide con el parámetro de configuración "sin razonamiento" para la mayoría de las búsquedas. Ten en cuenta que `minimal` no garantiza que el razonamiento esté desactivado. Es posible que el modelo razone de forma muy mínima para tareas complejas. |
| **`low`** | Admitido | Admitido | Admitido | Admitido | No compatible | Admitido | Admitido | Minimiza la latencia y el costo. |
| **`medium`** | Admitido (predeterminado) | Admitido (predeterminado) | Admitido | Admitido | No compatible | Admitido | Admitido | Pensamiento equilibrado para la mayoría de las tareas. |
| **`high`** | Admitido (dinámico) | Admitido (dinámico) | Admitido (predeterminado, dinámico) | Admitido (dinámico) | Admitido (dinámico) | Admitido (predeterminado, dinámico) | Admitido (predeterminado, dinámico) | Maximiza la profundidad del razonamiento. El modelo puede tardar mucho más en alcanzar un primer token de salida (sin pensar), pero la salida se razonará con más cuidado. |

En el siguiente ejemplo, se muestra cómo establecer el nivel de pensamiento.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

No puedes inhabilitar la función de pensamiento de Gemini 3.1 Pro. Gemini 3 Flash y Flash-Lite tampoco admiten la desactivación completa del pensamiento. Si no especificas un nivel de pensamiento, Gemini usará el nivel de pensamiento predeterminado de los modelos de Gemini 3 (p.ej., `"high"` para Gemini 3.1 Pro y `"medium"` para Gemini 3.5 Flash).

Los modelos de la serie Gemini 2.5 no admiten `thinkingLevel`; usa `thinkingBudget` en su lugar.

### Límites de tokens y `max_output_tokens`

El parámetro de generación [`max_output_tokens`](https://ai.google.dev/api/generate-content?hl=es-419#v1beta.GenerationConfig) establece la cantidad máxima de tokens que puede generar una respuesta, incluidos los tokens de pensamiento.

Cuando se establece, este parámetro actúa como un límite estricto que aplica la infraestructura sin cambiar la forma en que el modelo asigna su presupuesto de pensamiento (`thinking_level`).

Si el modelo alcanza este límite durante el razonamiento, deja de generar contenido con `finish_reason: MAX_TOKENS` y devuelve un resultado truncado o vacío (aunque se sigan facturando los tokens de razonamiento generados). Para reducir el costo o la latencia sin truncar las respuestas, disminuye `thinking_level` (`low` o `medium`) en lugar de establecer un `max_output_tokens` pequeño.

### Presupuestos de pensamiento

El parámetro `thinkingBudget`, que se introdujo con la serie de Gemini 2.5, guía al modelo sobre la cantidad específica de tokens de pensamiento que debe usar para el razonamiento.

A continuación, se incluyen los detalles de configuración de `thinkingBudget` para cada tipo de modelo.
Puedes inhabilitar el pensamiento estableciendo `thinkingBudget` en 0.
Si se establece el valor de `thinkingBudget` en -1, se activa el **pensamiento dinámico**, lo que significa que el modelo ajustará el presupuesto según la complejidad de la solicitud.

| Modelo | Parámetro de configuración predeterminado (no se establece el presupuesto de pensamiento) | Rango | Inhabilitar el pensamiento | Activa el pensamiento dinámico |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Pensamiento dinámico | De `128` a `32768` | N/A: No se puede inhabilitar el pensamiento | `thinkingBudget = -1` (predeterminado) |
| **2.5 Flash** | Pensamiento dinámico | De `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (predeterminado) |
| **Versión preliminar de 2.5 Flash** | Pensamiento dinámico | De `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (predeterminado) |
| **2.5 Flash Lite** | El modelo no piensa | De `512` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Versión preliminar de 2.5 Flash Lite** | El modelo no piensa | De `512` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Versión preliminar de Robotics-ER 1.6** | Pensamiento dinámico | De `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (predeterminado) |
| **Versión preliminar de audio nativo de Live de 2.5 Flash (09-2025)** | Pensamiento dinámico | De `0` a `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (predeterminado) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

Según la instrucción, el modelo podría exceder o no alcanzar el presupuesto de tokens.

## Firmas de razonamiento

La API de Gemini no tiene estado, por lo que el modelo trata cada solicitud a la API de forma independiente y no tiene acceso al contexto de pensamiento de los turnos anteriores en las interacciones de varios turnos.

Para mantener el contexto del pensamiento en las interacciones de varios turnos, Gemini devuelve firmas de pensamiento, que son representaciones encriptadas del proceso de pensamiento interno del modelo.

- Los **modelos de Gemini 2.5** devuelven firmas de pensamiento cuando se habilita el pensamiento y la solicitud incluye [llamadas a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#thinking), específicamente [declaraciones de funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#step-2).
- Los **modelos de Gemini 3** pueden devolver firmas de pensamiento para todos los tipos de [partes](https://ai.google.dev/api/caching?hl=es-419#Part).
  Te recomendamos que siempre pases todas las firmas tal como las recibiste, pero es *obligatorio* para las firmas de llamadas a funciones. Para obtener más información, consulta la página [Firmas de razonamiento](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=es-419).

Otras limitaciones de uso que se deben tener en cuenta con la llamada a funciones incluyen las siguientes:

- Las firmas se devuelven del modelo dentro de otras partes de la respuesta, por ejemplo, llamadas a funciones o partes de texto.
  [Devuelve toda la respuesta](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#step-4) con todas las partes al modelo en los turnos posteriores.
- No concatenes partes con firmas.
- No combines una parte con una firma con otra parte sin firma.

## Precios

Cuando se activa el razonamiento, el precio de la respuesta es la suma de los tokens de salida y los tokens de razonamiento. Puedes obtener la cantidad total de tokens de pensamiento generados en el campo `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

Los modelos de pensamiento generan ideas completas para mejorar la calidad de la respuesta final y, luego, generan [resúmenes](#summaries) para proporcionar información sobre el proceso de pensamiento. Por lo tanto, el precio se basa en los tokens de pensamiento completos que el modelo necesita generar para crear un resumen, a pesar de que solo el resumen se genera desde la API.

Puedes obtener más información sobre los tokens en la guía [Recuento de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419).

## Prácticas recomendadas

En esta sección, se incluye orientación para usar los modelos de pensamiento de manera eficiente.
Como siempre, si sigues nuestra [orientación y prácticas recomendadas para generar instrucciones](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=es-419), obtendrás los mejores resultados.

### Depuración y dirección

- **Revisa el razonamiento**: Cuando no obtengas la respuesta esperada de los modelos de pensamiento, puede ser útil analizar cuidadosamente los resúmenes de pensamiento de Gemini.
  Puedes ver cómo desglosó la tarea y llegó a su conclusión, y usar esa información para corregir los resultados.
- **Proporciona orientación en el razonamiento**: Si esperas una respuesta particularmente extensa, es posible que desees proporcionar orientación en tu instrucción para limitar la [cantidad de razonamiento](#set-budget) que usa el modelo. Esto te permite reservar más de la salida del token para tu respuesta.

### Complejidad de la tarea

- **Tareas fáciles (el pensamiento podría estar DESACTIVADO):** Para las solicitudes sencillas en las que no se requiere un razonamiento complejo, como la recuperación de hechos o la clasificación, no se requiere pensamiento. Los siguientes son algunos ejemplos:
  - "¿Dónde se fundó DeepMind?"
  - "¿Este correo electrónico solicita una reunión o solo proporciona información?"
- **Tareas medianas (predeterminadas/algo de pensamiento):** Muchas solicitudes comunes se benefician de un cierto grado de procesamiento paso a paso o de una comprensión más profunda. Gemini puede usar de forma flexible su capacidad de pensamiento para tareas como las siguientes:
  - Comparar la fotosíntesis con el crecimiento
  - Compara y contrasta los autos eléctricos y los autos híbridos.
- **Tareas difíciles (máxima capacidad de pensamiento):** Para desafíos realmente complejos, como resolver problemas matemáticos complejos o tareas de programación, recomendamos establecer un presupuesto de pensamiento alto. Estos tipos de tareas requieren que el modelo utilice todas sus capacidades de razonamiento y planificación, lo que a menudo implica muchos pasos internos antes de proporcionar una respuesta. Los siguientes son algunos ejemplos:
  - Resuelve el problema 1 de AIME 2025: Encuentra la suma de todas las bases enteras b > 9 para las que 17b es un divisor de 97b.
  - Escribe código de Python para una aplicación web que visualice datos del mercado de valores en tiempo real, incluida la autenticación del usuario. Haz que sea lo más eficiente posible.

## Modelos, herramientas y capacidades compatibles

Las funciones de pensamiento son compatibles con todos los modelos de las series 3 y 2.5.
Puedes encontrar todas las capacidades del modelo en la página de [descripción general del modelo](https://ai.google.dev/gemini-api/docs/models?hl=es-419).

Los modelos de pensamiento funcionan con todas las herramientas y capacidades de Gemini. Esto permite que los modelos interactúen con sistemas externos, ejecuten código o accedan a información en tiempo real, y que incorporen los resultados a su razonamiento y respuesta final.

Puedes probar ejemplos de uso de herramientas con modelos de pensamiento en el [Recetario de pensamiento][Colab].

## Próximos pasos

- La cobertura de Thinking está disponible en nuestra guía de [compatibilidad con OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=es-419#thinking).

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-25 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-25 (UTC)"],[],[]]
