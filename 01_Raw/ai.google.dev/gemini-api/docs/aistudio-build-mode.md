---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=es-419
fetched_at: 2026-09-21T06:00:40.167283+00:00
title: "Crea apps en Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Crea apps en Google AI Studio

En esta página, se describe cómo usar Google AI Studio para compilar rápidamente (o "vibe
code") y, luego, implementar apps que prueben las capacidades más recientes de Gemini, como
[Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419) y la [API
de Live](https://ai.google.dev/gemini-api/docs/live?hl=es-419). Google AI Studio admite la compilación de **apps web** con entornos de ejecución full-stack y **apps nativas para Android** con Kotlin y Jetpack Compose, todo a través de instrucciones en lenguaje natural.

## Comenzar

Comienza a usar el vibe coding en el [modo Build](https://aistudio.google.com/apps?hl=es-419) de Google AI Studio. Puedes comenzar a compilar de varias maneras:

- **Comienza con una instrucción**: En el modo Build, usa la casilla de entrada para ingresar una
  descripción de lo que quieres compilar. Selecciona AI Chips para agregar funciones específicas, como la generación de imágenes o los datos de Google Maps, a tu instrucción. Incluso puedes decir lo que quieres con el botón de voz a texto.
- **Botón "Voy a tener suerte"**: Si necesitas inspiración creativa, usa el botón "Voy a
  tener suerte" y Gemini generará una instrucción con una idea de proyecto
  para que comiences.
- **Remezcla un proyecto de la galería**: Abre un proyecto de la [Galería
  de apps](https://aistudio.google.com/apps?source=showcase&hl=es-419) y selecciona **Copiar app**.
- **Importa un proyecto desde GitHub**: En el modo Build, selecciona
  **Importar desde GitHub** en el menú **Agregar archivos** (ícono +) en la casilla de entrada de la instrucción
  para importar tu código existente.

Una vez que ejecutes la instrucción, verás que se generan el código y los archivos necesarios, con una vista previa en vivo de tu app que aparece en el lado derecho.

## ¿Qué se crea?

Cuando ejecutas la instrucción, AI Studio crea una aplicación completa. Puedes elegir compilar una **app web** o una **app para Android nativa** con el selector de plataformas.

En el caso de las **apps web** (opción predeterminada), AI Studio crea un entorno full-stack que incluye lo siguiente:

- **Cliente**: Un frontend web (React es la opción predeterminada).
- **Servidor**: Un entorno de ejecución de Node.js que permite llamadas seguras a la API,
  conexiones de bases de datos y el uso de paquetes npm.

En el caso de las **apps para Android**, AI Studio genera un proyecto de Kotlin y Jetpack Compose
que puedes obtener una vista previa en un emulador basado en el navegador, instalar en un dispositivo físico,
y publicar en Play Store para realizar pruebas. [Obtén más información para compilar apps para Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=es-419).

Para ver el código que se genera, selecciona la pestaña **Código** en el panel de vista previa de la derecha. El **agente de Antigravity** administra de forma inteligente varios archivos en tu pila, lo que garantiza que los cambios se propaguen correctamente.

### El agente de Antigravity

El **agente de Antigravity** es la principal funcionalidad de IA dentro de [Google
Antigravity](https://antigravity.google?hl=es-419), y ahora los componentes principales del
arnés del agente potencian la experiencia del modo Build en Google AI Studio. Va más allá de la simple generación de código, ya que mantiene el contexto de todo el proyecto, administra varios archivos y comprende instrucciones complejas para compilar aplicaciones full-stack sólidas.

Las siguientes son algunas de las funciones clave:

- **Reconocimiento del contexto**: Mantiene el contexto de las instrucciones anteriores y los estados de los archivos.
- **Administración de varios archivos**: Controla las dependencias en varios archivos.
- **Ejecución verificada**: Verifica las actualizaciones de código para reducir las alucinaciones.

## Capacidades full-stack

Google AI Studio libera el poder del ecosistema web moderno, lo que te permite compilar más que solo prototipos del cliente.

- **Entorno de ejecución del servidor y npm**: Usa la amplia biblioteca de paquetes npm. El agente identificará e instalará automáticamente los paquetes según sea necesario para tu app (p.ej., bibliotecas específicas para la visualización de datos o clientes de API). También puedes solicitar paquetes específicos si lo deseas.
- **Administración de secretos**: Almacena de forma segura claves de API y secretos en el
  **menú Configuración**. Se puede acceder a ellos en el código del servidor, lo que los mantiene a salvo de la exposición del cliente.
- **Multijugador**: Crea experiencias colaborativas en tiempo real directamente en
  AI Studio. El entorno de ejecución del servidor administra el estado y las conexiones necesarias para que los usuarios interactúen entre sí.
- **Firebase Firestore y Authentication**: Aprovisiona y configura Firebase automáticamente, incluida la base de datos de Firestore (almacenamiento de datos persistente) y
  Firebase Authentication (flujos de acceso, específicamente "Acceder con
  Google"). El agente controla todo el proceso de configuración e incluso escribe el código en tu app para estos servicios.
- **Integraciones de Google Workspace**: Conecta tu app a las APIs de Google Workspace, como Gmail, Hojas de cálculo, Documentos, Drive, Calendario y mucho más. AI Studio controla automáticamente toda la configuración de OAuth.

[Obtén más información para desarrollar apps full-stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=es-419)

### Apps para Android

También puedes compilar apps nativas para Android con Kotlin y Jetpack Compose.
Obtén una vista previa de tu app en un emulador de Android basado en el navegador, instálala en un dispositivo físico con ADB en el navegador y publícala en Play Store para realizar pruebas internas.

[Obtén más información para compilar apps para Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=es-419)

## Continúa con la compilación

Una vez que Google AI Studio genere el código inicial de tu aplicación, puedes seguir perfeccionándolo:

### Compila en Google AI Studio

- **Itera con Gemini**: Usa el panel de chat en el **modo Build** para pedirle a Gemini
  que realice modificaciones, agregue funciones nuevas o cambie el estilo.
- **Edita el código directamente**: Abre la **pestaña Código** en el panel de vista previa para
  realizar ediciones en vivo.

### Desarrolla externamente

Para flujos de trabajo más avanzados, puedes sincronizar o exportar el código para trabajar en tu entorno preferido:

- **Sincroniza con GitHub**: Conecta tu app a un repositorio de GitHub para habilitar
  la sincronización bidireccional. Puedes enviar los cambios solicitados en AI Studio directamente a tu repositorio con mensajes de confirmación generados por IA o extraer los cambios realizados de forma local en tu IDE o por compañeros de equipo a AI Studio. Administra el estado de sincronización en cualquier momento en la pestaña **GitHub** de Configuración.
- **Descarga y desarrolla de forma local**: Exporta el código generado como un **archivo
  ZIP** y, luego, impórtalo a tu editor de código.

## Características clave

Google AI Studio incluye varias funciones para que el proceso de compilación sea intuitivo y visual:

- **Crea y realiza iteraciones en apps full-stack**: Crea apps full-stack con solo
  una instrucción y realiza iteraciones a través del chat o el **modo de anotación**. El modo de anotación te permite destacar cualquier parte de la IU de tu app y describir el cambio que deseas.
- **Comparte e implementa tu app**: Puedes compartir tus creaciones con otras personas para
  colaborar o mostrar tu trabajo. Cuando compartes, las llamadas a la API se incluyen en tus límites de uso. Si usas modelos pagados, es posible que se apliquen costos. Luego, cuando tu app esté lista, impleméntala en Cloud Run.
- **Galería de apps**: La Galería de apps proporciona una biblioteca visual de ideas de proyectos.
  Puedes explorar lo que es posible con Gemini, obtener una vista previa de las aplicaciones al instante y remezclarlas para hacerlas tuyas.

## Implementa o archiva tu app

Una vez que tu aplicación esté lista, puedes implementarla:

- **Cloud Run**: Implementa tu aplicación como un servicio escalable.
  Es posible que se apliquen precios para [Google Cloud Run](https://cloud.google.com/run?hl=es-419) según el uso. Para obtener más información sobre la implementación, consulta
  [Cómo implementar desde Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=es-419).
- **GitHub**: Sincroniza tu proyecto con un repositorio de GitHub nuevo o existente
  para administrar el código fuente o colaborar con compañeros de equipo.

## Limitaciones

En esta sección, se enumeran las limitaciones actuales del modo Build en Google AI Studio.

### Administración de claves de API

Cuando creas una app nueva que usa la API de Gemini, AI Studio configura automáticamente tu clave de API de Gemini como un secreto en el entorno del servidor de la app.
Puedes ver y administrar esta clave en el panel **Secretos**.

- **Configuración automática**: Tu `GEMINI_API_KEY` está configurada para ti. No se requiere configuración manual
  para comenzar a compilar.
- **Solo del servidor**: Las claves de API se insertan en el entorno de ejecución del servidor y
  nunca se incluyen en el código del cliente.
- **Apps existentes**: En el caso de las apps compiladas antes del 14 de mayo de 2026, el agente actualizará
  automáticamente tu integración de la API de Gemini al enfoque recomendado del
  servidor la próxima vez que modifiques las funciones de Gemini de la app.

### Implementación fuera de Google AI Studio

- **Cloud Run**: Cuando implementas en Cloud Run desde AI Studio, tu clave de API se
  incluye de forma segura en el entorno del servidor. La app implementada usará tu clave de API para todas las llamadas a la API de Gemini de los usuarios.
- **Descarga de ZIP**: Si descargas tu app como un archivo ZIP para ejecutarla
  en otro lugar, deberás configurar la variable de entorno `GEMINI_API_KEY`en tu entorno de hosting. Dado que las llamadas a la API de Gemini de tu app se realizan desde el código del servidor, la clave no se expone a los usuarios finales.

### Error al compartir apps

Si compartes tu app y el usuario final se encuentra con un error **403 Access Restricted** cuando usa la URL compartida, puede deberse a uno de los siguientes motivos:

- **Extensiones del navegador**: Es posible que las extensiones de privacidad, como Privacy Badger, bloqueen la app. Inhabilita la extensión para evitar el error.
- **Problemas de compilación**: Es posible que haya problemas con el código actual. Pídele al agente que "corrija cualquier problema de compilación con el código actual" y, luego, vuelve a compartir la URL.

## Preguntas frecuentes

### ¿Qué es Build en AI Studio?

AI Studio Build es una plataforma diseñada para llevarte de una simple instrucción a una aplicación lista para producción potenciada por IA con Gemini. Describe lo que quieres compilar con una instrucción y Gemini generará una app para ti. También puedes explorar nuestra galería para ver lo que es posible con la API de Gemini y remezclar apps para hacerlas tuyas.

### ¿Cómo controla Build mi clave de API de Gemini?

Cuando creas una app que usa la API de Gemini, AI Studio configura automáticamente tu clave de API de Gemini como un secreto del servidor. Las llamadas a la API de Gemini de tu app se realizan desde el código del servidor con esta clave, por lo que nunca se expone en el navegador. Puedes ver tu clave de API en el panel **Secretos** de Configuración.

### ¿Se expone mi clave de API cuando comparto apps?

No. Tu clave de API se almacena como un secreto del servidor y nunca se incluye en el código del cliente. Cuando compartes tu app, otros usuarios pueden usarla, pero no pueden ver tu clave de API.

Cuando compartes tus apps con otras personas, las llamadas a la API se incluyen en tus límites de uso.
Si usas modelos pagados, es posible que se apliquen costos. AI Studio te avisará durante la configuración y antes de compartir si tu app podría generar costos.

### ¿Quién puede ver mis apps?

De forma predeterminada, tu app es privada. Puedes compartir tu app con otros usuarios para que la usen. Los usuarios con los que compartes tu app pueden ver su código y bifurcarlo para sus propios fines. Si compartes tu app con permiso de edición, los otros usuarios pueden editar el código de tu app.

### ¿Puedo ejecutar apps fuera de AI Studio?

Sí. Puedes implementar tu app en
[Cloud Run](https://cloud.google.com/run?hl=es-419) desde AI Studio, lo que
le otorga una URL pública con tu clave de API configurada de forma segura en el
entorno del servidor. También puedes descargar tu app como un archivo ZIP y alojarla en otro lugar. Deberás configurar la variable de entorno `GEMINI_API_KEY` en tu entorno de hosting. Dado que las llamadas a la API de Gemini se realizan desde el código del servidor, tu clave permanece segura.

Para obtener más información sobre las opciones de implementación, consulta [Cómo implementar desde Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=es-419).

### ¿Puedo desarrollar apps de forma local con mis propias herramientas y, luego, compartirlas aquí?

Sí. Puedes conectar tu app de AI Studio a un repositorio de GitHub para desarrollar de forma local con tu editor de código o herramientas de CLI preferidas, enviar tus cambios a GitHub y, luego, extraer esas actualizaciones directamente a AI Studio con la pestaña **GitHub** de Configuración.

### ¿Cómo puedo usar una base de datos o algún otro almacenamiento con mis apps?

Las apps de AI Studio son apps estándar que se ejecutan en un contenedor de Cloud Run. Puedes usar cualquier solución de almacenamiento a la que puedas conectarte a través de una red, siempre que no haya un firewall que impida el acceso desde un rango de IP dinámico.

Estamos trabajando para agregar compatibilidad directa con el almacenamiento en el futuro, que podrás configurar directamente en AI Studio.

### ¿Cómo puedo acceder al micrófono, la cámara web y otras APIs de Navigator?

Para asegurarnos de que los usuarios estén al tanto del uso que hace una app de su cámara web o de otros
dispositivos, requerimos una confirmación adicional antes de que la app pueda acceder a
estas [APIs de Navigator](https://developer.mozilla.org/en-US/docs/Web/API/Navigator).
Los creadores de apps pueden agregar estas solicitudes de permiso al archivo `metadata.json` de su app. Por ejemplo:

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

Los valores admitidos para `requestFramePermissions` son un subconjunto de las
funciones estándar [controladas por políticas](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md).

### ¿Cómo puedo usar GitHub con mis apps?

AI Studio admite la sincronización bidireccional con GitHub:

- **Importa un repositorio**: En el modo Build, selecciona **Importar desde GitHub**
  en el menú **Agregar archivos** (ícono +) en el cuadro de entrada de la instrucción para importar
  código existente.
- **Vincula un repositorio**: En Configuración, abre la pestaña **GitHub** para crear un
  repositorio de GitHub nuevo desde tu app o vincularlo a uno existente.
- **Sincronización bidireccional**: Envía los cambios solicitados en AI Studio directamente a tu
  repositorio con mensajes de confirmación generados por IA o extrae los cambios realizados de forma
  externa (como ediciones locales del IDE o solicitudes de extracción de compañeros de equipo) a AI
  Studio.
- **Resuelve conflictos de combinación**: Si los cambios entran en conflicto cuando se sincronizan con
  GitHub, AI Studio proporciona un diálogo **Resolver conflictos** con un
  visor de diferencias en paralelo, lo que te permite revisar las diferencias y elegir
  si deseas conservar la versión de AI Studio o GitHub para cada archivo en conflicto.

### ¿Puedo otorgar acceso de edición a otros usuarios a mi app?

AI Studio no admite la edición colaborativa directa en tiempo real.
Sin embargo, puedes colaborar con compañeros de equipo vinculando tu app a un repositorio de GitHub compartido. Los compañeros de equipo pueden enviar cambios o abrir solicitudes de extracción en GitHub, y tú puedes extraer esas actualizaciones a AI Studio.

### ¿Por qué se marcó mi app por incumplimiento de política?

Tenemos sistemas que revisan automáticamente las apps para garantizar que cumplan con nuestras políticas. Si determinamos que una app incumple nuestras políticas, se quitará de AI Studio. Los incumplimientos de política pueden incluir, entre otros, los siguientes:

- Apps que contienen software malicioso, phishing o suplantación de identidad
- Apps que muestran o distribuyen contenido que incumple la política de imágenes de abuso sexual infantil
- Apps que muestran o distribuyen contenido que incumple la política de acoso
- Apps que muestran o distribuyen contenido que incumple la política sobre la incitación al odio o a la violencia
- Apps que muestran o distribuyen contenido que incumple la política de trata de personas
- Apps que muestran o distribuyen contenido que incumple la política de contenido sexual explícito
- Apps que muestran o distribuyen contenido que incumple la política de Contenido violento o sangriento
- Apps que muestran o distribuyen contenido que incumple la política de contenido peligroso o dañino

Si se marcó tu app por incumplimiento de política y crees que se trata de un error, puedes enviar una apelación. Los incumplimientos reiterados de nuestras políticas pueden ocasionar la rescisión de tu acceso a AI Studio.

### ¿Cuáles son mis responsabilidades como desarrollador de apps?

Como recordatorio, como propietario de tu aplicación, eres responsable de su comportamiento y de todos los datos que maneja. Esto incluye lo siguiente:

- **Cumplimiento legal y derechos de terceros:** Asegurarte de que tu app cumpla con todas las leyes y reglamentaciones aplicables y no infrinja los derechos de otras personas, incluidos los derechos de propiedad intelectual y derechos de privacidad.
- **Supervisión de contenido:** Es posible que se aplique el cumplimiento de condiciones adicionales a
  otros servicios que usa tu app. Por ejemplo,
  [las Condiciones del Servicio de Google Cloud](https://cloud.google.com/terms?hl=es-419),
  aplicables a Firestore, requieren que los clientes que alojan contenido de terceros
  publiquen políticas que definan qué contenido está prohibido (p.ej., contenido
  ilegal) y supervisen la presencia de ese contenido ilegal.
- **Implementación segura:** Implementar las medidas de seguridad y las herramientas de moderación necesarias para evitar que se use de forma inadecuada tu aplicación

Ten en cuenta las [restricciones de uso](https://ai.google.dev/gemini-api/terms?hl=es-419#use-restrictions)
en las Condiciones del Servicio.

### ¿Qué condiciones se aplican a las apps de la galería de apps en AI Studio?

Las [Condiciones del Servicio Adicionales de la API de Gemini](https://ai.google.dev/gemini-api/terms?hl=es-419)
se aplican al uso de las apps que aparecen en la galería de apps de AI Studio, a menos que
se indique lo contrario.

## ¿Qué sigue?

- [Desarrollar apps full-stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=es-419) (web)
- [Compilar apps para Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=es-419)
- Ver ejemplos en la [Galería de apps](https://aistudio.google.com/apps?source=showcase&hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-11 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-11 (UTC)"],[],[]]
