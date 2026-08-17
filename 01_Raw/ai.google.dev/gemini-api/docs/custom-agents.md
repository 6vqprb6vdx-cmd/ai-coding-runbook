---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=es-419
fetched_at: 2026-08-17T02:23:03.067427+00:00
title: "C\u00f3mo crear agentes administrados \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Cómo crear agentes administrados

Los agentes administrados en la API de Gemini te permiten extender el agente de Antigravity con tus propias instrucciones, habilidades y datos. Puedes [personalizar el agente intercalado](#customize-inline) en el momento de la interacción o [guardar la configuración](#save-agent) como un agente administrado que invocas por ID.

## Personaliza el agente de Antigravity

La forma más rápida de compilar un agente personalizado es pasar tu configuración en línea mientras creas una interacción nueva sin necesidad de un paso de registro. Puedes extender el agente de varias maneras clave:

- **[Selección de modelos](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419#model-selection)**: Elige el modelo subyacente de Gemini a través de `agent_config` (el valor predeterminado es **Gemini 3.6 Flash**).
- **Instrucciones del sistema**: Pasa texto en línea a través de `system_instruction` para dar forma al comportamiento.
- **Herramientas**: Anula las herramientas predeterminadas (ejecución de código, búsqueda, contexto de URL), registra servidores MCP remotos o define funciones personalizadas (llamada a funciones).
- **Archivos y habilidades**: Monta archivos como `AGENTS.md` y `SKILL.md` en el entorno.

Aquí tienes un ejemplo de cómo pasar los tres en línea:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the Q1 revenue data and create a slide deck.",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",        
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
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

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the Q1 revenue data and create a slide deck.",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",        
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the Q1 revenue data and create a slide deck.",
    "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report."
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."
            }
        ]
    }
}'
```

Todo se define en el momento de la interacción. No es necesario registrar nada primero. El arnés del agente de Antigravity proporciona el entorno de ejecución (ejecución de código, administración de archivos, acceso web) y tus capas de configuración en la parte superior.

### Herramientas e instrucciones del sistema

Puedes personalizar el comportamiento y las capacidades del agente para una interacción específica con los parámetros `system_instruction` y `tools`.

- **Instrucciones del sistema**: Usa el parámetro `system_instruction` para pasar texto en línea que dé forma al comportamiento del agente. Esto es ideal para los ajustes rápidos que deseas cambiar por llamada. `system_instruction` y `AGENTS.md` son aditivos; ambos se aplican cuando están presentes.
- **Herramientas**: De forma predeterminada, el agente de Antigravity tiene acceso a `code_execution`, `google_search` y `url_context`. Puedes anular esta lista pasando el parámetro `tools` en el momento de la interacción. También puedes registrar [servidores MCP remotos](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419#mcp-servers) o definir [funciones personalizadas (llamada a funciones)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419#function-calling) para conectar el agente a tus propias APIs y bases de datos. Para obtener detalles completos sobre las herramientas disponibles, consulta [Agente Antigravity: Herramientas compatibles](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419#supported-tools).

### Personalización basada en archivos

#### Estructura del directorio del agente

Si bien puedes pasar la configuración en línea, te recomendamos que organices los archivos de tu agente en un directorio estructurado. Esto facilita la administración, el control de versiones y el montaje en el entorno del agente.

Un directorio típico de proyectos de agentes se ve de la siguiente manera:

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

El tiempo de ejecución de Antigravity analiza `.agents/` (y la raíz del entorno) en busca de estos archivos.

#### AGENTS.md

El agente carga automáticamente `.agents/AGENTS.md` (o `/.agents/AGENTS.md`) desde el entorno como instrucciones del sistema en el inicio. Usa `AGENTS.md` para definiciones de personajes de formato largo, instrucciones detalladas y las instrucciones que deseas controlar junto con tu código.

Monta un `AGENTS.md` con una fuente en línea:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the Q1 revenue data and create a report.",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
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

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the Q1 revenue data and create a report.",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Analyze the Q1 revenue data and create a report.",
      "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/AGENTS.md",
                  "content": "Always use matplotlib for charts. Include a summary table in every report."
              }
          ]
      }
  }'
```

#### Habilidades: SKILL.md

Las habilidades son archivos que extienden las capacidades del agente. Colócalos en `.agents/skills/<skill-name>/SKILL.md`, y el arnés los detectará y registrará automáticamente.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

Monta una habilidad con una fuente en línea:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Create a presentation about our Q1 results.",
    system_instruction="You create presentations from data.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html",
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

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Create a presentation about our Q1 results.",
    system_instruction: "You create presentations from data.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Create a presentation about our Q1 results.",
      "system_instruction": "You create presentations from data.",
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/skills/slide-maker/SKILL.md",
                  "content": "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html"
              }
          ]
      }
  }'
```

Las habilidades cargadas desde `.agents/skills/` y `/.agents/skills/` se detectan automáticamente.

## Crea un agente administrado

Una vez que hayas iterado en tu configuración, puedes crearla como un agente administrado con `agents.create`. Esto te permite invocar el agente por ID sin repetir la configuración cada vez.

El `id` que especifiques cuando crees un agente administrado debe ser único para tu proyecto y no debe comenzar con prefijos reservados (p.ej., `google-`, `gemini-`). Consulta [Restricciones de ID de agente](#agent-id-restrictions) para obtener la lista completa de prefijos restringidos.

### Desde fuentes

Especifica `base_agent`, `id`, `agent_config`, `system_instruction` y `base_environment` con fuentes. La plataforma aprovisiona un sandbox nuevo con tus archivos en cada invocación. Consulta [Entornos](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419) para conocer los tipos de fuentes disponibles (Git, GCS, en línea).

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="data-analyst",
    base_agent="antigravity-preview-05-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.6-flash",
    },
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
            {
                "type": "repository",
                "source": "https://github.com/my-org/analysis-templates",
                "target": "/workspace/templates",
            },
        ],
    },
)

print(f"Created agent: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const agent = await client.agents.create({
    id: "data-analyst",
    base_agent: "antigravity-preview-05-2026",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.6-flash",
    },
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
            {
                type: "repository",
                source: "https://github.com/my-org/analysis-templates",
                target: "/workspace/templates",
            },
        ],
    },
});

console.log(`Created agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "data-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "agent_config": {
        "type": "antigravity",
        "model": "gemini-3.6-flash"
    },
    "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report."
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."
            },
            {
                "type": "repository",
                "source": "https://github.com/my-org/analysis-templates",
                "target": "/workspace/templates"
            }
        ]
    }
}'
```

### Desde un entorno existente (bifurcación)

Itera con el agente de Antigravity base hasta que el entorno sea el adecuado (paquetes instalados, archivos en su lugar) y, luego, bifurcarlo en un agente administrado.

### Python

```
from google import genai

client = genai.Client()

# Step 1: set up the environment interactively
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment="remote",
)

# Step 2: fork that environment into a managed agent

agent = client.agents.create(
    id="my-data-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment=interaction.environment_id,
)

print(f"Forked agent successfully: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment: "remote",
}, { timeout: 300000 });

const agent = await client.agents.create({
    id: "my-data-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment: interaction.environment_id,
});

console.log(`Forked agent successfully: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
      "environment": "remote"
  }'
```

### Con reglas de red

Puedes bloquear el acceso saliente o insertar credenciales cuando guardas un agente administrado. Para obtener el esquema completo de la lista de entidades permitidas, los patrones de credenciales y los comodines, consulta [Entornos: Configuración de red](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419#network-configuration).

En el siguiente ejemplo, se crea un agente `issue-resolver` que solo puede acceder a GitHub y PyPI, con credenciales insertadas para GitHub:

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="issue-resolver",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/my-org/backend",
                "target": "/workspace/repo",
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    },
                },
                {"domain": "pypi.org"},
            ]
        },
    },
)

print(f"Created issue-resolver agent successfully: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const agent = await client.agents.create({
    id: "issue-resolver",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/my-org/backend",
                target: "/workspace/repo",
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    },
                },
                { domain: "pypi.org" },
            ]
        }
    },
});

console.log(`Created issue-resolver agent successfully: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "id": "issue-resolver",
      "base_agent": "antigravity-preview-05-2026",
      "system_instruction": "You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
      "base_environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "repository",
                  "source": "https://github.com/my-org/backend",
                  "target": "/workspace/repo"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "api.github.com",
                      "transform": {
                          "Authorization": "Basic YOUR_BASE64_TOKEN"
                      }
                  },
                  {"domain": "pypi.org"}
              ]
          }
      }
  }'
```

## Invoca al agente

Llama a tu agente administrado con su ID creando una interacción nueva. Cada invocación bifurca el entorno base, por lo que cada ejecución comienza de forma limpia.

### Python

```
result = client.interactions.create(
    agent="data-analyst",
    input="Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "data-analyst",
    input: "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
    environment: "remote",
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
      "environment": "remote"
  }'
```

Para obtener información sobre las conversaciones y la transmisión de varios turnos, consulta la [guía de inicio rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=es-419). Los mismos patrones `previous_interaction_id` y `environment` se aplican a los agentes administrados.

Los agentes administrados también admiten la ejecución y la cancelación en segundo plano. Para obtener detalles y ejemplos de código, consulta [Agente Antigravity: Ejecución en segundo plano](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419#background-execution).

## Anula la configuración en la invocación

Puedes anular la configuración de red `system_instruction`, `tools` y `environment` predeterminada del agente cuando creas una interacción. Esto te permite modificar el comportamiento, las capacidades o las credenciales del agente para una ejecución específica sin cambiar la definición del agente almacenada.

### Anula las instrucciones del sistema y las herramientas

### Python

```
result = client.interactions.create(
    agent="data-analyst",
    input="Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
    system_instruction="You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
    tools=[{"type": "code_execution"}], # Override to only use code execution
    environment="remote",
)
print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "data-analyst",
    input: "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
    system_instruction: "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
    tools: [{ type: "code_execution" }], // Override to only use code execution
    environment: "remote",
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
      "system_instruction": "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
      "tools": [{"type": "code_execution"}],
      "environment": "remote"
  }'
```

### Anula la configuración de red (actualiza las credenciales)

Si tu agente administrado tiene credenciales de red integradas en su `base_environment`, puedes anularlas en el momento de la invocación para actualizar los tokens vencidos o rotar las claves de API. Pasa un objeto `environment` con una nueva configuración `network`. Las nuevas reglas de red reemplazan por completo las anteriores para esa interacción. Se conservan las fuentes del entorno base (archivos, repositorios).

### Python

```
# Invoke the agent with a fresh token, overriding the base_environment credentials
result = client.interactions.create(
    agent="issue-resolver",
    input="Fix issue #42 and open a PR.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                    },
                },
                {"domain": "pypi.org"},
            ]
        },
    },
)

print(result.output_text)
```

### JavaScript

```
// Invoke the agent with a fresh token, overriding the base_environment credentials
const result = await client.interactions.create({
    agent: "issue-resolver",
    input: "Fix issue #42 and open a PR.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                    },
                },
                { domain: "pypi.org" },
            ]
        },
    },
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "issue-resolver",
      "input": "Fix issue #42 and open a PR.",
      "environment": {
          "type": "remote",
          "network": {
              "allowlist": [
                  {
                      "domain": "api.github.com",
                      "transform": {
                          "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                      }
                  },
                  {"domain": "pypi.org"}
              ]
          }
      }
  }'
```

## Administra los agentes

Puedes enumerar, obtener y borrar agentes.

### Mostrar lista de agentes

### Python

```
agents = client.agents.list()
for a in agents.agents:
    print(f"{a.id}: {a.description}")
```

### JavaScript

```
const agents = await client.agents.list();
if (agents.agents) {
    for (const a of agents.agents) {
        console.log(`${a.id}: ${a.description}`);
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Obtén un agente

### Python

```
agent = client.agents.get(id="data-analyst")
print(agent)
```

### JavaScript

```
const agent = await client.agents.get("data-analyst");
console.log(agent);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Borra un agente

Si borras la configuración, se quita. Los entornos y las interacciones existentes creados por el agente no se ven afectados.

### Python

```
client.agents.delete(id="data-analyst")
```

### JavaScript

```
await client.agents.delete("data-analyst");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Referencia de la definición del agente

| Campo | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| `id` | string | Sí | Identificador único del agente dentro del proyecto de Google Cloud. Se usa para invocar al agente. No debe usar prefijos reservados. Consulta [Restricciones de ID de agente](#agent-id-restrictions). |
| `description` | string | No | Descripción del agente legible por humanos. |
| `base_agent` | string | Sí | ID del agente base (p.ej., `antigravity-preview-05-2026`). |
| `agent_config` | objeto | No | Configuración del agente base, incluida la selección de modelos (`{"type": "antigravity", "model": "gemini-3.6-flash"}`). Si se omite, el valor predeterminado es `gemini-3.6-flash`. No se puede anular en el momento de la interacción para los agentes con nombre. |
| `system_instruction` | string | No | Indicación del sistema que define el comportamiento y el personaje. |
| `tools` | array | No | Herramientas que el agente puede usar. Si se omite, el valor predeterminado es `code_execution`, `google_search` y `url_context`. Las herramientas compatibles incluyen `code_execution`, `google_search`, `url_context`, `mcp_server` y definiciones `function` personalizadas. |
| `base_environment` | string u objeto | No | `"remote"`, un `environment_id` o un objeto de configuración con `sources` y `network`. Consulta Entornos. |

### Restricciones de ID de agente

Cuando creas un agente administrado, el `id` que especificas debe seguir estas reglas:

- Debe ser único para tu proyecto de Google Cloud.
- **No** debe comenzar con ninguno de los siguientes prefijos reservados (sin distinción entre mayúsculas y minúsculas); de lo contrario, la creación fallará:
  - `antigravity-`
  - `veo-`
  - `omni-`
  - `lyria-`
  - `imagen-`
  - `gemma-`
  - `gemini-`
  - `google-`
  - `youtube-`
  - `android-`
  - `chrome-`
  - `pixel-`
  - `waze-`
  - `fitbit-`
  - `nest-`
  - `kaggle-`

## Flujo de trabajo de iteración

1. **Crea prototipos** con el agente de Antigravity base. Pasa las instrucciones del sistema y las fuentes del entorno en línea. Prueba las instrucciones, las habilidades y la configuración del entorno de forma interactiva.
2. **Estabiliza** el entorno. Instala paquetes, monta fuentes y verifica que todo funcione.
3. **Persiste** como un agente administrado creando un agente nuevo, ya sea desde fuentes o bifurcando el entorno.
4. **Actualiza** la definición del agente. Cambia las instrucciones del sistema, intercambia habilidades o agrega fuentes. La próxima invocación recupera la configuración nueva.

## Limitaciones

- **Estado de vista previa**: Los agentes administrados están en versión preliminar. Las funciones y los esquemas pueden cambiar.
- **Agente base y modelos**: Solo se admite `antigravity-preview-05-2026` como `base_agent`. Las opciones de modelos compatibles en `agent_config` son `gemini-3.5-flash`, `gemini-3.6-flash` (predeterminado) y `gemini-3.5-flash-lite`. Para los agentes con nombre, el modelo no se puede anular en el momento de la interacción.
- **Sin control de versiones**: El control de versiones y la reversión de agentes aún no están disponibles.
- **Sin anidación de subagentes**: La delegación de subagentes aún no es compatible.
- Puedes tener hasta 1,000 agentes administrados.

## ¿Qué sigue?

- [Descripción general de los agentes](https://ai.google.dev/gemini-api/docs/agents?hl=es-419): Obtén información sobre los conceptos básicos de los agentes administrados.
- [Guía de inicio rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=es-419): Comienza a compilar con conversaciones y transmisión de varios turnos.
- [Agente Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419): Explora las capacidades, las herramientas y los precios del agente predeterminado.
- [Entornos de agentes](https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419): Configura sandboxes, fuentes y redes.
- [API de agentes administrados en Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=es-419): Para crear agentes con administración organizacional integrada.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-30 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-30 (UTC)"],[],[]]
