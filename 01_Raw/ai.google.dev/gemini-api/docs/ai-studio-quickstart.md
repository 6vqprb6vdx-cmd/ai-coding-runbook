---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=es-419
fetched_at: 2026-05-25T13:02:44.987956+00:00
title: "Gu\u00eda de inicio r\u00e1pido de Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Guía de inicio rápido de Google AI Studio

[Google AI Studio](https://aistudio.google.com/?hl=es-419) te permite probar rápidamente
modelos y experimentar con diferentes instrucciones. Cuando estés listo para compilar, puedes seleccionar "Obtener código" y tu lenguaje de programación preferido para usar la [API de Gemini](https://ai.google.dev/gemini-api/docs/quickstart?hl=es-419).

## Instrucciones y configuración

Google AI Studio proporciona varias interfaces para las instrucciones que están diseñadas para diferentes casos de uso. En esta guía, se abordan las **instrucciones de chat**, que se usan para crear
experiencias conversacionales. Esta técnica de instrucciones permite varios turnos de entrada
y respuesta para generar resultados. Puedes obtener más información con nuestro
[ejemplo de instrucción de chat a continuación](#chat_example).
Otras opciones incluyen **transmisión en tiempo real**, **generación de video** y
mucho más.

AI Studio también proporciona el panel **Configuración de ejecución**, en el que puedes realizar
ajustes en los [parámetros del modelo](https://ai.google.dev/docs/prompting-strategies?hl=es-419#model-parameters),
la [configuración de seguridad](https://ai.google.dev/gemini-api/docs/safety-settings?hl=es-419) y activar herramientas como el [resultado estructurado](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419), la [llamada a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419), la [ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) y la [fundamentación](https://ai.google.dev/gemini-api/docs/grounding?hl=es-419).

## Ejemplo de instrucción de chat: Compila una aplicación de chat personalizada

Si usaste un chatbot de uso general como
[Gemini](https://gemini.google.com/?hl=es-419), experimentaste de primera mano lo potentes que pueden ser los modelos de IA
generativa para el diálogo abierto. Si bien estos chatbots de uso general son útiles, a menudo deben adaptarse para casos de uso particulares.

Por ejemplo, tal vez quieras compilar un chatbot de atención al cliente que solo admita conversaciones sobre el producto de una empresa. Es posible que quieras compilar un chatbot que hable con un tono o estilo en particular: un bot que cuente muchos chistes, rime como un poeta o use muchos emojis en sus respuestas.

En este ejemplo, se muestra cómo usar Google AI Studio para compilar un chatbot amigable que se comunica como si fuera un extraterrestre que vive en una de las lunas de Júpiter, Europa.

### Paso 1: Crea una instrucción de chat

Para compilar un chatbot, debes proporcionar ejemplos de interacciones entre un usuario y el chatbot para guiar al modelo para que proporcione las respuestas que buscas.

Para crear una instrucción de chat, haz lo siguiente:

1. Abre [Google AI Studio](https://aistudio.google.com/?hl=es-419). El **Playground** se abrirá de forma predeterminada con una nueva instrucción de chat.
2. Haz clic en **Configuración de ejecución** tune en la esquina superior derecha
   para expandir el panel y ubica el
   [**Instrucciones del sistema**](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419#system-instructions)
   campo de entrada. Pega lo siguiente en el campo de entrada de texto:

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

Después de agregar las instrucciones del sistema, comienza a probar tu aplicación chateando con el modelo:

1. En el cuadro de entrada de texto con la etiqueta **Escribe algo...**, ingresa una pregunta u
   observación que un usuario podría hacer. Por ejemplo:

   **Usuario:**

   ```
   What's the weather like?
   ```
2. Haz clic en el botón **Ejecutar** para obtener una respuesta del chatbot. Esta respuesta puede ser similar a la siguiente:

   **Modelo:**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### Paso 2: Enséñale a tu bot a chatear mejor

Si proporcionas una sola instrucción, puedes compilar un chatbot básico de extraterrestre de Europa. Sin embargo, una sola instrucción puede no ser suficiente para garantizar la coherencia y la calidad en las respuestas del modelo. Sin instrucciones más específicas, la respuesta del modelo a una pregunta sobre el clima tiende a ser muy larga y puede tener su propia opinión.

Para personalizar el tono de tu chatbot, agrega lo siguiente a las instrucciones del sistema:

1. Inicia una nueva instrucción de chat o usa la misma. Las instrucciones del sistema se pueden modificar después de que se inicia la sesión de chat.
2. En la sección **Instrucciones del sistema**, cambia las instrucciones que ya tienes por las siguientes:

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. Vuelve a ingresar tu pregunta (`What's the weather like?`) y haz clic en el botón **Ejecutar**. Si no iniciaste un chat nuevo, tu respuesta podría verse así:

   **Modelo:**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

Puedes usar este enfoque para agregar profundidad adicional al chatbot. Haz más preguntas, edita las respuestas y mejora la calidad de tu chatbot. Sigue agregando o modificando las instrucciones y prueba cómo cambian el comportamiento de tu chatbot.

### Paso 3: Próximos pasos

Al igual que con los otros tipos de instrucciones, una vez que hayas creado un prototipo de tu instrucción a tu satisfacción, puedes usar el botón **Obtener código** para comenzar a programar o guardar la instrucción para trabajar en ella más adelante y compartirla con otras personas.

## Lecturas adicionales

- Si estás listo para pasar al código, consulta los [inicios rápidos
  de la API](https://ai.google.dev/gemini-api/docs/quickstart?hl=es-419).
- Para obtener información sobre cómo crear mejores instrucciones, consulta los [lineamientos
  de diseño de instrucciones](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-12 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-12 (UTC)"],[],[]]
