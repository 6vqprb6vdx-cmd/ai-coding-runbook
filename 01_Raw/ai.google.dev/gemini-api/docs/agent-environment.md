---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=es-419
fetched_at: 2026-09-28T06:12:59.817690+00:00
title: "Entornos en agentes administrados \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Entornos en agentes administrados

Los entornos son zonas de pruebas de Linux administradas que les brindan a los agentes un lugar aislado para ejecutar código y conservar archivos. Están desacoplados del contexto de interacción, por lo que puedes reutilizar el mismo entorno en varias interacciones o comenzar de nuevo en cualquier momento.

En el siguiente ejemplo, se muestra cómo crear una interacción con un entorno remoto nuevo y recuperar su ID:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Install pandas and matplotlib, verify the imports, and print the versions.",
    environment="remote",
)

print(f"Environment ID: {interaction.environment_id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Install pandas and matplotlib, verify the imports, and print the versions.",
    environment: "remote",
});

console.log(`Environment ID: ${interaction.environment_id}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Install pandas and matplotlib, verify the imports, and print the versions."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Environment ID: " + interaction.environmentId().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Install pandas and matplotlib, verify the imports, and print the versions."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.EnvironmentID != nil {
        fmt.Printf("Environment ID: %s\n", *res.Interaction.EnvironmentID)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Install pandas and matplotlib, verify the imports, and print the versions.",
    "environment": "remote"
}'
```

## El parámetro `environment`

El parámetro `environment` acepta tres formas:

| Formulario | Ejemplo | Cuándo debe utilizarse |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | Aprovisiona un sandbox nuevo. |
| ID del entorno | `environment="env_abc123"` | Reutiliza un entorno de pruebas existente con todos sus archivos y paquetes. |
| Objeto de configuración | `environment={...}` | Aprovisiona una zona de pruebas nueva con fuentes, reglas de red, variables de entorno o una combinación de estos elementos. |

En los siguientes ejemplos, se muestran las tres formas de usar el parámetro `environment`.

### Python

```
from google import genai

client = genai.Client()

# Fresh sandbox
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Write a hello world script.",
    environment="remote",
)

# Reuse an existing sandbox
interaction_2 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Modify the script to accept a name argument.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction.id,
)

# New sandbox with sources
interaction_3 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="List all files and summarize the project.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife",
            }
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Fresh sandbox
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Write a hello world script.",
    environment: "remote",
});

// Reuse an existing sandbox
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Modify the script to accept a name argument.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction.id,
});

// New sandbox with sources
const interaction3 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "List all files and summarize the project.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/octocat/Spoon-Knife",
                target: "/workspace/spoon-knife",
            },
        ],
    },
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

// Fresh sandbox
CreateAgentInteraction params1 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Write a hello world script."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();
Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();

// Reuse an existing sandbox
CreateAgentInteraction params2 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Modify the script to accept a name argument."))
    .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
    .previousInteractionId(interaction.id().orElse(""))
    .build();
Interaction interaction2 = client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();

// New sandbox with sources
Environment env3 = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/octocat/Spoon-Knife")
            .target("/workspace/spoon-knife")
            .build()
    ))
    .build();

CreateAgentInteraction params3 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("List all files and summarize the project."))
    .environment(CreateAgentInteractionEnvironment.of(env3))
    .build();
Interaction interaction3 = client.interactions.create(CreateInteractionRequestBody.of(params3)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Fresh sandbox
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Write a hello world script."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res1.Interaction

    // Reuse an existing sandbox
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Modify the script to accept a name argument."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
            PreviousInteractionID: interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res2

    // New sandbox with sources
    env3 := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/octocat/Spoon-Knife"),
                Target: genai.Ptr("/workspace/spoon-knife"),
            },
        },
    }

    res3, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("List all files and summarize the project."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env3)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res3

    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
}
```

### REST

```
# Fresh sandbox
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": [{"type": "text", "text": "Write a hello world script."}],
    "environment": "remote"
}'

# Reuse an existing sandbox (replace $ENV_ID and $INTERACTION_ID with values from the previous response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-09-2026\",
    \"input\": [{\"type\": \"text\", \"text\": \"Modify the script to accept a name argument.\"}],
    \"environment\": \"$ENV_ID\",
    \"previous_interaction_id\": \"$INTERACTION_ID\"
}"

# New sandbox with sources
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": [{"type": "text", "text": "List all files and summarize the project."}],
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife"
            }
        ]
    }
}'
```

## Configura un entorno

Una forma de configurar un entorno es decirle al agente qué necesitas instalar.
Maneja la resolución de dependencias y la solución de problemas. Una vez que el entorno esté listo, guarda el `environment_id` y reutilízalo.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    environment="remote",
)

# Reuse the configured environment
interaction_2 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction.id,
)

# Reuse the configured environment
interaction_3 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Using the tools in /workspace/tools, list the files.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction_2.id,
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    environment: "remote",
});

const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction.id,
});

const interaction3 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Using the tools in /workspace/tools, list the files.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction2.id,
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params1 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();
Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();

// Reuse the configured environment
CreateAgentInteraction params2 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies."))
    .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
    .previousInteractionId(interaction.id().orElse(""))
    .build();
Interaction interaction2 = client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();

// Reuse the configured environment
CreateAgentInteraction params3 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Using the tools in /workspace/tools, list the files."))
    .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
    .previousInteractionId(interaction2.id().orElse(""))
    .build();
Interaction interaction3 = client.interactions.create(CreateInteractionRequestBody.of(params3)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res1.Interaction

    // Reuse the configured environment
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
            PreviousInteractionID: interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction2 := res2.Interaction

    // Reuse the configured environment
    res3, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Using the tools in /workspace/tools, list the files."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
            PreviousInteractionID: interaction2.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res3

    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
}
```

### REST

```
# Create interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    "environment": "remote"
}'
```

### Cómo montar desde una fuente

Si sabes exactamente qué archivos necesita el agente, actívalos en una sola llamada en lugar de iterar. El objeto de configuración `environment` acepta un array `sources` con tres tipos:

| Tipo de fuente | Valor `type` | Descripción | Límite |
| --- | --- | --- | --- |
| Repositorio de Git | `repository` | Clona un repositorio desde una URL en el espacio aislado en `target`. | 500 MB |
| Cloud Storage | `gcs` | Copia un archivo o directorio de Cloud Storage en el espacio aislado en `target`. | 2 GB |
| Contenido intercalado | `inline` | Escribe contenido de texto sin formato en un archivo de la zona de pruebas en `target`. | 1 MB por archivo y 2 MB en total |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="List all files under /workspace and describe what you find.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife",
            },
            {
                "type": "gcs",
                "source": "gs://cloud-samples-data/bigquery/us-states/",
                "target": "/workspace/gcs-data",
            },
            {
                "type": "inline",
                "content": "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                "target": "/workspace/notes/readme.md",
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
    agent: "antigravity-preview-09-2026",
    input: "List all files under /workspace and describe what you find.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/octocat/Spoon-Knife",
                target: "/workspace/spoon-knife",
            },
            {
                type: "gcs",
                source: "gs://cloud-samples-data/bigquery/us-states/",
                target: "/workspace/gcs-data",
            },
            {
                type: "inline",
                content: "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                target: "/workspace/notes/readme.md",
            },
        ],
    },
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/octocat/Spoon-Knife")
            .target("/workspace/spoon-knife")
            .build(),
        Source.builder()
            .type(SourceType.GCS)
            .source("gs://cloud-samples-data/bigquery/us-states/")
            .target("/workspace/gcs-data")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .content("# Project Notes\n\n- Analyze state population data\n- Create visualizations\n")
            .target("/workspace/notes/readme.md")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("List all files under /workspace and describe what you find."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/octocat/Spoon-Knife"),
                Target: genai.Ptr("/workspace/spoon-knife"),
            },
            {
                Type:   interactions.SourceTypeGcs.ToPointer(),
                Source: genai.Ptr("gs://cloud-samples-data/bigquery/us-states/"),
                Target: genai.Ptr("/workspace/gcs-data"),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Content: genai.Ptr("# Project Notes\n\n- Analyze state population data\n- Create visualizations\n"),
                Target:  genai.Ptr("/workspace/notes/readme.md"),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("List all files under /workspace and describe what you find."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
# Create interaction with sources
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "List all files under /workspace and describe what you find.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife"
            },
            {
                "type": "gcs",
                "source": "gs://cloud-samples-data/bigquery/us-states/",
                "target": "/workspace/gcs-data"
            },
            {
                "type": "inline",
                "content": "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                "target": "/workspace/notes/readme.md"
            }
        ]
    }
}'
```

Puedes combinar ambos enfoques: primero, declarar las fuentes conocidas y, luego, iterar con interacciones de seguimiento para instalar paquetes o ejecutar secuencias de comandos de configuración. No puedes establecer la raíz (`/`) como destino cuando agregas una fuente personalizada. Siempre debes especificar un subdirectorio.

### Ganchos

También puedes activar un archivo de configuración `.agents/hooks.json` y secuencias de comandos de interceptación personalizadas en el entorno de pruebas para aplicar medidas de seguridad o ejecutar validaciones automatizadas cada vez que se ejecuten herramientas. Para ver definiciones de esquemas y ejemplos de código, consulta [Hooks](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=es-419).

### Fuentes privadas

También puedes descargar desde repositorios privados de GitHub o buckets privados de Cloud Storage autenticando el dominio de origen en la configuración de red.

Una opción es una [credencial](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=es-419) almacenada a la que se hace referencia por ID, de modo que almacenas el secreto una vez y cada entorno que necesita esa fuente puede hacer referencia a él:

```
"network": {
    "allowlist": [
        { "domain": "github.com", "credential": "github-production" },
        { "domain": "*" }
    ]
}
```

También puedes configurar el encabezado intercalado con `transform`, como se muestra en los siguientes ejemplos. El proxy de salida aplica ambas formas de la misma manera, y en ningún caso el secreto llega a la zona de pruebas.

Para los **repositorios Git privados**, usa la autenticación `Basic` con tu [token de acceso personal (PAT) de GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
Codifica el token con `x-oauth-basic` como nombre de usuario:

```
echo -n "x-oauth-basic:ghp_YourPATHere" | base64
```

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run the test for my backend app and fix any issue.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run the test for my backend app and fix any issue.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/your-org/backend",
                target: "/backend-app"
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "github.com",
                    transform: {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    domain: "*"
                }
            ]
        }
    },
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/your-org/backend")
            .target("/backend-app")
            .build()
    ))
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Basic YOUR_BASE64_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder()
                    .domain("*")
                    .build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Run the test for my backend app and fix any issue."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/your-org/backend"),
                Target: genai.Ptr("/backend-app"),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Basic YOUR_BASE64_TOKEN",
                    })),
                },
                {
                    Domain: "*",
                },
            },
        }))),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Run the test for my backend app and fix any issue."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Run the test for my backend app and fix any issue.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
}'
```

Para los **buckets privados de Cloud Storage**, usa un token de portador de OAuth 2.0 estándar:

```
gcloud auth print-access-token
```

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Analyze the discrepancies across the data in workspace",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "gcs",
                "source": "gs://my-private-bucket/data",
                "target": "/workspace",
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "*.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Analyze the discrepancies across the data in workspace",
    environment: {
        type: "remote",
        sources: [
            {
                type: "gcs",
                source: "gs://my-private-bucket/data",
                target: "/workspace",
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    domain: "*"
                }
            ]
        }
    },
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.GCS)
            .source("gs://my-private-bucket/data")
            .target("/workspace")
            .build()
    ))
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("*.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer YOUR_GCS_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder()
                    .domain("*")
                    .build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the discrepancies across the data in workspace"))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:   interactions.SourceTypeGcs.ToPointer(),
                Source: genai.Ptr("gs://my-private-bucket/data"),
                Target: genai.Ptr("/workspace"),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "*.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer YOUR_GCS_TOKEN",
                    })),
                },
                {
                    Domain: "*",
                },
            },
        }))),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Analyze the discrepancies across the data in workspace"),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Analyze the discrepancies across the data in workspace",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "gcs",
                "source": "gs://my-private-bucket/data",
                "target": "/workspace"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
}'
```

## Software ya instalado

El entorno de pruebas se ejecuta en Ubuntu y viene con tiempos de ejecución y paquetes comunes preinstalados. El agente puede instalar paquetes adicionales en el tiempo de ejecución con `pip
install` o `npm install`. Los paquetes instalados durante una interacción persisten cuando vuelves a usar el mismo `environment_id`.

| Categoría | Paquetes preinstalados |
| --- | --- |
| **Herramientas de UNIX** | `curl`, `wget`, `git`, `rsync`, `unzip`, `ripgrep`, `fd-find`, `gawk`, `bc`, `tree`, `which`, `lsof`, `htop`, `jq`, `iproute2`, `procps`, `gcloud CLI` |
| **Python 3.12** | `numpy`, `pandas`, `requests`, `google-genai`, `beautifulsoup4`, `pyyaml`, `ast-grep-cli` |
| **Node.js 22** | `create-next-app`, `create-vite`, `typescript` |

## Variables de entorno

Usa el campo `env` para establecer variables de entorno dentro de la zona de pruebas. Cada entrada asigna un nombre de variable a una cadena literal para la configuración o a una referencia a una [credencial](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=es-419) almacenada para un secreto. El agente los ve de la misma manera que en cualquier shell, por lo que las herramientas y los scripts que leen el entorno del proceso los detectan sin cableado adicional.

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `env` | `object` | Es un mapa del nombre de la variable y su valor. Un valor puede ser un literal `string` o una referencia de credencial con el formato `{"credential": "credential-id"}`. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Build the project and run the test suite.",
    environment={
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "LOG_LEVEL": "debug",
            "API_TOKEN": {"credential": "my-api-token"},
        },
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Build the project and run the test suite.",
    environment: {
        type: "remote",
        env: {
            NODE_ENV: "production",
            LOG_LEVEL: "debug",
            API_TOKEN: { credential: "my-api-token" },
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
    "agent": "antigravity-preview-09-2026",
    "input": [{"type": "text", "text": "Build the project and run the test suite."}],
    "environment": {
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "LOG_LEVEL": "debug",
            "API_TOKEN": {"credential": "my-api-token"}
        }
    }
}'
```

Las variables se aplican a todos los comandos que ejecuta el agente en esa interacción, incluidos los comandos de shell, los pasos de compilación y cualquier proceso que inicie.

Los dos tipos de valores se comportan de manera diferente. Una cadena literal se escribe en el contenedor como texto sin formato. Una referencia de credencial no es: La variable recibe un marcador de posición, y el proxy de salida sustituye el secreto real solo en las solicitudes salientes a los dominios de confianza de esa credencial. Consulta [Usa credenciales como variables de entorno](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=es-419#environment-variables) para saber cómo funciona.

## Configuración de red

De forma predeterminada, los entornos tienen acceso de red saliente sin restricciones. Usa el campo `network` para restringir el tráfico saliente a dominios específicos. Cada regla especifica un `domain`, además de un `credential` opcional para insertar un secreto almacenado y un objeto `transform` opcional para insertar encabezados en las solicitudes coincidentes.
Estos encabezados pueden ser únicos por interacción y puedes actualizarlos para el mismo entorno.

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `domain` | `string` | Es el dominio que se debe hacer coincidir. Usa un nombre de host exacto o `*` para todos los dominios. |
| `credential` | `string` | ID de una [credencial](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=es-419) almacenada. El proxy de salida lo resuelve y, luego, inyecta el encabezado de autorización en el momento de la solicitud. |
| `transform` | `object` | Objeto que contiene pares clave-valor simples que representan encabezados para insertar en las solicitudes coincidentes, p.ej., `{"Authorization": "Bearer ..."}`. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_your_github_token"
                    },
                },
                {"domain": "pypi.org"},
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

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Bearer ghp_your_github_token"
                    },
                },
                { domain: "pypi.org" },
                { domain: "*" },
            ]
        }
    },
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

Environment env = Environment.builder()
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer ghp_your_github_token"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("pypi.org").build(),
                AllowlistEntry.builder().domain("*").build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Fetch the latest issues from the GitHub API for my-org/my-repo."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "api.github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer ghp_your_github_token",
                    })),
                },
                {
                    Domain: "pypi.org",
                },
                {
                    Domain: "*",
                },
            },
        }))),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Fetch the latest issues from the GitHub API for my-org/my-repo."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": [{"type": "text", "text": "Fetch the latest issues from the GitHub API for my-org/my-repo."}],
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_your_github_token"
                    }
                },
                {"domain": "pypi.org"},
                {"domain": "*"}
            ]
        }
    }
}'
```

Cuando se establece una lista de entidades permitidas, solo se permiten las solicitudes a los dominios que se indican de forma explícita. Puedes usar comodines para hacer coincidir subdominios (p.ej., `{"domain":
"*.example.com"}`), pero ten en cuenta que esto no coincide con el dominio raíz `example.com`, que se debe agregar por separado. Para permitir todo el resto del tráfico, como el enrutamiento de dominios no incluidos en la lista sin encabezados insertados, agrega `{"domain": "*"}` como una entrada general.

### Credenciales

Existen dos formas de autenticar el tráfico saliente: una credencial almacenada a la que se hace referencia por ID y un `transform` intercalado en la regla de la lista de entidades permitidas. El proxy de salida se aplica tanto en la conexión como en el cable, por lo que, en ambos casos, el secreto nunca ingresa al sandbox ni aparece en las cargas útiles de interacción.

Una [credencial administrada](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=es-419) es la que debes usar cuando quieras almacenar el secreto una vez y volver a usarlo. Cada entorno, agente y activador de tu proyecto puede hacer referencia al mismo ID, y puedes rotarlo en un solo lugar.

### Python

```
from google import genai

client = genai.Client()

# Store the secret once
client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_your_github_token",
)

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {"domain": "api.github.com", "credential": "github-production"},
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

// Store the secret once
await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_your_github_token",
});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                { domain: "api.github.com", credential: "github-production" },
                { domain: "*" },
            ]
        }
    },
});

console.log(interaction.output_text);
```

### REST

```
# Store the secret once
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "github-production",
    "type": "bearer_token",
    "token": "ghp_your_github_token"
}'

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Fetch the latest issues from the GitHub API for my-org/my-repo.",
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                { "domain": "api.github.com", "credential": "github-production" },
                { "domain": "*" }
            ]
        }
    }
}'
```

Una credencial de `oauth2` también actualiza su token de acceso por sí sola, por lo que una interacción de larga duración no se interrumpe cuando vence el token. Consulta [Credenciales](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=es-419) para obtener la lista completa de los tipos de credenciales y las operaciones de administración.

También puedes establecer encabezados intercalados con `transform`. Esto se ajusta cuando el valor pertenece a una sola llamada, por ejemplo, un token que generas justo antes de crear la interacción. El mismo proxy de salida inyecta los encabezados establecidos de esta manera, y nunca se exponen dentro del sandbox como variables de entorno o archivos.

### Python

```
import subprocess
from google import genai

# Fetch a short-lived access token from your local gcloud CLI
gcloud_token = subprocess.check_output(
    ["gcloud", "auth", "print-access-token"], text=True
).strip()

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": f"Bearer {gcloud_token}"
                    },
                }
            ]
        },
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import { execSync } from "child_process";

const gcloudToken = execSync("gcloud auth print-access-token").toString().trim();

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": `Bearer ${gcloudToken}`
                    },
                }
            ]
        }
    },
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Map;

// Fetch a short-lived access token from your local gcloud CLI
Process process = new ProcessBuilder("gcloud", "auth", "print-access-token").start();
String gcloudToken = new String(process.getInputStream().readAllBytes(), StandardCharsets.UTF_8).trim();

Client client = new Client();

Environment env = Environment.builder()
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("storage.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer " + gcloudToken
                    )))
                    .build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("List the files in gs://my-bucket/reports/ using the GCS JSON API."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os/exec"
    "strings"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()

    // Fetch a short-lived access token from your local gcloud CLI
    out, err := exec.Command("gcloud", "auth", "print-access-token").Output()
    if err != nil {
        log.Fatal(err)
    }
    gcloudToken := strings.TrimSpace(string(out))

    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "storage.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer " + gcloudToken,
                    })),
                },
            },
        }))),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("List the files in gs://my-bucket/reports/ using the GCS JSON API."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer <YOUR_GCLOUD_TOKEN>"
                    }
                }
            ]
        }
    }
}'
```

`credential` y `transform` pueden aparecer en la misma regla. La credencial se aplica primero y `transform` se combina en la parte superior, por lo que un encabezado `transform` explícito gana si ambos establecen la misma clave. Un patrón común es una credencial para el encabezado de autenticación más un `transform` para los encabezados adicionales que espera el servicio junto con él.

### Inhabilita el acceso a la red

Para bloquear todo el acceso a la red de salida, establece `network` en `disabled`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Analyze the local files only.",
    environment={
        "type": "remote",
        "network": "disabled",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Analyze the local files only.",
    environment: {
        type: "remote",
        network: "disabled",
    },
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.NetworkEnum;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

Environment env = Environment.builder()
    .network(Network.of(NetworkEnum.DISABLED))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the local files only."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Network: genai.Ptr(interactions.NewNetwork(interactions.NetworkEnumDisabled)),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Analyze the local files only."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Analyze the local files only.",
    "environment": {
        "type": "remote",
        "network": "disabled"
    }
}'
```

### Actualiza las credenciales

Los tokens intercalados, como los tokens de acceso y las claves de API de corta duración, vencen.
Puedes actualizarlos pasando el `environment_id` existente junto con una nueva configuración de `network` en la próxima interacción. Las nuevas reglas de red reemplazan por completo las anteriores, mientras que se conserva el estado del sistema de archivos del entorno (paquetes instalados, archivos, repositorios).

Si usas una [credencial](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=es-419) almacenada, no necesitas esto. Una credencial de `oauth2` se actualiza por sí sola, y rotar cualquier credencial es un `PATCH` en la credencial que deja intacta cada regla de la lista de anunciantes permitidos que la referencia.

### Python

```
from google import genai

client = genai.Client()

# First interaction: use an initial token
first = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer INITIAL_TOKEN"
                    },
                }
            ]
        },
    },
)

# Later: refresh the token on the same environment
result = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Now download the file reports/q1.csv from the same bucket.",
    environment={
        "type": "remote",
        "environment_id": first.environment_id,
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    },
                }
            ]
        },
    },
)

print(result.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First interaction: use an initial token
const first = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer INITIAL_TOKEN"
                    },
                }
            ]
        }
    },
});

// Later: refresh the token on the same environment
const result = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Now download the file reports/q1.csv from the same bucket.",
    environment: {
        type: "remote",
        environment_id: first.environment_id,
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    },
                }
            ]
        }
    },
});

console.log(result.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

// First interaction: use an initial token
Environment initialEnv = Environment.builder()
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("storage.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer INITIAL_TOKEN"
                    )))
                    .build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction firstParams = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("List the files in gs://my-bucket/reports/ using the GCS JSON API."))
    .environment(CreateAgentInteractionEnvironment.of(initialEnv))
    .build();

Interaction first = client.interactions.create(CreateInteractionRequestBody.of(firstParams)).interaction().get();

// Later: refresh the token on the same environment
Environment refreshedEnv = Environment.builder()
    .environmentId(first.environmentId().orElse(""))
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("storage.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer REFRESHED_TOKEN"
                    )))
                    .build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction secondParams = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Now download the file reports/q1.csv from the same bucket."))
    .environment(CreateAgentInteractionEnvironment.of(refreshedEnv))
    .build();

Interaction result = client.interactions.create(CreateInteractionRequestBody.of(secondParams)).interaction().get();
System.out.println(result.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // First interaction: use an initial token
    initialEnv := interactions.Environment{
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "storage.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer INITIAL_TOKEN",
                    })),
                },
            },
        }))),
    }

    firstRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("List the files in gs://my-bucket/reports/ using the GCS JSON API."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(initialEnv)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    first := firstRes.Interaction

    // Later: refresh the token on the same environment
    refreshedEnv := interactions.Environment{
        EnvironmentID: first.EnvironmentID,
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "storage.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer REFRESHED_TOKEN",
                    })),
                },
            },
        }))),
    }

    secondRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Now download the file reports/q1.csv from the same bucket."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(refreshedEnv)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if secondRes.Interaction.OutputText != nil {
        fmt.Println(*secondRes.Interaction.OutputText)
    }
}
```

### REST

```
# Use the environment_id from a previous interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Now download the file reports/q1.csv from the same bucket.",
    "environment": {
        "type": "remote",
        "environment_id": "<ENVIRONMENT_ID_FROM_PREVIOUS_INTERACTION>",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    }
                }
            ]
        }
    }
}'
```

## Ciclo de vida del entorno

Los entornos siguen este ciclo de vida:

| Estado | Comportamiento |
| --- | --- |
| **Creado** | Se aprovisiona cuando una interacción especifica `environment: "remote"` o un objeto de configuración. |
| **Activo** | Se ejecuta mientras una interacción está en curso. |
| **Inactivo** | Se detuvo automáticamente después de 15 minutos de inactividad. |
| **Sin conexión** | Se retienen durante 7 días desde la última actividad. Se puede reanudar pasando su ID. |
| **Eliminado** | Se quitan del sistema automáticamente después de que vence la retención del TTL de 7 días o cuando se borran de forma manual. |

## API de Environments

Puedes usar la API de Environments para administrar sesiones de zona de pruebas de forma programática.
La enumeración de entornos te permite descubrir IDs de sesión activos y recuperar el estado si se interrumpe una conexión del cliente durante una tarea de larga duración. También puedes inspeccionar los metadatos de la sesión y borrar de forma explícita los entornos cuando finalizan los flujos de trabajo en lugar de esperar a que venza el TTL automático.

### Enumerar entornos

Enumera los entornos activos que pertenecen a tu proyecto. Usa parámetros de paginación para controlar el tamaño del lote de respuestas.

### Python

```
from google import genai

client = genai.Client()

response = client.environments.list(page_size=10)
for env in response.environments:
    print(f"Environment ID: {env.id}, Status: {env.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const response = await client.environments.list({ page_size: 10 });
for (const env of response.environments) {
    console.log(`Environment ID: ${env.id}, Status: ${env.status}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.environments.Environment;
import com.google.genai.gaos.models.environments.ListEnvironmentsResponse;
import java.util.List;

Client client = new Client();

ListEnvironmentsResponse response = client.environments.listEnvironments()
    .pageSize(10)
    .call()
    .listEnvironmentsResponse()
    .get();

for (Environment env : response.environments().orElse(List.of())) {
    System.out.println("Environment ID: " + env.id().orElse("") + ", Status: " + env.status().orElse(null));
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    res, err := sdk.Environments.ListEnvironments(ctx, operations.ListEnvironmentsRequest{
        PageSize: genai.Ptr(10),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.ListEnvironmentsResponse != nil {
        for _, env := range res.ListEnvironmentsResponse.Environments {
            fmt.Printf("Environment ID: %s, Status: %v\n", env.ID, env.Status)
        }
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments?pageSize=10" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

El resultado es similar al siguiente:

```
{
  "environments": [
    {
      "id": "140128b2a13c12c00a5a0d8cf7af9469",
      "status": "active"
    },
    {
      "id": "362b738275a1d74af6f1c62bc050da73",
      "status": "active"
    }
  ],
  "next_page_token": "Cj...5aE="
}
```

### Obtén un entorno

Recupera los metadatos y los detalles de configuración de un entorno específico por su nombre de recurso.

### Python

```
from google import genai

client = genai.Client()

env = client.environments.get(id="YOUR_ENVIRONMENT_ID")
print(f"Environment ID: {env.id}, Status: {env.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const env = await client.environments.get("YOUR_ENVIRONMENT_ID");
console.log(`Environment ID: ${env.id}, Status: ${env.status}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.environments.Environment;

Client client = new Client();

Environment env = client.environments.getEnvironment("YOUR_ENVIRONMENT_ID").environment().get();
System.out.println("Environment ID: " + env.id().orElse("") + ", Status: " + env.status().orElse(null));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    res, err := sdk.Environments.GetEnvironment(ctx, operations.GetEnvironmentRequest{
        ID: "YOUR_ENVIRONMENT_ID",
    })
    if err != nil {
        log.Fatal(err)
    }

    env := res.Environment
    fmt.Printf("Environment ID: %s, Status: %v\n", env.ID, env.Status)
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

El resultado es similar al siguiente:

```
{
  "id": "140128b2a13c12c00a5a0d8cf7af9469",
  "status": "active",
  "sources": [
    {
      "type": "repository",
      "source": "https://github.com/octocat/Spoon-Knife",
      "target": "/workspace/spoon-knife"
    }
  ],
  "network": {
    "allowlist": [
      {
        "domain": "api.github.com"
      },
      {
        "domain": "github.com"
      }
    ]
  }
}
```

### Borra un entorno

Finaliza y borra explícitamente un entorno para limpiar los recursos de la zona de pruebas cuando finalicen tus tareas o canalizaciones.

### Python

```
from google import genai

client = genai.Client()

client.environments.delete(id="YOUR_ENVIRONMENT_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

await client.environments.delete("YOUR_ENVIRONMENT_ID");
```

### Java

```
import com.google.genai.Client;

Client client = new Client();

client.environments.deleteEnvironment("YOUR_ENVIRONMENT_ID");
```

### Go

```
package main

import (
    "context"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    _, err := sdk.Environments.DeleteEnvironment(ctx, operations.DeleteEnvironmentRequest{
        ID: "YOUR_ENVIRONMENT_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Administra archivos en el entorno

El agente crea y modifica archivos dentro de la zona de pruebas durante la ejecución. Puedes explorar el contenido de los directorios, obtener metadatos de archivos, descargar archivos individuales o directorios completos como archivos tar, y subir archivos o extraer archivos directamente en el entorno. El almacenamiento en entornos de zona de pruebas está sujeto a límites de uso razonable.

### Enumera los archivos en un directorio

Enumera el contenido de un directorio en el entorno. De forma predeterminada, se muestra el directorio raíz.

#### Parámetros de consulta

| Parámetro | Tipo | Descripción |
| --- | --- | --- |
| `recursive` | booleano | Cuando es `true`, enumera todos los archivos y directorios de forma recursiva. Valor predeterminado: `false`. |

### Python

```
from google import genai

client = genai.Client()

# List root directory
response = client.environments.files.list(
    environment="YOUR_ENVIRONMENT_ID",
    path="",
)
for file in response.files:
    print(f"{file.name} ({file.type}) - {file.path}")

# List a subdirectory recursively
response = client.environments.files.list(
    environment="YOUR_ENVIRONMENT_ID",
    path="src",
    recursive=True,
)
for file in response.files:
    print(f"{file.name} ({file.type}) - {file.path}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// List root directory
const response = await client.environments.files.list({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "",
});
for (const file of response.files) {
    console.log(`${file.name} (${file.type}) - ${file.path}`);
}

// List a subdirectory recursively
const srcResponse = await client.environments.files.list({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "src",
    recursive: true,
});
for (const file of srcResponse.files) {
    console.log(`${file.name} (${file.type}) - ${file.path}`);
}
```

### REST

```
# List root directory
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# List a subdirectory
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/src" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# List all files recursively
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files?recursive=true" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

La respuesta devuelve un array `files` con metadatos para cada entrada:

```
{
  "files": [
    {
      "name": "config",
      "path": "config",
      "type": "DIRECTORY",
      "created": "2026-08-12T07:44:18Z",
      "modified": "2026-08-12T07:44:18Z"
    },
    {
      "name": "main.py",
      "path": "src/main.py",
      "type": "FILE",
      "size_bytes": "15",
      "mime_type": "text/x-python; charset=utf-8",
      "created": "2026-08-12T07:44:20Z",
      "modified": "2026-08-12T07:44:20Z"
    }
  ]
}
```

#### Campos de entrada de archivos

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `name` | string | Nombre del archivo o directorio |
| `path` | string | Es la ruta de acceso completa relativa a la raíz del entorno. |
| `type` | string | `FILE` o `DIRECTORY` |
| `size_bytes` | string | Tamaño del archivo en bytes (solo archivos). |
| `mime_type` | string | Tipo de MIME (solo para archivos). |
| `created` | string | Es la marca de tiempo de creación en formato ISO 8601. |
| `modified` | string | Es la marca de tiempo de última modificación según ISO 8601. |

### Obtén metadatos de archivos

Obtiene los metadatos de un archivo específico por ruta de acceso.

### Python

```
from google import genai

client = genai.Client()

response = client.environments.files.list(
    environment="YOUR_ENVIRONMENT_ID",
    path="src/main.py",
)
file = response.files[0]
print(f"Name: {file.name}, Size: {file.size_bytes} bytes, Type: {file.mime_type}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const response = await client.environments.files.list({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "src/main.py",
});
const file = response.files[0];
console.log(`Name: ${file.name}, Size: ${file.size_bytes} bytes, Type: ${file.mime_type}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/src/main.py" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

La respuesta devuelve los metadatos del archivo incluidos en un array `files`:

```
{
  "files": [
    {
      "name": "main.py",
      "path": "src/main.py",
      "type": "FILE",
      "size_bytes": "15",
      "mime_type": "text/x-python; charset=utf-8",
      "created": "2026-08-12T07:44:20Z",
      "modified": "2026-08-12T07:44:20Z"
    }
  ]
}
```

Si el archivo no existe, la API devuelve un error `404`:

```
{
  "error": {
    "message": "Path 'nonexistent.txt' not found in environment 'ENV_ID'.",
    "code": "not_found"
  }
}
```

### Cómo descargar un solo archivo

Descarga el contenido de un archivo específico. En los SDKs, usa el método `download()`. En las solicitudes de REST, anexa el parámetro de búsqueda `?alt=media` a la ruta de acceso al archivo. El servidor responde con `200 OK` y transmite el contenido del archivo sin procesar.

### Python

```
from google import genai

client = genai.Client()

content = client.environments.files.download(
    environment="YOUR_ENVIRONMENT_ID",
    path="src/main.py",
)

with open("main.py", "wb") as f:
    f.write(content)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "fs";

const client = new GoogleGenAI({});

const bytes = await client.environments.files.download({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "src/main.py",
});

fs.writeFileSync("main.py", Buffer.from(bytes));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/src/main.py?alt=media" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -o main.py
```

### Descarga un directorio como un archivo tar

Descarga un directorio completo como un archivo tar solicitando la ruta de acceso al directorio con `?alt=media`. Esto devuelve un archivo tar de POSIX (no comprimido con gzip). Usa `recursive=true` para incluir subdirectorios anidados.

### Python

```
import tarfile
from google import genai

client = genai.Client()

# Download a subdirectory archive
archive = client.environments.files.download(
    environment="YOUR_ENVIRONMENT_ID",
    path="src",
)

with open("src.tar", "wb") as f:
    f.write(archive)

with tarfile.open("src.tar") as tar:
    tar.extractall(path="./extracted")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { execSync } from "child_process";
import * as fs from "fs";

const client = new GoogleGenAI({});

// Download a subdirectory archive
const bytes = await client.environments.files.download({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "src",
});

fs.writeFileSync("src.tar", Buffer.from(bytes));
execSync("tar -xf src.tar -C ./extracted");
```

### REST

```
# Download a subdirectory (top-level files only)
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/src?alt=media" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -o src.tar

# Download a subdirectory recursively (includes nested directories)
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/config?alt=media&recursive=true" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -o config.tar

# Download root directory
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files?alt=media" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -o snapshot.tar

# Extract the archive
tar xf snapshot.tar -C ./extracted
```

#### Matriz de comportamiento

En la siguiente matriz de comportamiento, se resume el comportamiento esperado de la respuesta y el archivo en los extremos de archivos y directorios, los métodos HTTP y los parámetros de consulta:

| Solicitud | `alt` | `recursive` | `extract` | `overwrite` | Respuesta |
| --- | --- | --- | --- | --- | --- |
| `GET /files` | (ninguno) | (ninguno) | - | - | Listado en formato JSON del directorio raíz |
| `GET /files/{path}` (archivo) | (ninguno) | - | - | - | Metadatos en formato JSON del archivo |
| `GET /files/{path}` (dir) | (ninguno) | `false` | - | - | Listado en formato JSON de los hijos inmediatos |
| `GET /files/{path}` (dir) | (ninguno) | `true` | - | - | Listado en formato JSON de todos los elementos secundarios |
| `GET /files/{path}?alt=media` (archivo) | `media` | - | - | - | Contenido del archivo sin procesar |
| `GET /files/{path}?alt=media` (dir) | `media` | `false` | - | - | Archivo tar de los archivos inmediatos en el directorio |
| `GET /files/{path}?alt=media` (dir) | `media` | `true` | - | - | Archivo tar de todos los archivos de forma recursiva |
| `GET /files?alt=media` | `media` | `false` | - | - | Archivo tar de solo archivos de nivel raíz |
| `PUT /files/{path}` (archivo) | - | - | `false` | `false` | Escribe el archivo en la ruta de acceso. Devuelve `409 Conflict` si ya existe. |
| `PUT /files/{path}?overwrite=true` | - | - | `false` | `true` | Escribe o reemplaza el archivo en la ruta de acceso. |
| `PUT /files/{path}?extract=true` | - | - | `true` | `false` | Descomprime el archivo en el directorio de destino. Devuelve `409 Conflict` si existe algún archivo de destino. |
| `PUT /files/{path}?extract=true&overwrite=true` | - | - | `true` | `true` | Descomprime el archivo y reemplaza los archivos existentes. |

### Sube archivos al entorno

Sube archivos individuales o archivos de directorios directamente a un entorno de pruebas existente con `PUT` de HTTP. Los directorios principales se crean automáticamente si no existen. El almacenamiento en los entornos está sujeto a límites de uso razonable.

#### Cómo subir un solo archivo

### Python

```
from google import genai

client = genai.Client()

with open("local_file.txt", "rb") as f:
    result = client.environments.files.upload(
        environment="YOUR_ENVIRONMENT_ID",
        path="workspace/data/file.txt",
        file=f,
        mime_type="text/plain",
        overwrite=True,
    )

file = result.files[0]
print(f"Uploaded: {file.name} ({file.size_bytes} bytes)")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "fs";

const client = new GoogleGenAI({});

const content = fs.readFileSync("local_file.txt");
const result = await client.environments.files.upload({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "workspace/data/file.txt",
    file: content,
    mime_type: "text/plain",
    overwrite: true,
});

const file = result.files[0];
console.log(`Uploaded: ${file.name} (${file.size_bytes} bytes)`);
```

### REST

```
curl -X PUT "https://generativelanguage.googleapis.com/upload/v1beta/environments/$ENV_ID/files/workspace/data/file.txt" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: text/plain" \
  --data-binary @local_file.txt
```

La respuesta devuelve metadatos para el archivo subido, incluidos en un array `files` para mantener la coherencia con los extremos de lista y obtención:

```
{
  "files": [
    {
      "name": "file.txt",
      "path": "workspace/data/file.txt",
      "type": "FILE",
      "size_bytes": "1024",
      "mime_type": "text/plain"
    }
  ]
}
```

#### Cómo subir y extraer un archivo de directorio

Para inicializar una base de código o una estructura de directorios completa en una sola solicitud, sube un archivo `.tar` o `.tar.gz` con `extract=true`.

### Python

```
from google import genai

client = genai.Client()

with open("source.tar.gz", "rb") as f:
    result = client.environments.files.upload(
        environment="YOUR_ENVIRONMENT_ID",
        path="workspace/src/",
        file=f,
        extract=True,
    )

for entry in result.files:
    print(f"Extracted: {entry.path}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "fs";

const client = new GoogleGenAI({});

const archive = fs.readFileSync("source.tar.gz");
const result = await client.environments.files.upload({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "workspace/src/",
    file: archive,
    extract: true,
});

for (const entry of result.files) {
    console.log(`Extracted: ${entry.path}`);
}
```

### REST

```
curl -X PUT "https://generativelanguage.googleapis.com/upload/v1beta/environments/$ENV_ID/files/workspace/src/?extract=true" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/x-tar" \
  --data-binary @source.tar.gz
```

La respuesta enumera todos los archivos escritos por el archivo:

```
{
  "files": [
    {
      "name": "app.py",
      "path": "workspace/src/app.py",
      "type": "FILE",
      "size_bytes": "15",
      "mime_type": "text/x-python"
    },
    {
      "name": "requirements.txt",
      "path": "workspace/src/requirements.txt",
      "type": "FILE",
      "size_bytes": "17",
      "mime_type": "text/plain"
    }
  ]
}
```

#### Sube archivos grandes con una sesión reanudable

Para cargas útiles grandes o cuando se suben archivos a través de una conexión poco confiable, usa una sesión reanudable en lugar de enviar todo el cuerpo en una sola solicitud. Una carga reanudable divide la transferencia en fragmentos que se pueden volver a intentar de forma individual, por lo que una falla a mitad del proceso no te obliga a comenzar de nuevo.

Para comenzar, inicia la sesión con `uploadType=resumable`. Envía un cuerpo vacío y usa los encabezados `X-Upload-Content-Type` y `X-Upload-Content-Length` para declarar el tipo de medio y el tamaño total de la carga útil que deseas subir:

```
PUT /upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable HTTP/1.1
Host: generativelanguage.googleapis.com
X-Upload-Content-Type: application/octet-stream
X-Upload-Content-Length: 20971520
Content-Length: 0
x-goog-api-key: $GEMINI_API_KEY
```

La respuesta incluye la URL de la sesión en el encabezado `Location`. Esta URL ya contiene un `upload_id`, por lo que no necesita la clave de API nuevamente:

```
HTTP/1.1 200 OK
Location: https://generativelanguage.googleapis.com/upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable&upload_id=AJjja9bfHjiYlGi60pUazCaTuPY
Content-Length: 0
```

Sube la carga útil a esa URL en fragmentos. Cada fragmento declara su rango de bytes y el tamaño total con un encabezado `Content-Range`:

```
PUT /upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable&upload_id=AJjja9bfHjiYlGi60pUazCaTuPY HTTP/1.1
Host: generativelanguage.googleapis.com
Content-Type: application/octet-stream
Content-Range: bytes 0-10485759/20971520
Content-Length: 10485760

<10 MB binary payload>
```

Todos los fragmentos, excepto el último, devuelven `308 Resume Incomplete`. El encabezado `Range` te indica cuántos bytes confirmó el servidor, que es el punto desde el que reanudas la carga si falla un fragmento:

```
HTTP/1.1 308 Resume Incomplete
Range: bytes=0-10485759
Content-Length: 0
```

Envía los fragmentos restantes de la misma manera:

```
PUT /upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable&upload_id=AJjja9bfHjiYlGi60pUazCaTuPY HTTP/1.1
Host: generativelanguage.googleapis.com
Content-Type: application/octet-stream
Content-Range: bytes 10485760-20971519/20971520
Content-Length: 10485760

<remaining 10 MB binary payload>
```

El fragmento final completa la carga y devuelve los metadatos del archivo en el mismo sobre `files` que una carga de un solo intento:

```
{
  "files": [
    {
      "name": "large_dataset.bin",
      "path": "workspace/data/large_dataset.bin",
      "type": "FILE",
      "size_bytes": "20971520",
      "mime_type": "application/octet-stream"
    }
  ]
}
```

Las sesiones reanudables también funcionan con `extract` y `overwrite`. Establece esos parámetros de consulta en la solicitud inicial, no en los fragmentos individuales.

#### Protección contra reemplazo

El valor predeterminado de `overwrite` es `false`. Si la ruta de destino ya existe, la solicitud devuelve un error `409 Conflict` y no se escribe nada:

```
{
  "error": {
    "message": "Requested entity already exists",
    "code": "aborted"
  }
}
```

Para reemplazar un archivo o directorio existente, establece `overwrite=true` (o agrega `?overwrite=true` en REST). Con `extract=true`, la verificación de conflictos se aplica a todos los archivos del archivo, por lo que la solicitud falla si existe algún archivo de destino.

### Descarga la instantánea completa (obsoleto)

Para migrar el código existente a la API de archivos de entorno, haz lo siguiente:

- **Python**: Reemplaza las solicitudes de descarga de archivos heredados por lo siguiente:

  ```
  archive = client.environments.files.download(
      environment="YOUR_ENVIRONMENT_ID",
      path="workspace",
  )
  with open("snapshot.tar", "wb") as f:
      f.write(archive)
  ```
- **JavaScript**: Reemplaza las solicitudes de descarga de archivos heredados por lo siguiente:

  ```
  const bytes = await client.environments.files.download({
      environment: "YOUR_ENVIRONMENT_ID",
      path: "workspace",
  });
  fs.writeFileSync("snapshot.tar", Buffer.from(bytes));
  ```
- **REST**: Reemplaza `GET /v1beta/files/environment-$ENV_ID:download?alt=media` por lo siguiente:

  ```
  curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files?alt=media" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -o snapshot.tar
  ```

## Precios y recursos

Cada entorno se ejecuta con asignaciones de recursos fijos:

| Recurso | Valor |
| --- | --- |
| **CPU** | 4 núcleos |
| **Memoria** | 16 GB |

El procesamiento del entorno (CPU, memoria, ejecución en zona de pruebas) **no se factura** durante el período de vista previa. Consulta [Precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#pricing-for-agents) para conocer los costos de los tokens de agentes.

## Limitaciones

- **Estado de vista previa:** Los entornos y los agentes administrados están en versión preliminar. Las funciones y los esquemas pueden cambiar.
- **Tamaño de la fuente intercalada:** Las fuentes intercaladas están limitadas a 1 MB por archivo y 2 MB en total en todos los archivos.
- **Tamaño de la fuente**: Los repositorios de Git están limitados a 500 MB y los repositorios de Cloud Storage a 2 GB.
- **Inicio del entorno:** El aprovisionamiento de un entorno nuevo tarda hasta 5 segundos. Los repositorios de origen grandes pueden aumentar este tiempo.
- **Vencimiento del entorno:** Los entornos sin conexión inactivos se conservan durante 7 días antes de vencer con la limpieza automática del TTL. Si se pasa un ID de entorno vencido o no válido, se devuelve un error `404 Not Found`.
- **Compatibilidad con archivos:** Actualmente, el agente solo puede leer archivos de texto y de imágenes. Aún no está disponible la compatibilidad con archivos binarios.
- **No se puede realizar el montaje desde la raíz:** No puedes establecer la raíz (`/`) como destino cuando agregas una fuente personalizada. Siempre debes especificar un subdirectorio.

## ¿Qué sigue?

- [Descripción general de los agentes](https://ai.google.dev/gemini-api/docs/agents?hl=es-419): Obtén información sobre los conceptos básicos de los agentes administrados.
- [Guía de inicio rápido](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=es-419): Comienza a crear con conversaciones de varios turnos y transmisión.
- [Agente antigravedad](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=es-419): Explora las capacidades, las herramientas, la selección de modelos y los precios del agente predeterminado.
- [Cómo crear agentes personalizados](https://ai.google.dev/gemini-api/docs/custom-agents?hl=es-419): Define tus propios agentes con `AGENTS.md` y `SKILL.md`.
- [Hooks](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=es-419): Aplican barreras de seguridad y ejecutan validaciones de efectos secundarios dentro de la zona de pruebas.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-24 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-24 (UTC)"],[],[]]
