---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=es-419
fetched_at: 2026-09-07T05:29:22.991657+00:00
title: "Ganchos \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Ganchos

Los hooks te permiten ejecutar secuencias de comandos personalizadas o solicitudes HTTP externas justo antes o después de que el agente ejecute código o modifique archivos dentro de su zona de pruebas remota. Usa hooks para extender el bucle del agente con protecciones automatizadas y flujos de trabajo en segundo plano, como los siguientes:

- **Aplicar protecciones de seguridad y acceso** antes de que se ejecuten comandos de shell de alto riesgo o lecturas de archivos restringidas
- **Automatizar las transformaciones de canalizaciones de datos** justo después de que un agente cree o modifique archivos
- **Transmitir telemetría de auditoría empresarial** a sistemas de supervisión externos después de la ejecución de la herramienta

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "security-gate": {
        "pre_tool_execution": [
            {
                "matcher": "code_execution",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/gate.py",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

gate_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
"""

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run `rm -rf /tmp/forbidden` using code_execution.",
    tools=[{"type": "code_execution"}],
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/gate.py",
                "content": gate_script,
            },
        ],
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "security-gate": {
        pre_tool_execution: [
            {
                matcher: "code_execution",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/gate.py",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const gateScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`;

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run `rm -rf /tmp/forbidden` using code_execution.",
    tools: [{ type: "code_execution" }],
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                target: ".agents/hooks-scripts/gate.py",
                content: gateScript,
            },
        ],
    },
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": [{"type": "text", "text": "Run `rm -rf /tmp/forbidden` using code_execution."}],
      "tools": [{"type": "code_execution"}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"security-gate\": {\"pre_tool_execution\": [{\"matcher\": \"code_execution\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/gate.py\", \"timeout\": 10}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/gate.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\ncmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\nif \"rm -rf\" in cmd:\n    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\nelse:\n    print(json.dumps({\"decision\": \"allow\"}))\n"
              }
          ]
      }
  }'
```

## Eventos del ciclo de vida compatibles

Los hooks admiten 2 eventos dentro de la zona de pruebas:

| Evento | Cuándo se activa | Qué hace |
| --- | --- | --- |
| `pre_tool_execution` | Justo antes de que se ejecute una herramienta | Puede aprobar (`allow`) o bloquear (`deny`) la herramienta antes de que se ejecute. Cuando se bloquea, el modelo ve el motivo del rechazo y se adapta. |
| `post_tool_execution` | Justo después de que finaliza una herramienta | Ejecuta tareas de seguimiento, como dar formato al código, ejecutar pruebas de unidades o registrar telemetría. No puede bloquear ni deshacer acciones completadas. |

### `pre_tool_execution`

Se activa justo antes de que se ejecute una herramienta. Tu secuencia de comandos lee los detalles de la llamada a la herramienta desde `stdin` y muestra su decisión JSON (`allow` o `deny`) en `stdout`.

**Carga útil de entrada (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "rm -rf /tmp/forbidden",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

**Respuesta de salida (`stdout`):**

Para aprobar la llamada a la herramienta, haz lo siguiente:

```
{
  "decision": "allow"
}
```

Para bloquear la llamada a la herramienta y mostrar comentarios al modelo, haz lo siguiente:

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

Cuando un hook rechaza un comando, se omite la llamada a la herramienta de inmediato. El agente ve un resultado de error que contiene el motivo del rechazo directamente en su turno actual. Luego, el modelo puede corregirse por sí mismo eligiendo un comando alternativo o explicando el bloqueo al usuario.

Si tu secuencia de comandos muestra JSON no reconocido, texto sin formato o cualquier otro elemento que no sea `{"decision": "deny"}`, el entorno de ejecución trata la respuesta como una aprobación (`allow`).

### `post_tool_execution`

Se activa justo después de que se completa una herramienta. Tu secuencia de comandos lee los detalles de la ejecución y cualquier estado de error de `stdin`.

**Carga útil de entrada (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "python3 /workspace/app.py",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

Si un comando de shell imprime errores en el error estándar (`stderr`) o falla una operación del sistema de archivos, se incluye un campo `"error"` que contiene el texto del error en la carga útil. Cuando el comando se ejecuta correctamente sin errores, se omite por completo el campo `"error"`.

**Respuesta de salida (`stdout`):**

```
{}
```

Debido a que los hooks posteriores a la herramienta se ejecutan estrictamente para tareas en segundo plano, como el formato de código o el registro, el entorno de ejecución ignora cualquier valor de decisión que se muestre en `stdout`.

## Detección de configuración

El entorno de ejecución descubre automáticamente las definiciones de hook de `.agents/hooks.json` o `/.agents/hooks.json` dentro del entorno de zona de pruebas. Puedes proporcionar `hooks.json` junto con tus secuencias de comandos personalizadas usando cualquier [fuente de entorno](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419#mount_from_a_source):

- **Montaje de repositorio**: Un repositorio de Git que contiene `.agents/hooks.json` junto con `AGENTS.md`.
- **Cloud Storage (`gcs`)**: Un bucket de GCS que contiene `hooks.json` copiado en el entorno.
- **Fuentes intercaladas**: Cadena JSON sin procesar y contenido de la secuencia de comandos que se pasan en `environment.sources` cuando se llama a `client.interactions.create`.

### Esquema de `hooks.json`

Un archivo `hooks.json` agrupa las definiciones de eventos (`pre_tool_execution` o `post_tool_execution`) con nombres personalizados. Puedes habilitar o inhabilitar cada grupo de forma independiente:

```
{
  "security-gate": {
    "enabled": true,
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  },
  "auto-format": {
    "post_tool_execution": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/auto_lint.py",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

### Sintaxis y reglas del comparador

Cada grupo de reglas en `hooks.json` define cuándo y cómo se activan los controladores con las propiedades `matcher` y `hooks`:

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `enabled` | `boolean` | Es opcional. Configúralo en `false` para inhabilitar el grupo (`true` de forma predeterminada). |
| `matcher` | `string` | Patrón de expresión regular que coincide con los nombres de las herramientas de destino dentro del contenedor. |
| `hooks` | `array` | Lista ordenada de definiciones de controladores (`command` o `http`). Los controladores se ejecutan de forma secuencial en orden de declaración. |

#### Cómo funciona la evaluación de regex

Cuando el agente invoca una herramienta dentro de la zona de pruebas, el entorno de ejecución evalúa el nombre del contenedor de la herramienta con tu patrón `matcher` usando expresiones regulares RE2 estándar. Si la regex coincide con el nombre de la herramienta, todos los controladores del array `hooks` se ejecutan en orden. Si varios grupos de reglas coinciden con la misma herramienta, se ejecutan todos los arrays de controladores correspondientes.

Puedes segmentar cualquier nombre de herramienta de contenedor integrada: ejecución de código (`code_execution`) o operaciones del sistema de archivos (`read_file`, `write_file`, `list_files` y `delete_file`).

#### Expresiones de comparador comunes

- `"code_execution"`: Coincidencia exacta de cadenas para comandos de shell y ejecuciones de secuencias de comandos
- `"write_file"`: Coincidencia exacta para la creación de archivos del sistema de archivos y las escrituras de disco
- `"read_file|write_file"`: La separación de canalizaciones coincide con varios nombres de herramientas específicos en una sola regla.
- `".*_file"`: Comodín de regex que coincide con cualquier herramienta que termine en `_file` (como `read_file`, `write_file` o `delete_file`). Las expresiones regulares RE2 estándar requieren `.*`; los globs de shell simples como `*_file` no son una sintaxis de regex válida y no coincidirán.
- `".*"` o `"*"` o `""`: Patrón de captura que intercepta cada llamada a la herramienta dentro del contenedor

## Tipos de controladores

### Hooks de comandos

Los hooks de comandos ejecutan un comando o una secuencia de comandos de shell dentro de la zona de pruebas. La secuencia de comandos recibe el JSON del evento en `stdin` y muestra su decisión JSON en `stdout`.

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `type` | `string` | Debe ser `"command"`. |
| `command` | `string` | Línea de comandos para ejecutar dentro de la zona de pruebas (por ejemplo, `python3 /.agents/hooks-scripts/gate.py`). |
| `timeout` | `integer` | Tiempo de espera en segundos. Valor predeterminado: `30`. |

### Hooks HTTP

Los hooks HTTP envían el JSON del evento como una solicitud POST a una URL HTTPS externa directamente desde la red de la zona de pruebas. El servidor de destino muestra su decisión en el cuerpo de la respuesta HTTP con el mismo formato JSON (`{"decision": "allow"}` o `{"decision": "deny", "reason": "..."}`).

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `type` | `string` | Debe ser `"http"`. |
| `url` | `string` | Es el extremo HTTPS externo al que se enviará la carga útil del evento. |
| `headers` | `object` | Son pares clave-valor opcionales para encabezados personalizados no sensibles (como `{"X-Event-Source": "agent-sandbox"}`). Para las credenciales de autenticación, usa el proxy de red. |
| `timeout` | `integer` | Tiempo de espera en segundos. Valor predeterminado: `30`. |

#### Proxy de salida y transformación de tokens

Debido a que los hooks HTTP se ejecutan directamente desde el espacio de nombres de la red de la zona de pruebas, las solicitudes salientes pasan por el proxy de salida transparente. Esta arquitectura te brinda 2 ventajas de seguridad fundamentales:

- **Lista de entidades permitidas de la red:** Los extremos de destino deben permitirse de forma explícita en `network.allowlist` de tu entorno. El proxy bloquea el tráfico de bucle invertido (`127.0.0.1` o `localhost`); siempre segmenta los extremos externos permitidos.
- **Transformación de tokens:** No es necesario almacenar claves de API ni tokens de portador secretos dentro de `.agents/hooks.json` ni montarlos en el contenedor. En cambio, configura reglas de transformación de tokens en la [configuración de red](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419#network-configuration) (`network.allowlist.transform`). El proxy de salida intercepta automáticamente el tráfico de hook HTTP saliente y, luego, inserta tus encabezados de autenticación reales en la conexión antes de salir de la zona de pruebas.

## Cómo el entorno de ejecución controla las decisiones y las fallas

- **Espera síncrona:** El agente se detiene y espera a que terminen tus hooks antes de continuar.
- **Bloqueo de la ejecución de la herramienta:** Si tu hook anterior a la herramienta muestra `{"decision": "deny", "reason": "<your reason>"}`, el entorno de ejecución cancela de inmediato la llamada a la herramienta. El modelo ve el motivo del rechazo en su historial de conversaciones y se adapta eligiendo una alternativa segura o explicando el bloqueo al usuario.
- **Control de fallas de secuencias de comandos, errores HTTP y tiempos de espera:** Si falla una secuencia de comandos (estado de salida distinto de cero), un hook HTTP muestra un código de estado que no es 2xx (como un error del servidor 4xx o 5xx), o bien se agota el tiempo de espera de una operación o muestra JSON no reconocido, el entorno de ejecución lo trata como una aprobación (`allow`). La ejecución de la herramienta continúa con normalidad, por lo que una secuencia de comandos dañada o un servidor de telemetría inalcanzable nunca bloquean tu aplicación.

## Casos de uso habituales

### Recuperación de varios turnos para la privacidad y el cumplimiento de datos

Cuando un hook bloquea el acceso a recursos restringidos, como directorios que contienen información de identificación personal (PII) o registros financieros confidenciales, puedes pasar `previous_interaction_id` en la siguiente llamada para continuar el turno en el mismo entorno. El agente lee la explicación del rechazo y se recupera automáticamente consultando tablas públicas aprobadas.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "privacy-gate": {
        "pre_tool_execution": [
            {
                "matcher": "read_file",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/check_privacy.py",
                        "timeout": 5,
                    }
                ],
            }
        ]
    }
}

check_privacy_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
"""

# Step 1: Agent attempts to read confidential PII records and is intercepted
int_1 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                "content": check_privacy_script,
            },
            {
                "type": "inline",
                "target": "workspace/private/employees.json",
                "content": '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                "type": "inline",
                "target": "workspace/public/summary.json",
                "content": '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
)
print(int_1.output_text)

# Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
int_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment=int_1.environment_id,
    previous_interaction_id=int_1.id,
)
print(int_2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "privacy-gate": {
        pre_tool_execution: [
            {
                matcher: "read_file",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/check_privacy.py",
                        timeout: 5,
                    },
                ],
            },
        ],
    },
};

const checkPrivacyScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential \`/private/\` records is blocked by PII compliance policy. Query approved \`/public/\` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
`;

const int1 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                "target": ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                content: checkPrivacyScript,
            },
            {
                type: "inline",
                "target": "workspace/private/employees.json",
                content: '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                type: "inline",
                "target": "workspace/public/summary.json",
                content: '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
});
console.log(int1.output_text);

const int2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment: int1.environment_id,
    previous_interaction_id: int1.id,
});
console.log(int2.output_text);
```

### REST

```
# Step 1: Attempt to access restricted PII directory (blocked by hook)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to read /workspace/private/employees.json and summarize the employee details."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"privacy-gate\": {\"pre_tool_execution\": [{\"matcher\": \"read_file\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/check_privacy.py\", \"timeout\": 5}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/check_privacy.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\npath = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\nif \"/private/\" in path:\n    resp = {\"decision\": \"deny\", \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"}\nelse:\n    resp = {\"decision\": \"allow\"}\nprint(json.dumps(resp))\n"
              },
              {
                  "type": "inline",
                  "target": "workspace/private/employees.json",
                  "content": "{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}"
              },
              {
                  "type": "inline",
                  "target": "workspace/public/summary.json",
                  "content": "{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}"
              }
          ]
      }
  }'

# Step 2: Continue in the same environment using $ENV_ID and $INTERACTION_ID from the previous response
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "Content-Type: application/json" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -d '{
#       "agent": "antigravity-preview-05-2026",
#       "input": [{"type": "text", "text": "Understood. Please read the approved /workspace/public/summary.json file instead and provide the summary."}],
#       "environment": "'"$ENV_ID"'",
#       "previous_interaction_id": "'"$INTERACTION_ID"'"
#   }'
```

### Telemetría y registro de auditoría externos

Envía eventos de auditoría en tiempo real desde la zona de pruebas a un servidor de supervisión externo cada vez que se leen o modifican archivos.

- **Haz coincidir varias herramientas:** Debido a que los comparadores usan regex estándar, puedes combinar varias herramientas en una sola regla con canalizaciones (`read_file|write_file`) o comodines (`.*_file`).
- **Mantén los secretos fuera de tu configuración:** Define tokens de autenticación en la [configuración de red](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419#network-configuration) de tu entorno (`network.allowlist.transform`). El proxy de salida inserta automáticamente tus tokens de portador reales en las solicitudes salientes.

### Python

```
import json
from google import genai

client = genai.Client()

# Define hook without secrets; the egress proxy injects headers dynamically
hooks_config = {
    "audit-logging": {
        "post_tool_execution": [
            {
                "matcher": "read_file|write_file",
                "hooks": [
                    {
                        "type": "http",
                        "url": "https://telemetry.example.com/api/v1/agent-events",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "telemetry.example.com",
                    "transform": {
                        "Authorization": "Bearer telemetry_secret_token_123",
                    },
                },
                {"domain": "*"},
            ]
        },
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Define hook without secrets; the egress proxy injects headers dynamically
const hooksConfig = {
    "audit-logging": {
        post_tool_execution: [
            {
                matcher: "read_file|write_file",
                hooks: [
                    {
                        type: "http",
                        url: "https://telemetry.example.com/api/v1/agent-events",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
        ],
        network: {
            allowlist: [
                {
                    domain: "telemetry.example.com",
                    transform: {
                        Authorization: "Bearer telemetry_secret_token_123",
                    },
                },
                { domain: "*" },
            ],
        },
    },
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to create /workspace/audit.log containing event 1, then immediately read it back using your filesystem read tool."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"audit-logging\": {\"post_tool_execution\": [{\"matcher\": \"read_file|write_file\", \"hooks\": [{\"type\": \"http\", \"url\": \"https://telemetry.example.com/api/v1/agent-events\", \"timeout\": 10}]}]}}"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "telemetry.example.com",
                      "transform": {
                          "Authorization": "Bearer telemetry_secret_token_123"
                      }
                  },
                  {"domain": "*"}
              ]
          }
      }
  }'
```

## Limitaciones

- **Alcance de la herramienta de zona de pruebas:** Los hooks interceptan herramientas integradas dentro de la zona de pruebas: ejecución de código (`code_execution`) y operaciones del sistema de archivos (`read_file`, `write_file`, `list_files` y `delete_file`). No se activan para la llamada a funciones personalizadas (`function`) ni para las herramientas externas del Protocolo de contexto del modelo (`mcp_server`) que se controlan fuera del contenedor.
- **Listas de entidades permitidas de la red:** Los hooks HTTP se ejecutan dentro de la red del contenedor. Debes permitir de forma explícita las URLs de destino en `network.allowlist` de tu entorno. El proxy bloquea las direcciones de bucle invertido (`localhost`, `127.0.0.1`).
- **Aprobación automática en caso de errores:** Si falla una secuencia de comandos de hook (estado de salida distinto de cero), se agota el tiempo de espera o falla, el entorno de ejecución registra la falla y permite que continúe la llamada a la herramienta. Esto garantiza que las secuencias de comandos de linter dañadas o los procesos colgantes nunca provoquen interbloqueos en tus aplicaciones.
- **Protección de la configuración de la zona de pruebas:** Debido a que los hooks se ejecutan dentro de la zona de pruebas del contenedor, los agentes con herramientas de escritura del sistema de archivos o permisos de ejecución de código de shell pueden modificar `.agents/hooks.json` o secuencias de comandos locales dentro de espacios de trabajo grabables. Usa hooks de contenedor como guía de políticas automatizada y protecciones operativas. Si se requiere una resistencia estricta a la manipulación contra ejecuciones de modelos no confiables, monta fuentes de configuración desde repositorios de solo lectura.

## ¿Qué sigue?

- [Obtén información para configurar zonas de pruebas y entornos remotos persistentes.](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419)
- Explora las capacidades y las herramientas integradas del [agente de Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419).
- Revisa la [descripción general de la API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) para sesiones de varios turnos y transmisión.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-30 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-30 (UTC)"],[],[]]
