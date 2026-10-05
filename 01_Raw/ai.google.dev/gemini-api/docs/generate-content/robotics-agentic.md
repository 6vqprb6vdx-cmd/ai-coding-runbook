---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=es-419
fetched_at: 2026-10-05T06:31:22.581448+00:00
title: "Capacidades de visi\u00f3n de agente \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=es-419)

Enviar comentarios

# Capacidades de visión de agente

Los modelos ER de Gemini Robotics pueden escribir y ejecutar código de Python para manipular imágenes y aplicar lógica antes de responder. En esta página, se incluyen ejemplos de ejecución de código: detección de objetos con zoom y recorte, lectura de instrumentos, medición de fluidos, lectura de placas de circuitos y anotación de imágenes.

Para adaptar estos ejemplos a tu caso de uso, reemplaza el texto de la instrucción y el archivo de imagen subido por los tuyos. También puedes ajustar el esquema JSON solicitado en la instrucción para que coincida con la estructura de salida que necesita tu aplicación o agregar una `system_instruction` para aplicar el formato y la precisión de la salida.

Para obtener el código ejecutable completo, consulta el
[libro de recetas de Robotics](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Nivel de pensamiento

Puedes controlar el nivel de pensamiento para intercambiar latencia por precisión. Las tareas espaciales, como la detección de objetos, funcionan bien con un nivel de pensamiento bajo. Las tareas complejas, como el recuento o la estimación de peso, se benefician de un nivel de pensamiento más alto.

En el siguiente ejemplo, se establece el nivel de pensamiento en `high` para una tarea de recuento compleja:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('scene.jpeg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        "Identify and count all objects on the table."
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    )
)

print(response.text)
```

Consulta [Pensamiento](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=es-419) para obtener más detalles.

## Detección de objetos (zoom y recorte)

En el siguiente ejemplo, se muestra cómo usar la ejecución de código para acercar y recortar una imagen para obtener una vista más clara cuando se detectan objetos y se muestran cuadros delimitadores.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Return JSON in the format {label: val, y: val, x: val, y2: val, x2: val} for
the compostable objects in this scene. Please Zoom and crop the image for a
clearer view. Return an annotated image of the final result with the bounding
boxes drawn on it to the API caller as a part of your process.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

El resultado del modelo sería similar a la siguiente respuesta JSON:

```
[
  {"label": "compostable", "y": 256, "x": 482, "y2": 295, "x2": 546},
  {"label": "compostable", "y": 317, "x": 478, "y2": 350, "x2": 542},
  {"label": "compostable", "y": 586, "x": 556, "y2": 668, "x2": 595},
  {"label": "compostable", "y": 463, "x": 669, "y2": 511, "x2": 718},
  {"label": "compostable", "y": 178, "x": 565, "y2": 250, "x2": 609}
]
```

En la siguiente imagen, se muestran los cuadros que muestra el modelo.

![Ejemplo que muestra los cuadros de límite de los objetos encontrados](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-bounding-boxes.png?hl=es-419)

## Leer un indicador analógico y aplicar lógica

En el siguiente ejemplo, se muestra cómo usar el modelo para leer un indicador analógico y realizar cálculos de tiempo. Usa una instrucción del sistema para aplicar una salida JSON.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('gauge.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read the current value from this gauge. Then, calculate how long
        it will take at the current rate for the value to reach maximum.
        Reply in JSON: {"current_value": val, "max_value": val,
        "time_to_max_minutes": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## Medir el fluido en un contenedor

En el siguiente ejemplo, se muestra cómo usar la ejecución de código para medir el nivel de fluido en un contenedor.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('fluid.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Measure the amount of fluid in the container. Reply in JSON:
        {"fluid_level_ml": val, "container_capacity_ml": val,
        "percentage_full": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## Leer marcas en una placa de circuitos

En el siguiente ejemplo, se muestra cómo usar la ejecución de código para leer las marcas en una placa de circuitos.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('circuit_board.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read all visible component labels and markings on this circuit
        board. Reply in JSON: {"components": [{"label": val,
        "location": [y, x]}]}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

![Ejemplo que muestra marcas en una placa de circuito](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-circuit-board.png?hl=es-419)

## Anotación de la imagen

En el siguiente ejemplo, se muestra cómo usar la ejecución de código para anotar una imagen (p.ej., dibujar flechas para las instrucciones de eliminación) y mostrar la imagen modificada.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Look at this image and return it as an annotated version using arrows of
different colors to represent which items should go in which bins for
disposal. You must return the final image to the API caller.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

A continuación, se muestra un ejemplo de entrada de imagen.

![Un ejemplo que muestra un reloj para leer](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-image-annotation.png?hl=es-419)

El resultado del modelo sería similar al siguiente:

```
  The annotated image shows the suggested disposal locations for the items on the table:
  - **Green bin (Compost/Organic)**: Green chili, red chili, grapes, and cherries.
  - **Blue bin (Recycling)**: Yellow crushed can and plastic container.
  - **Black bin (Trash)**: Chocolate bar wrapper, Welch's packet, and white tissue.
```

## ¿Qué sigue?

- [Orquestación de tareas](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=es-419): tareas de largo plazo con APIs de robot personalizadas
- [Robótica con transmisión](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=es-419): transmisión bidireccional en tiempo real (solo Gemini Robotics ER 2).
- [Comprensión de video](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=es-419): búsqueda de momentos y clasificación de progreso (solo Gemini Robotics ER 2)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-08 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-08 (UTC)"],[],[]]
