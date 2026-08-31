---
source_url: https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=es-419
fetched_at: 2026-08-31T06:40:49.548213+00:00
title: "Comprensi\u00f3n de videos \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Comprensión de videos

Gemini Robotics ER 2 puede hacer un seguimiento del progreso de las tareas a partir de transmisiones de video continuas con dos capacidades:

- Búsqueda de momentos: Identifica la marca de tiempo precisa en la que se produce un evento clave.
- Clasificación de progreso: Asigna cada video a uno de los cinco intervalos de finalización (0–20%, 20–40%, 40–60%, 60–80%, 80–100%).

## Búsqueda de momentos

La búsqueda de momentos identifica el fotograma exacto del video en el que se produce un evento crítico, por ejemplo, cuando una taza está llena o se ata un nudo. Los robots usan esto para verificar el éxito, secuenciar los pasos y activar las correcciones.

En la siguiente instrucción de ejemplo, se le pide al modelo que identifique el momento de finalización de una tarea determinada en un video:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

A continuación, se muestran fotogramas de ejemplo de un video de búsqueda de momentos, en el que el modelo identifica la marca de tiempo de finalización de la tarea:

![Ejemplo de fotogramas de video que muestran el resultado de la búsqueda de momentos con una superposición de marca de tiempo](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=es-419)

## Clasificación de progreso

La clasificación de progreso asigna un video a uno de los cinco intervalos de finalización: 0–20%, 20–40%, 40–60%, 60–80% o 80–100%. Esto les brinda a los robots conciencia situacional en tiempo real para que puedan ajustar las acciones o volver a intentar los pasos fallidos sin reiniciar todo el flujo de trabajo.

En la siguiente instrucción de ejemplo, se le pide al modelo que clasifique el nivel de progreso actual de un video:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

A continuación, se muestran fotogramas de ejemplo de un video de clasificación de progreso, en el que el modelo asigna un intervalo de progreso:

![Ejemplo de fotogramas de video que muestran la salida de clasificación de progreso con una etiqueta de corchete de progreso](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=es-419)

## Ejemplos

Para obtener ejemplos ejecutables completos, incluido el seguimiento de tareas de varios pasos, consulta el
[libro de recetas de robótica](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## ¿Qué sigue?

- [API de Live para robótica](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=es-419): Transmisión bidireccional en tiempo real
- [Organización de tareas](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=es-419): Tareas de largo plazo con razonamiento espacial
- [Descripción general de Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=es-419): Comparación de modelos y capacidades

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-30 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-30 (UTC)"],[],[]]
