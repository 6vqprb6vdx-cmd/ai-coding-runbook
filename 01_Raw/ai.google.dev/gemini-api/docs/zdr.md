---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=es-419
fetched_at: 2026-09-28T06:14:55.300440+00:00
title: "Retenci\u00f3n de datos cero en la API de Gemini Developer \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Retención de datos cero en la API de Gemini Developer

En esta página, se describen los detalles de lo que comúnmente se conoce como "cero retención de datos" en la API de Gemini para desarrolladores.

## Restricción para el entrenamiento

Como se describe en las [Condiciones del Servicio de la API de Gemini](https://ai.google.dev/gemini-api/terms?hl=es-419), cuando usas los Servicios Pagados, Google no utiliza tus instrucciones (incluidas las instrucciones del sistema asociadas, el contenido almacenado en caché y los archivos, como imágenes, videos o documentos) ni las respuestas para mejorar nuestros productos. Los Servicios Pagados se definen [aquí](https://ai.google.dev/gemini-api/terms?hl=es-419#paid-services).

## Retención de datos del cliente y logro de la retención cero de datos

Por lo general, los datos de los clientes se retienen durante períodos limitados en las siguientes situaciones y condiciones. Para lograr la retención cero de datos, los clientes deben realizar acciones específicas o evitar funciones específicas en cada una de estas áreas:

- **Registro de instrucciones para la supervisión del abuso**: Como se describe en las [Condiciones del Servicio Adicionales de la API de Gemini](https://ai.google.dev/gemini-api/terms?hl=es-419), para los Servicios Pagados, Google registra las instrucciones y las respuestas durante un período limitado únicamente para detectar incumplimientos de la [Política de Uso Prohibido](https://policies.google.com/terms/generative-ai/use-policy?hl=es-419). Si tu carga de trabajo requiere una retención de datos garantizada de cero o acuerdos de procesamiento de datos empresariales, usa Vertex AI. Para obtener más información, consulta [Gemini Enterprise Agent Platform y retención de datos cero](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=es-419).
- **Fundamentación con la Búsqueda de Google**: Como se describe en las [Condiciones del Servicio Adicionales de la API de Gemini](https://ai.google.dev/gemini-api/terms?hl=es-419#grounding-with-google-search), Google almacena las instrucciones, la información contextual y el resultado generado durante treinta (30) días para crear resultados fundamentados y sugerencias de búsqueda.
  Esta información almacenada se puede usar para depurar y probar los sistemas que admiten la fundamentación. **No hay forma de inhabilitar el almacenamiento de esta información si usas la Fundamentación con la Búsqueda de Google.**
- **Fundamentación con Google Maps**: Como se describe en las [Condiciones del Servicio Adicionales de la API de Gemini](https://ai.google.dev/gemini-api/terms?hl=es-419), Google almacena las instrucciones, la información contextual y el resultado generado durante treinta (30) días para crear resultados fundamentados. Esta información almacenada solo se puede usar para la ingeniería de confiabilidad, como la depuración en caso de problemas con el servicio.
  **No hay forma de inhabilitar el almacenamiento de esta información si usas Fundamentación con Google Maps.**
- **API de Interactions**: La API de Interactions administra el estado activo de una conversación para habilitar turnos de varios turnos. **De forma predeterminada, la API de Interactions habilita el almacenamiento de estado**. Para garantizar que no se deje ningún rastro de datos, debes establecer de forma explícita el parámetro `store` en `false` en tus solicitudes a la API para inhabilitar la retención del estado predeterminado.
- **API de Live**: Esta API con estado permite la reconexión en tiempo real almacenando el estado de la conversación. Para lograr la retención cero de datos, **no configures SessionResumptionConfig**. Si se genera un identificador de sesión, el estado de la conversación (incluidos el texto, el audio y el video) se retiene durante un máximo de 24 horas.
- **Almacenamiento de la API de File**: La API de File permite a los usuarios subir recursos grandes.
  Los archivos se almacenan en reposo hasta que el usuario los borra o hasta que vencen.
  El uso de la API de File es independiente del registro de ZDR. Los usuarios deben borrar los archivos de forma manual para garantizar que no queden rastros de datos.
- **Almacenamiento en caché de contexto explícito**: Los usuarios pueden almacenar en caché manualmente conjuntos de datos grandes (p.ej., videos largos o bibliotecas de documentos) con el campo `cached_content`. Si bien los registros de estas solicitudes siguen las políticas de descarte de ZDR, el contexto almacenado en caché se almacena con un `ttl` o `expire_time` definido por el usuario. Para lograr una huella de datos absoluta de cero, no utilices la función cached\_content.
- **Almacenamiento en caché implícito en memoria**: De forma predeterminada, los modelos de Gemini almacenan datos en caché en la memoria para reducir la latencia y los costos para los desarrolladores. Estos datos se encuentran estrictamente en la RAM (no en reposo), están aislados a nivel del proyecto y tienen un TTL de 24 horas.
  **Esto no incumple la política de retención de datos cero.**

## ¿Qué sigue?

- Obtén más información sobre la [Política de Uso Prohibido de IA Generativas](https://policies.google.com/terms/generative-ai/use-policy?hl=es-419).
- Revisa las [Condiciones del Servicio Adicionales de la API de Gemini](https://ai.google.dev/gemini-api/terms?hl=es-419).
- Si necesitas controles de ZDR de autoservicio y nivel empresarial, consulta la [guía de retención cero de datos de Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-16 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-16 (UTC)"],[],[]]
