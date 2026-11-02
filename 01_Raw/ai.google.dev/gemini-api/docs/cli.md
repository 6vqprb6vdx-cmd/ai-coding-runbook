---
source_url: https://ai.google.dev/gemini-api/docs/cli?hl=es-419
fetched_at: 2026-11-02T07:20:10.664207+00:00
title: "CLI de la API de Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# CLI de la API de Gemini

La CLI de la API de Gemini (`gemini-api`) es un cliente de línea de comandos sin estado y sin dependencias creado para agentes de IA con acceso a la shell (y que se puede usar desde secuencias de comandos y CI).
Luego, tu agente de programación puede
generar texto y contenido multimedia, analizar archivos y delegar tareas a
[agentes administrados por Gemini](https://ai.google.dev/gemini-api/docs/agents?hl=es-419). Funciona con Antigravity,
Claude Code, Codex, Cursor, OpenClaw, Hermes o cualquier entorno de shell.

Cada función se ejecuta como un comando de shell estándar en la
[API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419). Ejecuta los mismos
comandos desde un subproceso del agente, tu terminal o una canalización de CI:

```
# 1. Install on macOS or Linux
curl -fsSL https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.sh | bash

# 2. Set your API key
export GEMINI_API_KEY="YOUR_API_KEY"

# 3. Generate media, analyze a file, or launch a background managed agent
gemini-api image "Minimalist isometric icon of a cloud database" --out ./assets/db-icon.jpg
gemini-api analyze -i ./docs/quarterly-report.pdf "Summarize the key findings in three bullets."
gemini-api agent run "Compare WebRTC SFU architectures and cite sources" \
  --agent deep-research-preview-04-2026 \
  --background \
  --stream=false
```

## Elige la herramienta de Gemini adecuada

Usa `gemini-api` cuando un agente o una secuencia de comandos necesiten **llamar** a Gemini directamente desde
la shell sin agregar código del SDK a tu proyecto. Usa los SDK y la
[configuración del agente de programación](https://ai.google.dev/gemini-api/docs/coding-agents?hl=es-419) cuando **incorpores**
Gemini en una aplicación:

| Herramienta | Qué hace | Cuándo se utiliza |
| --- | --- | --- |
| **CLI de la API de Gemini** (`gemini-api`) | Llama a los modelos de Gemini y a los agentes administrados desde cualquier shell. | Tu agente de programación, secuencia de comandos de shell o trabajo de CI necesita generar contenido multimedia generativo, analizar archivos o ejecutar un agente de investigación en segundo plano sin dependencias del proyecto. |
| **[SDKs de IA generativa de Google](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419)** | Importa bibliotecas cliente de Gemini en código de Python, TypeScript, JavaScript, Go, Java o C#. | Estás compilando funciones de Gemini en tu aplicación, servicio de backend o sesión de la [API de Live](https://ai.google.dev/gemini-api/docs/live-api?hl=es-419) en tiempo real. |
| **[MCP y habilidades de Gemini en Documentos](https://ai.google.dev/gemini-api/docs/coding-agents?hl=es-419)** | Ofrece a los agentes de programación búsqueda de documentación en tiempo real y reglas de SDK actuales. | Tu agente de programación está escribiendo código de la aplicación que importa un SDK de IA generativa de Google. |

## Cómo funciona

Las llamadas de REST sin procesar y las CLI interactivas suelen causar problemas a los agentes de programación. El contenido multimedia en Base64
llena la ventana de contexto, las instrucciones interactivas bloquean los subprocesos y los datos de entrenamiento
obsoletos causan marcas de alucinación.

Cuatro opciones de diseño mantienen la confiabilidad de `gemini-api` para los agentes:

- **Búsqueda de esquemas sin conexión:** Pasa `--usage` para imprimir el árbol de comandos (en
  [KDL](https://kdl.dev)) o `--schema` para imprimir el esquema JSON de las solicitudes
  `--body`.
- **Archivos en el disco, rutas de acceso en `stdout`:** Los comandos de contenido multimedia y transcripción escriben archivos en el disco y solo imprimen la ruta de acceso de salida, lo que mantiene los datos binarios fuera de contexto.
- **Ejecuciones de prueba y resultado estructurado:** `--dry-run` valida las entradas, oculta
  las credenciales y obtiene una vista previa de la solicitud HTTP sin conexión. Pasa `-o json`, `-o toon`
  o `--jq` para obtener un resultado legible por máquinas. Agrega `--agent-mode` para devolver errores de JSON estructurados en `stderr` y verifica los [códigos de salida](https://ai.google.dev/gemini-api/docs/cli?hl=es-419#exit-codes) para controlar las fallas. Los comandos
  nunca se solicitan, a menos que pases `--interactive`.
- **Sin estado de forma predeterminada:** Los comandos no mantienen ningún estado local oculto. Encadena
  el trabajo de varios pasos de forma explícita con `--previous-interaction-id`, un URI de `files/<id>`
  subido o un ID de interacción en segundo plano.

Con `-o json`, los comandos de contenido multimedia siguen escribiendo el archivo en el disco y mostrando los metadatos
en `stdout`:

```
{
  "kind": "image",
  "mime_type": "image/jpeg",
  "path": "/path/to/project/assets/db-icon.jpg",
  "response_id": "v1_...",
  "size_bytes": 2914159,
  "status": "completed"
}
```

## Comenzar

Instala la CLI, coloca `gemini-api` en tu `PATH`, configura `GEMINI_API_KEY` y agrega
reglas de uso a tu agente de programación.

### 1. Instala el objeto binario

### macOS y Linux

```
curl -fsSL https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.sh | bash
```

Para instalar una versión específica, establece `GEMINI_VERSION` en una etiqueta de versión:

```
curl -fsSL https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.sh | GEMINI_VERSION=<release-tag> bash
```

### Windows (PowerShell)

```
iwr -useb https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.ps1 | iex
```

### Go

```
go install github.com/google-gemini/gemini-api-cli/cmd/gemini-api@latest
```

### Objetos binarios compilados previamente

Descarga archivos con versiones para macOS, Linux y Windows desde
[Versiones de GitHub](https://github.com/google-gemini/gemini-api-cli/releases)
y coloca `gemini-api` en tu `PATH`. Usa archivos compilados previamente para fijar versiones
exactas en imágenes de Docker y CI.

### 2. Configura la autenticación y verifica

Crea una clave de API en [Google AI Studio](https://aistudio.google.com/apikey?hl=es-419) (consulta
[Claves de API](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419)). Establece `GEMINI_API_KEY` en tu shell y
en el entorno de subprocesos de tu agente:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

En una estación de trabajo local, puedes guardar la clave en el llavero de tu SO (llavero de macOS,
servicio de secretos de Linux o Administrador de credenciales de Windows). Pasa `--no-keyring` para almacenar la clave en `~/.config/gemini-api/config.yaml`:

```
# Save to your OS keychain (or run gemini-api configure --interactive)
gemini-api configure --api-key "YOUR_API_KEY"

# Check the active credential source, then preview a request offline
gemini-api whoami
gemini-api generate "Confirm CLI setup in one sentence." --dry-run
```

### 3. Dale instrucciones a tu agente

Agrega este fragmento al `AGENTS.md`, `CLAUDE.md`, `.cursorrules` o
sistema de tu proyecto para que tu agente de programación sepa cómo usar `gemini-api`:

```
## Gemini API CLI (`gemini-api`)

You have access to `gemini-api` through the shell. Use it to generate text or media (images, speech, music, video), analyze documents and recordings, or run and manage Gemini managed agents.

1. Run `gemini-api --help` or `gemini-api --usage` to choose a command, and `gemini-api <command> --schema` before building a `--body` JSON payload.
2. Preview unfamiliar or complex calls offline with `--dry-run -o json`.
3. For a single JSON result or `--jq` filtering on `generate` or `agent run`, pass `--stream=false -o json`.
4. To chain multi-step workflows, capture the output paths that media and transcription commands print to stdout, and the `id` values returned by `generate` or `agent run`.
```

Luego, envía instrucciones a tu agente de programación como de costumbre:

```
Build a landing page for our developer tool. Use Gemini to generate a hero
illustration and a 15-second welcome voiceover, and start a background Deep
Research agent to compare competing CLI onboarding flows. Wire the assets and
findings into the page.
```

## Comandos

Ejecuta `gemini-api --help` para ver una lista de todos los comandos o `gemini-api explore` para explorarlos
de forma interactiva.

| Grupo | Comando | Qué hace |
| --- | --- | --- |
| Crear | `image` | Genera o edita imágenes (`-i`), escribe un archivo JPEG y muestra su ruta de acceso. |
| Crear | `tts` | Sintetiza voz en formato WAV mono de 24 kHz (una o dos bocinas) y muestra la ruta de acceso de salida. |
| Crear | `music` | Genera pistas de música o bucles, escribe el archivo de audio y muestra su ruta de acceso. |
| Crear | `video` | Genera o edita clips MP4 y espera hasta que se complete (`--async` devuelve un ID de inmediato). |
| Crear | `generate` | Genera texto y lo transmite a `stdout` (`--stream=false` devuelve un resultado completo). |
| Comprender | `analyze` | Responde preguntas sobre archivos PDF, imágenes, audio, video, CSV y de texto, o URLs públicas de YouTube. |
| Comprender | `transcribe` | Escribe transcripciones con etiquetas de interlocutor y marcas de tiempo (`md`, `text`, `json` o `srt`) y, luego, imprime las rutas de acceso de salida. |
| Administrar los agentes | `agent` | Ejecuta agentes administrados (`run`, `status`, `cancel`, `delete-interaction`) y administra definiciones de agentes personalizados (`create`, `list`, `get`, `delete`). |
| Administrar los agentes | `environments`, `credentials`, `webhooks`, `triggers` | Configura entornos de zona de pruebas, credenciales almacenadas, entrega de webhooks y ejecuciones programadas para agentes administrados. |
| Configuración y archivos | `configure`, `auth`, `whoami` | Configura las credenciales y los valores predeterminados, y muestra el estado de autenticación activo. |
| Configuración y archivos | `files` | Sube, enumera, inspecciona y borra archivos en la API de Files. |
| Configuración y archivos | `models` | Enumera los modelos disponibles. |

## Workflows

Cada comando se establece de forma predeterminada en un modelo adecuado para su tarea. Pasa `--model` (`-m`) para
elegir un modelo diferente. Ejecuta `gemini-api models` para ver una lista de las opciones disponibles.

### Generación y edición de imágenes

Los agentes que crean IU web o para dispositivos móviles pueden generar marcadores de posición, íconos e imágenes hero
con [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419). Pasa una ruta de acceso generada
con `-i` para editar la imagen:

```
# Generate a 16:9 image at 2K resolution (512, 1K, 2K, or 4K) and capture its path
HERO_PATH=$(gemini-api image "Friendly robot mascot in a sunlit workshop, space on left for headline" \
  --aspect-ratio 16:9 \
  --image-size 2K \
  --out ./public/images/hero.jpg)

# Edit the generated image
gemini-api image "Add a winter scarf and soft snowfall outside the window" \
  -i "$HERO_PATH" \
  --out ./public/images/hero-winter.jpg
```

Pasa `-i` varias veces para combinar imágenes de referencia, como un personaje y una
guía de estilo.

### Síntesis de voz

`gemini-api tts` sintetiza audio WAV de 24 kHz para indicaciones de IU, vistas previas de accesibilidad
y explicaciones narradas. La voz predeterminada es `Kore`; elige otra
con `--voice`. Para un diálogo de dos interlocutores, etiqueta cada turno en la instrucción y asigna
las voces a los interlocutores:

```
gemini-api tts "Build succeeded. All integration tests passed." \
  --voice Aoede \
  --out ./public/audio/build-ok.wav

gemini-api tts "Alice: Welcome to the release walkthrough! Bob: Let's look at what shipped today." \
  --multi-speaker "Alice=Kore,Bob=Puck" \
  --out ./public/audio/release-intro.wav
```

### Música y video

Compón pistas originales con [Lyria](https://ai.google.dev/gemini-api/docs/music-generation?hl=es-419) y
genera clips en MP4 con [Gemini Omni](https://ai.google.dev/gemini-api/docs/video?hl=es-419):

```
gemini-api music "Warm ambient synth and acoustic guitar background loop, 95 BPM" \
  --out ./public/audio/bg-loop.mp3

gemini-api video "A drone shot of a mountain landscape at sunrise." \
  --aspect-ratio 16:9 \
  --resolution 1080p \
  --out ./public/video/mountain-sunrise.mp4
```

De forma predeterminada, el comando `video` espera a que finalice la generación y escribe el archivo MP4 en el disco. Pasa `--async` para devolver un ID de interacción de inmediato y, luego, ejecuta `gemini-api video --resume <id> --out <path>` más tarde. Pasa `-i` para animar una imagen existente.

### Generación de texto

`gemini-api generate` transmite texto a `stdout`:

```
gemini-api generate "Write a one-paragraph welcome message for new users of a note-taking app."
```

Agrega `--stdin` para canalizar el texto a la instrucción. Pasa `--previous-interaction-id` para
continuar una interacción anterior.

### Análisis y transcripción de documentos

`analyze` responde preguntas sobre archivos PDF, hojas de cálculo, capturas de pantalla, archivos de audio y
video, y URLs públicas de YouTube. `transcribe` escribe una transcripción con formato
(`md`, `text`, `json` o `srt`) en el disco:

```
gemini-api analyze -i ./docs/product-brief.pdf "List the open questions and who owns each one." > open-questions.md

gemini-api transcribe -i ./fixtures/customer-call.mp4 --format srt --out ./fixtures/customer-call.srt
```

Pasa `-i` varias veces a `analyze` para comparar archivos, como capturas de pantalla de antes y después.

`gemini-api` envía archivos locales intercalados de hasta 14 MB (20 MB después de la codificación base64).
Para archivos más grandes, sube una vez con `files upload --wait` y vuelve a usar el URI
`files/<id>` que se muestra:

```
FILE_URI=$(gemini-api files upload ./recordings/all-hands.mp4 --wait)

gemini-api analyze -i "$FILE_URI" "List action items with owners and timestamps."
gemini-api transcribe -i "$FILE_URI" --format json --out ./recordings/all-hands.json
```

### Ejecuta y administra agentes

Tu agente de programación puede delegar tareas de investigación de varios pasos o de zona de pruebas a
[agentes administrados por Gemini](https://ai.google.dev/gemini-api/docs/agents?hl=es-419), como el
[agente de Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419). Pasa
`--background --stream=false` para obtener un ID de interacción de inmediato en lugar de
mantener un flujo abierto:

```
# Launch a Deep Research job in the background and capture its interaction ID
RESEARCH_ID=$(gemini-api agent run "Compare open-source vector index benchmarks and cite primary papers." \
  --agent deep-research-preview-04-2026 \
  --background \
  --stream=false \
  --jq '.id')

# Check status or fetch the finished result while continuing other work
gemini-api agent status "$RESEARCH_ID" -o json
```

Ejecuta `gemini-api agent cancel <id>` para detener un trabajo en ejecución. También puedes iniciar
el [agente de Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419) en una zona de pruebas remota
con `agent run` o administrar [agentes personalizados](https://ai.google.dev/gemini-api/docs/custom-agents?hl=es-419) con
`agent create`, `list`, `get` y `delete`. Consulta
[Entornos](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419) para configurar entornos de pruebas de agentes.

## Cuerpos de solicitud personalizados

Para las opciones sin marcas dedicadas, pasa una carga útil de JSON sin procesar de la [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) con `--body` (intercalada o como `@file.json`). Pasa `--body` para establecer esquemas de `response_format`, herramientas de llamada a funciones, `generation_config` o `"store": false`. Primero, ejecuta
`gemini-api <command> --schema` para verificar los campos válidos:

```
# Inspect the JSON Schema for the request body
gemini-api generate --schema > generate-schema.json

# Return schema-constrained JSON and skip storing the interaction
cat logs.txt | gemini-api generate "Extract every error message from these logs." \
  --stdin \
  --body '{
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {"errors": {"type": "array", "items": {"type": "string"}}},
        "required": ["errors"]
      }
    },
    "store": false
  }'
```

`--body` se combina con las marcas de comando. Si ambos establecen la misma clave, el comando falla
con el código de salida `2` para que las entradas en conflicto fallen rápido.

## Códigos de salida

Cada comando devuelve un código de salida con tipo para que las secuencias de comandos y los agentes puedan controlar
las fallas sin analizar el texto del error. Por ejemplo, `3` indica un problema de autenticación y `2` indica una sintaxis de comando no válida:

| Código | Significado |
| --- | --- |
| `0` | El comando se ejecutó correctamente. |
| `1` | Error de entorno de ejecución o de API, como una falla de red, un límite de frecuencia o un trabajo en segundo plano con errores |
| `2` | Error de uso o validación, como una marca desconocida, una entrada faltante o una clave `--body` duplicada. |
| `3` | Falla de autenticación o autorización, como un token o una clave de API faltantes o no válidos. |

Ejecuta `gemini-api --help-global` para enumerar las marcas globales que comparten todos los comandos
(autenticación, salida, red y diagnóstico).

## Limitaciones

- Los comandos de transmisión (`generate` y `agent run`) requieren `--stream=false`
  cuando se combinan con `-o json` o `--jq` para devolver un solo objeto de respuesta
  JSON.
- Las entradas de archivos `-i` intercaladas tienen un límite de 14 MB de datos de archivos sin procesar (carga útil de solicitud de 20 MB,
  incluida la codificación en Base64). Sube archivos grandes con `gemini-api files upload`.
  La API de Files borra los archivos subidos después de 48 horas.
- `gemini-api` admite solicitudes HTTP estándar, transmisión de SSE y sondeo asíncrono,
  no WebSockets bidireccionales. Para la transmisión de voz y video en tiempo real, usa la [API de Live](https://ai.google.dev/gemini-api/docs/live-api?hl=es-419) con los
  [SDK de IA generativa de Google](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419).

## ¿Qué sigue?

- [Configuración del agente de programación](https://ai.google.dev/gemini-api/docs/coding-agents?hl=es-419)
- [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419)
- [Agentes administrados de Gemini](https://ai.google.dev/gemini-api/docs/agents?hl=es-419)
- [gemini-api-cli en GitHub](https://github.com/google-gemini/gemini-api-cli)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-28 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-28 (UTC)"],[],[]]
