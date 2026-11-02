---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=es-419
fetched_at: 2026-11-02T07:27:39.582934+00:00
title: "Pr\u00e1cticas recomendadas para la API de Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Prácticas recomendadas para la API de Live

En esta guía, se describen las prácticas recomendadas que puedes seguir para optimizar el uso de la API de Live.
Consulta la página [Comienza a usar la API de Live](https://ai.google.dev/gemini-api/docs/live?hl=es-419) para obtener una descripción general y un código de muestra para casos de uso comunes.

## Diseña instrucciones claras del sistema

Para obtener el mejor rendimiento de la API en vivo, te recomendamos que tengas un conjunto claramente definido de instrucciones del sistema (SI) que definan el arquetipo del agente, las reglas de conversación y los parámetros de protección, en este orden.

Para obtener los mejores resultados, separa cada agente en un SI distinto.

1. **Especifica el arquetipo del agente:** Proporciona detalles sobre el nombre, el rol y las características preferidas del agente. Si quieres especificar el acento, asegúrate de indicar también el idioma de salida preferido (por ejemplo, un acento británico para un hablante de inglés).
2. **Especifica las reglas de conversación:** Coloca estas reglas en el orden en que esperas que el modelo las siga. Delimita los elementos únicos de la conversación y los bucles conversacionales. Por ejemplo:

   - **Elemento único:** Recopila los detalles de un cliente una sola vez (como el nombre, la ubicación o el número de tarjeta de lealtad).
   - **Bucle conversacional:** El usuario puede hablar sobre recomendaciones, precios, devoluciones y entregas, y puede querer pasar de un tema a otro. Permite que el modelo sepa que puede participar en este ciclo conversacional durante el tiempo que el usuario desee.
3. **Especifica las llamadas a herramientas dentro de un flujo en oraciones distintas:** Por ejemplo, si un paso único para recopilar los detalles de un cliente requiere invocar una función `get_user_info`, puedes decir: *El primer paso es recopilar la información del usuario. Primero, pídele al usuario que proporcione su nombre, ubicación y número de tarjeta de lealtad. Luego, invoca `get_user_info` con estos detalles.*
4. **Agrega las medidas de protección necesarias:** Proporciona las medidas de protección generales de conversación que no quieres que realice el modelo. No dudes en proporcionar ejemplos específicos de si sucede *x*, quieres que el modelo haga *y*. Si aún no obtienes el nivel de precisión deseado, usa la palabra *inequívocamente* para guiar al modelo y que sea preciso.

## Define herramientas con precisión

Cuando uses herramientas con la API en vivo, sé específico en las definiciones de las herramientas.
Asegúrate de indicarle a Gemini en qué condiciones se debe invocar una llamada a la herramienta. Para obtener más detalles, consulta [Definiciones de herramientas](#tool-definitions-example) en la sección de ejemplos.

## Crea instrucciones eficaces

- **Usa instrucciones claras:** Proporciona ejemplos de lo que los modelos deben y no deben hacer en las instrucciones, y trata de limitar las instrucciones a una por arquetipo o rol a la vez. En lugar de usar instrucciones largas de varias páginas, considera usar el encadenamiento de instrucciones. El modelo funciona mejor en tareas con llamadas a función únicas.
- **Proporciona comandos e información iniciales:** La API de Live espera la entrada del usuario antes de responder. Para que la API de Live inicie la conversación, incluye una instrucción que le pida que salude al usuario o que comience la conversación. Incluye información sobre el usuario para que la API de Live personalice el saludo.

## Especifica el idioma

Los modelos de audio de la API de Live detectan y se adaptan automáticamente al idioma hablado del usuario sin necesidad de un código de idioma explícito.

Si quieres que el modelo responda en un idioma específico, incluye una instrucción como parte de las instrucciones del sistema:

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## Transmisión

Cuando implementes audio en tiempo real, sigue estas prácticas recomendadas:

- **Tamaño del fragmento y latencia**: Envía audio en fragmentos de 20 ms a 40 ms.
- **Control de interrupciones**: Cuando el usuario habla mientras el modelo responde, el servidor envía un mensaje `server_content` con `"interrupted": true`. Debes descartar de inmediato el búfer de audio del cliente para evitar que el agente siga hablando por encima del usuario.

## Administración del contexto

Usa `ContextWindowCompressionConfig` para sesiones largas, ya que los tokens de audio nativos se acumulan rápidamente (aproximadamente 25 tokens por segundo de audio).

## Almacenamiento en búfer del cliente

No almacenes en búfer el audio de entrada de forma significativa (por ejemplo, 1 segundo) antes de enviarlo. Envía fragmentos pequeños (de 20 a 100 ms) para minimizar la latencia.

## Reproducción de muestras

Asegúrate de que tu aplicación cliente vuelva a muestrear la entrada del micrófono (a menudo, 44.1 kHz o 48 kHz) a 16 kHz antes de la transmisión.

## Administración de las sesiones

Sigue estos lineamientos para controlar el ciclo de vida de la sesión y garantizar una experiencia del usuario confiable:

- **Habilita la compresión de la ventana de contexto:** Los tokens de audio se acumulan a aproximadamente 25 tokens por segundo. Sin compresión, las sesiones solo de audio se limitan a 15 minutos y las sesiones de audio y video, a 2 minutos. Habilita la [compresión de la ventana de contexto](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=es-419#context-window-compression) para extender las sesiones a una duración ilimitada.
- **Implementa la reanudación de la sesión:** Es posible que el servidor restablezca periódicamente la conexión de WebSocket. Usa la [reanudación de sesión](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=es-419#session-resumption) para volver a conectarte sin problemas y sin perder el contexto. Conserva el token de reanudación más reciente de los mensajes de `SessionResumptionUpdate` y pásalo como identificador cuando te vuelvas a conectar. Los tokens de reanudación son válidos durante 2 horas después de que finaliza la última sesión.
- **Controla los mensajes GoAway:** El servidor envía un mensaje [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=es-419#goaway-message) antes de finalizar una conexión. Escucha este mensaje y usa el campo `timeLeft` para finalizar o restablecer la conexión correctamente antes de que se cierre.
- **Controla los indicadores de generationComplete:** Usa el mensaje [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=es-419#generation-complete-message) para saber cuándo el modelo terminó de generar una respuesta, de modo que tu aplicación pueda actualizar su IU o continuar con la siguiente acción.

Para obtener detalles sobre la implementación, consulta [Administración de sesiones](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=es-419).

## Ejemplos

En este ejemplo, se combinan las prácticas recomendadas y los [lineamientos para el diseño de instrucciones del sistema](#system-instruction-guidelines) para guiar el rendimiento del modelo como asesor profesional.

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### Definiciones de herramientas

Este JSON define las funciones pertinentes que se llaman en el ejemplo del asesor profesional.
Para obtener los mejores resultados cuando definas funciones, incluye sus nombres, descripciones, parámetros y condiciones de invocación.

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

## Precios y facturación

La API de Gemini Live se factura estrictamente según el uso de tokens. Debido a que la API de Live mantiene una sesión de WebSocket persistente, la facturación sigue un modelo compuesto basado en la ventana de contexto activa.

### La ventana de contexto de la sesión (costos compuestos)

La API te cobra por turno por todos los tokens presentes en la ventana de contexto de la sesión. Un "turno" se define como una entrada del usuario y la respuesta correspondiente del modelo.

- **Acumulación:** La ventana de contexto incluye tokens nuevos del turno actual y todos los tokens acumulados de los turnos anteriores.
- **Refacturación:** Los tokens anteriores se vuelven a procesar y se tienen en cuenta en cada turno nuevo, hasta el tamaño de la ventana de contexto configurada. A medida que se alarga una sesión, aumenta el costo por turno porque se vuelve a procesar el historial de conversación.

### Tokens de audio y transcripciones

La API de Live es multimodal de forma nativa. Conserva el historial de conversación como tokens de audio sin procesar para preservar el tono y los matices acústicos.

- **Facturación de audio:** La API te factura los tokens de audio nativos acumulados a la tarifa estándar de entrada de audio en cada turno.
- **Cargo adicional por transcripción:** Cuando se habilita la transcripción de audio a texto (`inputAudioTranscription` o `outputAudioTranscription`), la API cobra todos los tokens de texto generados para la transcripción a la tarifa de salida de tokens de texto, además de los costos estándar de los tokens de audio.

### Administra los costos con límites de contexto

Para evitar el crecimiento ilimitado de los costos en sesiones largas, configura el tamaño de la ventana de contexto con `contextWindowCompression`.

Si estableces un activador de compresión (p.ej., 25,000 tokens) y una ventana deslizante (p.ej., 8,000 tokens), la API expulsa automáticamente los tokens más antiguos una vez que se alcanza el umbral. Luego, la API factura los turnos posteriores solo por el historial retenido y los tokens nuevos.

### Audio proactivo

Cuando se habilita el audio proactivo, la API cobra los tokens de entrada durante todo el tiempo que la API de Live está escuchando y cobra los tokens de salida solo cuando la API responde.

- **Nota para Gemini 3.8:** El audio proactivo está habilitado de forma permanente en `gemini-3.8-live` y `gemini-3.8-live-extended-thinking`.
- **Nota para Gemini 3.1:** El audio proactivo no es compatible con `gemini-3.1-flash-live-preview`. En este modelo, la API solo factura el audio cuando transmites activamente la entrada.

Para obtener información detallada sobre los precios, consulta la [página de precios de la API de Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-17 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-17 (UTC)"],[],[]]
