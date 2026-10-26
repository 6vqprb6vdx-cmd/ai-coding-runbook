---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=es-419
fetched_at: 2026-10-26T05:42:18.827032+00:00
title: "Crea apps para Android en Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Crea apps para Android en Google AI Studio

Google AI Studio te permite crear apps nativas para Android a partir de una instrucción en lenguaje natural. Describe la app que quieres y el
[agente de Antigravity](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=es-419#antigravity-agent)
generará un proyecto completo de Kotlin y [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=es-419). Desde el navegador, puedes obtener una vista previa de tu app en un Android Emulator basado en el navegador, instalarla
en un dispositivo físico y publicarla para realizar pruebas.

Las apps para Android también admiten la [integración de Firebase](#firebase-integration) para
llamar a modelos de Gemini con Firebase AI Logic y la Verificación de aplicaciones, almacenar datos en
Cloud Firestore y permitir que los usuarios accedan con Firebase Authentication.

## Comenzar

Para comenzar a compilar una app para Android, haz lo siguiente:

1. Ve al [modo de compilación](https://aistudio.google.com/apps?hl=es-419) en Google AI Studio con el panel de navegación de la izquierda.
2. Selecciona **Android** en el selector de plataformas.
3. Ingresa una instrucción que describa la app que quieres compilar (por ejemplo, *"Crea una tabla de seguimiento de tareas diarias con almacenamiento local"* o *"Crea una app de recetas que use IA para sugerir comidas a partir de ingredientes"*).
4. El agente genera el proyecto y lo inicia en el Android Emulator basado en el navegador.

Luego, puedes iterar en tu app con el panel de chat, tal como lo harías en la experiencia
web. El agente administra todos los archivos de tu proyecto de Android y propaga
los cambios en la base de código.

## Integración en Firebase

Google AI Studio se integra en
[Firebase](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=es-419)
para que tu app para Android pueda llamar a los modelos de Gemini de forma segura, conservar datos y
autenticar usuarios sin un backend personalizado del servidor. Cuando le pides al
agente que cree funciones que requieran IA generativa, una base de datos o un acceso, puede
aprovisionar y configurar automáticamente los siguientes servicios en tu
proyecto de Firebase:

- **[Firebase AI Logic](https://firebase.google.com/docs/ai-logic?hl=es-419) y
  [Verificación de aplicaciones de Firebase](https://firebase.google.com/docs/ai-logic/app-check?hl=es-419)**:
  Llama a los modelos de Gemini directamente desde tu app para Android sin incorporar claves de API
  sin procesar en el APK. AI Studio configura automáticamente la Verificación de aplicaciones para verificar que
  las solicitudes provengan de una instancia auténtica de tu app:
  - **Pruebas y uso compartido (compilaciones de depuración)**: Usa un token de depuración de Verificación de aplicaciones
    administrado automáticamente por AI Studio cuando se obtiene una vista previa en el emulador basado en el navegador,
    se instala a través de USB o se comparte con los verificadores.
  - **Publicación en Google Play (compilaciones de lanzamiento)**: Cambia automáticamente
    a reCAPTCHA Enterprise con una clave de sitio preconfigurada cuando se compila una
    versión de actualización para Google Play.
- **Cloud Firestore**: Almacena y sincroniza datos en una base de datos NoSQL en la nube,
  incluidas las reglas de seguridad de Firestore generadas automáticamente
  (`firestore.rules`).
- **Firebase Authentication**: Agrega flujos de "Acceder con Google" para autenticar
  a los usuarios.

Puedes habilitar Firebase desde la tarjeta de configuración que aparece en el chat cuando
solicitas estas funciones o en cualquier momento en **Configuración > Integraciones**. Para
obtener detalles sobre la configuración del proyecto, las cuotas compartidas y el ciclo de vida de la Verificación de aplicaciones, consulta
[Agrega Firebase a tu app de Google AI Studio](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=es-419).

## Android Emulator basado en el navegador

El Android Emulator se ejecuta por completo en la nube y se transmite a tu navegador.
No necesitas instalar el SDK de Android, Android Studio ni un emulador local.

El emulador proporciona lo siguiente:

- **Simulación de dispositivos similar a Pixel**: Presiona, desplázate e interactúa con tu app como lo harías en un dispositivo real.
- **Compatibilidad con rotación**: Alterna entre la orientación vertical y horizontal.
- **Vista previa en vivo**: Cuando el agente realiza cambios en el código, la app se vuelve a compilar y
  el emulador se actualiza automáticamente.

### Limitaciones del emulador

El emulador basado en el navegador no admite todas las funciones de hardware. Las siguientes funciones
no están disponibles en el emulador:

- Cámara y captura de fotos
- NFC y Bluetooth
- GPS (se simula la ubicación)
- Servicios de Google Play (Acceso con Google, Maps y otras funciones de los Servicios de Play funcionan en un dispositivo real, pero no en el emulador)

## Cómo instalar en un dispositivo con ADB

Puedes instalar el APK compilado directamente en un dispositivo Android físico conectado a tu computadora con un cable USB. Esto usa [WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=es-419) para comunicarse con tu dispositivo a través del navegador. No se requiere una instalación local de ADB.

### Requisitos previos

- Un navegador Chrome o Edge que admita WebUSB
- Un dispositivo Android con las [Opciones para desarrolladores y la depuración por USB](https://developer.android.com/studio/debug/dev-options?hl=es-419) habilitadas
- Un cable USB que conecte el dispositivo a la computadora

### Instala la app en tu dispositivo

1. Haz clic en **Install on Device** en el panel de vista previa.
2. Selecciona tu dispositivo Android en el selector de dispositivos USB del navegador.
3. El APK se transferirá y se instalará en tu dispositivo.
4. La app se inicia automáticamente.

## Publica en Play Store

Puedes publicar tu app para Android en el segmento de pruebas internas de [Google Play Console](https://play.google.com/console?hl=es-419), que te permite distribuirla a un máximo de 100 verificadores.

### Requisitos previos

- Una [cuenta de desarrollador de Google Play](https://play.google.com/console/signup?hl=es-419) (requiere una tarifa de registro única de USD 25)
- Un perfil de desarrollador completo en Play Console

### Cómo publicar tu app

1. Abre **Configuración > Publicar** en Google AI Studio.
2. Haz clic en **Publish to Play Store**.
3. Autentica con tu cuenta de desarrollador de Google Play.
4. AI Studio firma el APK, crea la ficha de la app (o sube una versión nueva)
   y la publica en el segmento de pruebas internas.
5. Recibirás un vínculo para compartir con los verificadores.

AI Studio administra la firma de APK automáticamente con un almacén de claves administrado. Puedes
personalizar la ficha de la app (ícono, capturas de pantalla y descripción) más adelante en Play
Console.

## Qué se genera

Cuando compilas una app para Android, el agente genera un proyecto estándar basado en Gradle
con la siguiente estructura:

- **Configuración de compilación**: Archivos `build.gradle.kts` (a nivel de proyecto y de app) con DSL de Kotlin
- **Capa de la IU**: Componentes de [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=es-419) con temas de [Material 3](https://m3.material.io/)
- **Arquitectura**: Arquitectura de actividad única con ViewModels y clases de datos
- **Recursos**: `AndroidManifest.xml`, elementos de diseño, cadenas y otros recursos de Android.
- **Configuración de Firebase** (cuando Firebase está habilitado):
  `google-services.json`, `firebase_applet_config.xml` y `firestore.rules`.

El agente administra automáticamente las dependencias de Gradle y agrega paquetes de los repositorios de Maven
y Google según sea necesario.

Puedes ver y editar el código generado con la pestaña **Código** en el panel de
vista previa. Para continuar con el desarrollo en Android Studio, descarga el proyecto como un
**archivo ZIP**.

## Limitaciones

La compilación de apps para Android en AI Studio tiene las siguientes limitaciones:

### Limitaciones de la plataforma

- **Solo del lado del cliente**: Las apps para Android no incluyen un componente del lado del servidor.
  Las funciones que requieren un entorno de ejecución del servidor (administración de secretos, multijugador,
  APIs de Google Workspace) no están disponibles.
- **Arquitectura de actividad única**: Solo se admiten proyectos de actividad única y módulo único.
- **Solo Jetpack Compose**: Las apps usan Kotlin y Jetpack Compose. No se admiten los diseños de Java y XML.
- **Sin NDK ni código nativo**: No se admite el código C ni C++.
- **No se admiten Wear OS ni Android TV**: Solo se admiten los factores de forma de teléfonos y tablets.

### Exporta limitaciones

- **Solo descarga de ZIP**: Puedes descargar el proyecto como un archivo ZIP. La exportación a GitHub aún no está disponible para los proyectos de Android.

## ¿Qué sigue?

- [Crea apps en Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=es-419)
- [Desarrolla apps de pila completa](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=es-419) (web)
- Consulta ejemplos en la [Galería de apps](https://aistudio.google.com/apps?source=showcase&hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-20 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-20 (UTC)"],[],[]]
